"""Smoke test da interface Python fina sobre a lobby nativa C++."""
import numpy as np

from cpp_lobby_env import CppTFTLobbyWrapper
from reward_outcome_producers import build_action_outcome_events


def test_native_lobby_adapter_executes_a_step():
    lobby = CppTFTLobbyWrapper(seed=123)

    try:
        observations = lobby.reset(seed=123)
        assert observations.ndim == 2
        assert observations.shape[0] == 8
        assert np.isfinite(observations).all()

        # Todos os agentes passam; as regras e a resolução permanecem em C++.
        source_snapshot = lobby.get_snapshot_metadata()["native_state_snapshot"]
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
        oracle_events = build_action_outcome_events(
            before_snapshot=source_snapshot,
            after_snapshot=info["decision_snapshot"]["native_state_snapshot"],
            action_traces=info["action_trace"],
        )
        for player_id, (event, oracle) in enumerate(zip(info["action_outcome_events"], oracle_events)):
            assert event["contract_id"] == "tft.engine.action-outcome-event"
            assert event["player_id"] == player_id
            assert event["action_family"] == oracle["action"]["family"] == "pass"
            assert event["action_type"] == oracle["action"]["type"] == 6
            assert event["handler_applied"] == oracle["action"]["handler_applied"] is True
            assert event["status_reason"] == oracle["action"]["status_reason"]
            assert event["outcome_player_decision_sequence"] == info["decision_snapshot"]["player_decision_sequences"][player_id]
    finally:
        lobby.close()


def _buy_first_shop_unit(lobby):
    masks = lobby.get_packed_action_masks_for_training()
    legal_slots = np.flatnonzero(masks[0, 9:14])
    assert legal_slots.size
    actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
    actions[0] = [0, int(legal_slots[0]), 0, 0, 0, 0]
    lobby.step(actions)


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
        _, _, _, info = lobby.step(actions)
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
        _, _, _, info = lobby.step(actions)
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
        assert events[0]["handler_applied"] is False
        assert events[0]["decision_advanced"] is False
        assert events[0]["status_reason"]
        assert events[1]["mask_permitted"] is True
        assert lobby._engine.get_audit_snapshot()["snapshot_sequence"] == before
    finally:
        lobby.close()
