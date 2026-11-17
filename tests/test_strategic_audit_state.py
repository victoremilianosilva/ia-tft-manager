from scripts.strategic_audit_state import (
    composition_delta,
    detect_cycle,
    diff_units,
    state_signature,
)


def unit(uuid, champion="TFT_Nasus", star=1):
    return {"occupied": True, "uuid": uuid, "champion_id": champion, "star": star}


def player(board, bench):
    return {
        "board": board + [ {"occupied": False} for _ in range(max(0, 2-len(board))) ],
        "bench": bench + [ {"occupied": False} for _ in range(max(0, 2-len(bench))) ],
    }


def test_unit_move_records_stable_id_and_effective_origin_destination():
    before = player([], [unit("u-1")])
    after = player([unit("u-1")], [])
    delta = diff_units(before, after)

    assert delta["unit_state_changed"] is True
    assert len(delta["moved_units"]) == 1
    move = delta["moved_units"][0]
    assert move["unit_id"] == "uuid:u-1"
    assert move["from"] == {"zone": "bench", "slot": 0, "location": "bench[0]"}
    assert move["to"] == {"zone": "board", "slot": 0, "location": "board[0]"}
    assert delta["added_units"] == []
    assert delta["removed_units"] == []


def test_return_to_previously_seen_board_bench_state_is_confirmed_cycle():
    initial = player([unit("u-1")], [])
    moved_out = player([], [unit("u-1")])
    visited = {state_signature(initial): {"step": 2, "action": [3, 0, 0, 0, 0, 0]}}
    assert state_signature(initial) != state_signature(moved_out)

    cycle = detect_cycle(state_signature(initial), visited, step=5)
    assert cycle == {
        "previous_step": 2,
        "cycle_length": 3,
        "previous_action": [3, 0, 0, 0, 0, 0],
    }


def test_same_champion_different_uuid_is_not_mistaken_for_same_unit():
    before = player([unit("u-1")], [])
    after = player([unit("u-2")], [])
    delta = diff_units(before, after)
    assert delta["moved_units"] == []
    assert {x["unit_id"] for x in delta["removed_units"]} == {"uuid:u-1"}
    assert {x["unit_id"] for x in delta["added_units"]} == {"uuid:u-2"}


def test_composition_delta_keeps_strategy_before_after_and_score_delta():
    before_player = player([unit("u-1")], [])
    after_player = player([unit("u-1", star=2)], [])
    before_strategy = {
        "composition_direction": "Nasus",
        "composition_locked": False,
        "composition_focus": "TFT_Nasus",
        "composition_strength": 0.3,
        "board_composition_score": 1.25,
        "board_unit_count": 1,
        "board_two_star_count": 0,
        "core_units": ["TFT_Nasus"],
        "core_traits": ["Shurima"],
        "active_traits": {"Shurima": 1},
    }
    after_strategy = {
        **before_strategy,
        "composition_locked": True,
        "composition_strength": 0.6,
        "board_composition_score": 1.75,
        "board_two_star_count": 1,
    }
    delta = composition_delta(before_strategy, after_strategy, before_player, after_player)
    assert delta["board_units_changed"] is True
    assert delta["board_composition_score_delta"] == 0.5
    assert delta["board_two_star_count_delta"] == 1.0
    assert "composition_locked" in delta["strategy_fields_changed"]
