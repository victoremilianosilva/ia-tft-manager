"""State-diff helpers for strategic TFT audits.

Unit UUIDs are authoritative when exposed by the native engine. Champion/ordinal
fallbacks are marked lower-confidence and should not be treated as globally unique.
"""
from __future__ import annotations

import json
from collections import defaultdict
from typing import Any


def state_signature(player: dict[str, Any]) -> str:
    """Canonical board+bench signature including unit identity and star level."""
    def slots(units):
        result = []
        for unit in units or []:
            if not isinstance(unit, dict) or not unit.get("occupied"):
                result.append(None)
            else:
                result.append({
                    "unit_id": str(unit.get("uuid") or ""),
                    "champion_id": str(unit.get("champion_id") or ""),
                    "star": int(unit.get("star", 0) or 0),
                })
        return result
    return json.dumps(
        {"board": slots(player.get("board")), "bench": slots(player.get("bench"))},
        sort_keys=True, separators=(",", ":"),
    )


def _unit_locations(player: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Map units to stable IDs and explicit zone/slot locations."""
    found: dict[str, dict[str, Any]] = {}
    duplicate_counts: dict[str, int] = defaultdict(int)
    for zone in ("board", "bench"):
        for slot, unit in enumerate(player.get(zone) or []):
            if not isinstance(unit, dict) or not unit.get("occupied"):
                continue
            uuid = str(unit.get("uuid") or "").strip()
            champion = str(unit.get("champion_id") or "unknown")
            if uuid:
                unit_id, confidence = f"uuid:{uuid}", "engine_uuid"
            else:
                # Deterministic fallback across a single snapshot. Not guaranteed
                # to track a particular duplicate copy across snapshots.
                base = f"champion:{champion}"
                ordinal = duplicate_counts[base]
                duplicate_counts[base] += 1
                unit_id, confidence = f"{base}:copy:{ordinal}", "champion_ordinal_fallback"
            found[unit_id] = {
                "unit_id": unit_id,
                "identity_confidence": confidence,
                "champion_id": champion,
                "star": int(unit.get("star", 0) or 0),
                "zone": zone,
                "slot": slot,
                "location": f"{zone}[{slot}]",
            }
    return found


def diff_units(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    """Describe actual unit moves, additions/removals, and star changes."""
    old, new = _unit_locations(before), _unit_locations(after)
    moved, added, removed, upgraded = [], [], [], []
    for unit_id in sorted(old.keys() & new.keys()):
        a, b = old[unit_id], new[unit_id]
        if (a["zone"], a["slot"]) != (b["zone"], b["slot"]):
            moved.append({
                **{k: a[k] for k in ("unit_id", "identity_confidence", "champion_id", "star")},
                "from": {"zone": a["zone"], "slot": a["slot"], "location": a["location"]},
                "to": {"zone": b["zone"], "slot": b["slot"], "location": b["location"]},
            })
        if a["star"] != b["star"]:
            upgraded.append({"unit_id": unit_id, "champion_id": b["champion_id"],
                             "star_before": a["star"], "star_after": b["star"]})
    for unit_id in sorted(new.keys() - old.keys()):
        added.append(new[unit_id])
    for unit_id in sorted(old.keys() - new.keys()):
        removed.append(old[unit_id])
    return {"moved_units": moved, "added_units": added, "removed_units": removed,
            "star_changes": upgraded, "unit_state_changed": bool(moved or added or removed or upgraded)}


def composition_delta(before_strategy: dict[str, Any], after_strategy: dict[str, Any],
                      before_player: dict[str, Any], after_player: dict[str, Any]) -> dict[str, Any]:
    """Summarize strategic and board-composition changes around one action."""
    def board_units(player):
        return [
            {"champion_id": str(u.get("champion_id") or ""),
             "uuid": str(u.get("uuid") or ""),
             "star": int(u.get("star", 0) or 0)}
            for u in player.get("board", []) or []
            if isinstance(u, dict) and u.get("occupied")
        ]
    fields = ("composition_direction", "composition_locked", "composition_focus",
              "composition_strength", "core_units", "core_traits", "active_traits",
              "board_composition_score", "board_unit_count", "board_two_star_count")
    before = {k: before_strategy.get(k) for k in fields}
    after = {k: after_strategy.get(k) for k in fields}
    return {
        "board_units_before": board_units(before_player),
        "board_units_after": board_units(after_player),
        "board_units_changed": board_units(before_player) != board_units(after_player),
        "strategy_before": before,
        "strategy_after": after,
        "strategy_fields_changed": [k for k in fields if before.get(k) != after.get(k)],
        "board_composition_score_delta": _number(after.get("board_composition_score"))
            - _number(before.get("board_composition_score")),
        "board_unit_count_delta": _number(after.get("board_unit_count"))
            - _number(before.get("board_unit_count")),
        "board_two_star_count_delta": _number(after.get("board_two_star_count"))
            - _number(before.get("board_two_star_count")),
    }


def _number(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError, OverflowError):
        return 0.0


def detect_cycle(signature: str, visited: dict[str, dict[str, Any]], step: int):
    """Return prior-state evidence if the current board+bench state was seen."""
    previous = visited.get(signature)
    if previous is None:
        return None
    return {
        "previous_step": int(previous["step"]),
        "cycle_length": int(step - previous["step"]),
        "previous_action": previous.get("action"),
    }
