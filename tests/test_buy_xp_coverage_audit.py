import tempfile
import unittest
from pathlib import Path

from scripts.audit_buy_xp_coverage import analyze_buy_xp_audit, render_markdown


class BuyXpCoverageAuditTests(unittest.TestCase):
    def write(self, root, name, content):
        path = root / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_classifies_selected_positive_outscored_and_non_positive_candidates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actions = self.write(root, "actions.md", """# Action audit

| Jogador | Round | Step | PPO executou | Recomendação |
|---|---|---:|---|---|
| Jogador 1 | 4-1 | 10 | PASS | BUY_XP |
| Jogador 1 | 4-1 | 11 | PASS | HOLD |
| Jogador 1 | 4-1 | 12 | PASS | HOLD |

| Jogador | Round | Step | Ação | Campeão | Disponível | Δ ouro direto | Juros perdidos | Oportunidade | Board | Sobrevivência | Streak | Composição | Upgrade | Postura | Score custo direto | Score juros | Score oportunidade | Total | Selecionado |
|---|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jogador 1 | 4-1 | 10 | BUY_XP | -1 | True | 4 | 0 | 0.25 | 0.36 | 0.1 | 0.02 | 0 | 0.07 | 0.24 | -0.22 | 0 | -0.025 | 0.5 | True |
| Jogador 1 | 4-1 | 10 | BUY_UNIT | 12 | True | 2 | 0 | 0.35 | 0.2 | 0 | 0 | 0 | 0.1 | 0 | -0.11 | 0 | -0.035 | 0.3 | False |
| Jogador 1 | 4-1 | 11 | BUY_XP | -1 | True | 4 | 0 | 0.25 | 0.12 | 0 | 0 | 0 | 0.014 | 0 | -0.22 | 0 | -0.025 | 0.1 | False |
| Jogador 1 | 4-1 | 11 | BUY_UNIT | 14 | True | 2 | 0 | 0.35 | 0.3 | 0 | 0 | 0 | 0.1 | 0 | -0.11 | 0 | -0.035 | 0.2 | True |
| Jogador 1 | 4-1 | 12 | BUY_XP | -1 | True | 4 | 1 | 0.25 | 0.12 | 0 | 0 | 0 | 0.014 | 0 | -0.22 | -0.1 | -0.025 | -0.2 | False |
| Jogador 1 | 4-1 | 12 | BUY_UNIT | 16 | True | 2 | 0 | 0.35 | 0.3 | 0 | 0 | 0 | 0.1 | 0 | -0.11 | 0 | -0.035 | 0.3 | True |
""")
            economy = self.write(root, "economy.md", """| Jogador | Round | Step | Postura | Confiança | Pressão sobrevivência | Pressão board |
|---|---|---:|---|---:|---:|---:|
| Jogador 1 | 4-1 | 10 | INVEST_EXPERIENCE | 0.8 | 0.2 | 0.3 |
""")
            result = analyze_buy_xp_audit(actions, economy)
            self.assertEqual(result["buy_xp_candidate_count"], 3)
            self.assertEqual(result["buy_xp_selected_candidate_count"], 1)
            self.assertEqual(result["final_buy_xp_recommendation_count"], 1)
            self.assertEqual(result["review_buckets"]["selected_recommendation"], 1)
            self.assertEqual(result["review_buckets"]["positive_but_outscored"], 1)
            self.assertEqual(result["review_buckets"]["non_positive_candidate"], 1)
            self.assertEqual(result["economic_context_matches"], 1)
            self.assertEqual(result["positive_score_but_outscored_margin"]["mean"], -0.1)

    def test_missing_economic_context_is_reported_not_inferred(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actions = self.write(root, "actions.md", """| Jogador | Round | Step | PPO executou | Recomendação |
|---|---|---:|---|---|
| Jogador 2 | 5-1 | 20 | PASS | HOLD |

| Jogador | Round | Step | Ação | Campeão | Disponível | Δ ouro direto | Juros perdidos | Oportunidade | Board | Sobrevivência | Streak | Composição | Upgrade | Postura | Score custo direto | Score juros | Score oportunidade | Total | Selecionado |
|---|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jogador 2 | 5-1 | 20 | BUY_XP | -1 | True | 4 | 0 | 0.25 | 0.36 | 0.1 | 0.02 | 0 | 0.07 | 0.24 | -0.22 | 0 | -0.025 | 0.5 | True |
""")
            result = analyze_buy_xp_audit(actions)
            self.assertEqual(result["economic_context_missing"], 1)
            self.assertEqual(result["economic_context_matches"], 0)
            self.assertIn("not proof", result["limitations"][0])

    def test_markdown_discloses_scope_and_limitations(self):
        report = render_markdown({
            "buy_xp_candidate_count": 1,
            "buy_xp_selected_candidate_count": 1,
            "final_buy_xp_recommendation_count": 1,
            "positive_score_candidate_count": 1,
            "economic_context_matches": 0,
            "economic_context_missing": 1,
            "review_buckets": {"selected_recommendation": 1},
            "candidate_components": {},
            "selected_by_round": {"5-1": 1},
            "rounds": {},
            "limitations": ["Diagnostic only."],
        })
        self.assertIn("BUY_XP coverage audit", report)
        self.assertIn("Diagnostic only.", report)


if __name__ == "__main__":
    unittest.main()
