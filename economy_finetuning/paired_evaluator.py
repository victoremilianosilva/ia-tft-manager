"""Paired full-lobby evaluation: original and fine-tuned policies, same seeds."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cpp_lobby_env import CppTFTLobbyWrapper
from engine_contracts import ActionType
from policy import TFTPolicy
from economy_finetuning.finetune import ACTION_DIMS, _actions_to_native, _flatten_masks


def load_policy(checkpoint_path: Path, obs_dim: int, device):
    payload = torch.load(checkpoint_path, map_location=device, weights_only=False)
    state = payload.get("policy", payload)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    policy.load_compatible_state_dict(state)
    policy.eval()
    return policy


def extract_final_metrics(final_state, audit_snapshot=None):
    """Join terminal placement/HP with freshly recomputed audit board metrics."""
    if not isinstance(final_state, dict):
        return []
    finished = bool(final_state.get("finished", False))
    ranking = final_state.get("ranking", [])
    rank_by_id = {
        int(player_id): index + 1
        for index, player_id in enumerate(ranking or [])
    }
    audit_players = {}
    if isinstance(audit_snapshot, dict):
        audit_players = {
            int(item.get("player_id", -1)): item
            for item in (audit_snapshot.get("players", []) or [])
            if isinstance(item, dict)
        }
    metrics = []
    for player in final_state.get("players", []) or []:
        if not isinstance(player, dict):
            continue
        player_id = int(player.get("player_id", -1))
        audit_player = audit_players.get(player_id, {})
        placement = player.get("placement")
        if placement is None and finished:
            placement = rank_by_id.get(player_id)
        metric = {
            "player_id": player_id,
            "placement": int(placement) if placement is not None else None,
            "top4": bool(int(placement) <= 4) if placement is not None else None,
            "hp": float(player["hp"]) if player.get("hp") is not None else None,
            "gold": float(player["gold"]) if player.get("gold") is not None else None,
            "level": float(player["level"]) if player.get("level") is not None else None,
        }
        # PlayerInfo's cached board scores can be stale/zero. The audit snapshot
        # recomputes BoardEvaluation from the actual terminal board.
        for key in (
            "board_power", "board_quality_score", "board_positional_score",
            "board_structural_score", "board_exposed_carries",
            "board_frontline_count", "board_isolated_frontline_count",
            "board_important_bench_units_unplayed",
        ):
            value = audit_player.get(key, player.get(key))
            metric[key] = float(value) if value is not None else None
        metrics.append(metric)
    return metrics


def _metric_delta(original, tuned, key):
    a, b = original.get(key), tuned.get(key)
    if a is None or b is None:
        return None
    return round(float(b) - float(a), 6)


def compare_final_metrics(original_metrics, tuned_metrics):
    original = {int(item["player_id"]): item for item in original_metrics}
    tuned = {int(item["player_id"]): item for item in tuned_metrics}
    result = []
    for player_id in sorted(set(original) & set(tuned)):
        a, b = original[player_id], tuned[player_id]
        row = {"player_id": player_id}
        for key in (
            "placement", "hp", "gold", "level", "board_power",
            "board_quality_score", "board_positional_score", "board_structural_score",
        ):
            row[f"original_{key}"] = a.get(key)
            row[f"finetuned_{key}"] = b.get(key)
            row[f"{key}_delta"] = _metric_delta(a, b, key)
        row["original_top4"] = a.get("top4")
        row["finetuned_top4"] = b.get("top4")
        if a.get("top4") is not None and b.get("top4") is not None:
            row["top4_delta"] = int(bool(b["top4"])) - int(bool(a["top4"]))
        else:
            row["top4_delta"] = None
        result.append(row)
    return result


def run_match(policy, seed: int, max_steps: int, device):
    env = CppTFTLobbyWrapper(seed=seed)
    try:
        obs = env.reset(seed=seed)
        initial_observation_sha256 = hashlib.sha256(
            np.asarray(obs, dtype=np.float32).tobytes()
        ).hexdigest()
        totals = np.zeros(8, dtype=np.float64)
        actions = [Counter() for _ in range(8)]
        final_info = None
        for step in range(max_steps):
            masks = _flatten_masks(env.get_action_masks(), device)
            obs_tensor = torch.as_tensor(obs, dtype=torch.float32, device=device)
            with torch.no_grad():
                selected, _, _, _ = policy.get_action_and_value(
                    obs_tensor, masks=masks, deterministic=True
                )
            action_array = selected.cpu().numpy().astype(np.int64)
            for player_id, row in enumerate(action_array):
                actions[player_id][ActionType(int(row[0])).name] += 1
            obs, rewards, done, info = env.step(_actions_to_native(action_array))
            totals += np.asarray(rewards, dtype=np.float64)
            if done:
                final_info = env.get_public_state()
                final_audit = env.get_audit_snapshot()
                return {
                    "seed": seed, "steps": step + 1, "completed": True,
                    "initial_observation_sha256": initial_observation_sha256,
                    "total_rewards": totals.tolist(),
                    "action_counts": [dict(counter) for counter in actions],
                    "final_state": final_info,
                    "final_metrics": extract_final_metrics(final_info, final_audit),
                }
        final_info = env.get_public_state()
        final_audit = env.get_audit_snapshot()
        return {
            "seed": seed, "steps": max_steps, "completed": False,
            "initial_observation_sha256": initial_observation_sha256,
            "total_rewards": totals.tolist(),
            "action_counts": [dict(counter) for counter in actions],
            "final_state": final_info,
            "final_metrics": extract_final_metrics(final_info, final_audit),
        }
    finally:
        env.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", required=True)
    parser.add_argument("--finetuned", required=True)
    parser.add_argument("--seeds", default="20261105,20261106,20261107,20261108")
    parser.add_argument("--max-steps", type=int, default=2500)
    parser.add_argument("--output", required=True, help="JSONL de saída dentro do diretório da execução")
    args = parser.parse_args()
    original_path = Path(args.original).expanduser().resolve()
    tuned_path = Path(args.finetuned).expanduser().resolve()
    if not original_path.is_file() or not tuned_path.is_file():
        raise FileNotFoundError("Os dois checkpoints precisam existir.")
    seeds = [int(value.strip()) for value in args.seeds.split(",") if value.strip()]
    if not seeds or args.max_steps <= 0:
        parser.error("Informe ao menos uma seed e max-steps positivo.")

    device = torch.device("cpu")
    probe = CppTFTLobbyWrapper(seed=seeds[0])
    try:
        initial = probe.reset(seed=seeds[0])
        obs_dim = int(initial.shape[-1])
    finally:
        probe.close()
    original = load_policy(original_path, obs_dim, device)
    tuned = load_policy(tuned_path, obs_dim, device)

    output = Path(args.output)
    if output.exists():
        raise FileExistsError(
            f"O JSONL de saída já existe e não será sobrescrito: {output}"
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as stream:
        for seed in seeds:
            original_result = run_match(original, seed, args.max_steps, device)
            tuned_result = run_match(tuned, seed, args.max_steps, device)
            same_initial_state = (
                original_result["initial_observation_sha256"]
                == tuned_result["initial_observation_sha256"]
            )
            if not same_initial_state:
                raise RuntimeError(
                    f"Seed {seed}: os modelos não começaram da mesma observação; "
                    "comparação pareada inválida."
                )
            reward_deltas = [
                round(b - a, 6)
                for a, b in zip(original_result["total_rewards"], tuned_result["total_rewards"])
            ]
            final_player_deltas = compare_final_metrics(
                original_result.get("final_metrics", []),
                tuned_result.get("final_metrics", []),
            )
            row = {
                "seed": seed,
                "original": original_result,
                "finetuned": tuned_result,
                "final_player_deltas": final_player_deltas,
                "reward_delta_per_player": reward_deltas,
                "mean_reward_delta": float(np.mean(reward_deltas)),
                "both_completed": original_result["completed"] and tuned_result["completed"],
                "same_initial_state": same_initial_state,
            }
            stream.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
            print(
                f"seed={seed} original_steps={original_result['steps']} "
                f"finetuned_steps={tuned_result['steps']} "
                f"mean_reward_delta={row['mean_reward_delta']:.4f}"
            )
    print(f"Resultados pareados: {output}")


if __name__ == "__main__":
    main()
