"""Smoke test da interface Python fina sobre a lobby nativa C++."""
import numpy as np

from cpp_lobby_env import CppTFTLobbyWrapper
from reward_outcome_producers import build_action_outcome_events


def test_native_lobby_adapter_executes_a_step():
    lobby = CppTFTLobbyWrapper(seed=123)

    try:
        observations = lobby.reset(seed=123)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert np.isfinite(observations).all()

        # Todos os agentes passam; as regras e a resolução permanecem em C++.
        source_snapshot = lobby.get_snapshot_metadata()["native_state_snapshot"]
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
        assert info["action_context"]["contract_id"] == "tft.engine.action-context"
        assert info["action_context"]["contract_version"] == 1
        assert info["action_context"]["action_masks"].shape == (8, 1280)
        assert not info["action_context"]["action_masks"].flags.writeable
        assert len(info["action_outcome_events"]) == 8
        oracle_events = build_action_outcome_events(
            before_snapshot=source_snapshot,
            after_snapshot=info["decision_snapshot"]["native_state_snapshot"],
            action_traces=info["action_trace"],
        )
        for player_id, (event, oracle) in enumerate(zip(info["action_outcome_events"], oracle_events)):
            assert event["contract_id"] == "tft.engine.action-outcome-event"
            assert event["player_id"] == player_id
            assert event["action_family"] == oracle["action"]["family"] == "pass"
            assert event["action_type"] == oracle["action"]["type"] == 6
            assert event["handler_applied"] == oracle["action"]["handler_applied"] is True
            assert event["status_reason"] == oracle["action"]["status_reason"]
            assert event["outcome_player_decision_sequence"] == info["decision_snapshot"]["player_decision_sequences"][player_id]
    finally:
        lobby.close()
