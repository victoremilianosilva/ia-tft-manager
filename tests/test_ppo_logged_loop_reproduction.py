"""Reproduz oscilações do viewer pelo caminho real de amostragem da policy PPO.

Os logs guardam nomes de unidades, mas não um snapshot completo de slots para cada
linha; por isso cada caso reproduz a topologia do loop (duas unidades alternando
entre dois slots), não pretende ser replay byte a byte da partida.

A máscara é deliberadamente configurada para permitir a reversão. Isso isola a
pergunta: a policy PPO consegue produzir o loop observado quando a proteção não
o remove? O teste passa quando o loop é reproduzido. Ele NÃO afirma que a máscara
nativa C++ permitiu o mesmo movimento; isso exige um replay integrado do estado.
"""
import pytest
import torch

from policy import TFTPolicy


PLAYERS = 8
ACTION_DIMS = [7, 5, 9, 28, 28, 28]
OBS_DIM = 22 + (4 * 7 * 5) + (1 + 4 * 7) + ((9 + 5) * 8)

# Top pair de movimento reportado na auditoria dos oito .tft.
# counts são frequências observadas no log, não IDs de slots.
LOGGED_PAIR_CASES = [
    ("P1", "Nasus", "Twisted Fate", 18),
    ("P2", "Jax", "Teemo", 17),
    ("P3", "Jax", "Poppy", 21),
    ("P4", "Leona", "Teemo", 13),
    ("P5", "Illaoi", "Twisted Fate", 10),
    ("P6", "Teemo", "Veigar", 15),
    ("P7", "Fizz", "Gnar", 17),
    ("P8", "Teemo", "Twisted Fate", 16),
]


def _masks_for_forced_board_swap(source: int, target: int):
    """Máscaras com a mesma estrutura entregue ao PPO; só um swap é elegível."""
    masks = {
        "type_mask": torch.zeros(PLAYERS, 7, dtype=torch.bool),
        "shop_mask": torch.ones(PLAYERS, 5, dtype=torch.bool),
        "bench_source_mask": torch.ones(PLAYERS, 9, dtype=torch.bool),
        "board_target_mask": torch.ones(PLAYERS, 28, dtype=torch.bool),
        "board_source_mask": torch.ones(PLAYERS, 28, dtype=torch.bool),
        "board_move_target_masks": torch.ones(PLAYERS, 28, 28, dtype=torch.bool),
        "bench_move_source_mask": torch.ones(PLAYERS, 9, dtype=torch.bool),
        "bench_to_board_target_masks": torch.ones(PLAYERS, 9, 28, dtype=torch.bool),
    }

    # Os outros sete agentes passam. O agente 0 recebe um MOVE_BOARD obrigatório.
    masks["type_mask"][:, 6] = True
    masks["type_mask"][0] = False
    masks["type_mask"][0, 4] = True

    masks["board_source_mask"][0] = False
    masks["board_source_mask"][0, source] = True
    masks["board_move_target_masks"][0] = False
    masks["board_move_target_masks"][0, source, target] = True
    return masks


@pytest.mark.parametrize(
    "player,unit_a,unit_b,observed_count",
    LOGGED_PAIR_CASES,
    ids=[case[0] for case in LOGGED_PAIR_CASES],
)
def test_ppo_reproduces_logged_two_unit_oscillation_when_reverse_is_unmasked(
    player, unit_a, unit_b, observed_count
):
    """Prova reproduzível de que o caminho PPO executa o ciclo se a mask o permite."""
    torch.manual_seed(20261022)
    policy = TFTPolicy(obs_dim=OBS_DIM, action_dims=ACTION_DIMS, hidden_size=32)
    policy.eval()

    # Modelo observa o formato real; os masks são os do contrato PPO (8 agentes).
    obs = torch.zeros(PLAYERS, OBS_DIM, dtype=torch.float32)
    board = {0: unit_a, 1: unit_b}
    initial_board = dict(board)
    moves = []

    with torch.no_grad():
        for step in range(observed_count):
            # Alterna a unidade selecionada, tal como a identidade troca de slot.
            source = next(slot for slot, name in board.items()
                          if name == (unit_a if step % 2 == 0 else unit_b))
            target = 1 - source
            masks = _masks_for_forced_board_swap(source, target)
            actions, logprob, entropy, values = policy.get_action_and_value(
                obs, masks=masks, deterministic=True
            )

            chosen = actions[0].tolist()
            assert chosen[0] == 4, f"{player}: PPO não escolheu MOVE_BOARD: {chosen}"
            assert chosen[4] == source, f"{player}: origem inesperada: {chosen}"
            assert chosen[5] == target, f"{player}: destino inesperado: {chosen}"
            assert torch.isfinite(logprob).all()
            assert torch.isfinite(entropy).all()
            assert torch.isfinite(values).all()

            # Aplicar o swap real ao pequeno estado de teste.
            board[source], board[target] = board[target], board[source]
            moves.append((source, target, board[0], board[1]))

            # Cada par de swaps restaura exatamente o estado anterior: ciclo A-B-A.
            if (step + 1) % 2 == 0:
                assert board == initial_board, (
                    f"{player}: o par {unit_a}/{unit_b} não retornou ao estado "
                    f"original após {step + 1} movimentos"
                )

    assert len(moves) == observed_count
    assert moves[0][2:] == (unit_b, unit_a)
    assert moves[1][2:] == (unit_a, unit_b)
