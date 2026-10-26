from scripts.migrate_set_data import build_traits, build_units, item_catalog_filename, select_set


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
