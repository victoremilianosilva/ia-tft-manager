"""Read-only BUY_XP coverage audit for Action Evaluator Markdown exports."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path


DECISION_HEADER = "| Jogador | Round | Step | PPO executou | Recomendação |"
CANDIDATE_HEADER = "| Jogador | Round | Step | Ação | Campeão | Disponível |"
ECONOMY_HEADER = "| Jogador | Round | Step | Postura |"


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
    raw = row.get(key)
    if raw is None or raw == "":
        return None
    if isinstance(raw, (int, float)):
        return float(raw)
    value = str(raw).strip()
    if not value or value in {"—", "-"}:
        return None
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return None


def _key(row: dict[str, str]) -> tuple[str, str, str]:
    return row.get("Jogador", ""), row.get("Round", ""), row.get("Step", "")


def _stats(rows: list[dict[str, str]], field: str) -> dict:
    values = [value for row in rows if (value := _number(row, field)) is not None]
    if not values:
        return {"count": 0, "mean": None, "min": None, "max": None}
    return {
        "count": len(values),
        "mean": round(sum(values) / len(values), 4),
        "min": min(values),
        "max": max(values),
    }


def analyze_buy_xp_audit(actions_path: Path, economy_path: Path | None = None) -> dict:
    candidates = _read_table(actions_path, CANDIDATE_HEADER)
    decisions = _read_table(actions_path, DECISION_HEADER)
    xp_rows = [row for row in candidates if row.get("Ação") == "BUY_XP"]
    by_decision: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in candidates:
        by_decision[_key(row)].append(row)

    economy_by_key = {}
    if economy_path is not None:
        economy_by_key = {
            _key(row): row for row in _read_table(economy_path, ECONOMY_HEADER)
        }

    buckets = Counter()
    rounds: dict[str, list[dict[str, str]]] = defaultdict(list)
    enriched = []
    for row in xp_rows:
        score = _number(row, "Total")
        selected = row.get("Selecionado", "").lower() == "true"
        alternatives = [
            _number(other, "Total")
            for other in by_decision[_key(row)]
            if other.get("Ação") != "BUY_XP"
        ]
        alternatives = [value for value in alternatives if value is not None]
        best_alternative = max(alternatives) if alternatives else None
        margin = score - best_alternative if score is not None and best_alternative is not None else None

        if score is None or row.get("Disponível", "").lower() not in {"true", "false"}:
            bucket = "inconclusive_missing_candidate_data"
        elif selected:
            bucket = "selected_recommendation"
        elif score > 0:
            bucket = "positive_but_outscored"
        else:
            bucket = "non_positive_candidate"

        economy = economy_by_key.get(_key(row))
        enriched_row = dict(row)
        enriched_row["_bucket"] = bucket
        enriched_row["_best_alternative"] = best_alternative
        enriched_row["_margin"] = margin
        enriched_row["_economic_posture"] = (economy or {}).get("Postura")
        enriched.append(enriched_row)
        buckets[bucket] += 1
        rounds[row.get("Round", "?")].append(enriched_row)

    final_buy_xp = [row for row in decisions if row.get("Recomendação") == "BUY_XP"]
    selected_rows = [row for row in enriched if row["_bucket"] == "selected_recommendation"]
    positive_rows = [row for row in enriched if _number(row, "Total") is not None and _number(row, "Total") > 0]
    matched = sum(row["_economic_posture"] is not None for row in enriched)

    component_fields = (
        "Δ ouro direto", "Juros perdidos", "Oportunidade", "Board",
        "Sobrevivência", "Streak", "Composição", "Upgrade",
        "Score custo direto", "Score juros", "Score oportunidade", "Total",
    )
    round_report = {}
    for round_id, rows in sorted(rounds.items()):
        round_report[round_id] = {
            "candidate_count": len(rows),
            "selected_count": sum(row["_bucket"] == "selected_recommendation" for row in rows),
            "positive_score_count": sum(
                _number(row, "Total") is not None and _number(row, "Total") > 0 for row in rows
            ),
            "mean_total": _stats(rows, "Total")["mean"],
            "mean_cost_score": _stats(rows, "Score custo direto")["mean"],
            "mean_interest_score": _stats(rows, "Score juros")["mean"],
        }

    return {
        "buy_xp_candidate_count": len(xp_rows),
        "buy_xp_selected_candidate_count": len(selected_rows),
        "final_buy_xp_recommendation_count": len(final_buy_xp),
        "positive_score_candidate_count": len(positive_rows),
        "economic_context_matches": matched,
        "economic_context_missing": len(enriched) - matched,
        "review_buckets": dict(sorted(buckets.items())),
        "candidate_components": {
            field: _stats(xp_rows, field) for field in component_fields
        },
        "selected_by_round": dict(sorted(Counter(row.get("Round", "?") for row in selected_rows).items())),
        "positive_score_not_selected": sum(row["_bucket"] == "positive_but_outscored" for row in enriched),
        "positive_score_but_outscored_margin": _stats(
            [row for row in enriched if row["_bucket"] == "positive_but_outscored"], "_margin"
        ),
        "rounds": round_report,
        "limitations": [
            "Positive score is evidence that the evaluator valued the candidate, not proof that buying XP was strategically optimal.",
            "Positive-but-outscored means another candidate had a higher score at the same decision; it is not a missed-opportunity label.",
            "The available candidate table does not expose raw current gold, level, XP-to-next-level, shop odds, or the counterfactual board after leveling.",
            "Economic posture is joined by player/round/step when the optional economic audit is supplied; it does not fill missing raw state.",
            "No target frequency is imposed. This report does not change scores, recommendations, PPO actions, training, or gameplay.",
        ],
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# BUY_XP coverage audit",
        "",
        "> Shadow/read-only diagnostic. No action, score, PPO behavior, or gameplay is changed.",
        "",
        f"- BUY_XP candidates: **{result['buy_xp_candidate_count']}**",
        f"- Selected BUY_XP candidates: **{result['buy_xp_selected_candidate_count']}**",
        f"- Final BUY_XP recommendations: **{result['final_buy_xp_recommendation_count']}**",
        f"- Candidates with positive total score: **{result['positive_score_candidate_count']}**",
        f"- Economic posture context matched: **{result['economic_context_matches']}**",
        f"- Economic posture context missing: **{result['economic_context_missing']}**",
        "",
        "## Candidate classification",
        "",
        "| Classification | Candidates |",
        "|---|---:|",
    ]
    labels = {
        "selected_recommendation": "Selected recommendation",
        "positive_but_outscored": "Positive score, outscored by another action",
        "non_positive_candidate": "Non-positive candidate score",
        "inconclusive_missing_candidate_data": "Incomplete candidate data",
    }
    lines.extend(
        f"| {labels.get(key, key)} | {value} |"
        for key, value in result["review_buckets"].items()
    )
    lines += [
        "",
        "## Candidate score components",
        "",
        "| Component | N | Mean | Min | Max |",
        "|---|---:|---:|---:|---:|",
    ]
    for field, stats in result["candidate_components"].items():
        lines.append(
            f"| {field} | {stats['count']} | {stats['mean']} | {stats['min']} | {stats['max']} |"
        )
    lines += [
        "",
        "## Selected recommendations by round",
        "",
        "| Round | Selected BUY_XP |",
        "|---|---:|",
    ]
    lines.extend(f"| {round_id} | {count} |" for round_id, count in result["selected_by_round"].items())
    lines += [
        "",
        "## Candidate coverage by round",
        "",
        "| Round | Candidates | Positive score | Selected | Mean total |",
        "|---|---:|---:|---:|---:|",
    ]
    for round_id, stats in result["rounds"].items():
        lines.append(
            f"| {round_id} | {stats['candidate_count']} | {stats['positive_score_count']} | "
            f"{stats['selected_count']} | {stats['mean_total']} |"
        )
    lines += ["", "## Limitations", ""]
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
    report = render_markdown(analyze_buy_xp_audit(args.actions_audit, args.economy_audit))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"BUY_XP audit written to {args.output}")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
