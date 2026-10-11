
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
