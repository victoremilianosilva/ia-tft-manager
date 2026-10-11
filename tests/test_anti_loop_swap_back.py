
import pytest

from ai.AntiLoopManager import AntiLoopManager


@pytest.fixture
def anti_loop():
    return AntiLoopManager()


def test_blocks_swap_back_when_unit_identity_changes(anti_loop):
    """Bloqueia o desfazimento da troca, mesmo com outra unidade na origem."""
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    # Nasus e Teemo trocam entre as posições 3 e 10.
    anti_loop.register_move(
        "board_swap", 3, 10, nasus
    )

    # Após a troca, Teemo pode estar na posição 3.
    # A tentativa de trocar novamente deve ser bloqueada.
    assert anti_loop.should_block_move(
        move_type="board_swap",
        source=3,
        target=10,
        unit=teemo,
    )


def test_allows_swap_between_different_positions(anti_loop):
    """Não bloqueia uma troca que envolve outro par de posições."""
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    anti_loop.register_move(
        "board_swap", 3, 10, nasus
    )

    assert not anti_loop.should_block_move(
        move_type="board_swap",
        source=3,
        target=12,
        unit=teemo,
    )


def test_blocks_swap_back_with_reversed_positions(anti_loop):
    """Reconhece o mesmo par mesmo se origem e destino forem invertidos."""
    nasus = {"uuid": "nasus-1", "id": "Nasus", "star": 1}
    teemo = {"uuid": "teemo-1", "id": "Teemo", "star": 1}

    anti_loop.register_move(
        "board_swap", 3, 10, nasus
    )

    assert anti_loop.should_block_move(
        move_type="board_swap",
        source=10,
        target=3,
        unit=teemo,
    )
