from __future__ import annotations

import json
from pathlib import Path

import pytest

from replay.runner import run_deterministic_replay
from replay.recorder import (
    ReplayIntegrityError,
    ReplayRecorder,
    build_dataset_manifest,
    load_replay,
)


def _write_replay(root: Path, episode: int) -> Path:
    recorder = ReplayRecorder(
        root,
        engine_instance_id=f"engine-{episode}",
        episode_id=episode,
        seed=episode,
        code_version="test-commit",
        champion_catalog_path=None,
        item_catalog_path=None,
    )
    recorder.append("reset", {
        "snapshot": {"round": 1, "decision_sequence": 0},
        "observations": [[0.0, 1.0]],
        "action_masks": [{"type_mask": [True, False]}],
    })
    recorder.append("transition", {
        "source_decision": {"round": 1, "decision_sequence": 0},
        "requested_actions": [[6, 0, 0, 0, 0, 0]],
        "effective_action_traces": [{"status": "accepted"}],
        "rewards": [0.0],
        "events": ["COMBAT_OUTCOME_V1:{\"calibration_eligible\":false}"],
        "next_snapshot": {"round": 1, "decision_sequence": 1},
    })
    recorder.close()
    return recorder.path


def test_replay_records_are_hash_chained_and_loadable(tmp_path):
    path = _write_replay(tmp_path, 1)

    loaded = load_replay(path, require_complete=True)

    assert loaded["complete"] is True
    assert [record["record_type"] for record in loaded["records"]] == [
        "manifest", "reset", "transition", "footer"
    ]
    assert loaded["manifest"]["reexecution_eligible"] is False
    assert loaded["manifest"]["seed_available"] is True


def test_replay_tampering_is_detected(tmp_path):
    path = _write_replay(tmp_path, 2)
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = json.loads(lines[1])
    changed["payload"]["observations"][0][0] = 99.0
    lines[1] = json.dumps(changed)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with pytest.raises(ReplayIntegrityError, match="hash mismatch"):
        load_replay(path)


def test_interrupted_replay_is_valid_but_not_complete(tmp_path):
    recorder = ReplayRecorder(
        tmp_path, engine_instance_id="engine", episode_id=3, seed=3,
        code_version="test-commit",
    )
    path = recorder.path
    recorder.append("reset", {"snapshot": {"round": 1}})
    recorder.close("interrupted")

    loaded = load_replay(path)
    assert loaded["complete"] is False
    with pytest.raises(ReplayIntegrityError, match="incomplete"):
        load_replay(path, require_complete=True)


def test_dataset_splits_are_match_disjoint_and_immutable(tmp_path):
    paths = [_write_replay(tmp_path, episode) for episode in range(3, 13)]
    output = tmp_path / "dataset.json"

    manifest = build_dataset_manifest(paths, output, split_seed="stable-seed")

    splits = manifest["splits"]
    assert splits["train"]
    assert splits["validation"]
    assert splits["test"]
    assert not (set(splits["train"]) & set(splits["validation"]))
    assert not (set(splits["train"]) & set(splits["test"]))
    assert not (set(splits["validation"]) & set(splits["test"]))
    assert manifest["replay_count"] == len(paths)
    with pytest.raises(FileExistsError):
        build_dataset_manifest(paths, output, split_seed="stable-seed")


def test_dataset_rejects_fewer_than_three_independent_matches(tmp_path):
    paths = [_write_replay(tmp_path, episode) for episode in range(2)]
    with pytest.raises(ValueError, match="three independent matches"):
        build_dataset_manifest(paths, tmp_path / "dataset.json")


def test_deterministic_runner_checks_reset_and_transition_contract(tmp_path):
    class FakeLobby:
        def __init__(self, seed):
            self.seed = seed
            self._last_dones = [False]
            self._masks = [{"type_mask": [True]}]
            self._snapshot = {
                "episode_id": 9, "decision_sequence": 0,
                "player_decision_sequences": [0], "round": 1, "stage": "2-1",
            }
            self.closed = False

        def reset(self, seed=None):
            assert seed == 5
            return [1.0]

        def get_action_masks(self):
            return self._masks

        def get_snapshot_metadata(self):
            return self._snapshot

        def step(self, actions, timer_enabled=False, timer_expired=False):
            assert actions == [[6, 0, 0, 0, 0, 0]]
            self._snapshot = {
                "episode_id": 9, "decision_sequence": 1,
                "player_decision_sequences": [1], "round": 1, "stage": "2-1",
            }
            info = {
                "players": [], "action_trace": [], "events": [],
                "action_outcome_events": [], "action_rewards": [0.0],
                "combat_rewards": [0.0], "placement_rewards": [0.0],
                "reward_audit": {},
            }
            return [2.0], [0.5], False, info

        def close(self):
            self.closed = True

    recorder = ReplayRecorder(
        tmp_path, engine_instance_id="engine-9", episode_id=9, seed=5,
        code_version="test-commit",
    )
    recorder.append("reset", {
        "snapshot": {
            "episode_id": 9, "decision_sequence": 0,
            "player_decision_sequences": [0], "round": 1, "stage": "2-1",
            "engine_instance_id": "original-engine",
        },
        "observations": [1.0],
        "action_masks": [{"type_mask": [True]}],
    })
    recorder.append("transition", {
        "source_snapshot": {
            "episode_id": 9, "decision_sequence": 0,
            "player_decision_sequences": [0], "round": 1, "stage": "2-1",
        },
        "source_observations": [1.0],
        "source_action_masks": [{"type_mask": [True]}],
        "normalized_actions": [[6, 0, 0, 0, 0, 0]],
        "timer_enabled": False, "timer_expired": False,
        "next_snapshot": {
            "episode_id": 9, "decision_sequence": 1,
            "player_decision_sequences": [1], "round": 1, "stage": "2-1",
            "engine_instance_id": "original-engine",
        },
        "next_observations": [2.0],
        "next_action_masks": [{"type_mask": [True]}],
        "rewards": [0.5], "dones": [False], "lobby_done": False,
        "players": [], "action_traces": [], "events": [],
        "action_outcome_events": [], "action_rewards": [0.0],
        "combat_rewards": [0.0], "placement_rewards": [0.0],
        "reward_audit": {},
    })
    recorder.close()

    report = run_deterministic_replay(
        recorder.path, wrapper_factory=FakeLobby, verify_runtime_identity=False
    )
    assert report["reproduced"] is True
    assert report["transitions_checked"] == 1
