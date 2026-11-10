from scripts.audit_item_composition_learning import audit_records


def test_audit_aggregates_all_players_items_and_composition_evidence():
    records = []
    for player_id in range(8):
        records.append({
            "player_id": player_id,
            "alive_at_decision": True,
            "selected_action": [0, 0, 0, 0, 0, 0],
            "board_after": [{"occupied": True, "star": 2, "items": [{"api_name": "TFT_Item_Deathblade"}]}],
            "bench_after": [],
            "item_inventory_after": ["TFT_Item_GargoyleStoneplate"],
            "item_components_after": ["TFT_Item_Component_Sword"],
            "strategy_after": {
                "composition_direction": "Invoker",
                "core_units": ["Carry"],
                "planned_units": ["Carry", "Tank"],
                "planned_acquisition_notes": [
                    "OPGG_META_AUDIT: status=selected; catalog_candidates=2"
                ],
            },
            "engine_events": ["COMPONENT_LOOT_GRANTED: player=0, count=1"],
        })

    report = audit_records(records)
    assert report["all_players_present"] is True
    assert report["missing_players"] == []
    assert report["item_evidence_available"] is True
    assert report["action_counts"]["BUY"] == 8
    assert report["item_event_counts"]["COMPONENT_LOOT_GRANTED"] == 8
    assert report["players"]["0"]["board_item_instances"] == 1
    assert report["players"]["0"]["bag_item_instances"] == 1
    assert report["players"]["0"]["component_instances"] == 1
    assert report["players"]["0"]["directions"] == {"Invoker": 1}
    assert report["players"]["0"]["opgg_statuses"] == {"selected": 1}
    assert report["item_evidence_players"] == list(range(8))
    assert report["item_evidence_available"] is True
    assert report["players"]["0"]["last_board_item_instances"] == 1
    assert report["players"]["0"]["last_bag_item_instances"] == 1


def test_audit_reports_missing_item_evidence_instead_of_guessing_quality():
    report = audit_records([{
        "player_id": 0,
        "selected_action": [6, 0, 0, 0, 0, 0],
        "board_after": [{"occupied": True, "star": 1}],
        "bench_after": [],
    }])
    assert report["item_evidence_available"] is False
    assert report["players_without_item_evidence"] == list(range(8))
    assert "incomplete" in report["item_evidence_note"]
    assert report["all_players_present"] is False


def test_item_evidence_must_cover_every_expected_player():
    records = []
    for player_id in range(8):
        row = {
            "player_id": player_id,
            "selected_action": [6, 0, 0, 0, 0, 0],
            "board_after": [],
            "bench_after": [],
        }
        if player_id != 7:
            row["item_inventory_after"] = []
            row["item_components_after"] = []
        records.append(row)
    report = audit_records(records)
    assert report["all_players_present"] is True
    assert report["item_evidence_available"] is False
    assert report["players_without_item_evidence"] == [7]
