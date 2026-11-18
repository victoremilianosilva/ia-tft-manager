"""Versioned semantic projection of the native AuditSnapshot player facts.

This projection deliberately excludes StrategyInfo, Shadow recommendations,
confidence, evaluator scores and legacy observation offsets. Unknown catalog
bindings remain explicit through the per-slot champion-valid feature.
"""
from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Mapping, Sequence

SEMANTIC_STATE_CONTRACT_ID = "tft.ppo.semantic-native-state.v1"
SEMANTIC_STATE_CONTRACT_VERSION = 1
SEMANTIC_ENTITY_SLOTS = 28 + 9 + 5
SEMANTIC_ENTITY_FEATURES = 6
SEMANTIC_GLOBAL_FEATURES = 17
SEMANTIC_NUMERIC_DIM = (
    SEMANTIC_GLOBAL_FEATURES
    + SEMANTIC_ENTITY_SLOTS * SEMANTIC_ENTITY_FEATURES
)
SEMANTIC_ID_EMBED_DIM = 16


def _finite_number(value, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"native semantic field {field} must be numeric")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"native semantic field {field} must be finite")
    return result


def _non_negative_int(value, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"native semantic field {field} must be a non-negative integer")
    return value


def catalog_identity(catalog_map: Mapping[str, int]) -> dict:
    if not isinstance(catalog_map, Mapping) or not catalog_map:
        raise ValueError("champion catalog map must be a non-empty mapping")
    normalized = {}
    for name, internal_id in catalog_map.items():
        if not isinstance(name, str) or not name:
            raise ValueError("champion catalog keys must be non-empty strings")
        if isinstance(internal_id, bool) or not isinstance(internal_id, int) or internal_id < 0:
            raise ValueError(f"invalid internal champion id for {name!r}")
        if internal_id in normalized.values():
            raise ValueError(f"duplicate internal champion id: {internal_id}")
        normalized[name] = internal_id
    canonical = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return {
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "vocab_size": max(normalized.values()) + 2,
    }


def build_semantic_state_checkpoint_contract(catalog_map: Mapping[str, int]) -> dict:
    identity = catalog_identity(catalog_map)
    payload = {
        "contract_id": SEMANTIC_STATE_CONTRACT_ID,
        "version": SEMANTIC_STATE_CONTRACT_VERSION,
        "source": {
            "contract_id": "tft.native-state-snapshot",
            "contract_version": 3,
            "producer": "TFTEngine::get_audit_snapshot",
            "source_namespace": "tft.engine.observation-snapshot",
        },
        "catalog": identity,
        "global_features": [
            "hp/100", "damage_taken/100", "alive", "wins/100", "losses/100",
            "gold/200", "level/10", "xp/10", "win_streak/10", "loss_streak/10",
            "gold_before_interest/200", "interest_if_resolved_now/5",
            "placement/8", "placement_valid", "opponent_present",
            "stage/7", "round/50",
        ],
        "entity_slots": {
            "order": ["board[0:28]", "bench[0:9]", "shop[0:5]"],
            "features": [
                "occupied", "star/3", "cost/5", "item_count/9",
                "trait_count/10", "champion_id_valid",
            ],
            "champion_id": "catalog_internal_id_plus_one; zero=unknown_or_empty",
        },
        "numeric_dimension": SEMANTIC_NUMERIC_DIM,
        "entity_slot_count": SEMANTIC_ENTITY_SLOTS,
        "id_embedding_dimension": SEMANTIC_ID_EMBED_DIM,
        "encoder": {
            "kind": "champion_embedding_plus_mlp",
            "numeric_plus_embedding_input_dim": (
                SEMANTIC_NUMERIC_DIM + SEMANTIC_ENTITY_SLOTS * SEMANTIC_ID_EMBED_DIM
            ),
            "hidden_dim": 256,
            "output_dim": "policy_hidden_size",
            "fusion": "additive_to_shared_actor_critic_latent",
            "final_layer_initialization": "zero",
        },
        "critic_action_mask_input": "separate_independent_side_input",
        "missing_policy": "preserve validity; never synthesize a champion identity",
        "excluded": [
            "legacy_strategy_id", "legacy_strategy_one_hot", "legacy_composition_direction",
            "shadow_recommendation", "shadow_score", "shadow_confidence",
            "unverified_action_candidates", "legacy_flat_observation_offsets",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return {
        "manifest_version": 1,
        "contract": payload,
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    }


def validate_semantic_state_checkpoint_contract(manifest: Mapping, catalog_map: Mapping[str, int]) -> None:
    expected = build_semantic_state_checkpoint_contract(catalog_map)
    if not isinstance(manifest, Mapping) or dict(manifest) != expected:
        raise ValueError("semantic_state_contract is incompatible with the native source/catalog projection")


def project_native_player_state(metadata: Mapping, catalog_map: Mapping[str, int]) -> dict:
    if not isinstance(metadata, Mapping):
        raise TypeError("semantic projection metadata must be a mapping")
    state = metadata.get("native_player_state")
    if not isinstance(state, Mapping):
        raise ValueError("native_player_state is required for semantic PPO projection")
    player_id = _non_negative_int(metadata.get("player_id"), "metadata.player_id")
    if state.get("player_id") != player_id:
        raise ValueError("native player state does not match rollout player identity")
    if not isinstance(metadata.get("engine_instance_id"), str) or not metadata["engine_instance_id"]:
        raise ValueError("semantic projection requires Engine identity")
    for field in ("episode_id", "decision_sequence", "player_decision_sequence", "lobby_index"):
        _non_negative_int(metadata.get(field), f"metadata.{field}")
    if metadata.get("native_state_contract_id") != "tft.native-state-snapshot" or metadata.get("native_state_contract_version") != 3:
        raise ValueError("unsupported native state snapshot contract")
    if metadata.get("native_state_producer") != "TFTEngine::get_audit_snapshot":
        raise ValueError("unexpected native state producer")
    if metadata.get("native_state_source_namespace") != "tft.engine.observation-snapshot":
        raise ValueError("unexpected native state source namespace")

    placement = state.get("placement")
    if placement is not None:
        placement = _non_negative_int(placement, "placement")
    opponent_id = state.get("opponent_id")
    if opponent_id is not None:
        _non_negative_int(opponent_id, "opponent_id")

    global_values = [
        _finite_number(state.get("hp"), "hp") / 100.0,
        _finite_number(state.get("damage_taken"), "damage_taken") / 100.0,
        float(bool(state.get("alive"))),
        _non_negative_int(state.get("wins"), "wins") / 100.0,
        _non_negative_int(state.get("losses"), "losses") / 100.0,
        _non_negative_int(state.get("gold"), "gold") / 200.0,
        _non_negative_int(state.get("level"), "level") / 10.0,
        _non_negative_int(state.get("xp"), "xp") / 10.0,
        _non_negative_int(state.get("win_streak"), "win_streak") / 10.0,
        _non_negative_int(state.get("loss_streak"), "loss_streak") / 10.0,
        _non_negative_int(state.get("gold_before_interest"), "gold_before_interest") / 200.0,
        _non_negative_int(state.get("interest_if_resolved_now"), "interest_if_resolved_now") / 5.0,
        0.0 if placement is None else placement / 8.0,
        float(placement is not None),
        float(opponent_id is not None),
        _non_negative_int(metadata.get("stage"), "stage") / 7.0,
        _non_negative_int(metadata.get("round"), "round") / 50.0,
    ]

    catalog = dict(catalog_map)
    numeric = list(global_values)
    champion_ids = []
    for group_name, expected_count in (("board", 28), ("bench", 9), ("shop", 5)):
        entities = state.get(group_name)
        if not isinstance(entities, Sequence) or isinstance(entities, (str, bytes)) or len(entities) != expected_count:
            raise ValueError(f"native {group_name} must contain exactly {expected_count} stable slots")
        for slot, entity in enumerate(entities):
            if not isinstance(entity, Mapping):
                raise TypeError(f"native {group_name}[{slot}] must be an object")
            occupied = entity.get("occupied")
            if not isinstance(occupied, bool):
                raise TypeError(f"native {group_name}[{slot}].occupied must be boolean")
            if not occupied:
                numeric.extend([0.0] * SEMANTIC_ENTITY_FEATURES)
                champion_ids.append(0)
                continue
            champion_name = entity.get("champion_id")
            star = _non_negative_int(entity.get("star"), f"{group_name}[{slot}].star")
            cost = _non_negative_int(entity.get("cost"), f"{group_name}[{slot}].cost")
            items = entity.get("items")
            traits = entity.get("trait_names")
            if not isinstance(champion_name, str) or not champion_name:
                raise ValueError(f"occupied {group_name}[{slot}] has no champion identity")
            if not 1 <= star <= 3 or not 1 <= cost <= 5:
                raise ValueError(f"occupied {group_name}[{slot}] has invalid star/cost")
            if not isinstance(items, list) or not isinstance(traits, list):
                raise TypeError(f"occupied {group_name}[{slot}] requires items and trait_names lists")
            internal_id = catalog.get(champion_name)
            champion_valid = internal_id is not None
            numeric.extend([
                1.0,
                star / 3.0,
                cost / 5.0,
                min(len(items), 9) / 9.0,
                min(len(traits), 10) / 10.0,
                float(champion_valid),
            ])
            champion_ids.append(0 if internal_id is None else int(internal_id) + 1)

    if len(numeric) != SEMANTIC_NUMERIC_DIM or len(champion_ids) != SEMANTIC_ENTITY_SLOTS:
        raise RuntimeError("semantic projection produced an invalid tensor layout")
    if not all(math.isfinite(value) for value in numeric):
        raise ValueError("semantic projection contains a non-finite value")

    identity = {
        "engine_instance_id": metadata["engine_instance_id"],
        "episode_id": metadata["episode_id"],
        "decision_sequence": metadata["decision_sequence"],
        "player_decision_sequence": metadata["player_decision_sequence"],
        "player_id": player_id,
        "lobby_index": metadata["lobby_index"],
    }
    digest = hashlib.sha256(
        json.dumps(
            {"identity": identity, "numeric": numeric, "champion_ids": champion_ids},
            sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        ).encode("utf-8")
    ).hexdigest()
    return {
        "numeric": numeric,
        "champion_ids": champion_ids,
        "identity": identity,
        "sha256": digest,
    }


def build_semantic_batch(metadata_rows, catalog_map: Mapping[str, int]):
    projected = [project_native_player_state(row, catalog_map) for row in metadata_rows]
    return {
        "numeric": [row["numeric"] for row in projected],
        "champion_ids": [row["champion_ids"] for row in projected],
        "hashes": [row["sha256"] for row in projected],
        "identities": [row["identity"] for row in projected],
    }
