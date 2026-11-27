from pathlib import Path
import hashlib
import json

import numpy as np
import torch

from cpp_lobby_env import CppTFTLobbyWrapper, _NativeLobbyBatchManager
from semantic_observation import (
    build_semantic_state_checkpoint_contract,
    project_native_player_state,
    semantic_item_state_tensors,
)
from trainer import Trainer
from vector_lobby_env import LobbyVectorEnv


def test_semantic_item_adapter_preserves_native_trait_id_tensor():
    numeric = torch.zeros((8, 7958), dtype=torch.float32)
    native_trait_ids = torch.arange(8 * 42 * 10, dtype=torch.long).reshape(8, 42, 10)
    items = semantic_item_state_tensors(numeric, trait_ids=native_trait_ids)
    assert items["trait_ids"] is native_trait_ids


def test_semantic_hash_canonical_json_cross_language_edge_fixture():
    payload = {
        "empty": [],
        "limit": [-2147483648, 2147483647, 0.0, 1.0],
        "optional": None,
        "unicode": "Akame-赤い🌸",
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    assert canonical == (
        '{"empty":[],"limit":[-2147483648,2147483647,0.0,1.0],'
        '"optional":null,"unicode":"Akame-赤い🌸"}'
    )
    assert hashlib.sha256(canonical.encode("utf-8")).hexdigest() == (
        "2e2d30a202100fa3180341c79085abcaf66b0bd265bc933337d3e77a6819532e"
    )


def test_native_semantic_v8_projection_matches_python_oracle_exactly():
    root = Path(__file__).resolve().parents[1]
    item_catalog = root / "data" / "itens.json"
    manager = _NativeLobbyBatchManager(1, 7310, "", str(item_catalog))
    env = LobbyVectorEnv(
        [
            lambda: CppTFTLobbyWrapper(
                seed=7310,
                item_catalog_path=str(item_catalog),
                native_engine=manager.engine(0),
            )
        ],
        batch_manager=manager,
    )
    try:
        env.reset(seed=87310)
        catalog_map = env.envs[0].get_champion_id_map()
        contract = build_semantic_state_checkpoint_contract(catalog_map)
        lobby_snapshots = env.get_snapshot_metadata()
        metadata_rows = Trainer._expand_lobby_snapshot_metadata(
            lobby_snapshots, 8, "native semantic fast-path test",
            include_native_player_state=False,
        )
        assert all("native_player_state" not in row for row in metadata_rows)
        assert all(row["native_state_contract_id"] == "tft.native-state-snapshot" for row in metadata_rows)
        oracle_rows = Trainer._expand_lobby_snapshot_metadata(
            lobby_snapshots, 8, "native semantic parity oracle"
        )
        native = env._last_native_batch.semantic_projection(
            catalog_map, contract["sha256"]
        )
        oracle = [
            project_native_player_state(row, catalog_map)
            for row in oracle_rows
        ]

        expected_numeric = np.asarray(
            [row["numeric"] for row in oracle], dtype=np.float32
        )
        expected_champion_ids = np.asarray(
            [row["champion_ids"] for row in oracle], dtype=np.int64
        )
        np.testing.assert_array_equal(
            native["numeric"].reshape(8, -1), expected_numeric
        )
        np.testing.assert_array_equal(
            native["champion_ids"].reshape(8, -1), expected_champion_ids
        )
        expected_trait_ids = np.rint(
            expected_numeric[:, 70 + np.arange(42)[:, None] * 45 + 29 + np.arange(10)[None, :]]
            * 65536
        ).astype(np.int64)
        np.testing.assert_array_equal(
            native["trait_ids"].reshape(8, 42, 10), expected_trait_ids
        )
        assert native["hashes"] == [row["sha256"] for row in oracle]
        assert native["identities"] == [row["identity"] for row in oracle]
        assert native["entity_identity"] == [
            row["entity_identity"] for row in oracle
        ]
        assert native["item_catalog_sha256"] == oracle[0]["item_state_identity"]["item_catalog_sha256"]
        assert native["contract_id"] == contract["contract"]["contract_id"]
        assert native["contract_hash"] == contract["sha256"]

        # The six item tensors are independent typed views over the one
        # contiguous v8 carrier, not copied per-block allocations.
        item_blocks = native["item_blocks"]
        expected_shapes = {
            "components": (1, 8, 10),
            "inventory": (1, 8, 9, 17),
            "recipes": (1, 8, 100, 17),
            "inventory_target_fit": (1, 8, 9, 37),
            "recipe_target_fit": (1, 8, 100, 37),
            "anvil_options": (1, 8, 9, 11),
            "anvil_state": (1, 8, 3),
        }
        assert set(item_blocks) == set(expected_shapes)
        for name, shape in expected_shapes.items():
            block = item_blocks[name]
            assert block.shape == shape
            assert block.dtype == np.float32
            assert block.flags.c_contiguous
            assert not block.flags.writeable
            assert np.shares_memory(block, native["numeric"])
        # Verify every typed block is an exact view of its canonical v8
        # numeric carrier region, not merely a correctly-shaped alias.
        item_offsets = {
            "components": (1960, 10),
            "inventory": (1970, 9 * 17),
            "recipes": (2123, 100 * 17),
            "inventory_target_fit": (3823, 9 * 37),
            "recipe_target_fit": (4156, 100 * 37),
            "anvil_state": (7856, 3),
            "anvil_options": (7859, 9 * 11),
        }
        carrier = native["numeric"].reshape(8, -1)
        for name, (offset, width) in item_offsets.items():
            expected = carrier[:, offset:offset + width].reshape(item_blocks[name].shape)
            np.testing.assert_array_equal(item_blocks[name], expected)

        # Views retain their backing allocation even if the dictionary's
        # direct carrier reference is released.
        retained_components = item_blocks["components"]
        view_owner = retained_components.base
        assert isinstance(view_owner, dict)
        assert view_owner["batch"] is env._last_native_batch
        assert view_owner["numeric"] is native["numeric"]
        del native["numeric"]
        assert retained_components.shape == (1, 8, 10)
        assert np.isfinite(retained_components).all()
    finally:
        env.close()



def test_native_semantic_projection_matches_oracle_after_physical_duplicate_upgrade():
    root = Path(__file__).resolve().parents[1]
    item_catalog = root / "data" / "itens.json"
    manager = _NativeLobbyBatchManager(1, 7312, "", str(item_catalog))
    native_engine = manager.engine(0)
    env = LobbyVectorEnv(
        [
            lambda: CppTFTLobbyWrapper(
                seed=7312,
                item_catalog_path=str(item_catalog),
                native_engine=native_engine,
            )
        ],
        batch_manager=manager,
    )
    try:
        env.reset(seed=87312)
        initial = native_engine.get_audit_snapshot()
        champion_id = initial["players"][0]["shop"][0]["champion_id"]
        assert champion_id
        assert native_engine.set_player_economy_for_testing(0, 20, 3, 0)
        assert native_engine.set_unit_for_testing(0, True, 0, champion_id, 1)
        assert native_engine.set_unit_for_testing(0, False, 0, champion_id, 1)
        assert native_engine.set_shop_offer_for_testing(0, 0, champion_id)

        before = native_engine.get_audit_snapshot()["players"][0]
        physical_uuids = {
            before["board"][0]["uuid"],
            before["bench"][0]["uuid"],
            before["shop"][0]["uuid"],
        }
        assert len(physical_uuids) == 3 and "" not in physical_uuids

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [0, 0, 0, 0, 0, 0]
        env.step([actions])

        after = native_engine.get_audit_snapshot()["players"][0]
        upgraded = [
            unit
            for location in ("board", "bench")
            for unit in after[location]
            if unit["occupied"] and unit["champion_id"] == champion_id and unit["star"] == 2
        ]
        assert len(upgraded) == 1
        assert upgraded[0]["uuid"] in physical_uuids

        snapshots = env.get_snapshot_metadata()
        catalog_map = env.envs[0].get_champion_id_map()
        contract = build_semantic_state_checkpoint_contract(catalog_map)
        native = env._last_native_batch.semantic_projection(
            catalog_map, contract["sha256"]
        )
        oracle_rows = Trainer._expand_lobby_snapshot_metadata(
            snapshots, 8, "physical duplicate semantic parity oracle"
        )
        oracle = [
            project_native_player_state(row, catalog_map)
            for row in oracle_rows
        ]
        expected_numeric = np.asarray(
            [row["numeric"] for row in oracle], dtype=np.float32
        )
        expected_champion_ids = np.asarray(
            [row["champion_ids"] for row in oracle], dtype=np.int64
        )
        np.testing.assert_array_equal(
            native["numeric"].reshape(8, -1), expected_numeric
        )
        np.testing.assert_array_equal(
            native["champion_ids"].reshape(8, -1), expected_champion_ids
        )
        assert native["hashes"] == [row["sha256"] for row in oracle]
        assert native["identities"] == [row["identity"] for row in oracle]
        assert native["entity_identity"] == [
            row["entity_identity"] for row in oracle
        ]
    finally:
        env.close()


def test_terminal_auto_reset_next_snapshot_uses_native_semantic_projection():
    root = Path(__file__).resolve().parents[1]
    item_catalog = root / "data" / "itens.json"
    manager = _NativeLobbyBatchManager(1, 7311, "", str(item_catalog))
    env = LobbyVectorEnv(
        [
            lambda: CppTFTLobbyWrapper(
                seed=7311,
                item_catalog_path=str(item_catalog),
                native_engine=manager.engine(0),
            )
        ],
        batch_manager=manager,
    )
    try:
        env.reset(seed=87311)
        catalog_map = env.envs[0].get_champion_id_map()
        contract = build_semantic_state_checkpoint_contract(catalog_map)
        wrapper = env.envs[0]
        consume = wrapper._consume_step_result

        def force_terminal_boundary(result, source_snapshot):
            observations, rewards, _native_done, info = consume(result, source_snapshot)
            return observations, rewards, True, info

        wrapper._consume_step_result = force_terminal_boundary
        _, _, dones, infos = env.step([[[6, 0, 0, 0, 0, 0] for _ in range(8)]])
        assert bool(dones.all())
        next_snapshots = [info["next_snapshot"] for info in infos]
        native = env.semantic_projection_from_snapshots(
            next_snapshots, catalog_map, contract["sha256"]
        )
        compact_rows = Trainer._expand_lobby_snapshot_metadata(
            next_snapshots, 8, "terminal native semantic fast path",
            include_native_player_state=False,
        )
        assert all("native_player_state" not in row for row in compact_rows)
        oracle_rows = Trainer._expand_lobby_snapshot_metadata(
            next_snapshots, 8, "terminal semantic parity oracle"
        )
        oracle = [
            project_native_player_state(row, catalog_map)
            for row in oracle_rows
        ]
        np.testing.assert_array_equal(
            native["numeric"].reshape(8, -1),
            np.asarray([row["numeric"] for row in oracle], dtype=np.float32),
        )
        np.testing.assert_array_equal(
            native["champion_ids"].reshape(8, -1),
            np.asarray([row["champion_ids"] for row in oracle], dtype=np.int64),
        )
        expected_numeric = np.asarray([row["numeric"] for row in oracle], dtype=np.float32)
        expected_trait_ids = np.rint(
            expected_numeric[:, 70 + np.arange(42)[:, None] * 45 + 29 + np.arange(10)[None, :]]
            * 65536
        ).astype(np.int64)
        np.testing.assert_array_equal(
            native["trait_ids"].reshape(8, 42, 10), expected_trait_ids
        )
        assert native["hashes"] == [row["sha256"] for row in oracle]
        assert native["identities"] == [row["identity"] for row in oracle]
    finally:
        env.close()

def test_native_semantic_projection_matches_oracle_with_equipped_item_state():
    root = Path(__file__).resolve().parents[1]
    item_catalog = root / "data" / "itens.json"
    manager = _NativeLobbyBatchManager(1, 7313, "", str(item_catalog))
    native_engine = manager.engine(0)
    env = LobbyVectorEnv(
        [
            lambda: CppTFTLobbyWrapper(
                seed=7313,
                item_catalog_path=str(item_catalog),
                native_engine=native_engine,
            )
        ],
        batch_manager=manager,
    )
    try:
        env.reset(seed=87313)
        before = native_engine.get_audit_snapshot()["players"][0]
        starter_slot = next(
            (slot for slot, unit in enumerate(before["bench"]) if unit["occupied"]),
            None,
        )
        assert starter_slot is not None
        starter_uuid = before["bench"][starter_slot]["uuid"]
        assert starter_uuid

        item_id = "TFT_Item_AdaptiveHelm"
        assert native_engine.add_completed_item_for_testing(0, item_id)
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = [7, 0, 28 + starter_slot, 0, 0, 0]
        env.step([actions])

        after = native_engine.get_audit_snapshot()["players"][0]
        assert after["item_inventory"] == []
        assert any(
            row["unit_uuid"] == starter_uuid and row["catalog_id"] == item_id
            for row in after["equipped_items"]
        )

        snapshots = env.get_snapshot_metadata()
        catalog_map = env.envs[0].get_champion_id_map()
        contract = build_semantic_state_checkpoint_contract(catalog_map)
        native = env._last_native_batch.semantic_projection(
            catalog_map, contract["sha256"]
        )
        oracle_rows = Trainer._expand_lobby_snapshot_metadata(
            snapshots, 8, "equipped-item semantic parity oracle"
        )
        oracle = [
            project_native_player_state(row, catalog_map)
            for row in oracle_rows
        ]
        expected_numeric = np.asarray(
            [row["numeric"] for row in oracle], dtype=np.float32
        )
        expected_champion_ids = np.asarray(
            [row["champion_ids"] for row in oracle], dtype=np.int64
        )
        np.testing.assert_array_equal(
            native["numeric"].reshape(8, -1), expected_numeric
        )
        np.testing.assert_array_equal(
            native["champion_ids"].reshape(8, -1), expected_champion_ids
        )
        assert native["hashes"] == [row["sha256"] for row in oracle]
        assert native["identities"] == [row["identity"] for row in oracle]
        assert native["entity_identity"] == [
            row["entity_identity"] for row in oracle
        ]
    finally:
        env.close()
