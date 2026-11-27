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
    validate_semantic_state_checkpoint_contract,
)
from trainer import Trainer, project_semantic_batch
from action_contract import (
    MASK_SHAPES,
    build_action_mask_checkpoint_contract,
    build_critic_mask_input_checkpoint_contract,
)
from checkpoint_contract import (
    build_checkpoint_lineage_contract,
    validate_checkpoint_lineage_contract,
)
from policy import ACTION_DIMS, TFTPolicy
from reward_contract import build_reward_checkpoint_contract
from rollout import RolloutBuffer
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
            # Player rows are separated by the full 7958-feature carrier
            # stride; preserving that stride is required for correct zero-copy
            # views, so these blocks are intentionally not globally contiguous.
            assert not block.flags.c_contiguous
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

def test_native_semantic_projection_matches_oracle_for_item_inventory_and_shop_revision():
    root = Path(__file__).resolve().parents[1]
    item_catalog = root / "data" / "itens.json"
    manager = _NativeLobbyBatchManager(1, 7314, "", str(item_catalog))
    native_engine = manager.engine(0)
    env = LobbyVectorEnv(
        [
            lambda: CppTFTLobbyWrapper(
                seed=7314,
                item_catalog_path=str(item_catalog),
                native_engine=native_engine,
            )
        ],
        batch_manager=manager,
    )
    try:
        env.reset(seed=87314)
        initial_snapshot = native_engine.get_audit_snapshot()["players"][0]
        current_shop = initial_snapshot["shop"]
        replacement_champion_id = next(
            (
                offer["champion_id"]
                for offer in current_shop[1:]
                if offer["champion_id"] != current_shop[0]["champion_id"]
            ),
            None,
        )
        assert replacement_champion_id

        # Exercise inventory-backed features and the independent shop identity
        # revision without relying on a policy action to trigger loot.
        assert native_engine.add_item_component_for_testing(
            0, "TFT_Item_BFSword"
        )
        assert native_engine.add_item_component_for_testing(
            0, "TFT_Item_ChainVest"
        )
        assert native_engine.add_completed_item_for_testing(
            0, "TFT_Item_AdaptiveHelm"
        )
        before_revision = list(
            native_engine.get_audit_snapshot()["players"][0]["shop_offer_revisions"]
        )
        assert native_engine.set_shop_offer_for_testing(0, 0, replacement_champion_id)
        after_player = native_engine.get_audit_snapshot()["players"][0]
        assert after_player["item_inventory"]
        assert after_player["item_components"]
        assert after_player["shop_offer_revisions"] != before_revision

        # Publish a fresh NativeDecisionBatch after direct authoritative test hooks.
        env.step([[[6, 0, 0, 0, 0, 0] for _ in range(8)]])
        snapshots = env.get_snapshot_metadata()
        catalog_map = env.envs[0].get_champion_id_map()
        contract = build_semantic_state_checkpoint_contract(catalog_map)
        native = env._last_native_batch.semantic_projection(
            catalog_map, contract["sha256"]
        )
        oracle_rows = Trainer._expand_lobby_snapshot_metadata(
            snapshots, 8, "item inventory and shop revision parity oracle"
        )
        oracle = [
            project_native_player_state(row, catalog_map)
            for row in oracle_rows
        ]

        expected_numeric = np.asarray(
            [row["numeric"] for row in oracle], dtype=np.float32
        )
        np.testing.assert_array_equal(
            native["numeric"].reshape(8, -1), expected_numeric
        )
        assert native["hashes"] == [row["sha256"] for row in oracle]
        assert native["identities"] == [row["identity"] for row in oracle]
        assert native["entity_identity"] == [
            row["entity_identity"] for row in oracle
        ]
        assert native["entity_identity"][0]["shop_offer_revisions"] == tuple(
            after_player["shop_offer_revisions"]
        )

        # Every typed item block must preserve its exact v8 region for all
        # eight player rows, including inventory and target-fit features.
        carrier = native["numeric"].reshape(8, -1)
        offsets = {
            "components": (1960, 10),
            "inventory": (1970, 9 * 17),
            "recipes": (2123, 100 * 17),
            "inventory_target_fit": (3823, 9 * 37),
            "recipe_target_fit": (4156, 100 * 37),
            "anvil_state": (7856, 3),
            "anvil_options": (7859, 9 * 11),
        }
        for name, (offset, width) in offsets.items():
            block = native["item_blocks"][name]
            expected = carrier[:, offset:offset + width].reshape(block.shape)
            np.testing.assert_array_equal(block, expected)
            assert not block.flags.writeable
            assert np.shares_memory(block, native["numeric"])
    finally:
        env.close()



def test_native_projection_flows_through_ppo_rollout_and_v8_checkpoint(tmp_path, monkeypatch):
    root = Path(__file__).resolve().parents[1]
    item_catalog = root / "data" / "itens.json"
    manager = _NativeLobbyBatchManager(1, 7350, "", str(item_catalog))
    env = LobbyVectorEnv(
        [
            lambda: CppTFTLobbyWrapper(
                seed=7350,
                item_catalog_path=str(item_catalog),
                native_engine=manager.engine(0),
            )
        ],
        batch_manager=manager,
    )
    try:
        observations = env.reset(seed=87350)
        catalog_map = env.envs[0].get_champion_id_map()
        semantic_contract = build_semantic_state_checkpoint_contract(catalog_map)

        def reject_python_projection(*_args, **_kwargs):
            raise AssertionError("production native PPO must not use Python semantic reconstruction")

        monkeypatch.setattr("trainer.build_semantic_batch", reject_python_projection)
        lobby_snapshots = env.get_snapshot_metadata()
        metadata_rows = Trainer._expand_lobby_snapshot_metadata(
            lobby_snapshots, 8, "native PPO/rollout/checkpoint integration",
            include_native_player_state=False,
        )
        semantic_batch = project_semantic_batch(
            env, metadata_rows, catalog_map, semantic_contract,
            lobby_snapshots=lobby_snapshots,
        )

        obs = torch.as_tensor(observations.reshape(8, -1), dtype=torch.float32)
        mask_rows = env.envs[0].get_action_masks()
        masks = {
            name: torch.as_tensor(
                np.stack([row[name] for row in mask_rows]), dtype=torch.bool
            )
            for name in MASK_SHAPES
        }
        semantic_numeric = torch.from_numpy(semantic_batch["numeric"])
        semantic_state = {
            "numeric": semantic_numeric,
            "items": semantic_item_state_tensors(
                semantic_numeric,
                trait_ids=torch.from_numpy(semantic_batch["trait_ids"]),
            ),
            "champion_ids": torch.from_numpy(semantic_batch["champion_ids"]),
            "entity_identity": semantic_batch["entity_identity"],
            "identities": semantic_batch["identities"],
            "hashes": semantic_batch["hashes"],
            "contract_id": semantic_batch["contract_id"],
            "contract_hash": semantic_batch["contract_hash"],
        }

        policy = TFTPolicy(
            obs_dim=obs.shape[-1],
            action_dims=list(ACTION_DIMS),
            hidden_size=32,
            semantic_vocab_size=max(catalog_map.values()) + 2,
            require_semantic_state=True,
        )
        actions, logprobs, entropy, values = policy.get_action_and_value(
            obs, masks=masks, deterministic=True, semantic_state=semantic_state
        )
        assert torch.isfinite(logprobs).all()
        assert torch.isfinite(entropy).all()
        assert torch.isfinite(values).all()

        rollout = RolloutBuffer(
            num_steps=1, num_envs=8, obs_dim=obs.shape[-1], action_dim=6,
            device="cpu", mask_shapes=MASK_SHAPES, require_semantic_state=True,
        )
        rollout.add(
            obs, actions, logprobs, torch.zeros(8), torch.zeros(8), values, masks,
            semantic_state=semantic_state,
        )
        minibatch = next(rollout.get_batches(batch_size=8))
        torch.testing.assert_close(
            minibatch["semantic_state"]["numeric"], semantic_numeric
        )
        torch.testing.assert_close(
            minibatch["semantic_state"]["champion_ids"], semantic_state["champion_ids"]
        )
        replay_logprobs, replay_entropy, replay_values = policy.evaluate_actions(
            minibatch["obs"], minibatch["actions"], minibatch["masks"],
            semantic_state=minibatch["semantic_state"],
        )
        assert torch.isfinite(replay_logprobs).all()
        assert torch.isfinite(replay_entropy).all()
        assert torch.isfinite(replay_values).all()
        optimizer = torch.optim.Adam(policy.parameters(), lr=3e-4)
        loss = (
            -replay_logprobs.mean()
            + 0.5 * replay_values.square().mean()
            - 0.01 * replay_entropy.mean()
        )
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()

        action_mask_contract = build_action_mask_checkpoint_contract()
        critic_mask_contract = build_critic_mask_input_checkpoint_contract()
        reward_contract = build_reward_checkpoint_contract()
        lineage = build_checkpoint_lineage_contract(
            policy.state_dict(), action_mask_contract, critic_mask_contract,
            semantic_contract, reward_contract,
        )
        checkpoint_path = tmp_path / "native-semantic-v8-ppo.pt"
        torch.save({
            "policy": policy.state_dict(),
            "semantic_state_contract": semantic_contract,
            "action_mask_contract": action_mask_contract,
            "critic_mask_input_contract": critic_mask_contract,
            "reward_contract": reward_contract,
            "checkpoint_contract": lineage,
        }, checkpoint_path)
        restored_checkpoint = torch.load(
            checkpoint_path, map_location="cpu", weights_only=False
        )
        validate_semantic_state_checkpoint_contract(
            restored_checkpoint["semantic_state_contract"], catalog_map
        )
        restored_policy = TFTPolicy(
            obs_dim=obs.shape[-1],
            action_dims=list(ACTION_DIMS),
            hidden_size=32,
            semantic_vocab_size=max(catalog_map.values()) + 2,
            require_semantic_state=True,
        )
        restored_policy.load_state_dict(restored_checkpoint["policy"], strict=True)
        validate_checkpoint_lineage_contract(
            restored_checkpoint["checkpoint_contract"],
            restored_policy.state_dict(),
            restored_checkpoint["action_mask_contract"],
            restored_checkpoint["critic_mask_input_contract"],
            restored_checkpoint["semantic_state_contract"],
            restored_checkpoint["reward_contract"],
        )
        for key, value in policy.state_dict().items():
            torch.testing.assert_close(restored_policy.state_dict()[key], value)
    finally:
        env.close()
