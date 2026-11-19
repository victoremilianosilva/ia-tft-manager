"""Pure projections for canonical Shadow diagnostics consumed by the Viewer."""

from __future__ import annotations


def shadow_diagnostics(player_snapshot: dict) -> tuple[dict, dict]:
    shadow = player_snapshot.get("shadow_composition")
    if not isinstance(shadow, dict):
        return {}, {}
    diagnostics = shadow.get("diagnostics")
    return shadow, diagnostics if isinstance(diagnostics, dict) else {}


def shadow_lineup_entries(player_snapshot: dict) -> list[dict]:
    _, diagnostics = shadow_diagnostics(player_snapshot)
    lineup = diagnostics.get("lineup_plan")
    if not isinstance(lineup, dict):
        return []
    entries = lineup.get("selected_board")
    return [entry for entry in entries if isinstance(entry, dict)] if isinstance(entries, list) else []


def shadow_status_text(player_snapshot: dict) -> str:
    shadow, diagnostics = shadow_diagnostics(player_snapshot)
    if shadow.get("status") == "unavailable" or not diagnostics:
        return "Shadow: aguardando diagnóstico"
    decision = diagnostics.get("composition_decision")
    decision = decision if isinstance(decision, dict) else {}
    lineup = diagnostics.get("lineup_plan")
    lineup = lineup if isinstance(lineup, dict) else {}
    action = diagnostics.get("action_recommendation")
    action = action if isinstance(action, dict) else {}
    composition_id = str(shadow.get("composition_id") or "sem composição ativa")
    version = shadow.get("composition_version")
    decision_name = str(decision.get("decision") or "INDEFINIDA")
    lineup_status = str(lineup.get("status") or "indisponível")
    recommended = action.get("recommended_action")
    action_text = f" · ação Shadow {recommended}" if recommended is not None else ""
    stale_text = " · EVIDÊNCIA OBSOLETA" if shadow.get("stale") else ""
    return (
        f"Shadow: {decision_name} · {composition_id} v{version} · "
        f"lineup {lineup_status}{action_text}{stale_text}"
    )
