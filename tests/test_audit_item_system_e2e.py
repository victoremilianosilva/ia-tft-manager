import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
import torch

from policy import TFTPolicy
from scripts.audit_item_system_e2e import (
    ACTION_DIMS,
    action_dict,
    run_audit,
    validate_action,
    validate_masks,
)


def make_masks(pass_only=True):
    masks = {
        "type_mask": np.zeros(9, dtype=np.bool_),
        "shop_mask": np.ones(5, dtype=np.bool_),
        "bench_source_mask": np.ones(9, dtype=np.bool_),
        "board_target_mask": np.ones(28, dtype=np.bool_),
        "board_source_mask": np.ones(28, dtype=np.bool_),
        "board_move_target_masks": np.ones((28, 28), dtype=np.bool_),
        "bench_move_source_mask": np.ones(9, dtype=np.bool_),
        "bench_to_board_target_masks": np.ones((9, 28), dtype=np.bool_),
        "item_inventory_mask": np.ones(9, dtype=np.bool_),
        "item_component_first_mask": np.ones(10, dtype=np.bool_),
        "item_component_pair_masks": np.ones((10, 10), dtype=np.bool_),
        "item_target_mask": np.ones(37, dtype=np.bool_),
    }
    masks["type_mask"][6 if pass_only else 7] = True
    if not pass_only:
        masks["type_mask"][8] = True
    return masks


class FakeLobby:
    def __init__(self, seed=0, complete=True):
        self.seed = seed
        self.complete = complete
        self.finished = False
        self.players = [type("Player", (), {"alive": True})() for _ in range(8)]
        self.closed = False

    def reset(self):
        return np.zeros((8, 252), dtype=np.float32)

    def get_action_masks(self):
        return [make_masks() for _ in range(8)]

    def step(self, actions):
        self.finished = self.complete
        return (
            np.zeros((8, 252), dtype=np.float32),
            np.zeros(8, dtype=np.float32),
            self.complete,
            {"round": 1, "events": []},
        )

    def get_public_state(self):
        return {"ranking": [{"player_id": player_id} for player_id in range(8)]}

    def close(self):
        self.closed = True


class ItemSystemE2EAuditTests(unittest.TestCase):
    def test_mask_contract_checks_all_eight_players(self):
        result = validate_masks([make_masks() for _ in range(8)])
        self.assertEqual(result["players"], 8)
        self.assertEqual(result["mask_arrays_checked"], 12 * 8)
        with self.assertRaisesRegex(ValueError, "shape"):
            bad = make_masks()
            bad["item_target_mask"] = np.ones(36, dtype=np.bool_)
            validate_masks([bad] + [make_masks() for _ in range(7)])

    def test_item_action_contract_and_native_argument_mapping(self):
        masks = make_masks(pass_only=False)
        validate_action([7, 2, 12, 0, 0, 0], masks, 0)
        self.assertEqual(action_dict([7, 2, 12, 0, 0, 0])["item_slot"], 2)
        self.assertEqual(action_dict([8, 3, 4, 19, 0, 0])["component_second"], 4)
        with self.assertRaisesRegex(ValueError, "item_target"):
            validate_action([7, 2, 37, 0, 0, 0], masks, 0)

    def _checkpoint(self, path):
        policy = TFTPolicy(252, ACTION_DIMS)
        torch.save({"policy": policy.state_dict(), "update": 123}, path)

    def test_complete_match_writes_checkpoint_trace_and_metrics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint = root / "policy.pt"
            self._checkpoint(checkpoint)
            instances = []

            def factory(seed):
                lobby = FakeLobby(seed=seed, complete=True)
                instances.append(lobby)
                return lobby

            report = run_audit(checkpoint, root / "out", env_factory=factory, max_steps=2)
            self.assertEqual(report["status"], "passed")
            self.assertTrue(report["complete_match"])
            self.assertEqual(len(report["placements"]), 8)
            self.assertTrue((root / "out" / "trace.jsonl").is_file())
            persisted = json.loads((root / "out" / "audit.json").read_text(encoding="utf-8"))
            self.assertEqual(persisted["status"], "passed")
            self.assertTrue(instances[0].closed)

    def test_truncated_match_is_failure_not_success(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint = root / "policy.pt"
            self._checkpoint(checkpoint)

            with self.assertRaisesRegex(RuntimeError, "não terminou"):
                run_audit(
                    checkpoint,
                    root / "out",
                    env_factory=lambda seed: FakeLobby(seed=seed, complete=False),
                    max_steps=1,
                )
            persisted = json.loads((root / "out" / "audit.json").read_text(encoding="utf-8"))
            self.assertEqual(persisted["status"], "failed")
            self.assertFalse(persisted["complete_match"])


def test_item_composition_audit_reports_all_players_and_inventory():
    from scripts.audit_item_composition_learning import audit_records

    rows = []
    for player_id in range(8):
        rows.append({
            "player_id": player_id,
            "selected_action": [0, 0, 0, 0, 0, 0],
            "board_after": [{"occupied": True, "star": 2, "item_ids": ["TFT_Item_Deathblade"]}],
            "bench_after": [],
            "item_inventory_after": ["TFT_Item_GargoyleStoneplate"],
            "item_components_after": ["TFT_Item_Component_Sword"],
            "strategy_after": {"composition_direction": "Invoker", "core_units": ["Carry"]},
        })
    report = audit_records(rows)
    assert report["all_players_present"]
    assert report["item_evidence_available"]
    assert report["players"]["0"]["board_item_instances"] == 1
    assert report["players"]["0"]["bag_item_instances"] == 1
    assert report["players"]["0"]["component_instances"] == 1


if __name__ == "__main__":
    unittest.main()
