"""Read-only audit for the unified strategic direction/pivot event stream.

Input contract: one JSON object per line in strategic_direction_pivot.jsonl.
The producer is expected to emit the normalized UnifiedStrategicStateMachine
snapshot. Missing fields remain unavailable; this module never reconstructs
strategic decisions from PPO actions or assumes that missing evidence is false.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_direction_pivot_jsonl(path: str | Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    try:
        source = Path(path).read_text(encoding="utf-8-sig")
    except OSError as exc:
        return [], [f"Não foi possível ler {path}: {exc}"]
    for line_number, line in enumerate(source.splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"Linha {line_number}: JSON inválido ({exc.msg}).")
            continue
        if not isinstance(value, dict):
            errors.append(f"Linha {line_number}: registro precisa ser um objeto JSON.")
            continue
        if not isinstance(value.get("phase"), str):
            errors.append(f"Linha {line_number}: campo 'phase' ausente; registro ignorado.")
            continue
        records.append(value)
    return records, errors


def _identity(value: Any) -> str | None:
    if isinstance(value, dict):
        value = value.get("identity") or value.get("composition_identity") or value.get("composition_id")
    return str(value) if value not in (None, "") else None


def _version(value: Any) -> int | None:
    if isinstance(value, dict):
        value = value.get("version") if value.get("version") is not None else value.get("composition_version")
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def audit_direction_pivot_records(records: list[dict[str, Any]], errors: list[str] | None = None) -> dict[str, Any]:
    phase_counts: Counter[str] = Counter()
    pivot_counts: Counter[str] = Counter()
    carry_gate_counts: Counter[str] = Counter()
    missing_counts: Counter[str] = Counter()
    per_player: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "records": 0, "rounds": set(), "phase_counts": Counter(),
        "pivot_counts": Counter(), "carry_gate_counts": Counter(),
        "support_units": Counter(), "shop_evidence_records": 0,
        "conflicts": [], "confirmed_transitions": [], "samples": [],
        "pivot_reason_counts": Counter(),
    })
    conflicts: list[dict[str, Any]] = []
    transitions: list[dict[str, Any]] = []
    sequence_by_player: dict[str, list[int]] = defaultdict(list)
    sequence_values: list[int] = []

    for record in records:
        player = str(record.get("player_id", "unknown"))
        round_id = record.get("round")
        phase = str(record.get("phase") or "UNKNOWN").upper()
        phase_counts[phase] += 1
        item = per_player[player]
        item["records"] += 1
        item["phase_counts"][phase] += 1
        if round_id is not None:
            item["rounds"].add(str(round_id))
        sequence = record.get("sequence")
        if isinstance(sequence, int):
            sequence_by_player[player].append(sequence)
            sequence_values.append(sequence)

        active = record.get("active_composition")
        direction = record.get("direction_anchor")
        pivot = record.get("pivot_candidate")
        feasibility = record.get("feasibility") or {}
        if not isinstance(feasibility, dict):
            feasibility = {}
        carry = record.get("carry_gate") or {}
        if not isinstance(carry, dict):
            carry = {}
        status = str(feasibility.get("status") or record.get("pivot_status") or "UNAVAILABLE").upper()
        if phase == "PIVOT_EVALUATION":
            pivot_counts[status] += 1
            item["pivot_counts"][status] += 1
            reason = str(feasibility.get("reason") or record.get("reason") or "UNAVAILABLE")
            item["pivot_reason_counts"][reason] += 1
        elif phase == "PIVOT_CONFIRMED":
            pivot_counts["CONFIRMED"] += 1
            item["pivot_counts"]["CONFIRMED"] += 1
        elif phase == "INVALIDATED":
            pivot_counts["INVALIDATED"] += 1
            item["pivot_counts"]["INVALIDATED"] += 1
        elif phase == "NO_EVIDENCE":
            pivot_counts["INSUFFICIENT_EVIDENCE"] += 1
            item["pivot_counts"]["INSUFFICIENT_EVIDENCE"] += 1
        if carry.get("eligible") is True:
            carry_gate_counts["eligible"] += 1
            item["carry_gate_counts"]["eligible"] += 1
        elif carry.get("eligible") is False:
            carry_gate_counts["not_eligible"] += 1
            item["carry_gate_counts"]["not_eligible"] += 1
        else:
            carry_gate_counts["unavailable"] += 1
            item["carry_gate_counts"]["unavailable"] += 1
            missing_counts["carry_gate"] += 1

        support = record.get("unit_support")
        if isinstance(support, list):
            for unit in support:
                if not isinstance(unit, dict):
                    continue
                relation = str(unit.get("relation") or unit.get("classification") or "UNKNOWN").upper()
                item["support_units"][relation] += 1
                for field in ("copies_owned", "highest_star", "target_star"):
                    if unit.get(field) is None:
                        missing_counts[f"unit_support.{field}"] += 1
        else:
            missing_counts["unit_support"] += 1

        shop = record.get("shop_evidence")
        if isinstance(shop, list):
            item["shop_evidence_records"] += 1
        else:
            missing_counts["shop_evidence"] += 1

        if len(item["samples"]) < 100:
            item["samples"].append({
                "round": round_id, "sequence": sequence, "phase": phase,
                "active_composition": {"identity": _identity(active), "version": _version(active)},
                "direction_anchor": {
                    "identity": _identity(direction),
                    "composition_identity": direction.get("composition_identity") if isinstance(direction, dict) else None,
                    "composition_version": _version(direction),
                    "lifecycle": direction.get("lifecycle") if isinstance(direction, dict) else None,
                },
                "pivot_candidate": {
                    "identity": pivot.get("identity") if isinstance(pivot, dict) else None,
                    "target": (pivot.get("target_composition_identity") or pivot.get("target_direction")) if isinstance(pivot, dict) else None,
                    "source_direction_anchor_identity": pivot.get("source_direction_anchor_identity") if isinstance(pivot, dict) else None,
                },
                "pivot_status": status,
                "pivot_reason": feasibility.get("reason") or record.get("reason"),
                "blockers": feasibility.get("blockers"),
                "missing_data": feasibility.get("missing_data"),
                "carry_gate": carry if isinstance(carry, dict) else None,
                "shop_evidence_count": len(shop) if isinstance(shop, list) else None,
                "shop_evidence": shop if isinstance(shop, list) else None,
                "unit_support": support if isinstance(support, list) else None,
            })

        active_id, active_version = _identity(active), _version(active)
        direction_comp = direction.get("composition_identity") if isinstance(direction, dict) else None
        direction_version = _version(direction)
        direction_id = _identity(direction)
        pivot_source_id = pivot.get("source_direction_anchor_identity") if isinstance(pivot, dict) else None
        pivot_source_version = _version(pivot.get("source_composition_version")) if isinstance(pivot, dict) else None
        pivot_target = (pivot.get("target_composition_identity") or pivot.get("target_direction")) if isinstance(pivot, dict) else None

        def add_conflict(code: str, message: str, evidence: dict[str, Any]) -> None:
            value = {"player_id": player, "round": round_id, "sequence": sequence,
                     "phase": phase, "code": code, "message": message, "evidence": evidence}
            conflicts.append(value)
            item["conflicts"].append(value)

        # During evaluation, the active direction must remain anchored to the
        # current composition; the candidate must point back to that anchor.
        if phase in ("COMPOSITION_ACTIVE", "PIVOT_EVALUATION", "NO_EVIDENCE", "INVALIDATED"):
            if active_id is not None and direction_comp is not None and active_id != direction_comp:
                add_conflict("ACTIVE_DIRECTION_ID_MISMATCH",
                             "Composição ativa e composição da âncora de direção divergem.",
                             {"active_composition": active_id, "direction_composition": direction_comp})
            if active_version is not None and direction_version is not None and active_version != direction_version:
                add_conflict("ACTIVE_DIRECTION_VERSION_MISMATCH",
                             "Versão da composição ativa difere da versão da âncora de direção.",
                             {"active_version": active_version, "direction_version": direction_version})
        if phase == "PIVOT_EVALUATION" and isinstance(pivot, dict):
            if direction_id and pivot_source_id and direction_id != pivot_source_id:
                add_conflict("PIVOT_SOURCE_ANCHOR_MISMATCH",
                             "Candidata de pivot não referencia a âncora de direção vigente.",
                             {"direction_anchor": direction_id, "pivot_source_anchor": pivot_source_id})
            if direction_version is not None and pivot_source_version is not None and direction_version != pivot_source_version:
                add_conflict("PIVOT_SOURCE_VERSION_MISMATCH",
                             "Candidata de pivot foi avaliada contra uma versão obsoleta.",
                             {"direction_version": direction_version, "pivot_source_version": pivot_source_version})
        if phase == "PIVOT_CONFIRMED":
            if not active_id or not direction_comp or active_id != direction_comp:
                add_conflict("CONFIRMED_PIVOT_DIRECTION_NOT_SYNCHRONIZED",
                             "Pivot confirmado sem sincronização entre composição e âncora de direção.",
                             {"active_composition": active_id, "direction_composition": direction_comp})
            if active_version is not None and direction_version is not None and active_version != direction_version:
                add_conflict("CONFIRMED_PIVOT_VERSION_NOT_SYNCHRONIZED",
                             "Pivot confirmado com versões divergentes.",
                             {"active_version": active_version, "direction_version": direction_version})
            if pivot_target and active_id and str(pivot_target) != active_id:
                add_conflict("CONFIRMED_PIVOT_TARGET_MISMATCH",
                             "Composição confirmada não corresponde ao destino da candidata.",
                             {"pivot_target": pivot_target, "active_composition": active_id})
            transition = record.get("transition")
            transition_record = {
                "player_id": player, "round": round_id,
                "from": (transition or {}).get("from_composition_identity") if isinstance(transition, dict) else None,
                "to": (transition or {}).get("to_composition_identity") if isinstance(transition, dict) else active_id,
                "previous_version": (transition or {}).get("previous_version") if isinstance(transition, dict) else None,
                "new_version": (transition or {}).get("new_version") if isinstance(transition, dict) else active_version,
                "direction_anchor": direction_id,
            }
            transitions.append(transition_record)
            item["confirmed_transitions"].append(transition_record)

        if phase == "PIVOT_CONFIRMED" and pivot is not None:
            add_conflict("PIVOT_CANDIDATE_RETAINED_AFTER_CONFIRMATION",
                         "Candidata de pivot ainda está presente após a confirmação.",
                         {"pivot_candidate": pivot})

    duplicate_sequences = {
        player: sorted(value for value, count in Counter(values).items() if count > 1)
        for player, values in sequence_by_player.items()
    }
    out_of_order = {
        player: sum(1 for left, right in zip(values, values[1:]) if right < left)
        for player, values in sequence_by_player.items()
    }
    normalized_players = {}
    for player, value in per_player.items():
        normalized_players[player] = {
            **value,
            "rounds": sorted(value["rounds"]),
            "phase_counts": dict(value["phase_counts"]),
            "pivot_counts": dict(value["pivot_counts"]),
            "carry_gate_counts": dict(value["carry_gate_counts"]),
            "support_units": dict(value["support_units"]),
            "pivot_reason_counts": dict(value["pivot_reason_counts"]),
            "samples": value["samples"],
            "conflicts": value["conflicts"],
            "confirmed_transitions": value["confirmed_transitions"],
        }
    return {
        "record_count": len(records),
        "parse_errors": list(errors or []),
        "phase_counts": dict(phase_counts),
        "pivot_status_counts": dict(pivot_counts),
        "carry_gate_counts": dict(carry_gate_counts),
        "missing_data_counts": dict(missing_counts),
        "players": normalized_players,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
        "confirmed_transitions": transitions,
        "duplicate_sequences": duplicate_sequences,
        "out_of_order_sequences": out_of_order,
        "data_status": "AVAILABLE" if records else "NO_STRATEGIC_CYCLE_RECORDS",
        "interpretation": (
            "Auditoria observacional read-only. Ausência de campo é dado indisponível, "
            "não reprovação estratégica. Contagens repetidas são snapshots, não revisões independentes."
        ),
    }


def format_direction_pivot_audit(report: dict[str, Any], source_found: bool = True) -> str:
    lines = [
        "# Auditoria de direção estratégica e pivot",
        "",
        f"- Fonte: **{'encontrada' if source_found else 'não encontrada'}**",
        f"- Snapshots de ciclo: **{report['record_count']}**",
        f"- Estado dos dados: **{report['data_status']}**",
        f"- Conflitos de identidade/versão: **{report['conflict_count']}**",
        f"- Sequências duplicadas: **{report['duplicate_sequences'] or 'nenhuma'}**",
        f"- Sequências fora de ordem por jogador: **{sum(report['out_of_order_sequences'].values())}**",
        "",
    ]
    if not source_found or not report["record_count"]:
        lines.extend([
            "## Limitação de instrumentação",
            "",
            "Não há eventos da máquina unificada de direção/pivot nesta sessão. "
            "Os logs legados de composição/PPO não são usados para inventar âncoras, "
            "candidatas, critérios de carry ou confirmações. A ausência é reportada "
            "como indisponibilidade de dados, não como falha estratégica.",
            "",
        ])
    lines.extend(["## Fases observadas", "", "| Fase | Snapshots |", "|---|---:|"])
    lines.extend(f"| {phase} | {count} |" for phase, count in sorted(report["phase_counts"].items()))
    if not report["phase_counts"]:
        lines.append("| sem dados | 0 |")
    lines.extend(["", "## Avaliações de pivot", "", "| Resultado | Snapshots |", "|---|---:|"])
    lines.extend(f"| {status} | {count} |" for status, count in sorted(report["pivot_status_counts"].items()))
    if not report["pivot_status_counts"]:
        lines.append("| sem dados | 0 |")
    lines.extend(["", "## Motivos de avaliação", ""])
    reason_totals = Counter()
    for player_data in report["players"].values():
        reason_totals.update(player_data["pivot_reason_counts"])
    lines.extend(f"- {reason}: {count}" for reason, count in sorted(reason_totals.items()))
    if not reason_totals:
        lines.append("- Sem motivos de pivot disponíveis.")
    lines.extend(["", "## Critério de carry", "", "| Estado | Snapshots |", "|---|---:|"])
    lines.extend(f"| {status} | {count} |" for status, count in sorted(report["carry_gate_counts"].items()))
    lines.extend(["", "## Dados ausentes", ""])
    lines.extend(f"- {field}: {count}" for field, count in sorted(report["missing_data_counts"].items()))
    if not report["missing_data_counts"]:
        lines.append("- Nenhum campo ausente detectado nos registros fornecidos.")
    lines.extend(["", "## Amostras por jogador/round", "",
                  "| Jogador | Round | Fase | Composição ativa | Âncora de direção | Pivot | Carry | Loja (evidência) | Unidades (cópias/estrelas) | Motivo |",
                  "|---|---|---|---|---|---|---|---|---|---|"])
    for player, player_data in sorted(report["players"].items()):
        for sample in player_data["samples"]:
            active = sample["active_composition"]
            direction = sample["direction_anchor"]
            pivot_sample = sample["pivot_candidate"]
            carry_sample = sample["carry_gate"] or {}
            safe = lambda value: str(value if value is not None else "—").replace("|", "\\|")
            shop_text = ", ".join(
                f"{offer.get('champion_id', '?')} cost={offer.get('cost', '?')} copies={offer.get('copies', '?')}"
                for offer in (sample.get("shop_evidence") or []) if isinstance(offer, dict)
            ) or ("sem ofertas registradas" if sample["shop_evidence_count"] is not None else "indisponível")
            unit_text = ", ".join(
                f"{unit.get('champion_id', '?')}:{unit.get('relation', unit.get('classification', '?'))} "
                f"copies={unit.get('copies_owned', '?')}★{unit.get('highest_star', '?')}→{unit.get('target_star', '?')}★"
                for unit in (sample.get("unit_support") or []) if isinstance(unit, dict)
            ) or "indisponível"
            lines.append(
                f"| {player} | {safe(sample['round'])} | {sample['phase']} | "
                f"{safe(active['identity'])} v{safe(active['version'])} | "
                f"{safe(direction['identity'])} ({safe(direction['composition_identity'])} v{safe(direction['composition_version'])}) | "
                f"{safe(pivot_sample['identity'])} → {safe(pivot_sample['target'])} | "
                f"{safe(carry_sample.get('eligible'))}: {safe(carry_sample.get('reason'))} | "
                f"{safe(shop_text)} | {safe(unit_text)} | {safe(sample['pivot_reason'])} |"
            )
    if not any(value["samples"] for value in report["players"].values()):
        lines.append("| — | — | — | — | — | — | — | — | Sem snapshots |")
    lines.extend(["", "## Transições confirmadas", "",
                  "| Jogador | Round | Origem | Destino | Versão anterior → nova | Âncora final |",
                  "|---|---|---|---|---|---|"])
    for item in report["confirmed_transitions"]:
        lines.append(f"| {item['player_id']} | {item['round'] or '—'} | {item['from'] or '—'} | "
                     f"{item['to'] or '—'} | {item['previous_version'] or '—'} → "
                     f"{item['new_version'] or '—'} | {item['direction_anchor'] or '—'} |")
    if not report["confirmed_transitions"]:
        lines.append("| — | — | — | — | — | Nenhuma transição confirmada observada |")
    lines.extend(["", "## Conflitos detectados", "",
                  "| Jogador | Round | Fase | Código | Evidência |",
                  "|---|---|---|---|---|"])
    for item in report["conflicts"]:
        evidence = json.dumps(item["evidence"], ensure_ascii=False, sort_keys=True)
        safe_evidence = evidence.replace("|", "\\\\|")
        lines.append(f"| {item['player_id']} | {item['round'] or '—'} | {item['phase']} | "
                     f"{item['code']} | {safe_evidence} |")
    if not report["conflicts"]:
        lines.append("| — | — | — | Nenhum conflito observado | — |")
    lines.extend(["", "## Integridade dos dados", ""])
    lines.extend(f"- {error}" for error in report["parse_errors"])
    lines.extend([
        "",
        report["interpretation"],
        "A comparação com PPO é apenas contextual: PPO não é ground truth para direção ou pivot.",
        "",
    ])
    return "\n".join(lines)
