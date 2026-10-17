"""Regression tests for viewer-only timed preparation and backline fallback."""

from viewer.session import ViewerConfig, ViewerSession


def _unit(occupied=False):
    return {"occupied": occupied}


def _session(level=3, board_count=2, occupied_backline=(21,), bench_slots=(2,)):
    session = ViewerSession.__new__(ViewerSession)
    board = [_unit() for _ in range(28)]
    bench = [_unit() for _ in range(9)]
    for slot in range(max(0, board_count - len(occupied_backline))):
        board[slot] = _unit(True)
    for slot in occupied_backline:
        board[slot] = _unit(True)
    for slot in bench_slots:
        bench[slot] = _unit(True)
    session.audit_snapshot = {
        "players": [{
            "player_id": 0,
            "level": level,
            "board": board,
            "bench": bench,
        }]
    }
    return session


def test_viewer_defaults_to_six_second_preparation_and_five_second_fallback(tmp_path):
    config = ViewerConfig(tmp_path / "checkpoint.pth")

    assert config.use_wall_clock_preparation is True
    assert config.preparation_seconds == 6.0
    assert config.backline_fallback_seconds == 5.0


def test_backline_fallback_places_first_bench_unit_in_first_vacant_backline_slot():
    session = _session(level=3, board_count=2, occupied_backline=(21,), bench_slots=(2,))

    assert session._backline_fallback_action(0) == [3, 0, 2, 22, 0, 0]


def test_backline_fallback_does_not_exceed_level_capacity():
    session = _session(level=3, board_count=3, occupied_backline=(21,), bench_slots=(2,))

    assert session._backline_fallback_action(0) is None


def test_backline_fallback_requires_a_bench_unit_and_vacant_backline_slot():
    no_bench_unit = _session(level=3, board_count=2, occupied_backline=(21,), bench_slots=())
    full_backline = _session(
        level=10, board_count=2, occupied_backline=tuple(range(21, 28)), bench_slots=(2,)
    )

    assert no_bench_unit._backline_fallback_action(0) is None
    assert full_backline._backline_fallback_action(0) is None
