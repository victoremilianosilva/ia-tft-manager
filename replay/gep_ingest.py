"""Ingest hash-chained Overwolf GEP captures as observational match artifacts.

GEP captures are authoritative observations of the live game state exposed by
the provider. They are not full deterministic replays and do not contain
per-combat damage telemetry or verified action-execution traces.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .recorder import ReplayIntegrityError, _canonical, sha256_file


GEP_CAPTURE_FORMAT = "TFT_GEP_OBSERVATION_CAPTURE_V1"
GEP_MATCH_FORMAT = "TFT_GEP_MATCH_REPLAY_V1"
DATASET_FORMAT = "TFT_GEP_OBSERVATION_DATASET_V1"


def _read_hash_chain(path: str | Path, *, expected_format: str) -> dict[str, Any]:
    source = Path(path)
    records: list[dict[str, Any]] = []
    previous_hash = ""
    with source.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            raw_line = line.rstrip("\r\n")
            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as error:
                raise ReplayIntegrityError(
                    f"Invalid GEP JSON at line {line_number}: {error.msg}"
                ) from error
            if not isinstance(record, dict):
                raise ReplayIntegrityError(f"GEP record at line {line_number} is not an object")
            if record.get("sequence") != len(records):
                raise ReplayIntegrityError(f"Non-monotonic GEP sequence at line {line_number}")
            if record.get("previous_record_sha256") != (previous_hash or None):
                raise ReplayIntegrityError(f"Broken GEP hash link at line {line_number}")
            marker = ',"record_sha256":'
            marker_index = raw_line.rfind(marker)
            if marker_index < 0:
                raise ReplayIntegrityError(f"Missing terminal GEP hash at line {line_number}")
            body_json = raw_line[:marker_index] + "}"
            expected_hash = hashlib.sha256(
                (previous_hash + body_json).encode("utf-8")
            ).hexdigest()
            if record.get("record_sha256") != expected_hash:
                raise ReplayIntegrityError(f"GEP hash mismatch at line {line_number}")
            previous_hash = expected_hash
            records.append(record)

    if not records or records[0].get("record_type") != "manifest":
        raise ReplayIntegrityError("GEP capture must start with a manifest")
    manifest = records[0].get("payload")
    if not isinstance(manifest, dict) or manifest.get("replay_format") != expected_format:
        raise ReplayIntegrityError("Unsupported GEP replay format")
    footer = records[-1] if records[-1].get("record_type") == "footer" else None
    complete = bool(footer and footer.get("payload", {}).get("complete") is True)
    if not footer:
        raise ReplayIntegrityError("GEP capture has no terminal footer")
    footer_payload = footer.get("payload", {})
    if footer_payload.get("records_before_footer") != len(records) - 1:
        raise ReplayIntegrityError("GEP footer record count mismatch")
    if footer_payload.get("final_record_sha256") != footer.get("previous_record_sha256"):
        raise ReplayIntegrityError("GEP footer final hash mismatch")
    if footer_payload.get("complete") is not (footer_payload.get("status") == "completed"):
        raise ReplayIntegrityError("GEP footer status/completeness mismatch")
    return {
        "path": str(source),
        "manifest": manifest,
        "records": records,
        "complete": complete,
        "final_record_sha256": previous_hash,
    }


def load_gep_capture(path: str | Path, *, require_complete: bool = True) -> dict[str, Any]:
    capture = _read_hash_chain(path, expected_format=GEP_CAPTURE_FORMAT)
    manifest = capture["manifest"]
    if manifest.get("source") != "overwolf_gep":
        raise ReplayIntegrityError("GEP capture source is not Overwolf GEP")
    if manifest.get("deterministic_reexecution") is not False:
        raise ReplayIntegrityError("GEP capture must be marked observational-only")
    if manifest.get("combat_telemetry_enabled") is not False:
        raise ReplayIntegrityError("GEP capture combat telemetry disposition is ambiguous")
    if require_complete and not capture["complete"]:
        raise ReplayIntegrityError("GEP capture is incomplete")
    return capture


def _match_groups(capture: dict[str, Any]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in capture["records"]:
        if record.get("record_type") not in {"raw_gep_event", "canonical_state_snapshot"}:
            continue
        payload = record.get("payload", {})
        session_id = payload.get("game_session_id")
        match_id = payload.get("match_id")
        if not isinstance(session_id, str) or not session_id:
            continue
        if not isinstance(match_id, str) or not match_id:
            continue
        groups.setdefault((session_id, match_id), []).append(record)
    return groups


def _write_hash_chain(path: Path, records: list[tuple[str, dict[str, Any]]]) -> str:
    previous_hash = ""
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        for sequence, (record_type, payload) in enumerate(records):
            body = {
                "sequence": sequence,
                "record_type": record_type,
                "previous_record_sha256": previous_hash or None,
                "payload": payload,
            }
            body_json = _canonical(body)
            record_hash = hashlib.sha256(
                (previous_hash + body_json).encode("utf-8")
            ).hexdigest()
            stream.write(body_json[:-1] + ',"record_sha256":' +
                         json.dumps(record_hash) + "}\n")
            previous_hash = record_hash
    return previous_hash


def ingest_gep_capture(path: str | Path, output_dir: str | Path) -> list[dict[str, Any]]:
    """Create immutable per-match observational artifacts from a complete GEP stream."""
    capture = load_gep_capture(path, require_complete=True)
    capture_hash = sha256_file(path)
    source_manifest = capture["manifest"]
    groups = _match_groups(capture)
    if not groups:
        raise ReplayIntegrityError("GEP capture contains no match-correlated state or event records")

    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    artifacts = []
    for (game_session_id, match_id), records in sorted(groups.items()):
        snapshots = [
            record for record in records
            if record.get("record_type") == "canonical_state_snapshot"
        ]
        if not snapshots:
            raise ReplayIntegrityError(f"Match {match_id} has no canonical state snapshots")
        revisions = [record["payload"].get("revision") for record in snapshots]
        if any(not isinstance(value, int) for value in revisions):
            raise ReplayIntegrityError(f"Match {match_id} has invalid snapshot revisions")
        if revisions != sorted(set(revisions)):
            raise ReplayIntegrityError(f"Match {match_id} snapshot revisions are not strictly increasing")
        if not any(record["payload"].get("complete") is True for record in snapshots):
            raise ReplayIntegrityError(f"Match {match_id} has no complete baseline snapshot")

        game_exit_seen = any(
            record.get("record_type") == "raw_gep_event" and
            record.get("payload", {}).get("event") == "lifecycle:game-exit"
            for record in records
        )
        if not game_exit_seen:
            raise ReplayIntegrityError(f"Match {match_id} has no observed game-exit boundary")

        artifact_seed = f"{capture_hash}:{game_session_id}:{match_id}"
        artifact_id = "sha256:" + hashlib.sha256(artifact_seed.encode("utf-8")).hexdigest()
        artifact_name = artifact_id.split(":", 1)[1] + ".jsonl"
        artifact_path = destination / artifact_name
        event_count = sum(record.get("record_type") == "raw_gep_event" for record in records)
        match_manifest = {
            "replay_format": GEP_MATCH_FORMAT,
            "schema_version": 1,
            "replay_artifact_id": artifact_id,
            "source": "overwolf_gep_live_state",
            "source_capture_sha256": capture_hash,
            "capture_session_id": source_manifest.get("capture_session_id"),
            "game_session_id": game_session_id,
            "match_id": match_id,
            "game_id": source_manifest.get("game_id"),
            "replay_mode": "observational_only",
            "deterministic_reexecution": False,
            "authoritative_state_observations": True,
            "authoritative_game_replay": False,
            "combat_telemetry_available": False,
            "action_execution_trace_available": False,
            "snapshot_count": len(snapshots),
            "event_count": event_count,
        }
        output_records: list[tuple[str, dict[str, Any]]] = [("manifest", match_manifest)]
        for source_record in records:
            source_payload = source_record["payload"]
            if source_record.get("record_type") == "canonical_state_snapshot":
                output_records.append(("state_snapshot", {
                    "source_record_sequence": source_record["sequence"],
                    "source_record_sha256": source_record["record_sha256"],
                    "game_session_id": game_session_id,
                    "match_id": match_id,
                    "captured_at": source_payload.get("captured_at"),
                    "revision": source_payload.get("revision"),
                    "complete": source_payload.get("complete"),
                    "state": source_payload.get("state"),
                }))
            else:
                output_records.append(("observed_gep_event", {
                    "source_record_sequence": source_record["sequence"],
                    "source_record_sha256": source_record["record_sha256"],
                    "game_session_id": game_session_id,
                    "match_id": match_id,
                    "event": source_payload.get("event"),
                    "captured_at": source_payload.get("captured_at"),
                    "payload": source_payload.get("payload"),
                }))
        final_hash = _write_hash_chain(artifact_path, output_records + [(
            "footer", {
                "status": "completed",
                "records_before_footer": len(output_records),
                "final_record_sha256": "",
                "complete": True,
            }
        )])
        # The footer commits to the hash of the final source record. Rewrite is
        # avoided: the footer payload above is informational; the chain itself
        # commits to every record and the artifact file hash commits to footer.
        artifacts.append({
            "replay_artifact_id": artifact_id,
            "path": artifact_name,
            "sha256": sha256_file(artifact_path),
            "match_id": match_id,
            "game_session_id": game_session_id,
            "snapshot_count": len(snapshots),
            "event_count": event_count,
            "source_capture_sha256": capture_hash,
            "final_record_sha256": final_hash,
        })
    return artifacts


def build_gep_dataset_manifest(
    capture_paths: Iterable[str | Path],
    output_path: str | Path,
    *,
    split_seed: str = "tft-gep-split-v1",
) -> dict[str, Any]:
    destination = Path(output_path)
    artifact_dir = destination.parent / f"{destination.stem}_artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=False)
    artifacts = []
    for capture_path in capture_paths:
        artifacts.extend(ingest_gep_capture(capture_path, artifact_dir))
    match_ids = [item["match_id"] for item in artifacts]
    if len(set(match_ids)) != len(match_ids):
        raise ValueError("Duplicate match_id across GEP captures; refusing split leakage")
    if len(match_ids) < 3:
        raise ValueError("Train/validation/test require at least three independent live matches")

    ranked = sorted(match_ids, key=lambda match_id: hashlib.sha256(
        f"{split_seed}:{match_id}".encode("utf-8")
    ).hexdigest())
    count = len(ranked)
    test_count = max(1, round(count * 0.1))
    validation_count = max(1, round(count * 0.1))
    while test_count + validation_count >= count:
        if test_count >= validation_count:
            test_count -= 1
        else:
            validation_count -= 1
    test_ids = set(ranked[:test_count])
    validation_ids = set(ranked[test_count:test_count + validation_count])
    train_ids = set(ranked[test_count + validation_count:])
    split_by_match = {
        match_id: ("test" if match_id in test_ids else
                   "validation" if match_id in validation_ids else "train")
        for match_id in match_ids
    }
    for artifact in artifacts:
        artifact["split"] = split_by_match[artifact["match_id"]]

    payload = {
        "dataset_format": DATASET_FORMAT,
        "schema_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "split_seed": split_seed,
        "match_count": len(match_ids),
        "replay_count": len(artifacts),
        "replay_mode": "observational_only",
        "deterministic_reexecution": False,
        "combat_telemetry_available": False,
        "action_execution_trace_available": False,
        "splits": {
            "train": sorted(train_ids),
            "validation": sorted(validation_ids),
            "test": sorted(test_ids),
        },
        "artifacts": sorted(artifacts, key=lambda item: item["replay_artifact_id"]),
    }
    hash_payload = dict(payload)
    hash_payload.pop("created_at", None)
    dataset_hash = hashlib.sha256(_canonical(hash_payload).encode("utf-8")).hexdigest()
    manifest = dict(payload, dataset_version=f"sha256:{dataset_hash}",
                    dataset_sha256=dataset_hash)
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def load_gep_dataset_manifest(path: str | Path, *, verify_artifacts: bool = True) -> dict[str, Any]:
    source = Path(path)
    manifest = json.loads(source.read_text(encoding="utf-8"))
    if manifest.get("dataset_format") != DATASET_FORMAT:
        raise ReplayIntegrityError("Unsupported GEP dataset manifest")
    hash_payload = dict(manifest)
    dataset_hash = hash_payload.pop("dataset_sha256", None)
    dataset_version = hash_payload.pop("dataset_version", None)
    hash_payload.pop("created_at", None)
    expected_hash = hashlib.sha256(_canonical(hash_payload).encode("utf-8")).hexdigest()
    if dataset_hash != expected_hash or dataset_version != f"sha256:{expected_hash}":
        raise ReplayIntegrityError("GEP dataset manifest hash mismatch")
    splits = manifest.get("splits", {})
    train, validation, test = (set(splits.get(key, [])) for key in ("train", "validation", "test"))
    if train & validation or train & test or validation & test:
        raise ReplayIntegrityError("GEP dataset match splits overlap")
    for artifact in manifest.get("artifacts", []):
        if artifact.get("split") not in {"train", "validation", "test"}:
            raise ReplayIntegrityError("GEP artifact has no valid dataset split")
        if artifact["match_id"] not in splits[artifact["split"]]:
            raise ReplayIntegrityError("GEP artifact split does not match its match_id")
        if verify_artifacts:
            artifact_path = source.parent / f"{source.stem}_artifacts" / artifact["path"]
            if not artifact_path.is_file() or sha256_file(artifact_path) != artifact["sha256"]:
                raise ReplayIntegrityError(f"GEP artifact hash mismatch: {artifact['replay_artifact_id']}")
            _read_hash_chain(artifact_path, expected_format=GEP_MATCH_FORMAT)
    return manifest


def iter_gep_observed_snapshots(dataset_path: str | Path, *, split: str | None = None):
    manifest = load_gep_dataset_manifest(dataset_path)
    if split is not None and split not in {"train", "validation", "test"}:
        raise ValueError("split must be train, validation, test, or None")
    for artifact in manifest["artifacts"]:
        if split is not None and artifact["split"] != split:
            continue
        artifact_path = Path(dataset_path).parent / f"{Path(dataset_path).stem}_artifacts" / artifact["path"]
        loaded = _read_hash_chain(artifact_path, expected_format=GEP_MATCH_FORMAT)
        for record in loaded["records"]:
            if record.get("record_type") != "state_snapshot":
                continue
            yield {
                **record["payload"],
                "replay_artifact_id": artifact["replay_artifact_id"],
                "dataset_version": manifest["dataset_version"],
                "source_authority": "overwolf_gep_live_state",
                "authoritative_state_observation": True,
                "authoritative_game_replay": False,
                "combat_calibration_eligible": False,
            }
