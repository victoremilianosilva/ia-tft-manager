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
        "if (current_round >= 9 && !info.composition_direction.empty())", start
    )
    native_generation = source[start:end]
    assert "NativeStrategicCompositionGenerator{}.generate(native_input)" in native_generation
    assert "strategic_native_owned" in native_generation
    assert "StrategyInfo" not in native_generation
    assert "info." not in native_generation
    assert "copies_by_unit" not in native_generation

    # The native fact snapshot must exist before legacy economic and direction
    # generation, so its producer cannot depend on those derived values.
    legacy_economy = source.index("strategy::select_economic_strategy(strategy_context)")
    legacy_direction = source.index("Port of Python _update_comp_direction()")
    assert start < legacy_economy
    assert start < legacy_direction


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
        "refresh_native_strategic_runtime(\n            i, current_round, economy, strategic_native_owned"
    )
    native_generation = source.index(
        "NativeStrategicCompositionGenerator{}.generate(native_input)"
    )
    legacy_economy = source.index(
        "strategy::select_economic_strategy(strategy_context)"
    )
    legacy_direction = source.index("Port of Python _update_comp_direction()")
    assert native_generation < call < legacy_economy
    assert call < legacy_direction


def test_native_runtime_entrypoint_uses_only_native_cycle_inputs():
    source = ENGINE_SOURCE.read_text(encoding="utf-8")
    start = source.index("void refresh_native_strategic_runtime(")
    end = source.index("void update_strategy(std::size_t i)", start)
    runtime = source[start:end]
    forbidden = ("StrategyInfo", "strategy_snapshot", "copies_by_unit",
                 "StrategicSharedContext", "select_economic_strategy",
                 "composition_intelligence_enabled")
    found = [token for token in forbidden if token in runtime]
    assert not found, f"Native runtime entrypoint depends on legacy/optional state: {found}"
    assert "strategic_shadow_runtimes[i]" in runtime
    assert "strategic_context_sequences[i]" in runtime
    assert "strategic_native_owned" in runtime
    assert "native_runtime.refresh(native_audit_context, native_input)" in runtime
