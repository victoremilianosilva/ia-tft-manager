"""Stable item-action representation; native C++ remains authoritative for legality."""
from __future__ import annotations
from enum import IntEnum
from typing import Mapping, Sequence

class ItemActionType(IntEnum):
    WAIT = 0
    CRAFT = 1
    EQUIP = 2
    TRANSFER = 3
    UNEQUIP = 4

class UnitLocation(IntEnum):
    BENCH = 0
    BOARD = 1

ITEM_ACTION_DIMS = (5, 18, 18, 18, 37, 37, 3)
ITEM_ACTION_KEYS = ("type", "first_component", "second_component", "inventory_item",
                    "source_unit", "target_unit", "equipped_item")

def normalize_item_action(action: Sequence[int] | Mapping[str, int]) -> list[int]:
    """Normalize shape and bounds. This is not a substitute for native state masks."""
    if isinstance(action, Mapping):
        values = [int(action.get(key, 0)) for key in ITEM_ACTION_KEYS]
    else:
        values = list(action)
        if len(values) != len(ITEM_ACTION_DIMS):
            raise ValueError(f"Item action must contain {len(ITEM_ACTION_DIMS)} components; received {len(values)}.")
        try:
            values = [int(value) for value in values]
        except (TypeError, ValueError) as exc:
            raise ValueError("Item action components must be integers.") from exc
    if len(values) != len(ITEM_ACTION_DIMS):
        raise ValueError(f"Item action must contain {len(ITEM_ACTION_DIMS)} components; received {len(values)}.")
    for index, (value, dimension) in enumerate(zip(values, ITEM_ACTION_DIMS)):
        if value < 0 or value >= dimension:
            raise ValueError(f"Item action component {ITEM_ACTION_KEYS[index]}={value} is outside [0, {dimension}).")
    if values[0] == ItemActionType.TRANSFER and values[4] == values[5]:
        raise ValueError("An item cannot be transferred to the same unit.")
    return values
