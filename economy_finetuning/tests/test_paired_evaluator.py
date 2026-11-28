import unittest
import tempfile
from pathlib import Path

import numpy as np
import torch

from economy_finetuning.finetune import (
    MASK_SHAPES, _flatten_masks, _load_checkpoint, _rollout_snapshot_metadata,
)
from action_contract import (
    MASK_SNAPSHOT_HASH_ALGORITHM,
    build_action_mask_checkpoint_contract,
    build_critic_mask_input_checkpoint_contract,
)
from reward_contract import build_reward_checkpoint_contract
from policy import ACTION_DIMS, TFTPolicy
from semantic_observation import (
    SEMANTIC_ENTITY_SLOTS, SEMANTIC_NUMERIC_DIM, SEMANTIC_STATE_CONTRACT_ID,
    catalog_identity, semantic_item_state_tensors, build_semantic_state_checkpoint_contract,
)
from rollout import RolloutBuffer
from economy_finetuning.paired_evaluator import (
    aggregate_mirrored_runs,
    compare_final_metrics,
    extract_final_metrics,
    masks_sha256,
    mirrored_policy_variants,
    validate_evaluation_checkpoint_contracts,
)


class PairedEvaluatorTests(unittest.TestCase):
    def test_policy_subgroups_can_flatten_four_player_masks(self):
        masks = [
            {key: np.ones(shape, dtype=np.int8) for key, shape in MASK_SHAPES.items()}
            for _ in range(4)
        ]
        flattened = _flatten_masks(masks, torch.device("cpu"))
        self.assertEqual(flattened["type_mask"].shape[0], 4)

    def test_action_mask_hash_is_stable_and_detects_mask_changes(self):
        masks = [
            {"type_mask": [1, 0, 1], "bench_mask": [0, 1]},
            {"type_mask": [0, 1, 0], "bench_mask": [1, 0]},
        ]
        self.assertEqual(masks_sha256(masks), masks_sha256(masks))
        changed = [
            {"type_mask": [1, 0, 1], "bench_mask": [0, 1]},
            {"type_mask": [0, 1, 1], "bench_mask": [1, 0]},
        ]
        self.assertNotEqual(masks_sha256(masks), masks_sha256(changed))

    def test_terminal_ranking_and_fresh_audit_board_metrics_are_joined(self):
        public_state = {
            "finished": True,
            "ranking": [2, 0, 1],
            "players": [
                {"player_id": 0, "placement": None, "hp": 35, "gold": 80, "level": 8,
                 "board_quality_score": 0.0},
                {"player_id": 1, "placement": 3, "hp": 20, "gold": 60, "level": 7},
                {"player_id": 2, "placement": 1, "hp": 50, "gold": 40, "level": 9},
            ],
        }
        audit_snapshot = {
            "players": [
                {"player_id": 0, "board_power": 40, "board_quality_score": 0.35,
                 "board_positional_score": 0.20, "board_structural_score": 0.15},
            ],
        }
        metrics = extract_final_metrics(public_state, audit_snapshot)
        player_zero = next(item for item in metrics if item["player_id"] == 0)
        self.assertEqual(player_zero["placement"], 2)
        self.assertEqual(player_zero["top4"], True)
        self.assertAlmostEqual(player_zero["board_quality_score"], 0.35)
        self.assertAlmostEqual(player_zero["board_structural_score"], 0.15)

    def test_mirrored_mixed_lobbies_pair_same_seat_and_policy_cohorts(self):
        def make_run(variants, mirror):
            metrics = []
            rewards = []
            counts = []
            for player_id, variant in enumerate(variants):
                if mirror:
                    placement = player_id // 2 + (1 if variant == "finetuned" else 5)
                else:
                    placement = player_id // 2 + (1 if variant == "finetuned" else 5)
                metrics.append({
                    "player_id": player_id,
                    "policy_variant": variant,
                    "placement": placement,
                    "top4": placement <= 4,
                    "hp": 50 if variant == "finetuned" else 20,
                    "gold": 70, "level": 8, "board_power": 40,
                    "board_quality_score": 0.3, "board_positional_score": 0.2,
                    "board_structural_score": 0.1,
                })
                rewards.append(10.0 if variant == "finetuned" else 5.0)
                counts.append({"BUY_XP": 1})
            return {
                "seed": 99, "steps": 250, "completed": True,
                "policy_variants": variants,
                "initial_observation_sha256": "same-observation",
                "initial_masks_sha256": "same-masks",
                "total_rewards": rewards,
                "action_counts": counts,
                "final_metrics": metrics,
            }

        variants_a = ["finetuned" if i % 2 == 0 else "original" for i in range(8)]
        variants_b = ["original" if i % 2 == 0 else "finetuned" for i in range(8)]
        row = aggregate_mirrored_runs(
            make_run(variants_a, False),
            make_run(variants_b, True),
            {"evaluation_mode": "mixed_4v4_mirrored_seats"},
        )
        self.assertTrue(row["both_completed"])
        self.assertTrue(row["same_initial_state"])
        self.assertAlmostEqual(row["mean_reward_delta"], 5.0)
        self.assertEqual(len(row["final_player_deltas"]), 8)
        self.assertTrue(all(item["placement_delta"] == -4 for item in row["final_player_deltas"]))


    def test_seed_rotated_mirror_schedule_is_balanced_deterministic_and_complementary(self):
        first_a, first_b = mirrored_policy_variants(20261105)
        repeated_a, repeated_b = mirrored_policy_variants(20261105)
        next_a, next_b = mirrored_policy_variants(20261106)

        self.assertEqual(first_a, repeated_a)
        self.assertEqual(first_b, repeated_b)
        self.assertEqual(first_b, ["original" if value == "finetuned" else "finetuned" for value in first_a])
        self.assertEqual(first_a.count("finetuned"), 4)
        self.assertEqual(first_b.count("finetuned"), 4)
        self.assertNotEqual(first_a, next_a)

    def test_evaluation_requires_matching_action_reward_and_semantic_contracts(self):
        catalog = {"TFT_TestChampion": 17}
        semantic = build_semantic_state_checkpoint_contract(catalog)
        payload = {
            "action_mask_contract": build_action_mask_checkpoint_contract(),
            "critic_mask_input_contract": build_critic_mask_input_checkpoint_contract(),
            "reward_contract": build_reward_checkpoint_contract(),
            "semantic_state_contract": semantic,
            "policy": {
                "critic_mask_encoder.weight": object(),
                "critic_mask_encoder.bias": object(),
                "semantic_id_embedding.weight": object(),
                "semantic_trait_embedding.weight": object(),
                "semantic_encoder.0.weight": object(),
                "semantic_encoder.0.bias": object(),
                "semantic_encoder.2.weight": object(),
                "semantic_encoder.2.bias": object(),
            },
        }
        status = validate_evaluation_checkpoint_contracts(payload, catalog)
        self.assertEqual(status, {
            "action_mask": "validated",
            "critic_mask_input": "validated",
            "reward": "validated",
            "semantic_state": "validated",
        })

        incompatible = dict(payload)
        incompatible["reward_contract"] = {"contract_id": "wrong", "version": 1, "sha256": "0" * 64}
        with self.assertRaises(ValueError):
            validate_evaluation_checkpoint_contracts(incompatible, catalog)

    def test_evaluation_rejects_unversioned_checkpoint_without_explicit_opt_in(self):
        with self.assertRaisesRegex(ValueError, "Action/Mask Contract"):
            validate_evaluation_checkpoint_contracts({"policy": {}}, {"TFT_TestChampion": 17})

    def test_paired_evaluation_rejects_legacy_checkpoint_without_explicit_v6_warm_start(self):
        payload = {
            "action_mask_contract": build_action_mask_checkpoint_contract(),
            "critic_mask_input_contract": build_critic_mask_input_checkpoint_contract(),
            "reward_contract": build_reward_checkpoint_contract(),
            "policy": {
                "critic_mask_encoder.weight": object(),
                "critic_mask_encoder.bias": object(),
            },
        }
        with self.assertRaisesRegex(ValueError, "semantic_state v6"):
            validate_evaluation_checkpoint_contracts(payload, {"TFT_TestChampion": 17})

    def test_compare_final_metrics_uses_finetuned_minus_original(self):
        original = [{
            "player_id": 0, "placement": 6, "top4": False, "hp": 10,
            "gold": 100, "level": 7, "board_power": 25,
            "board_quality_score": 0.1, "board_positional_score": 0.05,
            "board_structural_score": 0.05,
        }]
        tuned = [{
            "player_id": 0, "placement": 3, "top4": True, "hp": 35,
            "gold": 70, "level": 8, "board_power": 40,
            "board_quality_score": 0.3, "board_positional_score": 0.1,
            "board_structural_score": 0.2,
        }]
        delta = compare_final_metrics(original, tuned)[0]
        self.assertEqual(delta["placement_delta"], -3)
        self.assertEqual(delta["top4_delta"], 1)
        self.assertEqual(delta["hp_delta"], 25)
        self.assertAlmostEqual(delta["board_structural_score_delta"], 0.15)


    def test_economic_finetuning_loads_only_complete_semantic_v6_checkpoints(self):
        catalog = {"TFT_TestChampion": 0}
        policy = TFTPolicy(
            10000, ACTION_DIMS,
            semantic_vocab_size=catalog_identity(catalog)["vocab_size"],
            require_semantic_state=True,
        )
        payload = {
            "policy": policy.state_dict(),
            "action_mask_contract": build_action_mask_checkpoint_contract(),
            "critic_mask_input_contract": build_critic_mask_input_checkpoint_contract(),
            "reward_contract": build_reward_checkpoint_contract(),
            "semantic_state_contract": build_semantic_state_checkpoint_contract(catalog),
        }
        with tempfile.TemporaryDirectory() as directory:
            checkpoint_path = Path(directory) / "semantic-v6.pt"
            torch.save(payload, checkpoint_path)
            _, loaded, migrated = _load_checkpoint(
                checkpoint_path, 10000, torch.device("cpu"), catalog
            )

        self.assertFalse(migrated)
        self.assertTrue(loaded.require_semantic_state)


    def test_economic_finetuning_binds_decision_result_and_next_semantic_rows(self):
        raw_masks = [
            {key: np.ones(shape, dtype=np.bool_) for key, shape in MASK_SHAPES.items()}
            for _ in range(8)
        ]
        masks = _flatten_masks(raw_masks, torch.device("cpu"))
        decision_rows = [
            {
                "engine_instance_id": "engine-a", "episode_id": 7,
                "decision_sequence": 10, "player_decision_sequence": 20 + i,
                "player_id": i, "lobby_index": 0, "round": 3,
            }
            for i in range(8)
        ]
        next_rows = [
            {
                "engine_instance_id": "engine-a", "episode_id": 7,
                "decision_sequence": 11, "player_decision_sequence": 21 + i,
                "player_id": i, "lobby_index": 0, "round": 3,
            }
            for i in range(8)
        ]
        traces = [
            {"player_id": i, "requested_action": [6, 0, 0, 0, 0, 0],
             "effective_action": [6, 0, 0, 0, 0, 0], "handler_applied": True,
             "status_reason": "accepted"}
            for i in range(8)
        ]

        events = [
            {
                "contract_id": "tft.engine.action-outcome-event",
                "contract_version": 1,
                "event_id": f"engine-a/episode/7/decision/{20 + i}/player/{i}/action",
                "engine_instance_id": "engine-a",
                "episode_id": 7,
                "player_id": i,
                "source_player_decision_sequence": 20 + i,
                "outcome_player_decision_sequence": 21 + i,
                "requested_action": [6, 0, 0, 0, 0, 0],
                "normalized_action": [6, 0, 0, 0, 0, 0],
                "effective_action": [6, 0, 0, 0, 0, 0],
                "mask_permitted": True,
                "preflight_accepted": True,
                "handler_applied": True,
                "decision_advanced": True,
                "execution_status": "applied",
                "affected_unit_uuids": [],
                "status_reason": "accepted",
            }
            for i in range(8)
        ]
        decision, result, next_state = _rollout_snapshot_metadata(
            {"snapshot_metadata": decision_rows},
            {"snapshot_metadata": next_rows},
            masks,
            traces,
            events,
        )

        self.assertEqual(len(decision), 8)
        self.assertEqual(len(result), 8)
        self.assertEqual(len(next_state), 8)
        self.assertEqual(decision[3]["player_id"], 3)
        self.assertEqual(result[3]["action_trace"]["player_id"], 3)
        self.assertEqual(result[3]["action_outcome_event"]["player_id"], 3)
        self.assertEqual(next_state[3]["decision_sequence"], 11)
        self.assertEqual(len(decision[3]["mask_snapshot_hash"]), 64)

        entity_identity = {
            "occupied": tuple([False] * SEMANTIC_ENTITY_SLOTS),
            "unit_uuids": tuple([""] * SEMANTIC_ENTITY_SLOTS),
            "shop_offer_revisions": (0, 0, 0, 0, 0),
        }
        for row in decision:
            row["semantic_entity_identity"] = entity_identity
            row["semantic_identity"] = {
                key: row[key] for key in (
                    "engine_instance_id", "episode_id", "decision_sequence",
                    "player_decision_sequence", "player_id", "round", "lobby_index",
                )
            }
            row["semantic_projection_hash"] = "a" * 64
            row["semantic_projection_contract_id"] = SEMANTIC_STATE_CONTRACT_ID
            row["semantic_projection_contract_hash"] = "b" * 64

        numeric = torch.zeros((8, SEMANTIC_NUMERIC_DIM), dtype=torch.float32)
        semantic_state = {
            "numeric": numeric,
            "items": semantic_item_state_tensors(numeric),
            "champion_ids": torch.zeros((8, SEMANTIC_ENTITY_SLOTS), dtype=torch.long),
            "entity_identity": [entity_identity] * 8,
            "identities": [row["semantic_identity"] for row in decision],
            "hashes": ["a" * 64] * 8,
            "contract_id": SEMANTIC_STATE_CONTRACT_ID,
            "contract_hash": "b" * 64,
        }
        buffer = RolloutBuffer(
            1, 8, 4, 6, torch.device("cpu"),
            mask_shapes=MASK_SHAPES, require_semantic_state=True,
        )
        actions = torch.tensor([[6, 0, 0, 0, 0, 0]] * 8, dtype=torch.long)
        buffer.add(
            torch.zeros((8, 4)), actions, torch.zeros(8), torch.zeros(8),
            torch.zeros(8), torch.zeros(8), masks,
            semantic_state=semantic_state,
            snapshot_metadata=decision,
            result_snapshot_metadata=result,
            next_snapshot_metadata=next_state,
        )
        self.assertEqual(buffer.ptr, 1)
        self.assertEqual(
            buffer.snapshot_metadata[0][3]["semantic_projection_hash"], "a" * 64
        )
        self.assertEqual(
            buffer.snapshot_metadata[0][3]["mask_snapshot_hash_algorithm"],
            MASK_SNAPSHOT_HASH_ALGORITHM,
        )

if __name__ == "__main__":
    unittest.main()
