"""Read-only HOLD baseline audit for Action Evaluator Markdown exports."""
from __future__ import annotations

import argparse
import statistics
from collections import Counter, defaultdict
from pathlib import Path

DECISION_HEADER = "| Jogador | Round | Step | PPO executou | Recomendação |"
CANDIDATE_HEADER = "| Jogador | Round | Step | Ação | Campeão | Disponível |"
ECONOMY_HEADER = "| Jogador | Round | Step | Postura |"


def read_table(path: Path, prefix: str) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(prefix)), None)
    if start is None:
        return []
    headers = [cell.strip() for cell in lines[start].strip("|").split("|")]
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        values = [cell.strip() for cell in line.strip("|").split("|")]
        if len(values) == len(headers):
            rows.append(dict(zip(headers, values)))
    return rows


def number(row: dict[str, str], key: str) -> float | None:
    value = row.get(key, "").strip()
    if not value or value in {"—", "-"}:
        return None
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return None


def key(row: dict[str, str]) -> tuple[str, str, str]:
    return row.get("Jogador", ""), row.get("Round", ""), row.get("Step", "")


def summarize(values: list[float]) -> dict:
    if not values:
        return {"count": 0, "mean": None, "min": None, "max": None, "distinct": 0}
    return {
        "count": len(values), "mean": round(statistics.mean(values), 4),
        "min": min(values), "max": max(values), "distinct": len(set(values)),
    }


def analyze_hold_audit(actions_path: Path, economy_path: Path | None = None) -> dict:
    candidates = read_table(actions_path, CANDIDATE_HEADER)
    decisions = read_table(actions_path, DECISION_HEADER)
    holds = [row for row in candidates if row.get("Ação") == "HOLD"]
    by_decision: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in candidates:
        by_decision[key(row)].append(row)

    economy = {}
    if economy_path:
        economy = {key(row): row for row in read_table(economy_path, ECONOMY_HEADER)}

    selected = [row for row in holds if row.get("Selecionado", "").lower() == "true"]
    totals = [value for row in holds if (value := number(row, "Total")) is not None]
    component_names = (
        "Score custo direto", "Score juros", "Score oportunidade",
        "Board", "Sobrevivência", "Streak", "Composição", "Upgrade", "Postura",
    )
    components = {
        field: summarize([v for row in holds if (v := number(row, field)) is not None])
        for field in component_names
    }
    posture_counts = Counter()
    by_posture = defaultdict(list)
    comparison = Counter()
    margins = []
    enriched = []
    for row in holds:
        posture = economy.get(key(row), {}).get("Postura", "CONTEXTO_AUSENTE")
        posture_counts[posture] += 1
        total = number(row, "Total")
        alternatives = [
            value for other in by_decision[key(row)]
            if other.get("Ação") != "HOLD"
            and (value := number(other, "Total")) is not None
            and other.get("Disponível", "").lower() == "true"
        ]
        best_alt = max(alternatives) if alternatives else None
        if total is not None:
            by_posture[posture].append(total)
        if total is None:
            comparison["incomplete_score"] += 1
        elif best_alt is None:
            comparison["no_available_alternative"] += 1
        elif total >= best_alt:
            comparison["hold_at_or_above_best_alternative"] += 1
        else:
            comparison["hold_below_best_alternative"] += 1
            margins.append(total - best_alt)
        enriched.append((row, posture, total, best_alt))

    selected_decisions = sum(
        row.get("Recomendação") == "HOLD" for row in decisions
    )
    return {
        "candidate_count": len(holds),
        "selected_candidate_count": len(selected),
        "final_hold_recommendations": selected_decisions,
        "total_score": summarize(totals),
        "components": components,
        "posture_counts": dict(sorted(posture_counts.items())),
        "score_by_posture": {
            posture: summarize(values) for posture, values in sorted(by_posture.items())
        },
        "comparisons": dict(sorted(comparison.items())),
        "hold_minus_best_alternative": summarize(margins),
        "missing_economy_context": posture_counts.get("CONTEXTO_AUSENTE", 0),
        "limitations": [
            "The exported score is a heuristic ranking value, not a calibrated utility or probability.",
            "A candidate score of zero may still be selected as the explicit fallback when no positive alternative wins.",
            "The table does not establish whether holding was strategically optimal; that requires counterfactual state and outcome evidence.",
            "Economic posture is joined by player/round/step. Missing matches remain explicit and are not inferred.",
            "This audit does not modify HOLD scoring, recommendations, PPO, training, observations, masks, rewards, rules, or execution.",
        ],
    }


def render_markdown(result: dict) -> str:
    score = result["total_score"]
    lines = [
        "# HOLD baseline audit",
        "",
        "> Shadow/read-only diagnostic. This report does not change the HOLD baseline or any gameplay behavior.",
        "",
        f"- HOLD candidates: **{result['candidate_count']}**",
        f"- Selected HOLD candidates: **{result['selected_candidate_count']}**",
        f"- Final HOLD recommendations: **{result['final_hold_recommendations']}**",
        f"- Total score: **mean {score['mean']} / min {score['min']} / max {score['max']} / distinct values {score['distinct']}**",
        f"- Missing economic posture context: **{result['missing_economy_context']}**",
        "",
        "## Code-path review",
        "",
        "- Baseline `strategy::ActionEvaluator`: HOLD receives a +0.24 posture component under `AccumulateResources`; the implementation does not add this bonus in the other posture branches.",
        "- Independent `ContextualActionEvaluator`: HOLD total score is explicitly reset to 0.0 and retained as the fallback when no positive contextual candidate is selected.",
        "- Therefore, the observed 0.240 is not a universal invariant across both evaluators. The report checks whether the reference session's constant value is explained by its observed economic-posture distribution.",
        "",
        "## Score components",
        "",
        "| Component | N | Mean | Min | Max | Distinct |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, stats in result["components"].items():
        lines.append(f"| {name} | {stats['count']} | {stats['mean']} | {stats['min']} | {stats['max']} | {stats['distinct']} |")
    lines += [
        "",
        "## Economic posture",
        "",
        "| Posture | Candidates | HOLD score mean | Min | Max | Distinct |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for posture, count in result["posture_counts"].items():
        stats = result["score_by_posture"].get(posture, {})
        lines.append(f"| {posture} | {count} | {stats.get('mean')} | {stats.get('min')} | {stats.get('max')} | {stats.get('distinct')} |")
    lines += [
        "",
        "## Comparison against available alternatives",
        "",
        "| Classification | Decisions |",
        "|---|---:|",
    ]
    labels = {
        "hold_at_or_above_best_alternative": "HOLD score at or above best available alternative",
        "hold_below_best_alternative": "HOLD score below best available alternative",
        "no_available_alternative": "No other available scored alternative",
        "incomplete_score": "Incomplete HOLD score",
    }
    for name, count in result["comparisons"].items():
        lines.append(f"| {labels.get(name, name)} | {count} |")
    margin = result["hold_minus_best_alternative"]
    lines += [
        "",
        f"Mean HOLD-minus-best-alternative margin when HOLD is lower: **{margin['mean']}** (N={margin['count']}).",
        "",
        "## Interpretation boundaries",
        "",
    ]
    lines.extend(f"- {item}" for item in result["limitations"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actions_audit", type=Path)
    parser.add_argument("--economy-audit", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    for path in (args.actions_audit, args.economy_audit):
        if path is not None and not path.is_file():
            parser.error(f"Audit file not found: {path}")
    report = render_markdown(analyze_hold_audit(args.actions_audit, args.economy_audit))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"HOLD audit written to {args.output}")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
