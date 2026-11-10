"""JSONL ingestion and audit helpers for Composition Intelligence diagnostics."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


def load_diagnostic_jsonl(path: str | Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line_number, raw in enumerate(stream, 1):
            if not raw.strip():
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"Linha {line_number}: JSON inválido ({exc.msg}).")
                continue
            if not isinstance(record, dict):
                errors.append(f"Linha {line_number}: registro precisa ser um objeto JSON.")
                continue
            if "diagnostics" not in record or not isinstance(record.get("diagnostics"), dict):
                errors.append(f"Linha {line_number}: campo 'diagnostics' ausente ou inválido; registro ignorado.")
                continue
            records.append(record)
    return records, errors


def audit_diagnostic_records(records: list[dict[str, Any]], errors: list[str] | None = None) -> dict[str, Any]:
    sequences = [r.get("sequence") for r in records if isinstance(r.get("sequence"), int)]
    duplicate_sequences = sorted(v for v, count in Counter(sequences).items() if count > 1)
    out_of_order = sum(1 for left, right in zip(sequences, sequences[1:]) if right < left)
    stale = [r for r in records if bool(r.get("stale"))]
    intents: Counter[str] = Counter()
    candidates: Counter[str] = Counter()
    evidence_quality: Counter[str] = Counter()
    transitions, correlations = [], []
    recommendation_count = 0
    for record in records:
        payload = record.get("diagnostics") or {}
        for unit in payload.get("unit_intentions", []) or []:
            if isinstance(unit, dict):
                intents[str(unit.get("intent") or "UNKNOWN")] += 1
        action = payload.get("action_recommendation") or {}
        if action.get("recommended_action") is not None:
            recommendation_count += 1
        for candidate in action.get("candidates", []) or []:
            if isinstance(candidate, dict):
                candidates[str(candidate.get("disposition") or "unknown")] += 1
                if candidate.get("selected"):
                    candidates["selected"] += 1
        evidence = payload.get("evidence") or {}
        for section in ("economy", "board", "items"):
            metadata = (evidence.get(section) or {}).get("metadata") or {}
            if metadata.get("quality") is not None:
                evidence_quality[str(metadata["quality"])] += 1
        transition = payload.get("published_transition")
        if isinstance(transition, dict):
            transitions.append({
                "from": transition.get("previous_composition_id"),
                "to": transition.get("new_composition_id"),
                "previous_version": transition.get("previous_version"),
                "new_version": transition.get("new_version"),
                "round": record.get("round"),
            })
        correlation = payload.get("recommendation_to_later_outcome")
        if isinstance(correlation, dict):
            correlations.append(correlation)
    versions = [r.get("composition_version") for r in records]
    version_regressions = sum(
        1 for old, new in zip(versions, versions[1:])
        if isinstance(old, int) and isinstance(new, int) and new < old
    )
    return {
        "record_count": len(records), "parse_errors": list(errors or []),
        "stale_count": len(stale),
        "stale_reasons": Counter(str(r.get("stale_reason") or "sem motivo informado") for r in stale),
        "duplicate_sequences": duplicate_sequences, "out_of_order_sequences": out_of_order,
        "version_regressions": version_regressions, "transitions": transitions,
        "intent_counts": intents, "candidate_counts": candidates,
        "evidence_quality": evidence_quality, "recommendation_count": recommendation_count,
        "correlation_count": len(correlations), "correlations": correlations,
    }


def format_diagnostic_audit(records: list[dict[str, Any]], report: dict[str, Any]) -> str:
    lines = [
        "COMPOSITION INTELLIGENCE · AUDITORIA SHADOW", "=" * 58,
        f"Snapshots: {report['record_count']} | Recomendações registradas: {report['recommendation_count']}",
        f"Snapshots stale: {report['stale_count']} | Correlações posteriores: {report['correlation_count']}",
        f"Sequências duplicadas: {report['duplicate_sequences'] or 'nenhuma'}",
        f"Sequências fora de ordem: {report['out_of_order_sequences']}",
        f"Regressões de versão: {report['version_regressions']}", "", "INTENÇÕES POR UNIDADE",
    ]
    lines.extend(f"  {k}: {v}" for k, v in sorted(report["intent_counts"].items()) or [("sem dados", 0)])
    lines.extend(["", "CANDIDATOS DE AÇÃO"])
    lines.extend(f"  {k}: {v}" for k, v in sorted(report["candidate_counts"].items()) or [("sem dados", 0)])
    lines.extend(["", "QUALIDADE DAS EVIDÊNCIAS (enumeração emitida pela fonte)"])
    lines.extend(f"  quality={k}: {v}" for k, v in sorted(report["evidence_quality"].items()) or [("sem dados", 0)])
    lines.extend(["", "TRANSIÇÕES PUBLICADAS"])
    for item in report["transitions"]:
        lines.append(f"  round {item['round']}: {item['from']} v{item['previous_version']} -> {item['to']} v{item['new_version']}")
    if not report["transitions"]:
        lines.append("  nenhuma transição publicada no arquivo")
    lines.extend(["", "CORRELAÇÃO COM RESULTADOS POSTERIORES"])
    for item in report["correlations"]:
        lines.append(f"  round {item.get('recommendation_round')} -> round {item.get('outcome_round')} (composition v{item.get('composition_version')})")
    if not report["correlations"]:
        lines.append("  nenhum resultado posterior associado")
    lines.extend(["", "INTEGRIDADE / PARSING"])
    lines.extend(f"  {e}" for e in report["parse_errors"])
    if not report["parse_errors"]:
        lines.append("  sem erros de parsing")
    lines.extend([
        "", "NOTA: confiança é um score não calibrado, não uma probabilidade.",
        "Resultados posteriores são correlações observacionais, não prova de causalidade.",
        "Este relatório não executa ações nem altera o estado da engine.", "", "DETALHE DOS SNAPSHOTS",
    ])
    for index, record in enumerate(records):
        payload = record.get("diagnostics") or {}
        decision = payload.get("composition_decision") or {}
        action = payload.get("action_recommendation") or {}
        lines.append(
            f"  #{record.get('sequence', index + 1)} round={record.get('round', '?')} "
            f"{record.get('composition_id') or 'sem composição'} v{record.get('composition_version', '?')} "
            f"decision={decision.get('decision', '—')} action={action.get('recommended_action', '—')} "
            f"stale={bool(record.get('stale'))}"
        )
    return "\n".join(lines)
