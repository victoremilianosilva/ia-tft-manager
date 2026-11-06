import pytest
import torch

from ppo_protection.replay_buffer import ReferenceReplayBuffer
from economy_finetuning.scenario_generator import SCENARIOS


MASK_SHAPES = {
    "type_mask": (9,), "shop_mask": (5,), "bench_source_mask": (9,),
    "board_target_mask": (28,), "board_source_mask": (28,),
    "board_move_target_masks": (28, 28), "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28), "item_inventory_mask": (9,),
    "item_component_first_mask": (10,), "item_component_pair_masks": (10, 10),
    "item_target_mask": (37,),
}


def payload():
    scenarios = [item.scenario_id for item in SCENARIOS if item.trainable]
    count = len(scenarios) * 2
    labels = [[scenario] for scenario in scenarios for _ in range(2)]
    return {
        "schema_version": 1,
        "source_checkpoint_sha256": "a" * 64,
        "minimum_per_scenario": 2,
        "scenario_counts": {scenario: 2 for scenario in scenarios},
        "observations": torch.zeros(count, 12),
        "actions": torch.zeros(count, 6, dtype=torch.long),
        "scenario_ids": labels,
        "masks": {key: torch.ones((count, *shape), dtype=torch.bool) for key, shape in MASK_SHAPES.items()},
    }


def test_replay_samples_valid_balanced_batches():
    replay = ReferenceReplayBuffer(payload(), "cpu")
    batch = replay.sample(8)
    assert batch["obs"].shape == (8, 12)
    assert batch["actions"].shape == (8, 6)
    assert set(batch["masks"]) == set(MASK_SHAPES)
    assert replay.source_checkpoint_sha256 == "a" * 64


def test_replay_rejects_incomplete_scenario_coverage():
    data = payload()
    scenario = next(item.scenario_id for item in SCENARIOS if item.trainable)
    data["scenario_counts"][scenario] = 1
    with pytest.raises(ValueError, match="cobertura mínima"):
        ReferenceReplayBuffer(data, "cpu")
