"""Immutable, shareable ownership for native audit snapshot subtrees.

The native snapshot is a JSON-like value. Freeze a player subtree once at the
Python ownership boundary; deepcopy then safely reuses that immutable value
inside RolloutBuffer instead of cloning the same nested tree on every access.
"""

from collections.abc import Mapping
import copy


class FrozenDict(dict):
    """Dict-compatible immutable mapping; preserves isinstance(value, dict)."""

    def __init__(self, values=()):
        dict.__init__(self)
        source = values.items() if isinstance(values, Mapping) else values
        for key, value in source:
            dict.__setitem__(self, key, freeze_snapshot(value))

    @classmethod
    def _empty(cls):
        """Allocate an empty instance for the native builder to populate."""
        return dict.__new__(cls)

    def _immutable(self, *_args, **_kwargs):
        raise TypeError("snapshot ownership is immutable")

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    pop = _immutable
    popitem = _immutable
    setdefault = _immutable
    update = _immutable
    __ior__ = _immutable

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self


class FrozenList(list):
    """List-compatible immutable sequence; preserves isinstance(value, list)."""

    def __init__(self, values=()):
        list.__init__(self, (freeze_snapshot(value) for value in values))

    @classmethod
    def _empty(cls):
        """Allocate an empty instance for the native builder to populate."""
        return list.__new__(cls)

    def _immutable(self, *_args, **_kwargs):
        raise TypeError("snapshot ownership is immutable")

    __setitem__ = _immutable
    __delitem__ = _immutable
    __iadd__ = _immutable
    __imul__ = _immutable
    append = _immutable
    clear = _immutable
    extend = _immutable
    insert = _immutable
    pop = _immutable
    remove = _immutable
    reverse = _immutable
    sort = _immutable

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self


def freeze_snapshot(value):
    """Copy a JSON-like snapshot subtree into immutable, deepcopy-shareable data."""
    if isinstance(value, FrozenDict) or isinstance(value, FrozenList):
        return value
    if isinstance(value, Mapping):
        return FrozenDict(value)
    if isinstance(value, list):
        return FrozenList(value)
    if isinstance(value, tuple):
        return tuple(freeze_snapshot(item) for item in value)
    if isinstance(value, (str, bytes, int, float, bool, type(None))):
        return value
    # Preserve support for uncommon immutable scalar/container values without
    # silently sharing an object whose mutation semantics are unknown.
    return copy.deepcopy(value)
