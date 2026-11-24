"""Immutable, hash-chained recorder for authoritative native lobby transitions."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPLAY_FORMAT = "TFT_NATIVE_LOBBY_REPLAY_V1"
SCHEMA_VERSION = 1


class ReplayIntegrityError(ValueError):
    """Raised when a replay is malformed, reordered, or has been modified."""


def _jsonable(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if hasattr(value, "tolist"):
        return _jsonable(value.tolist())
    if hasattr(value, "item"):
        return _jsonable(value.item())
    raise TypeError(f"Replay contains unsupported value: {type(value).__name__}")


def _canonical(value: dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class ReplayRecorder:
    """Append-only recorder. Each record commits to the previous record hash."""

    def __init__(self, output_dir: str | Path, *, engine_instance_id: str,
                 episode_id: int, seed: int | None,
                 champion_catalog_path: str | Path | None = None,
                 item_catalog_path: str | Path | None = None,
                 code_version: str | None = None):
        self.output_dir = Path(output_dir).expanduser().resolve()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.replay_id = str(uuid.uuid4())
        self.path = self.output_dir / f"replay-{self.replay_id}.jsonl"
        self.engine_instance_id = str(engine_instance_id)
        self.episode_id = int(episode_id)
        self._sequence = 0
        self._previous_hash = ""
        self._closed = False
        catalogs = {}
        for key, path in (
            ("champion_catalog_sha256", champion_catalog_path),
            ("item_catalog_sha256", item_catalog_path),
        ):
            if path is not None and Path(path).is_file():
                catalogs[key] = sha256_file(path)
            else:
                catalogs[key] = None
        version = code_version or os.environ.get("TFT_REPLAY_CODE_VERSION") or os.environ.get("GIT_COMMIT_SHA")
        if not version:
            try:
                version = subprocess.run(
                    ["git", "rev-parse", "HEAD"],
                    cwd=Path(__file__).resolve().parents[1],
                    check=True, capture_output=True, text=True, timeout=2,
                ).stdout.strip()
            except (OSError, subprocess.SubprocessError):
                version = None
        self.manifest = {
            "replay_format": REPLAY_FORMAT,
            "schema_version": SCHEMA_VERSION,
            "replay_id": self.replay_id,
            "source": "native_lobby_simulation",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "engine_instance_id": self.engine_instance_id,
            "episode_id": self.episode_id,
            "match_key": f"{self.engine_instance_id}:{self.episode_id}",
            "seed": int(seed) if seed is not None else None,
            "seed_available": seed is not None,
            "deterministic": True,
            "code_version": version or "unknown",
            "catalogs": catalogs,
            "contracts": {
                relative: sha256_file(Path(__file__).resolve().parents[1] / relative)
                if (Path(__file__).resolve().parents[1] / relative).is_file() else None
                for relative in (
                    "action_contract.py", "decision_identity.py", "reward_audit.py",
                    "cpp/include/decision/ActionMaskEngine.hpp",
                )
            },
            "runtime_config": {
                key: os.environ.get(key)
                for key in (
                    "TFT_ABLATE_ITEM_ACTIONS",
                    "TFT_COMPOSITION_INTELLIGENCE_SHADOW",
                )
            },
            "reexecution_eligible": seed is not None and bool(version) and all(catalogs.values()),
        }
        # Exclusive creation prevents accidental overwrite of an existing artifact.
        self._stream = self.path.open("x", encoding="utf-8", newline="\n")
        self.append("manifest", self.manifest)

    def append(self, record_type: str, payload: dict[str, Any]) -> str:
        if self._closed:
            raise RuntimeError("Cannot append to a closed replay")
        if not isinstance(record_type, str) or not record_type:
            raise ValueError("Replay record_type must be non-empty")
        body = {
            "sequence": self._sequence,
            "record_type": record_type,
            "previous_record_sha256": self._previous_hash or None,
            "payload": _jsonable(payload),
        }
        record_hash = hashlib.sha256(
            (self._previous_hash + _canonical(body)).encode("utf-8")
        ).hexdigest()
        record = dict(body, record_sha256=record_hash)
        self._stream.write(_canonical(record) + "\n")
        self._stream.flush()
        os.fsync(self._stream.fileno())
        self._sequence += 1
        self._previous_hash = record_hash
        return record_hash

    def close(self, status: str = "completed") -> None:
        if self._closed:
            return
        if status not in {"completed", "interrupted", "episode_reset", "error"}:
            raise ValueError(f"Unsupported replay close status: {status}")
        self.append("footer", {
            "status": status,
            "records_before_footer": self._sequence,
            "final_record_sha256": self._previous_hash,
            "complete": status == "completed",
        })
        self._stream.close()
        self._closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close("error" if exc_type else "completed")


def load_replay(path: str | Path, *, require_complete: bool = False) -> dict[str, Any]:
    source = Path(path)
    records = []
    previous_hash = ""
    with source.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ReplayIntegrityError(
                    f"Invalid JSON at line {line_number}: {error.msg}"
                ) from error
            if not isinstance(record, dict):
                raise ReplayIntegrityError(f"Record at line {line_number} is not an object")
            expected_sequence = len(records)
            if record.get("sequence") != expected_sequence:
                raise ReplayIntegrityError(f"Non-monotonic replay sequence at line {line_number}")
            if record.get("previous_record_sha256") != (previous_hash or None):
                raise ReplayIntegrityError(f"Broken replay hash link at line {line_number}")
            supplied_hash = record.get("record_sha256")
            marker = ',\\\"record_sha256\\\":'
            marker_index = line.rstrip("\\r\\n").rfind(marker)
            if marker_index < 0 or marker_index + len(marker) >= len(line):
                raise ReplayIntegrityError(f"Missing terminal record hash at line {line_number}")
            body_json = line.rstrip("\\r\\n")[:marker_index] + "}"
            expected_hash = hashlib.sha256(
                (previous_hash + body_json).encode("utf-8")
            ).hexdigest()
            if supplied_hash != expected_hash:
                raise ReplayIntegrityError(f"Replay hash mismatch at line {line_number}")
            previous_hash = supplied_hash
            records.append(record)

    if not records or records[0].get("record_type") != "manifest":
        raise ReplayIntegrityError("Replay must start with a manifest record")
    manifest = records[0].get("payload")
    if not isinstance(manifest, dict) or manifest.get("replay_format") != REPLAY_FORMAT:
        raise ReplayIntegrityError("Unsupported replay manifest")
    footer = records[-1] if records[-1].get("record_type") == "footer" else None
    complete = bool(footer and footer.get("payload", {}).get("complete") is True)
    if footer:
        footer_payload = footer.get("payload", {})
        if footer_payload.get("records_before_footer") != len(records) - 1:
            raise ReplayIntegrityError("Replay footer record count mismatch")
        if footer_payload.get("final_record_sha256") != footer.get("previous_record_sha256"):
            raise ReplayIntegrityError("Replay footer final hash mismatch")
        if footer_payload.get("complete") is not (footer_payload.get("status") == "completed"):
            raise ReplayIntegrityError("Replay footer status/completeness mismatch")
    if require_complete and not complete:
        raise ReplayIntegrityError("Replay is valid but incomplete/non-terminal")
    return {
        "path": str(source),
        "manifest": manifest,
        "records": records,
        "complete": complete,
        "record_count": len(records),
        "final_record_sha256": previous_hash,
    }


def build_dataset_manifest(replay_paths: Iterable[str | Path], output_path: str | Path,
                           *, split_seed: str = "tft-replay-split-v1") -> dict[str, Any]:
    replays = [load_replay(path, require_complete=True) for path in replay_paths]
    if not replays:
        raise ValueError("At least one complete replay is required")
    replay_ids = [item["manifest"]["replay_id"] for item in replays]
    if len(set(replay_ids)) != len(replay_ids):
        raise ValueError("Duplicate replay_id in dataset input")
    grouped: dict[str, list[dict[str, Any]]] = {}
    for replay in replays:
        manifest = replay["manifest"]
        match_key = manifest.get("match_key")
        if not isinstance(match_key, str) or not match_key:
            raise ValueError("Replay is missing a stable match_key")
        grouped.setdefault(match_key, []).append(replay)
    match_keys = sorted(grouped)
    if len(match_keys) < 3:
        raise ValueError("Train/validation/test require at least three independent matches")
    ranked = sorted(match_keys, key=lambda key: hashlib.sha256(
        f"{split_seed}:{key}".encode("utf-8")
    ).hexdigest())
    count = len(ranked)
    test_count = max(1, round(count * 0.1))
    validation_count = max(1, round(count * 0.1))
    while test_count + validation_count >= count:
        if test_count >= validation_count:
            test_count -= 1
        else:
            validation_count -= 1
    test_keys = set(ranked[:test_count])
    validation_keys = set(ranked[test_count:test_count + validation_count])
    train_keys = set(ranked[test_count + validation_count:])
    split_by_match = {
        key: ("test" if key in test_keys else
              "validation" if key in validation_keys else "train")
        for key in match_keys
    }

    artifacts = []
    for replay in replays:
        manifest = replay["manifest"]
        artifacts.append({
            "replay_id": manifest["replay_id"],
            "path": str(Path(replay["path"]).name),
            "sha256": sha256_file(replay["path"]),
            "match_key": manifest["match_key"],
            "engine_instance_id": manifest["engine_instance_id"],
            "episode_id": manifest["episode_id"],
            "record_count": replay["record_count"],
            "split": split_by_match[manifest["match_key"]],
            "reexecution_eligible": manifest.get("reexecution_eligible", False),
        })
    payload = {
        "dataset_format": "TFT_REPLAY_DATASET_V1",
        "schema_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "split_seed": split_seed,
        "match_count": len(match_keys),
        "replay_count": len(artifacts),
        "splits": {
            "train": sorted(train_keys),
            "validation": sorted(validation_keys),
            "test": sorted(test_keys),
        },
        "artifacts": sorted(artifacts, key=lambda item: item["replay_id"]),
    }
    dataset_hash = hashlib.sha256(_canonical(payload).encode("utf-8")).hexdigest()
    result = dict(payload, dataset_version=f"sha256:{dataset_hash}",
                  dataset_sha256=dataset_hash)
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    return result
