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
            assert batch["episode_id"] == single["episode_id"]
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
            assert batch["engine_instance_id"] == single["engine_instance_id"]
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
