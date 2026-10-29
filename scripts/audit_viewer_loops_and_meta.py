#!/usr/bin/env python3
"""Audit movement oscillations and OP.GG composition lifecycle from legacy viewer logs.

This is deliberately an evidence extractor, not a movement blocker. Legacy .tft
logs do not contain stable unit UUIDs or a snapshot after every action, so this
tool labels text-level reversals as candidates; exact state-cycle confirmation
must come from audit_native_ppo_loops.py snapshots.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

MOVE_RE = re.compile(
    r"\[(?P<time>[^]]+)\]\s+MOVE (?P<kind>Bench -> Board|Board -> Board): "
    r"(?P<a>.*?) \(i:(?P<ia>[\d.]+)\) <-> (?P<b>.*?)"
    r"(?: \(i:(?P<ib>[\d.]+)\))? \| Rew: (?P<reward>[+-]?[\d.]+)",
    re.I,
)
META_RE = re.compile(r"OPGG_META_AUDIT: status=(?P<status>[a-z_]+).*?best=(?P<best>[^;]+)", re.I)
CANDIDATE_RE = re.compile(r"OPGG_META_CANDIDATE: (?P<name>.*?) \(score=(?P<score>-?[\d.]+), native_score=(?P<native>-?[\d.]+)\)", re.I)
DIRECTION_RE = re.compile(r"COMP DIRECTION: (?P<direction>[^|]+)\| FOCUS: (?P<focus>[^|]+)\| LOCK: (?P<lock>[^|]+)\| STRENGTH: (?P<strength>[\d.]+)(?: \| FONTE COMP: (?P<source>[^\r\n]+))?", re.I)
BUY_RE = re.compile(r"\] COMPROU: (?P<unit>.*?) \(Custo (?P<cost>\d+)", re.I)
ROUND_RE = re.compile(r"FIM DO ROUND (?P<stage>\d+)-(?P<round>\d+) \| GOLD: (?P<gold>\d+)", re.I)
SYNERGY_RE = re.compile(r"[⬆⬇] SINERGIA: (?P<name>.*?) nível (?P<level>\d+)", re.I)
PLACEMENT_RE = re.compile(r"(?:ELIMINADO · colocação final|COLOCAÇÃO FINAL:)\s*#(?P<place>\d+)", re.I)
UNIT_RE = re.compile(r"\[([^\[\]]+\|[^\[\]]+)\]")


def parse_log(path: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    moves, meta_events, purchases, strategy_events, rounds, synergies = [], [], [], [], [], []
    selected_name = None
    for line_no, line in enumerate(text.splitlines(), 1):
        mm = MOVE_RE.search(line)
        if mm:
            row = mm.groupdict()
            row.update(line=line_no, reward=float(row["reward"]))
            row["a"] = row["a"].strip()
            row["b"] = row["b"].strip()
            moves.append(row)
        for cm in CANDIDATE_RE.finditer(line):
            selected_name = cm.group("name").strip()
            meta_events.append({"line": line_no, "event": "candidate", "composition": selected_name,
                                "score": float(cm.group("score")), "native_score": float(cm.group("native"))})
        sm = META_RE.search(line)
        if sm:
            meta_events.append({"line": line_no, "event": sm.group("status"),
                                "best": sm.group("best").strip()})
        dm = DIRECTION_RE.search(line)
        if dm:
            row = dm.groupdict()
            row.update(line=line_no)
            for key in ("direction", "focus", "lock", "source"):
                if row.get(key) is not None:
                    row[key] = row[key].strip()
            row["strength"] = float(row["strength"])
            strategy_events.append(row)
        bm = BUY_RE.search(line)
        if bm:
            purchases.append({"line": line_no, "unit": bm.group("unit").strip(), "cost": int(bm.group("cost"))})
        rm = ROUND_RE.search(line)
        if rm:
            rounds.append({"line": line_no, **{k: int(v) for k, v in rm.groupdict().items()}})
        ym = SYNERGY_RE.search(line)
        if ym:
            synergies.append({"line": line_no, "name": ym.group("name").strip(),
                              "level": int(ym.group("level"))})

    # A reverse is only a textual oscillation candidate: labels are not stable
    # unit identities and the legacy format has no complete per-action snapshots.
    reversals = []
    for i, first in enumerate(moves):
        if first["b"].casefold() == "vazio":
            continue
        pair = sorted((first["a"].casefold(), first["b"].casefold()))
        for second in moves[i + 1:i + 9]:
            if second["b"].casefold() == "vazio":
                continue
            if sorted((second["a"].casefold(), second["b"].casefold())) == pair:
                gap = second["line"] - first["line"]
                if gap <= 80:
                    reversals.append({
                        "first_line": first["line"], "second_line": second["line"],
                        "first_time": first["time"], "second_time": second["time"],
                        "pair": [first["a"], first["b"]],
                        "first_reward": first["reward"], "second_reward": second["reward"],
                        "combined_reward": round(first["reward"] + second["reward"], 4),
                        "classification": "nonpositive_reverse_candidate"
                            if first["reward"] + second["reward"] <= 0 else "reverse_with_positive_reward",
                    })
                    break

    # Compress identical status messages while retaining every actual selection.
    selected_events = [e for e in meta_events if e["event"] == "selected"]
    candidate_names = sorted({e["composition"] for e in meta_events if e["event"] == "candidate"})
    selected_names = sorted({e.get("best", "") for e in selected_events})
    latest = strategy_events[-1] if strategy_events else {}
    placement_match = PLACEMENT_RE.search(text)
    board_sections = text.split("--- CONFIGURAÇÃO DO TABULEIRO ---")
    final_board = []
    if len(board_sections) > 1:
        final_section = board_sections[-1].split("--- ESTADO DO BANCO ---", 1)[0]
        for token in UNIT_RE.findall(final_section):
            parts = token.split("|")
            if len(parts) >= 3 and parts[0].strip() not in (".", " . ", "VAZIO"):
                final_board.append({"display": token, "name": parts[0].strip(),
                                    "role": parts[1].strip(), "star": parts[2].strip()})
    latest_opgg_source = next((e for e in reversed(strategy_events)
                               if (e.get("source") or "").startswith("OP.GG")), None)
    selected_comp_names = {e.get("best", "") for e in selected_events}
    executed_meta = bool(latest_opgg_source and any(
        name.casefold() in (latest_opgg_source.get("source") or "").casefold()
        for name in selected_comp_names if name
    ))
    return {
        "file": str(path),
        "bytes": len(text.encode("utf-8")),
        "is_empty": not bool(text.strip()),
        "movement_count": len(moves),
        "textual_reverse_candidates": reversals,
        "meta": {
            "candidate_names": candidate_names,
            "selected_names": selected_names,
            "status_counts": dict(Counter(e["event"] for e in meta_events)),
            "selection_count": len(selected_events),
            "strategy_direction_events": strategy_events,
            "last_strategy": latest,
            "selected_to_execution": {
                "status": "executed_source_observed" if executed_meta else
                          ("selected_but_execution_not_proven" if selected_events else "not_selected"),
                "last_opgg_source": latest_opgg_source,
                "selected_names": selected_names,
            },
            "candidate_to_selection": [
                {"composition": e.get("best"), "line": e["line"],
                 "selected_has_matching_candidate": e.get("best") in candidate_names}
                for e in selected_events
            ],
        },
        "purchases": purchases,
        "rounds": rounds,
        "synergy_events": synergies,
        "final_board_units": final_board,
        "final_placement": int(placement_match.group("place")) if placement_match else None,
        "limitations": [
            "Legacy .tft movement labels do not contain unit UUIDs or full before/after snapshots.",
            "Textual reversals are candidates for replay, not proof of an exact state cycle.",
            "Final deployed units, active synergies, and placement require structured match snapshots/results; they are not inferred from candidate status alone.",
        ],
    }


def audit(path: Path) -> dict:
    files = sorted(path.glob("player_*_log.tft")) if path.is_dir() else [path]
    players = [parse_log(file) for file in files]
    return {
        "schema_version": 1,
        "match_dir": str(path),
        "players": players,
        "summary": {
            "player_logs": len(players),
            "empty_logs": [p["file"] for p in players if p["is_empty"]],
            "movement_count": sum(p["movement_count"] for p in players),
            "textual_reverse_candidates": sum(len(p["textual_reverse_candidates"]) for p in players),
            "meta_selected": sum(p["meta"]["selection_count"] for p in players),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="diretório de sessão ou arquivo player_N_log.tft")
    parser.add_argument("--json", type=Path, default=None, help="salvar relatório JSON")
    args = parser.parse_args()
    report = audit(args.path)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    for player in report["players"]:
        print(f'{Path(player["file"]).name}: moves={player["movement_count"]}, '
              f'reversals={len(player["textual_reverse_candidates"])}, '
              f'meta_selected={player["meta"]["selection_count"]}, empty={player["is_empty"]}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
