from viewer.integrated_audit import (
    build_integrated_audit_index, format_integrated_audit_markdown,
    normalize_ppo_action, normalize_evaluator_action, classify_semantic_pair,
)


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
        "composition_version": 4, "engine_match_id": 42, "stale": False,
        "context_bridge": {
            "metadata": {
                "match_id": 42, "player_id": player_id, "round": round_number,
                "composition_id": "comp-a", "composition_version": 4,
                "timestamp_unix_ms": timestamp,
            },
            "recommended": {
            "economic_posture": {"value": "ACCUMULATE_RESOURCES", "quality": "valid", "origin": "recommended"},
        }},
        "action_evaluator_comparison": {
            "baseline": {"recommended_action": 1, "recommended_champion_id": 10, "stale": False},
            "contextual": {"recommended_action": 3, "recommended_champion_id": 20, "stale": False},
            "comparison": {"comparison_available": True, "diverged": True},
        },
        "diagnostics": {
            "composition_decision": {"decision": "KEEP"},
            "unit_intentions": [],
            "lineup_plan": {"status": "ready"},
            "evidence": {
                "economy": {"metadata": {"available": True, "quality_name": "valid", "quality": 2}},
                "board": {"metadata": {"available": True, "quality_name": "valid", "quality": 2}},
                "items": {"metadata": {"available": False, "quality_name": "stale", "quality": 1}},
            },
        },
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
    assert index["evaluator_comparison_count"] == 1
    assert index["evaluator_divergence_count"] == 1
    assert index["source_presence"]["strategic_planner"] is True
    assert index["source_presence"]["contextual_action_evaluator"] is True
    assert index["source_presence"]["economic_controller"] is True
    assert index["source_presence"]["economy_evidence"] is True
    assert index["source_presence"]["economy_evidence_valid"] is True
    assert index["source_presence"]["board_evidence"] is True
    assert index["source_presence"]["board_evidence_valid"] is True
    assert index["source_presence"]["item_evidence"] is True
    assert index["source_presence"]["item_evidence_valid"] is False
    assert index["source_presence"]["unit_priority"] is True
    assert index["source_presence"]["lineup"] is True
    assert index["producer_counts"]["economy_evidence_valid"] == 1
    assert index["producer_counts"]["board_evidence_valid"] == 1
    assert index["producer_counts"].get("item_evidence_valid", 0) == 0
    assert index["bridge_identity_mismatch_count"] == 0


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



def test_context_bridge_identity_mismatches_are_reported():
    record = _composition()
    record["context_bridge"]["metadata"]["match_id"] = 99
    index = build_integrated_audit_index([], [], [record], match_id="match-a")
    assert index["bridge_identity_mismatch_count"] == 1
    assert index["bridge_identity_mismatches"][0]["field"] == "match_id"



def test_stale_evaluator_recommendations_are_unavailable_not_compared():
    record = _composition()
    record["action_evaluator_comparison"]["baseline"]["stale"] = True
    record["action_evaluator_comparison"]["contextual"]["stale"] = True
    index = build_integrated_audit_index(
        [_decision()], [], [record], match_id="match-a"
    )
    assert index["recommendation_vs_ppo"]["baseline"]["compared"] == 0
    assert index["recommendation_vs_ppo"]["baseline"]["unavailable"] == 1
    assert index["recommendation_vs_ppo"]["contextual"]["compared"] == 0
    assert index["recommendation_vs_ppo"]["contextual"]["unavailable"] == 1


def test_evaluator_snapshot_outside_timestamp_window_is_unavailable():
    record = _composition(timestamp=1794398460000)
    index = build_integrated_audit_index(
        [_decision()], [], [record], match_id="match-a"
    )
    assert index["recommendation_vs_ppo"]["baseline"]["compared"] == 0
    assert index["recommendation_vs_ppo"]["baseline"]["unavailable"] == 1



def test_same_player_sequence_with_different_payload_is_preserved_and_flagged():
    first = _decision(action="BUY")
    conflicting = _decision(action="SELL")
    index = build_integrated_audit_index(
        [first, conflicting], [], [], match_id="match-a"
    )
    assert index["player_log_duplicate_count"] == 1
    assert index["player_sequence_conflict_count"] == 1
    assert index["groups"][0]["ppo_action_count"] == 2


def test_same_composition_sequence_with_different_payload_is_preserved_and_flagged():
    first = _composition(sequence=1)
    conflicting = _composition(sequence=1)
    conflicting["composition_version"] = 5
    conflicting["context_bridge"]["metadata"]["composition_version"] = 5
    index = build_integrated_audit_index(
        [], [], [first, conflicting], match_id="match-a"
    )
    assert index["composition_duplicate_count"] == 1
    assert index["composition_sequence_conflict_count"] == 1
    assert index["groups"][0]["composition_snapshot_count"] == 2



def test_unrecognized_source_schema_is_reported_as_incompatible():
    record = _composition()
    record["schema_version"] = 2
    index = build_integrated_audit_index([], [], [record], match_id="match-a")
    assert index["incompatible_schemas"] == [
        {"schema_version": 2, "sequence": 10, "player_id": 0}
    ]



def test_semantic_taxonomy_maps_direct_partial_and_unmapped_actions():
    direct_cases = {
        "BUY": "BUY_UNIT",
        "SELL": "SELL_UNIT",
        "BUY_XP": "BUY_XP",
        "REROLL": "REROLL",
    }
    for raw, expected in direct_cases.items():
        normalized = normalize_ppo_action(raw)
        assert normalized["original"] == raw
        assert normalized["semantic_category"] == expected
        assert normalized["mapping_quality"] == "direct"
        assert classify_semantic_pair(
            normalized, normalize_evaluator_action(expected)
        ) == "direct_match"

    partial_cases = {
        "MOVE_BOARD": "DEPLOY_OR_MOVE",
        "MOVE_BENCH": "DEPLOY_OR_MOVE",
        "PASS": "HOLD",
    }
    for raw, expected in partial_cases.items():
        normalized = normalize_ppo_action(raw)
        assert normalized["semantic_category"] == expected
        assert classify_semantic_pair(
            normalized, normalize_evaluator_action(expected)
        ) == "partial_compatibility"

    assert normalize_ppo_action("ITEM")["semantic_category"] is None
    assert classify_semantic_pair(
        normalize_ppo_action("ITEM"), normalize_evaluator_action("HOLD")
    ) == "not_comparable"
    assert classify_semantic_pair(
        normalize_ppo_action("BUY"), normalize_evaluator_action("SELL_UNIT")
    ) == "incompatible"


def test_integrated_report_preserves_original_and_normalized_taxonomies():
    record = _composition()
    record["action_evaluator_comparison"]["baseline"]["recommended_action"] = 6
    record["action_evaluator_comparison"]["contextual"]["recommended_action"] = 5
    index = build_integrated_audit_index(
        [_decision(action="PASS")], [], [record], match_id="match-a"
    )
    taxonomy = index["recommendation_vs_ppo"]["semantic_taxonomy"]
    assert taxonomy["baseline"]["partial_compatibility"] == 1
    assert taxonomy["contextual"]["incompatible"] == 1
    markdown = format_integrated_audit_markdown(index)
    assert "PPO original | PPO normalizado | Evaluator original | Evaluator normalizado" in markdown
    assert "| PASS | HOLD | HOLD | HOLD | partial_compatibility |" in markdown
