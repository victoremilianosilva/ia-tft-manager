import numpy as np
import pytest

native = pytest.importorskip("tft_engine")


def _pass_actions(count):
    return [[[6, 0, 0, 0, 0, 0] for _ in range(8)] for _ in range(count)]


def test_lobby_batch_manager_owns_independent_stable_engines():
    manager = native.LobbyBatchManager(3, 8100)
    try:
        ids = manager.engine_instance_ids
        assert manager.lobby_count == 3
        assert len(set(ids)) == 3
        resets = manager.reset(seed=900)
        assert [row["engine_instance_id"] for row in resets] == ids
        results = manager.step(_pass_actions(3))
        assert [row["engine_instance_id"] for row in results] == ids
        assert all(np.asarray(row["rewards"]).shape == (8,) for row in results)
        assert all(np.asarray(row["observations"]).shape[0] == 8 for row in results)
    finally:
        manager.close()


def test_lobby_batch_manager_matches_direct_engine_for_same_seed_and_actions():
    manager = native.LobbyBatchManager(2, 700)
    direct = [native.TFTLobby(700 + i) for i in range(2)]
    try:
        batch_reset = manager.reset(seed=1234)
        direct_reset = [engine.reset(seed=1234 + i) for i, engine in enumerate(direct)]
        for batch, single in zip(batch_reset, direct_reset):
            np.testing.assert_array_equal(batch["observations"], single["observations"])
            np.testing.assert_array_equal(batch["action_masks"], single["action_masks"])
            assert batch["episode_id"] == single["episode_id"]
            assert batch["decision_sequence"] == single["decision_sequence"]
            assert batch["player_decision_sequences"] == single["player_decision_sequences"]
        actions = _pass_actions(2)
        batch_steps = manager.step(actions)
        direct_steps = [engine.step(actions[i]) for i, engine in enumerate(direct)]
        for batch, single in zip(batch_steps, direct_steps):
            np.testing.assert_array_equal(batch["observations"], single["observations"])
            np.testing.assert_array_equal(batch["rewards"], single["rewards"])
            np.testing.assert_array_equal(batch["action_rewards"], single["action_rewards"])
            np.testing.assert_array_equal(batch["combat_rewards"], single["combat_rewards"])
            np.testing.assert_array_equal(batch["placement_rewards"], single["placement_rewards"])
            np.testing.assert_array_equal(batch["dones"], single["dones"])
            np.testing.assert_array_equal(batch["action_masks"], single["action_masks"])
            assert batch["action_traces"] == single["action_traces"]
            assert batch["engine_instance_id"]
            assert batch["episode_id"] == single["episode_id"]
            assert batch["decision_sequence"] == single["decision_sequence"]
            assert batch["player_decision_sequences"] == single["player_decision_sequences"]
    finally:
        manager.close()
        for engine in direct:
            engine.close()


def test_lobby_batch_manager_rejects_invalid_lifecycle_and_batch_shapes():
    manager = native.LobbyBatchManager(2, 100)
    with pytest.raises(RuntimeError, match="reset"):
        manager.step(_pass_actions(2))
    with pytest.raises(ValueError, match="seed|lobby"):
        manager.reset(seed=2**64 - 1)
    manager.reset(seed=100)
    with pytest.raises(ValueError, match="lobby"):
        manager.step(_pass_actions(1))
    with pytest.raises(ValueError, match="8 jogadores"):
        manager.step([[[6, 0, 0, 0, 0, 0] for _ in range(7)] for _ in range(2)])
    manager.close()
    manager.close()
    with pytest.raises(RuntimeError, match="encerrado"):
        manager.reset()



def test_lobby_batch_manager_requires_full_reset_after_partial_step_failure():
    manager = native.LobbyBatchManager(2, 500)
    try:
        manager.reset(seed=1200)
        malformed = _pass_actions(2)
        malformed[1] = [[6, 0, 0, 0, 0, 0] for _ in range(7)]
        with pytest.raises(ValueError, match="8 jogadores"):
            manager.step(malformed)
        with pytest.raises(RuntimeError, match="reset"):
            manager.step(_pass_actions(2))

        recovered = manager.reset(seed=1300)
        assert len(recovered) == 2
        assert len(manager.step(_pass_actions(2))) == 2
    finally:
        manager.close()

def test_lobby_batch_manager_keeps_lobby_rng_and_state_independent():
    batch = native.LobbyBatchManager(2, 4400)
    reference = native.LobbyBatchManager(1, 4400)
    try:
        batch_reset = batch.reset(seed=9910)
        reference_reset = reference.reset(seed=9910)
        np.testing.assert_array_equal(batch_reset[0]["observations"], reference_reset[0]["observations"])

        # Advance the second lobby with a different action stream. Its RNG and
        # state must not perturb the first lobby's deterministic trajectory.
        batch.step(_pass_actions(2))
        reference.step(_pass_actions(1))
        batch_next = batch.step(_pass_actions(2))[0]
        reference_next = reference.step(_pass_actions(1))[0]

        np.testing.assert_array_equal(batch_next["observations"], reference_next["observations"])
        np.testing.assert_array_equal(batch_next["rewards"], reference_next["rewards"])
        np.testing.assert_array_equal(batch_next["dones"], reference_next["dones"])
        assert batch_next["decision_sequence"] == reference_next["decision_sequence"]
        assert batch_next["player_decision_sequences"] == reference_next["player_decision_sequences"]
    finally:
        batch.close()
        reference.close()



def test_lobby_batch_manager_publishes_one_versioned_contiguous_batch():
    manager = native.LobbyBatchManager(2, 7300)
    try:
        reset_batch = manager.reset(seed=8100)
        assert isinstance(reset_batch, native.NativeDecisionBatch)
        assert reset_batch.contract_id == "tft.native-decision-batch"
        assert reset_batch.contract_version == 1
        assert reset_batch.kind == "reset"
        assert reset_batch.lobby_count == 2
        assert reset_batch.players_per_lobby == 8
        assert reset_batch.observations.shape[0:2] == (2, 8)
        assert reset_batch.action_masks.shape == (2, 8, 1280)
        assert reset_batch.observations.flags.c_contiguous
        assert reset_batch.action_masks.flags.c_contiguous
        native_context = reset_batch.native_context(0)
        first_engine_instance_id = native_context.engine_instance_id
        first_episode_id = native_context.episode_id
        assert isinstance(native_context, native.NativeDecisionContext)
        assert native_context.availability == native.ContextAvailability.COMPLETE
        assert native_context.player_count == 8
        assert native_context.engine_instance_id == reset_batch.lobby_result(0)["engine_instance_id"]
        assert native_context.shared_pool["contract_id"] == "tft.shared-champion-pool-snapshot"
        assert len(native_context.shared_pool["catalog_fingerprint"]) == 64
        context_player = native_context.player(0)
        assert context_player["player_id"] == 0
        retained_components = context_player["item_component_features"]
        assert retained_components.shape == (10,)
        assert not retained_components.flags.writeable
        assert len(context_player["board"]) == 28
        assert len(context_player["bench"]) == 9
        assert len(context_player["shop"]) == 5
        assert all(not slot["occupied"] for slot in context_player["board"])
        assert isinstance(native_context.trait_counts(0), list)
        assert native_context.provenance(0)["player_decision_sequence"] == reset_batch.lobby_result(0)["player_decision_sequences"][0]
        spatial = reset_batch.native_spatial_context(0, 0)
        assert isinstance(spatial, native.NativeSpatialContext)
        assert spatial.contract_id == "tft.native-spatial-context"
        assert spatial.contract_version == 1
        assert spatial.geometry_id == "tft.board-grid.rectangular-4x7"
        assert spatial.geometry_version == 1
        assert spatial.engine_instance_id == native_context.engine_instance_id
        assert spatial.episode_id == native_context.episode_id
        assert spatial.snapshot_sequence == native_context.snapshot_sequence
        assert spatial.player_decision_sequence == native_context.provenance(0)["player_decision_sequence"]
        assert len(spatial.unit_traits) == 28
        assert spatial.rows == 4 and spatial.columns == 7
        assert spatial.availability == native.ContextAvailability.COMPLETE
        assert spatial.row_buffer().shape == (28,)
        assert spatial.column_buffer().shape == (28,)
        assert spatial.occupancy_buffer().shape == (28,)
        assert spatial.catalog_id_buffer().shape == (28,)
        assert spatial.role_buffer().shape == (28,)
        assert spatial.stats_buffer().shape == (28, 5)
        assert spatial.relations.shape[1] == 3
        assert not spatial.row_buffer().flags.writeable
        assert not spatial.stats_buffer().flags.writeable
        assert len(spatial.unit_uuids) == 28
        assert spatial.board_metrics["quality"] == native_context.player(0)["board_quality_score"]
        for player_id in range(8):
            player_context = native_context.player(player_id)
            assert player_context["player_id"] == player_id
            assert len(player_context["board"]) == 28
            assert len(player_context["bench"]) == 9
            assert len(player_context["shop"]) == 5
            assert native_context.provenance(player_id)["player_decision_sequence"] == reset_batch.lobby_result(0)["player_decision_sequences"][player_id]
        assert native_context.pending_anvil_availability(0) == native.ContextAvailability.NOT_APPLICABLE
        del native_context
        assert retained_components.shape == (10,)
        second_context = reset_batch.native_context(1)
        assert second_context.engine_instance_id != first_engine_instance_id
        assert second_context.episode_id == first_episode_id
        assert not reset_batch.observations.flags.writeable
        assert not reset_batch.action_masks.flags.writeable

        first = reset_batch.lobby_result(0)
        assert np.shares_memory(first["observations"], reset_batch.observations)
        assert np.shares_memory(first["action_masks"], reset_batch.action_masks)
        assert not first["observations"].flags.writeable
        assert not first["action_masks"].flags.writeable

        # A lobby view owns the aggregate batch, so it remains valid after the
        # temporary batch variable is released.
        retained_observations = first["observations"]
        del reset_batch
        np.testing.assert_array_equal(retained_observations, first["observations"])

        step_batch = manager.step(_pass_actions(2))
        assert isinstance(step_batch, native.NativeDecisionBatch)
        assert step_batch.kind == "step"
        assert step_batch.rewards.shape == (2, 8)
        assert step_batch.action_rewards.shape == (2, 8)
        assert step_batch.combat_rewards.shape == (2, 8)
        assert step_batch.placement_rewards.shape == (2, 8)
        assert step_batch.dones.shape == (2, 8)
        assert step_batch.lobby_done.shape == (2,)
        row = step_batch.lobby_result(1)
        step_context = step_batch.native_context(1)
        assert step_context.engine_instance_id == row["engine_instance_id"]
        assert step_context.snapshot_sequence == row["decision_sequence"]
        assert step_context.player_count == 8
        assert np.shares_memory(row["rewards"], step_batch.rewards)
        assert np.shares_memory(row["dones"], step_batch.dones)
    finally:
        manager.close()



@pytest.mark.parametrize("lobby_count", [1, 2, 4])
def test_native_decision_batch_shapes_scale_with_lobby_count(lobby_count):
    manager = native.LobbyBatchManager(lobby_count, 12000)
    try:
        batch = manager.reset(seed=13000)
        assert batch.observations.shape[:2] == (lobby_count, 8)
        assert batch.action_masks.shape == (lobby_count, 8, 1280)
        stepped = manager.step(_pass_actions(lobby_count))
        assert stepped.observations.shape[:2] == (lobby_count, 8)
        assert stepped.rewards.shape == (lobby_count, 8)
        assert stepped.dones.shape == (lobby_count, 8)
        assert [stepped.lobby_result(i)["engine_instance_id"] for i in range(lobby_count)] == manager.engine_instance_ids
    finally:
        manager.close()


def test_native_decision_batch_publishes_versioned_action_context_and_events():
    manager = native.LobbyBatchManager(2, 9100)
    try:
        manager.reset(seed=9200)
        batch = manager.step(_pass_actions(2))
        assert batch.action_context_contract_id == "tft.engine.action-context"
        assert batch.action_context_contract_version == 1
        assert batch.action_mask_contract_id == "tft.action-masks.packed"
        assert batch.action_mask_contract_version == 1
        assert batch.action_mask_layout.startswith("type,shop,bench_source")
        assert batch.action_masks.shape == (2, 8, 1280)
        assert batch.action_masks.flags.c_contiguous
        assert not batch.action_masks.flags.writeable

        action_context = batch.action_context(0)
        assert action_context["contract_id"] == "tft.engine.action-context"
        assert action_context["contract_version"] == 1
        assert np.shares_memory(action_context["action_masks"], batch.action_masks)
        assert not action_context["action_masks"].flags.writeable
        assert len(action_context["action_outcome_events"]) == 8

        for lobby_index in range(2):
            row = batch.lobby_result(lobby_index)
            assert row["action_context"]["contract_id"] == "tft.engine.action-context"
            assert row["action_context_contract_id"] == "tft.engine.action-context"
            assert row["action_context_contract_version"] == 1
            assert row["action_mask_contract_id"] == "tft.action-masks.packed"
            assert row["action_mask_contract_version"] == 1
            events = row["action_outcome_events"]
            assert len(events) == 8
            for player_id, event in enumerate(events):
                assert event["contract_id"] == "tft.engine.action-outcome-event"
                assert event["contract_version"] == 1
                assert event["engine_instance_id"] == row["engine_instance_id"]
                assert event["episode_id"] == row["episode_id"]
                assert event["player_id"] == player_id
                assert event["action_family"] == "pass"
                assert event["effective_action"] == [6, 0, 0, 0, 0, 0]
                assert event["mask_permitted"] is True
                assert event["normalized_action"] == event["requested_action"]
                assert event["handler_applied"] is True
                assert event["status_reason"] == "applied"
                assert event["auto_merge"] is False
                assert event["outcome_player_decision_sequence"] == row["player_decision_sequences"][player_id]
                assert event["source_player_decision_sequence"] + 1 == event["outcome_player_decision_sequence"]
    finally:
        manager.close()


def test_native_action_event_records_purchase_candidate_and_affected_uuid():
    manager = native.LobbyBatchManager(1, 9300)
    try:
        reset = manager.reset(seed=9400)
        masks = reset.lobby_result(0)["action_masks"]
        assert masks.shape == (8, 1280)
        assert bool(masks[0, 0])
        legal_shop_slots = np.flatnonzero(masks[0, 9:14])
        assert legal_shop_slots.size > 0

        actions = _pass_actions(1)
        actions[0][0] = [0, int(legal_shop_slots[0]), 0, 0, 0, 0]
        step = manager.step(actions)
        event = step.lobby_result(0)["action_outcome_events"][0]

        assert event["action_family"] == "purchase"
        assert event["action_type"] == 0
        assert event["mask_permitted"] is True
        assert event["normalized_action"] == event["requested_action"]
        assert event["handler_applied"] is True
        assert event["catalog_champion_id"] >= 0
        assert event["affected_unit_uuids"]
        assert len(event["affected_unit_uuids"]) == len(set(event["affected_unit_uuids"]))
    finally:
        manager.close()

@pytest.mark.parametrize(
    ("action_type", "family"),
    [(1, "reroll"), (2, "xp_purchase")],
)
def test_native_action_events_cover_economic_action_families(action_type, family):
    manager = native.LobbyBatchManager(1, 9500 + action_type)
    try:
        reset = manager.reset(seed=9600 + action_type)
        masks = reset.lobby_result(0)["action_masks"]
        assert bool(masks[0, action_type]), f"action type {action_type} should be legal in the initial economy"

        actions = _pass_actions(1)
        actions[0][0] = [action_type, 0, 0, 0, 0, 0]
        step = manager.step(actions)
        event = step.lobby_result(0)["action_outcome_events"][0]

        assert event["action_family"] == family
        assert event["mask_permitted"] is True
        assert event["handler_applied"] is True
        assert event["gold_delta"] < 0
        assert event["action_cost"] > 0
    finally:
        manager.close()


def _buy_one_unit(manager):
    reset = manager.reset(seed=9700)
    masks = reset.lobby_result(0)["action_masks"]
    shop_slots = np.flatnonzero(masks[0, 9:14])
    assert bool(masks[0, 0]) and shop_slots.size
    actions = _pass_actions(1)
    actions[0][0] = [0, int(shop_slots[0]), 0, 0, 0, 0]
    return manager.step(actions)


def test_native_action_event_covers_bench_to_board_deployment():
    manager = native.LobbyBatchManager(1, 9800)
    try:
        bought = _buy_one_unit(manager)
        masks = bought.lobby_result(0)["action_masks"]
        assert bool(masks[0, 3])
        source_slots = np.flatnonzero(masks[0, 863:872])
        assert source_slots.size
        source = int(source_slots[0])
        targets = np.flatnonzero(masks[0, 872 + source * 28:872 + (source + 1) * 28])
        assert targets.size
        actions = _pass_actions(1)
        actions[0][0] = [3, 0, source, int(targets[0]), 0, 0]
        step = manager.step(actions)
        event = step.lobby_result(0)["action_outcome_events"][0]
        assert event["action_family"] == "deploy"
        assert event["handler_applied"] is True
        assert event["candidate_unit_uuids"]
        assert event["affected_unit_uuids"]
    finally:
        manager.close()


def test_native_action_event_covers_board_positioning():
    manager = native.LobbyBatchManager(1, 9900)
    try:
        bought = _buy_one_unit(manager)
        masks = bought.lobby_result(0)["action_masks"]
        source_slots = np.flatnonzero(masks[0, 863:872])
        source = int(source_slots[0])
        targets = np.flatnonzero(masks[0, 872 + source * 28:872 + (source + 1) * 28])
        actions = _pass_actions(1)
        actions[0][0] = [3, 0, source, int(targets[0]), 0, 0]
        deployed = manager.step(actions)
        masks = deployed.lobby_result(0)["action_masks"]
        assert bool(masks[0, 4])
        board_moves = masks[0, 79:863].reshape(28, 28)
        sources, destinations = np.where(board_moves)
        assert sources.size
        actions = _pass_actions(1)
        actions[0][0] = [4, 0, 0, 0, int(sources[0]), int(destinations[0])]
        step = manager.step(actions)
        event = step.lobby_result(0)["action_outcome_events"][0]
        assert event["action_family"] == "positioning"
        assert event["handler_applied"] is True
        assert event["candidate_unit_uuids"]
        assert event["affected_unit_uuids"]
    finally:
        manager.close()


def test_native_action_event_covers_bench_sale():
    manager = native.LobbyBatchManager(1, 10000)
    try:
        bought = _buy_one_unit(manager)
        masks = bought.lobby_result(0)["action_masks"]
        assert bool(masks[0, 5])
        bench_slots = np.flatnonzero(masks[0, 14:23])
        assert bench_slots.size
        actions = _pass_actions(1)
        actions[0][0] = [5, 0, int(bench_slots[0]), 0, 0, 0]
        step = manager.step(actions)
        event = step.lobby_result(0)["action_outcome_events"][0]
        assert event["action_family"] == "sale"
        assert event["handler_applied"] is True
        assert event["candidate_unit_uuids"]
        assert event["affected_unit_uuids"]
        assert event["sale_proceeds"] > 0
    finally:
        manager.close()
