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
        self.player_decision_sequences = [0] * 8
        self.fail_reset = False
        self.fail_step = False

    def _native_state_snapshot(self):
        return {
            "contract_id": "tft.native-state-snapshot",
            "contract_version": 2,
            "board_geometry_id": "tft.board-grid.rectangular-4x7",
            "board_geometry_version": 1,
            "board_rows": 4,
            "board_columns": 7,
            "board_position_formula": "row=slot/7;column=slot%7",
            "source_namespace": "tft.engine.observation-snapshot",
            "producer": "TFTEngine::get_audit_snapshot",
            "engine_instance_id": f"fake-engine-{id(self)}",
            "episode_id": self.episode_id,
            "snapshot_sequence": self.decision_sequence,
            "player_decision_sequences": list(self.player_decision_sequences),
            "round": 1,
            "stage": 1,
            "finished": False,
            "shared_pool": {
                "contract_id": "tft.shared-champion-pool-snapshot",
                "contract_version": 1,
                "source_namespace": "tft.engine.observation-snapshot",
                "producer": "UnitPool::available",
                "engine_instance_id": f"fake-engine-{id(self)}",
                "episode_id": self.episode_id,
                "snapshot_sequence": self.decision_sequence,
                "player_decision_sequences": list(self.player_decision_sequences),
                "total_available": 17,
                "champions": [
                    {"champion_internal_id": 0, "champion_id": "Test_A", "cost": 1, "initial_count": 30, "available_count": 10},
                    {"champion_internal_id": 1, "champion_id": "Test_B", "cost": 2, "initial_count": 25, "available_count": 7},
                ],
            },
            "players": [
                {
                    "player_id": player_id,
                    "board": [{"occupied": False, "champion_id": "", "uuid": "", "star": 0, "cost": 0, "items": [], "trait_names": []} for _ in range(28)],
                    "bench": [{"occupied": False, "champion_id": "", "uuid": "", "star": 0, "cost": 0, "items": [], "trait_names": []} for _ in range(9)],
                    "shop": [{"occupied": False, "champion_id": "", "uuid": "", "star": 0, "cost": 0, "items": [], "trait_names": []} for _ in range(5)],
                    "shop_offer_revisions": [0] * 5,
                    "item_components": [], "item_inventory": [], "item_component_counts": [], "item_inventory_counts": [], "equipped_items": [], "item_component_catalog": [],
                    "pending_anvil": False,
                    "pending_anvil_sequence": 0,
                    "pending_anvil_options": [],
                    "item_ownership_retired": False,
                    "retired_item_component_counts": [],
                    "retired_item_inventory_counts": [],
                    "retired_equipped_item_counts": [],
                    "retired_pending_anvils": [],
                }
                for player_id in range(8)
            ],
        }

    def reset(self, _seed=None):
        if self.fail_reset:
            self.fail_reset = False
            raise RuntimeError("synthetic reset failure")
        self.episode_id += 1
        self.decision_sequence += 1
        self.player_decision_sequences = [value + 1 for value in self.player_decision_sequences]
        return {
            "observations": np.full((8, 4), self.episode_id, dtype=np.float32),
            "action_masks": make_masks(0),
            "engine_instance_id": f"fake-engine-{id(self)}",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "player_decision_sequences": list(self.player_decision_sequences),
            "native_state_snapshot": self._native_state_snapshot(),
            "observation_dim": 4,
        }

    def step(self, _actions, _timer_enabled=False, _timer_expired=False):
        if self.fail_step:
            self.fail_step = False
            raise RuntimeError("synthetic step failure")
        self.decision_sequence += 1
        self.player_decision_sequences = [value + 1 for value in self.player_decision_sequences]
        return {
            "observations": np.full((8, 4), 2, dtype=np.float32),
            "rewards": np.zeros(8, dtype=np.float32),
            "dones": np.zeros(8, dtype=np.bool_),
            "action_masks": make_masks(2),
            "engine_instance_id": f"fake-engine-{id(self)}",
            "episode_id": self.episode_id,
            "decision_sequence": self.decision_sequence,
            "player_decision_sequences": list(self.player_decision_sequences),
            "native_state_snapshot": self._native_state_snapshot(),
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


def test_wrapper_rejects_duplicate_unit_instance_uuid_across_active_owners():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    unit = {
        "occupied": True,
        "champion_id": "Test_A",
        "uuid": "duplicate-unit-uuid",
        "star": 1,
        "cost": 1,
        "items": [],
        "trait_names": ["TestTrait"],
    }
    snapshot["players"][0]["board"][0] = dict(unit)
    snapshot["players"][1]["bench"][0] = dict(unit)
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    with pytest.raises(RuntimeError, match="UUID de UnitInstance duplicado"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_invalid_unit_trait_membership():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    snapshot["players"][0]["bench"][0] = {
        "occupied": True,
        "champion_id": "Test_A",
        "uuid": "unit-with-invalid-trait",
        "star": 1,
        "cost": 1,
        "items": [],
        "trait_names": ["", 7],
    }
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    with pytest.raises(RuntimeError, match="trait_names inválido"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_reset_masks_are_taken_from_same_native_snapshot(monkeypatch):
    monkeypatch.setattr(cpp_lobby_env, "_NativeTFTLobby", FakeNativeLobby)
    lobby = cpp_lobby_env.CppTFTLobbyWrapper(seed=7)

    try:
        observations = lobby.reset()
        masks = lobby.get_action_masks()

        assert observations.shape == (8, 4)
        assert all(mask["type_mask"][0] for mask in masks)
        assert all(not mask["type_mask"][8] for mask in masks)
        metadata = lobby.get_snapshot_metadata()
        assert metadata["engine_instance_id"] == f"fake-engine-{id(lobby._engine)}"
        assert metadata["episode_id"] == 1
        assert metadata["decision_sequence"] == 1
        assert metadata["player_decision_sequences"] == [1] * 8
        assert metadata["native_state_snapshot"]["snapshot_sequence"] == 1
        pool = metadata["native_state_snapshot"]["shared_pool"]
        assert pool["snapshot_sequence"] == 1
        assert pool["total_available"] == 17
        assert len(pool["champions"]) == 2
        assert len(metadata["native_state_snapshot"]["players"][0]["board"]) == 28
        assert len(metadata["native_state_snapshot"]["players"][0]["bench"]) == 9
        assert len(metadata["native_state_snapshot"]["players"][0]["shop"]) == 5
        metadata["native_state_snapshot"]["players"][0]["board"].clear()
        assert len(lobby.get_snapshot_metadata()["native_state_snapshot"]["players"][0]["board"]) == 28
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
        metadata = info["decision_snapshot"]
        assert metadata["engine_instance_id"] == f"fake-engine-{id(lobby._engine)}"
        assert metadata["episode_id"] == 1
        assert metadata["decision_sequence"] == 2
        assert metadata["player_decision_sequences"] == [2] * 8
        assert metadata["native_state_snapshot"]["snapshot_sequence"] == 2
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


class _VectorStepEnv:
    def __init__(self, *, fail_step=False):
        self.fail_step = fail_step
        self.step_calls = 0
        self.reset_calls = 0
        self.players = [type("Player", (), {"alive": True})() for _ in range(8)]

    def reset(self):
        self.reset_calls += 1
        return np.zeros((8, 3), dtype=np.float32)

    def step(self, _actions):
        self.step_calls += 1
        if self.fail_step:
            raise ValueError("synthetic step failure")
        return (
            np.zeros((8, 3), dtype=np.float32),
            np.zeros(8, dtype=np.float32),
            False,
            {},
        )


def test_vector_env_fails_closed_after_partial_step_and_recovers_on_full_reset():
    from vector_lobby_env import LobbyVectorEnv

    first = _VectorStepEnv()
    second = _VectorStepEnv(fail_step=True)
    vector = LobbyVectorEnv([lambda: first, lambda: second])

    with pytest.raises(RuntimeError, match="estado das lobbies"):
        vector.step([np.zeros((8, 6)), np.zeros((8, 6))])

    assert first.step_calls == 1
    assert second.step_calls == 1

    with pytest.raises(RuntimeError, match="estado inconsistente"):
        vector.step([np.zeros((8, 6)), np.zeros((8, 6))])

    second.fail_step = False
    observations = vector.reset()
    assert observations.shape == (2, 8, 3)
    assert first.reset_calls == 1
    assert second.reset_calls == 1

    result = vector.step([np.zeros((8, 6)), np.zeros((8, 6))])
    assert result[0].shape == (2, 8, 3)



class _VectorResetShapeEnv:
    def __init__(self, observation_shape):
        self.observation_shape = observation_shape
        self.players = [type("Player", (), {"alive": True})() for _ in range(8)]

    def reset(self):
        return np.zeros(self.observation_shape, dtype=np.float32)

    def step(self, _actions):
        return (
            np.zeros(self.observation_shape, dtype=np.float32),
            np.zeros(8, dtype=np.float32),
            False,
            {},
        )


def test_vector_reset_stays_poisoned_when_observation_batch_cannot_be_stacked():
    from vector_lobby_env import LobbyVectorEnv
    first = _VectorResetShapeEnv((8, 3))
    second = _VectorResetShapeEnv((8, 4))
    vector = LobbyVectorEnv([lambda: first, lambda: second])

    with pytest.raises(ValueError):
        vector.reset()

    with pytest.raises(RuntimeError, match="estado inconsistente"):
        vector.step([np.zeros((8, 6)), np.zeros((8, 6))])

    # Once all environments can produce a compatible reset batch, the vector
    # may recover and accept a new step.
    second.observation_shape = (8, 3)
    observations = vector.reset()
    assert observations.shape == (2, 8, 3)

    result = vector.step([np.zeros((8, 6)), np.zeros((8, 6))])
    assert result[0].shape == (2, 8, 3)


def test_wrapper_rejects_structured_snapshot_with_mismatched_sequence():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 2
    native.player_decision_sequences = [2] * 8
    snapshot = native._native_state_snapshot()
    snapshot["snapshot_sequence"] = 1
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 1,
        "decision_sequence": 2,
        "player_decision_sequences": [2] * 8,
    }
    with pytest.raises(RuntimeError, match="sequência publicada"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_structured_snapshot_with_wrong_slot_cardinality():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 1
    native.player_decision_sequences = [1] * 8
    snapshot = native._native_state_snapshot()
    snapshot["players"][0]["board"].pop()
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 1,
        "decision_sequence": 1,
        "player_decision_sequences": [1] * 8,
    }
    with pytest.raises(RuntimeError, match="cardinalidade inválida em board"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)



def test_wrapper_rejects_pool_snapshot_with_mismatched_sequence():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 2
    native.player_decision_sequences = [2] * 8
    snapshot = native._native_state_snapshot()
    snapshot["shared_pool"]["snapshot_sequence"] = 1
    identity = {"engine_instance_id": f"fake-engine-{id(native)}", "episode_id": 1, "decision_sequence": 2, "player_decision_sequences": [2] * 8}
    with pytest.raises(RuntimeError, match="identidade do snapshot nativo"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_pool_snapshot_with_inconsistent_total():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 1
    native.player_decision_sequences = [1] * 8
    snapshot = native._native_state_snapshot()
    snapshot["shared_pool"]["total_available"] = 18
    identity = {"engine_instance_id": f"fake-engine-{id(native)}", "episode_id": 1, "decision_sequence": 1, "player_decision_sequences": [1] * 8}
    with pytest.raises(RuntimeError, match="soma das disponibilidades"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_accepts_counted_item_ownership_rows_and_live_equipment():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 1
    native.player_decision_sequences = [1] * 8
    snapshot = native._native_state_snapshot()
    player = snapshot["players"][0]
    player["item_component_counts"] = [{"catalog_id": "component_x", "count": 2}]
    player["item_inventory_counts"] = [{"catalog_id": "item_y", "count": 1}]
    player["equipped_items"] = [{
        "unit_uuid": "unit-live-1", "location": "board", "slot": 3, "catalog_id": "item_z"
    }]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 1,
        "decision_sequence": 1,
        "player_decision_sequences": [1] * 8,
    }
    copied = cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)
    assert copied["players"][0]["item_component_counts"][0]["count"] == 2
    assert copied["players"][0]["equipped_items"][0]["unit_uuid"] == "unit-live-1"


def test_wrapper_rejects_invalid_item_ownership_count():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 1
    native.player_decision_sequences = [1] * 8
    snapshot = native._native_state_snapshot()
    snapshot["players"][0]["item_inventory_counts"] = [{"catalog_id": "item_x", "count": True}]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 1,
        "decision_sequence": 1,
        "player_decision_sequences": [1] * 8,
    }
    with pytest.raises(RuntimeError, match="item_inventory_counts inválido"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_equipment_without_valid_live_slot():
    native = FakeNativeLobby()
    native.episode_id = 1
    native.decision_sequence = 1
    native.player_decision_sequences = [1] * 8
    snapshot = native._native_state_snapshot()
    snapshot["players"][0]["equipped_items"] = [{
        "unit_uuid": "unit-live-1", "location": "board", "slot": 28, "catalog_id": "item_x"
    }]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 1,
        "decision_sequence": 1,
        "player_decision_sequences": [1] * 8,
    }
    with pytest.raises(RuntimeError, match="equipped_items inválido"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_native_snapshot_rejects_invalid_shop_offer_revisions():
    wrapper = cpp_lobby_env.CppTFTLobbyWrapper.__new__(cpp_lobby_env.CppTFTLobbyWrapper)
    snapshot = FakeNativeLobby()._native_state_snapshot()
    snapshot["players"][0]["shop_offer_revisions"] = [0, True, 0, 0, 0]
    identity = {"engine_instance_id": snapshot["engine_instance_id"], "episode_id": snapshot["episode_id"], "decision_sequence": snapshot["snapshot_sequence"], "player_decision_sequences": snapshot["player_decision_sequences"]}
    with pytest.raises(RuntimeError, match="revisões de oferta inválidas"):
        wrapper._copy_native_state_snapshot(snapshot, identity)


def test_native_snapshot_rejects_occupied_shop_offer_without_revision():
    wrapper = cpp_lobby_env.CppTFTLobbyWrapper.__new__(cpp_lobby_env.CppTFTLobbyWrapper)
    snapshot = FakeNativeLobby()._native_state_snapshot()
    snapshot["players"][0]["shop"][0] = {"occupied": True, "champion_id": "Test_A", "uuid": "unit-a", "star": 1, "cost": 1, "items": [], "trait_names": []}
    identity = {"engine_instance_id": snapshot["engine_instance_id"], "episode_id": snapshot["episode_id"], "decision_sequence": snapshot["snapshot_sequence"], "player_decision_sequences": snapshot["player_decision_sequences"]}
    with pytest.raises(RuntimeError, match="sem revisão nativa"):
        wrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_accepts_terminal_item_retirement_summary():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    player = snapshot["players"][0]
    player["item_ownership_retired"] = True
    player["retired_item_component_counts"] = [{"catalog_id": "sword", "count": 2}]
    player["retired_item_inventory_counts"] = [{"catalog_id": "damage_blade", "count": 1}]
    player["retired_equipped_item_counts"] = [
        {"unit_uuid": "unit-retired", "catalog_id": "guard_plate", "count": 1}
    ]
    player["retired_pending_anvils"] = [
        {"sequence": 7, "kind": 0, "options": ["sword", "bow"]}
    ]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    copied = cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)
    assert copied["players"][0]["item_ownership_retired"] is True
    assert copied["players"][0]["retired_item_component_counts"][0]["count"] == 2


def test_wrapper_rejects_live_item_ownership_after_retirement():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    player = snapshot["players"][0]
    player["item_ownership_retired"] = True
    player["item_components"] = ["sword"]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    with pytest.raises(RuntimeError, match="Ownership ativo presente"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_malformed_retired_equipment_count():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    snapshot["players"][0]["retired_equipped_item_counts"] = [
        {"unit_uuid": "unit-retired", "catalog_id": "guard_plate", "count": True}
    ]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    with pytest.raises(RuntimeError, match="retired_equipped_item_counts inválido"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_pending_anvil_without_identity_sequence():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    player = snapshot["players"][0]
    player["pending_anvil"] = True
    player["pending_anvil_options"] = ["sword"]
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    with pytest.raises(RuntimeError, match="Bigorna pendente sem sequência"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)


def test_wrapper_rejects_anvil_sequence_without_pending_choice():
    native = FakeNativeLobby()
    snapshot = native._native_state_snapshot()
    snapshot["players"][0]["pending_anvil_sequence"] = 3
    identity = {
        "engine_instance_id": f"fake-engine-{id(native)}",
        "episode_id": 0,
        "decision_sequence": 0,
        "player_decision_sequences": [0] * 8,
    }
    with pytest.raises(RuntimeError, match="Sequência de bigorna presente"):
        cpp_lobby_env.CppTFTLobbyWrapper._copy_native_state_snapshot(snapshot, identity)
