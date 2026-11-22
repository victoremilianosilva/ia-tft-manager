"""Architecture contract: native strategic facts flow into PPO without legacy strategy APIs."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "cpp" / "src" / "lobby" / "TftEngine.cpp"
ENGINE_HEADER = ROOT / "cpp" / "include" / "lobby" / "TftEngine.hpp"
BINDINGS = ROOT / "cpp" / "bindings" / "tft_engine_bindings.cpp"
PYTHON_ADAPTER = ROOT / "cpp_lobby_env.py"
ENGINE_CONTRACTS = ROOT / "engine_contracts.py"
SEMANTIC = ROOT / "semantic_observation.py"
TRAINER = ROOT / "trainer.py"
POLICY = ROOT / "policy.py"
ROLLOUT = ROOT / "rollout.py"


class NativeStrategicPpoContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = ENGINE.read_text(encoding="utf-8")
        cls.engine_header = ENGINE_HEADER.read_text(encoding="utf-8")
        cls.bindings = BINDINGS.read_text(encoding="utf-8")
        cls.adapter = PYTHON_ADAPTER.read_text(encoding="utf-8")
        cls.contracts = ENGINE_CONTRACTS.read_text(encoding="utf-8")
        cls.semantic = SEMANTIC.read_text(encoding="utf-8")
        cls.trainer = TRAINER.read_text(encoding="utf-8")
        cls.policy = POLICY.read_text(encoding="utf-8")
        cls.rollout = ROLLOUT.read_text(encoding="utf-8")

    def test_legacy_strategy_contracts_are_absent(self):
        forbidden = (
            "StrategyInfo",
            "StrategyPolicy",
            "CompositionDirectionPolicy",
            "get_strategies",
            "get_viewer_strategy_snapshots",
            "get_strategy_snapshots",
            "update_legacy_strategy_compatibility_projection",
            "class Strategy(IntEnum)",
        )
        sources = (
            self.engine,
            self.engine_header,
            self.bindings,
            self.adapter,
            self.contracts,
        )
        for source in sources:
            for token in forbidden:
                with self.subTest(token=token):
                    self.assertNotIn(token, source)

    def test_native_engine_publishes_owned_strategic_facts(self):
        self.assertIn("void refresh_native_strategic_state(std::size_t i)", self.engine)
        self.assertIn("refresh_native_composition_candidates", self.engine)
        self.assertIn("refresh_native_strategic_runtime", self.engine)
        self.assertIn("AuditStrategicOwnerSnapshot strategic_state", self.engine_header)
        for field in (
            "active_composition_id",
            "active_composition_version",
            "direction_identity",
            "pivot_candidate_identity",
            "unit_copy_progress",
            "opportunity_cost_available",
        ):
            with self.subTest(field=field):
                self.assertIn(field, self.engine_header)

    def test_python_adapter_validates_native_strategic_snapshot(self):
        self.assertIn('strategic = player.get("strategic_state")', self.adapter)
        self.assertIn('strategic.get("unit_copy_progress")', self.adapter)
        self.assertIn('result.get("native_state_snapshot")', self.adapter)
        self.assertIn("get_audit_snapshot", self.engine)

    def test_semantic_projection_consumes_native_strategic_facts(self):
        self.assertIn('strategic = state.get("strategic_state")', self.semantic)
        for field in (
            "active_composition_valid",
            "direction_valid",
            "pivot_candidate_valid",
            "unit_copy_progress",
            "opportunity_cost_available",
        ):
            with self.subTest(field=field):
                self.assertIn(field, self.semantic)

    def test_trainer_passes_semantic_state_to_ppo_and_rollout(self):
        self.assertIn("build_semantic_batch(", self.trainer)
        self.assertIn("semantic_state=semantic_state", self.trainer)
        self.assertIn("semantic_state=next_semantic_state", self.trainer)
        self.assertIn("semantic_state=sample_semantic_state", self.trainer)
        self.assertIn("Native PPO rollout requires semantic_state v6", self.rollout)
        self.assertIn("semantic_state=semantic_state", self.rollout)

    def test_policy_uses_native_semantic_encoder(self):
        self.assertIn("self.semantic_encoder", self.policy)
        self.assertIn("self._semantic_entity_features", self.policy)
        self.assertIn("native PPO inference requires semantic_state v6", self.policy)

    def test_ppo_action_resolution_remains_read_only(self):
        self.assertIn("StrategicActionExecutor", self.engine)
        self.assertIn("resolution_request.source_context", self.engine)
        self.assertIn("StrategicActionResolution", self.engine)


if __name__ == "__main__":
    unittest.main()
