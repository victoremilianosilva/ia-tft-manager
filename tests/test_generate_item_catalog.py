from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.generate_item_catalog import build_catalog  # noqa: E402


def source_fixture():
    return {
        "items": [
            {"apiName": "TFT_Item_Sword", "name": "Sword", "composition": [], "effects": {"AD": 0.1}},
            {"apiName": "TFT_Item_Bow", "name": "Bow", "composition": [], "effects": {"AS": 10}},
            {
                "apiName": "TFT_Item_TestBlade",
                "name": "Test Blade",
                "composition": ["TFT_Item_Sword", "TFT_Item_Bow"],
                "effects": {"AS": 10, "AP": 20, "CritChance": 35, "AD": 0.3},
                "desc": "A test item",
                "icon": "test.tex",
            },
            {
                "apiName": "TFT_Item_TestBlade_Alt",
                "name": "Test Blade Alt",
                "composition": ["TFT_Item_Sword", "TFT_Item_Sword"],
                "effects": {"Health": 150, "Armor": 20},
            },
            {
                "apiName": "TFT16_Augment_Test",
                "name": "Test Augment",
                "isAugment": True,
                "composition": ["TFT_Item_Sword", "TFT_Item_Bow"],
                "effects": {"AP": 99},
            },
            {
                "apiName": "TFT17_Item_Unrelated",
                "name": "Unrelated",
                "composition": ["TFT_Item_Sword", "TFT_Item_Bow"],
                "effects": {"AP": 99},
            },
        ],
        "setData": [
            {"number": 16, "name": "Set16", "items": ["TFT_Item_Sword", "TFT_Item_Bow", "TFT_Item_TestBlade"]},
            {"number": 16, "name": "Set16", "items": ["TFT_Item_TestBlade_Alt", "TFT16_Augment_Test"]},
            {"number": 17, "name": "Set17", "items": ["TFT17_Item_Unrelated"]},
        ],
    }


def test_merges_same_set_entries_and_filters_recipes():
    catalog = build_catalog(source_fixture(), "16")
    assert catalog["set_id"] == "Set16"
    assert catalog["source_set_entries_merged"] == 2
    assert {item["id"] for item in catalog["items"]} == {
        "TFT_Item_TestBlade",
        "TFT_Item_TestBlade_Alt",
    }
    assert {component["id"] for component in catalog["components"]} == {
        "TFT_Item_Sword",
        "TFT_Item_Bow",
    }


def test_normalizes_supported_stats_and_preserves_raw_effects():
    catalog = build_catalog(source_fixture(), "Set16")
    item = next(item for item in catalog["items"] if item["id"] == "TFT_Item_TestBlade")
    assert item["stats"]["attack_speed"] == pytest.approx(0.1)
    assert item["stats"]["ability_power"] == 20
    assert item["stats"]["critical_strike_chance"] == pytest.approx(0.35)
    assert item["stats"]["attack_damage"] == 0
    assert item["source_effects"]["AD"] == pytest.approx(0.3)
    assert item["source_description"] == "A test item"
    assert item["weights"]["carry"] == 1


def test_rejects_unknown_set():
    with pytest.raises(ValueError, match="não encontrado"):
        build_catalog(source_fixture(), "99")


def test_rejects_duplicate_recipe_in_selected_set():
    source = source_fixture()
    source["items"].append({
        "apiName": "TFT_Item_TestBlade_Second",
        "name": "Duplicate Recipe",
        "composition": ["TFT_Item_Bow", "TFT_Item_Sword"],
        "effects": {},
    })
    source["setData"][0]["items"].append("TFT_Item_TestBlade_Second")
    with pytest.raises(ValueError, match="receitas duplicadas"):
        build_catalog(source, "16")


def test_rejects_more_than_engine_component_head_limit():
    source = source_fixture()
    for index in range(10):
        component_id = f"TFT_Item_Component_{index}"
        source["items"].append({
            "apiName": component_id,
            "name": component_id,
            "composition": [],
            "effects": {},
        })
        recipe_id = f"TFT_Item_Recipe_{index}"
        source["items"].append({
            "apiName": recipe_id,
            "name": recipe_id,
            "composition": [component_id, "TFT_Item_Sword"],
            "effects": {},
        })
        source["setData"][0]["items"].extend([component_id, recipe_id])
    with pytest.raises(ValueError, match="no máximo 10"):
        build_catalog(source, "16")
