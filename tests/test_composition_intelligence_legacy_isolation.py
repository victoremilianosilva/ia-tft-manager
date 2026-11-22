"""Regression checks for native composition intelligence and legacy removal."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENGINE_SOURCE = ROOT / "cpp" / "src" / "lobby" / "TftEngine.cpp"


def test_native_composition_refresh_uses_live_engine_facts():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "refresh_native_composition_candidates" in source
    assert "NativeStrategicCompositionGenerator{}.generate(native_input)" in source
    assert "strategic_native_owned" in source
    assert "physical_star_counts_by_unit" in source
    assert "StrategyInfo" not in source
    assert "info.planned_unit_ids" not in source
    assert "info.core_unit_ids" not in source
    assert "copies_by_unit" not in source


def test_native_direction_and_composition_runtime_uses_owned_cycle_inputs():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "void refresh_native_strategic_runtime(" in source
    assert "strategic_shadow_runtimes[i]" in source
    assert "strategic_context_sequences[i] + 1" in source
    assert "strategic_native_owned" in source
    assert "native_runtime.refresh(native_audit_context, native_input)" in source
    assert "StrategicPlanner{}.evaluate(planner_context, planner_commitment)" in source
    assert "void refresh_native_strategic_state(std::size_t i)" in source


def test_retired_strategy_policies_are_physically_removed():
    assert not (ROOT / "cpp/include/strategy/StrategyPolicy.hpp").exists()
    assert not (ROOT / "cpp/include/strategy/CompositionDirectionPolicy.hpp").exists()
    assert not (ROOT / "cpp/tests/test_strategy_policy.cpp").exists()
    assert not (ROOT / "cpp/tests/test_composition_direction_policy.cpp").exists()
    cmake = (ROOT / "cpp/CMakeLists.txt").read_text(encoding="utf-8")
    assert "test_strategy_policy" not in cmake
    assert "test_composition_direction_policy" not in cmake


def test_retired_composition_planner_is_physically_removed():
    assert not (ROOT / "cpp/include/strategy/CompositionPlanner.hpp").exists()
    assert not (ROOT / "cpp/tests/test_composition_planner.cpp").exists()
    assert not (ROOT / "cpp/tests/test_composition_planner_opgg.cpp").exists()
    cmake = (ROOT / "cpp/CMakeLists.txt").read_text(encoding="utf-8")
    assert "test_composition_planner" not in cmake
    assert "composition_planner_opgg" not in cmake


def test_native_planning_does_not_read_legacy_strategy_contracts():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    header = (ROOT / "cpp/include/lobby/TftEngine.hpp").read_text(encoding="utf-8")
    binding = (ROOT / "cpp/bindings/tft_engine_bindings.cpp").read_text(encoding="utf-8")
    wrapper = (ROOT / "cpp_lobby_env.py").read_text(encoding="utf-8")
    forbidden = (
        "StrategyInfo",
        "StrategyPolicy",
        "CompositionDirectionPolicy",
        "select_economic_strategy",
        "update_legacy_strategy_compatibility_projection",
        "get_strategies",
        "get_viewer_strategy_snapshots",
        "get_strategy_snapshots",
        "void update_strategy(",
    )
    for candidate in (source, header, binding, wrapper):
        for token in forbidden:
            assert token not in candidate, f"legacy dependency remains: {token}"


def test_action_comparison_requires_nonempty_exact_candidate_identity():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "!strategic_context.action_candidates.empty()" in source
    assert "baseline_candidate.candidate_id != source.candidate_id" in source
    assert "contextual_candidate.candidate_id != source.candidate_id" in source


def test_native_runtime_is_the_only_composition_publisher():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    assert "native_strategic_runtime_owns_composition_publication" in source
    assert "UnifiedStrategicShadowRuntime" in source
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
    assert "if (pool)\n                        priority_evidence.pool_remaining = pool->available(champion_id);" in source
    assert "native_input.target_slots = std::clamp(std::max(8, economy.level), 1, 10)" in source


def test_lineup_and_upgrade_diagnostics_preserve_physical_evidence():
    priority = (ROOT / "cpp/include/composition_intelligence/UnitPriorityPlanner.hpp").read_text(encoding="utf-8")
    lineup = (ROOT / "cpp/include/composition_intelligence/LineupPlanner.hpp").read_text(encoding="utf-8")
    diagnostics = (ROOT / "cpp/include/composition_intelligence/CompositionDiagnostics.hpp").read_text(encoding="utf-8")
    assert "copies_by_star" in priority
    assert "copies_toward_next_star" in priority
    assert "copies_needed_for_next_star" in priority
    assert "affordable_shop_copies" in priority
    assert "pool_remaining" in priority
    assert "LineupTargetEntry" in lineup
    assert "availability" in lineup and "deferred_reason" in lineup
    assert '"target_states"' in diagnostics
    assert '"copies_by_star"' in diagnostics


if __name__ == "__main__":
    for name, test in sorted(globals().items()):
        if name.startswith("test_") and callable(test):
            test()
    print("native composition ownership and legacy removal checks passed")
