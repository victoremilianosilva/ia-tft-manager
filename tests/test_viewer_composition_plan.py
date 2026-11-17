from viewer.composition_plan import summarize_planned_traits, suggest_initial_positions, is_position_misplaced


def test_planned_trait_summary_counts_synergies_and_marks_planner_priorities():
    units = [
        {"traits": ["Vanguard", "Mystic"]},
        {"traits": ["Vanguard", "Arcanist"]},
        {"traits": ["Mystic"]},
    ]

    assert summarize_planned_traits(units, ["Vanguard"]) == [
        ("Vanguard", 2, True),
        ("Mystic", 2, False),
        ("Arcanist", 1, False),
    ]


def test_initial_formation_preview_puts_tanks_forward_and_carry_in_backline():
    tank = {
        "name": "Tank",
        "combat_profile": {"is_tank": True, "frontline": True, "attack_range": 1},
    }
    carry = {
        "name": "Carry",
        "combat_profile": {"is_carry": True, "backline": True, "attack_range": 4},
    }
    fighter = {
        "name": "Fighter",
        "combat_profile": {"is_fighter": True, "frontline": True, "attack_range": 1},
    }

    positions = suggest_initial_positions([tank, carry, fighter])

    assert positions[3] is tank
    assert positions[10] is fighter
    assert positions[24] is carry
    assert len(positions) == 3


def test_formation_preview_keeps_all_units_visible_when_lane_overflows():
    units = [{"name": f"unit-{i}", "combat_profile": {"is_tank": True}} for i in range(10)]

    positions = suggest_initial_positions(units)

    assert len(positions) == 10
    assert set(unit["name"] for unit in positions.values()) == {unit["name"] for unit in units}



def test_position_warning_marks_only_clear_front_backline_mismatches():
    fighter = {"role_name": "fighter", "combat_profile": {"is_fighter": True}}
    carry = {"role_name": "carry", "combat_profile": {"is_carry": True}}
    unknown = {"role_name": "unknown", "combat_profile": {}}

    assert is_position_misplaced(fighter, 0) is False
    assert is_position_misplaced(fighter, 1) is False
    assert is_position_misplaced(fighter, 2) is True
    assert is_position_misplaced(fighter, 3) is True
    assert is_position_misplaced(carry, 0) is True
    assert is_position_misplaced(carry, 1) is True
    assert is_position_misplaced(carry, 2) is False
    assert is_position_misplaced(carry, 3) is False
    assert is_position_misplaced(unknown, 0) is False


def test_explicit_role_name_wins_over_stale_contradictory_flags():
    fighter = {"role_name": "fighter", "combat_profile": {
        "is_fighter": True, "is_tank": True, "is_carry": True,
    }}

    assert is_position_misplaced(fighter, 0) is False
    assert is_position_misplaced(fighter, 3) is True
