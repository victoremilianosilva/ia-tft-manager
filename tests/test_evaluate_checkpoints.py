"""Regression tests for deterministic checkpoint evaluation helpers.

These tests avoid training and real checkpoint files. They validate action/mask
plumbing and ensure evaluation refuses incomplete match results instead of
silently manufacturing placements.
"""
from __future__ import annotations

import numpy as np
import pytest
import torch

from scripts.evaluate_checkpoints import (
    action_dict,
    as_mask_batch,
    policy_actions,
    run_match,
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
    masks = [{"type_mask": np.ones(7, dtype=np.bool_)} for _ in range(4)]

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
