
import numpy as np
import pytest
ACTION_DIMS = (7, 5, 9, 28, 28, 28)
try:
    from tft_engine import TFTLobby
except ImportError:
    pytest.skip(
        "tft_engine ainda nao foi compilado.",
        allow_module_level=True,
    )


def test_lobby_reset_contract():
    engine = TFTLobby(seed=2026)

    try:
        result = engine.reset()

        assert "observations" in result
        assert "action_masks" in result

        observations = result["observations"]

        assert isinstance(observations, np.ndarray)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert observations.shape[1] > 0

        assert len(result["action_masks"]) == 8
    finally:
        engine.close()


def test_lobby_step_contract():
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        # PASS deve ser substituido pelo indice real da acao
        # neutra definido pela implementacao C++.
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]

        result = engine.step(actions)

        assert result["observations"].shape == (
            8,
            engine.observation_dim,
        )
        assert result["rewards"].shape == (8,)
        assert result["dones"].shape == (8,)
        assert len(result["action_masks"]) == 8
        assert isinstance(result["lobby_done"], bool)

                # O estado público deve refletir o resultado do step.
        state = engine.get_public_state()

        assert state["round"] == 2
        assert state["round_index"] == 1
        assert state["stage"] == 1

        # A última posição da observação provisória representa a rodada.
        assert np.all(result["observations"][:, -1] == 2)
        
    finally:
        engine.close()


def test_public_state_matches_python_lobby_contract():
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()
        state = engine.get_public_state()

        assert isinstance(state, dict)

        expected_keys = {
            "stage",
            "round",
            "round_index",
            "finished",
            "winner_id",
            "ranking",
            "alive_players",
            "players",
        }
        assert expected_keys.issubset(state.keys())

        assert state["stage"] == 1
        assert state["round"] == 1
        assert state["round_index"] == 0
        assert state["finished"] is False
        assert state["winner_id"] is None
        assert state["ranking"] == []
        assert state["alive_players"] == list(range(8))

        players = state["players"]
        assert isinstance(players, list)
        assert len(players) == 8

        assert [
            player["player_id"] for player in players
        ] == list(range(8))

        expected_player_keys = {
            "player_id", "hp", "gold", "level", "xp",
            "alive", "eliminated", "wins", "losses",
            "placement", "opponent_id", "damage_taken",
        }
        assert expected_player_keys.issubset(players[0].keys())

    finally:
        engine.close()

def test_public_round_and_stage_remain_consistent():
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]

        # Sete avanços levam a partida para a rodada pública 8.
        for _ in range(7):
            engine.step(actions)

        state = engine.get_public_state()

        assert state["round"] == 8
        assert state["round_index"] == 7
        assert state["stage"] == 2

    finally:
        engine.close()


def test_action_dimensions_accept_highest_valid_indices():
    """Cada componente aceita seu maior índice válido."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        actions = [
            [dimension - 1 for dimension in ACTION_DIMS]
            for _ in range(8)
        ]

        result = engine.step(actions)

        assert result["observations"].shape == (
            8,
            engine.observation_dim,
        )
    finally:
        engine.close()


@pytest.mark.parametrize(
    ("component", "invalid_value"),
    [
        (component, invalid_value)
        for component, dimension in enumerate(ACTION_DIMS)
        for invalid_value in (-1, dimension)
    ],
)
def test_action_dimensions_reject_out_of_range_indices(
    component,
    invalid_value,
):
    """Cada dimensão rejeita índices negativos e acima do limite."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0][component] = invalid_value

        with pytest.raises(
            ValueError,
            match="Componente de acao fora dos limites",
        ):
            engine.step(actions)

        # A ação inválida não deve avançar a partida.
        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


@pytest.mark.parametrize(
    "actions",
    [
        [[6, 0, 0, 0, 0, 0] for _ in range(7)],
        [[6, 0, 0, 0, 0] for _ in range(8)],
        [[6, 0, 0, 0, 0, 0, 0] for _ in range(8)],
    ],
)
def test_step_rejects_wrong_action_shape(actions):
    """O binding exige 8 jogadores e 6 componentes por ação."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises(ValueError):
            engine.step(actions)

        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


def test_observation_reward_done_and_mask_formats():
    engine = TFTLobby(seed=2026)

    try:
        reset_result = engine.reset()

        # Observações do reset.
        observations = reset_result["observations"]
        assert isinstance(observations, np.ndarray)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert observations.dtype == np.float32

        # Máscaras retornadas pelo reset.
        masks = reset_result["action_masks"]
        assert len(masks) == 8

        expected_shapes = {
            "type_mask": (7,),
            "shop_mask": (5,),
            "bench_source_mask": (9,),
            "board_target_mask": (28,),
            "board_source_mask": (28,),
            "board_move_target_masks": (28, 28),
            "bench_move_source_mask": (9,),
            "bench_to_board_target_masks": (9, 28),
        }

        for player_masks in masks:
            assert isinstance(player_masks, dict)

            for name, shape in expected_shapes.items():
                mask = player_masks[name]
                assert isinstance(mask, np.ndarray), name
                assert mask.shape == shape, name
                assert mask.dtype == np.bool_, name

        # Resultado do step.
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        step_result = engine.step(actions)

        assert step_result["observations"].shape == (
            8,
            engine.observation_dim,
        )
        assert step_result["observations"].dtype == np.float32

        assert step_result["rewards"].shape == (8,)
        assert step_result["rewards"].dtype == np.float32

        assert step_result["dones"].shape == (8,)
        assert step_result["dones"].dtype == np.bool_

        assert len(step_result["action_masks"]) == 8

    finally:
        engine.close()

def test_reset_accepts_missing_seed():
    """reset() e reset(seed=None) devem funcionar."""
    engine = TFTLobby(seed=2026)

    try:
        result_default = engine.reset()
        assert result_default["observations"].shape == (
            8,
            engine.observation_dim,
        )

        result_none = engine.reset(seed=None)
        assert result_none["observations"].shape == (
            8,
            engine.observation_dim,
        )

        # Cada reset inicia um novo episódio.
        assert result_none["episode_id"] > result_default["episode_id"]

    finally:
        engine.close()


@pytest.mark.parametrize(
    "invalid_seed",
    [
        -1,
        "seed_invalida",
        1.5,
    ],
)
def test_reset_rejects_invalid_seed(invalid_seed):
    """Seeds inválidas devem gerar erro Python controlado."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        previous_episode_id = engine.episode_id
        previous_state = engine.get_public_state()

        with pytest.raises((TypeError, ValueError, OverflowError)):
            engine.reset(seed=invalid_seed)

        # Uma falha de validação não deve reiniciar o episódio.
        assert engine.episode_id == previous_episode_id
        assert engine.get_public_state()["round"] == (
            previous_state["round"]
        )

    finally:
        engine.close()


def test_step_rejects_missing_actions():
    """step(None) deve falhar sem avançar a rodada."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises((TypeError, ValueError)):
            engine.step(None)

        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0

    finally:
        engine.close()


def test_engine_rejects_operations_after_close():
    """Operações após close() devem falhar de forma controlada."""
    engine = TFTLobby(seed=2026)
    engine.reset()
    engine.close()

    actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]

    with pytest.raises(RuntimeError, match="fechado"):
        engine.reset()

    with pytest.raises(RuntimeError, match="fechado"):
        engine.step(actions)

    with pytest.raises(RuntimeError, match="fechado"):
        engine.get_public_state()


def test_default_action_masks_have_valid_fallbacks():
    engine = TFTLobby(seed=2026)

    try:
        result = engine.reset()
        masks_by_player = result["action_masks"]

        assert len(masks_by_player) == 8

        for masks in masks_by_player:
            # Toda dimensão categórica precisa ter
            # pelo menos uma opção válida.
            assert masks["type_mask"].any()
            assert masks["shop_mask"].any()
            assert masks["bench_source_mask"].any()
            assert masks["board_target_mask"].any()
            assert masks["board_source_mask"].any()
            assert masks["bench_move_source_mask"].any()

            assert masks["board_move_target_masks"].shape == (28, 28)
            assert masks["board_move_target_masks"].any()

            assert masks["bench_to_board_target_masks"].shape == (9, 28)
            assert masks["bench_to_board_target_masks"].any()

            # A única ação habilitada na cabeça de tipo é PASS.
            assert masks["type_mask"][6]
            assert masks["type_mask"].sum() == 1

    finally:
        engine.close()


def test_step_rejects_none_without_advancing_round():
    """Entrada ausente deve gerar erro sem alterar o estado."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises(TypeError):
            engine.step(None)

        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


@pytest.mark.parametrize(
    ("seed", "expected_error"),
    [
        ("2026", TypeError),  # Texto não é aceito.
        (True, TypeError),    # Booleano não é aceito.
        (-1, ValueError),     # Seed negativa.
        (2**64, ValueError),  # Acima do limite de uint64.
    ],
)
def test_reset_rejects_invalid_seed(seed, expected_error):
    """O reset deve rejeitar seeds inválidas."""
    engine = TFTLobby(seed=2026)

    try:
        engine.reset()

        with pytest.raises(expected_error):
            engine.reset(seed=seed)

        # O reset inválido não deve iniciar outra rodada.
        state = engine.get_public_state()
        assert state["round"] == 1
        assert state["round_index"] == 0
    finally:
        engine.close()


def test_operations_after_close_raise_runtime_error():
    """O motor fechado não deve aceitar novas operações."""
    engine = TFTLobby(seed=2026)
    engine.reset()
    engine.close()

    with pytest.raises(RuntimeError):
        engine.reset()

    with pytest.raises(RuntimeError):
        engine.step([[6, 0, 0, 0, 0, 0] for _ in range(8)])
