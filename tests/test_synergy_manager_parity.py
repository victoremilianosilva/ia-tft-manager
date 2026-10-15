"""Direct Python/C++ parity tests for SynergyManager's bonus formulas."""
from __future__ import annotations
import os
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
for module_dir in (ROOT / "cpp" / "build" / "bin", ROOT / "cpp" / "build" / "bin" / "Release"):
    if module_dir.exists():
        sys.path.insert(0, str(module_dir))
if os.environ.get("REQUIRE_CPP_PARITY") == "1":
    import tft_engine as cpp
else:
    pytest.importorskip("tft_engine")
    import tft_engine as cpp

from SynergyManager import SynergyManager


@pytest.fixture
def pair(tmp_path):
    import json
    traits = [
        {"name": "Mage", "effects": [{"minUnits": 2}, {"minUnits": 4}, {"minUnits": 6}]},
        {"name": "Tank", "effects": [{"minUnits": 2}, {"minUnits": 5}]},
        {"name": "Support", "effects": [{"minUnits": 3}]},
    ]
    path = tmp_path / "traits.json"
    path.write_text(json.dumps({"traits": traits}), encoding="utf-8")
    py = SynergyManager(str(path))
    native = cpp.SynergyManagerNative({"Mage": [2, 4, 6], "Tank": [2, 5], "Support": [3]})
    return py, native


@pytest.mark.parametrize("active", [
    {},
    {"Mage": 1},
    {"Mage": 2},
    {"Mage": 4, "Tank": 2},
    {"Mage": 6, "Tank": 5, "Support": 3},
    {"Unknown": 99, "Mage": -1},
])
def test_global_and_individual_multipliers_match(pair, active):
    py, native = pair
    py.set_state if hasattr(py, "set_state") else None
    py.active_traits = dict(active)
    assert native.calculate_multiplier(active) == pytest.approx(py.calculate_multiplier(active), abs=1e-10)
    assert native.get_all_multipliers(active) == pytest.approx(py.get_all_multipliers(active), abs=1e-10)


@pytest.mark.parametrize("trait,count", [
    ("Mage", -1), ("Mage", 0), ("Mage", 1), ("Mage", 2), ("Mage", 4), ("Mage", 6), ("Unknown", 99)
])
def test_trait_level_matches(pair, trait, count):
    py, native = pair
    assert native.get_trait_level(trait, count) == py.get_trait_level(trait, count)


@pytest.mark.parametrize("active,partial,traits,focus", [
    ({}, {}, ["Mage"], None),
    ({"Mage": 2}, {}, ["Mage"], None),
    ({}, {"Mage": 1}, ["Mage"], None),
    ({"Mage": 4, "Tank": 2}, {}, ["Mage", "Tank"], None),
    ({}, {}, ["Unknown"], None),
    ({"Mage": 2}, {}, ["Mage"], {"Mage": 3}),
    ({"Mage": 2}, {}, ["Mage", "Tank"], {"Mage": 1}),
    ({}, {"Mage": 1}, ["Mage", "Unknown"], {"Unknown": 4}),
])
def test_unit_synergy_bonus_matches(pair, active, partial, traits, focus):
    py, native = pair
    py.active_traits = dict(active)
    py.partial_traits = dict(partial)
    native.set_state(active, partial)
    assert native.get_unit_synergy_bonus(traits, focus or {}) == pytest.approx(
        py.get_unit_synergy_bonus({"traits": traits}, focus), abs=1e-10
    )


def test_empty_unit_and_focus_edge_cases(pair):
    py, native = pair
    assert native.get_unit_synergy_bonus([]) == pytest.approx(py.get_unit_synergy_bonus({"traits": []}))
    assert native.get_unit_synergy_bonus(["Mage"], {}) == pytest.approx(
        py.get_unit_synergy_bonus({"traits": ["Mage"]}, {})
    )
