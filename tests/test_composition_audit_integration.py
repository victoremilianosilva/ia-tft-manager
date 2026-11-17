import json
import sys

from scripts import audit_viewer_match


def test_session_audit_generates_composition_reports_in_audit_directory(tmp_path, monkeypatch):
    session = tmp_path / "match-fixture"
    session.mkdir()
    (session / "player_1_log.json").write_text(json.dumps({
        "entries": [{
            "event_type": "action",
            "sequence_id": 1,
            "step": 1,
            "round": "2-1",
            "payload": {
                "action": [6, 0, 0, 0, 0, 0],
                "action_name": "PASS",
                "state_before": {},
                "state_after": {},
            },
        }],
    }), encoding="utf-8")
    diagnostic = {
        "sequence": 1,
        "round": 3,
        "player_id": 0,
        "composition_version": 2,
        "stale": False,
        "diagnostics": {
            "composition_decision": {"decision": "KEEP"},
            "transition_plan": {"to": "comp-a"},
            "unit_intentions": [{
                "champion_id": 44,
                "intent": "SEEK",
                "relation": "MISSING_TARGET",
                "priority": 5,
                "confidence_not_probability": 0.6,
                "reasons": [{"code": 1, "message": "Alvo da composição ainda não possuído."}],
            }],
            "action_recommendation": {"recommended_action": 1, "candidates": []},
        },
    }
    (session / "composition_diagnostics.jsonl").write_text(
        json.dumps(diagnostic) + "\n", encoding="utf-8"
    )

    monkeypatch.setattr(sys, "argv", ["audit_viewer_match.py", str(session)])
    assert audit_viewer_match.main() == 0

    audit_dir = session / "audit"
    composition = (audit_dir / "audit_composition_intelligence.md").read_text(encoding="utf-8")
    comparison = (audit_dir / "audit_composition_vs_ppo.md").read_text(encoding="utf-8")
    assert "Snapshots válidos: **1**" in composition
    assert "Alvo da composição ainda não possuído." in composition
    assert "Recomendações da Composition Intelligence" in comparison
    assert "PASS" in comparison

    integrated = (audit_dir / "audit_integrado.md").read_text(encoding="utf-8")
    assert "Índice integrado de auditoria" in integrated
    assert "Envelopes de composição incompletos: 1" in integrated
    report = json.loads((audit_dir / "audit_report.json").read_text(encoding="utf-8"))
    index = report["integrated_audit_index"]
    assert index["composition_envelope_missing_count"] == 1
    assert index["groups"][0]["ppo_action_count"] == 1
    assert index["groups"][0]["composition_snapshot_count"] == 0
