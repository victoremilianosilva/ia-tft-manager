from scripts.strategic_audit_state import state_signature
from scripts.validate_strategic_cycles import validate


def unit(uuid, champion="TFT_Nasus", star=1):
    return {"occupied": True, "uuid": uuid, "champion_id": champion, "star": star}


def snap(board=None, bench=None):
    return {"board": board or [{"occupied": False}],
            "bench": bench or [{"occupied": False}]}


def row(seed, step, before, after, action=None):
    action = action or [3, 0, 0, 0, 0, 0]
    return {
        "seed": seed, "step": step, "player_id": 0, "action": action,
        "action_effect_observed": True,
        "board_before": before["board"], "bench_before": before["bench"],
        "board_after": after["board"], "bench_after": after["bench"],
        "board_bench_signature_before": state_signature(before),
        "board_bench_signature_after": state_signature(after),
        "unit_changes": {"moved_units": []},
    }


def test_validator_confirms_return_cycle_using_snapshot_signatures():
    on_board = snap(board=[unit("u-1")])
    on_bench = snap(bench=[unit("u-1")])
    records = [
        row(20261022, 0, on_board, on_bench),
        row(20261022, 1, on_bench, on_board),
    ]
    result = validate(records, [20261022])
    assert result["signature_mismatches"] == []
    assert result["identity_conflicts"] == []
    assert len(result["confirmed_cycles"]) == 1
    assert result["confirmed_cycles"][0]["previous_step"] == -1
    assert result["confirmed_cycles"][0]["step"] == 1


def test_validator_flags_stored_signature_drift():
    state = snap(board=[unit("u-1")])
    record = row(20261022, 0, state, state, action=[6, 0, 0, 0, 0, 0])
    record["board_bench_signature_after"] = "stale-signature"
    result = validate([record], [20261022])
    assert any(item["side"] == "after" for item in result["signature_mismatches"])


def test_validator_requires_both_planned_seeds():
    state = snap(board=[unit("u-1")])
    result = validate([row(20261022, 0, state, state, action=[6, 0, 0, 0, 0, 0])],
                      [20261022, 20261023])
    assert result["observed_seeds"] == [20261022]
    assert result["missing_seeds"] == [20261023]


def test_validator_flags_uuid_reused_for_different_champion():
    before = snap(board=[unit("same-id", "TFT_Nasus")])
    after = snap(board=[unit("same-id", "TFT_Briar")])
    result = validate([row(20261022, 0, before, after)], [20261022])
    assert result["identity_conflicts"]
