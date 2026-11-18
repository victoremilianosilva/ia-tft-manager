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

# Composition Intelligence must derive synergy/item affinity from the native
# StrategicSharedContext, never from legacy StrategyInfo core traits.
ci_start = source.index("// New Composition Intelligence pipeline")
ci_end = source.index("// Correlate strategic/economic context", ci_start)
composition_intelligence_input = source[ci_start:ci_end]
assert "info.core_traits" not in composition_intelligence_input
assert "strategic_context.current_core_traits" in composition_intelligence_input
assert "profile.preferred_traits = strategic_context.current_core_traits;" in composition_intelligence_input
assert "match_id" in context_header and "player_id" in context_header
assert "sequence" in context_header and "provenance" in context_header
assert "derived_core_unit_ids" not in context_header
assert "std::vector<std::int32_t> core_unit_ids" not in context_header

# The remaining item profile helper is explicitly isolated as legacy PPO/reward
# compatibility. New Composition Intelligence item evidence is sourced from the
# native StrategicSharedContext in the dedicated pipeline below.
legacy_profiles_start = source.index("legacy_item_unit_profiles")
legacy_profiles_end = source.index("const UnitInstance* item_target_unit", legacy_profiles_start)
legacy_profiles_source = source[legacy_profiles_start:legacy_profiles_end]
assert "player.strategy" in legacy_profiles_source
assert "unit_composition_score" in legacy_profiles_source
assert "legacy_item_unit_profiles(i)" in source
assert "lobby.legacy_item_unit_profiles(player_id)" in source
assert "profile.preferred_traits = strategic_context.current_core_traits;" in source

# Viewer-facing legacy shape is now a one-way projection from canonical owners.
viewer_projection_start = source.index("TFTEngine::get_strategies() const")
viewer_projection_end = source.index("RewardState TFTEngine::get_reward_state", viewer_projection_start)
viewer_projection_source = source[viewer_projection_start:viewer_projection_end]
assert "strategic_planner_commitments[i]" in viewer_projection_source
assert "composition_intelligence_players[i].active.current()" in viewer_projection_source
assert "composition_projection_source = \"tft_strategic_engine\"" in viewer_projection_source
assert "canonical_active_composition" in viewer_projection_source
assert "native_composition_unavailable" in viewer_projection_source
assert "unit_composition_score" not in item_profiles_source

evidence_header = Path("cpp/include/composition_intelligence/PlannerEvidenceAdapters.hpp").read_text(encoding="utf-8")
diagnostics_header = Path("cpp/include/composition_intelligence/CompositionDiagnostics.hpp").read_text(encoding="utf-8")
runtime_header = Path("cpp/include/composition_intelligence/CompositionIntelligenceRuntime.hpp").read_text(encoding="utf-8")
bridge_header = Path("cpp/include/composition_intelligence/StrategicContextBridge.hpp").read_text(encoding="utf-8")

# Snapshot identity/version is owned once; source metadata carries source-local freshness only.
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

# Runtime envelope owns match/player/round; stage rows retain only stage-local identity.
assert '{"match_id", match_id_}' not in runtime_header
assert '{"player_id", player_id_}' not in runtime_header
assert '{"round", round_}' not in runtime_header
assert '{"stage_sequence", ++next_stage_sequence_}' in runtime_header

# The new contract must not even name the old strategic source types.
for forbidden in ("StrategyInfo", "CompositionDirectionPolicy", "CompositionPlanner"):
    assert forbidden not in context_header, f"legacy type dependency: {forbidden}"

print("strategic evidence context architecture checks passed")

planning_header = Path("cpp/include/strategy/StrategicPlanning.hpp").read_text(encoding="utf-8")
assert "std::vector<std::int32_t> core_unit_ids;" not in planning_header
