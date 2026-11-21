from copy import deepcopy

import pytest

from reward_outcome_producers import build_action_outcome_events


def _unit(uuid="unit-a", champion="A", star=1):
    return {
        "occupied": True, "uuid": uuid, "champion_id": champion,
        "star": star, "cost": 2, "items": [], "trait_names": [],
        "role": 3, "attack_damage": 0.0, "attack_speed": 0.0,
        "max_health": 0.0, "armor": 0.0, "magic_resist": 0.0,
    }


def _empty():
    return {
        "occupied": False, "uuid": "", "champion_id": "",
        "star": 0, "cost": 0, "items": [], "trait_names": [],
        "role": 3, "attack_damage": 0.0, "attack_speed": 0.0,
        "max_health": 0.0, "armor": 0.0, "magic_resist": 0.0,
    }


def _player(player_id):
    return {
        "player_id": player_id, "gold": 30, "level": 5, "xp": 2,
        "interest_if_resolved_now": 2, "positioning_score": 0.0,
        "board_quality_score": 0.0,
        "board": [_empty() for _ in range(28)],
        "bench": [_empty() for _ in range(9)],
        "shop": [_empty() for _ in range(5)],
        "shop_offer_revisions": [0] * 5,
        "equipped_items": [], "item_inventory_counts": [], "item_component_counts": [],
    }


def _snapshot(sequence, player_sequence, round_number=4):
    return {
        "contract_id": "tft.native-state-snapshot",
        "contract_version": 5,
        "source_namespace": "tft.engine.observation-snapshot",
        "producer": "TFTEngine::get_audit_snapshot",
        "engine_instance_id": "engine-1",
        "episode_id": 7,
        "snapshot_sequence": sequence,
        "player_decision_sequences": [player_sequence] * 8,
        "round": round_number,
        "economy_resolution_events": [],
        "pvp_result_credit_events": [],
        "players": [_player(i) for i in range(8)],
    }


def _traces(action_type=6, selected=0):
    return [
        {
            "player_id": player_id,
            "effective_action": [action_type if player_id == 0 else 6, selected, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        }
        for player_id in range(8)
    ]


def test_produces_factual_purchase_and_upgrade_events_without_reward_labels():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["shop"][0] = _unit(uuid="offer-a")
    before["players"][0]["shop_offer_revisions"][0] = 3
    after["players"][0]["bench"][0] = _unit(uuid="owned-a")
    after["players"][0]["gold"] = 28
    traces = _traces(action_type=0)

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=traces
    )

    event = events[0]
    assert event["contract_id"] == "tft.reward-action-outcome.v1"
    assert event["action"]["family"] == "purchase"
    assert event["facts"]["selected_shop_offer"]["champion_id"] == "A"
    assert event["facts"]["units_added"][0]["uuid"] == "owned-a"
    assert event["facts"]["owned_copy_equivalent_delta"] == {"A": 1}
    assert event["reward"] is None
    assert event["reward_eligible"] is False


def test_records_reroll_shop_revision_changes_and_xp_progress():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["shop_offer_revisions"] = [1, 1, 1, 1, 1]
    after["players"][0]["shop_offer_revisions"] = [2, 2, 2, 2, 2]
    before["players"][1]["xp"] = 2
    after["players"][1]["xp"] = 6
    before["players"][1]["gold"] = 30
    after["players"][1]["gold"] = 24
    traces = _traces(action_type=1)
    traces[1]["effective_action"] = [2, 0, 0, 0, 0, 0]

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=traces
    )

    assert len(events[0]["facts"]["shop_revision_changes"]) == 5
    assert events[0]["action"]["family"] == "reroll"
    assert events[1]["action"]["family"] == "xp_purchase"
    assert events[1]["facts"]["xp_delta"] == 4
    assert events[1]["facts"]["gold_delta"] == -6


def test_records_sale_and_physical_board_position_changes():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["bench"][0] = _unit()
    after["players"][0]["gold"] = 33
    before["players"][1]["board"][0] = _unit(uuid="mover")
    after["players"][1]["board"][1] = _unit(uuid="mover")
    after["players"][1]["positioning_score"] = 1.5
    after["players"][1]["board_quality_score"] = 2.0
    traces = _traces(action_type=5)
    traces[1]["effective_action"] = [4, 0, 0, 0, 0, 1]

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=traces
    )

    assert events[0]["action"]["family"] == "sale"
    assert events[0]["facts"]["units_removed"][0]["uuid"] == "unit-a"
    assert events[1]["action"]["family"] == "positioning"
    assert events[1]["facts"]["board_unit_moves"] == [
        {
            "uuid": "mover", "from_location": "board", "from_slot": 0,
            "to_location": "board", "to_slot": 1,
        }
    ]
    assert events[1]["facts"]["positioning_score_delta"] == 1.5
    assert events[1]["facts"]["board_quality_delta"] == 2.0


def test_does_not_claim_action_gold_or_xp_delta_when_round_income_overlaps():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["gold"] = 49
    after["players"][0]["gold"] = 55
    after["economy_resolution_events"] = [{"player_id": 0, "producer": "EconomyEngine::resolve_round"}]

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=_traces(action_type=2)
    )

    assert events[0]["facts"]["economy_resolution_overlapped"] is True
    assert events[0]["facts"]["gold_delta"] is None
    assert events[0]["facts"]["xp_delta"] is None


def test_rejects_snapshot_or_player_sequence_misalignment():
    before = _snapshot(5, 10)
    after = _snapshot(6, 10)
    with pytest.raises(RuntimeError, match="Sequência por jogador não avançou"):
        build_action_outcome_events(
            before_snapshot=before, after_snapshot=after, action_traces=_traces()
        )

    after = _snapshot(6, 11)
    after["engine_instance_id"] = "other-engine"
    with pytest.raises(RuntimeError, match="divergem em engine_instance_id"):
        build_action_outcome_events(
            before_snapshot=before, after_snapshot=after, action_traces=_traces()
        )


def test_detects_merge_upgrade_from_physical_star_tier_counts():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["bench"][0] = _unit(uuid="copy-a", champion="A", star=1)
    before["players"][0]["bench"][1] = _unit(uuid="copy-b", champion="A", star=1)
    after["players"][0]["bench"][0] = _unit(uuid="merged-a", champion="A", star=2)
    traces = _traces(action_type=0)

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=traces
    )

    assert events[0]["facts"]["owned_copy_equivalent_delta"] == {"A": 1}
    assert events[0]["facts"]["star_tier_count_deltas"] == [
        {"champion_id": "A", "star": 1, "count_delta": -2},
        {"champion_id": "A", "star": 2, "count_delta": 1},
    ]
    assert events[0]["causal_attribution"] == "not_established"
    assert events[0]["reward_eligible"] is False


def test_does_not_attribute_automatic_round_shop_refresh_to_reroll():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["shop_offer_revisions"] = [1, 1, 1, 1, 1]
    after["players"][0]["shop_offer_revisions"] = [2, 2, 2, 2, 2]
    after["economy_resolution_events"] = [{"player_id": 0, "producer": "EconomyEngine::resolve_round"}]

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=_traces(action_type=1)
    )

    assert events[0]["facts"]["shop_revision_changes"] is None
    assert len(events[0]["facts"]["shop_revision_changes_unattributed"]) == 5
    assert events[0]["facts"]["shop_refresh_overlapped_with_round_resolution"] is True


def test_does_not_attribute_pvp_win_gold_credit_to_action_economy():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["gold"] = 30
    after["players"][0]["gold"] = 31
    after["pvp_result_credit_events"] = [{
        "winner_player_id": 0, "loser_player_id": 1,
        "credited_gold": 1, "gold_before_credit": 30, "gold_after_credit": 31,
    }]

    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=_traces(action_type=5)
    )

    assert events[0]["facts"]["gold_delta"] is None
    assert events[0]["facts"]["pvp_credit_overlapped"] is True
    assert events[0]["facts"]["pvp_result_credit_events"][0]["credited_gold"] == 1



def test_records_item_assignment_and_removal_by_stable_item_identity():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["board"][0] = _unit(uuid="carrier")
    after["players"][0]["board"][0] = _unit(uuid="carrier")
    before["players"][0]["board"][0]["item_ids"] = ["component-a", "component-b"]
    after["players"][0]["board"][0]["item_ids"] = ["completed-item"]
    traces = _traces(action_type=7)
    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=traces
    )
    changes = events[0]["facts"]["item_assignment_changes"]
    assert changes == [{
        "unit_uuid": "carrier",
        "item_ids_before": ["component-a", "component-b"],
        "item_ids_after": ["completed-item"],
        "items_added": ["completed-item"],
        "items_removed": ["component-a", "component-b"],
    }]
    assert events[0]["reward"] is None
    assert events[0]["reward_eligible"] is False


def test_item_assignment_rejects_unidentifiable_or_duplicate_items():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["board"][0] = _unit(uuid="carrier")
    after["players"][0]["board"][0] = _unit(uuid="carrier")
    before["players"][0]["board"][0]["item_ids"] = [{"name": "unknown"}]
    after["players"][0]["board"][0]["item_ids"] = []
    with pytest.raises(ValueError, match="identidade estável"):
        build_action_outcome_events(
            before_snapshot=before, after_snapshot=after, action_traces=_traces(action_type=7)
        )



def test_item_action_records_equipped_item_and_inventory_component_deltas():
    before = _snapshot(5, 10)
    after = _snapshot(6, 11)
    before["players"][0]["equipped_items"] = [{
        "unit_uuid": "carrier", "catalog_id": "item-a", "location": "bench", "slot": 0
    }]
    after["players"][0]["equipped_items"] = [{
        "unit_uuid": "carrier", "catalog_id": "item-a", "location": "board", "slot": 4
    }, {
        "unit_uuid": "carrier", "catalog_id": "item-b", "location": "board", "slot": 4
    }]
    before["players"][0]["item_inventory_counts"] = [{"catalog_id": "item-c", "count": 2}]
    after["players"][0]["item_inventory_counts"] = [{"catalog_id": "item-c", "count": 1}]
    before["players"][0]["item_component_counts"] = [{"catalog_id": "component-a", "count": 2}]
    after["players"][0]["item_component_counts"] = [{"catalog_id": "component-a", "count": 1}]
    events = build_action_outcome_events(
        before_snapshot=before, after_snapshot=after, action_traces=_traces(action_type=7)
    )
    facts = events[0]["facts"]
    assert {row["kind"] for row in facts["equipped_item_changes"]} == {"moved", "equipped"}
    assert facts["item_inventory_count_deltas"] == {"item-c": -1}
    assert facts["item_component_count_deltas"] == {"component-a": -1}
