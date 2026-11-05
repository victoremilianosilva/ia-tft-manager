"""Standalone PPO economic fine-tuning. Does not modify or instantiate Trainer."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import random
import sys
from pathlib import Path

import numpy as np
import torch
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cpp_lobby_env import CppTFTLobbyWrapper
from engine_contracts import ActionType
from policy import TFTPolicy
from ppo import PPOTrainer
from rollout import RolloutBuffer
from economy_finetuning.scenario_generator import (
    SCENARIOS, decode_observation, matching_scenarios, shaped_action_reward,
)

ACTION_DIMS = [9, 5, 9, 28, 28, 28]
MASK_SHAPES = {
    "type_mask": (9,), "shop_mask": (5,), "bench_source_mask": (9,),
    "board_target_mask": (28,), "board_source_mask": (28,),
    "board_move_target_masks": (28, 28), "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28), "item_inventory_mask": (9,),
    "item_component_first_mask": (10,), "item_component_pair_masks": (10, 10),
    "item_target_mask": (37,),
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_checkpoint(path: Path, obs_dim: int, device: torch.device):
    checkpoint = torch.load(path, map_location=device, weights_only=False)
    state = checkpoint.get("policy", checkpoint)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    migrated = policy.load_compatible_state_dict(state)
    return checkpoint, policy, migrated


def _flatten_masks(raw_masks, device):
    flattened = {}
    if len(raw_masks) != 8:
        raise ValueError(f"Esperadas 8 máscaras; recebidas {len(raw_masks)}")
    for name, shape in MASK_SHAPES.items():
        values = []
        for player_id, player_mask in enumerate(raw_masks):
            array = np.asarray(player_mask[name])
            if array.shape != shape:
                raise ValueError(f"Máscara {name} inválida no jogador {player_id}: {array.shape} != {shape}")
            if not np.isfinite(array).all() or not np.isin(array, [0, 1]).all():
                raise ValueError(f"Máscara {name} contém valores inválidos")
            values.append(array.astype(np.bool_, copy=False))
        flattened[name] = torch.as_tensor(np.asarray(values), dtype=torch.bool, device=device)
    invalid = ~flattened["type_mask"].any(dim=1)
    if invalid.any():
        flattened["type_mask"][invalid] = False
        flattened["type_mask"][invalid, int(ActionType.PASS)] = True
    return flattened


def _actions_to_native(actions: np.ndarray):
    result = []
    for row in actions:
        kind = int(row[0])
        if kind == int(ActionType.EQUIP_FROM_INVENTORY):
            result.append({"type": kind, "item_slot": int(row[1]), "item_target": int(row[2])})
        elif kind == int(ActionType.CRAFT_AND_EQUIP):
            result.append({
                "type": kind, "component_first": int(row[1]),
                "component_second": int(row[2]), "item_target": int(row[3]),
            })
        else:
            result.append({
                "type": kind, "shop_slot": int(row[1]), "bench_slot": int(row[2]),
                "board_target": int(row[3]), "board_source": int(row[4]),
                "board_move_target": int(row[5]),
            })
    return result


def _individual_dones(info, lobby_done: bool):
    players = info.get("players", [])
    dones = np.asarray(
        [not bool(players[i].get("alive", True)) if i < len(players) else False for i in range(8)],
        dtype=np.float32,
    )
    if lobby_done:
        dones[:] = 1.0
    return dones


def _type_probabilities(policy, observations, masks):
    with torch.no_grad():
        features = policy.encode(observations)
        logits = policy.type_head(features)
        logits = policy._mask_logits(logits, masks["type_mask"])
        return torch.softmax(logits, dim=-1).cpu().numpy()


def _freeze_non_target_heads(policy):
    for parameter in policy.parameters():
        parameter.requires_grad = False
    for name, parameter in policy.named_parameters():
        if name.startswith("type_head.") or name.startswith("value_head."):
            parameter.requires_grad = True
    trainable = [name for name, p in policy.named_parameters() if p.requires_grad]
    if not trainable:
        raise RuntimeError("Nenhum parâmetro ficou habilitado para fine-tuning.")
    return trainable


@torch.no_grad()
def _project_type_head_to_reference(policy, reference_policy, max_relative_drift: float):
    """Keep the shared action-type head inside a small L2 trust region."""
    if max_relative_drift <= 0:
        raise ValueError("max_relative_drift deve ser > 0")
    candidate = dict(policy.named_parameters())
    reference = dict(reference_policy.named_parameters())
    names = [name for name in candidate if name.startswith("type_head.")]
    delta_sq = torch.zeros((), device=next(policy.parameters()).device)
    reference_sq = torch.zeros_like(delta_sq)
    for name in names:
        delta_sq += (candidate[name] - reference[name]).pow(2).sum()
        reference_sq += reference[name].pow(2).sum()
    delta_norm = torch.sqrt(delta_sq)
    reference_norm = torch.sqrt(reference_sq).clamp_min(1.0)
    allowed = max_relative_drift * reference_norm
    if delta_norm > allowed:
        scale = allowed / delta_norm.clamp_min(1e-12)
        for name in names:
            candidate[name].copy_(
                reference[name] + scale * (candidate[name] - reference[name])
            )
    return float(delta_norm.item()), float(allowed.item())


def _write_jsonl(path: Path, row: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def run(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    device = torch.device("cpu")
    checkpoint_path = Path(args.checkpoint).expanduser().resolve()
    if not checkpoint_path.is_file():
        raise FileNotFoundError(f"Checkpoint original não encontrado: {checkpoint_path}")

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    run_dir = Path(args.run_dir).expanduser().resolve()
    logs_dir = run_dir / "logs"
    reports_dir = run_dir / "reports"
    logs_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    env = CppTFTLobbyWrapper(seed=args.seed)
    writer = None
    try:
        observations = env.reset(seed=args.seed)
        if observations.ndim != 2 or observations.shape[0] != 8:
            raise ValueError(f"Shape de observação nativo inesperado: {observations.shape}")
        obs_dim = int(observations.shape[-1])
        original_checkpoint, policy, migrated = _load_checkpoint(checkpoint_path, obs_dim, device)
        original_policy = copy.deepcopy(policy).eval()
        trainable_names = _freeze_non_target_heads(policy)
        optimizer = optim.Adam(
            [parameter for parameter in policy.parameters() if parameter.requires_grad],
            lr=args.learning_rate,
            eps=1e-5,
        )
        writer = SummaryWriter(str(run_dir / "tensorboard"))
        ppo = PPOTrainer(
            policy, optimizer, writer, clip_coef=args.clip_coef,
            ent_coef=args.entropy_coef, vf_coef=0.5,
            max_grad_norm=0.25, target_kl=args.target_kl,
        )

        metadata = {
            "checkpoint": str(checkpoint_path),
            "checkpoint_sha256": _sha256(checkpoint_path),
            "checkpoint_migrated": bool(migrated),
            "observation_dim": obs_dim,
            "action_dims": ACTION_DIMS,
            "trainable_parameters": trainable_names,
            "seed": args.seed,
            "learning_rate": args.learning_rate,
            "clip_coef": args.clip_coef,
            "target_kl": args.target_kl,
            "updates": args.updates,
            "rollout_steps": args.rollout_steps,
            "scenario_catalog": [item.to_dict() for item in SCENARIOS],
            "state_initialization": "natural_native_simulation_state_mining",
            "state_injection_available": False,
        }
        (reports_dir / "experiment_config.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("Cenários econômicos monitorados:")
        for scenario in SCENARIOS:
            print(f"- {scenario.scenario_id}: {scenario.title} | {'TREINO' if scenario.trainable else 'MONITOR'}")

        total_matches = {scenario.scenario_id: 0 for scenario in SCENARIOS}
        action_counts = {scenario.scenario_id: {} for scenario in SCENARIOS}
        decision_path = logs_dir / "decision_trace.jsonl"
        scenario_path = logs_dir / "scenario_results.jsonl"
        update_path = logs_dir / "training_metrics.jsonl"
        last_done = np.zeros(8, dtype=np.float32)
        global_step = 0

        for update in range(1, args.updates + 1):
            rollout = RolloutBuffer(
                args.rollout_steps, 8, obs_dim, 6, device, mask_shapes=MASK_SHAPES
            )
            matched_transitions = 0
            episode_reward = np.zeros(8, dtype=np.float64)

            for step in range(args.rollout_steps):
                raw_masks = env.get_action_masks()
                masks = _flatten_masks(raw_masks, device)
                obs_tensor = torch.as_tensor(observations, dtype=torch.float32, device=device)
                with torch.no_grad():
                    actions, logprobs, _, values = policy.get_action_and_value(
                        obs_tensor, masks=masks, deterministic=False
                    )
                    reference_actions, _, _, _ = original_policy.get_action_and_value(
                        obs_tensor, masks=masks, deterministic=True
                    )
                    candidate_greedy_actions, _, _, _ = policy.get_action_and_value(
                        obs_tensor, masks=masks, deterministic=True
                    )
                action_array = actions.cpu().numpy().astype(np.int64)
                reference_array = reference_actions.cpu().numpy().astype(np.int64)
                candidate_greedy_array = candidate_greedy_actions.cpu().numpy().astype(np.int64)
                candidate_type_probs = _type_probabilities(policy, obs_tensor, masks)
                reference_type_probs = _type_probabilities(original_policy, obs_tensor, masks)

                shaped_rewards = []
                valid = []
                for player_id in range(8):
                    state = decode_observation(observations[player_id], player_id=player_id)
                    action_type = int(action_array[player_id, 0])
                    shaping, matched_ids = shaped_action_reward(state, action_type)
                    shaped_rewards.append(shaping)
                    trainable_match = any(
                        item.scenario_id in matched_ids and item.trainable for item in SCENARIOS
                    )
                    valid.append(trainable_match)
                    for scenario_id in matched_ids:
                        total_matches[scenario_id] += 1
                        action_name = ActionType(action_type).name
                        action_counts[scenario_id][action_name] = action_counts[scenario_id].get(action_name, 0) + 1
                    _write_jsonl(decision_path, {
                        "step": global_step, "update": update, "lobby_seed": args.seed,
                        "player_id": player_id, "state": state,
                        "scenario_ids": matched_ids,
                        "original_action": reference_array[player_id].tolist(),
                        "finetuned_action": candidate_greedy_array[player_id].tolist(),
                        "training_action": action_type,
                        "original_type_probabilities": reference_type_probs[player_id].round(7).tolist(),
                        "finetuned_type_probabilities": candidate_type_probs[player_id].round(7).tolist(),
                    })

                next_observations, rewards, lobby_done, info = env.step(_actions_to_native(action_array))
                rewards = np.asarray(rewards, dtype=np.float32) + np.asarray(shaped_rewards, dtype=np.float32)
                episode_reward += rewards
                matched_transitions += int(sum(valid))
                dones = _individual_dones(info, lobby_done)

                rollout.add(
                    obs_tensor, torch.as_tensor(action_array, dtype=torch.long, device=device),
                    logprobs, torch.as_tensor(rewards, dtype=torch.float32, device=device),
                    torch.as_tensor(dones, dtype=torch.float32, device=device), values,
                    masks, valid=torch.as_tensor(valid, dtype=torch.bool, device=device),
                )
                observations = next_observations
                last_done = dones
                global_step += 1

                if lobby_done:
                    _write_jsonl(scenario_path, {
                        "update": update, "step": global_step, "seed": args.seed,
                        "episode_rewards": episode_reward.tolist(),
                        "scenario_matches": total_matches,
                        "terminal_state": info.get("final_state", info.get("players", [])),
                    })
                    observations = env.reset(seed=args.seed + global_step)
                    # Keep terminal dones for GAE bootstrap at the rollout boundary.
                    episode_reward.fill(0.0)

            next_masks = _flatten_masks(env.get_action_masks(), device)
            with torch.no_grad():
                next_value = policy.get_value(
                    torch.as_tensor(observations, dtype=torch.float32, device=device),
                    masks=next_masks,
                )
            rollout.compute_returns_and_advantages(
                next_value, torch.as_tensor(last_done, dtype=torch.float32, device=device),
                gamma=0.99, gae_lambda=0.95,
            )

            if matched_transitions >= args.min_scenario_transitions:
                metrics = ppo.update(rollout, batch_size=args.batch_size, epochs=args.ppo_epochs) or {}
            else:
                metrics = {"optimizer_steps": 0, "early_stop": False, "approx_kl_max": 0.0}
                if matched_transitions:
                    print(
                        f"update={update}: apenas {matched_transitions} transições elegíveis; "
                        f"mínimo={args.min_scenario_transitions}, update ignorado"
                    )
            head_drift, head_drift_limit = _project_type_head_to_reference(
                policy, original_policy, args.max_type_head_drift
            )
            metrics_row = {
                "update": update, "matched_transitions": matched_transitions,
                "mean_reward": float(rollout.rewards[:rollout.ptr].mean().item()),
                "type_head_relative_drift_before_projection": head_drift,
                "type_head_relative_drift_limit": head_drift_limit,
                **{key: value for key, value in metrics.items()
                   if isinstance(value, (int, float, bool))},
            }
            _write_jsonl(update_path, metrics_row)
            writer.add_scalar("fine_tuning/matched_transitions", matched_transitions, update)
            writer.add_scalar("fine_tuning/mean_reward", metrics_row["mean_reward"], update)
            print(
                f"update={update}/{args.updates} matched={matched_transitions} "
                f"optimizer_steps={metrics_row.get('optimizer_steps', 0)}"
            )

        # Always save a distinct fine-tuned artifact; never overwrite the source.
        torch.save({
            "policy": policy.state_dict(),
            # Do not serialize the partial optimizer: the main Trainer has a
            # different full-parameter optimizer and must initialize it fresh.
            "update": 0,
            "fine_tuning": metadata,
            "source_checkpoint_sha256": metadata["checkpoint_sha256"],
        }, output)
        (reports_dir / "scenario_catalog.json").write_text(
            json.dumps([item.to_dict() for item in SCENARIOS], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        summary = {
            "checkpoint_original": str(checkpoint_path),
            "checkpoint_finetuned": str(output),
            "scenario_matches": total_matches,
            "scenario_action_counts": action_counts,
            "matched_transitions_total": int(sum(total_matches.values())),
            "warning": (
                "Scenarios are matched on naturally reached native states. "
                "The current C++ API exposes no arbitrary state injection."
            ),
        }
        (reports_dir / "training_summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Checkpoint fine-tuned salvo em: {output}")
        print(f"Relatórios e logs: {run_dir}")
    finally:
        if writer is not None:
            writer.close()
        env.close()


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True, help="Checkpoint original .pt")
    parser.add_argument("--output", default="economy_finetuning/checkpoints/economy_ft.pt")
    parser.add_argument("--run-dir", default="economy_finetuning/runs/latest")
    parser.add_argument("--updates", type=int, default=100)
    parser.add_argument("--rollout-steps", type=int, default=128)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--ppo-epochs", type=int, default=2)
    parser.add_argument("--learning-rate", type=float, default=1e-5)
    parser.add_argument("--clip-coef", type=float, default=0.1)
    parser.add_argument("--target-kl", type=float, default=0.01)
    parser.add_argument("--entropy-coef", type=float, default=0.002)
    parser.add_argument("--max-type-head-drift", type=float, default=0.02)
    parser.add_argument("--min-scenario-transitions", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20261105)
    args = parser.parse_args()
    if args.updates <= 0 or args.rollout_steps <= 0 or args.batch_size <= 0 or args.ppo_epochs <= 0:
        parser.error("updates, rollout-steps, batch-size e ppo-epochs devem ser positivos")
    if not 0 < args.clip_coef < 1 or args.learning_rate <= 0 or args.target_kl <= 0:
        parser.error("clip-coef, learning-rate ou target-kl inválido")
    if args.max_type_head_drift <= 0 or args.min_scenario_transitions <= 0:
        parser.error("max-type-head-drift e min-scenario-transitions devem ser > 0")
    return args


if __name__ == "__main__":
    run(parse_args())
