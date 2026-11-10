from scripts.strategic_economic_comparison import OutcomeEvaluator, build_shadow_markdown_reports
from viewer.player_logs import PlayerJsonLogWriter


def _decision(action="BUY", recommendation="BUY_UNIT", with_shadow=True):
    shadow = {
        "strategic_decision_name": "ADAPT",
        "strategic_target_direction": "Arcanist",
        "strategic_reason": "reuse owned units",
        "economic_posture_name": "STABILIZE_BOARD",
        "economic_posture_reason": "weak board",
        "economic_posture_confidence": 0.7,
        "economic_survival_pressure": 0.4,
        "economic_board_pressure": 0.8,
        "economic_resource_pressure": 0.2,
        "action_recommendation_name": recommendation,
        "action_recommended_champion_id": 90,
        "action_expected_direct_gold_cost": 3.0,
        "action_expected_lost_interest_cost": 0.5,
        "action_expected_opportunity_cost": 0.25,
        "action_candidate_scores": [
            {"action": "BUY_UNIT", "champion_id": 90, "available": True,
             "direct_gold_cost": 3.0, "lost_interest_cost": 0.5, "opportunity_cost": 0.35,
             "board_component": 0.5, "survival_component": 0.1,
             "streak_component": 0.05, "composition_component": 0.1,
             "upgrade_component": 0.1, "posture_component": 0.05,
             "direct_cost_component": -0.1, "lost_interest_component": -0.05,
             "opportunity_cost_component": -0.02, "total_score": 0.8, "selected": True},
            {"action": "BUY_UNIT", "champion_id": 91, "available": False,
             "direct_gold_cost": 4.0, "lost_interest_cost": 1.0, "opportunity_cost": 0.5,
             "board_component": 0.2, "total_score": 0.1, "selected": False}
        ],
        "action_reason": "high marginal value",
        "action_expected_board_delta": 2.5,
        "action_expected_hp_preservation": 1.0,
        "action_expected_economy_cost": 3.0,
        "action_expected_streak_value": 0.5,
        "action_confidence": 0.8,
    } if with_shadow else {}
    return {
        "player": "1", "round": "2-3", "step": 7, "action_name": action,
        "state_before": {
            "gold": 30, "hp": 70, "level": 6, "xp": 10, "board_power": 20,
            "comp_direction": "Invoker", "strategy_name": "ECON",
            "shadow_planning": shadow,
        },
        "state_after": {
            "gold": 27, "hp": 70, "level": 6, "xp": 10, "board_power": 22,
            "placement": None, "comp_direction": "Invoker",
        },
        "economic_diagnostics": {
            "strategic_snapshot_before": {"combined_pair_count": 1, "board_two_star_or_higher": 2, "board_three_star": 0},
            "strategic_snapshot_after": {"combined_pair_count": 2, "board_two_star_or_higher": 3, "board_three_star": 0},
        },
    }


def test_shadow_reports_compare_ppo_action_with_recommendation():
    reports = build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [_decision()]
    })
    assert "Decisões comparáveis: **1**" in reports["audit_divergencias.md"]
    assert "BUY_UNIT" in reports["audit_acoes.md"]
    assert "Strategic Planner" in reports["audit_estrategia.md"]
    assert "STABILIZE_BOARD" in reports["audit_economia.md"]
    assert "2.000" in reports["audit_resultados.md"]
    assert "Campeão recomendado" in reports["audit_acoes.md"]
    assert "Scores dos candidatos" in reports["audit_acoes.md"]
    assert "3.000" in reports["audit_acoes.md"]
    assert "0.350" in reports["audit_acoes.md"]


def test_divergence_is_reported_without_claiming_bad_decision():
    reports = build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [_decision("PASS", "BUY_UNIT")]
    })
    assert "Divergências: **1**" in reports["audit_divergencias.md"]
    assert "Não prova que uma recomendação era melhor" in reports["audit_divergencias.md"]


def test_legacy_logs_mark_shadow_fields_unavailable():
    reports = build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [_decision(with_shadow=False)]
    })
    assert "Strategic Planner indisponíveis" in reports["audit_estrategia.md"]
    assert "Action Evaluator indisponíveis" in reports["audit_acoes.md"]
    assert "Comparação indisponível" in reports["audit_divergencias.md"]


def test_missing_shadow_values_are_not_treated_as_available():
    legacy = _decision()
    legacy["state_before"]["shadow_planning"] = {"action_recommendation_name": None}
    reports = build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [legacy]
    })
    assert "Comparação indisponível" in reports["audit_divergencias.md"]


def test_outcome_evaluator_correlates_round_end_without_action_attribution():
    decision = _decision()
    result = OutcomeEvaluator().evaluate(
        [decision],
        [{
            "player": "1", "round": "2-3", "sequence_id": 8, "step": 8,
            "state_after": {"gold": 22, "hp": 60, "board_power": 25, "placement": 5},
            "combat_reward": -0.3, "placement": 5,
        }],
    )
    outcome = result["decisions"][0]
    assert outcome["hp_delta"] == 0.0
    assert len(result["round_summaries"]) == 1
    assert result["round_summaries"][0]["combat_reward"] == -0.3
    assert "Resultado de combate (uma linha por jogador e round)" in build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [decision],
        "round_outcome_timeline": [{
            "player": "1", "round": "2-3", "sequence_id": 8, "step": 8,
            "state_after": {"gold": 22, "hp": 60, "board_power": 25, "placement": 5},
            "combat_reward": -0.3, "placement": 5,
        }]
    })["audit_resultados.md"]
    assert result["final_states"][0]["hp"] == 60
    assert result["final_states"][0]["placement"] == 5



def test_outcome_evaluator_deduplicates_round_combat_and_preserves_last_alive_state():
    decisions = [_decision()]
    decisions[0]["round"] = "2-3"
    decisions[0]["state_after"].update({"hp": 54, "round": "2-3", "step": 7})
    outcomes = [
        {"player": "1", "round": "2-3",
         "state_after": {"hp": 50, "gold": 24, "board_power": 24, "round": "2-3"},
         "combat_reward": -0.2, "placement": None, "sequence_id": 10},
        {"player": "1", "round": "2-3",
         "state_after": {"hp": 50, "gold": 24, "board_power": 24, "round": "2-3"},
         "combat_reward": None, "placement": None, "sequence_id": 11},
        {"player": "1", "round": "2-4",
         "state_after": {"hp": 0, "gold": 18, "board_power": 0, "round": "2-4"},
         "combat_reward": -1.0, "placement": 5, "sequence_id": 12},
    ]
    result = OutcomeEvaluator().evaluate(decisions, outcomes)
    assert len(result["round_summaries"]) == 2
    assert result["round_summaries"][0]["combat_reward"] == -0.2
    assert result["final_states"][0]["hp"] == 50
    assert result["final_states"][0]["terminal_hp"] == 0
    assert result["final_states"][0]["placement"] == 5


def test_outcome_evaluator_correlates_recommendations_with_next_one_and_two_rounds():
    first = _decision(recommendation="BUY_UNIT")
    first["round"] = "2-3"
    second = _decision(recommendation="REROLL")
    second["round"] = "2-3"
    outcomes = [
        {"player": "1", "round": "2-3",
         "state_after": {"hp": 70, "gold": 30, "board_power": 20}},
        {"player": "1", "round": "2-4",
         "state_after": {"hp": 62, "gold": 26, "board_power": 23}},
        {"player": "1", "round": "3-1",
         "state_after": {"hp": 58, "gold": 20, "board_power": 25}},
    ]
    result = OutcomeEvaluator().evaluate([first, second], outcomes)
    row = result["recommendation_rounds"][0]
    assert row["recommendations"] == {"BUY_UNIT": 1, "REROLL": 1}
    assert row["next_round_hp_delta"] == -8.0
    assert row["next_round_board_delta"] == 3.0
    assert row["next_two_rounds_hp_delta"] == -12.0
    assert row["next_two_rounds_gold_delta"] == -10.0
    assert len(result["round_summaries"]) == 3
    reports = build_shadow_markdown_reports({
        "players_seen": ["1"],
        "decision_timeline": [first, second],
        "round_outcome_timeline": outcomes,
    })
    assert "Evolução posterior das recomendações" in reports["audit_resultados.md"]
    assert reports["audit_resultados.md"].count("-0.200") <= 1



def test_native_flat_audit_fields_are_persisted_in_shadow_snapshot():
    writer = PlayerJsonLogWriter.__new__(PlayerJsonLogWriter)
    native_audit = {
        "player_id": 0,
        "strategic_action_recommendation_name": "BUY_UNIT",
        "strategic_action_recommended_champion_id": 90,
        "strategic_action_candidate_scores": [
            {"action": "BUY_UNIT", "champion_id": 90, "total_score": 0.8, "selected": True}
        ],
        "strategic_action_expected_direct_gold_cost": 3.0,
        "strategic_action_expected_lost_interest_cost": 0.5,
        "strategic_action_expected_opportunity_cost": 0.25,
        "economic_posture_name": "STABILIZE_BOARD",
    }

    snapshot = writer._player_snapshot(native_audit, {"player_id": 0})
    shadow = snapshot["shadow_planning"]

    assert shadow["action_recommendation_name"] == "BUY_UNIT"
    assert shadow["action_recommended_champion_id"] == 90
    assert shadow["action_candidate_scores"][0]["total_score"] == 0.8
    assert shadow["action_expected_direct_gold_cost"] == 3.0
    assert shadow["action_expected_lost_interest_cost"] == 0.5
    assert shadow["action_expected_opportunity_cost"] == 0.25
    assert shadow["economic_posture_name"] == "STABILIZE_BOARD"


def test_action_audit_exports_every_candidate_and_selection_integrity():
    reports = build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [_decision()]
    })
    actions = reports["audit_acoes.md"]

    assert "Candidatos" in actions
    assert "Disponível" in actions
    assert "BUY_UNIT" in actions
    assert "91" in actions
    assert "False" in actions
    assert "Score custo direto" in actions
    assert "Integridade da seleção" in actions
    assert "Consistente" in actions
    assert "0.500" in actions
    assert "0.350" in actions
    assert "0.250" in actions
    assert len(actions.strip()) > 500


def test_keep_audit_separates_confidence_and_persistence():
    decision = _decision()
    shadow = decision["state_before"]["shadow_planning"]
    shadow.update({
        "strategic_decision_name": "KEEP", "current_direction_confidence": 0.73,
        "anchor_confidence": 0.61, "current_direction_score": 0.82,
        "best_anchor_score": 0.91, "alternative_advantage": 0.09,
        "required_pivot_advantage": 0.75, "current_direction_viable": True,
        "decision_path_reason": "alternative_below_minimum_adapt_advantage",
    })
    decision["state_before"].update({
        "composition_locked": True, "composition_candidate_direction": "Duelist",
        "composition_candidate_streak": 2,
    })
    report = build_shadow_markdown_reports({"players_seen": ["1"], "decision_timeline": [decision]})
    strategy = report["audit_estrategia.md"]
    assert "Auditoria de KEEP" in strategy
    assert "0.730" in strategy and "0.610" in strategy
    assert "alternative_below_minimum_adapt_advantage" in strategy
    assert "Duelist" in strategy and "0.750" in strategy


def test_keep_unit_audit_separates_alignment_from_investment_proxies():
    decision = _decision()
    shadow = decision["state_before"]["shadow_planning"]
    shadow.update({
        "strategic_decision_name": "KEEP", "strategic_preserve_unit_ids": [90, 91],
        "strategic_replaceable_unit_ids": [], "current_direction_confidence": 0.7,
    })
    decision["state_before"].update({
        "comp_direction": "Invoker", "core_units": [90], "core_traits": ["Invoker"],
        "board": [
            {"occupied": True, "champion_id": "90", "name": "Core Mage", "star": 1,
             "traits": ["Invoker"], "items": [], "impact": 8.0},
        ], "bench": [
            {"occupied": True, "champion_id": "91", "name": "Item Holder", "star": 1,
             "traits": ["Bruiser"], "items": ["item_a"], "impact": 4.0},
        ],
    })
    report = build_shadow_markdown_reports({"players_seen": ["1"], "decision_timeline": [decision]})
    strategy = report["audit_estrategia.md"]
    assert "observable_strategic_signals" in strategy
    assert "investment_proxy_without_alignment" in strategy
    assert "core_unit" in strategy and "equipped_items" in strategy


def test_keep_audit_includes_thresholds_and_temporal_followup():
    decision = _decision()
    decision["round"] = "2-3"
    decision["state_before"]["shadow_planning"].update({
        "strategic_decision_name": "KEEP", "current_direction_confidence": 0.8,
        "decision_path_reason": "current_direction_viable_without_alternative",
    })
    outcomes = [
        {"player": "1", "round": "2-3", "state_after": {"hp": 70, "gold": 27, "board_power": 22}},
        {"player": "1", "round": "2-4", "state_after": {"hp": 64, "gold": 30, "board_power": 25}},
        {"player": "1", "round": "3-1", "state_after": {"hp": 60, "gold": 35, "board_power": 27}},
    ]
    report = build_shadow_markdown_reports({
        "players_seen": ["1"], "decision_timeline": [decision], "round_outcome_timeline": outcomes,
    })
    strategy = report["audit_estrategia.md"]
    assert "Vantagem absoluta para mudança | 0.75" in strategy
    assert "Revisões consecutivas bloqueado | 3" in strategy
    assert "Evolução posterior dos KEEP" in strategy
    assert "2-4" in strategy
