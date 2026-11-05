import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from economy_finetuning import chain_manager as chain
from economy_finetuning.scenario_generator import SCENARIOS


class ScenarioChainTests(unittest.TestCase):
    def test_order_is_ten_stages_and_strictly_sequential(self):
        self.assertEqual(len(chain.SCENARIO_ORDER), 10)
        trainable = {item.scenario_id for item in SCENARIOS if item.trainable}
        self.assertEqual(trainable, set(chain.SCENARIO_ORDER))
        self.assertEqual(chain.predecessor(chain.SCENARIO_ORDER[0]), None)
        self.assertEqual(chain.predecessor(chain.SCENARIO_ORDER[1]), chain.SCENARIO_ORDER[0])

    def test_second_scenario_is_blocked_until_predecessor_approved(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "chain_state.json"
            with patch.object(chain, "STATE_PATH", state):
                with self.assertRaisesRegex(RuntimeError, "depende de critical_hp_high_gold"):
                    chain.check_scenario("late_game_high_gold_underleveled", Path("tft_checkpoint.pt"))

    def test_approval_requires_matching_checkpoint_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "chain_state.json"
            checkpoint = root / "scenario1.pt"
            summary = root / "summary.json"
            evaluation = root / "evaluation.json"
            checkpoint.write_bytes(b"checkpoint")
            summary.write_text(json.dumps({
                "selected_scenario": "critical_hp_high_gold",
                "selected_scenario_transitions": 100,
                "source_checkpoint_sha256": "source-hash",
            }), encoding="utf-8")
            with patch.object(chain, "STATE_PATH", state):
                chain.record_training("critical_hp_high_gold", checkpoint, summary)
                digest = chain.sha256_file(checkpoint)
                evaluation.write_text(json.dumps({
                    "approved": True, "checkpoint_sha256": "wrong-hash",
                }), encoding="utf-8")
                with self.assertRaisesRegex(RuntimeError, "não corresponde"):
                    chain.approve_scenario("critical_hp_high_gold", evaluation)
                evaluation.write_text(json.dumps({
                    "approved": True, "checkpoint_sha256": digest,
                    "summary": {"top4_delta": 0.02},
                }), encoding="utf-8")
                chain.approve_scenario("critical_hp_high_gold", evaluation)
                self.assertEqual(
                    chain._load()["scenarios"]["critical_hp_high_gold"]["status"],
                    "approved",
                )

    def test_approved_checkpoint_is_the_only_next_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "chain_state.json"
            checkpoint = root / "scenario1.pt"
            summary = root / "summary.json"
            evaluation = root / "evaluation.json"
            checkpoint.write_bytes(b"checkpoint")
            summary.write_text(json.dumps({
                "selected_scenario": "critical_hp_high_gold",
                "selected_scenario_transitions": 10,
                "source_checkpoint_sha256": "original",
            }), encoding="utf-8")
            with patch.object(chain, "STATE_PATH", state):
                chain.record_training("critical_hp_high_gold", checkpoint, summary)
                evaluation.write_text(json.dumps({
                    "approved": True, "checkpoint_sha256": chain.sha256_file(checkpoint),
                }), encoding="utf-8")
                chain.approve_scenario("critical_hp_high_gold", evaluation)
                self.assertEqual(
                    chain.check_scenario(
                        "late_game_high_gold_underleveled", Path("tft_checkpoint.pt")
                    ),
                    checkpoint.resolve(),
                )


if __name__ == "__main__":
    unittest.main()
