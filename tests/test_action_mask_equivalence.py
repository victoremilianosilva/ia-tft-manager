
# tests/test_action_mask_equivalence.py

from types import SimpleNamespace

import numpy as np
import pytest

from ai.ActionMaskManager import ActionMaskManager
from ai.AntiLoopManager import AntiLoopManager
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
    anti_loop=None,
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
        anti_loop_manager=(
            anti_loop
            if anti_loop is not None
            else FakeAntiLoopManager()
        ),
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

def _native_identity(state, location, index):
    """Obtém a identidade nativa da unidade na posição informada."""
    unit = getattr(state, location)[index]
    assert unit is not None
    return unit.identity


def _register_move_both(
    python_anti_loop,
    native_anti_loop,
    state,
    *,
    move_type,
    source,
    target,
    identity_location,
    identity_index,
):
    """Registra o mesmo movimento nos históricos Python e C++."""
    native_identity = _native_identity(
        state,
        identity_location,
        identity_index,
    )

    python_unit = {
        "uuid": native_identity.uuid,
        "id": native_identity.id,
        "star": native_identity.star,
    }

    python_anti_loop.register_move(
        move_type,
        source,
        target,
        python_unit,
    )

    native_anti_loop.register_move(
        move_type,
        source,
        target,
        native_identity,
    )


def _assert_masks_match_with_history(
    env,
    native_module,
    python_anti_loop,
    native_anti_loop,
):
    """Compara as seis máscaras com históricos previamente sincronizados."""
    env.anti_loop_manager = python_anti_loop

    expected = python_masks(env)

    state = build_player_state(
        env,
        native_module=native_module,
    )

    actual_batch = native_module.ActionMaskEngine().generate_masks(
        state,
        native_anti_loop,
    )

    actual = [
        np.asarray(actual_batch.type_mask, dtype=np.uint8),
        np.asarray(actual_batch.shop_mask, dtype=np.uint8),
        np.asarray(actual_batch.bench_source_mask, dtype=np.uint8),
        np.asarray(actual_batch.board_target_mask, dtype=np.uint8),
        np.asarray(actual_batch.board_source_mask, dtype=np.uint8),
        np.any(
            np.asarray(
                actual_batch.board_move_target_masks,
                dtype=np.uint8,
            ),
            axis=0,
        ).astype(np.uint8),
    ]

    names = [
        "type_mask",
        "shop_mask",
        "bench_source_mask",
        "board_target_mask",
        "board_source_mask",
        "conditioned_board_target_mask",
    ]

    for name, python_mask, cpp_mask in zip(names, expected, actual):
        np.testing.assert_array_equal(
            np.asarray(python_mask, dtype=np.uint8),
            cpp_mask,
            err_msg=f"A máscara {name} divergiu com histórico AntiLoop.",
        )

    return state


def test_anti_loop_blocks_reverse_board_move_equally(native_module):
    unit = make_unit("ReverseUnit")
    board = [None] * 28
    board[12] = unit

    python_anti_loop = AntiLoopManager()
    env = make_env(board=board, anti_loop=python_anti_loop)

    state = build_player_state(env, native_module=native_module)
    native_anti_loop = native_module.AntiLoopEngine()

    _register_move_both(
        python_anti_loop,
        native_anti_loop,
        state,
        move_type="board_move",
        source=4,
        target=12,
        identity_location="board",
        identity_index=12,
    )

    _assert_masks_match_with_history(
        env,
        native_module,
        python_anti_loop,
        native_anti_loop,
    )

    assert python_anti_loop.should_block_move(
        "board_move",
        12,
        4,
        unit,
    )


def test_anti_loop_blocks_repeated_board_swap_equally(native_module):
    unit_a = make_unit("SwapUnitA")
    unit_b = make_unit("SwapUnitB")

    board = [None] * 28
    board[4] = unit_b
    board[12] = unit_a

    python_anti_loop = AntiLoopManager()
    env = make_env(board=board, anti_loop=python_anti_loop)

    state = build_player_state(env, native_module=native_module)
    native_anti_loop = native_module.AntiLoopEngine()

    _register_move_both(
        python_anti_loop,
        native_anti_loop,
        state,
        move_type="board_swap",
        source=4,
        target=12,
        identity_location="board",
        identity_index=12,
    )

    _assert_masks_match_with_history(
        env,
        native_module,
        python_anti_loop,
        native_anti_loop,
    )

    assert python_anti_loop.should_block_move(
        "board_swap",
        12,
        4,
        unit_a,
    )


def test_anti_loop_blocks_repeated_bench_board_transition_equally(
    native_module,
):
    unit = make_unit("BenchBoardUnit")

    board = [None] * 28
    bench = [None] * 9
    bench[2] = unit

    python_anti_loop = AntiLoopManager()
    env = make_env(
        board=board,
        bench=bench,
        anti_loop=python_anti_loop,
    )

    state = build_player_state(env, native_module=native_module)
    native_anti_loop = native_module.AntiLoopEngine()

    native_identity = _native_identity(state, "bench", 2)
    python_unit = {
        "uuid": native_identity.uuid,
        "id": native_identity.id,
        "star": native_identity.star,
    }

    python_anti_loop.register_move(
        "bench_to_board", 2, 4, python_unit
    )
    native_anti_loop.register_move(
        "bench_to_board", 2, 4, native_identity
    )

    python_anti_loop.register_move(
        "board_to_bench", 4, 2, python_unit
    )
    native_anti_loop.register_move(
        "board_to_bench", 4, 2, native_identity
    )

    _assert_masks_match_with_history(
        env,
        native_module,
        python_anti_loop,
        native_anti_loop,
    )

    assert python_anti_loop.should_block_move(
        "bench_to_board",
        2,
        4,
        unit,
    )


def test_anti_loop_mask_generation_does_not_mutate_history(native_module):
    board = [None] * 28
    board[4] = make_unit("HistoryUnitA")
    board[12] = make_unit("HistoryUnitB")

    python_anti_loop = AntiLoopManager()
    env = make_env(board=board, anti_loop=python_anti_loop)

    state = build_player_state(env, native_module=native_module)
    native_anti_loop = native_module.AntiLoopEngine()

    _register_move_both(
        python_anti_loop,
        native_anti_loop,
        state,
        move_type="board_move",
        source=3,
        target=4,
        identity_location="board",
        identity_index=4,
    )

    python_before = python_anti_loop.get_state()
    native_before = native_anti_loop.get_state()

    _assert_masks_match_with_history(
        env,
        native_module,
        python_anti_loop,
        native_anti_loop,
    )

    python_after = python_anti_loop.get_state()
    native_after = native_anti_loop.get_state()

    assert python_after == python_before
    assert native_after.history_size == native_before.history_size
    assert native_after.move_history_size == native_before.move_history_size
    assert native_after.blocked_moves == native_before.blocked_moves
    assert native_after.known_states == native_before.known_states

def test_anti_loop_detects_repeated_board_cycle_equally(native_module):
    unit = make_unit("CycleUnit")

    board = [None] * 28
    board[3] = unit

    python_anti_loop = AntiLoopManager()
    env = make_env(board=board, anti_loop=python_anti_loop)

    state = build_player_state(env, native_module=native_module)
    native_anti_loop = native_module.AntiLoopEngine()
    native_identity = _native_identity(state, "board", 3)

    python_unit = {
        "uuid": native_identity.uuid,
        "id": native_identity.id,
        "star": native_identity.star,
    }

    # Dois percursos pelo mesmo ciclo:
    # 3 -> 10 -> 12 -> 3 -> 10 -> 12 -> 3
    moves = [
        (3, 10),
        (10, 12),
        (12, 3),
        (3, 10),
        (10, 12),
        (12, 3),
    ]

    for source, target in moves:
        python_anti_loop.register_move(
            "board_move", source, target, python_unit
        )
        native_anti_loop.register_move(
            "board_move", source, target, native_identity
        )

    assert python_anti_loop.is_cycle_move(
        "board_move", 3, 10, unit
    )

    assert native_anti_loop.is_cycle_move(
        "board_move", 3, 10, native_identity
    )

    _assert_masks_match_with_history(
        env,
        native_module,
        python_anti_loop,
        native_anti_loop,
    )

def test_python_mask_allows_move_when_anti_loop_raises():
    class RaisingAntiLoopManager:
        def should_block_move(self, **kwargs):
            raise RuntimeError("Falha simulada no AntiLoop")

    board = [None] * 28
    board[4] = make_unit("ExceptionUnit")

    env = make_env(
        board=board,
        anti_loop=RaisingAntiLoopManager(),
    )

    masks = python_masks(env)

    # MOVE_BOARD deve continuar disponível porque existe
    # um movimento legal e a falha do AntiLoop não o bloqueia.
    assert masks[0][4] == 1.0
    assert masks[4][4] == 1.0