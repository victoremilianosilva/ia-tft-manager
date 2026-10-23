#!/usr/bin/env python3
"""Validate strategic audit state signatures, unit identities, and cycle evidence.

Reads player_*.jsonl from audit_strategic_policy.py. It does not infer that a
repeated action is a loop: cycles are based on reconstructed board+bench states.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from scripts.strategic_audit_state import state_signature


def read_records(input_dir: Path, pattern: str):
    records, errors = [], []
    for path in sorted(input_dir.glob(pattern)):
        try:
            with path.open(encoding="utf-8-sig") as stream:
                for line_no, line in enumerate(stream, 1):
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                        if isinstance(row, dict):
                            row["_source_file"] = path.name
                            row["_line"] = line_no
                            records.append(row)
                        else:
                            errors.append(f"{path.name}:{line_no}: registro não é objeto")
                    except json.JSONDecodeError as exc:
                        errors.append(f"{path.name}:{line_no}: JSON inválido: {exc.msg}")
        except OSError as exc:
            errors.append(f"{path}: {exc}")
    return records, errors


def player_snapshot(row: dict[str, Any], suffix: str):
    return {
        "board": row.get(f"board_{suffix}", []),
        "bench": row.get(f"bench_{suffix}", []),
    }


def unit_map(snapshot: dict[str, Any]):
    found = {}
    duplicates = []
    for zone in ("board", "bench"):
        for slot, unit in enumerate(snapshot.get(zone) or []):
            if not isinstance(unit, dict) or not unit.get("occupied"):
                continue
            uuid = str(unit.get("uuid") or "").strip()
            if not uuid:
                continue
            if uuid in found:
                duplicates.append(uuid)
            found[uuid] = {
                "champion_id": str(unit.get("champion_id") or ""),
                "star": int(unit.get("star", 0) or 0),
                "zone": zone,
                "slot": slot,
            }
    return found, duplicates


def validate(records, expected_seeds):
    grouped = defaultdict(list)
    for row in records:
        seed, pid = row.get("seed"), row.get("player_id")
        if seed is None or pid is None:
            continue
        grouped[(int(seed), int(pid))].append(row)

    signature_mismatches, identity_conflicts, duplicate_uuids = [], [], []
    cycles, suspicious_sequences = [], []
    seen_seeds = sorted({int(r["seed"]) for r in records if r.get("seed") is not None})
    player_counts = {}
    for key, rows in grouped.items():
        seed, pid = key
        rows.sort(key=lambda r: int(r.get("step", -1)))
        player_counts[f"{seed}:{pid}"] = len(rows)
        visited = {}
        last_after = None
        uuid_history = {}
        movement_window = []
        for row in rows:
            step = int(row.get("step", -1))
            before = player_snapshot(row, "before")
            after = player_snapshot(row, "after")
            before_sig, after_sig = state_signature(before), state_signature(after)
            if row.get("board_bench_signature_before") != before_sig:
                signature_mismatches.append({"seed": seed, "player_id": pid, "step": step,
                                             "side": "before", "stored": row.get("board_bench_signature_before"),
                                             "recomputed": before_sig})
            if row.get("board_bench_signature_after") != after_sig:
                signature_mismatches.append({"seed": seed, "player_id": pid, "step": step,
                                             "side": "after", "stored": row.get("board_bench_signature_after"),
                                             "recomputed": after_sig})
            if last_after is not None and before_sig != last_after:
                # A discontinuity may be legitimate if the engine snapshot is not
                # synchronous; retain as evidence rather than silently joining chains.
                signature_mismatches.append({"seed": seed, "player_id": pid, "step": step,
                                             "side": "transition", "stored": last_after,
                                             "recomputed": before_sig})
            last_after = after_sig

            for side, snapshot in (("before", before), ("after", after)):
                units, duplicates = unit_map(snapshot)
                if duplicates:
                    duplicate_uuids.append({"seed": seed, "player_id": pid, "step": step,
                                            "side": side, "uuids": sorted(set(duplicates))})
                for uuid, unit in units.items():
                    identity_key = (seed, pid, uuid)
                    identity = (unit["champion_id"], unit["star"])
                    prior = uuid_history.get(identity_key)
                    if prior and prior["champion_id"] != unit["champion_id"]:
                        identity_conflicts.append({"seed": seed, "player_id": pid, "step": step,
                                                   "uuid": uuid, "previous_champion": prior["champion_id"],
                                                   "current_champion": unit["champion_id"], "side": side})
                    uuid_history[identity_key] = {"champion_id": unit["champion_id"],
                                                  "last_star": unit["star"]}

            # Register the pre-action state as well: otherwise a cycle returning
            # to the initial snapshot of a seed is invisible to this validator.
            visited.setdefault(before_sig, {"step": step - 1, "action": None})
            action = row.get("action", [])
            action_type = action[0] if isinstance(action, list) and action else (
                action.get("type") if isinstance(action, dict) else None)
            if action_type in (3, 4) and row.get("action_effect_observed"):
                movement_window.append({
                    "step": step, "round": row.get("round_after", row.get("round_before")),
                    "action": action, "before": before, "after": after,
                    "before_signature": before_sig, "after_signature": after_sig,
                    "unit_changes": row.get("unit_changes", {}),
                    "strategy_before": row.get("strategy_before", {}),
                    "strategy_after": row.get("strategy_after", {}),
                    "action_reward": row.get("action_reward"),
                })
                if before_sig != after_sig and after_sig in visited:
                    prior = visited[after_sig]
                    cycles.append({
                        "seed": seed, "player_id": pid, "step": step,
                        "previous_step": prior["step"], "cycle_length": step-prior["step"],
                        "action": action, "prior_action": prior["action"],
                        "identity_confidence": "uuid" if all(
                            u.get("uuid") for z in ("board", "bench")
                            for u in after.get(z, []) if isinstance(u, dict) and u.get("occupied")
                        ) else "partial_or_missing_uuid",
                        "before": before, "after": after,
                        "unit_changes": row.get("unit_changes", {}),
                        "strategy_before": row.get("strategy_before", {}),
                        "strategy_after": row.get("strategy_after", {}),
                        "action_reward": row.get("action_reward"),
                    })
                if after_sig not in visited:
                    visited[after_sig] = {"step": step, "action": action}
                if len(movement_window) >= 4:
                    w = movement_window[-4:]
                    if w[0]["after_signature"] == w[2]["after_signature"] and w[1]["after_signature"] == w[3]["after_signature"]:
                        suspicious_sequences.append({
                            "seed": seed, "player_id": pid, "round": row.get("round_after", row.get("round_before")),
                            "steps": [x["step"] for x in w],
                            "actions": [x["action"] for x in w],
                            "state_signatures": [x["after_signature"] for x in w],
                            "unit_changes": [x["unit_changes"] for x in w],
                            "rewards": [x["action_reward"] for x in w],
                        })
            # Keep state visits for every record so a later movement can return to
            # a state last observed after a purchase/sale or other action.
            visited.setdefault(after_sig, {"step": step, "action": action})

    missing_seeds = sorted(set(expected_seeds) - set(seen_seeds))
    return {
        "expected_seeds": expected_seeds, "observed_seeds": seen_seeds,
        "missing_seeds": missing_seeds, "records": len(records), "player_seed_groups": len(grouped),
        "player_counts": player_counts, "signature_mismatches": signature_mismatches,
        "identity_conflicts": identity_conflicts, "duplicate_uuids": duplicate_uuids,
        "confirmed_cycles": cycles, "repeated_state_sequences": suspicious_sequences,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=Path("reports/strategic_policy_v2"))
    parser.add_argument("--pattern", default="player_*.jsonl")
    parser.add_argument("--seeds", default="20261022,20261023")
    parser.add_argument("--out", type=Path, default=Path("reports/strategic_cycle_validation.json"))
    args = parser.parse_args()
    expected = [int(x.strip()) for x in args.seeds.split(",") if x.strip()]
    records, errors = read_records(args.input_dir, args.pattern)
    result = validate(records, expected)
    result["read_errors"] = errors
    result["ok"] = not (errors or result["missing_seeds"] or result["signature_mismatches"]
                        or result["identity_conflicts"] or result["duplicate_uuids"])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Records: {result['records']} | seeds observados: {result['observed_seeds']}")
    print(f"Assinaturas/transições inconsistentes: {len(result['signature_mismatches'])}")
    print(f"Conflitos de identidade UUID: {len(result['identity_conflicts'])}")
    print(f"UUIDs duplicados no mesmo snapshot: {len(result['duplicate_uuids'])}")
    print(f"Ciclos confirmados: {len(result['confirmed_cycles'])}")
    print(f"Sequências com estados repetidos: {len(result['repeated_state_sequences'])}")
    print(f"Seeds ausentes: {result['missing_seeds']}")
    print(f"Relatório: {args.out}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
