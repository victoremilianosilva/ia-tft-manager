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



def test_viewer_diagnostic_sidecar_resets_cursor_for_new_engine_episode(tmp_path):
    class NativeLobby:
        episode_id = 1
        lines = []

        def get_snapshot_metadata(self):
            return {"episode_id": self.episode_id}

        def get_composition_diagnostics_jsonl(self):
            return list(self.lines)

    lobby = NativeLobby()
    session = ViewerSession()
    session.lobby = lobby
    session._session_dir = tmp_path
    session.match_id = "viewer-session"

    lobby.lines = [
        json.dumps({
            "engine_match_id": 1, "player_id": 0, "round": 9,
            "sequence": 1, "composition_id": "episode-one",
            "composition_version": 1,
        })
    ]
    session._persist_composition_diagnostics()
    assert session._composition_diagnostics_written == 1

    lobby.episode_id = 2
    lobby.lines = [
        json.dumps({
            "engine_match_id": 2, "player_id": 0, "round": 9,
            "sequence": 1, "composition_id": "episode-two",
            "composition_version": 1,
        })
    ]
    session._persist_composition_diagnostics()

    records = [
        json.loads(line)
        for line in (tmp_path / "composition_diagnostics.jsonl").read_text().splitlines()
    ]
    assert [record["engine_match_id"] for record in records] == [1, 2]
    assert [record["sequence"] for record in records] == [1, 1]
