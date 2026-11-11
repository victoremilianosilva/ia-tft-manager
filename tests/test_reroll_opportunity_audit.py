import tempfile
import unittest
from pathlib import Path

from scripts.audit_reroll_opportunity import analyze_reroll_audit, render_markdown


class RerollOpportunityAuditTests(unittest.TestCase):
    def write(self, root, name, content):
        path = root / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_matches_economic_context_and_preserves_missing_as_inconclusive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actions = self.write(root, "actions.md", """| Jogador | Round | Step | Ação | Campeão | Oportunidade | Board | Sobrevivência | Composição | Upgrade | Postura | Score custo direto | Score juros | Score oportunidade | Total |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 2-1 | 10 | REROLL | -1 | 3.5 | 0.09 | 0 | 0.04 | 0.07 | 0 | -0.11 | 0 | -0.35 | -0.25 |
| Jogador 1 | 2-1 | 11 | REROLL | -1 | 4.0 | 0.01 | 0 | 0 | 0 | 0 | -0.11 | 0 | -0.40 | -0.50 |
""")
            economy = self.write(root, "economy.md", """| Jogador | Round | Step | Postura | Confiança | Pressão sobrevivência | Pressão board |
|---|---|---:|---|---:|---:|---:|
| Jogador 1 | 2-1 | 10 | STABILIZE_BOARD | 0.8 | 0.1 | 0.8 |
""")
            result = analyze_reroll_audit(actions, economy)
            self.assertEqual(result["reroll_candidate_count"], 2)
            self.assertEqual(result["economic_context_matches"], 1)
            self.assertEqual(result["economic_context_missing"], 1)
            self.assertEqual(result["review_buckets"]["plausible_window_review"], 1)
            self.assertEqual(result["review_buckets"]["inconclusive"], 1)
            self.assertEqual(result["score_statistics"]["Score oportunidade"]["mean"], -0.375)

    def test_accumulation_without_upgrade_signal_is_only_a_review_flag(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actions = self.write(root, "actions.md", """| Jogador | Round | Step | Ação | Campeão | Oportunidade | Board | Sobrevivência | Composição | Upgrade | Postura | Score custo direto | Score juros | Score oportunidade | Total |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 2 | 3-2 | 20 | REROLL | -1 | 4 | 0 | 0 | 0 | 0 | 0 | -0.11 | 0 | -0.4 | -0.51 |
""")
            economy = self.write(root, "economy.md", """| Jogador | Round | Step | Postura | Pressão sobrevivência | Pressão board |
|---|---|---:|---|---:|---:|
| Jogador 2 | 3-2 | 20 | ACCUMULATE_RESOURCES | 0.1 | 0.1 |
""")
            result = analyze_reroll_audit(actions, economy)
            self.assertEqual(result["review_buckets"]["weak_reroll_evidence_review"], 1)
            self.assertIn("not labels of optimal play", result["limitations"][0])

    def test_report_discloses_diagnostic_limitations(self):
        result = {
            "reroll_candidate_count": 0, "economic_context_matches": 0,
            "economic_context_missing": 0, "review_buckets": {},
            "economic_postures": {}, "score_statistics": {}, "rounds": {},
            "limitations": ["Diagnostic only."],
        }
        self.assertIn("Diagnostic only", render_markdown(result))


if __name__ == "__main__":
    unittest.main()
