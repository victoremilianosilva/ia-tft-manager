#!/usr/bin/env python3
"""Analyze per-player JSONL output from scripts/audit_strategic_policy.py.

Run:
  python scripts/analyze_strategic_policy.py --input-dir reports/strategic_policy

Produces Markdown and JSON summaries. Flags patterns for review, not proof that
an alternative action was better. The current audit schema lacks full board/shop
snapshots and composition-direction fields, which are noted in the report.
"""
from __future__ import annotations
import argparse, json, math, statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

# Verify these labels against the current C++ action enum before treating counts as official.
ACTION_NAMES = {0: "buy", 1: "sell", 2: "reroll", 3: "move_bench", 4: "move_board", 5: "other_5", 6: "pass"}
MOVE_TYPES = {3, 4}

def read_jsonl(path: Path):
    rows, errors = [], []
    try:
        with path.open("r", encoding="utf-8-sig") as f:
            for n, line in enumerate(f, 1):
                if not line.strip(): continue
                try:
                    obj = json.loads(line)
                    if isinstance(obj, dict): rows.append(obj)
                    else: errors.append(f"{path.name}:{n}: registro não é objeto JSON")
                except json.JSONDecodeError as exc:
                    errors.append(f"{path.name}:{n}: JSON inválido ({exc.msg})")
    except OSError as exc: errors.append(f"{path}: erro de leitura ({exc})")
    return rows, errors

def integer(v: Any, default=None):
    try: return default if v is None else int(v)
    except (TypeError, ValueError, OverflowError): return default

def number(v: Any):
    try:
        n = float(v)
        return n if math.isfinite(n) else None
    except (TypeError, ValueError, OverflowError): return None

def get_action(row):
    a = row.get("action")
    if isinstance(a, dict):
        keys = ("type", "shop_slot", "bench_slot", "board_target", "board_source", "conditioned_board_target")
        vals = [integer(a.get(k)) for k in keys]
        return [int(v or 0) for v in vals] if vals[0] is not None else None
    if isinstance(a, (list, tuple)) and a: return [integer(v, 0) or 0 for v in a]
    return None

def diagnostic_items(row):
    d = row.get("diagnostics")
    if isinstance(d, dict): return [d]
    if isinstance(d, list): return [x for x in d if isinstance(x, dict)]
    return []

def inspect_diagnostics(row):
    checked, violations, probs, not_top1 = 0, [], [], 0
    for d in diagnostic_items(row):
        selected, mask = integer(d.get("selected")), d.get("mask")
        if selected is not None and isinstance(mask, list) and 0 <= selected < len(mask):
            checked += 1
            try:
                if not bool(mask[selected]): violations.append(f"{d.get('head', '?')}: selected={selected}, mask=0")
            except (TypeError, ValueError): pass
        p, values = number(d.get("selected_probability")), d.get("probabilities")
        if p is None and selected is not None and isinstance(values, list) and 0 <= selected < len(values):
            p = number(values[selected])
        if p is not None: probs.append(p)
        top = d.get("top_choices")
        if selected is not None and isinstance(top, list) and top and isinstance(top[0], dict):
            if integer(top[0].get("index")) != selected: not_top1 += 1
    return checked, violations, probs, not_top1

def analyze_player(pid, rows):
    rows.sort(key=lambda r: (integer(r.get("seed"), 0) or 0, integer(r.get("step"), 0) or 0))
    counts, gold_delta, action_rewards, total_rewards, selected_probs = Counter(), [], [], [], []
    mask_checks, mask_violations, not_top1, missing_actions = 0, [], 0, 0
    rounds, movements, signatures = set(), defaultdict(list), defaultdict(list)
    confirmed_cycles, actual_unit_moves, composition_changes = [], 0, 0
    for row in rows:
        seed = integer(row.get("seed"), 0) or 0
        step = integer(row.get("step"), 0) or 0
        rnd = integer(row.get("round_after", row.get("round_before", row.get("round"))), 0) or 0
        rounds.add((seed, rnd))
        a, active = get_action(row), row.get("alive_at_decision") is not False
        sig = tuple(a) if a is not None else None
        signatures[(seed, rnd)].append(sig)
        if a is None: missing_actions += 1
        elif active:
            counts[ACTION_NAMES.get(a[0], f"type_{a[0]}")] += 1
            if a[0] in MOVE_TYPES: movements[(seed, rnd)].append(sig)
        before, after = number(row.get("gold_before")), number(row.get("gold_after"))
        if active and before is not None and after is not None: gold_delta.append(after-before)
        for key, target in (("action_reward", action_rewards), ("total_reward", total_rewards)):
            val = number(row.get(key))
            if active and val is not None: target.append(val)
        cycle = row.get("loop_detected")
        if isinstance(cycle, dict):
            confirmed_cycles.append({
                "seed": seed, "step": step,
                "previous_step": integer(cycle.get("previous_step")),
                "cycle_length": integer(cycle.get("cycle_length")),
                "action": a,
            })
        changes = row.get("unit_changes")
        if isinstance(changes, dict):
            actual_unit_moves += len(changes.get("moved_units", []) or [])
        comp = row.get("composition_delta")
        if isinstance(comp, dict) and (comp.get("board_units_changed") or comp.get("strategy_fields_changed")):
            composition_changes += 1
        checked, bad, probs, nt1 = inspect_diagnostics(row)
        mask_checks += checked
        mask_violations.extend(f"seed={seed} step={step}: {v}" for v in bad)
        selected_probs.extend(probs); not_top1 += nt1

    loops = []
    for (seed, rnd), moves in movements.items():
        for sig, n in Counter(moves).items():
            if n >= 3: loops.append(f"seed={seed} round={rnd}: movimento idêntico {n}x: {list(sig)}")
        for i in range(len(moves)-3):
            w = moves[i:i+4]
            if w[0] == w[2] and w[1] == w[3] and w[0] != w[1]:
                loops.append(f"seed={seed} round={rnd}: padrão alternado em 4 movimentos: {w}"); break
    for (seed, rnd), seq in signatures.items():
        prev, streak = None, 0
        for sig in seq + [None]:
            if sig is not None and sig == prev: streak += 1
            else:
                if streak >= 3 and prev and prev[0] in MOVE_TYPES:
                    loops.append(f"seed={seed} round={rnd}: sequência de movimento idêntico {streak}x: {list(prev)}")
                prev, streak = sig, 1
    active_rows = [r for r in rows if r.get("alive_at_decision") is not False]
    mean = lambda xs: statistics.mean(xs) if xs else None
    return {
        "player_id": pid, "records": len(rows), "active_records": len(active_rows),
        "seeds": sorted({integer(r.get("seed"), 0) or 0 for r in rows}), "rounds_seen": len(rounds),
        "action_counts": dict(counts), "movement_actions": counts.get("move_bench",0)+counts.get("move_board",0),
        "pass_actions": counts.get("pass",0), "gold_delta_mean": mean(gold_delta),
        "gold_delta_negative_steps": sum(x<0 for x in gold_delta), "gold_delta_positive_steps": sum(x>0 for x in gold_delta),
        "action_reward_mean": mean(action_rewards), "action_reward_negative_steps": sum(x<0 for x in action_rewards),
        "total_reward_mean": mean(total_rewards), "diagnostic_heads_checked": mask_checks,
        "mask_violations": len(mask_violations), "mask_violation_examples": mask_violations[:20],
        "selected_probability_mean": mean(selected_probs), "selected_probability_below_005": sum(x<.05 for x in selected_probs),
        "selected_not_top1_count": not_top1, "missing_action_records": missing_actions, "loop_suspicions": loops,
        "confirmed_state_cycles": confirmed_cycles, "confirmed_state_cycle_count": len(confirmed_cycles),
        "actual_unit_moves": actual_unit_moves, "composition_change_steps": composition_changes,
    }

def fmt(v):
    return "n/d" if v is None else f"{v:.3f}" if isinstance(v, float) else str(v)

def markdown_report(summaries, errors, total):
    out = ["# Auditoria estratégica TFT", "", f"- Registros válidos: **{total}**",
      f"- Jogadores listados: **{len(summaries)}**", f"- Erros de leitura: **{len(errors)}**", "",
      "> Alertas são indícios para revisão, não prova de que outra ação seria melhor.", "",
      "## Resumo por jogador", "",
      "| Jogador | Ativos | Seeds | Ações de movimento | Unidades movidas | Passes | Δ ouro médio | Recompensa média | Suspeitas | Ciclos confirmados | Máscara inválida |",
      "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for s in summaries:
        out.append(f"| {s['player_id']} | {s['active_records']} | {len(s['seeds'])} | {s['movement_actions']} | {s['actual_unit_moves']} | {s['pass_actions']} | {fmt(s['gold_delta_mean'])} | {fmt(s['action_reward_mean'])} | {len(s['loop_suspicions'])} | {s['confirmed_state_cycle_count']} | {s['mask_violations']} |")
    out += ["", "## Detalhes e alertas", ""]
    for s in summaries:
        out += [f"### Jogador {s['player_id']}", f"- Contagem de ações: {s['action_counts'] or 'nenhuma'}",
          f"- Variações de ouro positivas/negativas: {s['gold_delta_positive_steps']}/{s['gold_delta_negative_steps']}",
          f"- Probabilidade média selecionada: {fmt(s['selected_probability_mean'])}; abaixo de 0,05: {s['selected_probability_below_005']}",
          f"- Cabeças com máscara verificável: {s['diagnostic_heads_checked']}; violações: {s['mask_violations']}",
          f"- Seleções diferentes da opção top-1: {s['selected_not_top1_count']}",
          f"- Movimentos reais de unidade reconstruídos: {s['actual_unit_moves']}",
          f"- Steps com mudança de composição/estratégia: {s['composition_change_steps']}",
          f"- Ciclos confirmados por retorno ao mesmo estado: {s['confirmed_state_cycle_count']}"]
        out += [f"- **Ciclo confirmado:** seed={x['seed']} step={x['step']} retorno ao estado do step={x['previous_step']} (comprimento {x['cycle_length']})" for x in s["confirmed_state_cycles"]]
        out += [f"- **Possível loop por padrão de ação (não confirmado):** {x}" for x in s["loop_suspicions"]]
        out.append("")
    out += ["## Limitações dos dados", "",
      "- O JSONL registra ação, round, ouro antes/depois, recompensas, máscaras e diagnósticos.",
      "- O schema v2 inclui snapshots antes/depois de tabuleiro, banco e loja; identidade da unidade, origem/destino, estratégia e diferenças de composição.",
      "- Ciclo confirmado significa retorno ao mesmo estado de tabuleiro+banco (incluindo UUIDs expostos pela engine), não prova por si só que a ação foi estrategicamente ruim.",
      "- Quando a engine não expõe UUID, o fallback champion/ordinal tem confiança menor e pode não distinguir cópias idênticas.",
      "- A máscara só pode ser validada quando diagnostics contém mask e selected. Ausência de diagnóstico não conta como violação.",
      "- A variação líquida de ouro não é necessariamente o custo da ação.",
      "- Os rótulos de ações 0–6 são hipóteses; confirme os enums atuais da engine antes de usar as contagens oficialmente.", "", "## Erros de leitura", ""]
    out += [f"- {e}" for e in errors] if errors else ["Nenhum."]
    return "\n".join(out) + "\n"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input-dir", type=Path, default=Path("reports/strategic_policy"))
    p.add_argument("--pattern", default="player_*.jsonl")
    p.add_argument("--out-dir", type=Path, default=Path("reports/strategic_analysis"))
    args = p.parse_args()
    files = sorted(args.input_dir.glob(args.pattern))
    if not files: p.error(f"Nenhum arquivo encontrado: {args.input_dir / args.pattern}")
    errors, grouped, total = [], defaultdict(list), 0
    for path in files:
        rows, errs = read_jsonl(path); errors.extend(errs); total += len(rows)
        file_pid = integer(path.stem.removeprefix("player_")) if path.stem.startswith("player_") else None
        for row in rows:
            pid = integer(row.get("player_id"), file_pid)
            if pid is None: errors.append(f"{path.name}: registro sem player_id"); continue
            if file_pid is not None and pid != file_pid:
                errors.append(f"{path.name}: contém jogador {pid}, mas nome indica {file_pid}")
            grouped[pid].append(row)
    summaries = [analyze_player(pid, grouped.get(pid, [])) for pid in sorted(set(range(8)) | set(grouped))]
    report = markdown_report(summaries, errors, total)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    md, js = args.out_dir/"strategic_audit.md", args.out_dir/"strategic_audit.json"
    md.write_text(report, encoding="utf-8")
    js.write_text(json.dumps({"input_files":[str(f) for f in files],"records_total":total,"read_errors":errors,"players":summaries}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Arquivos: {len(files)} | registros válidos: {total}")
    print(f"Relatório Markdown: {md}\nRelatório JSON: {js}")
    if total == 0: print("ATENÇÃO: nenhum registro lido; confira se os JSONL estão vazios ou o diretório está correto.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
