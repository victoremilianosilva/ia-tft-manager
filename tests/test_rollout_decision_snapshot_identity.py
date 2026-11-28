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
        self.player_decision_sequences = [0] * 8
        self.players = [
            type("Player", (), {"alive": True})() for _ in range(8)
        ]
        self._metadata = None

    def reset(self):
        self.episode_id += 1
        self.decision_sequence += 1
        self.player_decision_sequences = [value + 1 for value in self.player_decision_sequences]
        self._metadata = {
            "engine_instance_id": "engine-A",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "player_decision_sequences": list(self.player_decision_sequences),
            "round": 0,
            "stage": 1,
            "snapshot_kind": "reset",
        }
        return np.full((8, 3), self.episode_id, dtype=np.float32)

    def get_snapshot_metadata(self):
        return dict(self._metadata)

    def step(self, _actions):
        self.decision_sequence += 1
        self.player_decision_sequences = [value + 1 for value in self.player_decision_sequences]
        self._metadata = {
            "engine_instance_id": "engine-A",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "player_decision_sequences": list(self.player_decision_sequences),
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
                        "player_id": player_id,
                        "requested_action": [6, 0, 0, 0, 0, 0],
                        "effective_action": [6, 0, 0, 0, 0, 0],
                        "handler_applied": True,
                        "status_reason": "applied",
                    }
                    for player_id in range(8)
                ],
                "action_outcome_events": [
                    {
                        "contract_id": "tft.engine.action-outcome-event",
                        "contract_version": 1,
                        "event_id": f"engine-A/episode/{self.episode_id}/decision/{self.player_decision_sequences[player_id] - 1}/player/{player_id}/action",
                        "engine_instance_id": "engine-A",
                        "episode_id": self.episode_id,
                        "player_id": player_id,
                        "source_player_decision_sequence": self.player_decision_sequences[player_id] - 1,
                        "outcome_player_decision_sequence": self.player_decision_sequences[player_id],
                        "requested_action": [6, 0, 0, 0, 0, 0],
                        "normalized_action": [6, 0, 0, 0, 0, 0],
                        "effective_action": [6, 0, 0, 0, 0, 0],
                        "mask_permitted": True,
                        "preflight_accepted": True,
                        "handler_applied": True,
                        "decision_advanced": True,
                        "execution_status": "applied",
                        "affected_unit_uuids": [],
                        "status_reason": "applied",
                    }
                    for player_id in range(8)
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
        assert info["step_result_snapshot"]["player_decision_sequences"] == [2] * 8
        assert len(info["action_trace"]) == 8
        assert info["action_trace"][0]["handler_applied"] is True
        assert info["next_snapshot"]["episode_id"] == 2
        assert info["next_snapshot"]["decision_sequence"] == 3
        assert info["next_snapshot"]["player_decision_sequences"] == [3] * 8
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
            "player_decision_sequence": 12,
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
            "player_decision_sequence": 13,
            "snapshot_kind": "step_result",
            "action_trace": {
                "player_id": item["player_id"],
                "requested_action": [6, 0, 0, 0, 0, 0],
                "effective_action": [6, 0, 0, 0, 0, 0],
                "handler_applied": True,
                "status_reason": "applied",
            },
            "action_outcome_event": {
                "contract_id": "tft.engine.action-outcome-event",
                "contract_version": 1,
                "event_id": f"engine-A/episode/{item['episode_id']}/decision/12/player/{item['player_id']}/action",
                "engine_instance_id": item["engine_instance_id"],
                "episode_id": item["episode_id"],
                "player_id": item["player_id"],
                "source_player_decision_sequence": 12,
                "outcome_player_decision_sequence": 13,
                "requested_action": [6, 0, 0, 0, 0, 0],
                "normalized_action": [6, 0, 0, 0, 0, 0],
                "effective_action": [6, 0, 0, 0, 0, 0],
                "mask_permitted": True,
                "preflight_accepted": True,
                "handler_applied": True,
                "decision_advanced": True,
                "execution_status": "applied",
                "affected_unit_uuids": [],
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

    batch = next(buffer.get_batches(batch_size=2, include_metadata=True))
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
                "decision_sequence": 2, "player_decision_sequence": 2, "player_id": 0, "lobby_index": 0,
            }],
            next_snapshot_metadata=[{
                "engine_instance_id": "engine-A", "episode_id": 1,
                "decision_sequence": 2, "player_decision_sequence": 2, "player_id": 0, "lobby_index": 0,
            }],
        )


def test_rollout_buffer_preserves_terminal_result_and_new_episode_identity():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "b" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {
            "player_id": 0,
            "requested_action": [0, 0, 0, 0, 0, 0],
            "effective_action": [0, 0, 0, 0, 0, 0],
            "handler_applied": False, "status_reason": "rejected",
        },
        "action_outcome_event": {
            "contract_id": "tft.engine.action-outcome-event",
            "contract_version": 1,
            "event_id": "engine-A/episode/4/decision/21/player/0/action",
            "engine_instance_id": "engine-A", "episode_id": 4, "player_id": 0,
            "source_player_decision_sequence": 21, "outcome_player_decision_sequence": 22,
            "requested_action": [0, 0, 0, 0, 0, 0],
            "normalized_action": [0, 0, 0, 0, 0, 0],
            "effective_action": [0, 0, 0, 0, 0, 0],
            "mask_permitted": True, "preflight_accepted": True, "handler_applied": False,
            "decision_advanced": True, "execution_status": "no_effect",
            "affected_unit_uuids": [], "status_reason": "rejected",
        },
    }
    next_state = {
        "engine_instance_id": "engine-A", "episode_id": 5,
        "decision_sequence": 23, "player_decision_sequence": 23, "player_id": 0, "lobby_index": 0,
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
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "c" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 5,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
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
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "d" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {
            "player_id": 0,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        },
    }
    next_state = {key: value for key, value in result.items() if key not in ("action_trace", "action_outcome_event")}

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
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "e" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {"player_id": 0, "requested_action": [6, 0]},
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
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "f" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {"player_id": 0, **action_trace},
        "action_outcome_event": {
            "contract_id": "tft.engine.action-outcome-event",
            "contract_version": 1,
            "event_id": "engine-A/episode/4/decision/21/player/0/action",
            "engine_instance_id": "engine-A", "episode_id": 4, "player_id": 0,
            "source_player_decision_sequence": 21,
            "outcome_player_decision_sequence": 22,
            "requested_action": action_trace.get("requested_action"),
            "normalized_action": action_trace.get("requested_action"),
            "effective_action": action_trace.get("effective_action"),
            "mask_permitted": True, "preflight_accepted": True, "handler_applied": action_trace.get("handler_applied"),
            "decision_advanced": True,
            "execution_status": "applied",
            "affected_unit_uuids": [],
            "status_reason": action_trace.get("status_reason"),
        },
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

def test_rollout_rejects_transition_without_native_action_trace():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "a" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
    }
    with pytest.raises(ValueError, match="action_trace é obrigatório"):
        buffer.add(
            obs=np.zeros((1, 3), dtype=np.float32),
            actions=np.zeros((1, 6), dtype=np.int64),
            logprobs=np.zeros(1, dtype=np.float32),
            rewards=np.zeros(1, dtype=np.float32),
            dones=np.zeros(1, dtype=np.float32),
            values=np.zeros(1, dtype=np.float32),
            masks_dict={},
            snapshot_metadata=[decision],
            result_snapshot_metadata=[result],
            next_snapshot_metadata=[result],
        )

def test_rollout_rejects_action_trace_owned_by_another_player():
    trace = {
        "player_id": 1,
        "requested_action": [6, 0, 0, 0, 0, 0],
        "effective_action": [6, 0, 0, 0, 0, 0],
        "handler_applied": True,
        "status_reason": "applied",
    }
    with pytest.raises(ValueError, match="player_id não corresponde"):
        _add_rollout_with_action_trace_for_validation(trace)



def test_integrated_vector_to_rollout_preserves_terminal_transition_correlation():
    env = LobbyVectorEnv([FakeIdentityEnv])
    buffer = RolloutBuffer(
        num_steps=1,
        num_envs=8,
        obs_dim=3,
        action_dim=6,
        device=torch.device("cpu"),
    )
    try:
        observations = env.reset()
        decision_metadata = Trainer._expand_lobby_snapshot_metadata(
            env.get_snapshot_metadata(), 8, "snapshot da decisão PPO"
        )

        # Build the complete typed mask bundle consumed by the policy. The
        # test uses PASS as the selected legal action for all eight players.
        masks = {
            name: torch.zeros((8, *shape), dtype=torch.bool)
            for name, shape in Trainer.MASK_SHAPES.items()
        }
        masks["type_mask"][:, 6] = True
        for metadata, mask_hash in zip(
            decision_metadata, Trainer._hash_mask_rows(masks)
        ):
            metadata["mask_snapshot_hash"] = mask_hash
            metadata["mask_snapshot_hash_algorithm"] = "tft-action-mask-snapshot-v1"

        actions = torch.tensor([[6, 0, 0, 0, 0, 0]] * 8, dtype=torch.long)
        # Exercise the production PPO-action-to-native-payload adapter rather
        # than hand-constructing the dictionaries accepted by the fake Engine.
        trainer = Trainer.__new__(Trainer)
        trainer.num_envs = 1
        trainer.num_agents = 8
        trainer.PLAYERS_PER_LOBBY = 8
        trainer.ACTION_DIM = 6
        lobby_actions = trainer._actions_to_lobby_format(actions)
        next_observations, rewards, dones, infos = env.step(lobby_actions)

        result_metadata = Trainer._expand_lobby_snapshot_metadata(
            [infos[0]["step_result_snapshot"]], 8, "snapshot de resultado"
        )
        next_metadata = Trainer._expand_lobby_snapshot_metadata(
            [infos[0]["next_snapshot"]], 8, "próxima observação"
        )
        Trainer._attach_native_action_traces(
            result_metadata,
            infos,
            players_per_lobby=8,
        )
        for player_id, metadata in enumerate(result_metadata):
            assert metadata["action_trace"]["player_id"] == player_id

        buffer.add(
            obs=observations.reshape(8, 3),
            actions=actions,
            logprobs=torch.zeros(8),
            rewards=torch.as_tensor(rewards.reshape(8)),
            dones=torch.as_tensor(dones.reshape(8), dtype=torch.float32),
            values=torch.zeros(8),
            masks_dict=masks,
            snapshot_metadata=decision_metadata,
            result_snapshot_metadata=result_metadata,
            next_snapshot_metadata=next_metadata,
        )

        stored_decisions = buffer.snapshot_metadata[0]
        stored_results = buffer.result_snapshot_metadata[0]
        stored_next = buffer.next_snapshot_metadata[0]
        assert len(stored_decisions) == len(stored_results) == len(stored_next) == 8
        for player_id in range(8):
            assert stored_decisions[player_id]["player_id"] == player_id
            assert stored_decisions[player_id]["episode_id"] == 1
            assert stored_decisions[player_id]["decision_sequence"] == 1
            assert stored_decisions[player_id]["mask_snapshot_hash"] == Trainer._hash_mask_rows(masks)[player_id]
            assert stored_results[player_id]["player_id"] == player_id
            assert stored_results[player_id]["episode_id"] == 1
            assert stored_results[player_id]["decision_sequence"] == 2
            assert stored_results[player_id]["action_trace"]["requested_action"] == [6, 0, 0, 0, 0, 0]
            assert stored_next[player_id]["episode_id"] == 2
            assert stored_next[player_id]["decision_sequence"] == 3
            assert stored_next[player_id]["snapshot_kind"] == "reset"

        assert next_observations.shape == (1, 8, 3)
        assert np.all(rewards == 0.75)
        assert np.all(dones)
    finally:
        env.close()


def _valid_native_action_trace_rows():
    infos = [{
        "action_trace": [
            {
                "player_id": player_id,
                "requested_action": [6, 0, 0, 0, 0, 0],
                "effective_action": [6, 0, 0, 0, 0, 0],
                "handler_applied": True,
                "status_reason": "pass",
            }
            for player_id in range(8)
        ],
        "temporal_events": [
            {
                "contract_id": "tft.engine.temporal-event",
                "contract_version": 1,
                "event_id": f"engine-A/episode/4/decision/21/player/{player_id}/action",
                "event_type": "action_outcome",
                "scope": "player",
                "engine_instance_id": "engine-A",
                "episode_id": 4,
                "global_sequence": player_id + 1,
                "player_sequence": 21,
                "player_id": player_id,
                "round": 1,
                "stage": 1,
                "causal_event_id": "",
                "source_player_decision_sequence": 21,
                "observed_player_decision_sequence": 22,
                "fact_source": "tft.engine.action-outcome-event",
                "unit_uuid": "",
                "related_unit_uuid": "",
                "resource": "gold",
                "delta": 0,
                "value_before": 0,
                "value_after": 0,
                "delayed": False,
            }
            for player_id in range(8)
        ],
        "action_outcome_events": [
            {
                "contract_id": "tft.engine.action-outcome-event",
                "contract_version": 1,
                "event_id": f"engine-A/episode/4/decision/21/player/{player_id}/action",
                "engine_instance_id": "engine-A",
                "episode_id": 4,
                "player_id": player_id,
                "outcome_player_decision_sequence": 22,
                "mask_permitted": True,
                "preflight_accepted": True,
                "handler_applied": True,
                "decision_advanced": True,
                "execution_status": "applied",
                "affected_unit_uuids": [],
                "status_reason": "applied",
            }
            for player_id in range(8)
        ],
    }]
    result_metadata = [
        {
            "lobby_index": 0, "player_id": player_id,
            "engine_instance_id": "engine-A", "episode_id": 4,
            "player_decision_sequence": 22,
        }
        for player_id in range(8)
    ]
    return result_metadata, infos


def test_attach_native_action_traces_rejects_missing_player_trace():
    result_metadata, infos = _valid_native_action_trace_rows()
    infos[0]["action_trace"].pop()

    with pytest.raises(RuntimeError, match="8 registros"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_trace_for_wrong_player():
    result_metadata, infos = _valid_native_action_trace_rows()
    infos[0]["action_trace"][3]["player_id"] = 4

    with pytest.raises(RuntimeError, match="esperado 3"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_misaligned_result_row():
    result_metadata, infos = _valid_native_action_trace_rows()
    result_metadata[5]["lobby_index"] = 1

    with pytest.raises(RuntimeError, match="Snapshot de resultado desalinhado"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_incomplete_trace_fields():
    result_metadata, infos = _valid_native_action_trace_rows()
    del infos[0]["action_trace"][2]["status_reason"]

    with pytest.raises(RuntimeError, match="Trace de ação inválido"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_snapshot_cardinality_mismatch():
    result_metadata, infos = _valid_native_action_trace_rows()
    result_metadata.pop()

    with pytest.raises(RuntimeError, match="não corresponde"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_boolean_result_player_id():
    result_metadata, infos = _valid_native_action_trace_rows()
    result_metadata[0]["player_id"] = False

    with pytest.raises(RuntimeError, match="Snapshot de resultado desalinhado"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_non_integer_result_lobby_id():
    result_metadata, infos = _valid_native_action_trace_rows()
    result_metadata[0]["lobby_index"] = "0"

    with pytest.raises(RuntimeError, match="Snapshot de resultado desalinhado"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_non_mapping_result_row():
    result_metadata, infos = _valid_native_action_trace_rows()
    result_metadata[0] = None

    with pytest.raises(RuntimeError, match="Snapshot de resultado inválido"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)


def test_attach_native_action_traces_rejects_non_mapping_lobby_info():
    result_metadata, infos = _valid_native_action_trace_rows()
    infos[0] = None

    with pytest.raises(RuntimeError, match="Info nativa inválida"):
        Trainer._attach_native_action_traces(result_metadata, infos, 8)



def test_rollout_metadata_isolated_on_store_and_shared_read_only_in_batches():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "a" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
        "native_player_state": {
            "board": [{"unit": "unit-a", "items": ["item-a", "item-b"]}],
            "bench": [],
            "traits": [{"name": "trait-a", "count": 2}],
        },
        "item_recipes": [{"components": ["item-a", "item-b"], "result": "item-c"}],
    }
    trace = {
        "player_id": 0,
        "requested_action": [6, 0, 0, 0, 0, 0],
        "effective_action": [6, 0, 0, 0, 0, 0],
        "handler_applied": True,
        "status_reason": "applied",
    }
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": trace,
        "action_outcome_event": {
            "contract_id": "tft.engine.action-outcome-event",
            "contract_version": 1,
            "event_id": "engine-A/episode/4/decision/21/player/0/action",
            "engine_instance_id": "engine-A", "episode_id": 4, "player_id": 0,
            "source_player_decision_sequence": 21, "outcome_player_decision_sequence": 22,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "normalized_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "mask_permitted": True, "preflight_accepted": True, "handler_applied": True,
            "decision_advanced": True, "execution_status": "applied",
            "affected_unit_uuids": [], "status_reason": "applied",
        },
    }
    next_state = dict(result)

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

    trace["requested_action"][0] = 0
    result["action_trace"]["status_reason"] = "caller-mutated"
    # Compatibility accessors return defensive copies; compare their values,
    # then retain the canonical sidecar reference for zero-copy batch checks.
    stored_trace = buffer.result_snapshot_metadata[0][0]["action_trace"]
    canonical_trace = buffer._metadata_records[0][0][1]["action_trace"]
    assert stored_trace is not canonical_trace
    assert stored_trace == canonical_trace
    assert stored_trace["requested_action"] == [6, 0, 0, 0, 0, 0]
    assert stored_trace["status_reason"] == "applied"

    assert buffer._metadata_records[0][0][1] is buffer._metadata_records[0][0][2]
    audit = buffer.get_transition_metadata(0, 0)
    assert audit["snapshot_metadata"]["mask_snapshot_hash"] == "a" * 64
    assert audit["snapshot_metadata"]["native_player_state"]["board"][0]["items"] == ["item-a", "item-b"]
    assert audit["snapshot_metadata"]["item_recipes"][0]["result"] == "item-c"
    assert audit["result_snapshot_metadata"]["action_trace"]["status_reason"] == "applied"
    audit["result_snapshot_metadata"]["action_trace"]["status_reason"] = "audit-mutated"
    assert buffer.result_snapshot_metadata[0][0]["action_trace"]["status_reason"] == "applied"

    training_batch = next(buffer.get_batches(batch_size=1))
    assert training_batch["snapshot_metadata"] is None
    assert training_batch["result_snapshot_metadata"] is None
    assert training_batch["next_snapshot_metadata"] is None
    assert "identities" not in training_batch["semantic_state"]
    assert "hashes" not in training_batch["semantic_state"]

    batch = next(buffer.get_batches(batch_size=1, include_metadata=True))
    batch_trace = batch["result_snapshot_metadata"][0]["action_trace"]
    assert batch["snapshot_metadata"][0] is buffer._metadata_records[0][0][0]
    assert batch["result_snapshot_metadata"][0] is buffer._metadata_records[0][0][1]
    assert batch["next_snapshot_metadata"][0] is buffer._metadata_records[0][0][2]
    assert batch_trace is canonical_trace
    assert batch_trace["effective_action"] == [6, 0, 0, 0, 0, 0]
    assert batch_trace["status_reason"] == "applied"


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("engine_instance_id", ""),
        ("engine_instance_id", 123),
        ("episode_id", True),
        ("episode_id", "4"),
        ("decision_sequence", False),
        ("decision_sequence", "21"),
        ("player_id", True),
        ("player_id", "0"),
        ("lobby_index", False),
        ("lobby_index", "0"),
    ],
)
def test_rollout_rejects_malformed_identity_field_types(field, invalid_value):
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=3, action_dim=6, device=torch.device("cpu")
    )
    decision = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 21, "player_decision_sequence": 21, "player_id": 0, "lobby_index": 0,
        "mask_snapshot_hash": "a" * 64,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
    }
    decision[field] = invalid_value
    result = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
        "action_trace": {
            "player_id": 0,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        },
    }
    next_state = {
        "engine_instance_id": "engine-A", "episode_id": 4,
        "decision_sequence": 22, "player_decision_sequence": 22, "player_id": 0, "lobby_index": 0,
    }

    with pytest.raises(ValueError, match=field):
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

def test_trainer_expands_native_state_snapshot_to_exact_player_rows():
    from trainer import Trainer
    from decision_identity import build_player_identity_envelopes

    snapshot = {
        "engine_instance_id": "engine-A",
        "episode_id": 4,
        "decision_sequence": 9,
        "player_decision_sequences": [9] * 8,
        "round": 1,
        "native_state_snapshot": {
            "engine_instance_id": "engine-A",
            "episode_id": 4,
            "snapshot_sequence": 9,
            "round": 1,
            "player_decision_sequences": [9] * 8,
            "players": [
                {
                    "player_id": player_id,
                    "board": [{"occupied": False} for _ in range(28)],
                    "bench": [{"occupied": False} for _ in range(9)],
                    "shop": [{"occupied": False} for _ in range(5)],
                }
                for player_id in range(8)
            ],
        },
    }
    snapshot["player_identity_envelopes"] = build_player_identity_envelopes(snapshot)
    rows = Trainer._expand_lobby_snapshot_metadata([snapshot], 8, "teste")
    assert len(rows) == 8
    assert [row["native_player_state"]["player_id"] for row in rows] == list(range(8))
    assert all(row["player_decision_sequence"] == 9 for row in rows)
    assert "native_state_snapshot" not in rows[0]

    # Canonical identity is frozen once at expansion. RolloutBuffer's later
    # deepcopy shares this immutable envelope instead of copying it again.
    from copy import deepcopy
    from immutable_snapshot import FrozenDict
    for player_id, row in enumerate(rows):
        source_envelope = snapshot["player_identity_envelopes"][player_id]
        assert isinstance(row["identity"], FrozenDict)
        assert row["identity"] == source_envelope
        assert deepcopy(row["identity"]) is row["identity"]
    with pytest.raises(TypeError, match="immutable"):
        rows[0]["identity"]["player_id"] = "player-99"


def test_observation_rows_receive_stable_content_hashes():
    observations = torch.tensor(
        [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
        dtype=torch.float32,
    )
    first = Trainer._hash_observation_rows(observations)
    repeated = Trainer._hash_observation_rows(observations.clone())
    assert first == repeated
    assert len(first) == 2
    assert first[0] != first[1]

    changed = observations.clone()
    changed[0, 1] += 0.001
    changed_hashes = Trainer._hash_observation_rows(changed)
    assert changed_hashes[0] != first[0]
    assert changed_hashes[1] == first[1]


def test_observation_row_hash_rejects_non_float32_or_non_matrix_input():
    with pytest.raises(TypeError, match="float32"):
        Trainer._hash_observation_rows(torch.zeros((2, 3), dtype=torch.float64))
    with pytest.raises(TypeError, match="batch"):
        Trainer._hash_observation_rows(torch.zeros(3, dtype=torch.float32))


def test_freeze_snapshot_is_deeply_immutable_and_deepcopy_shares_ownership():
    from copy import deepcopy
    from immutable_snapshot import freeze_snapshot

    source = {
        "player_id": 3,
        "units": [{"champion_id": 42, "items": [1, 2]}],
        "strategic_state": {"active_unit_ids": [42]},
    }
    frozen = freeze_snapshot(source)
    source["units"][0]["items"].append(9)

    assert isinstance(frozen, dict)
    assert isinstance(frozen["units"], list)
    assert frozen["units"][0]["items"] == [1, 2]
    assert deepcopy(frozen) is frozen
    assert deepcopy({"native_player_state": frozen})["native_player_state"] is frozen

    with pytest.raises(TypeError, match="immutable"):
        frozen["player_id"] = 4
    with pytest.raises(TypeError, match="immutable"):
        frozen["units"][0]["items"].append(3)
    with pytest.raises(TypeError, match="immutable"):
        frozen["strategic_state"]["active_unit_ids"][0] = 99

def test_trainer_flattens_packed_action_masks_to_contract_tensors():
    trainer = Trainer.__new__(Trainer)
    trainer.num_envs = 1
    trainer.device = torch.device("cpu")
    trainer.PLAYERS_PER_LOBBY = 8

    packed = np.zeros((8, 1280), dtype=np.bool_)
    packed[:, 0] = True
    packed[:, 9] = True

    packed_flattened = trainer._flatten_masks([packed])

    legacy_players = [dict() for _ in range(8)]
    offset = 0
    for key, shape in Trainer.MASK_SHAPES.items():
        width = int(np.prod(shape))
        for player_id in range(8):
            legacy_players[player_id][key] = packed[
                player_id, offset:offset + width
            ].reshape(shape).copy()
        offset += width

    legacy_flattened = trainer._flatten_masks([legacy_players])

    assert offset == 1280
    assert set(packed_flattened) == set(Trainer.MASK_SHAPES)
    assert tuple(packed_flattened["type_mask"].shape) == (8, 9)
    assert tuple(packed_flattened["shop_mask"].shape) == (8, 5)
    assert packed_flattened["type_mask"][:, 0].all()
    assert packed_flattened["shop_mask"][:, 0].all()
    assert all(value.dtype == torch.bool for value in packed_flattened.values())
    for key in Trainer.MASK_SHAPES:
        assert torch.equal(packed_flattened[key], legacy_flattened[key])



def test_expansion_reuses_native_player_state_only_for_exact_snapshot_revision():
    from copy import deepcopy
    from trainer import Trainer
    from decision_identity import build_player_identity_envelopes

    snapshot = {
        "engine_instance_id": "engine-cache",
        "episode_id": 12,
        "decision_sequence": 44,
        "player_decision_sequences": [44] * 8,
        "round": 5,
        "native_state_snapshot": {
            "engine_instance_id": "engine-cache",
            "episode_id": 12,
            "snapshot_sequence": 44,
            "round": 5,
            "player_decision_sequences": [44] * 8,
            "contract_id": "native-state-v1",
            "contract_version": 1,
            "producer": "test-engine",
            "source_namespace": "tft.engine.snapshot",
            "players": [
                {
                    "player_id": player_id,
                    "board": [{"occupied": player_id == 0}],
                    "bench": [{"occupied": False}],
                    "shop": [{"champion_id": player_id}],
                }
                for player_id in range(8)
            ],
        },
    }
    snapshot["player_identity_envelopes"] = build_player_identity_envelopes(snapshot)
    # Separate mappings model the result and next-snapshot bridge outputs.
    next_snapshot = deepcopy(snapshot)
    next_snapshot["player_identity_envelopes"] = build_player_identity_envelopes(next_snapshot)

    cache = {}
    result_rows = Trainer._expand_lobby_snapshot_metadata(
        [snapshot], 8, "result", native_state_cache=cache
    )
    next_rows = Trainer._expand_lobby_snapshot_metadata(
        [next_snapshot], 8, "next", native_state_cache=cache
    )

    for result_row, next_row in zip(result_rows, next_rows):
        assert result_row["native_player_state"] is next_row["native_player_state"]
        assert result_row["native_player_state"] == next_row["native_player_state"]

    # A new episode is a different revision namespace and must not alias.
    new_episode = deepcopy(next_snapshot)
    new_episode["episode_id"] = 13
    new_episode["native_state_snapshot"]["episode_id"] = 13
    new_episode["player_identity_envelopes"] = build_player_identity_envelopes(new_episode)
    new_episode_rows = Trainer._expand_lobby_snapshot_metadata(
        [new_episode], 8, "new episode", native_state_cache=cache
    )
    assert all(
        old_row["native_player_state"] is not new_row["native_player_state"]
        for old_row, new_row in zip(result_rows, new_episode_rows)
    )


def test_expansion_rejects_contract_drift_for_same_native_snapshot_revision():
    from copy import deepcopy
    import pytest
    from trainer import Trainer
    from decision_identity import build_player_identity_envelopes

    def make_snapshot():
        value = {
            "engine_instance_id": "engine-contract-cache",
            "episode_id": 21,
            "decision_sequence": 9,
            "player_decision_sequences": [9] * 8,
            "round": 3,
            "native_state_snapshot": {
                "engine_instance_id": "engine-contract-cache",
                "episode_id": 21,
                "snapshot_sequence": 9,
                "round": 3,
                "player_decision_sequences": [9] * 8,
                "contract_id": "native-state-v1",
                "contract_version": 1,
                "producer": "test-engine",
                "source_namespace": "tft.engine.snapshot",
                "players": [
                    {"player_id": player_id, "board": [], "bench": [], "shop": []}
                    for player_id in range(8)
                ],
            },
        }
        value["player_identity_envelopes"] = build_player_identity_envelopes(value)
        return value

    first = make_snapshot()
    changed_contract = deepcopy(first)
    changed_contract["native_state_snapshot"]["contract_version"] = 2
    cache = {}
    Trainer._expand_lobby_snapshot_metadata(
        [first], 8, "first", native_state_cache=cache
    )

    with pytest.raises(RuntimeError, match="Contrato nativo diverge"):
        Trainer._expand_lobby_snapshot_metadata(
            [changed_contract], 8, "changed contract", native_state_cache=cache
        )


def test_expansion_does_not_reuse_native_player_state_across_round_revisions():
    from copy import deepcopy
    from trainer import Trainer
    from decision_identity import build_player_identity_envelopes

    def make_snapshot(round_number):
        value = {
            "engine_instance_id": "engine-round-cache",
            "episode_id": 4,
            "decision_sequence": 18,
            "player_decision_sequences": [18] * 8,
            "round": round_number,
            "native_state_snapshot": {
                "engine_instance_id": "engine-round-cache",
                "episode_id": 4,
                "snapshot_sequence": 18,
                "round": round_number,
                "player_decision_sequences": [18] * 8,
                "contract_id": "native-state-v1",
                "contract_version": 1,
                "producer": "test-engine",
                "source_namespace": "tft.engine.snapshot",
                "players": [
                    {"player_id": player_id, "board": [], "bench": [], "shop": []}
                    for player_id in range(8)
                ],
            },
        }
        value["player_identity_envelopes"] = build_player_identity_envelopes(value)
        return value

    cache = {}
    first_rows = Trainer._expand_lobby_snapshot_metadata(
        [make_snapshot(6)], 8, "round 6", native_state_cache=cache
    )
    next_rows = Trainer._expand_lobby_snapshot_metadata(
        [make_snapshot(7)], 8, "round 7", native_state_cache=cache
    )
    assert all(
        first["native_player_state"] is not next_["native_player_state"]
        for first, next_ in zip(first_rows, next_rows)
    )


def test_expansion_keeps_native_player_state_isolated_between_lobby_rows():
    from copy import deepcopy
    from trainer import Trainer
    from decision_identity import build_player_identity_envelopes

    snapshot = {
        "engine_instance_id": "duplicate-engine-fixture",
        "episode_id": 2,
        "decision_sequence": 11,
        "player_decision_sequences": [11] * 8,
        "round": 4,
        "native_state_snapshot": {
            "engine_instance_id": "duplicate-engine-fixture",
            "episode_id": 2,
            "snapshot_sequence": 11,
            "round": 4,
            "player_decision_sequences": [11] * 8,
            "contract_id": "native-state-v1",
            "contract_version": 1,
            "producer": "test-engine",
            "source_namespace": "tft.engine.snapshot",
            "players": [
                {"player_id": player_id, "board": [], "bench": [], "shop": []}
                for player_id in range(8)
            ],
        },
    }
    snapshot["player_identity_envelopes"] = build_player_identity_envelopes(snapshot)
    second_lobby = deepcopy(snapshot)
    second_lobby["player_identity_envelopes"] = build_player_identity_envelopes(second_lobby)

    rows = Trainer._expand_lobby_snapshot_metadata(
        [snapshot, second_lobby], 8, "two lobbies", native_state_cache={}
    )
    first_lobby_rows, second_lobby_rows = rows[:8], rows[8:]
    assert all(
        first["native_player_state"] is not second["native_player_state"]
        for first, second in zip(first_lobby_rows, second_lobby_rows)
    )



def test_metadata_equality_short_circuits_shared_immutable_subtrees():
    class EqualityMustNotRun(dict):
        def __eq__(self, _other):
            raise AssertionError("shared subtree equality should be skipped")

    shared_native_state = EqualityMustNotRun({"board": [{"unit": 42}]})
    left = {
        "identity": {"episode_id": 3, "player_id": 1},
        "native_player_state": shared_native_state,
        "action_trace": {"requested_action": [6, 0, 0, 0, 0, 0]},
    }
    right = {
        "identity": {"episode_id": 3, "player_id": 1},
        "native_player_state": shared_native_state,
        "action_trace": {"requested_action": [6, 0, 0, 0, 0, 0]},
    }

    assert RolloutBuffer._metadata_values_equal(left, right)

    changed = {
        **right,
        "action_trace": {"requested_action": [6, 1, 0, 0, 0, 0]},
    }
    assert not RolloutBuffer._metadata_values_equal(left, changed)


def test_metadata_equality_handles_non_scalar_equality_results_safely():
    class AmbiguousEquality:
        def __eq__(self, _other):
            return np.array([True, False])

    assert not RolloutBuffer._metadata_values_equal(
        {"value": AmbiguousEquality()},
        {"value": AmbiguousEquality()},
    )



def test_metadata_equality_preserves_list_and_tuple_type_semantics():
    assert not RolloutBuffer._metadata_values_equal([1, 2], (1, 2))
    assert RolloutBuffer._metadata_values_equal([1, 2], [1, 2])
    assert RolloutBuffer._metadata_values_equal((1, 2), (1, 2))
