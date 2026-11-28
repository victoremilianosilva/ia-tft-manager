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


def _item_key(value: Any) -> str:
    if isinstance(value, Mapping):
        for key in ("item_instance_id", "instance_id", "uuid", "item_id", "id"):
            candidate = value.get(key)
            if candidate is not None and str(candidate).strip():
                return str(candidate).strip()
        raise ValueError("Item nativo sem identidade estável.")
    if isinstance(value, bool) or value is None:
        raise ValueError("Identidade de item inválida.")
    if isinstance(value, (str, int)):
        result = str(value).strip()
        if result:
            return result
    raise ValueError("Formato de identidade de item não suportado.")


def _catalog_counts(player: Mapping[str, Any], field: str) -> dict[str, int]:
    rows = player.get(field)
    if not isinstance(rows, Sequence):
        raise ValueError(f"Snapshot sem {field} nativo.")
    result = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError(f"Registro inválido em {field}.")
        catalog_id = str(row.get("catalog_id", "")).strip()
        count = _int(row.get("count"), f"{field}.count")
        if not catalog_id or count is None or count <= 0 or catalog_id in result:
            raise ValueError(f"Identidade/contagem inválida ou duplicada em {field}.")
        result[catalog_id] = count
    return result


def _equipped_items(player: Mapping[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    rows = player.get("equipped_items")
    if not isinstance(rows, Sequence):
        raise ValueError("Snapshot sem equipped_items nativo.")
    result = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("Registro equipped_items inválido.")
        unit_uuid = str(row.get("unit_uuid", "")).strip()
        catalog_id = str(row.get("catalog_id", "")).strip()
        location = row.get("location")
        slot = _int(row.get("slot"), "equipped_items.slot")
        if not unit_uuid or not catalog_id or location not in ("board", "bench") or slot is None or not 0 <= slot < (28 if location == "board" else 9):
            raise ValueError("Identidade/localização inválida em equipped_items.")
        key = (unit_uuid, catalog_id)
        if key in result:
            raise ValueError("Item equipado duplicado para unidade/catálogo.")
        result[key] = {"unit_uuid": unit_uuid, "catalog_id": catalog_id,
            "location": location, "slot": slot}
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
    for snapshot in (before_snapshot, after_snapshot):
        if (
            snapshot.get("contract_id") != "tft.native-state-snapshot"
            or _int(snapshot.get("contract_version"), "snapshot.contract_version") != 7
            or snapshot.get("source_namespace") != "tft.engine.observation-snapshot"
            or snapshot.get("producer") != "TFTEngine::get_audit_snapshot"
        ):
            raise RuntimeError("Snapshot pré/pós-ação não pertence ao contrato nativo v7.")
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

    economy_events = after_snapshot.get("economy_resolution_events")
    if not isinstance(economy_events, Sequence):
        raise RuntimeError("Snapshot pós-ação sem lista nativa de resolução econômica.")
    if any(not isinstance(event, Mapping) for event in economy_events):
        raise RuntimeError("Evento nativo de resolução econômica inválido.")
    economy_resolved = {
        _int(event.get("player_id"), "economy_resolution.player_id")
        for event in economy_events
    }
    pvp_credit_events = after_snapshot.get("pvp_result_credit_events")
    if not isinstance(pvp_credit_events, Sequence) or any(
        not isinstance(event, Mapping) for event in pvp_credit_events
    ):
        raise RuntimeError("Snapshot pós-ação sem eventos nativos de crédito PvP.")
    pvp_credit_players = {
        player_id
        for event in pvp_credit_events
        for player_id in (
            _int(event.get("winner_player_id"), "pvp_credit.winner_player_id"),
            _int(event.get("loser_player_id"), "pvp_credit.loser_player_id"),
        )
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
        applied_value = trace.get("handler_applied")
        if not isinstance(applied_value, bool):
            raise RuntimeError(f"handler_applied não é booleano para player_id={player_id}.")
        applied = applied_value
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
        pvp_credit_overlapped = player_id in pvp_credit_players
        gold_delta = None if resolved or pvp_credit_overlapped else after_gold - before_gold
        xp_delta = None if resolved else (
            _int(after.get("xp"), "after.xp") - _int(before.get("xp"), "before.xp")
        )
        level_delta = None if resolved else (
            _int(after.get("level"), "after.level") - _int(before.get("level"), "before.level")
        )
        round_income_events = [
            dict(event) for event in economy_events
            if _int(event.get("player_id"), "economy_resolution.player_id") == player_id
        ]
        player_pvp_credit_events = [
            dict(event) for event in pvp_credit_events
            if player_id in (
                _int(event.get("winner_player_id"), "pvp_credit.winner_player_id"),
                _int(event.get("loser_player_id"), "pvp_credit.loser_player_id"),
            )
        ]
        equipped_item_changes = []
        item_inventory_deltas = {}
        item_component_deltas = {}
        if family == "item_action":
            before_equipped = _equipped_items(before)
            after_equipped = _equipped_items(after)
            for row in before_equipped.values():
                unit = before_units.get(row["unit_uuid"])
                if unit is None or (unit["location"], unit["slot"]) != (row["location"], row["slot"]):
                    raise RuntimeError("equipped_items pré-ação diverge da unidade física.")
            for row in after_equipped.values():
                unit = after_units.get(row["unit_uuid"])
                if unit is None or (unit["location"], unit["slot"]) != (row["location"], row["slot"]):
                    raise RuntimeError("equipped_items pós-ação diverge da unidade física.")
            for key in sorted(set(before_equipped) | set(after_equipped)):
                previous = before_equipped.get(key)
                current = after_equipped.get(key)
                if previous is None:
                    equipped_item_changes.append({"kind": "equipped", **current})
                elif current is None:
                    equipped_item_changes.append({"kind": "unequipped", **previous})
                elif previous != current:
                    equipped_item_changes.append({"kind": "moved", "before": previous, "after": current})
            for field, target in (("item_inventory_counts", item_inventory_deltas),
                                  ("item_component_counts", item_component_deltas)):
                before_counts = _catalog_counts(before, field)
                after_counts = _catalog_counts(after, field)
                for catalog_id in sorted(set(before_counts) | set(after_counts)):
                    delta = after_counts.get(catalog_id, 0) - before_counts.get(catalog_id, 0)
                    if delta:
                        target[catalog_id] = delta

        item_changes = []
        if family == "item_action":
            for uuid in sorted(set(before_units) & set(after_units)):
                previous_items = before_units[uuid]["item_ids"]
                current_items = after_units[uuid]["item_ids"]
                previous_keys = [_item_key(item) for item in previous_items]
                current_keys = [_item_key(item) for item in current_items]
                if len(previous_keys) != len(set(previous_keys)) or len(current_keys) != len(set(current_keys)):
                    raise RuntimeError("Snapshot contém identidade de item duplicada na mesma unidade.")
                added_items = [item for item, key in zip(current_items, current_keys) if key not in set(previous_keys)]
                removed_items = [item for item, key in zip(previous_items, previous_keys) if key not in set(current_keys)]
                if added_items or removed_items:
                    item_changes.append({
                        "unit_uuid": uuid,
                        "item_ids_before": previous_keys,
                        "item_ids_after": current_keys,
                        "items_added": [_item_key(item) for item in added_items],
                        "items_removed": [_item_key(item) for item in removed_items],
                    })

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
        pre_positional = _finite(before.get("board_positional_score", 0.0), "before.board_positional_score")
        post_positional = _finite(after.get("board_positional_score", 0.0), "after.board_positional_score")
        pre_structural = _finite(before.get("board_structural_score", 0.0), "before.board_structural_score")
        post_structural = _finite(after.get("board_structural_score", 0.0), "after.board_structural_score")

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
                "shop_revision_changes": (
                    None if family == "reroll" and resolved
                    else (shop_revision_changes if family == "reroll" else [])
                ),
                "shop_revision_changes_unattributed": (
                    shop_revision_changes if family == "reroll" and resolved else []
                ),
                "shop_refresh_overlapped_with_round_resolution": bool(
                    family == "reroll" and resolved
                ),
                "xp_delta": xp_delta if family == "xp_purchase" else None,
                "level_delta": level_delta if family == "xp_purchase" else None,
                "gold_before": before_gold,
                "gold_after": after_gold,
                "gold_delta": gold_delta,
                "interest_if_resolved_now_before": before_interest,
                "interest_if_resolved_now_after": after_interest,
                "interest_if_resolved_now_delta": (
                    None if resolved or pvp_credit_overlapped
                    else after_interest - before_interest
                ),
                "economy_resolution_overlapped": resolved,
                "pvp_credit_overlapped": pvp_credit_overlapped,
                "round_income_events": round_income_events,
                "pvp_result_credit_events": player_pvp_credit_events,
                "item_assignment_changes": item_changes if family == "item_action" else [],
                "equipped_item_changes": equipped_item_changes if family == "item_action" else [],
                "item_inventory_count_deltas": item_inventory_deltas if family == "item_action" else {},
                "item_component_count_deltas": item_component_deltas if family == "item_action" else {},
                "board_unit_moves": moved if family in ("deploy", "positioning") else [],
                "positioning_score_before": pre_position,
                "positioning_score_after": post_position,
                "positioning_score_delta": post_position - pre_position,
                "board_quality_before": pre_quality,
                "board_quality_after": post_quality,
                "board_quality_delta": post_quality - pre_quality,
                "board_positional_before": pre_positional,
                "board_positional_after": post_positional,
                "board_positional_delta": post_positional - pre_positional,
                "board_structural_before": pre_structural,
                "board_structural_after": post_structural,
                "board_structural_delta": post_structural - pre_structural,
                "exposed_carries_before": _int(before.get("board_exposed_carries", 0), "before.board_exposed_carries"),
                "exposed_carries_after": _int(after.get("board_exposed_carries", 0), "after.board_exposed_carries"),
                "frontline_count_before": _int(before.get("board_frontline_count", 0), "before.board_frontline_count"),
                "frontline_count_after": _int(after.get("board_frontline_count", 0), "after.board_frontline_count"),
                "isolated_frontline_count_before": _int(before.get("board_isolated_frontline_count", 0), "before.board_isolated_frontline_count"),
                "isolated_frontline_count_after": _int(after.get("board_isolated_frontline_count", 0), "after.board_isolated_frontline_count"),
                "important_bench_units_unplayed_before": _int(before.get("board_important_bench_units_unplayed", 0), "before.board_important_bench_units_unplayed"),
                "important_bench_units_unplayed_after": _int(after.get("board_important_bench_units_unplayed", 0), "after.board_important_bench_units_unplayed"),
            },
            "causal_attribution": "not_established",
            "reward": None,
            "reward_eligible": False,
        }
        events.append(event)
    return events
