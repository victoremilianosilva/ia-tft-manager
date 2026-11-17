"""Read-only REROLL opportunity-cost audit for Viewer Markdown reports."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path


def _read_table(path: Path, prefix: str) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(prefix)), None)
    if start is None:
        raise ValueError(f"Table not found in {path}: {prefix}")
    headers = [cell.strip() for cell in lines[start].strip("|").split("|")]
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        values = [cell.strip() for cell in line.strip("|").split("|")]
        if len(values) == len(headers):
            rows.append(dict(zip(headers, values)))
    return rows


def _number(row: dict[str, str], key: str) -> float | None:
    value = row.get(key, "").strip()
    if not value or value in {"—", "-"}:
        return None
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return None


def _key(row: dict[str, str]) -> tuple[str, str, str]:
    return row.get("Jogador", ""), row.get("Round", ""), row.get("Step", "")


def _review_bucket(candidate: dict[str, str], economy: dict[str, str] | None) -> str:
    """Conservative triage labels; they do not claim that a reroll is optimal."""
    upgrade_signal = (_number(candidate, "Upgrade") or 0.0) > 0.0
    composition_signal = (_number(candidate, "Composição") or 0.0) > 0.0
    survival = _number(economy or {}, "Pressão sobrevivência") or 0.0
    board_pressure = _number(economy or {}, "Pressão board") or 0.0
    posture = (economy or {}).get("Postura", "")
    supportive = (
        posture in {"EMERGENCY_INVESTMENT", "STABILIZE_BOARD"}
        or survival >= 0.65 or board_pressure >= 0.65
    )
    conservative = posture in {
        "ACCUMULATE_RESOURCES", "PRESERVE_WIN_STREAK", "INVEST_EXPERIENCE"
    }
    if (upgrade_signal or composition_signal) and supportive:
        return "plausible_window_review"
    if not upgrade_signal and not composition_signal and conservative and not supportive:
        return "weak_reroll_evidence_review"
    return "inconclusive"


def analyze_reroll_audit(actions_path: Path, economy_path: Path) -> dict:
    candidates = _read_table(actions_path, "| Jogador | Round | Step | Ação | Campeão")
    postures = _read_table(economy_path, "| Jogador | Round | Step | Postura")
    economy_by_key = {_key(row): row for row in postures}
    rerolls = [row for row in candidates if row.get("Ação") == "REROLL"]
    buckets, postures_count = Counter(), Counter()
    rounds = defaultdict(list)
    matched = 0
    for candidate in rerolls:
        economy = economy_by_key.get(_key(candidate))
        matched += economy is not None
        posture = (economy or {}).get("Postura", "NO_ECONOMY_MATCH")
        postures_count[posture] += 1
        bucket = _review_bucket(candidate, economy)
        buckets[bucket] += 1
        rounds[candidate.get("Round", "?")].append({
            "score": _number(candidate, "Total"),
            "opportunity_component": _number(candidate, "Score oportunidade"),
            "bucket": bucket,
        })

    def stats(values):
        values = [value for value in values if value is not None]
        if not values:
            return {"count": 0, "mean": None, "min": None, "max": None}
        return {"count": len(values), "mean": round(sum(values) / len(values), 4),
                "min": min(values), "max": max(values)}

    fields = ("Total", "Oportunidade", "Score oportunidade", "Score custo direto",
              "Score juros", "Board", "Sobrevivência", "Upgrade", "Composição", "Postura")
    return {
        "reroll_candidate_count": len(rerolls),
        "economic_context_matches": matched,
        "economic_context_missing": len(rerolls) - matched,
        "review_buckets": dict(sorted(buckets.items())),
        "economic_postures": dict(sorted(postures_count.items())),
        "score_statistics": {field: stats([_number(row, field) for row in rerolls])
                             for field in fields},
        "rounds": {
            round_id: {
                "count": len(values),
                "mean_score": stats([item["score"] for item in values])["mean"],
                "mean_opportunity_component": stats(
                    [item["opportunity_component"] for item in values])["mean"],
                "review_buckets": dict(sorted(Counter(
                    item["bucket"] for item in values).items())),
            }
            for round_id, values in sorted(rounds.items())
        },
        "limitations": [
            "Review buckets are triage heuristics, not labels of optimal play.",
            "Candidate score components are proxies, not calibrated win-rate or placement predictions.",
            "The audit does not expose shop odds, champion pool availability, or all future shop outcomes.",
            "Missing economic context is not treated as evidence against reroll.",
            "This report does not modify scores, recommendations, PPO actions, or gameplay.",
        ],
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# REROLL opportunity-cost audit", "",
        "> Diagnostic only: no score, recommendation, PPO action, or gameplay behavior is changed.", "",
        f"- REROLL candidates: **{result['reroll_candidate_count']}**",
        f"- Economic context matched: **{result['economic_context_matches']}**",
        f"- Economic context missing: **{result['economic_context_missing']}**", "",
        "## Review triage", "", "| Category | Candidates |", "|---|---:|",
    ]
    lines.extend(f"| {key} | {value} |" for key, value in result["review_buckets"].items())
    lines += ["", "## Economic posture", "", "| Posture | Candidates |", "|---|---:|"]
    lines.extend(f"| {key} | {value} |" for key, value in result["economic_postures"].items())
    lines += ["", "## Score components", "",
              "| Component | N | Mean | Min | Max |", "|---|---:|---:|---:|---:|"]
    for key, value in result["score_statistics"].items():
        lines.append(f"| {key} | {value['count']} | {value['mean']} | {value['min']} | {value['max']} |")
    lines += ["", "## By round", "",
              "| Round | N | Mean score | Mean opportunity penalty | Review triage |",
              "|---|---:|---:|---:|---|"]
    for round_id, value in result["rounds"].items():
        triage = ", ".join(f"{key}: {count}" for key, count in value["review_buckets"].items())
        lines.append(f"| {round_id} | {value['count']} | {value['mean_score']} | "
                     f"{value['mean_opportunity_component']} | {triage} |")
    lines += ["", "## Limitations", ""]
    lines.extend(f"- {item}" for item in result["limitations"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actions_audit", type=Path)
    parser.add_argument("economy_audit", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    for path in (args.actions_audit, args.economy_audit):
        if not path.is_file():
            parser.error(f"Audit file not found: {path}")
    report = render_markdown(analyze_reroll_audit(args.actions_audit, args.economy_audit))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"REROLL audit written to {args.output}")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
