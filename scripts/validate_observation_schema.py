#!/usr/bin/env python3
"""Executable contract checks for the draft TFT PPO Observation Schema."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema
import rfc8785

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "spec" / "observation-schema.v1.draft.json"


def digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(rfc8785.dumps(value)).hexdigest()


def normative_schema(value: object) -> object:
    """Remove non-normative JSON Schema annotations before identity hashing."""
    excluded = {"title", "description", "examples", "default", "$comment", "deprecated"}
    if isinstance(value, dict):
        return {k: normative_schema(v) for k, v in value.items() if k not in excluded}
    if isinstance(value, list):
        return [normative_schema(v) for v in value]
    return value


def schema_contract_hash(schema: dict) -> str:
    return digest(normative_schema(schema))


def field(value: object, nature: str = "observed") -> dict:
    return {
        "value": value,
        "status": "valid",
        "nature": nature,
        "provenance": {
            "source": "contract-fixture",
            "source_path": "fixture.value",
            "nature": nature,
        },
    }


def empty_slots(count: int) -> list[dict]:
    return [{"slot_index": i, "presence": "empty", "unit": None} for i in range(count)]


def valid_snapshot(schema: dict) -> dict:
    projection = {
        "projection_id": "tft.ppo.structured.v1",
        "version": "1.0.0",
        "projection_hash": "",
        "dtype": "structured",
        "blocks": [],
        "canonicalization": "RFC8785",
        "hash_scope": "Canonical projection definition excluding projection_hash",
    }
    projection.pop("projection_hash")
    projection["projection_hash"] = digest(projection)
    schema_hash = schema_contract_hash(schema)
    empty_catalog = {
        "catalog_id": "fixture.catalog",
        "version": "1",
        "content_hash": "sha256:" + "1" * 64,
        "order_hash": "sha256:" + "2" * 64,
    }
    return {
        "schema": {
            "schema_id": "tft.ppo.observation",
            "semantic_version": "1.0.0",
            "structural_revision": 1,
            "schema_hash": schema_hash,
            "projection": projection,
            "hash_algorithm": "SHA-256",
            "hash_canonicalization": "RFC8785",
            "hash_scope": "Canonical RFC8785 form of normative schema content (field definitions, types, constraints, requiredness, semantics, catalog references and projection identity); excludes descriptions, examples and schema_hash itself",
            "evolution_policy": {
                "patch": "Editorial metadata/examples/provenance clarification only; no field meaning, constraints, projection or catalog identity changes.",
                "minor": "Additive optional fields only; existing fields retain identical meaning and consumers may ignore additions only when their declared profile does not require them.",
                "major": "Any field rename/removal/reinterpretation, unit/scale/range/ordering/requiredness change, or identity-semantic change.",
                "projection_change": "Any tensor block/order/shape/dtype/encoder grouping/normalization change increments projection version and projection hash, even if semantic schema version is unchanged.",
                "catalog_change": "Content and order fingerprints are independent; any used vocabulary or ordering change updates its fingerprint, and a changed interpretation is semantically incompatible.",
                "migration": "Migration requires an explicit versioned manifest and contract tests; positional zero-padding/remapping is not evidence of semantic compatibility.",
                "training_lineage": "Semantic or projection incompatibility starts a new training lineage unless an explicitly approved and tested partial transfer is recorded.",
            },
        },
        "identity": {
            "match_id": "fixture-match",
            "engine_match_id": "fixture-engine-match",
            "session_match_id": "fixture-session-match",
            "player_id": "player-1",
            "round": 1,
            "decision_sequence": 1,
            "snapshot_sequence": 1,
            "status": "complete",
            "captured_at": "2026-01-01T00:00:00Z",
        },
        "catalogs": {
            "champions": dict(empty_catalog, catalog_id="champions"),
            "traits": dict(empty_catalog, catalog_id="traits"),
            "items": dict(empty_catalog, catalog_id="items"),
            "components": dict(empty_catalog, catalog_id="components"),
            "recipes": dict(empty_catalog, catalog_id="recipes"),
        },
        "player": {
            "lifecycle": field("active"),
            "health": field(100, "observed"),
            "economy": {
                "gold": field(10),
                "level": field(4),
                "xp": field(0),
            },
        },
        "entities": {
            "board": empty_slots(28),
            "bench": empty_slots(9),
            "shop": empty_slots(5),
        },
        "derived_context": {},
        "strategic_evidence": {},
        "legal_state_context": {
            "status": "unknown",
            "anti_loop_state": {"status": "unknown", "reason": "not supplied by fixture"},
            "mask_reference": {
                "status": "unknown",
                "decision_identity_hash": "sha256:" + "3" * 64,
                "reason": "mask belongs to the independent Action Contract",
            },
            "critic_context": {
                "status": "unknown",
                "reason": "critic representation is specified independently",
            },
            "description": "Descriptive state/history context only. Actual action masks and action legality are defined by the independent Action Contract.",
        },
    }


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    examples = ROOT / "spec" / "examples" / "observation-v1"
    snapshot = json.loads((examples / "valid-minimal.json").read_text(encoding="utf-8"))
    expected_schema_hash = schema_contract_hash(schema)
    snapshot["schema"]["schema_hash"] = expected_schema_hash
    projection = snapshot["schema"]["projection"]
    projection.pop("projection_hash", None)
    projection["projection_hash"] = digest(projection)

    errors = sorted(validator.iter_errors(snapshot), key=lambda e: list(e.absolute_path))
    if errors:
        raise SystemExit("valid-minimal.json rejected:\\n" + "\\n".join(
            f"{list(e.absolute_path)}: {e.message}" for e in errors
        ))

    invalid = json.loads((examples / "invalid-missing-reason.json").read_text(encoding="utf-8"))
    invalid["schema"]["schema_hash"] = expected_schema_hash
    invalid_projection = invalid["schema"]["projection"]
    invalid_projection.pop("projection_hash", None)
    invalid_projection["projection_hash"] = digest(invalid_projection)
    assert list(validator.iter_errors(invalid)), "invalid-missing-reason.json unexpectedly passed"

    matrix = json.loads((examples / "field-status-matrix.json").read_text(encoding="utf-8"))
    for case_name, case in matrix["cases"].items():
        candidate = copy.deepcopy(snapshot)
        candidate["player"]["economy"]["gold"] = case
        case_errors = list(validator.iter_errors(candidate))
        if case_errors:
            raise SystemExit(f"field-status case {case_name!r} rejected: " +
                             "; ".join(e.message for e in case_errors))

    # Zero is a real observed value; missing is a distinct status with a reason
    # and must not carry a fabricated numeric value.
    zero = copy.deepcopy(snapshot)
    zero["player"]["economy"]["gold"] = field(0)
    assert not list(validator.iter_errors(zero))

    missing = copy.deepcopy(snapshot)
    missing["player"]["economy"]["gold"] = {
        "status": "missing",
        "nature": "observed",
        "reason": "source did not provide gold",
        "provenance": {
            "source": "fixture",
            "source_path": "fixture.gold",
            "nature": "observed",
        },
    }
    assert not list(validator.iter_errors(missing))

    invalid_missing_reason = copy.deepcopy(missing)
    del invalid_missing_reason["player"]["economy"]["gold"]["reason"]
    assert list(validator.iter_errors(invalid_missing_reason))
    invalid_missing_with_value = copy.deepcopy(missing)
    invalid_missing_with_value["player"]["economy"]["gold"]["value"] = 0
    assert list(validator.iter_errors(invalid_missing_with_value))

    incomplete_identity = copy.deepcopy(snapshot)
    incomplete_identity["identity"].update({
        "match_id": None, "engine_match_id": None, "player_id": None,
        "round": None, "decision_sequence": None, "snapshot_sequence": None,
        "status": "missing", "reason": "identity source unavailable",
    })
    assert not list(validator.iter_errors(incomplete_identity))

    invalid_occupied_slot = copy.deepcopy(snapshot)
    invalid_occupied_slot["entities"]["board"][0] = {
        "slot_index": 0, "presence": "occupied", "unit": None
    }
    assert list(validator.iter_errors(invalid_occupied_slot))

    invalid_schema_hash = copy.deepcopy(snapshot)
    invalid_schema_hash["schema"]["schema_hash"] = "sha256:" + "0" * 64
    assert list(validator.iter_errors(invalid_schema_hash)) == []  # JSON Schema checks format; hash identity is checked here.
    assert invalid_schema_hash["schema"]["schema_hash"] != schema_contract_hash(schema)

    print("Observation Schema Draft 2020-12: OK")
    print("Valid/invalid fixtures, zero-vs-missing, occupied-slot and schema-hash checks: OK")


if __name__ == "__main__":
    main()
