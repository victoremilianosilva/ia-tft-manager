"""Observational replay inspection and deterministic native re-execution."""
from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any, Callable

from .recorder import ReplayIntegrityError, load_replay, sha256_file


ROOT = Path(__file__).resolve().parents[1]


class ReplayCompatibilityError(ValueError):
    """Raised when the current runtime cannot safely re-execute an artifact."""


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
    return str(value)


def _first_difference(expected: Any, actual: Any, path: str = "$",
                      tolerance: float = 1e-6) -> str | None:
    expected = _jsonable(expected)
    actual = _jsonable(actual)
    if isinstance(expected, dict) and isinstance(actual, dict):
        if set(expected) != set(actual):
            return f"{path}: object keys differ"
        for key in sorted(expected):
            difference = _first_difference(expected[key], actual[key],
                                            f"{path}.{key}", tolerance)
            if difference:
                return difference
        return None
    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return f"{path}: array lengths differ ({len(expected)} != {len(actual)})"
        for index, (left, right) in enumerate(zip(expected, actual)):
            difference = _first_difference(left, right, f"{path}[{index}]",
                                            tolerance)
            if difference:
                return difference
        return None
    if (isinstance(expected, (int, float)) and not isinstance(expected, bool) and
            isinstance(actual, (int, float)) and not isinstance(actual, bool)):
        import math
        if math.isclose(float(expected), float(actual), rel_tol=tolerance,
                        abs_tol=tolerance):
            return None
        return f"{path}: numeric mismatch ({expected!r} != {actual!r})"
    if expected != actual:
        return f"{path}: value mismatch ({expected!r} != {actual!r})"
    return None


def validate_runtime_compatibility(manifest: dict[str, Any]) -> None:
    if not manifest.get("reexecution_eligible"):
        raise ReplayCompatibilityError(
            "Replay is observational only: seed, code version or catalog identity is missing"
        )
    try:
        current_version = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT,
            check=True, capture_output=True, text=True, timeout=2,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError) as error:
        raise ReplayCompatibilityError("Cannot determine current source revision") from error
    if current_version != manifest.get("code_version"):
        raise ReplayCompatibilityError(
            "Replay code_version differs from the current checkout"
        )
    expected_catalogs = {
        "champion_catalog_sha256": ROOT / "data" / "units_gerado.json",
        "item_catalog_sha256": ROOT / "data" / "itens.json",
    }
    for key, path in expected_catalogs.items():
        if not path.is_file() or sha256_file(path) != manifest.get("catalogs", {}).get(key):
            raise ReplayCompatibilityError(f"Replay catalog identity mismatch: {key}")
    for relative, expected_hash in manifest.get("contracts", {}).items():
        path = ROOT / relative
        if expected_hash is not None and (
            not path.is_file() or sha256_file(path) != expected_hash
        ):
            raise ReplayCompatibilityError(f"Replay contract identity mismatch: {relative}")


def run_deterministic_replay(
    replay_path: str | Path,
    *,
    wrapper_factory: Callable[..., Any] | None = None,
    verify_runtime_identity: bool = True,
) -> dict[str, Any]:
    loaded = load_replay(replay_path, require_complete=True)
    manifest = loaded["manifest"]
    if manifest.get("source") != "native_lobby_simulation":
        raise ReplayCompatibilityError("Replay source is not the native lobby simulator")
    if verify_runtime_identity:
        validate_runtime_compatibility(manifest)
    if wrapper_factory is None:
        from cpp_lobby_env import CppTFTLobbyWrapper
        wrapper_factory = CppTFTLobbyWrapper

    # Replay execution must not recursively record another replay.
    previous_output = os.environ.pop("TFT_REPLAY_OUTPUT_DIR", None)
    env = None
    try:
        env = wrapper_factory(seed=int(manifest["seed"]))
        reset_records = [
            record for record in loaded["records"]
            if record["record_type"] == "reset"
        ]
        transitions = [
            record for record in loaded["records"]
            if record["record_type"] == "transition"
        ]
        if len(reset_records) != 1 or not transitions:
            raise ReplayIntegrityError("Replay requires one reset and at least one transition")
        reset_record = reset_records[0]
        expected_reset = reset_record["payload"]
        observations = env.reset(seed=int(manifest["seed"]))
        difference = _first_difference(
            expected_reset["observations"], observations, "$.reset.observations"
        )
        if difference:
            return {
                "reproduced": False, "replay_id": manifest["replay_id"],
                "first_divergence": difference, "transitions_checked": 0,
            }
        difference = _first_difference(
            expected_reset["action_masks"], env.get_action_masks(),
            "$.reset.action_masks",
        )
        if difference:
            return {
                "reproduced": False, "replay_id": manifest["replay_id"],
                "first_divergence": difference, "transitions_checked": 0,
            }
        snapshot_keys = ("episode_id", "decision_sequence", "player_decision_sequences",
                         "round", "stage")
        expected_reset_snapshot = {
            key: expected_reset["snapshot"].get(key) for key in snapshot_keys
        }
        actual_reset_snapshot = {
            key: env.get_snapshot_metadata().get(key) for key in snapshot_keys
        }
        difference = _first_difference(
            expected_reset_snapshot, actual_reset_snapshot, "$.reset.snapshot"
        )
        if difference:
            return {
                "reproduced": False, "replay_id": manifest["replay_id"],
                "first_divergence": difference, "transitions_checked": 0,
            }

        checked = 0
        for record in transitions:
            payload = record["payload"]
            current = env.get_snapshot_metadata()
            difference = _first_difference(
                payload["source_observations"], observations,
                f"$.transition[{checked}].source_observations",
            )
            if difference:
                return {
                    "reproduced": False, "replay_id": manifest["replay_id"],
                    "first_divergence": difference, "transitions_checked": checked,
                }
            difference = _first_difference(
                payload["source_action_masks"], env.get_action_masks(),
                f"$.transition[{checked}].source_action_masks",
            )
            if difference:
                return {
                    "reproduced": False, "replay_id": manifest["replay_id"],
                    "first_divergence": difference, "transitions_checked": checked,
                }
            for key in ("episode_id", "decision_sequence", "player_decision_sequences",
                        "round", "stage"):
                difference = _first_difference(
                    payload["source_snapshot"].get(key), current.get(key),
                    f"$.transition[{checked}].source_snapshot.{key}",
                )
                if difference:
                    return {
                        "reproduced": False, "replay_id": manifest["replay_id"],
                        "first_divergence": difference, "transitions_checked": checked,
                    }
            observations, rewards, lobby_done, info = env.step(
                payload["normalized_actions"],
                timer_enabled=bool(payload.get("timer_enabled", False)),
                timer_expired=bool(payload.get("timer_expired", False)),
            )
            comparisons = (
                ("next_observations", observations),
                ("rewards", rewards),
                ("lobby_done", lobby_done),
                ("dones", env._last_dones),
                ("next_action_masks", env.get_action_masks()),
                ("next_snapshot", {
                    key: env.get_snapshot_metadata().get(key)
                    for key in snapshot_keys
                }),
                ("players", info["players"]),
                ("action_traces", info["action_trace"]),
                ("events", info["events"]),
                ("action_outcome_events", info["action_outcome_events"]),
                ("action_rewards", info["action_rewards"]),
                ("combat_rewards", info["combat_rewards"]),
                ("placement_rewards", info["placement_rewards"]),
                ("reward_audit", info["reward_audit"]),
            )
            for key, actual in comparisons:
                expected = payload[key]
                if key == "next_snapshot":
                    expected = {name: payload["next_snapshot"].get(name) for name in snapshot_keys}
                difference = _first_difference(
                    expected, actual, f"$.transition[{checked}].{key}"
                )
                if difference:
                    return {
                        "reproduced": False, "replay_id": manifest["replay_id"],
                        "first_divergence": difference, "transitions_checked": checked,
                    }
            checked += 1
        return {
            "reproduced": True, "replay_id": manifest["replay_id"],
            "transitions_checked": checked, "first_divergence": None,
        }
    finally:
        if env is not None:
            env.close()
        if previous_output is not None:
            os.environ["TFT_REPLAY_OUTPUT_DIR"] = previous_output
