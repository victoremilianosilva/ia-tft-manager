import pytest

from policy import TFTPolicy
from trainer import Trainer


def test_action_dimensions_match_the_environment_contract():
    assert Trainer.ACTION_DIMS == [7, 5, 9, 28, 28, 28]
    assert Trainer.ACTION_DIM == len(Trainer.ACTION_DIMS)


def test_policy_heads_match_action_dimensions():
    policy = TFTPolicy(
        obs_dim=162,
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )

    assert policy.type_head.out_features == 7
    assert policy.shop_head[-1].out_features == 1
    assert policy.shop_head[0].in_features == 32 + 7 + 8
    assert policy.sell_head[-1].out_features == 1
    assert policy.sell_head[0].in_features == 32 + 7 + 8
    assert policy.bench_head.out_features == 9
    assert policy.bench_to_board_head.out_features == 28
    assert policy.board_source_head.out_features == 28
    assert policy.board_move_target_head.out_features == 28


def test_policy_rejects_invalid_action_dimensions():
    invalid_dimensions = [
        [7, 5, 9, 28, 28],
        [7, 5, 9, 28, 28, 27],
        [7, 5, 9, 28, 28, 28, 1],
    ]

    for dimensions in invalid_dimensions:
        with pytest.raises(ValueError):
            TFTPolicy(
                obs_dim=162,
                action_dims=dimensions,
                hidden_size=32,
            )