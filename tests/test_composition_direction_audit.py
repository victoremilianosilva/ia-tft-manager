from audit_viewer_match import audit_composition_direction_changes


def test_composition_direction_audit_measures_gain_and_no_gain():
    entries = [
        {
            "event_type": "action",
            "step": 4,
            "round": "3-2",
            "sequence_id": 4,
            "payload": {
                "action_name": "MOVE_BENCH",
                "state_before": {
                    "composition_strength": 3.0,
                    "board_power": 20.0,
                    "synergy_score": 2.0,
                },
                "state_after": {
                    "composition_strength": 4.0,
                    "board_power": 20.0,
                    "synergy_score": 2.0,
                },
                "composition_diagnostics": {
                    "direction_event": {
                        "from": "Bruiser",
                        "to": "Mage",
                        "from_strength": 3.0,
                        "reason": "persistent_superior_candidate",
                        "was_locked": True,
                    },
                    "unit_fit": {},
                },
            },
        },
        {
            "event_type": "action",
            "step": 8,
            "round": "3-3",
            "sequence_id": 8,
            "payload": {
                "action_name": "PASS",
                "state_before": {
                    "composition_strength": 4.0,
                    "board_power": 20.0,
                    "synergy_score": 2.0,
                },
                "state_after": {
                    "composition_strength": 3.8,
                    "board_power": 20.0,
                    "synergy_score": 2.0,
                },
                "composition_diagnostics": {
                    "direction_event": {
                        "from": "Mage",
                        "to": "Ranger",
                        "from_strength": 4.0,
                        "reason": "current_direction_unviable",
                        "was_locked": True,
                    },
                    "unit_fit": {},
                },
            },
        },
    ]
    report = {}
    audit_composition_direction_changes(entries, "Jogador 1", report)

    metrics = report["composition_direction_metrics"]["Jogador 1"]
    assert metrics["direction_changes"] == 2
    assert metrics["changes_with_measurable_gain"] == 1
    assert metrics["changes_without_measurable_gain"] == 1
    assert metrics["rate_without_measurable_gain"] == 0.5
    assert metrics["details"][0]["strength_delta"] == 1.0
    assert metrics["details"][0]["measurable_gain"] is True
    assert metrics["details"][1]["measurable_gain"] is False


def test_composition_direction_audit_ignores_entries_without_transition_events():
    report = {}
    audit_composition_direction_changes(
        [{"event_type": "action", "payload": {"composition_diagnostics": {}}}],
        "Jogador 1",
        report,
    )
    assert "composition_direction_metrics" not in report
