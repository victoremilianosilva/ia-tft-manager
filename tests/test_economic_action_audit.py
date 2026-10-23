from audit_viewer_match import audit_economic_actions


def _entry(sequence, action, diagnostics, gold, power=10.0, stage=2):
    return {
        "event_type": "action",
        "sequence_id": sequence,
        "stage": stage,
        "payload": {
            "action_name": action,
            "action_reward": 0.0,
            "economic_diagnostics": diagnostics,
            "state_after": {"gold": gold, "board_power": power},
        },
    }


def test_economic_audit_aggregates_costs_and_reports_without_changing_rewards():
    entries = [
        _entry(1, "BUY_XP", {
            "action_cost": 4, "sale_proceeds": 0, "potential_interest_delta": -1,
            "reason_code": "XP_NO_LEVEL_UP", "measurable_improvement": False,
        }, 15),
        _entry(2, "REROLL", {
            "action_cost": 2, "sale_proceeds": 0, "potential_interest_delta": 0,
            "reason_code": "REROLL_NO_IMMEDIATE_BOARD_GAIN", "measurable_improvement": False,
        }, 13),
        _entry(3, "PASS", {
            "action_cost": 0, "sale_proceeds": 0, "potential_interest_delta": 0,
            "reason_code": "PASS_NO_SPEND", "measurable_improvement": False,
        }, 13),
    ]
    report = {}
    audit_economic_actions(entries, "Jogador 1", report)

    metrics = report["economic_action_metrics"]["Jogador 1"]
    assert metrics["actions"] == 3
    assert metrics["gold_spent"] == 6
    assert metrics["potential_interest_lost"] == 1
    assert metrics["xp_without_level_up"] == 1
    assert metrics["rerolls_without_immediate_gain"] == 1
    assert metrics["rerolls_followed_by_pass"] == 1
    assert metrics["final_gold"] == 13
    assert metrics["by_action"]["BUY_XP"]["gold_spent"] == 4
    assert "reward" not in metrics


def test_economic_audit_ignores_non_action_entries_and_missing_diagnostics():
    entries = [
        {"event_type": "round_finished", "payload": {"economic_diagnostics": {"action_cost": 99}}},
        {"event_type": "action", "payload": {"action_name": "PASS"}},
    ]
    report = {}
    audit_economic_actions(entries, "Jogador 2", report)
    assert "economic_action_metrics" not in report
