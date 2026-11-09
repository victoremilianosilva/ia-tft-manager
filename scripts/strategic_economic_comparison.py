"""Shadow-decision comparison and outcome Markdown reports for Viewer audits.

The module consumes the structured audit timeline only. Missing diagnostics remain
explicitly unavailable; heuristic recommendations are never treated as PPO actions.
"""
from __future__ import annotations

from collections import Counter, defaultdict
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


def _canonical_action(value: Any) -> str | None:
    if value is None:
        return None
    key = str(value).strip().upper()
    return ACTION_ALIASES.get(key, key or None)


def _delta(before: dict, after: dict, key: str):
    left, right = before.get(key), after.get(key)
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return round(float(right) - float(left), 4)
    return None


class OutcomeEvaluator:
    """Offline evaluator for observed post-action deltas and final logged state."""

    def evaluate(self, decisions: list[dict], round_outcomes: list[dict] | None = None) -> dict:
        by_player = defaultdict(list)
        decision_outcomes = []
        outcomes_by_round = {}
        for outcome in round_outcomes or []:
            outcomes_by_round[(str(outcome.get("player", "?")), str(outcome.get("round", "?")))] = outcome
        for decision in decisions:
            before = decision.get("state_before") or {}
            after = decision.get("state_after") or {}
            economic = decision.get("economic_diagnostics") or {}
            snap_before = economic.get("strategic_snapshot_before") or {}
            snap_after = economic.get("strategic_snapshot_after") or {}
            round_outcome = outcomes_by_round.get((
                str(decision.get("player", "?")), str(decision.get("round", "?"))
            ), {})
            round_state = round_outcome.get("state_after") or {}
            decision_outcomes.append({
                "player": decision.get("player"),
                "round": decision.get("round"),
                "step": decision.get("step"),
                "action": decision.get("action_name"),
                "gold_delta": _delta(before, after, "gold"),
                "hp_delta": _delta(before, after, "hp"),
                "board_power_delta": _delta(before, after, "board_power"),
                "level_delta": _delta(before, after, "level"),
                "xp_delta": _delta(before, after, "xp"),
                "pair_delta": _delta(snap_before, snap_after, "combined_pair_count"),
                "two_star_delta": _delta(snap_before, snap_after, "board_two_star_or_higher"),
                "three_star_delta": _delta(snap_before, snap_after, "board_three_star"),
                # These round-end deltas include all remaining preparation actions
                # and combat; they are contextual outcomes, not attribution to this action.
                "round_end_hp_delta": _delta(before, round_state, "hp"),
                "round_end_gold_delta": _delta(before, round_state, "gold"),
                "round_end_board_delta": _delta(before, round_state, "board_power"),
                "round_combat_reward": round_outcome.get("combat_reward"),
                "round_placement": round_outcome.get("placement", round_state.get("placement")),
            })
            by_player[str(decision.get("player", "?"))].append(decision)

        final_states = []
        for player, values in sorted(
            by_player.items(),
            key=lambda item: int(item[0]) if item[0].isdigit() else 999,
        ):
            final = next((d.get("state_after") or {} for d in reversed(values)
                          if d.get("state_after")), {})
            final_states.append({
                "player": player,
                "hp": final.get("hp"),
                "gold": final.get("gold"),
                "level": final.get("level"),
                "board_power": final.get("board_power"),
                "composition_direction": final.get("comp_direction"),
                "placement": final.get("placement"),
            })
        return {"decisions": decision_outcomes, "final_states": final_states}


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
    strategy_rows = [(d, s) for d, s in available if s.get("strategic_decision_name") is not None]
    economy_rows = [(d, s) for d, s in available if s.get("economic_posture_name") is not None]
    action_rows = [(d, s) for d, s in available if s.get("action_recommendation_name") is not None]

    actual = Counter()
    recommended = Counter()
    agreements = divergences = compared = 0
    divergence_rows = []
    for decision, shadow in action_rows:
        actual_name = _canonical_action(decision.get("action_name"))
        recommendation = _canonical_action(shadow.get("action_recommendation_name"))
        if not actual_name or not recommendation:
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
    ppo += ["| Jogador | Round | Step | Ação executada | Ouro antes → depois | HP antes → depois | Board antes → depois | Estratégia ativa |",
            "|---|---|---:|---|---:|---:|---:|---|"]
    for d in decisions:
        before, after = d.get("state_before") or {}, d.get("state_after") or {}
        ppo.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), d.get("action_name"),
            f"{before.get('gold', '—')} → {after.get('gold', '—')}",
            f"{before.get('hp', '—')} → {after.get('hp', '—')}",
            f"{before.get('board_power', '—')} → {after.get('board_power', '—')}",
            before.get("strategy_name"),
        )) + " |")
    if not decisions:
        ppo += ["| — | — | — | Dados de decisão indisponíveis | — | — | — | — |"]
    ppo += ["", f"Decisões PPO encontradas: **{len(decisions)}**.", ""]

    strategy = header(
        "Strategic Planner — recomendações",
        "Direção atual e recomendação do planner são mantidas separadas. O planner não altera o compromisso ativo nesta fase."
    )
    strategy += ["| Jogador | Round | Step | Direção ativa | Decisão | Direção alvo | Âncora | Confiança | Custo de transição | Motivo |",
                 "|---|---|---:|---|---|---|---:|---:|---:|---|"]
    for d, s in strategy_rows:
        before = d.get("state_before") or {}
        strategy.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), before.get("comp_direction"),
            s.get("strategic_decision_name"), s.get("strategic_target_direction"),
            s.get("strategic_anchor_champion_id"), s.get("strategic_confidence"),
            s.get("strategic_transition_cost"), s.get("strategic_reason"),
        )) + " |")
    if not strategy_rows:
        strategy += ["", "**Dados do Strategic Planner indisponíveis** nesta sessão. Logs anteriores à captura shadow continuam válidos para as demais auditorias."]
    strategy += ["", f"Decisões com diagnóstico estratégico: **{len(strategy_rows)} / {len(decisions)}**.", ""]

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
    actions += ["| Jogador | Round | Step | PPO executou | Recomendação | Board delta estimado | HP preservado estimado | Custo econômico estimado | Valor de streak estimado | Confiança | Motivo |",
                "|---|---|---:|---|---|---:|---:|---:|---:|---:|---|"]
    for d, s in action_rows:
        actions.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), d.get("action_name"),
            s.get("action_recommendation_name"), s.get("action_expected_board_delta"),
            s.get("action_expected_hp_preservation"), s.get("action_expected_economy_cost"),
            s.get("action_expected_streak_value"), s.get("action_confidence"),
            s.get("action_reason"),
        )) + " |")
    if not action_rows:
        actions += ["", "**Dados do Action Evaluator indisponíveis** nesta sessão."]
    actions += ["", f"Recomendações disponíveis: **{len(action_rows)} / {len(decisions)}**.", ""]

    divergence = header(
        "Divergências — PPO versus Action Evaluator",
        "A comparação usa categorias normalizadas: PASS/HOLD, BUY/BUY_UNIT, BUY_XP/BUY_EXPERIENCE, REROLL/REROLL_SHOP, SELL/SELL_UNIT e movimentos/DEPLOY_OR_MOVE."
    )
    divergence += [
        f"- Decisões comparáveis: **{compared}**",
        f"- Concordâncias: **{agreements}**",
        f"- Divergências: **{divergences}**",
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
        "## Efeito imediato por decisão",
        "",
        "| Jogador | Round | Step | Ação PPO | Δ Ouro | Δ HP | Δ Board | Δ Nível | Δ XP | Δ pares | Δ 2★+ | Δ 3★ | Δ HP até fim round | Δ Ouro até fim round | Δ Board até fim round | Rew combate | Colocação |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in outcome_summary["decisions"]:
        values = (
            item.get("player"), item.get("round"), item.get("step"), item.get("action"),
            item.get("gold_delta"), item.get("hp_delta"), item.get("board_power_delta"),
            item.get("level_delta"), item.get("xp_delta"), item.get("pair_delta"),
            item.get("two_star_delta"), item.get("three_star_delta"),
            item.get("round_end_hp_delta"), item.get("round_end_gold_delta"),
            item.get("round_end_board_delta"), item.get("round_combat_reward"),
            item.get("round_placement"),
        )
        outcomes.append("| " + " | ".join(_cell(x) for x in values) + " |")
    if not decisions:
        outcomes += ["| — | — | — | Sem decisões estruturadas | — | — | — | — | — | — | — | — | — | — | — | — | — |"]
    outcomes += ["", "## Estado final observado por jogador", "",
                 "| Jogador | HP final | Ouro final | Nível | Board power | Direção | Colocação |",
                 "|---|---:|---:|---:|---:|---|---:|"]
    for final in outcome_summary["final_states"]:
        outcomes.append("| " + " | ".join(_cell(x) for x in (
            final.get("player"), final.get("hp"), final.get("gold"), final.get("level"),
            final.get("board_power"), final.get("composition_direction"), final.get("placement"),
        )) + " |")
    if not by_player:
        outcomes += ["| — | — | — | — | — | — | — |"]
    outcomes += [
        "",
        "Os deltas imediatos medem a transição da ação. Os deltas até o fim do round incluem as ações restantes da preparação e o combate; são contexto posterior e não podem ser atribuídos isoladamente à ação da linha. Resultado final é o último estado observado no log, não uma previsão. Dados ausentes permanecem como —.",
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
        "- [Resumo geral](audit_report_geral.md)",
        "- [Ações efetivamente executadas pelo PPO](audit_ppo.md)",
        "- [Strategic Planner](audit_estrategia.md)",
        "- [Economic Controller](audit_economia.md)",
        "- [Action Evaluator](audit_acoes.md)",
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
