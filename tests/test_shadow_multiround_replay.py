"""Deterministic multi-round integration replay for the read-only Shadow pipeline."""
import json

import pytest

try:
    from cpp_lobby_env import CppTFTLobbyWrapper
except ImportError:
    pytest.skip("tft_engine ainda nao foi compilado.", allow_module_level=True)


PASS = [6, 0, 0, 0, 0, 0]
PASS_BATCH = [PASS[:] for _ in range(CppTFTLobbyWrapper.PLAYERS_PER_LOBBY)]
ACTIONS_PER_ROUND = 15


def _advance_rounds(engine, rounds):
    info = None
    for _ in range(rounds * ACTIONS_PER_ROUND):
        _, _, done, info = engine.step(PASS_BATCH)
        assert not done, "O replay de preparação não deve encerrar a partida."
    return info


def _records(engine):
    return [json.loads(line) for line in engine.get_composition_diagnostics_jsonl()]


def test_shadow_pipeline_replays_multiple_rounds_with_correlated_sequences(monkeypatch):
    monkeypatch.setenv("TFT_COMPOSITION_INTELLIGENCE_SHADOW", "1")
    engine = CppTFTLobbyWrapper(seed=20261119)
    try:
        engine.reset(seed=20261119)
        initial = engine.get_snapshot_metadata()
        final_info = _advance_rounds(engine, 9)
        final = engine.get_snapshot_metadata()

        assert final["engine_instance_id"] == initial["engine_instance_id"]
        assert final["episode_id"] == initial["episode_id"]
        assert final["decision_sequence"] > initial["decision_sequence"]
        assert final_info["round"] >= 9

        records = _records(engine)
        assert records, "A pipeline Shadow habilitada não publicou snapshots multi-round."
        sequences = [record["sequence"] for record in records]
        assert sequences == sorted(sequences)
        assert len(sequences) == len(set(sequences))
        assert sequences == list(range(1, len(sequences) + 1))

        observed_rounds = set()
        observed_players = set()
        for record in records:
            assert record["engine_match_id"] == initial["episode_id"]
            assert isinstance(record["round"], int) and record["round"] >= 1
            assert 0 <= record["player_id"] < CppTFTLobbyWrapper.PLAYERS_PER_LOBBY
            assert record.get("shadow_only") is True
            assert record.get("execution_enabled") is False
            assert record.get("native_action_applied") is False
            comparison = record.get("action_evaluator_comparison")
            assert isinstance(comparison, dict)
            comparison_result = comparison.get("comparison", {})
            if comparison_result.get("initial_candidate_count") == 0:
                assert comparison_result.get("comparison_available") is False
            observed_rounds.add(record["round"])
            observed_players.add(record["player_id"])

        assert len(observed_rounds) >= 2, "O replay não atravessou múltiplas rodadas Shadow."
        assert observed_players, "Nenhum jogador produziu evidência Shadow."

        # Reset must retire the previous replay history and advance the episode scope.
        engine.reset(seed=20261119)
        reset = engine.get_snapshot_metadata()
        assert reset["engine_instance_id"] == initial["engine_instance_id"]
        assert reset["episode_id"] > initial["episode_id"]
        assert _records(engine) == []
    finally:
        engine.close()


def test_shadow_pipeline_feature_flag_off_emits_no_composition_snapshots(monkeypatch):
    monkeypatch.setenv("TFT_COMPOSITION_INTELLIGENCE_SHADOW", "0")
    engine = CppTFTLobbyWrapper(seed=20261120)
    try:
        engine.reset(seed=20261120)
        _advance_rounds(engine, 2)
        assert _records(engine) == []
    finally:
        engine.close()
