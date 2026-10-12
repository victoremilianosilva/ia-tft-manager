
from ai.AntiLoopManager import AntiLoopManager


def test_allows_first_closure_of_swap_cycle():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    # 🔄 Nasus passa pelas posições 3 → 10 → 12.
    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)

    # ✅ O primeiro fechamento do ciclo deve ser permitido.
    assert not anti_loop.should_block_move(
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

def test_blocks_repeated_swap_cycle():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    # 🔄 Primeiro ciclo completo.
    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)
    anti_loop.register_move("board_swap", 12, 3, nasus)

    # 🔄 A unidade repete o percurso.
    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)

    # 🚫 O segundo fechamento deve ser bloqueado.
    assert anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=3,
        unit=nasus,
    )

def test_swap_cycle_tracks_two_units_independently():
    anti_loop = AntiLoopManager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    # Nasus e Teemo trocam de posição.
    anti_loop.register_move("board_swap", 3, 10, nasus)

    # Depois da troca, Teemo ocupa a posição 3 e Nasus a posição 10.
    # O histórico de Teemo não deve ser confundido com o de Nasus.
    anti_loop.register_move("board_swap", 10, 12, teemo)

    # Um candidato de Nasus não deve ser bloqueado apenas
    # porque Teemo participou de outro swap.
    assert not anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=15,
        unit=nasus,
    )


def test_repeated_swap_cycle_blocks_closure_but_allows_new_destination():
    anti_loop = AntiLoopManager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    # Primeiro percurso do ciclo.
    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)
    anti_loop.register_move("board_swap", 12, 3, nasus)

    # Repetição do percurso, ainda sem fechar o segundo ciclo.
    anti_loop.register_move("board_swap", 3, 10, nasus)
    anti_loop.register_move("board_swap", 10, 12, nasus)

    # O segundo fechamento deve ser bloqueado.
    assert anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=3,
        unit=nasus,
    )

    # Um destino novo não deve ser bloqueado pelo ciclo anterior.
    assert not anti_loop.should_block_move(
        move_type="board_swap",
        source=12,
        target=15,
        unit=nasus,
    )


def test_reverse_swap_is_blocked_regardless_of_unit_identity():
    anti_loop = AntiLoopManager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    # Nasus troca com Teemo entre as posições 3 e 10.
    anti_loop.register_move("board_swap", 3, 10, nasus)

    # Como ambos trocaram de posição, a reversão pode ser
    # solicitada usando a identidade da outra unidade.
    assert anti_loop.should_block_move(
        move_type="board_swap",
        source=10,
        target=3,
        unit=teemo,
    )