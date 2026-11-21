"""Factual, audit-only producers for action consequences.

The producer compares two authoritative native snapshots around one executed
decision. It emits observations, never reward values or Shadow-derived labels.
"""
from __future__ import annotations

import math
from collections import Counter
from collections.abc import Mapping, Sequence
from typing import Any

ACTION_FAMILIES = {
    0: "purchase",
    1: "reroll",
    2: "xp_purchase",
    3: "deploy",
    4: "positioning",
    5: "sale",
    6: "pass",
    7: "item_action",
    8: "item_action",
}
_PLAYERS = 8


def _int(value: Any, field: str, default: int | None = None) -> int | None:
    if value is None and default is not None:
        return default
    if isinstance(value, bool):
        raise ValueError(f"{field} inválido.")
    try:
        return int(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{field} inválido.") from exc


def _finite(value: Any, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{field} inválido.") from exc
    if not math.isfinite(number):
        raise ValueError(f"{field} não finito.")
    return number


def _owned_units(player: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for location in ("board", "bench"):
        rows = player.get(location)
        if not isinstance(rows, Sequence):
            raise ValueError(f"Snapshot sem {location} nativo.")
        for slot, unit in enumerate(rows):
            if not isinstance(unit, Mapping):
                raise ValueError(f"Unidade inválida em {location}[{slot}].")
            if not unit.get("occupied"):
                continue
            uuid = str(unit.get("uuid", "")).strip()
            champion = str(unit.get("champion_id", "")).strip()
            if not uuid or not champion:
                raise ValueError("Unidade ocupada sem UUID/champion_id.")
            result[uuid] = {
                "uuid": uuid,
                "champion_id": champion,
                "star": _int(unit.get("star"), "star"),
                "cost": _int(unit.get("cost"), "cost"),
                "location": location,
                "slot": slot,
                "item_ids": list(unit.get("item_ids", unit.get("items", [])) or []),
            }
    return result


def _copy_equivalents(units: Mapping[str, Mapping[str, Any]]) -> Counter:
    copies = Counter()
    for unit in units.values():
        star = int(unit["star"])
        if star not in (1, 2, 3):
            raise ValueError("Tier de unidade fora do contrato factual.")
        copies[str(unit["champion_id"])] += (1, 3, 9)[star - 1]
    return copies


def _star_tiers(units: Mapping[str, Mapping[str, Any]]) -> Counter:
    tiers = Counter()
    for unit in units.values():
        tiers[(str(unit["champion_id"]), int(unit["star"]))] += 1
    return tiers


def _shop(player: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows = player.get("shop")
    revisions = player.get("shop_offer_revisions")
    if not isinstance(rows, Sequence) or len(rows) != 5:
        raise ValueError("Snapshot sem as cinco ofertas nativas.")
    if not isinstance(revisions, Sequence) or len(revisions) != 5:
        raise ValueError("Snapshot sem revisões nativas da loja.")
    result = []
    for slot, offer in enumerate(rows):
        if not isinstance(offer, Mapping):
            raise ValueError("Oferta nativa inválida.")
        result.append({
            "slot": slot,
            "occupied": bool(offer.get("occupied")),
            "champion_id": str(offer.get("champion_id", "")),
            "cost": _int(offer.get("cost", 0), "shop.cost"),
            "revision": _int(revisions[slot], "shop_offer_revision"),
        })
    return result


def build_action_outcome_events(
    *,
    before_snapshot: Mapping[str, Any],
    after_snapshot: Mapping[str, Any],
    action_traces: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Build one factual event per player decision from native snapshot diffs."""
    if not isinstance(before_snapshot, Mapping) or not isinstance(after_snapshot, Mapping):
        raise TypeError("Snapshots nativos pré/pós-ação são obrigatórios.")
    for field in ("engine_instance_id", "episode_id"):
        if before_snapshot.get(field) != after_snapshot.get(field):
            raise RuntimeError(f"Snapshots pré/pós-ação divergem em {field}.")
    engine_id = str(before_snapshot.get("engine_instance_id", "")).strip()
    episode_id = _int(before_snapshot.get("episode_id"), "episode_id")
    before_seq = _int(before_snapshot.get("snapshot_sequence"), "before.snapshot_sequence")
    after_seq = _int(after_snapshot.get("snapshot_sequence"), "after.snapshot_sequence")
    if not engine_id or before_seq is None or after_seq is None or after_seq <= before_seq:
        raise RuntimeError("Sequência de snapshots inválida para atribuição factual.")
    before_players = before_snapshot.get("players")
    after_players = after_snapshot.get("players")
    before_sequences = before_snapshot.get("player_decision_sequences")
    after_sequences = after_snapshot.get("player_decision_sequences")
    if any(not isinstance(rows, Sequence) or len(rows) != _PLAYERS for rows in
           (before_players, after_players, before_sequences, after_sequences)):
        raise RuntimeError("Snapshots sem oito jogadores/sequências.")
    if not isinstance(action_traces, Sequence) or len(action_traces) != _PLAYERS:
        raise RuntimeError("Action traces incompletos para produtores factuais.")

    economy_resolved = {
        _int(event.get("player_id"), "economy_resolution.player_id")
        for event in (after_snapshot.get("economy_resolution_events") or [])
        if isinstance(event, Mapping)
    }
    events = []
    for player_id in range(_PLAYERS):
        before = before_players[player_id]
        after = after_players[player_id]
        trace = action_traces[player_id]
        if not all(isinstance(value, Mapping) for value in (before, after, trace)):
            raise RuntimeError(f"Registro nativo inválido para player_id={player_id}.")
        if _int(before.get("player_id"), "before.player_id") != player_id or \
           _int(after.get("player_id"), "after.player_id") != player_id or \
           _int(trace.get("player_id"), "trace.player_id") != player_id:
            raise RuntimeError(f"Identidade de jogador desalinhada: {player_id}.")
        source_player_seq = _int(before_sequences[player_id], "before.player_sequence")
        outcome_player_seq = _int(after_sequences[player_id], "after.player_sequence")
        if source_player_seq is None or outcome_player_seq is None or outcome_player_seq <= source_player_seq:
            raise RuntimeError(f"Sequência por jogador não avançou: {player_id}.")

        action = trace.get("effective_action")
        if not isinstance(action, Sequence) or len(action) < 2:
            raise RuntimeError(f"Ação efetiva ausente para player_id={player_id}.")
        action_type = _int(action[0], "effective_action.type")
        if action_type not in ACTION_FAMILIES:
            raise RuntimeError(f"Tipo de ação sem família factual: {action_type}.")
        family = ACTION_FAMILIES[action_type]
        applied = bool(trace.get("handler_applied", False))
        before_units = _owned_units(before)
        after_units = _owned_units(after)
        before_copies = _copy_equivalents(before_units)
        after_copies = _copy_equivalents(after_units)
        before_tiers = _star_tiers(before_units)
        after_tiers = _star_tiers(after_units)
        star_tier_deltas = [
            {
                "champion_id": champion,
                "star": star,
                "count_delta": int(after_tiers[(champion, star)] - before_tiers[(champion, star)]),
            }
            for champion, star in sorted(set(before_tiers) | set(after_tiers))
            if after_tiers[(champion, star)] != before_tiers[(champion, star)]
        ]
        upgrades = []
        for uuid, current in after_units.items():
            previous = before_units.get(uuid)
            if previous and int(current["star"]) > int(previous["star"]):
                upgrades.append({
                    "uuid": uuid,
                    "champion_id": current["champion_id"],
                    "star_before": previous["star"],
                    "star_after": current["star"],
                })
        removed = [unit for uuid, unit in before_units.items() if uuid not in after_units]
        added = [unit for uuid, unit in after_units.items() if uuid not in before_units]
        copy_delta = {
            champion: int(after_copies[champion] - before_copies[champion])
            for champion in sorted(set(before_copies) | set(after_copies))
            if after_copies[champion] != before_copies[champion]
        }
        before_shop = _shop(before)
        after_shop = _shop(after)
        shop_revision_changes = [
            {"slot": slot, "before": before_shop[slot]["revision"],
             "after": after_shop[slot]["revision"],
             "offer_before": before_shop[slot], "offer_after": after_shop[slot]}
            for slot in range(5)
            if before_shop[slot]["revision"] != after_shop[slot]["revision"]
        ]
        selected_slot = _int(action[1], "effective_action.shop_slot", 0)
        selected_offer = before_shop[selected_slot] if 0 <= selected_slot < 5 else None
        before_gold = _int(before.get("gold"), "before.gold")
        after_gold = _int(after.get("gold"), "after.gold")
        before_interest = _int(before.get("interest_if_resolved_now"), "before.interest")
        after_interest = _int(after.get("interest_if_resolved_now"), "after.interest")
        resolved = player_id in economy_resolved
        gold_delta = None if resolved else after_gold - before_gold
        xp_delta = None if resolved else (
            _int(after.get("xp"), "after.xp") - _int(before.get("xp"), "before.xp")
        )
        level_delta = None if resolved else (
            _int(after.get("level"), "after.level") - _int(before.get("level"), "before.level")
        )
        round_income_events = [
            dict(event) for event in (after_snapshot.get("economy_resolution_events") or [])
            if isinstance(event, Mapping) and _int(event.get("player_id"), "economy_resolution.player_id") == player_id
        ]
        moved = []
        for uuid, current in after_units.items():
            previous = before_units.get(uuid)
            if previous and (
                previous["location"] != current["location"] or
                previous["slot"] != current["slot"]
            ):
                moved.append({
                    "uuid": uuid,
                    "from_location": previous["location"],
                    "from_slot": previous["slot"],
                    "to_location": current["location"],
                    "to_slot": current["slot"],
                })
        pre_position = _finite(before.get("positioning_score", 0.0), "before.positioning_score")
        post_position = _finite(after.get("positioning_score", 0.0), "after.positioning_score")
        pre_quality = _finite(before.get("board_quality_score", 0.0), "before.board_quality_score")
        post_quality = _finite(after.get("board_quality_score", 0.0), "after.board_quality_score")

        event = {
            "contract_id": "tft.reward-action-outcome.v1",
            "contract_version": 1,
            "producer": "build_action_outcome_events",
            "source": "paired_native_state_snapshots",
            "event_id": f"{engine_id}/episode/{episode_id}/decision/{source_player_seq}/player/{player_id}",
            "engine_instance_id": engine_id,
            "episode_id": episode_id,
            "player_id": player_id,
            "action": {
                "family": family,
                "type": action_type,
                "effective_action": list(map(int, action)),
                "handler_applied": applied,
                "status_reason": str(trace.get("status_reason", "")),
            },
            "source_decision": {
                "snapshot_sequence": before_seq,
                "player_decision_sequence": source_player_seq,
                "round": _int(before_snapshot.get("round"), "before.round"),
            },
            "outcome_snapshot": {
                "snapshot_sequence": after_seq,
                "player_decision_sequence": outcome_player_seq,
                "round": _int(after_snapshot.get("round"), "after.round"),
            },
            "facts": {
                "selected_shop_offer": selected_offer if family == "purchase" else None,
                "owned_copy_equivalent_delta": copy_delta if family in ("purchase", "sale") else {},
                "upgrades_observed": upgrades if family in ("purchase", "sale") else [],
                "star_tier_count_deltas": star_tier_deltas if family in ("purchase", "sale") else [],
                "units_added": added if family == "purchase" else [],
                "units_removed": removed if family == "sale" else [],
                "shop_revision_changes": shop_revision_changes if family == "reroll" else [],
                "xp_delta": xp_delta if family == "xp_purchase" else None,
                "level_delta": level_delta if family == "xp_purchase" else None,
                "gold_before": before_gold,
                "gold_after": after_gold,
                "gold_delta": gold_delta,
                "interest_if_resolved_now_before": before_interest,
                "interest_if_resolved_now_after": after_interest,
                "interest_if_resolved_now_delta": None if resolved else after_interest - before_interest,
                "economy_resolution_overlapped": resolved,
                "round_income_events": round_income_events,
                "board_unit_moves": moved if family in ("deploy", "positioning") else [],
                "positioning_score_before": pre_position,
                "positioning_score_after": post_position,
                "positioning_score_delta": post_position - pre_position,
                "board_quality_before": pre_quality,
                "board_quality_after": post_quality,
                "board_quality_delta": post_quality - pre_quality,
            },
            "causal_attribution": "not_established",
            "reward": None,
            "reward_eligible": False,
        }
        events.append(event)
    return events
