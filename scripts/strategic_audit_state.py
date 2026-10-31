"""Stable state-diff helpers shared by strategic audit scripts."""
from __future__ import annotations


def _unit_key(unit):
    if not isinstance(unit, dict) or not unit.get("occupied"):
        return None
    return (str(unit.get("uuid", "")), str(unit.get("champion_id", "")),
            int(unit.get("star", 1)), tuple(unit.get("item_ids", []) or []))


def state_signature(player):
    def slots(name):
        return tuple(_unit_key(unit) for unit in player.get(name, []) or [])
    return (slots("board"), slots("bench"), tuple(player.get("item_components", []) or []),
            tuple(player.get("item_inventory", []) or []))


def diff_units(before, after):
    def collect(player):
        result = {}
        for area in ("board", "bench"):
            for index, unit in enumerate(player.get(area, []) or []):
                key = _unit_key(unit)
                if key is not None:
                    identity = key[0] or (key[1], key[2], key[3])
                    result[identity] = {"area": area, "slot": index, "unit": unit}
        return result
    old, new = collect(before), collect(after)
    return {"added": [new[k] for k in new.keys() - old.keys()],
            "removed": [old[k] for k in old.keys() - new.keys()],
            "moved": [{"before": old[k], "after": new[k]} for k in old.keys() & new.keys()
                      if (old[k]["area"], old[k]["slot"]) != (new[k]["area"], new[k]["slot"])]}


def composition_delta(before_summary, after_summary, before, after):
    keys = ("composition_direction", "composition_focus", "composition_strength",
            "core_units", "core_traits", "board_composition_score", "board_unit_count",
            "board_two_star_count")
    result = {key: {"before": before_summary.get(key), "after": after_summary.get(key)}
              for key in keys if before_summary.get(key) != after_summary.get(key)}
    result["units"] = diff_units(before, after)
    return result


def detect_cycle(signature, visited, step):
    previous = visited.get(signature)
    if previous is None:
        return None
    previous_step = int(previous.get("step", -1)) if isinstance(previous, dict) else -1
    return {"detected": True, "previous_step": previous_step,
            "cycle_length": int(step) - previous_step}
