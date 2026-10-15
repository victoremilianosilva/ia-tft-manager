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


MASK_SHAPES = {
    "type_mask": (7,), "shop_mask": (5,), "bench_source_mask": (9,),
    "board_target_mask": (28,), "board_source_mask": (28,),
    "board_move_target_masks": (28, 28), "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28),
}

def _compare_action_masks(python_lobby, cpp_engine, step_name):
    """Compara todas as máscaras nomeadas e suas matrizes condicionais."""
    py_masks = python_lobby.get_action_masks()
    cpp_masks = cpp_engine.get_action_masks()
    assert len(py_masks) == len(cpp_masks) == 8, "%s: lote de máscaras inválido" % step_name
    for player_id, (py_player, cpp_player) in enumerate(zip(py_masks, cpp_masks)):
        for name, shape in MASK_SHAPES.items():
            assert name in py_player and name in cpp_player, (step_name, player_id, name)
            py_mask = np.asarray(py_player[name])
            cpp_mask = np.asarray(cpp_player[name])
            assert py_mask.shape == cpp_mask.shape == shape, "%s player=%d mask=%s shape" % (step_name, player_id, name)
            assert py_mask.dtype == np.bool_ and cpp_mask.dtype == np.bool_, (step_name, player_id, name, 'dtype')
            np.testing.assert_array_equal(py_mask, cpp_mask, err_msg='%s player=%d mask=%s divergiu' % (step_name, player_id, name))

def _compare_audit_snapshots(python_lobby, cpp_engine, step_name):
    """Compare unit slots and economy without relying on UUID or RNG."""
    native = cpp_engine.get_audit_snapshot()
    assert int(native["round"]) == int(python_lobby.get_public_state()["round"]), (step_name, "round audit")
    assert int(native["stage"]) == int(python_lobby.stage), (step_name, "stage audit")
    for player_id, player in enumerate(python_lobby.players):
        env = player.env
        py_economy = env.economy_manager
        cpp_player = native["players"][player_id]
        for field in ("gold", "level", "xp", "win_streak", "loss_streak"):
            assert int(getattr(py_economy, field)) == int(cpp_player[field]), (
                step_name, player_id, field, getattr(py_economy, field), cpp_player[field]
            )
        for py_name, cpp_name, py_units in (
            ("board", "board", env.board_manager.board),
            ("bench", "bench", env.bench_manager.bench),
        ):
            cpp_units = cpp_player[cpp_name]
            assert len(py_units) == len(cpp_units), (step_name, player_id, py_name, "length")
            for slot, (py_unit, cpp_unit) in enumerate(zip(py_units, cpp_units)):
                occupied = py_unit is not None
                assert occupied is bool(cpp_unit["occupied"]), (
                    step_name, player_id, py_name, slot, "occupied"
                )
                if not occupied:
                    continue
                assert int(py_unit.get("star", 1)) == int(cpp_unit["star"]), (
                    step_name, player_id, py_name, slot, "star"
                )
                assert int(py_unit.get("cost", 0)) == int(cpp_unit["cost"]), (
                    step_name, player_id, py_name, slot, "cost"
                )
                py_id = py_unit.get("champion_id", py_unit.get("apiName"))
                if py_id is not None:
                    assert str(py_id) == str(cpp_unit["champion_id"]), (
                        step_name, player_id, py_name, slot, py_id, cpp_unit["champion_id"]
                    )


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

        _compare_action_masks(python_lobby, cpp_engine, "reset")
        _compare_audit_snapshots(python_lobby, cpp_engine, "reset")

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

            _compare_action_masks(python_lobby, cpp_engine, step["name"])
            _compare_audit_snapshots(python_lobby, cpp_engine, step["name"])

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

            # Validate the full strategy analysis API against the Python
            # StrategyManager for each live player after every transition.
            cpp_strategies = cpp_engine.get_strategies()
            for player_id, player in enumerate(python_lobby.players):
                if not player.alive:
                    continue
                env = player.env
                manager = env.strategy_manager
                economy = env.economy_manager
                board_power = sum(
                    float(unit.get("cost", 1)) * float(unit.get("star", 1)) * 2.0
                    for unit in env.board_manager.board if unit is not None
                )
                cpp_strategy = cpp_strategies[player_id]
                _assert_close(
                    cpp_strategy["state_confidence"],
                    manager.compute_strategy_confidence(
                        hp=env.hp, gold=economy.gold, board_power=board_power,
                        level=economy.level, win_streak=economy.win_streak,
                        loss_streak=economy.loss_streak,
                    ),
                    f"{step['name']}.strategies[{player_id}].state_confidence",
                )
                expected_scores = {
                    int(strategy): manager.get_strategy_score(
                        strategy, hp=env.hp, gold=economy.gold,
                        level=economy.level, board_power=board_power,
                        win_streak=economy.win_streak,
                        loss_streak=economy.loss_streak,
                    )
                    for strategy in __import__(
                        "strategy.StrategyManager", fromlist=["Strategy"]
                    ).Strategy
                }
                cpp_scores = cpp_strategy["strategy_scores"]
                assert set(map(int, cpp_scores.keys())) == set(expected_scores), (
                    f"{step['name']}.strategies[{player_id}].strategy_scores keys differ"
                )
                for strategy_id, expected_score in expected_scores.items():
                    _assert_close(
                        cpp_scores[strategy_id], expected_score,
                        f"{step['name']}.strategies[{player_id}].scores[{strategy_id}]",
                    )
                best_expected = max(expected_scores, key=expected_scores.get)
                assert cpp_strategy["best_scored_strategy"] == best_expected, (
                    f"{step['name']}.strategies[{player_id}].best_scored_strategy: "
                    f"Python={best_expected}, C++={cpp_strategy['best_scored_strategy']}"
                )
                assert 0.0 <= float(cpp_strategy["confidence"]) <= 1.0
                assert 0.0 <= float(cpp_strategy["state_confidence"]) <= 1.0

                # CompositionManager parity: IDs, copy counts, direction/focus,
                # core membership and candidate-unit scores.
                composition = env.composition_manager
                comp_state = composition.get_state()
                assert cpp_strategy["composition_focus_id"] == (
                    -1 if comp_state["focus"] is None else int(comp_state["focus"])
                ), f"{step['name']}.composition[{player_id}].focus"
                assert cpp_strategy["composition_direction"] == (comp_state["direction"] or ""), (
                    f"{step['name']}.composition[{player_id}].direction"
                )
                assert set(cpp_strategy["core_unit_ids"]) == set(comp_state["core_units"]), (
                    f"{step['name']}.composition[{player_id}].core_units"
                )
                assert set(cpp_strategy["core_traits"]) == set(comp_state["core_traits"]), (
                    f"{step['name']}.composition[{player_id}].core_traits"
                )
                assert dict(cpp_strategy["active_traits"]) == comp_state["active_traits"], (
                    f"{step['name']}.composition[{player_id}].active_traits"
                )
                assert {int(k): int(v) for k, v in cpp_strategy["unit_counts_by_id"].items()} == {
                    int(k): int(v) for k, v in comp_state["unit_counts"].items()
                }, f"{step['name']}.composition[{player_id}].unit_counts"

                for champion_def in env.unit_manager.get_all_champions():
                    api_name = champion_def.get("apiName") or champion_def.get("api_name") or champion_def.get("champion_id")
                    if not api_name:
                        continue
                    candidate = env.unit_manager.create_unit(champion_def)
                    for star in (1, 2, 3):
                        candidate["star"] = star
                        _assert_close(
                            cpp_engine.get_unit_comp_score(player_id, api_name, star),
                            composition.get_unit_comp_score(candidate),
                            f"{step['name']}.composition[{player_id}].score[{api_name},star={star}]",
                        )
                    assert cpp_engine.is_core_unit(player_id, api_name) == composition.is_core_unit(candidate)
                    for trait in candidate.get("traits", []):
                        assert cpp_engine.is_core_trait(player_id, trait) == composition.is_core_trait(trait)

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


def test_shared_shop_and_economy_fixtures_cover_all_seven_actions():
    """Run every action against equal offers/economy and deterministic reroll."""
    fixture_seed = 90421
    python_lobby = PythonLobby(seed=fixture_seed)
    cpp_engine = NativeTFTEngine(fixture_seed, str(CATALOG_PATH))
    try:
        python_lobby.reset()
        cpp_engine.reset(fixture_seed)

        env0 = python_lobby.players[0].env
        champions = [
            champion for champion in env0.unit_manager.get_all_champions()
            if int(champion.get("cost", 1)) == 1
        ]
        assert len(champions) >= 5, "Need five distinct cost-1 champions for deterministic reroll"
        names = [
            champion.get("apiName") or champion.get("api_name")
            or champion.get("champion_id")
            for champion in champions[:5]
        ]
        assert all(names), "Fixture champions must have apiName"

        # Normalize board/bench and economy. The C++ fixture hooks keep shop
        # reservations consistent with the global native pool.
        for player_id, player in enumerate(python_lobby.players):
            env = player.env
            env.board_manager.board[:] = [None] * len(env.board_manager.board)
            env.bench_manager.bench[:] = [None] * len(env.bench_manager.bench)
            env.bench_manager.bench[0] = env.unit_manager.create_unit(champions[0])
            env.economy_manager.gold = 30
            env.economy_manager.level = 2
            env.economy_manager.xp = 0
            assert cpp_engine.set_unit_for_testing(
                player_id, False, 0, names[0], 1
            ), "Could not configure shared bench fixture"
            assert cpp_engine.set_player_economy_for_testing(
                player_id, 30, 2, 0
            ), "Could not configure native economy fixture"
            assert env.shop_manager.set_offer_for_testing(0, names[0]), (
                "Could not reserve Python fixture offer for player %d" % player_id
            )
            assert cpp_engine.set_shop_offer_for_testing(
                player_id, 0, names[0]
            ), "Could not reserve native fixture offer for player %d" % player_id

        # MOVE_BENCH and MOVE_BOARD need independent, known source units.
        env3 = python_lobby.players[3].env
        env3._rebuild_player_state()
        env4 = python_lobby.players[4].env
        env4.board_manager.board[0] = env4.unit_manager.create_unit(champions[1])
        assert cpp_engine.set_unit_for_testing(4, True, 0, names[1], 1)
        env5 = python_lobby.players[5].env
        env5._rebuild_player_state()
        for player in python_lobby.players:
            player.env._rebuild_player_state()

        assert python_lobby.players[1].env.shop_manager.set_next_roll_for_testing(names)
        assert cpp_engine.set_next_shop_roll_for_testing(1, names)

        # One action per player, all in one preparation phase. PASS players
        # do not resolve the round because the other six players have not passed.
        py_actions = [
            {"type": 0, "shop_slot": 0},                       # BUY
            {"type": 1},                                       # REROLL
            {"type": 2},                                       # BUY_XP
            {"type": 3, "bench_slot": 0, "board_target": 5},   # MOVE_BENCH
            {"type": 4, "board_source": 0, "conditioned_board_target": 1},
            {"type": 5, "bench_slot": 0},                      # SELL
            {"type": 6},                                       # PASS
            {"type": 6},                                       # PASS
        ]
        cpp_actions = [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [3, 0, 0, 5, 0, 0],
            [4, 0, 0, 0, 0, 1],
            [5, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0],
        ]

        # The chosen actions must be legal in both engines before execution.
        py_masks = python_lobby.get_action_masks()
        cpp_masks = cpp_engine.get_action_masks()
        for player_id, action_type in enumerate([0, 1, 2, 3, 4, 5, 6, 6]):
            assert bool(py_masks[player_id]["type_mask"][action_type]), (
                "Python fixture action is masked: player=%d type=%d" % (player_id, action_type)
            )
            assert bool(cpp_masks[player_id]["type_mask"][action_type]), (
                "C++ fixture action is masked: player=%d type=%d" % (player_id, action_type)
            )

        _, py_rewards, _, _ = python_lobby.step(py_actions)
        cpp_result = cpp_engine.step(cpp_actions)

        _compare_action_masks(python_lobby, cpp_engine, "all_seven_actions")
        _compare_audit_snapshots(python_lobby, cpp_engine, "all_seven_actions")

        assert len(py_rewards) == len(cpp_result["rewards"]) == 8
        for player_id, (py_reward, cpp_reward) in enumerate(
            zip(py_rewards, cpp_result["rewards"])
        ):
            _assert_close(py_reward, cpp_reward, "all_seven_actions.rewards[%d]" % player_id)

        # The shop offer consumed by BUY disappears in both engines. The
        # forced REROLL offers are identical by champion and slot.
        py_shop0 = python_lobby.players[0].env.shop_manager.get_shop()
        cpp_snapshot = cpp_engine.get_audit_snapshot()
        assert py_shop0[0] is None
        assert not cpp_snapshot["players"][0]["shop"][0]["occupied"]
        py_shop1 = python_lobby.players[1].env.shop_manager.get_shop()
        cpp_shop1 = cpp_snapshot["players"][1]["shop"]
        for slot, name in enumerate(names):
            py_name = py_shop1[slot].get("apiName", py_shop1[slot].get("champion_id"))
            assert py_name == name, ("Python forced reroll mismatch", slot, py_name, name)
            assert cpp_shop1[slot]["champion_id"] == name, (
                "C++ forced reroll mismatch", slot, cpp_shop1[slot]["champion_id"], name
            )

        # Economy side effects are checked explicitly as a readable contract.
        py_gold = [player.env.economy_manager.gold for player in python_lobby.players]
        cpp_gold = [player["gold"] for player in cpp_snapshot["players"]]
        assert py_gold == cpp_gold
        assert py_gold[0] == 30 - int(champions[0]["cost"])
        assert py_gold[1] == 28
        assert py_gold[2] == 26
    finally:
        python_lobby.close() if hasattr(python_lobby, "close") else None
        cpp_engine.close()
