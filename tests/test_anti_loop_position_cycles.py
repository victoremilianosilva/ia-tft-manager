
from ai.AntiLoopManager import AntiLoopManager


def test_blocks_three_position_cycle():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)

    assert anti_loop.should_block_move(
        move_type="board_move",
        source=12,
        target=3,
        unit=nasus,
    )


def test_allows_move_to_new_position():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)

    assert not anti_loop.should_block_move(
        move_type="board_move",
        source=12,
        target=15,
        unit=nasus,
    )


def test_does_not_detect_cycle_for_another_unit():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)

    assert not anti_loop.should_block_move(
        move_type="board_move",
        source=12,
        target=3,
        unit=teemo,
    )

def test_does_not_detect_cycle_from_disconnected_transitions():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    # Histórico desconexo: não representa uma sequência contínua.
    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 3, 12, nasus)
    anti_loop.register_move("board_move", 12, 15, nasus)

    # 15 -> 3 parece fechar um ciclo para a lógica atual,
    # mas o histórico não contém uma sequência contínua válida.
    assert not anti_loop.is_cycle_move(
        move_type="board_move",
        source=15,
        target=3,
        unit=nasus,
    )