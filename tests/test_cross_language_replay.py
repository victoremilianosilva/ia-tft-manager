"""Cross-language replay tests for the Python lobby and native TFTEngine.

These tests intentionally run the same fixture through both public APIs. They
are not formula/golden-value tests: each step executes the real lobby engine,
then compares externally observable state and rewards.
"""
from __future__ import annotations

import json
import math
import os
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

if os.environ.get("REQUIRE_CPP_PARITY") == "1":
    # CI must fail rather than silently skip parity when a native module fails to build/import.
    from tft_engine import TFTLobby as NativeTFTEngine  # noqa: E402
    import combat_engine  # noqa: F401,E402
else:
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

        # Build the same owned-unit snapshot in both backends. Shop offers
        # remain random, but all board/bench/trait/combat features are controlled.
        champions = python_lobby.players[0].env.unit_manager.get_all_champions()
        assert champions, "Python champion catalog is empty"
        champion = champions[0]
        champion_api_name = (
            champion.get("apiName")
            or champion.get("api_name")
            or champion.get("champion_id")
        )
        assert champion_api_name, f"Champion lacks apiName: {champion!r}"

        for player_id, player in enumerate(python_lobby.players):
            env = player.env
            env.board_manager.board[:] = [None] * len(env.board_manager.board)
            env.bench_manager.bench[:] = [None] * len(env.bench_manager.bench)
            env.bench_manager.bench[0] = env.unit_manager.create_unit(champion)
            assert cpp_engine.set_unit_for_testing(
                player_id, False, 0, champion_api_name, 1
            ), f"C++ could not set shared bench unit for player {player_id}"

            if player_id == 0:
                env.board_manager.board[6] = env.unit_manager.create_unit(champion)
                env.board_manager.board[13] = env.unit_manager.create_unit(champion)
                assert cpp_engine.set_unit_for_testing(
                    player_id, True, 6, champion_api_name, 1
                )
                assert cpp_engine.set_unit_for_testing(
                    player_id, True, 13, champion_api_name, 1
                )
            elif player_id == 1:
                env.board_manager.board[0] = env.unit_manager.create_unit(champion)
                assert cpp_engine.set_unit_for_testing(
                    player_id, True, 0, champion_api_name, 1
                )

            env._rebuild_player_state()

            # One controlled PVP pair makes winner/loser reward parity
            # deterministic and avoids differences in matchmaking RNG.
            if player_id >= 2:
                player.alive = False
                player.env.done = True
                player.env.hp = 0
                assert cpp_engine.set_player_alive_for_testing(player_id, False)

        python_lobby.round_finished = [False] * python_lobby.PLAYERS_PER_LOBBY
        for player_id in range(2, python_lobby.PLAYERS_PER_LOBBY):
            python_lobby.round_finished[player_id] = True

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
            # Observation ABI is float32 on both sides; do not hide a dtype
            # regression by casting before checking the public API contract.
            assert np.asarray(py_obs).dtype == np.dtype(np.float32), (
                f"{step['name']}: Python observations must be float32"
            )
            assert cpp_result["observations"].dtype == np.dtype(np.float32), (
                f"{step['name']}: C++ observations must be float32"
            )
            assert cpp_engine.observation_dim == np.asarray(py_obs).shape[1], (
                f"{step['name']}.observation_dim: native={cpp_engine.observation_dim}, "
                f"Python={np.asarray(py_obs).shape[1]}"
            )
            py_obs_array = np.asarray(py_obs)
            cpp_obs_array = np.asarray(cpp_result["observations"])
            # Owned-unit data is identical by fixture. Only shop offers
            # remain dependent on the backend-specific random stream.
            dim = py_obs_array.shape[1]
            bench_start = 22 + 28 * 5
            shop_start = bench_start + 9 * 5
            shop_end = shop_start + 5 * 5
            excluded = set(range(shop_start, shop_end))
            deterministic_indices = np.array(
                [index for index in range(dim) if index not in excluded],
                dtype=np.int64,
            )
            py_deterministic = py_obs_array[:, deterministic_indices]
            cpp_deterministic = cpp_obs_array[:, deterministic_indices]
            if not np.allclose(
                py_deterministic, cpp_deterministic, rtol=1e-5, atol=2e-5
            ):
                mismatches = np.argwhere(
                    ~np.isclose(
                        py_deterministic, cpp_deterministic,
                        rtol=1e-5, atol=2e-5
                    )
                )
                first = tuple(int(x) for x in mismatches[0])
                pytest.fail(
                    f"{step['name']}.deterministic_observations{first}: "
                    f"Python={py_deterministic[first]!r}, "
                    f"C++={cpp_deterministic[first]!r}; "
                    f"total mismatches={len(mismatches)}; "
                        f"original_indices={deterministic_indices[mismatches[:20, 1]].tolist()}"
                )
            assert np.isfinite(py_obs_array).all(), f"{step['name']}: Python observation contains NaN/inf"
            assert np.isfinite(cpp_obs_array).all(), f"{step['name']}: C++ observation contains NaN/inf"
            random_dependent = np.arange(shop_start, shop_end)
            py_random = py_obs_array[:, random_dependent]
            cpp_random = cpp_obs_array[:, random_dependent]
            assert np.isfinite(py_random).all() and np.isfinite(cpp_random).all(), (
                f"{step['name']}: random-dependent observation fields contain NaN/inf"
            )
            assert ((py_random >= 0.0) & (py_random <= 1.0)).all()
            assert ((cpp_random >= 0.0) & (cpp_random <= 1.0)).all()

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

            # Compare reward components separately so an aggregate total
            # cannot hide an omitted or duplicated action/combat/placement term.
            py_players_info = py_info.get("players", [])
            py_action_components = np.asarray(
                [float(item.get("action_reward", 0.0)) for item in py_players_info],
                dtype=np.float32,
            )
            py_combat_components = np.asarray(
                [float(item.get("combat_reward", 0.0)) for item in py_players_info],
                dtype=np.float32,
            )
            placement_map = py_info.get("placement_rewards", {}) or {}
            py_placement_components = np.asarray(
                [
                    float(placement_map.get(pid, placement_map.get(str(pid), 0.0)))
                    for pid in range(8)
                ],
                dtype=np.float32,
            )
            component_pairs = (
                ("action_rewards", py_action_components, cpp_result["action_rewards"]),
                ("combat_rewards", py_combat_components, cpp_result["combat_rewards"]),
                ("placement_rewards", py_placement_components, cpp_result["placement_rewards"]),
            )
            for component_name, py_component, cpp_component in component_pairs:
                assert np.asarray(cpp_component).shape == (8,), (
                    f"{step['name']}.{component_name}: C++ component shape is invalid"
                )
                for player_id, (py_value, cpp_value) in enumerate(
                    zip(py_component, cpp_component)
                ):
                    _assert_close(
                        py_value, cpp_value,
                        f"{step['name']}.{component_name}[{player_id}]",
                        abs_tol=2e-4,
                    )

            _assert_close(
                float(np.sum(cpp_result["action_rewards"] +
                             cpp_result["combat_rewards"] +
                             cpp_result["placement_rewards"])),
                float(np.sum(cpp_result["rewards"])),
                f"{step['name']}.cpp_reward_components_sum",
                abs_tol=5e-4,
            )
            _assert_close(
                float(np.sum(py_action_components +
                             py_combat_components +
                             py_placement_components)),
                float(np.sum(py_rewards)),
                f"{step['name']}.python_reward_components_sum",
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
            expected_round_resolved = step.get("expected_round_resolved", True)
            assert all(
                item.get("round_resolved", False) is expected_round_resolved
                for item in py_info["players"]
                if not item.get("dead", False)
            ), (
                f"{step['name']}: Python round_resolved flags do not match "
                f"expected={expected_round_resolved}"
            )
            assert int(cpp_result["round"]) >= 1, (
                f"{step['name']}: C++ returned an invalid round number"
            )
    finally:
        close = getattr(python_lobby, "close", None)
        if callable(close):
            close()
        cpp_engine.close()
