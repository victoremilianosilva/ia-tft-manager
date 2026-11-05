"""Generate a compact Markdown audit from fine-tuning JSONL traces."""
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
ECONOMIC_TYPES = {0, 1, 2, 5, 6}


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
    kl_pm = sum(a * math.log(a / b) for a, b in zip(p, m))
    kl_qm = sum(a * math.log(a / b) for a, b in zip(q, m))
    return 0.5 * (kl_pm + kl_qm)


def build_report(rows, paired_rows=None):
    total = 0
    type_divergences = []
    action_divergences = 0
    by_scenario = defaultdict(lambda: {"rows": 0, "action_diff": 0, "js": []})
    action_counts = {"original": Counter(), "finetuned": Counter()}
    category = defaultdict(lambda: {"rows": 0, "different": 0})
    for row in rows:
        total += 1
        original = row.get("original_action", [6])[0]
        candidate = row.get("finetuned_action", [6])[0]
        action_counts["original"][ACTION_NAMES.get(int(original), str(original))] += 1
        action_counts["finetuned"][ACTION_NAMES.get(int(candidate), str(candidate))] += 1
        differs = row.get("original_action") != row.get("finetuned_action")
        action_divergences += int(differs)
        p = row.get("original_type_probabilities")
        q = row.get("finetuned_type_probabilities")
        if p and q and len(p) == len(q):
            divergence = js_divergence(p, q)
            type_divergences.append(divergence)
        else:
            divergence = None
        state = row.get("state", {})
        strategy = state.get("strategy_name", "UNKNOWN")
        bucket = category[strategy]
        bucket["rows"] += 1
        bucket["different"] += int(differs)
        for scenario_id in row.get("scenario_ids", []):
            item = by_scenario[scenario_id]
            item["rows"] += 1
            item["action_diff"] += int(differs)
            if divergence is not None:
                item["js"].append(divergence)

    def action_table():
        names = sorted(set(action_counts["original"]) | set(action_counts["finetuned"]))
        lines = ["| Ação | Original | Fine-tuned | Diferença |", "|---|---:|---:|---:|"]
        for name in names:
            a = action_counts["original"][name]
            b = action_counts["finetuned"][name]
            lines.append(f"| {name} | {a} | {b} | {b-a:+d} |")
        return "\n".join(lines)

    scenario_lines = ["| Cenário | Estados | Ações divergentes | Taxa | JS média |",
                      "|---|---:|---:|---:|---:|"]
    for scenario_id, item in sorted(by_scenario.items()):
        count = item["rows"]
        rate = item["action_diff"] / count if count else 0.0
        mean_js = sum(item["js"]) / len(item["js"]) if item["js"] else float("nan")
        scenario_lines.append(
            f"| {scenario_id} | {count} | {item['action_diff']} | {rate:.1%} | "
            f"{mean_js:.5f} |" if math.isfinite(mean_js) else
            f"| {scenario_id} | {count} | {item['action_diff']} | {rate:.1%} | n/a |"
        )

    strategy_lines = ["| Estratégia | Estados | Ações diferentes | Divergência |",
                      "|---|---:|---:|---:|"]
    for strategy, item in sorted(category.items()):
        rate = item["different"] / item["rows"] if item["rows"] else 0.0
        strategy_lines.append(
            f"| {strategy} | {item['rows']} | {item['different']} | {rate:.1%} |"
        )

    mean_js = sum(type_divergences) / len(type_divergences) if type_divergences else float("nan")
    action_rate = action_divergences / total if total else 0.0
    status = "INCONCLUSIVO" if total == 0 else "REVISAR ALTERAÇÕES" if action_rate > 0.10 else "SEM ALERTA GLOBAL"
    paired_section = "## Partidas completas pareadas\\n\\nNenhum arquivo de partidas pareadas foi fornecido.\\n"
    if paired_rows is not None:
        deltas = [float(item.get("mean_reward_delta", 0.0)) for item in paired_rows]
        completed = sum(bool(item.get("both_completed")) for item in paired_rows)
        paired_mean = sum(deltas) / len(deltas) if deltas else float("nan")
        paired_section = (
            "## Partidas completas pareadas\\n\\n"
            f"- Seeds avaliadas: **{len(paired_rows)}**\\n"
            f"- Ambas as partidas concluídas: **{completed}/{len(paired_rows)}**\\n"
            f"- Diferença média de reward (fine-tuned - original): **{paired_mean:.5f}**\\n\\n"
            "| Seed | Reward delta médio | Ambas concluídas |\\n|---:|---:|:---:|\\n"
            + "\\n".join(
                f"| {item.get('seed')} | {float(item.get('mean_reward_delta', 0.0)):+.5f} | "
                f"{'Sim' if item.get('both_completed') else 'Não'} |"
                for item in paired_rows
            )
            + "\\n\\nReward é reportado como a soma nativa por jogador; não deve ser interpretado como colocação sem validar o schema terminal.\\n"
        )

    return f"""# Auditoria de Fine-tuning Econômico

> Relatório gerado automaticamente a partir de `decision_trace.jsonl`.
> Esta auditoria compara as políticas nos mesmos estados observados; não substitui partidas completas pareadas.

## Resumo executivo

- Estados comparados: **{total}**
- Ações completas diferentes: **{action_divergences} ({action_rate:.1%})**
- Jensen-Shannon média das distribuições de tipo: **{mean_js:.6f}** (n/a quando não há amostras)
- Status preliminar de preservação: **{status}**

O status é um alerta de triagem, não uma aprovação automática. A interpretação deve considerar tamanho da amostra, contexto, estratégia e consequências em partidas completas.

## Frequência de ações

{action_table()}

## Preservação por estratégia

{chr(10).join(strategy_lines)}

## Cenários econômicos

{chr(10).join(scenario_lines)}

{paired_section}

## Interpretação e limitações

- A comparação de ações usa vetores completos de seis componentes; mudanças de slot/destino também contam como divergência.
- A divergência JS compara a distribuição da cabeça de tipo, não todas as distribuições condicionais autorregressivas.
- Cabeças de loja, banco, tabuleiro e itens permanecem congeladas no treinamento padrão, mas suas escolhas podem mudar quando a cabeça de tipo muda.
- Este relatório não afirma que uma ação divergente é melhor. O resultado precisa ser confrontado com a avaliação de partidas completas.
- Cenários de monitoramento não recebem recompensa artificial.
- Estados-alvo são encontrados durante simulação nativa; o motor atual não oferece injeção pública de estado inicial.
- Uma amostra pequena ou ausência de ocorrência de um cenário deve ser classificada como **dados insuficientes**, nunca como preservação comprovada.

## Critério de aprovação

Aprovação exige melhoria econômica demonstrada, amostra suficiente, ausência de regressão relevante por estratégia e validação pareada de partidas completas. Este relatório, isoladamente, não promove o checkpoint.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", default="economy_finetuning/runs/latest/logs/decision_trace.jsonl")
    parser.add_argument("--paired", default=None, help="JSONL opcional de partidas completas pareadas")
    parser.add_argument("--output", default="economy_finetuning/runs/latest/reports/ECONOMY_FINETUNING_AUDIT.md")
    args = parser.parse_args()
    trace = Path(args.trace)
    if not trace.is_file():
        raise FileNotFoundError(trace)
    paired_path = Path(args.paired) if args.paired else None
    paired_rows = list(read_jsonl(paired_path)) if paired_path and paired_path.is_file() else None
    report = build_report(read_jsonl(trace), paired_rows)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Auditoria gerada: {output}")


if __name__ == "__main__":
    main()
