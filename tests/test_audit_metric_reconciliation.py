from scripts.audit_viewer_match import (
    _validate_action_from_mask,
    audit_composition_direction_changes,
    audit_team_progression,
)


def test_action_validation_fallback_checks_conditional_parameters():
    mask = {
        "type_mask": [1, 0, 0, 1, 0, 0, 1, 1, 1],
        "shop_mask": [1, 0, 1],
        "bench_to_board_target_masks": [[0, 0, 0], [0, 0, 1]],
    }
    assert _validate_action_from_mask([0, 2], mask) is True
    assert _validate_action_from_mask([0, 1], mask) is False
    assert _validate_action_from_mask([3, 0, 1, 2], mask) is True
    assert _validate_action_from_mask([3, 0, 0, 2], mask) is False
    assert _validate_action_from_mask([7, 0, 0], mask) is None


def test_composition_audit_recovers_transition_from_before_after_states():
    report = {}
    entries = [{
        "event_type": "action",
        "sequence_id": 1,
        "step": 12,
        "round": "4-2",
        "payload": {
            "action_name": "BUY",
            "state_before": {"comp_direction": "CompA"},
            "state_after": {"comp_direction": "CompB"},
            "composition_diagnostics": {},
        },
    }]
    audit_composition_direction_changes(entries, "Jogador 1", report)
    metrics = report["composition_direction_metrics"]["Jogador 1"]
    assert metrics["direction_changes"] == 1
    assert metrics["details"][0]["from"] == "CompA"
    assert metrics["details"][0]["to"] == "CompB"
    assert metrics["details"][0]["reason"] == "state_transition_fallback"
    assert metrics["changes_without_measurable_gain"] == 1


def test_terminal_placement_is_kept_without_using_eliminated_economy():
    report = {}
    entries = [{
        "event_type": "action",
        "sequence_id": 1,
        "step": 99,
        "stage": 6,
        "round_in_stage": 5,
        "payload": {
            "action_name": "PASS",
            "state_before": {"board": [], "bench": [], "gold": 12, "level": 8, "hp": 1},
            "state_after": {
                "board": [],
                "bench": [],
                "gold": 0,
                "level": 8,
                "hp": 0,
                "alive": False,
                "eliminated": True,
                "placement": 5,
            },
        },
    }]
    audit_team_progression(entries, "Jogador 5", report)
    metrics = report["team_progression_metrics"]["Jogador 5"]
    assert metrics["final_placement"] == 5
    assert metrics["final_gold"] is None
    assert metrics["final_hp"] is None
