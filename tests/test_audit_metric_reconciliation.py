from scripts.audit_viewer_match import (
    _validate_action_from_mask,
    audit_board_quality,
    audit_composition_direction_changes,
    audit_item_state,
    audit_purchase_sequences,
    audit_team_progression,
    audit_xp_stabilization_opportunities,
    audit_session_inputs,
    discover_session_inputs,
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


def test_xp_review_windows_prioritize_stabilization_but_exclude_slowroll():
    report = {}
    entries = [
        {
            "event_type": "action", "sequence_id": 1, "step": 10,
            "stage": 4, "round_in_stage": 2,
            "payload": {
                "action_name": "PASS",
                "state_before": {"gold": 24, "level": 6, "hp": 28, "strategy_name": "STABILIZE", "board": []},
                "state_after": {},
            },
        },
        {
            "event_type": "action", "sequence_id": 2, "step": 11,
            "stage": 4, "round_in_stage": 2,
            "payload": {
                "action_name": "REROLL",
                "state_before": {"gold": 30, "level": 6, "hp": 24, "strategy_name": "SLOWROLL", "board": []},
                "state_after": {},
            },
        },
    ]
    audit_xp_stabilization_opportunities(entries, "Jogador 4", report)
    metrics = report["xp_stabilization_metrics"]["Jogador 4"]
    assert metrics["review_window_count"] == 1
    assert metrics["review_windows"][0]["action"] == "PASS"
    assert "não prova" in metrics["interpretation"]


def test_anvil_selection_is_checked_against_logged_options():
    report = {}
    entries = [{
        "event_type": "action", "sequence_id": 1, "step": 20,
        "stage": 3, "round_in_stage": 4,
        "payload": {
            "action_name": "ANVIL_CHOICE",
            "state_after": {"alive": True, "board": [], "bench": [], "item_components": []},
            "item_audit": {"decision": {
                "operation": "anvil_component_choice", "is_anvil_choice": True,
                "anvil_kind": "component", "anvil_options_before": ["TFT_Item_ChainVest", "TFT_Item_NeedlesslyLargeRod"],
                "selected_id": "TFT_Item_RecurveBow", "selected_component_id": "TFT_Item_RecurveBow",
                "item_fit": 0.2, "estimated_immediate_strength": 0.1,
            }},
        },
    }]
    audit_item_state(entries, "Jogador 2", report)
    metrics = report["item_state_metrics"]["Jogador 2"]
    assert metrics["anvil_choices"] == 1
    assert metrics["anvil_decisions"][0]["selection_in_options"] is False
    assert any(issue["code"] == "ANVIL_SELECTION_NOT_IN_OPTIONS" for issue in report["issues"])


def test_structural_and_positional_scores_are_correlated_with_round_combat():
    report = {}
    entries = []
    for index, (structural, positional, combat) in enumerate([
        (1.0, 1.0, -1.0), (2.0, 2.0, 0.0), (3.0, 3.0, 1.0), (4.0, 4.0, 2.0),
    ], start=1):
        entries.append({
            "event_type": "round_finished", "sequence_id": index, "step": index * 10,
            "stage": 3, "round_in_stage": index,
            "payload": {
                "state_before": {"board_structural_score": structural, "board_positional_score": positional},
                "combat_reward": combat,
            },
        })
    audit_board_quality(entries, "Jogador 1", report)
    metrics = report["board_quality_metrics"]["Jogador 1"]
    assert metrics["combat_round_samples"] == 4
    assert metrics["structural_combat_correlation"] == 1.0
    assert metrics["positional_combat_correlation"] == 1.0


def test_core_sale_is_not_flagged_when_near_term_board_gain_compensates():
    report = {}
    entries = [
        {
            "event_type": "action", "sequence_id": 1, "step": 1,
            "stage": 2, "round_in_stage": 1,
            "payload": {
                "action": [6], "action_name": "PASS",
                "state_before": {"board": [], "bench": [], "gold": 20},
                "state_after": {"board": [], "bench": [], "gold": 20, "comp_direction": "CompA"},
            },
        },
        {
            "event_type": "action", "sequence_id": 2, "step": 2,
            "stage": 2, "round_in_stage": 1,
            "payload": {
                "action": [5, 0, 0], "action_name": "SELL",
                "state_before": {
                    "board": [], "bench": [{"occupied": True, "champion_id": "CoreUnit", "star": 1, "cost": 3}],
                    "core_units": ["CoreUnit"], "comp_direction": "CompA", "gold": 20,
                },
                "state_after": {
                    "board": [], "bench": [], "core_units": ["CoreUnit"],
                    "comp_direction": "CompA", "gold": 23,
                },
            },
        },
        {
            "event_type": "action", "sequence_id": 3, "step": 3,
            "stage": 2, "round_in_stage": 1,
            "payload": {
                "action": [0, 0], "action_name": "BUY",
                "state_before": {"board": [], "bench": [], "shop": []},
                "state_after": {
                    "board": [{"occupied": True, "champion_id": "Replacement", "star": 2, "cost": 4}],
                    "bench": [], "comp_direction": "CompA",
                },
            },
        },
    ]
    audit_purchase_sequences(entries, "Jogador 4", report)
    metrics = report["purchase_sequence_metrics"]["Jogador 4"]
    assert metrics["sales_with_demonstrated_compensation"] == 1
    assert metrics["sales_requiring_review"] == 0
    assert metrics["sale_review_records"][0]["compensation"]["future"]
    assert not any(issue["code"] == "SOLD_CORE_UNIT" for issue in report["issues"])



def test_session_discovery_uses_metadata_and_untracked_json_sidecars(tmp_path):
    (tmp_path / "metadata.json").write_text(
        '{"player_log_files":["player_1_log.tft"],'
        '"structured_player_log_files":["player_1_log.json"]}',
        encoding="utf-8",
    )
    (tmp_path / "player_1_log.tft").write_text(
        "[12:00:00] PASSOU TURNO | Rew: +0.00\n", encoding="utf-8"
    )
    # Deliberately create a local sidecar; it need not be tracked by Git.
    (tmp_path / "player_1_log.json").write_text(
        '{"player_number":1,"entries":[]}', encoding="utf-8"
    )

    tft_files, json_files, root = discover_session_inputs(tmp_path)

    assert root == tmp_path
    assert [path.name for path in tft_files] == ["player_1_log.tft"]
    assert [path.name for path in json_files] == ["player_1_log.json"]


def test_combined_audit_keeps_structured_and_text_evidence_together(tmp_path):
    text_log = tmp_path / "player_1_log.tft"
    sidecar = tmp_path / "player_1_log.json"
    text_log.write_text(
        "[12:00:00] PASSOU TURNO | Rew: +0.00\n"
        "    STRATEGY: STABILIZE | COMP DIRECTION: — | FOCUS: CarryA\n"
        "    STRATEGY REASON: weak board | CONF: 0.90\n",
        encoding="utf-8",
    )
    sidecar.write_text(
        '{"player_number":1,"entries":[{'
        '"event_type":"action","sequence_id":1,"step":1,"stage":1,"round_in_stage":1,'
        '"payload":{"action_name":"PASS","action":[6],'
        '"state_before":{"gold":12,"level":3,"hp":80,"board":[],"bench":[]},'
        '"state_after":{"gold":12,"level":3,"hp":80,"board":[],"bench":[],"alive":true}}'
        '}]}',
        encoding="utf-8",
    )
    report = {
        "source": str(tmp_path), "log_files": [], "players_seen": set(),
        "entries_read": 0, "diagnostics_missing": 0, "issues": [], "notes": [],
        "decision_timeline": [],
    }

    audit_session_inputs([text_log], [sidecar], report, 8, 8)

    assert report["entries_read"] == 1
    assert "1" in report["players_seen"]
    assert "Jogador 1" in report.get("decision_audit_metrics", {})
    assert "Jogador 1" in report.get("text_log_metrics", {})
    assert report["text_log_metrics"]["Jogador 1"]["actions"] == 1
    assert report["text_log_metrics"]["Jogador 1"]["strategies_seen"]["STABILIZE"] >= 1
    assert len(report["text_decision_timeline"]) == 1
    assert len(report["decision_timeline"]) == 1


def test_single_tft_input_discovers_its_json_sidecar(tmp_path):
    text_log = tmp_path / "player_2_log.tft"
    sidecar = tmp_path / "player_2_log.json"
    text_log.write_text("legacy text", encoding="utf-8")
    sidecar.write_text('{"player_number":2,"entries":[]}', encoding="utf-8")

    tft_files, json_files, _ = discover_session_inputs(text_log)

    assert text_log in tft_files
    assert sidecar in json_files
