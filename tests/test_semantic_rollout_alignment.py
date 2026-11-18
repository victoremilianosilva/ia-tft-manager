import torch

from action_contract import MASK_SHAPES
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
