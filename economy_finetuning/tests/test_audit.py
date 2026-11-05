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
        self.assertIn("estrutura", report)
        self.assertIn("1/2 → 2/2", report)
        self.assertIn("50.0% → 100.0%", report)
        self.assertIn("Frequência de ações nas partidas completas", report)

    def test_report_includes_checkpoint_engine_and_reward_provenance(self):
        metadata = {
            "repository_commit": "abc123",
            "checkpoint_sha256": "original-hash",
            "finetuned_checkpoint_sha256": "tuned-hash",
            "reward_model_source_sha256": "reward-hash",
            "engine_source_sha256": "engine-hash",
            "config_sha256": "config-hash",
            "selected_scenario": "critical_hp_high_gold",
            "ppo_parameters": {"learning_rate": 1e-5, "clip_coef": 0.1},
        }
        summary = {
            "selected_scenario_transitions": 120,
            "optimizer_steps_total": 15,
        }
        report = build_report([], metadata=metadata, training_summary=summary)
        self.assertIn("abc123", report)
        self.assertIn("original-hash", report)
        self.assertIn("reward-hash", report)
        self.assertIn("critical_hp_high_gold", report)
        self.assertIn("optimizer steps", report)

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
