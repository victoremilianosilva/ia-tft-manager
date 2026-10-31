import json
import tempfile
import unittest
from pathlib import Path

from scripts import audit_viewer_match as audit
from viewer.player_logs import PlayerJsonLogWriter, _mask_audit


def unit(name, **extra):
    return {"champion_id": name, "occupied": True, **extra}


class UnifiedAuditRegressionTests(unittest.TestCase):
    def test_structured_json_inside_tft_extension_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            doc = {"entries": [{"event_type": "match_started", "payload": {"state": {"board": [], "bench": []}}}]}
            path = root / "player_1_log.tft"
            path.write_text(json.dumps(doc), encoding="utf-8")
            parsed = audit.read_json(path)
            self.assertIsInstance(parsed, dict)
            self.assertEqual(len(parsed["entries"]), 1)

    def test_nested_board_supported(self):
        state = {"board": [[unit("A"), None], [None, unit("B")]], "bench": []}
        self.assertEqual([audit.unit_name(u) for _, _, u in audit.iter_units(state)], ["A", "B"])

    def test_legacy_text_log_reconstructs_strategy_action_and_gold(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "player_1_log.tft"
            path.write_text(
                "[10:00:00] REROLL LOJA | Rew: -0.04\n"
                "    STRATEGY: FAST8 | COMP DIRECTION: Invoker | FOCUS: Support\n"
                "    STRATEGY REASON: FAST8 target | CONF: 0.90\n"
                "    GOLD: 34 | renda base +5 | juros +3 | sequência +0 | vitória +0\n",
                encoding="utf-8",
            )
            report = {"issues": [], "players_seen": set(), "log_files": []}
            audit.audit_text(path, report)
            metrics = report["text_log_metrics"]["Jogador 1"]
            self.assertEqual(metrics["action_counts"]["REROLL"], 1)
            self.assertEqual(metrics["timeline"][0]["strategy"], "FAST8")
            self.assertEqual(metrics["timeline"][0]["gold_after"], 34)
            self.assertEqual(metrics["timeline"][0]["income"]["interest"], 3)
            self.assertEqual(metrics["timeline"][0]["conformity_candidate"], "FAST8_REROLL_REVIEW")

    def test_mask_audit_preserves_legal_alternatives(self):
        mask = {"type_mask": [1, 1, 1, 0, 0, 1, 1, 0, 0], "shop_mask": [1, 0, 1, 0, 0],
                "bench_source_mask": [1] + [0] * 8, "board_target_mask": [0] * 28,
                "board_source_mask": [0] * 28, "bench_to_board_target_masks": [[0] * 28 for _ in range(9)],
                "board_move_target_masks": [[0] * 28 for _ in range(28)]}
        result = _mask_audit([0, 2, 0, 0, 0, 0], mask)
        self.assertTrue(result["chosen_type_enabled"])
        self.assertTrue(result["chosen_action_fully_validated"])
        self.assertEqual(result["legal_shop_slots"], [0, 2])
        self.assertIn({"id": 1, "name": "REROLL"}, result["legal_action_types"])

    def test_writer_persists_structured_json_sidecars(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            writer = PlayerJsonLogWriter(root, match_id="test-match", checkpoint_sha256="abc",
                seed=7, deterministic=True, catalog_path=root / "missing-catalog.json")
            writer.close()
            doc = json.loads((root / "player_1_log.json").read_text(encoding="utf-8"))
            self.assertEqual(doc["schema_version"], 2)
            self.assertEqual(doc["match_id"], "test-match")
            self.assertTrue((root / "player_1_log.tft").is_file())
            snapshot = writer._player_snapshot(
                {"positioning_score": 0.7, "board_quality_score": 0.7,
                 "board_positional_score": 0.4, "board_structural_score": 0.3,
                 "board_frontline_count": 2},
                {"board_quality_score": 0.0, "board_positional_score": 0.0,
                 "board_structural_score": 0.0, "board_frontline_count": 0},
            )
            self.assertEqual(snapshot["positioning_score"], 0.7)
            self.assertEqual(snapshot["board_quality_score"], 0.7)
            self.assertEqual(snapshot["board_positional_score"], 0.4)
            self.assertEqual(snapshot["board_structural_score"], 0.3)
            self.assertEqual(snapshot["board_frontline_count"], 2)

    def test_decision_audit_crosses_mask_reward_and_uuid(self):
        entry = {"event_type": "action", "sequence_id": 1, "step": 10, "round": 4, "payload": {
            "action": [0, 0, 0, 0, 0, 0], "action_name": "BUY",
            "decision_context": {"hp": 72, "level": 5, "gold": 22, "xp": 4, "board_power": 40, "strategy": "STABILIZE"},
            "legal_action_audit": {"chosen_type_enabled": True, "chosen_action_fully_validated": True,
                                   "legal_action_types": [{"id": 0, "name": "BUY"}]},
            "action_mask_before": {"type_mask": [1]},
            "reward_components": {"action": 0.1, "combat": 0.0, "placement": 0.0, "returned_reward": 0.1},
            "state_before": {"board": [], "bench": []},
            "state_after": {"board": [], "bench": [unit("A", uuid="unit-uuid")]}}}
        report = {"issues": []}
        audit.audit_decision_context([entry], "Jogador 1", report)
        metrics = report["decision_audit_metrics"]["Jogador 1"]
        self.assertEqual(metrics["mask_snapshots"], 1)
        self.assertEqual(metrics["reward_channels_complete"], 1)
        self.assertEqual(report["decision_timeline"][0]["unit_changes"]["added"][0]["uuid"], "unit-uuid")

    def test_uuid_signature_distinguishes_duplicate_champions(self):
        state = {"board": [], "bench": [unit("A", uuid="unit-1"), unit("A", uuid="unit-2")]}
        sig = audit.signature(state)
        self.assertEqual(len(sig), 2)
        self.assertNotEqual(sig[0][2], sig[1][2])


    def test_full_report_includes_decision_evidence_and_existing_summary(self):
        report = {
            "source": "fixture", "log_files": ["player_1_log.json"],
            "players_seen": ["1"], "entries_read": 1, "diagnostics_missing": 0,
            "issues": [{"severity": "MEDIUM", "code": "TEST", "player": "Jogador 1",
                        "round": "2-1", "step": 7, "message": "review", "evidence": {"gold": 12}}],
            "notes": [],
            "decision_timeline": [{
                "player": "Jogador 1", "round": "2-1", "step": 7, "sequence_id": 8,
                "action": [0, 1, 0, 0, 0, 0], "action_name": "BUY", "strategy": "STABILIZE",
                "decision_context": {"gold": 12, "level": 4},
                "state_before": {"gold": 12, "board": [unit("A", uuid="u1")]},
                "state_after": {"gold": 9, "board": [unit("A", uuid="u1")], "comp_direction": "A"},
                "legal_action_audit": {"chosen_type_enabled": True, "raw_mask": {"type_mask": [1, 1]}},
                "action_mask_before": {"type_mask": [1, 1]},
                "policy_diagnostics": {"entropy": 0.2},
                "reward_components": {"action": 0.25},
                "economic_diagnostics": {"action_cost": 3},
                "unit_changes": {"added": [], "removed": []},
                "composition_diagnostics": {"unit_fit": {"focus_fit_score": 1.0}},
                "item_audit": {"inventory_after": ["item_a"]},
            }],
        }
        full = audit.markdown_full_report(report)
        self.assertTrue(full.startswith("# Auditoria da partida TFT"))
        self.assertIn("## Evidências resumidas dos achados", full)
        self.assertIn("Legalidade: tipo permitido", full)
        self.assertNotIn('"type_mask": [', full)
        self.assertNotIn('"focus_fit_score": 1.0', full)
        self.assertNotIn('"inventory_after": [', full)
        self.assertIn("Evidência adicional: gold=12", full)

    def test_full_report_supports_legacy_without_decisions(self):
        full = audit.markdown_full_report({
            "source": "legacy", "log_files": [], "players_seen": [],
            "entries_read": 0, "diagnostics_missing": 0, "issues": [],
            "notes": [], "decision_timeline": [],
        })
        self.assertIn("Decisões com timeline: 0", full)


if __name__ == "__main__":
    unittest.main(verbosity=2)
