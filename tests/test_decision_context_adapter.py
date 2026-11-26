from trainer import Trainer
import pytest
from decision_identity import build_player_identity_envelopes


def _snapshot():
    player_sequences = list(range(11, 19))
    snapshot = {
        "engine_instance_id": "engine-decision-context",
        "episode_id": 7,
        "decision_sequence": 31,
        "round": 9,
        "stage": 3,
        "player_decision_sequences": player_sequences,
    }
    snapshot["player_identity_envelopes"] = build_player_identity_envelopes(snapshot)
    snapshot["native_state_snapshot"] = {
        "contract_id": "tft.native-state-snapshot",
        "contract_version": 6,
        "producer": "TFTEngine::get_audit_snapshot",
        "source_namespace": "tft.engine.observation-snapshot",
        "engine_instance_id": snapshot["engine_instance_id"],
        "episode_id": snapshot["episode_id"],
        "snapshot_sequence": snapshot["decision_sequence"],
        "player_decision_sequences": player_sequences,
        "round": snapshot["round"],
        "stage": snapshot["stage"],
        "combat_sequence": 12,
        "shared_pool": {"total_available": 42, "champions": []},
        "players": [
            {
                "player_id": player_id,
                "strategic_state": {"contract_id": "tft.strategic-owner-observation"},
                "board_relations": [],
                "actions_taken_this_round": player_id,
                "board_move_age": [0] * 28,
                "action_history_contract_id": "tft.player-action-history",
                "action_history_contract_version": 1,
                "recent_action_history": [{
                    "source_player_decision_sequence": 10 + player_id,
                    "outcome_player_decision_sequence": 11 + player_id,
                    "source_snapshot_sequence": 30,
                    "outcome_snapshot_sequence": 31,
                    "source_round": 4,
                    "outcome_round": 4,
                    "source_stage": 2,
                    "outcome_stage": 2,
                    "action_type": 6,
                    "handler_applied": True,
                }],
            }
            for player_id in range(8)
        ],
    }
    return snapshot


def test_decision_context_shares_lobby_facts_and_keeps_player_views_separate():
    expanded = Trainer._expand_lobby_snapshot_metadata(
        [_snapshot()], players_per_lobby=8, label="decision-context"
    )

    assert len(expanded) == 8
    contexts = [row["decision_context"] for row in expanded]
    assert all(context["contract_id"] == "tft.decision-context.player" for context in contexts)
    assert all(context["contract_version"] == 1 for context in contexts)
    assert all(context["lobby"] is contexts[0]["lobby"] for context in contexts)
    assert contexts[0]["lobby"]["contract_id"] == "tft.decision-context.lobby"
    assert contexts[0]["lobby"]["identity"]["snapshot_sequence"] == 31
    assert contexts[0]["lobby"]["shared_pool"]["total_available"] == 42

    for player_id, (row, context) in enumerate(zip(expanded, contexts)):
        assert context["player_id"] == player_id
        assert context["player_decision_sequence"] == 11 + player_id
        assert context["audit_player"] is row["native_player_state"]
        assert context["strategic"] is context["audit_player"]["strategic_state"]
        assert len(context["positioning"]) == 0
        assert context["temporal"]["actions_taken_this_round"] == player_id
        assert context["temporal"]["board_move_age"] == [0] * 28
        assert context["temporal"]["action_history_contract_id"] == "tft.player-action-history"
        assert context["temporal"]["recent_action_history"][0]["action_type"] == 6
        assert context["action_execution"] is None


def test_action_trace_is_attached_only_to_matching_decision_context():
    expanded = Trainer._expand_lobby_snapshot_metadata(
        [_snapshot()], players_per_lobby=8, label="decision-context"
    )
    traces = [
        {
            "contract_id": "tft.action-execution-event",
            "contract_version": 1,
            "source_namespace": "tft.engine.action-execution",
            "producer": "TFTEngine::step",
            "player_id": player_id,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
            "source_snapshot_sequence": 30,
            "outcome_snapshot_sequence": 31,
            "source_player_decision_sequence": 10 + player_id,
            "outcome_player_decision_sequence": 11 + player_id,
        }
        for player_id in range(8)
    ]
    infos = [{"action_trace": traces}]
    Trainer._attach_native_action_traces(expanded, infos, players_per_lobby=8)

    for player_id, row in enumerate(expanded):
        assert row["decision_context"]["action_execution"] == traces[player_id]

def test_action_context_rejects_boolean_contract_version():
    expanded = Trainer._expand_lobby_snapshot_metadata(
        [_snapshot()], players_per_lobby=8, label="decision-context"
    )
    traces = [
        {
            "contract_id": "tft.action-execution-event",
            "contract_version": True,
            "source_namespace": "tft.engine.action-execution",
            "producer": "TFTEngine::step",
            "player_id": player_id,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        }
        for player_id in range(8)
    ]
    with pytest.raises(RuntimeError, match="Contrato de Action Context"):
        Trainer._attach_native_action_traces(
            expanded, [{"action_trace": traces}], players_per_lobby=8
        )
