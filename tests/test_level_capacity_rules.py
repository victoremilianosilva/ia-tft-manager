"""Regression tests for level-based deployment capacity and bench swaps."""

from types import SimpleNamespace
from unittest.mock import Mock

from ai.ActionMaskManager import ActionMaskManager
from env import MiniTFTEnv
from units.BoardManager import BoardManager
from units.BenchManager import BenchManager


def unit(name):
    return {"id": name, "name": name, "champion_id": name, "cost": 1, "star": 1}


def make_action_mask_manager(level, board_count):
    board = BoardManager(rows=4, cols=7)
    bench = BenchManager(max_bench=9)

    for position in range(board_count):
        assert board.add_unit(unit(f"board-{position}"), position)

    assert bench.add_unit(unit("bench-unit"))

    anti_loop = Mock()
    anti_loop.should_block_move.return_value = False
    economy = SimpleNamespace(
        level=level,
        gold=0,
        can_spend=lambda amount: False,
        can_buy_xp=lambda: False,
    )
    manager = ActionMaskManager(
        board_manager=board,
        bench_manager=bench,
        shop_manager=Mock(),
        economy_manager=economy,
        composition_manager=Mock(),
        positioning_manager=Mock(),
        anti_loop_manager=anti_loop,
        unit_manager=Mock(),
    )
    return manager, board, bench


def make_env(level, board_count):
    env = MiniTFTEnv.__new__(MiniTFTEnv)
    env.max_bench = 9
    env.board_manager = BoardManager(rows=4, cols=7)
    env.bench_manager = BenchManager(max_bench=9)
    env.economy_manager = SimpleNamespace(level=level)
    env.anti_loop_manager = Mock()
    env.anti_loop_manager.get_block_reason.return_value = None
    env.decision_engine_runtime = Mock()
    env.positioning_manager = Mock()
    env.positioning_manager.evaluate_board_positioning.return_value = 0.0
    env.reward_manager = Mock()
    env.reward_manager.calculate_action_reward.return_value = 0.05

    for position in range(board_count):
        assert env.board_manager.add_unit(unit(f"board-{position}"), position)
    assert env.bench_manager.add_unit(unit("incoming"))
    return env


def test_full_level_masks_allow_replacement_but_block_extra_unit():
    manager, board, bench = make_action_mask_manager(level=2, board_count=2)

    source_mask, target_masks, has_valid_move = manager.get_bench_move_masks()

    assert has_valid_move
    assert source_mask[0] == 1.0
    assert target_masks[0, 0] == 1.0
    assert target_masks[0, 1] == 1.0
    assert target_masks[0, 2] == 0.0
    assert board.get_unit_count() == 2
    assert bench.get_unit_count() == 1


def test_under_level_masks_allow_empty_placement_and_replacement():
    manager, _, _ = make_action_mask_manager(level=2, board_count=1)

    _, target_masks, has_valid_move = manager.get_bench_move_masks()

    assert has_valid_move
    assert target_masks[0, 0] == 1.0
    assert target_masks[0, 1] == 1.0


def test_capacity_violation_is_penalized_without_mutating_units():
    env = make_env(level=2, board_count=2)
    board_before = list(env.board_manager.board)
    bench_before = list(env.bench_manager.bench)
    info = {}

    reward = env._execute_move_bench(
        {"bench_slot": 0, "board_target": 2},
        info,
    )

    assert reward == -0.25
    assert info["action_success"] is False
    assert info["rule_violation"] == "board_capacity"
    assert info["board_units"] == 2
    assert info["board_capacity"] == 2
    assert env.board_manager.board == board_before
    assert env.bench_manager.bench == bench_before


def test_replacement_at_capacity_is_atomic_and_does_not_penalize():
    env = make_env(level=2, board_count=2)
    incoming = env.bench_manager.get_unit(0)
    displaced = env.board_manager.get_unit(0)
    board_count_before = env.board_manager.get_unit_count()
    info = {}

    reward = env._execute_move_bench(
        {"bench_slot": 0, "board_target": 0},
        info,
    )

    assert reward == 0.05
    assert info["action_success"] is True
    assert info["swapped_unit"] is displaced
    assert env.board_manager.get_unit(0) is incoming
    assert env.bench_manager.get_unit(0) is displaced
    assert env.board_manager.get_unit_count() == board_count_before
