import torch

from action_contract import (
    MASK_SHAPES, MASK_SNAPSHOT_HASH_ALGORITHM,
    ACTION_CONTRACT_ID, ACTION_CONTRACT_VERSION, ACTION_CONTRACT_HASH,
    MASK_CONTRACT_ID, MASK_CONTRACT_VERSION, MASK_CONTRACT_HASH,
    hash_mask_row,
)
from rollout import RolloutBuffer
from semantic_observation import SEMANTIC_ENTITY_SLOTS, SEMANTIC_NUMERIC_DIM


def test_rollout_keeps_semantic_projection_aligned_with_each_transition():
    batch_size = 2
    buffer = RolloutBuffer(
        num_steps=1,
        num_envs=batch_size,
        obs_dim=4,
        action_dim=6,
        device="cpu",
        mask_shapes=MASK_SHAPES,
    )
    masks = {
        name: torch.zeros((batch_size, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    semantic = {
        "numeric": torch.arange(
            batch_size * SEMANTIC_NUMERIC_DIM, dtype=torch.float32
        ).reshape(batch_size, SEMANTIC_NUMERIC_DIM),
        "champion_ids": torch.arange(
            batch_size * SEMANTIC_ENTITY_SLOTS, dtype=torch.long
        ).reshape(batch_size, SEMANTIC_ENTITY_SLOTS),
    }
    actions = torch.zeros(batch_size, 6, dtype=torch.long)
    actions[:, 0] = 6
    buffer.add(
        torch.zeros(batch_size, 4),
        actions,
        torch.zeros(batch_size),
        torch.zeros(batch_size),
        torch.zeros(batch_size),
        torch.zeros(batch_size),
        masks,
        semantic_state=semantic,
    )

    batch = next(buffer.get_batches(batch_size=batch_size))
    assert torch.equal(batch["semantic_state"]["numeric"], semantic["numeric"])
    assert torch.equal(batch["semantic_state"]["champion_ids"], semantic["champion_ids"])


def test_rollout_rejects_semantic_projection_shape_and_non_finite_values():
    buffer = RolloutBuffer(
        num_steps=1,
        num_envs=1,
        obs_dim=4,
        action_dim=6,
        device="cpu",
        mask_shapes=MASK_SHAPES,
    )
    masks = {
        name: torch.zeros((1, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    invalid = {
        "numeric": torch.full((1, SEMANTIC_NUMERIC_DIM), float("nan")),
        "champion_ids": torch.zeros((1, SEMANTIC_ENTITY_SLOTS), dtype=torch.long),
    }
    try:
        actions = torch.zeros(1, 6, dtype=torch.long)
        actions[:, 0] = 6
        buffer.add(
            torch.zeros(1, 4),
            actions,
            torch.zeros(1),
            torch.zeros(1),
            torch.zeros(1),
            torch.zeros(1),
            masks,
            semantic_state=invalid,
        )
    except ValueError as exc:
        assert "NaN" in str(exc)
    else:
        raise AssertionError("non-finite semantic state must be rejected")

def test_rollout_replay_keeps_semantic_identity_and_hash_with_the_same_row():
    buffer = RolloutBuffer(
        num_steps=1, num_envs=1, obs_dim=4, action_dim=6, device="cpu",
        mask_shapes=MASK_SHAPES,
    )
    masks = {
        name: torch.zeros((1, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    action = [6, 0, 0, 0, 0, 0]
    identity = {
        "engine_instance_id": "engine-a", "episode_id": 1,
        "decision_sequence": 10, "player_decision_sequence": 2,
        "player_id": 0, "round": 1, "lobby_index": 0,
    }
    digest = "a" * 64
    decision = dict(identity)
    decision.update({
        "semantic_identity": identity,
        "semantic_projection_hash": digest,
        "semantic_projection_contract_id": "tft.ppo.semantic-native-state.v2",
        "semantic_projection_contract_hash": "b" * 64,
        "mask_snapshot_hash": hash_mask_row({name: masks[name][0] for name in MASK_SHAPES}),
        "mask_snapshot_hash_algorithm": MASK_SNAPSHOT_HASH_ALGORITHM,
        "action_contract_id": ACTION_CONTRACT_ID,
        "action_contract_version": ACTION_CONTRACT_VERSION,
        "action_contract_hash": ACTION_CONTRACT_HASH,
        "mask_contract_id": MASK_CONTRACT_ID,
        "mask_contract_version": MASK_CONTRACT_VERSION,
        "mask_contract_hash": MASK_CONTRACT_HASH,
    })
    result = {
        **identity, "decision_sequence": 11, "player_decision_sequence": 3,
        "action_trace": {
            "player_id": 0, "requested_action": action, "effective_action": action,
            "handler_applied": True, "status_reason": "accepted",
        },
    }
    next_state = {
        **identity, "decision_sequence": 11, "player_decision_sequence": 3,
    }
    semantic = {
        "numeric": torch.zeros((1, SEMANTIC_NUMERIC_DIM), dtype=torch.float32),
        "champion_ids": torch.zeros((1, SEMANTIC_ENTITY_SLOTS), dtype=torch.long),
        "identities": [identity], "hashes": [digest],
    }
    actions = torch.tensor([action], dtype=torch.long)
    buffer.add(
        torch.zeros(1, 4), actions, torch.zeros(1), torch.zeros(1),
        torch.zeros(1), torch.zeros(1), masks,
        semantic_state=semantic,
        snapshot_metadata=[decision],
        result_snapshot_metadata=[result],
        next_snapshot_metadata=[next_state],
    )
    batch = next(buffer.get_batches(batch_size=1))
    assert batch["semantic_state"]["identities"] == [identity]
    assert batch["semantic_state"]["hashes"] == [digest]
    assert batch["snapshot_metadata"][0]["semantic_projection_hash"] == digest
