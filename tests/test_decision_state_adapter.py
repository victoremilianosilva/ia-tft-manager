# tests/test_decision_state_adapter.py

from copy import deepcopy
from types import SimpleNamespace

import pytest

from ai.DecisionStateAdapter import build_player_state
from config.GameConfig import GameConfig


@pytest.fixture
def native_module():
    """Usa a extensão compilada de verdade."""
    return pytest.importorskip(
        "decision_engine",
        reason="Extensão C++ decision_engine não compilada ou indisponível.",
    )


@pytest.fixture
def make_env():
    """Cria um estado controlado sem inicializar uma partida completa."""

    def _make_env(
        *,
        board=None,
        bench=None,
        shop=None,
        gold=10,
        level=2,
        xp=0,
        player_id=3,
    ):
        return SimpleNamespace(
            player_id=player_id,
            board_manager=SimpleNamespace(
                board=list(board) if board is not None else [None] * 28
            ),
            bench_manager=SimpleNamespace(
                bench=list(bench) if bench is not None else [None] * 9
            ),
            shop_manager=SimpleNamespace(
                shop=list(shop) if shop is not None else [None] * 5
            ),
            economy_manager=SimpleNamespace(
                gold=gold,
                level=level,
                xp=xp,
            ),
        )

    return _make_env


def test_converts_empty_state_with_expected_dimensions(
    native_module,
    make_env,
):
    env = make_env()

    state = build_player_state(env, native_module=native_module)

    assert state.player_id == 3
    assert state.is_alive is True
    assert len(state.board) == 28
    assert len(state.bench) == 9
    assert len(state.shop) == 5

    assert all(unit is None for unit in state.board)
    assert all(unit is None for unit in state.bench)
    assert all(unit is None for unit in state.shop)


def test_converts_economy_using_game_config(
    native_module,
    make_env,
):
    env = make_env(
        gold=37,
        level=4,
        xp=7,
    )

    state = build_player_state(env, native_module=native_module)

    assert state.economy.gold == 37
    assert state.economy.level == 4
    assert state.economy.current_xp == 7
    assert state.economy.max_level == GameConfig.MAX_LEVEL
    assert state.economy.xp_to_next_level == (
        GameConfig.get_xp_to_next(4)
    )
    assert state.economy.reroll_cost == GameConfig.REROLL_COST
    assert state.economy.xp_purchase_cost == GameConfig.BUY_XP_COST


def test_converts_units_and_preserves_empty_slots(
    native_module,
    make_env,
):
    board_unit = {
        "uuid": "unit-board-001",
        "id": "Nasus",
        "star": 2,
        "cost": 3,
    }
    bench_unit = {
        "uuid": "unit-bench-002",
        "id": "Teemo",
        "star": 1,
        "cost": 1,
    }
    shop_unit = {
        "uuid": "unit-shop-003",
        "id": "Briar",
        "star": 1,
        "cost": 2,
        "available": True,
    }

    board = [None] * 28
    bench = [None] * 9
    shop = [None] * 5

    board[12] = board_unit
    bench[4] = bench_unit
    shop[2] = shop_unit

    env = make_env(board=board, bench=bench, shop=shop)

    state = build_player_state(env, native_module=native_module)

    assert state.board[12] is not None
    assert state.board[12].identity.uuid == "unit-board-001"
    assert state.board[12].identity.star == 2
    assert state.board[12].cost == 3

    assert state.bench[4] is not None
    assert state.bench[4].identity.uuid == "unit-bench-002"

    assert state.shop[2] is not None
    assert state.shop[2].identity.uuid == "unit-shop-003"
    assert state.shop[2].available is True

    assert state.board[0] is None
    assert state.bench[0] is None
    assert state.shop[0] is None


def test_string_catalog_id_without_uuid_is_not_fabricated_as_numeric_id(
    native_module,
    make_env,
):
    unit = {
        "id": "Champion_X",
        "star": 1,
        "cost": 2,
    }
    bench = [None] * 9
    bench[0] = unit

    env = make_env(bench=bench)

    state = build_player_state(env, native_module=native_module)

    assert state.bench[0] is not None
    assert state.bench[0].identity.uuid is None
    assert state.bench[0].identity.id is None


def test_preserves_unavailable_shop_unit(
    native_module,
    make_env,
):
    shop = [None] * 5
    shop[1] = {
        "uuid": "unavailable-unit",
        "id": "Champion_Y",
        "star": 1,
        "cost": 1,
        "available": False,
    }

    env = make_env(shop=shop)

    state = build_player_state(env, native_module=native_module)

    assert state.shop[1] is not None
    assert state.shop[1].available is False


@pytest.mark.parametrize(
    ("attribute", "invalid_slots", "expected_size"),
    [
        ("board", [None] * 27, 28),
        ("bench", [None] * 8, 9),
        ("shop", [None] * 4, 5),
    ],
)
def test_rejects_invalid_slot_dimensions(
    native_module,
    make_env,
    attribute,
    invalid_slots,
    expected_size,
):
    env = make_env()
    manager_name = {
        "board": "board_manager",
        "bench": "bench_manager",
        "shop": "shop_manager",
    }[attribute]

    setattr(getattr(env, manager_name), attribute, invalid_slots)

    with pytest.raises(
        ValueError,
        match=rf"{attribute}.*dimensão inválida",
    ):
        build_player_state(env, native_module=native_module)

    assert len(invalid_slots) != expected_size


@pytest.mark.parametrize(
    ("economy_values", "expected_message"),
    [
        ({"gold": -1}, "economy.gold"),
        ({"level": 0}, "economy.level"),
        ({"level": GameConfig.MAX_LEVEL + 1}, "economy.level"),
        ({"xp": -1}, "economy.xp"),
    ],
)
def test_rejects_invalid_economy(
    native_module,
    make_env,
    economy_values,
    expected_message,
):
    env = make_env()

    for key, value in economy_values.items():
        setattr(env.economy_manager, key, value)

    with pytest.raises(ValueError, match=expected_message):
        build_player_state(env, native_module=native_module)


def test_rejects_non_dictionary_unit(
    native_module,
    make_env,
):
    board = [None] * 28
    board[3] = "not-a-unit-dictionary"

    env = make_env(board=board)

    with pytest.raises(ValueError, match=r"board\[3\]"):
        build_player_state(env, native_module=native_module)


def test_conversion_does_not_mutate_python_managers(
    native_module,
    make_env,
):
    board = [None] * 28
    bench = [None] * 9
    shop = [None] * 5

    board[2] = {
        "uuid": "board-unit",
        "id": "Champion_A",
        "star": 1,
        "cost": 2,
    }
    bench[6] = {
        "uuid": "bench-unit",
        "id": "Champion_B",
        "star": 2,
        "cost": 3,
    }
    shop[3] = {
        "uuid": "shop-unit",
        "id": "Champion_C",
        "star": 1,
        "cost": 4,
        "available": False,
    }

    env = make_env(
        board=board,
        bench=bench,
        shop=shop,
        gold=25,
        level=5,
        xp=11,
    )

    before = deepcopy(
        {
            "board": env.board_manager.board,
            "bench": env.bench_manager.bench,
            "shop": env.shop_manager.shop,
            "gold": env.economy_manager.gold,
            "level": env.economy_manager.level,
            "xp": env.economy_manager.xp,
        }
    )

    build_player_state(env, native_module=native_module)

    after = {
        "board": env.board_manager.board,
        "bench": env.bench_manager.bench,
        "shop": env.shop_manager.shop,
        "gold": env.economy_manager.gold,
        "level": env.economy_manager.level,
        "xp": env.economy_manager.xp,
    }

    assert after == before