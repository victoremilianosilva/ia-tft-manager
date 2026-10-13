
# tests/test_action_mask_equivalence.py

from types import SimpleNamespace

import numpy as np
import pytest

from ai.ActionMaskManager import ActionMaskManager
from ai.DecisionStateAdapter import build_player_state
from config.GameConfig import GameConfig


@pytest.fixture
def native_module():
    """Usa a extensão C++ compilada de verdade."""
    return pytest.importorskip(
        "decision_engine",
        reason="Compile a extensão C++ decision_engine antes do teste.",
    )


class FakeBoardManager:
    def __init__(self, board):
        self.board = board

    def get_empty_positions(self):
        return [
            index
            for index, unit in enumerate(self.board)
            if unit is None
        ]

    def is_valid_position(self, position):
        return 0 <= position < len(self.board)


class FakeBenchManager:
    def __init__(self, bench):
        self.bench = bench

    def has_free_slot(self):
        return any(unit is None for unit in self.bench)


class FakeShopManager:
    def __init__(self, shop):
        self.shop = shop

    def get_shop(self):
        return self.shop


class FakeEconomyManager:
    def __init__(self, gold, level, xp=0):
        self.gold = gold
        self.level = level
        self.xp = xp

    def can_spend(self, amount):
        return self.gold >= amount

    def can_buy_xp(self):
        return (
            self.level < GameConfig.MAX_LEVEL
            and self.can_spend(GameConfig.BUY_XP_COST)
        )


class FakeAntiLoopManager:
    """Sem bloqueios: isola a equivalência das máscaras básicas."""

    def should_block_move(
        self,
        *,
        move_type,
        source,
        target,
        unit,
    ):
        return False


def make_unit(
    name,
    *,
    cost=1,
    uuid=None,
    available=True,
    star=1,
):
    return {
        "id": name,
        "uuid": uuid or f"uuid-{name}",
        "cost": cost,
        "available": available,
        "star": star,
    }


def make_env(
    *,
    board=None,
    bench=None,
    shop=None,
    gold=10,
    level=2,
    xp=0,
):
    board = list(board) if board is not None else [None] * 28
    bench = list(bench) if bench is not None else [None] * 9
    shop = list(shop) if shop is not None else [None] * 5

    return SimpleNamespace(
        player_id=1,
        board_manager=FakeBoardManager(board),
        bench_manager=FakeBenchManager(bench),
        shop_manager=FakeShopManager(shop),
        economy_manager=FakeEconomyManager(gold, level, xp),
        composition_manager=None,
        positioning_manager=None,
        anti_loop_manager=FakeAntiLoopManager(),
        unit_manager=None,
    )


def python_masks(env):
    manager = ActionMaskManager(
        board_manager=env.board_manager,
        bench_manager=env.bench_manager,
        shop_manager=env.shop_manager,
        economy_manager=env.economy_manager,
        composition_manager=env.composition_manager,
        positioning_manager=env.positioning_manager,
        anti_loop_manager=env.anti_loop_manager,
        unit_manager=env.unit_manager,
    )

    return manager.get_action_masks()


def native_masks(env, native_module):
    state = build_player_state(
        env,
        native_module=native_module,
    )

    engine = native_module.ActionMaskEngine()
    anti_loop = native_module.AntiLoopEngine()
    batch = engine.generate_masks(state, anti_loop)

    # A sexta máscara Python é a união dos destinos válidos
    # para todas as origens ocupadas do tabuleiro.
    conditioned_board_target = np.any(
        np.asarray(batch.board_move_target_masks, dtype=np.uint8),
        axis=0,
    ).astype(np.uint8)

    return [
        np.asarray(batch.type_mask, dtype=np.uint8),
        np.asarray(batch.shop_mask, dtype=np.uint8),
        np.asarray(batch.bench_source_mask, dtype=np.uint8),
        np.asarray(batch.board_target_mask, dtype=np.uint8),
        np.asarray(batch.board_source_mask, dtype=np.uint8),
        conditioned_board_target,
    ], batch


def assert_masks_match(env, native_module):
    expected = python_masks(env)
    actual, batch = native_masks(env, native_module)

    names = [
        "type_mask",
        "shop_mask",
        "bench_source_mask",
        "board_target_mask",
        "board_source_mask",
        "conditioned_board_target_mask",
    ]

    expected_dimensions = [7, 5, 9, 28, 28, 28]

    assert len(expected) == len(actual) == 6

    for name, python_mask, cpp_mask, size in zip(
        names,
        expected,
        actual,
        expected_dimensions,
    ):
        python_mask = np.asarray(python_mask, dtype=np.uint8)

        assert python_mask.shape == (size,), (
            f"{name}: dimensão Python inesperada: {python_mask.shape}"
        )
        assert cpp_mask.shape == (size,), (
            f"{name}: dimensão C++ inesperada: {cpp_mask.shape}"
        )

        np.testing.assert_array_equal(
            cpp_mask,
            python_mask,
            err_msg=f"A máscara {name} divergiu entre Python e C++.",
        )

    # Os fallbacks técnicos não devem ser confundidos com
    # disponibilidade real das ações.
    assert batch.buy_available == bool(expected[0][0])
    assert batch.sell_available == bool(expected[0][5])
    assert batch.bench_move_available == bool(expected[0][3])
    assert batch.board_move_available == bool(expected[0][4])


def test_empty_state_masks_match(native_module):
    env = make_env(gold=0)

    assert_masks_match(env, native_module)


def test_shop_masks_match_with_affordable_units(native_module):
    shop = [None] * 5
    shop[1] = make_unit("ChampionA", cost=2)
    shop[3] = make_unit("ChampionB", cost=5)

    env = make_env(shop=shop, gold=5)

    assert_masks_match(env, native_module)


def test_unavailable_shop_unit_preserves_python_behavior(native_module):
    shop = [None] * 5
    shop[2] = make_unit(
        "ChampionUnavailable",
        cost=1,
        available=False,
    )

    env = make_env(shop=shop, gold=10)

    # O Python atual não filtra "available" na máscara de compra.
    assert python_masks(env)[1][2] == 1.0

    assert_masks_match(env, native_module)


def test_bench_to_board_masks_match(native_module):
    bench = [None] * 9
    bench[2] = make_unit("BenchChampionA", cost=2)
    bench[6] = make_unit("BenchChampionB", cost=3)

    env = make_env(bench=bench)

    assert_masks_match(env, native_module)


def test_board_move_masks_match(native_module):
    board = [None] * 28
    board[4] = make_unit("BoardChampionA")
    board[12] = make_unit("BoardChampionB")

    env = make_env(board=board)

    assert_masks_match(env, native_module)


def test_economy_and_sell_masks_match(native_module):
    bench = [None] * 9
    bench[7] = make_unit("SellCandidate")

    shop = [None] * 5
    shop[0] = make_unit("ExpensiveChampion", cost=5)

    env = make_env(
        bench=bench,
        shop=shop,
        gold=2,
    )

    assert_masks_match(env, native_module)