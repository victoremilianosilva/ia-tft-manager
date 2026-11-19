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
    assert projected["numeric"][17] == 1.0  # occupied
    assert projected["numeric"][22] == 1.0  # mapped champion identity valid
    assert projected["identity"]["player_id"] == 2
    assert len(projected["sha256"]) == 64


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
    assert projected["numeric"][22] == 0.0


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
