from pathlib import Path

from viewer.session import ViewerSession


ROOT = Path(__file__).resolve().parents[1]
LEGACY_SESSION = (
    ROOT / "viewer" / "sessions"
    / "match-20261111-141511-b26d6f2c"
)


def test_historical_session_directory_loads_legacy_tft_timeline_read_only():
    session = ViewerSession()
    try:
        count = session.load_replay(LEGACY_SESSION)
        assert count > 0
        assert session.replay_mode is True
        first = session.replay_event(0)
        assert first["event_type"] == "legacy_text_line"
        assert first["legacy_source_format"] == "tft_text_v1"
        assert first["text"].startswith("=")
        header = session.replay_event(1)
        assert header["text"].startswith("TFT AI LOG")
        assert first["legacy_line_number"] == 1
        # The compatibility reader must not invent structured game facts.
        assert "action" not in first
        assert "state_before" not in first
        assert "state_after" not in first
    finally:
        session.close()


def test_historical_tft_file_can_be_loaded_directly():
    session = ViewerSession()
    try:
        path = LEGACY_SESSION / "player_1_log.tft"
        count = session.load_replay(path)
        assert count > 0
        last = session.replay_event(count - 1)
        assert last["event_type"] == "legacy_text_line"
        assert last["legacy_line_number"] > 1
        assert isinstance(last["text"], str)
    finally:
        session.close()
