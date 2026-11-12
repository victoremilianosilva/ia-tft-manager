from __future__ import annotations

from scripts.strategic_economic_comparison import build_shadow_markdown_reports
from viewer.strategic_keep_audit import (
    INCONCLUSIVE,
    PERSISTENCE,
    SUPPORTED,
    aggregate_keep_evidence,
    classify_keep_evidence,
)


def test_keep_is_supported_by_explicit_current_viability_and_aligned_owned_unit():
    state = {
        "comp_direction": "Arcanist",
        "board": [{
            "occupied": True, "champion_id": "Ahri", "name": "Ahri",
            "star": 1, "traits": ["Arcanist"], "items": [],
        }],
        "bench": [],
        "composition_locked": True,
    }
    shadow = {
        "current_direction_viable": True,
        "current_direction_score": 0.8,
        "strategic_preserve_unit_ids": ["Ahri"],
        "strategic_candidate_diagnostics": [],
    }

    result = classify_keep_evidence(state, shadow, [{
        "strategic_signals": ["current_direction_or_core_trait"],
        "investment_indicators": [],
    }])

    assert result["classification"] == SUPPORTED
    assert "planner_reports_current_direction_viable" in result["classification_reasons"]
    assert result["strategically_aligned_unit_count"] == 1


def test_keep_is_persistence_associated_when_only_investment_and_lock_are_observed():
    state = {
        "comp_direction": "Arcanist",
        "composition_locked": True,
        "composition_candidate_direction": "Bruiser",
        "composition_candidate_streak": 1,
    }
    shadow = {
        "current_direction_viable": False,
        "strategic_candidate_direction": "Bruiser",
        "strategic_candidate_streak": 1,
    }

    result = classify_keep_evidence(state, shadow, [{
        "strategic_signals": [],
        "investment_indicators": ["upgraded_unit", "equipped_items"],
    }])

    assert result["classification"] == PERSISTENCE
    assert "composition_lock_active" in result["classification_reasons"]
    assert "investment_proxy_without_current_alignment" in result["classification_reasons"]
    assert result["investment_only_unit_count"] == 1


def test_board_presence_without_directional_alignment_is_not_positive_keep_support():
    result = classify_keep_evidence(
        {"comp_direction": "Arcanist"},
        {"current_direction_viable": None},
        [{
            "strategic_signals": ["currently_contributes_to_board"],
            "investment_indicators": [],
        }],
    )

    assert result["classification"] == INCONCLUSIVE
    assert result["strategically_aligned_unit_count"] == 0
    assert result["board_contribution_only_unit_count"] == 1


def test_keep_is_inconclusive_when_current_support_and_persistence_are_unavailable():
    result = classify_keep_evidence(
        {"comp_direction": "Arcanist"},
        {"current_direction_viable": None},
        [],
    )

    assert result["classification"] == INCONCLUSIVE
    assert "current_direction_viability_unavailable" in result["classification_reasons"]


def test_keep_alternative_audit_distinguishes_score_rejection_and_threshold():
    rejected = classify_keep_evidence({}, {
        "strategic_candidate_diagnostics": [
            {"evaluation_reason": "not_best_scoring_candidate"},
            {"evaluation_reason": "valid_but_not_selected"},
        ],
    })
    below_threshold = classify_keep_evidence({}, {
        "has_anchor_candidate": True,
        "alternative_advantage": 0.05,
        "minimum_adapt_advantage": 0.10,
        "required_pivot_advantage": 0.75,
    })

    assert rejected["alternative_status"] == "ALTERNATIVE_REJECTED_BY_STRATEGIC_SCORE"
    assert below_threshold["alternative_status"] == "ALTERNATIVE_BELOW_ADAPT_THRESHOLD"


def test_keep_aggregation_groups_unique_reviews_by_player_and_round():
    report = aggregate_keep_evidence([
        {"player": "Jogador 1", "round": "3-2", "classification": SUPPORTED,
         "alternative_status": "ALTERNATIVE_REJECTED_BY_STRATEGIC_SCORE"},
        {"player": "Jogador 1", "round": "3-2", "classification": PERSISTENCE,
         "alternative_status": "ALTERNATIVE_BELOW_ADAPT_THRESHOLD"},
        {"player": "Jogador 2", "round": "4-1", "classification": INCONCLUSIVE,
         "alternative_status": "NO_ALTERNATIVE_GENERATED"},
    ])

    assert report["review_count"] == 3
    assert report["classification_counts"] == {
        INCONCLUSIVE: 1, PERSISTENCE: 1, SUPPORTED: 1,
    }
    assert report["by_player_round"][0] == {
        "player": "Jogador 1", "round": "3-2",
        PERSISTENCE: 1, SUPPORTED: 1,
    }


def test_strategy_report_exposes_keep_classification_without_changing_decision():
    decision = {
        "event_type": "action",
        "player": "Jogador 1",
        "round": "3-2",
        "step": 20,
        "state_before": {
            "comp_direction": "Arcanist",
            "composition_locked": False,
            "board": [{
                "occupied": True, "champion_id": "Ahri", "name": "Ahri",
                "star": 1, "traits": ["Arcanist"], "items": [],
            }],
            "bench": [],
            "shadow_planning": {
                "strategic_decision_name": "KEEP",
                "current_direction_viable": True,
                "current_direction_score": 0.8,
                "strategic_preserve_unit_ids": ["Ahri"],
            },
        },
        "state_after": {},
    }

    strategy = build_shadow_markdown_reports({
        "decision_timeline": [decision],
        "round_outcome_timeline": [],
        "players_seen": ["1"],
    })["audit_estrategia.md"]

    assert "KEEP fundamentado por evidência atual: **1**" in strategy
    assert "KEEP associado principalmente à persistência/investimento: **0**" in strategy
    assert "KEEP inconclusivo por falta de evidência: **0**" in strategy
    assert "KEEP_SUPPORTED_BY_CURRENT_EVIDENCE" in strategy
    assert "A ausência de alternativa gerada nunca é contada como evidência positiva" in strategy
