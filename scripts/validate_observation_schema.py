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


def schema_path_exists(schema: dict, path: str) -> bool:
    current = schema
    for part in path.split("."):
        if "$ref" in current:
            ref = current["$ref"]
            if not ref.startswith("#/"):
                return False
            current = schema
            for token in ref[2:].split("/"):
                current = current.get(token.replace("~1", "/").replace("~0", "~"), {})
        if current.get("type") == "array":
            current = current.get("items", {})
        if "$ref" in current:
            ref = current["$ref"]
            if not ref.startswith("#/"):
                return False
            current = schema
            for token in ref[2:].split("/"):
                current = current.get(token.replace("~1", "/").replace("~0", "~"), {})
        current = current.get("properties", {}).get(part)
        if not isinstance(current, dict):
            return False
    return True


def collect_field_paths(schema: dict) -> set[str]:
    paths: set[str] = set()

    def visit(node: object, path: str, seen: set[str]) -> None:
        if not isinstance(node, dict):
            return
        ref = node.get("$ref")
        if ref:
            if ref == "#/$defs/field":
                paths.add(path)
                return
            if isinstance(ref, str) and ref.startswith("#/") and ref not in seen:
                target: object = schema
                for token in ref[2:].split("/"):
                    target = target.get(token.replace("~1", "/").replace("~0", "~"), {}) if isinstance(target, dict) else {}
                visit(target, path, seen | {ref})
            return
        if node.get("type") == "array":
            visit(node.get("items"), path + "[]", seen)
        for key, child in node.get("properties", {}).items():
            visit(child, f"{path}.{key}" if path else key, seen)
        additional = node.get("additionalProperties")
        if isinstance(additional, dict):
            visit(additional, path + ".*", seen)
        for keyword in ("allOf", "anyOf", "oneOf"):
            for child in node.get(keyword, []):
                visit(child, path, seen)

    visit(schema, "", set())
    return paths


def verify_catalog_fingerprints(snapshot: dict, expected: dict) -> None:
    for catalog_name, fingerprints in expected.items():
        actual = snapshot["catalogs"][catalog_name]
        if actual["content_hash"] != fingerprints["content_hash"]:
            raise ValueError(f"{catalog_name} content fingerprint mismatch")
        if actual["order_hash"] != fingerprints["order_hash"]:
            raise ValueError(f"{catalog_name} order fingerprint mismatch")


def verify_context_identity(snapshot: dict) -> None:
    identity = snapshot["identity"]
    if identity["status"] != "complete":
        legal = snapshot["legal_state_context"]
        if any(legal[key]["status"] == "valid" for key in ("anti_loop_state", "mask_reference", "critic_context")):
            raise ValueError("incomplete identity cannot carry valid mask/critic/history context")
        return
    expected_sequence = identity["decision_sequence"]
    anti_loop = snapshot["legal_state_context"]["anti_loop_state"]
    if anti_loop["status"] == "valid" and anti_loop.get("source_decision_sequence") != expected_sequence:
        raise ValueError("anti-loop history sequence does not match observation identity")
    critic = snapshot["legal_state_context"]["critic_context"]
    if critic["status"] == "valid" and critic.get("source_decision_sequence") != expected_sequence:
        raise ValueError("critic context sequence does not match observation identity")


def verify_provenance_nature(value: object, path: str = "$") -> None:
    if isinstance(value, list):
        for index, item in enumerate(value):
            verify_provenance_nature(item, f"{path}[{index}]")
    elif isinstance(value, dict):
        if "provenance" in value and "nature" in value:
            if value["provenance"].get("nature") != value["nature"]:
                raise ValueError(f"provenance nature mismatch at {path}")
        for key, item in value.items():
            verify_provenance_nature(item, f"{path}.{key}")


def decision_identity_hash(identity: dict) -> str:
    payload = {key: identity[key] for key in (
        "match_id", "engine_match_id", "player_id", "round",
        "decision_sequence", "snapshot_sequence"
    )}
    return digest(payload)


def verify_snapshot_hashes(snapshot: dict, schema: dict) -> None:
    if snapshot["schema"]["schema_hash"] != schema_contract_hash(schema):
        raise ValueError("observation schema hash mismatch")
    projection = copy.deepcopy(snapshot["schema"]["projection"])
    actual = projection.pop("projection_hash", None)
    if actual != digest(projection):
        raise ValueError("projection hash mismatch")
    identity = snapshot["identity"]
    if identity["status"] == "complete":
        expected_identity_hash = decision_identity_hash(identity)
        if identity["decision_identity_hash"] != expected_identity_hash:
            raise ValueError("decision identity hash mismatch")
        if snapshot["legal_state_context"]["mask_reference"]["decision_identity_hash"] != expected_identity_hash:
            raise ValueError("mask/observation decision identity mismatch")
    else:
        if identity["decision_identity_hash"] is not None:
            raise ValueError("incomplete identity must not expose a decision identity hash")
        if snapshot["legal_state_context"]["mask_reference"]["decision_identity_hash"] is not None:
            raise ValueError("incomplete identity must not expose a mask decision identity hash")


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


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )

    examples = ROOT / "spec" / "examples" / "observation-v1"
    source_map = json.loads((ROOT / "spec" / "observation-schema.v1.source-map.json").read_text(encoding="utf-8"))
    migration_map = json.loads((ROOT / "spec" / "observation-schema.v1.migration-map.json").read_text(encoding="utf-8"))
    legacy_map = json.loads((ROOT / "spec" / "observation-schema.v1.legacy-feature-map.json").read_text(encoding="utf-8"))
    snapshot = json.loads((examples / "valid-minimal.json").read_text(encoding="utf-8"))

    # Legacy coverage and source-map completeness.
    legacy_fields = {
        f"{block['id']}|{feature['name']}": feature
        for block in legacy_map["blocks"] for feature in block["fields"]
    }
    migration_fields = {
        f"{mapping['legacy_block']}|{mapping['legacy_field']}": mapping
        for mapping in migration_map["mappings"]
    }
    assert len(legacy_fields) == len(migration_fields) == migration_map["source_feature_count"] == 66
    assert set(legacy_fields) == set(migration_fields), "migration crosswalk does not cover the exact legacy feature inventory"
    for key, feature in legacy_fields.items():
        assert feature.get("source") and feature.get("nature") and feature.get("encoding")
        assert feature.get("consumers"), f"legacy feature has no consumer mapping: {key}"
        assert migration_fields[key]["legacy_source"] == feature["source"], f"legacy source drift: {key}"
    for mapping in migration_map["mappings"]:
        assert mapping["decision"] in migration_map["decision_vocabulary"]
        for destination in mapping["destination_paths"]:
            assert schema_path_exists(schema, destination), f"migration destination not in schema: {destination}"
        if mapping["decision"] == "drop_constant":
            assert not mapping["destination_paths"], "constant legacy feature unexpectedly has a destination"

    source_paths = [entry["field"] for entry in source_map["entries"]]
    normalized_source_paths = [path.replace("[]", "").replace(".*", "") for path in source_paths]
    field_paths = collect_field_paths(schema)
    uncovered_fields = [
        path for path in field_paths
        if not any(
            path.replace("[]", "").replace(".*", "") == mapped
            or path.replace("[]", "").replace(".*", "").startswith(mapped + ".")
            for mapped in normalized_source_paths
        )
    ]
    assert not uncovered_fields, f"schema fields without source/availability mapping: {sorted(uncovered_fields)}"
    assert len(source_paths) == len(set(source_paths)), "duplicate source-map field paths"
    required_source_metadata = {
        "current_source", "availability", "nature", "intended_consumer",
        "owner_issue", "unit", "normalization_or_scale", "validity_rule", "notes", "formula_or_version"
    }
    for entry in source_map["entries"]:
        missing_metadata = required_source_metadata - set(entry)
        assert not missing_metadata, f"{entry['field']} missing source metadata: {sorted(missing_metadata)}"
        assert entry["nature"] in {"observed", "derived", "estimated", "inferred", "recommended"}
        assert schema_path_exists(schema, entry["field"]), f"source-map path not present in schema: {entry['field']}"
    for excluded in source_map.get("excluded_legacy_projections", []):
        assert excluded.get("legacy_projection") and excluded.get("reason"), "excluded projection needs a reason"

    # Materialize the fixture's normative schema, projection and decision hashes.
    expected_schema_hash = schema_contract_hash(schema)
    snapshot["schema"]["schema_hash"] = expected_schema_hash
    snapshot["identity"]["decision_identity_hash"] = decision_identity_hash(snapshot["identity"])
    snapshot["legal_state_context"]["mask_reference"]["decision_identity_hash"] = snapshot["identity"]["decision_identity_hash"]
    projection = snapshot["schema"]["projection"]
    projection.pop("projection_hash", None)
    projection["projection_hash"] = digest(projection)

    for block in projection["blocks"]:
        for source_path in block["source_paths"]:
            assert schema_path_exists(schema, source_path), f"projection source path not in schema: {source_path}"

    expected_catalogs = {
        name: {"content_hash": item["content_hash"], "order_hash": item["order_hash"]}
        for name, item in snapshot["catalogs"].items()
    }
    verify_snapshot_hashes(snapshot, schema)
    verify_catalog_fingerprints(snapshot, expected_catalogs)
    verify_provenance_nature(snapshot)
    verify_context_identity(snapshot)

    errors = sorted(validator.iter_errors(snapshot), key=lambda e: list(e.absolute_path))
    if errors:
        raise SystemExit("valid-minimal.json rejected: " + "; ".join(e.message for e in errors))

    # A deliberately invalid fixture must be rejected for its missing reason.
    invalid = json.loads((examples / "invalid-missing-reason.json").read_text(encoding="utf-8"))
    invalid["schema"]["schema_hash"] = expected_schema_hash
    invalid["identity"]["decision_identity_hash"] = decision_identity_hash(invalid["identity"])
    invalid["legal_state_context"]["mask_reference"]["decision_identity_hash"] = invalid["identity"]["decision_identity_hash"]
    invalid_projection = invalid["schema"]["projection"]
    invalid_projection.pop("projection_hash", None)
    invalid_projection["projection_hash"] = digest(invalid_projection)
    assert list(validator.iter_errors(invalid)), "invalid-missing-reason.json unexpectedly passed"

    # Every field-status example must validate and retain provenance nature.
    matrix = json.loads((examples / "field-status-matrix.json").read_text(encoding="utf-8"))
    for case_name, case in matrix["cases"].items():
        candidate = copy.deepcopy(snapshot)
        candidate["player"]["economy"]["gold"] = case
        case_errors = list(validator.iter_errors(candidate))
        if case_errors:
            raise SystemExit(f"field-status case {case_name!r} rejected: " + "; ".join(e.message for e in case_errors))
        verify_provenance_nature(candidate)
        verify_context_identity(candidate)

    # Zero is observed data; unavailable states carry no fabricated value.
    zero = copy.deepcopy(snapshot)
    zero["player"]["economy"]["gold"] = field(0)
    assert not list(validator.iter_errors(zero))

    missing = copy.deepcopy(snapshot)
    missing["player"]["economy"]["gold"] = {
        "status": "missing",
        "nature": "observed",
        "reason": "source did not provide gold",
        "provenance": {"source": "fixture", "source_path": "fixture.gold", "nature": "observed"},
    }
    assert not list(validator.iter_errors(missing))
    invalid_missing_reason = copy.deepcopy(missing)
    del invalid_missing_reason["player"]["economy"]["gold"]["reason"]
    assert list(validator.iter_errors(invalid_missing_reason))
    invalid_missing_with_value = copy.deepcopy(missing)
    invalid_missing_with_value["player"]["economy"]["gold"]["value"] = 0
    assert list(validator.iter_errors(invalid_missing_with_value))

    # Incomplete identity cannot be combined with valid mask/critic context.
    incomplete_identity = copy.deepcopy(snapshot)
    incomplete_identity["identity"].update({
        "match_id": None, "engine_match_id": None, "player_id": None,
        "round": None, "decision_sequence": None, "snapshot_sequence": None,
        "status": "missing", "reason": "identity source unavailable",
        "decision_identity_hash": None,
    })
    incomplete_identity["legal_state_context"]["mask_reference"].update({
        "status": "unknown", "decision_identity_hash": None,
        "reason": "no complete decision identity",
    })
    incomplete_identity["legal_state_context"]["critic_context"].update({
        "status": "unknown", "reason": "no complete decision identity",
    })
    assert not list(validator.iter_errors(incomplete_identity))
    invalid_incomplete_context = copy.deepcopy(incomplete_identity)
    invalid_incomplete_context["legal_state_context"]["critic_context"].update({
        "status": "valid", "representation": "exact_masks", "source_decision_sequence": 1,
    })
    assert list(validator.iter_errors(invalid_incomplete_context))
    try:
        verify_context_identity(invalid_incomplete_context)
    except ValueError:
        pass
    else:
        raise AssertionError("valid critic context with incomplete identity was not rejected")

    # Complete anti-loop context requires exact histories and matching sequence.
    complete_anti_loop = copy.deepcopy(snapshot)
    anti_loop = complete_anti_loop["legal_state_context"]["anti_loop_state"]
    anti_loop.update({
        "status": "valid",
        "source_decision_sequence": 1,
        "position_history": [{"state_hash": "sha256:" + "4" * 64, "round": 1, "decision_sequence": 1}],
        "move_history": [{"round": 1, "decision_sequence": 1, "move_type": "board_move", "source_slot": 0, "target_slot": 1}],
        "blocked_move_records": [{"round": 1, "decision_sequence": 1, "move_type": "board_move", "reason": "repeated_state"}],
        "state_visits": [{"state_hash": "sha256:" + "4" * 64, "visit_count": 1, "last_seen_round": 1, "last_seen_sequence": 1}],
    })
    complete_anti_loop["legal_state_context"]["status"] = "valid"
    complete_anti_loop["legal_state_context"].pop("reason", None)
    assert not list(validator.iter_errors(complete_anti_loop))
    verify_context_identity(complete_anti_loop)
    stale_anti_loop = copy.deepcopy(complete_anti_loop)
    stale_anti_loop["legal_state_context"]["anti_loop_state"]["source_decision_sequence"] = 0
    try:
        verify_context_identity(stale_anti_loop)
    except ValueError:
        pass
    else:
        raise AssertionError("stale anti-loop history was not rejected")

    invalid_occupied_slot = copy.deepcopy(snapshot)
    invalid_occupied_slot["entities"]["board"][0] = {"slot_index": 0, "presence": "occupied", "unit": None}
    assert list(validator.iter_errors(invalid_occupied_slot))

    # Hashes, catalog ordering, schema evolution and projection padding.
    invalid_schema_hash = copy.deepcopy(snapshot)
    invalid_schema_hash["schema"]["schema_hash"] = "sha256:" + "0" * 64
    assert not list(validator.iter_errors(invalid_schema_hash))  # Format is valid; semantic hash check must reject.
    try:
        verify_snapshot_hashes(invalid_schema_hash, schema)
    except ValueError:
        pass
    else:
        raise AssertionError("schema hash mismatch was not rejected")

    mismatched_mask_identity = copy.deepcopy(snapshot)
    mismatched_mask_identity["legal_state_context"]["mask_reference"]["decision_identity_hash"] = "sha256:" + "0" * 64
    try:
        verify_snapshot_hashes(mismatched_mask_identity, schema)
    except ValueError:
        pass
    else:
        raise AssertionError("mask/observation identity mismatch was not rejected")

    mismatched_catalog = copy.deepcopy(snapshot)
    wrong_catalogs = copy.deepcopy(expected_catalogs)
    wrong_catalogs["traits"]["order_hash"] = "sha256:" + "f" * 64
    try:
        verify_catalog_fingerprints(mismatched_catalog, wrong_catalogs)
    except ValueError:
        pass
    else:
        raise AssertionError("catalog order mismatch was not rejected")

    changed_normative_schema = copy.deepcopy(schema)
    changed_normative_schema["$defs"]["field"]["properties"]["status"]["type"] = "string"
    assert schema_contract_hash(changed_normative_schema) != schema_contract_hash(schema)
    changed_annotation_only = copy.deepcopy(schema)
    changed_annotation_only["description"] = "non-normative wording change"
    assert schema_contract_hash(changed_annotation_only) == schema_contract_hash(schema)

    invalid_padding = copy.deepcopy(snapshot)
    del invalid_padding["schema"]["projection"]["blocks"][1]["presence_mask_path"]
    assert list(validator.iter_errors(invalid_padding))
    invalid_shape = copy.deepcopy(snapshot)
    invalid_shape["schema"]["projection"]["blocks"][1]["shape"] = [14, -1]
    assert list(validator.iter_errors(invalid_shape))

    invalid_projection_hash = copy.deepcopy(snapshot)
    invalid_projection_hash["schema"]["projection"]["projection_hash"] = "sha256:" + "0" * 64
    try:
        verify_snapshot_hashes(invalid_projection_hash, schema)
    except ValueError:
        pass
    else:
        raise AssertionError("projection hash mismatch was not rejected")

    print("Observation Schema Draft 2020-12: OK")
    print("Fixtures, provenance, identity, masks, anti-loop history, catalog/order, padding and 66-feature crosswalk: OK")

if __name__ == "__main__":
    main()
