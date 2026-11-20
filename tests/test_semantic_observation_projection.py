import pytest

from semantic_observation import (
    SEMANTIC_ENTITY_SLOTS,
    SEMANTIC_NUMERIC_DIM,
    build_semantic_batch,
    build_semantic_state_checkpoint_contract,
    project_native_player_state,
    validate_semantic_state_checkpoint_contract,
)


def _unit(occupied=False, champion_id="", star=0, cost=0):
    return {
        "occupied": occupied,
        "champion_id": champion_id,
        "star": star,
        "cost": cost,
        "items": [],
        "trait_names": [],
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
    }
    player["board"][0] = _unit(True, "TFT_TestChampion", 2, 3)
    player["board"][0]["items"] = ["ItemA"]
    player["board"][0]["trait_names"] = ["TraitA", "TraitB"]
    player["bench"][0] = _unit(True, "TFT_TestChampion", 1, 3)
    player["strategic_state"] = {
        "contract_id": "tft.strategic-owner-observation",
        "contract_version": 2,
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
        "native_state_contract_version": 3,
        "native_state_producer": "TFTEngine::get_audit_snapshot",
        "native_state_source_namespace": "tft.engine.observation-snapshot",
        "native_player_state": player,
        # These diagnostics must never enter the PPO semantic projection.
        "strategy": 4,
        "strategic_action_recommendation": 0,
        "strategic_confidence": 0.99,
    }


def test_native_semantic_projection_has_stable_shape_and_explicit_identity():
    catalog = {"TFT_TestChampion": 17}
    projected = project_native_player_state(_metadata(), catalog)
    assert len(projected["numeric"]) == SEMANTIC_NUMERIC_DIM
    assert len(projected["champion_ids"]) == SEMANTIC_ENTITY_SLOTS
    assert projected["champion_ids"][0] == 18
    assert projected["numeric"][21] == 1.0  # occupied
    assert projected["numeric"][26] == 1.0  # mapped champion identity valid
    assert projected["numeric"][27] == 1.0  # active composition member
    assert projected["numeric"][28] == 1.0  # active core member
    assert projected["numeric"][29] == 1.0  # direction reference
    assert projected["numeric"][30] == 1.0  # pivot reference
    assert projected["numeric"][31] == 4.0 / 9.0  # one 2-star plus one 1-star copy
    assert projected["numeric"][32] == 0.0  # native UnitCopyProgress reports no 2-star progress
    assert projected["identity"]["player_id"] == 2
    assert len(projected["sha256"]) == 64


def test_copy_progress_consumes_native_unit_copy_progress_without_recounting():
    row = _metadata()
    row["native_player_state"]["strategic_state"]["unit_copy_progress"][0][
        "copies_toward_next_star"
    ] = 2
    projected = project_native_player_state(row, {"TFT_TestChampion": 17})
    assert projected["numeric"][32] == 1.0


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
    assert projected["numeric"][26] == 0.0


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
