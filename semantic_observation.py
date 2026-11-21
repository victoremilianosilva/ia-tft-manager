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

SEMANTIC_STATE_CONTRACT_ID = "tft.ppo.semantic-native-state.v6"
SEMANTIC_STATE_CONTRACT_VERSION = 6
SEMANTIC_ENTITY_SLOTS = 28 + 9 + 5
SEMANTIC_ENTITY_FEATURES = 39
SEMANTIC_GLOBAL_FEATURES = 52
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
SEMANTIC_TRAIT_VOCAB_SIZE = 4096
SEMANTIC_TRAIT_EMBED_DIM = 16


def semantic_item_state_tensors(numeric):
    """Expose named item/anvil tensors from the identity-bound semantic row."""
    if not isinstance(numeric, __import__("torch").Tensor):
        raise TypeError("semantic numeric input must be a torch tensor")
    if numeric.ndim != 2 or numeric.shape[-1] != SEMANTIC_NUMERIC_DIM:
        raise ValueError("semantic numeric input has an incompatible v6 shape")
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
            "contract_version": 4,
            "producer": "TFTEngine::get_audit_snapshot",
            "source_namespace": "tft.engine.observation-snapshot",
        },
        "strategic_owner_source": {
            "contract_id": "tft.strategic-owner-observation",
            "contract_version": 2,
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
            "board_move_age[0:28]/10",
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
                "trait_id_hash_bucket[0:10]/4096",
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
                    "occupied", "cost/5", "star/3", "equipped_item_count/9",
                    "trait_count/10", "owned_copy_equivalent/9",
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
    """Allow only the reviewed semantic v2-to-v6 and owner v1-to-v2 warm-starts."""
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
        # Reviewed v2 -> v6 migration: native snapshot v3 -> v4 adds capacity,
        # temporal facts, board/bench item-target profiles and structured item/anvil blocks. The semantic
        # entity stride expands while historical identity remains bound.
        historical_payload["contract_id"] = expected["contract"]["contract_id"]
        historical_payload["version"] = expected["contract"]["version"]
        historical_source = dict(historical_payload.get("source", {}))
        historical_source["contract_version"] = 4
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
    elif historical_owner_source.get("contract_version") == 1:
        historical_owner_source["contract_version"] = 2
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
    if metadata.get("native_state_contract_id") != "tft.native-state-snapshot" or metadata.get("native_state_contract_version") != 4:
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
        or strategic_version != 2
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
    # No validated per-action opportunity-cost producer is published here yet.
    if opportunity_available:
        raise ValueError("opportunity-cost evidence is not yet published by a native action producer")

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
    ]

    catalog = dict(catalog_map)
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
    known_catalog_ids = set(catalog.values())
    if not (set(copy_progress) & known_catalog_ids).issubset(observed_owned_ids):
        raise ValueError("native UnitCopyProgress contains known champions absent from board/bench")
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
            trait_ids = [
                int.from_bytes(hashlib.sha256(trait.encode("utf-8")).digest()[:4], "big")
                % SEMANTIC_TRAIT_VOCAB_SIZE + 1
                for trait in traits
            ]
            numeric.extend(float(trait_id / SEMANTIC_TRAIT_VOCAB_SIZE) for trait_id in trait_ids)
            numeric.extend([0.0] * (SEMANTIC_TRAIT_SLOTS - len(trait_ids)))
            champion_ids.append(0 if internal_id is None else int(internal_id) + 1)

    def read_feature_block(field, shape):
        value = state.get(field)
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
        if any(value < 0.0 or value > 1.0 for value in flat):
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
                },
            },
            sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        ).encode("utf-8")
    ).hexdigest()
    return {
        "numeric": numeric,
        "champion_ids": champion_ids,
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


def build_semantic_batch(metadata_rows, catalog_map: Mapping[str, int]):
    projected = [project_native_player_state(row, catalog_map) for row in metadata_rows]
    contract = build_semantic_state_checkpoint_contract(catalog_map)
    return {
        "numeric": [row["numeric"] for row in projected],
        "champion_ids": [row["champion_ids"] for row in projected],
        "hashes": [row["sha256"] for row in projected],
        "identities": [row["identity"] for row in projected],
        "contract_id": contract["contract"]["contract_id"],
        "contract_hash": contract["sha256"],
    }


def validate_semantic_batch_alignment(
    batch: Mapping,
    metadata_rows: Sequence[Mapping],
    expected_contract: Mapping,
    catalog_map: Mapping[str, int],
) -> None:
    """Fail closed unless each semantic row is bound to its exact native snapshot."""
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
    active_contract = build_semantic_state_checkpoint_contract(catalog_map)
    if dict(expected_contract) != active_contract:
        raise ValueError("active semantic checkpoint contract does not match the native catalog")
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
        # Re-project from the native source so a detached/mutated tensor cannot
        # retain a stale digest merely because its metadata still looks valid.
        expected_row = project_native_player_state(metadata, catalog_map)
        if (
            list(numeric[index]) != expected_row["numeric"]
            or list(champion_ids[index]) != expected_row["champion_ids"]
            or digest != expected_row["sha256"]
        ):
            raise ValueError(f"semantic row {index} tensor content does not match its native projection hash")
