"""Paired mixed-lobby evaluation with mirrored policy seats."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
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


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_commit() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT,
            check=True, capture_output=True, text=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return os.environ.get("GITHUB_SHA")


def load_policy(checkpoint_path: Path, obs_dim: int, device) -> TFTPolicy:
    payload = torch.load(checkpoint_path, map_location=device, weights_only=False)
    state = payload.get("policy", payload)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    policy.load_compatible_state_dict(state)
    policy.eval()
    return policy


def masks_sha256(raw_masks) -> str:
    payload = [
        {
            key: np.asarray(mask[key], dtype=np.uint8).tolist()
            for key in sorted(mask)
        }
        for mask in raw_masks
    ]
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


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
        # PlayerInfo's cached board scores may be stale. The audit snapshot
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


def run_match(policies_by_player, policy_variants, seed: int, max_steps: int, device):
    """Run one 4-vs-4 lobby. Policy assignment is mirrored in the paired run."""
    if len(policies_by_player) != 8 or len(policy_variants) != 8:
        raise ValueError("A lobby requires exactly eight player policies and variants.")
    env = CppTFTLobbyWrapper(seed=seed)
    try:
        obs = env.reset(seed=seed)
        initial_observation_sha256 = hashlib.sha256(
            np.asarray(obs, dtype=np.float32).tobytes()
        ).hexdigest()
        initial_masks_sha256 = None
        totals = np.zeros(8, dtype=np.float64)
        actions = [Counter() for _ in range(8)]
        final_info = None
        for step in range(max_steps):
            raw_masks = env.get_action_masks()
            if step == 0:
                initial_masks_sha256 = masks_sha256(raw_masks)
            action_array = np.zeros((8, len(ACTION_DIMS)), dtype=np.int64)
            # Batch the four agents controlled by each policy.
            policy_groups = {}
            for player_id, policy in enumerate(policies_by_player):
                policy_groups.setdefault(id(policy), (policy, []))[1].append(player_id)
            for policy, player_ids in policy_groups.values():
                mask_subset = _flatten_masks([raw_masks[i] for i in player_ids], device)
                obs_subset = torch.as_tensor(
                    obs[player_ids], dtype=torch.float32, device=device
                )
                with torch.no_grad():
                    selected, _, _, _ = policy.get_action_and_value(
                        obs_subset, masks=mask_subset, deterministic=True
                    )
                action_array[player_ids] = selected.cpu().numpy().astype(np.int64)
            for player_id, row in enumerate(action_array):
                actions[player_id][ActionType(int(row[0])).name] += 1
            obs, rewards, done, info = env.step(_actions_to_native(action_array))
            totals += np.asarray(rewards, dtype=np.float64)
            if done:
                final_info = env.get_public_state()
                final_audit = env.get_audit_snapshot()
                final_metrics = extract_final_metrics(final_info, final_audit)
                for metric in final_metrics:
                    metric["policy_variant"] = policy_variants[metric["player_id"]]
                return {
                    "seed": seed, "steps": step + 1, "completed": True,
                    "policy_variants": list(policy_variants),
                    "initial_observation_sha256": initial_observation_sha256,
                    "initial_masks_sha256": initial_masks_sha256,
                    "total_rewards": totals.tolist(),
                    "action_counts": [dict(counter) for counter in actions],
                    "final_metrics": final_metrics,
                }
        final_info = env.get_public_state()
        final_audit = env.get_audit_snapshot()
        final_metrics = extract_final_metrics(final_info, final_audit)
        for metric in final_metrics:
            metric["policy_variant"] = policy_variants[metric["player_id"]]
        return {
            "seed": seed, "steps": max_steps, "completed": False,
            "policy_variants": list(policy_variants),
            "initial_observation_sha256": initial_observation_sha256,
            "initial_masks_sha256": initial_masks_sha256,
            "total_rewards": totals.tolist(),
            "action_counts": [dict(counter) for counter in actions],
            "final_metrics": final_metrics,
        }
    finally:
        env.close()


def aggregate_mirrored_runs(run_a, run_b, provenance):
    """Pair each seat's original and tuned result across mirrored 4-vs-4 lobbies."""
    original_metrics, tuned_metrics = {}, {}
    original_rewards, tuned_rewards = {}, {}
    original_actions, tuned_actions = {}, {}
    for run in (run_a, run_b):
        for player_id, variant in enumerate(run["policy_variants"]):
            metric = next(
                (item for item in run.get("final_metrics", [])
                 if int(item["player_id"]) == player_id),
                None,
            )
            if metric is not None:
                if variant == "original":
                    original_metrics[player_id] = {k: v for k, v in metric.items() if k != "policy_variant"}
                else:
                    tuned_metrics[player_id] = {k: v for k, v in metric.items() if k != "policy_variant"}
            if variant == "original":
                original_rewards[player_id] = float(run["total_rewards"][player_id])
                original_actions[player_id] = run["action_counts"][player_id]
            else:
                tuned_rewards[player_id] = float(run["total_rewards"][player_id])
                tuned_actions[player_id] = run["action_counts"][player_id]

    original_ids = sorted(original_rewards)
    tuned_ids = sorted(tuned_rewards)
    paired_reward_deltas = [
        tuned_rewards[player_id] - original_rewards[player_id]
        for player_id in sorted(set(original_rewards) & set(tuned_rewards))
    ]
    mean_reward_delta = (
        sum(paired_reward_deltas) / len(paired_reward_deltas)
        if paired_reward_deltas else 0.0
    )
    same_initial_observation = (
        run_a["initial_observation_sha256"] == run_b["initial_observation_sha256"]
    )
    same_initial_masks = (
        run_a["initial_masks_sha256"] == run_b["initial_masks_sha256"]
    )
    original_metric_list = [original_metrics[i] for i in sorted(original_metrics)]
    tuned_metric_list = [tuned_metrics[i] for i in sorted(tuned_metrics)]
    return {
        "seed": run_a["seed"],
        "both_completed": bool(run_a["completed"] and run_b["completed"]),
        "same_initial_observation": same_initial_observation,
        "same_initial_masks": same_initial_masks,
        "same_initial_state": bool(same_initial_observation and same_initial_masks),
        "mean_reward_delta": round(mean_reward_delta, 6),
        "reward_deltas_per_player_seat": {
            str(player_id): round(tuned_rewards[player_id] - original_rewards[player_id], 6)
            for player_id in sorted(set(original_rewards) & set(tuned_rewards))
        },
        "original": {
            "total_rewards": [original_rewards[i] for i in original_ids],
            "action_counts": [original_actions[i] for i in original_ids],
            "final_metrics": original_metric_list,
            "mean_reward": (
                sum(original_rewards.values()) / len(original_rewards)
                if original_rewards else None
            ),
        },
        "finetuned": {
            "total_rewards": [tuned_rewards[i] for i in tuned_ids],
            "action_counts": [tuned_actions[i] for i in tuned_ids],
            "final_metrics": tuned_metric_list,
            "mean_reward": (
                sum(tuned_rewards.values()) / len(tuned_rewards)
                if tuned_rewards else None
            ),
        },
        "final_player_deltas": compare_final_metrics(
            original_metric_list, tuned_metric_list
        ),
        "mirror_runs": [
            {
                "completed": bool(run["completed"]),
                "steps": int(run["steps"]),
                "initial_observation_sha256": run["initial_observation_sha256"],
                "initial_masks_sha256": run["initial_masks_sha256"],
                "policy_variants": run["policy_variants"],
            }
            for run in (run_a, run_b)
        ],
        "provenance": provenance,
    }


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
    provenance = {
        "repository_commit": repository_commit(),
        "original_checkpoint_sha256": file_sha256(original_path),
        "finetuned_checkpoint_sha256": file_sha256(tuned_path),
        "reward_model_source_sha256": file_sha256(
            ROOT / "cpp" / "include" / "reward" / "RewardModel.hpp"
        ),
        "engine_source_sha256": file_sha256(
            ROOT / "cpp" / "src" / "lobby" / "TftEngine.cpp"
        ),
        "action_mask_source_sha256": file_sha256(
            ROOT / "cpp" / "src" / "decision" / "ActionMaskEngine.cpp"
        ),
        "policy_source_sha256": file_sha256(ROOT / "policy.py"),
        "observation_dim": obs_dim,
        "action_dims": ACTION_DIMS,
        "evaluation_mode": "mixed_4v4_mirrored_seats",
    }

    output = Path(args.output)
    if output.exists():
        raise FileExistsError(
            f"O JSONL de saída já existe e não será sobrescrito: {output}"
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as stream:
        for seed in seeds:
            # First lobby: tuned policy occupies even seats.
            variants_a = ["finetuned" if player_id % 2 == 0 else "original" for player_id in range(8)]
            policies_a = [tuned if variant == "finetuned" else original for variant in variants_a]
            run_a = run_match(policies_a, variants_a, seed, args.max_steps, device)

            # Mirror the assignment to cancel deterministic seat/ordering bias.
            variants_b = ["original" if player_id % 2 == 0 else "finetuned" for player_id in range(8)]
            policies_b = [original if variant == "original" else tuned for variant in variants_b]
            run_b = run_match(policies_b, variants_b, seed, args.max_steps, device)

            row = aggregate_mirrored_runs(run_a, run_b, provenance)
            if not row["same_initial_state"]:
                raise RuntimeError(
                    f"Seed {seed}: observação inicial ou máscaras iniciais divergiram "
                    "entre as lobbies espelhadas; comparação pareada inválida."
                )
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            print(
                f"seed={seed} completed={row['both_completed']} "
                f"mean_reward_delta={row['mean_reward_delta']:+.5f} "
                f"paired_seats={len(row['final_player_deltas'])}"
            )


if __name__ == "__main__":
    main()
