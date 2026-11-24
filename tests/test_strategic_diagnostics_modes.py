"""Integration checks for separating strategic context from optional diagnostics."""

from cpp_lobby_env import CppTFTLobbyWrapper


def _run_mode(monkeypatch, mode):
    monkeypatch.setenv("TFT_COMPOSITION_INTELLIGENCE_ENABLED", "1")
    monkeypatch.setenv("TFT_COMPOSITION_DIAGNOSTICS_MODE", mode)
    lobby = CppTFTLobbyWrapper(seed=542031)
    try:
        lobby.reset(seed=542031)
        snapshots = []
        for _ in range(4):
            actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
            _, _, _, info = lobby.step(actions)
            snapshots.append(info["decision_snapshot"]["native_state_snapshot"])
        diagnostics = lobby.get_composition_diagnostics_jsonl()
        return snapshots, diagnostics
    finally:
        lobby.close()


def test_normal_and_audit_modes_preserve_identical_semantic_strategic_context(monkeypatch):
    normal_snapshots, normal_diagnostics = _run_mode(monkeypatch, "off")
    audit_snapshots, audit_diagnostics = _run_mode(monkeypatch, "audit")

    assert normal_diagnostics == []
    assert audit_diagnostics, "Audit mode must retain detailed diagnostic snapshots."
    assert len(normal_snapshots) == len(audit_snapshots)

    for normal, audit in zip(normal_snapshots, audit_snapshots):
        assert normal["episode_id"] == audit["episode_id"]
        assert normal["snapshot_sequence"] == audit["snapshot_sequence"]
        assert len(normal["players"]) == len(audit["players"]) == 8
        for normal_player, audit_player in zip(normal["players"], audit["players"]):
            normal_strategic = normal_player["strategic_state"]
            audit_strategic = audit_player["strategic_state"]
            assert normal_strategic == audit_strategic
            assert normal_strategic["opportunity_costs"] == audit_strategic["opportunity_costs"]


def test_diagnostic_mode_is_independent_from_composition_intelligence_flag():
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    source = (root / "cpp" / "src" / "lobby" / "TftEngine.cpp").read_text(encoding="utf-8")

    assert 'std::string("off")' in source
    assert 'composition_diagnostics_mode == "audit"' in source
    assert 'composition_diagnostics_mode == "debug"' in source
    contextual = source.index("ci::ContextualActionEvaluator{}.evaluate(")
    opportunity_costs = source.index("strategic_opportunity_costs[i].clear();", contextual)
    diagnostic_gate = source.index("if (composition_diagnostics_enabled) {", opportunity_costs)
    assert contextual < opportunity_costs < diagnostic_gate
    assert "ci::CompositionActionEvaluator{}.evaluate(" in source
    assert "if (composition_diagnostics_enabled) {" in source
