import torch

from action_contract import (
    MASK_SHAPES, MASK_SNAPSHOT_HASH_ALGORITHM,
    ACTION_CONTRACT_ID, ACTION_CONTRACT_VERSION, ACTION_CONTRACT_HASH,
    MASK_CONTRACT_ID, MASK_CONTRACT_VERSION, MASK_CONTRACT_HASH,
    hash_mask_row,
)
from rollout import RolloutBuffer
from semantic_observation import SEMANTIC_ENTITY_SLOTS, SEMANTIC_NUMERIC_DIM, semantic_item_state_tensors


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
    semantic_numeric = torch.zeros((batch_size, SEMANTIC_NUMERIC_DIM), dtype=torch.float32)
    native_trait_ids = torch.zeros(
        (batch_size, SEMANTIC_ENTITY_SLOTS, 10), dtype=torch.long
    )
    native_trait_ids[:, 0, 0] = torch.tensor([1234, 4321])
    semantic_numeric[:, 70 + 29] = native_trait_ids[:, 0, 0].float() / 65536.0
    semantic = {
        "numeric": semantic_numeric,
        "items": semantic_item_state_tensors(
            semantic_numeric, trait_ids=native_trait_ids
        ),
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
    # Minibatch order is intentionally shuffled; compare identity-bound rows
    # after sorting by the first champion ID, not by their original batch slot.
    expected_order = torch.argsort(semantic["champion_ids"][:, 0])
    batch_order = torch.argsort(batch["semantic_state"]["champion_ids"][:, 0])
    actual = batch["semantic_state"]["champion_ids"][batch_order]
    expected = semantic["champion_ids"][expected_order]
    assert torch.equal(actual, expected)
    actual_trait_ids = batch["semantic_state"]["items"]["trait_ids"][batch_order]
    expected_trait_ids = native_trait_ids[expected_order]
    assert torch.equal(actual_trait_ids, expected_trait_ids)
    actual_numeric = batch["semantic_state"]["numeric"][batch_order]
    assert torch.equal(actual_numeric, semantic["numeric"][expected_order])


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
    entity_identity = {
        "occupied": tuple([False] * SEMANTIC_ENTITY_SLOTS),
        "unit_uuids": tuple([""] * SEMANTIC_ENTITY_SLOTS),
        "shop_offer_revisions": (0, 0, 0, 0, 0),
    }
    decision = dict(identity)
    decision.update({
        "semantic_identity": identity,
        "semantic_entity_identity": entity_identity,
        "semantic_projection_hash": digest,
        "semantic_projection_contract_id": "tft.ppo.semantic-native-state.v8",
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
    semantic_numeric = torch.zeros((1, SEMANTIC_NUMERIC_DIM), dtype=torch.float32)
    semantic = {
        "numeric": semantic_numeric,
        "items": semantic_item_state_tensors(semantic_numeric),
        "champion_ids": torch.zeros((1, SEMANTIC_ENTITY_SLOTS), dtype=torch.long),
        "entity_identity": [entity_identity],
        "identities": [identity], "hashes": [digest],
        "contract_id": "tft.ppo.semantic-native-state.v8",
        "contract_hash": "b" * 64,
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
    batch = next(buffer.get_batches(batch_size=1, include_metadata=True))
    assert batch["semantic_state"]["identities"] == [identity]
    assert batch["semantic_state"]["entity_identity"] == semantic["entity_identity"]
    assert batch["semantic_state"]["hashes"] == [digest]
    assert batch["snapshot_metadata"][0]["semantic_projection_hash"] == digest


def test_production_rollout_rejects_missing_semantic_state():
    buffer = RolloutBuffer(
        num_steps=1,
        num_envs=1,
        obs_dim=4,
        action_dim=6,
        device="cpu",
        mask_shapes=MASK_SHAPES,
        require_semantic_state=True,
    )
    masks = {
        name: torch.zeros((1, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    actions = torch.zeros(1, 6, dtype=torch.long)
    actions[:, 0] = 6

    try:
        buffer.add(
            torch.zeros(1, 4), actions, torch.zeros(1), torch.zeros(1),
            torch.zeros(1), torch.zeros(1), masks,
        )
    except ValueError as exc:
        assert "requires semantic_state v8" in str(exc)
    else:
        raise AssertionError("production rollout must reject a missing semantic state")
