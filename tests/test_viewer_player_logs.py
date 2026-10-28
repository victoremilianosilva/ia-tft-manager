"""Regression tests for per-player TFT text logs without JSON sidecar files."""
import json

from viewer.player_logs import PlayerJsonLogWriter
from scripts.audit_viewer_match import audit_economic_actions


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
            "gold_before_interest": 10 if player_id == 0 else 0,
            "interest_if_resolved_now": 1 if player_id == 0 else 0,
            "board_power": 0.0, "synergy_score": 0.0, "positioning_score": 0.0,
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
                "composition_locked": player_id == 0,
                "composition_strength": 3.25 if player_id == 0 else 0.0,
                "composition_candidate_direction": "",
                "composition_candidate_strength": 0.0,
                "composition_candidate_streak": 0,
                "previous_composition_direction": "",
                "previous_composition_strength": 0.0,
                "composition_direction_change_was_locked": False,
                "composition_direction_change_round": 0,
                "composition_direction_change_focus_weight": 0.0,
                "composition_direction_change_reason": "initial",
                "composition_direction_change_count": 0,
                "composition_focus_weights": {"Space Groove": 2.5, "Prankster": 1.2} if player_id == 0 else {},
                "confidence": 0.75 if player_id == 0 else 0.0,
                "reason": "composition fit" if player_id == 0 else "",
                "core_units": ["TFT_Test_Briar"] if player_id == 0 else [],
                "core_traits": ["Space Groove"] if player_id == 0 else [],
                "planned_units": ["TFT_Test_Briar", "TFT_Test_Teemo", "TFT_Test_Tank"] if player_id == 0 else [],
                "planned_unit_ids": [101, 202, 303] if player_id == 0 else [],
                "planned_traits": ["Space Groove", "Prankster"] if player_id == 0 else [],
                "planned_main_carry_id": 202 if player_id == 0 else -1,
                "planned_composition_score": 17.5 if player_id == 0 else 0.0,
                "planned_acquisition_notes": ["TFT_Test_Teemo (cost=1, chance_now~6%, chance_horizon~6%, hard_to_find)"] if player_id == 0 else [],
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


def test_writes_only_tft_logs_per_player_and_keeps_structured_diagnostics_in_memory(tmp_path):
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
    after["audit_players"][0]["board_power"] = 2.0
    after["audit_players"][0]["synergy_score"] = 1.0
    after["audit_players"][0]["positioning_score"] = 0.25
    # The engine step also resolves +5 income after this zero-cost move.
    after["players"][0]["gold"] = 15
    after["audit_players"][0]["gold"] = 15
    # Simulate a real strategy recomputation after the board changes.
    after["audit_players"][0]["strategy_info"]["composition_direction"] = "Prankster"
    after["audit_players"][0]["strategy_info"]["composition_focus"] = "Briar"
    after["audit_players"][0]["strategy_info"]["composition_locked"] = False
    after["audit_players"][0]["strategy_info"]["composition_strength"] = 2.0
    after["audit_players"][0]["strategy_info"]["previous_composition_direction"] = "Space Groove"
    after["audit_players"][0]["strategy_info"]["previous_composition_strength"] = 3.25
    after["audit_players"][0]["strategy_info"]["composition_direction_change_was_locked"] = True
    after["audit_players"][0]["strategy_info"]["composition_direction_change_round"] = 4
    after["audit_players"][0]["strategy_info"]["composition_direction_change_focus_weight"] = 1.4
    after["audit_players"][0]["strategy_info"]["composition_direction_change_reason"] = "persistent_superior_candidate"
    after["audit_players"][0]["strategy_info"]["composition_direction_change_count"] = 1
    after["audit_players"][0]["strategy_info"]["reason"] = "board fit changed"
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
        info=_empty_info(events=["ECONOMIC_ACTION player 0 action_cost=0 sale_proceeds=0 gold_before=10 gold_after=10 interest_before=1 interest_after=1 level_before=2 level_after=2 xp_before=0 xp_after=0"]),
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

    output_dir = tmp_path / "match-test"
    paths = sorted(output_dir.glob("player_*_log.tft"))
    assert len(paths) == 8
    assert not list(output_dir.glob("player_*_log.json"))
    assert not (output_dir / "events.jsonl").exists()

    player1_log_text = (output_dir / "player_1_log.tft").read_text(encoding="utf-8")
    assert "--- INÍCIO DA PARTIDA" in player1_log_text
    assert "MOVE Bench -> Board" in player1_log_text

    # Structured diagnostics are still used in memory by the writer/tests,
    # but are no longer serialized into per-player JSON files.
    player1 = writer.documents[0]
    assert player1["log_format"] == "tft_player_log"
    assert player1["player_id"] == 0
    assert player1["player_number"] == 1
    assert player1["impact_estimate_formula"].startswith("cost * star * 2.0")

    action_entry = next(item for item in player1["entries"] if item["event_type"] == "action")
    assert "MOVE Bench -> Board" in action_entry["text"]
    assert "Briar (i:2.0)" in action_entry["text"]
    assert action_entry["payload"]["state_after"]["board"][0]["name"] == "Briar"
    economics = action_entry["payload"]["economic_diagnostics"]
    assert economics["gold_before"] == 10
    assert economics["gold_after"] == 10  # action-time balance, before round income
    assert economics["gold_after_step"] == 15  # later snapshot includes round income
    assert economics["gold_delta"] == 0
    assert economics["board_power_delta"] == 2.0
    assert economics["gold_before_interest"] == 10
    assert economics["interest_if_resolved_before"] == 1
    assert economics["potential_interest_delta"] == 0
    assert economics["engine_synergy_after"] == 1.0
    assert economics["positioning_delta"] == 0.25
    assert economics["reason_code"] == "DEPLOY_BOARD_GAIN"
    assert economics["cost_source"] == "native_action_transition"
    assert economics["action_cost"] == 0
    assert economics["measurable_improvement"] is True
    assert economics["two_star_or_higher_after"] == 0
    assert economics["pairs_before"] == 0
    assert action_entry["payload"]["state_after"]["bench"][0]["occupied"] is False
    assert action_entry["payload"]["state_after"]["strategy_name"] == "STABILIZE"
    assert action_entry["payload"]["state_after"]["comp_direction"] == "Prankster"
    assert action_entry["payload"]["state_after"]["comp_focus"] == "Briar"
    plan_state = action_entry["payload"]["state_after"]
    assert plan_state["planned_units"] == ["TFT_Test_Briar", "TFT_Test_Teemo", "TFT_Test_Tank"]
    assert plan_state["planned_unit_ids"] == [101, 202, 303]
    assert plan_state["planned_traits"] == ["Space Groove", "Prankster"]
    assert plan_state["planned_main_carry_id"] == 202
    assert plan_state["planned_composition_score"] == 17.5
    assert plan_state["planned_acquisition_notes"] == ["TFT_Test_Teemo (cost=1, chance_now~6%, chance_horizon~6%, hard_to_find)"]
    assert "ACQUISITION CHECK:" in action_entry["text"]
    assert "chance_horizon~6%" in action_entry["text"]
    assert plan_state["planner_target_slots"] == 8
    assert plan_state["planner_mode"] == "LEVEL_8_CORE"
    assert "COMPOSITION PLAN [LEVEL_8_CORE]" in action_entry["text"]
    assert "TFT_Test_Teemo" in action_entry["text"]
    assert "level 1-8 targets the same 8-unit core" in action_entry["text"]
    assert plan_state["composition_locked"] is False
    assert action_entry["payload"]["state_after"]["composition_strength"] == 2.0
    comp_diag = action_entry["payload"]["composition_diagnostics"]
    assert comp_diag["direction_changed"] is True
    assert comp_diag["focus_changed"] is True
    assert comp_diag["lock_changed"] is True
    assert comp_diag["before"]["direction"] == "Space Groove"
    assert comp_diag["after"]["direction"] == "Prankster"
    assert comp_diag["after"]["reason"] == "board fit changed"
    assert comp_diag["direction_event"] == {
        "round": 4,
        "from": "Space Groove",
        "to": "Prankster",
        "from_strength": 3.25,
        "to_strength": 2.0,
        "was_locked": True,
        "focus_weight": 1.4,
        "reason": "persistent_superior_candidate",
        "change_count": 1,
    }
    assert comp_diag["candidate_direction"] == ""
    assert comp_diag["after"]["core_units"] == ["TFT_Test_Briar"]
    assert comp_diag["unit_fit"]["unit"] == "Briar"
    assert comp_diag["unit_fit"]["core_unit_match"] is True
    assert comp_diag["unit_fit"]["focus_fit_score"] == 0.0
    assert action_entry["payload"]["state_after"]["composition_focus_weights"]["Space Groove"] == 2.5
    log_text = (tmp_path / "match-test" / "player_1_log.tft").read_text(encoding="utf-8")
    assert "LOCK: OPEN" in log_text
    assert "STRENGTH: 2.00" in log_text
    assert "FOCUS WEIGHTS: Space Groove 2.50, Prankster 1.20" in log_text
    assert "STRATEGY: STABILIZE" in (tmp_path / "match-test" / "player_1_log.tft").read_text(encoding="utf-8")
    assert "COMP DIRECTION: Prankster" in (tmp_path / "match-test" / "player_1_log.tft").read_text(encoding="utf-8")
    assert "COMP BEFORE -> AFTER: dir=Space Groove -> Prankster" in log_text
    assert "foco=Teemo -> Briar" in log_text
    assert "STRATEGY REASON: board fit changed" in log_text
    assert "FIT UNIDADE: Briar | core=SIM | fit=0.00" in log_text
    assert "RENDA PRÓXIMO ROUND: +5 base, +2 juros, +1 sequência, +1 vitória (total: +9)" in (
        tmp_path / "match-test" / "player_1_log.tft"
    ).read_text(encoding="utf-8")
    assert action_entry["payload"]["state_after"]["round_interest"] == 2
    assert action_entry["payload"]["state_after"]["round_total_income"] == 9

    event_types = {entry["event_type"] for entry in player1["entries"]}
    assert {"round_finished", "board_header", "board_view", "bench_header", "bench_view", "shop_view"} <= event_types
    board_text = "".join(entry["text"] for entry in player1["entries"] if entry["event_type"] == "board_view")
    assert "[Bri|T|1*|i:2.0]" in board_text

    # Player 2's structured timeline remains available in memory, but is not persisted.
    player2 = writer.documents[1]
    assert player2["player_id"] == 1
    player2_action = next(item for item in player2["entries"] if item["event_type"] == "action")
    assert "Vazio" in player2_action["text"]
    assert player2_action["payload"]["state_after"]["board"][0]["occupied"] is False


def _economic_entry(sequence, action, diagnostics, gold, stage=2, round_number=3):
    return {
        "event_type": "action", "sequence_id": sequence, "stage": stage, "round": round_number,
        "payload": {
            "action_name": action,
            "action_reward": 0.0,
            "economic_diagnostics": diagnostics,
            "state_after": {"gold": gold, "board_power": 10.0, "board": [{"occupied": True}]},
        },
    }


def test_economic_action_audit_reports_cost_interest_xp_and_reroll_pass():
    entries = [
        _economic_entry(1, "BUY_XP", {
            "action_cost": 4, "sale_proceeds": 0, "potential_interest_delta": -1,
            "reason_code": "XP_NO_LEVEL_UP", "measurable_improvement": False,
        }, 15),
        _economic_entry(2, "REROLL", {
            "action_cost": 2, "sale_proceeds": 0, "potential_interest_delta": 0,
            "reason_code": "REROLL_NO_IMMEDIATE_BOARD_GAIN", "measurable_improvement": False,
        }, 13),
        _economic_entry(3, "PASS", {
            "action_cost": 0, "sale_proceeds": 0, "potential_interest_delta": 0,
            "reason_code": "PASS_NO_SPEND", "measurable_improvement": False,
        }, 13),
    ]
    report = {}
    audit_economic_actions(entries, "Jogador 1", report)
    metrics = report["economic_action_metrics"]["Jogador 1"]
    assert metrics["actions"] == 3
    assert metrics["gold_spent"] == 6
    assert metrics["potential_interest_lost"] == 1
    assert metrics["xp_without_level_up"] == 1
    assert metrics["rerolls_without_immediate_gain"] == 1
    assert metrics["rerolls_followed_by_pass"] == 1
    assert metrics["final_gold"] == 13
    assert metrics["by_action"]["BUY_XP"]["gold_spent"] == 4
    assert "reward" not in metrics


def test_economic_action_audit_flags_unused_level_up_and_ignores_non_actions():
    entries = [
        {
            "event_type": "round_finished", "payload": {"economic_diagnostics": {"action_cost": 99}},
        },
        _economic_entry(1, "BUY_XP", {
            "action_cost": 4, "sale_proceeds": 0, "potential_interest_delta": 0,
            "reason_code": "XP_LEVEL_UP", "level_after": 3, "measurable_improvement": True,
        }, 0),
        _economic_entry(2, "PASS", {
            "action_cost": 0, "sale_proceeds": 0, "potential_interest_delta": 0,
            "reason_code": "PASS_NO_SPEND", "measurable_improvement": False,
        }, 0),
    ]
    entries[1]["payload"]["state_after"]["board"] = [{"occupied": True}]
    entries[2]["payload"]["state_after"]["board"] = [{"occupied": True}]
    report = {}
    audit_economic_actions(entries, "Jogador 2", report)
    metrics = report["economic_action_metrics"]["Jogador 2"]
    assert metrics["xp_level_up_unused"] == 1
    assert metrics["actions"] == 2



def test_player_snapshot_preserves_board_quality_diagnostics():
    writer = PlayerJsonLogWriter.__new__(PlayerJsonLogWriter)
    state = writer._player_snapshot(
        {"positioning_score": 0.2},
        {
            "player_id": 0,
            "board_quality_score": 0.4,
            "board_positional_score": 0.7,
            "board_structural_score": -0.3,
            "board_quality_delta": 0.1,
            "board_exposed_carries": 1,
            "board_frontline_count": 2,
            "board_isolated_frontline_count": 1,
            "board_important_bench_units_unplayed": 2,
        },
    )
    assert state["board_quality_score"] == 0.4
    assert state["board_positional_score"] == 0.7
    assert state["board_structural_score"] == -0.3
    assert state["board_quality_delta"] == 0.1
    assert state["board_exposed_carries"] == 1
    assert state["board_frontline_count"] == 2
    assert state["board_isolated_frontline_count"] == 1
    assert state["board_important_bench_units_unplayed"] == 2



def test_player_snapshot_marks_opgg_composition_source():
    writer = object.__new__(PlayerJsonLogWriter)
    writer._unit_info = lambda unit, slot, location: unit
    audit = {
        "strategy_info": {
            "composition_direction": "Colosso",
            "planned_acquisition_notes": [
                "OPGG_META_CANDIDATE: Colosso flex (score=18.2, native_score=16.9)",
                "OPGG_META_AUDIT: status=selected",
            ],
        },
        "board": [],
        "bench": [],
        "shop": [],
    }
    snapshot = writer._player_snapshot(audit, {"player_id": 0, "level": 6})
    assert snapshot["composition_source"] == "OP.GG"
    assert snapshot["composition_source_name"] == "Colosso flex"

    audit["strategy_info"]["planned_acquisition_notes"] = [
        "OPGG_META_AUDIT: status=candidate_below_native_margin"
    ]
    native_snapshot = writer._player_snapshot(audit, {"player_id": 0, "level": 6})
    assert native_snapshot["composition_source"] == "NATIVE"
    assert native_snapshot["composition_source_name"] == ""
