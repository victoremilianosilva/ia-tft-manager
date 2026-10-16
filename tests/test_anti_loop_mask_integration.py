from types import SimpleNamespace

import numpy as np

from ai.ActionMaskManager import ActionMaskManager
from ai.AntiLoopManager import AntiLoopManager


class FakeBoardManager:
    def __init__(self):
        self.board = [None] * 28

    def get_empty_positions(self):
        return [
            i for i, unit in enumerate(self.board)
            if unit is None
        ]


class FakeBenchManager:
    def __init__(self):
        self.bench = [None] * 9

    def has_free_slot(self):
        return any(unit is None for unit in self.bench)


def create_manager():
    board = FakeBoardManager()
    bench = FakeBenchManager()
    anti_loop = AntiLoopManager()

    manager = ActionMaskManager.__new__(
        ActionMaskManager
    )
    manager.board_manager = board
    manager.bench_manager = bench
    manager.anti_loop_manager = anti_loop
    manager.economy_manager = SimpleNamespace(level=10)
    manager.board_size = 28
    manager.bench_size = 9
    manager.shop_size = 5

    return manager, board, bench, anti_loop



def test_mask_blocks_reverse_board_move():
    manager, board, _, anti_loop = create_manager()

    unit = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    # Nasus está em 10; a posição 3 ficou vazia
    # após o movimento original 3 -> 10.
    board.board[10] = unit

    anti_loop.register_move(
        "board_move", 3, 10, unit
    )

    # Retornar para a posição vazia anterior deve ser bloqueado.
    assert not manager._is_valid_board_move(10, 3)

    # Um destino diferente continua permitido.
    assert manager._is_valid_board_move(10, 12)


def test_mask_blocks_reverse_board_swap():
    manager, board, _, anti_loop = create_manager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    # Estado DEPOIS da troca original entre 3 e 10.
    board.board[3] = teemo
    board.board[10] = nasus

    # A troca original foi iniciada por Nasus em 3.
    anti_loop.register_move(
        "board_swap", 3, 10, nasus
    )

    # Nasus está em 10 e tentaria trocar de volta com Teemo.
    assert not manager._is_valid_board_move(10, 3)



def test_mask_blocks_explicitly_blocked_bench_move():
    manager, board, bench, anti_loop = create_manager()

    unit = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    bench.bench[2] = unit

    anti_loop.block_move(
        "bench_to_board", 2, 12, unit
    )

    assert not manager._is_valid_bench_board_move(2, 12)


def test_mask_allows_valid_bench_move():
    manager, board, bench, _ = create_manager()

    bench.bench[2] = {
        "uuid": "nasus-1",
        "id": "Nasus",
        "star": 1,
    }

    assert manager._is_valid_bench_board_move(2, 12)


def test_board_mask_excludes_reverse_destination():
    manager, board, _, anti_loop = create_manager()

    unit = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    board.board[10] = unit

    anti_loop.register_move(
        "board_move", 3, 10, unit
    )

    mask = manager.get_board_move_target_mask(10)

    assert mask[3] == 0
    assert mask[12] == 1
    assert np.isfinite(mask).all()

def test_bench_board_loop_does_not_block_unrelated_board_move():
    anti_loop = AntiLoopManager()
    unit = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    anti_loop.register_move("bench_to_board", 2, 10, unit)
    anti_loop.register_move("board_to_bench", 10, 2, unit)

    # O histórico indica alternância banco/tabuleiro.
    # Isso não significa que qualquer movimento posterior
    # da unidade no tabuleiro perpetue o mesmo ciclo.
    assert not anti_loop.should_block_move(
        move_type="board_move",
        source=10,
        target=12,
        unit=unit,
    )


def test_bench_board_loop_does_not_block_different_destination():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    anti_loop.register_move("bench_to_board", 2, 10, nasus)
    anti_loop.register_move("board_to_bench", 10, 2, nasus)

    # O histórico contém alternância, mas o candidato
    # utiliza outra origem e outro destino.
    assert not anti_loop.should_block_move(
        move_type="bench_to_board",
        source=4,
        target=12,
        unit=nasus,
    )


def test_bench_board_loop_detects_repeated_transition():
    anti_loop = AntiLoopManager()
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}

    anti_loop.register_move("bench_to_board", 2, 10, nasus)
    anti_loop.register_move("board_to_bench", 10, 2, nasus)

    # Repetir a mesma transição fecha o ciclo.
    assert anti_loop.should_block_move(
        move_type="bench_to_board",
        source=2,
        target=10,
        unit=nasus,
    )


def test_explicit_block_remains_active_without_state_change():
    manager, board, bench, anti_loop = create_manager()

    unit = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    bench.bench[2] = unit

    anti_loop.register_state(board.board, bench.bench)
    anti_loop.block_move("bench_to_board", 2, 12, unit)

    # O estado não mudou: o bloqueio continua válido.
    assert not manager._is_valid_bench_board_move(2, 12)


def test_explicit_block_is_released_after_state_change():
    manager, board, bench, anti_loop = create_manager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    bench.bench[2] = nasus

    # Registra o estado em que o movimento foi bloqueado.
    anti_loop.register_state(board.board, bench.bench)
    anti_loop.block_move("bench_to_board", 2, 12, nasus)

    assert not manager._is_valid_bench_board_move(2, 12)

    # Outro posicionamento altera a assinatura do estado.
    board.board[0] = teemo
    anti_loop.register_state(board.board, bench.bench)

    # O movimento voltou a ser considerado válido.
    assert manager._is_valid_bench_board_move(2, 12)

def test_mask_blocks_persistent_cycle_but_keeps_new_destination():
    manager, board, _, anti_loop = create_manager()

    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    board.board[12] = nasus

    # Primeira volta completa: 3 -> 10 -> 12 -> 3
    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)
    anti_loop.register_move("board_move", 12, 3, nasus)

    # A unidade repete o percurso até antes do segundo fechamento.
    anti_loop.register_move("board_move", 3, 10, nasus)
    anti_loop.register_move("board_move", 10, 12, nasus)

    mask = manager.get_board_move_target_mask(12)

    # O ciclo persistente deve ser bloqueado na máscara.
    assert mask[3] == 0

    # Uma posição nova deve continuar disponível.
    assert mask[15] == 1

def test_mask_queries_do_not_change_execution_metrics():
    manager, board, _, anti_loop = create_manager()

    nasus = {
        "uuid": "nasus-1",
        "id": "Nasus",
        "star": 1,
    }
    teemo = {
        "uuid": "teemo-1",
        "id": "Teemo",
        "star": 1,
    }

    board.board[10] = nasus
    board.board[12] = teemo

    # Cria um histórico que faz algumas consultas
    # de movimento passarem pelas regras anti-loop.
    anti_loop.register_move(
        "board_move", 3, 10, nasus
    )

    metrics_before = anti_loop.execution_metrics.copy()

    # Consultas típicas durante a criação das máscaras.
    manager.get_board_move_target_mask(10)
    manager.get_board_source_mask()
    manager.get_conditioned_board_target_mask()

    # Consultar diretamente também não deve registrar
    # uma tentativa nem um bloqueio de execução.
    anti_loop.should_block_move(
        move_type="board_move",
        source=10,
        target=3,
        unit=nasus,
    )

    assert anti_loop.execution_metrics == metrics_before