"""Static contract checks for the native strategic evidence architecture."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "cpp/src/lobby/TftEngine.cpp").read_text(encoding="utf-8")
engine_header = (ROOT / "cpp/include/lobby/TftEngine.hpp").read_text(encoding="utf-8")
context_header = (ROOT / "cpp/include/strategy/StrategicEvidenceContext.hpp").read_text(encoding="utf-8")
planner_header = (ROOT / "cpp/include/strategy/StrategicPlanner.hpp").read_text(encoding="utf-8")
planning_header = (ROOT / "cpp/include/strategy/StrategicPlanning.hpp").read_text(encoding="utf-8")
evidence_header = (ROOT / "cpp/include/composition_intelligence/PlannerEvidenceAdapters.hpp").read_text(encoding="utf-8")
diagnostics_header = (ROOT / "cpp/include/composition_intelligence/CompositionDiagnostics.hpp").read_text(encoding="utf-8")
runtime_header = (ROOT / "cpp/include/composition_intelligence/CompositionIntelligenceRuntime.hpp").read_text(encoding="utf-8")
bridge_header = (ROOT / "cpp/include/composition_intelligence/StrategicContextBridge.hpp").read_text(encoding="utf-8")
wrapper = (ROOT / "cpp_lobby_env.py").read_text(encoding="utf-8")
semantic = (ROOT / "semantic_observation.py").read_text(encoding="utf-8")
trainer = (ROOT / "trainer.py").read_text(encoding="utf-8")


# The native planner consumes facts and owned native state, never a legacy strategy projection.
start = source.index("strategy::StrategicSharedContext strategic_context;")
end = source.index("const auto strategic_decision = strategic_planner.evaluate(", start)
planner_input = source[start:end]
for forbidden in (
    "StrategyInfo",
    "CompositionDirectionPolicy",
    "StrategyPolicy",
    "info.composition_direction",
    "info.composition_focus",
    "info.core_traits",
    "info.composition_locked",
    "info.core_unit_ids",
    "info.planned_unit_ids",
    "info.strategy",
):
    assert forbidden not in planner_input, f"legacy strategic input leaked: {forbidden}"

assert "StrategicEvidenceContext" in planner_header
assert "StrategicEvidenceContextBuilder" in source
assert "strategic_planner_commitments[i]" in source
assert "strategic_planner_commitments = {};" in source
assert "refresh_native_strategic_state" in source
assert "refresh_native_composition_candidates" in source

# Composition evaluation derives traits and item affinity from native owners and semantic profiles.
ci_start = source.index("// BEGIN ISOLATED NATIVE PLANNER BOUNDARY.")
ci_end = source.index("// Correlate strategic/economic context", ci_start)
composition_intelligence_input = source[ci_start:ci_end]
assert "info.core_traits" not in composition_intelligence_input
assert "strategic_context.current_core_traits" in composition_intelligence_input
assert "semantic_item_unit_profiles(i)" in composition_intelligence_input
assert "legacy_item_unit_profiles" not in source
assert "profile.preferred_traits = strategic_context.current_core_traits;" not in source

semantic_profile_start = source.index("std::vector<items::UnitProfile> semantic_item_unit_profiles")
semantic_profile_end = source.index("\n    const UnitInstance* item_target_unit", semantic_profile_start)
semantic_profile_source = source[semantic_profile_start:semantic_profile_end]
assert "composition_intelligence_players[player_index].active.current()" in semantic_profile_source
assert "target.core" in semantic_profile_source
assert "definition->traits" in semantic_profile_source
assert "preferred_traits" in semantic_profile_source
assert "items::UnitProfile{" in semantic_profile_source

# No legacy strategy DTO, policy, compatibility getter or projection remains in the native engine API.
for forbidden in (
    "StrategyInfo",
    "StrategyPolicy",
    "CompositionDirectionPolicy",
    "get_strategies",
    "get_viewer_strategy_snapshots",
    "update_legacy_strategy_compatibility_projection",
):
    for candidate in (source, engine_header, wrapper):
        assert forbidden not in candidate, f"legacy API remains: {forbidden}"

# Native owner contracts preserve match/player/sequence provenance without duplicating envelope identity.
assert "match_id" in context_header and "player_id" in context_header
assert "sequence" in context_header and "provenance" in context_header
assert "derived_core_unit_ids" not in context_header
assert "std::vector<std::int32_t> core_unit_ids" not in context_header
metadata_decl = evidence_header.split("struct EvidenceSourceMetadata", 1)[1].split("};", 1)[0]
for inherited in ("match_id", "player_id", "composition_id", "source_version"):
    assert inherited not in metadata_decl, f"duplicate evidence identity field: {inherited}"
assert '"match_id", e.match_id' not in diagnostics_header
assert '"composition_version", e.composition_version' not in diagnostics_header
assert '"match_id",metadata.match_id' not in bridge_header
assert '"timestamp_unix_ms",metadata.timestamp_unix_ms' not in bridge_header
bridge_metadata = bridge_header.split("struct ContextBridgeMetadata", 1)[1].split("};", 1)[0]
bridge_input = bridge_header.split("struct ContextBridgeInput", 1)[1].split("};", 1)[0]
for inherited in ("match_id", "player_id", "round", "timestamp_unix_ms", "sequence", "composition_id", "composition_version"):
    assert inherited not in bridge_metadata, f"duplicate context bridge envelope field: {inherited}"
for inherited in ("match_id", "timestamp_unix_ms", "sequence"):
    assert inherited not in bridge_input, f"unused context bridge input field: {inherited}"
assert "static PlannerEvidenceSnapshot combine(" not in evidence_header
assert "std::uint32_t schema_version{2}" in diagnostics_header
assert "std::uint64_t match_id{0}" in diagnostics_header
assert "std::int32_t player_id{-1}" in diagnostics_header
assert 'canonical.erase("timestamp_unix_ms")' in runtime_header
assert '{"match_id", match_id_}' not in runtime_header
assert '{"player_id", player_id_}' not in runtime_header
assert '{"round", round_}' not in runtime_header
assert '{"stage_sequence", ++next_stage_sequence_}' in runtime_header
assert "std::vector<std::int32_t> core_unit_ids;" not in planning_header

# The factual native strategic owner state is projected into semantic observations and PPO batches.
assert "AuditStrategicOwnerSnapshot strategic_state" in engine_header
assert 'strategic = player.get("strategic_state")' in wrapper
assert 'strategic = state.get("strategic_state")' in semantic
for field in (
    "active_composition_valid",
    "direction_valid",
    "pivot_candidate_valid",
    "unit_copy_progress",
    "opportunity_cost_available",
):
    assert field in semantic
assert "build_semantic_batch(" in trainer
assert "semantic_state=semantic_state" in trainer
assert "semantic_state=next_semantic_state" in trainer

print("native strategic evidence architecture checks passed")
