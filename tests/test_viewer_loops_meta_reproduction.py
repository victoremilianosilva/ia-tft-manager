from pathlib import Path

from scripts.audit_viewer_loops_and_meta import audit, parse_log


ROOT = Path(__file__).resolve().parents[1]
SESSION = ROOT / "viewer" / "sessions" / "match-20261028-213933-26547a5c"


def test_committed_viewer_session_reproduces_movement_reversal_candidates():
    report = audit(SESSION)
    assert report["summary"]["player_logs"] == 8
    assert {Path(p).name for p in report["summary"]["empty_logs"]} == {
        "player_2_log.tft", "player_4_log.tft"
    }
    by_name = {Path(p["file"]).name: p for p in report["players"]}
    # These are evidence for later native-state replay, not proof of exact cycles.
    assert by_name["player_1_log.tft"]["movement_count"] > 100
    assert by_name["player_5_log.tft"]["textual_reverse_candidates"]
    assert by_name["player_7_log.tft"]["textual_reverse_candidates"]
    assert any(
        row["classification"] == "nonpositive_reverse_candidate"
        for row in by_name["player_5_log.tft"]["textual_reverse_candidates"]
    )


def test_meta_selected_is_distinct_from_executed_source_and_final_outcome():
    player = parse_log(SESSION / "player_7_log.tft")
    meta = player["meta"]
    assert meta["selection_count"] > 0
    assert meta["selected_names"]
    assert meta["selected_to_execution"]["status"] == "executed_source_observed"
    assert player["final_placement"] == 3
    assert player["purchases"]
    assert player["final_board_units"]
    assert player["synergy_events"]
    # We must not infer actual execution merely from a candidate event.
    empty = parse_log(SESSION / "player_2_log.tft")
    assert empty["meta"]["selection_count"] == 0
    assert empty["meta"]["selected_to_execution"]["status"] == "not_selected"
