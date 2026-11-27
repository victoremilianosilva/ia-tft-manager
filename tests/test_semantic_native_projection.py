from pathlib import Path

import numpy as np

from cpp_lobby_env import CppTFTLobbyWrapper, _NativeLobbyBatchManager
from semantic_observation import (
    build_semantic_state_checkpoint_contract,
    project_native_player_state,
)
from trainer import Trainer
from vector_lobby_env import LobbyVectorEnv


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
        metadata_rows = Trainer._expand_lobby_snapshot_metadata(
            env.get_snapshot_metadata(), 8, "native semantic parity test"
        )
        native = env._last_native_batch.semantic_projection(
            catalog_map, contract["sha256"]
        )
        oracle = [
            project_native_player_state(row, catalog_map)
            for row in metadata_rows
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
        assert native["item_catalog_sha256"] == oracle[0]["item_state_identity"]["item_catalog_sha256"]
        assert native["contract_id"] == contract["contract"]["contract_id"]
        assert native["contract_hash"] == contract["sha256"]
    finally:
        env.close()
