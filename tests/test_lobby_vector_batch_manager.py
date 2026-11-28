from pathlib import Path

import numpy as np
import pytest

from cpp_lobby_env import CppTFTLobbyWrapper, _NativeLobbyBatchManager
from vector_lobby_env import LobbyVectorEnv


def _actions(lobbies):
    return [[[6, 0, 0, 0, 0, 0] for _ in range(8)] for _ in range(lobbies)]


def _without_instance_identifiers(value):
    if isinstance(value, dict):
        return {
            key: _without_instance_identifiers(item)
            for key, item in value.items()
            if key not in {"engine_instance_id", "event_id", "candidate_unit_uuids", "affected_unit_uuids"}
        }
    if isinstance(value, list):
        return [_without_instance_identifiers(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_without_instance_identifiers(item) for item in value)
    return value


def _make_batch_vector(count, seed, item_catalog):
    manager = _NativeLobbyBatchManager(count, seed, "", str(item_catalog))
    envs = [
        lambda index=index: CppTFTLobbyWrapper(
            seed=seed + index,
            item_catalog_path=str(item_catalog),
            native_engine=manager.engine(index),
        )
        for index in range(count)
    ]
    return LobbyVectorEnv(envs, batch_manager=manager)


def test_lobby_vector_batch_path_matches_individual_wrapper_path():
    item_catalog = Path(__file__).resolve().parents[1] / "data" / "itens.json"
    count = 2
    batch = _make_batch_vector(count, 1700, item_catalog)
    individual = LobbyVectorEnv([
        lambda index=index: CppTFTLobbyWrapper(
            seed=1700 + index,
            item_catalog_path=str(item_catalog),
        )
        for index in range(count)
    ])
    try:
        batch_obs = batch.reset(seed=9200)
        individual_obs = individual.reset(seed=9200)
        np.testing.assert_array_equal(batch_obs, individual_obs)
        for batch_env, individual_env in zip(batch.envs, individual.envs):
            batch_masks = batch_env.get_action_masks_for_training()
            individual_masks = individual_env.get_action_masks_for_training()
            for batch_player, individual_player in zip(batch_masks, individual_masks):
                assert batch_player.keys() == individual_player.keys()
                for key in batch_player:
                    np.testing.assert_array_equal(batch_player[key], individual_player[key])

        actions = _actions(count)
        batch_obs, batch_rewards, batch_dones, batch_infos = batch.step(actions)
        individual_obs, individual_rewards, individual_dones, individual_infos = individual.step(actions)
        np.testing.assert_array_equal(batch_obs, individual_obs)
        np.testing.assert_array_equal(batch_rewards, individual_rewards)
        np.testing.assert_array_equal(batch_dones, individual_dones)
        for batch_env, individual_env in zip(batch.envs, individual.envs):
            batch_masks = batch_env.get_action_masks_for_training()
            individual_masks = individual_env.get_action_masks_for_training()
            for batch_player, individual_player in zip(batch_masks, individual_masks):
                for key in batch_player:
                    np.testing.assert_array_equal(batch_player[key], individual_player[key])

        for batch_info, individual_info in zip(batch_infos, individual_infos):
            assert batch_info["round"] == individual_info["round"]
            assert batch_info["stage"] == individual_info["stage"]
            assert batch_info["step_result_snapshot"]["episode_id"] == individual_info["step_result_snapshot"]["episode_id"]
            assert batch_info["step_result_snapshot"]["decision_sequence"] == individual_info["step_result_snapshot"]["decision_sequence"]
            assert batch_info["action_trace"] == individual_info["action_trace"]
    finally:
        batch.close()
        individual.close()

def test_lobby_vector_batch_reset_failure_invalidates_all_wrappers_and_recovers():
    item_catalog = Path(__file__).resolve().parents[1] / "data" / "itens.json"
    batch = _make_batch_vector(2, 2700, item_catalog)
    real_manager = batch._batch_manager

    class FailingResetManager:
        def reset(self, *, seed=None):
            raise RuntimeError("synthetic batch reset failure")

    try:
        batch.reset(seed=9300)
        assert all(env.get_action_masks_for_training() for env in batch.envs)
        batch._batch_manager = FailingResetManager()

        with pytest.raises(RuntimeError, match="synthetic batch reset failure"):
            batch.reset(seed=9400)

        for env in batch.envs:
            with pytest.raises(RuntimeError, match="Execute reset"):
                env.get_action_masks_for_training()
            with pytest.raises(RuntimeError, match="Execute reset"):
                env.get_snapshot_metadata()

        with pytest.raises(RuntimeError, match="estado inconsistente"):
            batch.step(_actions(2))

        batch._batch_manager = real_manager
        recovered = batch.reset(seed=9500)
        assert recovered.shape[0] == 2
        assert len(batch.step(_actions(2))[3]) == 2
    finally:
        batch._batch_manager = real_manager
        batch.close()


def test_lobby_vector_batch_parity_includes_reward_provenance_and_action_events():
    item_catalog = Path(__file__).resolve().parents[1] / "data" / "itens.json"
    batch = _make_batch_vector(2, 3700, item_catalog)
    individual = LobbyVectorEnv([
        lambda index=index: CppTFTLobbyWrapper(
            seed=3700 + index,
            item_catalog_path=str(item_catalog),
        )
        for index in range(2)
    ])
    try:
        batch.reset(seed=10100)
        individual.reset(seed=10100)
        actions = _actions(2)
        _, batch_rewards, batch_dones, batch_infos = batch.step(actions)
        _, single_rewards, single_dones, single_infos = individual.step(actions)

        np.testing.assert_array_equal(batch_rewards, single_rewards)
        np.testing.assert_array_equal(batch_dones, single_dones)
        engine_ids = [info["step_result_snapshot"]["engine_instance_id"] for info in batch_infos]
        assert len(set(engine_ids)) == 2
        all_temporal_ids = set()
        for batch_info, single_info in zip(batch_infos, single_infos):
            for field in ("round", "stage", "lobby_done", "action_trace", "events", "temporal_events"):
                assert _without_instance_identifiers(batch_info[field]) == _without_instance_identifiers(single_info[field])
            for field in ("action_rewards", "combat_rewards", "placement_rewards"):
                np.testing.assert_array_equal(batch_info[field], single_info[field])
            assert batch_info["step_result_snapshot"]["episode_id"] == single_info["step_result_snapshot"]["episode_id"]
            assert batch_info["step_result_snapshot"]["decision_sequence"] == single_info["step_result_snapshot"]["decision_sequence"]
            assert batch_info["next_snapshot"]["episode_id"] == single_info["next_snapshot"]["episode_id"]
            assert batch_info["next_snapshot"]["decision_sequence"] == single_info["next_snapshot"]["decision_sequence"]
            assert _without_instance_identifiers(batch_info["action_outcome_events"]) == _without_instance_identifiers(single_info["action_outcome_events"])
            temporal_ids = {event["event_id"] for event in batch_info["temporal_events"]}
            assert len(temporal_ids) == len(batch_info["temporal_events"])
            assert not (all_temporal_ids & temporal_ids)
            all_temporal_ids.update(temporal_ids)
            assert all(event["engine_instance_id"] == batch_info["step_result_snapshot"]["engine_instance_id"]
                       for event in batch_info["temporal_events"])
            native_context = batch_info["action_context"]["native_decision_context"]
            assert len(native_context.temporal_events) == len(
                batch_info["step_result_snapshot"]["native_state_snapshot"]["temporal_events"]
            )
            assert native_context.temporal_causal_anchor_ids(0) is not None
            assert native_context.anti_loop_history(0)["contract_id"] == "tft.engine.anti-loop-history"
            assert native_context.temporal_history_availability is not None
            assert _without_instance_identifiers(batch_info["reward_audit"]["player_rewards"]) == _without_instance_identifiers(single_info["reward_audit"]["player_rewards"])
    finally:
        batch.close()
        individual.close()

def test_batch_terminal_autoreset_keeps_transition_and_next_episode_snapshots_separate():
    item_catalog = Path(__file__).resolve().parents[1] / "data" / "itens.json"
    batch = _make_batch_vector(1, 4800, item_catalog)
    try:
        batch.reset(seed=11100)
        env = batch.envs[0]
        consume = env._consume_step_result

        def force_terminal_boundary(result, source_snapshot):
            obs, rewards, _native_done, info = consume(result, source_snapshot)
            # Exercise the vector terminal-boundary contract without requiring
            # a full match simulation in this focused lifecycle test.
            return obs, rewards, True, info

        env._consume_step_result = force_terminal_boundary
        _, rewards, dones, infos = batch.step(_actions(1))
        info = infos[0]
        terminal_snapshot = info["step_result_snapshot"]
        next_snapshot = info["next_snapshot"]

        assert bool(dones.all())
        assert info["lobby_done"] is True
        assert terminal_snapshot["snapshot_kind"] == "step"
        assert next_snapshot["snapshot_kind"] == "reset"
        assert terminal_snapshot["episode_id"] != next_snapshot["episode_id"]
        assert terminal_snapshot["decision_sequence"] > 0
        terminal_native = terminal_snapshot["native_state_snapshot"]
        next_native = next_snapshot["native_state_snapshot"]
        assert terminal_native["temporal_events"]
        assert terminal_native["temporal_contract_id"] == "tft.engine.temporal-history"
        assert next_native["temporal_events"] == []
        assert next_native["episode_id"] == next_snapshot["episode_id"]
        current_snapshot = env.get_snapshot_metadata()
        assert next_snapshot["decision_sequence"] == current_snapshot["decision_sequence"]
        assert next_snapshot["player_decision_sequences"] == current_snapshot["player_decision_sequences"]
        assert rewards.shape == (1, 8)
    finally:
        batch.close()

def test_lobby_vector_batch_step_preparation_failure_invalidates_every_wrapper():
    item_catalog = Path(__file__).resolve().parents[1] / "data" / "itens.json"
    batch = _make_batch_vector(2, 5700, item_catalog)
    try:
        batch.reset(seed=12100)
        original_prepare = batch.envs[0]._prepare_batch_step

        def fail_preparation(actions):
            raise RuntimeError("synthetic action preparation failure")

        batch.envs[0]._prepare_batch_step = fail_preparation
        with pytest.raises(RuntimeError, match="interrompido durante step"):
            batch.step(_actions(2))

        for env in batch.envs:
            with pytest.raises(RuntimeError, match="Execute reset"):
                env.get_action_masks_for_training()
            with pytest.raises(RuntimeError, match="Execute reset"):
                env.get_snapshot_metadata()

        with pytest.raises(RuntimeError, match="estado inconsistente"):
            batch.step(_actions(2))

        batch.envs[0]._prepare_batch_step = original_prepare
        assert batch.reset(seed=12200).shape[0] == 2
        assert len(batch.step(_actions(2))[3]) == 2
    finally:
        batch.close()
