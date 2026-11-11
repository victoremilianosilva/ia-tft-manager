"""JSONL ingestion and decision-level audit helpers for Composition Intelligence."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def _validated_record(value: Any, line_number: int, records: list, errors: list) -> None:
    if not isinstance(value, dict):
        errors.append(f"Linha {line_number}: registro precisa ser um objeto JSON.")
    elif not isinstance(value.get("diagnostics"), dict):
        errors.append(f"Linha {line_number}: campo 'diagnostics' ausente ou inválido; registro ignorado.")
    else:
        records.append(value)


def load_diagnostic_jsonl(path: str | Path) -> tuple[list[dict[str, Any]], list[str]]:
    """Read normal JSONL and recover older files separated by literal \\n tokens.

    The recovery happens only between decoded JSON values, so escaped newlines
    inside JSON strings are preserved.
    """
    source = Path(path).read_text(encoding="utf-8-sig")
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    decoder = json.JSONDecoder()
    position = 0
    line_number = 1
    while position < len(source):
        while position < len(source):
            if source[position].isspace():
                if source[position] == "\n":
                    line_number += 1
                position += 1
                continue
            if source.startswith("\\n", position):
                position += 2
                line_number += 1
                continue
            if source.startswith("\\r", position):
                position += 2
                continue
            break
        if position >= len(source):
            break
        start_line = line_number
        try:
            value, end = decoder.raw_decode(source, position)
        except json.JSONDecodeError as exc:
            errors.append(f"Linha {start_line}: JSON inválido ({exc.msg}).")
            newline = source.find("\n", position)
            if newline < 0:
                break
            position = newline + 1
            line_number += 1
            continue
        _validated_record(value, start_line, records, errors)
        line_number += source.count("\n", position, end)
        position = end
    return records, errors


def _snapshot_review_key(record: dict[str, Any]) -> tuple:
    payload = record.get("diagnostics") or {}
    decision = payload.get("composition_decision") or {}
    transition = payload.get("transition_plan") or {}
    return (
        record.get("player_id", -1),
        record.get("round"),
        record.get("composition_version"),
        decision.get("decision"),
        transition.get("to"),
    )


def _intent_key(record: dict[str, Any], unit: dict[str, Any]) -> tuple:
    reasons = unit.get("reasons") or []
    reason_codes = tuple(sorted(
        str(reason.get("code", "")) for reason in reasons if isinstance(reason, dict)
    ))
    return (
        record.get("player_id", -1), record.get("round"),
        record.get("composition_version"), unit.get("champion_id"),
        unit.get("intent"), unit.get("relation"), unit.get("target_star"),
        reason_codes,
    )


def audit_diagnostic_records(records: list[dict[str, Any]], errors: list[str] | None = None) -> dict[str, Any]:
    sequences = [r.get("sequence") for r in records if isinstance(r.get("sequence"), int)]
    duplicate_sequences = sorted(v for v, count in Counter(sequences).items() if count > 1)
    out_of_order = sum(1 for left, right in zip(sequences, sequences[1:]) if right < left)
    stale = [r for r in records if bool(r.get("stale"))]
    intents: Counter[str] = Counter()
    observed_intents: Counter[str] = Counter()
    candidates: Counter[str] = Counter()
    evidence_quality: Counter[str] = Counter()
    transitions, correlations = [], []
    recommendation_count = 0
    reviews: dict[tuple, dict[str, Any]] = {}
    unique_intents: dict[tuple, dict[str, Any]] = {}
    for record in records:
        payload = record.get("diagnostics") or {}
        review_key = _snapshot_review_key(record)
        review = reviews.setdefault(review_key, {
            "player_id": record.get("player_id", -1),
            "round": record.get("round"),
            "composition_version": record.get("composition_version"),
            "decision": (payload.get("composition_decision") or {}).get("decision", "UNKNOWN"),
            "target": (payload.get("transition_plan") or {}).get("to"),
            "first_sequence": record.get("sequence"),
            "last_sequence": record.get("sequence"),
            "observations": 0,
        })
        review["observations"] += 1
        if isinstance(record.get("sequence"), int):
            if not isinstance(review.get("first_sequence"), int) or record["sequence"] < review["first_sequence"]:
                review["first_sequence"] = record["sequence"]
            if not isinstance(review.get("last_sequence"), int) or record["sequence"] > review["last_sequence"]:
                review["last_sequence"] = record["sequence"]

        for unit in payload.get("unit_intentions", []) or []:
            if not isinstance(unit, dict):
                continue
            intent = str(unit.get("intent") or "UNKNOWN")
            observed_intents[intent] += 1
            key = _intent_key(record, unit)
            item = unique_intents.setdefault(key, {
                "player_id": record.get("player_id", -1),
                "round": record.get("round"),
                "composition_version": record.get("composition_version"),
                "champion_id": unit.get("champion_id"),
                "intent": intent,
                "relation": unit.get("relation", "UNKNOWN"),
                "priority": unit.get("priority"),
                "confidence_not_probability": unit.get("confidence_not_probability"),
                "copies_owned": unit.get("copies_owned"),
                "highest_star": unit.get("highest_star"),
                "target_star": unit.get("target_star"),
                "on_board": unit.get("on_board"),
                "sale_restricted": unit.get("sale_restricted"),
                "reasons": unit.get("reasons") or [],
                "first_sequence": record.get("sequence"),
                "last_sequence": record.get("sequence"),
                "observations": 0,
            })
            item["observations"] += 1
            if isinstance(record.get("sequence"), int):
                if not isinstance(item.get("first_sequence"), int) or record["sequence"] < item["first_sequence"]:
                    item["first_sequence"] = record["sequence"]
                if not isinstance(item.get("last_sequence"), int) or record["sequence"] > item["last_sequence"]:
                    item["last_sequence"] = record["sequence"]

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
                "player_id": record.get("player_id", -1),
            })
        correlation = payload.get("recommendation_to_later_outcome")
        if isinstance(correlation, dict):
            correlations.append(correlation)

    versions_by_player: dict[Any, list] = defaultdict(list)
    for record in records:
        versions_by_player[record.get("player_id", -1)].append(record.get("composition_version"))
    version_regressions = sum(
        1 for versions in versions_by_player.values()
        for old, new in zip(versions, versions[1:])
        if isinstance(old, int) and isinstance(new, int) and new < old
    )
    for key, item in unique_intents.items():
        intents[item["intent"]] += 1
    return {
        "record_count": len(records), "parse_errors": list(errors or []),
        "stale_count": len(stale),
        "stale_reasons": Counter(str(r.get("stale_reason") or "sem motivo informado") for r in stale),
        "duplicate_sequences": duplicate_sequences, "out_of_order_sequences": out_of_order,
        "version_regressions": version_regressions, "transitions": transitions,
        "intent_counts": intents, "observed_intent_counts": observed_intents,
        "unique_intent_count": len(unique_intents),
        "unique_intents": list(unique_intents.values()),
        "unique_review_count": len(reviews), "reviews": list(reviews.values()),
        "candidate_counts": candidates, "evidence_quality": evidence_quality,
        "recommendation_count": recommendation_count,
        "correlation_count": len(correlations), "correlations": correlations,
    }


def format_diagnostic_audit(records: list[dict[str, Any]], report: dict[str, Any]) -> str:
    lines = [
        "# Composition Intelligence — auditoria shadow",
        "",
        f"- Snapshots válidos: **{report['record_count']}**",
        f"- Revisões estratégicas únicas (jogador/round/versão/decisão/alvo): **{report['unique_review_count']}**",
        f"- Recomendações registradas: **{report['recommendation_count']}**",
        f"- Snapshots stale: **{report['stale_count']}**",
        f"- Correlações posteriores: **{report['correlation_count']}**",
        f"- Sequências duplicadas: **{report['duplicate_sequences'] or 'nenhuma'}**",
        f"- Sequências fora de ordem: **{report['out_of_order_sequences']}**",
        f"- Regressões de versão por jogador: **{report['version_regressions']}**",
        "",
        "## Intenções por unidade — decisões únicas",
        "",
        "As contagens abaixo deduplicam observações repetidas da mesma unidade dentro da mesma revisão estratégica. A contagem de snapshots permanece disponível para comparação.",
        "",
        "| Intenção | Decisões únicas | Observações nos snapshots |",
        "|---|---:|---:|",
    ]
    for name in sorted(set(report["intent_counts"]) | set(report["observed_intent_counts"])):
        lines.append(f"| {name} | {report['intent_counts'][name]} | {report['observed_intent_counts'][name]} |")
    if not report["intent_counts"]:
        lines.append("| sem dados | 0 | 0 |")
    lines.extend([
        "",
        "## Detalhamento das intenções",
        "",
        "| Jogador | Round | Versão | Unidade (ID) | Intenção | Relação | Prioridade | Confiança* | Cópias | Alvo estrelas | Evidências / justificativas | Snapshots |",
        "|---|---|---:|---:|---|---|---:|---:|---:|---:|---|---:|",
    ])
    for item in sorted(report["unique_intents"], key=lambda x: (
        int(x.get("player_id", -1) or -1), str(x.get("round")), int(x.get("champion_id", -1) or -1)
    )):
        reasons = "; ".join(
            str(reason.get("message") or reason.get("code") or "")
            for reason in item.get("reasons", []) if isinstance(reason, dict)
        ) or "sem justificativa registrada"
        lines.append("| " + " | ".join(str(value if value is not None else "—").replace("|", "\\|") for value in (
            f"Jogador {int(item['player_id']) + 1}" if isinstance(item.get("player_id"), int) else item.get("player_id"),
            item.get("round"), item.get("composition_version"), item.get("champion_id"),
            item.get("intent"), item.get("relation"), item.get("priority"),
            item.get("confidence_not_probability"), item.get("copies_owned"),
            item.get("target_star"), reasons, item.get("observations"),
        )) + " |")
    if not report["unique_intents"]:
        lines.append("| — | — | — | — | — | — | — | — | — | — | Sem intenções disponíveis | 0 |")
    lines.extend([
        "",
        "* Confiança é um score não calibrado, não uma probabilidade.",
        "",
        "## Candidatos de ação",
        "",
    ])
    lines.extend(f"- {k}: {v}" for k, v in sorted(report["candidate_counts"].items()) or [("sem dados", 0)])
    lines.extend(["", "## Qualidade das evidências (enumeração emitida pela fonte)", ""])
    lines.extend(f"- quality={k}: {v}" for k, v in sorted(report["evidence_quality"].items()) or [("sem dados", 0)])
    lines.extend(["", "## Transições publicadas", ""])
    for item in report["transitions"]:
        player = f"Jogador {int(item['player_id']) + 1}" if isinstance(item.get("player_id"), int) else item.get("player_id")
        lines.append(f"- {player}, round {item['round']}: {item['from']} v{item['previous_version']} → {item['to']} v{item['new_version']}")
    if not report["transitions"]:
        lines.append("- Nenhuma transição publicada no arquivo.")
    lines.extend(["", "## Correlação com resultados posteriores", ""])
    for item in report["correlations"]:
        lines.append(f"- round {item.get('recommendation_round')} → round {item.get('outcome_round')} (composition v{item.get('composition_version')})")
    if not report["correlations"]:
        lines.append("- Nenhum resultado posterior associado.")
    lines.extend(["", "## Integridade / parsing", ""])
    lines.extend(f"- {e}" for e in report["parse_errors"])
    if not report["parse_errors"]:
        lines.append("- Sem erros de parsing.")
    if report["stale_reasons"]:
        lines.extend(["", "### Motivos de stale", ""])
        lines.extend(f"- {reason}: {count}" for reason, count in sorted(report["stale_reasons"].items()))
    lines.extend([
        "",
        "Resultados posteriores são correlações observacionais, não prova de causalidade.",
        "Este relatório é somente leitura: nenhuma recomendação é executada e nenhuma ação do PPO é alterada.",
        "",
    ])
    return "\n".join(lines)


def format_composition_vs_ppo(records: list[dict[str, Any]], decision_timeline: list[dict[str, Any]]) -> str:
    ppo_actions: Counter[str] = Counter()
    for decision in decision_timeline:
        name = str(decision.get("action_name") or "").strip()
        if name:
            ppo_actions[name] += 1
    ci_names = {
        0: "NONE", 1: "BUY_UNIT", 2: "BUY_XP", 3: "REROLL",
        4: "SELL_UNIT", 5: "DEPLOY_OR_MOVE", 6: "HOLD",
    }
    composition_actions: Counter[str] = Counter()
    for record in records:
        action = (record.get("diagnostics") or {}).get("action_recommendation") or {}
        if action.get("recommended_action") is not None:
            try:
                value = int(action["recommended_action"])
            except (TypeError, ValueError):
                continue
            composition_actions[ci_names.get(value, f"UNKNOWN_{value}")] += 1
    lines = [
        "# Composition Intelligence × PPO — comparação descritiva",
        "",
        f"- Snapshots válidos da Composition Intelligence: **{len(records)}**",
        f"- Decisões PPO encontradas na auditoria: **{sum(ppo_actions.values())}**",
        "",
        "As distribuições são agregadas e não representam correspondência ação-a-ação.",
        "",
        "## Ações executadas pelo PPO",
        "",
    ]
    lines.extend(f"- {name}: {count}" for name, count in sorted(ppo_actions.items()) or [("sem dados", 0)])
    lines.extend(["", "## Recomendações da Composition Intelligence", ""])
    lines.extend(f"- {name}: {count}" for name, count in sorted(composition_actions.items()) or [("sem dados", 0)])
    lines.extend([
        "",
        "## Interpretação",
        "",
        "O PPO é a única fonte das ações executadas; recomendações shadow não são executadas.",
        "Diferenças entre as distribuições não demonstram erro nem causalidade. Considere round, jogador, estado e evidência.",
        "",
    ])
    return "\n".join(lines)
