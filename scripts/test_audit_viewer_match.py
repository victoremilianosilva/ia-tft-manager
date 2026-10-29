import json
import tempfile
import unittest
from pathlib import Path

from scripts import audit_viewer_match as audit


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

    def test_uuid_signature_distinguishes_duplicate_champions(self):
        state = {"board": [], "bench": [unit("A", uuid="unit-1"), unit("A", uuid="unit-2")]}
        sig = audit.signature(state)
        self.assertEqual(len(sig), 2)
        self.assertNotEqual(sig[0][2], sig[1][2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
