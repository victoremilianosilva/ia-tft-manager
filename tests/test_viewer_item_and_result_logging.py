from viewer.player_logs import PlayerJsonLogWriter


def test_item_actions_are_not_logged_as_passes():
    writer = object.__new__(PlayerJsonLogWriter)

    assert "EQUIP_FROM_INVENTORY" in writer._action_text([7, 0, 0, 0, 0, 0], {})
    assert "CRAFT_AND_EQUIP" in writer._action_text([8, 0, 0, 0, 0, 0], {})


def test_final_report_marks_winner_from_engine_winner_id():
    text = PlayerJsonLogWriter._final_result_text(
        2, {"winner_id": 2}, {"placement": 1, "hp": 15, "gold": 3, "level": 8, "wins": 4, "losses": 2}
    )
    assert "VITÓRIA" in text
    assert "VENCEDOR DA PARTIDA: JOGADOR 3" in text
    assert "HP final: 15" in text


def test_final_report_does_not_invent_missing_placement():
    text = PlayerJsonLogWriter._final_result_text(
        0, {}, {"alive": True, "hp": 10, "gold": 40, "level": 6}
    )
    assert "colocação não fornecida pela engine" in text


def test_item_state_captures_bag_and_equipped_units():
    audit = {
        "item_components": ["BFSword"],
        "item_inventory": ["Deathblade"],
        "board": [{
            "occupied": True, "slot": 3, "champion_id": "TFT_TestCarry",
            "uuid": "unit-1", "items": ["Deathblade"],
        }],
        "bench": [],
    }
    state = PlayerJsonLogWriter._item_state(audit)
    assert state["components"] == ["BFSword"]
    assert state["inventory"] == ["Deathblade"]
    assert state["equipped"][0]["champion_id"] == "TFT_TestCarry"
    assert state["equipped"][0]["items"] == ["Deathblade"]
