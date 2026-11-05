import unittest

from economy_finetuning.audit import build_report, js_divergence


class AuditTests(unittest.TestCase):
    def test_js_divergence_is_zero_for_equal_distributions(self):
        self.assertAlmostEqual(js_divergence([0.2, 0.8], [0.2, 0.8]), 0.0)

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
