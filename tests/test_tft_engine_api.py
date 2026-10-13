
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
