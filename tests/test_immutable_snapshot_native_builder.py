"""Contract tests for immutable snapshot containers built by native bindings."""

import copy
import pytest

from immutable_snapshot import FrozenDict, FrozenList, freeze_snapshot


def test_native_empty_factories_preserve_container_contracts():
    nested = FrozenDict._empty()
    dict.__setitem__(nested, "items", FrozenList._empty())
    list.append(nested["items"], 1)
    assert isinstance(nested, dict)
    assert isinstance(nested["items"], list)
    assert nested["items"] == [1]
    assert copy.deepcopy(nested) is nested
    with pytest.raises(TypeError, match="immutable"):
        nested["new"] = 2
    with pytest.raises(TypeError, match="immutable"):
        nested["items"].append(2)


def test_native_container_factories_match_recursive_freeze_semantics():
    native_built = FrozenDict._empty()
    children = FrozenList._empty()
    player = FrozenDict._empty()
    board = FrozenList._empty()
    dict.__setitem__(player, "board", board)
    list.append(board, FrozenDict._empty())
    list.append(children, player)
    dict.__setitem__(native_built, "players", children)
    expected = freeze_snapshot({"players": [{"board": [{}]}]})
    assert native_built == expected
    assert type(native_built) is type(expected)
    assert type(native_built["players"]) is type(expected["players"])
    assert type(native_built["players"][0]["board"][0]) is type(expected["players"][0]["board"][0])
