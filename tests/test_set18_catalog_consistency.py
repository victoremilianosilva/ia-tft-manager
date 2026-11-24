from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_set18_manifest_matches_active_catalogs():
    manifest = _read("data/set18_manifest.json")
    items = _read("data/itens.json")
    traits = _read("data/traits.json")
    combat_traits = _read("data/trait_combat_effects.json")

    assert manifest["set"] == 18
    assert manifest["name"] == "Set18"
    assert manifest["source"] == "CommunityDragon"
    assert items["set_id"] == traits.get("set_id", "Set18")
    assert combat_traits["set_id"] == "Set18"
    assert manifest["champions"] == len(_read("data/units_gerado.json"))
    assert manifest["traits"] == len(traits["traits"])


def test_every_active_set_trait_has_a_combat_coverage_disposition():
    source = _read("data/traits.json")["traits"]
    combat = _read("data/trait_combat_effects.json")["traits"]
    source_by_id = {trait["apiName"]: trait for trait in source}
    combat_by_id = {trait["api_name"]: trait for trait in combat}

    assert len(source_by_id) == len(source)
    assert len(combat_by_id) == len(combat)
    assert set(source_by_id) == set(combat_by_id)

    allowed_statuses = {"complete", "non_combat", "partial", "not_implemented"}
    for api_name, trait in combat_by_id.items():
        assert trait["coverage_status"] in allowed_statuses
        source_tiers = source_by_id[api_name]["effects"]
        normalized_tiers = trait["tiers"]
        assert [tier["min_units"] for tier in normalized_tiers] == sorted({
            (tier["minUnits"] if tier.get("minUnits") is not None else 1) for tier in source_tiers
        })
        if trait["coverage_status"] == "complete":
            assert trait["effects_complete"] is True
            assert normalized_tiers
            assert all(tier["effects"] for tier in normalized_tiers)
        elif trait["coverage_status"] == "non_combat":
            assert trait["effects_complete"] is True
            assert all(not tier["effects"] for tier in normalized_tiers)
        else:
            assert trait["effects_complete"] is False


def test_trait_unit_membership_is_explicit_and_fail_closed():
    traits = _read("data/traits.json")["traits"]
    units = _read("data/units_gerado.json")

    assert all(trait["unit_mapping_source"] == "data/units_gerado.json"
               for trait in traits)
    assert all(trait["unit_mapping_status"] == (
        "mapped" if trait["units"] else "unmapped_source_trait"
    ) for trait in traits)

    mapped = {unit_id for trait in traits for unit_id in trait["units"]}
    assert mapped == {unit["apiName"] for unit in units}
    assert [trait["apiName"] for trait in traits if not trait["units"]] == [
        "DA_18_Eclipse"
    ]
