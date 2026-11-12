from __future__ import annotations

import json

from viewer.strategic_direction_pivot_audit import (
    audit_direction_pivot_records,
    format_direction_pivot_audit,
    load_direction_pivot_jsonl,
)


def _record(phase="PIVOT_EVALUATION", sequence=1):
    return {
        "schema_version": 1,
        "sequence": sequence,
        "player_id": 2,
        "round": "4-2",
        "phase": phase,
        "active_composition": {"identity": "comp-current", "version": 4},
        "direction_anchor": {
            "identity": "direction-current-v4",
            "composition_identity": "comp-current",
            "composition_version": 4,
            "unit_ids": [10, 20],
        },
        "pivot_candidate": {
            "identity": "pivot-next",
            "target_composition_identity": "comp-next",
            "source_direction_anchor_identity": "direction-current-v4",
            "source_composition_version": 4,
        },
        "unit_support": [
            {"champion_id": 10, "relation": "ACTIVE_CORE", "copies_owned": 2,
             "highest_star": 1, "target_star": 2},
            {"champion_id": 20, "relation": "TRAIT_COMPLETION", "copies_owned": 1,
             "highest_star": 1, "target_star": 2},
            {"champion_id": 30, "relation": "TEMPORARY_SUPPORT", "copies_owned": 1,
             "highest_star": 1, "target_star": 2},
        ],
        "shop_evidence": [{"champion_id": 20, "cost": 3, "copies": 1}],
        "carry_gate": {"eligible": True, "champion_id": 10, "cost": 2,
                       "star": 2, "reason": "carry_already_two_star"},
        "feasibility": {"status": "VIABLE", "reason": "required_evidence_present",
                        "blockers": [], "missing_data": []},
    }


def test_pivot_evaluation_preserves_current_anchor_and_counts_evidence():
    record = _record()
    report = audit_direction_pivot_records([record])
    assert report["phase_counts"] == {"PIVOT_EVALUATION": 1}
    assert report["pivot_status_counts"] == {"VIABLE": 1}
    assert report["carry_gate_counts"] == {"eligible": 1}
    assert report["players"]["2"]["support_units"] == {
        "ACTIVE_CORE": 1, "TRAIT_COMPLETION": 1, "TEMPORARY_SUPPORT": 1
    }
    assert report["conflict_count"] == 0


def test_confirmed_pivot_requires_composition_direction_identity_and_version_sync():
    record = _record("PIVOT_CONFIRMED")
    record["active_composition"] = {"identity": "comp-next", "version": 5}
    record["direction_anchor"] = {
        "identity": "direction-next-v5",
        "composition_identity": "comp-next",
        "composition_version": 5,
    }
    record["transition"] = {
        "from_composition_identity": "comp-current",
        "to_composition_identity": "comp-next",
        "previous_version": 4,
        "new_version": 5,
    }
    record["pivot_candidate"] = None
    report = audit_direction_pivot_records([record])
    assert report["conflict_count"] == 0
    assert report["confirmed_transitions"] == [{
        "player_id": "2", "round": "4-2", "from": "comp-current",
        "to": "comp-next", "previous_version": 4, "new_version": 5,
        "direction_anchor": "direction-next-v5",
    }]


def test_confirmed_pivot_flags_unsynchronized_anchor_and_retained_candidate():
    record = _record("PIVOT_CONFIRMED")
    record["active_composition"] = {"identity": "comp-next", "version": 5}
    record["direction_anchor"] = {
        "identity": "direction-old-v4",
        "composition_identity": "comp-current",
        "composition_version": 4,
    }
    report = audit_direction_pivot_records([record])
    codes = {item["code"] for item in report["conflicts"]}
    assert "CONFIRMED_PIVOT_DIRECTION_NOT_SYNCHRONIZED" in codes
    assert "CONFIRMED_PIVOT_VERSION_NOT_SYNCHRONIZED" in codes
    assert "CONFIRMED_PIVOT_TARGET_MISMATCH" in codes
    assert "PIVOT_CANDIDATE_RETAINED_AFTER_CONFIRMATION" in codes


def test_stale_pivot_source_is_detected_during_evaluation():
    record = _record()
    record["pivot_candidate"]["source_composition_version"] = 3
    record["pivot_candidate"]["source_direction_anchor_identity"] = "old-anchor"
    report = audit_direction_pivot_records([record])
    codes = {item["code"] for item in report["conflicts"]}
    assert "PIVOT_SOURCE_ANCHOR_MISMATCH" in codes
    assert "PIVOT_SOURCE_VERSION_MISMATCH" in codes


def test_missing_data_is_not_counted_as_strategic_rejection():
    record = _record()
    record.pop("shop_evidence")
    record.pop("carry_gate")
    record.pop("unit_support")
    report = audit_direction_pivot_records([record])
    assert report["data_status"] == "AVAILABLE"
    assert report["carry_gate_counts"] == {"unavailable": 1}
    assert report["missing_data_counts"]["carry_gate"] == 1
    assert report["missing_data_counts"]["shop_evidence"] == 1
    assert report["missing_data_counts"]["unit_support"] == 1
    assert report["pivot_status_counts"] == {"VIABLE": 1}


def test_loader_reports_invalid_lines_without_dropping_valid_records(tmp_path):
    path = tmp_path / "strategic_direction_pivot.jsonl"
    path.write_text(
        json.dumps(_record()) + "\nnot-json\n" +
        json.dumps({"phase": "EXPLORATION", "player_id": 0}) + "\n",
        encoding="utf-8",
    )
    records, errors = load_direction_pivot_jsonl(path)
    assert len(records) == 2
    assert len(errors) == 1
    assert "Linha 2" in errors[0]


def test_empty_stream_report_explicitly_marks_instrumentation_gap():
    report = audit_direction_pivot_records([], ["sidecar ausente"])
    rendered = format_direction_pivot_audit(report, source_found=False)
    assert report["data_status"] == "NO_STRATEGIC_CYCLE_RECORDS"
    assert "Não há eventos da máquina unificada" in rendered
    assert "indisponibilidade de dados" in rendered
