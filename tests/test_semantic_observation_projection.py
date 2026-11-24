import hashlib

import pytest
import torch

from semantic_observation import (
    SEMANTIC_ENTITY_SLOTS,
    SEMANTIC_GLOBAL_FEATURES,
    SEMANTIC_NUMERIC_DIM,
    SEMANTIC_TRAIT_VOCAB_SIZE,
    SEMANTIC_POLICY_STATE_KEYS,
    semantic_policy_state_keys,
    validate_semantic_policy_state_dict,
    semantic_item_state_tensors,
    build_semantic_batch,
    build_semantic_state_checkpoint_contract,
    project_native_player_state,
    validate_semantic_state_checkpoint_contract,
    validate_semantic_state_checkpoint_integrity,
    validate_semantic_state_warm_start_migration,
    validate_semantic_batch_alignment,
    semantic_batch_matches_snapshot_rows,
)


def _unit(occupied=False, champion_id="", star=0, cost=0):
    return {
        "occupied": occupied,
        "champion_id": champion_id,
        "star": star,
        "cost": cost,
        "items": [],
        "trait_names": [],
        "role": 1,
        "attack_damage": 100.0,
        "attack_speed": 1.0,
        "max_health": 1000.0,
        "armor": 50.0,
        "magic_resist": 50.0,
    }


def _metadata():
    player = {
        "player_id": 2,
        "hp": 87.5,
        "damage_taken": 12.0,
        "alive": True,
        "wins": 3,
        "losses": 1,
        "placement": None,
        "opponent_id": 4,
        "gold": 42,
        "level": 6,
        "xp": 2,
        "win_streak": 2,
        "loss_streak": 0,
        "gold_before_interest": 42,
        "interest_if_resolved_now": 4,
        "board": [_unit() for _ in range(28)],
        "bench": [_unit() for _ in range(9)],
        "shop": [_unit() for _ in range(5)],
        "actions_taken_this_round": 3,
        "board_move_age": [0] + [10] * 27,
        "board_quality_score": 0.25,
        "board_positional_score": 0.5,
        "board_structural_score": -0.25,
        "board_exposed_carries": 1,
        "board_frontline_count": 2,
        "board_isolated_frontline_count": 1,
        "board_important_bench_units_unplayed": 1,
        "board_frontline_lane_count": 2,
        "board_exposed_main_carries": 1,
        "board_fragile_frontline_count": 1,
        "board_missing_frontline_count": 0,
        "board_missing_backline_count": 0,
        "board_active_trait_count": 2,
        "board_strategic_fit_score": 0.22,
        "board_unit_quality_score": 0.18,
        "board_trait_coherence_score": 0.07,
        "item_components": [],
        "item_inventory": [],
        "item_component_catalog": [f"component_{index}" for index in range(10)],
        "equipped_items": [],
        "pending_anvil": False,
        "pending_anvil_sequence": 0,
        "pending_anvil_kind": -1,
        "pending_anvil_options": [],
        "item_component_features": [0.0] * 10,
        "item_inventory_features": [[0.0] * 17 for _ in range(9)],
        "item_recipe_features": [[0.0] * 17 for _ in range(100)],
        "item_inventory_target_fit": [[0.0] * 37 for _ in range(9)],
        "item_recipe_target_fit": [[0.0] * 37 for _ in range(100)],
        "pending_anvil_option_features": [[0.0] * 11 for _ in range(9)],
    }
    player["board"][0] = _unit(True, "TFT_TestChampion", 2, 3)
    player["board"][0]["items"] = ["ItemA"]
    player["board"][0]["trait_names"] = ["TraitA", "TraitB"]
    player["bench"][0] = _unit(True, "TFT_TestChampion", 1, 3)
    player["strategic_state"] = {
        "contract_id": "tft.strategic-owner-observation",
        "contract_version": 3,
        "source_namespace": "tft.engine.strategic-owners",
        "producer": "TFTEngine::get_audit_snapshot",
        "episode_id": 5,
        "player_decision_sequence": 7,
        "strategic_context_sequence": 5,
        "player_id": 2,
        "round": 12,
        "active_composition_valid": True,
        "active_composition_id": "comp-a",
        "active_composition_version": 3,
        "active_source_sequence": 6,
        "active_unit_ids": [17],
        "active_core_unit_ids": [17],
        "direction_valid": True,
        "direction_identity": "direction-a",
        "direction_selected_round": 8,
        "direction_reference_unit_ids": [17],
        "pivot_candidate_valid": True,
        "pivot_candidate_identity": "pivot-b",
        "pivot_target_composition_identity": "comp-b",
        "pivot_source_composition_version": 3,
        "pivot_reference_unit_ids": [17],
        "unit_copy_progress": [
            {
                "champion_internal_id": 17,
                "owned_copy_equivalent": 4,
                "copies_toward_next_star": 0,
                "highest_star": 2,
            }
        ],
        "opportunity_cost_available": False,
        "planner_outputs_valid": False,
        "planner_output_sequence": 0,
        "unit_priorities": [],
        "opportunity_costs": [],
        "lineup_selected_unit_ids": [],
        "lineup_entry_unit_ids": [],
        "lineup_exit_unit_ids": [],
        "lineup_deferred_unit_ids": [],
        "strategic_refresh_failed": False,
        "strategic_refresh_failure_reason": "",
    }
    return {
        "engine_instance_id": "engine-1",
        "episode_id": 5,
        "decision_sequence": 11,
        "player_decision_sequence": 7,
        "player_id": 2,
        "lobby_index": 0,
        "stage": 3,
        "round": 12,
        "native_state_contract_id": "tft.native-state-snapshot",
        "native_state_contract_version": 6,
        "native_state_producer": "TFTEngine::get_audit_snapshot",
        "native_state_source_namespace": "tft.engine.observation-snapshot",
        "native_player_state": player,
        # These diagnostics must never enter the PPO semantic projection.
        "strategy": 4,
        "strategic_action_recommendation": 0,
        "strategic_confidence": 0.99,
    }


def test_strategic_refresh_failure_is_explicit_in_semantic_ppo_state():
    metadata = _metadata()
    strategic = metadata["native_player_state"]["strategic_state"]
    strategic["strategic_refresh_failed"] = True
    strategic["strategic_refresh_failure_reason"] = "native_strategic_refresh_exception: test"
    projected = project_native_player_state(metadata, {"TFT_TestChampion": 17})
    assert projected["numeric"][53] == 1.0


def test_native_planner_priority_lineup_and_opportunity_cost_reach_semantic_ppo_features():
    metadata = _metadata()
    strategic = metadata["native_player_state"]["strategic_state"]
    strategic["planner_outputs_valid"] = True
    strategic["planner_output_sequence"] = 5
    strategic["unit_priorities"] = [{
        "champion_internal_id": 17,
        "intent": 1,
        "relation": 0,
        "priority": 80,
        "target_star": 2,
        "sale_restricted": False,
        "confidence": 0.8,
    }]
    strategic["lineup_selected_unit_ids"] = [17]
    strategic["lineup_entry_unit_ids"] = []
    strategic["lineup_exit_unit_ids"] = []
    strategic["lineup_deferred_unit_ids"] = []
    strategic["opportunity_cost_available"] = True
    strategic["opportunity_costs"] = [{
        "champion_internal_id": 17,
        "value": 25.0,
        "uncertainty": 0.2,
        "horizon_rounds": 1,
        "source": "same_snapshot_competing_alternative.v1",
        "forgone_candidate_id": "action:alternative:1",
        "value_basis": "contextual_action_score.v1",
    }]
    projected = project_native_player_state(metadata, {"TFT_TestChampion": 17})
    entity_start = SEMANTIC_GLOBAL_FEATURES
    assert projected["numeric"][entity_start + 39] == 0.8
    assert projected["numeric"][entity_start + 41] == 1.0
    assert projected["numeric"][entity_start + 43] == 0.25
    assert projected["numeric"][entity_start + 44] == 1.0


def test_semantic_projection_rejects_inconsistent_native_planner_contracts():
    stale = _metadata()
    strategic = stale["native_player_state"]["strategic_state"]
    strategic["planner_outputs_valid"] = True
    strategic["planner_output_sequence"] = strategic["strategic_context_sequence"] - 1
    with pytest.raises(ValueError, match="planner outputs are not bound"):
        project_native_player_state(stale, {"TFT_TestChampion": 17})

    unavailable_rows = _metadata()
    strategic = unavailable_rows["native_player_state"]["strategic_state"]
    strategic["unit_priorities"] = [{
        "champion_internal_id": 17, "intent": 1, "relation": 0,
        "priority": 80, "target_star": 2, "sale_restricted": False,
        "confidence": 0.8,
    }]
    with pytest.raises(ValueError, match="unavailable planner outputs"):
        project_native_player_state(unavailable_rows, {"TFT_TestChampion": 17})

    mismatched_failure = _metadata()
    strategic = mismatched_failure["native_player_state"]["strategic_state"]
    strategic["strategic_refresh_failed"] = True
    with pytest.raises(ValueError, match="failure flag/reason mismatch"):
        project_native_player_state(mismatched_failure, {"TFT_TestChampion": 17})

    duplicate_lineup = _metadata()
    strategic = duplicate_lineup["native_player_state"]["strategic_state"]
    strategic["planner_outputs_valid"] = True
    strategic["planner_output_sequence"] = strategic["strategic_context_sequence"]
    strategic["lineup_selected_unit_ids"] = [17, 17]
    with pytest.raises(ValueError, match="contains duplicate IDs"):
        project_native_player_state(duplicate_lineup, {"TFT_TestChampion": 17})


def test_semantic_projection_rejects_duplicate_or_unavailable_opportunity_cost():
    row = _metadata()
    strategic = row["native_player_state"]["strategic_state"]
    opportunity = {
        "champion_internal_id": 17,
        "value": 25.0,
        "uncertainty": 0.2,
        "horizon_rounds": 1,
        "source": "same_snapshot_competing_alternative.v1",
        "forgone_candidate_id": "action:alternative:1",
        "value_basis": "contextual_action_score.v1",
    }
    strategic["opportunity_cost_available"] = True
    strategic["opportunity_costs"] = [opportunity, dict(opportunity)]
    with pytest.raises(ValueError, match="invalid or duplicate evidence"):
        project_native_player_state(row, {"TFT_TestChampion": 17})

    row = _metadata()
    strategic = row["native_player_state"]["strategic_state"]
    strategic["opportunity_cost_available"] = True
    with pytest.raises(ValueError, match="diverges from native opportunity rows"):
        project_native_player_state(row, {"TFT_TestChampion": 17})


def test_native_semantic_projection_has_stable_shape_and_explicit_identity():
    catalog = {"TFT_TestChampion": 17}
    projected = project_native_player_state(_metadata(), catalog)
    assert len(projected["numeric"]) == SEMANTIC_NUMERIC_DIM
    assert len(projected["champion_ids"]) == SEMANTIC_ENTITY_SLOTS
    assert projected["champion_ids"][0] == 18
    assert projected["numeric"][54] == 0.25  # native board quality
    assert projected["numeric"][55] == 0.5  # native positional score
    assert projected["numeric"][56] == -0.25  # native structural score
    assert projected["numeric"][57] == 1.0 / 9.0  # exposed carries
    assert projected["numeric"][58] == 2.0 / 9.0  # frontline count
    assert projected["numeric"][59] == 1.0 / 9.0  # isolated frontline count
    assert projected["numeric"][60] == 1.0 / 9.0  # important unplayed bench units
    assert projected["numeric"][61] == 2.0 / 7.0  # frontline lanes
    assert projected["numeric"][62] == 1.0 / 9.0  # exposed main carries
    assert projected["numeric"][63] == 1.0 / 9.0  # fragile frontline
    assert projected["numeric"][64] == 0.0  # missing frontline
    assert projected["numeric"][65] == 0.0  # missing backline
    assert projected["numeric"][66] == 2.0 / 28.0  # active traits
    assert projected["numeric"][67] == 0.22  # strategic fit
    assert projected["numeric"][68] == 0.18  # unit quality
    assert projected["numeric"][69] == 0.07  # trait coherence
    entity_start = SEMANTIC_GLOBAL_FEATURES
    assert projected["numeric"][entity_start] == 1.0  # occupied
    assert projected["numeric"][entity_start + 5] == 1.0  # mapped champion identity valid
    assert projected["numeric"][entity_start + 6] == 1.0  # active composition member
    assert projected["numeric"][entity_start + 7] == 1.0  # active core member
    assert projected["numeric"][entity_start + 8] == 1.0  # direction reference
    assert projected["numeric"][entity_start + 9] == 1.0  # pivot reference
    assert projected["numeric"][entity_start + 10] == 4.0 / 9.0  # owned copies
    assert projected["numeric"][entity_start + 11] == 0.0  # no upgrade progress
    # The appended 17-field item target profile comes from the native snapshot.
    assert projected["numeric"][entity_start + 12] == 1.0  # occupied target
    assert projected["numeric"][entity_start + 13] == 1.0  # board target
    assert projected["numeric"][entity_start + 17] == 1.0  # classifier role one-hot (fighter)
    assert projected["numeric"][entity_start + 21] == 1.0  # frontline row
    assert projected["numeric"][entity_start + 23] == 0.5  # attack damage / 200
    assert projected["numeric"][entity_start + 28] == 1.0 / 3.0  # equipped item count / 3
    bench_target_start = SEMANTIC_GLOBAL_FEATURES + 28 * 45 + 12
    assert projected["numeric"][bench_target_start + 2] == 1.0
    assert projected["numeric"][bench_target_start + 9] == 0.0
    assert projected["numeric"][21] == 5.0 / 9.0  # board capacity
    assert projected["numeric"][22] == 8.0 / 9.0  # bench capacity
    assert projected["numeric"][23] == 0.3  # actions taken this round
    assert projected["numeric"][24] == 0.0  # current board slot move age
    assert projected["numeric"][25] == 1.0  # empty slot move age is capped
    assert projected["identity"]["player_id"] == 2
    assert len(projected["sha256"]) == 64


def test_copy_progress_consumes_native_unit_copy_progress_without_recounting():
    row = _metadata()
    row["native_player_state"]["strategic_state"]["unit_copy_progress"][0][
        "copies_toward_next_star"
    ] = 2
    projected = project_native_player_state(row, {"TFT_TestChampion": 17})
    assert projected["numeric"][SEMANTIC_GLOBAL_FEATURES + 11] == 1.0


def test_native_trait_identities_are_stably_hashed_and_exposed_to_policy():
    metadata = _metadata()
    metadata["native_player_state"]["board"][0]["trait_names"] = ["TraitAlpha", "TraitBeta"]
    projected = project_native_player_state(metadata, {"Test_A": 0})
    trait_ids = semantic_item_state_tensors(
        torch.tensor([projected["numeric"]], dtype=torch.float32)
    )["trait_ids"]

    expected = [
        int.from_bytes(hashlib.sha256(name.encode("utf-8")).digest()[:4], "big")
        % SEMANTIC_TRAIT_VOCAB_SIZE + 1
        for name in ("TraitAlpha", "TraitBeta")
    ]
    assert trait_ids.shape == (1, SEMANTIC_ENTITY_SLOTS, 10)
    assert trait_ids[0, 0, :2].tolist() == expected
    assert trait_ids[0, 0, 2:].count_nonzero().item() == 0
    assert trait_ids[0, 1].count_nonzero().item() == 0


def test_item_identity_and_anvil_sequence_are_bound_to_projection_hash():
    base = _metadata()
    base["native_player_state"]["item_inventory"] = ["completed_item_alpha"]
    first = project_native_player_state(base, {"Test_A": 0})

    changed_item = _metadata()
    changed_item["native_player_state"]["item_inventory"] = ["completed_item_beta"]
    second = project_native_player_state(changed_item, {"Test_A": 0})
    assert first["sha256"] != second["sha256"]

    pending = _metadata()
    pending["native_player_state"]["pending_anvil"] = True
    pending["native_player_state"]["pending_anvil_sequence"] = 7
    pending["native_player_state"]["pending_anvil_kind"] = 0
    pending["native_player_state"]["pending_anvil_options"] = ["component_0"]
    pending["native_player_state"]["pending_anvil_option_features"][0][0] = 1.0
    pending_first = project_native_player_state(pending, {"Test_A": 0})

    next_sequence = dict(pending)
    next_sequence["native_player_state"]["pending_anvil_sequence"] = 8
    pending_second = project_native_player_state(next_sequence, {"Test_A": 0})
    assert pending_first["sha256"] != pending_second["sha256"]


def test_semantic_batch_is_deterministic_and_catalog_contract_is_bound():
    rows = [_metadata()]
    catalog = {"TFT_TestChampion": 17}
    first = build_semantic_batch(rows, catalog)
    second = build_semantic_batch(rows, dict(catalog))
    assert first == second

    contract = build_semantic_state_checkpoint_contract(catalog)
    validate_semantic_state_checkpoint_contract(contract, catalog)
    incompatible_catalog = {"TFT_TestChampion": 18}
    try:
        validate_semantic_state_checkpoint_contract(contract, incompatible_catalog)
    except ValueError:
        pass
    else:
        raise AssertionError("semantic checkpoint must reject catalog drift")


def test_unknown_champion_is_not_fabricated_and_is_marked_invalid():
    row = _metadata()
    row["native_player_state"]["board"][0]["champion_id"] = "TFT_UnknownChampion"
    projected = project_native_player_state(row, {"TFT_TestChampion": 17})
    assert projected["champion_ids"][0] == 0
    assert projected["numeric"][SEMANTIC_GLOBAL_FEATURES + 5] == 0.0


def test_projection_rejects_missing_native_provenance_or_player_mismatch():
    row = _metadata()
    row["native_state_producer"] = "legacy_strategy"
    try:
        project_native_player_state(row, {"TFT_TestChampion": 17})
    except ValueError:
        pass
    else:
        raise AssertionError("unverified producer must be rejected")

    row = _metadata()
    row["native_player_state"]["strategic_state"]["player_decision_sequence"] = 99
    try:
        project_native_player_state(row, {"TFT_TestChampion": 17})
    except ValueError as exc:
        assert "player_decision_sequence" in str(exc)
    else:
        raise AssertionError("stale strategic owner state must be rejected")

    row = _metadata()
    row["native_player_state"]["player_id"] = 1
    try:
        project_native_player_state(row, {"TFT_TestChampion": 17})
    except ValueError:
        pass
    else:
        raise AssertionError("cross-player native state must be rejected")


def test_semantic_projection_and_trainer_do_not_query_legacy_strategy_api():
    from copy import deepcopy
    from pathlib import Path

    catalog = {"TFT_TestChampion": 17}
    baseline = _metadata()
    changed_legacy_diagnostics = deepcopy(baseline)
    changed_legacy_diagnostics["strategy"] = 0
    changed_legacy_diagnostics["strategic_action_recommendation"] = 8
    changed_legacy_diagnostics["strategic_confidence"] = 0.01
    changed_legacy_diagnostics["composition_direction"] = "unrelated-legacy-label"

    first = project_native_player_state(baseline, catalog)
    second = project_native_player_state(changed_legacy_diagnostics, catalog)
    assert first["numeric"] == second["numeric"]
    assert first["champion_ids"] == second["champion_ids"]

    trainer_source = (
        Path(__file__).resolve().parents[1] / "trainer.py"
    ).read_text(encoding="utf-8")
    assert 'env_method(\n                        "get_strategies"' not in trainer_source


def test_semantic_projection_rejects_invalid_strategic_context_sequence():
    row = _metadata()
    row["native_player_state"]["strategic_state"]["strategic_context_sequence"] = True
    with pytest.raises(ValueError, match="strategic_context_sequence"):
        project_native_player_state(row, {"TFT_TestChampion": 17})

def test_semantic_batch_alignment_rejects_cross_snapshot_and_contract_drift():
    row = _metadata()
    catalog = {"TFT_TestChampion": 17}
    batch = build_semantic_batch([row], catalog)
    contract = build_semantic_state_checkpoint_contract(catalog)
    row["semantic_projection_hash"] = batch["hashes"][0]
    row["semantic_projection_contract_id"] = batch["contract_id"]
    row["semantic_projection_contract_hash"] = batch["contract_hash"]
    validate_semantic_batch_alignment(batch, [row], contract, catalog)

    crossed = dict(batch)
    crossed["identities"] = [dict(batch["identities"][0], player_decision_sequence=99)]
    with pytest.raises(ValueError, match="identity"):
        validate_semantic_batch_alignment(crossed, [row], contract, catalog)

    stale = dict(row, semantic_projection_hash="0" * 64)
    with pytest.raises(ValueError, match="projection hash"):
        validate_semantic_batch_alignment(batch, [stale], contract, catalog)


def test_semantic_projection_hash_binds_owner_identity_even_when_tensor_is_equal():
    first_row = _metadata()
    second_row = _metadata()
    second_row["native_player_state"]["strategic_state"]["active_composition_id"] = "comp-other"
    first = project_native_player_state(first_row, {"TFT_TestChampion": 17})
    second = project_native_player_state(second_row, {"TFT_TestChampion": 17})
    assert first["numeric"] == second["numeric"]
    assert first["champion_ids"] == second["champion_ids"]
    assert first["sha256"] != second["sha256"]




def test_semantic_v2_checkpoint_has_only_explicit_v8_warm_start_path():
    import copy
    import hashlib
    import json

    catalog = {"TFT_TestChampion": 17}
    current = build_semantic_state_checkpoint_contract(catalog)
    historical = copy.deepcopy(current)
    payload = historical["contract"]
    payload["contract_id"] = "tft.ppo.semantic-native-state.v2"
    payload["version"] = 2
    payload["source"]["contract_version"] = 3
    payload["strategic_owner_source"]["contract_version"] = 2
    payload["global_features"] = payload["global_features"][:21]
    payload["entity_slots"]["features"] = payload["entity_slots"]["features"][:12]
    payload["numeric_dimension"] = 21 + SEMANTIC_ENTITY_SLOTS * 12
    payload["encoder"]["numeric_plus_embedding_input_dim"] = (
        payload["numeric_dimension"] + SEMANTIC_ENTITY_SLOTS * 16
    )
    payload.pop("item_state")
    payload.pop("trait_embedding")
    payload["encoder"]["kind"] = "champion_embedding_plus_mlp"
    payload["encoder"]["fusion"] = "additive_to_shared_actor_critic_latent"
    payload["encoder"].pop("board_cnn_source")
    payload["encoder"].pop("action_candidate_source")
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    historical["sha256"] = hashlib.sha256(canonical).hexdigest()

    validate_semantic_state_checkpoint_integrity(historical)
    validate_semantic_state_warm_start_migration(historical, catalog)
    with pytest.raises(ValueError, match="incompatible"):
        validate_semantic_state_checkpoint_contract(historical, catalog)

def test_semantic_v6_checkpoint_has_explicit_v8_warm_start_path():
    import copy
    import hashlib
    import json

    catalog = {"TFT_TestChampion": 17}
    current = build_semantic_state_checkpoint_contract(catalog)
    historical = copy.deepcopy(current)
    payload = historical["contract"]
    payload["contract_id"] = "tft.ppo.semantic-native-state.v6"
    payload["version"] = 6
    payload["source"]["contract_version"] = 5
    payload["strategic_owner_source"]["contract_version"] = 2
    payload["global_features"] = payload["global_features"][:52]
    payload["entity_slots"]["features"] = payload["entity_slots"]["features"][:39]
    payload["numeric_dimension"] -= (
        SEMANTIC_GLOBAL_FEATURES - 52 + SEMANTIC_ENTITY_SLOTS * 6
    )
    payload["encoder"]["numeric_plus_embedding_input_dim"] -= (
        SEMANTIC_GLOBAL_FEATURES - 52 + SEMANTIC_ENTITY_SLOTS * 6
    )
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    historical["sha256"] = hashlib.sha256(canonical).hexdigest()

    validate_semantic_state_checkpoint_integrity(historical)
    validate_semantic_state_warm_start_migration(historical, catalog)
    with pytest.raises(ValueError, match="incompatible"):
        validate_semantic_state_checkpoint_contract(historical, catalog)

    unrelated_change = copy.deepcopy(historical)
    unrelated_change["contract"]["critic_action_mask_input"] = "legacy_fused_input"
    canonical = json.dumps(
        unrelated_change["contract"], sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    unrelated_change["sha256"] = hashlib.sha256(canonical).hexdigest()
    with pytest.raises(ValueError, match="all other contract fields must match"):
        validate_semantic_state_warm_start_migration(unrelated_change, catalog)


def test_semantic_v7_checkpoint_has_explicit_v8_warm_start_path():
    import copy
    import hashlib
    import json

    catalog = {"TFT_TestChampion": 17}
    current = build_semantic_state_checkpoint_contract(catalog)
    historical = copy.deepcopy(current)
    payload = historical["contract"]
    payload["contract_id"] = "tft.ppo.semantic-native-state.v7"
    payload["version"] = 7
    payload["source"]["contract_version"] = 5
    payload["global_features"] = payload["global_features"][:-16]
    payload["numeric_dimension"] -= 16
    payload["encoder"]["numeric_plus_embedding_input_dim"] -= 16
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    historical["sha256"] = hashlib.sha256(canonical).hexdigest()

    validate_semantic_state_checkpoint_integrity(historical)
    validate_semantic_state_warm_start_migration(historical, catalog)
    with pytest.raises(ValueError, match="incompatible"):
        validate_semantic_state_checkpoint_contract(historical, catalog)


def test_semantic_checkpoint_manifest_integrity_is_separate_from_runtime_compatibility():
    import copy

    catalog = {"TFT_TestChampion": 17}
    historical = build_semantic_state_checkpoint_contract(catalog)
    validate_semantic_state_checkpoint_integrity(historical)
    changed = copy.deepcopy(historical)
    changed["contract"]["strategic_owner_source"]["contract_version"] = 1
    import hashlib
    import json
    canonical = json.dumps(
        changed["contract"], sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    changed["sha256"] = hashlib.sha256(canonical).hexdigest()
    validate_semantic_state_checkpoint_integrity(changed)
    validate_semantic_state_warm_start_migration(changed, catalog)
    with pytest.raises(ValueError, match="incompatible"):
        validate_semantic_state_checkpoint_contract(changed, catalog)
    with pytest.raises(ValueError, match="catalog, normalization"):
        validate_semantic_state_warm_start_migration(
            changed, {"TFT_TestChampion": 18}
        )
    changed["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="hash is invalid"):
        validate_semantic_state_checkpoint_integrity(changed)


def test_semantic_v8_checkpoint_weight_contract_requires_trait_embedding():
    complete = {key: object() for key in SEMANTIC_POLICY_STATE_KEYS}
    assert semantic_policy_state_keys(complete) == SEMANTIC_POLICY_STATE_KEYS
    validate_semantic_policy_state_dict(complete)

    incomplete = dict(complete)
    incomplete.pop("semantic_trait_embedding.weight")
    assert semantic_policy_state_keys(incomplete) != SEMANTIC_POLICY_STATE_KEYS
    with pytest.raises(ValueError, match="Semantic v8 policy weights are incomplete"):
        validate_semantic_policy_state_dict(incomplete)



def test_semantic_alignment_can_validate_binding_without_reprojecting(monkeypatch):
    import semantic_observation

    catalog = {"TFT_TestChampion": 17}
    row = _metadata()
    contract = build_semantic_state_checkpoint_contract(catalog)
    batch = build_semantic_batch([row], catalog, contract=contract)
    row["semantic_projection_hash"] = batch["hashes"][0]
    row["semantic_projection_contract_id"] = batch["contract_id"]
    row["semantic_projection_contract_hash"] = batch["contract_hash"]

    def unexpected_projection(*args, **kwargs):
        raise AssertionError("alignment validation must not rebuild an existing projection")

    monkeypatch.setattr(semantic_observation, "project_native_player_state", unexpected_projection)
    validate_semantic_batch_alignment(
        batch, [row], contract, catalog, reproject=False, verify_catalog=False
    )


def test_semantic_batch_reuses_precomputed_v8_contract(monkeypatch):
    import semantic_observation

    catalog = {"TFT_TestChampion": 17}
    contract = build_semantic_state_checkpoint_contract(catalog)

    def unexpected_contract_build(*args, **kwargs):
        raise AssertionError("precomputed contract should be reused")

    monkeypatch.setattr(
        semantic_observation, "build_semantic_state_checkpoint_contract",
        unexpected_contract_build,
    )
    batch = build_semantic_batch([_metadata()], catalog, contract=contract)
    assert batch["contract_id"] == contract["contract"]["contract_id"]
    assert batch["contract_hash"] == contract["sha256"]



def test_semantic_projection_cache_requires_exact_native_snapshot_revision():
    catalog = {"TFT_TestChampion": 17}
    contract = build_semantic_state_checkpoint_contract(catalog)
    row = _metadata()
    batch = build_semantic_batch([row], catalog, contract=contract)
    assert semantic_batch_matches_snapshot_rows(batch, [row], contract)

    for field, changed in (
        ("engine_instance_id", "engine-other"),
        ("episode_id", 6),
        ("decision_sequence", 12),
        ("player_decision_sequence", 8),
        ("player_id", 3),
        ("round", 13),
        ("lobby_index", 1),
        ("native_state_contract_version", 5),
    ):
        altered = dict(row, **{field: changed})
        assert not semantic_batch_matches_snapshot_rows(batch, [altered], contract), field

    stale_contract = dict(contract, sha256="0" * 64)
    assert not semantic_batch_matches_snapshot_rows(batch, [row], stale_contract)



def test_semantic_cache_invalidates_unit_item_and_trait_mutations_when_revision_advances():
    from copy import deepcopy

    catalog = {"TFT_TestChampion": 17}
    contract = build_semantic_state_checkpoint_contract(catalog)
    original = _metadata()
    batch = build_semantic_batch([original], catalog, contract=contract)

    mutations = (
        ("unit", lambda row: row["native_player_state"]["board"][0].update(star=3)),
        ("items", lambda row: row["native_player_state"]["board"][0]["items"].append("ItemB")),
        ("traits", lambda row: row["native_player_state"]["board"][0]["trait_names"].append("TraitC")),
        ("inventory", lambda row: row["native_player_state"]["item_inventory"].append("completed_item_alpha")),
    )
    for name, mutate in mutations:
        changed = deepcopy(original)
        mutate(changed)
        changed["decision_sequence"] += 1
        changed["player_decision_sequence"] += 1
        assert not semantic_batch_matches_snapshot_rows(batch, [changed], contract), name


def test_semantic_cache_invalidates_on_real_catalog_contract_change():
    original_catalog = {"TFT_TestChampion": 17}
    changed_catalog = {"TFT_TestChampion": 17, "TFT_AnotherChampion": 18}
    original_contract = build_semantic_state_checkpoint_contract(original_catalog)
    changed_contract = build_semantic_state_checkpoint_contract(changed_catalog)
    row = _metadata()
    batch = build_semantic_batch([row], original_catalog, contract=original_contract)

    assert original_contract["sha256"] != changed_contract["sha256"]
    assert not semantic_batch_matches_snapshot_rows(batch, [row], changed_contract)
