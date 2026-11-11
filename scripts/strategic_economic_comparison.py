"""Shadow-decision comparison and outcome Markdown reports for Viewer audits.

The module consumes the structured audit timeline only. Missing diagnostics remain
explicitly unavailable; heuristic recommendations are never treated as PPO actions.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
import json
from pathlib import Path
from typing import Any

ACTION_ALIASES = {
    "BUY": "BUY_UNIT", "BUY_UNIT": "BUY_UNIT",
    "BUY_XP": "BUY_EXPERIENCE", "BUY_EXPERIENCE": "BUY_EXPERIENCE",
    "REROLL": "REROLL_SHOP", "REROLL_SHOP": "REROLL_SHOP",
    "SELL": "SELL_UNIT", "SELL_UNIT": "SELL_UNIT",
    "MOVE_BENCH": "DEPLOY_OR_MOVE", "MOVE_BOARD": "DEPLOY_OR_MOVE",
    "DEPLOY_OR_MOVE": "DEPLOY_OR_MOVE",
    "PASS": "HOLD", "HOLD": "HOLD",
}


def classify_candidate_selection(candidate_count: int, selected_ids: list, recommended_id: Any) -> str:
    """Classify selection integrity without treating an empty initial state as a failure."""
    selected_count = len(selected_ids)
    if candidate_count == 0 and selected_count == 0:
        return "NOT_APPLICABLE"
    if candidate_count == 0 and selected_count > 0:
        return "INCONSISTENT"
    if selected_count == 0 or recommended_id is None:
        return "INCOMPLETE"
    return "CONSISTENT" if selected_ids == [recommended_id] else "INCONSISTENT"


def _cell(value: Any) -> str:
    if value is None or value == "":
        return "—"
    if isinstance(value, float):
        return f"{value:.3f}"
    if isinstance(value, (dict, list, tuple)):
        value = ", ".join(map(str, value)) if isinstance(value, (list, tuple)) else "; ".join(
            f"{key}={item}" for key, item in value.items()
        )
    return str(value).replace("|", r"\|").replace("\n", " ").replace("\r", " ")


def _shadow(decision: dict) -> dict:
    before = decision.get("state_before") or {}
    value = before.get("shadow_planning")
    if not isinstance(value, dict):
        return {}
    return value if any(item is not None for item in value.values()) else {}



@lru_cache(maxsize=1)
def _champion_catalog_aliases() -> dict[str, set[str]]:
    """Map native ChampionCatalog indices to the textual keys in Viewer snapshots."""
    catalog_path = Path(__file__).resolve().parents[1] / "data" / "units_gerado.json"
    try:
        definitions = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(definitions, list):
        return {}
    aliases = {}
    for internal_id, definition in enumerate(definitions):
        if not isinstance(definition, dict):
            continue
        values = {
            str(definition.get(key)).strip()
            for key in ("apiName", "characterName")
            if definition.get(key) not in (None, "")
        }
        if values:
            aliases[str(internal_id)] = values
    return aliases


def _strategic_unit_evidence(state: dict, shadow: dict) -> list[dict]:
    """Audit alignment and investment using native IDs and Viewer catalog keys."""
    state = state if isinstance(state, dict) else {}
    shadow = shadow if isinstance(shadow, dict) else {}
    catalog_aliases = _champion_catalog_aliases()

    def expand_ids(values) -> set[str]:
        expanded = set()
        for value in values or []:
            token = str(value).strip()
            if token:
                expanded.add(token)
                expanded.update(catalog_aliases.get(token, set()))
        return expanded

    preserved = expand_ids(shadow.get("strategic_preserve_unit_ids"))
    replaceable = expand_ids(shadow.get("strategic_replaceable_unit_ids"))
    core_ids = expand_ids(state.get("core_units"))
    core_traits = {str(value).casefold() for value in (state.get("core_traits") or [])}
    direction = str(state.get("comp_direction") or "").casefold()

    def unit_aliases(unit: dict) -> set[str]:
        values = {
            str(unit.get(key)).strip()
            for key in ("champion_id", "apiName", "api_name", "characterName")
            if unit.get(key) not in (None, "")
        }
        expanded = set(values)
        for value in values:
            expanded.update(catalog_aliases.get(value, set()))
        return expanded

    owned = [unit for area in ("board", "bench") for unit in (state.get(area) or [])
             if isinstance(unit, dict) and unit.get("occupied", True)]
    counts = Counter(
        next(iter(sorted(unit_aliases(unit))), "")
        for unit in owned
    )
    result = []
    for area in ("board", "bench"):
        for unit in state.get(area) or []:
            if not isinstance(unit, dict) or not unit.get("occupied", True):
                continue
            aliases = unit_aliases(unit)
            is_preserved = bool(aliases & preserved)
            is_replaceable = bool(aliases & replaceable)
            if not is_preserved and not is_replaceable:
                continue
            champion = str(unit.get("champion_id") or unit.get("apiName")
                           or unit.get("api_name") or unit.get("name") or "")
            traits = {str(value).casefold() for value in (unit.get("traits") or [])}
            alignment, investment = [], []
            if aliases & core_ids:
                alignment.append("core_unit")
            if (direction and direction in traits) or traits & core_traits:
                alignment.append("current_direction_or_core_trait")
            if area == "board":
                alignment.append("currently_contributes_to_board")
            star = int(unit.get("star", 1) or 1)
            items = list(unit.get("items") or [])
            if star >= 2:
                investment.append("upgraded_unit")
            if items:
                investment.append("equipped_items")
            identity = next(iter(sorted(aliases)), champion)
            if counts[identity] > 1:
                investment.append("multiple_owned_copies")
            classification = (
                "strategic_and_investment_signals" if alignment and investment
                else "observable_strategic_signals" if alignment
                else "investment_proxy_without_alignment" if investment
                else "insufficient_unit_evidence"
            )
            result.append({
                "name": unit.get("name", champion), "area": area, "star": star,
                "classification": classification, "strategic_signals": alignment,
                "investment_indicators": investment,
                "planner_classification": "preserve" if is_preserved else "replaceable",
            })
    return result


def _strategic_persistence_snapshot(state: dict, shadow: dict) -> dict:
    state = state if isinstance(state, dict) else {}
    shadow = shadow if isinstance(shadow, dict) else {}
    return {
        "locked": state.get("composition_locked"),
        "candidate_direction": state.get("composition_candidate_direction"),
        "candidate_streak": state.get("composition_candidate_streak"),
        "last_change_reason": state.get("composition_direction_change_reason"),
        "last_change_round": state.get("composition_direction_change_round"),
        "change_count": state.get("composition_direction_change_count"),
        "planner_candidate_direction": shadow.get("strategic_candidate_direction"),
        "planner_candidate_streak": shadow.get("strategic_candidate_streak"),
        "planner_candidate_last_review_round": shadow.get("strategic_candidate_last_review_round"),
        "planner_committed_direction": shadow.get("strategic_committed_direction"),
        "planner_selected_round": shadow.get("strategic_selected_round"),
    }

def _canonical_action(value: Any) -> str | None:
    if value is None:
        return None
    key = str(value).strip().upper()
    return ACTION_ALIASES.get(key)


def _delta(before: dict, after: dict, key: str):
    left, right = before.get(key), after.get(key)
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return round(float(right) - float(left), 4)
    return None


class OutcomeEvaluator:
    """Offline evaluator with unique round outcomes and multi-round follow-up."""

    @staticmethod
    def _round_order(value: Any) -> tuple[int, int]:
        parts = str(value or "").split("-", 1)
        try:
            return (int(parts[0]), int(parts[1]) if len(parts) > 1 else 0)
        except (TypeError, ValueError):
            return (999, 999)

    @staticmethod
    def _is_alive_state(state: dict) -> bool:
        if not isinstance(state, dict):
            return False
        if state.get("alive") is False or state.get("eliminated") is True:
            return False
        hp = state.get("hp")
        return isinstance(hp, (int, float)) and hp > 0

    def evaluate(self, decisions: list[dict], round_outcomes: list[dict] | None = None) -> dict:
        decisions_by_player_round = defaultdict(list)
        for decision in decisions:
            decisions_by_player_round[(
                str(decision.get("player", "?")), str(decision.get("round", "?"))
            )].append(decision)

        unique_rounds = {}
        for outcome in round_outcomes or []:
            key = (str(outcome.get("player", "?")), str(outcome.get("round", "?")))
            previous = unique_rounds.get(key)
            order = (
                int(outcome.get("sequence_id") or outcome.get("step") or 0),
                int(outcome.get("step") or 0),
            )
            previous_order = (
                int((previous or {}).get("sequence_id") or (previous or {}).get("step") or 0),
                int((previous or {}).get("step") or 0),
            )
            use_incoming = previous is None or order >= previous_order
            selected = dict(outcome if use_incoming else previous)
            fallback = previous if use_incoming else outcome
            for field in ("combat_reward", "reward", "placement", "state_after"):
                if selected.get(field) in (None, {}):
                    selected[field] = (fallback or {}).get(field)
            unique_rounds[key] = selected

        rounds_by_player = defaultdict(list)
        for (player, round_id), outcome in unique_rounds.items():
            rounds_by_player[player].append((round_id, outcome))
        for values in rounds_by_player.values():
            values.sort(key=lambda item: self._round_order(item[0]))

        decision_outcomes = []
        for decision in decisions:
            before, after = decision.get("state_before") or {}, decision.get("state_after") or {}
            economic = decision.get("economic_diagnostics") or {}
            snap_before = economic.get("strategic_snapshot_before") or {}
            snap_after = economic.get("strategic_snapshot_after") or {}
            shadow = _shadow(decision)
            decision_outcomes.append({
                "player": decision.get("player"), "round": decision.get("round"),
                "step": decision.get("step"), "action": decision.get("action_name"),
                "recommendation": shadow.get("action_recommendation_name"),
                "recommended_champion_id": shadow.get("action_recommended_champion_id"),
                "gold_delta": _delta(before, after, "gold"),
                "hp_delta": _delta(before, after, "hp"),
                "board_power_delta": _delta(before, after, "board_power"),
                "level_delta": _delta(before, after, "level"),
                "xp_delta": _delta(before, after, "xp"),
                "pair_delta": _delta(snap_before, snap_after, "combined_pair_count"),
                "two_star_delta": _delta(snap_before, snap_after, "board_two_star_or_higher"),
                "bench_two_star_delta": _delta(snap_before, snap_after, "bench_two_star_or_higher"),
                "three_star_delta": _delta(snap_before, snap_after, "board_three_star"),
                "bench_three_star_delta": _delta(snap_before, snap_after, "bench_three_star"),
                "win_streak_delta": _delta(before, after, "win_streak"),
                "loss_streak_delta": _delta(before, after, "loss_streak"),
                "composition_before": before.get("comp_direction"),
                "composition_after": after.get("comp_direction"),
                "composition_changed": (
                    before.get("comp_direction") != after.get("comp_direction")
                    if before.get("comp_direction") is not None and after.get("comp_direction") is not None
                    else None
                ),
            })

        round_summaries = []
        for player in sorted(rounds_by_player, key=lambda x: int(x) if x.isdigit() else 999):
            for round_id, outcome in rounds_by_player[player]:
                state = outcome.get("state_after") or {}
                round_summaries.append({
                    "player": player, "round": round_id, "hp": state.get("hp"),
                    "gold": state.get("gold"), "board_power": state.get("board_power"),
                    "level": state.get("level"), "win_streak": state.get("win_streak"),
                    "loss_streak": state.get("loss_streak"),
                    "composition_direction": state.get("comp_direction"),
                    "combat_reward": outcome.get("combat_reward"),
                    "placement": outcome.get("placement", state.get("placement")),
                    "alive": self._is_alive_state(state),
                })

        recommendation_rounds = []
        for (player, round_id), values in sorted(
            decisions_by_player_round.items(),
            key=lambda item: (
                int(item[0][0]) if item[0][0].isdigit() else 999,
                self._round_order(item[0][1]),
            ),
        ):
            recommendation_counts, action_counts = Counter(), Counter()
            for decision in values:
                recommendation = _shadow(decision).get("action_recommendation_name")
                if recommendation:
                    recommendation_counts[str(recommendation)] += 1
                actual = _canonical_action(decision.get("action_name"))
                if actual:
                    action_counts[actual] += 1
            player_rounds = rounds_by_player.get(player, [])
            index = next((i for i, item in enumerate(player_rounds)
                          if item[0] == round_id), None)
            next_one = player_rounds[index + 1][1] if index is not None and index + 1 < len(player_rounds) else None
            next_two = player_rounds[index + 2][1] if index is not None and index + 2 < len(player_rounds) else None
            current_state = (player_rounds[index][1].get("state_after") or {}) if index is not None else {}
            next_one_state = (next_one or {}).get("state_after") or {}
            next_two_state = (next_two or {}).get("state_after") or {}
            recommendation_rounds.append({
                "player": player, "round": round_id,
                "recommendations": dict(recommendation_counts),
                "actual_actions": dict(action_counts),
                "next_round": player_rounds[index + 1][0] if index is not None and index + 1 < len(player_rounds) else None,
                "next_round_hp_delta": _delta(current_state, next_one_state, "hp") if next_one else None,
                "next_round_gold_delta": _delta(current_state, next_one_state, "gold") if next_one else None,
                "next_round_board_delta": _delta(current_state, next_one_state, "board_power") if next_one else None,
                "next_two_rounds_hp_delta": _delta(current_state, next_two_state, "hp") if next_two else None,
                "next_two_rounds_gold_delta": _delta(current_state, next_two_state, "gold") if next_two else None,
                "next_two_rounds_board_delta": _delta(current_state, next_two_state, "board_power") if next_two else None,
                "placement": (
                    player_rounds[-1][1].get("placement")
                    or (player_rounds[-1][1].get("state_after") or {}).get("placement")
                ) if player_rounds else None,
            })

        players = {key[0] for key in decisions_by_player_round}
        players.update(rounds_by_player.keys())
        final_states = []
        for player in sorted(players, key=lambda x: int(x) if x.isdigit() else 999):
            alive_candidates = []
            for round_id, outcome in rounds_by_player.get(player, []):
                state = outcome.get("state_after") or {}
                if self._is_alive_state(state):
                    alive_candidates.append((
                        self._round_order(round_id),
                        int(outcome.get("sequence_id") or outcome.get("step") or 0),
                        int(outcome.get("step") or 0) * 2 + 2,
                        state,
                    ))
            for decision in decisions:
                if str(decision.get("player", "?")) != player:
                    continue
                round_order = self._round_order(decision.get("round"))
                sequence_id = int(decision.get("sequence_id") or decision.get("step") or 0)
                step = int(decision.get("step") or 0)
                before = decision.get("state_before") or {}
                after = decision.get("state_after") or {}
                if self._is_alive_state(before):
                    alive_candidates.append((round_order, sequence_id, step * 2, before))
                if self._is_alive_state(after):
                    alive_candidates.append((round_order, sequence_id, step * 2 + 1, after))
            alive_candidates.sort(key=lambda item: item[:3])
            last_alive = alive_candidates[-1][3] if alive_candidates else {}
            terminal = (
                rounds_by_player[player][-1][1].get("state_after") or {}
                if rounds_by_player.get(player) else {}
            )
            final_states.append({
                "player": player, "hp": last_alive.get("hp"),
                "gold": last_alive.get("gold"), "level": last_alive.get("level"),
                "board_power": last_alive.get("board_power"),
                "composition_direction": last_alive.get("comp_direction"),
                "placement": (
                    terminal.get("placement")
                    or (rounds_by_player[player][-1][1].get("placement")
                        if rounds_by_player.get(player) else None)
                    or last_alive.get("placement")
                ),
                "win_streak": last_alive.get("win_streak"),
                "loss_streak": last_alive.get("loss_streak"),
                "terminal_hp": terminal.get("hp"),
                "last_alive_state_preserved": bool(last_alive),
            })
        return {
            "decisions": decision_outcomes, "round_summaries": round_summaries,
            "recommendation_rounds": recommendation_rounds, "final_states": final_states,
        }


def _group_strategic_reviews(rows: list[tuple[dict, dict]]) -> list[tuple[dict, dict]]:
    """Collapse repeated per-action snapshots into one strategic review.

    A review is scoped to player, round, active direction, decision, target,
    anchor and reason. The latest observation supplies current scores while
    first/last steps and observation count preserve the audit trail.
    """
    grouped = {}
    for decision, shadow in rows:
        before = decision.get("state_before") or {}
        key = (
            str(decision.get("player", "?")),
            str(decision.get("round", "?")),
            str(before.get("comp_direction") or ""),
            str(shadow.get("strategic_decision_name") or ""),
            str(shadow.get("strategic_target_direction") or ""),
            str(shadow.get("strategic_anchor_champion_id") or ""),
            str(shadow.get("decision_path_reason") or shadow.get("strategic_reason") or ""),
        )
        step = decision.get("step")
        if key not in grouped:
            grouped[key] = {
                "decision": decision,
                "shadow": dict(shadow),
                "first_step": step,
                "last_step": step,
                "observations": 1,
            }
            continue
        item = grouped[key]
        item["observations"] += 1
        if isinstance(step, (int, float)):
            if not isinstance(item["first_step"], (int, float)) or step < item["first_step"]:
                item["first_step"] = step
            if not isinstance(item["last_step"], (int, float)) or step > item["last_step"]:
                item["last_step"] = step
        # Keep the latest row's diagnostic values and the complete review span.
        item["decision"] = decision
        item["shadow"] = dict(shadow)
    result = []
    for item in grouped.values():
        shadow = item["shadow"]
        shadow["_review_first_step"] = item["first_step"]
        shadow["_review_last_step"] = item["last_step"]
        shadow["_review_observations"] = item["observations"]
        result.append((item["decision"], shadow))
    result.sort(key=lambda row: (
        str(row[0].get("player", "?")),
        str(row[0].get("round", "?")),
        row[1].get("_review_first_step") or 0,
    ))
    return result


def build_shadow_markdown_reports(report: dict) -> dict[str, str]:
    """Return Markdown documents; no JSON artifacts are written by this module."""
    decisions = [
        item for item in report.get("decision_timeline", [])
        if isinstance(item, dict) and item.get("event_type", "action") == "action"
    ]
    by_player = defaultdict(list)
    for decision in decisions:
        by_player[str(decision.get("player", "?"))].append(decision)
    for values in by_player.values():
        values.sort(key=lambda item: (item.get("sequence_id") or 0, item.get("step") or 0))

    outcome_summary = OutcomeEvaluator().evaluate(decisions, report.get("round_outcome_timeline", []))
    shadow_rows = [(d, _shadow(d)) for d in decisions]
    available = [(d, s) for d, s in shadow_rows if s]
    strategy_observation_count = sum(1 for _, shadow in available if shadow.get("strategic_decision_name") is not None)
    strategy_rows = _group_strategic_reviews([
        (d, shadow) for d, shadow in available
        if shadow.get("strategic_decision_name") is not None
    ])
    economy_rows = [(d, s) for d, s in available if s.get("economic_posture_name") is not None]
    action_rows = [
        (d, s) for d, s in available
        if any(s.get(key) is not None for key in (
            "action_recommendation_name", "action_candidate_scores",
            "action_reason", "action_confidence",
        ))
    ]

    actual = Counter()
    recommended = Counter()
    agreements = divergences = compared = 0
    not_comparable = 0
    divergence_rows = []
    for decision, shadow in action_rows:
        actual_name = _canonical_action(decision.get("action_name"))
        recommendation = _canonical_action(shadow.get("action_recommendation_name"))
        if not actual_name or not recommendation:
            not_comparable += 1
            continue
        compared += 1
        actual[actual_name] += 1
        recommended[recommendation] += 1
        if actual_name == recommendation:
            agreements += 1
        else:
            divergences += 1
            divergence_rows.append((decision, shadow, actual_name, recommendation))

    def header(title: str, intro: str) -> list[str]:
        return [f"# {title}", "", intro, "",
                "> Recomendações em shadow mode são diagnósticos heurísticos. Elas não foram executadas nem alteraram a ação do PPO.",
                ""]

    ppo = header(
        "Ações executadas pelo PPO",
        "Esta seção registra a ação observada no log. A recomendação das novas camadas aparece nos documentos próprios."
    )
    ppo += ["| Jogador | Round | Step | Ação executada | Origem | Ouro antes → depois | HP antes → depois | Board antes → depois | Estratégia ativa |",
            "|---|---|---:|---|---|---:|---:|---:|---|"]
    for d in decisions:
        before, after = d.get("state_before") or {}, d.get("state_after") or {}
        ppo.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), d.get("action_name"),
            (d.get("legal_action_audit") or {}).get("action_source"),
            f"{before.get('gold', '—')} → {after.get('gold', '—')}",
            f"{before.get('hp', '—')} → {after.get('hp', '—')}",
            f"{before.get('board_power', '—')} → {after.get('board_power', '—')}",
            before.get("strategy_name"),
        )) + " |")
    if not decisions:
        ppo += ["| — | — | — | Dados de decisão indisponíveis | — | — | — | — | — |"]
    ppo += ["", f"Decisões PPO encontradas: **{len(decisions)}**.", ""]

    strategy = header(
        "Strategic Planner — recomendações",
        "Direção atual e recomendação do planner são mantidas separadas. O planner não altera o compromisso ativo nesta fase."
    )
    strategy += ["| Jogador | Round | Steps observados | Observações | Direção ativa | Decisão | Direção alvo | Âncora | Confiança | Custo de transição | Preservadas | Substituíveis | Candidatos avaliados (ID/direção/score/resultado) | Motivo |",
                 "|---|---|---|---:|---|---|---:|---:|---:|---:|---|---|---|---|"]
    for d, s in strategy_rows:
        before = d.get("state_before") or {}
        strategy.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"),
            f"{s.get('_review_first_step')}–{s.get('_review_last_step')}",
            s.get("_review_observations", 1), before.get("comp_direction"),
            s.get("strategic_decision_name"), s.get("strategic_target_direction"),
            s.get("strategic_anchor_champion_id"), s.get("strategic_confidence"),
            s.get("strategic_transition_cost"),
            s.get("strategic_preserve_unit_ids"),
            s.get("strategic_replaceable_unit_ids"),
            [
                f"{c.get('champion_id')}:{c.get('target_direction')}:{_cell(c.get('score'))}:{c.get('evaluation_reason')}"
                for c in (s.get("strategic_candidate_diagnostics") or [])
            ],
            s.get("strategic_reason"),
        )) + " |")
    if not strategy_rows:
        strategy += ["", "**Dados do Strategic Planner indisponíveis** nesta sessão. Logs anteriores à captura shadow continuam válidos para as demais auditorias."]
    decision_counts = Counter(str(shadow.get("strategic_decision_name"))
                               for _, shadow in strategy_rows)
    if decision_counts:
        strategy += ["", "### Frequência das decisões", ""]
        strategy += [f"- {name}: {count}" for name, count in sorted(decision_counts.items())]
    candidate_rows = sum(
        len(shadow.get("strategic_candidate_diagnostics") or [])
        for _, shadow in strategy_rows
    )
    strategy += [
        "",
        f"Revisões estratégicas únicas: **{len(strategy_rows)}**.",
        f"Snapshots estratégicos observados: **{strategy_observation_count}** (inclui repetições por ação).",
        f"Candidatos de âncora avaliados: **{candidate_rows}**.",
        "",
    ]

    insufficient_rows = [
        (d, shadow) for d, shadow in strategy_rows
        if shadow.get("strategic_decision_name") == "INSUFFICIENT_EVIDENCE"
    ]
    insufficient_reasons = Counter(
        str(shadow.get("decision_path_reason") or "unavailable")
        for _, shadow in insufficient_rows
    )
    generation_reasons = Counter(
        str(shadow.get("candidate_generation_reason") or "unavailable")
        for _, shadow in insufficient_rows
    )
    current_viability = Counter(
        "viable" if shadow.get("current_direction_viable") is True
        else "not_viable" if shadow.get("current_direction_viable") is False
        else "unavailable"
        for _, shadow in insufficient_rows
    )
    # KEEP must be evaluated independently: absence of a better alternative
    # is not, by itself, evidence that the current composition is strong.
    keep_rows = [(d, s) for d, s in strategy_rows
                 if s.get("strategic_decision_name") == "KEEP"]
    keep_reasons = Counter(str(s.get("decision_path_reason") or s.get("strategic_reason") or "unavailable")
                           for _, s in keep_rows)
    confidence_buckets = Counter()
    keep_evidence = []
    outcomes_by_round = {(str(x.get("player")), str(x.get("round"))): x
                         for x in outcome_summary["recommendation_rounds"]}
    for d, s in keep_rows:
        confidence = s.get("current_direction_confidence")
        confidence_buckets["unavailable" if confidence is None else
                           "zero" if float(confidence or 0.0) == 0.0 else "positive"] += 1
        keep_evidence.append((d, s, _strategic_unit_evidence(d.get("state_before") or {}, s),
                              outcomes_by_round.get((str(d.get("player")), str(d.get("round"))), {})))
    strategy += [
        "", "### Auditoria de KEEP — continuidade fundamentada versus persistência", "",
        f"- KEEP auditados: **{len(keep_rows)}**",
        "- Confiança da direção atual: " + _cell(dict(confidence_buckets)),
        "- Motivos/path: " + _cell(dict(keep_reasons)), "",
        "| Jogador | Round | Step | Direção | Score atual | Conf. direção atual | Conf. alternativa | Score alternativa | Vantagem | Viável | Motivo | Lock | Candidato pendente | Streak | Limite PIVOT |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---|---|---|---|---:|---:|",
    ]
    for d, s, _, _ in keep_evidence:
        before = d.get("state_before") or {}
        persistence = _strategic_persistence_snapshot(before, s)
        strategy.append("| " + " | ".join(_cell(v) for v in (
            d.get("player"), d.get("round"), d.get("step"), before.get("comp_direction"),
            s.get("current_direction_score"), s.get("current_direction_confidence"),
            s.get("anchor_confidence"), s.get("best_anchor_score"), s.get("alternative_advantage"),
            s.get("current_direction_viable"), s.get("decision_path_reason"),
            persistence["locked"], persistence["candidate_direction"] or persistence["planner_candidate_direction"],
            persistence["candidate_streak"] if persistence["candidate_streak"] is not None else persistence["planner_candidate_streak"],
            s.get("required_pivot_advantage"),
        )) + " |")
    strategy += [
        "", "### Unidades preservadas — sinais estratégicos versus investimento", "",
        "| Jogador | Round | Unidade | Área | Estrelas | Classificação | Sinais estratégicos | Indicadores de investimento |",
        "|---|---|---|---|---:|---|---|---|",
    ]
    unit_count = 0
    for d, _, units, _ in keep_evidence:
        for unit in units:
            if unit["planner_classification"] != "preserve":
                continue
            unit_count += 1
            strategy.append("| " + " | ".join(_cell(v) for v in (
                d.get("player"), d.get("round"), unit["name"], unit["area"], unit["star"],
                unit["classification"], unit["strategic_signals"], unit["investment_indicators"],
            )) + " |")
    if not unit_count:
        strategy.append("| — | — | Sem unidades preservadas identificáveis no snapshot | — | — | — | — | — |")
    strategy += [
        "", f"Unidades preservadas com evidência observável: **{unit_count}**.",
        "Classificações são proxies do snapshot (core, traits, presença no board, estrelas, itens e cópias). "
        "Não provam que o Planner preservou por investimento anterior; custo passado não é valor estratégico por si só.",
        "", "### Thresholds e histerese configurados", "",
        "| Parâmetro | Valor padrão no StrategicPlannerConfig |",
        "|---|---:|",
        "| Score mínimo de âncora | 0.01 |",
        "| Vantagem mínima para ADAPT | 0.10 |",
        "| Vantagem absoluta para mudança | 0.75 |",
        "| Vantagem relativa para mudança | 20% |",
        "| Revisões consecutivas desbloqueado | 2 |",
        "| Revisões consecutivas bloqueado | 3 |",
        "",
        "CompositionDirectionPolicy possui política separada: vantagem absoluta 0.75, relativa 20% e 3 atualizações consecutivas quando bloqueada. "
        "Os valores são defaults do código; a auditoria não presume configuração customizada em runtime.",
        "", "### Evolução posterior dos KEEP", "",
        "| Jogador | Round | Step | Próximo round | Δ HP | Δ Ouro | Δ Board | Próximos 2 rounds Δ HP / Ouro / Board | Colocação final |",
        "|---|---|---:|---|---:|---:|---:|---|---:|",
    ]
    for d, _, _, followup in keep_evidence:
        strategy.append("| " + " | ".join(_cell(v) for v in (
            d.get("player"), d.get("round"), d.get("step"), followup.get("next_round"),
            followup.get("next_round_hp_delta"), followup.get("next_round_gold_delta"),
            followup.get("next_round_board_delta"),
            f"{followup.get('next_two_rounds_hp_delta')} / {followup.get('next_two_rounds_gold_delta')} / {followup.get('next_two_rounds_board_delta')}",
            followup.get("placement"),
        )) + " |")
    if not keep_evidence:
        strategy.append("| — | — | — | — | — | — | — | — | — |")
    strategy += ["", "A evolução posterior é associação temporal, não atribuição causal à recomendação shadow.", ""]

    strategy += [
        "", "### Auditoria de INSUFFICIENT_EVIDENCE", "",
        "| Jogador | Round | Step | Motivo específico | Geração de candidatos | Direção atual | Viável atual | Score atual | Score âncora | Vantagem | Mín. ADAPT | Limite PIVOT | Conf. âncora | Conf. direção atual | Âncora disponível | Filtros (considerados/gerados/catálogo ausente/planos vazios/âncora ausente) |",
        "|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for d, shadow in insufficient_rows:
        strategy.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"),
            shadow.get("decision_path_reason"), shadow.get("candidate_generation_reason"),
            (d.get("state_before") or {}).get("comp_direction"),
            shadow.get("current_direction_viable"),
            shadow.get("current_direction_score"), shadow.get("best_anchor_score"),
            shadow.get("alternative_advantage"), shadow.get("minimum_adapt_advantage"),
            shadow.get("required_pivot_advantage"), shadow.get("anchor_confidence"),
            shadow.get("current_direction_confidence"), shadow.get("has_anchor_candidate"),
            f"{shadow.get('anchors_considered')} / {shadow.get('candidates_generated')} / "
            f"{shadow.get('rejected_missing_champion_definition')} / "
            f"{shadow.get('rejected_empty_plan')} / {shadow.get('rejected_anchor_not_in_plan')}",
        )) + " |")
    if not insufficient_rows:
        strategy.append("| — | — | — | Dados INSUFFICIENT_EVIDENCE indisponíveis | — | — | — | — | — | — | — | — | — | — | — | — |")
    strategy += [
        "", "**Motivos agregados:** " + _cell(dict(insufficient_reasons)),
        "**Motivos de geração agregados:** " + _cell(dict(generation_reasons)),
        "**Viabilidade da direção atual:** " + _cell(dict(current_viability)),
        "",
        "Confiança da âncora e confiança da direção atual são derivadas de score e não são probabilidades calibradas. "
        "Snapshots por ação podem repetir a mesma revisão; não devem ser contados como revisões independentes.",
        "",
    ]

    # Candidate coverage is reported per player/round. These are action-level
    # observations, not independent strategic reviews; repeated snapshots are
    # intentionally labelled as observations.
    anchor_coverage = defaultdict(lambda: {
        "observations": 0, "insufficient": 0, "anchors_considered": 0,
        "candidates_generated": 0, "rejected_cost_below_four": 0,
        "no_cost_four_or_five_anchor": 0, "no_high_cost_anchor_units_seen": 0,
    })
    for decision, shadow in available:
        coverage_key = (str(decision.get("player", "?")), str(decision.get("round", "?")))
        bucket = anchor_coverage[coverage_key]
        bucket["observations"] += 1
        bucket["insufficient"] += int(
            shadow.get("strategic_decision_name") == "INSUFFICIENT_EVIDENCE"
        )
        for metric in ("anchors_considered", "candidates_generated", "rejected_cost_below_four"):
            try:
                bucket[metric] += int(shadow.get(metric) or 0)
            except (TypeError, ValueError):
                pass
        generation_reason = str(shadow.get("candidate_generation_reason") or "")
        if generation_reason == "no_cost_four_or_five_anchor":
            bucket["no_cost_four_or_five_anchor"] += 1
        elif generation_reason == "no_high_cost_anchor_units_seen":
            bucket["no_high_cost_anchor_units_seen"] += 1

    strategy += [
        "", "### Cobertura de âncoras por jogador/round", "",
        "| Jogador | Round | Observações | INSUFFICIENT_EVIDENCE | Âncoras consideradas | Candidatos gerados | Rejeitados por custo < 4 | Sem âncora custo 4/5 | Sem unidades âncora |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for (player, round_id), coverage in sorted(
        anchor_coverage.items(),
        key=lambda item: (item[0][0], OutcomeEvaluator._round_order(item[0][1])),
    ):
        strategy.append("| " + " | ".join(_cell(value) for value in (
            player, round_id, coverage["observations"], coverage["insufficient"],
            coverage["anchors_considered"], coverage["candidates_generated"],
            coverage["rejected_cost_below_four"], coverage["no_cost_four_or_five_anchor"],
            coverage["no_high_cost_anchor_units_seen"],
        )) + " |")
    if not anchor_coverage:
        strategy.append("| — | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    strategy += [
        "",
        "As contagens são observações por ação, não revisões independentes. "
        "A rejeição por custo inferior a 4 reflete o filtro atual da geração de âncoras; "
        "nenhuma direção inicial é inferida a partir desses candidatos rejeitados.",
        "",
    ]

    economy = header(
        "Economic Controller — posturas recomendadas",
        "A postura descreve a orientação econômica sugerida no instante anterior à ação do PPO."
    )
    economy += ["| Jogador | Round | Step | Postura | Confiança | Pressão sobrevivência | Pressão board | Pressão recursos | Motivo |",
                "|---|---|---:|---|---:|---:|---:|---:|---|"]
    posture_counts = Counter()
    for d, s in economy_rows:
        posture = s.get("economic_posture_name")
        if posture:
            posture_counts[str(posture)] += 1
        economy.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), posture,
            s.get("economic_posture_confidence"), s.get("economic_survival_pressure"),
            s.get("economic_board_pressure"), s.get("economic_resource_pressure"),
            s.get("economic_posture_reason"),
        )) + " |")
    if not economy_rows:
        economy += ["", "**Dados do Economic Controller indisponíveis** nesta sessão."]
    if posture_counts:
        economy += ["", "### Frequência das posturas", ""]
        economy += [f"- {name}: {count}" for name, count in sorted(posture_counts.items())]
    economy += ["", f"Decisões com diagnóstico econômico: **{len(economy_rows)} / {len(decisions)}**.", ""]

    actions = header(
        "Action Evaluator — recomendações e scores",
        "O Action Evaluator classifica candidatos disponíveis; a coluna PPO mostra o que realmente foi executado."
    )
    actions += ["| Jogador | Round | Step | PPO executou | Recomendação | Campeão recomendado | Δ board (proxy) | Δ ouro direto | Juros perdidos | Custo oportunidade | Custo econômico líquido | HP (proxy) | Streak (proxy) | Confiança | Motivo |",
                "|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for d, s in action_rows:
        actions.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), d.get("action_name"),
            s.get("action_recommendation_name"),
            s.get("action_recommended_champion_id"),
            s.get("action_expected_board_delta"),
            s.get("action_expected_direct_gold_cost"),
            s.get("action_expected_lost_interest_cost"),
            s.get("action_expected_opportunity_cost"),
            s.get("action_expected_economy_cost"),
            s.get("action_expected_hp_preservation"),
            s.get("action_expected_streak_value"), s.get("action_confidence"),
            s.get("action_reason"),
        )) + " |")
    if not action_rows:
        actions += ["", "**Dados do Action Evaluator indisponíveis** nesta sessão."]
    actions += ["", f"Recomendações disponíveis: **{len(action_rows)} / {len(decisions)}**.",
                "", "### Scores dos candidatos (proxies heurísticos)", "",
                "| Jogador | Round | Step | Ação | Campeão | Disponível | Δ ouro direto | Juros perdidos | Oportunidade | Board | Sobrevivência | Streak | Composição | Upgrade | Postura | Score custo direto | Score juros | Score oportunidade | Total | Selecionado |",
                "|---|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for d, shadow in action_rows:
        for candidate in shadow.get("action_candidate_scores") or []:
            actions.append("| " + " | ".join(_cell(x) for x in (
                d.get("player"), d.get("round"), d.get("step"),
                candidate.get("action"), candidate.get("champion_id"),
                candidate.get("available"),
                candidate.get("direct_gold_cost"), candidate.get("lost_interest_cost"),
                candidate.get("opportunity_cost"),
                candidate.get("board_component"), candidate.get("survival_component"),
                candidate.get("streak_component"), candidate.get("composition_component"),
                candidate.get("upgrade_component"), candidate.get("posture_component"),
                candidate.get("direct_cost_component"), candidate.get("lost_interest_component"),
                candidate.get("opportunity_cost_component"), candidate.get("total_score"),
                candidate.get("selected"),
            )) + " |")
    selected_candidate_checks = []
    for d, shadow in action_rows:
        candidates = shadow.get("action_candidate_scores") or []
        selected = [candidate for candidate in candidates if candidate.get("selected") is True]
        recommended_id = shadow.get("action_recommended_champion_id")
        selected_ids = [candidate.get("champion_id") for candidate in selected]
        selected_candidate_checks.append({
            "player": d.get("player"), "round": d.get("round"), "step": d.get("step"),
            "selected_count": len(selected),
            "recommended_champion_id": recommended_id,
            "selected_champion_ids": selected_ids,
            "integrity_status": classify_candidate_selection(
                len(candidates), selected_ids, recommended_id,
            ),
        })
    integrity_counts = Counter(check["integrity_status"] for check in selected_candidate_checks)
    actions += ["", "### Integridade da seleção", ""]
    actions += [
        f"- Consistentes: **{integrity_counts.get('CONSISTENT', 0)}**",
        f"- Inconsistentes: **{integrity_counts.get('INCONSISTENT', 0)}**",
        f"- Incompletos: **{integrity_counts.get('INCOMPLETE', 0)}**",
        f"- Não aplicáveis (sem candidatos e sem seleção): **{integrity_counts.get('NOT_APPLICABLE', 0)}**",
        "",
    ]
    actions += ["| Jogador | Round | Step | Candidatos | Selecionados | Campeão recomendado | Campeão selecionado | Status |",
                "|---|---|---:|---:|---:|---:|---|---|"]
    for check, (d, shadow) in zip(selected_candidate_checks, action_rows):
        actions.append("| " + " | ".join(_cell(value) for value in (
            check["player"], check["round"], check["step"],
            len(shadow.get("action_candidate_scores") or []), check["selected_count"],
            check["recommended_champion_id"], check["selected_champion_ids"],
            check["integrity_status"],
        )) + " |")
    actions += ["", "Board delta, HP e streak são proxies heurísticos, não previsões calibradas. Custo direto, juros perdidos e custo de oportunidade são exibidos separadamente. A integridade verifica a correspondência entre o candidato marcado como selecionado e o campeão recomendado; não recalcula nem altera o score nativo.", ""]

    divergence = header(
        "Divergências — PPO versus Action Evaluator",
        "A comparação usa categorias normalizadas: PASS/HOLD, BUY/BUY_UNIT, BUY_XP/BUY_EXPERIENCE, REROLL/REROLL_SHOP, SELL/SELL_UNIT e movimentos/DEPLOY_OR_MOVE."
    )
    divergence += [
        f"- Decisões comparáveis: **{compared}**",
        f"- Concordâncias: **{agreements}**",
        f"- Divergências: **{divergences}**",
        f"- Não comparáveis (ação sem categoria equivalente): **{not_comparable}**",
        f"- Concordância observada: **{(agreements / compared * 100):.1f}%**" if compared else "- Concordância observada: **indisponível**",
        "",
        "| Jogador | Round | Step | PPO executou | Action Evaluator recomendou | Motivo da recomendação |",
        "|---|---|---:|---|---|---|",
    ]
    for d, s, actual_name, recommendation in divergence_rows:
        divergence.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), actual_name,
            recommendation, s.get("action_reason"),
        )) + " |")
    if compared == 0:
        divergence += ["", "**Comparação indisponível**: a sessão não contém diagnósticos suficientes do Action Evaluator."]
    elif not divergence_rows:
        divergence += ["", "Nenhuma divergência observada nas decisões comparáveis."]
    divergence += [
        "",
        "A concordância mede apenas semelhança entre rótulos de ação. Não prova que uma recomendação era melhor. As divergências são pontos de revisão, não erros automáticos.",
        "",
    ]

    outcomes = header(
        "Outcome Evaluator — resultados observados",
        "Esta auditoria mede mudanças observadas depois de cada ação e o estado final registrado. Não atribui causalidade exclusiva à ação ou à recomendação shadow."
    )
    outcomes += [
        "## Efeito imediato por decisão (sem repetir combate)",
        "",
        "| Jogador | Round | Step | PPO executou | Action Evaluator recomendou | Campeão recomendado | Δ Ouro | Δ HP | Δ Board | Δ Nível | Δ XP | Δ pares | Δ 2★ board/bench | Δ 3★ board/bench | Δ win/loss streak | Composição antes → depois |",
        "|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in outcome_summary["decisions"]:
        values = (
            item.get("player"), item.get("round"), item.get("step"), item.get("action"),
            item.get("recommendation"), item.get("recommended_champion_id"),
            item.get("gold_delta"), item.get("hp_delta"), item.get("board_power_delta"),
            item.get("level_delta"), item.get("xp_delta"), item.get("pair_delta"),
            f"{item.get('two_star_delta')} / {item.get('bench_two_star_delta')}",
            f"{item.get('three_star_delta')} / {item.get('bench_three_star_delta')}",
            f"{item.get('win_streak_delta')} / {item.get('loss_streak_delta')}",
            f"{item.get('composition_before') or '—'} → {item.get('composition_after') or '—'}",
        )
        outcomes.append("| " + " | ".join(_cell(x) for x in values) + " |")
    if not decisions:
        outcomes += ["| — | — | — | Sem decisões estruturadas | — | — | — | — | — | — | — | — | — | — | — | — |"]
    outcomes += ["", "## Resultado de combate (uma linha por jogador e round)", "",
                 "| Jogador | Round | HP fim round | Ouro | Board power | Nível | Win streak | Loss streak | Recompensa combate | Colocação | Vivo no snapshot |",
                 "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for round_result in outcome_summary["round_summaries"]:
        outcomes.append("| " + " | ".join(_cell(x) for x in (
            round_result.get("player"), round_result.get("round"), round_result.get("hp"),
            round_result.get("gold"), round_result.get("board_power"), round_result.get("level"),
            round_result.get("win_streak"), round_result.get("loss_streak"),
            round_result.get("combat_reward"), round_result.get("placement"),
            round_result.get("alive"),
        )) + " |")
    outcomes += ["", "## Evolução posterior das recomendações por jogador/round", "",
                 "| Jogador | Round das recomendações | Contagem por recomendação | Ações PPO | Próximo round | Δ HP | Δ Ouro | Δ Board | Próximos 2 rounds Δ HP / Ouro / Board | Colocação final |",
                 "|---|---|---|---|---|---:|---:|---:|---|---:|"]
    for item in outcome_summary["recommendation_rounds"]:
        outcomes.append("| " + " | ".join(_cell(x) for x in (
            item.get("player"), item.get("round"), item.get("recommendations"),
            item.get("actual_actions"), item.get("next_round"),
            item.get("next_round_hp_delta"), item.get("next_round_gold_delta"),
            item.get("next_round_board_delta"),
            f"{item.get('next_two_rounds_hp_delta')} / {item.get('next_two_rounds_gold_delta')} / {item.get('next_two_rounds_board_delta')}",
            item.get("placement"),
        )) + " |")
    outcomes += ["", "## Último estado vivo preservado por jogador", "",
                 "| Jogador | HP último estado vivo | Ouro | Nível | Board power | Direção | Win streak | Loss streak | Colocação final | HP terminal |",
                 "|---|---:|---:|---:|---:|---|---:|---:|---:|---:|"]
    for final in outcome_summary["final_states"]:
        outcomes.append("| " + " | ".join(_cell(x) for x in (
            final.get("player"), final.get("hp"), final.get("gold"), final.get("level"),
            final.get("board_power"), final.get("composition_direction"),
            final.get("win_streak"), final.get("loss_streak"), final.get("placement"),
            final.get("terminal_hp"),
        )) + " |")
    if not by_player:
        outcomes += ["| — | — | — | — | — | — | — | — | — | — |"]
    outcomes += [
        "",
        "Os deltas imediatos medem apenas a transição registrada após a ação. O resultado de combate aparece uma única vez por jogador/round. A tabela de evolução liga o conjunto de recomendações daquele round aos próximos um e dois rounds; é associação temporal, não causalidade. O estado vivo é preservado separadamente do estado terminal de eliminação. Dados ausentes permanecem como —.",
        "",
    ]

    overview = [
        "# Auditoria completa — índice",
        "",
        f"- Jogadores: **{len(report.get('players_seen', []))}**",
        f"- Decisões registradas: **{len(decisions)}**",
        f"- Diagnósticos shadow disponíveis: **{len(available)}**",
        f"- Comparações PPO × Action Evaluator: **{compared}**",
        f"- Concordâncias: **{agreements}** | Divergências: **{divergences}**",
        "",
        "## Relatórios",
        "",
        "- [Resumo geral — parte 1](audit_report_geral_parte_1.md)",
        "- [Resumo geral — parte 2](audit_report_geral_parte_2.md)",
        "- [Resumo geral — parte 3](audit_report_geral_parte_3.md)",
        "- [Ações efetivamente executadas pelo PPO](audit_ppo.md)",
        "- [Strategic Planner](audit_estrategia.md)",
        "- [Economic Controller](audit_economia.md)",
        "- [Action Evaluator — parte 1](audit_acoes_parte_1.md)",
        "- [Action Evaluator — parte 2](audit_acoes_parte_2.md)",
        "- [Action Evaluator — parte 3](audit_acoes_parte_3.md)",
        "- [Cobertura de BUY_XP](audit_buy_xp.md)",
        "- [Baseline de HOLD](audit_hold.md)",
        "- [Divergências PPO × Action Evaluator](audit_divergencias.md)",
        "- [Resultados observados / Outcome Evaluator](audit_resultados.md)",
        "- [Evidências detalhadas dos achados](audit_report_achados.md)",
        "",
        "Os documentos são gerados pela mesma ação do Viewer. Os dados estruturados usados durante o processamento são temporários; os artefatos da auditoria são Markdown.",
        "",
    ]
    return {
        "audit_report.md": "\n".join(overview),
        "audit_report_geral.md": report.get("_markdown_general", ""),
        "audit_report_achados.md": report.get("_markdown_evidence", ""),
        "audit_report_completo.md": "\n".join(overview),
        "audit_ppo.md": "\n".join(ppo),
        "audit_estrategia.md": "\n".join(strategy),
        "audit_economia.md": "\n".join(economy),
        "audit_acoes.md": "\n".join(actions),
        "audit_divergencias.md": "\n".join(divergence),
        "audit_resultados.md": "\n".join(outcomes),
    }
