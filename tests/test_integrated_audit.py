from viewer.integrated_audit import build_integrated_audit_index, format_integrated_audit_markdown


def _decision(action="BUY", player="Jogador 1", round_number=3, timestamp="2026-11-11T12:00:00+00:00"):
    return {
        "player": player, "round": round_number, "step": 20, "sequence_id": 7,
        "timestamp": timestamp, "action_name": action,
        "state_after": {"shadow_planning": {
            "strategic_decision_name": "KEEP",
            "decision_path_reason": "current_direction_still_viable",
        }},
        "economic_diagnostics": {"gold": 30, "interest": 3},
        "decision_context": {"gold": 30},
    }


def _composition(match_id="match-a", player_id=0, round_number=3, sequence=10, timestamp=1794398400000):
    return {
        "schema_version": 1, "match_id": match_id, "player_id": player_id,
        "round": round_number, "sequence": sequence,
        "timestamp_unix_ms": timestamp, "composition_id": "comp-a",
        "composition_version": 4, "stale": False,
        "context_bridge": {"recommended": {
            "economic_posture": {"value": "ACCUMULATE_RESOURCES", "quality": "valid", "origin": "recommended"},
        }},
        "action_evaluator_comparison": {
            "baseline": {"recommended_action": 1, "recommended_champion_id": 10, "stale": False},
            "contextual": {"recommended_action": 3, "recommended_champion_id": 20, "stale": False},
            "comparison": {"diverged": True},
        },
        "diagnostics": {"composition_decision": {"decision": "KEEP"}},
    }


def test_integrated_index_correlates_same_match_player_round_and_compares_categories():
    index = build_integrated_audit_index(
        [_decision()], [], [_composition()], match_id="match-a"
    )

    assert index["group_count"] == 1
    group = index["groups"][0]
    assert group["correlation_key"] == {
        "match_id": "match-a", "player_id": 0, "round": 3,
    }
    assert group["strategic_review_count"] == 1
    assert group["ppo_action_count"] == 1
    assert group["composition_snapshot_count"] == 1
    comparison = index["recommendation_vs_ppo"]
    assert comparison["baseline"]["matches"] == 1
    assert comparison["contextual"]["divergences"] == 1
    assert index["source_presence"]["strategic_planner"] is True
    assert index["source_presence"]["contextual_action_evaluator"] is True
    assert index["source_presence"]["economic_controller"] is True


def test_integrated_index_never_joins_another_match_or_player():
    records = [
        _composition(match_id="other-match"),
        _composition(match_id="match-a", player_id=1, sequence=11),
    ]
    index = build_integrated_audit_index(
        [_decision()], [], records, match_id="match-a"
    )

    assert index["group_count"] == 2
    by_player = {group["player_id"]: group for group in index["groups"]}
    assert by_player[0]["composition_snapshot_count"] == 0
    assert by_player[1]["composition_snapshot_count"] == 1
    assert by_player[0]["ppo_action_count"] == 1
    assert by_player[1]["ppo_action_count"] == 0


def test_integrated_index_preserves_unavailable_legacy_envelopes_without_synthetic_records():
    legacy = {
        "schema_version": 1, "sequence": 2, "round": 3,
        "composition_id": "legacy-comp", "composition_version": 1,
        "diagnostics": {"composition_decision": {"decision": "KEEP"}},
    }
    index = build_integrated_audit_index(
        [_decision()], [], [legacy], match_id="match-a"
    )

    assert index["composition_envelope_missing_count"] == 1
    assert index["source_presence"]["composition_intelligence"] is False
    assert index["recommendation_vs_ppo"]["baseline"]["unavailable"] == 1
    assert index["groups"][0]["composition_snapshot_count"] == 0


def test_integrated_index_detects_duplicate_and_out_of_order_per_player_sequences():
    records = [
        _composition(sequence=4),
        _composition(sequence=4),
        _composition(sequence=3),
    ]
    index = build_integrated_audit_index([], [], records, match_id="match-a")

    assert index["composition_duplicate_count"] == 1
    assert index["duplicate_sequences"] == [{"player_id": 0, "sequence": 4}]
    assert index["out_of_order_sequences"] == [
        {"match_id": "match-a", "player_id": 0, "previous": 4, "current": 3}
    ]


def test_outcomes_are_linked_as_correlation_not_causality():
    outcome = {
        "player": "Jogador 1", "round": 3, "step": 30,
        "placement": 2, "combat_reward": 0.4,
    }
    index = build_integrated_audit_index(
        [_decision()], [outcome], [_composition()], match_id="match-a"
    )

    group = index["groups"][0]
    assert group["outcomes"][0]["placement"] == 2
    assert group["outcomes"][0]["interpretation"] == "correlation_only_not_causation"
    assert "não demonstra causalidade" in format_integrated_audit_markdown(index)


def test_player_id_normalization_handles_zero_based_and_viewer_labels():
    records = [_composition(player_id=0)]
    index = build_integrated_audit_index(
        [_decision(player="Jogador 1")], [], records, match_id="match-a"
    )
    assert index["groups"][0]["player_id"] == 0



def test_stage_round_labels_are_normalized_to_native_global_rounds():
    index = build_integrated_audit_index(
        [_decision(round_number="2-1")],
        [],
        [_composition(round_number=5)],
        match_id="match-a",
    )
    assert index["group_count"] == 1
    assert index["groups"][0]["round"] == 5
    assert index["groups"][0]["composition_snapshot_count"] == 1


def test_repeated_strategic_observations_are_deduplicated_without_dropping_actions():
    first = _decision()
    second = _decision()
    second["sequence_id"] = 8
    second["step"] = 21
    index = build_integrated_audit_index(
        [first, second], [], [], match_id="match-a"
    )
    group = index["groups"][0]
    assert group["ppo_action_count"] == 2
    assert group["strategic_review_observations"] == 2
    assert group["strategic_review_count"] == 1
    assert group["strategic_reviews"][0]["observations"] == 2


def test_player_log_duplicate_sequence_does_not_inflate_action_count():
    event = _decision()
    index = build_integrated_audit_index(
        [event, dict(event)], [], [], match_id="match-a"
    )
    assert index["player_log_duplicate_count"] == 1
    assert index["groups"][0]["ppo_action_count"] == 1


def test_sequence_gaps_are_reported_per_match():
    index = build_integrated_audit_index(
        [], [], [_composition(sequence=1), _composition(sequence=3)],
        match_id="match-a",
    )
    assert index["sequence_gaps"] == [
        {"match_id": "match-a", "count": 1, "missing": [2]}
    ]


def test_known_composition_version_mismatch_is_not_correlated_to_other_version():
    event = _decision()
    event["state_after"]["composition_id"] = "comp-a"
    event["state_after"]["composition_version"] = 99
    index = build_integrated_audit_index(
        [event], [], [_composition()], match_id="match-a"
    )
    assert index["recommendation_vs_ppo"]["baseline"]["unavailable"] == 1
    assert index["recommendation_vs_ppo"]["baseline"]["compared"] == 0
