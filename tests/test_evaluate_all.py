import json

from scripts.evaluate_all import read_json, read_jsonl


def test_read_jsonl_returns_valid_rows_and_counts_malformed_lines(tmp_path):
    path = tmp_path / "audit.jsonl"
    path.write_text(
        '{"seed": 1, "action": [0, 1]}\nnot-json\n[1, 2]\n{"seed": 2}\n',
        encoding="utf-8",
    )

    rows, errors = read_jsonl(path)

    assert rows == [{"seed": 1, "action": [0, 1]}, {"seed": 2}]
    assert errors == 2


def test_read_jsonl_missing_file_is_empty_without_errors(tmp_path):
    rows, errors = read_jsonl(tmp_path / "missing.jsonl")

    assert rows == []
    assert errors == 0


def test_read_json_accepts_only_json_objects(tmp_path):
    path = tmp_path / "summary.json"
    path.write_text(json.dumps({"ok": True}), encoding="utf-8")

    assert read_json(path) == {"ok": True}

    path.write_text("[1, 2]", encoding="utf-8")
    assert read_json(path) is None


def test_read_json_returns_none_for_missing_or_invalid_file(tmp_path):
    path = tmp_path / "broken.json"
    assert read_json(path) is None

    path.write_text("{invalid", encoding="utf-8")
    assert read_json(path) is None
