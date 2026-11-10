"""Testa os perfis de combate diretamente pelo binding C++ nativo."""
from __future__ import annotations

import os
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
for module_dir in (ROOT / "cpp" / "build" / "bin", ROOT / "cpp" / "build" / "bin" / "Release"):
    if module_dir.exists() and str(module_dir) not in sys.path:
        sys.path.insert(0, str(module_dir))

if os.environ.get("REQUIRE_CPP_ENGINE") == "1":
    import tft_engine as cpp
else:
    pytest.importorskip("tft_engine", reason="Compile cpp target tft_engine before native combat-profile tests")
    import tft_engine as cpp


@pytest.mark.parametrize(("unit", "expected_role"), [
    ({"apiName": "tank", "max_hp": 1500, "armor": 60, "magic_resist": 60, "attack_range": 1}, 0),
    ({"apiName": "carry", "max_hp": 400, "attack_damage": 100, "attack_speed": 1.0, "attack_range": 4}, 1),
    ({"apiName": "assassin", "max_hp": 400, "attack_damage": 30, "attack_speed": 0.5, "attack_range": 1,
      "ability": {"description": "Dash toward the backline and target the furthest enemy"}}, 4),
    ({"apiName": "fighter", "attack_range": 1, "max_hp": 750, "armor": 35}, 3),
])
def test_cpp_infers_combat_role_from_unit(unit, expected_role):
    profile = cpp.combat_profile_get_profile(unit)

    assert profile["role"] == expected_role
    assert profile["role_name"] == ("tank", "carry", "support", "fighter", "assassin")[expected_role]
    assert profile[f"is_{profile['role_name']}"] is True


def test_cpp_profile_contains_combat_stats_and_positioning_flags():
    unit = {
        "apiName": "BackCarry",
        "star": 2,
        "hp": 700,
        "max_hp": 900,
        "mana": 20,
        "max_mana": 100,
        "attack_damage": 80,
        "attack_speed": 0.9,
        "armor": 35,
        "magic_resist": 25,
        "attack_range": 3,
    }

    profile = cpp.combat_profile_get_profile(unit)
    required = {
        "role", "role_name", "frontline", "backline", "is_tank", "is_carry",
        "is_support", "is_fighter", "is_assassin", "attack_range",
        "attack_speed", "attack_damage", "armor", "magic_resist", "max_hp", "max_mana",
    }
    assert required.issubset(profile)
    assert profile["attack_range"] == 3
    assert profile["attack_speed"] == pytest.approx(0.9)
    assert profile["attack_damage"] == 80
    assert profile["armor"] == 35
    assert profile["magic_resist"] == 25
    assert profile["max_hp"] == 900
    assert profile["max_mana"] == 100
    assert isinstance(profile["frontline"], bool)
    assert isinstance(profile["backline"], bool)
    assert profile["backline"] is True
    assert profile["frontline"] is False


def test_ambiguous_profile_defaults_to_fighter_not_tank():
    # Missing ability/stats used to tie every score at zero and select role 0
    # (tank) solely because the inference loop started at the first enum value.
    profile = cpp.combat_profile_get_profile({})
    assert profile["role"] == 3
    assert profile["role_name"] == "fighter"
    assert profile["is_tank"] is False
    assert profile["is_fighter"] is True


def test_cpp_role_helpers_have_defined_none_behavior():
    assert cpp.combat_profile_get_role(None) == 3
    assert cpp.combat_profile_is_frontline(None) is True
    assert cpp.combat_profile_is_backline(None) is False


def test_cpp_builds_combat_input_from_unit_stats():
    unit = {
        "apiName": "CombatUnit", "star": 2, "hp": 700, "max_hp": 900,
        "mana": 20, "max_mana": 100, "attack_damage": 80,
        "attack_speed": 0.9, "armor": 35, "magic_resist": 25, "attack_range": 3,
    }

    combat_input = cpp.combat_profile_build_combat_input(unit)

    assert combat_input["id"] == "CombatUnit"
    assert combat_input["star"] == 2
    assert combat_input["hp"] == 700
    assert combat_input["max_hp"] == 900
    assert combat_input["mana"] == 20
    assert combat_input["max_mana"] == 100
    assert combat_input["attack_damage"] == 80
    assert combat_input["attack_speed"] == pytest.approx(0.9)
    assert combat_input["armor"] == 35
    assert combat_input["magic_resist"] == 25
    assert combat_input["attack_range"] == 3
    assert combat_input["role"] == cpp.combat_profile_get_role(unit)


def test_cpp_combat_input_supports_identifier_fallbacks():
    unit = {"id": 123, "hp": 450, "max_hp": 600, "ad": 61, "mr": 17,
            "ability": {"effect": "Dash to the furthest enemy"}}
    combat_input = cpp.combat_profile_build_combat_input(unit)

    assert combat_input["id"] == 123
    assert combat_input["hp"] == 450
    assert combat_input["max_hp"] == 600
    assert combat_input["attack_damage"] == 61
    assert combat_input["magic_resist"] == 17



@pytest.mark.parametrize(("unit", "expected_role"), [
    (
        {"apiName": "Bruiser", "max_hp": 900, "attack_damage": 60,
         "attack_speed": 0.75, "armor": 35, "magic_resist": 35,
         "attack_range": 1,
         "ability": {"description": "Deal physical damage to the target"}},
        3,
    ),
    (
        {"apiName": "CarryDamageText", "max_hp": 650, "attack_damage": 85,
         "attack_speed": 0.9, "armor": 25, "magic_resist": 25,
         "attack_range": 4,
         "ability": {"description": "Deal physical damage to the target"}},
        1,
    ),
])
def test_generic_damage_text_does_not_override_combat_stats(unit, expected_role):
    profile = cpp.combat_profile_get_profile(unit)

    assert profile["role"] == expected_role
    assert profile["is_tank"] is False
