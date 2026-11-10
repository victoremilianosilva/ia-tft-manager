from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from scripts.validate_opgg_meta_catalog import validate_catalog


def fixture():
    now = datetime(2026, 10, 27, 12, tzinfo=timezone.utc)
    units = [
        {"apiName": "DA_18_Carry", "characterName": "DA_18_Carry", "name": "Carry"},
        {"apiName": "DA_18_Tank", "characterName": "DA_18_Tank", "name": "Tank"},
    ]
    meta = {
        "schema_version": 1,
        "source": "op.gg",
        "fetched_at": now.isoformat(),
        "compositions": [{
            "team_code": "abcTFTSet18",
            "units": [
                {"key": "DA_18_Carry", "items": ["DA_Deathblade"], "cell": {"x": 5, "y": 3}},
                {"key": "DA_18_Tank", "items": [], "cell": {"x": 1, "y": 0}},
            ],
            "early_game": {"units": [{"key": "DA_18_Carry"}]},
            "mid_game": {"units": [{"key": "DA_18_Tank"}]},
        }],
    }
    return meta, units, now


def test_accepts_fresh_catalog_with_matching_set_and_full_unit_coverage():
    meta, units, now = fixture()
    report = validate_catalog(meta, units, now=now)
    assert report["coverage"] == 1.0
    assert report["meta_set_ids"] == ["18"]
    assert report["unmapped_unit_keys"] == []


def test_rejects_catalog_from_another_set():
    meta, units, now = fixture()
    meta["compositions"][0]["team_code"] = "abcTFTSet17"
    with pytest.raises(ValueError, match="incompatível"):
        validate_catalog(meta, units, now=now)


def test_rejects_meta_when_item_catalog_set_id_differs():
    meta, units, now = fixture()
    with pytest.raises(ValueError, match="catálogo de itens"):
        validate_catalog(meta, units, items_doc={"set_id": "Set17"}, now=now)


def test_rejects_stale_catalog():
    meta, units, now = fixture()
    meta["fetched_at"] = (now - timedelta(days=10)).isoformat()
    with pytest.raises(ValueError, match="desatualizado"):
        validate_catalog(meta, units, now=now, max_age_hours=168)


def test_rejects_low_unit_coverage():
    meta, units, now = fixture()
    meta["compositions"][0]["units"].append({"key": "DA_18_Missing"})
    with pytest.raises(ValueError, match="Cobertura"):
        validate_catalog(meta, units, now=now, min_coverage=0.9)
