
from ai.AntiLoopManager import AntiLoopManager


def test_allows_first_closure_of_three_position_cycle():
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

def test_allows_first_closure_of_three_position_cycle():
    anti_loop = AntiLoopManager()
    unit = {"uuid": "nasus-1"}

    anti_loop.register_move("board_move", 3, 10, unit)
    anti_loop.register_move("board_move", 10, 12, unit)

    # 🔓 Primeiro fechamento: ainda permite o movimento.
    assert not anti_loop.is_cycle_move(
        "board_move", 12, 3, unit
    )


def test_blocks_persistent_three_position_cycle():
    anti_loop = AntiLoopManager()
    unit = {"uuid": "nasus-1"}

    # 🔁 Primeira volta completa.
    anti_loop.register_move("board_move", 3, 10, unit)
    anti_loop.register_move("board_move", 10, 12, unit)
    anti_loop.register_move("board_move", 12, 3, unit)

    # 🔁 A unidade começa a repetir a mesma sequência.
    anti_loop.register_move("board_move", 3, 10, unit)
    anti_loop.register_move("board_move", 10, 12, unit)

    # 🚫 O segundo fechamento deve ser detectado.
    assert anti_loop.is_cycle_move(
        "board_move", 12, 3, unit
    )


def test_allows_move_to_new_position_after_cycle():
    anti_loop = AntiLoopManager()
    unit = {"uuid": "nasus-1"}

    anti_loop.register_move("board_move", 3, 10, unit)
    anti_loop.register_move("board_move", 10, 12, unit)
    anti_loop.register_move("board_move", 12, 3, unit)
    anti_loop.register_move("board_move", 3, 10, unit)
    anti_loop.register_move("board_move", 10, 12, unit)

    # 🆕 Uma posição nova não deve ser bloqueada como ciclo.
    assert not anti_loop.is_cycle_move(
        "board_move", 12, 15, unit
    )

def test_cycle_history_of_another_unit_does_not_block():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1"}
    teemo = {"uuid": "teemo-1"}

    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)
    anti_loop.register_move("board_move", 12, 3, nasus)
    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)

    # 🧍 O histórico do Nasus não bloqueia o Teemo.
    assert not anti_loop.is_cycle_move(
        "board_move", 12, 3, teemo
    )