"""The viewer's opt-in policy diagnostics must not change inference outputs."""
import torch

from policy import TFTPolicy

def _complete_mask_bundle(masks, batch_size, device="cpu"):
    """Build full native mask snapshots for focused Policy unit fixtures."""
    shapes = {
        "type_mask": (9,), "shop_mask": (5,), "bench_source_mask": (9,),
        "board_target_mask": (28,), "board_source_mask": (28,),
        "board_move_target_masks": (28, 28), "bench_move_source_mask": (9,),
        "bench_to_board_target_masks": (9, 28), "item_inventory_mask": (9,),
        "item_component_first_mask": (10,), "item_component_pair_masks": (10, 10),
        "item_target_mask": (37,),
    }
    result = {
        key: torch.zeros((batch_size, *shape), dtype=torch.bool, device=device)
        for key, shape in shapes.items()
    }
    for key, value in masks.items():
        result[key] = value
    return result



def _fixture():
    torch.manual_seed(781)
    policy = TFTPolicy(obs_dim=162, action_dims=[9, 5, 9, 28, 28, 28], hidden_size=64)
    obs = torch.randn(2, 162)
    masks = {
        "type_mask": torch.zeros(2, 9, dtype=torch.bool),
        "shop_mask": torch.ones(2, 5, dtype=torch.bool),
        "bench_source_mask": torch.ones(2, 9, dtype=torch.bool),
        "bench_move_source_mask": torch.ones(2, 9, dtype=torch.bool),
        "bench_to_board_target_masks": torch.ones(2, 9, 28, dtype=torch.bool),
        "board_target_mask": torch.ones(2, 28, dtype=torch.bool),
        "board_source_mask": torch.ones(2, 28, dtype=torch.bool),
        "board_move_target_masks": torch.ones(2, 28, 28, dtype=torch.bool),
    }
    masks = _complete_mask_bundle(masks, obs.shape[0])
    masks["type_mask"][0, 0] = True  # BUY
    masks["type_mask"][1, 4] = True  # MOVE_BOARD
    return policy.eval(), obs, masks


def test_diagnostics_do_not_change_deterministic_actions_or_values():
    policy, obs, masks = _fixture()
    weights_before = {name: value.detach().clone() for name, value in policy.state_dict().items()}
    with torch.inference_mode():
        normal = policy.get_action_and_value(obs, masks=masks, deterministic=True)
        diagnostic = policy.get_action_and_value_with_diagnostics(
            obs, masks=masks, deterministic=True
        )
    for expected, actual in zip(normal, diagnostic[:4]):
        assert torch.equal(expected, actual)
    assert len(diagnostic[4]) == 2
    assert all(torch.equal(weights_before[name], value) for name, value in policy.state_dict().items())
    assert {item["head"] for item in diagnostic[4][0]} == {"type", "shop_slot"}
    assert {item["head"] for item in diagnostic[4][1]} == {
        "type", "board_source", "board_move_target"
    }
    for player in diagnostic[4]:
        for item in player:
            assert abs(sum(item["probabilities"]) - 1.0) < 1e-5
            assert 0.0 <= item["selected_probability"] <= 1.0
            assert len(item["top_choices"]) == 3


def test_diagnostics_do_not_consume_extra_rng_in_stochastic_mode():
    policy, obs, masks = _fixture()
    torch.manual_seed(9912)
    with torch.inference_mode():
        normal = policy.get_action_and_value(obs, masks=masks, deterministic=False)
    torch.manual_seed(9912)
    with torch.inference_mode():
        diagnostic = policy.get_action_and_value_with_diagnostics(
            obs, masks=masks, deterministic=False
        )
    for expected, actual in zip(normal, diagnostic[:4]):
        assert torch.equal(expected, actual)
