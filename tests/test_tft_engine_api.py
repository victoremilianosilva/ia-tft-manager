
import numpy as np
import pytest

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