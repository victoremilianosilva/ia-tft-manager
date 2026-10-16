"""Terminal integration coverage for native lobby ranking and placement rewards."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
for module_dir in (
    ROOT / "cpp" / "build" / "bin",
    ROOT / "cpp" / "build" / "bin" / "Release",
):
    if module_dir.exists():
        import sys
        sys.path.insert(0, str(module_dir))

pytest.importorskip("tft_engine", reason="Build native TFT engine to test terminal ranking")
from tft_engine import TFTLobby  # noqa: E402

CATALOG_PATH = ROOT / "units_gerado.json"


def test_native_match_finishes_with_unique_ordered_placements_and_one_reward_each():
    """Move each starter to board, pass rounds, and verify the true terminal state."""
    assert CATALOG_PATH.is_file()
    engine = TFTLobby(20261016, str(CATALOG_PATH))
    try:
        engine.reset(20261016)
        cumulative_placement_rewards = np.zeros(8, dtype=np.float64)
        saw_combat = False
        saw_elimination = False

        # Deploy each player's real starter using the legal conditional mask.
        masks = engine.get_action_masks()
        actions = []
        for player_id, mask in enumerate(masks):
            targets = np.asarray(mask["bench_to_board_target_masks"], dtype=np.bool_)
            valid = np.argwhere(targets)
            if bool(mask["type_mask"][3]) and len(valid):
                source, target = map(int, valid[0])
                actions.append([3, 0, source, target, 0, 0])
            else:
                actions.append([6, 0, 0, 0, 0, 0])
        result = engine.step(actions)
        cumulative_placement_rewards += np.asarray(
            result["placement_rewards"], dtype=np.float64
        )

        # A legal PASS from every player closes each preparation phase. With
        # deployed units, combat and stage damage eventually produce a terminal lobby.
        for _ in range(500):
            if engine.is_done():
                break
            result = engine.step([[6, 0, 0, 0, 0, 0] for _ in range(8)])
            cumulative_placement_rewards += np.asarray(
                result["placement_rewards"], dtype=np.float64
            )
            events = result.get("events", [])
            saw_combat |= any(str(event).startswith("COMBAT:") for event in events)
            saw_elimination |= any(str(event).startswith("ELIMINATED:") for event in events)
        else:
            pytest.fail("Native lobby did not finish within 500 PASS transitions")

        state = engine.get_public_state()
        assert state["finished"] is True
        assert saw_combat, "The terminal test must exercise real combat"
        assert saw_elimination, "The terminal test must exercise player elimination"

        ranking = [int(player_id) for player_id in state["ranking"]]
        assert len(ranking) == 8
        assert set(ranking) == set(range(8)), "Ranking must contain every player exactly once"

        players = state["players"]
        placements = {
            int(player["player_id"]): int(player["placement"])
            for player in players
        }
        assert sorted(placements.values()) == list(range(1, 9))
        assert ranking == sorted(range(8), key=lambda player_id: placements[player_id])
        assert int(state["winner_id"]) == ranking[0]
        assert placements[ranking[0]] == 1

        expected_rewards = {
            player_id: 1.0 - 2.0 * ((placement - 1) / 7.0)
            for player_id, placement in placements.items()
        }
        for player_id in range(8):
            assert cumulative_placement_rewards[player_id] == pytest.approx(
                expected_rewards[player_id], abs=2e-5
            ), f"Player {player_id} placement reward missing or duplicated"
    finally:
        engine.close()
