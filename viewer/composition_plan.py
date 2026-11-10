"""Pure helpers for presenting the native composition plan in the viewer."""
from __future__ import annotations

from collections import Counter


def summarize_planned_traits(units: list[dict], highlighted_traits: list[str] | None = None):
    """Return (trait, count, highlighted) rows for the planned lineup."""
    counts = Counter(
        str(trait)
        for unit in units
        for trait in (unit.get("traits") or [])
        if trait
    )
    highlighted = set(highlighted_traits or [])
    return sorted(
        ((trait, count, trait in highlighted) for trait, count in counts.items()),
        key=lambda row: (not row[2], -row[1], row[0].casefold()),
    )


def suggest_initial_positions(units: list[dict]) -> dict[int, dict]:
    """Build an explanatory role-based formation preview (not an engine command)."""
    lanes = {"front": [], "mid_front": [], "mid_back": [], "back": []}
    for unit in units:
        profile = unit.get("combat_profile") or {}
        role_name = str(unit.get("role_name") or profile.get("role_name") or "").casefold()
        attack_range = float(profile.get("attack_range", 0.0) or 0.0)
        if profile.get("is_tank") or (profile.get("frontline") and not profile.get("is_fighter")):
            lane = "front"
        elif profile.get("is_carry") or profile.get("is_support") or profile.get("backline") or attack_range >= 3:
            lane = "back"
        elif profile.get("is_fighter") or role_name in {"fighter", "bruiser"}:
            lane = "mid_front"
        elif role_name in {"mage", "marksman", "ranged"}:
            lane = "back"
        else:
            lane = "mid_back"
        lanes[lane].append(unit)

    result: dict[int, dict] = {}
    row_for_lane = {"front": 0, "mid_front": 1, "mid_back": 2, "back": 3}
    overflow = []
    for lane, row in row_for_lane.items():
        lane_units = lanes[lane]
        if len(lane_units) > 7:
            overflow.extend(lane_units[7:])
            lane_units = lane_units[:7]
        start = (7 - len(lane_units)) // 2
        for offset, unit in enumerate(lane_units):
            result[row * 7 + start + offset] = unit

    # Keep every planned unit visible if an unusual catalog has >7 units in a lane.
    for unit in overflow:
        free = next((index for index in range(28) if index not in result), None)
        if free is None:
            break
        result[free] = unit
    return result



def is_position_misplaced(unit: dict, row: int) -> bool:
    """Flag only clear front/backline mismatches; rows are zero-based."""
    profile = unit.get("combat_profile") or {}
    role_name = str(unit.get("role_name") or profile.get("role_name") or "").casefold()
    is_front = bool(profile.get("is_tank") or profile.get("is_fighter")) or role_name in {"tank", "fighter", "bruiser"}
    is_back = bool(profile.get("is_carry") or profile.get("is_support") or profile.get("is_assassin")) or role_name in {"carry", "support", "assassin", "mage", "marksman", "ranged"}
    if is_front and is_back:
        # Explicit role name wins when catalog flags are stale or contradictory.
        if role_name in {"tank", "fighter", "bruiser"}:
            is_back = False
        elif role_name in {"carry", "support", "assassin", "mage", "marksman", "ranged"}:
            is_front = False
        else:
            return False
    if is_front:
        return row >= 2
    if is_back:
        return row <= 1
    # Unknown roles should not be marked as wrong based on a guess.
    return False
