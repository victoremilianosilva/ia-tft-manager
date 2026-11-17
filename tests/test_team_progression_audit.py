from scripts.audit_viewer_match import audit_team_progression


def _unit(name, impact=1.0, star=1):
    return {"occupied": True, "champion_id": name, "name": name, "impact": impact, "star": star, "traits": []}


def _state(*, board=(), bench=(), gold=10, level=3, direction="CompA", pairs=0):
    return {
        "board": list(board) + [{"occupied": False}] * (4 - len(board)),
        "bench": list(bench) + [{"occupied": False}] * (4 - len(bench)),
        "gold": gold, "level": level, "xp": 0, "hp": 80,
        "placement": None, "comp_direction": direction, "comp_focus": "Carry",
        "composition_strength": 1.0, "positioning_score": 0.25,
        "active_traits": {}, "board_quality_score": 0.2,
    }


def test_team_progression_separates_board_strength_from_bench_potential_and_pairs():
    before = _state(board=[_unit("Tank", 3)], bench=[_unit("Carry", 2)], gold=10)
    after = _state(board=[_unit("Tank", 3)], bench=[_unit("Carry", 2), _unit("Carry", 2)], gold=8)
    entries = [{
        "event_type": "action", "sequence_id": 1, "step": 1, "stage": 2, "round_in_stage": 1,
        "payload": {
            "action_name": "BUY", "combat_reward": 0.0,
            "state_before": before, "state_after": after,
            "economic_diagnostics": {"action_cost": 2, "purchased_champion": "Carry"},
            "strategic_snapshot_before": {
                "board_strength": 3.0, "bench_potential_strength": 2.0,
                "board_two_star_or_higher": 0, "board_three_star": 0,
                "combined_pair_count": 0, "board_occupancy": 0.25, "gold": 10, "level": 3,
                "active_synergies": {}, "positioning_quality": 0.25,
                "composition_direction": "CompA", "composition_focus": "Carry",
            },
            "strategic_snapshot_after": {
                "board_strength": 3.0, "bench_potential_strength": 4.0,
                "board_two_star_or_higher": 0, "board_three_star": 0,
                "combined_pair_count": 1, "board_occupancy": 0.25, "gold": 8, "level": 3,
                "active_synergies": {}, "positioning_quality": 0.25,
                "composition_direction": "CompA", "composition_focus": "Carry",
            },
            "purchase_marginal_value": {
                "classification": "PAIR_POTENTIAL", "board_strength_delta": 0.0,
                "bench_potential_delta": 2.0,
            },
        },
    }]
    report = {}
    audit_team_progression(entries, "Jogador 1", report)
    metrics = report["team_progression_metrics"]["Jogador 1"]
    stage = metrics["stages"]["2-1"]
    assert stage["board_strength_start"] == 3.0
    assert stage["board_strength_end"] == 3.0
    assert stage["bench_potential_start"] == 2.0
    assert stage["bench_potential_end"] == 4.0
    assert stage["pairs_start"] == 0
    assert stage["pairs_end"] == 1
    assert stage["gold_spent"] == 2
    assert metrics["purchase_marginal_classes"] == {"PAIR_POTENTIAL": 1}
    assert metrics["final_gold"] == 8


def test_team_progression_tracks_stage_deltas_synergy_and_direction_changes():
    before = _state(board=[_unit("Tank", 2)], direction="CompA")
    after = _state(board=[_unit("Tank", 2), _unit("Carry", 3, star=2)], direction="CompB", gold=6)
    entries = [{
        "event_type": "action", "sequence_id": 1, "step": 5, "stage": 3, "round_in_stage": 2,
        "payload": {
            "action_name": "MOVE_BENCH", "combat_reward": 0.5,
            "state_before": before, "state_after": after,
            "economic_diagnostics": {"action_cost": 0},
            "strategic_snapshot_before": {
                "board_strength": 2, "bench_potential_strength": 0,
                "board_two_star_or_higher": 0, "board_three_star": 0,
                "combined_pair_count": 0, "board_occupancy": 0.25, "gold": 10, "level": 3,
                "active_synergies": {"TraitA": 1}, "positioning_quality": 0.1,
                "composition_direction": "CompA", "composition_focus": "Tank",
            },
            "strategic_snapshot_after": {
                "board_strength": 5, "bench_potential_strength": 0,
                "board_two_star_or_higher": 1, "board_three_star": 0,
                "combined_pair_count": 0, "board_occupancy": 0.5, "gold": 6, "level": 3,
                "active_synergies": {"TraitA": 0, "TraitB": 1}, "positioning_quality": 0.4,
                "composition_direction": "CompB", "composition_focus": "Carry",
            },
        },
    }]
    report = {}
    audit_team_progression(entries, "Jogador 2", report)
    metrics = report["team_progression_metrics"]["Jogador 2"]
    stage = metrics["stages"]["3-2"]
    assert stage["board_strength_delta"] == 3.0
    assert stage["board_two_star_start"] == 0
    assert stage["board_two_star_end"] == 1
    assert stage["synergy_milestones_reached"][0]["trait"] == "TraitB"
    assert stage["synergy_milestones_lost"][0]["trait"] == "TraitA"
    assert stage["composition_changes"][0]["from"] == "CompA"
    assert stage["composition_changes"][0]["to"] == "CompB"
    assert stage["mean_combat_reward"] == 0.5
    assert metrics["composition_direction_changes"] == 1
