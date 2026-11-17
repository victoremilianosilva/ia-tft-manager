#!/usr/bin/env python3
"""Executable validation for Observation Schema v2 and Decision Identity v2."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import jsonschema
import rfc8785

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "spec" / "observation-schema.v2.draft.json"
REGISTRY_PATH = ROOT / "spec" / "sequence-namespace-registry.v2.draft.json"
VECTORS_PATH = ROOT / "spec" / "decision-identity-v2-hash-vectors.draft.json"
IDENTITY_SOURCE_MAP_PATH = ROOT / "spec" / "observation-schema.v2.identity-source-map.draft.json"
FIXTURE_PATH = ROOT / "spec" / "examples" / "observation-v2" / "valid-minimal.json"
HASH_SCOPE = (
    "RFC8785-SHA256:v2:identity_version,match_id,engine_match_id,player_id,round,"
    "decision_sequence.namespace,decision_sequence.value,"
    "snapshot_sequence.namespace,snapshot_sequence.value"
)


def digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(rfc8785.dumps(value)).hexdigest()


def normative_schema(value: object) -> object:
    excluded = {"title", "description", "examples", "default", "$comment", "deprecated"}
    if isinstance(value, dict):
        return {key: normative_schema(item) for key, item in value.items() if key not in excluded}
    if isinstance(value, list):
        return [normative_schema(item) for item in value]
    return value


def schema_hash(schema: dict) -> str:
    return digest(normative_schema(schema))


def projection_hash(projection: dict) -> str:
    payload = copy.deepcopy(projection)
    payload.pop("projection_hash", None)
    return digest(payload)


def decision_identity_hash(identity: dict) -> str:
    payload = {
        key: identity[key]
        for key in (
            "identity_version", "match_id", "engine_match_id", "player_id",
            "round", "decision_sequence", "snapshot_sequence"
        )
    }
    return digest(payload)


def verify_provenance_nature(value: object, path: str = "$") -> None:
    if isinstance(value, list):
        for index, item in enumerate(value):
            verify_provenance_nature(item, f"{path}[{index}]")
    elif isinstance(value, dict):
        if "provenance" in value and "nature" in value:
            provenance = value["provenance"]
            if provenance.get("nature") != value["nature"]:
                raise ValueError(f"provenance nature mismatch at {path}")
            if value["nature"] in {"derived", "estimated", "inferred", "recommended"}:
                if not provenance.get("formula_id") or not provenance.get("formula_version"):
                    raise ValueError(f"formula identity missing at {path}")
        for key, item in value.items():
            verify_provenance_nature(item, f"{path}.{key}")


def verify_cardinality(snapshot: dict) -> None:
    entities = snapshot["entities"]
    expected = {"board": 28, "bench": 9, "shop": 5}
    physical_ids = set()
    for name, count in expected.items():
        slots = entities[name]
        if len(slots) != count:
            raise ValueError(f"{name} cardinality must be exactly {count}")
        if [slot["slot_index"] for slot in slots] != list(range(count)):
            raise ValueError(f"{name} slots must preserve contiguous canonical slot order")
        for slot in slots:
            if slot["presence"] == "occupied":
                unit = slot.get("unit")
                if not isinstance(unit, dict):
                    raise ValueError(f"occupied {name} slot requires a physical unit")
                if name in {"board", "bench"}:
                    instance_id = unit["instance_id"]
                    if instance_id in physical_ids:
                        raise ValueError(f"duplicate physical unit instance_id: {instance_id}")
                    physical_ids.add(instance_id)
            elif slot.get("unit", "not-present") is not None:
                raise ValueError(f"non-occupied {name} slot must carry unit=null")


def verify_identity(snapshot: dict, registry: dict) -> None:
    identity = snapshot["identity"]
    namespaces = {entry["namespace"]: entry for entry in registry["entries"]}
    if identity["decision_identity_hash_scope"] != HASH_SCOPE:
        raise ValueError("Decision Identity v2 hash scope drift")
    for field_name in ("decision_sequence", "snapshot_sequence"):
        reference = identity[field_name]
        if reference is None:
            continue
        entry = namespaces.get(reference["namespace"])
        if entry is None:
            raise ValueError(f"unregistered sequence namespace: {reference['namespace']}")
        if not entry["availability"].startswith("implemented_"):
            raise ValueError(f"unimplemented or unverified namespace used by snapshot: {reference['namespace']}")
        if field_name == "decision_sequence" and not entry["canonical_decision_eligible"]:
            raise ValueError("snapshot publication sequence cannot stand in for per-player decision sequence")

    mask = snapshot["legal_state_context"]["mask_reference"]
    if identity["status"] == "complete":
        decision = identity["decision_sequence"]
        if decision is None or identity["snapshot_sequence"] is None:
            raise ValueError("complete identity requires decision and snapshot sequence references")
        expected = decision_identity_hash(identity)
        if identity["decision_identity_hash"] != expected:
            raise ValueError("decision identity hash mismatch")
        if mask["status"] == "valid" and mask["decision_identity_hash"] != expected:
            raise ValueError("mask/observation decision identity mismatch")
    else:
        if not identity.get("reason"):
            raise ValueError("incomplete identity requires a reason")
        if identity["decision_identity_hash"] is not None:
            raise ValueError("incomplete identity must not expose a decision identity hash")
        if mask["decision_identity_hash"] is not None:
            raise ValueError("incomplete identity cannot carry a mask decision identity hash")


def verify_context_identity(snapshot: dict) -> None:
    identity = snapshot["identity"]
    legal = snapshot["legal_state_context"]
    owners = snapshot["strategic_evidence"]["owner_snapshots"]
    if identity["status"] != "complete":
        if legal["mask_reference"]["status"] == "valid":
            raise ValueError("incomplete identity cannot carry valid masks")
        if legal["critic_context"]["status"] == "valid":
            raise ValueError("incomplete identity cannot carry valid Critic context")
        if legal["anti_loop_state"]["status"] == "valid":
            raise ValueError("incomplete identity cannot carry valid temporal history")
        if any(owner["status"] == "valid" for owner in owners.values()):
            raise ValueError("incomplete identity cannot carry valid strategic owner snapshots")
        return

    expected_sequence = identity["decision_sequence"]["value"]
    for name in ("critic_context", "anti_loop_state"):
        context = legal[name]
        if context["status"] == "valid" and context.get("source_decision_sequence") != expected_sequence:
            raise ValueError(f"{name} source sequence does not match decision identity")
    for owner_name, owner in owners.items():
        if owner["status"] == "valid" and owner.get("source_decision_sequence") != expected_sequence:
            raise ValueError(f"{owner_name} source sequence does not match decision identity")


def verify_hash_vectors(vectors: dict) -> None:
    for vector in vectors["vectors"]:
        canonical = rfc8785.dumps(vector["input"]).decode("utf-8")
        if canonical != vector["canonical_bytes"]:
            raise ValueError(f"RFC 8785 canonical bytes mismatch: {vector['id']}")
        if digest(vector["input"]) != vector["expected_hash"]:
            raise ValueError(f"Decision Identity v2 hash mismatch: {vector['id']}")


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    vectors = json.loads(VECTORS_PATH.read_text(encoding="utf-8"))
    identity_source_map = json.loads(IDENTITY_SOURCE_MAP_PATH.read_text(encoding="utf-8"))
    snapshot = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())

    identity_entries = {entry["field_path"]: entry for entry in identity_source_map["fields"]}
    identity_fields = set(identity_entries)
    schema_identity_fields = {"identity." + name for name in schema["$defs"]["sequenceIdentity"]["properties"]}
    if identity_fields != schema_identity_fields:
        raise SystemExit("Decision Identity source map must cover every v2 identity property exactly")
    required_metadata = {"owner", "source", "availability", "nature", "scope", "canonical_decision_eligible", "notes"}
    for entry in identity_source_map["fields"]:
        if required_metadata - set(entry):
            raise SystemExit("incomplete identity source mapping: " + entry["field_path"])
    if identity_entries["identity.snapshot_sequence"]["availability"] != "implemented_native_engine_pr428":
        raise SystemExit("snapshot_sequence source mapping does not match native Engine evidence")
    if identity_entries["identity.decision_sequence"]["availability"] != "proposed_not_implemented":
        raise SystemExit("per-player decision_sequence must remain explicitly unavailable")

    namespace_names = [entry["namespace"] for entry in registry["entries"]]
    if len(namespace_names) != len(set(namespace_names)):
        raise SystemExit("duplicate sequence namespace registration")
    if registry["version"] != "2.1.0-draft":
        raise SystemExit("sequence namespace registry version drift")

    # Native decision_sequence is an Engine-wide snapshot ordinal, not a player decision counter.
    native_snapshot = next(
        entry for entry in registry["entries"]
        if entry["namespace"] == "tft.engine.observation-snapshot"
    )
    if native_snapshot["availability"] != "implemented_native_engine_pr428":
        raise SystemExit("native snapshot sequence availability evidence drift")
    if native_snapshot["canonical_decision_eligible"]:
        raise SystemExit("Engine-wide snapshot sequence cannot be a per-player decision sequence")

    expected_schema_hash = schema_hash(schema)
    snapshot["schema"]["schema_hash"] = expected_schema_hash
    snapshot["schema"]["projection"]["projection_hash"] = projection_hash(
        snapshot["schema"]["projection"]
    )

    errors = sorted(validator.iter_errors(snapshot), key=lambda error: list(error.absolute_path))
    if errors:
        raise SystemExit("valid-minimal.json rejected: " + "; ".join(error.message for error in errors))

    if snapshot["schema"]["schema_hash"] != expected_schema_hash:
        raise SystemExit("schema hash materialization failed")
    verify_identity(snapshot, registry)
    verify_context_identity(snapshot)
    verify_provenance_nature(snapshot)
    verify_cardinality(snapshot)
    verify_hash_vectors(vectors)

    # A partial identity must fail closed even when a mask reference is marked valid.
    invalid_mask = copy.deepcopy(snapshot)
    invalid_mask["legal_state_context"]["mask_reference"].update({
        "status": "valid",
        "action_contract_id": "tft.ppo.action",
        "action_contract_version": "1.0.0",
        "action_contract_hash": "sha256:" + "1" * 64,
        "mask_contract_id": "tft.ppo.action-mask",
        "mask_contract_version": "1.0.0",
        "mask_contract_hash": "sha256:" + "2" * 64,
        "mask_snapshot_hash": "sha256:" + "3" * 64,
        "decision_identity_hash": "sha256:" + "4" * 64,
    })
    try:
        verify_identity(invalid_mask, registry)
        verify_context_identity(invalid_mask)
    except ValueError:
        pass
    else:
        raise AssertionError("partial identity was allowed to carry valid mask context")

    # The Engine snapshot ordinal must never be promoted to a per-player decision sequence.
    invalid_sequence = copy.deepcopy(snapshot)
    invalid_sequence["identity"]["decision_sequence"] = {
        "namespace": "tft.engine.observation-snapshot", "value": 1
    }
    invalid_sequence["identity"]["status"] = "complete"
    invalid_sequence["identity"]["match_id"] = "match-001"
    invalid_sequence["identity"]["engine_match_id"] = "engine-001"
    invalid_sequence["identity"]["decision_identity_hash"] = "sha256:" + "0" * 64
    try:
        verify_identity(invalid_sequence, registry)
    except ValueError:
        pass
    else:
        raise AssertionError("Engine snapshot ordinal was promoted to per-player decision sequence")

    # Checked-in negative fixtures prove that fail-closed rules are executable.
    invalid_mask_fixture = json.loads(
        (FIXTURE_PATH.parent / "invalid-partial-mask.json").read_text(encoding="utf-8")
    )
    try:
        verify_identity(invalid_mask_fixture, registry)
        verify_context_identity(invalid_mask_fixture)
    except ValueError:
        pass
    else:
        raise AssertionError("partial identity was allowed to carry valid mask context")

    invalid_sequence_fixture = json.loads(
        (FIXTURE_PATH.parent / "invalid-engine-snapshot-as-decision.json").read_text(encoding="utf-8")
    )
    try:
        verify_identity(invalid_sequence_fixture, registry)
    except ValueError:
        pass
    else:
        raise AssertionError("Engine snapshot ordinal was promoted to per-player decision sequence")

    invalid_slots_fixture = json.loads(
        (FIXTURE_PATH.parent / "invalid-slot-order.json").read_text(encoding="utf-8")
    )
    try:
        verify_cardinality(invalid_slots_fixture)
    except ValueError:
        pass
    else:
        raise AssertionError("non-canonical slot order was accepted")

    invalid_duplicate = copy.deepcopy(snapshot)
    invalid_duplicate["entities"]["bench"][0] = copy.deepcopy(
        invalid_duplicate["entities"]["board"][0]
    )
    invalid_duplicate["entities"]["bench"][0]["slot_index"] = 0
    try:
        verify_cardinality(invalid_duplicate)
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate physical unit instance was accepted")

    # Zero is valid data; missing/unknown requires a reason and no fabricated value.
    gold = snapshot["player"]["economy"]["gold"]
    if gold["status"] != "valid" or gold["value"] != 10:
        raise AssertionError("minimal fixture no longer preserves a valid numeric value")
    invalid_missing = copy.deepcopy(snapshot)
    invalid_missing["player"]["economy"]["gold"] = {
        "status": "missing", "nature": "observed",
        "provenance": {"source": "fixture", "source_path": "fixture.gold", "nature": "observed"}
    }
    if not list(validator.iter_errors(invalid_missing)):
        raise AssertionError("missing field without reason unexpectedly validated")

    print("Observation Schema v2, Decision Identity v2, provenance, cardinality and hash vectors: PASS")


if __name__ == "__main__":
    main()
