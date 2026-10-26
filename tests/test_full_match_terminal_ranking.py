"""Terminal integration coverage for native lobby ranking and forced item choices."""
from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
for module_dir in (
    ROOT / "cpp" / "build" / "bin",
    ROOT / "cpp" / "build" / "bin" / "Release",
):
    if module_dir.exists():
        sys.path.insert(0, str(module_dir))

pytest.importorskip("tft_engine", reason="Build native TFT engine to test terminal ranking")
from tft_engine import TFTLobby  # noqa: E402

CATALOG_PATH = ROOT / "data" / "units_gerado.json"
PASS_ACTION = [6, 0, 0, 0, 0, 0]


def _legal_idle_action(mask: dict, player_id: int) -> list[int]:
    """Pass when legal; otherwise resolve the forced anvil exposed by native masks."""
    type_mask = np.asarray(mask["type_mask"], dtype=np.bool_)
    if type_mask.shape != (9,) or not type_mask.any():
        pytest.fail(f"Player {player_id} has an invalid/empty native action mask: {type_mask}")

    if type_mask[6]:
        return PASS_ACTION.copy()

    # A pending anvil is represented as the only enabled action type (7), with
    # an option index on the inventory head and target index 0 as a sentinel.
    if np.array_equal(np.flatnonzero(type_mask), np.array([7], dtype=np.int64)):
        options = np.flatnonzero(np.asarray(mask["item_inventory_mask"], dtype=np.bool_))
        targets = np.asarray(mask["item_target_mask"], dtype=np.bool_)
        if len(options) and targets.shape == (37,) and targets[0]:
            return [7, int(options[0]), 0, 0, 0, 0]
        pytest.fail(
            f"Player {player_id} has a forced item choice but incomplete masks: "
            f"options={options.tolist()}, target0={bool(targets[0]) if len(targets) else False}"
        )

    pytest.fail(
        f"Player {player_id} cannot PASS and has no recognized forced choice; "
        f"enabled action types={np.flatnonzero(type_mask).tolist()}"
    )


def _idle_actions(engine) -> list[list[int]]:
    masks = engine.get_action_masks()
    if len(masks) != 8:
        pytest.fail(f"Native engine returned {len(masks)} masks instead of eight")
    return [_legal_idle_action(mask, player_id) for player_id, mask in enumerate(masks)]


def test_native_match_finishes_with_unique_ordered_placements_and_one_reward_each():
    """Drive a complete match while resolving forced rewards through real action masks."""
    assert CATALOG_PATH.is_file()
    engine = TFTLobby(20261016, str(CATALOG_PATH))
    try:
        engine.reset(20261016)
        cumulative_placement_rewards = np.zeros(8, dtype=np.float64)
        saw_combat = False
        saw_elimination = False
        saw_component_anvil = False
        saw_completed_item_anvil = False

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
                actions.append(_legal_idle_action(mask, player_id))
        result = engine.step(actions)
        cumulative_placement_rewards += np.asarray(
            result["placement_rewards"], dtype=np.float64
        )

        for _ in range(500):
            if engine.is_done:
                break
            # Never blindly submit PASS: forced anvil states must be resolved
            # using the same masks the PPO policy receives.
            result = engine.step(_idle_actions(engine))
            cumulative_placement_rewards += np.asarray(
                result["placement_rewards"], dtype=np.float64
            )
            events = [str(event) for event in result.get("events", [])]
            saw_combat |= any(event.startswith("COMBAT:") for event in events)
            saw_elimination |= any(event.startswith("ELIMINATED:") for event in events)
            saw_component_anvil |= any(
                event.startswith("COMPONENT_ANVIL_GRANTED:") for event in events
            )
            saw_completed_item_anvil |= any(
                event.startswith("COMPLETED_ITEM_ANVIL_GRANTED:") for event in events
            )
        else:
            pytest.fail("Native lobby did not finish within 500 mask-valid transitions")

        state = engine.get_public_state()
        assert state["finished"] is True
        assert saw_combat, "The terminal test must exercise real combat"
        assert saw_elimination, "The terminal test must exercise player elimination"
        assert saw_component_anvil, "The complete match must resolve the 4-7 component anvil"

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
