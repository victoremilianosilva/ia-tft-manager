"""Summarize economy/decision JSONL traces from audit_native_ppo_loops.py.

Example:
  python scripts/summarize_economy_audit.py reports/economy_audit.jsonl --output reports/economy_summary.json

Metrics are reported per seed and player. Reversals require the exact unit UUID,
not just a matching champion name; ambiguous sales are not counted as confirmed.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def units(player, key):
    return [u for u in player.get(key, []) if isinstance(u, dict) and u.get("occupied")]


def inventory(player):
    return units(player, "board") + units(player, "bench")


def unit_map(player):
    return {str(u.get("uuid")): u for u in inventory(player) if u.get("uuid")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("reports/economy_summary.json"))
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"Audit JSONL not found: {args.input}")

    grouped = defaultdict(list)
    with args.input.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSON at line {line_number}: {exc}") from exc
            grouped[(int(row.get("seed", 0)), int(row.get("player_id", -1)))].append(row)

    summaries = []
    for (seed, player_id), rows in sorted(grouped.items()):
        rows.sort(key=lambda r: int(r.get("step", 0)))
        recent_buys = {}
        confirmed_reversals = []
        buys = xp_buys = sells = upgrades = passes = 0
        high_gold_passes = 0
        for row in rows:
            action = row.get("selected_action") or [-1]
            kind = int(action[0]) if action else -1
            before = {"board": row.get("board_before", []), "bench": row.get("bench_before", [])}
            after = {"board": row.get("board_after", []), "bench": row.get("bench_after", [])}
            before_units, after_units = unit_map(before), unit_map(after)
            added = set(after_units) - set(before_units)
            removed = set(before_units) - set(after_units)
            if kind == 0:
                buys += 1
                for uuid in added:
                    recent_buys[uuid] = {
                        "step": int(row.get("step", 0)),
                        "champion_id": after_units[uuid].get("champion_id"),
                    }
            elif kind == 1:
                xp_buys += 1
            elif kind == 5:
                sells += 1
                sold_uuid = None
                source = int(action[2]) if len(action) > 2 else -1
                bench_before = units(before, "bench")
                # Action source points to the bench slot; use its UUID only.
                if 0 <= source < len(before.get("bench", [])):
                    candidate = before["bench"][source]
                    if isinstance(candidate, dict) and candidate.get("occupied"):
                        sold_uuid = str(candidate.get("uuid", "")) or None
                if sold_uuid and sold_uuid in recent_buys and sold_uuid in removed:
                    confirmed_reversals.append({
                        "buy_step": recent_buys[sold_uuid]["step"],
                        "sell_step": int(row.get("step", 0)),
                        "uuid": sold_uuid,
                        "champion_id": recent_buys[sold_uuid]["champion_id"],
                    })
            elif kind == 6:
                passes += 1
                if int(row.get("gold_before", 0)) >= 50:
                    high_gold_passes += 1

            before_by_id = {str(u.get("champion_id")): int(u.get("star", 1))
                            for u in before_units.values()}
            after_by_id = {str(u.get("champion_id")): int(u.get("star", 1))
                           for u in after_units.values()}
            if any(star > before_by_id.get(champ, 0)
                   for champ, star in after_by_id.items()):
                upgrades += 1

        final = rows[-1]
        final_player = {
            "gold": final.get("gold_after"),
            "level": (final.get("cycle_context_after") or {}).get("level", final.get("level_after")),
            "hp": final.get("hp_after"),
            "board_composition_score": (final.get("strategy_after") or {}).get("board_composition_score"),
            "board_unit_count": (final.get("strategy_after") or {}).get("board_unit_count"),
            "board_two_star_count": (final.get("strategy_after") or {}).get("board_two_star_count"),
            "placement": final.get("placement", final.get("final_placement")),
        }
        summaries.append({
            "seed": seed, "player_id": player_id, "steps": len(rows),
            "final": final_player,
            "buys": buys, "xp_buys": xp_buys, "sells": sells,
            "upgrade_steps_heuristic": upgrades,
            "confirmed_buy_sell_reversals_by_uuid": len(confirmed_reversals),
            "reversal_examples": confirmed_reversals[:20],
            "passes": passes, "passes_with_50plus_gold": high_gold_passes,
            "economy_missed_progress_candidates": sum(
                bool(r.get("economy_diagnostic", {}).get("potential_missed_progress"))
                for r in rows
            ),
        })

    result = {
        "source": str(args.input),
        "players": summaries,
        "coverage": {
            "seed_count": len({x["seed"] for x in summaries}),
            "player_rows": len(summaries),
            "all_eight_players_present_per_seed": all(
                sum(x["seed"] == seed for x in summaries) == 8
                for seed in {x["seed"] for x in summaries}
            ),
        },
        "limitations": [
            "Placement is null unless the input trace explicitly includes it.",
            "Upgrade steps are heuristic; UUID-based buy/sell reversals are identity-confirmed.",
            "Board strength uses the logged composition score, not combat simulation power.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["coverage"], ensure_ascii=False))
    print(f"Summary written to {args.output}")


if __name__ == "__main__":
    main()
