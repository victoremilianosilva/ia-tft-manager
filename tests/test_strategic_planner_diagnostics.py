from scripts.audit_viewer_match import audit_strategic_planner_diagnostics
from scripts.strategic_economic_comparison import build_shadow_markdown_reports


def test_strategic_planner_audit_groups_insufficient_evidence_reasons():
    entries = [
        {
            "event_type": "action", "round": 3, "step": 12,
            "payload": {"state_after": {
                "comp_direction": "Bruiser",
                "shadow_planning": {
                    "strategic_decision_name": "INSUFFICIENT_EVIDENCE",
                    "decision_path_reason": "alternative_below_minimum_adapt_advantage",
                    "candidate_generation_reason": "candidate_generated",
                    "has_anchor_candidate": True,
                    "current_direction_viable": True,
                    "current_direction_score": 2.0,
                    "best_anchor_score": 2.05,
                    "alternative_advantage": 0.05,
                    "minimum_adapt_advantage": 0.10,
                    "required_pivot_advantage": 0.75,
                    "anchor_confidence": 0.91,
                    "current_direction_confidence": 0.90,
                    "anchors_considered": 3,
                    "candidates_generated": 1,
                    "rejected_missing_champion_definition": 1,
                    "rejected_empty_plan": 1,
                    "rejected_anchor_not_in_plan": 0,
                },
            }},
        },
        {
            "event_type": "action", "round": 3, "step": 13,
            "payload": {"state_after": {
                "comp_direction": "Bruiser",
                "shadow_planning": {
                    "strategic_decision_name": "INSUFFICIENT_EVIDENCE",
                    "decision_path_reason": "no_high_cost_anchor_units_seen",
                    "candidate_generation_reason": "no_high_cost_anchor_units_seen",
                    "has_anchor_candidate": False,
                    "current_direction_viable": False,
                },
            }},
        },
    ]
    report = {}
    audit_strategic_planner_diagnostics(entries, "Jogador 1", report)
    metrics = report["strategic_planner_metrics"]["Jogador 1"]
    assert metrics["records"] == 2
    assert metrics["decision_counts"]["INSUFFICIENT_EVIDENCE"] == 2
    assert metrics["insufficient_with_anchor"] == 1
    assert metrics["insufficient_without_anchor"] == 1
    assert metrics["insufficient_current_viability_counts"] == {
        "viable": 1, "not_viable": 1,
    }
    assert metrics["insufficient_reason_counts"] == {
        "alternative_below_minimum_adapt_advantage": 1,
        "no_high_cost_anchor_units_seen": 1,
    }
    assert metrics["candidate_generation_rejections"]["rejected_missing_champion_definition"] == 1


def test_strategic_markdown_explains_insufficient_evidence():
    decision = {
        "event_type": "action", "player": "Jogador 1", "round": "3-2", "step": 20,
        "state_before": {
            "comp_direction": "Bruiser",
            "shadow_planning": {
                "strategic_decision_name": "INSUFFICIENT_EVIDENCE",
                "decision_path_reason": "alternative_below_minimum_adapt_advantage",
                "candidate_generation_reason": "candidate_generated",
                "current_direction_score": 2.0,
                "best_anchor_score": 2.05,
                "alternative_advantage": 0.05,
                "minimum_adapt_advantage": 0.10,
                "required_pivot_advantage": 0.75,
                "anchor_confidence": 0.91,
                "current_direction_confidence": 0.90,
                "current_direction_viable": True,
                "has_anchor_candidate": True,
                "anchors_considered": 3,
                "candidates_generated": 1,
                "rejected_missing_champion_definition": 1,
                "rejected_empty_plan": 1,
                "rejected_anchor_not_in_plan": 0,
            },
        },
        "state_after": {},
    }
    documents = build_shadow_markdown_reports({
        "decision_timeline": [decision],
        "round_outcome_timeline": [],
        "players_seen": ["1"],
    })
    strategy = documents["audit_estrategia.md"]
    assert "Auditoria de INSUFFICIENT_EVIDENCE" in strategy
    assert "alternative_below_minimum_adapt_advantage" in strategy
    assert "Viável atual" in strategy
    assert "True" in strategy
    assert "Confiança da âncora e confiança da direção atual" in strategy



def test_strategic_markdown_reports_anchor_coverage_per_player_round():
    decisions = [
        {
            "event_type": "action", "player": "Jogador 1", "round": "2-1", "step": 10,
            "state_after": {"shadow_planning": {
                "strategic_decision_name": "INSUFFICIENT_EVIDENCE",
                "candidate_generation_reason": "no_cost_four_or_five_anchor",
                "anchors_considered": 8, "candidates_generated": 0,
                "rejected_cost_below_four": 8,
            }},
        },
        {
            "event_type": "action", "player": "Jogador 1", "round": "2-1", "step": 11,
            "state_after": {"shadow_planning": {
                "strategic_decision_name": "INSUFFICIENT_EVIDENCE",
                "candidate_generation_reason": "no_cost_four_or_five_anchor",
                "anchors_considered": 9, "candidates_generated": 0,
                "rejected_cost_below_four": 9,
            }},
        },
        {
            "event_type": "action", "player": "Jogador 1", "round": "2-2", "step": 20,
            "state_after": {"shadow_planning": {
                "strategic_decision_name": "KEEP",
                "candidate_generation_reason": "candidate_generated",
                "anchors_considered": 5, "candidates_generated": 1,
                "rejected_cost_below_four": 2,
            }},
        },
    ]
    documents = build_shadow_markdown_reports({
        "decision_timeline": decisions,
        "round_outcome_timeline": [],
        "players_seen": ["1"],
    })
    strategy = documents["audit_estrategia.md"]
    assert "Cobertura de âncoras por jogador/round" in strategy
    assert "| Jogador 1 | 2-1 | 2 | 2 | 17 | 0 | 17 | 2 | 0 |" in strategy
    assert "| Jogador 1 | 2-2 | 1 | 0 | 5 | 1 | 2 | 0 | 0 |" in strategy
    assert "revisões independentes" in strategy
    assert "nenhuma direção inicial é inferida" in strategy
