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
        match = re.fullmatch(r"\s*(\d+)\s*-\s*(\d+)\s*", str(value or ""))
        if not match:
            return None
        stage, round_in_stage = (int(part) for part in match.groups())
        if stage < 1 or round_in_stage < 1:
            return None
        if stage == 1:
            return round_in_stage
        return 5 + (stage - 2) * 7 + (round_in_stage - 1)


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


def _economic_controller_available(event: dict, composition: dict | None = None) -> bool:
    payload = event.get("economic_diagnostics")
    if isinstance(payload, dict) and payload:
        return True
    for state in (event.get("state_after"), event.get("state_before")):
        if isinstance(state, dict) and any(k in state for k in ("economic_controller", "economic_decision", "economic_diagnostics")):
            return True
    if composition:
        bridge = composition.get("context_bridge") or {}
        recommended = bridge.get("recommended") or {} if isinstance(bridge, dict) else {}
        posture = recommended.get("economic_posture") or {} if isinstance(recommended, dict) else {}
        if not isinstance(posture, dict):
            posture = {}
        quality = str(posture.get("quality") or "").lower()
        return posture.get("value") is not None and quality in ("valid", "partial")
    return False


def _recommendations(record: dict) -> dict[str, Any]:
    comparison = record.get("action_evaluator_comparison") or {}
    if not isinstance(comparison, dict):
        comparison = {}
    baseline = comparison.get("baseline") or {}
    contextual = comparison.get("contextual") or {}
    if not isinstance(baseline, dict):
        baseline = {}
    if not isinstance(contextual, dict):
        contextual = {}
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
    player_decisions: dict[tuple[str | None, int, int], list[dict]] = defaultdict(list)
    player_compositions: dict[tuple[str, int, int], list[dict]] = defaultdict(list)
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
    evaluator_comparison_count = 0
    evaluator_divergence_count = 0
    incompatible_schemas = []
    legacy_schema_count = 0

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
        event_match = event.get("match_id") or match_id
        event_sequence = event.get("sequence_id")
        if isinstance(event_sequence, int):
            event_key = (event_match, pid, event_sequence)
            if event_key in seen_player_event_keys:
                player_duplicate_count += 1
                continue
            seen_player_event_keys.add(event_key)
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
                "file": event.get("source_file") or f"player_{pid + 1}_log.json",
                "sequence_id": event.get("sequence_id"),
                "step": event.get("step"),
            },
            "step": event.get("step"),
            "timestamp": event.get("timestamp"),
            "action": action,
            "normalized_category": category,
            "strategy": event.get("strategy"),
            "strategy_reason": event.get("strategy_reason"),
            "source_payload": event.get("source_payload") or {
                "action": event.get("action"),
                "state_before": event.get("state_before"),
                "state_after": event.get("state_after"),
                "decision_context": event.get("decision_context"),
                "economic_diagnostics": event.get("economic_diagnostics"),
                "legal_action_audit": event.get("legal_action_audit"),
                "policy_diagnostics": event.get("policy_diagnostics"),
                "reward_components": event.get("reward_components"),
            },
        }
        shadow = _shadow(event)
        if shadow:
            decision["strategic_planner"] = shadow
            group["strategic_reviews"].append({
                "source": "shadow_planning",
                "composition_id": composition_id,
                "composition_version": composition_version,
                "sequence_id": event.get("sequence_id"),
                "source_reference": {"file": event.get("source_file") or f"player_{pid + 1}_log.json", "sequence_id": event.get("sequence_id")},
                "payload": shadow,
                "step": event.get("step"),
                "timestamp": event.get("timestamp"),
                "decision": shadow.get("strategic_decision_name"),
                "decision_path_reason": shadow.get("decision_path_reason"),
                "candidate_generation_reason": shadow.get("candidate_generation_reason"),
                "current_direction": state.get("comp_direction"),
                "target_direction": shadow.get("target_composition_direction"),
                "current_direction_score": shadow.get("current_direction_score"),
                "best_anchor_score": shadow.get("best_anchor_score"),
                "alternative_advantage": shadow.get("alternative_advantage"),
                "minimum_adapt_advantage": shadow.get("minimum_adapt_advantage"),
                "required_pivot_advantage": shadow.get("required_pivot_advantage"),
                "anchor_confidence": shadow.get("anchor_confidence"),
                "current_direction_confidence": shadow.get("current_direction_confidence"),
                "has_anchor_candidate": shadow.get("has_anchor_candidate"),
                "current_direction_viable": shadow.get("current_direction_viable"),
            })
            producer_counts["strategic_planner"] += 1
        group["ppo_actions"].append(decision)
        player_decisions[(event_match, pid, rnd)].append(event)
        producer_counts["ppo"] += 1
        if _economic_controller_available(event):
            economy = event.get("economic_diagnostics") or {}
            group["economic_observations"].append({
                "source": "structured_player_log",
                "sequence_id": event.get("sequence_id"),
                "step": event.get("step"),
                "timestamp": event.get("timestamp"),
                "observed": economy,
            })
            producer_counts["economic_controller"] += 1

    for record in composition_records or []:
        if not isinstance(record, dict):
            continue
        corr = record.get("correlation") if isinstance(record.get("correlation"), dict) else {}
        record_match = record.get("match_id") or corr.get("match_id")
        raw_player_id = record.get("player_id")
        raw_round = record.get("round")
        sequence = record.get("sequence")
        pid = _player_id(raw_player_id if raw_player_id is not None else corr.get("player_id"))
        rnd = _round(raw_round if raw_round is not None else corr.get("round"))
        sequence = sequence if sequence is not None else corr.get("sequence_id")
        schema = record.get("schema_version")
        if schema is None:
            legacy_schema_count += 1
        elif schema not in (1, 2):
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
        evaluator_comparison = record.get("action_evaluator_comparison") or {}
        evaluator_comparison_meta = evaluator_comparison.get("comparison") or {}
        if evaluator_comparison_meta.get("comparison_available"):
            evaluator_comparison_count += 1
            if evaluator_comparison_meta.get("diverged") is True:
                evaluator_divergence_count += 1
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
            "source_payload": record,
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
        player_compositions[(str(record_match), pid, rnd)].append(record)
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
                "composition_id": record.get("composition_id"),
                "composition_version": record.get("composition_version"),
                "sequence": sequence,
                "source_reference": {"file": "composition_diagnostics.jsonl", "sequence": sequence},
                "payload": strategic_value,
                "decision": strategic_value.get("value"),
                "quality": strategic_value.get("quality"),
                "origin": strategic_value.get("origin"),
            })
        if _economic_controller_available({}, record):
            producer_counts["economic_controller"] += 1
            group["economic_observations"].append({
                "source": "context_bridge",
                "sequence": sequence,
                "posture": economic_value.get("value"),
                "quality": economic_value.get("quality"),
                "origin": economic_value.get("origin"),
            })
        diagnostics = record.get("diagnostics") or {}
        if "unit_intentions" in diagnostics:
            producer_counts["unit_priority"] += 1
        if isinstance(diagnostics.get("lineup_plan"), dict):
            producer_counts["lineup"] += 1
        evidence = diagnostics.get("evidence") or {}
        for domain in ("economy", "board", "items"):
            domain_evidence = evidence.get(domain) or {}
            metadata = domain_evidence.get("metadata") or {} if isinstance(domain_evidence, dict) else {}
            if not isinstance(metadata, dict) or not metadata:
                continue
            producer_counts[f"{domain}_evidence_records"] += 1
            evidence_key = "item_evidence" if domain == "items" else f"{domain}_evidence"
            producer_counts[evidence_key] += 1
            quality_name = str(metadata.get("quality_name") or "").lower()
            is_valid = metadata.get("available") is True and (
                quality_name == "valid" or (not quality_name and metadata.get("quality") == 2)
            )
            if is_valid:
                producer_counts[f"{domain}_evidence_valid"] += 1
                valid_key = "item_evidence_valid" if domain == "items" else f"{domain}_evidence_valid"
                producer_counts[valid_key] += 1
            if domain == "economy":
                group["economic_observations"].append({
                    "source": "planner_evidence",
                    "sequence": sequence,
                    "quality": metadata.get("quality_name") or metadata.get("quality"),
                    "available": metadata.get("available"),
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
            "source_reference": {
                "file": outcome.get("source_file") or f"player_{pid + 1}_log.json",
                "sequence_id": outcome.get("sequence_id"),
                "step": outcome.get("step"),
            },
            "step": outcome.get("step"),
            "sequence_id": outcome.get("sequence_id"),
            "placement": outcome.get("placement"),
            "combat_reward": outcome.get("combat_reward"),
            "reward": outcome.get("reward"),
            "source_payload": outcome.get("source_payload") or {
                "state_after": outcome.get("state_after"),
                "combat_reward": outcome.get("combat_reward"),
                "reward": outcome.get("reward"),
                "placement": outcome.get("placement"),
            },
            "interpretation": "correlation_only_not_causation",
        })
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
                observation.get("composition_id"),
                observation.get("composition_version"),
                observation.get("decision"),
                observation.get("decision_path_reason"),
                observation.get("candidate_generation_reason"),
                observation.get("current_direction"),
                observation.get("target_direction"),
                observation.get("current_direction_score"),
                observation.get("best_anchor_score"),
                observation.get("alternative_advantage"),
                observation.get("minimum_adapt_advantage"),
                observation.get("required_pivot_advantage"),
                observation.get("anchor_confidence"),
                observation.get("current_direction_confidence"),
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

    sequence_gap_report = []
    for sequence_match, values in sorted(global_sequences_by_match.items()):
        missing = sorted(set(range(1, max(values) + 1)) - set(values)) if values else []
        if missing:
            sequence_gap_report.append({
                "match_id": sequence_match, "count": len(missing), "missing": missing[:100],
            })

    players = sorted({group["player_id"] for group in groups.values()})
    source_presence = {
        "strategic_planner": producer_counts["strategic_planner"] > 0,
        "economic_controller": producer_counts["economic_controller"] > 0,
        "economy_evidence": producer_counts["economy_evidence_records"] > 0,
        "economy_evidence_valid": producer_counts["economy_evidence_valid"] > 0,
        "board_evidence": producer_counts["board_evidence_records"] > 0,
        "board_evidence_valid": producer_counts["board_evidence_valid"] > 0,
        "item_evidence": producer_counts["item_evidence"] > 0,
        "item_evidence_valid": producer_counts["item_evidence_valid"] > 0,
        "unit_priority": producer_counts["unit_priority"] > 0,
        "lineup": producer_counts["lineup"] > 0,
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
        "evaluator_comparison_count": evaluator_comparison_count,
        "evaluator_divergence_count": evaluator_divergence_count,
        "duplicate_sequences": duplicate_sequences[:100],
        "out_of_order_sequences": out_of_order_sequences[:100],
        "sequence_gaps": sequence_gap_report,
        "incompatible_schemas": incompatible_schemas[:100],
        "legacy_schema_count": legacy_schema_count,
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
        ("economic_controller", "Economic Controller"),
        ("economy_evidence", "Economy evidence records"),
        ("economy_evidence_valid", "Economy evidence valid"),
        ("board_evidence", "Board evidence records"),
        ("board_evidence_valid", "Board evidence valid"),
        ("item_evidence", "Item evidence records"),
        ("item_evidence_valid", "Item evidence valid"),
        ("unit_priority", "Unit Priority"),
        ("lineup", "Lineup Planner"),
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
        f"- Lacunas de sequência: {sum(item.get('count', 0) for item in index.get('sequence_gaps', []))}",
        f"- Eventos duplicados no log de jogadores: {index.get('player_log_duplicate_count', 0)}",
        f"- Comparações baseline/contextual disponíveis: {index.get('evaluator_comparison_count', 0)}",
        f"- Divergências baseline/contextual: {index.get('evaluator_divergence_count', 0)}",
        f"- Registros sem versão (legado): {index.get('legacy_schema_count', 0)}",
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
        versions = ", ".join(
            f"{item.get('composition_id') or 'unavailable'}@{item.get('composition_version') if item.get('composition_version') is not None else 'unavailable'}"
            for item in group.get("composition_versions", [])
        ) or "unavailable"
        lines.append(
            f"- Strategic reviews únicos: {group['strategic_review_count']} "
            f"(observações={group['strategic_review_observations']}) · "
            f"PPO actions: {group['ppo_action_count']} · "
            f"Composition snapshots: {group['composition_snapshot_count']} · "
            f"Outcomes: {group['outcome_count']}"
        )
        lines.append(f"- Composition identity/version: {versions}")
        for decision in group["strategic_reviews"][:10]:
            lines.append(
                f"- Strategic Planner [{decision.get('source')} seq={decision.get('sequence_id', decision.get('sequence', '—'))}]: "
                f"{decision.get('decision') or 'unavailable'} "
                f"({decision.get('decision_path_reason') or 'reason unavailable'})"
            )
        for recommendation in group["action_evaluator_recommendations"][-3:]:
            lines.append(
                f"- Evaluators [composition_diagnostics.jsonl seq={recommendation.get('sequence', '—')}]: "
                f"baseline={((recommendation.get('baseline') or {}).get('category') or 'unavailable')} · "
                f"contextual={((recommendation.get('contextual') or {}).get('category') or 'unavailable')}"
            )
        for action in group["ppo_actions"][-5:]:
            lines.append(
                f"- PPO observado [{(action.get('source_reference') or {}).get('file')} "
                f"seq={(action.get('source_reference') or {}).get('sequence_id')}]: "
                f"{action.get('action')} → {action.get('normalized_category') or 'unavailable'}"
            )
        for outcome in group["outcomes"]:
            lines.append(f"- Outcome observado: placement={outcome.get('placement')} (correlação, não causalidade)")
        lines.append("")
    lines += ["## Limitações explícitas", ""]
    lines.extend(f"- {item}" for item in index.get("limitations", []))
    return "\n".join(lines) + "\n"
