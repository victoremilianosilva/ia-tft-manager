"""Generate a compact, evidence-based Markdown audit from JSONL traces."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ACTION_NAMES = {
    0: "BUY", 1: "REROLL", 2: "BUY_XP", 3: "MOVE_BENCH",
    4: "MOVE_BOARD", 5: "SELL", 6: "PASS",
    7: "EQUIP_FROM_INVENTORY", 8: "CRAFT_AND_EQUIP",
}
# The intended tuning scope is BUY_XP/PASS/REROLL in selected economic cohorts.
# All other action families are explicitly audited as non-target behavior.
NON_TARGET_TYPES = {0, 3, 4, 5, 7, 8}


def read_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if line.strip():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"JSONL inválido em {path}:{line_number}: {exc}") from exc


def js_divergence(p, q):
    eps = 1e-12
    p = [max(eps, float(x)) for x in p]
    q = [max(eps, float(x)) for x in q]
    ps, qs = sum(p), sum(q)
    p = [x / ps for x in p]
    q = [x / qs for x in q]
    m = [(a + b) / 2 for a, b in zip(p, q)]
    return 0.5 * (
        sum(a * math.log(a / middle) for a, middle in zip(p, m))
        + sum(a * math.log(a / middle) for a, middle in zip(q, m))
    )


def build_report(rows, paired_rows=None, metadata=None, training_summary=None):
    total = action_divergences = non_target_states = non_target_divergences = 0
    conditional_argument_changes = 0
    type_divergences = []
    by_scenario = defaultdict(lambda: {"rows": 0, "action_diff": 0, "js": []})
    by_strategy = defaultdict(lambda: {"rows": 0, "different": 0, "non_target": 0, "non_target_diff": 0})
    original_counts, tuned_counts = Counter(), Counter()
    for row in rows:
        total += 1
        original_action = row.get("original_action", [6, 0, 0, 0, 0, 0])
        tuned_action = row.get("finetuned_action", [6, 0, 0, 0, 0, 0])
        original_type, tuned_type = int(original_action[0]), int(tuned_action[0])
        original_counts[original_type] += 1
        tuned_counts[tuned_type] += 1
        differs = original_action != tuned_action
        action_divergences += int(differs)
        if original_type == tuned_type and original_action[1:] != tuned_action[1:]:
            conditional_argument_changes += 1
        non_target = original_type in NON_TARGET_TYPES or tuned_type in NON_TARGET_TYPES
        if non_target:
            non_target_states += 1
            non_target_divergences += int(differs)

        p = row.get("original_type_probabilities")
        q = row.get("finetuned_type_probabilities")
        divergence = None
        if p and q and len(p) == len(q):
            divergence = js_divergence(p, q)
            type_divergences.append(divergence)

        state = row.get("state", {})
        strategy = state.get("strategy_name", "UNKNOWN")
        bucket = by_strategy[strategy]
        bucket["rows"] += 1
        bucket["different"] += int(differs)
        bucket["non_target"] += int(non_target)
        bucket["non_target_diff"] += int(non_target and differs)
        for scenario_id in row.get("scenario_ids", []):
            item = by_scenario[scenario_id]
            item["rows"] += 1
            item["action_diff"] += int(differs)
            if divergence is not None:
                item["js"].append(divergence)

    action_lines = ["| Ação | Original | Fine-tuned | Diferença |",
                    "|---|---:|---:|---:|"]
    for action_type in range(9):
        a, b = original_counts[action_type], tuned_counts[action_type]
        action_lines.append(
            f"| {ACTION_NAMES[action_type]} | {a} | {b} | {b-a:+d} |"
        )

    strategy_lines = ["| Estratégia | Estados | Ações diferentes | Divergência |",
                      "|---|---:|---:|---:|"]
    for strategy, item in sorted(by_strategy.items()):
        rate = item["different"] / item["rows"] if item["rows"] else 0.0
        strategy_lines.append(
            f"| {strategy} | {item['rows']} | {item['different']} | {rate:.1%} |"
        )

    preservation_lines = [
        "| Família fora do alvo | Original | Fine-tuned | Diferença |",
        "|---|---:|---:|---:|",
    ]
    for action_type in sorted(NON_TARGET_TYPES):
        a, b = original_counts[action_type], tuned_counts[action_type]
        preservation_lines.append(
            f"| {ACTION_NAMES[action_type]} | {a} | {b} | {b-a:+d} |"
        )

    scenario_lines = ["| Cenário | Estados | Ações divergentes | Taxa | JS média |",
                      "|---|---:|---:|---:|---:|"]
    for scenario_id, item in sorted(by_scenario.items()):
        count = item["rows"]
        rate = item["action_diff"] / count if count else 0.0
        mean_js = sum(item["js"]) / len(item["js"]) if item["js"] else None
        js_text = f"{mean_js:.5f}" if mean_js is not None else "n/a"
        scenario_lines.append(
            f"| {scenario_id} | {count} | {item['action_diff']} | {rate:.1%} | {js_text} |"
        )

    mean_js = sum(type_divergences) / len(type_divergences) if type_divergences else None
    action_rate = action_divergences / total if total else 0.0
    non_target_rate = non_target_divergences / non_target_states if non_target_states else None
    status = (
        "INCONCLUSIVO" if total == 0 or non_target_rate is None
        else "INVESTIGAR ALTERAÇÕES FORA DO ESCOPO" if non_target_rate > 0.05
        else "SEM ALERTA AUTOMÁTICO — REVISÃO DE CONSEQUÊNCIAS OBRIGATÓRIA"
    )

    paired_section = "## Partidas completas pareadas\\n\\nNenhum arquivo de partidas pareadas foi fornecido.\\n"
    if paired_rows is not None:
        deltas = [float(item.get("mean_reward_delta", 0.0)) for item in paired_rows]
        completed_rows = [item for item in paired_rows if item.get("both_completed")]
        completed = len(completed_rows)
        paired_mean = sum(deltas) / len(deltas) if deltas else None
        paired_mean_text = f"{paired_mean:.5f}" if paired_mean is not None else "n/a"
        player_rows = [
            player for match in completed_rows
            for player in match.get("final_player_deltas", [])
        ]

        def mean_metric(key):
            values = [
                float(player[key]) for player in player_rows
                if player.get(key) is not None
            ]
            return sum(values) / len(values) if values else None

        def metric_text(value):
            return f"{value:+.3f}" if value is not None else "n/a"

        def percent_text(value):
            return f"{value * 100:.1f}%" if value is not None else "n/a"

        placement_delta = mean_metric("placement_delta")
        top4_original = mean_metric("original_top4")
        top4_tuned = mean_metric("finetuned_top4")
        win_original = (
            sum(1 for player in player_rows if player.get("original_placement") == 1) / len(player_rows)
            if player_rows else None
        )
        win_tuned = (
            sum(1 for player in player_rows if player.get("finetuned_placement") == 1) / len(player_rows)
            if player_rows else None
        )
        paired_lines = []
        for item in paired_rows:
            players = item.get("final_player_deltas", [])
            seed_placement = [
                float(player["placement_delta"]) for player in players
                if player.get("placement_delta") is not None
            ]
            seed_top4_orig = [
                bool(player["original_top4"]) for player in players
                if player.get("original_top4") is not None
            ]
            seed_top4_tuned = [
                bool(player["finetuned_top4"]) for player in players
                if player.get("finetuned_top4") is not None
            ]
            placement_text = (
                f"{sum(seed_placement) / len(seed_placement):+.2f}"
                if seed_placement else "n/a"
            )
            top4_text = (
                f"{sum(seed_top4_orig)}/{len(seed_top4_orig)} → "
                f"{sum(seed_top4_tuned)}/{len(seed_top4_tuned)}"
                if seed_top4_orig and seed_top4_tuned else "n/a"
            )
            paired_lines.append(
                f"| {item.get('seed')} | {float(item.get('mean_reward_delta', 0.0)):+.5f} | "
                f"{placement_text} | {top4_text} | "
                f"{'Sim' if item.get('both_completed') else 'Não'} |"
            )
        paired_section = (
            "## Partidas completas pareadas\\n\\n"
            f"- Seeds avaliadas: **{len(paired_rows)}**\\n"
            f"- Ambas as partidas concluídas: **{completed}/{len(paired_rows)}**\\n"
            f"- Pares jogador/seed com colocação comparável: **{len(player_rows)}**\\n"
            f"- Diferença média de reward (fine-tuned - original): **{paired_mean_text}**\\n"
            f"- Diferença média de colocação (fine-tuned - original): **{metric_text(placement_delta)}** (negativo é melhor)\\n"
            f"- Taxa Top 4: **{percent_text(top4_original)} → {percent_text(top4_tuned)}**\\n"
            f"- Taxa de vitória: **{percent_text(win_original)} → {percent_text(win_tuned)}**\\n"
            f"- Delta médio de HP/ouro/nível/estrutura: **{metric_text(mean_metric('hp_delta'))} / "
            f"{metric_text(mean_metric('gold_delta'))} / {metric_text(mean_metric('level_delta'))} / "
            f"{metric_text(mean_metric('board_structural_score_delta'))}**\\n\\n"
            "| Seed | Reward delta médio | Placement delta médio | Top 4 original → fine-tuned | Ambas concluídas |\\n"
            "|---:|---:|---:|:---:|:---:|\\n"
            + "\\n".join(paired_lines)
            + "\\n\\nPlacement é calculada pelo ranking terminal nativo; partidas incompletas não entram nas métricas de colocação.\\n"
        )

    provenance_section = "## Proveniência do experimento\\n\\nMetadados não fornecidos.\\n"
    if metadata is not None or training_summary is not None:
        metadata = metadata or {}
        training_summary = training_summary or {}
        params = metadata.get("ppo_parameters", {})
        parameter_lines = [
            f"- {key}: `{value}`" for key, value in sorted(params.items())
        ]
        provenance_section = (
            "## Proveniência do experimento\\n\\n"
            f"- Commit do repositório/engine: `{metadata.get('repository_commit', 'n/a')}`\\n"
            f"- SHA-256 checkpoint original: `{metadata.get('checkpoint_sha256', 'n/a')}`\\n"
            f"- SHA-256 checkpoint fine-tuned: `{metadata.get('finetuned_checkpoint_sha256', training_summary.get('finetuned_checkpoint_sha256', 'n/a'))}`\\n"
            f"- SHA-256 RewardModel: `{metadata.get('reward_model_source_sha256', 'n/a')}`\\n"
            f"- SHA-256 TftEngine: `{metadata.get('engine_source_sha256', 'n/a')}`\\n"
            f"- Cenário: **{metadata.get('selected_scenario', training_summary.get('selected_scenario', 'n/a'))}**\\n"
            f"- Transições do cenário: **{training_summary.get('selected_scenario_transitions', 'n/a')}**\\n"
            f"- PPO optimizer steps: **{training_summary.get('optimizer_steps_total', 'n/a')}**\\n"
            f"- SHA-256 config: `{metadata.get('config_sha256', 'n/a')}`\\n"
            + ("\\n".join(parameter_lines) + "\\n" if parameter_lines else "")
        )

    js_text = f"{mean_js:.6f}" if mean_js is not None else "n/a"
    non_target_text = f"{non_target_rate:.1%}" if non_target_rate is not None else "n/a"
    return f"""# Auditoria de Fine-tuning Econômico

> Gerado a partir de `decision_trace.jsonl`. A comparação shadow usa o mesmo estado e as mesmas máscaras.

## Resumo executivo

- Estados comparados: **{total}**
- Ações completas diferentes: **{action_divergences} ({action_rate:.1%})**
- Mudanças de argumentos com mesmo tipo de ação: **{conditional_argument_changes}**
- Divergência JS média da cabeça de tipo: **{js_text}**
- Estados em que ao menos uma ação é fora do escopo: **{non_target_states}**
- Divergência entre esses estados: **{non_target_divergences} ({non_target_text})**
- Status preliminar: **{status}**

O limite de 5% é apenas um alerta de triagem para mudanças fora do escopo, não um critério universal de aprovação.

## Frequência de todas as ações

{chr(10).join(action_lines)}

## Preservação das famílias não treinadas

{chr(10).join(preservation_lines)}

## Preservação por estratégia

{chr(10).join(strategy_lines)}

## Cenários econômicos

{chr(10).join(scenario_lines)}

{paired_section}

{provenance_section}

## Interpretação e limitações

- Ação divergente inclui mudanças em qualquer um dos seis componentes, inclusive slot, origem ou destino.
- A preservação das famílias não treinadas é medida por ação executada e divergência por estado; a tabela de frequência não prova qualidade.
- A divergência JS compara somente a distribuição da cabeça de tipo, não todas as distribuições condicionais autorregressivas.
- Cabeças de loja, venda, banco, tabuleiro e itens permanecem congeladas no treinamento padrão; ainda assim, sua seleção pode mudar se o tipo de ação mudar.
- Cenários de monitoramento não recebem recompensa artificial.
- Estados-alvo são encontrados durante simulação nativa; a engine atual não oferece injeção pública de estado inicial.
- Zero ocorrências significa **não coberto**, não preservação comprovada.
- A comparação shadow não substitui partidas completas pareadas, pois as trajetórias divergem após ações diferentes.

## Critério de aprovação

Aprovação exige ganho econômico demonstrado, amostra suficiente, ausência de regressão relevante nas decisões fora do escopo, partidas completas pareadas concluídas e generalização em seeds não usadas no treino. Este relatório isoladamente não promove o checkpoint.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", required=True, help="JSONL de decisões da execução")
    parser.add_argument("--paired", default=None, help="JSONL opcional de partidas completas pareadas")
    parser.add_argument("--metadata", default=None, help="experiment_config.json da execução")
    parser.add_argument("--summary", default=None, help="training_summary.json da execução")
    parser.add_argument("--output", default="economy_finetuning/reports/ECONOMY_FINETUNING_AUDIT.md")
    args = parser.parse_args()
    trace = Path(args.trace)
    if not trace.is_file():
        raise FileNotFoundError(trace)
    paired_path = Path(args.paired) if args.paired else None
    paired_rows = list(read_jsonl(paired_path)) if paired_path and paired_path.is_file() else None
    metadata_path = Path(args.metadata) if args.metadata else None
    summary_path = Path(args.summary) if args.summary else None
    metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path and metadata_path.is_file() else None
    training_summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path and summary_path.is_file() else None
    report = build_report(read_jsonl(trace), paired_rows, metadata, training_summary)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Auditoria gerada: {output}")


if __name__ == "__main__":
    main()
