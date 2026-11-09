from viewer.player_logs import PlayerJsonLogWriter


def test_player_snapshot_captures_shadow_planning_recommendations():
    writer = PlayerJsonLogWriter.__new__(PlayerJsonLogWriter)
    snapshot = writer._player_snapshot(
        {
            "strategy_info": {
                "strategic_composition_decision_name": "ADAPT",
                "strategic_target_direction": "Arcanist",
                "strategic_reason": "reuse owned units",
                "strategic_confidence": 0.75,
                "strategic_preserve_unit_ids": [10, 11],
                "strategic_replaceable_unit_ids": [12],
                "strategic_candidate_diagnostics": [
                    {"champion_id": 90, "target_direction": "Arcanist",
                     "score": 3.2, "accepted": True,
                     "evaluation_reason": "selected_best_candidate"}
                ],
                "economic_posture_name": "STABILIZE_BOARD",
                "economic_posture_reason": "weak board",
                "economic_posture_confidence": 0.8,
                "strategic_action_recommendation_name": "BUY_UNIT",
                "strategic_action_reason": "upgrade opportunity",
                "strategic_action_expected_board_delta": 2.0,
                "strategic_action_expected_direct_gold_cost": 3.0,
                "strategic_action_expected_lost_interest_cost": 1.0,
                "strategic_action_expected_opportunity_cost": 0.35,
                "strategic_action_recommended_champion_id": 90,
                "strategic_action_candidate_scores": [
                    {"action": "BUY_UNIT", "champion_id": 90,
                     "total_score": 0.8, "selected": True}
                ],
                "strategic_action_confidence": 0.7,
            }
        },
        {"player_id": 0},
    )
    shadow = snapshot["shadow_planning"]
    assert shadow["strategic_decision_name"] == "ADAPT"
    assert shadow["strategic_target_direction"] == "Arcanist"
    assert shadow["strategic_preserve_unit_ids"] == [10, 11]
    assert shadow["strategic_replaceable_unit_ids"] == [12]
    assert shadow["strategic_candidate_diagnostics"][0]["champion_id"] == 90
    assert shadow["economic_posture_name"] == "STABILIZE_BOARD"
    assert shadow["action_recommendation_name"] == "BUY_UNIT"
    assert shadow["action_expected_board_delta"] == 2.0
    assert shadow["action_expected_direct_gold_cost"] == 3.0
    assert shadow["action_expected_lost_interest_cost"] == 1.0
    assert shadow["action_expected_opportunity_cost"] == 0.35
    assert shadow["action_recommended_champion_id"] == 90
    assert shadow["action_candidate_scores"][0]["selected"] is True


def test_player_snapshot_keeps_missing_shadow_fields_missing():
    writer = PlayerJsonLogWriter.__new__(PlayerJsonLogWriter)
    snapshot = writer._player_snapshot({}, {"player_id": 0})
    assert all(value is None for value in snapshot["shadow_planning"].values())
