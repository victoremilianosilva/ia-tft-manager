"""Paired PPO regression gate plus scenario replay-retention checks.

This gate never promotes a checkpoint. It emits promotion_allowed only when
all numerical, completion, seed, and replay-coverage checks pass; a human still
reviews the report before choosing the production checkpoint.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import torch

from policy import TFTPolicy
from economy_finetuning.finetune import ACTION_DIMS
from economy_finetuning.scenario_generator import SCENARIOS


def _mean_ci(values):
    values = np.asarray(values, dtype=np.float64)
    if values.size == 0:
        return None
    mean = float(values.mean())
    se = float(values.std(ddof=1) / math.sqrt(values.size)) if values.size > 1 else float("inf")
    return {"n": int(values.size), "mean": mean, "lower95": mean - 1.96 * se, "upper95": mean + 1.96 * se}


def _load_rows(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(f"JSONL inválido na linha {line_no}: {exc}") from exc
    return rows


def replay_agreement(checkpoint_path, replay_path, min_type_agreement):
    replay = torch.load(replay_path, map_location="cpu", weights_only=False)
    observations = torch.as_tensor(replay["observations"], dtype=torch.float32)
    actions = torch.as_tensor(replay["actions"], dtype=torch.long)
    masks = {key: torch.as_tensor(value, dtype=torch.bool) for key, value in replay["masks"].items()}
    policy_payload = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    policy = TFTPolicy(observations.shape[-1], ACTION_DIMS)
    policy.load_compatible_state_dict(policy_payload.get("policy", policy_payload))
    policy.eval()
    by_scenario = {}
    for index, labels in enumerate(replay["scenario_ids"]):
        for label in labels:
            by_scenario.setdefault(label, []).append(index)
    report = {}
    passed = True
    with torch.no_grad():
        for label, indices in sorted(by_scenario.items()):
            predicted = []
            for start in range(0, len(indices), 512):
                batch_ids = torch.as_tensor(indices[start:start + 512], dtype=torch.long)
                batch_masks = {key: value.index_select(0, batch_ids) for key, value in masks.items()}
                selected, _, _, _ = policy.get_action_and_value(
                    observations.index_select(0, batch_ids), masks=batch_masks, deterministic=True
                )
                predicted.append(selected.cpu())
            predicted = torch.cat(predicted, dim=0)
            reference = actions[torch.as_tensor(indices, dtype=torch.long)]
            type_agreement = float((predicted[:, 0] == reference[:, 0]).float().mean().item())
            full_agreement = float((predicted == reference).all(dim=1).float().mean().item())
            report[label] = {
                "samples": len(indices),
                "action_type_agreement": type_agreement,
                "full_action_agreement": full_agreement,
                "meets_minimum": type_agreement >= min_type_agreement,
            }
            passed = passed and report[label]["meets_minimum"]
    return {"passed": passed, "minimum_type_agreement": min_type_agreement, "scenarios": report,
            "source_checkpoint_sha256": replay.get("source_checkpoint_sha256")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paired", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--replay", required=True)
    parser.add_argument("--coverage", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--min-seeds", type=int, default=30)
    parser.add_argument("--max-placement-regression", type=float, default=0.15)
    parser.add_argument("--max-top4-drop", type=float, default=0.03)
    parser.add_argument("--max-reward-drop", type=float, default=0.05)
    parser.add_argument("--max-board-score-drop", type=float, default=0.02)
    parser.add_argument("--min-type-agreement", type=float, default=0.80)
    args = parser.parse_args()
    if args.min_seeds < 2 or not 0 < args.min_type_agreement <= 1:
        parser.error("min-seeds deve ser >=2 e min-type-agreement deve estar em (0,1].")

    rows = _load_rows(args.paired)
    coverage = json.loads(Path(args.coverage).read_text(encoding="utf-8"))
    coverage_rows = coverage.get("coverage", {})
    expected_scenarios = {item.scenario_id for item in SCENARIOS if item.trainable}
    coverage_pass = expected_scenarios.issubset(coverage_rows) and all(
        coverage_rows.get(key, {}).get("meets_minimum", False) for key in expected_scenarios
    )
    completed = all(row.get("both_completed") and row.get("same_initial_state") for row in rows)
    seed_count_pass = len(rows) >= args.min_seeds
    deltas = [item for row in rows for item in row.get("final_player_deltas", [])]
    # Seeds, not individual player seats, are the independent statistical units.
    placement_by_seed, top4_by_seed = [], []
    board_by_seed = {"board_quality_score": [], "board_positional_score": [], "board_structural_score": []}
    for row in rows:
        seed_deltas = row.get("final_player_deltas", [])
        placements = [item["placement_delta"] for item in seed_deltas if item.get("placement_delta") is not None]
        top4_values = [item["top4_delta"] for item in seed_deltas if item.get("top4_delta") is not None]
        if placements:
            placement_by_seed.append(float(np.mean(placements)))
        if top4_values:
            top4_by_seed.append(float(np.mean(top4_values)))
        for key in board_by_seed:
            values = [item[key + "_delta"] for item in seed_deltas if item.get(key + "_delta") is not None]
            if values:
                board_by_seed[key].append(float(np.mean(values)))
    placement = _mean_ci(placement_by_seed)
    top4 = _mean_ci(top4_by_seed)
    reward = _mean_ci([row["mean_reward_delta"] for row in rows if row.get("mean_reward_delta") is not None])
    board_metrics = {key: _mean_ci(values) for key, values in board_by_seed.items()}
    replay = replay_agreement(args.checkpoint, args.replay, args.min_type_agreement)
    reference_hashes = {
        row.get("provenance", {}).get("original_checkpoint_sha256") for row in rows
        if row.get("provenance", {}).get("original_checkpoint_sha256")
    }
    replay_matches_reference = (
        len(reference_hashes) == 1
        and replay.get("source_checkpoint_sha256") in reference_hashes
    )

    checks = {
        "minimum_seed_count": seed_count_pass,
        "all_pairs_completed_and_identical_initial_state": completed,
        "all_finetuning_scenarios_have_replay_coverage": coverage_pass,
        "placement_not_regressed": bool(placement and placement["upper95"] <= args.max_placement_regression),
        "top4_not_regressed": bool(top4 and top4["lower95"] >= -args.max_top4_drop),
        "reward_not_regressed": bool(reward and reward["lower95"] >= -args.max_reward_drop),
        "board_scores_not_regressed": all(
            board_metrics[key] is not None and board_metrics[key]["lower95"] >= -args.max_board_score_drop
            for key in board_metrics
        ),
        "scenario_action_type_retention": replay["passed"],
        "replay_collected_from_evaluation_reference": replay_matches_reference,
    }
    promotion_allowed = all(checks.values())
    result = {
        "schema_version": 1,
        "approved": False,
        "promotion_allowed": promotion_allowed,
        "human_review_required": True,
        "checkpoint": str(Path(args.checkpoint).resolve()),
        "paired_seeds": len(rows),
        "metrics": {"placement_delta_candidate_minus_reference": placement,
                    "top4_delta_candidate_minus_reference": top4,
                    "mean_reward_delta_candidate_minus_reference": reward,
                    "board_score_deltas": board_metrics},
        "replay_preservation": replay,
        "coverage": coverage_rows,
        "checks": checks,
        "limits": {
            "max_placement_regression": args.max_placement_regression,
            "max_top4_drop": args.max_top4_drop,
            "max_reward_drop": args.max_reward_drop,
            "max_board_score_drop": args.max_board_score_drop,
            "min_type_agreement": args.min_type_agreement,
        },
        "note": "promotion_allowed é apenas elegibilidade técnica. A decisão humana continua obrigatória; nenhum checkpoint é promovido automaticamente.",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"promotion_allowed": promotion_allowed, "checks": checks, "output": str(output)}, ensure_ascii=False, indent=2))
    if not promotion_allowed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
