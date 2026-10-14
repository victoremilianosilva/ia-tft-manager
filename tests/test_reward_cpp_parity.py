import math
from types import SimpleNamespace

import pytest

from ai.RewardManager import RewardManager


def manager():
    return RewardManager(
        economy_manager=object(),
        composition_manager=object(),
        positioning_manager=object(),
    )


def test_reward_sequence_matches_cpp_reward_model_golden_values():
    reward = manager()
    board = [None] * 28

    # Snapshot 0 -> 1: buying/placing a 2-cost, 1-star unit.
    board[0] = {"id": "unit-a"}
    first = (
        reward.calculate_action_reward("buy", True, 0.05)
        + reward.calculate_power_reward(4.0)
        + reward.calculate_synergy_reward(0.5)
        + reward.calculate_positioning_reward(0.3)
        + reward.calculate_level_reward(1)
        + reward.calculate_economy_reward(8, 1, 100)
        + reward.calculate_streak_reward(0, 0)
        + reward.calculate_board_reward(board, 28)
    )

    expected_first = (
        0.05 + math.tanh(0.4) + math.tanh(0.5)
        + 0.5 * math.tanh(0.3) + (1 / 28) * 0.15
    )
    assert first == pytest.approx(expected_first, abs=1e-9)

    # Snapshot 1 -> 2: same board power, improved synergy/position score,
    # and gold reaches the 10/20 interest thresholds.
    second = (
        reward.calculate_power_reward(4.0)
        + reward.calculate_synergy_reward(1.0)
        + reward.calculate_positioning_reward(0.8)
        + reward.calculate_level_reward(1)
        + reward.calculate_economy_reward(20, 1, 100)
        + reward.calculate_streak_reward(0, 0)
        + reward.calculate_board_reward(board, 28)
    )
    expected_second = (
        math.tanh(0.5) + 0.5 * math.tanh(0.5)
        + 0.10 + (1 / 28) * 0.15
    )
    assert second == pytest.approx(expected_second, abs=1e-9)


def test_combat_reward_matches_cpp_golden_values():
    reward = manager()

    won = reward.calculate_combat_reward(
        True, damage_dealt=3, damage_taken=0,
        enemy_alive=0, own_alive=2,
    )
    lost = reward.calculate_combat_reward(
        False, damage_dealt=0, damage_taken=3,
        enemy_alive=2, own_alive=0,
    )

    assert won == pytest.approx(2 + math.tanh(0.3) + 0.1, abs=1e-9)
    assert lost == pytest.approx(-2 - 0.1 - math.tanh(0.2), abs=1e-9)
