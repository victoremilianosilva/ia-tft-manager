from __future__ import annotations

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "update_opgg_meta_catalog.py"
SPEC = importlib.util.spec_from_file_location("opgg_meta_catalog", SCRIPT)
assert SPEC and SPEC.loader
opgg = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(opgg)


def sample_payload():
    return {
        "metadata": {"gameStatCounts": 250000, "gameStatDateTime": "2026-10-27T00:59:33.000Z"},
        "data": [{
            "id": "deck-1",
            "name": {"pt_BR": "Composição de teste", "en_US": "Test composition"},
            "cost": 8,
            "teamCode": "abc",
            "units": [
                {"key": "TFT_Test_Carry", "items": ["Item_A"], "tier": 4,
                 "cell": {"x": 5, "y": 3}, "isCore": True, "priority": 1},
                {"key": "TFT_Test_Tank", "items": [], "tier": 2,
                 "cell": {"x": 2, "y": 0}, "isCore": False, "priority": 2},
            ],
            "traits": [{"key": "TestTrait", "style": 2, "numUnits": 4}],
            "stat": {
                "deck": {"totalCount": 2000, "avgPlacement": 3.1, "top4Rate": 0.72},
                "label": {"totalCount": 500, "avgPlacement": 3.5, "top4Rate": 0.65},
            },
            "early": {
                "level": 5,
                "units": [{"characterId": "TFT_Test_Tank", "items": [], "tier": 2,
                           "cell": {"x": 1, "y": 0}}],
                "traits": [{"key": "TestTrait", "style": 1, "numUnits": 2}],
                "play": 10, "win": 6, "lose": 4,
            },
            "middle": {
                "level": 7,
                "units": [{"characterId": "TFT_Test_Carry", "items": ["Item_A"], "tier": 4,
                           "cell": {"x": 5, "y": 3}}],
                "traits": [], "play": 10, "win": 7, "lose": 3,
            },
        }],
    }


def test_normalize_preserves_final_and_stage_units():
    result = opgg.normalize_payload(sample_payload())
    assert result["schema_version"] == 1
    assert result["source"] == "op.gg"
    assert len(result["compositions"]) == 1
    comp = result["compositions"][0]
    assert comp["name"] == "Composição de teste"
    assert comp["units"][0]["key"] == "TFT_Test_Carry"
    assert comp["units"][0]["is_core"] is True
    assert comp["early_game"]["level"] == 5
    assert comp["early_game"]["units"][0]["key"] == "TFT_Test_Tank"
    assert comp["mid_game"]["level"] == 7
    assert comp["mid_game"]["units"][0]["key"] == "TFT_Test_Carry"
    assert comp["statistics"]["deck"]["totalCount"] == 2000


def test_normalize_rejects_payload_without_compositions():
    try:
        opgg.normalize_payload({"metadata": {}, "data": []})
    except ValueError as exc:
        assert "nenhuma composição" in str(exc)
    else:
        raise AssertionError("Payload sem comps deveria falhar")


def test_unit_without_key_is_ignored():
    result = opgg.normalize_payload({
        "data": [{"id": "deck-1", "units": [{"items": [], "cell": {}}],
                  "early": {}, "middle": {}}],
    })
    assert result["compositions"][0]["units"] == []
