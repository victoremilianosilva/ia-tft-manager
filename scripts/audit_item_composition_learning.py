#!/usr/bin/env python3
"""Aggregate item/composition evidence across every player in native PPO JSONL audits.

Example:
  python scripts/audit_item_composition_learning.py \
      --input reports/native_ppo_loop_audit.jsonl \
      --output reports/item_composition_learning_audit.json
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def _units(state: Any) -> list[dict[str, Any]]:
    if not isinstance(state, list):
        return []
    return [unit for unit in state if isinstance(unit, dict) and unit.get("occupied", True)]


def _item_ids(unit: dict[str, Any]) -> list[str]:
    values = []
    for key in ("items", "equipped_items", "item_ids"):
        candidate = unit.get(key)
        if isinstance(candidate, list) and candidate:
            values = candidate
            break
        if isinstance(candidate, list) and not values:
            values = candidate
    result = []
    for item in values:
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, dict):
            item_id = item.get("id", item.get("api_name", item.get("apiName", item.get("name"))))
            if isinstance(item_id, str) and item_id:
                result.append(item_id)
    return result


def audit_records(records: list[dict[str, Any]], expected_players: int = 8) -> dict[str, Any]:
    per_player: dict[int, dict[str, Any]] = {}
    item_events: Counter[str] = Counter()
    action_counts: Counter[str] = Counter()

    def player_bucket(player_id: int) -> dict[str, Any]:
        if player_id not in per_player:
            per_player[player_id] = {
                "rows": 0,
                "alive_rows": 0,
                "directions": Counter(),
                "core_unit_observations": 0,
                "planned_unit_observations": 0,
                "board_item_instances": 0,
                "bench_item_instances": 0,
                "bag_item_instances": 0,
                "component_instances": 0,
                "item_inventory_observations": 0,
                "component_observations": 0,
                "item_inventory_peak": 0,
                "component_inventory_peak": 0,
                "distinct_item_ids": set(),
                "bag_item_ids": set(),
                "component_ids": set(),
                "item_evidence_rows": 0,
                "last_board_item_instances": 0,
                "last_bench_item_instances": 0,
                "last_bag_item_instances": 0,
                "last_component_instances": 0,
                "board_two_star_peak": 0,
                "buy_actions": 0,
                "sell_actions": 0,
                "loot_events": 0,
                "anvil_events": 0,
                "opgg_statuses": Counter(),
            }
        return per_player[player_id]

    for row in records:
        if not isinstance(row, dict):
            continue
        try:
            player_id = int(row.get("player_id", row.get("player", -1)))
        except (TypeError, ValueError):
            continue
        if player_id < 0:
            continue
        bucket = player_bucket(player_id)
        bucket["rows"] += 1
        if row.get("alive_at_decision", True):
            bucket["alive_rows"] += 1

        action = row.get("selected_action")
        if isinstance(action, list) and action:
            kind = int(action[0])
            action_name = {0: "BUY", 1: "REROLL", 2: "BUY_XP", 3: "MOVE_BENCH",
                           4: "MOVE_BOARD", 5: "SELL", 6: "PASS", 7: "ITEM", 8: "CRAFT"}.get(
                               kind, f"UNKNOWN_{kind}")
            action_counts[action_name] += 1
            if kind == 0:
                bucket["buy_actions"] += 1
            elif kind == 5:
                bucket["sell_actions"] += 1

        strategy = row.get("strategy_after", {})
        if isinstance(strategy, dict):
            direction = str(strategy.get("composition_direction", "") or "")
            if direction:
                bucket["directions"][direction] += 1
            if strategy.get("core_units"):
                bucket["core_unit_observations"] += 1
            if strategy.get("planned_units"):
                bucket["planned_unit_observations"] += 1
            notes = strategy.get("planned_acquisition_notes", [])
            if isinstance(notes, list):
                for note in notes:
                    if isinstance(note, str) and note.startswith("OPGG_META_AUDIT:"):
                        status = next((part.split("=", 1)[1] for part in note.split(";")
                                       if part.strip().startswith("status=")), "unknown")
                        bucket["opgg_statuses"][status] += 1

        board = _units(row.get("board_after"))
        bench = _units(row.get("bench_after"))
        observed_items = 0
        for unit in board:
            items = _item_ids(unit)
            observed_items += len(items)
            bucket["board_item_instances"] += len(items)
            bucket["distinct_item_ids"].update(items)
        for unit in bench:
            items = _item_ids(unit)
            observed_items += len(items)
            bucket["bench_item_instances"] += len(items)
            bucket["distinct_item_ids"].update(items)
        inventory_after = row.get("item_inventory_after")
        components_after = row.get("item_components_after")
        if isinstance(inventory_after, list):
            bucket["item_inventory_observations"] += 1
            bucket["bag_item_instances"] += len(inventory_after)
            bucket["item_inventory_peak"] = max(bucket["item_inventory_peak"], len(inventory_after))
            bucket["bag_item_ids"].update(str(item) for item in inventory_after if isinstance(item, str))
        if isinstance(components_after, list):
            bucket["component_observations"] += 1
            bucket["component_instances"] += len(components_after)
            bucket["component_inventory_peak"] = max(bucket["component_inventory_peak"], len(components_after))
            bucket["component_ids"].update(str(item) for item in components_after if isinstance(item, str))
        has_unit_item_fields = any(
            any(key in unit for key in ("items", "equipped_items", "item_ids"))
            for unit in board + bench
        )
        has_inventory_fields = isinstance(inventory_after, list) or isinstance(components_after, list)
        if observed_items or has_unit_item_fields or has_inventory_fields:
            bucket["item_evidence_rows"] += 1
        # Latest-state counts are separate from cumulative observation totals.
        bucket["last_board_item_instances"] = sum(len(_item_ids(unit)) for unit in board)
        bucket["last_bench_item_instances"] = sum(len(_item_ids(unit)) for unit in bench)
        bucket["last_bag_item_instances"] = len(inventory_after) if isinstance(inventory_after, list) else 0
        bucket["last_component_instances"] = len(components_after) if isinstance(components_after, list) else 0
        bucket["board_two_star_peak"] = max(
            bucket["board_two_star_peak"],
            sum(int(unit.get("star", 1) or 1) >= 2 for unit in board),
        )

        events = row.get("engine_events", [])
        if isinstance(events, list):
            for event in events:
                value = event if isinstance(event, str) else json.dumps(event, ensure_ascii=False)
                for token in ("COMPONENT_LOOT_GRANTED", "COMPONENT_ANVIL_GRANTED",
                              "COMPLETED_ITEM_ANVIL_GRANTED", "ITEM_EQUIPPED",
                              "ITEM_CRAFTED", "ITEM_RETURNED"):
                    if token in value:
                        item_events[token] += 1
                        if "LOOT" in token:
                            bucket["loot_events"] += 1
                        if "ANVIL" in token:
                            bucket["anvil_events"] += 1

    players_seen = sorted(per_player)
    expected_ids = set(range(expected_players))
    missing_players = sorted(expected_ids - set(players_seen))
    evidence_players = sorted(
        player_id for player_id, bucket in per_player.items()
        if bucket["item_evidence_rows"] > 0
    )
    missing_evidence_players = sorted(expected_ids - set(evidence_players))
    summaries = {}
    for player_id, bucket in sorted(per_player.items()):
        summaries[str(player_id)] = {
            **{key: value for key, value in bucket.items()
               if key not in ("directions", "distinct_item_ids", "bag_item_ids", "component_ids", "opgg_statuses")},
            "directions": dict(bucket["directions"]),
            "distinct_item_ids": sorted(bucket["distinct_item_ids"]),
            "bag_item_ids": sorted(bucket["bag_item_ids"]),
            "component_ids": sorted(bucket["component_ids"]),
            "opgg_statuses": dict(bucket["opgg_statuses"]),
        }
    return {
        "records": len(records),
        "players_seen": players_seen,
        "missing_players": missing_players,
        "all_players_present": not missing_players,
        "item_evidence_players": evidence_players,
        "players_without_item_evidence": missing_evidence_players,
        "item_evidence_available": not missing_players and not missing_evidence_players,
        "item_evidence_note": (
            "All expected players have item snapshots; latest-state counts are separated from cumulative observations."
            if not missing_players and not missing_evidence_players else
            "Item evidence is incomplete: missing player snapshots or item fields for one or more players."
        ),
        "action_counts": dict(action_counts),
        "item_event_counts": dict(item_events),
        "players": summaries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("reports/item_composition_learning_audit.json"))
    parser.add_argument("--expected-players", type=int, default=8)
    args = parser.parse_args()
    if args.expected_players < 1:
        parser.error("--expected-players must be positive")
    try:
        records = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines()
                   if line.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(f"Could not read JSONL input: {exc}")
    report = audit_records(records, args.expected_players)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Audit: {report['records']} rows | players={len(report['players_seen'])}/"
          f"{args.expected_players} | item evidence={'yes' if report['item_evidence_available'] else 'no'}")
    if report["missing_players"]:
        print(f"Players without rows: {report['missing_players']}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
