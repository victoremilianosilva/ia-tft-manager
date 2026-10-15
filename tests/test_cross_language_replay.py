"""Cross-language replay tests for the Python lobby and native TFTEngine.

These tests intentionally run the same fixture through both public APIs. They
are not formula/golden-value tests: each step executes the real lobby engine,
then compares externally observable state and rewards.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import sys

import pytest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
# CMake's current output directory is cpp/build/bin. Keep the older Windows
# Release path supported for local builds that still use it.
for module_dir in (ROOT / "cpp" / "build" / "bin", ROOT / "cpp" / "build" / "bin" / "Release"):
    if module_dir.exists():
        sys.path.insert(0, str(module_dir))
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "cross_language_replay.json"
CATALOG_PATH = ROOT / "units_gerado.json"

pytest.importorskip("tft_engine", reason="Build cpp target tft_engine to run cross-language parity")
from tft_engine import TFTLobby as NativeTFTEngine  # noqa: E402

pytest.importorskip("combat_engine", reason="Python lobby combat integration requires combat_engine")
from lobby.TFTLobby import TFTLobby as PythonLobby  # noqa: E402


def _assert_close(actual, expected, path: str, *, abs_tol: float = 1e-5):
    assert math.isclose(float(actual), float(expected), rel_tol=1e-5, abs_tol=abs_tol), (
        f"Cross-language mismatch at {path}: Python={actual!r}, C++={expected!r}"
    )


def _python_snapshot(lobby):
    public = lobby.get_public_state()
    players = public.get("players", [])
    snapshot = {
        "round": int(public.get("round", lobby.round)),
        "stage": int(public.get("stage", lobby.stage)),
        "finished": bool(public.get("finished", lobby.finished)),
        "players": [],
    }
    for p in players:
        snapshot["players"].append({
            "player_id": int(p.get("player_id", -1)),
            "hp": float(p.get("hp", 0.0)),
            "gold": int(p.get("gold", 0)),
            "level": int(p.get("level", 0)),
            "xp": int(p.get("xp", 0)),
            "alive": bool(p.get("alive", True)),
            "wins": int(p.get("wins", 0)),
            "losses": int(p.get("losses", 0)),
        })
    return snapshot


def _native_snapshot(engine):
    public = engine.get_public_state()
    return {
        "round": int(public["round"]),
        "stage": int(public["stage"]),
        "finished": bool(public["finished"]),
        "players": [{
            "player_id": int(p["player_id"]),
            "hp": float(p["hp"]),
            "gold": int(p["gold"]),
            "level": int(p["level"]),
            "xp": int(p["xp"]),
            "alive": bool(p["alive"]),
            "wins": int(p["wins"]),
            "losses": int(p["losses"]),
        } for p in public["players"]],
    }


def _compare_snapshots(py_state, cpp_state, step_name):
    for field in ("round", "stage", "finished"):
        assert py_state[field] == cpp_state[field], (
            f"{step_name}.{field}: Python={py_state[field]!r}, "
            f"C++={cpp_state[field]!r}"
        )
    assert len(py_state["players"]) == len(cpp_state["players"]) == 8
    for index, (py_player, cpp_player) in enumerate(
        zip(py_state["players"], cpp_state["players"])
    ):
        for field in ("player_id", "gold", "level", "xp", "alive", "wins", "losses"):
            assert py_player[field] == cpp_player[field], (
                f"{step_name}.players[{index}].{field}: "
                f"Python={py_player[field]!r}, C++={cpp_player[field]!r}"
            )
        _assert_close(py_player["hp"], cpp_player["hp"],
                      f"{step_name}.players[{index}].hp")


def test_same_action_fixture_matches_python_and_cpp_after_every_step():
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert CATALOG_PATH.exists(), f"Champion catalog not found: {CATALOG_PATH}"

    python_lobby = PythonLobby(seed=fixture["seed"])
    cpp_engine = NativeTFTEngine(fixture["seed"], str(CATALOG_PATH))
    try:
        python_lobby.reset()
        cpp_engine.reset(fixture["seed"])
        python_reward_totals = [0.0] * 8
        cpp_reward_totals = [0.0] * 8

        for step in fixture["steps"]:
            # Execute identical semantic actions through the two public APIs.
            py_obs, py_rewards, py_done, py_info = python_lobby.step(
                step["python_actions"]
            )
            cpp_result = cpp_engine.step(step["cpp_actions"])

            assert all(math.isfinite(float(value)) for value in py_rewards), (
                f"{step['name']}: Python returned a non-finite reward"
            )
            assert all(math.isfinite(float(value)) for value in cpp_result["rewards"]), (
                f"{step['name']}: C++ returned a non-finite reward"
            )
            assert len(py_obs) == 8, (
                f"{step['name']}: Python observation batch must have 8 players"
            )
            assert cpp_result["observations"].shape[0] == 8, (
                f"{step['name']}: C++ observation batch must have 8 players"
            )
            assert np.asarray(py_obs).shape == cpp_result["observations"].shape, (
                f"{step['name']}.observations.shape: Python={np.asarray(py_obs).shape}, "
                f"C++={cpp_result['observations'].shape}"
            )
            py_obs_array = np.asarray(py_obs, dtype=np.float32)
            cpp_obs_array = np.asarray(cpp_result["observations"], dtype=np.float32)
            if not np.allclose(py_obs_array, cpp_obs_array, rtol=1e-5, atol=2e-5):
                mismatches = np.argwhere(
                    ~np.isclose(py_obs_array, cpp_obs_array, rtol=1e-5, atol=2e-5)
                )
                first = tuple(int(x) for x in mismatches[0])
                pytest.fail(
                    f"{step['name']}.observations{first}: "
                    f"Python={py_obs_array[first]!r}, C++={cpp_obs_array[first]!r}; "
                    f"total mismatches={len(mismatches)}"
                )

            py_state = _python_snapshot(python_lobby)
            cpp_state = _native_snapshot(cpp_engine)
            _compare_snapshots(py_state, cpp_state, step["name"])

            assert len(py_rewards) == len(cpp_result["rewards"]) == 8
            for player_id, (py_reward, cpp_reward) in enumerate(
                zip(py_rewards, cpp_result["rewards"])
            ):
                _assert_close(
                    py_reward, cpp_reward,
                    f"{step['name']}.rewards[{player_id}]",
                    abs_tol=2e-4,
                )
                python_reward_totals[player_id] += float(py_reward)
                cpp_reward_totals[player_id] += float(cpp_reward)
                _assert_close(
                    python_reward_totals[player_id],
                    cpp_reward_totals[player_id],
                    f"{step['name']}.cumulative_rewards[{player_id}]",
                    abs_tol=5e-4,
                )

            # Public round metadata is compared too; rewards alone can hide
            # a broken state transition.
            assert bool(py_done) == bool(cpp_result["lobby_done"]), (
                f"{step['name']}.done: Python={py_done}, "
                f"C++={cpp_result['lobby_done']}"
            )
            assert int(python_lobby.round) == int(cpp_result["round"]), (
                f"{step['name']}.round result: Python={python_lobby.round}, "
                f"C++={cpp_result['round']}"
            )
            assert int(python_lobby.stage) == int(cpp_result["stage"]), (
                f"{step['name']}.stage result: Python={python_lobby.stage}, "
                f"C++={cpp_result['stage']}"
            )
            assert py_info["round_info"].get("round_resolved") is True, (
                f"{step['name']}: Python did not resolve the round"
            )
            assert int(cpp_result["round"]) >= 1, (
                f"{step['name']}: C++ returned an invalid round number"
            )
    finally:
        close = getattr(python_lobby, "close", None)
        if callable(close):
            close()
        cpp_engine.close()
