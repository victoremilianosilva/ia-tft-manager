import pytest
import torch

from action_contract import (
    ACTION_CONTRACT_HASH,
    ACTION_CONTRACT_ID,
    ACTION_CONTRACT_VERSION,
    MASK_CONTRACT_HASH,
    MASK_CONTRACT_ID,
    MASK_CONTRACT_VERSION,
    MASK_SHAPES,
    build_action_mask_checkpoint_contract,
    hash_mask_rows,
    validate_action_mask_checkpoint_contract,
)
from policy import TFTPolicy
from rollout import RolloutBuffer


def _mask_batch(batch_size=1):
    masks = {
        name: torch.zeros((batch_size, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    return masks


def _metadata(mask_hash, player_id=0):
    return {
        "engine_instance_id": "engine-contract-test",
        "episode_id": 1,
        "decision_sequence": 10,
        "player_id": player_id,
        "lobby_index": 0,
        "mask_snapshot_hash": mask_hash,
        "mask_snapshot_hash_algorithm": "tft-action-mask-snapshot-v1",
        "action_contract_id": ACTION_CONTRACT_ID,
        "action_contract_version": ACTION_CONTRACT_VERSION,
        "action_contract_hash": ACTION_CONTRACT_HASH,
        "mask_contract_id": MASK_CONTRACT_ID,
        "mask_contract_version": MASK_CONTRACT_VERSION,
        "mask_contract_hash": MASK_CONTRACT_HASH,
    }


def _add_identity_rollout(mask_hash):
    masks = _mask_batch()
    buffer = RolloutBuffer(
        num_steps=1,
        num_envs=1,
        obs_dim=3,
        action_dim=6,
        device=torch.device("cpu"),
        mask_shapes=MASK_SHAPES,
    )
    decision = _metadata(mask_hash)
    result = {
        "engine_instance_id": "engine-contract-test",
        "episode_id": 1,
        "decision_sequence": 11,
        "player_id": 0,
        "lobby_index": 0,
        "action_trace": {
            "player_id": 0,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        },
    }
    next_state = {
        "engine_instance_id": "engine-contract-test",
        "episode_id": 1,
        "decision_sequence": 11,
        "player_id": 0,
        "lobby_index": 0,
    }
    buffer.add(
        obs=torch.zeros((1, 3)),
        actions=torch.tensor([[6, 0, 0, 0, 0, 0]], dtype=torch.long),
        logprobs=torch.zeros(1),
        rewards=torch.zeros(1),
        dones=torch.zeros(1),
        values=torch.zeros(1),
        masks_dict=masks,
        snapshot_metadata=[decision],
        result_snapshot_metadata=[result],
        next_snapshot_metadata=[next_state],
    )
    return buffer


def test_action_and_mask_contracts_have_independent_stable_hashes():
    first = build_action_mask_checkpoint_contract()
    second = build_action_mask_checkpoint_contract()

    assert first == second
    assert first["action_contract"]["sha256"] == ACTION_CONTRACT_HASH
    assert first["mask_contract"]["sha256"] == MASK_CONTRACT_HASH
    assert ACTION_CONTRACT_HASH != MASK_CONTRACT_HASH


def test_checkpoint_contract_rejects_changed_action_or_mask_semantics():
    manifest = build_action_mask_checkpoint_contract()
    validate_action_mask_checkpoint_contract(manifest)

    changed_action = dict(manifest)
    changed_action["action_contract"] = dict(manifest["action_contract"])
    changed_action["action_contract"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="action_contract incompatível"):
        validate_action_mask_checkpoint_contract(changed_action)

    changed_mask = dict(manifest)
    changed_mask["mask_contract"] = dict(manifest["mask_contract"])
    changed_mask["mask_contract"]["version"] = 2
    with pytest.raises(ValueError, match="mask_contract incompatível"):
        validate_action_mask_checkpoint_contract(changed_mask)


def test_mask_snapshot_hash_matches_exact_boolean_payload():
    masks = _mask_batch(batch_size=2)
    first = hash_mask_rows(masks)
    assert first == hash_mask_rows(masks)
    assert first[0] == first[1]

    masks["type_mask"][1, 5] = True
    changed = hash_mask_rows(masks)
    assert changed[0] == first[0]
    assert changed[1] != first[1]


def test_rollout_recomputes_mask_hash_from_the_persisted_payload():
    masks = _mask_batch()
    expected_hash = hash_mask_rows(masks)[0]
    buffer = _add_identity_rollout(expected_hash)

    assert buffer.snapshot_metadata[0][0]["mask_snapshot_hash"] == expected_hash
    for name in MASK_SHAPES:
        assert torch.equal(buffer.masks[name][0, 0], masks[name][0])


def test_rollout_rejects_well_formed_but_incorrect_mask_hash():
    masks = _mask_batch()
    actual_hash = hash_mask_rows(masks)[0]
    assert actual_hash != "0" * 64
    with pytest.raises(ValueError, match="Hash da máscara não corresponde"):
        _add_identity_rollout("0" * 64)


@pytest.mark.parametrize(
    "action",
    [
        [0, 2, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [3, 0, 4, 17, 0, 0],
        [4, 0, 0, 0, 9, 18],
        [5, 0, 7, 0, 0, 0],
        [6, 0, 0, 0, 0, 0],
        [7, 2, 36, 0, 0, 0],
        [8, 1, 2, 4, 0, 0],
    ],
)
def test_every_action_type_accepts_its_canonical_six_integer_encoding(action):
    tensor = torch.tensor([action], dtype=torch.long)
    TFTPolicy._validate_canonical_action_parameters(tensor)


@pytest.mark.parametrize(
    "action",
    [
        [0, 2, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [2, 0, 0, 1, 0, 0],
        [3, 1, 4, 17, 0, 0],
        [4, 1, 0, 0, 9, 18],
        [5, 0, 7, 1, 0, 0],
        [6, 0, 0, 0, 0, 1],
        [7, 2, 36, 1, 0, 0],
        [8, 1, 2, 4, 1, 0],
    ],
)
def test_every_action_type_rejects_nonzero_inactive_arguments(action):
    tensor = torch.tensor([action], dtype=torch.long)
    with pytest.raises(ValueError, match="argumentos inativos"):
        TFTPolicy._validate_canonical_action_parameters(tensor)


def test_action_validation_rejects_float_indices_instead_of_coercing():
    actions = torch.tensor([1.0], dtype=torch.float32)
    mask = torch.tensor([[True, True]], dtype=torch.bool)
    with pytest.raises(TypeError, match="torch.int64"):
        TFTPolicy._validate_selected_actions(actions, mask, "test")
