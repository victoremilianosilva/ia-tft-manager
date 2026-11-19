import json

from viewer.session import ViewerSession


def test_viewer_refresh_uses_shadow_diagnostics_without_strategyinfo_enrichment():
    class NativeLobby:
        def get_audit_snapshot(self):
            return {"players": [{"player_id": 2, "gold": 30}]}

        def get_composition_diagnostics_jsonl(self):
            return [
                '{"sequence": 4, "round": 9, "player_id": 2, "composition_id": "comp-a", "composition_version": 3}'
            ]

        def get_strategy_snapshots(self):
            raise AssertionError("Viewer must not request legacy StrategyInfo snapshots.")

    session = ViewerSession()
    session.lobby = NativeLobby()
    snapshot = session._refresh_audit_snapshot()
    player = snapshot["players"][0]
    assert "strategy_info" not in player
    assert player["shadow_composition"]["composition_id"] == "comp-a"
    assert player["shadow_composition"]["sequence"] == 4
