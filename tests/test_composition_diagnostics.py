import json

from viewer.composition_diagnostics import (
    audit_diagnostic_records, format_diagnostic_audit, load_diagnostic_jsonl,
)


def _record(sequence=1, round_number=3, stale=False, version=2):
    return {
        "schema_version": 1, "sequence": sequence, "round": round_number,
        "composition_id": "comp-a", "composition_version": version, "stale": stale,
        "stale_reason": "version mismatch" if stale else "",
        "diagnostics": {
            "composition_decision": {"decision": "KEEP"},
            "unit_intentions": [{"intent": "KEEP"}, {"intent": "SEEK"}],
            "action_recommendation": {
                "recommended_action": 1,
                "candidates": [
                    {"disposition": "accepted", "selected": True},
                    {"disposition": "rejected", "selected": False},
                ],
            },
            "evidence": {
                "economy": {"metadata": {"quality": 2}},
                "board": {"metadata": {"quality": 3}},
                "items": {"metadata": {"quality": 0}},
            },
            "published_transition": None,
            "recommendation_to_later_outcome": {
                "recommendation_round": 3, "outcome_round": 6,
                "composition_version": 2, "interpretation": "correlation_only_not_causation",
            },
        },
    }


def test_load_jsonl_reports_invalid_lines_and_keeps_valid_records(tmp_path):
    path = tmp_path / "composition.jsonl"
    path.write_text(json.dumps(_record()) + "\nnot-json\n", encoding="utf-8")
    records, errors = load_diagnostic_jsonl(path)
    assert len(records) == 1
    assert len(errors) == 1
    assert "Linha 2" in errors[0]


def test_audit_counts_stale_intentions_candidates_evidence_and_correlations():
    records = [_record(), _record(2, 4, stale=True)]
    report = audit_diagnostic_records(records)
    assert report["record_count"] == 2
    assert report["stale_count"] == 1
    assert report["intent_counts"]["KEEP"] == 2
    assert report["intent_counts"]["SEEK"] == 2
    assert report["candidate_counts"]["accepted"] == 2
    assert report["candidate_counts"]["rejected"] == 2
    assert report["candidate_counts"]["selected"] == 2
    assert report["correlation_count"] == 2


def test_audit_detects_duplicate_and_out_of_order_sequences_and_version_regression():
    records = [_record(3, version=3), _record(3, version=2), _record(2, version=1)]
    report = audit_diagnostic_records(records)
    assert report["duplicate_sequences"] == [3]
    assert report["out_of_order_sequences"] == 1
    assert report["version_regressions"] == 2


def test_report_labels_confidence_and_outcome_as_non_probabilistic_and_correlational():
    report = audit_diagnostic_records([_record()])
    rendered = format_diagnostic_audit([_record()], report)
    assert "não uma probabilidade" in rendered
    assert "não prova de causalidade" in rendered
