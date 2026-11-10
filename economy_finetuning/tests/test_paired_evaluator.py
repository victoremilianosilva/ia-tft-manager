import unittest

import numpy as np
import torch

from economy_finetuning.finetune import MASK_SHAPES, _flatten_masks
from economy_finetuning.paired_evaluator import (
    aggregate_mirrored_runs,
    compare_final_metrics,
    extract_final_metrics,
    masks_sha256,
)


class PairedEvaluatorTests(unittest.TestCase):
    def test_policy_subgroups_can_flatten_four_player_masks(self):
        masks = [
            {key: np.ones(shape, dtype=np.int8) for key, shape in MASK_SHAPES.items()}
            for _ in range(4)
        ]
        flattened = _flatten_masks(masks, torch.device("cpu"))
        self.assertEqual(flattened["type_mask"].shape[0], 4)

    def test_action_mask_hash_is_stable_and_detects_mask_changes(self):
        masks = [
            {"type_mask": [1, 0, 1], "bench_mask": [0, 1]},
            {"type_mask": [0, 1, 0], "bench_mask": [1, 0]},
        ]
        self.assertEqual(masks_sha256(masks), masks_sha256(masks))
        changed = [
            {"type_mask": [1, 0, 1], "bench_mask": [0, 1]},
            {"type_mask": [0, 1, 1], "bench_mask": [1, 0]},
        ]
        self.assertNotEqual(masks_sha256(masks), masks_sha256(changed))

    def test_terminal_ranking_and_fresh_audit_board_metrics_are_joined(self):
        public_state = {
            "finished": True,
            "ranking": [2, 0, 1],
            "players": [
                {"player_id": 0, "placement": None, "hp": 35, "gold": 80, "level": 8,
                 "board_quality_score": 0.0},
                {"player_id": 1, "placement": 3, "hp": 20, "gold": 60, "level": 7},
                {"player_id": 2, "placement": 1, "hp": 50, "gold": 40, "level": 9},
            ],
        }
        audit_snapshot = {
            "players": [
                {"player_id": 0, "board_power": 40, "board_quality_score": 0.35,
                 "board_positional_score": 0.20, "board_structural_score": 0.15},
            ],
        }
        metrics = extract_final_metrics(public_state, audit_snapshot)
        player_zero = next(item for item in metrics if item["player_id"] == 0)
        self.assertEqual(player_zero["placement"], 2)
        self.assertEqual(player_zero["top4"], True)
        self.assertAlmostEqual(player_zero["board_quality_score"], 0.35)
        self.assertAlmostEqual(player_zero["board_structural_score"], 0.15)

    def test_mirrored_mixed_lobbies_pair_same_seat_and_policy_cohorts(self):
        def make_run(variants, mirror):
            metrics = []
            rewards = []
            counts = []
            for player_id, variant in enumerate(variants):
                if mirror:
                    placement = player_id // 2 + (1 if variant == "finetuned" else 5)
                else:
                    placement = player_id // 2 + (1 if variant == "finetuned" else 5)
                metrics.append({
                    "player_id": player_id,
                    "policy_variant": variant,
                    "placement": placement,
                    "top4": placement <= 4,
                    "hp": 50 if variant == "finetuned" else 20,
                    "gold": 70, "level": 8, "board_power": 40,
                    "board_quality_score": 0.3, "board_positional_score": 0.2,
                    "board_structural_score": 0.1,
                })
                rewards.append(10.0 if variant == "finetuned" else 5.0)
                counts.append({"BUY_XP": 1})
            return {
                "seed": 99, "steps": 250, "completed": True,
                "policy_variants": variants,
                "initial_observation_sha256": "same-observation",
                "initial_masks_sha256": "same-masks",
                "total_rewards": rewards,
                "action_counts": counts,
                "final_metrics": metrics,
            }

        variants_a = ["finetuned" if i % 2 == 0 else "original" for i in range(8)]
        variants_b = ["original" if i % 2 == 0 else "finetuned" for i in range(8)]
        row = aggregate_mirrored_runs(
            make_run(variants_a, False),
            make_run(variants_b, True),
            {"evaluation_mode": "mixed_4v4_mirrored_seats"},
        )
        self.assertTrue(row["both_completed"])
        self.assertTrue(row["same_initial_state"])
        self.assertAlmostEqual(row["mean_reward_delta"], 5.0)
        self.assertEqual(len(row["final_player_deltas"]), 8)
        self.assertTrue(all(item["placement_delta"] == -4 for item in row["final_player_deltas"]))

    def test_compare_final_metrics_uses_finetuned_minus_original(self):
        original = [{
            "player_id": 0, "placement": 6, "top4": False, "hp": 10,
            "gold": 100, "level": 7, "board_power": 25,
            "board_quality_score": 0.1, "board_positional_score": 0.05,
            "board_structural_score": 0.05,
        }]
        tuned = [{
            "player_id": 0, "placement": 3, "top4": True, "hp": 35,
            "gold": 70, "level": 8, "board_power": 40,
            "board_quality_score": 0.3, "board_positional_score": 0.1,
            "board_structural_score": 0.2,
        }]
        delta = compare_final_metrics(original, tuned)[0]
        self.assertEqual(delta["placement_delta"], -3)
        self.assertEqual(delta["top4_delta"], 1)
        self.assertEqual(delta["hp_delta"], 25)
        self.assertAlmostEqual(delta["board_structural_score_delta"], 0.15)


if __name__ == "__main__":
    unittest.main()
