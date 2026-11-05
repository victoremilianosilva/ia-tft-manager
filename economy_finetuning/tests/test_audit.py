import unittest

from economy_finetuning.audit import build_report, js_divergence


class AuditTests(unittest.TestCase):
    def test_js_divergence_is_zero_for_equal_distributions(self):
        self.assertAlmostEqual(js_divergence([0.2, 0.8], [0.2, 0.8]), 0.0)

    def test_paired_report_includes_placement_and_board_outcomes(self):
        paired = [{
            "seed": 123,
            "both_completed": True,
            "mean_reward_delta": 0.25,
            "final_player_deltas": [
                {
                    "player_id": 0,
                    "original_placement": 1, "finetuned_placement": 2,
                    "placement_delta": 1, "original_top4": True,
                    "finetuned_top4": True, "hp_delta": -4,
                    "gold_delta": -10, "level_delta": 1,
                    "board_structural_score_delta": 0.08,
                },
                {
                    "player_id": 1,
                    "original_placement": 5, "finetuned_placement": 4,
                    "placement_delta": -1, "original_top4": False,
                    "finetuned_top4": True, "hp_delta": 8,
                    "gold_delta": -5, "level_delta": 1,
                    "board_structural_score_delta": 0.12,
                },
            ],
        }]
        report = build_report([], paired)
        self.assertIn("Diferença média de colocação", report)
        self.assertIn("Taxa Top 4", report)
        self.assertIn("board_structural_score", report)
        self.assertIn("1/2 → 2/2", report)

    def test_report_includes_non_target_preservation(self):
        rows = [{
            "original_action": [4, 0, 0, 0, 1, 2],
            "finetuned_action": [4, 0, 0, 0, 2, 2],
            "original_type_probabilities": [0.1] * 9,
            "finetuned_type_probabilities": [0.1] * 9,
            "state": {"strategy_name": "FAST8"},
            "scenario_ids": [],
        }]
        report = build_report(rows)
        self.assertIn("Preservação das famílias não treinadas", report)
        self.assertIn("MOVE_BOARD", report)
        self.assertIn("Mudanças de argumentos com mesmo tipo de ação", report)


if __name__ == "__main__":
    unittest.main()
