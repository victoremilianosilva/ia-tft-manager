from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_trait_catalog import build_trait_catalog


def test_active_set_trait_catalog_maps_all_roster_memberships():
    traits = json.loads((ROOT / "data" / "traits.json").read_text(encoding="utf-8"))
    units = json.loads((ROOT / "data" / "units_gerado.json").read_text(encoding="utf-8"))

    generated = build_trait_catalog(traits, units)
    by_id = {trait["apiName"]: trait for trait in generated["traits"]}

    assert len(by_id) == 36
    assert sum(len(trait["units"]) for trait in generated["traits"]) == sum(
        len(unit.get("traits", [])) for unit in units
    )
    assert all(trait["unit_mapping_source"] == "data/units_gerado.json"
               for trait in generated["traits"])
    assert all(trait["unit_mapping_status"] == (
        "mapped" if trait["units"] else "unmapped_source_trait"
    ) for trait in generated["traits"])

    mapped_units = {
        unit_id
        for trait in generated["traits"]
        for unit_id in trait["units"]
    }
    assert mapped_units == {unit["apiName"] for unit in units}


def test_only_eclipse_is_unmapped_in_current_set18_roster():
    traits = json.loads((ROOT / "data" / "traits.json").read_text(encoding="utf-8"))
    units = json.loads((ROOT / "data" / "units_gerado.json").read_text(encoding="utf-8"))

    generated = build_trait_catalog(traits, units)
    unmapped = [
        trait["apiName"] for trait in generated["traits"]
        if not trait["units"]
    ]

    assert unmapped == ["DA_18_Eclipse"]


def test_unknown_unit_trait_fails_closed():
    traits = {"traits": [{"apiName": "trait_a", "name": "Trait A", "en_name": "Trait A"}]}
    units = [{"apiName": "unit_a", "traits": ["Trait B"]}]

    try:
        build_trait_catalog(traits, units)
    except ValueError as error:
        assert "unknown trait" in str(error)
    else:
        raise AssertionError("Unknown unit trait must not be silently discarded")
