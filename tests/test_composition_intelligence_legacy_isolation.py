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
