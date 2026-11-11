import tempfile
import unittest
from pathlib import Path

from scripts.audit_hold_baseline import analyze_hold_audit, render_markdown


class HoldBaselineAuditTests(unittest.TestCase):
    def write(self, root, name, content):
        path = root / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_reports_fixed_hold_score_and_alternative_margin(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actions = self.write(root, "actions.md", """| Jogador | Round | Step | PPO executou | Recomendação |
|---|---|---:|---|---|
| P1 | 4-1 | 10 | PASS | HOLD |
| P1 | 4-1 | 11 | PASS | BUY_UNIT |

| Jogador | Round | Step | Ação | Campeão | Disponível | Δ ouro direto | Juros perdidos | Oportunidade | Board | Sobrevivência | Streak | Composição | Upgrade | Postura | Score custo direto | Score juros | Score oportunidade | Total | Selecionado |
|---|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P1 | 4-1 | 10 | HOLD | -1 | True | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.24 | 0 | 0 | 0 | 0.24 | True |
| P1 | 4-1 | 10 | BUY_UNIT | 90 | True | 3 | 0 | 0 | 0.8 | 0 | 0 | 0.2 | 0.1 | 0 | -0.1 | 0 | 0 | 0.8 | False |
| P1 | 4-1 | 11 | HOLD | -1 | True | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.24 | 0 | 0 | 0 | 0.24 | False |
| P1 | 4-1 | 11 | BUY_UNIT | 91 | True | 3 | 0 | 0 | 0.1 | 0 | 0 | 0 | 0 | 0 | -0.1 | 0 | 0 | 0.1 | True |
""")
            economy = self.write(root, "economy.md", """| Jogador | Round | Step | Postura | Confiança |
|---|---|---:|---|---:|
| P1 | 4-1 | 10 | ACCUMULATE_RESOURCES | 0.8 |
| P1 | 4-1 | 11 | STABILIZE_BOARD | 0.7 |
""")
            result = analyze_hold_audit(actions, economy)
            self.assertEqual(result["candidate_count"], 2)
            self.assertEqual(result["selected_candidate_count"], 1)
            self.assertEqual(result["final_hold_recommendations"], 1)
            self.assertEqual(result["total_score"]["distinct"], 1)
            self.assertEqual(result["comparisons"]["hold_below_best_alternative"], 1)
            self.assertEqual(result["missing_economy_context"], 0)
            self.assertIn("HOLD baseline audit", render_markdown(result))

    def test_missing_tables_and_economic_context_are_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actions = self.write(root, "actions.md", "# no action candidates\n")
            result = analyze_hold_audit(actions)
            self.assertEqual(result["candidate_count"], 0)
            self.assertEqual(result["missing_economy_context"], 0)
            self.assertIn("not a calibrated utility", result["limitations"][0])


if __name__ == "__main__":
    unittest.main()
