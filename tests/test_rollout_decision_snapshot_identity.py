"""Identity correlation tests for vector auto-reset and PPO rollout storage."""

import numpy as np
import pytest
import torch

from rollout import RolloutBuffer
from vector_lobby_env import LobbyVectorEnv
from trainer import Trainer


class FakeIdentityEnv:
    def __init__(self):
        self.episode_id = 0
        self.decision_sequence = 0
        self.players = [
            type("Player", (), {"alive": True})() for _ in range(8)
        ]
        self._metadata = None

    def reset(self):
        self.episode_id += 1
        self.decision_sequence += 1
        self._metadata = {
            "engine_instance_id": "engine-A",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "round": 0,
            "stage": 1,
            "snapshot_kind": "reset",
        }
        return np.full((8, 3), self.episode_id, dtype=np.float32)

    def get_snapshot_metadata(self):
        return dict(self._metadata)

    def step(self, _actions):
        self.decision_sequence += 1
        self._metadata = {
            "engine_instance_id": "engine-A",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "round": 5,
            "stage": 2,
            "snapshot_kind": "step",
        }
        return (
            np.full((8, 3), 99, dtype=np.float32),
            np.full(8, 0.75, dtype=np.float32),
            True,
            {
                "decision_snapshot": dict(self._metadata),
                "players": [{"player_id": i, "alive": True} for i in range(8)],
                "action_trace": [
                    {
                        "requested_action": [6, 0, 0, 0, 0, 0],
                        "effective_action": [6, 0, 0, 0, 0, 0],
                        "handler_applied": True,
                        "status_reason": "applied",
                    }
                    for _ in range(8)
                ],
            },
        )

    def get_public_state(self):
        return {"players": [], "round": 5}

    def close(self):
        pass


def test_terminal_auto_reset_keeps_transition_and_next_episode_identity_separate():
    env = LobbyVectorEnv([FakeIdentityEnv])
    try:
        initial_obs = env.reset()
        assert np.all(initial_obs == 1)
        assert env.get_snapshot_metadata()[0]["episode_id"] == 1

        observations, rewards, dones, infos = env.step(
            [[{"type": 6} for _ in range(8)]]
        )

        assert np.all(observations == 2)
        assert np.all(rewards == 0.75)
        assert np.all(dones)

        info = infos[0]
        assert info["step_result_snapshot"]["episode_id"] == 1
        assert info["step_result_snapshot"]["round"] == 5
        assert info["step_result_snapshot"]["decision_sequence"] == 2
        assert len(info["action_trace"]) == 8
        assert info["action_trace"][0]["handler_applied"] is True
        assert info["next_snapshot"]["episode_id"] == 2
        assert info["next_snapshot"]["decision_sequence"] == 3
        assert info["next_snapshot"]["snapshot_kind"] == "reset"
        assert env.get_snapshot_metadata()[0]["episode_id"] == 2
        assert env.get_snapshot_metadata()[0]["decision_sequence"] == 3
    finally:
        env.close()


def test_rollout_buffer_preserves_per_agent_snapshot_identity():
    buffer = RolloutBuffer(
        num_steps=2,
        num_envs=2,
        obs_dim=3,
        action_dim=6,
        device=torch.device("cpu"),
    )
    metadata = [
        {
            "engine_instance_id": "engine-A",
            "episode_id": 7,
            "decision_sequence": 12,
            "round": 4,
            "stage": 2,
            "snapshot_kind": "step",
            "lobby_index": 0,
            "player_id": player_id,
            "mask_snapshot_hash": "a" * 64,
            "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
        }
        for player_id in range(2)
    ]
    result_metadata = [
        {
            **item,
            "decision_sequence": 13,
            "snapshot_kind": "step_result",
            "action_trace": {
                "requested_action": [6, 0, 0, 0, 0, 0],
                "effective_action": [6, 0, 0, 0, 0, 0],
                "handler_applied": True,
                "status_reason": "applied",
            },
        }
        for item in metadata
    ]
    next_metadata = [dict(item) for item in result_metadata]

    buffer.add(
        obs=np.zeros((2, 3), dtype=np.float32),
        actions=np.tile(np.array([6, 0, 0, 0, 0, 0], dtype=np.int64), (2, 1)),
        logprobs=np.zeros(2, dtype=np.float32),
        rewards=np.zeros(2, dtype=np.float32),
        dones=np.zeros(2, dtype=np.float32),
        values=np.zeros(2, dtype=np.float32),
        masks_dict={},
        snapshot_metadata=metadata,
        result_snapshot_metadata=result_metadata,
        next_snapshot_metadata=next_metadata,
    )

    metadata[0]["episode_id"] = 999
    stored = buffer.snapshot_metadata[0]
    assert stored[0]["episode_id"] == 7
    assert stored[0]["decision_sequence"] == 12
    assert stored[0]["player_id"] == 0
    assert stored[1]["player_id"] == 1
    assert stored[1]["engine_instance_id"] == "engine-A"
    assert buffer.result_snapshot_metadata[0][0]["decision_sequence"] == 13
    assert buffer.result_snapshot_metadata[0][0]["action_trace"]["handler_applied"] is True
    assert buffer.next_snapshot_metadata[0][0]["decision_sequence"] == 13

    batch = next(buffer.get_batches(batch_size=2))
    assert len(batch["snapshot_metadata"]) == 2
    assert all(item["mask_snapshot_hash"] == "a" * 64 for item in batch["snapshot_metadata"])
    assert all(item["decision_sequence"] == 13 for item in batch["result_snapshot_metadata"])

    buffer.reset()
    assert buffer.snapshot_metadata[0] is None
    assert buffer.result_snapshot_metadata[0] is None
    assert buffer.next_snapshot_metadata[0] is None


def test_rollout_buffer_rejects_incomplete_snapshot_identity():
    buffer = RolloutBuffer(
        num_steps=1,
        num_envs=1,
        obs_dim=3,
        action_dim=6,
        device=torch.device("cpu"),
    )
    with pytest.raises(ValueError, match="campos obrigatórios"):
        buffer.add(
            obs=np.zeros((1, 3), dtype=np.float32),
            actions=np.zeros((1, 6), dtype=np.int64),
            logprobs=np.zeros(1, dtype=np.float32),
            rewards=np.zeros(1, dtype=np.float32),
            dones=np.zeros(1, dtype=np.float32),
            values=np.zeros(1, dtype=np.float32),
            masks_dict={},
            snapshot_metadata=[{"episode_id": 1, "player_id": 0}],
            result_snapshot_metadata=[{
                "engine_instance_id": "engine-A", "episode_id": 1,
                "decision_sequence": 2, "player_id": 0, "lobby_index": 0,
            }],
            next_snapshot_metadata=[{
                "engine_instance_id": "engine-A", "episode_id": 1,
                "decision_sequence": 2, "player_id": 0, "lobby_index": 0,
            }],
        )


def test_rollout_buffer_preserves_terminal_result_and_new_episode_identity():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "b" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_id": 0, "lobby_index": 0,
    }
    next_state = {
        "engine_instance_id": "engine-A", "episode_id": 5,
        "decision_sequence": 23, "player_id": 0, "lobby_index": 0,
    }
    buffer.add(
        obs=np.zeros((1, 3), dtype=np.float32),
        actions=np.zeros((1, 6), dtype=np.int64),
        logprobs=np.zeros(1, dtype=np.float32),
        rewards=np.ones(1, dtype=np.float32),
        dones=np.ones(1, dtype=np.float32),
        values=np.zeros(1, dtype=np.float32),
        masks_dict={},
        snapshot_metadata=[decision],
        result_snapshot_metadata=[result],
        next_snapshot_metadata=[next_state],
    )
    assert buffer.snapshot_metadata[0][0]["decision_sequence"] == 21
    assert buffer.result_snapshot_metadata[0][0]["decision_sequence"] == 22
    assert buffer.next_snapshot_metadata[0][0]["episode_id"] == 5


def test_rollout_buffer_rejects_result_identity_from_another_episode():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "c" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 5,
        "decision_sequence": 22, "player_id": 0, "lobby_index": 0,
    }
    with pytest.raises(ValueError, match="Episode divergente"):
        buffer.add(
            obs=np.zeros((1, 3), dtype=np.float32),
            actions=np.zeros((1, 6), dtype=np.int64),
            logprobs=np.zeros(1, dtype=np.float32),
            rewards=np.ones(1, dtype=np.float32),
            dones=np.ones(1, dtype=np.float32),
            values=np.zeros(1, dtype=np.float32),
            masks_dict={},
            snapshot_metadata=[decision],
            result_snapshot_metadata=[result],
            next_snapshot_metadata=[result],
        )


def test_mask_snapshot_hash_is_deterministic_and_sensitive_to_payload():
    masks = {
        name: torch.zeros((2, *shape), dtype=torch.bool)
        for name, shape in Trainer.MASK_SHAPES.items()
    }
    first = Trainer._hash_mask_rows(masks)
    second = Trainer._hash_mask_rows(masks)
    assert first == second
    assert first[0] == first[1]

    masks["type_mask"][1, 3] = True
    changed = Trainer._hash_mask_rows(masks)
    assert changed[0] == first[0]
    assert changed[1] != first[1]


def test_rollout_rejects_action_trace_that_differs_from_ppo_action():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "d" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        },
    }
    next_state = {key: value for key, value in result.items() if key != "action_trace"}

    with pytest.raises(ValueError, match="Ação PPO diverge"):
        buffer.add(
            obs=np.zeros((1, 3), dtype=np.float32),
            actions=np.array([[0, 0, 0, 0, 0, 0]], dtype=np.int64),
            logprobs=np.zeros(1, dtype=np.float32),
            rewards=np.zeros(1, dtype=np.float32),
            dones=np.zeros(1, dtype=np.float32),
            values=np.zeros(1, dtype=np.float32),
            masks_dict={},
            snapshot_metadata=[decision],
            result_snapshot_metadata=[result],
            next_snapshot_metadata=[next_state],
        )


def test_rollout_rejects_malformed_requested_action_trace():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "e" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {"requested_action": [6, 0]},
    }
    next_state = {key: value for key, value in result.items() if key != "action_trace"}

    with pytest.raises(ValueError, match="deve conter 6 parâmetros"):
        buffer.add(
            obs=np.zeros((1, 3), dtype=np.float32),
            actions=np.array([[6, 0, 0, 0, 0, 0]], dtype=np.int64),
            logprobs=np.zeros(1, dtype=np.float32),
            rewards=np.zeros(1, dtype=np.float32),
            dones=np.zeros(1, dtype=np.float32),
            values=np.zeros(1, dtype=np.float32),
            masks_dict={},
            snapshot_metadata=[decision],
            result_snapshot_metadata=[result],
            next_snapshot_metadata=[next_state],
        )


def _add_rollout_with_action_trace_for_validation(action_trace):
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "f" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": action_trace,
    }
    next_state = {key: value for key, value in result.items() if key != "action_trace"}
    buffer.add(
        obs=np.zeros((1, 3), dtype=np.float32),
        actions=np.array([[6, 0, 0, 0, 0, 0]], dtype=np.int64),
        logprobs=np.zeros(1, dtype=np.float32),
        rewards=np.zeros(1, dtype=np.float32),
        dones=np.zeros(1, dtype=np.float32),
        values=np.zeros(1, dtype=np.float32),
        masks_dict={},
        snapshot_metadata=[decision],
        result_snapshot_metadata=[result],
        next_snapshot_metadata=[next_state],
    )


def test_rollout_rejects_malformed_effective_action_trace():
    trace = {
        "requested_action": [6, 0, 0, 0, 0, 0],
        "effective_action": [6, 0],
        "handler_applied": True,
        "status_reason": "applied",
    }
    with pytest.raises(ValueError, match="effective_action deve conter 6 parâmetros"):
        _add_rollout_with_action_trace_for_validation(trace)


def test_rollout_rejects_non_boolean_action_handler_status():
    trace = {
        "requested_action": [6, 0, 0, 0, 0, 0],
        "effective_action": [6, 0, 0, 0, 0, 0],
        "handler_applied": 1,
        "status_reason": "applied",
    }
    with pytest.raises(ValueError, match="handler_applied deve ser booleano"):
        _add_rollout_with_action_trace_for_validation(trace)


def test_rollout_rejects_empty_action_status_reason():
    trace = {
        "requested_action": [6, 0, 0, 0, 0, 0],
        "effective_action": [6, 0, 0, 0, 0, 0],
        "handler_applied": False,
        "status_reason": "   ",
    }
    with pytest.raises(ValueError, match="status_reason deve ser texto não vazio"):
        _add_rollout_with_action_trace_for_validation(trace)