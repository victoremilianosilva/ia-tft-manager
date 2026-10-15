"""Cross-language parity tests for CombatProfileManager role inference and input mapping."""
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

from combat.CombatProfileManager import CombatProfileManager, UnitRole


@pytest.fixture
def manager():
    return CombatProfileManager()


@pytest.mark.parametrize("unit, expected", [
    ({"apiName":"tank","max_hp":1500,"armor":60,"magic_resist":60,"attack_range":1}, UnitRole.TANK),
    ({"apiName":"carry","max_hp":400,"attack_damage":100,"attack_speed":1.0,"attack_range":4}, UnitRole.CARRY),
    ({"apiName":"assassin","max_hp":400,"attack_damage":30,"attack_speed":0.5,"attack_range":1,
      "ability":{"description":"Dash toward the backline and target the furthest enemy"}}, UnitRole.ASSASSIN),
    ({"apiName":"default","attack_range":0}, UnitRole.TANK if False else UnitRole.TANK),
    ({"apiName":"fighter","max_hp":750,"armor":35,"attack_range":1}, UnitRole.FIGHTER),
])
def test_role_inference_matches_cpp(manager, unit, expected):
    py_role = int(manager.get_role(unit))
    cpp_profile = cpp.combat_profile_get_profile(unit)
    assert cpp_profile["role"] == py_role
    assert cpp_profile["role_name"] == UnitRole(py_role).name.lower()


def test_profile_fields_and_front_back_flags_match(manager):
    units = [
        {"apiName":"u1","star":2,"hp":700,"max_hp":900,"mana":20,"max_mana":100,
         "attack_damage":80,"attack_speed":0.9,"armor":35,"magic_resist":25,"attack_range":3},
        {"apiName":"u2","ability":"Heals all allies and restores mana","hp":400,"max_hp":400},
        {"apiName":"u3","ability":{"name":"Protect allies with a shield"},"max_hp":1000},
    ]
    for unit in units:
        py_profile = manager.get_profile(unit)
        native = cpp.combat_profile_get_profile(unit)
        for key in ("role","role_name","frontline","backline","is_tank","is_carry","is_support","is_fighter","is_assassin",
                    "attack_range","attack_speed","attack_damage","armor","magic_resist","max_hp","max_mana"):
            assert native[key] == py_profile[key], (key, unit, native[key], py_profile[key])


def test_build_combat_input_matches_python(manager):
    units = [
        {"apiName":"CombatUnit","star":2,"hp":700,"max_hp":900,"mana":20,"max_mana":100,
         "attack_damage":80,"attack_speed":0.9,"armor":35,"magic_resist":25,"attack_range":3},
        {"id":123,"hp":"bad","max_hp":"bad","ad":61,"mr":17,"ability":{"effect":"Dash to the furthest enemy"}},
        {"characterName":"fallback","hp":500,"max_hp":600,"attack_damage":40,"attack_range":1},
    ]
    for unit in units:
        expected = manager.build_combat_input(unit)
        actual = cpp.combat_profile_build_combat_input(unit)
        assert actual == expected


def test_none_and_role_helpers_match():
    assert cpp.combat_profile_get_role(None) == int(UnitRole.FIGHTER)
    for role, unit in [
        (UnitRole.TANK, {"max_hp":1200,"armor":50}),
        (UnitRole.CARRY, {"attack_damage":100,"attack_speed":1,"attack_range":4}),
        (UnitRole.SUPPORT, {"ability":"Heals all allies"}),
        (UnitRole.FIGHTER, {"attack_range":1,"max_hp":800}),
        (UnitRole.ASSASSIN, {"ability":"Jump to the backline"}),
    ]:
        py = CombatProfileManager()
        assert cpp.combat_profile_get_role(unit) == int(py.get_role(unit))
        assert cpp.combat_profile_is_frontline(unit) == py.is_frontline(unit)
        assert cpp.combat_profile_is_backline(unit) == py.is_backline(unit)
