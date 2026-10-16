"""Additional end-to-end audit regressions for AntiLoop and checkpoint evaluation.

These tests use the real Python lobby/environment. They deliberately separate
state mutation from execution-attempt telemetry: a rejected move may increment
the AntiLoop rejection counters, but must not move units, alter gold, or return
copies to the shared pool.
"""
from __future__ import annotations

from ai.ActionMaskManager import ActionType
from lobby.TFTLobby import TFTLobby


def _unit_ids(slots):
    return [
        None if unit is None else (
            unit.get("uuid"),
            unit.get("id"),
            int(unit.get("star", 1)),
        )
        for unit in slots
    ]


def test_antiloop_rejected_reverse_move_does_not_mutate_game_state():
    lobby = TFTLobby(seed=612034)
    try:
        lobby.reset()
        player = lobby.players[0]
        env = player.env

        # Use a real unit from the player's bench and place it on the board.
        source_bench = next(
            i for i, unit in enumerate(env.bench_manager.bench)
            if unit is not None
        )
        unit = env.bench_manager.bench[source_bench]
        env.bench_manager.bench[source_bench] = None
        env.board_manager.board[10] = unit

        # Simulate the earlier move 3 -> 10; the attempted reverse is 10 -> 3.
        env.anti_loop_manager.register_move(
            move_type="board_move",
            source=3,
            target=10,
            unit=unit,
        )

        board_before = _unit_ids(env.board_manager.board)
        bench_before = _unit_ids(env.bench_manager.bench)
        gold_before = env.economy_manager.gold
        pool_before = dict(lobby.unit_pool.available)
        history_before = env.anti_loop_manager.get_state()["move_history_size"]

        _, reward, _, info = env.step({
            "type": int(ActionType.MOVE_BOARD),
            "board_source": 10,
            "conditioned_board_target": 3,
        })

        assert info.get("anti_loop_blocked"), "A reversão deveria ser rejeitada"
        assert info.get("action_success") is not True
        assert reward < 0
        assert _unit_ids(env.board_manager.board) == board_before
        assert _unit_ids(env.bench_manager.bench) == bench_before
        assert env.economy_manager.gold == gold_before
        assert lobby.unit_pool.available == pool_before
        assert env.anti_loop_manager.get_state()["move_history_size"] == history_before
    finally:
        close = getattr(lobby, "close", None)
        if callable(close):
            close()


def test_antiloop_rejection_does_not_hide_a_different_legal_move():
    lobby = TFTLobby(seed=612035)
    try:
        lobby.reset()
        env = lobby.players[0].env
        source_bench = next(
            i for i, unit in enumerate(env.bench_manager.bench)
            if unit is not None
        )
        unit = env.bench_manager.bench[source_bench]
        env.bench_manager.bench[source_bench] = None
        env.board_manager.board[10] = unit

        env.anti_loop_manager.register_move(
            move_type="board_move",
            source=3,
            target=10,
            unit=unit,
        )

        # The reverse destination is blocked, but another empty square remains legal.
        masks = env.action_mask_manager.get_board_move_target_mask(10)
        assert masks[3] == 0
        assert masks[12] == 1

        board_before = _unit_ids(env.board_manager.board)
        _, reward, _, info = env.step({
            "type": int(ActionType.MOVE_BOARD),
            "board_source": 10,
            "conditioned_board_target": 12,
        })

        assert info.get("action_success") is True
        assert info.get("anti_loop_blocked") is None
        assert reward > -0.10
        assert env.board_manager.board[10] is None
        assert env.board_manager.board[12] is unit
        assert _unit_ids(env.board_manager.board) != board_before
    finally:
        close = getattr(lobby, "close", None)
        if callable(close):
            close()
