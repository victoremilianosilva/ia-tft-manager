
import pytest


def test_single_board_unit_can_move_to_empty_position():
    """
    Auditoria:
    uma unidade no tabuleiro deve poder mudar para
    uma posição vazia, desde que o movimento seja legal.

    A preparação do ambiente e a chamada à máscara devem
    usar as fixtures/helpers já existentes no projeto.
    """
    pytest.skip(
        "Ligar ao fixture real do ActionMaskManager após "
        "confirmar seu construtor e a API de geração das máscaras."
    )
