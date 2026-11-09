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
            order = (outcome.get("sequence_id") or 0, outcome.get("step") or 0)
            previous_order = ((previous or {}).get("sequence_id") or 0,
                              (previous or {}).get("step") or 0)
            if previous is None or order >= previous_order:
                unique_rounds[key] = outcome

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
                        outcome.get("sequence_id") or 0,
                        outcome.get("step") or 0,
                        state,
                    ))
            for decision in decisions:
                if str(decision.get("player", "?")) != player:
                    continue
                round_order = self._round_order(decision.get("round"))
                sequence_id = decision.get("sequence_id") or 0
                step = decision.get("step") or 0
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
    strategy += ["| Jogador | Round | Step | Direção ativa | Decisão | Direção alvo | Âncora | Confiança | Custo de transição | Preservadas | Substituíveis | Candidatos avaliados (ID/direção/score/resultado) | Motivo |",
                 "|---|---|---:|---|---|---|---:|---:|---:|---|---|---|---|"]
    for d, s in strategy_rows:
        before = d.get("state_before") or {}
        strategy.append("| " + " | ".join(_cell(x) for x in (
            d.get("player"), d.get("round"), d.get("step"), before.get("comp_direction"),
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
    actions += ["| Jogador | Round | Step | PPO executou | Recomendação | Campeão recomendado | Δ board (proxy) | Δ ouro direto | Juros perdidos | Custo oportunidade | Custo total estimado | HP (proxy) | Streak (proxy) | Confiança | Motivo |",
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
                "| Jogador | Round | Step | Ação | Campeão | Board | Sobrevivência | Streak | Composição | Upgrade | Postura | Custo direto | Juros | Oportunidade | Total | Selecionado |",
                "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for d, shadow in action_rows:
        for candidate in shadow.get("action_candidate_scores") or []:
            actions.append("| " + " | ".join(_cell(x) for x in (
                d.get("player"), d.get("round"), d.get("step"),
                candidate.get("action"), candidate.get("champion_id"),
                candidate.get("board_component"), candidate.get("survival_component"),
                candidate.get("streak_component"), candidate.get("composition_component"),
                candidate.get("upgrade_component"), candidate.get("posture_component"),
                candidate.get("direct_cost_component"), candidate.get("lost_interest_component"),
                candidate.get("opportunity_cost_component"), candidate.get("total_score"),
                candidate.get("selected"),
            )) + " |")
    actions += ["", "Board delta, HP e streak são proxies heurísticos, não previsões calibradas. Custo direto, juros perdidos e custo de oportunidade são exibidos separadamente.", ""]

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
