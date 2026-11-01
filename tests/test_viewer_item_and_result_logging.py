from viewer.player_logs import PlayerJsonLogWriter


def test_item_actions_are_not_logged_as_passes():
    writer = object.__new__(PlayerJsonLogWriter)

    assert "EQUIP_FROM_INVENTORY" in writer._action_text([7, 0, 0, 0, 0, 0], {})
    assert "CRAFT_AND_EQUIP" in writer._action_text([8, 0, 0, 0, 0, 0], {})


def test_anvil_choice_is_not_logged_as_normal_equipment():
    writer = object.__new__(PlayerJsonLogWriter)
    before = {
        "pending_anvil": True,
        "pending_anvil_kind": 0,
        "pending_anvil_options": ["BFSword", "RecurveBow", "NeedlesslyLargeRod"],
        "item_inventory": [],
        "board": [],
        "bench": [],
    }
    assert writer._action_text([7, 1, 0, 0, 0, 0], before) == (
        "BIGORNA: escolheu componente RecurveBow"
    )
    after_state = {
        "last_item_action_kind": "anvil_component_choice",
        "last_item_id": "RecurveBow",
        "last_item_target_slot": -1,
        "last_item_target_on_board": False,
    }
    decision = writer._item_action_diagnostics(
        [7, 1, 0, 0, 0, 0], before, {}, after_state,
        {"components": [], "inventory": [], "equipped": []},
        {"components": ["RecurveBow"], "inventory": [], "equipped": []},
    )
    assert decision["is_anvil_choice"] is True
    assert decision["anvil_kind"] == "component"
    assert decision["selected_id"] == "RecurveBow"
    assert decision["selected_item_id"] is None
    assert decision["selected_component_id"] == "RecurveBow"
    assert decision["target"] is None


def test_item_action_audit_records_selected_item_and_exact_target():
    writer = object.__new__(PlayerJsonLogWriter)
    before = {
        "item_inventory": ["Deathblade"],
        "item_component_catalog": [],
        "pending_anvil": False,
        "board": [],
        "bench": [],
    }
    target = {
        "uuid": "unit-carry-1", "champion_id": "TFT_TestCarry",
        "name": "Test Carry", "star": 2, "items": ["Deathblade"],
    }
    after_state = {
        "last_item_action_kind": "equip_inventory_item",
        "last_item_id": "Deathblade",
        "last_item_target_uuid": "unit-carry-1",
        "last_item_target_slot": 0,
        "last_item_target_on_board": True,
        "last_item_fit": 4.25,
        "last_item_immediate_strength": 0.31,
        "last_item_role_alignment": 0.8,
        "last_item_assignment_reward": 0.12,
        "board": [target],
        "bench": [],
    }
    decision = writer._item_action_diagnostics(
        [7, 0, 0, 0, 0, 0], before, {}, after_state,
        {"components": [], "inventory": ["Deathblade"], "equipped": []},
        {"components": [], "inventory": [], "equipped": [
            {"location": "board", "slot": 0, "uuid": "unit-carry-1", "items": ["Deathblade"]}
        ]},
    )
    assert decision["operation"] == "equip_inventory_item"
    assert decision["selected_item_id"] == "Deathblade"
    assert decision["target"]["uuid"] == "unit-carry-1"
    assert decision["target"]["location"] == "board"
    assert decision["target"]["slot"] == 0
    assert decision["item_fit"] == 4.25
    assert decision["estimated_immediate_strength"] == 0.31
    assert decision["assignment_reward"] == 0.12


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
