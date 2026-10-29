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
    """Yield occupied units from flat or nested arrays, preserving board coordinates."""
    for location in locations:
        units = state.get(location) or []
        if not isinstance(units, list):
            continue
        flat_index = 0
        for index, item in enumerate(units):
            if isinstance(item, list):
                for col, unit in enumerate(item):
                    if is_occupied(unit):
                        if isinstance(unit, dict):
                            unit.setdefault("_audit_row", index)
                            unit.setdefault("_audit_col", col)
                        yield location, flat_index, unit
                    flat_index += 1
            else:
                if is_occupied(item):
                    if isinstance(item, dict) and location == "board" and len(units) >= 28:
                        item.setdefault("_audit_row", index // 7)
                        item.setdefault("_audit_col", index % 7)
                    yield location, index, item
                flat_index += 1


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
    return [u for _, _, u in iter_units(state, (location,))]


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
        if not isinstance(entry, dict) or entry.get("event_type") not in ("action", "round_finished"):
            continue
        payload = entry.get("payload") or {}
        action = payload.get("action") or []
        if action:
            actions.append((entry, payload, action))

    metrics = {
        "buys": 0, "sells": 0, "reversed_1": 0, "reversed_2": 0, "reversed_4": 0,
        "net_gold_lost_reversed": 0, "upgrade_completing_buys": 0,
        "buys_with_positive_comp_fit": 0, "buys_with_board_gain": 0, "buys_with_synergy_milestone": 0,
        "core_or_pair_sales": 0, "core_unit_sales": 0, "classified_sales": {}, "purchase_records": [],
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
            fit_score = float(fit.get("focus_fit_score", 0.0) or 0.0) + (5.0 if fit.get("core_unit_match") else 0.0)
            economic = payload.get("economic_diagnostics") or {}
            synergy_gain = len(economic.get("synergy_milestones_changed") or {})
            upgrade_completed = _star_counts(after)[2] > _star_counts(before)[2]
            board_gain = _board_power(after) > _board_power(before) + 1e-6
            metrics["buys"] += 1
            metrics["upgrade_completing_buys"] += int(upgrade_completed)
            metrics["buys_with_positive_comp_fit"] += int(fit_score > 0)
            metrics["buys_with_board_gain"] += int(board_gain)
            metrics["buys_with_synergy_milestone"] += int(synergy_gain > 0)
            strategic_value = fit_score + (2.0 if upgrade_completed else 0.0) + 1.5 * synergy_gain + max(
                0, _pair_count(after) - _pair_count(before))
            if board_gain:
                strategic_value += 1.0
            record = {
                "champion": champion, "uuid": unit.get("uuid"), "buy_action_index": idx, "step": step, "round": rnd,
                "cost": max(0, int(unit.get("cost", 0) or 0)), "fit_score": fit_score,
                "strategic_value": round(strategic_value, 4),
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
            core_units = [str(value).casefold() for value in (before.get("core_units") or [])]
            core_sale = any(champion.casefold() == core or champion.casefold() in core
                            or core in champion.casefold() for core in core_units if core)
            if core_sale:
                metrics["core_unit_sales"] += 1
            pair_lost = _pair_count(before) > _pair_count(after)
            if core_sale or pair_lost:
                metrics["core_or_pair_sales"] += 1
                code = "SOLD_CORE_UNIT" if core_sale else "SOLD_UPGRADE_PAIR_COPY"
                severity = "HIGH" if core_sale or pair_lost else "MEDIUM"
                add_issue(report, severity, code, player, rnd, step,
                          f"Venda de '{champion}' removeu uma unidade core ou reduziu pares disponíveis; verificar custo estratégico.",
                          {"champion": champion, "core_sale": core_sale, "pair_lost": pair_lost,
                           "pair_count_before": _pair_count(before), "pair_count_after": _pair_count(after),
                           "gold_before": before.get("gold"), "gold_after": after.get("gold")})
            sold_uuid = unit.get("uuid")
            match = next((p for p in reversed(purchases)
                          if not p["sold"]
                          and ((sold_uuid and p.get("uuid") and p["uuid"] == sold_uuid)
                               or (not sold_uuid or not p.get("uuid"))
                               and p["champion"].casefold() == champion.casefold())
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
    values = [float(record.get("strategic_value", 0.0)) for record in metrics["purchase_records"]]
    metrics["average_strategic_value_per_purchase"] = round(sum(values) / len(values), 4) if values else 0.0
    buys = max(1, metrics["buys"])
    metrics["upgrade_completion_rate"] = round(metrics["upgrade_completing_buys"] / buys, 4)
    metrics["positive_comp_fit_rate"] = round(metrics["buys_with_positive_comp_fit"] / buys, 4)
    metrics["board_gain_rate"] = round(metrics["buys_with_board_gain"] / buys, 4)
    metrics["synergy_milestone_rate"] = round(metrics["buys_with_synergy_milestone"] / buys, 4)
    report.setdefault("purchase_sequence_metrics", {})[player] = metrics



def audit_economic_actions(entries: list[dict], player: str, report: dict) -> None:
    """Summarize action-level economic telemetry emitted by the native engine/viewer."""
    actions = [
        entry for entry in entries
        if isinstance(entry, dict) and entry.get("event_type") == "action"
        and isinstance((entry.get("payload") or {}).get("economic_diagnostics"), dict)
    ]
    totals = Counter()
    by_action = defaultdict(lambda: {
        "actions": 0, "gold_spent": 0, "gold_recovered": 0,
        "measurable_improvements": 0, "potential_interest_lost": 0,
    })
    by_stage = defaultdict(lambda: {"gold_spent": 0, "actions": 0})
    xp_without_level_up = 0
    xp_level_up_unused = 0
    rerolls_without_immediate_gain = 0
    rerolls_followed_by_pass = 0
    interest_threshold_crossings = 0
    reward_component_samples = 0
    final_gold = None
    final_board_power = None
    for index, entry in enumerate(actions):
        payload = entry.get("payload") or {}
        diag = payload.get("economic_diagnostics") or {}
        action_name = str(payload.get("action_name", "UNKNOWN"))
        stage = str(entry.get("stage", "?"))
        bucket = by_action[action_name]
        bucket["actions"] += 1
        cost = max(0, int(diag.get("action_cost", 0) or 0))
        recovered = max(0, int(diag.get("sale_proceeds", 0) or 0))
        bucket["gold_spent"] += cost
        bucket["gold_recovered"] += recovered
        bucket["measurable_improvements"] += int(bool(diag.get("measurable_improvement")))
        potential_delta = int(diag.get("potential_interest_delta", 0) or 0)
        if potential_delta < 0:
            bucket["potential_interest_lost"] += -potential_delta
        by_stage[stage]["gold_spent"] += cost
        by_stage[stage]["actions"] += 1
        totals["actions"] += 1
        totals["gold_spent"] += cost
        totals["gold_recovered"] += recovered
        totals["potential_interest_lost"] += max(0, -potential_delta)
        if potential_delta < 0:
            interest_threshold_crossings += 1
        if action_name == "BUY_XP" and diag.get("reason_code") == "XP_NO_LEVEL_UP":
            xp_without_level_up += 1
        if action_name == "BUY_XP" and diag.get("reason_code") == "XP_LEVEL_UP":
            after_level = int(diag.get("level_after", 0) or 0)
            state_after_xp = payload.get("state_after") or {}
            board_after_xp = sum(bool(unit.get("occupied")) for unit in state_after_xp.get("board", []) if isinstance(unit, dict))
            used_new_slot = False
            for later in actions[index + 1:]:
                if later.get("round") != entry.get("round") or later.get("stage") != entry.get("stage"):
                    break
                later_payload = later.get("payload") or {}
                if later_payload.get("action_name") == "PASS":
                    break
                if later_payload.get("action_name") == "MOVE_BENCH":
                    later_state = later_payload.get("state_after") or {}
                    later_board = sum(bool(unit.get("occupied")) for unit in later_state.get("board", []) if isinstance(unit, dict))
                    if later_board > board_after_xp and later_board <= after_level:
                        used_new_slot = True
                        break
            if not used_new_slot and board_after_xp < after_level:
                xp_level_up_unused += 1
        if action_name == "REROLL" and diag.get("reason_code") == "REROLL_NO_IMMEDIATE_BOARD_GAIN":
            rerolls_without_immediate_gain += 1
            if index + 1 < len(actions):
                next_entry = actions[index + 1]
                same_round = (
                    next_entry.get("round") == entry.get("round")
                    and next_entry.get("stage") == entry.get("stage")
                )
                if same_round and next_entry.get("payload", {}).get("action_name") == "PASS":
                    rerolls_followed_by_pass += 1
        if payload.get("action_reward") is not None:
            reward_component_samples += 1
        after = payload.get("state_after") or {}
        if after:
            final_gold = after.get("gold", final_gold)
            final_board_power = after.get("board_power", final_board_power)
    if not actions:
        return
    report.setdefault("economic_action_metrics", {})[player] = {
        **dict(totals),
        "by_action": {name: dict(values) for name, values in sorted(by_action.items())},
        "by_stage": {stage: dict(values) for stage, values in sorted(by_stage.items())},
        "xp_without_level_up": xp_without_level_up,
        "xp_level_up_unused": xp_level_up_unused,
        "rerolls_without_immediate_gain": rerolls_without_immediate_gain,
        "rerolls_followed_by_pass": rerolls_followed_by_pass,
        "interest_threshold_crossings": interest_threshold_crossings,
        "final_gold": final_gold,
        "final_board_power": final_board_power,
        "action_reward_samples": reward_component_samples,
        "interpretation": "No-immediate-gain is a diagnostic, not proof that an action was strategically wrong.",
    }


def audit_composition_direction_changes(entries: list[dict], player: str, report: dict) -> None:
    """Measure direction transitions with observable strength/synergy/board/fit gains."""
    metrics = {
        "direction_changes": 0,
        "changes_with_measurable_gain": 0,
        "changes_without_measurable_gain": 0,
        "details": [],
        "interpretation": (
            "Without measurable gain means the available log fields did not show a gain; "
            "it is a review signal, not proof that the strategic transition was wrong."
        ),
    }
    for entry in sorted(entries, key=lambda e: (e.get("sequence_id", 0), e.get("step", 0))):
        if not isinstance(entry, dict) or entry.get("event_type") != "action":
            continue
        payload = entry.get("payload") or {}
        diagnostics = payload.get("composition_diagnostics") or {}
        event = diagnostics.get("direction_event")
        if not isinstance(event, dict):
            continue
        before = payload.get("state_before") or {}
        after = payload.get("state_after") or {}
        strength_delta = (
            float(after.get("composition_strength", 0.0) or 0.0)
            - float(event.get("from_strength", before.get("composition_strength", 0.0)) or 0.0)
        )
        board_delta = float(after.get("board_power", 0.0) or 0.0) - float(
            before.get("board_power", 0.0) or 0.0
        )
        synergy_delta = float(after.get("synergy_score", 0.0) or 0.0) - float(
            before.get("synergy_score", 0.0) or 0.0
        )
        economic = payload.get("economic_diagnostics") or {}
        synergy_milestones = economic.get("synergy_milestones_changed") or {}
        fit = diagnostics.get("unit_fit") or {}
        compatibility_gain = (
            str(payload.get("action_name", "")).upper() == "BUY"
            and (bool(fit.get("core_unit_match")) or float(fit.get("focus_fit_score", 0.0) or 0.0) > 0.0)
        )
        measurable_gain = (
            strength_delta > 1e-6 or board_delta > 1e-6
            or synergy_delta > 1e-6 or bool(synergy_milestones) or compatibility_gain
        )
        metrics["direction_changes"] += 1
        metrics["changes_with_measurable_gain"] += int(measurable_gain)
        metrics["changes_without_measurable_gain"] += int(not measurable_gain)
        metrics["details"].append({
            "step": entry.get("step"),
            "round": get_round(entry),
            "from": event.get("from"),
            "to": event.get("to"),
            "reason": event.get("reason"),
            "was_locked": event.get("was_locked"),
            "strength_delta": round(strength_delta, 4),
            "board_power_delta": round(board_delta, 4),
            "synergy_delta": round(synergy_delta, 4),
            "synergy_milestones_changed": synergy_milestones,
            "compatibility_gain": compatibility_gain,
            "measurable_gain": measurable_gain,
        })
    if metrics["direction_changes"]:
        metrics["rate_without_measurable_gain"] = round(
            metrics["changes_without_measurable_gain"] / metrics["direction_changes"], 4
        )
        no_gain_streak = []
        for detail in metrics["details"]:
            if not detail["measurable_gain"]:
                no_gain_streak.append(detail)
            else:
                no_gain_streak = []
            if len(no_gain_streak) == 3:
                tail = no_gain_streak[-3:]
                add_issue(report, "MEDIUM", "COMP_DIRECTION_CHANGES_WITHOUT_GAIN", player,
                          tail[-1]["round"], tail[-1]["step"],
                          "Três mudanças consecutivas de composição sem ganho mensurável nos campos registrados; revisar se a IA está perseguindo comps sem evidência.",
                          {"transitions": [{"step": x["step"], "from": x["from"], "to": x["to"],
                                            "reason": x["reason"], "strength_delta": x["strength_delta"],
                                            "board_power_delta": x["board_power_delta"],
                                            "synergy_delta": x["synergy_delta"]} for x in tail]})
                if len(no_gain_streak) > 3:
                    no_gain_streak = no_gain_streak[-3:]
        report.setdefault("composition_direction_metrics", {})[player] = metrics


def audit_board_quality(entries: list[dict], player: str, report: dict) -> None:
    """Aggregate structural/positional gains per action alongside combat outcomes."""
    actions = [
        entry for entry in entries
        if isinstance(entry, dict) and entry.get("event_type") == "action"
        and isinstance((entry.get("payload") or {}).get("state_after"), dict)
    ]
    totals = {
        "actions_with_metrics": 0, "positive_quality_delta": 0,
        "negative_quality_delta": 0, "neutral_quality_delta": 0,
        "quality_delta_sum": 0.0, "structural_delta_sum": 0.0,
        "positive_combat_outcomes": 0, "negative_combat_outcomes": 0,
        "quality_delta_when_combat_reward_positive": 0.0,
        "quality_delta_when_combat_reward_negative": 0.0,
        "positive_combat_samples": 0, "negative_combat_samples": 0,
        "by_action": {},
    }
    by_action = defaultdict(lambda: {"actions": 0, "quality_delta_sum": 0.0,
                                     "positive_gains": 0, "structural_delta_sum": 0.0})
    for entry in actions:
        payload = entry.get("payload") or {}
        before = payload.get("state_before") or {}
        after = payload.get("state_after") or {}
        if after.get("board_quality_score") is None:
            continue
        try:
            delta = float(after.get("board_quality_delta", 0.0) or 0.0)
            structural_before = float(before.get("board_structural_score", 0.0) or 0.0)
            structural_after = float(after.get("board_structural_score", 0.0) or 0.0)
            combat = float(payload.get("combat_reward", 0.0) or 0.0)
        except (TypeError, ValueError):
            continue
        action_name = str(payload.get("action_name", "UNKNOWN"))
        bucket = by_action[action_name]
        bucket["actions"] += 1
        bucket["quality_delta_sum"] += delta
        bucket["structural_delta_sum"] += structural_after - structural_before
        bucket["positive_gains"] += int(delta > 1e-6)
        totals["actions_with_metrics"] += 1
        totals["quality_delta_sum"] += delta
        totals["structural_delta_sum"] += structural_after - structural_before
        if delta > 1e-6:
            totals["positive_quality_delta"] += 1
        elif delta < -1e-6:
            totals["negative_quality_delta"] += 1
        else:
            totals["neutral_quality_delta"] += 1
        if combat > 1e-6:
            totals["positive_combat_outcomes"] += 1
            totals["quality_delta_when_combat_reward_positive"] += delta
            totals["positive_combat_samples"] += 1
        elif combat < -1e-6:
            totals["negative_combat_outcomes"] += 1
            totals["quality_delta_when_combat_reward_negative"] += delta
            totals["negative_combat_samples"] += 1
    totals["mean_quality_delta"] = (
        totals["quality_delta_sum"] / totals["actions_with_metrics"]
        if totals["actions_with_metrics"] else 0.0
    )
    totals["mean_structural_delta"] = (
        totals["structural_delta_sum"] / totals["actions_with_metrics"]
        if totals["actions_with_metrics"] else 0.0
    )
    for label, sample_count, key in (
        ("mean_quality_delta_when_combat_reward_positive", totals["positive_combat_samples"],
         "quality_delta_when_combat_reward_positive"),
        ("mean_quality_delta_when_combat_reward_negative", totals["negative_combat_samples"],
         "quality_delta_when_combat_reward_negative"),
    ):
        totals[label] = totals[key] / sample_count if sample_count else 0.0
    totals["by_action"] = {
        name: {
            **values,
            "mean_quality_delta": values["quality_delta_sum"] / values["actions"]
                if values["actions"] else 0.0,
            "mean_structural_delta": values["structural_delta_sum"] / values["actions"]
                if values["actions"] else 0.0,
        }
        for name, values in sorted(by_action.items())
    }
    report.setdefault("board_quality_metrics", {})[player] = totals


def audit_team_progression(entries: list[dict], player: str, report: dict) -> None:
    """Track separate board strength, bench potential, upgrades, synergies and economy by stage."""
    actions = sorted(
        (entry for entry in entries if isinstance(entry, dict)
         and entry.get("event_type") in ("action", "round_finished")
         and isinstance((entry.get("payload") or {}).get("state_after"), dict)),
        key=lambda e: (e.get("sequence_id", 0), e.get("step", 0)),
    )
    stages = {}
    purchase_classes = Counter()
    purchase_records = []
    direction_changes = 0
    positioning_improved = positioning_worsened = 0
    gold_spent_total = 0
    previous_direction = None
    final_state = {}
    for entry in actions:
        payload = entry.get("payload") or {}
        before, after = payload.get("state_before") or {}, payload.get("state_after") or {}
        snap_before = payload.get("strategic_snapshot_before") or (payload.get("economic_diagnostics") or {}).get("strategic_snapshot_before") or {}
        snap_after = payload.get("strategic_snapshot_after") or (payload.get("economic_diagnostics") or {}).get("strategic_snapshot_after") or {}
        if not snap_after:
            # Backward-compatible fallback for older logs: keep reserve power separate.
            board = _occupied_units(after, "board")
            bench = _occupied_units(after, "bench")
            snap_after = {
                "board_strength": _board_power(after),
                "bench_potential_strength": sum(float(u.get("impact", 0.0) or 0.0) for u in bench),
                "board_unit_count": len(board), "bench_unit_count": len(bench),
                "board_two_star_or_higher": sum(int(u.get("star", 1) or 1) >= 2 for u in board),
                "board_three_star": sum(int(u.get("star", 1) or 1) >= 3 for u in board),
                "combined_pair_count": _pair_count(after),
                "active_synergies": {
                    str(k): int(v or 0) for k, v in (after.get("active_traits") or {}).items()
                },
                "gold": after.get("gold"), "level": after.get("level"),
                "positioning_quality": after.get("positioning_score"),
                "composition_direction": after.get("comp_direction"),
                "composition_focus": after.get("comp_focus"),
                "board_occupancy": len(board) / max(1, len(after.get("board") or [])),
            }
        stage_key = f"{entry.get('stage', '?')}-{entry.get('round_in_stage', '?')}"
        stage = stages.setdefault(stage_key, {
            "stage": stage_key, "actions": 0, "gold_spent": 0, "purchases": 0,
            "purchase_marginal_classes": {}, "board_strength_start": None, "board_strength_end": None,
            "bench_potential_start": None, "bench_potential_end": None,
            "board_two_star_start": None, "board_two_star_end": None,
            "board_three_star_start": None, "board_three_star_end": None,
            "pairs_start": None, "pairs_end": None, "board_occupancy_start": None,
            "board_occupancy_end": None, "gold_start": None, "gold_end": None,
            "level_start": None, "level_end": None, "positioning_delta_sum": 0.0,
            "positioning_samples": 0, "combat_reward_sum": 0.0, "combat_samples": 0,
            "synergy_milestones_reached": [], "synergy_milestones_lost": [],
            "composition_changes": [], "board_strength_delta": 0.0,
            "bench_potential_delta": 0.0,
        })
        current = snap_after
        initial = snap_before or current
        stage["actions"] += 1
        if stage["board_strength_start"] is None:
            stage["board_strength_start"] = float(initial.get("board_strength", _board_power(before)) or 0.0)
            stage["bench_potential_start"] = float(initial.get("bench_potential_strength", 0.0) or 0.0)
            stage["board_two_star_start"] = int(initial.get("board_two_star_or_higher", 0) or 0)
            stage["board_three_star_start"] = int(initial.get("board_three_star", 0) or 0)
            stage["pairs_start"] = int(initial.get("combined_pair_count", _pair_count(before)) or 0)
            stage["board_occupancy_start"] = float(initial.get("board_occupancy", 0.0) or 0.0)
            stage["gold_start"] = initial.get("gold", before.get("gold"))
            stage["level_start"] = initial.get("level", before.get("level"))
        old_board = float(initial.get("board_strength", _board_power(before)) or 0.0)
        new_board = float(current.get("board_strength", _board_power(after)) or 0.0)
        old_bench = float(initial.get("bench_potential_strength", 0.0) or 0.0)
        new_bench = float(current.get("bench_potential_strength", 0.0) or 0.0)
        stage["board_strength_delta"] += new_board - old_board
        stage["bench_potential_delta"] += new_bench - old_bench
        stage["board_strength_end"] = new_board
        stage["bench_potential_end"] = new_bench
        stage["board_two_star_end"] = int(current.get("board_two_star_or_higher", 0) or 0)
        stage["board_three_star_end"] = int(current.get("board_three_star", 0) or 0)
        stage["pairs_end"] = int(current.get("combined_pair_count", _pair_count(after)) or 0)
        stage["board_occupancy_end"] = float(current.get("board_occupancy", 0.0) or 0.0)
        stage["gold_end"] = current.get("gold", after.get("gold"))
        stage["level_end"] = current.get("level", after.get("level"))
        econ = payload.get("economic_diagnostics") or {}
        cost = max(0, int(econ.get("action_cost", 0) or 0))
        stage["gold_spent"] += cost
        gold_spent_total += cost
        action_name = str(payload.get("action_name") or "")
        if action_name == "BUY":
            stage["purchases"] += 1
            marginal = payload.get("purchase_marginal_value") or econ.get("purchase_marginal_value") or {}
            classification = str(marginal.get("classification") or "UNCLASSIFIED")
            classes = stage["purchase_marginal_classes"]
            classes[classification] = classes.get(classification, 0) + 1
            purchase_classes[classification] += 1
            purchase_records.append({
                "step": entry.get("step"), "round": get_round(entry),
                "classification": classification, "champion": econ.get("purchased_champion"),
                "board_strength_delta": marginal.get("board_strength_delta", new_board - old_board),
                "bench_potential_delta": marginal.get("bench_potential_delta", new_bench - old_bench),
                "composition_direction": current.get("composition_direction", after.get("comp_direction")),
            })
        position_delta = float(current.get("positioning_quality", after.get("positioning_score", 0.0)) or 0.0) - float(
            initial.get("positioning_quality", before.get("positioning_score", 0.0)) or 0.0
        )
        stage["positioning_delta_sum"] += position_delta
        stage["positioning_samples"] += 1
        positioning_improved += int(position_delta > 1e-6)
        positioning_worsened += int(position_delta < -1e-6)
        combat = payload.get("combat_reward")
        if isinstance(combat, (int, float)):
            stage["combat_reward_sum"] += float(combat)
            stage["combat_samples"] += 1
        old_synergies = initial.get("active_synergies") or {}
        new_synergies = current.get("active_synergies") or {}
        for trait in sorted(set(old_synergies) | set(new_synergies)):
            old_level, new_level = int(old_synergies.get(trait, 0) or 0), int(new_synergies.get(trait, 0) or 0)
            if new_level > old_level:
                stage["synergy_milestones_reached"].append({"trait": trait, "from": old_level, "to": new_level, "step": entry.get("step")})
            elif new_level < old_level:
                stage["synergy_milestones_lost"].append({"trait": trait, "from": old_level, "to": new_level, "step": entry.get("step")})
        direction = current.get("composition_direction", after.get("comp_direction"))
        if direction != previous_direction and direction and previous_direction is not None:
            direction_changes += 1
            stage["composition_changes"].append({"step": entry.get("step"), "from": previous_direction, "to": direction,
                                                 "focus": current.get("composition_focus", after.get("comp_focus"))})
        if direction:
            previous_direction = direction
        final_state = after
    for values in stages.values():
        values["board_strength_delta"] = round(values["board_strength_delta"], 4)
        values["bench_potential_delta"] = round(values["bench_potential_delta"], 4)
        values["mean_positioning_delta"] = (
            values["positioning_delta_sum"] / values["positioning_samples"] if values["positioning_samples"] else 0.0
        )
        values["mean_combat_reward"] = (
            values["combat_reward_sum"] / values["combat_samples"] if values["combat_samples"] else 0.0
        )
    report.setdefault("team_progression_metrics", {})[player] = {
        "stages": stages,
        "purchase_marginal_classes": dict(purchase_classes),
        "purchase_records": purchase_records,
        "purchases": len(purchase_records),
        "gold_spent_total": gold_spent_total,
        "positioning_improved_actions": positioning_improved,
        "positioning_worsened_actions": positioning_worsened,
        "composition_direction_changes": direction_changes,
        "final_gold": final_state.get("gold"),
        "final_level": final_state.get("level"),
        "final_hp": final_state.get("hp"),
        "final_placement": final_state.get("placement"),
        "interpretation": "Bench strength and pairs are future potential, not current combat strength. Heuristic changes require validation against combat results.",
    }




def _audit_role(unit: dict) -> str:
    for key in ("role", "combat_role", "unit_role", "inferred_role", "profile_role", "class_role"):
        value = unit.get(key)
        if value is None:
            continue
        normalized = re.sub(r"[^a-z0-9]+", "", str(value).casefold())
        if any(token in normalized for token in ("tank", "tanker", "frontline", "guardian")):
            return "tank"
        if any(token in normalized for token in ("carry", "marksman", "mage", "assassin", "backline", "damage")):
            return "carry"
        if any(token in normalized for token in ("fighter", "bruiser", "warrior", "melee")):
            return "fighter"
    traits = unit.get("traits") or unit.get("synergies") or []
    if isinstance(traits, list):
        text_traits = " ".join(str(t.get("name", t) if isinstance(t, dict) else t) for t in traits).casefold()
        if any(token in text_traits for token in ("bruiser", "warden", "bastion", "sentinel")):
            return "tank_trait"
    return "unknown"


def _audit_row(slot: int, unit: dict, state: dict) -> int | None:
    for key in ("row", "board_row", "y", "_audit_row"):
        value = unit.get(key)
        if isinstance(value, int):
            return value
    board = state.get("board")
    if isinstance(board, list) and len(board) >= 28 and all(not isinstance(x, list) for x in board):
        return slot // 7
    return None


def audit_positioning_and_composition(entries: list[dict], player: str, report: dict) -> None:
    """Flag role/row mismatches and core units absent across consecutive snapshots."""
    emitted_positions = set()
    missing_counts: Counter = Counter()
    missing_reported = set()
    for entry in sorted(entries, key=lambda e: (e.get("sequence_id", 0), e.get("step", 0))):
        if not isinstance(entry, dict) or entry.get("event_type") not in ("action", "round_finished", "match_started"):
            continue
        payload = entry.get("payload") or {}
        state = payload.get("state_after") or payload.get("state") or {}
        if not isinstance(state, dict) or not state:
            continue
        board_rows = []
        for slot, unit in [(slot, unit) for _, slot, unit in iter_units(state, ("board",))]:
            row = _audit_row(slot, unit, state)
            if row is not None:
                board_rows.append((slot, unit, row, _audit_role(unit)))
        for slot, unit, row, role in board_rows:
            ident = str(unit.get("uuid") or unit_name(unit))
            if row <= 1 and role == "carry":
                key = (ident, "carry_front")
                if key not in emitted_positions:
                    add_issue(report, "MEDIUM", "CARRY_IN_FRONTLINE", player, get_round(entry), entry.get("step"),
                              f"Carry '{unit_name(unit)}' está nas fileiras 0-1; verificar se está exposto sem necessidade.",
                              {"unit": unit_name(unit), "row": row, "slot": slot, "role": role})
                    emitted_positions.add(key)
            elif row >= 2 and role in ("tank", "tank_trait"):
                key = (ident, "tank_back")
                if key not in emitted_positions:
                    add_issue(report, "MEDIUM", "TANK_IN_BACKLINE", player, get_round(entry), entry.get("step"),
                              f"Tanque '{unit_name(unit)}' está nas fileiras 2+; verificar posicionamento.",
                              {"unit": unit_name(unit), "row": row, "slot": slot, "role": role})
                    emitted_positions.add(key)
        if board_rows and any(role == "carry" for _, _, _, role in board_rows):
            if not any(row <= 1 and role in ("tank", "tank_trait", "fighter") for _, _, row, role in board_rows):
                key = (get_round(entry), "no_frontline")
                if key not in emitted_positions:
                    add_issue(report, "LOW", "NO_FRONTLINE_PROTECTION", player, get_round(entry), entry.get("step"),
                              "Há carry(s) no tabuleiro, mas não foi identificado tank/fighter nas fileiras da frontline.",
                              {"board_roles": [{"unit": unit_name(u), "row": row, "role": role}
                                               for _, u, row, role in board_rows]})
                    emitted_positions.add(key)
        core = state.get("core_units") or state.get("comp_units") or state.get("core_champions") or []
        if isinstance(core, list):
            present = {re.sub(r"[^a-z0-9]+", "", unit_name(u).casefold())
                       for _, _, u in iter_units(state)}
            current_core = set()
            for value in core:
                name = unit_name(value) if isinstance(value, dict) else str(value).strip()
                if not name:
                    continue
                normalized = re.sub(r"[^a-z0-9]+", "", name.casefold())
                current_core.add(normalized)
                if normalized and normalized not in present:
                    missing_counts[normalized] += 1
                    if missing_counts[normalized] in (3, 8) and normalized not in missing_reported:
                        count = missing_counts[normalized]
                        add_issue(report, "HIGH" if count >= 8 else "MEDIUM", "CORE_UNIT_MISSING_REPEATEDLY",
                                  player, get_round(entry), entry.get("step"),
                                  f"Unidade core '{name}' ficou ausente do tabuleiro e banco em {count} snapshots consecutivos.",
                                  {"core_unit": name, "missing_snapshots": count,
                                   "comp_direction": state.get("comp_direction"), "comp_focus": state.get("comp_focus")})
                        missing_reported.add(normalized)
                else:
                    missing_counts.pop(normalized, None)
                    missing_reported.discard(normalized)
            # A core list that no longer includes a champion ends that missing-unit episode.
            for normalized in list(missing_counts):
                if normalized not in current_core:
                    missing_counts.pop(normalized, None)
                    missing_reported.discard(normalized)
        else:
            # No core metadata means the gap cannot be called consecutive.
            missing_counts.clear()
            missing_reported.clear()

def audit_json(path: Path, doc: dict, report: dict, loop_window: int, comp_window: int) -> None:
    player_id = doc.get("player_number")
    if player_id is None:
        raw_id = doc.get("player_id")
        player_id = raw_id + 1 if isinstance(raw_id, int) else path.stem
    player = f"Jogador {player_id}"
    report["players_seen"].add(str(player_id))
    report["entries_read"] += len(doc["entries"])
    audit_purchase_sequences(doc["entries"], player, report)
    audit_economic_actions(doc["entries"], player, report)
    audit_composition_direction_changes(doc["entries"], player, report)
    audit_board_quality(doc["entries"], player, report)
    audit_positioning_and_composition(doc["entries"], player, report)
    audit_team_progression(doc["entries"], player, report)
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
    if report.get("economic_action_metrics"):
        lines += ["## Auditoria econômica por ação", "",
                  "| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |",
                   "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for player, metrics in sorted(report["economic_action_metrics"].items()):
            lines.append(
                f"| {player} | {metrics['actions']} | {metrics['gold_spent']} | {metrics['gold_recovered']} | "
                f"{metrics['potential_interest_lost']} | {metrics['xp_without_level_up']} | {metrics['xp_level_up_unused']} | "
                f"{metrics['rerolls_without_immediate_gain']} | {metrics['rerolls_followed_by_pass']} | "
                f"{metrics.get('final_gold', '—')} | {metrics.get('final_board_power', '—')} |"
            )
            action_breakdown = ", ".join(
                f"{name}: {values['gold_spent']}g"
                for name, values in sorted(metrics.get("by_action", {}).items())
            ) or "nenhum"
            stage_breakdown = ", ".join(
                f"stage {stage}: {values['gold_spent']}g"
                for stage, values in sorted(metrics.get("by_stage", {}).items())
            ) or "nenhum"
            lines.append(f"- {player} — gasto por ação: {action_breakdown}")
            lines.append(f"- {player} — gasto por estágio: {stage_breakdown}")
        lines += ["", "Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.", ""]

    if report.get("composition_direction_metrics"):
        lines += ["## Auditoria de mudanças de composição", "",
                  "| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |",
                  "|---|---:|---:|---:|---:|"]
        for player, metrics in sorted(report["composition_direction_metrics"].items()):
            lines.append(
                f"| {player} | {metrics['direction_changes']} | "
                f"{metrics['changes_with_measurable_gain']} | "
                f"{metrics['changes_without_measurable_gain']} | "
                f"{metrics.get('rate_without_measurable_gain', 0.0):.1%} |"
            )
        lines += ["", "Os detalhes por transição ficam em audit_report.json. "
                  "‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.", ""]

    if report.get("board_quality_metrics"):
        lines += ["## Qualidade estrutural e posicionamento do tabuleiro", "",
                  "| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ médio qualidade | Δ estrutural médio | Δ qualidade quando combate positivo | Δ qualidade quando combate negativo |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for player, metrics in sorted(report["board_quality_metrics"].items()):
            lines.append(
                f"| {player} | {metrics['actions_with_metrics']} | "
                f"{metrics['positive_quality_delta']} | {metrics['negative_quality_delta']} | "
                f"{metrics['neutral_quality_delta']} | {metrics['mean_quality_delta']:.4f} | "
                f"{metrics['mean_structural_delta']:.4f} | "
                f"{metrics['mean_quality_delta_when_combat_reward_positive']:.4f} | "
                f"{metrics['mean_quality_delta_when_combat_reward_negative']:.4f} |"
            )
            breakdown = ", ".join(
                f"{name}: Δ {values['mean_quality_delta']:.4f} ({values['actions']} ações)"
                for name, values in sorted(metrics.get("by_action", {}).items())
            ) or "nenhuma ação com métrica"
            lines.append(f"- {player} — ganho médio por ação: {breakdown}")
        lines += ["", "A pontuação é uma heurística para auditoria, não uma verdade absoluta. "
                  "Compare-a com recompensas e resultados de combate; correlação não prova causalidade.", ""]

    if report.get("team_progression_metrics"):
        lines += ["## Evolução estratégica por jogador e estágio", "",
                  "| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |",
                  "|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|"]
        for player, metrics in sorted(report["team_progression_metrics"].items()):
            for stage_name, stage in sorted(metrics.get("stages", {}).items()):
                lines.append(
                    f"| {player} | {stage_name} | {stage['actions']} | {stage['board_strength_delta']:.3f} | "
                    f"{stage['bench_potential_delta']:.3f} | {stage.get('board_two_star_start', 0)} → {stage.get('board_two_star_end', 0)} | "
                    f"{stage.get('pairs_start', 0)} → {stage.get('pairs_end', 0)} | "
                    f"{float(stage.get('board_occupancy_start') or 0):.0%} → {float(stage.get('board_occupancy_end') or 0):.0%} | "
                    f"{stage.get('gold_start', '—')} → {stage.get('gold_end', '—')} | {stage['gold_spent']} | "
                    f"{stage.get('level_start', '—')} → {stage.get('level_end', '—')} | "
                    f"{stage.get('mean_positioning_delta', 0.0):.3f} | {stage.get('mean_combat_reward', 0.0):.3f} |"
                )
            classes = ", ".join(f"{name}: {count}" for name, count in sorted(metrics.get("purchase_marginal_classes", {}).items())) or "nenhuma compra classificada"
            lines.append(f"- {player} — valor marginal das compras: {classes}; mudanças de composição: {metrics.get('composition_direction_changes', 0)}; posicionamento melhorou em {metrics.get('positioning_improved_actions', 0)} ações e piorou em {metrics.get('positioning_worsened_actions', 0)}.")
            lines.append(f"- {player} — estado final: ouro {metrics.get('final_gold', '—')}, nível {metrics.get('final_level', '—')}, vida {metrics.get('final_hp', '—')}, colocação {metrics.get('final_placement', '—')}.")
        lines += ["", "Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.", ""]

    if report.get("purchase_sequence_metrics"):
        lines += ["## Auditoria de compras e vendas", "",
                  "| Jogador | Compras | Vendas | Revertidas ≤1 ação | ≤2 ações | ≤4 ações | Ouro perdido | Upgrades | Vendas core/par | Valor médio |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for player, metrics in sorted(report["purchase_sequence_metrics"].items()):
            lines.append(
                f"| {player} | {metrics['buys']} | {metrics['sells']} | "
                f"{metrics['reversed_1']} | {metrics['reversed_2']} | {metrics['reversed_4']} | "
                f"{metrics['net_gold_lost_reversed']} | {metrics['upgrade_completing_buys']} | "
                f"{metrics['core_or_pair_sales']} | {metrics.get('average_strategic_value_per_purchase', 0.0)} |"
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
              "- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.",
              "- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.",
              "- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.", ""]
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
              "purchase_sequence_metrics": {}, "economic_action_metrics": {},
              "composition_direction_metrics": {},
              "board_quality_metrics": {},
              "team_progression_metrics": {},
              "entries_read": 0, "diagnostics_missing": 0, "issues": [], "notes": [],
              "mask_note_added": False}
    for path in files:
        if path.suffix.lower() == ".json":
            doc = read_json(path)
            if doc:
                audit_json(path, doc, report, args.loop_window, args.comp_window)
        elif path.suffix.lower() == ".tft":
            # Current PlayerJsonLogWriter stores structured JSON documents in .tft
            # files. Prefer structured analysis; fall back to legacy text parsing.
            doc = read_json(path)
            if doc:
                audit_json(path, doc, report, args.loop_window, args.comp_window)
            else:
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
