from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.generate_item_catalog import (  # noqa: E402
    build_catalog,
    default_catalog_output_path,
    item_effects_candidates,
    validate_catalog_semantics,
)


def source_fixture():
    return {
        "items": [
            {"apiName": "DA_Component_Sword", "name": "Sword", "tags": ["component"], "composition": [], "effects": {"AD": 0.1}},
            {"apiName": "DA_Component_Bow", "name": "Bow", "tags": ["component"], "composition": [], "effects": {"AS": 10}},
            {
                "apiName": "DA_Item_Consumable_Test",
                "name": "Test Consumable",
                "tags": ["Consumable"],
                "composition": ["DA_Component_Sword", "DA_Component_Bow"],
                "effects": {"AP": 999},
            },
            {
                "apiName": "DA_Item_Recipe_Using_Consumable",
                "name": "Invalid Recipe Using Consumable",
                "composition": ["DA_Item_Consumable_Test", "DA_Component_Sword"],
                "effects": {"AP": 999},
            },
            {
                "apiName": "DA_Item_TestBlade",
                "name": "Test Blade",
                "composition": ["DA_Component_Sword", "DA_Component_Bow"],
                "effects": {"AS": 10, "AP": 20, "CritChance": 35, "AD": 0.3, "ManaRegen": 3},
                "desc": "A test item",
                "icon": "test.tex",
            },
            {
                "apiName": "DA_Item_TestBlade_Alt",
                "name": "Test Blade Alt",
                "composition": ["DA_Component_Sword", "DA_Component_Sword"],
                "effects": {"Health": 150, "Armor": 20},
            },
            {
                "apiName": "TFT16_Augment_Test",
                "name": "Test Augment",
                "isAugment": True,
                "composition": ["DA_Component_Sword", "DA_Component_Bow"],
                "effects": {"AP": 99},
            },
            {
                "apiName": "TFT17_Item_Unrelated",
                "name": "Unrelated",
                "composition": ["DA_Component_Sword", "DA_Component_Bow"],
                "effects": {"AP": 99},
            },
        ],
        "setData": [
            {"number": 16, "name": "Set16", "items": ["DA_Component_Sword", "DA_Component_Bow", "DA_Item_TestBlade", "DA_Item_Consumable_Test", "DA_Item_Recipe_Using_Consumable"]},
            {"number": 16, "name": "Set16", "items": ["DA_Item_TestBlade_Alt", "TFT16_Augment_Test"]},
            {"number": 17, "name": "Set17", "items": ["TFT17_Item_Unrelated"]},
        ],
    }


def test_merges_same_set_entries_and_filters_recipes():
    catalog = build_catalog(source_fixture(), "16")
    assert catalog["set_id"] == "Set16"
    assert catalog["source_set_entries_merged"] == 2
    assert {item["id"] for item in catalog["items"]} == {
        "DA_Item_TestBlade",
        "DA_Item_TestBlade_Alt",
    }
    assert {component["id"] for component in catalog["components"]} == {
        "DA_Component_Sword",
        "DA_Component_Bow",
    }


def test_ignores_tft_item_aliases_even_when_they_have_valid_da_recipe():
    source = source_fixture()
    source["items"].extend([
        {
            "apiName": "TFT_Item_AliasBlade",
            "name": "TFT alias blade",
            "composition": ["DA_Component_Sword", "DA_Component_Bow"],
            "effects": {"AP": 500},
        },
        {
            "apiName": "TFT_Item_AliasComponent",
            "name": "TFT alias component",
            "tags": ["component"],
            "composition": [],
            "effects": {},
        },
    ])
    source["setData"][0]["items"].extend([
        "TFT_Item_AliasBlade",
        "TFT_Item_AliasComponent",
    ])
    catalog = build_catalog(source, "16")
    assert {item["id"] for item in catalog["items"]} == {
        "DA_Item_TestBlade",
        "DA_Item_TestBlade_Alt",
    }
    assert {component["id"] for component in catalog["components"]} == {
        "DA_Component_Sword",
        "DA_Component_Bow",
    }


def test_ignores_items_tagged_as_consumable_and_recipes_using_them():
    catalog = build_catalog(source_fixture(), "16")
    output_ids = {item["id"] for item in catalog["items"]}
    component_ids = {component["id"] for component in catalog["components"]}
    assert "DA_Item_Consumable_Test" not in output_ids
    assert "DA_Item_Recipe_Using_Consumable" not in output_ids
    assert "DA_Item_Consumable_Test" not in component_ids


def test_only_items_tagged_component_can_be_used_as_recipe_components():
    source = source_fixture()
    source["items"].append({
        "apiName": "DA_Item_NotAComponent",
        "name": "Not a component",
        "tags": ["Unique"],
        "composition": [],
        "effects": {},
    })
    source["items"].append({
        "apiName": "DA_Item_Recipe_With_NonComponent",
        "name": "Recipe with non-component",
        "composition": ["DA_Item_NotAComponent", "DA_Component_Sword"],
        "effects": {},
    })
    source["setData"][0]["items"].extend([
        "DA_Item_NotAComponent",
        "DA_Item_Recipe_With_NonComponent",
    ])

    catalog = build_catalog(source, "16")
    output_ids = {item["id"] for item in catalog["items"]}
    component_ids = {component["id"] for component in catalog["components"]}
    assert "DA_Item_Recipe_With_NonComponent" not in output_ids
    assert "DA_Item_NotAComponent" not in component_ids
    assert component_ids == {"DA_Component_Sword", "DA_Component_Bow"}


def test_normalizes_supported_stats_and_preserves_raw_effects():
    catalog = build_catalog(source_fixture(), "Set16")
    item = next(item for item in catalog["items"] if item["id"] == "DA_Item_TestBlade")
    assert item["stats"]["attack_speed"] == pytest.approx(0.1)
    assert item["stats"]["ability_power"] == 20
    assert item["stats"]["critical_strike_chance"] == pytest.approx(0.35)
    assert item["stats"]["attack_damage"] == 0
    assert item["source_effects"]["AD"] == pytest.approx(0.3)
    assert {
        "trigger": "combat_start",
        "operation": "add_stat",
        "stat": "attack_damage",
        "target": "self",
        "value": pytest.approx(0.3),
        "percent_of_stat": True,
    } in item["combat_effects"]
    assert item["source_description"] == "A test item"
    assert item["weights"]["carry"] == 1


def test_semantic_validation_accepts_active_repository_catalog():
    import json

    catalog_path = Path(__file__).resolve().parents[1] / "data" / "itens.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    validate_catalog_semantics(catalog)


def test_source_mana_regen_becomes_generic_combat_effect():
    catalog = build_catalog(source_fixture(), "16")
    item = next(item for item in catalog["items"] if item["id"] == "DA_Item_TestBlade")
    assert {
        "trigger": "combat_start",
        "operation": "mana_regen",
        "value": 3.0,
    } in item["combat_effects"]


def test_semantic_validation_rejects_structurally_valid_but_inert_catalog():
    catalog = {
        "items": [
            {"id": "Item_A", "stats": {key: 0.0 for key in (
                "attack_damage", "attack_speed", "ability_power",
                "critical_strike_chance", "critical_strike_damage", "health",
                "armor", "magic_resist", "mana", "omnivamp",
                "damage_amplification", "damage_reduction",
            )}, "combat_effects": [], "source_effects": {"PassiveDamage": 100}},
            {"id": "Item_B", "stats": {}, "combat_effects": [], "source_effects": {}},
        ]
    }
    with pytest.raises(ValueError, match="sem efeitos de combate aplicáveis"):
        validate_catalog_semantics(catalog)


def test_semantic_validation_accepts_normalized_stats_or_explicit_effects():
    catalog = {
        "items": [
            {"id": "Item_A", "stats": {"attack_speed": 0.1}, "combat_effects": []},
            {"id": "Item_B", "stats": {}, "combat_effects": [{"trigger": "COMBAT_START", "operation": "GRANT_SHIELD"}]},
        ]
    }
    validate_catalog_semantics(catalog)


def test_explicit_trait_metadata_can_add_non_craftable_items():
    catalog = build_catalog(
        source_fixture(),
        "16",
        {"DA_16_EmblemTest": {
            "grants_trait": "TestTrait",
            "granted_trait_active_count": 1,
            "combat_effects": [],
        }},
    )
    emblem = next(item for item in catalog["items"] if item["id"] == "DA_16_EmblemTest")
    assert emblem["recipe_components"] == []
    assert emblem["grants_trait"] == "TestTrait"
    assert emblem["weights"]["utility"] == 1.0


def test_canonical_set_identity_uses_number_when_source_name_is_stale():
    source = source_fixture()
    source["setData"] = [{
        "number": 18,
        "name": "Set10",
        "items": ["DA_Component_Sword", "DA_Component_Bow", "DA_Item_TestBlade", "DA_Item_TestBlade_Alt"],
    }]
    catalog = build_catalog(source, "18")
    assert catalog["set_id"] == "Set18"
    assert catalog["source_set_number"] == 18
    assert catalog["source_set_name"] == "Set10"


def test_rejects_unknown_set():
    with pytest.raises(ValueError, match="não encontrado"):
        build_catalog(source_fixture(), "99")


def test_rejects_duplicate_recipe_in_selected_set():
    source = source_fixture()
    source["items"].append({
        "apiName": "DA_Item_TestBlade_Second",
        "name": "Duplicate Recipe",
        "composition": ["DA_Component_Bow", "DA_Component_Sword"],
        "effects": {},
    })
    source["setData"][0]["items"].append("DA_Item_TestBlade_Second")
    with pytest.raises(ValueError, match="receitas duplicadas"):
        build_catalog(source, "16")


def test_rejects_more_than_engine_component_head_limit():
    source = source_fixture()
    for index in range(10):
        component_id = f"DA_Component_{index}"
        source["items"].append({
            "apiName": component_id,
            "name": component_id,
            "tags": ["component"],
            "composition": [],
            "effects": {},
        })
        recipe_id = f"DA_Item_Recipe_{index}"
        source["items"].append({
            "apiName": recipe_id,
            "name": recipe_id,
            "composition": [component_id, "DA_Component_Sword"],
            "effects": {},
        })
        source["setData"][0]["items"].extend([component_id, recipe_id])
    with pytest.raises(ValueError, match="no máximo 10"):
        build_catalog(source, "16")

def test_applies_set_specific_trait_item_metadata_without_overriding_source():
    metadata = {
        "DA_Item_TestBlade": {
            "grants_trait": "TFT17_TestTrait",
            "granted_trait_active_count": 1,
            "combat_effects": [{
                "trigger": "on_attack",
                "operation": "bonus_damage",
                "damage_type": "MAGIC",
                "value": 0.03,
                "percent_of_max_health": True,
            }],
            "name": "must not override source name",
            "stats": {"ability_power": 999},
        }
    }
    catalog = build_catalog(source_fixture(), "16", metadata)
    item = next(item for item in catalog["items"] if item["id"] == "DA_Item_TestBlade")
    assert item["grants_trait"] == "TFT17_TestTrait"
    assert item["combat_effects"][0]["operation"] == "bonus_damage"
    assert item["name"] == "Test Blade"
    assert item["stats"]["ability_power"] == 20



def test_set18_uses_generic_catalog_and_effects_filenames():
    assert str(default_catalog_output_path("18")).replace("\\", "/") == "data/itens.json"
    assert str(default_catalog_output_path("Set18")).replace("\\", "/") == "data/itens.json"
    assert [str(path).replace("\\", "/") for path in item_effects_candidates("18")] == ["data/item_effects.json"]
    assert [str(path).replace("\\", "/") for path in item_effects_candidates("Set18")] == ["data/item_effects.json"]


def test_other_sets_keep_set_specific_catalog_and_effects_filenames():
    assert str(default_catalog_output_path("Set17")).replace("\\", "/") == "data/item_catalog_set17.json"
    assert [str(path).replace("\\", "/") for path in item_effects_candidates("17")] == [
        "data/item_effects_17.json", "data/item_effects_set17.json"
    ]
