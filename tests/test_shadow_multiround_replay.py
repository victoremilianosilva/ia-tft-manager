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
        final_info = _advance_rounds(engine, 10)
        final = engine.get_snapshot_metadata()

        assert final["engine_instance_id"] == initial["engine_instance_id"]
        assert final["episode_id"] == initial["episode_id"]
        assert final["decision_sequence"] > initial["decision_sequence"]
        assert final_info["round"] >= 9

        records = _records(engine)
        assert records, "A pipeline Shadow habilitada não publicou snapshots multi-round."
        native_audit = engine.get_audit_snapshot()
        latest_by_player = {}
        for record in records:
            previous = latest_by_player.get(record["player_id"])
            if previous is None or record["sequence"] > previous["sequence"]:
                latest_by_player[record["player_id"]] = record
        for player in native_audit.get("players", []):
            record = latest_by_player.get(player.get("player_id"))
            if record is None:
                continue
            resolution = record["action_evaluator_comparison"]["native_action_resolution"]
            assert player["strategic_state"]["strategic_context_sequence"] == (
                resolution["identity"]["source_sequence"]
            )
        sequences = [record["sequence"] for record in records]
        assert sequences == sorted(sequences)
        assert len(sequences) == len(set(sequences))
        assert all(right > left for left, right in zip(sequences, sequences[1:]))

        observed_rounds = set()
        observed_players = set()
        correlated_outcomes = []
        for record in records:
            assert record["engine_match_id"] == initial["episode_id"]
            assert isinstance(record["round"], int) and record["round"] >= 1
            assert 0 <= record["player_id"] < CppTFTLobbyWrapper.PLAYERS_PER_LOBBY
            diagnostics = record.get("diagnostics")
            assert isinstance(diagnostics, dict)
            for component in (
                "source_metadata", "composition_decision", "transition_plan",
                "unit_priority_evidence_consumption", "unit_intentions",
                "lineup_plan", "evidence", "action_recommendation",
                "outcome_observation", "recommendation_to_later_outcome",
            ):
                assert component in diagnostics
            assert isinstance(diagnostics["lineup_plan"].get("selected_board"), list)
            assert isinstance(diagnostics["action_recommendation"].get("candidates"), list)
            outcome = diagnostics.get("outcome_observation")
            correlation = diagnostics.get("recommendation_to_later_outcome")
            if outcome is not None:
                assert isinstance(outcome.get("observed_round"), int)
                assert outcome["observed_round"] > record["round"] - 1
                assert outcome.get("interpretation") == "correlation_only_not_causation"
            if correlation is not None:
                assert correlation["match_id"] == initial["episode_id"]
                assert correlation["player_id"] == record["player_id"]
                assert correlation["recommendation_round"] < correlation["outcome_round"]
                assert correlation["recommendation_sequence"] > 0
                assert correlation["interpretation"] == "correlation_only_not_causation"
                correlated_outcomes.append(correlation)

            comparison = record.get("action_evaluator_comparison")
            assert isinstance(comparison, dict)
            assert comparison.get("shadow_only") is True
            assert comparison.get("executor_connected") is True
            assert comparison.get("execution_enabled") is False
            assert comparison.get("native_action_applied") is False
            for component in (
                "candidate_generation", "baseline", "contextual",
                "strategic_positioning", "native_action_resolution", "comparison",
            ):
                assert component in comparison
            assert isinstance(record.get("context_bridge"), dict)
            comparison_result = comparison.get("comparison", {})
            if comparison_result.get("initial_candidate_count") == 0:
                assert comparison_result.get("comparison_available") is False
            observed_rounds.add(record["round"])
            observed_players.add(record["player_id"])

        assert len(observed_rounds) >= 2, "O replay não atravessou múltiplas rodadas Shadow."
        assert observed_players, "Nenhum jogador produziu evidência Shadow."
        assert correlated_outcomes, "O replay não correlacionou uma recomendação anterior com um outcome posterior."

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


def test_generated_strategic_replay_artifact_is_loadable_by_viewer():
    from pathlib import Path
    from viewer.session import ViewerSession

    artifact = Path(__file__).resolve().parents[1] / "cpp" / "build" / "strategic_integrated_replay.jsonl"
    if not artifact.is_file():
        pytest.skip("O artefato CTest só existe após executar o replay nativo integrado.")

    session = ViewerSession()
    count = session.load_replay(artifact)
    assert count == 8
    events = [session.replay_event(index) for index in range(count)]
    assert [item["sequence_id"] for item in events] == list(range(1, 9))
    assert all(item["event_type"] == "strategic_replay_scenario" for item in events)
    scenarios = [item["payload"]["scenario"] for item in events]
    assert scenarios == [
        "buy_upgrade", "sell", "positioning", "stale_same_round",
        "pivot_invalidates_old_recommendation", "contradictory_evidence",
        "no_candidates", "executor_reset",
    ]
    assert all(item["payload"].get("native_action_applied") is False for item in events[:5])
    assert all(item["payload"].get("execution_attempted") is False for item in events[:5])
