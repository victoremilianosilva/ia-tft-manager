from collections.abc import Mapping
"""Integration regressions for native action masks and PPO strategy signals.

Champion identities are loaded from the active production catalog so these tests
remain valid when the TFT set changes.
"""
import json
from pathlib import Path

import numpy as np
import torch

from action_contract import MASK_SHAPES, hash_mask_rows
from policy import TFTPolicy, ACTION_DIMS
from trainer import Trainer
from cpp_lobby_env import CppTFTLobbyWrapper
from semantic_observation import build_semantic_batch, catalog_identity, semantic_item_state_tensors


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "units_gerado.json"


def _active_champion_ids(count: int = 2) -> list[str]:
    with CATALOG_PATH.open(encoding="utf-8") as source:
        catalog = json.load(source)
    ids = [
        str(unit.get("apiName", "")).strip()
        for unit in catalog
        if str(unit.get("apiName", "")).strip()
    ]
    # Preserve catalog order while avoiding duplicate identifiers.
    ids = list(dict.fromkeys(ids))
    if len(ids) < count:
        raise AssertionError(
            f"Active champion catalog needs at least {count} unique API IDs; got {len(ids)}"
        )
    return ids[:count]


def _state_signature(player):
    def slots(units):
        return tuple(
            (u.get("champion_id"), u.get("uuid"), int(u.get("star", 0)))
            if u.get("occupied") else None
            for u in units
        )
    return slots(player["board"]), slots(player["bench"])


def _move_action(source, target):
    # PPO action layout: type, shop, bench, board_target, board_source, move_target.
    return [4, 0, 0, target, source, target]


def test_native_mask_blocks_reverse_swap_and_executor_rejects_forced_reverse():
    first_champion, second_champion = _active_champion_ids(2)
    lobby = CppTFTLobbyWrapper(seed=20261022)
    try:
        lobby.reset(seed=20261022)
        native = lobby._engine

        assert native.set_player_economy_for_testing(0, 10, 3, 0)
        assert native.set_unit_for_testing(0, True, 3, first_champion, 1)
        assert native.set_unit_for_testing(0, True, 10, second_champion, 1)

        native_snapshot_after_setup = lobby.get_audit_snapshot()
        before = native_snapshot_after_setup["players"][0]
        before_signature = _state_signature(before)
        # Test-only setters mutate native state outside reset/step. Refresh the
        # wrapper's source snapshot at the same sequence so action facts are
        # compared against the exact state used by the native action handler.
        lobby._last_snapshot_metadata["native_state_snapshot"] = (
            lobby._copy_native_state_snapshot(
                native_snapshot_after_setup, lobby._last_snapshot_metadata
            )
        )
        # Read the native mask directly for this fixture; production consumers
        # must use the wrapper's correlated snapshot.
        forward_masks = native.get_action_masks()[0]
        assert bool(forward_masks["type_mask"][4])
        assert bool(forward_masks["board_move_target_masks"][3][10]), (
            "O movimento inicial deve ser elegível na máscara nativa."
        )

        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = _move_action(3, 10)
        lobby.step(actions)

        after_forward = lobby.get_audit_snapshot()["players"][0]
        assert _state_signature(after_forward) != before_signature, (
            "A engine não aplicou o primeiro movimento autorizado; "
            f"before={before_signature!r}, after={_state_signature(after_forward)!r}"
        )

        reverse_masks = lobby.get_action_masks()[0]
        reverse_allowed = bool(reverse_masks["board_move_target_masks"][10][3])
        assert not reverse_allowed, (
            "A máscara C++ permitiu a reversão imediata 10->3. "
            f"mask[10][3]={int(reverse_masks['board_move_target_masks'][10][3])}; "
            f"board={_state_signature(after_forward)!r}"
        )

        # Bypass the policy mask to exercise the executor's second line of defense.
        before_forced_reverse = _state_signature(after_forward)
        actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
        actions[0] = _move_action(10, 3)
        lobby.step(actions)
        after_forced_reverse = lobby.get_audit_snapshot()["players"][0]
        assert _state_signature(after_forced_reverse) == before_forced_reverse, (
            "A execução C++ aceitou uma reversão que a máscara deveria bloquear. "
            f"before={before_forced_reverse!r}, after={_state_signature(after_forced_reverse)!r}"
        )
    finally:
        lobby.close()


def test_native_composition_score_requires_a_published_active_composition():
    lobby = CppTFTLobbyWrapper(seed=20261023)
    try:
        lobby.reset(seed=20261023)
        native = lobby._engine
        player_state = native.get_audit_snapshot()["players"][0]["strategic_state"]
        champion_ids = player_state.get("active_unit_ids", [])
        api_by_id = {
            int(internal_id): api_name
            for api_name, internal_id in native.get_champion_id_map().items()
        }

        if not player_state.get("active_composition_valid", False):
            # No active composition means no authoritative unit-priority snapshot.
            # The compatibility score must stay unavailable rather than inventing
            # a score for an arbitrary first catalog entry.
            assert not champion_ids
            for champion_id in _active_champion_ids(1):
                scores = [
                    float(native.get_unit_comp_score(0, champion_id, star))
                    for star in (1, 2, 3)
                ]
                assert scores == [0.0, 0.0, 0.0], (
                    "O score de composição foi publicado sem composição ativa: "
                    f"{champion_id}={scores}"
                )
            return

        assert champion_ids, "Composição ativa publicada sem unidades-alvo."
        champion_id = api_by_id.get(int(champion_ids[0]))
        assert champion_id, (
            "Unidade da composição ativa não existe no mapa do catálogo nativo."
        )
        scores = [
            float(native.get_unit_comp_score(0, champion_id, star))
            for star in (1, 2, 3)
        ]
        assert all(np.isfinite(score) for score in scores), (
            f"Scores nativos não finitos para {champion_id}: {scores}"
        )
        assert scores[1] > scores[0] and scores[2] > scores[1], (
            f"O sinal estratégico não diferencia tiers para unidade-alvo "
            f"{champion_id}: 1★={scores[0]}, 2★={scores[1]}, 3★={scores[2]}"
        )
    finally:
        lobby.close()


def _run_native_ppo_identity_replay(
    seed: int, decisions: int = 40, monkeypatch=None,
    disable_legacy_strategy_projection: bool = False,
):
    torch.manual_seed(seed)
    if disable_legacy_strategy_projection:
        if monkeypatch is None:
            raise ValueError("monkeypatch is required to isolate legacy producer environment.")
        monkeypatch.setenv("TFT_DISABLE_LEGACY_STRATEGY_PROJECTION", "1")
    lobby = CppTFTLobbyWrapper(seed=seed)
    try:
        observations = lobby.reset(seed=seed)
        champion_id_map = lobby.get_champion_id_map()
        policy = TFTPolicy(
            obs_dim=int(observations.shape[-1]),
            action_dims=list(ACTION_DIMS),
            hidden_size=32,
            semantic_vocab_size=catalog_identity(champion_id_map)["vocab_size"],
            require_semantic_state=True,
        ).eval()
        trace = []
        seen_rounds = set()

        for _ in range(decisions):
            metadata = lobby.get_snapshot_metadata()
            native_snapshot = metadata.get("native_state_snapshot")
            assert isinstance(native_snapshot, Mapping)
            assert native_snapshot["contract_id"] == "tft.native-state-snapshot"
            assert native_snapshot["engine_instance_id"] == metadata["engine_instance_id"]
            assert native_snapshot["episode_id"] == metadata["episode_id"]
            assert native_snapshot["snapshot_sequence"] == metadata["decision_sequence"]
            assert native_snapshot["player_decision_sequences"] == metadata["player_decision_sequences"]

            mask_rows = lobby.get_action_masks()
            masks = {
                name: torch.as_tensor(
                    np.stack([row[name] for row in mask_rows]),
                    dtype=torch.bool,
                )
                for name in MASK_SHAPES
            }
            obs_tensor = torch.as_tensor(observations, dtype=torch.float32)
            observation_hashes = Trainer._hash_observation_rows(obs_tensor)
            mask_hashes = hash_mask_rows(masks)
            semantic_rows = []
            for player_id, native_player in enumerate(native_snapshot["players"]):
                semantic_rows.append({
                    "engine_instance_id": metadata["engine_instance_id"],
                    "episode_id": metadata["episode_id"],
                    "decision_sequence": metadata["decision_sequence"],
                    "player_decision_sequence": metadata["player_decision_sequences"][player_id],
                    "player_id": player_id,
                    "lobby_index": 0,
                    "stage": native_snapshot["stage"],
                    "round": native_snapshot["round"],
                    "native_state_contract_id": native_snapshot["contract_id"],
                    "native_state_contract_version": native_snapshot["contract_version"],
                    "native_state_producer": native_snapshot["producer"],
                    "native_state_source_namespace": native_snapshot["source_namespace"],
                    "native_player_state": native_player,
                })
            semantic_batch = build_semantic_batch(semantic_rows, champion_id_map)
            semantic_numeric = torch.as_tensor(semantic_batch["numeric"], dtype=torch.float32)
            semantic_state = {
                "numeric": semantic_numeric,
                "items": semantic_item_state_tensors(semantic_numeric),
                "champion_ids": torch.as_tensor(semantic_batch["champion_ids"], dtype=torch.long),
            }

            with torch.inference_mode():
                actions, logprobs, entropy, values = policy.get_action_and_value(
                    obs_tensor, masks=masks, deterministic=True,
                    semantic_state=semantic_state,
                )
                replay_logprobs, replay_entropy, replay_values = policy.evaluate_actions(
                    obs_tensor, actions, masks, semantic_state=semantic_state,
                )
                bootstrap_values = policy.get_value(
                    obs_tensor, masks=masks, semantic_state=semantic_state,
                )
            torch.testing.assert_close(replay_logprobs, logprobs)
            torch.testing.assert_close(replay_entropy, entropy)
            torch.testing.assert_close(replay_values, values)
            torch.testing.assert_close(bootstrap_values, values)
            action_rows = actions.cpu().numpy().astype(np.int64).tolist()
            for player_id, action in enumerate(action_rows):
                assert bool(masks["type_mask"][player_id, action[0]])
            assert torch.isfinite(logprobs).all()
            assert torch.isfinite(entropy).all()
            assert torch.isfinite(values).all()

            next_observations, rewards, lobby_done, info = lobby.step(action_rows)
            result_metadata = info["decision_snapshot"]
            assert result_metadata["decision_sequence"] == metadata["decision_sequence"] + 1
            assert result_metadata["episode_id"] == metadata["episode_id"]
            assert result_metadata["player_decision_sequences"] == [
                value + 1 for value in metadata["player_decision_sequences"]
            ]
            assert result_metadata["native_state_snapshot"]["snapshot_sequence"] == result_metadata["decision_sequence"]
            assert np.isfinite(rewards).all()

            seen_rounds.add(int(result_metadata["round"]))
            # Semantic projection hashes intentionally bind Engine/episode/player identity.
            # Compare the projected tensor content here because each replay owns a distinct
            # Engine instance; identity-bound hashes are validated within each replay above.
            semantic_content = tuple(
                (tuple(numeric), tuple(champion_ids))
                for numeric, champion_ids in zip(
                    semantic_batch["numeric"], semantic_batch["champion_ids"]
                )
            )
            trace.append((
                tuple(observation_hashes),
                tuple(mask_hashes),
                semantic_content,
                tuple(tuple(action) for action in action_rows),
            ))
            observations = next_observations
            if lobby_done:
                break

        assert len(seen_rounds) >= 3, (
            f"Replay não atravessou rounds suficientes: {sorted(seen_rounds)}"
        )
        return trace, sorted(seen_rounds)
    finally:
        lobby.close()


def test_native_multi_round_ppo_replay_is_deterministic_and_binds_observation_to_masks():
    first_trace, first_rounds = _run_native_ppo_identity_replay(seed=20261118)
    second_trace, second_rounds = _run_native_ppo_identity_replay(seed=20261118)

    assert first_rounds == second_rounds
    assert first_trace == second_trace


def test_native_multi_round_ppo_replay_survives_without_legacy_strategy_projection(monkeypatch):
    trace, rounds = _run_native_ppo_identity_replay(
        seed=20261118,
        decisions=40,
        monkeypatch=monkeypatch,
        disable_legacy_strategy_projection=True,
    )

    assert len(rounds) >= 3
    assert trace
