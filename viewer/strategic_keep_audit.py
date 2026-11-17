"""Evidence classification for Strategic Planner KEEP reviews.

This module is observational only. It classifies evidence already present in
Viewer snapshots; it never calls or changes a planner, threshold, or policy.
"""
from __future__ import annotations

from typing import Any


SUPPORTED = "KEEP_SUPPORTED_BY_CURRENT_EVIDENCE"
PERSISTENCE = "KEEP_ASSOCIATED_WITH_PERSISTENCE"
INCONCLUSIVE = "KEEP_INCONCLUSIVE"


def _number(value: Any) -> float | None:
    if isinstance(value, bool) or value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _positive(value: Any) -> bool:
    number = _number(value)
    return number is not None and number > 0


def _candidate_diagnostics(shadow: dict[str, Any]) -> list[dict[str, Any]]:
    values = shadow.get("strategic_candidate_diagnostics")
    if not isinstance(values, list):
        return []
    return [item for item in values if isinstance(item, dict)]


def classify_keep_evidence(
    state: dict[str, Any],
    shadow: dict[str, Any],
    unit_evidence: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Classify why a KEEP is observable, preserving unavailable evidence.

    Positive support requires explicit current-direction viability or at least
    one owned unit with an observable strategic alignment signal. Investment
    indicators alone never count as current strategic support.
    """
    state = state if isinstance(state, dict) else {}
    shadow = shadow if isinstance(shadow, dict) else {}
    units = [item for item in (unit_evidence or []) if isinstance(item, dict)]

    # Board presence alone is useful context, but it does not establish that
    # the unit supports the chosen composition direction.
    directional_signals = {"core_unit", "current_direction_or_core_trait"}
    strategically_aligned = [
        item for item in units
        if directional_signals.intersection(item.get("strategic_signals") or [])
    ]
    board_only = [
        item for item in units
        if "currently_contributes_to_board" in (item.get("strategic_signals") or [])
        and not directional_signals.intersection(item.get("strategic_signals") or [])
    ]
    investment_only = [
        item for item in units
        if not directional_signals.intersection(item.get("strategic_signals") or [])
        and bool(item.get("investment_indicators") or [])
    ]

    viable = shadow.get("current_direction_viable")
    current_score = _number(shadow.get("current_direction_score"))
    score_available = current_score is not None
    persistence = {
        "composition_locked": state.get("composition_locked"),
        "composition_candidate_direction": state.get("composition_candidate_direction"),
        "composition_candidate_streak": state.get("composition_candidate_streak"),
        "planner_candidate_direction": shadow.get("strategic_candidate_direction"),
        "planner_candidate_streak": shadow.get("strategic_candidate_streak"),
        "planner_candidate_last_review_round": shadow.get("strategic_candidate_last_review_round"),
        "planner_committed_direction": shadow.get("strategic_committed_direction"),
    }
    lock_active = persistence["composition_locked"] is True
    pending_candidate = bool(
        persistence["composition_candidate_direction"]
        or persistence["planner_candidate_direction"]
    )
    streak_active = (
        _positive(persistence["composition_candidate_streak"])
        or _positive(persistence["planner_candidate_streak"])
    )
    investment_only_evidence = bool(investment_only)
    current_support = viable is True or bool(strategically_aligned)

    if current_support:
        classification = SUPPORTED
        reasons = []
        if viable is True:
            reasons.append("planner_reports_current_direction_viable")
        if strategically_aligned:
            reasons.append("owned_units_have_current_strategic_alignment")
    elif lock_active or (pending_candidate and streak_active) or investment_only_evidence:
        classification = PERSISTENCE
        reasons = []
        if lock_active:
            reasons.append("composition_lock_active")
        if pending_candidate and streak_active:
            reasons.append("pending_candidate_with_observed_streak")
        if investment_only_evidence:
            reasons.append("investment_proxy_without_current_alignment")
    else:
        classification = INCONCLUSIVE
        reasons = ["current_support_or_persistence_evidence_unavailable"]
        if viable is False:
            reasons.append("planner_reports_current_direction_not_viable")
        elif viable is None:
            reasons.append("current_direction_viability_unavailable")
        if not strategically_aligned and not units:
            reasons.append("unit_alignment_evidence_unavailable")

    candidates = _candidate_diagnostics(shadow)
    advantage = _number(shadow.get("alternative_advantage"))
    adapt_threshold = _number(shadow.get("minimum_adapt_advantage"))
    pivot_threshold = _number(shadow.get("required_pivot_advantage"))
    candidate_generated = shadow.get("candidates_generated")
    has_anchor = shadow.get("has_anchor_candidate")
    candidate_reasons = [
        str(item.get("evaluation_reason") or "unavailable")
        for item in candidates
    ]
    candidate_outcomes = {str(item.get("evaluation_reason") or "") for item in candidates}
    candidate_pending = pending_candidate or (
        bool(shadow.get("strategic_candidate_direction"))
        and _positive(shadow.get("strategic_candidate_streak"))
    )

    if candidates and candidate_outcomes and candidate_outcomes <= {
        "not_best_scoring_candidate", "valid_but_not_selected"
    }:
        alternative_status = "ALTERNATIVE_REJECTED_BY_STRATEGIC_SCORE"
    elif advantage is not None and adapt_threshold is not None and advantage < adapt_threshold:
        alternative_status = "ALTERNATIVE_BELOW_ADAPT_THRESHOLD"
    elif advantage is not None and pivot_threshold is not None and advantage < pivot_threshold:
        alternative_status = "ALTERNATIVE_BELOW_PIVOT_THRESHOLD"
    elif candidate_pending and lock_active:
        alternative_status = "ALTERNATIVE_BLOCKED_OR_HELD_BY_PERSISTENCE"
    elif candidates:
        alternative_status = "ALTERNATIVE_EVALUATED_OUTCOME_UNCLEAR"
    elif candidate_generated == 0 or has_anchor is False:
        alternative_status = "NO_ALTERNATIVE_GENERATED"
    else:
        alternative_status = "ALTERNATIVE_EVIDENCE_UNAVAILABLE"

    return {
        "classification": classification,
        "classification_reasons": reasons,
        "current_direction_viable": viable,
        "current_direction_score": current_score,
        "current_direction_score_available": score_available,
        "strategically_aligned_unit_count": len(strategically_aligned),
        "investment_only_unit_count": len(investment_only),
        "board_contribution_only_unit_count": len(board_only),
        "strategic_unit_evidence": strategically_aligned,
        "board_contribution_only_evidence": board_only,
        "investment_only_unit_evidence": investment_only,
        "persistence": persistence,
        "alternative_status": alternative_status,
        "alternative_advantage": advantage,
        "minimum_adapt_advantage": adapt_threshold,
        "required_pivot_advantage": pivot_threshold,
        "alternative_candidate_count": len(candidates),
        "alternative_candidate_reasons": candidate_reasons,
        "interpretation": (
            "Classificação diagnóstica baseada somente em campos observados. "
            "Investimento passado, lock ou ausência de alternativa não provam erro; "
            "ausência de evidência não é suporte positivo."
        ),
    }


def aggregate_keep_evidence(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate one already-deduplicated KEEP review per record."""
    counts: dict[str, int] = {}
    alternative_counts: dict[str, int] = {}
    by_player_round: dict[tuple[str, str], dict[str, int]] = {}
    samples = []
    for record in records:
        classification = str(record.get("classification") or INCONCLUSIVE)
        alternative = str(record.get("alternative_status") or "ALTERNATIVE_EVIDENCE_UNAVAILABLE")
        counts[classification] = counts.get(classification, 0) + 1
        alternative_counts[alternative] = alternative_counts.get(alternative, 0) + 1
        key = (str(record.get("player", "?")), str(record.get("round", "?")))
        bucket = by_player_round.setdefault(key, {})
        bucket[classification] = bucket.get(classification, 0) + 1
        samples.append(record)
    return {
        "review_count": len(records),
        "classification_counts": dict(sorted(counts.items())),
        "alternative_status_counts": dict(sorted(alternative_counts.items())),
        "by_player_round": [
            {"player": player, "round": round_id, **dict(sorted(counts.items()))}
            for (player, round_id), counts in sorted(by_player_round.items())
        ],
        "samples": samples,
    }
