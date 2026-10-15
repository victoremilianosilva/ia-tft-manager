"""Cross-language parity tests for PositioningManager and native PositioningEngine."""
from __future__ import annotations
import math
import os
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
for module_dir in (ROOT / "cpp" / "build" / "bin", ROOT / "cpp" / "build" / "bin" / "Release"):
    if module_dir.exists():
        sys.path.insert(0, str(module_dir))
if os.environ.get("REQUIRE_CPP_PARITY") == "1":
    import tft_engine as cpp
else:
    pytest.importorskip("tft_engine")
    import tft_engine as cpp
from strategy.PositioningManager import PositioningManager
from combat.CombatProfileManager import UnitRole

ROLES = [UnitRole.TANK, UnitRole.CARRY, UnitRole.SUPPORT, UnitRole.FIGHTER, UnitRole.ASSASSIN]

def _py_board(roles):
    return [None if r < 0 else {"role": UnitRole(r), "uuid": f"u{i}"} for i, r in enumerate(roles)]

def _close(a, b, where):
    assert math.isclose(float(a), float(b), rel_tol=1e-7, abs_tol=1e-7), f"{where}: Python={a}, C++={b}"

@pytest.mark.parametrize("roles", [
    [-1] * 28,
    [0, 3, -1, -1, 1, 2, -1] + [-1] * 21,
    [4, -1, 1, 0, 2, -1, 3, 1, 2, -1, 0, -1, 4, -1, -1, 3, -1, 1, 2, -1, 0, -1, -1, 4, 3, -1, 1, 2],
    [((i * 7 + 3) % 5) if i % 3 else -1 for i in range(28)],
])
def test_positioning_formula_search_and_geometry_match(roles):
    manager = PositioningManager()
    board = _py_board(roles)
    assert cpp.positioning_is_valid_position(-1) == manager.is_valid_position(-1)
    for p in range(-1, 29):
        assert bool(cpp.positioning_is_valid_position(p)) == manager.is_valid_position(p)
        cpp_rc = tuple(cpp.positioning_position_to_row_col(p))\n        py_rc = manager.position_to_row_col(p)\n        assert ((None, None) if cpp_rc == (-1, -1) else cpp_rc) == py_rc
        for diagonal in (False, True):
            assert list(cpp.positioning_get_neighbors(p, diagonal)) == manager.get_neighbors(p, diagonal)

    _close(cpp.positioning_evaluate_board_positioning(roles), manager.evaluate_board_positioning(board), "board")
    _close(cpp.positioning_get_normalized_score(roles), manager.get_normalized_positioning_score(board), "normalized")
    for p in range(28):
        _close(cpp.positioning_evaluate_unit_placement(roles, p), manager.evaluate_unit_placement(board, p), f"placement[{p}]")
        _close(cpp.positioning_evaluate_protection(roles, p), manager.evaluate_protection(board, p), f"protection[{p}]")
        for role in range(5):
            unit = {"role": UnitRole(role)}
            _close(cpp.positioning_evaluate_unit_placement(roles, p, role), manager.evaluate_unit_placement(board, p, unit), f"candidate[{p},{role}]")

    empty_positions = [p for p, r in enumerate(roles) if r < 0]
    for role in range(5):
        py_position, py_score = manager.find_best_position(board, {"role": UnitRole(role)})
        cpp_position, cpp_score = cpp.positioning_find_best_position(roles, role)
        assert (None if cpp_position < 0 else cpp_position) == py_position, f"best position role={role}"
        if py_position is not None:
            _close(cpp_score, py_score, f"best-position-score[{role}]")

    for source, role in enumerate(roles):
        py_position, py_delta = manager.find_best_swap(board, source)
        cpp_position, cpp_delta = cpp.positioning_find_best_swap(roles, source)
        assert (None if cpp_position < 0 else cpp_position) == py_position, f"best swap source={source}"
        if py_position is not None:
            _close(cpp_delta, py_delta, f"best-swap-delta[{source}]")
    assert bool(cpp.positioning_is_board_stable(roles)) == manager.is_board_stable(board)
