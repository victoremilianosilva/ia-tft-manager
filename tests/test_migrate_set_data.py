import json

from scripts.migrate_set_data import (
    build_traits,
    build_units,
    item_catalog_filename,
    load_item_effects_metadata,
    select_set,
)


def source_data():
    return {
        "setData": [{
            "number": 18,
            "name": "Enchanted Wilds",
            "traits": [{
                "apiName": "DA_18_Riftbeast",
                "name": "Riftbeast",
                "desc": "Trait description",
                "icon": "trait.tex",
                "effects": [{"minUnits": 2}],
            }],
            "champions": [
                {
                    "apiName": "DA_18_TestUnit",
                    "characterName": "DA_18_TestUnit",
                    "name": "Test Unit",
                    "cost": 2,
                    "icon": "champ.tex",
                    "squareIcon": "square.tex",
                    "tileIcon": "tile.tex",
                    "traits": ["DA_18_Riftbeast"],
                    "stats": {
                        "hp": 700, "damage": 45, "attackSpeed": 0.7,
                        "armor": 30, "magicResist": 30, "range": 1,
                        "mana": 100, "initialMana": 0,
                    },
                    "ability": {"name": "Test Spell", "desc": "Description", "variables": []},
                },
                {"apiName": "DA_18_TestSpawn", "name": "Test Spawn", "cost": 0,
                 "traits": ["DA_18_Riftbeast"]},
            ],
        }]
    }


def test_select_set_18_returns_matching_entries():
    name, entries = select_set(source_data(), 18)
    assert name == "Enchanted Wilds"
    assert len(entries) == 1


def test_build_units_normalizes_engine_contract_and_filters_non_shop_units():
    _, entries = select_set(source_data(), 18)
    units = build_units(entries)
    assert len(units) == 1
    unit = units[0]
    assert unit["apiName"] == "DA_18_TestUnit"
    assert unit["stats"]["max_hp"] == 700
    assert unit["stats"]["attack_damage"] == 45
    assert unit["stats"]["attack_range"] == 1
    assert unit["traits"] == ["Riftbeast"]
    assert unit["ability"]["name"] == "Test Spell"



def test_build_units_precomputes_complete_combat_profile_from_source():
    _, entries = select_set(source_data(), 18)
    unit = build_units(entries)[0]
    assert unit["role"] == 3
    assert unit["role_name"] == "fighter"
    assert unit["combat_profile"] == {
        "role": 3, "role_name": "fighter",
        "frontline": True, "backline": False,
        "is_tank": False, "is_carry": False, "is_support": False,
        "is_fighter": True, "is_assassin": False,
        "attack_range": 1.0, "attack_speed": 0.7,
        "attack_damage": 45.0, "armor": 30.0,
        "magic_resist": 30.0, "max_hp": 700.0, "max_mana": 100.0,
    }


def test_precomputed_role_matches_native_scoring_rules():
    from scripts.migrate_set_data import _infer_combat_role

    stats = {
        "attack_range": 4.0, "attack_speed": 0.9, "attack_damage": 80.0,
        "armor": 20.0, "magic_resist": 20.0, "max_hp": 700.0, "max_mana": 100.0,
    }
    assert _infer_combat_role("Rapid fire projectile attack damage", stats) == (1, "carry")
    tank = dict(stats, attack_range=1.0, attack_speed=0.5, attack_damage=40.0,
                armor=60.0, magic_resist=60.0, max_hp=1200.0)
    assert _infer_combat_role("Taunt and damage reduction", tank) == (0, "tank")
    support = dict(stats, attack_range=2.0, attack_speed=0.5, attack_damage=40.0,
                   armor=20.0, magic_resist=20.0, max_hp=700.0)
    assert _infer_combat_role("Heal allies and grant mana", support) == (2, "support")
    assassin = dict(stats, attack_range=1.0, attack_speed=0.5, attack_damage=40.0,
                    armor=20.0, magic_resist=20.0, max_hp=700.0)
    assert _infer_combat_role("Dash to the furthest enemy", assassin) == (4, "assassin")


def test_empty_profile_uses_fighter_as_neutral_fallback():
    from scripts.migrate_set_data import _infer_combat_role
    empty = {key: 0.0 for key in (
        "attack_range", "attack_speed", "attack_damage", "armor",
        "magic_resist", "max_hp", "max_mana",
    )}
    assert _infer_combat_role("", empty) == (3, "fighter")


def test_build_traits_references_units_by_canonical_api_name():
    _, entries = select_set(source_data(), 18)
    units = build_units(entries)
    traits = build_traits(entries, units)["traits"]
    assert len(traits) == 1
    assert traits[0]["apiName"] == "DA_18_Riftbeast"
    assert traits[0]["units"] == [{"unit": "DA_18_TestUnit", "unit_cost": 2}]



def test_set18_migration_uses_generic_item_catalog_filename():
    assert item_catalog_filename(18) == "itens.json"
    assert item_catalog_filename(17) == "item_catalog_set17.json"



def test_load_item_effects_metadata_reads_set18_trait_overrides(tmp_path):
    path = tmp_path / "item_effects.json"
    path.write_text(
        json.dumps({
            "schema_version": 1,
            "set_id": "Set18",
            "items": {
                "DA_18_EmblemBlackthorn": {
                    "grants_trait": "DA_18_Blackthorn",
                    "granted_trait_active_count": 1,
                    "combat_effects": [],
                },
                "invalid": None,
            },
        }),
        encoding="utf-8",
    )
    metadata = load_item_effects_metadata(path)
    assert metadata == {
        "DA_18_EmblemBlackthorn": {
            "grants_trait": "DA_18_Blackthorn",
            "granted_trait_active_count": 1,
            "combat_effects": [],
        }
    }


def test_load_item_effects_metadata_missing_file_returns_empty(tmp_path):
    assert load_item_effects_metadata(tmp_path / "missing.json") == {}
