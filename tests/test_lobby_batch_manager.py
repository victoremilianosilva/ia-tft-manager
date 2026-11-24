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
            np.testing.assert_array_equal(batch["dones"], single["dones"])
            assert batch["decision_sequence"] == single["decision_sequence"]
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
