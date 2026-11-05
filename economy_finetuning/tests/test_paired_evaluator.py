import unittest

from economy_finetuning.paired_evaluator import (
    compare_final_metrics,
    extract_final_metrics,
)


class PairedEvaluatorTests(unittest.TestCase):
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
