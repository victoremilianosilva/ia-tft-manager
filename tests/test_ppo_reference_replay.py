import pytest
import torch

from ppo_protection.replay_buffer import ReferenceReplayBuffer


MASK_SHAPES = {
    "type_mask": (9,), "shop_mask": (5,), "bench_source_mask": (9,),
    "board_target_mask": (28,), "board_source_mask": (28,),
    "board_move_target_masks": (28, 28), "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28), "item_inventory_mask": (9,),
    "item_component_first_mask": (10,), "item_component_pair_masks": (10, 10),
    "item_target_mask": (37,),
}


def payload():
    return {
        "schema_version": 1,
        "source_checkpoint_sha256": "abc",
        "minimum_per_scenario": 2,
        "scenario_counts": {"scenario_a": 2, "scenario_b": 2},
        "observations": torch.zeros(4, 12),
        "actions": torch.zeros(4, 6, dtype=torch.long),
        "scenario_ids": [["scenario_a"], ["scenario_a"], ["scenario_b"], ["scenario_b"]],
        "masks": {key: torch.ones((4, *shape), dtype=torch.bool) for key, shape in MASK_SHAPES.items()},
    }


def test_replay_samples_valid_balanced_batches():
    replay = ReferenceReplayBuffer(payload(), "cpu")
    batch = replay.sample(8)
    assert batch["obs"].shape == (8, 12)
    assert batch["actions"].shape == (8, 6)
    assert set(batch["masks"]) == set(MASK_SHAPES)
    assert replay.source_checkpoint_sha256 == "abc"


def test_replay_rejects_incomplete_scenario_coverage():
    data = payload()
    data["scenario_counts"]["scenario_b"] = 1
    with pytest.raises(ValueError, match="cobertura mínima"):
        ReferenceReplayBuffer(data, "cpu")
