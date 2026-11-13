from pathlib import Path

source = Path("cpp/src/lobby/TftEngine.cpp").read_text(encoding="utf-8")
planner_header = Path("cpp/include/strategy/StrategicPlanner.hpp").read_text(encoding="utf-8")
context_header = Path("cpp/include/strategy/StrategicEvidenceContext.hpp").read_text(encoding="utf-8")

start = source.index("strategy::StrategicSharedContext strategic_context;")
end = source.index("const auto shadow_decision = strategic_planner.evaluate(", start)
planner_input = source[start:end]

for forbidden in (
    "info.composition_direction",
    "info.composition_focus",
    "info.core_traits",
    "info.composition_locked",
    "info.core_unit_ids",
    "info.planned_unit_ids",
    "info.strategic_committed_direction",
    "info.strategic_candidate_direction",
    "info.strategic_candidate_streak",
    "info.strategy",
):
    assert forbidden not in planner_input, f"legacy strategic input leaked: {forbidden}"

assert "StrategicEvidenceContext" in planner_header
assert "StrategicEvidenceContextBuilder" in source
assert "strategic_planner_commitments[i]" in source
assert "strategic_planner_commitments = {};" in source
assert "match_id" in context_header and "player_id" in context_header
assert "sequence" in context_header and "provenance" in context_header

# The new contract must not even name the old strategic source types.
for forbidden in ("StrategyInfo", "CompositionDirectionPolicy", "CompositionPlanner"):
    assert forbidden not in context_header, f"legacy type dependency: {forbidden}"

print("strategic evidence context architecture checks passed")
