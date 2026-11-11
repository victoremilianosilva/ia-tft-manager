from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "cpp" / "src" / "lobby" / "TftEngine.cpp"
HEADER = ROOT / "cpp" / "include" / "lobby" / "TftEngine.hpp"


def _function_body(source: str, signature: str) -> str:
    start = source.index(signature)
    opening = source.index("{", start)
    depth = 0
    state = "code"
    i = opening
    while i < len(source):
        char = source[i]
        nxt = source[i + 1] if i + 1 < len(source) else ""
        if state == "line_comment":
            if char == "\n":
                state = "code"
        elif state == "block_comment":
            if char == "*" and nxt == "/":
                state = "code"
                i += 1
        elif state == "string":
            if char == "\\":
                i += 1
            elif char == '"':
                state = "code"
        elif state == "char":
            if char == "\\":
                i += 1
            elif char == "'":
                state = "code"
        else:
            if char == "/" and nxt == "/":
                state = "line_comment"
                i += 1
            elif char == "/" and nxt == "*":
                state = "block_comment"
                i += 1
            elif char == '"':
                state = "string"
            elif char == "'":
                state = "char"
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return source[opening + 1:i]
        i += 1
    raise AssertionError(f"Unclosed C++ function: {signature}")


class ShadowPpoIsolationArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = ENGINE.read_text(encoding="utf-8")
        cls.header = HEADER.read_text(encoding="utf-8")
        start_marker = "// BEGIN SHADOW-ONLY EVALUATION BOUNDARY."
        end_marker = "// END SHADOW-ONLY EVALUATION BOUNDARY."
        start = cls.source.index(start_marker)
        end = cls.source.index(end_marker, start)
        cls.shadow_block = cls.source[start:end]

    def test_all_strategic_shadow_work_uses_no_throw_boundary(self):
        self.assertIn("run_shadow_isolated([&]()", self.shadow_block)
        self.assertIn("}, [&]() noexcept", self.shadow_block)
        self.assertIn("info.strategic_shadow_only = false;", self.shadow_block)
        self.assertIn("info.economic_shadow_only = false;", self.shadow_block)

    def test_shadow_block_cannot_call_game_or_ppo_mutators(self):
        forbidden = (
            r"\brefresh_masks\s*\(",
            r"\bbuild_observations\s*\(",
            r"\bstate_reward\s*\(",
            r"\bresolve_combats\s*\(",
            r"\bvalidate_action(?:_against_masks)?\s*\(",
            r"\baction_mask_engine\b",
            r"\bRewardModel\b|\breward_model::",
            r"\bStepResult\b|\bResetResult\b|\bPlayerAction\b",
            r"\boptimizer\b|\brollout\b|\bcheckpoint\b",
            r"\.step\s*\(",
        )
        for pattern in forbidden:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.shadow_block))

    def test_shadow_diagnostic_fields_are_not_ppo_observation_inputs(self):
        body = _function_body(
            self.source,
            "std::vector<float> build_observations() const",
        )
        diagnostic_fields = (
            "strategic_shadow_only",
            "economic_shadow_only",
            "strategic_action_recommendation",
            "strategic_composition_decision",
            "strategic_candidate_diagnostics",
            "economic_posture",
        )
        for field in diagnostic_fields:
            with self.subTest(field=field):
                self.assertNotIn(field, body)

    def test_shadow_failure_boundary_is_noexcept_and_catches_reporter_failure(self):
        self.assertIn("bool run_shadow_isolated", self.header)
        self.assertIn("noexcept", self.header)
        self.assertIn("catch (...)", self.header)
        self.assertIn("std::forward<OnFailure>(on_failure)()", self.header)


if __name__ == "__main__":
    unittest.main()
