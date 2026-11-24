from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from replay.gep_ingest import (
    GEP_CAPTURE_FORMAT,
    ReplayIntegrityError,
    build_gep_dataset_manifest,
    iter_gep_observed_snapshots,
    load_gep_capture,
    load_gep_dataset_manifest,
)
from replay.recorder import _canonical


def _write_capture(path: Path, match_id: str, *, game_exit: bool = True,
                   capture_error: bool = False) -> Path:
    session_id = f"game-session-{match_id}"
    source_records = [
        ("manifest", {
            "replay_format": GEP_CAPTURE_FORMAT,
            "schema_version": 1,
            "capture_session_id": f"capture-{match_id}",
            "source": "overwolf_gep",
            "game_id": 21570,
            "replay_mode": "observational_only",
            "deterministic_reexecution": False,
            "combat_telemetry_enabled": False,
        }),
        ("canonical_state_snapshot", {
            "capture_session_id": f"capture-{match_id}",
            "game_session_id": session_id,
            "match_id": match_id,
            "game_id": 21570,
            "captured_at": "2026-11-23T10:00:00Z",
            "revision": 1,
            "complete": True,
            "state": {
                "contract": "tft.live-state",
                "contractVersion": 1,
                "matchId": {"known": True, "value": match_id},
                "round": {"known": True, "value": 1},
            },
        }),
        ("canonical_state_snapshot", {
            "capture_session_id": f"capture-{match_id}",
            "game_session_id": session_id,
            "match_id": match_id,
            "game_id": 21570,
            "captured_at": "2026-11-23T10:01:00Z",
            "revision": 2,
            "complete": True,
            "state": {
                "contract": "tft.live-state",
                "contractVersion": 1,
                "matchId": {"known": True, "value": match_id},
                "round": {"known": True, "value": 2},
            },
        }),
    ]
    if capture_error:
        source_records.append(("raw_gep_event", {
            "game_session_id": session_id,
            "match_id": match_id,
            "event": "capture-error",
            "payload": {"message": "provider gap"},
        }))
    if game_exit:
        source_records.append(("raw_gep_event", {
            "capture_session_id": f"capture-{match_id}",
            "game_session_id": session_id,
            "match_id": match_id,
            "game_id": 21570,
            "event": "lifecycle:game-exit",
            "captured_at": "2026-11-23T10:02:00Z",
            "payload": None,
        }))

    path.parent.mkdir(parents=True, exist_ok=True)
    previous = ""
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for sequence, (record_type, payload) in enumerate(source_records + [
            ("footer", {
                "status": "completed" if game_exit and not capture_error else "incomplete",
                "records_before_footer": len(source_records),
                "final_record_sha256": None,
                "complete": game_exit and not capture_error,
            })
        ]):
            if record_type == "footer":
                payload["final_record_sha256"] = previous
            body = {
                "sequence": sequence,
                "record_type": record_type,
                "previous_record_sha256": previous or None,
                "payload": payload,
            }
            body_json = _canonical(body)
            digest = hashlib.sha256((previous + body_json).encode("utf-8")).hexdigest()
            stream.write(body_json[:-1] + ',"record_sha256":' + json.dumps(digest) + "}\n")
            previous = digest
    return path


def test_complete_gep_capture_is_ingested_as_observational_match_artifact(tmp_path):
    capture_path = _write_capture(tmp_path / "capture.jsonl", "match-001")

    capture = load_gep_capture(capture_path)
    assert capture["complete"] is True

    dataset_path = tmp_path / "live_dataset.json"
    manifest = build_gep_dataset_manifest([capture_path], dataset_path) if False else None
    # Three independent matches are required for disjoint train/validation/test.
    captures = [
        _write_capture(tmp_path / f"capture-{index}.jsonl", f"match-{index}")
        for index in range(3)
    ]
    manifest = build_gep_dataset_manifest(captures, dataset_path)

    assert manifest["dataset_format"] == "TFT_GEP_OBSERVATION_DATASET_V1"
    assert manifest["replay_mode"] == "observational_only"
    assert manifest["deterministic_reexecution"] is False
    assert manifest["combat_telemetry_available"] is False
    assert manifest["action_execution_trace_available"] is False
    loaded = load_gep_dataset_manifest(dataset_path)
    assert loaded["dataset_version"] == manifest["dataset_version"]

    snapshots = list(iter_gep_observed_snapshots(dataset_path))
    assert len(snapshots) == 6
    assert all(item["authoritative_state_observation"] is True for item in snapshots)
    assert all(item["authoritative_game_replay"] is False for item in snapshots)
    assert all(item["combat_calibration_eligible"] is False for item in snapshots)
    assert all(item["dataset_version"] == manifest["dataset_version"] for item in snapshots)


def test_gep_capture_tampering_is_detected(tmp_path):
    path = _write_capture(tmp_path / "capture.jsonl", "match-010")
    lines = path.read_text(encoding="utf-8").splitlines()
    record = json.loads(lines[1])
    record["payload"]["state"]["round"]["value"] = 99
    lines[1] = json.dumps(record)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with pytest.raises(ReplayIntegrityError, match="hash mismatch"):
        load_gep_capture(path)


def test_gep_capture_without_game_exit_is_not_ingested(tmp_path):
    path = _write_capture(tmp_path / "capture.jsonl", "match-011", game_exit=False)
    with pytest.raises(ReplayIntegrityError, match="incomplete"):
        load_gep_capture(path)


def test_dataset_rejects_duplicate_matches_to_prevent_split_leakage(tmp_path):
    captures = [
        _write_capture(tmp_path / "capture-a.jsonl", "same-match"),
        _write_capture(tmp_path / "capture-b.jsonl", "same-match"),
        _write_capture(tmp_path / "capture-c.jsonl", "other-match"),
    ]
    with pytest.raises(ValueError, match="Duplicate match_id"):
        build_gep_dataset_manifest(captures, tmp_path / "dataset.json")


def test_dataset_requires_three_independent_live_matches(tmp_path):
    capture = _write_capture(tmp_path / "capture.jsonl", "match-020")
    with pytest.raises(ValueError, match="three independent live matches"):
        build_gep_dataset_manifest([capture], tmp_path / "dataset.json")
