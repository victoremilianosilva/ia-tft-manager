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


def audit_json(path: Path, doc: dict, report: dict, loop_window: int, comp_window: int) -> None:
    player_id = doc.get("player_number")
    if player_id is None:
        raw_id = doc.get("player_id")
        player_id = raw_id + 1 if isinstance(raw_id, int) else path.stem
    player = f"Jogador {player_id}"
    report["players_seen"].add(str(player_id))
    report["entries_read"] += len(doc["entries"])
    report["log_files"].append(str(path))

    entries = sorted(doc["entries"], key=lambda e: (e.get("sequence_id", 0), e.get("step", 0)))
    recent_moves = deque(maxlen=loop_window)
    state_visits = defaultdict(lambda: deque(maxlen=loop_window))
    comp_history = deque(maxlen=comp_window)

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
                comp_history.append({"step": step, "round": rnd, "comp": comp,
                                     "focus": focus, "strategy": strategy})
                if len(comp_history) == comp_window and len({x["comp"] for x in comp_history}) >= 3:
                    add_issue(report, "MEDIUM", "COMP_DIRECTION_CHURN", player, rnd, step,
                              "Direção de composição mudou pelo menos três vezes numa janela curta.",
                              list(comp_history))
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
        sm = STRATEGY_RE.search(line)
        if sm:
            strategy, comp, focus = [x.strip() for x in sm.groups()]
            comp = "" if comp in ("—", "-", "None") else comp
            comps.append((line_no, current_round, comp, focus, strategy))
            recent = comps[-5:]
            nonempty = [x[2] for x in recent if x[2]]
            if len(nonempty) >= 4 and len(set(nonempty)) >= 3:
                add_issue(report, "MEDIUM", "COMP_DIRECTION_CHURN", f"Jogador {player_id}",
                          current_round, line_no,
                          "Direção da composição mudou repetidamente; pode ser adaptação legítima.",
                          [{"line": x[0], "round": x[1], "comp": x[2], "focus": x[3]} for x in recent])


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
              "- Logs .tft permitem apenas heurísticas textuais; os JSON estruturados são preferíveis.", ""]
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
        files = sorted(source.glob("player_*_log.json")) + sorted(source.glob("player_*_log.tft"))
        if not files:
            files = sorted(source.rglob("player_*_log.json")) + sorted(source.rglob("player_*_log.tft"))
        default_out = source / "audit"
    else:
        parser.error(f"caminho não existe: {source}")
    report = {"source": str(source), "log_files": [], "players_seen": set(),
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
