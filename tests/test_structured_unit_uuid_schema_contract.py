import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "spec" / "observation-schema.v2.draft.json"
MANIFEST_PATH = ROOT / "spec" / "observation-structured-entity-temporal-contract.v1.draft.json"
COVERAGE_PATH = ROOT / "spec" / "observation-structured-entity-producer-coverage.v1.draft.csv"


def test_structured_unit_identity_uses_native_uuid_and_composite_scope():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    unit = schema["$defs"]["unit"]
    assert "uuid" in unit["required"]
    assert "uuid" in unit["properties"]
    assert "instance_id" not in unit["required"]
    assert "instance_id" not in unit["properties"]
    assert "identity.engine_match_id" in unit["properties"]["uuid"]["description"]

    role = schema["properties"]["derived_context"]["properties"]["unit_roles"]["items"]
    assert "uuid" in role["required"]
    assert "uuid" in role["properties"]
    assert "instance_id" not in role["properties"]


def test_unit_identity_manifest_matches_native_engine_episode_scope():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    unit = next(entity for entity in manifest["entities"] if entity["kind"] == "unit_instance")
    assert unit["identity_status"] == "native_observed_scoped_adapter_pending"
    assert unit["scope"] == ["engine_match_id"]
    assert "UnitInstance::uuid" in unit["native_identity_candidate"]
    assert "engine_instance_id + episode_id" in unit["native_identity_candidate"]
    assert "player_id is the current owner relation" in unit["identity"]
    gaps = " ".join(unit["gaps"])
    assert "Raw UUID is not globally unique" in gaps
    assert "joins must include the canonical Engine-episode scope" in gaps
    assert "player_id is ownership metadata, not physical identity" in gaps

    coverage = COVERAGE_PATH.read_text(encoding="utf-8")
    assert "entities.board[].unit.uuid" in coverage
    assert "entities.bench[].unit.uuid" in coverage
    assert "entities.board[].unit.instance_id" not in coverage
    assert "entities.bench[].unit.instance_id" not in coverage
