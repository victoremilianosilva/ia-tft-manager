#!/usr/bin/env python3
"""Auditoria offline dos logs de uma partida TFT gerados pelo Viewer.

Aceita player_*_log.json estruturados e player_*_log.tft legados.
Gera audit_report.json e audit_report.md; não altera os logs originais.

Exemplos:
  python audit_viewer_match.py viewer/sessions/match-20261016-203216-43b53954
  python audit_viewer_match.py caminho/player_1_log.json --out-dir auditoria
  python audit_viewer_match.py viewer/sessions/match-... --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

ACTION_NAMES = {0: "BUY", 1: "REROLL", 2: "BUY_XP", 3: "MOVE_BENCH",
                4: "MOVE_BOARD", 5: "SELL", 6: "PASS"}
MOVE_RE = re.compile(
    r"MOVE\s+(Bench\s*->\s*Board|Board\s*->\s*Board):\s*(.*?)\s*<->\s*(.*?)\s*\|\s*Rew:\s*([+-]?\d+(?:\.\d+)?)",
    re.IGNORECASE,
)
ROUND_RE = re.compile(r"FIM DO ROUND\s+(\d+)-(\d+)\s*\|\s*GOLD:\s*(\d+)", re.I)
STRATEGY_RE = re.compile(r"STRATEGY:\s*([^|]+)\|\s*COMP DIRECTION:\s*([^|]+)\|\s*FOCUS:\s*(.+)", re.I)


def add_issue(report: dict, severity: str, code: str, player: str, rnd: str,
              step: Any, message: str, evidence: Any = None) -> None:
    report["issues"].append({
        "severity": severity, "code": code, "player": player, "round": rnd or "?",
        "step": step, "message": message, "evidence": evidence,
    })


def get_round(entry: dict) -> str:
    if entry.get("stage") is not None and entry.get("round_in_stage") is not None:
        return f"{entry['stage']}-{entry['round_in_stage']}"
    return str(entry.get("round", "?"))


def get_state(entry: dict, field: str) -> dict:
    payload = entry.get("payload") or {}
    state = payload.get(field)
    if isinstance(state, dict):
        return state
    if field == "state_after" and isinstance(payload.get("state"), dict):
        return payload["state"]
    return {}


def unit_name(unit: Any) -> str:
    if not isinstance(unit, dict):
        return ""
    return str(unit.get("champion_id") or unit.get("apiName") or unit.get("name") or "").strip()


def is_occupied(unit: Any) -> bool:
    return isinstance(unit, dict) and unit.get("occupied", True) and bool(unit_name(unit))


def iter_units(state: dict, locations=("board", "bench")):
    for location in locations:
        units = state.get(location) or []
        if not isinstance(units, list):
            continue
        for slot, unit in enumerate(units):
            if is_occupied(unit):
                yield location, slot, unit


def signature(state: dict) -> tuple:
    result = []
    for location, slot, unit in iter_units(state):
        result.append((location, slot,
                       str(unit.get("uuid") or unit_name(unit)),
                       int(unit.get("star", 1) or 1)))
    return tuple(sorted(result))


def positions(state: dict) -> dict:
    result = {}
    for location, slot, unit in iter_units(state):
        ident = str(unit.get("uuid") or unit_name(unit))
        result[ident] = (location, slot, int(unit.get("star", 1) or 1))
    return result


def read_json(path: Path):
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[WARN] Falha lendo {path}: {exc}", file=sys.stderr)
        return None
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        print(f"[WARN] Formato não reconhecido em {path}", file=sys.stderr)
        return None
    return data


def _occupied_units(state: dict, location: str) -> list[dict]:
    return [u for u in (state.get(location) or [])
            if isinstance(u, dict) and u.get("occupied", True) and unit_name(u)]


def _board_power(state: dict) -> float:
    return sum(float(u.get("impact", 0.0) or 0.0)
               for u in _occupied_units(state, "board"))


def _star_counts(state: dict) -> Counter:
    return Counter(int(u.get("star", 1) or 1)
                   for u in _occupied_units(state, "board") + _occupied_units(state, "bench"))


def _pair_count(state: dict) -> int:
    counts = Counter(unit_name(u).casefold()
                     for u in _occupied_units(state, "board") + _occupied_units(state, "bench")
                     if int(u.get("star", 1) or 1) == 1)
    return sum(1 for count in counts.values() if count >= 2)


def audit_purchase_sequences(entries: list[dict], player: str, report: dict) -> None:
    """Correlate buys and sells by champion across the next 1/2/4 player actions."""
    actions = []
    for entry in sorted(entries, key=lambda e: (e.get("sequence_id", 0), e.get("step", 0))):
        if not isinstance(entry, dict) or entry.get("event_type") != "action":
            continue
        payload = entry.get("payload") or {}
        action = payload.get("action") or []
        if action:
            actions.append((entry, payload, action))

    metrics = {
        "buys": 0, "sells": 0, "reversed_1": 0, "reversed_2": 0, "reversed_4": 0,
        "net_gold_lost_reversed": 0, "upgrade_completing_buys": 0,
        "buys_with_positive_comp_fit": 0, "buys_with_board_gain": 0,
        "core_or_pair_sales": 0, "classified_sales": {}, "purchase_records": [],
    }
    purchases = []
    classifications = Counter()
    for idx, (entry, payload, action) in enumerate(actions):
        before, after = payload.get("state_before") or {}, payload.get("state_after") or {}
        name = str(payload.get("action_name") or ACTION_NAMES.get(action[0], "UNKNOWN"))
        rnd, step = get_round(entry), entry.get("step")
        if name == "BUY" and len(action) > 1:
            shop = before.get("shop") or []
            slot = int(action[1])
            unit = shop[slot] if 0 <= slot < len(shop) else None
            if not isinstance(unit, dict) or not unit.get("occupied", True):
                continue
            champion = unit_name(unit)
            fit = ((payload.get("composition_diagnostics") or {}).get("unit_fit") or {})
            fit_score = float(fit.get("focus_fit_score", 0.0) or 0.0)
            upgrade_completed = _star_counts(after)[2] > _star_counts(before)[2]
            board_gain = _board_power(after) > _board_power(before) + 1e-6
            metrics["buys"] += 1
            metrics["upgrade_completing_buys"] += int(upgrade_completed)
            metrics["buys_with_positive_comp_fit"] += int(fit_score > 0)
            metrics["buys_with_board_gain"] += int(board_gain)
            record = {
                "champion": champion, "buy_action_index": idx, "step": step, "round": rnd,
                "cost": max(0, int(unit.get("cost", 0) or 0)), "fit_score": fit_score,
                "upgrade_completed": upgrade_completed, "pair_count_before": _pair_count(before),
                "pair_count_after": _pair_count(after), "board_power_before": _board_power(before),
                "board_power_after": _board_power(after), "gold_before": before.get("gold"),
                "gold_after": after.get("gold"), "comp_direction": after.get("comp_direction"),
                "sold": False, "classification": "NOT_REVERSED",
            }
            purchases.append(record)
            metrics["purchase_records"].append(record)
        elif name == "SELL" and len(action) > 2:
            bench = before.get("bench") or []
            slot = int(action[2])
            unit = bench[slot] if 0 <= slot < len(bench) else None
            if not isinstance(unit, dict) or not unit.get("occupied", True):
                continue
            champion = unit_name(unit)
            metrics["sells"] += 1
            if _pair_count(before) > _pair_count(after):
                metrics["core_or_pair_sales"] += 1
            match = next((p for p in reversed(purchases)
                          if not p["sold"] and p["champion"].casefold() == champion.casefold()
                          and 1 <= idx - p["buy_action_index"] <= 4), None)
            if match is None:
                classifications["UNKNOWN"] += 1
                continue
            distance = idx - match["buy_action_index"]
            bench_units = _occupied_units(before, "bench")
            bench_was_full = bool(before.get("bench")) and len(bench_units) >= len(before.get("bench") or [])
            comp_changed = (match.get("comp_direction") != before.get("comp_direction")
                            and bool(match.get("comp_direction") or before.get("comp_direction")))
            intervening = actions[match["buy_action_index"] + 1:idx + 1]
            deployed = any(any(unit_name(u).casefold() == champion.casefold()
                               for u in _occupied_units((item[1].get("state_after") or {}), "board"))
                           for item in intervening)
            if match["upgrade_completed"]:
                classification = "PURCHASE_UPGRADE"
            elif bench_was_full:
                classification = "BENCH_CAPACITY"
            elif comp_changed:
                classification = "COMP_TRANSITION"
            elif deployed:
                classification = "UNKNOWN"
            else:
                classification = "PURCHASE_REVERSED"
            match.update({"sold": True, "classification": classification, "sell_step": step,
                          "sell_round": rnd, "actions_to_sale": distance,
                          "sale_gold_delta": int(after.get("gold") or 0) - int(before.get("gold") or 0)})
            match["net_gold_lost"] = max(0, match["cost"] - match["sale_gold_delta"])
            classifications[classification] += 1
            if classification == "PURCHASE_REVERSED":
                metrics["net_gold_lost_reversed"] += match["net_gold_lost"]
                metrics["reversed_1"] += int(distance <= 1)
                metrics["reversed_2"] += int(distance <= 2)
                metrics["reversed_4"] += int(distance <= 4)
                add_issue(report, "MEDIUM", "PURCHASE_REVERSED", player, rnd, step,
                          f"Compra de {champion} desfeita em {distance} ação(ões), sem upgrade, implantação ou motivo de capacidade/composição demonstrado.",
                          {"buy_step": match["step"], "cost": match["cost"],
                           "sale_gold_delta": match["sale_gold_delta"],
                           "net_gold_lost": match["net_gold_lost"], "fit_score": match["fit_score"]})
    metrics["classified_sales"] = dict(classifications)
    report.setdefault("purchase_sequence_metrics", {})[player] = metrics


def audit_json(path: Path, doc: dict, report: dict, loop_window: int, comp_window: int) -> None:
    player_id = doc.get("player_number")
    if player_id is None:
        raw_id = doc.get("player_id")
        player_id = raw_id + 1 if isinstance(raw_id, int) else path.stem
    player = f"Jogador {player_id}"
    report["players_seen"].add(str(player_id))
    report["entries_read"] += len(doc["entries"])
    audit_purchase_sequences(doc["entries"], player, report)
    report["log_files"].append(str(path))

    entries = sorted(doc["entries"], key=lambda e: (e.get("sequence_id", 0), e.get("step", 0)))
    recent_moves = deque(maxlen=loop_window)
    state_visits = defaultdict(lambda: deque(maxlen=loop_window))
    comp_history = deque(maxlen=comp_window)
    last_comp_key = None
    last_churn_episode_step = None

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        event_type = str(entry.get("event_type", ""))
        step = entry.get("step")
        rnd = get_round(entry)
        payload = entry.get("payload") or {}
        before = get_state(entry, "state_before")
        after = get_state(entry, "state_after")
        if not after and event_type == "match_started":
            after = payload.get("state") or {}
        state = after or before

        if event_type == "action":
            action = payload.get("action") or []
            action_name = str(payload.get("action_name") or (
                ACTION_NAMES.get(action[0], "UNKNOWN") if action else "UNKNOWN"
            ))

            if action_name in ("MOVE_BENCH", "MOVE_BOARD") and before and after:
                sig = signature(after)
                previous = state_visits[sig]
                if previous:
                    try:
                        distance = int(step) - int(previous[-1]["step"])
                    except (TypeError, ValueError):
                        distance = 0
                    if 1 <= distance <= loop_window:
                        add_issue(report, "HIGH", "REPEATED_POSITION_AFTER_MOVE", player, rnd, step,
                                  f"Estado tabuleiro+banco repetido após movimento ({distance} passo(s)); possível loop.",
                                  {"previous_step": previous[-1]["step"], "signature": repr(sig)[:500]})
                state_visits[sig].append({"step": step, "round": rnd})

                old_pos, new_pos = positions(before), positions(after)
                moved = [(ident, old_pos.get(ident), new_pos.get(ident))
                         for ident in set(old_pos) | set(new_pos)
                         if old_pos.get(ident) != new_pos.get(ident)]
                recent_moves.append({"step": step, "round": rnd, "action": action_name,
                                     "moved": moved, "reward": payload.get("reward")})
                if len(recent_moves) >= 4:
                    tail = list(recent_moves)[-4:]
                    if all(len(item["moved"]) == 1 for item in tail):
                        ids = [item["moved"][0][0] for item in tail]
                        transitions = [(item["moved"][0][1], item["moved"][0][2]) for item in tail]
                        if (len(set(ids)) == 1 and transitions[0] == transitions[2]
                                and transitions[1] == transitions[3] and transitions[0] != transitions[1]):
                            add_issue(report, "CRITICAL", "UNIT_BACK_AND_FORTH", player, rnd, step,
                                      "A mesma unidade alternou entre duas posições em quatro movimentos consecutivos.",
                                      [{"step": x["step"], "transition": x["moved"][0][1:],
                                        "reward": x["reward"]} for x in tail])

            # Verifica fusão só com unidades já compradas: tabuleiro + banco.
            if after:
                counts = Counter()
                slots = defaultdict(list)
                for location, slot, unit in iter_units(after):
                    name = unit_name(unit).casefold()
                    star = int(unit.get("star", 1) or 1)
                    counts[(name, star)] += 1
                    slots[(name, star)].append(f"{location}[{slot}]")
                for (name, star), count in counts.items():
                    if star == 1 and count >= 3:
                        add_issue(report, "CRITICAL", "MISSING_ONE_TO_TWO_STAR_MERGE", player, rnd, step,
                                  f"{count} cópias 1★ de '{name}' no tabuleiro+banco após ação; fusão para 2★ aparentemente ausente.",
                                  {"copies": slots[(name, star)]})
                    elif star == 2 and count >= 3:
                        add_issue(report, "HIGH", "MISSING_TWO_TO_THREE_STAR_MERGE", player, rnd, step,
                                  f"{count} cópias 2★ de '{name}' no tabuleiro+banco; verifique fusão para 3★.",
                                  {"copies": slots[(name, star)]})

            # Diagnósticos da policy: sanidade numérica, não reconstitui máscaras.
            diagnostics = payload.get("policy_diagnostics")
            if not isinstance(diagnostics, (dict, list)) or not diagnostics:
                report["diagnostics_missing"] += 1
            elif isinstance(diagnostics, list):
                for item in diagnostics:
                    if not isinstance(item, dict):
                        continue
                    probs = item.get("probabilities")
                    if isinstance(probs, list) and probs:
                        numeric = [float(x) for x in probs if isinstance(x, (int, float))]
                        total = sum(numeric)
                        if numeric and abs(total - 1.0) > 0.03:
                            add_issue(report, "MEDIUM", "POLICY_PROBABILITY_SUM", player, rnd, step,
                                      f"Probabilidades somam {total:.4f}, esperado próximo de 1.",
                                      {"head": item.get("head"), "sum": total})
                    selected = item.get("selected_probability")
                    if isinstance(selected, (int, float)) and not 0 <= selected <= 1:
                        add_issue(report, "HIGH", "POLICY_SELECTED_PROBABILITY_RANGE", player, rnd, step,
                                  "selected_probability fora do intervalo [0, 1].", {"value": selected})

        if state and any(k in state for k in ("comp_direction", "strategy_name", "strategy_confidence")):
            comp = str(state.get("comp_direction") or "").strip()
            focus = str(state.get("comp_focus") or "").strip()
            strategy = str(state.get("strategy_name") or "").strip()
            confidence = state.get("strategy_confidence")
            scores = state.get("strategy_scores")
            core_units = state.get("core_units")
            if isinstance(confidence, (int, float)) and not 0 <= confidence <= 1:
                add_issue(report, "MEDIUM", "COMP_CONFIDENCE_RANGE", player, rnd, step,
                          "strategy_confidence fora de [0, 1].", {"value": confidence})
            if scores is not None and not isinstance(scores, dict):
                add_issue(report, "MEDIUM", "STRATEGY_SCORES_SHAPE", player, rnd, step,
                          "strategy_scores deveria ser objeto JSON.", {"type": type(scores).__name__})
            if core_units is not None and not isinstance(core_units, list):
                add_issue(report, "MEDIUM", "CORE_UNITS_SHAPE", player, rnd, step,
                          "core_units deveria ser lista.", {"type": type(core_units).__name__})
            if comp:
                comp_key = (comp, focus, strategy)
                if comp_key != last_comp_key:
                    comp_history.append({"step": step, "round": rnd, "comp": comp,
                                         "focus": focus, "strategy": strategy})
                    last_comp_key = comp_key
                    if len(comp_history) >= 4 and len({x["comp"] for x in comp_history}) >= 3:
                        if last_churn_episode_step is None or (isinstance(step, int) and isinstance(last_churn_episode_step, int) and step - last_churn_episode_step > comp_window):
                            add_issue(report, "MEDIUM", "COMP_DIRECTION_CHURN", player, rnd, step,
                                      "Episódio de mudanças repetidas de composição; revisar as transições listadas.",
                                      list(comp_history))
                            last_churn_episode_step = step
            if focus and isinstance(core_units, list) and core_units:
                if not any(focus.casefold() in str(unit).casefold()
                           or str(unit).casefold() in focus.casefold() for unit in core_units):
                    add_issue(report, "LOW", "FOCUS_NOT_IN_CORE_UNITS", player, rnd, step,
                              "comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir.",
                              {"focus": focus, "core_units": core_units})

    if report["diagnostics_missing"] and not report["mask_note_added"]:
        report["notes"].append(
            "Os logs não persistem a máscara completa de ações válidas. Portanto, não é possível "
            "provar retrospectivamente se uma ação inválida foi bloqueada. Registre type_mask e "
            "máscaras condicionais por ação para validar mask de forma conclusiva."
        )
        report["mask_note_added"] = True


def audit_text(path: Path, report: dict) -> None:
    try:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError as exc:
        print(f"[WARN] Falha lendo {path}: {exc}", file=sys.stderr)
        return
    match = re.search(r"player_(\d+)_log", path.name)
    player_id = match.group(1) if match else path.stem
    report["players_seen"].add(str(player_id))
    report["log_files"].append(str(path))
    current_round = "?"
    moves, comps = [], []
    for line_no, line in enumerate(text.splitlines(), 1):
        rm = ROUND_RE.search(line)
        if rm:
            current_round = f"{rm.group(1)}-{rm.group(2)}"
        mm = MOVE_RE.search(line)
        if mm:
            kind, left, right, reward = mm.groups()
            move = (line_no, current_round, kind, left.strip(), right.strip(), float(reward), line.strip())
            moves.append(move)
            if len(moves) >= 4:
                a, b, c, d = moves[-4:]
                if ((a[2:5] == c[2:5]) and (b[2:5] == d[2:5])
                        and a[2:5] != b[2:5]):
                    add_issue(report, "HIGH", "TEXT_MOVE_OSCILLATION", f"Jogador {player_id}",
                              current_round, line_no,
                              "Possível alternância de duas unidades; confirme no JSON estruturado.",
                              [a[6], b[6], c[6], d[6]])
        # A direção da composição é auditada no JSON estruturado; não duplicar o mesmo estado
        # lendo-o novamente no .tft. O .tft aqui serve para corroborar loops de movimento.


def markdown_report(report: dict) -> str:
    counts = Counter(x["severity"] for x in report["issues"])
    lines = [
        "# Auditoria da partida TFT", "",
        f"- Arquivos lidos: **{len(set(report['log_files']))}**",
        f"- Jogadores encontrados: **{len(report['players_seen'])}** ({', '.join(report['players_seen']) or 'nenhum'})",
        f"- Entradas JSON analisadas: **{report['entries_read']}**",
        f"- Achados: **{len(report['issues'])}**",
        f"- CRITICAL: {counts['CRITICAL']} | HIGH: {counts['HIGH']} | MEDIUM: {counts['MEDIUM']} | LOW: {counts['LOW']}", "",
    ]
    if report.get("purchase_sequence_metrics"):
        lines += ["## Auditoria de compras e vendas", "",
                  "| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Compras com upgrade |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for player, metrics in sorted(report["purchase_sequence_metrics"].items()):
            lines.append(
                f"| {player} | {metrics['buys']} | {metrics['sells']} | "
                f"{metrics['reversed_1']} | {metrics['reversed_2']} | {metrics['reversed_4']} | "
                f"{metrics['net_gold_lost_reversed']} | {metrics['upgrade_completing_buys']} |"
            )
        lines += ["", "As classificações detalhadas e cada sequência correlacionada ficam em audit_report.json.",
                  "Uma venda sem compra correspondente na janela é UNKNOWN; sequências ambíguas não são penalizadas automaticamente.", ""]
    if report["issues"]:
        lines += ["## Achados", "", "| Severidade | Jogador | Round | Step | Código | Descrição |",
                  "|---|---|---:|---:|---|---|"]
        for item in report["issues"]:
            message = item["message"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {item['severity']} | {item['player']} | {item['round']} | {item['step'] if item['step'] is not None else '—'} | {item['code']} | {message} |")
    else:
        lines += ["Nenhum problema detectável pelos campos disponíveis. Isso não prova ausência de bugs.", ""]
    if report["notes"]:
        lines += ["", "## Limitações e melhorias de instrumentação", ""]
        lines.extend(f"- {note}" for note in report["notes"])
    lines += ["", "## Como interpretar", "",
              "- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.",
              "- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.",
              "- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.",
              "- JSON e TFT são usados de forma complementar: JSON para estado/estratégia; TFT para corroborar loops de movimento. Alertas de composição do TFT foram desativados para não duplicar episódios.",
              "- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.",
              "- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", type=Path, help="pasta da sessão ou arquivo player log")
    parser.add_argument("--out-dir", type=Path, help="diretório dos relatórios; padrão: <entrada>/audit")
    parser.add_argument("--loop-window", type=int, default=8, help="janela para repetição de posição (mínimo 4)")
    parser.add_argument("--comp-window", type=int, default=8, help="janela para instabilidade de composição (mínimo 3)")
    parser.add_argument("--strict", action="store_true", help="retorna código 1 se houver CRITICAL/HIGH")
    args = parser.parse_args()
    if args.loop_window < 4 or args.comp_window < 3:
        parser.error("--loop-window precisa ser >= 4 e --comp-window >= 3")
    source = args.input
    if source.is_file():
        files = [source]
        default_out = source.parent / "audit"
    elif source.is_dir():
        json_files = sorted(source.glob("player_*_log.json"))
        tft_files = sorted(source.glob("player_*_log.tft"))
        if not json_files:
            json_files = sorted(source.rglob("player_*_log.json"))
        if not tft_files:
            tft_files = sorted(source.rglob("player_*_log.tft"))
        # JSON fornece estado estruturado; TFT complementa movimentos que o JSON não reconstrói bem.
        files = json_files + tft_files
        default_out = source / "audit"
    else:
        parser.error(f"caminho não existe: {source}")
    report = {"source": str(source), "log_files": [], "players_seen": set(),
              "purchase_sequence_metrics": {},
              "entries_read": 0, "diagnostics_missing": 0, "issues": [], "notes": [],
              "mask_note_added": False}
    for path in files:
        if path.suffix.lower() == ".json":
            doc = read_json(path)
            if doc:
                audit_json(path, doc, report, args.loop_window, args.comp_window)
        elif path.suffix.lower() == ".tft":
            audit_text(path, report)
    unique, seen = [], set()
    for item in report["issues"]:
        key = (item["severity"], item["code"], item["player"], item["round"], item["step"], item["message"])
        if key not in seen:
            seen.add(key)
            unique.append(item)
    report["issues"] = unique
    report["players_seen"] = sorted(report["players_seen"], key=lambda x: int(x) if x.isdigit() else 9999)
    report["summary"] = dict(Counter(x["severity"] for x in unique))
    out_dir = args.out_dir or default_out
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path, md_path = out_dir / "audit_report.json", out_dir / "audit_report.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(markdown_report(report), encoding="utf-8")
    print(markdown_report(report))
    print(f"\nRelatórios salvos em:\n- {json_path}\n- {md_path}")
    if args.strict and any(x["severity"] in ("CRITICAL", "HIGH") for x in unique):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
