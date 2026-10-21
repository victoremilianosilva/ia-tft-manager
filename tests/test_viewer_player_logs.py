"""Regression tests for one readable JSON movement log per TFT player."""
import json

from viewer.player_logs import PlayerJsonLogWriter


def _unit(occupied=False, **overrides):
    value = {"occupied": occupied}
    value.update(overrides)
    return value


def _snapshot(with_unit=False):
    public_players = []
    audit_players = []
    for player_id in range(8):
        board = [_unit() for _ in range(28)]
        bench = [_unit() for _ in range(9)]
        shop = [_unit() for _ in range(5)]
        if with_unit and player_id == 0:
            bench[0] = _unit(
                True, champion_id="TFT_Test_Briar", uuid="briar-1", star=1, cost=1
            )
            shop[0] = _unit(
                True, champion_id="TFT_Test_Briar", uuid="shop-briar", star=1, cost=1
            )
        public_players.append({
            "player_id": player_id, "hp": 100, "gold": 10, "level": 2, "xp": 0,
            "alive": True, "eliminated": False, "wins": 0, "losses": 0,
            "placement": None, "opponent_id": None,
        })
        audit_players.append({
            "player_id": player_id, "gold": 10, "level": 2, "xp": 0,
            "win_streak": 0, "loss_streak": 0,
            "round_gold": 8 if player_id == 0 else 0,
            "round_base_gold": 5 if player_id == 0 else 0,
            "round_interest": 2 if player_id == 0 else 0,
            "round_streak_gold": 1 if player_id == 0 else 0,
            "round_win_gold": 1 if player_id == 0 else 0,
            "strategy_info": {
                "strategy": 1 if player_id == 0 else 0,
                "strategy_name": "STABILIZE" if player_id == 0 else "ECON",
                "composition_direction": "Space Groove" if player_id == 0 else "",
                "composition_focus": "Teemo" if player_id == 0 else "",
                "confidence": 0.75 if player_id == 0 else 0.0,
                "reason": "composition fit" if player_id == 0 else "",
                "core_units": ["TFT_Test_Briar"] if player_id == 0 else [],
                "core_traits": ["Space Groove"] if player_id == 0 else [],
                "active_traits": {"Space Groove": 2} if player_id == 0 else {},
                "strategy_scores": {"1": 0.8} if player_id == 0 else {},
            },
            "board": board, "bench": bench, "shop": shop,
        })
    return {
        "round": 1, "stage": 1, "finished": False,
        "players": public_players, "audit_players": audit_players,
        "ranking": [], "winner_id": None,
    }


def _empty_info(events=None):
    return {
        "events": list(events or []),
        "action_rewards": [0.05] * 8,
        "combat_rewards": [0.0] * 8,
        "placement_rewards": [0.0] * 8,
    }


def test_writes_one_json_log_per_player_with_legacy_movement_lines(tmp_path):
    catalog = tmp_path / "units.json"
    catalog.write_text(json.dumps([{
        "apiName": "TFT_Test_Briar",
        "characterName": "TFT_Test_Briar",
        "name": "Briar",
        "cost": 1,
        "role": 0,
        "role_name": "tank",
        "traits": ["TestTrait"],
        "combat_profile": {"role": 0, "role_name": "tank"},
    }]), encoding="utf-8")

    before = _snapshot(with_unit=True)
    after = json.loads(json.dumps(before))
    after["audit_players"][0]["board"][0] = after["audit_players"][0]["bench"][0]
    after["audit_players"][0]["bench"][0] = _unit()
    # Only player 1 gets the unit; other players' state remains independent.
    actions = [[3, 0, 0, 0, 0, 0] for _ in range(8)]

    writer = PlayerJsonLogWriter(
        tmp_path / "match-test",
        match_id="match-test",
        checkpoint_sha256="abc123",
        seed=42,
        deterministic=True,
        catalog_path=catalog,
        initial_snapshot=before,
    )
    writer.record_step(
        before=before,
        after=after,
        actions=actions,
        diagnostics=[{"action_name": "MOVE_BENCH", "value_estimate": 0.3} for _ in range(8)],
        rewards=[0.05] * 8,
        info=_empty_info(),
        step=1,
        finished=False,
    )

    # End the round on the next batch, as the eight-seat native engine does.
    pass_actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
    writer.record_step(
        before=after,
        after=after,
        actions=pass_actions,
        diagnostics=[{"action_name": "PASS"} for _ in range(8)],
        rewards=[0.0] * 8,
        info=_empty_info(["ROUND_RESOLVED"]),
        step=2,
        finished=False,
    )
    writer.close()

    paths = sorted((tmp_path / "match-test").glob("player_*_log.json"))
    assert len(paths) == 8
    assert not (tmp_path / "match-test" / "events.jsonl").exists()

    player1 = json.loads((tmp_path / "match-test" / "player_1_log.json").read_text(encoding="utf-8"))
    assert player1["log_format"] == "tft_player_log"
    assert player1["player_id"] == 0
    assert player1["player_number"] == 1
    assert player1["impact_estimate_formula"].startswith("cost * star * 2.0")

    action_entry = next(item for item in player1["entries"] if item["event_type"] == "action")
    assert "MOVE Bench -> Board" in action_entry["text"]
    assert "Briar (i:2.0)" in action_entry["text"]
    assert action_entry["payload"]["state_after"]["board"][0]["name"] == "Briar"
    assert action_entry["payload"]["state_after"]["bench"][0]["occupied"] is False
    assert action_entry["payload"]["state_after"]["strategy_name"] == "STABILIZE"
    assert action_entry["payload"]["state_after"]["comp_direction"] == "Space Groove"
    assert action_entry["payload"]["state_after"]["comp_focus"] == "Teemo"
    assert "STRATEGY: STABILIZE" in (tmp_path / "match-test" / "player_1_log.tft").read_text(encoding="utf-8")
    assert "COMP DIRECTION: Space Groove" in (tmp_path / "match-test" / "player_1_log.tft").read_text(encoding="utf-8")
    assert "RENDA PRÓXIMO ROUND: +5 base, +2 juros, +1 sequência, +1 vitória (total: +9)" in (
        tmp_path / "match-test" / "player_1_log.tft"
    ).read_text(encoding="utf-8")
    assert action_entry["payload"]["state_after"]["round_interest"] == 2
    assert action_entry["payload"]["state_after"]["round_total_income"] == 9

    event_types = {entry["event_type"] for entry in player1["entries"]}
    assert {"round_finished", "board_header", "board_view", "bench_header", "bench_view", "shop_view"} <= event_types
    board_text = "".join(entry["text"] for entry in player1["entries"] if entry["event_type"] == "board_view")
    assert "[Bri|T|1*|i:2.0]" in board_text

    player2 = json.loads((tmp_path / "match-test" / "player_2_log.json").read_text(encoding="utf-8"))
    assert player2["player_id"] == 1
    player2_action = next(item for item in player2["entries"] if item["event_type"] == "action")
    assert "Vazio" in player2_action["text"]
    assert player2_action["payload"]["state_after"]["board"][0]["occupied"] is False
