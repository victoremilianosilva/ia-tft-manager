"""Versioned semantic projection of the native AuditSnapshot player facts.

This projection deliberately excludes StrategyInfo, recommendation and evaluator metadata,
confidence, and legacy observation offsets. Unknown catalog
bindings remain explicit through the per-slot champion-valid feature.
"""
from __future__ import annotations

import hashlib
import json
import math

import numpy as np
from collections.abc import Mapping, Sequence

SEMANTIC_STATE_CONTRACT_ID = "tft.ppo.semantic-native-state.v8"
SEMANTIC_STATE_CONTRACT_VERSION = 8
SEMANTIC_ENTITY_SLOTS = 28 + 9 + 5
SEMANTIC_ENTITY_FEATURES = 45
SEMANTIC_GLOBAL_FEATURES = 70
SEMANTIC_ITEM_COMPONENT_FEATURES = 10
SEMANTIC_ITEM_SEMANTIC_FEATURES = 17
SEMANTIC_ITEM_TARGETS = 37
SEMANTIC_ANVIL_OPTIONS = 9
SEMANTIC_ANVIL_OPTION_FEATURES = 11
SEMANTIC_ENTITY_OFFSET = SEMANTIC_GLOBAL_FEATURES
SEMANTIC_ITEM_OFFSET = (
    SEMANTIC_GLOBAL_FEATURES + SEMANTIC_ENTITY_SLOTS * SEMANTIC_ENTITY_FEATURES
)
SEMANTIC_ITEM_STATE_DIM = (
    SEMANTIC_ITEM_COMPONENT_FEATURES
    + 9 * SEMANTIC_ITEM_SEMANTIC_FEATURES
    + 100 * SEMANTIC_ITEM_SEMANTIC_FEATURES
    + 9 * SEMANTIC_ITEM_TARGETS
    + 100 * SEMANTIC_ITEM_TARGETS
    + 3
    + SEMANTIC_ANVIL_OPTIONS * SEMANTIC_ANVIL_OPTION_FEATURES
)
SEMANTIC_NUMERIC_DIM = SEMANTIC_ITEM_OFFSET + SEMANTIC_ITEM_STATE_DIM
SEMANTIC_ID_EMBED_DIM = 16
SEMANTIC_TRAIT_SLOTS = 10
SEMANTIC_TRAIT_VOCAB_SIZE = 65536
SEMANTIC_TRAIT_EMBED_DIM = 16

SEMANTIC_POLICY_STATE_KEYS = frozenset({
    "semantic_id_embedding.weight",
    "semantic_trait_embedding.weight",
    "semantic_encoder.0.weight",
    "semantic_encoder.0.bias",
    "semantic_encoder.2.weight",
    "semantic_encoder.2.bias",
})


def semantic_policy_state_keys(state_dict: Mapping) -> set[str]:
    """Return every semantic-policy parameter present in a checkpoint state dict."""
    if not isinstance(state_dict, Mapping):
        raise TypeError("policy state_dict must be a mapping")
    prefixes = ("semantic_id_embedding.", "semantic_trait_embedding.", "semantic_encoder.")
    return {key for key in state_dict if isinstance(key, str) and key.startswith(prefixes)}


def validate_semantic_policy_state_dict(state_dict: Mapping) -> None:
    """Require the complete v8 semantic encoder parameter set."""
    present = semantic_policy_state_keys(state_dict)
    if present != SEMANTIC_POLICY_STATE_KEYS:
        missing = sorted(SEMANTIC_POLICY_STATE_KEYS - present)
        unexpected = sorted(present - SEMANTIC_POLICY_STATE_KEYS)
        raise ValueError(
            "Semantic v8 policy weights are incomplete: "
            f"missing={missing}, unexpected={unexpected}"
        )


def semantic_item_state_tensors(numeric):
    """Expose named item/anvil tensors from the identity-bound semantic row."""
    if not isinstance(numeric, __import__("torch").Tensor):
        raise TypeError("semantic numeric input must be a torch tensor")
    if numeric.ndim != 2 or numeric.shape[-1] != SEMANTIC_NUMERIC_DIM:
        raise ValueError("semantic numeric input has an incompatible v8 shape")
    import torch
    batch = numeric.shape[0]
    offset = SEMANTIC_ITEM_OFFSET
    components = numeric[:, offset:offset + SEMANTIC_ITEM_COMPONENT_FEATURES]
    offset += SEMANTIC_ITEM_COMPONENT_FEATURES
    inventory = numeric[:, offset:offset + 9 * SEMANTIC_ITEM_SEMANTIC_FEATURES].reshape(
        batch, 9, SEMANTIC_ITEM_SEMANTIC_FEATURES
    )
    offset += 9 * SEMANTIC_ITEM_SEMANTIC_FEATURES
    recipes = numeric[:, offset:offset + 100 * SEMANTIC_ITEM_SEMANTIC_FEATURES].reshape(
        batch, 100, SEMANTIC_ITEM_SEMANTIC_FEATURES
    )
    offset += 100 * SEMANTIC_ITEM_SEMANTIC_FEATURES
    inventory_fit = numeric[:, offset:offset + 9 * SEMANTIC_ITEM_TARGETS].reshape(
        batch, 9, SEMANTIC_ITEM_TARGETS
    )
    offset += 9 * SEMANTIC_ITEM_TARGETS
    recipe_fit = numeric[:, offset:offset + 100 * SEMANTIC_ITEM_TARGETS].reshape(
        batch, 100, SEMANTIC_ITEM_TARGETS
    )
    offset += 100 * SEMANTIC_ITEM_TARGETS
    anvil_state = numeric[:, offset:offset + 3]
    offset += 3
    anvil_options = numeric[:, offset:].reshape(
        batch, SEMANTIC_ANVIL_OPTIONS, SEMANTIC_ANVIL_OPTION_FEATURES
    )
    entity_numeric = numeric[:, SEMANTIC_ENTITY_OFFSET:SEMANTIC_ITEM_OFFSET].reshape(
        batch, SEMANTIC_ENTITY_SLOTS, SEMANTIC_ENTITY_FEATURES
    )
    raw_trait_ids = (
        entity_numeric[:, :, 29:29 + SEMANTIC_TRAIT_SLOTS]
        * SEMANTIC_TRAIT_VOCAB_SIZE
    )
    if (
        not torch.isfinite(raw_trait_ids).all()
        or (raw_trait_ids < 0).any()
        or (raw_trait_ids > SEMANTIC_TRAIT_VOCAB_SIZE).any()
        or not torch.allclose(raw_trait_ids, raw_trait_ids.round(), atol=1e-4, rtol=0.0)
    ):
        raise ValueError("semantic trait hash IDs are outside the canonical integer vocabulary")
    trait_ids = raw_trait_ids.round().long()
    return {
        "trait_ids": trait_ids,
        "components": components,
        "inventory": inventory,
        "recipes": recipes,
        "inventory_target_fit": inventory_fit,
        "recipe_target_fit": recipe_fit,
        "anvil_pending": anvil_state[:, 0] > 0.5,
        "anvil_component": anvil_state[:, 1] > 0.5,
        "anvil_completed_item": anvil_state[:, 2] > 0.5,
        "anvil_kind_features": anvil_state[:, 1:3],
        "anvil_options": anvil_options,
    }


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
            "contract_version": 6,
            "producer": "TFTEngine::get_audit_snapshot",
            "source_namespace": "tft.engine.observation-snapshot",
        },
        "strategic_owner_source": {
            "contract_id": "tft.strategic-owner-observation",
            "contract_version": 3,
            "producer": "TFTEngine::get_audit_snapshot",
            "source_namespace": "tft.engine.strategic-owners",
            "identity": ["episode_id", "player_id", "round", "player_decision_sequence"],
        },
        "catalog": identity,
        "global_features": [
            "hp/100", "damage_taken/100", "alive", "wins/100", "losses/100",
            "gold/200", "level/10", "xp/10", "win_streak/10", "loss_streak/10",
            "gold_before_interest/200", "interest_if_resolved_now/5",
            "placement/8", "placement_valid", "opponent_present",
            "stage/7", "round/50", "active_composition_valid",
            "direction_valid", "pivot_candidate_valid", "opportunity_cost_available",
            "board_capacity/9", "bench_capacity/9", "actions_taken_this_round/10",
            "board_move_age[0:28]/10", "planner_outputs_valid", "strategic_refresh_failed",
            "board_quality_score", "board_positional_score", "board_structural_score",
            "board_exposed_carries/9", "board_frontline_count/9",
            "board_isolated_frontline_count/9", "board_important_bench_units_unplayed/9",
            "board_frontline_lane_count/7", "board_exposed_main_carries/9",
            "board_fragile_frontline_count/9", "board_missing_frontline_count/9",
            "board_missing_backline_count/9", "board_active_trait_count/28",
            "board_strategic_fit_score", "board_unit_quality_score",
            "board_trait_coherence_score",
        ],
        "entity_slots": {
            "order": ["board[0:28]", "bench[0:9]", "shop[0:5]"],
            "features": [
                "occupied", "star/3", "cost/5", "item_count/9",
                "static_trait_count/10", "champion_id_valid",
                "active_composition_member", "active_composition_core_member",
                "direction_reference_member", "pivot_reference_member",
                "owned_copy_equivalent/9", "same_star_upgrade_progress/3",
                "item_target.occupied", "item_target.on_board", "item_target.on_bench",
                "item_target.star/3", "item_target.role_one_hot[0:5]",
                "item_target.frontline", "item_target.backline",
                "item_target.attack_damage/200", "item_target.attack_speed/2",
                "item_target.max_health/2000", "item_target.armor/150",
                "item_target.magic_resist/150", "item_target.equipped_item_count/3",
                "trait_id_hash_bucket[0:10]/65536", "strategic_priority/100", "strategic_intent/6", "lineup_selected", "lineup_target", "opportunity_cost/100", "opportunity_cost_available",
            ],
            "champion_id": "catalog_internal_id_plus_one; zero=unknown_or_empty",
        },
        "item_state": {
            "source": "AuditPlayerSnapshot native ItemEngine/catalog projection",
            "blocks": {
                "components": [10],
                "inventory": [9, 17],
                "recipes": [100, 17],
                "inventory_target_fit": [9, 37],
                "recipe_target_fit": [100, 37],
                "anvil_state": [3],
                "anvil_options": [9, 11],
            },
            "identity_bound_fields": [
                "item_components", "item_inventory", "equipped_items",
                "item_component_catalog", "item_catalog_sha256", "pending_anvil_sequence",
                "pending_anvil_kind", "pending_anvil_options",
            ],
        },
        "numeric_dimension": SEMANTIC_NUMERIC_DIM,
        "entity_slot_count": SEMANTIC_ENTITY_SLOTS,
        "id_embedding_dimension": SEMANTIC_ID_EMBED_DIM,
        "trait_embedding": {
            "kind": "stable_sha256_bucket_embedding",
            "vocabulary_buckets": SEMANTIC_TRAIT_VOCAB_SIZE,
            "slots_per_entity": SEMANTIC_TRAIT_SLOTS,
            "embedding_dimension": SEMANTIC_TRAIT_EMBED_DIM,
            "padding_id": 0,
        },
        "encoder": {
            "kind": "champion_and_trait_embedding_plus_mlp",
            "numeric_plus_embedding_input_dim": (
                SEMANTIC_ITEM_OFFSET
                + SEMANTIC_ENTITY_SLOTS * SEMANTIC_ID_EMBED_DIM
                + SEMANTIC_ENTITY_SLOTS * SEMANTIC_TRAIT_EMBED_DIM
            ),
            "hidden_dim": 256,
            "output_dim": "policy_hidden_size",
            "fusion": "semantic_global_mlp_plus_additive_to_shared_actor_critic_latent",
            "final_layer_initialization": "zero",
            "board_cnn_source": {
                "entity_range": "board[0:28]",
                "features": [
                    "occupied", "cost/5", "star/3",
                    "equipped_item_count/9", "trait_count/10",
                ],
                "spatial_order": "row_major_4x7",
            },
            "action_candidate_source": {
                "entity_ranges": ["bench[0:9]", "shop[0:5]"],
                "features": [
                    "occupied", "cost/5", "star/3", "trait_count/10",
                    "owned_copy_equivalent/9", "same_star_upgrade_progress/3",
                ],
            },
        },
        "critic_action_mask_input": "separate_independent_side_input",
        "missing_policy": "preserve validity; never synthesize a champion identity",
        "excluded": [
            "legacy_strategy_id", "legacy_strategy_one_hot", "legacy_composition_direction",
            "shadow_recommendation", "shadow_score", "shadow_confidence",
            "unverified_action_candidates", "legacy_flat_observation_offsets",
            "strategy_recommendations", "strategy_scores", "strategy_confidence",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return {
        "manifest_version": 1,
        "contract": payload,
        "sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
    }


def validate_semantic_state_checkpoint_integrity(manifest: Mapping) -> None:
    """Validate an old semantic manifest's own hash before an explicit warm-start."""
    if not isinstance(manifest, Mapping):
        raise TypeError("semantic_state_contract must be a mapping")
    if type(manifest.get("manifest_version")) is not int or manifest.get("manifest_version") != 1:
        raise ValueError("semantic_state_contract manifest version is unsupported")
    payload = manifest.get("contract")
    if not isinstance(payload, Mapping):
        raise TypeError("semantic_state_contract.contract must be a mapping")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    expected_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if manifest.get("sha256") != expected_hash:
        raise ValueError("semantic_state_contract hash is invalid")


def validate_semantic_state_warm_start_migration(
    manifest: Mapping, catalog_map: Mapping[str, int]
) -> None:
    """Allow only reviewed semantic v2/v6/v7-to-v8 and owner v1/v2-to-v3 warm-starts."""
    validate_semantic_state_checkpoint_integrity(manifest)
    expected = build_semantic_state_checkpoint_contract(catalog_map)
    historical_payload = manifest.get("contract")
    if not isinstance(historical_payload, Mapping):
        raise TypeError("semantic_state_contract.contract must be a mapping")
    historical_payload = dict(historical_payload)
    historical_owner_source = historical_payload.get("strategic_owner_source")
    if not isinstance(historical_owner_source, Mapping):
        raise ValueError("historical semantic contract has no strategic owner source")
    historical_owner_source = dict(historical_owner_source)
    if (
        historical_payload.get("contract_id") == "tft.ppo.semantic-native-state.v2"
        and historical_payload.get("version") == 2
        and historical_payload.get("source", {}).get("contract_version") == 3
        and historical_owner_source.get("contract_version") == 2
    ):
        # Reviewed v2 -> v8 migration: native snapshot v3 -> v6 adds capacity,
        # temporal facts, board/bench item-target profiles and structured item/anvil blocks. The semantic
        # entity stride expands while historical identity remains bound.
        historical_payload["contract_id"] = expected["contract"]["contract_id"]
        historical_payload["version"] = expected["contract"]["version"]
        historical_source = dict(historical_payload.get("source", {}))
        historical_source["contract_version"] = 6
        historical_payload["source"] = historical_source
        historical_payload["global_features"] = expected["contract"]["global_features"]
        historical_payload["numeric_dimension"] = expected["contract"]["numeric_dimension"]
        historical_encoder = dict(historical_payload.get("encoder", {}))
        historical_encoder["kind"] = "champion_and_trait_embedding_plus_mlp"
        historical_encoder["fusion"] = (
            "semantic_global_mlp_plus_additive_to_shared_actor_critic_latent"
        )
        historical_entity_slots = dict(historical_payload.get("entity_slots", {}))
        historical_entity_slots["features"] = expected["contract"]["entity_slots"]["features"]
        historical_payload["entity_slots"] = historical_entity_slots
        historical_payload["item_state"] = expected["contract"]["item_state"]
        historical_payload["trait_embedding"] = expected["contract"]["trait_embedding"]
        historical_encoder["numeric_plus_embedding_input_dim"] = (
            expected["contract"]["encoder"]["numeric_plus_embedding_input_dim"]
        )
        historical_encoder["board_cnn_source"] = (
            expected["contract"]["encoder"]["board_cnn_source"]
        )
        historical_encoder["action_candidate_source"] = (
            expected["contract"]["encoder"]["action_candidate_source"]
        )
        historical_payload["encoder"] = historical_encoder
        historical_owner_source["contract_version"] = (
            expected["contract"]["strategic_owner_source"]["contract_version"]
        )
        historical_payload["strategic_owner_source"] = historical_owner_source
    elif (
        historical_payload.get("contract_id") == "tft.ppo.semantic-native-state.v7"
        and historical_payload.get("version") == 7
        and historical_payload.get("source", {}).get("contract_version") == 5
        and historical_owner_source.get("contract_version") == 3
    ):
        # Reviewed v7 -> v8 migration: append native BoardEvaluation outputs
        # after the existing 54 global features; entity/item offsets move by 16.
        historical_payload["contract_id"] = expected["contract"]["contract_id"]
        historical_payload["version"] = expected["contract"]["version"]
        historical_source = dict(historical_payload.get("source", {}))
        historical_source["contract_version"] = expected["contract"]["source"]["contract_version"]
        historical_payload["source"] = historical_source
        historical_payload["global_features"] = expected["contract"]["global_features"]
        historical_payload["numeric_dimension"] = expected["contract"]["numeric_dimension"]
        historical_encoder = dict(historical_payload.get("encoder", {}))
        historical_encoder["numeric_plus_embedding_input_dim"] = (
            expected["contract"]["encoder"]["numeric_plus_embedding_input_dim"]
        )
        historical_payload["encoder"] = historical_encoder
    elif (
        historical_payload.get("contract_id") == "tft.ppo.semantic-native-state.v6"
        and historical_payload.get("version") == 6
        and historical_payload.get("source", {}).get("contract_version") == 5
        and historical_owner_source.get("contract_version") == 2
    ):
        # Reviewed v6 -> v8 migration: preserve the v6 encoder/checkpoint lineage
        # while adding v7 strategic context, v8 BoardEvaluation facts and owner v3.
        historical_payload["contract_id"] = expected["contract"]["contract_id"]
        historical_payload["version"] = expected["contract"]["version"]
        historical_owner_source["contract_version"] = (
            expected["contract"]["strategic_owner_source"]["contract_version"]
        )
        historical_payload["strategic_owner_source"] = historical_owner_source
        historical_source = dict(historical_payload.get("source", {}))
        historical_source["contract_version"] = expected["contract"]["source"]["contract_version"]
        historical_payload["source"] = historical_source
        historical_payload["global_features"] = expected["contract"]["global_features"]
        historical_payload["numeric_dimension"] = expected["contract"]["numeric_dimension"]
        historical_entity_slots = dict(historical_payload.get("entity_slots", {}))
        historical_entity_slots["features"] = expected["contract"]["entity_slots"]["features"]
        historical_payload["entity_slots"] = historical_entity_slots
        historical_encoder = dict(historical_payload.get("encoder", {}))
        historical_encoder["numeric_plus_embedding_input_dim"] = (
            expected["contract"]["encoder"]["numeric_plus_embedding_input_dim"]
        )
        historical_payload["encoder"] = historical_encoder
    elif historical_owner_source.get("contract_version") == 1:
        historical_owner_source["contract_version"] = (
            expected["contract"]["strategic_owner_source"]["contract_version"]
        )
        historical_payload["strategic_owner_source"] = historical_owner_source
    else:
        raise ValueError("semantic warm-start source contract is not an approved migration")

    if historical_payload != expected["contract"]:
        raise ValueError(
            "semantic warm-start requires the approved provenance/layout migration; "
            "catalog, normalization, and all other contract fields must match"
        )


def validate_semantic_state_checkpoint_contract(manifest: Mapping, catalog_map: Mapping[str, int]) -> None:
    validate_semantic_state_checkpoint_integrity(manifest)
    expected = build_semantic_state_checkpoint_contract(catalog_map)
    if dict(manifest) != expected:
        raise ValueError("semantic_state_contract is incompatible with the native source/catalog projection")



def _build_semantic_projection_context(catalog_map: Mapping[str, int]) -> dict:
    """Prepare catalog lookups and a batch-local stable trait hash cache."""
    catalog = dict(catalog_map)
    return {
        "catalog": catalog,
        "known_catalog_ids": frozenset(catalog.values()),
        "trait_hash_cache": {},
    }


def project_native_player_state(
    metadata: Mapping,
    catalog_map: Mapping[str, int],
    *,
    _projection_context: dict | None = None,
) -> dict:
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
    if metadata.get("native_state_contract_id") != "tft.native-state-snapshot" or metadata.get("native_state_contract_version") != 6:
        raise ValueError("unsupported native state snapshot contract")
    if metadata.get("native_state_producer") != "TFTEngine::get_audit_snapshot":
        raise ValueError("unexpected native state producer")
    if metadata.get("native_state_source_namespace") != "tft.engine.observation-snapshot":
        raise ValueError("unexpected native state source namespace")

    strategic = state.get("strategic_state")
    if not isinstance(strategic, Mapping):
        raise ValueError("native strategic owner snapshot is required for PPO projection")
    strategic_version = strategic.get("contract_version")
    if (
        strategic.get("contract_id") != "tft.strategic-owner-observation"
        or isinstance(strategic_version, bool)
        or not isinstance(strategic_version, int)
        or strategic_version != 3
        or strategic.get("producer") != "TFTEngine::get_audit_snapshot"
        or strategic.get("source_namespace") != "tft.engine.strategic-owners"
    ):
        raise ValueError("unsupported strategic owner snapshot contract")
    strategic_context_sequence = strategic.get("strategic_context_sequence")
    if (
        isinstance(strategic_context_sequence, bool)
        or not isinstance(strategic_context_sequence, int)
        or strategic_context_sequence < 0
    ):
        raise ValueError("invalid strategic owner strategic_context_sequence")

    for field, expected in (
        ("episode_id", metadata["episode_id"]),
        ("player_decision_sequence", metadata["player_decision_sequence"]),
        ("player_id", player_id),
        ("round", metadata["round"]),
    ):
        actual = strategic.get(field)
        if isinstance(actual, bool) or not isinstance(actual, int) or actual != expected:
            raise ValueError(f"strategic owner snapshot diverges in {field}")

    def _id_set(field):
        values = strategic.get(field)
        if not isinstance(values, list):
            raise TypeError(f"strategic owner field {field} must be a list")
        result = set()
        for value in values:
            result.add(_non_negative_int(value, f"strategic_state.{field}"))
        if len(result) != len(values):
            raise ValueError(f"strategic owner field {field} contains duplicate IDs")
        return result

    active_valid = strategic.get("active_composition_valid")
    direction_valid = strategic.get("direction_valid")
    pivot_valid = strategic.get("pivot_candidate_valid")
    opportunity_available = strategic.get("opportunity_cost_available")
    if not all(isinstance(value, bool) for value in (
        active_valid, direction_valid, pivot_valid, opportunity_available
    )):
        raise TypeError("strategic owner validity fields must be boolean")
    active_ids = _id_set("active_unit_ids")
    core_ids = _id_set("active_core_unit_ids")
    direction_ids = _id_set("direction_reference_unit_ids")
    pivot_ids = _id_set("pivot_reference_unit_ids")
    progress_rows = strategic.get("unit_copy_progress")
    if not isinstance(progress_rows, list):
        raise TypeError("strategic owner unit_copy_progress must be a list")
    copy_progress = {}
    for row in progress_rows:
        if not isinstance(row, Mapping):
            raise TypeError("unit_copy_progress rows must be objects")
        champion_id = _non_negative_int(row.get("champion_internal_id"), "unit_copy_progress.champion_internal_id")
        copies = _non_negative_int(row.get("owned_copy_equivalent"), "unit_copy_progress.owned_copy_equivalent")
        toward_next = _non_negative_int(row.get("copies_toward_next_star"), "unit_copy_progress.copies_toward_next_star")
        highest_star = _non_negative_int(row.get("highest_star"), "unit_copy_progress.highest_star")
        if champion_id in copy_progress:
            raise ValueError("unit_copy_progress contains duplicate champion IDs")
        if not 1 <= highest_star <= 3 or not 1 <= copies <= 9 or toward_next > 2:
            raise ValueError("unit_copy_progress values are outside native ranges")
        if highest_star == 3 and toward_next != 0:
            raise ValueError("three-star units cannot have progress toward another upgrade")
        copy_progress[champion_id] = {
            "owned_copy_equivalent": copies,
            "copies_toward_next_star": toward_next,
            "highest_star": highest_star,
        }
    if not core_ids.issubset(active_ids):
        raise ValueError("active core units must belong to the active composition")
    if not active_valid and (active_ids or core_ids):
        raise ValueError("invalid active composition cannot publish unit membership")
    if active_valid and (
        not isinstance(strategic.get("active_composition_id"), str)
        or not strategic["active_composition_id"]
        or _non_negative_int(strategic.get("active_composition_version"), "active_composition_version") == 0
    ):
        raise ValueError("active composition identity/version is incomplete")
    if not direction_valid and direction_ids:
        raise ValueError("invalid direction cannot publish reference units")
    if direction_valid and (
        not isinstance(strategic.get("direction_identity"), str)
        or not strategic["direction_identity"]
    ):
        raise ValueError("direction identity is incomplete")
    if not pivot_valid and pivot_ids:
        raise ValueError("invalid pivot cannot publish reference units")
    if pivot_valid and (
        not isinstance(strategic.get("pivot_candidate_identity"), str)
        or not strategic["pivot_candidate_identity"]
        or not isinstance(strategic.get("pivot_target_composition_identity"), str)
        or not strategic["pivot_target_composition_identity"]
        or _non_negative_int(strategic.get("pivot_source_composition_version"), "pivot_source_composition_version") == 0
    ):
        raise ValueError("pivot candidate identity/version is incomplete")
    opportunity_rows = strategic.get("opportunity_costs")
    if not isinstance(opportunity_rows, list):
        raise TypeError("strategic_state.opportunity_costs must be a list")
    opportunity_by_id = {}
    for row in opportunity_rows:
        if not isinstance(row, Mapping):
            raise TypeError("opportunity cost rows must be objects")
        champion_id = _non_negative_int(row.get("champion_internal_id"), "opportunity_cost.champion_internal_id")
        value = _finite_number(row.get("value"), "opportunity_cost.value")
        uncertainty = _finite_number(row.get("uncertainty"), "opportunity_cost.uncertainty")
        horizon = _non_negative_int(row.get("horizon_rounds"), "opportunity_cost.horizon_rounds")
        source = row.get("source")
        value_basis = row.get("value_basis")
        forgone = row.get("forgone_candidate_id")
        if (champion_id in opportunity_by_id or value < 0.0 or
            not 0.0 <= uncertainty < 1.0 or horizon == 0 or
            source != "same_snapshot_competing_alternative.v1" or
            value_basis not in ("contextual_action_score.v1", "native_board_contribution.v1") or
            not isinstance(forgone, str) or not forgone):
            raise ValueError("opportunity cost row has invalid or duplicate evidence")
        opportunity_by_id[champion_id] = (value, uncertainty)
    if opportunity_available != bool(opportunity_by_id):
        raise ValueError("opportunity_cost_available diverges from native opportunity rows")

    placement = state.get("placement")
    if placement is not None:
        placement = _non_negative_int(placement, "placement")
        if not 1 <= placement <= 8:
            raise ValueError("placement must be in the native lobby range 1..8")
    opponent_id = state.get("opponent_id")
    if opponent_id is not None:
        opponent_id = _non_negative_int(opponent_id, "opponent_id")
        if opponent_id >= 8 or opponent_id == player_id:
            raise ValueError("opponent_id must identify a different player in this lobby")
    alive = state.get("alive")
    if not isinstance(alive, bool):
        raise TypeError("native semantic field alive must be boolean")
    stage = _non_negative_int(metadata.get("stage"), "stage")
    round_number = _non_negative_int(metadata.get("round"), "round")
    if not 1 <= stage <= 7 or round_number > 50:
        raise ValueError("native stage/round is outside the supported lobby range")
    hp = _finite_number(state.get("hp"), "hp")
    damage_taken = _finite_number(state.get("damage_taken"), "damage_taken")
    if not 0.0 <= hp <= 100.0 or damage_taken < 0.0:
        raise ValueError("native HP/damage facts are outside their valid range")

    board_rows = state.get("board")
    bench_rows = state.get("bench")
    if (
        not isinstance(board_rows, Sequence) or isinstance(board_rows, (str, bytes))
        or len(board_rows) != 28
        or not isinstance(bench_rows, Sequence) or isinstance(bench_rows, (str, bytes))
        or len(bench_rows) != 9
    ):
        raise ValueError("native board/bench slots are required for capacity projection")
    board_count = sum(
        1 for row in board_rows
        if isinstance(row, Mapping) and row.get("occupied") is True
    )
    bench_count = sum(
        1 for row in bench_rows
        if isinstance(row, Mapping) and row.get("occupied") is True
    )
    action_count = _non_negative_int(
        state.get("actions_taken_this_round"), "actions_taken_this_round"
    )
    move_ages = state.get("board_move_age")
    if (
        not isinstance(move_ages, Sequence) or isinstance(move_ages, (str, bytes))
        or len(move_ages) != 28
    ):
        raise ValueError("native board_move_age must contain 28 slot-aligned values")
    move_age_values = [
        min(_non_negative_int(age, f"board_move_age[{index}]"), 10) / 10.0
        for index, age in enumerate(move_ages)
    ]

    board_quality_score = _finite_number(state.get("board_quality_score"), "board_quality_score")
    board_positional_score = _finite_number(state.get("board_positional_score"), "board_positional_score")
    board_structural_score = _finite_number(state.get("board_structural_score"), "board_structural_score")
    board_exposed_carries = _non_negative_int(state.get("board_exposed_carries"), "board_exposed_carries")
    board_frontline_count = _non_negative_int(state.get("board_frontline_count"), "board_frontline_count")
    board_isolated_frontline_count = _non_negative_int(
        state.get("board_isolated_frontline_count"), "board_isolated_frontline_count"
    )
    board_important_bench_units_unplayed = _non_negative_int(
        state.get("board_important_bench_units_unplayed"),
        "board_important_bench_units_unplayed",
    )
    board_frontline_lane_count = _non_negative_int(state.get("board_frontline_lane_count"), "board_frontline_lane_count")
    board_exposed_main_carries = _non_negative_int(state.get("board_exposed_main_carries"), "board_exposed_main_carries")
    board_fragile_frontline_count = _non_negative_int(state.get("board_fragile_frontline_count"), "board_fragile_frontline_count")
    board_missing_frontline_count = _non_negative_int(state.get("board_missing_frontline_count"), "board_missing_frontline_count")
    board_missing_backline_count = _non_negative_int(state.get("board_missing_backline_count"), "board_missing_backline_count")
    board_active_trait_count = _non_negative_int(state.get("board_active_trait_count"), "board_active_trait_count")
    board_strategic_fit_score = _finite_number(state.get("board_strategic_fit_score"), "board_strategic_fit_score")
    board_unit_quality_score = _finite_number(state.get("board_unit_quality_score"), "board_unit_quality_score")
    board_trait_coherence_score = _finite_number(state.get("board_trait_coherence_score"), "board_trait_coherence_score")
    if (
        board_exposed_carries > 28 or board_frontline_count > 28
        or board_isolated_frontline_count > 28
        or board_important_bench_units_unplayed > 9
        or board_frontline_lane_count > 7 or board_exposed_main_carries > 28
        or board_fragile_frontline_count > 28 or board_missing_frontline_count > 28
        or board_missing_backline_count > 28 or board_active_trait_count > 28
    ):
        raise ValueError("native board evaluation counts exceed their canonical slot limits")

    global_values = [
        hp / 100.0,
        damage_taken / 100.0,
        float(alive),
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
        stage / 7.0,
        round_number / 50.0,
        float(active_valid),
        float(direction_valid),
        float(pivot_valid),
        float(opportunity_available),
        min(max(_non_negative_int(state.get("level"), "level") - board_count, 0), 9) / 9.0,
        (9 - bench_count) / 9.0,
        min(action_count, 10) / 10.0,
        *move_age_values,
        float(strategic.get("planner_outputs_valid") is True),
        float(strategic.get("strategic_refresh_failed") is True),
        board_quality_score,
        board_positional_score,
        board_structural_score,
        board_exposed_carries / 9.0,
        board_frontline_count / 9.0,
        board_isolated_frontline_count / 9.0,
        board_important_bench_units_unplayed / 9.0,
        board_frontline_lane_count / 7.0,
        board_exposed_main_carries / 9.0,
        board_fragile_frontline_count / 9.0,
        board_missing_frontline_count / 9.0,
        board_missing_backline_count / 9.0,
        board_active_trait_count / 28.0,
        board_strategic_fit_score,
        board_unit_quality_score,
        board_trait_coherence_score,
    ]

    planner_valid = strategic.get("planner_outputs_valid")
    strategic_failed = strategic.get("strategic_refresh_failed")
    if not isinstance(planner_valid, bool) or not isinstance(strategic_failed, bool):
        raise TypeError("strategic planner/failure availability fields must be boolean")
    failure_reason = strategic.get("strategic_refresh_failure_reason")
    if not isinstance(failure_reason, str) or strategic_failed != bool(failure_reason):
        raise ValueError("strategic refresh failure flag/reason mismatch")
    planner_sequence = _non_negative_int(strategic.get("planner_output_sequence"), "planner_output_sequence")
    priority_rows = strategic.get("unit_priorities")
    selected_ids = strategic.get("lineup_selected_unit_ids")
    entry_ids = strategic.get("lineup_entry_unit_ids")
    exit_ids = strategic.get("lineup_exit_unit_ids")
    deferred_ids = strategic.get("lineup_deferred_unit_ids")
    for field, values in (("unit_priorities", priority_rows), ("lineup_selected_unit_ids", selected_ids),
                          ("lineup_entry_unit_ids", entry_ids), ("lineup_exit_unit_ids", exit_ids),
                          ("lineup_deferred_unit_ids", deferred_ids)):
        if not isinstance(values, list):
            raise TypeError(f"strategic_state.{field} must be a list")
    priority_by_id = {}
    if planner_valid:
        if planner_sequence != strategic_context_sequence:
            raise ValueError("planner outputs are not bound to the strategic context sequence")
        for row in priority_rows:
            if not isinstance(row, Mapping):
                raise TypeError("unit priority rows must be objects")
            champion_id = _non_negative_int(row.get("champion_internal_id"), "unit_priority.champion_internal_id")
            priority = _non_negative_int(row.get("priority"), "unit_priority.priority")
            intent = _non_negative_int(row.get("intent"), "unit_priority.intent")
            confidence = _finite_number(row.get("confidence"), "unit_priority.confidence")
            target_star = _non_negative_int(row.get("target_star"), "unit_priority.target_star")
            sale_restricted = row.get("sale_restricted")
            if champion_id in priority_by_id or intent > 6 or target_star > 3 or not 0.0 <= confidence <= 1.0 or not isinstance(sale_restricted, bool):
                raise ValueError("unit priority row has duplicate identity or invalid values")
            priority_by_id[champion_id] = (priority, intent, confidence, target_star, sale_restricted)
    elif priority_rows or selected_ids or entry_ids or exit_ids or deferred_ids:
        raise ValueError("unavailable planner outputs cannot publish priority or lineup rows")
    def validate_ids(field, values):
        result = set()
        for value in values:
            champion_id = _non_negative_int(value, f"strategic_state.{field}")
            if champion_id in result:
                raise ValueError(f"strategic_state.{field} contains duplicate IDs")
            result.add(champion_id)
        return result
    selected_set = validate_ids("lineup_selected_unit_ids", selected_ids)
    entry_set = validate_ids("lineup_entry_unit_ids", entry_ids)
    validate_ids("lineup_exit_unit_ids", exit_ids)
    deferred_set = validate_ids("lineup_deferred_unit_ids", deferred_ids)
    target_set = selected_set | entry_set | deferred_set

    projection_context = (
        _build_semantic_projection_context(catalog_map)
        if _projection_context is None else _projection_context
    )
    catalog = projection_context["catalog"]
    known_catalog_ids = projection_context["known_catalog_ids"]
    trait_hash_cache = projection_context["trait_hash_cache"]
    observed_owned_ids = set()
    for group_name in ("board", "bench"):
        for entity in state[group_name]:
            if isinstance(entity, Mapping) and entity.get("occupied") is True:
                champion_name = entity.get("champion_id")
                internal_id = catalog.get(champion_name)
                if internal_id is not None:
                    observed_owned_ids.add(int(internal_id))
                    if int(internal_id) not in copy_progress:
                        raise ValueError(
                            f"native UnitCopyProgress is missing owned champion {champion_name}"
                        )
    if not (set(copy_progress) & known_catalog_ids).issubset(observed_owned_ids):
        raise ValueError("native UnitCopyProgress contains known champions absent from board/bench")
    shop_offer_revisions = state.get("shop_offer_revisions")
    if (
        not isinstance(shop_offer_revisions, Sequence)
        or isinstance(shop_offer_revisions, (str, bytes))
        or len(shop_offer_revisions) != 5
    ):
        raise ValueError("native shop_offer_revisions must contain five slot-aligned values")
    shop_offer_revisions = [
        _non_negative_int(value, f"shop_offer_revisions[{slot}]")
        for slot, value in enumerate(shop_offer_revisions)
    ]

    numeric = list(global_values)
    champion_ids = []
    entity_identity = []
    observed_unit_uuids = set()
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
            unit_uuid = entity.get("uuid", "")
            if not isinstance(unit_uuid, str):
                raise TypeError(f"native {group_name}[{slot}].uuid must be a string")
            if occupied:
                if not unit_uuid:
                    raise ValueError(f"occupied {group_name}[{slot}] has no physical unit UUID")
                if unit_uuid in observed_unit_uuids:
                    raise ValueError("native player snapshot contains duplicate physical unit UUIDs")
                observed_unit_uuids.add(unit_uuid)
            elif unit_uuid:
                raise ValueError(f"empty {group_name}[{slot}] cannot retain a physical unit UUID")
            entity_identity.append({
                "location": group_name,
                "slot": slot,
                "occupied": occupied,
                "unit_uuid": unit_uuid,
                "shop_offer_revision": (
                    shop_offer_revisions[slot] if group_name == "shop" else None
                ),
            })
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
            if (
                not isinstance(items, list)
                or any(not isinstance(item, str) or not item for item in items)
                or not isinstance(traits, list)
                or any(not isinstance(trait, str) or not trait for trait in traits)
                or len(traits) != len(set(traits))
            ):
                raise TypeError(f"occupied {group_name}[{slot}] requires valid items and unique trait_names")
            internal_id = catalog.get(champion_name)
            champion_valid = internal_id is not None
            native_id = None if internal_id is None else int(internal_id)
            native_progress = copy_progress.get(native_id, {})
            copy_equivalent = native_progress.get("owned_copy_equivalent", 0)
            upgrade_progress = native_progress.get("copies_toward_next_star", 0) / 2.0
            numeric.extend([
                1.0,
                star / 3.0,
                cost / 5.0,
                min(len(items), 9) / 9.0,
                min(len(traits), 10) / 10.0,
                float(champion_valid),
                float(native_id in active_ids) if native_id is not None else 0.0,
                float(native_id in core_ids) if native_id is not None else 0.0,
                float(native_id in direction_ids) if native_id is not None else 0.0,
                float(native_id in pivot_ids) if native_id is not None else 0.0,
                min(copy_equivalent, 9) / 9.0,
                upgrade_progress,
            ])
            # Target profile is native catalog data, not reconstructed from the
            # flat item-target observation. Shop slots are not legal item targets.
            target_features = [0.0] * 17
            if group_name in ("board", "bench"):
                role = _non_negative_int(entity.get("role"), f"{group_name}[{slot}].role")
                if role > 4:
                    raise ValueError(f"{group_name}[{slot}] has invalid target role")
                attack_damage = _finite_number(entity.get("attack_damage"), f"{group_name}[{slot}].attack_damage")
                attack_speed = _finite_number(entity.get("attack_speed"), f"{group_name}[{slot}].attack_speed")
                max_health = _finite_number(entity.get("max_health"), f"{group_name}[{slot}].max_health")
                armor = _finite_number(entity.get("armor"), f"{group_name}[{slot}].armor")
                magic_resist = _finite_number(entity.get("magic_resist"), f"{group_name}[{slot}].magic_resist")
                if min(attack_damage, attack_speed, max_health, armor, magic_resist) < 0.0:
                    raise ValueError(f"{group_name}[{slot}] has negative target profile stats")
                on_board = group_name == "board"
                target_features[0] = 1.0
                target_features[1] = float(on_board)
                target_features[2] = float(not on_board)
                target_features[3] = star / 3.0
                target_features[4 + role] = 1.0
                target_features[9] = float(on_board and slot // 7 <= 1)
                target_features[10] = float(on_board and slot // 7 >= 2)
                target_features[11] = min(attack_damage / 200.0, 1.0)
                target_features[12] = min(attack_speed / 2.0, 1.0)
                target_features[13] = min(max_health / 2000.0, 1.0)
                target_features[14] = min(armor / 150.0, 1.0)
                target_features[15] = min(magic_resist / 150.0, 1.0)
                target_features[16] = min(len(items) / 3.0, 1.0)
            numeric.extend(target_features)
            if len(traits) > SEMANTIC_TRAIT_SLOTS:
                raise ValueError(f"{group_name}[{slot}] exceeds the native trait slot limit")
            trait_ids = []
            for trait in traits:
                trait_id = trait_hash_cache.get(trait)
                if trait_id is None:
                    trait_id = (
                        int.from_bytes(hashlib.sha256(trait.encode("utf-8")).digest()[:4], "big")
                        % SEMANTIC_TRAIT_VOCAB_SIZE + 1
                    )
                    trait_hash_cache[trait] = trait_id
                trait_ids.append(trait_id)
            numeric.extend(float(trait_id / SEMANTIC_TRAIT_VOCAB_SIZE) for trait_id in trait_ids)
            numeric.extend([0.0] * (SEMANTIC_TRAIT_SLOTS - len(trait_ids)))
            priority = priority_by_id.get(native_id, (0, 0, 0.0, 0, False)) if native_id is not None else (0, 0, 0.0, 0, False)
            opportunity = opportunity_by_id.get(native_id) if native_id is not None else None
            numeric.extend([
                min(priority[0], 100) / 100.0,
                priority[1] / 6.0,
                float(native_id in selected_set) if native_id is not None else 0.0,
                float(native_id in target_set) if native_id is not None else 0.0,
                min(opportunity[0], 100.0) / 100.0 if opportunity is not None else 0.0,
                float(opportunity is not None),
            ])
            champion_ids.append(0 if internal_id is None else int(internal_id) + 1)

    def read_feature_block(field, shape):
        value = state.get(field)
        if isinstance(value, np.ndarray):
            if (
                value.dtype != np.dtype(np.float32)
                or value.shape != shape
                or not value.flags.c_contiguous
                or value.flags.writeable
            ):
                raise ValueError(
                    f"native semantic item field {field} has invalid native view contract"
                )
            if not np.isfinite(value).all():
                raise ValueError(
                    f"native semantic item field {field} contains non-finite values"
                )
            if np.any(value < 0.0) or np.any(value > 1.0):
                raise ValueError(
                    f"native semantic item field {field} is outside [0, 1]"
                )
            # Convert only at the canonical v8 projection boundary. Python
            # float values preserve the float32 payload represented by the
            # previous list-backed pybind serialization, including hash order.
            return value.reshape(-1).tolist()

        # Dict-backed fixtures and external sequence producers retain the
        # recursive compatibility path; only native ndarray views are zero-copy.
        if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
            raise TypeError(f"native semantic item field {field} must be a sequence")
        flat = []

        def visit(node, depth=0):
            if depth == len(shape):
                flat.append(_finite_number(node, field))
                return
            if (
                not isinstance(node, Sequence) or isinstance(node, (str, bytes))
                or len(node) != shape[depth]
            ):
                raise ValueError(f"native semantic item field {field} has invalid shape")
            for child in node:
                visit(child, depth + 1)

        visit(value)
        if any(number < 0.0 or number > 1.0 for number in flat):
            raise ValueError(f"native semantic item field {field} is outside [0, 1]")
        return flat

    component_features = read_feature_block("item_component_features", (10,))
    inventory_features = read_feature_block("item_inventory_features", (9, 17))
    recipe_features = read_feature_block("item_recipe_features", (100, 17))
    inventory_target_fit = read_feature_block("item_inventory_target_fit", (9, 37))
    recipe_target_fit = read_feature_block("item_recipe_target_fit", (100, 37))
    anvil_option_features = read_feature_block("pending_anvil_option_features", (9, 11))

    pending_anvil = state.get("pending_anvil")
    pending_sequence = _non_negative_int(
        state.get("pending_anvil_sequence"), "pending_anvil_sequence"
    )
    pending_kind = state.get("pending_anvil_kind")
    pending_options = state.get("pending_anvil_options")
    if not isinstance(pending_anvil, bool):
        raise TypeError("native pending_anvil must be boolean")
    if isinstance(pending_kind, bool) or not isinstance(pending_kind, int):
        raise TypeError("native pending_anvil_kind must be an integer")
    if not isinstance(pending_options, list) or any(
        not isinstance(option, str) or not option for option in pending_options
    ):
        raise TypeError("native pending_anvil_options must be non-empty string IDs")
    if pending_anvil:
        if pending_sequence <= 0 or pending_kind not in (0, 1) or not pending_options:
            raise ValueError("pending anvil lacks a valid sequence, kind or options")
    elif pending_sequence != 0 or pending_kind != -1 or pending_options:
        raise ValueError("non-pending anvil must not publish sequence, kind or options")

    item_components = state.get("item_components")
    item_inventory = state.get("item_inventory")
    item_component_catalog = state.get("item_component_catalog")
    equipped_items = state.get("equipped_items")
    for field, values in (
        ("item_components", item_components),
        ("item_inventory", item_inventory),
        ("item_component_catalog", item_component_catalog),
    ):
        if not isinstance(values, list) or any(not isinstance(value, str) or not value for value in values):
            raise TypeError(f"native {field} must contain non-empty string IDs")
    if not isinstance(equipped_items, list) or any(not isinstance(row, Mapping) for row in equipped_items):
        raise TypeError("native equipped_items must be a list of structured ownership rows")
    if len(item_component_catalog) != 10 or len(set(item_component_catalog)) != 10:
        raise ValueError("native item component catalog must contain ten unique ordered IDs")
    if pending_anvil and pending_kind == 0 and any(
        option not in item_component_catalog for option in pending_options
    ):
        raise ValueError("component anvil option is absent from the native component catalog")
    if len(item_inventory) > 9 or len(pending_options) > 9:
        raise ValueError("native item inventory/anvil options exceed their canonical slot counts")

    item_catalog_sha256 = hashlib.sha256(json.dumps(
        {
            "component_ids": item_component_catalog,
            "recipe_features": recipe_features,
        },
        sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    ).encode("utf-8")).hexdigest()

    numeric.extend(component_features)
    numeric.extend(inventory_features)
    numeric.extend(recipe_features)
    numeric.extend(inventory_target_fit)
    numeric.extend(recipe_target_fit)
    numeric.extend([
        float(pending_anvil),
        float(pending_anvil and pending_kind == 0),
        float(pending_anvil and pending_kind == 1),
    ])
    numeric.extend(anvil_option_features)

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
        "round": round_number,
        "lobby_index": metadata["lobby_index"],
    }
    digest = hashlib.sha256(
        json.dumps(
            {
                "identity": identity,
                "numeric": numeric,
                "champion_ids": champion_ids,
                "item_state_identity": {
                    "item_components": item_components,
                    "item_inventory": item_inventory,
                    "equipped_items": equipped_items,
                    "item_component_catalog": item_component_catalog,
                    "item_catalog_sha256": item_catalog_sha256,
                    "pending_anvil": pending_anvil,
                    "pending_anvil_sequence": pending_sequence,
                    "pending_anvil_kind": pending_kind,
                    "pending_anvil_options": pending_options,
                },
                "strategic_owner_provenance": {
                    "contract_id": strategic.get("contract_id"),
                    "contract_version": strategic.get("contract_version"),
                    "strategic_context_sequence": strategic_context_sequence,
                    "active_composition_id": strategic.get("active_composition_id"),
                    "active_composition_version": strategic.get("active_composition_version"),
                    "direction_identity": strategic.get("direction_identity"),
                    "pivot_candidate_identity": strategic.get("pivot_candidate_identity"),
                    "pivot_target_composition_identity": strategic.get("pivot_target_composition_identity"),
                    "pivot_source_composition_version": strategic.get("pivot_source_composition_version"),
                    "active_composition_valid": active_valid,
                    "direction_valid": direction_valid,
                    "pivot_candidate_valid": pivot_valid,
                    "opportunity_cost_available": opportunity_available,
                    "planner_outputs_valid": planner_valid,
                    "planner_output_sequence": planner_sequence,
                    "unit_priorities": priority_rows,
                    "lineup_selected_unit_ids": selected_ids,
                    "lineup_entry_unit_ids": entry_ids,
                    "lineup_exit_unit_ids": exit_ids,
                    "lineup_deferred_unit_ids": deferred_ids,
                    "opportunity_costs": opportunity_rows,
                    "strategic_refresh_failed": strategic_failed,
                    "strategic_refresh_failure_reason": failure_reason,
                },
            },
            sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        ).encode("utf-8")
    ).hexdigest()
    return {
        "numeric": numeric,
        "champion_ids": champion_ids,
        # Physical slot identity is deliberately outside the v8 PPO hash/tensor.
        # It is audit/context metadata for the typed entity contract, not a policy feature.
        "entity_identity": entity_identity,
        "identity": identity,
        "item_state_identity": {
            "item_components": item_components,
            "item_inventory": item_inventory,
            "equipped_items": equipped_items,
            "item_component_catalog": item_component_catalog,
            "item_catalog_sha256": item_catalog_sha256,
            "pending_anvil": pending_anvil,
            "pending_anvil_sequence": pending_sequence,
            "pending_anvil_kind": pending_kind,
            "pending_anvil_options": pending_options,
        },
        "sha256": digest,
    }


def build_semantic_batch(
    metadata_rows,
    catalog_map: Mapping[str, int],
    *,
    contract: Mapping | None = None,
):
    """Project each native row once, reusing the caller's immutable catalog contract."""
    contract = contract if contract is not None else build_semantic_state_checkpoint_contract(catalog_map)
    if (
        not isinstance(contract, Mapping)
        or contract.get("contract", {}).get("contract_id") != SEMANTIC_STATE_CONTRACT_ID
        or contract.get("contract", {}).get("version") != SEMANTIC_STATE_CONTRACT_VERSION
    ):
        raise ValueError("semantic batch requires the active v8 checkpoint contract")
    # Catalog normalization and stable trait hashing are shared only within this
    # batch. No mutable cache escapes into the returned PPO projection.
    projection_context = _build_semantic_projection_context(catalog_map)
    projected = [
        project_native_player_state(row, catalog_map, _projection_context=projection_context)
        for row in metadata_rows
    ]
    item_catalog_hashes = {
        row["item_state_identity"]["item_catalog_sha256"] for row in projected
    }
    if len(item_catalog_hashes) > 1:
        raise ValueError("native players in one batch disagree on the item catalog fingerprint")
    return {
        "item_catalog_sha256": next(iter(item_catalog_hashes), None),
        "numeric": [row["numeric"] for row in projected],
        "champion_ids": [row["champion_ids"] for row in projected],
        "hashes": [row["sha256"] for row in projected],
        "identities": [row["identity"] for row in projected],
        "contract_id": contract["contract"]["contract_id"],
        "contract_hash": contract["sha256"],
    }


def semantic_batch_matches_snapshot_rows(
    batch: Mapping,
    metadata_rows: Sequence[Mapping],
    expected_contract: Mapping,
) -> bool:
    """Return whether a cached v8 projection belongs to these exact snapshot revisions.

    The native decision/player sequence numbers are the immutable snapshot revision.
    A producer that changes facts without advancing those sequences violates the native
    snapshot contract; a different engine, episode, player, round, lobby or catalog
    contract always invalidates the cache.
    """
    if not isinstance(batch, Mapping) or not isinstance(expected_contract, Mapping):
        return False
    identities = batch.get("identities")
    if not isinstance(metadata_rows, Sequence) or isinstance(metadata_rows, (str, bytes)):
        return False
    if not isinstance(identities, Sequence) or len(identities) != len(metadata_rows):
        return False
    if (
        batch.get("contract_id") != expected_contract.get("contract", {}).get("contract_id")
        or batch.get("contract_hash") != expected_contract.get("sha256")
    ):
        return False
    identity_fields = (
        "engine_instance_id", "episode_id", "decision_sequence",
        "player_decision_sequence", "player_id", "round", "lobby_index",
    )
    for metadata, identity in zip(metadata_rows, identities):
        if not isinstance(metadata, Mapping) or not isinstance(identity, Mapping):
            return False
        if (
            metadata.get("native_state_contract_id") != "tft.native-state-snapshot"
            or metadata.get("native_state_contract_version") != 6
            or any(metadata.get(field) != identity.get(field) for field in identity_fields)
        ):
            return False
    return True


def validate_semantic_batch_alignment(
    batch: Mapping,
    metadata_rows: Sequence[Mapping],
    expected_contract: Mapping,
    catalog_map: Mapping[str, int],
    *,
    reproject: bool = True,
    verify_catalog: bool = True,
) -> None:
    """Validate snapshot binding; optionally re-project only at an external trust boundary."""
    if not isinstance(batch, Mapping):
        raise TypeError("semantic batch must be a mapping")
    if not isinstance(metadata_rows, Sequence) or isinstance(metadata_rows, (str, bytes)):
        raise TypeError("semantic metadata rows must be a sequence")
    identities = batch.get("identities")
    hashes = batch.get("hashes")
    numeric = batch.get("numeric")
    champion_ids = batch.get("champion_ids")
    expected_id = expected_contract.get("contract", {}).get("contract_id")
    expected_hash = expected_contract.get("sha256")
    if verify_catalog:
        active_contract = build_semantic_state_checkpoint_contract(catalog_map)
        if dict(expected_contract) != active_contract:
            raise ValueError("active semantic checkpoint contract does not match the native catalog")
    elif (
        not isinstance(expected_contract, Mapping)
        or expected_contract.get("contract", {}).get("contract_id") != SEMANTIC_STATE_CONTRACT_ID
        or expected_contract.get("contract", {}).get("version") != SEMANTIC_STATE_CONTRACT_VERSION
    ):
        raise ValueError("semantic checkpoint contract is not the active v8 contract")
    if batch.get("contract_id") != expected_id or batch.get("contract_hash") != expected_hash:
        raise ValueError("semantic batch contract identity/hash diverges from the active checkpoint contract")
    row_count = len(metadata_rows)
    if not all(isinstance(value, Sequence) and len(value) == row_count for value in (
        identities, hashes, numeric, champion_ids
    )):
        raise ValueError("semantic batch rows do not match native metadata row count")
    identity_fields = (
        "engine_instance_id", "episode_id", "decision_sequence",
        "player_decision_sequence", "player_id", "round", "lobby_index",
    )
    observed_item_catalog_hashes = set()
    for index, (metadata, identity, digest) in enumerate(zip(metadata_rows, identities, hashes)):
        if not isinstance(metadata, Mapping) or not isinstance(identity, Mapping):
            raise TypeError(f"semantic row {index} identity/metadata must be mappings")
        expected_identity = {field: metadata.get(field) for field in identity_fields}
        if dict(identity) != expected_identity:
            raise ValueError(f"semantic row {index} identity does not match its native snapshot")
        if not isinstance(digest, str) or len(digest) != 64 or any(
            char not in "0123456789abcdef" for char in digest
        ):
            raise ValueError(f"semantic row {index} has an invalid projection hash")
        if metadata.get("semantic_projection_hash") != digest:
            raise ValueError(f"semantic row {index} projection hash is not bound to its snapshot metadata")
        if metadata.get("semantic_projection_contract_id") != expected_id:
            raise ValueError(f"semantic row {index} contract ID is not bound to its snapshot metadata")
        if metadata.get("semantic_projection_contract_hash") != expected_hash:
            raise ValueError(f"semantic row {index} contract hash is not bound to its snapshot metadata")
        if reproject:
            # Full source-to-tensor verification remains available at external audit
            # boundaries. The Trainer has just built this projection in-process.
            expected_row = project_native_player_state(metadata, catalog_map)
            observed_item_catalog_hashes.add(
                expected_row["item_state_identity"]["item_catalog_sha256"]
            )
            if (
                list(numeric[index]) != expected_row["numeric"]
                or list(champion_ids[index]) != expected_row["champion_ids"]
                or digest != expected_row["sha256"]
            ):
                raise ValueError(f"semantic row {index} tensor content does not match its native projection hash")
    if reproject:
        expected_item_catalog_hash = (
            next(iter(observed_item_catalog_hashes)) if len(observed_item_catalog_hashes) == 1 else None
        )
        if (
            len(observed_item_catalog_hashes) > 1
            or batch.get("item_catalog_sha256") != expected_item_catalog_hash
        ):
            raise ValueError("semantic batch item catalog fingerprint diverges from native player snapshots")
