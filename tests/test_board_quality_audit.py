from audit_viewer_match import audit_board_quality


def test_board_quality_audit_tracks_action_delta_and_combat_context():
    entries = [
        {
            "event_type": "action",
            "payload": {
                "action_name": "MOVE_BOARD",
                "combat_reward": 0.0,
                "state_before": {"board_structural_score": -0.5},
                "state_after": {
                    "board_quality_score": 0.7,
                    "board_quality_delta": 0.2,
                    "board_structural_score": -0.1,
                },
            },
        },
        {
            "event_type": "action",
            "payload": {
                "action_name": "MOVE_BOARD",
                "combat_reward": -1.0,
                "state_before": {"board_structural_score": -0.1},
                "state_after": {
                    "board_quality_score": 0.3,
                    "board_quality_delta": -0.4,
                    "board_structural_score": -0.3,
                },
            },
        },
        {
            "event_type": "action",
            "payload": {
                "action_name": "PASS",
                "combat_reward": 1.0,
                "state_before": {"board_structural_score": -0.3},
                "state_after": {
                    "board_quality_score": 0.3,
                    "board_quality_delta": 0.0,
                    "board_structural_score": -0.3,
                },
            },
        },
    ]
    report = {}
    audit_board_quality(entries, "Jogador 1", report)
    metrics = report["board_quality_metrics"]["Jogador 1"]

    assert metrics["actions_with_metrics"] == 3
    assert metrics["positive_quality_delta"] == 1
    assert metrics["negative_quality_delta"] == 1
    assert metrics["neutral_quality_delta"] == 1
    assert metrics["mean_quality_delta"] == -0.2 / 3
    assert metrics["mean_quality_delta_when_combat_reward_positive"] == 0.0
    assert metrics["mean_quality_delta_when_combat_reward_negative"] == -0.4
    assert metrics["by_action"]["MOVE_BOARD"]["actions"] == 2
    assert metrics["by_action"]["MOVE_BOARD"]["mean_quality_delta"] == -0.1


def test_board_quality_audit_ignores_entries_without_native_metrics():
    report = {}
    audit_board_quality(
        [{"event_type": "action", "payload": {"state_after": {"board": []}}}],
        "Jogador 2",
        report,
    )
    metrics = report["board_quality_metrics"]["Jogador 2"]
    assert metrics["actions_with_metrics"] == 0
    assert metrics["mean_quality_delta"] == 0.0
