import unittest
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("audit_viewer_match.py")
spec = importlib.util.spec_from_file_location("audit_viewer_match", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def unit(name, **extra):
    return {"champion_id": name, "occupied": True, **extra}


class UnifiedAuditTests(unittest.TestCase):
    def test_nested_board_is_supported(self):
        state = {"board": [[unit("A"), None], [None, unit("B")]], "bench": []}
        self.assertEqual([audit.unit_name(u) for _, _, u in audit.iter_units(state)], ["A", "B"])

    def test_carry_frontline_and_tank_backline_are_reported(self):
        board = [None] * 28
        board[0] = unit("Veigar", role="carry")
        board[21] = unit("Braum", role="tank")
        entries = [{"event_type": "action", "step": 1, "stage": 2, "round_in_stage": 1,
                    "payload": {"state_after": {"board": board, "bench": []}}}]
        report = {"issues": []}
        audit.audit_positioning_and_composition(entries, "Jogador 1", report)
        codes = {issue["code"] for issue in report["issues"]}
        self.assertIn("CARRY_IN_FRONTLINE", codes)
        self.assertIn("TANK_IN_BACKLINE", codes)

    def test_missing_core_requires_repeated_snapshots(self):
        entries = [{"event_type": "action", "step": i, "stage": 2, "round_in_stage": 1,
                    "payload": {"state_after": {"board": [], "bench": [], "core_units": ["Nasus"]}}}
                   for i in range(1, 4)]
        report = {"issues": []}
        audit.audit_positioning_and_composition(entries, "Jogador 1", report)
        self.assertIn("CORE_UNIT_MISSING_REPEATEDLY", {issue["code"] for issue in report["issues"]})

    def test_selling_a_pair_copy_is_reported(self):
        before = {"board": [], "bench": [unit("Briar"), unit("Briar")], "gold": 6}
        after = {"board": [], "bench": [unit("Briar")], "gold": 7}
        entries = [{"event_type": "action", "sequence_id": 1, "step": 2, "stage": 2,
                    "round_in_stage": 1, "payload": {"action": [5, 0, 1], "action_name": "SELL",
                    "state_before": before, "state_after": after}}]
        report = {"issues": []}
        audit.audit_purchase_sequences(entries, "Jogador 1", report)
        self.assertIn("SOLD_UPGRADE_PAIR_COPY", {issue["code"] for issue in report["issues"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
