from scripts.audit_viewer_match import audit_board_quality, audit_item_state


def test_board_quality_audit_tracks_action_delta_and_combat_context():
    entries = [
        {
            "event_type": "action",
            "payload": {
                "action_name": "MOVE_BOARD",
                "combat_reward": 0.0,
                "state_before": {"board_structural_score": -0.5, "positioning_score": 0.5, "board_quality_score": 0.5},
                "state_after": {
                    "positioning_score": 0.7,
                    "board_quality_score": 0.7,
                    "board_positional_score": 0.6,
                    "board_quality_delta": 0.2,
                    "board_structural_score": -0.1,
                    "board_exposed_carries": 0,
                    "board_frontline_count": 2,
                    "board_isolated_frontline_count": 1,
                    "board_important_bench_units_unplayed": 0,
                },
            },
        },
        {
            "event_type": "action",
            "payload": {
                "action_name": "MOVE_BOARD",
                "combat_reward": -1.0,
                "state_before": {"board_structural_score": -0.1, "positioning_score": 0.7, "board_quality_score": 0.7},
                "state_after": {
                    "positioning_score": 0.3,
                    "board_quality_score": 0.3,
                    "board_positional_score": 0.4,
                    "board_quality_delta": -0.4,
                    "board_structural_score": -0.3,
                    "board_exposed_carries": 1,
                    "board_frontline_count": 1,
                    "board_isolated_frontline_count": 2,
                    "board_important_bench_units_unplayed": 1,
                },
            },
        },
        {
            "event_type": "action",
            "payload": {
                "action_name": "PASS",
                "combat_reward": 1.0,
                "state_before": {"board_structural_score": -0.3, "positioning_score": 0.3, "board_quality_score": 0.3},
                "state_after": {
                    "positioning_score": 0.3,
                    "board_quality_score": 0.3,
                    "board_positional_score": 0.4,
                    "board_quality_delta": 0.0,
                    "board_structural_score": -0.3,
                    "board_exposed_carries": 1,
                    "board_frontline_count": 1,
                    "board_isolated_frontline_count": 2,
                    "board_important_bench_units_unplayed": 1,
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
    assert abs(metrics["mean_quality_delta_when_combat_reward_negative"] + 0.4) < 1e-9
    assert metrics["by_action"]["MOVE_BOARD"]["actions"] == 2
    assert metrics["by_action"]["MOVE_BOARD"]["mean_quality_delta"] == -0.1
    assert metrics["structural_metrics_available"] is True
    assert metrics["structural_samples"] == 3
    assert abs(metrics["mean_structural_delta"] - (0.2 / 3)) < 1e-9
    assert abs(metrics["mean_structural_score"] - (-0.7 / 3)) < 1e-9
    assert abs(metrics["mean_positional_score"] - ((0.6 + 0.4 + 0.4) / 3)) < 1e-9


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


def test_item_state_audit_reads_equipment_bag_components_and_events():
    entries = [
        {
            "event_type": "action",
            "sequence_id": 1,
            "payload": {
                "action_name": "EQUIP_FROM_INVENTORY",
                "state_after": {
                    "board": [
                        {"occupied": True, "items": ["Deathblade"]},
                        {"occupied": False, "items": []},
                    ],
                    "bench": [{"occupied": True, "items": ["GargoyleStoneplate"]}],
                    "item_inventory": ["JeweledGauntlet"],
                    "item_components": ["ComponentSword"],
                },
                "events": ["ITEM_EQUIPPED"],
            },
        },
        {
            "event_type": "action",
            "sequence_id": 2,
            "payload": {
                "action_name": "PASS",
                "state_after": {
                    "board": [{"occupied": True, "items": ["Deathblade", "JeweledGauntlet"]}],
                    "bench": [],
                    "item_inventory": [],
                    "item_components": ["ComponentSword"],
                },
            },
        },
    ]
    report = {}
    audit_item_state(entries, "Jogador 1", report)
    metrics = report["item_state_metrics"]["Jogador 1"]
    assert metrics["item_evidence_available"] is True
    assert metrics["snapshots"] == 2
    assert metrics["distinct_equipped_item_ids"] == [
        "Deathblade", "GargoyleStoneplate", "JeweledGauntlet"
    ]
    assert metrics["final_snapshot"]["board_equipped_items"] == 2
    assert metrics["final_snapshot"]["bag_item_count"] == 0
    assert metrics["final_snapshot"]["component_count"] == 1
    assert metrics["item_events"]["ITEM_EQUIPPED"] == 1


def test_board_quality_uses_live_positioning_not_zero_initialized_cached_fields():
    report = {}
    entries = [{
        "event_type": "action",
        "payload": {
            "action_name": "MOVE_BOARD",
            "state_before": {"positioning_score": 0.4, "board_quality_score": 0.0},
            "state_after": {"positioning_score": 0.7, "board_quality_score": 0.0},
        },
    }]
    audit_board_quality(entries, "Jogador 1", report)
    metrics = report["board_quality_metrics"]["Jogador 1"]
    assert metrics["actions_with_metrics"] == 1
    assert metrics["positive_quality_delta"] == 1
    assert abs(metrics["mean_quality_delta"] - 0.3) < 1e-9
    assert metrics["structural_metrics_available"] is False
    assert metrics["structural_samples"] == 0
