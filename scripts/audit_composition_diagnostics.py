"""Audit a Composition Intelligence diagnostic JSONL file."""
from __future__ import annotations

import argparse
from pathlib import Path

from viewer.composition_diagnostics import (
    audit_diagnostic_records, format_diagnostic_audit, load_diagnostic_jsonl,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path, help="CompositionDiagnosticRecorder JSONL file")
    parser.add_argument("--output", type=Path, help="Optional report destination")
    args = parser.parse_args()
    records, errors = load_diagnostic_jsonl(args.jsonl)
    report = audit_diagnostic_records(records, errors)
    rendered = format_diagnostic_audit(records, report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return int(bool(errors or report["stale_count"] or report["duplicate_sequences"]
                    or report["out_of_order_sequences"] or report["version_regressions"]))


if __name__ == "__main__":
    raise SystemExit(main())
