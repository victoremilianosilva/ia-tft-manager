"""Behavioral parity tests for Python RewardManager and native RewardManager."""
import math
import os
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
for d in (ROOT / "cpp" / "build" / "bin", ROOT / "cpp" / "build" / "bin" / "Release"):
    if d.exists():
        sys.path.insert(0, str(d))
if os.environ.get("REQUIRE_CPP_PARITY") == "1":
    import tft_engine as cpp
else:
    pytest.importorskip("tft_engine")
    import tft_engine as cpp
from ai.RewardManager import RewardManager as PythonRewardManager

def close(a, b, label):
    assert math.isclose(float(a), float(b), rel_tol=1e-7, abs_tol=1e-7), f"{label}: Python={a}, C++={b}"

def compare_state(py, native, label):
    ps, ns = py.get_state(), native.get_state()
    assert ps.keys() == ns.keys(), f"{label}: state keys differ"
    for key in ps:
        close(ps[key], ns[key], f"{label}.{key}")

def test_all_reward_components_and_state_match():
    py, native = PythonRewardManager(None, None, None), cpp.RewardManager()
    scenarios = [
        dict(won=True, damage_dealt=13, damage_taken=0, enemy_alive=2, own_alive=3),
        dict(won=False, damage_dealt=0, damage_taken=24, enemy_alive=1, own_alive=0),
        dict(won=True, damage_dealt=0, damage_taken=0, enemy_alive=0, own_alive=5),
    ]
    for i, s in enumerate(scenarios):
        close(py.calculate_combat_reward(**s), native.calculate_combat_reward(**s), f"combat[{i}]")
        compare_state(py, native, f"combat-state[{i}]")

    for i, power in enumerate((0.0, 10.0, 10.0, 4.0, 1000.0)):
        close(py.calculate_power_reward(power), native.calculate_power_reward(power), f"power[{i}]")
    for i, score in enumerate((0.0, 1.0, 1.0, -0.5, 20.0)):
        close(py.calculate_synergy_reward(score), native.calculate_synergy_reward(score), f"synergy[{i}]")
    for i, score in enumerate((0.0, 0.2, 0.7, -0.1)):
        close(py.calculate_positioning_reward(score), native.calculate_positioning_reward(score), f"positioning[{i}]")
    for level in (1, 2, 4, 3, 8, 1):
        close(py.calculate_level_reward(level), native.calculate_level_reward(level), f"level[{level}]")
    for gold, level, hp in ((0, 1, 100), (10, 2, 50), (50, 8, 100), (20, 4, 30), (30, 5, 15)):
        close(py.calculate_economy_reward(gold, level, hp), native.calculate_economy_reward(gold, level, hp), f"economy[{gold},{level},{hp}]")
    for wins, losses in ((0,0),(2,0),(5,0),(0,2),(0,9),(3,4)):
        close(py.calculate_streak_reward(wins, losses), native.calculate_streak_reward(wins, losses), f"streak[{wins},{losses}]")
    for occupied, total in ((0,28),(1,28),(14,28),(28,28),(2,0)):
        close(py.calculate_board_reward([object()] * occupied, total), native.calculate_board_reward(occupied, total), f"board[{occupied},{total}]")
    for kind in ("BUY","REROLL","BUY_XP","MOVE_BENCH","MOVE_BOARD","SELL","PASS"):
        for success, value in ((True,0.0),(True,0.25),(False,3.0)):
            close(py.calculate_action_reward(kind, success, value), native.calculate_action_reward(kind, success, value), f"action[{kind},{success},{value}]")

    totals = [
        dict(combat_reward=2.5, power_reward=.2, synergy_reward=.3, positioning_reward=.1,
             level_reward=.5, economy_reward=.2, streak_reward=.1, board_reward=.15, action_reward=.05),
        dict(combat_reward=-8.0, action_reward=-.1),
        dict(combat_reward=10.0),
    ]
    for i, args in enumerate(totals):
        close(py.calculate_total_reward(**args), native.calculate_total_reward(**args), f"total[{i}]")
        compare_state(py, native, f"total-state[{i}]")

    py.reset()
    native.reset()
    compare_state(py, native, "reset")

def test_total_reward_clamps_each_round_but_accumulates_clamped_value():
    py, native = PythonRewardManager(None, None, None), cpp.RewardManager()
    for args in (dict(combat_reward=100), dict(combat_reward=-100), dict(action_reward=1.25)):
        close(py.calculate_total_reward(**args), native.calculate_total_reward(**args), "clamp")
        compare_state(py, native, "clamp-state")
    state = py.get_state()
    assert state["round_reward"] == 1.25
    assert state["total_reward"] == 1.25 - 5.0 + 5.0
