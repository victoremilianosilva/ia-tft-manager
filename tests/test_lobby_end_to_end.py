"""Smoke test da interface Python fina sobre a lobby nativa C++."""
import numpy as np
import pytest

from cpp_lobby_env import CppTFTLobbyWrapper
from reward_outcome_producers import build_action_outcome_events


def _assert_action_events_match_oracle(info, before_snapshot):
    oracle_events = build_action_outcome_events(
        before_snapshot=before_snapshot,
        after_snapshot=info["decision_snapshot"]["native_state_snapshot"],
        action_traces=info["action_trace"],
    )
    assert len(oracle_events) == len(info["action_outcome_events"]) == 8
    for native_event, oracle_event in zip(info["action_outcome_events"], oracle_events):
        assert native_event["action_type"] == oracle_event["action"]["type"]
        assert native_event["action_family"] == oracle_event["action"]["family"]
        assert native_event["handler_applied"] == oracle_event["action"]["handler_applied"]
        assert native_event["status_reason"] == oracle_event["action"]["status_reason"]
        facts = oracle_event["facts"]
        if facts["gold_delta"] is not None:
            assert native_event["gold_delta"] == facts["gold_delta"]
        if native_event["action_family"] == "purchase":
            expected_added_units = {unit["uuid"] for unit in facts["units_added"]}
            affected_units = set(native_event["affected_unit_uuids"])
            assert expected_added_units.issubset(affected_units)
            expected_auto_merge = any(delta["star"] > 1 and delta["count_delta"] > 0 for delta in facts["star_tier_count_deltas"])
            assert native_event["auto_merge"] is expected_auto_merge
            if expected_auto_merge:
                # The legacy oracle did not publish consumed UUIDs for BUY; the
                # native event must still expose every consumed copy.
                assert len(affected_units) > len(expected_added_units)
            else:
                assert affected_units == expected_added_units
        elif native_event["action_family"] == "sale":
            assert set(native_event["affected_unit_uuids"]) == {
                unit["uuid"] for unit in facts["units_removed"]
            }
            assert native_event["sale_proceeds"] == max(0, facts["gold_delta"] or 0)
        elif native_event["action_family"] in ("deploy", "positioning"):
            assert set(native_event["affected_unit_uuids"]) == {
                move["uuid"] for move in facts["board_unit_moves"]
            }
        elif native_event["action_family"] == "item_action":
            assert set(native_event["affected_unit_uuids"]) == {
                change["unit_uuid"] for change in facts["item_assignment_changes"]
            }
        elif native_event["action_family"] == "xp_purchase":
            assert native_event["xp_after"] - native_event["xp_before"] == facts["xp_delta"]
            assert native_event["level_after"] - native_event["level_before"] == facts["level_delta"]


def test_native_lobby_adapter_executes_a_step():
    lobby = CppTFTLobbyWrapper(seed=123)

    try:
        observations = lobby.reset(seed=123)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert np.isfinite(observations).all()

        # Todos os agentes passam; as regras e a resolução permanecem em C++.
        source_snapshot = lobby._engine.get_audit_snapshot()
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        next_observations, rewards, done, info = lobby.step(actions)

        assert next_observations.shape == observations.shape
        assert rewards.shape == (8,)
        assert np.isfinite(next_observations).all()
        assert np.isfinite(rewards).all()
        assert isinstance(done, bool)
        assert len(info["players"]) == 8
        assert info["round"] >= 1
        assert info["lobby_done"] is done
        assert info["action_context"]["contract_id"] == "tft.engine.action-context"
        assert info["action_context"]["contract_version"] == 1
        assert info["action_context"]["action_masks"].shape == (8, 1280)
        assert not info["action_context"]["action_masks"].flags.writeable
        assert len(info["action_outcome_events"]) == 8
        _assert_action_events_match_oracle(info, source_snapshot)
        for player_id, event in enumerate(info["action_outcome_events"]):
            assert event["contract_id"] == "tft.engine.action-outcome-event"
            assert event["player_id"] == player_id
            assert event["action_family"] == "pass"
            assert event["action_type"] == 6
            assert event["handler_applied"] is True
            assert event["status_reason"] == "applied"
            assert event["outcome_player_decision_sequence"] == info["decision_snapshot"]["player_decision_sequences"][player_id]
    finally:
        lobby.close()


def _buy_first_shop_unit(lobby):
    masks = lobby.get_packed_action_masks_for_training()
    legal_slots = np.flatnonzero(masks[0, 9:14])
    assert legal_slots.size
    actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
    actions[0] = [0, int(legal_slots[0]), 0, 0, 0, 0]
    before_snapshot = lobby._engine.get_audit_snapshot()
    _, _, _, info = lobby.step(actions)
    _assert_action_events_match_oracle(info, before_snapshot)
    return info


def test_native_action_event_covers_item_equip_handler():
    lobby = CppTFTLobbyWrapper(seed=124)
    try:
        lobby.reset(seed=124)
        _buy_first_shop_unit(lobby)
        assert lobby.grant_completed_item(0, "TFT_Item_AdaptiveHelm")
        masks = lobby._engine.get_action_masks()
        inventory_slots = np.flatnonzero(masks[0]["item_inventory_mask"])
        target_slots = np.flatnonzero(masks[0]["item_target_mask"])
        assert inventory_slots.size and target_slots.size

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [7, int(inventory_slots[0]), int(target_slots[0]), 0, 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["action_family"] == "item_action"
        assert event["item_action_kind"] == "equip_inventory_item"
        assert event["item_id"] == "TFT_Item_AdaptiveHelm"
        assert event["affected_unit_uuids"]
    finally:
        lobby.close()


def test_native_action_event_covers_item_craft_handler():
    lobby = CppTFTLobbyWrapper(seed=125)
    try:
        lobby.reset(seed=125)
        _buy_first_shop_unit(lobby)
        assert lobby.grant_item_component(0, "TFT_Item_BFSword")
        assert lobby.grant_item_component(0, "TFT_Item_ChainVest")
        masks = lobby._engine.get_action_masks()
        pair_masks = np.asarray(masks[0]["item_component_pair_masks"])
        first, second = np.where(pair_masks)
        target_slots = np.flatnonzero(masks[0]["item_target_mask"])
        assert first.size and target_slots.size

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [8, int(first[0]), int(second[0]), int(target_slots[0]), 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["action_family"] == "item_action"
        assert event["item_action_kind"] == "craft_and_equip"
        assert event["first_component_id"] == "TFT_Item_BFSword"
        assert event["second_component_id"] == "TFT_Item_ChainVest"
        assert event["item_id"]
        assert event["affected_unit_uuids"]
    finally:
        lobby.close()


def test_native_preflight_rejection_is_a_factual_event_without_state_advance():
    lobby = CppTFTLobbyWrapper(seed=126)
    try:
        lobby.reset(seed=126)
        before = lobby._engine.get_audit_snapshot()["snapshot_sequence"]
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, 99, 0, 0, 0, 0]

        with pytest.raises(ValueError, match="Native action preflight rejected") as rejected:
            lobby.step(actions)

        context = rejected.value.action_context
        assert context["contract_id"] == "tft.engine.action-context"
        assert context["rejected"] is True
        assert context["decision_advanced"] is False
        events = context["events"]
        assert len(events) == 8
        assert events[0]["mask_permitted"] is False
        assert events[0]["preflight_accepted"] is False
        assert events[0]["handler_applied"] is False
        assert events[0]["decision_advanced"] is False
        assert events[0]["execution_status"] == "rejected"
        assert events[0]["status_reason"]
        assert events[1]["mask_permitted"] is True
        assert lobby._engine.get_audit_snapshot()["snapshot_sequence"] == before
    finally:
        lobby.close()


def test_native_action_event_reports_capacity_noop_without_fabricated_effect():
    lobby = CppTFTLobbyWrapper(seed=127)
    try:
        lobby.reset(seed=127)
        champion_api_name = next(iter(lobby._engine.get_champion_id_map()))
        assert lobby._engine.set_unit_for_testing(0, True, 0, champion_api_name)
        assert lobby._engine.set_unit_for_testing(0, False, 0, champion_api_name)
        masks = lobby._engine.get_action_masks()[0]
        assert masks["type_mask"][3] == 1
        assert masks["bench_move_source_mask"][0] == 1

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        # The board has reached level capacity; moving the bench unit to an
        # empty slot is structurally valid but produces an explicit no-op.
        actions[0] = [3, 0, 0, 1, 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["mask_permitted"] is False
        assert event["preflight_accepted"] is True
        assert event["handler_applied"] is False
        assert event["status_reason"] == "board_capacity_limit"
        assert event["execution_status"] == "no_effect"
        assert event["candidate_unit_uuids"]
        assert event["affected_unit_uuids"] == []
    finally:
        lobby.close()


def test_native_action_event_tracks_both_entities_in_board_swap():
    lobby = CppTFTLobbyWrapper(seed=128)
    try:
        lobby.reset(seed=128)
        champion_names = list(lobby._engine.get_champion_id_map())
        assert len(champion_names) >= 2
        assert lobby._engine.set_unit_for_testing(0, True, 0, champion_names[0])
        assert lobby._engine.set_unit_for_testing(0, True, 1, champion_names[1])
        masks = lobby._engine.get_action_masks()[0]
        move_matrix = np.asarray(masks["board_move_target_masks"]).reshape(28, 28)
        sources, destinations = np.where(move_matrix)
        assert sources.size

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [4, 0, 0, 0, int(sources[0]), int(destinations[0])]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["action_family"] == "positioning"
        assert event["handler_applied"] is True
        assert len(event["candidate_unit_uuids"]) == 2
        assert len(event["affected_unit_uuids"]) == 2
        assert len(set(event["affected_unit_uuids"])) == 2
    finally:
        lobby.close()


def test_native_action_event_covers_anvil_choice_without_unit_target():
    lobby = CppTFTLobbyWrapper(seed=129)
    try:
        lobby.reset(seed=129)
        assert lobby._engine.grant_component_anvil_for_testing(
            0, ["TFT_Item_BFSword", "TFT_Item_ChainVest"]
        )
        masks = lobby._engine.get_action_masks()[0]
        assert masks["type_mask"][7] == 1
        options = np.flatnonzero(masks["item_inventory_mask"])
        assert options.size == 2
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [7, int(options[1]), 0, 0, 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["action_family"] == "item_action"
        assert event["item_action_kind"] == "anvil_component_choice"
        assert event["execution_status"] == "applied"
        assert event["item_id"] == "TFT_Item_ChainVest"
        assert event["handler_applied"] is True
        assert event["affected_unit_uuids"] == []
    finally:
        lobby.close()


def test_native_action_event_reports_auto_merge_and_all_consumed_unit_uuids():
    lobby = CppTFTLobbyWrapper(seed=130)
    try:
        lobby.reset(seed=130)
        champion_api_name = next(iter(lobby._engine.get_champion_id_map()))
        assert lobby._engine.set_unit_for_testing(0, False, 0, champion_api_name)
        assert lobby._engine.set_unit_for_testing(0, False, 1, champion_api_name)
        assert lobby._engine.set_shop_offer_for_testing(0, 0, champion_api_name)

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, 0, 0, 0, 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["action_family"] == "purchase"
        assert event["handler_applied"] is True
        assert event["auto_merge"] is True
        assert event["execution_status"] == "applied"
        assert len(event["affected_unit_uuids"]) == 3
        assert len(set(event["affected_unit_uuids"])) == 3
    finally:
        lobby.close()


def test_native_action_event_reports_eliminated_player_pass_only_transition():
    lobby = CppTFTLobbyWrapper(seed=131)
    try:
        lobby.reset(seed=131)
        assert lobby._engine.set_player_alive_for_testing(0, False)
        masks = lobby._engine.get_action_masks()[0]
        assert masks["type_mask"][6] == 1
        assert sum(masks["type_mask"]) == 1
        assert masks["shop_mask"][0] == 1
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        event = info["action_outcome_events"][0]
        assert event["action_family"] == "pass"
        assert event["mask_permitted"] is True
        assert event["preflight_accepted"] is True
        assert event["handler_applied"] is False
        assert event["status_reason"] == "player_eliminated"
        assert event["execution_status"] == "not_processed"
        assert event["decision_advanced"] is True
    finally:
        lobby.close()


def test_native_action_event_oracle_parity_for_deployment_and_sale():
    lobby = CppTFTLobbyWrapper(seed=133)
    try:
        lobby.reset(seed=133)
        _buy_first_shop_unit(lobby)
        masks = lobby.get_packed_action_masks_for_training()
        source_slots = np.flatnonzero(masks[0, 863:872])
        assert source_slots.size
        source = int(source_slots[0])
        targets = np.flatnonzero(masks[0, 872 + source * 28:872 + (source + 1) * 28])
        assert targets.size
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [3, 0, source, int(targets[0]), 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, deployed = lobby.step(actions)
        _assert_action_events_match_oracle(deployed, before_snapshot)
        assert deployed["action_outcome_events"][0]["action_family"] == "deploy"

        lobby.reset(seed=135)
        _buy_first_shop_unit(lobby)
        masks = lobby.get_packed_action_masks_for_training()
        bench_slots = np.flatnonzero(masks[0, 14:23])
        assert bench_slots.size
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [5, 0, int(bench_slots[0]), 0, 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, sold = lobby.step(actions)
        _assert_action_events_match_oracle(sold, before_snapshot)
        assert sold["action_outcome_events"][0]["action_family"] == "sale"
    finally:
        lobby.close()


@pytest.mark.parametrize(("action_type", "family"), [(1, "reroll"), (2, "xp_purchase")])
def test_native_action_event_oracle_parity_for_economic_actions(action_type, family):
    lobby = CppTFTLobbyWrapper(seed=134 + action_type)
    try:
        lobby.reset(seed=134 + action_type)
        masks = lobby.get_packed_action_masks_for_training()
        assert bool(masks[0, action_type])
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [action_type, 0, 0, 0, 0, 0]
        before_snapshot = lobby._engine.get_audit_snapshot()
        _, _, _, info = lobby.step(actions)
        _assert_action_events_match_oracle(info, before_snapshot)
        assert info["action_outcome_events"][0]["action_family"] == family
    finally:
        lobby.close()
