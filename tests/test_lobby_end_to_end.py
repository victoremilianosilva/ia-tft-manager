"""Smoke test da interface Python fina sobre a lobby nativa C++."""
import numpy as np

from cpp_lobby_env import CppTFTLobbyWrapper


def test_native_lobby_adapter_executes_a_step():
    lobby = CppTFTLobbyWrapper(seed=123)

    try:
        observations = lobby.reset(seed=123)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert np.isfinite(observations).all()

        # Todos os agentes passam; as regras e a resolução permanecem em C++.
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        next_observations, rewards, done, info = lobby.step(actions)

        assert next_observations.shape == observations.shape
        assert rewards.shape == (8,)
        assert np.isfinite(next_observations).all()
        assert np.isfinite(rewards).all()
        assert isinstance(done, bool)
        assert len(info["players"]) == 8
        assert info["round"] >= 1
        assert info["lobby_done"] is done
        assert len(info["action_outcome_events"]) == 8
        for player_id, event in enumerate(info["action_outcome_events"]):
            assert event["contract_id"] == "tft.engine.action-outcome-event"
            assert event["player_id"] == player_id
            assert event["action_family"] == "pass"
            assert event["handler_applied"] is True
            assert event["outcome_player_decision_sequence"] == info["decision_snapshot"]["player_decision_sequences"][player_id]
    finally:
        lobby.close()
