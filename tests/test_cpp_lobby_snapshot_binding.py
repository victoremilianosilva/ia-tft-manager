"""Regression tests for observation/action-mask snapshot correlation."""

import numpy as np
import pytest

import cpp_lobby_env


def make_masks(marker):
    keys = {
        "type_mask": (9,),
        "shop_mask": (5,),
        "bench_source_mask": (9,),
        "board_target_mask": (28,),
        "board_source_mask": (28,),
        "board_move_target_masks": (28, 28),
        "bench_move_source_mask": (9,),
        "bench_to_board_target_masks": (9, 28),
        "item_inventory_mask": (9,),
        "item_component_first_mask": (10,),
        "item_component_pair_masks": (10, 10),
        "item_target_mask": (37,),
    }
    masks = []
    for player in range(8):
        item = {key: np.zeros(shape, dtype=np.bool_) for key, shape in keys.items()}
        item["type_mask"][marker] = True
        masks.append(item)
    return masks


class FakeNativeLobby:
    def __init__(self, *_args):
        self.mask_reads = 0
        self.episode_id = 0
        self.decision_sequence = 0
        self.fail_reset = False
        self.fail_step = False

    def reset(self, _seed=None):
        if self.fail_reset:
            self.fail_reset = False
            raise RuntimeError("synthetic reset failure")
        self.episode_id += 1
        self.decision_sequence += 1
        return {
            "observations": np.full((8, 4), self.episode_id, dtype=np.float32),
            "action_masks": make_masks(0),
            "engine_instance_id": f"fake-engine-{id(self)}",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "observation_dim": 4,
        }

    def step(self, _actions, _timer_enabled=False, _timer_expired=False):
        if self.fail_step:
            self.fail_step = False
            raise RuntimeError("synthetic step failure")
        self.decision_sequence += 1
        return {
            "observations": np.full((8, 4), 2, dtype=np.float32),
            "rewards": np.zeros(8, dtype=np.float32),
            "dones": np.zeros(8, dtype=np.bool_),
            "action_masks": make_masks(2),
            "engine_instance_id": f"fake-engine-{id(self)}",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "round": 3,
            "stage": 2,
            "lobby_done": False,
            "players": [
                {"player_id": i, "alive": True, "eliminated": False}
                for i in range(8)
            ],
            "action_traces": [
                {
                    "player_id": player_id,
                    "requested_action": [6, 0, 0, 0, 0, 0],
                    "effective_action": [6, 0, 0, 0, 0, 0],
                    "handler_applied": True,
                    "status_reason": "applied",
                }
                for player_id in range(8)
            ],
            "events": [],
        }

    def get_action_masks(self):
        self.mask_reads += 1
        # A later live read deliberately differs from the returned snapshot.
        return make_masks(8)

    def close(self):
        pass


def test_reset_masks_are_taken_from_same_native_snapshot(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        observations = lobby.reset()
        masks = lobby.get_action_masks()

        assert observations.shape == (8, 4)
        assert all(mask["type_mask"][0] for mask in masks)
        assert all(not mask["type_mask"][8] for mask in masks)
        assert lobby.get_snapshot_metadata() == {
            "engine_instance_id": f"fake-engine-{id(lobby._engine)}",
            "episode_id": 1,
            "decision_sequence": 1,
            "round": 0,
            "stage": 1,
            "snapshot_kind": "reset",
        }
        assert lobby._engine.mask_reads == 0
    finally:
        lobby.close()


def test_step_masks_are_taken_from_same_native_snapshot(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        observations, rewards, done, info = lobby.step(
            [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        )
        masks = lobby.get_action_masks()

        assert observations.shape == (8, 4)
        assert rewards.shape == (8,)
        assert done is False
        assert all(mask["type_mask"][2] for mask in masks)
        assert all(not mask["type_mask"][8] for mask in masks)
        assert len(info["action_trace"]) == 8
        assert info["action_trace"][0] == {
            "player_id": 0,
            "requested_action": [6, 0, 0, 0, 0, 0],
            "effective_action": [6, 0, 0, 0, 0, 0],
            "handler_applied": True,
            "status_reason": "applied",
        }
        assert info["decision_snapshot"] == {
            "engine_instance_id": f"fake-engine-{id(lobby._engine)}",
            "episode_id": 1,
            "decision_sequence": 2,
            "round": 3,
            "stage": 2,
            "snapshot_kind": "step",
        }
        assert lobby.get_snapshot_metadata() == info["decision_snapshot"]
        assert lobby._engine.mask_reads == 0
    finally:
        lobby.close()


def test_policy_requires_branch_specific_bench_masks():
    from policy import TFTPolicy

    with pytest.raises(ValueError, match="bench_move_source_mask"):
        TFTPolicy._require_mask(
            {"bench_source_mask": np.ones((8, 9), dtype=np.bool_)},
            "bench_move_source_mask",
        )

    with pytest.raises(ValueError, match="bench_to_board_target_masks"):
        TFTPolicy._require_mask(
            {"board_target_mask": np.ones((8, 28), dtype=np.bool_)},
            "bench_to_board_target_masks",
        )


def test_policy_required_mask_returns_exact_snapshot_payload():
    from policy import TFTPolicy

    expected = np.ones((8, 9, 28), dtype=np.bool_)
    actual = TFTPolicy._require_mask(
        {"bench_to_board_target_masks": expected},
        "bench_to_board_target_masks",
    )
    assert actual is expected


def test_item_ablation_fails_closed_when_it_removes_all_legal_actions(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    monkeypatch.setenv("TFT_ABLATE_ITEM_ACTIONS", "1")
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        # The fake native snapshot permits only craft (type 8). Ablation removes
        # it; the wrapper must not fabricate HOLD/PASS as a replacement.
        lobby._last_action_masks = make_masks(8)
        import pytest
        with pytest.raises(RuntimeError, match="nenhuma ação substituta será inventada"):
            lobby.get_action_masks()
    finally:
        lobby.close()


def test_item_ablation_preserves_mandatory_anvil_choice(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    monkeypatch.setenv("TFT_ABLATE_ITEM_ACTIONS", "1")
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        lobby._last_action_masks = make_masks(7)
        result = lobby.get_action_masks()
        assert all(mask["type_mask"][7] for mask in result)
        assert all(not mask["type_mask"][8] for mask in result)
    finally:
        lobby.close()


def test_returned_masks_are_copies_not_mutable_snapshot_storage(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        first = lobby.get_action_masks()
        first[0]["type_mask"][:] = False
        second = lobby.get_action_masks()

        assert second[0]["type_mask"][0]
        assert lobby._engine.mask_reads == 0
    finally:
        lobby.close()



def test_failed_step_invalidates_previous_snapshot_and_masks(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        assert lobby.get_action_masks()
        assert lobby.get_snapshot_metadata()["snapshot_kind"] == "reset"

        lobby._engine.fail_step = True
        with pytest.raises(RuntimeError, match="synthetic step failure"):
            lobby.step([[6, 0, 0, 0, 0, 0] for _ in range(8)])

        with pytest.raises(RuntimeError, match="Execute reset"):
            lobby.get_action_masks()
        with pytest.raises(RuntimeError, match="Execute reset"):
            lobby.get_snapshot_metadata()

        # A successful reset establishes a fresh usable pair again.
        lobby.reset()
        assert lobby.get_snapshot_metadata()["snapshot_kind"] == "reset"
        assert lobby.get_action_masks()
    finally:
        lobby.close()


def test_failed_reset_invalidates_previous_snapshot_and_masks(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        assert lobby.get_action_masks()
        assert lobby.get_snapshot_metadata()["snapshot_kind"] == "reset"

        lobby._engine.fail_reset = True
        with pytest.raises(RuntimeError, match="synthetic reset failure"):
            lobby.reset()

        with pytest.raises(RuntimeError, match="Execute reset"):
            lobby.get_action_masks()
        with pytest.raises(RuntimeError, match="Execute reset"):
            lobby.get_snapshot_metadata()
    finally:
        lobby.close()


def test_player_liveness_exposes_latest_wrapper_state(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        lobby.reset()
        assert lobby.get_player_liveness() == [True] * 8

        lobby._players[3].alive = False
        assert lobby.get_player_liveness() == [True, True, True, False, True, True, True, True]
    finally:
        lobby.close()
