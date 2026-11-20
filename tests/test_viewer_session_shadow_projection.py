import json

from viewer.session import ViewerSession


def test_viewer_refresh_uses_shadow_diagnostics_without_strategyinfo_enrichment():
    class NativeLobby:
        def get_audit_snapshot(self):
            return {"players": [{"player_id": 2, "gold": 30}]}

        def get_snapshot_metadata(self):
            return {"episode_id": 77}

        def get_composition_diagnostics_jsonl(self):
            return [
                '{"engine_match_id": 77, "sequence": 4, "round": 9, "player_id": 2, "composition_id": "comp-a", "composition_version": 3}'
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



def test_viewer_close_resets_diagnostic_cursor_for_new_engine_with_same_episode_id(tmp_path):
    class NativeLobby:
        def __init__(self, composition_id):
            self.lines = [json.dumps({
                "engine_match_id": 1, "player_id": 0, "round": 9,
                "sequence": 1, "composition_id": composition_id,
                "composition_version": 1,
            })]

        def get_snapshot_metadata(self):
            return {"episode_id": 1}

        def get_composition_diagnostics_jsonl(self):
            return list(self.lines)

        def close(self):
            pass

    session = ViewerSession()
    old_dir = tmp_path / "old"
    old_dir.mkdir()
    session.lobby = NativeLobby("old-engine")
    session._session_dir = old_dir
    session.match_id = "old-session"
    session._persist_composition_diagnostics()
    assert session._composition_diagnostics_written == 1

    session.close()
    assert session._composition_diagnostics_written == 0
    assert session._composition_diagnostics_episode_id is None

    new_dir = tmp_path / "new"
    new_dir.mkdir()
    session.lobby = NativeLobby("new-engine")
    session._session_dir = new_dir
    session.match_id = "new-session"
    session._persist_composition_diagnostics()

    records = [
        json.loads(line)
        for line in (new_dir / "composition_diagnostics.jsonl").read_text().splitlines()
    ]
    assert len(records) == 1
    assert records[0]["composition_id"] == "new-engine"


def test_viewer_shadow_projection_rejects_unmatched_episode_and_boolean_identity_fields():
    class NativeLobby:
        def get_audit_snapshot(self):
            return {"players": [{"player_id": 0, "gold": 12}]}

        def get_snapshot_metadata(self):
            return {"episode_id": 12}

        def get_composition_diagnostics_jsonl(self):
            return [
                json.dumps({"engine_match_id": 11, "player_id": 0, "round": 2, "sequence": 8, "composition_id": "stale"}),
                json.dumps({"engine_match_id": 12, "player_id": True, "round": 2, "sequence": 9, "composition_id": "bool-player"}),
                json.dumps({"engine_match_id": 12, "player_id": 0, "round": 2, "sequence": True, "composition_id": "bool-sequence"}),
            ]

    session = ViewerSession()
    session.lobby = NativeLobby()
    snapshot = session._refresh_audit_snapshot()
    assert snapshot["players"][0]["shadow_composition"] == {
        "status": "unavailable",
        "reason": "no_shadow_snapshot_for_player_in_current_episode",
    }


def test_viewer_shadow_projection_requires_native_episode_identity():
    class NativeLobby:
        def get_audit_snapshot(self):
            return {"players": [{"player_id": 0, "gold": 12}]}

        def get_composition_diagnostics_jsonl(self):
            return [
                json.dumps({"engine_match_id": 12, "player_id": 0, "round": 2, "sequence": 9, "composition_id": "unscoped"})
            ]

    session = ViewerSession()
    session.lobby = NativeLobby()
    snapshot = session._refresh_audit_snapshot()
    assert snapshot["players"][0]["shadow_composition"]["status"] == "unavailable"


def _shadow_record(*, round_number=9, source_sequence=12, composition_id="comp-a", version=3):
    return {
        "engine_match_id": 77,
        "player_id": 2,
        "round": round_number,
        "sequence": 5,
        "composition_id": composition_id,
        "composition_version": version,
        "diagnostics": {
            "composition_decision": {"decision": "KEEP"},
            "lineup_plan": {
                "status": "ready",
                "selected_board": [{"champion_id": 101, "owned": True}],
            },
        },
        "action_evaluator_comparison": {
            "native_action_resolution": {
                "identity": {"source_sequence": source_sequence},
            },
        },
    }


def _native_snapshot(*, round_number=9, player_sequence=12, composition_id="comp-a", version=3):
    return {
        "round": round_number,
        "players": [{
            "player_id": 2,
            "strategic_state": {
                "episode_id": 77,
                "player_decision_sequence": player_sequence,
                "round": round_number,
                "active_composition_valid": True,
                "active_composition_id": composition_id,
                "active_composition_version": version,
            },
        }],
    }


def test_viewer_rejects_same_round_diagnostic_from_an_older_player_sequence():
    class NativeLobby:
        def get_audit_snapshot(self):
            return _native_snapshot(player_sequence=12)

        def get_snapshot_metadata(self):
            return {"episode_id": 77}

        def get_composition_diagnostics_jsonl(self):
            return [json.dumps(_shadow_record(source_sequence=11))]

    session = ViewerSession()
    session.lobby = NativeLobby()
    player = session._refresh_audit_snapshot()["players"][0]
    shadow = player["shadow_composition"]

    assert shadow["stale"] is True
    assert shadow["stale_reason"] == "diagnostic_sequence_does_not_match_current_native_player_state"
    assert "EVIDÊNCIA OBSOLETA" in __import__("viewer.shadow_projection", fromlist=["shadow_status_text"]).shadow_status_text(player)
    assert __import__("viewer.shadow_projection", fromlist=["shadow_lineup_entries"]).shadow_lineup_entries(player) == []


def test_viewer_rejects_diagnostic_from_a_previous_round_or_composition_version():
    class NativeLobby:
        def get_audit_snapshot(self):
            return _native_snapshot(round_number=10, player_sequence=13, version=4)

        def get_snapshot_metadata(self):
            return {"episode_id": 77}

        def get_composition_diagnostics_jsonl(self):
            return [json.dumps(_shadow_record(round_number=9, source_sequence=12, version=3))]

    session = ViewerSession()
    session.lobby = NativeLobby()
    shadow = session._refresh_audit_snapshot()["players"][0]["shadow_composition"]

    assert shadow["stale"] is True
    assert shadow["stale_reason"] == "diagnostic_round_does_not_match_current_native_snapshot"


def test_viewer_accepts_diagnostic_only_when_round_sequence_and_composition_match():
    class NativeLobby:
        def get_audit_snapshot(self):
            return _native_snapshot()

        def get_snapshot_metadata(self):
            return {"episode_id": 77}

        def get_composition_diagnostics_jsonl(self):
            return [json.dumps(_shadow_record())]

    session = ViewerSession()
    session.lobby = NativeLobby()
    player = session._refresh_audit_snapshot()["players"][0]

    assert player["shadow_composition"]["stale"] is not True
    assert player["shadow_composition"]["composition_version"] == 3


def test_persisted_diagnostic_identity_requires_engine_episode_id(tmp_path):
    class NativeLobby:
        def get_snapshot_metadata(self):
            return {"episode_id": 77}

        def get_composition_diagnostics_jsonl(self):
            return [json.dumps({
                "player_id": 0, "round": 2, "sequence": 1,
                "composition_id": "comp-a", "composition_version": 1,
            })]

    session = ViewerSession()
    session.lobby = NativeLobby()
    session._session_dir = tmp_path
    session.match_id = "viewer-session"
    session._persist_composition_diagnostics()

    record = json.loads((tmp_path / "composition_diagnostics.jsonl").read_text().strip())
    assert record["correlation"]["identity_complete"] is False
