"""Versioned, read-only correlation index across legacy and Composition Intelligence audits."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from typing import Any
import re


INDEX_SCHEMA_VERSION = 1
ACTION_KIND_NAMES = {
    0: "NONE", 1: "BUY_UNIT", 2: "BUY_XP", 3: "REROLL",
    4: "SELL", 5: "MOVE", 6: "HOLD",
}
PPO_ACTION_CATEGORIES = {
    "BUY": "BUY_UNIT", "REROLL": "REROLL", "BUY_XP": "BUY_XP",
    "MOVE_BENCH": "MOVE", "MOVE_BOARD": "MOVE", "SELL": "SELL",
    "PASS": "HOLD",
}


def _player_id(value: Any) -> int | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    match = re.search(r"(?:Jogador\s*)?(\d+)", str(value or ""), re.IGNORECASE)
    if not match:
        return None
    number = int(match.group(1))
    return number - 1 if "jogador" in str(value).casefold() else number


def _round(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _timestamp_ms(value: Any) -> int | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return int(value)
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return int(parsed.timestamp() * 1000)
    except (ValueError, OverflowError):
        return None


def _state(event: dict) -> dict:
    return event.get("state_after") or event.get("state_before") or {}


def _shadow(event: dict) -> dict | None:
    for candidate in (event.get("state_after"), event.get("state_before")):
        if isinstance(candidate, dict):
            value = candidate.get("shadow_planning")
            if isinstance(value, dict) and value:
                return value
    return None


def _economy_available(event: dict, composition: dict | None = None) -> bool:
    payload = event.get("economic_diagnostics")
    if isinstance(payload, dict) and payload:
        return True
    for state in (event.get("state_after"), event.get("state_before")):
        if isinstance(state, dict) and any(k in state for k in ("economic_controller", "economic_decision", "economic_diagnostics")):
            return True
    if composition:
        bridge = composition.get("context_bridge") or {}
        recommended = bridge.get("recommended") or {} if isinstance(bridge, dict) else {}
        posture = recommended.get("economic_posture") or {}
        if isinstance(posture, dict) and posture.get("value") is not None and posture.get("quality") in ("valid", "partial"):
            return True
        diagnostics = composition.get("diagnostics") or {}
        evidence = diagnostics.get("evidence") or {}
        return bool((evidence.get("economy") or {}).get("metadata", {}).get("available"))
    return False


def _recommendations(record: dict) -> dict[str, Any]:
    comparison = record.get("action_evaluator_comparison") or {}
    baseline = comparison.get("baseline") or {}
    contextual = comparison.get("contextual") or {}
    if not baseline:
        old = (record.get("diagnostics") or {}).get("action_recommendation") or {}
        if old:
            baseline = {
                "recommended_action": old.get("recommended_action"),
                "recommended_champion_id": old.get("recommended_champion_id"),
                "stale": old.get("stale", False),
            }
    result = {}
    for source, item in (("baseline", baseline), ("contextual", contextual)):
        if not item:
            result[source] = None
            continue
        raw = item.get("recommended_action")
        try:
            category = ACTION_KIND_NAMES.get(int(raw))
        except (TypeError, ValueError):
            category = None
        result[source] = {
            "category": category,
            "raw_action": raw,
            "champion_id": item.get("recommended_champion_id"),
            "stale": bool(item.get("stale", False)),
            "available": not bool(item.get("stale", False)) and category not in (None, "NONE"),
        }
    return result


def build_integrated_audit_index(
    decision_timeline: list[dict],
    outcome_timeline: list[dict],
    composition_records: list[dict],
    composition_errors: list[str] | None = None,
    *,
    match_id: str | None = None,
) -> dict:
    """Correlate only by explicit session/player/round identity; never infer missing data."""
    errors = list(composition_errors or [])
    groups: dict[tuple, dict] = {}
    player_decisions: dict[tuple[int, int], list[dict]] = defaultdict(list)
    player_compositions: dict[tuple[int, int], list[dict]] = defaultdict(list)
    player_outcomes: dict[tuple[int, int], list[dict]] = defaultdict(list)
    producer_counts: Counter[str] = Counter()
    missing_envelope = []
    duplicate_sequences = []
    out_of_order_sequences = []
    sequence_by_player: dict[tuple[str | None, int], list[int]] = defaultdict(list)
    seen_comp_keys: set[tuple] = set()
    seen_player_event_keys: set[tuple] = set()
    player_duplicate_count = 0
    global_sequences_by_match: dict[str, list[int]] = defaultdict(list)
    duplicate_comp_count = 0
    incompatible_schemas = []

    def group_for(pid: int, rnd: int, source_match: str | None = None) -> dict:
        resolved_match = source_match if source_match is not None else match_id
        key = (resolved_match, pid, rnd)
        return groups.setdefault(key, {
            "match_id": resolved_match, "player_id": pid, "round": rnd,
            "correlation_key": {"match_id": resolved_match, "player_id": pid, "round": rnd},
            "strategic_reviews": [], "strategic_review_observations": 0,
            "economic_observations": [], "ppo_actions": [], "composition_snapshots": [],
            "composition_versions": [], "action_evaluator_recommendations": [], "outcomes": [],
            "correlation_semantics": "same_match_player_round_association_not_causality",
        })

    for event in decision_timeline or []:
        if not isinstance(event, dict):
            continue
        pid = _player_id(event.get("player_id", event.get("player")))
        rnd = _round(event.get("round"))
        if pid is None or rnd is None:
            continue
        event_sequence = event.get("sequence_id")
        if isinstance(event_sequence, int):
            event_key = (pid, event_sequence)
            if event_key in seen_player_event_keys:
                player_duplicate_count += 1
                continue
            seen_player_event_keys.add(event_key)
        event_match = event.get("match_id") or match_id
        group = group_for(pid, rnd, event_match)
        action = str(event.get("action_name") or event.get("raw_action") or "UNKNOWN").upper()
        category = PPO_ACTION_CATEGORIES.get(action)
        state = _state(event)
        composition_id = state.get("active_composition_id") or state.get("composition_id")
        composition_version = state.get("active_composition_version", state.get("composition_version"))
        composition_state = state.get("composition") if isinstance(state.get("composition"), dict) else {}
        composition_id = composition_id or composition_state.get("composition_id")
        composition_version = composition_version if composition_version is not None else composition_state.get("composition_version")
        decision = {
            "source": "structured_player_log",
            "sequence_id": event.get("sequence_id"),
            "composition_id": composition_id,
            "composition_version": composition_version,
            "source_reference": {
                "file": f"player_{pid + 1}_log.json",
                "sequence_id": event.get("sequence_id"),
                "step": event.get("step"),
            },
            "step": event.get("step"),
            "timestamp": event.get("timestamp"),
            "action": action,
            "normalized_category": category,
            "strategy": event.get("strategy"),
            "strategy_reason": event.get("strategy_reason"),
        }
        shadow = _shadow(event)
        if shadow:
            decision["strategic_planner"] = shadow
            group["strategic_reviews"].append({
                "source": "shadow_planning",
                "sequence_id": event.get("sequence_id"),
                "step": event.get("step"),
                "timestamp": event.get("timestamp"),
                "decision": shadow.get("strategic_decision_name"),
                "decision_path_reason": shadow.get("decision_path_reason"),
                "candidate_generation_reason": shadow.get("candidate_generation_reason"),
                "has_anchor_candidate": shadow.get("has_anchor_candidate"),
                "current_direction_viable": shadow.get("current_direction_viable"),
            })
            producer_counts["strategic_planner"] += 1
        group["ppo_actions"].append(decision)
        player_decisions[(event_match, pid, rnd)].append(event)
        producer_counts["ppo"] += 1
        if _economy_available(event):
            economy = event.get("economic_diagnostics") or event.get("decision_context") or {}
            group["economic_observations"].append({
                "source": "structured_player_log",
                "sequence_id": event.get("sequence_id"),
                "step": event.get("step"),
                "timestamp": event.get("timestamp"),
                "observed": economy,
            })
            producer_counts["economy_observations"] += 1

    for record in composition_records or []:
        if not isinstance(record, dict):
            continue
        corr = record.get("correlation") if isinstance(record.get("correlation"), dict) else {}
        record_match = record.get("match_id") or corr.get("match_id")
        pid = _player_id(record.get("player_id", corr.get("player_id")))
        rnd = _round(record.get("round", corr.get("round")))
        sequence = record.get("sequence", corr.get("sequence_id"))
        schema = record.get("schema_version")
        if schema not in (1, 2):
            incompatible_schemas.append({"schema_version": schema, "sequence": sequence, "player_id": pid})
        if pid is None or rnd is None or not record_match:
            missing_envelope.append({
                "sequence": sequence, "player_id": pid, "round": rnd,
                "missing": [name for name, value in (
                    ("match_id", record_match), ("player_id", pid), ("round", rnd)
                ) if value is None],
            })
            continue
        # Records from another match are never joined into this session.
        if match_id and str(record_match) != str(match_id):
            continue
        if isinstance(sequence, int):
            key = (str(record_match), sequence)
            if key in seen_comp_keys:
                duplicate_comp_count += 1
                duplicate_sequences.append({"player_id": pid, "sequence": sequence})
                continue
            seen_comp_keys.add(key)
            sequence_by_player[(str(record_match), pid)].append(sequence)
            global_sequences_by_match[str(record_match)].append(sequence)
        group = group_for(pid, rnd, str(record_match))
        recommendations = _recommendations(record)
        item = {
            "source": "composition_intelligence",
            "source_reference": {"file": "composition_diagnostics.jsonl", "sequence": sequence},
            "schema_version": schema,
            "sequence": sequence,
            "timestamp_unix_ms": record.get("timestamp_unix_ms", corr.get("timestamp_unix_ms")),
            "composition_id": record.get("composition_id"),
            "composition_version": record.get("composition_version"),
            "stale": bool(record.get("stale", False)),
            "stale_reason": record.get("stale_reason"),
            "action_evaluator_comparison": record.get("action_evaluator_comparison"),
            "recommendations": recommendations,
            "context_bridge": record.get("context_bridge"),
            "diagnostics": record.get("diagnostics"),
        }
        group["composition_snapshots"].append(item)
        identity = {
            "composition_id": item["composition_id"],
            "composition_version": item["composition_version"],
        }
        if identity not in group["composition_versions"]:
            group["composition_versions"].append(identity)
        group["action_evaluator_recommendations"].append({
            "sequence": sequence, "composition_version": item["composition_version"],
            **recommendations,
        })
        player_compositions[(pid, rnd)].append(record)
        producer_counts["composition_intelligence"] += 1
        if recommendations["baseline"] is not None:
            producer_counts["action_evaluator_baseline"] += 1
        if recommendations["contextual"] is not None:
            producer_counts["contextual_action_evaluator"] += 1
        bridge = record.get("context_bridge") or {}
        recommended_bridge = bridge.get("recommended") or {} if isinstance(bridge, dict) else {}
        strategic_value = recommended_bridge.get("composition_decision") or {}
        economic_value = recommended_bridge.get("economic_posture") or {}
        if isinstance(strategic_value, dict) and strategic_value.get("value") is not None:
            producer_counts["strategic_planner"] += 1
            group["strategic_reviews"].append({
                "source": "context_bridge",
                "sequence": sequence,
                "decision": strategic_value.get("value"),
                "quality": strategic_value.get("quality"),
                "origin": strategic_value.get("origin"),
            })
        if _economy_available({}, record):
            producer_counts["economy_evidence"] += 1
            group["economic_observations"].append({
                "source": "context_bridge",
                "sequence": sequence,
                "posture": economic_value.get("value"),
                "quality": economic_value.get("quality"),
                "origin": economic_value.get("origin"),
            })

    for (sequence_match, pid), sequences in sequence_by_player.items():
        for left, right in zip(sequences, sequences[1:]):
            if right < left:
                out_of_order_sequences.append({
                    "match_id": sequence_match, "player_id": pid,
                    "previous": left, "current": right,
                })

    for outcome in outcome_timeline or []:
        if not isinstance(outcome, dict):
            continue
        pid = _player_id(outcome.get("player"))
        rnd = _round(outcome.get("round"))
        if pid is None or rnd is None:
            continue
        outcome_match = outcome.get("match_id") or match_id
        group = group_for(pid, rnd, outcome_match)
        group["outcomes"].append({
            "source": "round_outcome_timeline",
            "step": outcome.get("step"),
            "sequence_id": outcome.get("sequence_id"),
            "placement": outcome.get("placement"),
            "combat_reward": outcome.get("combat_reward"),
            "reward": outcome.get("reward"),
            "interpretation": "correlation_only_not_causation",
        })
        player_outcomes[(outcome_match, pid, rnd)].append(outcome)
        producer_counts["outcomes"] += 1

    comparison = {
        "baseline": {"compared": 0, "matches": 0, "divergences": 0, "unavailable": 0},
        "contextual": {"compared": 0, "matches": 0, "divergences": 0, "unavailable": 0},
        "method": "nearest timestamp within same player/round and at most 30 seconds; otherwise unavailable",
        "policy_action_is_not_ground_truth": True,
    }
    for key, events in player_decisions.items():
        event_match, pid, rnd = key
        snapshots = player_compositions.get(key, [])
        usable = []
        for record in snapshots:
            rec_time = _timestamp_ms(record.get("timestamp_unix_ms"))
            if rec_time is None:
                corr = record.get("correlation") or {}
                rec_time = _timestamp_ms(corr.get("timestamp_unix_ms"))
            if rec_time is None:
                rec_time = _timestamp_ms(record.get("timestamp"))
            if rec_time is not None:
                usable.append((rec_time, record))
        for event in events:
            event_time = _timestamp_ms(event.get("timestamp"))
            action = str(event.get("action_name") or event.get("raw_action") or "UNKNOWN").upper()
            actual = PPO_ACTION_CATEGORIES.get(action)
            event_comp_id = event.get("composition_id")
            event_comp_version = event.get("composition_version")
            eligible_snapshots = [
                pair for pair in usable
                if (event_comp_id is None or pair[1].get("composition_id") == event_comp_id)
                and (event_comp_version is None or pair[1].get("composition_version") == event_comp_version)
            ]
            if event_time is None or not eligible_snapshots:
                comparison["baseline"]["unavailable"] += 1
                comparison["contextual"]["unavailable"] += 1
                continue
            nearest_time, record = min(eligible_snapshots, key=lambda pair: abs(pair[0] - event_time))
            if abs(nearest_time - event_time) > 30_000:
                comparison["baseline"]["unavailable"] += 1
                comparison["contextual"]["unavailable"] += 1
                continue
            recommendations = _recommendations(record)
            for source in ("baseline", "contextual"):
                recommendation = recommendations[source]
                if actual is None or recommendation is None or not recommendation.get("available"):
                    comparison[source]["unavailable"] += 1
                    continue
                comparison[source]["compared"] += 1
                if actual == recommendation["category"]:
                    comparison[source]["matches"] += 1
                else:
                    comparison[source]["divergences"] += 1

    for group in groups.values():
        observations = group["strategic_reviews"]
        unique_reviews = {}
        for observation in observations:
            key = (
                observation.get("source"),
                observation.get("decision"),
                observation.get("decision_path_reason"),
                observation.get("candidate_generation_reason"),
                observation.get("has_anchor_candidate"),
                observation.get("current_direction_viable"),
                observation.get("origin"),
                observation.get("quality"),
            )
            if key not in unique_reviews:
                unique_reviews[key] = {**observation, "observations": 0}
            unique_reviews[key]["observations"] += 1
        group["strategic_review_observations"] = len(observations)
        group["strategic_reviews"] = list(unique_reviews.values())
        group["strategic_review_count"] = len(group["strategic_reviews"])
        group["composition_versions"].sort(
            key=lambda item: (str(item.get("composition_id")), item.get("composition_version") or 0)
        )
        group["ppo_action_count"] = len(group["ppo_actions"])
        group["composition_snapshot_count"] = len(group["composition_snapshots"])
        group["outcome_count"] = len(group["outcomes"])
        group["correlated"] = bool(group["composition_snapshots"] and group["ppo_actions"])
        group["correlation_quality"] = (
            "same_player_round" if group["correlated"] else "partial_or_unavailable"
        )

    players = sorted({group["player_id"] for group in groups.values()})
    source_presence = {
        "strategic_planner": producer_counts["strategic_planner"] > 0,
        "economy_observations": producer_counts["economy_observations"] > 0 or producer_counts["economy_evidence"] > 0,
        "composition_intelligence": producer_counts["composition_intelligence"] > 0,
        "action_evaluator_baseline": producer_counts["action_evaluator_baseline"] > 0,
        "contextual_action_evaluator": producer_counts["contextual_action_evaluator"] > 0,
        "ppo": producer_counts["ppo"] > 0,
        "outcomes": producer_counts["outcomes"] > 0,
    }
    missing_producers = [name for name, present in source_presence.items() if not present]
    index_groups = sorted(groups.values(), key=lambda x: (x["player_id"], x["round"]))
    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "match_id": match_id,
        "group_count": len(index_groups),
        "players": players,
        "groups": index_groups,
        "producer_counts": dict(producer_counts),
        "source_presence": source_presence,
        "missing_producers": missing_producers,
        "composition_envelope_missing_count": len(missing_envelope),
        "composition_envelope_missing": missing_envelope[:100],
        "composition_duplicate_count": duplicate_comp_count,
        "player_log_duplicate_count": player_duplicate_count,
        "duplicate_sequences": duplicate_sequences[:100],
        "out_of_order_sequences": out_of_order_sequences[:100],
        "sequence_gaps": [
            {"match_id": sequence_match, "missing": sorted(
                set(range(min(values), max(values) + 1)) - set(values)
            )[:100]}
            for sequence_match, values in sorted(global_sequences_by_match.items())
            if values and set(range(min(values), max(values) + 1)) - set(values)
        ],
        "incompatible_schemas": incompatible_schemas[:100],
        "parse_errors": errors,
        "recommendation_vs_ppo": comparison,
        "limitations": [
            "Associação por match/player/round não demonstra causalidade.",
            "Comparação com PPO usa a ação observada no log e a recomendação temporalmente mais próxima no mesmo jogador/round.",
            "Ação PPO não é ground truth; concordância não é métrica de qualidade.",
            "Snapshots sem identidade ou timestamp suficiente permanecem unavailable e não são reconstruídos.",
            "Sessões antigas podem não conter o envelope completo; são preservadas como dados legados não correlacionáveis.",
            "Fontes ausentes, stale, partial ou invalid não são convertidas em zero nem substituídas por decisões artificiais.",
        ],
    }


def format_integrated_audit_markdown(index: dict) -> str:
    counts = index.get("producer_counts", {})
    lines = [
        "# Índice integrado de auditoria",
        "",
        f"- Schema do índice: v{index.get('schema_version')}",
        f"- Match: {index.get('match_id') or 'unavailable'}",
        f"- Jogadores: {', '.join(str(p + 1) for p in index.get('players', [])) or 'nenhum'}",
        f"- Grupos jogador/round: {index.get('group_count', 0)}",
        "",
        "## Integridade dos produtores",
        "",
        "| Produtor | Registros | Disponível |",
        "|---|---:|---|",
    ]
    mapping = (
        ("strategic_planner", "Strategic Planner"),
        ("economy_observations", "Economy"),
        ("composition_intelligence", "Composition Intelligence"),
        ("action_evaluator_baseline", "Action Evaluator baseline"),
        ("contextual_action_evaluator", "Contextual Action Evaluator"),
        ("ppo", "Ações PPO observadas"),
        ("outcomes", "Outcomes"),
    )
    for key, label in mapping:
        lines.append(f"| {label} | {counts.get(key, 0)} | {'sim' if index.get('source_presence', {}).get(key) else 'unavailable'} |")
    lines += [
        "",
        "## Integridade do stream",
        "",
        f"- Envelopes de composição incompletos: {index.get('composition_envelope_missing_count', 0)}",
        f"- Sequências duplicadas: {index.get('composition_duplicate_count', 0)}",
        f"- Inversões de sequência: {len(index.get('out_of_order_sequences', []))}",
        f"- Lacunas de sequência: {len(index.get('sequence_gaps', []))}",
        f"- Eventos duplicados no log de jogadores: {index.get('player_log_duplicate_count', 0)}",
        f"- Schemas incompatíveis: {len(index.get('incompatible_schemas', []))}",
        f"- Erros de parsing: {len(index.get('parse_errors', []))}",
        "",
        "## Comparação observacional com PPO",
        "",
        "| Evaluator | Comparáveis | Concordâncias | Divergências | Indisponíveis |",
        "|---|---:|---:|---:|---:|",
    ]
    for key, label in (("baseline", "Baseline"), ("contextual", "Contextual")):
        data = index.get("recommendation_vs_ppo", {}).get(key, {})
        lines.append(
            f"| {label} | {data.get('compared', 0)} | {data.get('matches', 0)} | "
            f"{data.get('divergences', 0)} | {data.get('unavailable', 0)} |"
        )
    lines += ["", "## Timeline correlacionada", ""]
    for group in index.get("groups", []):
        lines.append(
            f"### Jogador {group['player_id'] + 1} · round {group['round']} "
            f"({group['correlation_quality']})"
        )
        lines.append(
            f"- Strategic reviews: {group['strategic_review_count']} · "
            f"PPO actions: {group['ppo_action_count']} · "
            f"Composition snapshots: {group['composition_snapshot_count']} · "
            f"Outcomes: {group['outcome_count']}"
        )
        for decision in group["strategic_reviews"][:10]:
            lines.append(
                f"- Strategic Planner: {decision.get('decision') or 'unavailable'} "
                f"({decision.get('decision_path_reason') or 'reason unavailable'})"
            )
        for recommendation in group["action_evaluator_recommendations"][-3:]:
            lines.append(
                f"- Evaluators: baseline={((recommendation.get('baseline') or {}).get('category') or 'unavailable')} · "
                f"contextual={((recommendation.get('contextual') or {}).get('category') or 'unavailable')}"
            )
        for action in group["ppo_actions"][-5:]:
            lines.append(f"- PPO observado: {action.get('action')} → {action.get('normalized_category') or 'unavailable'}")
        for outcome in group["outcomes"]:
            lines.append(f"- Outcome observado: placement={outcome.get('placement')} (correlação, não causalidade)")
        lines.append("")
    lines += ["## Limitações explícitas", ""]
    lines.extend(f"- {item}" for item in index.get("limitations", []))
    return "\n".join(lines) + "\n"
