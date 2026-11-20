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
