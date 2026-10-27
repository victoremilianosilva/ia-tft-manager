"""Paired-seed ablation for composition controls in the PPO observation.

Run after building the native C++ engine:
    python scripts/evaluate_composition_ablation.py --checkpoint tft_checkpoint.pt --matches 20

Each seed is played twice with the same deterministic policy: once with the
composition-control observation slice intact and once with that slice zeroed.
This measures whether the trained weights react to focus/lock/strength and
compares coarse in-match outcomes; it does not itself prove statistical
significance.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean

import numpy as np
import torch

from policy import TFTPolicy


ACTION_DIMS = [9, 5, 9, 28, 28, 28]
MASK_KEYS = (
    "type_mask",
    "shop_mask",
    "bench_source_mask",
    "board_target_mask",
    "board_source_mask",
    "board_move_target_masks",
    "bench_move_source_mask",
    "bench_to_board_target_masks",
)
ACTION_NAMES = ("BUY", "REROLL", "BUY_XP", "MOVE_BENCH", "MOVE_BOARD", "SELL", "PASS", "ITEM", "CRAFT")
CANDIDATE_FEATURE_DIM = 8


def infer_trait_count_from_observation_dim(obs_dim: int, fixed_dim: int = 433, vectors_per_trait: int = 4) -> int:
    """Infer the full trait catalog from the observation contract, not active match traits."""
    remainder = int(obs_dim) - int(fixed_dim)
    if fixed_dim <= 0 or vectors_per_trait <= 0 or remainder <= 0 or remainder % vectors_per_trait:
        raise ValueError(
            f"Observation dimension {obs_dim} is incompatible with layout "
            f"{fixed_dim} + {vectors_per_trait}*trait_count"
        )
    trait_count = remainder // vectors_per_trait
    if trait_count <= 0:
        raise ValueError(f"Invalid inferred trait count: {trait_count}")
    return trait_count


def zero_composition_controls(observations: torch.Tensor, trait_count: int, candidate_dim: int):
    """Zero [trait focus weights, locked flag, strength] without touching candidate tail."""
    if candidate_dim <= 0 or trait_count <= 0:
        raise ValueError(f"Invalid composition layout: traits={trait_count}, candidate_dim={candidate_dim}")
    control_dim = int(trait_count) + 2
    candidate_start = observations.shape[-1] - int(candidate_dim)
    start = candidate_start - control_dim
    end = start + control_dim
    if start < 0 or end != candidate_start:
        raise ValueError(
            f"Invalid composition slice: obs={observations.shape[-1]}, "
            f"traits={trait_count}, candidate_dim={candidate_dim}"
        )
    result = observations.clone()
    result[..., start:end] = 0
    return result


def _tensor_masks(raw_masks):
    if len(raw_masks) != 8:
        raise ValueError(f"Expected masks for 8 players, received {len(raw_masks)}")
    return {
        key: torch.as_tensor(
            np.stack([np.asarray(player_masks[key]) for player_masks in raw_masks]),
            dtype=torch.bool,
        )
        for key in MASK_KEYS
    }


def _run_match(policy, seed: int, ablate: bool, max_steps: int):
    # Import lazily so pure helper tests do not require the compiled native module.
    from cpp_lobby_env import CppTFTLobbyWrapper

    env = CppTFTLobbyWrapper(seed=seed)
    try:
        observations_np = env.reset(seed=seed)
        # active_traits may list only traits active in this match; use the full observation layout.
        try:
            trait_count = infer_trait_count_from_observation_dim(int(observations_np.shape[-1]))
        except ValueError as exc:
            raise RuntimeError("Could not infer the full trait catalog from the observation dimension.") from exc

        totals = np.zeros(8, dtype=np.float64)
        action_counts = np.zeros(len(ACTION_NAMES), dtype=np.int64)
        purchase_fit_sum = 0.0
        purchase_fit_count = 0
        deploy_fit_sum = 0.0
        deploy_fit_count = 0
        changed_action_rows = 0
        compared_action_rows = 0
        steps = 0
        candidate_dim = policy.candidate_observation_dim

        while steps < max_steps:
            obs = torch.as_tensor(observations_np, dtype=torch.float32)
            masks = _tensor_masks(env.get_action_masks())
            ablated_obs = zero_composition_controls(obs, trait_count, candidate_dim)

            with torch.no_grad():
                baseline_actions = policy.get_action_and_value(
                    obs, masks=masks, deterministic=True
                )[0]
                ablated_actions = policy.get_action_and_value(
                    ablated_obs, masks=masks, deterministic=True
                )[0]

            baseline_np = baseline_actions.cpu().numpy()
            ablated_np = ablated_actions.cpu().numpy()
            changed_action_rows += int(np.any(baseline_np != ablated_np, axis=1).sum())
            compared_action_rows += int(obs.shape[0])
            selected_actions = ablated_np if ablate else baseline_np

            # Candidate features remain in the observation tail: fit is feature 0
            # for each bench/shop candidate, aligned with action slots.
            raw_obs = observations_np
            tail_start = raw_obs.shape[1] - candidate_dim
            bench_tail_start = tail_start
            shop_tail_start = tail_start + 9 * CANDIDATE_FEATURE_DIM
            for player_id, action in enumerate(selected_actions):
                action_type = int(action[0])
                action_counts[action_type] += 1
                if action_type == 0:
                    shop_slot = int(action[1])
                    fit_idx = shop_tail_start + shop_slot * CANDIDATE_FEATURE_DIM
                    purchase_fit_sum += float(raw_obs[player_id, fit_idx])
                    purchase_fit_count += 1
                elif action_type == 3:
                    bench_slot = int(action[2])
                    fit_idx = bench_tail_start + bench_slot * CANDIDATE_FEATURE_DIM
                    deploy_fit_sum += float(raw_obs[player_id, fit_idx])
                    deploy_fit_count += 1

            observations_np, rewards, done, _info = env.step(selected_actions.tolist())
            totals += np.asarray(rewards, dtype=np.float64)
            steps += 1
            if done:
                break

        return {
            "seed": int(seed),
            "ablation": bool(ablate),
            "steps": int(steps),
            "mean_return_per_player": float(totals.mean()),
            "total_return_all_players": float(totals.sum()),
            "action_counts": {
                ACTION_NAMES[index]: int(count)
                for index, count in enumerate(action_counts)
            },
            "mean_purchase_fit": (
                purchase_fit_sum / purchase_fit_count if purchase_fit_count else None
            ),
            "purchase_count": int(purchase_fit_count),
            "mean_bench_deployment_fit": (
                deploy_fit_sum / deploy_fit_count if deploy_fit_count else None
            ),
            "bench_deployment_count": int(deploy_fit_count),
            "same_state_action_change_rate": (
                changed_action_rows / compared_action_rows if compared_action_rows else 0.0
            ),
        }
    finally:
        env.close()


def _aggregate(rows):
    def avg(key):
        values = [row[key] for row in rows if row.get(key) is not None]
        return float(mean(values)) if values else None

    action_counts = {
        name: int(sum(row["action_counts"][name] for row in rows))
        for name in ACTION_NAMES
    }
    return {
        "matches": len(rows),
        "mean_steps": avg("steps"),
        "mean_return_per_player": avg("mean_return_per_player"),
        "mean_purchase_fit": avg("mean_purchase_fit"),
        "mean_bench_deployment_fit": avg("mean_bench_deployment_fit"),
        "mean_same_state_action_change_rate": avg("same_state_action_change_rate"),
        "action_counts": action_counts,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", default="tft_checkpoint.pt")
    parser.add_argument("--matches", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20261022)
    parser.add_argument("--max-steps", type=int, default=5000)
    parser.add_argument("--output", default="reports/composition_ablation.json")
    args = parser.parse_args()
    if args.matches <= 0 or args.max_steps <= 0:
        parser.error("--matches and --max-steps must be positive")

    from cpp_lobby_env import CppTFTLobbyWrapper

    probe = CppTFTLobbyWrapper(seed=args.seed)
    try:
        initial_obs = probe.reset(seed=args.seed)
        obs_dim = int(initial_obs.shape[-1])
    finally:
        probe.close()

    policy = TFTPolicy(obs_dim=obs_dim, action_dims=ACTION_DIMS, hidden_size=512)
    checkpoint = torch.load(args.checkpoint, map_location="cpu", weights_only=False)
    if "policy" not in checkpoint:
        raise KeyError("Checkpoint must contain a 'policy' state_dict.")
    migrated = policy.load_compatible_state_dict(checkpoint["policy"])
    policy.eval()

    baseline_rows = []
    ablated_rows = []
    for index in range(args.matches):
        seed = args.seed + index
        baseline_rows.append(_run_match(policy, seed, ablate=False, max_steps=args.max_steps))
        ablated_rows.append(_run_match(policy, seed, ablate=True, max_steps=args.max_steps))

    report = {
        "checkpoint": str(args.checkpoint),
        "checkpoint_migrated": bool(migrated),
        "obs_dim": obs_dim,
        "matches_per_condition": args.matches,
        "seed_start": args.seed,
        "conditions": {
            "composition_controls_enabled": _aggregate(baseline_rows),
            "composition_controls_zeroed": _aggregate(ablated_rows),
        },
        "paired_matches": [
            {"seed": args.seed + index, "enabled": baseline_rows[index], "zeroed": ablated_rows[index]}
            for index in range(args.matches)
        ],
        "interpretation": (
            "A non-zero same-state action-change rate shows the trained policy reacts "
            "to the composition-control slice. Match-level improvements require repeated "
            "paired seeds and should be interpreted alongside rewards and compatibility-fit proxies."
        ),
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "checkpoint_migrated": bool(migrated),
        "enabled": report["conditions"]["composition_controls_enabled"],
        "zeroed": report["conditions"]["composition_controls_zeroed"],
    }, indent=2))


if __name__ == "__main__":
    main()
