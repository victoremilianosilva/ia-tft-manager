import numpy as np
import pytest

from reward_audit import RewardAuditLedger


def _inputs(*, action=None, combat=None, placement=None, combat_sequence=4,
           decision_sequence=10, episode_id=2, placements=None):
    action = np.zeros(8, dtype=np.float32) if action is None else np.asarray(action, dtype=np.float32)
    combat = np.zeros(8, dtype=np.float32) if combat is None else np.asarray(combat, dtype=np.float32)
    placement = np.zeros(8, dtype=np.float32) if placement is None else np.asarray(placement, dtype=np.float32)
    traces = [
        {
            "player_id": player_id,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        }
        for player_id in range(8)
    ]
    players = [
        {
            "player_id": player_id,
            "placement": None if placements is None else placements[player_id],
        }
        for player_id in range(8)
    ]
    source_sequence = decision_sequence - 1
    source_player_sequences = [source_sequence] * 8
    source_metadata = {
        "engine_instance_id": "engine-test",
        "episode_id": episode_id,
        "decision_sequence": source_sequence,
        "player_decision_sequences": source_player_sequences,
        "round": 6,
        "native_state_snapshot": {
            "engine_instance_id": "engine-test",
            "episode_id": episode_id,
            "snapshot_sequence": source_sequence,
            "player_decision_sequences": source_player_sequences,
            "combat_sequence": combat_sequence,
            "round": 6,
        },
    }
    metadata = {
        "engine_instance_id": "engine-test",
        "episode_id": episode_id,
        "decision_sequence": decision_sequence,
        "player_decision_sequences": [decision_sequence] * 8,
        "round": 7,
        "native_state_snapshot": {
            "engine_instance_id": "engine-test",
            "episode_id": episode_id,
            "snapshot_sequence": decision_sequence,
            "player_decision_sequences": [decision_sequence] * 8,
            "combat_sequence": combat_sequence,
            "round": 7,
        },
    }
    return {
        "rewards": action + combat + placement,
        "action_rewards": action,
        "combat_rewards": combat,
        "placement_rewards": placement,
        "action_traces": traces,
        "players": players,
        "decision_snapshot": metadata,
        "source_decision_snapshot": source_metadata,
    }


def _build(ledger, values):
    return ledger.build_record(**values)


def test_reward_audit_records_action_trace_and_authoritative_delayed_outcomes():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs(
        combat=[2.25, -2.25, 0, 0, 0, 0, 0, 0],
        placement=[0, 0, 0, 0, 0, 0, 0, -1],
        placements=[None, None, None, None, None, None, None, 8],
    )

    record = _build(ledger, values)

    assert record["contract_id"] == "tft.ppo.reward-audit.v1"
    assert record["temporal_credit_owner"] == "per_player_gae"
    assert record["source_decision_sequence"] == 9
    first = record["player_rewards"][0]
    assert first["player_decision_sequence"] == 9
    assert first["outcome_player_decision_sequence"] == 10
    assert first["action_decision"]["source_snapshot_sequence"] == 9
    assert first["action_decision"]["reward"] == 0.0
    assert first["combat_outcome"]["source"] == "native_pvp_resolution"
    assert first["combat_outcome"]["combat_sequence"] == 4
    assert first["terminal_placement"] is None
    last = record["player_rewards"][7]
    assert last["terminal_placement"]["source"] == "validated_terminal_placement"
    assert last["terminal_placement"]["placement"] == 8
    assert last["components"]["total"] == -1.0


def test_reward_audit_rejects_action_shaping_under_v1():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs(action=[0.1, 0, 0, 0, 0, 0, 0, 0])

    with pytest.raises(ValueError, match="action_reward neutro"):
        _build(ledger, values)


def test_reward_audit_rejects_total_that_does_not_match_components():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs(combat=[1, 0, 0, 0, 0, 0, 0, 0])
    values["rewards"][0] = 0.5

    with pytest.raises(ValueError, match="soma action"):
        _build(ledger, values)


def test_reward_audit_rejects_combat_reward_without_native_event_identity():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs(combat=[1, 0, 0, 0, 0, 0, 0, 0], combat_sequence=0)

    with pytest.raises(RuntimeError, match="combat_sequence"):
        _build(ledger, values)


def test_reward_audit_rejects_placement_reward_without_validated_placement():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs(placement=[0, 0, 0, 0, 0, 0, 0, -1])

    with pytest.raises(RuntimeError, match="colocação validada"):
        _build(ledger, values)


def test_reward_audit_deduplicates_combat_and_terminal_events_across_steps():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    first = _inputs(combat=[1, 0, 0, 0, 0, 0, 0, 0])
    _build(ledger, first)

    repeated = _inputs(
        combat=[1, 0, 0, 0, 0, 0, 0, 0],
        decision_sequence=11,
    )
    repeated["decision_snapshot"]["player_decision_sequences"] = [11] * 8
    with pytest.raises(RuntimeError, match="crédito repetido"):
        _build(ledger, repeated)


def test_reward_audit_rejects_cross_episode_or_snapshot_misalignment():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs()
    values["decision_snapshot"]["native_state_snapshot"]["snapshot_sequence"] = 9

    with pytest.raises(RuntimeError, match="desalinhados"):
        _build(ledger, values)



def test_reward_audit_deduplicates_terminal_placement_across_steps():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    first = _inputs(
        placement=[0, 0, 0, 0, 0, 0, 0, -1],
        placements=[None, None, None, None, None, None, None, 8],
    )
    _build(ledger, first)

    repeated = _inputs(
        placement=[0, 0, 0, 0, 0, 0, 0, -1],
        placements=[None, None, None, None, None, None, None, 8],
        decision_sequence=11,
    )
    with pytest.raises(RuntimeError, match="crédito repetido"):
        _build(ledger, repeated)


def test_reward_audit_rejects_misaligned_source_decision_snapshot():
    ledger = RewardAuditLedger()
    ledger.reset("engine-test", 2)
    values = _inputs()
    values["source_decision_snapshot"]["native_state_snapshot"]["snapshot_sequence"] = 8

    with pytest.raises(RuntimeError, match="pré-ação sem identidade nativa"):
        _build(ledger, values)
