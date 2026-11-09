import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from economy_finetuning import chain_manager as chain
from economy_finetuning.scenario_generator import SCENARIOS


class ScenarioChainTests(unittest.TestCase):
    def test_order_is_eight_stages_and_strictly_sequential(self):
        self.assertEqual(len(chain.SCENARIO_ORDER), 8)
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
            source = root / "source.pt"
            summary = root / "summary.json"
            evaluation = root / "evaluation.json"
            checkpoint.write_bytes(b"checkpoint")
            source.write_bytes(b"source-model")
            summary.write_text(json.dumps({
                "selected_scenario": "critical_hp_high_gold",
                "selected_scenario_transitions": 100,
                "source_checkpoint_path": str(source),
                "source_checkpoint_sha256": chain.sha256_file(source),
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
            source = root / "source.pt"
            summary = root / "summary.json"
            evaluation = root / "evaluation.json"
            checkpoint.write_bytes(b"checkpoint")
            source.write_bytes(b"source-model")
            summary.write_text(json.dumps({
                "selected_scenario": "critical_hp_high_gold",
                "selected_scenario_transitions": 10,
                "source_checkpoint_path": str(source),
                "source_checkpoint_sha256": chain.sha256_file(source),
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


    def test_custom_source_can_start_any_stage_without_predecessor_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            custom = Path(directory) / "custom.pt"
            custom.write_bytes(b"custom-model")
            with patch.object(chain, "STATE_PATH", Path(directory) / "chain_state.json"):
                self.assertEqual(chain.check_scenario("econ_gold_reserve", custom, custom_source=True), custom.resolve())
                with self.assertRaisesRegex(RuntimeError, "depende de late_game_high_gold_underleveled"):
                    chain.check_scenario("econ_gold_reserve", custom)

    def test_custom_source_training_can_be_approved_and_unlock_next_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, checkpoint = root / "external.pt", root / "econ.pt"
            summary, evaluation = root / "summary.json", root / "evaluation.json"
            source.write_bytes(b"external-model")
            checkpoint.write_bytes(b"fine-tuned-model")
            source_hash = chain.sha256_file(source)
            summary.write_text(json.dumps({"selected_scenario": "econ_gold_reserve", "selected_scenario_transitions": 50, "source_mode": "custom", "source_checkpoint_path": str(source), "source_checkpoint_sha256": source_hash}), encoding="utf-8")
            with patch.object(chain, "STATE_PATH", root / "chain_state.json"):
                chain.record_training("econ_gold_reserve", checkpoint, summary)
                entry = chain._load()["scenarios"]["econ_gold_reserve"]
                self.assertEqual(entry["source_mode"], "custom")
                self.assertEqual(entry["source_checkpoint_sha256"], source_hash)
                evaluation.write_text(json.dumps({"approved": True, "checkpoint_sha256": chain.sha256_file(checkpoint)}), encoding="utf-8")
                chain.approve_scenario("econ_gold_reserve", evaluation)
                self.assertEqual(chain.check_scenario("econ_surplus_strong_board", source), checkpoint.resolve())

    def test_custom_source_rejects_mismatched_source_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, checkpoint = root / "external.pt", root / "result.pt"
            summary = root / "summary.json"
            source.write_bytes(b"external")
            checkpoint.write_bytes(b"result")
            summary.write_text(json.dumps({"selected_scenario": "econ_gold_reserve", "selected_scenario_transitions": 1, "source_mode": "custom", "source_checkpoint_path": str(source), "source_checkpoint_sha256": "incorrect"}), encoding="utf-8")
            with patch.object(chain, "STATE_PATH", root / "chain_state.json"):
                with self.assertRaisesRegex(RuntimeError, "Hash do checkpoint de origem"):
                    chain.record_training("econ_gold_reserve", checkpoint, summary)

if __name__ == "__main__":
    unittest.main()
