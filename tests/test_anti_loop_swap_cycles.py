
from ai.AntiLoopManager import AntiLoopManager


def test_detects_cycle_across_multiple_swaps():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    # Nasus passa pelas posições 3 -> 10 -> 12.
    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)

    # Tentar voltar à posição 3 fecha o ciclo.
    assert anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=3,
        unit=nasus,
    )


def test_allows_swap_cycle_candidate_to_new_position():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)

    # Uma posição que não fecha o ciclo deve continuar permitida.
    assert not anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=15,
        unit=nasus,
    )


def test_board_swap_for_one_unit_is_not_blocked_by_another_units_moves():
    anti_loop = AntiLoopManager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    # Apenas Teemo percorreu este histórico.
    anti_loop.register_move("board_move", 3, 10, teemo)
    anti_loop.register_move("board_move", 10, 12, teemo)

    # O swap de Nasus não deve ser bloqueado pelo histórico
    # de movimentação exclusiva de Teemo.
    assert not anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=3,
        unit=nasus,
    )
