import pytest

from reward_signal_calibration import (
    build_attribution_candidates,
    extract_native_outcome_events,
    validate_calibration_manifest,
)


def _action(seq, family="purchase", *, applied=True):
    return {
        "contract_id": "tft.reward-action-outcome.v1",
        "event_id": f"action-{seq}",
        "engine_instance_id": "engine",
        "episode_id": 1,
        "player_id": 0,
        "action": {"family": family, "handler_applied": applied},
        "source_decision": {"player_decision_sequence": seq},
        "outcome_snapshot": {"player_decision_sequence": seq + 1},
        "causal_attribution": "not_established",
        "reward_eligible": False,
    }


def _outcome(seq=3):
    return {
        "event_id": "combat-1",
        "engine_instance_id": "engine",
        "episode_id": 1,
        "player_id": 0,
        "player_decision_sequence": seq,
        "source": "native_pvp_resolution",
        "reward": 1.0,
    }


def test_exclusive_candidate_never_moves_native_reward():
    result = build_attribution_candidates(
        action_events=[_action(1)], outcome_events=[_outcome(3)]
    )[0]
    assert result["attribution"] == "exclusive_candidate"
    assert result["causal_attribution"] == "candidate_not_proven"
    assert result["reward"] is None
    assert result["reward_moved"] is False


def test_intervening_action_blocks_delayed_credit():
    result = build_attribution_candidates(
        action_events=[_action(1), _action(2, "xp_purchase")],
        outcome_events=[_outcome(3)],
    )[0]
    assert result["attribution"] == "ambiguous"
    assert result["action_event_id"] is None


def test_multiple_candidate_actions_are_ambiguous():
    result = build_attribution_candidates(
        action_events=[_action(1), _action(2, "purchase")],
        outcome_events=[_outcome(3)],
    )[0]
    assert result["attribution"] == "ambiguous"


def test_failed_handler_does_not_receive_attribution():
    result = build_attribution_candidates(
        action_events=[_action(1, applied=False)], outcome_events=[_outcome(2)]
    )[0]
    assert result["attribution"] == "unattributed"


def test_calibration_manifest_rejects_missing_evidence_and_split_overlap():
    with pytest.raises(ValueError, match="evidência obrigatória"):
        validate_calibration_manifest({})
    manifest = {
        "dataset_hash": "d", "code_revision": "c", "engine_revision": "e",
        "catalog_hash": "k", "train_episode_ids": ["a"],
        "validation_episode_ids": ["b"], "test_episode_ids": ["c"],
        "seed_manifest_hash": "s", "pre_registered_hypothesis": "h",
        "baseline_report_hash": "b", "candidate_report_hash": "c",
        "ablation_report_hash": "a",
    }
    assert validate_calibration_manifest(manifest)["reward_activation_allowed"] is False
    manifest["test_episode_ids"] = ["a"]
    with pytest.raises(ValueError, match="se sobrepõem"):
        validate_calibration_manifest(manifest)



def test_extracts_native_outcomes_from_reward_audit_identity():
    audit = {
        "contract_id": "tft.ppo.reward-audit.v1",
        "engine_instance_id": "engine",
        "episode_id": 1,
        "player_rewards": [
            {
                "player_id": player_id,
                "outcome_player_decision_sequence": 12,
                "combat_outcome": ({
                    "event_id": f"combat-{player_id}",
                    "source": "native_pvp_resolution",
                    "reward": 0.5,
                    "combat_sequence": 4,
                } if player_id == 0 else None),
                "terminal_placement": None,
            }
            for player_id in range(8)
        ],
    }
    outcomes = extract_native_outcome_events(audit)
    assert len(outcomes) == 1
    assert outcomes[0]["event_id"] == "combat-0"
    assert outcomes[0]["player_decision_sequence"] == 12
    assert outcomes[0]["engine_instance_id"] == "engine"



def test_duplicate_native_outcome_event_id_is_rejected():
    duplicate = _outcome(3)
    with pytest.raises(ValueError, match="duplicado"):
        build_attribution_candidates(
            action_events=[_action(1)],
            outcome_events=[duplicate, dict(duplicate)],
        )
