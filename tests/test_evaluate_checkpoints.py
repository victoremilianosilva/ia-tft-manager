"""Regression tests for deterministic checkpoint evaluation helpers.

These tests avoid training and real checkpoint files. They validate action/mask
plumbing and ensure evaluation refuses incomplete match results instead of
silently manufacturing placements.
"""
from __future__ import annotations

import copy
import hashlib
import json
import numpy as np
import pytest
import torch

from scripts.audit_strategic_policy import _action_dict as strategic_action_dict, _json_masks, _player_gold

from scripts.evaluate_checkpoints import (
    ACTION_DIMS,
    action_dict,
    as_mask_batch,
    policy_actions,
    run_match,
    summarize_paired_seeds,
    candidate_slots_for_seed,
    validate_candidate_slots,
    run_paired_evaluation,
    write_paired_evaluation_artifacts,
)


def test_action_dict_preserves_all_six_action_components():
    assert action_dict([3, 4, 8, 27, 6, 19]) == {
        "type": 3,
        "shop_slot": 4,
        "bench_slot": 8,
        "board_target": 27,
        "board_source": 6,
        "conditioned_board_target": 19,
    }

def test_checkpoint_evaluator_uses_current_item_policy_dimensions():
    assert ACTION_DIMS == [9, 5, 9, 28, 28, 28]


def test_action_dict_serializes_inventory_equip_arguments_for_native_adapter():
    result = action_dict([7, 3, 11, 0, 0, 0])
    assert result["type"] == 7
    assert result["item_slot"] == 3
    assert result["item_target"] == 11


def test_action_dict_serializes_craft_and_equip_arguments_for_native_adapter():
    result = action_dict([8, 2, 4, 15, 0, 0])
    assert result["type"] == 8
    assert result["component_first"] == 2
    assert result["component_second"] == 4
    assert result["item_target"] == 15


def test_as_mask_batch_selects_requested_players_and_keeps_boolean_dtype():
    masks = [
        {"type_mask": np.array([True, False]), "shop_mask": np.array([False, True, True])},
        {"type_mask": np.array([False, True]), "shop_mask": np.array([True, False, True])},
        {"type_mask": np.array([True, True]), "shop_mask": np.array([True, True, False])},
    ]

    batch = as_mask_batch(masks, [2, 0], torch.device("cpu"))

    assert batch["type_mask"].dtype == torch.bool
    assert batch["shop_mask"].dtype == torch.bool
    torch.testing.assert_close(
        batch["type_mask"],
        torch.tensor([[True, True], [True, False]]),
    )
    torch.testing.assert_close(
        batch["shop_mask"],
        torch.tensor([[True, True, False], [False, True, True]]),
    )


class _FakePolicy:
    def get_action(self, observations, masks, deterministic):
        assert deterministic is True
        assert observations.ndim == 2
        assert all(mask.dtype == torch.bool for mask in masks.values())
        actions = torch.zeros((observations.shape[0], 6), dtype=torch.int64)
        actions[:, 0] = 6  # PASS
        return actions, None, None


def test_policy_actions_returns_one_six_component_action_per_requested_index():
    observations = np.zeros((4, 12), dtype=np.float32)
    masks = [{"type_mask": np.ones(9, dtype=np.bool_)} for _ in range(4)]

    result = policy_actions(
        _FakePolicy(),
        observations,
        masks,
        [1, 3],
        torch.device("cpu"),
    )

    assert result == {1: [6, 0, 0, 0, 0, 0], 3: [6, 0, 0, 0, 0, 0]}


class _FakePlayer:
    def __init__(self, alive=True):
        self.alive = alive


class _FakeLobby:
    def __init__(self, ranking=None, finish=True):
        self.finished = False
        self.players = [_FakePlayer() for _ in range(8)]
        self._ranking = ranking
        self._finish = finish
        self.last_actions = None

    def reset(self):
        return np.zeros((8, 12), dtype=np.float32)

    def get_action_masks(self):
        return [{"type_mask": np.ones(7, dtype=np.bool_)} for _ in range(8)]

    def step(self, actions):
        self.last_actions = actions
        self.finished = self._finish
        ranking = self._ranking or []
        players = [
            {"player_id": player_id, "placement": placement}
            for placement, player_id in enumerate(ranking, start=1)
        ]
        return (
            np.zeros((8, 12), dtype=np.float32),
            np.zeros(8, dtype=np.float32),
            self.finished,
            {"players": players},
        )

    def get_public_state(self):
        return {
            "finished": self.finished,
            "ranking": self._ranking or [],
            "players": [],
        }


def test_run_match_reports_all_eight_players_without_inventing_results():
    ranking = list(range(8))
    lobby = _FakeLobby(ranking=ranking)
    rows = run_match(
        factory=lambda seed: lobby,
        baseline=_FakePolicy(),
        candidate=_FakePolicy(),
        candidate_slots={0, 1, 2, 3},
        seed=123,
        device=torch.device("cpu"),
        max_steps=2,
    )

    assert len(rows) == 8
    assert {row["player_id"] for row in rows} == set(range(8))
    assert all(row["placement"] in range(1, 9) for row in rows)
    assert sum(row["win"] for row in rows) == 1
    assert sum(row["placement"] <= 4 for row in rows) == 4


def test_run_match_rejects_incomplete_final_ranking():
    lobby = _FakeLobby(ranking=[0, 1, 2, 3, 4, 5, 6])

    with pytest.raises(RuntimeError, match="não vou inferir rankings ausentes"):
        run_match(
            factory=lambda seed: lobby,
            baseline=_FakePolicy(),
            candidate=_FakePolicy(),
            candidate_slots={0, 1, 2, 3},
            seed=123,
            device=torch.device("cpu"),
            max_steps=2,
        )


def test_run_match_rejects_match_that_exceeds_step_limit():
    lobby = _FakeLobby(ranking=list(range(8)), finish=False)

    with pytest.raises(RuntimeError, match="excedeu max_steps"):
        run_match(
            factory=lambda seed: lobby,
            baseline=_FakePolicy(),
            candidate=_FakePolicy(),
            candidate_slots={0, 1, 2, 3},
            seed=123,
            device=torch.device("cpu"),
            max_steps=1,
        )



def test_strategic_audit_captures_gold_from_native_snapshot():
    class FakeLobby:
        def get_audit_snapshot(self):
            return {"players": [{"player_id": 0, "gold": 9}, {"player_id": 1, "gold": 20}]}

        def get_public_state(self):
            raise AssertionError("audit snapshot should already contain gold")

    assert _player_gold(FakeLobby()) == {0: 9, 1: 20}


def test_strategic_audit_records_exact_masks_and_action_components():
    assert strategic_action_dict([5, 4, 8, 27, 6, 19]) == {
        "type": 5,
        "shop_slot": 4,
        "bench_slot": 8,
        "board_target": 27,
        "board_source": 6,
        "conditioned_board_target": 19,
    }
    assert _json_masks({
        "type_mask": np.array([1, 0, 1], dtype=np.float32),
        "shop_mask": np.array([False, True]),
    }) == {"type_mask": [1, 0, 1], "shop_mask": [0, 1]}



def _seed_rows(seed, candidate_placements, baseline_placements):
    rows = []
    for version, placements, player_ids in (
        ("baseline", baseline_placements, range(4, 8)),
        ("candidate", candidate_placements, range(0, 4)),
    ):
        for player_id, placement in zip(player_ids, placements):
            rows.append({
                "seed": seed,
                "player_id": player_id,
                "version": version,
                "placement": placement,
                "win": int(placement == 1),
            })
    return rows


def test_metric_summary_reports_item_usage_and_action_rate():
    from scripts.evaluate_checkpoints import _metric_summary

    summary = _metric_summary([
        {"placement": 1, "win": 1, "actions": 10, "item_actions": 3,
         "equip_actions": 2, "craft_and_equip_actions": 1},
        {"placement": 4, "win": 0, "actions": 10, "item_actions": 1,
         "equip_actions": 1, "craft_and_equip_actions": 0},
    ])
    assert summary["actions"] == 20
    assert summary["item_actions"] == 4
    assert summary["item_action_rate"] == 0.2
    assert summary["equip_actions"] == 3
    assert summary["craft_and_equip_actions"] == 1


def test_paired_seed_summary_reports_deltas_and_bootstrap_interval():
    rows = (
        _seed_rows(100, [1, 2, 3, 4], [5, 6, 7, 8])
        + _seed_rows(101, [1, 2, 3, 4], [4, 5, 6, 7])
    )
    report = summarize_paired_seeds(rows, bootstrap_samples=500, bootstrap_seed=7)

    assert report["seed_count"] == 2
    assert report["baseline"]["mean_placement"] == 6.0
    assert report["candidate"]["mean_placement"] == 2.5
    placement_delta = report["paired_delta_candidate_minus_baseline"]["mean_placement"]
    assert placement_delta["mean"] < 0
    assert placement_delta["bootstrap_95_ci"][1] < 0
    assert len(report["per_seed"]) == 2
    assert report["per_seed"][0]["seed"] == 100


def test_paired_seed_summary_refuses_missing_players_instead_of_inventing_results():
    rows = _seed_rows(100, [1, 2, 3, 4], [5, 6, 7, 8])
    rows.pop()

    with pytest.raises(ValueError, match="exactly four players per policy"):
        summarize_paired_seeds(rows)


def test_paired_seed_summary_rejects_unknown_policy_labels():
    rows = _seed_rows(100, [1, 2, 3, 4], [5, 6, 7, 8])
    rows[0]["version"] = "unknown"

    with pytest.raises(ValueError, match="Unknown policy version"):
        summarize_paired_seeds(rows)


def test_candidate_seat_rotation_is_deterministic_and_balances_all_eight_slots():
    schedules = [candidate_slots_for_seed(seed, master_seed=91) for seed in range(8)]
    assert schedules == [candidate_slots_for_seed(seed, master_seed=91) for seed in range(8)]
    assert all(len(slots) == 4 for slots in schedules)
    appearances = {player_id: 0 for player_id in range(8)}
    for slots in schedules:
        for player_id in slots:
            appearances[player_id] += 1
    assert appearances == {player_id: 4 for player_id in range(8)}


def test_candidate_slot_validation_rejects_duplicates_invalid_ids_and_booleans():
    assert validate_candidate_slots({0, 1, 2, 3}) == {0, 1, 2, 3}
    with pytest.raises(ValueError, match="exactly four"):
        validate_candidate_slots({0, 1, 2})
    with pytest.raises(ValueError, match="exactly four"):
        validate_candidate_slots({0, 1, 2, 2})
    with pytest.raises(ValueError, match="exactly four"):
        validate_candidate_slots({0, 1, 2, 8})
    with pytest.raises(ValueError, match="exactly four"):
        validate_candidate_slots({False, 1, 2, 3})


def test_paired_summary_rejects_duplicate_or_overlapping_player_identity():
    rows = _seed_rows(500, [1, 2, 3, 4], [5, 6, 7, 8])
    rows[-1]["player_id"] = 2
    with pytest.raises(ValueError, match="distinct player IDs"):
        summarize_paired_seeds(rows)


def test_paired_summary_rejects_same_player_assigned_to_both_policies():
    rows = _seed_rows(501, [1, 2, 3, 4], [5, 6, 7, 8])
    rows[-1]["player_id"] = 4
    with pytest.raises(ValueError, match="distinct player IDs|assigns a player"):
        summarize_paired_seeds(rows)


def _evaluation_artifact(checkpoint_sha):
    contract = {
        "contract_id": "tft.ppo-checkpoint-lineage.v1",
        "version": 1,
        "components": {
            "action_mask_contract": {"contract_id": "action-mask-v1"},
            "critic_mask_input_contract": {"contract_id": "critic-mask-v1"},
            "semantic_state_contract": {"contract_id": "semantic-state-v1"},
            "reward_contract": {"contract_id": "reward-v1"},
        },
        "policy_state_signature": [{"name": "actor.weight", "shape": [4, 3], "dtype": "torch.float32"}],
    }
    canonical = json.dumps(
        contract, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return {
        "checkpoint_sha256": checkpoint_sha,
        "checkpoint_contract": {
            "manifest_version": 1,
            "contract": contract,
            "sha256": hashlib.sha256(canonical).hexdigest(),
        },
    }


def test_paired_evaluation_enforces_lineage_and_emits_rotated_reproducible_results():
    artifact = _evaluation_artifact("a" * 64)
    result = run_paired_evaluation(
        factory=lambda seed: _FakeLobby(ranking=list(range(8))),
        baseline=_FakePolicy(),
        candidate=_FakePolicy(),
        baseline_artifact=artifact,
        candidate_artifact=artifact,
        seeds=[100, 101, 102, 103],
        device=torch.device("cpu"),
        split="validation",
        master_seed=17,
        max_steps=2,
    )
    assert result["evaluation_mode"] == "evaluation_only"
    assert result["split"] == "validation"
    assert result["summary"]["seed_count"] == 4
    assert len(result["raw_results"]) == 32
    assert len(result["seat_rotation"]) == 4
    assert all(len(item["candidate_player_ids"]) == 4 for item in result["seat_rotation"])


def test_paired_evaluation_rejects_semantically_different_checkpoint_lineages():
    baseline = _evaluation_artifact("a" * 64)
    candidate = _evaluation_artifact("b" * 64)
    candidate["checkpoint_contract"]["contract"]["components"]["reward_contract"] = {
        "contract_id": "reward-v2"
    }
    contract = candidate["checkpoint_contract"]["contract"]
    candidate["checkpoint_contract"]["sha256"] = hashlib.sha256(
        json.dumps(contract, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    with pytest.raises(ValueError, match="not semantically compatible"):
        run_paired_evaluation(
            factory=lambda seed: _FakeLobby(ranking=list(range(8))),
            baseline=_FakePolicy(),
            candidate=_FakePolicy(),
            baseline_artifact=baseline,
            candidate_artifact=candidate,
            seeds=[1],
            device=torch.device("cpu"),
            split="test",
            max_steps=2,
        )


def test_paired_evaluation_rejects_tampered_lineage_hash_and_duplicate_seeds():
    artifact = _evaluation_artifact("a" * 64)
    tampered = copy.deepcopy(artifact)
    tampered["checkpoint_contract"]["contract"]["version"] = 2
    with pytest.raises(ValueError, match="hash does not match"):
        run_paired_evaluation(
            factory=lambda seed: _FakeLobby(ranking=list(range(8))),
            baseline=_FakePolicy(),
            candidate=_FakePolicy(),
            baseline_artifact=artifact,
            candidate_artifact=tampered,
            seeds=[1],
            device=torch.device("cpu"),
            split="test",
            max_steps=2,
        )
    with pytest.raises(ValueError, match="non-empty and unique"):
        run_paired_evaluation(
            factory=lambda seed: _FakeLobby(ranking=list(range(8))),
            baseline=_FakePolicy(),
            candidate=_FakePolicy(),
            baseline_artifact=artifact,
            candidate_artifact=artifact,
            seeds=[1, 1],
            device=torch.device("cpu"),
            split="test",
            max_steps=2,
        )


def test_evaluation_artifacts_are_hash_linked_and_never_overwritten(tmp_path):
    result = {
        "evaluation_mode": "evaluation_only",
        "split": "test",
        "baseline_checkpoint_sha256": "a" * 64,
        "candidate_checkpoint_sha256": "b" * 64,
        "checkpoint_lineage_sha256": "c" * 64,
        "raw_results": [
            {"seed": 9, "player_id": 0, "version": "candidate", "placement": 2,
             "win": 0, "actions": 12, "item_actions": 2,
             "equip_actions": 1, "craft_and_equip_actions": 1}
        ],
        "summary": {"seed_count": 1},
    }
    manifest = {
        "experiment_id": "paired-test-001",
        "code_revision": "d" * 40,
        "engine_build": "native-build-001",
        "catalog_sha256": "e" * 64,
        "split_manifest_sha256": "f" * 64,
        "split": "test",
        "baseline_checkpoint_sha256": "a" * 64,
        "candidate_checkpoint_sha256": "b" * 64,
        "primary_metric": "mean_placement",
        "practical_effect_threshold": 0.15,
    }

    output = tmp_path / "evaluation-001"
    written = write_paired_evaluation_artifacts(result, manifest, output)

    raw = json.loads((output / "raw_results.json").read_text(encoding="utf-8"))
    summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    report = json.loads((output / "report.json").read_text(encoding="utf-8"))
    assert raw == result["raw_results"]
    assert summary == result["summary"]
    assert report["sha256"]["raw_results_sha256"] == hashlib.sha256(
        json.dumps(raw, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    assert report["sha256"]["experiment_manifest_sha256"] == written["report"]["sha256"]["experiment_manifest_sha256"]
    with pytest.raises(FileExistsError):
        write_paired_evaluation_artifacts(result, manifest, output)


def test_evaluation_artifact_writer_rejects_missing_or_mismatched_manifest(tmp_path):
    result = {
        "evaluation_mode": "evaluation_only", "split": "validation",
        "baseline_checkpoint_sha256": "a" * 64,
        "candidate_checkpoint_sha256": "b" * 64,
        "checkpoint_lineage_sha256": "c" * 64,
        "raw_results": [{"seed": 1}], "summary": {"seed_count": 1},
    }
    with pytest.raises(ValueError, match="experiment manifest is missing"):
        write_paired_evaluation_artifacts(result, {}, tmp_path / "missing")
    manifest = {
        "experiment_id": "mismatch", "code_revision": "d" * 40,
        "engine_build": "build", "catalog_sha256": "e" * 64,
        "split_manifest_sha256": "f" * 64, "split": "test",
        "baseline_checkpoint_sha256": "a" * 64,
        "candidate_checkpoint_sha256": "b" * 64,
        "primary_metric": "mean_placement", "practical_effect_threshold": 0.1,
    }
    with pytest.raises(ValueError, match="split does not match"):
        write_paired_evaluation_artifacts(result, manifest, tmp_path / "mismatch")
