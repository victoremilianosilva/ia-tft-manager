"""Regression guard for the native Composition Intelligence Shadow boundary."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENGINE_SOURCE = ROOT / "cpp" / "src" / "lobby" / "TftEngine.cpp"


def _shadow_block() -> str:
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    start_marker = "// BEGIN SHADOW-ONLY EVALUATION BOUNDARY."
    end_marker = "// END SHADOW-ONLY EVALUATION BOUNDARY."
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    return source[start:end]


def test_composition_intelligence_shadow_does_not_read_legacy_strategy_info():
    block = _shadow_block()
    forbidden = (
        "StrategyInfo",
        "strategy_snapshot",
        "info.core_traits",
        "info.planned_units",
        "info.planned_traits",
        "info.composition_direction",
        "legacy_item_unit_profiles",
        "CompositionDirectionPolicy",
        "copies_by_unit",
    )
    found = [token for token in forbidden if token in block]
    assert not found, (
        "Composition Intelligence Shadow must not read legacy strategy state: "
        f"{found}"
    )


def test_native_composition_evidence_is_built_before_legacy_strategy():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    start = source.index(
        "// Native strategic evidence is generated directly from live engine facts"
    )
    end = source.index(
        "strategy::select_economic_strategy(strategy_context)", start
    )
    native_generation = source[start:end]
    assert "NativeStrategicCompositionGenerator{}.generate(native_input)" in native_generation
    assert "strategic_native_owned" in native_generation
    assert "StrategyInfo" not in native_generation
    assert "info.planned_unit_ids" not in native_generation
    assert "info.core_unit_ids" not in native_generation
    assert "copies_by_unit" not in native_generation

    # Native generation precedes the remaining economic compatibility policy.
    legacy_economy = source.index("strategy::select_economic_strategy(strategy_context)")
    assert start < legacy_economy


def test_shadow_core_and_item_fit_use_native_strategic_sources():
    block = _shadow_block()
    assert "strategic_native_generation" in block
    assert "strategic_context.current_core_traits" in block
    assert "profile.preferred_traits = strategic_context.current_core_traits" in block
    assert "candidate.is_core = active_native_direction" in block


def test_item_profiles_use_only_the_new_active_composition():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    start = source.index("std::vector<items::UnitProfile> semantic_item_unit_profiles")
    end = source.index("const UnitInstance* item_target_unit", start)
    profile_builder = source[start:end]
    forbidden = ("StrategyInfo", "planned_main_carry_id", "core_traits", "planned_traits",
                 "composition_direction", "legacy_item_unit_profiles")
    found = [token for token in forbidden if token in profile_builder]
    assert not found, f"item profile builder leaked legacy strategy data: {found}"
    assert "composition_intelligence_players[player_index].active.current()" in profile_builder
    assert "target.core" in profile_builder
    assert "definition->traits" in profile_builder
    assert "preferred_traits" in profile_builder


def test_action_comparison_requires_nonempty_exact_candidate_identity():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "!strategic_context.action_candidates.empty()" in source
    assert "baseline_candidate.candidate_id != source.candidate_id" in source
    assert "contextual_candidate.candidate_id != source.candidate_id" in source


def test_native_runtime_refresh_precedes_legacy_strategy_generation():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    call = source.index(
        "refresh_native_strategic_runtime(\n            i, current_round, economy, player_envs[i].info"
    )
    native_generation = source.index(
        "NativeStrategicCompositionGenerator{}.generate(native_input)"
    )
    legacy_economy = source.index(
        "strategy::select_economic_strategy(strategy_context)"
    )
    assert native_generation < call < legacy_economy


def test_native_runtime_entrypoint_uses_only_native_cycle_inputs():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    start = source.index("void refresh_native_strategic_runtime(")
    end = source.index("void update_strategy(std::size_t i)", start)
    runtime = source[start:end]
    forbidden = ("StrategyInfo", "strategy_snapshot", "copies_by_unit",
                 "select_economic_strategy",
                 "composition_intelligence_enabled")
    found = [token for token in forbidden if token in runtime]
    assert not found, f"Native runtime entrypoint depends on legacy/optional state: {found}"
    assert "strategic_shadow_runtimes[i]" in runtime
    assert "strategic_context_sequences[i] + 1" in runtime
    assert "strategic_native_owned" in runtime
    assert "StrategicPlanner{}.evaluate(planner_context, planner_commitment)" in runtime
    assert "native_runtime.refresh(native_audit_context, native_input)" in runtime

def test_native_runtime_is_the_only_composition_publisher():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    start = source.index("// New Composition Intelligence pipeline:")
    end = source.index(
        "static const std::array<const char*, 7> economic_posture_names", start
    )
    optional_pipeline = source[start:end]
    assert "publish_if_approved" not in optional_pipeline
    assert "native_strategic_runtime_owns_composition_publication" in optional_pipeline

def test_legacy_composition_generation_is_removed_from_engine():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "CompositionPlanner::build" not in source
    assert "strategy/CompositionPlanner.hpp" not in source
    assert "CompositionDirectionPolicy.hpp" not in source
    assert "should_replace_composition_plan" not in source
    assert "Port of Python _update_comp_direction()" not in source
    # StrategyInfo fields are compatibility projections only; no consumer
    # searches or branches on the legacy planned-unit vectors.
    assert "std::find(info.planned_unit_ids.begin()" not in source
    assert "std::find(strategy_before.planned_unit_ids.begin()" not in source
    assert "std::find(current_strategy.planned_unit_ids.begin()" not in source
    assert "composition_intelligence_players[i].active.current()" in source


def test_native_priority_and_lineup_outputs_are_version_bound_and_reused():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "ci::UnitPriorityPlanner{}.resolve(active, priority_context)" in source
    assert "ci::LineupPlanner{}.plan(active, priorities, lineup_context)" in source
    assert "runtime.unit_priorities = priorities" in source
    assert "runtime.lineup = lineup" in source
    assert "runtime.planner_outputs_valid" in source
    assert "priority_evidence.pool_remaining = pool->available(champion_id)" in source
    assert "priority_evidence.copies_in_shop" in source
    assert "native_input.target_slots = std::clamp(std::max(8, economy.level), 1, 10)" in source


def test_lineup_and_upgrade_diagnostics_preserve_physical_evidence():
    priority = (ROOT / "cpp" / "include" / "composition_intelligence" /
                "UnitPriorityPlanner.hpp").read_text(encoding="utf-8")
    lineup = (ROOT / "cpp" / "include" / "composition_intelligence" /
              "LineupPlanner.hpp").read_text(encoding="utf-8")
    diagnostics = (ROOT / "cpp" / "include" / "composition_intelligence" /
                   "CompositionDiagnostics.hpp").read_text(encoding="utf-8")
    assert "copies_by_star" in priority
    assert "copies_toward_next_star" in priority
    assert "copies_needed_for_next_star" in priority
    assert "affordable_shop_copies" in priority
    assert "pool_remaining" in priority
    assert "LineupTargetEntry" in lineup
    assert "availability" in lineup and "deferred_reason" in lineup
    assert "lineup_target_states" in diagnostics
    assert '"copies_by_star"' in diagnostics

