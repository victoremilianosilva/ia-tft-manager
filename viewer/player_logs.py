"""Per-player legacy-style TFT text logs, with structured entries kept in memory.

The persisted .tft files are readable UTF-8 timelines matching the old observer.
The native audit snapshot does not expose the old impact helper, so i: uses the
native board-power contribution (cost * star * 2).
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ACTION_NAMES = {
    0: "BUY", 1: "REROLL", 2: "BUY_XP", 3: "MOVE_BENCH",
    4: "MOVE_BOARD", 5: "SELL", 6: "PASS",
    7: "EQUIP_FROM_INVENTORY", 8: "CRAFT_AND_EQUIP",
}
ROLE_ABBREVIATIONS = {0: "T", 1: "C", 2: "S", 3: "F", 4: "A"}
ROLE_NAMES = {0: "tank", 1: "carry", 2: "support", 3: "fighter", 4: "assassin"}


def _jsonable(value: Any):
    if hasattr(value, "tolist"):
        try:
            return value.tolist()
        except (TypeError, ValueError):
            pass
    if hasattr(value, "item"):
        try:
            return value.item()
        except (TypeError, ValueError):
            pass
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, float):
        return value if value == value and abs(value) != float("inf") else None
    if isinstance(value, (str, int, bool)) or value is None:
        return value
    return str(value)


def _player_by_id(players, player_id):
    for player in players or []:
        try:
            if int(player.get("player_id", -1)) == player_id:
                return player
        except (AttributeError, TypeError, ValueError):
            continue
    return {}


def _round_coordinates(round_number: int) -> tuple[int, int]:
    number = max(1, int(round_number or 1))
    if number <= 4:
        return 1, number
    offset = number - 5
    return 2 + offset // 7, offset % 7 + 1


def _synergy_level(count: int) -> int:
    if count >= 9:
        return 3
    if count >= 6:
        return 2
    if count >= 3:
        return 1
    return 0


class PlayerJsonLogWriter:
    """Persists one self-contained legacy-style .tft timeline for each lobby seat."""

    def __init__(
        self, session_dir: str | Path, *, match_id: str, checkpoint_sha256: str,
        seed: int, deterministic: bool, catalog_path: str | Path,
        initial_snapshot: dict | None = None, flush_interval_steps: int = 10,
    ):
        self.session_dir = Path(session_dir)
        self.session_dir.mkdir(parents=True, exist_ok=True)
        self.match_id = str(match_id)
        self.checkpoint_sha256 = str(checkpoint_sha256)
        self.seed = int(seed)
        self.deterministic = bool(deterministic)
        self.flush_interval_steps = max(1, int(flush_interval_steps))
        self._sequence = [0] * 8
        self._pass_logged = [False] * 8
        self._dirty = set(range(8))
        self._closed = False
        self._catalog_by_alias: dict[str, dict] = {}
        self._load_catalog(Path(catalog_path))

        created_at = datetime.now(timezone.utc).isoformat()
        self.documents = []
        self.paths = []
        for player_id in range(8):
            player_number = player_id + 1
            self.documents.append({
                "schema_version": 1,
                "log_format": "tft_player_log",
                "match_id": self.match_id,
                "player_id": player_id,
                "player_number": player_number,
                "player_label": f"Jogador {player_number}",
                "checkpoint_sha256": self.checkpoint_sha256,
                "seed": self.seed,
                "deterministic": self.deterministic,
                "created_at": created_at,
                "updated_at": created_at,
                "impact_estimate_formula": "cost * star * 2.0 (contribuição de board_power da engine C++)",
                "entries": [],
            })
            self.paths.append(self.session_dir / f"player_{player_number}_log.tft")
        snapshot = initial_snapshot or {}
        initial_round = int(snapshot.get("round", 1) or 1)
        stage, round_in_stage = _round_coordinates(initial_round)
        timestamp, timestamp_iso = self._timestamp()
        for player_id in range(8):
            audit = _player_by_id(snapshot.get("audit_players", []), player_id)
            public = _player_by_id(snapshot.get("players", []), player_id)
            self._append_entry(
                player_id, timestamp=timestamp, timestamp_iso=timestamp_iso,
                step=0, round_number=initial_round, stage=stage,
                round_in_stage=round_in_stage, event_type="match_started",
                text=f"--- INÍCIO DA PARTIDA · JOGADOR {player_id + 1} ---",
                tag="round_msg",
                data={"state": self._player_snapshot(audit, public)},
            )
        self.flush(force=True)

    @staticmethod
    def _timestamp():
        now = datetime.now().astimezone()
        return now.strftime("%H:%M:%S"), now.isoformat()

    def _load_catalog(self, catalog_path: Path):
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            catalog = []
        if not isinstance(catalog, list):
            return
        for definition in catalog:
            if not isinstance(definition, dict):
                continue
            for alias in (definition.get("apiName"), definition.get("characterName"), definition.get("name")):
                if isinstance(alias, str) and alias.strip():
                    self._catalog_by_alias[alias.casefold()] = definition

    def _definition(self, unit: dict | None) -> dict:
        if not unit or not unit.get("occupied", True):
            return {}
        key = str(unit.get("champion_id") or unit.get("apiName") or unit.get("api_name") or unit.get("name") or "")
        return self._catalog_by_alias.get(key.casefold(), {})

    def _unit_info(self, unit: dict | None, slot: int, location: str) -> dict:
        if not unit or not unit.get("occupied", True):
            return {"slot": int(slot), "location": location, "occupied": False}
        definition = self._definition(unit)
        profile = definition.get("combat_profile", {})
        if not isinstance(profile, dict):
            profile = {}
        raw_role = profile.get("role", definition.get("role"))
        try:
            role = int(raw_role) if raw_role is not None else None
        except (TypeError, ValueError):
            role = None
        cost = int(unit.get("cost", definition.get("cost", 0)) or 0)
        star = max(1, int(unit.get("star", 1) or 1))
        impact = float(cost * star * 2.0)
        return {
            "slot": int(slot), "location": location, "occupied": True,
            "champion_id": unit.get("champion_id", ""), "name": definition.get("name") or unit.get("champion_id", "?"),
            "uuid": unit.get("uuid"), "cost": cost, "star": star, "role": role,
            "role_name": profile.get("role_name", definition.get("role_name", ROLE_NAMES.get(role, "unknown"))),
            "role_abbreviation": ROLE_ABBREVIATIONS.get(role, "?"),
            "traits": list(definition.get("traits", []) or []), "impact": impact,
            "impact_method": "cost * star * 2.0 (native board_power contribution)",
            "items": list(unit.get("items", []) or []),
        }

    @staticmethod
    def _item_state(audit: dict) -> dict:
        audit = audit or {}
        equipped = []
        for location in ("board", "bench"):
            for slot, unit in enumerate(audit.get(location, []) or []):
                if not isinstance(unit, dict) or not unit.get("occupied", True):
                    continue
                items = list(unit.get("items", unit.get("item_ids", [])) or [])
                if items:
                    equipped.append({
                        "location": location, "slot": int(unit.get("slot", slot)),
                        "champion_id": unit.get("champion_id") or unit.get("apiName") or "?",
                        "uuid": unit.get("uuid"), "items": items,
                    })
        return {
            "components": list(audit.get("item_components", []) or []),
            "inventory": list(audit.get("item_inventory", []) or []),
            "equipped": equipped,
        }

    def _player_snapshot(self, audit: dict, public: dict) -> dict:
        audit, public = audit or {}, public or {}
        return {
            "player_id": int(public.get("player_id", audit.get("player_id", -1))),
            "hp": public.get("hp"), "gold": public.get("gold", audit.get("gold")),
            "level": public.get("level", audit.get("level")), "xp": public.get("xp", audit.get("xp")),
            "alive": public.get("alive"), "eliminated": public.get("eliminated"),
            "wins": public.get("wins"), "losses": public.get("losses"),
            "placement": public.get("placement"), "opponent_id": public.get("opponent_id"),
            "win_streak": audit.get("win_streak"), "loss_streak": audit.get("loss_streak"),
            "gold_before_interest": audit.get("gold_before_interest"),
            "interest_if_resolved_now": audit.get("interest_if_resolved_now"),
            "board_power": audit.get("board_power"),
            "synergy_score": audit.get("synergy_score"),
            "positioning_score": audit.get("positioning_score"),
            "board_quality_score": public.get("board_quality_score"),
            "board_positional_score": public.get("board_positional_score"),
            "board_structural_score": public.get("board_structural_score"),
            "board_quality_delta": public.get("board_quality_delta"),
            "board_exposed_carries": public.get("board_exposed_carries"),
            "board_frontline_count": public.get("board_frontline_count"),
            "board_isolated_frontline_count": public.get("board_isolated_frontline_count"),
            "board_important_bench_units_unplayed": public.get("board_important_bench_units_unplayed"),
            "round_gold": audit.get("round_gold", 0),
            "round_base_gold": audit.get("round_base_gold", 0),
            "round_interest": audit.get("round_interest", 0),
            "round_streak_gold": audit.get("round_streak_gold", 0),
            "round_win_gold": audit.get("round_win_gold", 0),
            "round_total_income": (
                int(audit.get("round_gold", 0) or 0)
                + int(audit.get("round_win_gold", 0) or 0)
            ),
            "strategy_name": (audit.get("strategy_info") or {}).get("strategy_name", "ECON"),
            "strategy_id": (audit.get("strategy_info") or {}).get("strategy", 0),
            "comp_direction": (audit.get("strategy_info") or {}).get("composition_direction", ""),
            "comp_focus": (audit.get("strategy_info") or {}).get("composition_focus", ""),
            "composition_locked": bool((audit.get("strategy_info") or {}).get("composition_locked", False)),
            "composition_strength": float((audit.get("strategy_info") or {}).get("composition_strength", 0.0) or 0.0),
            "composition_candidate_direction": (audit.get("strategy_info") or {}).get("composition_candidate_direction", ""),
            "composition_candidate_strength": float((audit.get("strategy_info") or {}).get("composition_candidate_strength", 0.0) or 0.0),
            "composition_candidate_streak": int((audit.get("strategy_info") or {}).get("composition_candidate_streak", 0) or 0),
            "previous_composition_direction": (audit.get("strategy_info") or {}).get("previous_composition_direction", ""),
            "previous_composition_strength": float((audit.get("strategy_info") or {}).get("previous_composition_strength", 0.0) or 0.0),
            "composition_direction_change_was_locked": bool((audit.get("strategy_info") or {}).get("composition_direction_change_was_locked", False)),
            "composition_direction_change_round": int((audit.get("strategy_info") or {}).get("composition_direction_change_round", 0) or 0),
            "composition_direction_change_focus_weight": float((audit.get("strategy_info") or {}).get("composition_direction_change_focus_weight", 0.0) or 0.0),
            "composition_direction_change_reason": (audit.get("strategy_info") or {}).get("composition_direction_change_reason", ""),
            "composition_direction_change_count": int((audit.get("strategy_info") or {}).get("composition_direction_change_count", 0) or 0),
            "composition_focus_weights": dict((audit.get("strategy_info") or {}).get("composition_focus_weights", {}) or {}),
            "strategy_confidence": (audit.get("strategy_info") or {}).get("confidence", 0.0),
            "strategy_reason": (audit.get("strategy_info") or {}).get("reason", ""),
            "core_units": list((audit.get("strategy_info") or {}).get("core_units", []) or []),
            "core_traits": list((audit.get("strategy_info") or {}).get("core_traits", []) or []),
            # Planner output is kept separate from current board/bench state:
            # planned_units are targets, not units the policy already owns.
            "planned_units": list((audit.get("strategy_info") or {}).get("planned_units", []) or []),
            "planned_unit_ids": list((audit.get("strategy_info") or {}).get("planned_unit_ids", []) or []),
            "planned_traits": list((audit.get("strategy_info") or {}).get("planned_traits", []) or []),
            "planned_main_carry_id": int(
                (audit.get("strategy_info") or {}).get("planned_main_carry_id", -1)
                if (audit.get("strategy_info") or {}).get("planned_main_carry_id") is not None else -1
            ),
            "planned_composition_score": float((audit.get("strategy_info") or {}).get("planned_composition_score", 0.0) or 0.0),
            "planned_acquisition_notes": list((audit.get("strategy_info") or {}).get("planned_acquisition_notes", []) or []),
            "planner_target_slots": (
                8 if int(public.get("level", audit.get("level", 1)) or 1) <= 8
                else min(10, int(public.get("level", audit.get("level", 1)) or 1))
            ),
            "planner_mode": (
                "WAITING_FOR_DIRECTION" if not ((audit.get("strategy_info") or {}).get("planned_units", []) or [])
                else "LEVEL_8_CORE" if int(public.get("level", audit.get("level", 1)) or 1) <= 8
                else f"DYNAMIC_LEVEL_{min(10, int(public.get('level', audit.get('level', 1)) or 1))}"
            ),
            "active_traits": dict((audit.get("strategy_info") or {}).get("active_traits", {}) or {}),
            "strategy_scores": dict((audit.get("strategy_info") or {}).get("strategy_scores", {}) or {}),
            "board": [self._unit_info(u, i, "board") for i, u in enumerate(audit.get("board", []))],
            "bench": [self._unit_info(u, i, "bench") for i, u in enumerate(audit.get("bench", []))],
            "shop": [self._unit_info(u, i, "shop") for i, u in enumerate(audit.get("shop", []))],
            "item_components": list(audit.get("item_components", []) or []),
            "item_inventory": list(audit.get("item_inventory", []) or []),
        }


    @staticmethod
    def _board_power_state(state: dict) -> float:
        return round(sum(float(unit.get("impact", 0.0) or 0.0)
                         for unit in state.get("board", [])
                         if isinstance(unit, dict) and unit.get("occupied", True)), 4)

    @staticmethod
    def _board_trait_counts(state: dict) -> dict:
        counts = {}
        for unit in state.get("board", []) or []:
            if not isinstance(unit, dict) or not unit.get("occupied", True):
                continue
            for trait in unit.get("traits", []) or []:
                if isinstance(trait, str) and trait and trait.casefold() != "none":
                    counts[trait] = counts.get(trait, 0) + 1
        return counts

    @staticmethod
    def _upgrade_counts(state: dict) -> dict:
        units = [
            unit for location in ("board", "bench")
            for unit in (state.get(location) or [])
            if isinstance(unit, dict) and unit.get("occupied", True)
        ]
        return {
            "two_star_or_higher": sum(int(unit.get("star", 1) or 1) >= 2 for unit in units),
            "three_star": sum(int(unit.get("star", 1) or 1) >= 3 for unit in units),
        }

    @staticmethod
    def _pair_count_state(state: dict) -> int:
        counts = {}
        for location in ("board", "bench"):
            for unit in state.get(location, []) or []:
                if not isinstance(unit, dict) or not unit.get("occupied", True):
                    continue
                if int(unit.get("star", 1) or 1) != 1:
                    continue
                key = str(unit.get("champion_id") or unit.get("name") or "").casefold()
                if key:
                    counts[key] = counts.get(key, 0) + 1
        return sum(count >= 2 for count in counts.values())

    @classmethod
    def _strategic_snapshot(cls, state: dict) -> dict:
        """Keep current combat strength separate from reserve/upgrade potential."""
        board = [u for u in (state.get("board") or [])
                 if isinstance(u, dict) and u.get("occupied", True)]
        bench = [u for u in (state.get("bench") or [])
                 if isinstance(u, dict) and u.get("occupied", True)]
        def pairs(units):
            counts = {}
            for unit in units:
                if int(unit.get("star", 1) or 1) != 1:
                    continue
                name = str(unit.get("champion_id") or unit.get("name") or "").casefold()
                if name:
                    counts[name] = counts.get(name, 0) + 1
            return {name: count // 2 for name, count in counts.items() if count >= 2}
        board_pairs, bench_pairs = pairs(board), pairs(bench)
        combined_pairs = pairs(board + bench)
        trait_counts = cls._board_trait_counts(state)
        synergy_levels = {trait: _synergy_level(count) for trait, count in trait_counts.items()}
        core = {str(x).casefold() for x in (state.get("core_units") or [])}
        focus_weights = {str(k).casefold(): float(v or 0.0)
                         for k, v in (state.get("composition_focus_weights") or {}).items()}
        def compatible_count(units):
            total = 0
            for unit in units:
                ids = {str(unit.get("champion_id") or "").casefold(),
                       str(unit.get("name") or "").casefold()}
                traits = [str(t).casefold() for t in (unit.get("traits") or [])]
                if ids & core or any(focus_weights.get(t, 0.0) > 0 for t in traits):
                    total += 1
            return total
        compatible_board = compatible_count(board)
        compatible_bench = compatible_count(bench)
        return {
            "board_strength": (
                float(state["board_power"]) if state.get("board_power") is not None
                else cls._board_power_state(state)
            ),
            "bench_potential_strength": round(sum(float(u.get("impact", 0.0) or 0.0) for u in bench), 4),
            "board_unit_count": len(board),
            "bench_unit_count": len(bench),
            "board_occupancy": len(board) / max(1, len(state.get("board") or [])),
            "board_two_star_or_higher": sum(int(u.get("star", 1) or 1) >= 2 for u in board),
            "board_three_star": sum(int(u.get("star", 1) or 1) >= 3 for u in board),
            "bench_two_star_or_higher": sum(int(u.get("star", 1) or 1) >= 2 for u in bench),
            "bench_three_star": sum(int(u.get("star", 1) or 1) >= 3 for u in bench),
            "board_pairs": board_pairs,
            "bench_pairs": bench_pairs,
            "combined_pairs": combined_pairs,
            "board_pair_count": sum(board_pairs.values()),
            "bench_pair_count": sum(bench_pairs.values()),
            "combined_pair_count": sum(combined_pairs.values()),
            "active_synergies": synergy_levels,
            "active_trait_counts": trait_counts,
            "composition_compatible_board_units": compatible_board,
            "composition_compatible_bench_units": compatible_bench,
            "composition_compatible_total_units": compatible_board + compatible_bench,
            "composition_direction": state.get("comp_direction"),
            "composition_focus": state.get("comp_focus"),
            "composition_strength": float(state.get("composition_strength", 0.0) or 0.0),
            "gold": int(state.get("gold", 0) or 0),
            "level": int(state.get("level", 0) or 0),
            "xp": int(state.get("xp", 0) or 0),
            "positioning_quality": float(state.get("positioning_score", 0.0) or 0.0),
            "board_quality": state.get("board_quality_score"),
            "board_structural_score": state.get("board_structural_score"),
            "hp": state.get("hp"),
            "placement": state.get("placement"),
        }

    def _economic_diagnostics(self, action, before_state, after_state,
                              before_audit, after_audit) -> dict:
        action_type = int(action[0])
        gold_before = int(before_state.get("gold", 0) or 0)
        gold_after = int(after_state.get("gold", 0) or 0)
        shop_slot = int(action[1]) if action_type == 0 and len(action) > 1 else -1
        shop = before_state.get("shop") or []
        purchased = shop[shop_slot] if 0 <= shop_slot < len(shop) else {}
        sell_slot = int(action[2]) if action_type == 5 and len(action) > 2 else -1
        bench = before_state.get("bench") or []
        sold = bench[sell_slot] if 0 <= sell_slot < len(bench) else {}
        explicit_cost = int(purchased.get("cost", 0) or 0) if action_type == 0 else (
            2 if action_type == 1 else 4 if action_type == 2 else 0)
        gold_delta = gold_after - gold_before
        before_power = (
            float(before_state["board_power"])
            if before_state.get("board_power") is not None
            else self._board_power_state(before_state)
        )
        after_power = (
            float(after_state["board_power"])
            if after_state.get("board_power") is not None
            else self._board_power_state(after_state)
        )
        before_upgrades = self._upgrade_counts(before_state)
        after_upgrades = self._upgrade_counts(after_state)
        board_traits_before = self._board_trait_counts(before_state)
        board_traits_after = self._board_trait_counts(after_state)
        synergy_milestones = {}
        for trait in sorted(set(board_traits_before) | set(board_traits_after)):
            old_count, new_count = board_traits_before.get(trait, 0), board_traits_after.get(trait, 0)
            old_level, new_level = _synergy_level(old_count), _synergy_level(new_count)
            if old_level != new_level:
                synergy_milestones[trait] = {
                    "count_before": old_count, "count_after": new_count,
                    "level_before": old_level, "level_after": new_level,
                }
        diagnostics = {
            "gold_before": gold_before,
            "gold_after": gold_after,
            "gold_delta": gold_delta,
            "action_cost": max(0, -gold_delta),
            "listed_cost": explicit_cost,
            "sale_proceeds": max(0, gold_delta) if action_type == 5 else 0,
            "gold_before_interest": after_state.get("gold_before_interest"),
            "interest_if_resolved_before": before_state.get("interest_if_resolved_now"),
            "interest_if_resolved_after": after_state.get("interest_if_resolved_now"),
            "potential_interest_delta": int(after_state.get("interest_if_resolved_now") or 0) - int(before_state.get("interest_if_resolved_now") or 0),
            "level_before": int(before_state.get("level", 0) or 0),
            "level_after": int(after_state.get("level", 0) or 0),
            "xp_before": int(before_state.get("xp", 0) or 0),
            "xp_after": int(after_state.get("xp", 0) or 0),
            "base_income": int(after_state.get("round_base_gold", 0) or 0),
            "interest_income": int(after_state.get("round_interest", 0) or 0),
            "streak_income": int(after_state.get("round_streak_gold", 0) or 0),
            "win_income": int(after_state.get("round_win_gold", 0) or 0),
            "board_power_before": before_power,
            "board_power_after": after_power,
            "estimated_board_power_before": self._board_power_state(before_state),
            "estimated_board_power_after": self._board_power_state(after_state),
            "engine_synergy_before": before_state.get("synergy_score"),
            "engine_synergy_after": after_state.get("synergy_score"),
            "positioning_before": before_state.get("positioning_score"),
            "positioning_after": after_state.get("positioning_score"),
            "positioning_delta": float(after_state.get("positioning_score") or 0.0) - float(before_state.get("positioning_score") or 0.0),
            "board_power_delta": round(after_power - before_power, 4),
            "pairs_before": self._pair_count_state(before_state),
            "pairs_after": self._pair_count_state(after_state),
            "two_star_or_higher_before": before_upgrades["two_star_or_higher"],
            "two_star_or_higher_after": after_upgrades["two_star_or_higher"],
            "three_star_before": before_upgrades["three_star"],
            "three_star_after": after_upgrades["three_star"],
            "board_traits_before": board_traits_before,
            "board_traits_after": board_traits_after,
            "synergy_milestones_changed": synergy_milestones,
            "purchased_champion": purchased.get("champion_id") if action_type == 0 else None,
            "sold_champion": sold.get("champion_id") if action_type == 5 else None,
            "sold_core_unit": bool(
                action_type == 5 and str(sold.get("champion_id") or "").casefold()
                in {str(value).casefold() for value in (before_state.get("core_units") or [])}
            ),
            "pair_progress": self._pair_count_state(after_state) - self._pair_count_state(before_state),
            "space_freed": bool(
                action_type == 5 and sold.get("occupied", False)
                and 0 <= sell_slot < len(bench)
                and not (after_state.get("bench") or [])[sell_slot].get("occupied", False)
            ),
            "composition_direction_before": before_state.get("comp_direction"),
            "composition_direction_after": after_state.get("comp_direction"),
            "composition_fit": (
                self._unit_composition_fit(action, before_audit, before_state)
                if action_type in (0, 3, 4, 5) else None
            ),
        }
        # Motivos explicativos; não são recompensas nem alteram a policy.
        board_gain = float(diagnostics["board_power_delta"]) > 1e-6
        level_up = diagnostics["level_after"] > diagnostics["level_before"]
        upgrade_gain = diagnostics["two_star_or_higher_after"] > diagnostics["two_star_or_higher_before"]
        synergy_gain = bool(synergy_milestones)
        pair_progress = diagnostics["pair_progress"] > 0
        fit = diagnostics.get("composition_fit") or {}
        comp_fit_gain = bool(fit.get("core_unit_match")) or float(fit.get("focus_fit_score", 0.0) or 0.0) > 0.0
        if action_type == 0:
            reason = "PURCHASE_UPGRADE" if upgrade_gain else (
                "PURCHASE_PAIR_PROGRESS" if pair_progress else (
                    "PURCHASE_SYNERGY_GAIN" if synergy_gain else (
                        "PURCHASE_COMPATIBLE" if comp_fit_gain else (
                            "PURCHASE_BOARD_GAIN" if board_gain else "PURCHASE_NO_IMMEDIATE_GAIN"
                        )
                    )
                )
            )
        elif action_type == 1:
            reason = "REROLL_IMMEDIATE_GAIN" if (board_gain or upgrade_gain or synergy_gain) else "REROLL_NO_IMMEDIATE_BOARD_GAIN"
        elif action_type == 2:
            reason = "XP_LEVEL_UP" if level_up else "XP_NO_LEVEL_UP"
        elif action_type == 3:
            reason = "DEPLOY_BOARD_GAIN" if board_gain else "DEPLOY_NO_POWER_GAIN"
        elif action_type == 4:
            reason = "REPOSITION_IMPROVED" if float(diagnostics["positioning_delta"]) > 1e-6 else "REPOSITION_NO_SCORE_GAIN"
        elif action_type == 5:
            reason = "SALE_CORE_OR_PAIR_RISK" if (
                diagnostics["sold_core_unit"] or diagnostics["pairs_after"] < diagnostics["pairs_before"]
            ) else ("SALE_SPACE_FREED" if diagnostics["space_freed"] else "SALE_GOLD_RECOVERY")
        else:
            reason = "PASS_NO_SPEND"
        diagnostics["reason_code"] = reason
        strategic_before = self._strategic_snapshot(before_state)
        strategic_after = self._strategic_snapshot(after_state)
        diagnostics["strategic_snapshot_before"] = strategic_before
        diagnostics["strategic_snapshot_after"] = strategic_after
        if action_type == 0:
            board_gain = strategic_after["board_strength"] - strategic_before["board_strength"] > 1e-6
            bench_gain = strategic_after["bench_potential_strength"] - strategic_before["bench_potential_strength"] > 1e-6
            pair_gain = strategic_after["combined_pair_count"] > strategic_before["combined_pair_count"]
            star_gain = (
                strategic_after["board_two_star_or_higher"] + strategic_after["bench_two_star_or_higher"]
                > strategic_before["board_two_star_or_higher"] + strategic_before["bench_two_star_or_higher"]
            )
            synergy_changes = {
                trait: {"before": strategic_before["active_synergies"].get(trait, 0),
                        "after": strategic_after["active_synergies"].get(trait, 0)}
                for trait in set(strategic_before["active_synergies"]) | set(strategic_after["active_synergies"])
                if strategic_before["active_synergies"].get(trait, 0) != strategic_after["active_synergies"].get(trait, 0)
            }
            synergy_gain = any(item["after"] > item["before"] for item in synergy_changes.values())
            comp_gain = strategic_after["composition_compatible_total_units"] > strategic_before["composition_compatible_total_units"]
            if star_gain:
                marginal_class = "IMMEDIATE_UPGRADE"
            elif pair_gain:
                marginal_class = "PAIR_POTENTIAL"
            elif synergy_gain:
                marginal_class = "SYNERGY_MILESTONE"
            elif board_gain:
                marginal_class = "BOARD_STRENGTH_GAIN"
            elif comp_gain:
                marginal_class = "COMPOSITION_COMPATIBILITY"
            elif bench_gain:
                marginal_class = "BENCH_POTENTIAL_ONLY"
            else:
                marginal_class = "NO_IDENTIFIED_STRATEGIC_GAIN"
            diagnostics["purchase_marginal_value"] = {
                "classification": marginal_class,
                "board_strength_delta": round(strategic_after["board_strength"] - strategic_before["board_strength"], 4),
                "bench_potential_delta": round(strategic_after["bench_potential_strength"] - strategic_before["bench_potential_strength"], 4),
                "combined_pair_delta": strategic_after["combined_pair_count"] - strategic_before["combined_pair_count"],
                "board_upgrade_delta": (
                    strategic_after["board_two_star_or_higher"] - strategic_before["board_two_star_or_higher"]
                ),
                "synergy_changes": synergy_changes,
                "composition_compatible_board_delta": (
                    strategic_after["composition_compatible_board_units"] - strategic_before["composition_compatible_board_units"]
                ),
                "composition_compatible_bench_delta": (
                    strategic_after["composition_compatible_bench_units"] - strategic_before["composition_compatible_bench_units"]
                ),
            }
        diagnostics["measurable_improvement"] = bool(
            board_gain or upgrade_gain or synergy_gain or pair_progress or comp_fit_gain or level_up or
            float(diagnostics["positioning_delta"]) > 1e-6
        )
        return diagnostics

    def _unit_composition_fit(self, action, before_audit, after_state):
        """Estimate how the acted-on unit aligns with the current comp focus/core."""
        action_type = int(action[0])
        slot = location = None
        if action_type == 0:
            slot, location = int(action[1]), "shop"
        elif action_type == 3:
            slot, location = int(action[2]), "bench"
        elif action_type == 4:
            slot, location = int(action[4]), "board"
        elif action_type == 5:
            slot, location = int(action[2]), "bench"
        if location is None:
            return None
        raw = self._unit_at((before_audit or {}).get(location, []), slot)
        if not raw or not raw.get("occupied", True):
            return None
        unit = self._unit_info(raw, slot, location)
        traits = [str(trait) for trait in unit.get("traits", []) if trait]
        weights = {
            str(key).casefold(): float(value or 0.0)
            for key, value in (after_state.get("composition_focus_weights") or {}).items()
        }
        weighted_traits = [
            {"trait": trait, "weight": weights.get(trait.casefold(), 0.0)}
            for trait in traits
        ]
        core_units = {str(value).casefold() for value in (after_state.get("core_units") or [])}
        identities = {
            str(unit.get("champion_id") or "").casefold(),
            str(unit.get("name") or "").casefold(),
        }
        return {
            "unit": unit.get("name"),
            "champion_id": unit.get("champion_id"),
            "source": location,
            "slot": slot,
            "traits": traits,
            "core_unit_match": bool(identities & core_units),
            "focus_trait_matches": [item for item in weighted_traits if item["weight"] > 0],
            "focus_fit_score": round(sum(item["weight"] for item in weighted_traits), 4),
        }

    @staticmethod
    def _unit_composition_fit_text(unit_fit):
        if not unit_fit:
            return ""
        matches = ", ".join(
            f"{item['trait']}={item['weight']:.2f}"
            for item in unit_fit.get("focus_trait_matches", [])
        ) or "nenhum trait de foco"
        return (
            f"    FIT UNIDADE: {unit_fit.get('unit') or unit_fit.get('champion_id')} | "
            f"core={'SIM' if unit_fit.get('core_unit_match') else 'não'} | "
            f"fit={float(unit_fit.get('focus_fit_score', 0.0) or 0.0):.2f} | {matches}\n"
        )

    def _compact_unit(self, unit: dict | None, slot: int = 0, location: str = "unknown") -> str:
        if not unit or not unit.get("occupied", True):
            return "Vazio"
        info = self._unit_info(unit, slot, location)
        return f"{info['name']} (i:{info['impact']:.1f})"

    @staticmethod
    def _unit_at(units, index):
        return units[int(index)] if 0 <= int(index) < len(units) else None

    def _action_text(self, action: list[int], before_audit: dict) -> str:
        action_type = int(action[0])
        shop, bench, board = (
            before_audit.get("shop", []), before_audit.get("bench", []), before_audit.get("board", [])
        )
        if action_type == 0:
            slot = int(action[1])
            unit = self._unit_at(shop, slot)
            if unit and unit.get("occupied", True):
                info = self._unit_info(unit, slot, "shop")
                return f"COMPROU: {info['name']} (Custo {info['cost']} | i:{info['impact']:.1f})"
            return "COMPROU Vazio"
        if action_type == 1:
            return "REROLL"
        if action_type == 2:
            return "BUY XP"
        if action_type == 3:
            source, target = int(action[2]), int(action[3])
            return (
                f"MOVE Bench -> Board: {self._compact_unit(self._unit_at(bench, source), source, 'bench')} "
                f"<-> {self._compact_unit(self._unit_at(board, target), target, 'board')}"
            )
        if action_type == 4:
            source, target = int(action[4]), int(action[5])
            return (
                f"MOVE Board -> Board: {self._compact_unit(self._unit_at(board, source), source, 'board')} "
                f"<-> {self._compact_unit(self._unit_at(board, target), target, 'board')}"
            )
        if action_type == 5:
            slot = int(action[2])
            unit = self._unit_at(bench, slot)
            if unit and unit.get("occupied", True):
                info = self._unit_info(unit, slot, "bench")
                return f"VENDEU: {info['name']} (i:{info['impact']:.1f})"
            return "VENDEU Vazio"
        if action_type == 7:
            return f"EQUIP_FROM_INVENTORY (ação={action})"
        if action_type == 8:
            return f"CRAFT_AND_EQUIP (ação={action})"
        return f"AÇÃO DESCONHECIDA (ação={action})" if action_type != 6 else "PASSOU TURNO"

    def _board_snapshot_keyed(self, audit: dict) -> dict[str, dict]:
        result = {}
        for index, unit in enumerate(audit.get("bench", [])):
            if unit and unit.get("occupied", True):
                result[f"bench_{index}"] = self._unit_info(unit, index, "bench")
        for index, unit in enumerate(audit.get("board", [])):
            if unit and unit.get("occupied", True):
                result[f"board_{index // 7}_{index % 7}"] = self._unit_info(unit, index, "board")
        return result

    def _active_traits(self, audit: dict) -> dict[str, int]:
        counts: dict[str, int] = {}
        for location in ("board", "bench"):
            for unit in audit.get(location, []):
                if not unit or not unit.get("occupied", True):
                    continue
                for trait in self._definition(unit).get("traits", []) or []:
                    if isinstance(trait, str) and trait and trait.casefold() != "none":
                        counts[trait] = counts.get(trait, 0) + 1
        return counts

    def _append_entry(
        self, player_id: int, *, timestamp: str, timestamp_iso: str, step: int,
        round_number: int, stage: int, round_in_stage: int, event_type: str,
        text: str, tag: str | None, data: dict | None = None,
    ):
        self._sequence[player_id] += 1
        event = {
            "schema_version": 1, "match_id": self.match_id, "player_id": player_id,
            "player_number": player_id + 1, "sequence_id": self._sequence[player_id],
            "timestamp": timestamp, "timestamp_iso": timestamp_iso, "step": int(step),
            "round": int(round_number), "stage": int(stage), "round_in_stage": int(round_in_stage),
            "event_type": event_type, "tag": tag, "text": text, "payload": _jsonable(data or {}),
        }
        document = self.documents[player_id]
        document["entries"].append(event)
        document["updated_at"] = timestamp_iso
        self._dirty.add(player_id)

    def _append_shop(self, player_id: int, *, timestamp: str, timestamp_iso: str,
                     step: int, round_number: int, stage: int, round_in_stage: int, audit: dict):
        names = []
        for slot, unit in enumerate(audit.get("shop", [])):
            if unit and unit.get("occupied", True):
                info = self._unit_info(unit, slot, "shop")
                names.append(f"{info['name']}(i:{info['impact']:.1f})")
            else:
                names.append("None")
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="shop_view", text=f"[{timestamp}] 🛒 LOJA: {', '.join(names)}\n",
            tag="shop_view",
            data={"shop": [self._unit_info(u, i, "shop") for i, u in enumerate(audit.get("shop", []))]},
        )

    def _record_round_end(
        self, player_id: int, *, timestamp: str, timestamp_iso: str, step: int,
        round_number: int, stage: int, round_in_stage: int, audit: dict,
        public: dict, action: list[int], reward: float, before_state: dict,
        after_state: dict, diagnostics: dict, engine_events: list[str],
        economic_diagnostics: dict, combat_reward: float,
    ):
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="round_finished",
            text=(
                f"\n[{timestamp}] --- FIM DO ROUND {stage}-{round_in_stage} | GOLD: {after_state.get('gold', '?')} ---\n"
                f"    STRATEGY: {after_state.get('strategy_name', 'ECON')} | "
                f"COMP DIRECTION: {after_state.get('comp_direction') or '—'} | "
                f"FOCUS: {after_state.get('comp_focus') or '—'} | "
                f"LOCK: {'LOCKED' if after_state.get('composition_locked') else 'OPEN'} | "
                f"STRENGTH: {float(after_state.get('composition_strength', 0.0) or 0.0):.2f}\n"
                f"FOCUS WEIGHTS: {', '.join(f'{name} {float(weight):.2f}' for name, weight in sorted((after_state.get('composition_focus_weights') or {}).items(), key=lambda item: float(item[1]), reverse=True)[:5]) or '—'}\n"
                f"    RENDA PRÓXIMO ROUND: +{after_state.get('round_base_gold', 0)} base, "
                f"+{after_state.get('round_interest', 0)} juros, "
                f"+{after_state.get('round_streak_gold', 0)} sequência, "
                f"+{after_state.get('round_win_gold', 0)} vitória "
                f"(total: +{after_state.get('round_total_income', after_state.get('round_gold', 0))})\n"
            ),
            tag="round_msg",
            data={
                "action": action, "action_name": ACTION_NAMES.get(int(action[0]), "UNKNOWN"),
                "reward": reward, "state_before": before_state, "state_after": after_state,
                "economic_diagnostics": economic_diagnostics,
                "combat_reward": combat_reward,
                "strategic_snapshot_before": self._strategic_snapshot(before_state),
                "strategic_snapshot_after": self._strategic_snapshot(after_state),
                "purchase_marginal_value": economic_diagnostics.get("purchase_marginal_value"),
                "policy_diagnostics": diagnostics, "engine_events": engine_events,
            },
        )
        board = list(audit.get("board", []))
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="board_header", text="\n--- CONFIGURAÇÃO DO TABULEIRO ---\n",
            tag="board_view", data={"board": after_state["board"]},
        )
        frontline = backline = carries_front = tanks_back = assassins_front = 0
        rows = []
        for row in range(4):
            row_text = ""
            for col in range(7):
                index = row * 7 + col
                unit = board[index] if index < len(board) else None
                if unit and unit.get("occupied", True):
                    info = self._unit_info(unit, index, "board")
                    role = info.get("role")
                    char = f"[{str(info.get('name') or '?')[:3]}|{info.get('role_abbreviation', '?')}|{info['star']}*|i:{info['impact']:.1f}]"
                    if row <= 1:
                        frontline += 1
                    else:
                        backline += 1
                    if role == 1 and row <= 1:
                        carries_front += 1
                    if role == 0 and row >= 2:
                        tanks_back += 1
                    if role == 4 and row <= 1:
                        assassins_front += 1
                else:
                    char = "[ . ]"
                row_text += char.center(18)
            rows.append(row_text + "\n")
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="board_view", text="".join(rows), tag="board_view",
            data={"rows": [row.rstrip("\n") for row in rows]},
        )
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="board_separator", text="----------------------------------\n", tag="board_view",
        )
        analysis = []
        if carries_front > 0:
            analysis.append(f"⚠️ {carries_front} carry(s) expostos na frontline")
        if tanks_back > 0:
            analysis.append(f"⚠️ {tanks_back} tank(s) posicionados atrás")
        if assassins_front > 0:
            analysis.append(f"⚠️ {assassins_front} assassin(s) na frontline")
        if frontline == 0:
            analysis.append("⚠️ sem frontline")
        if backline == 0:
            analysis.append("⚠️ sem backline")
        if not analysis:
            analysis.append("✅ posicionamento parece consistente")
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="position_analysis", text="\n".join(analysis) + "\n", tag="system",
            data={"frontline": frontline, "backline": backline, "carries_frontline": carries_front,
                  "tanks_backline": tanks_back, "assassins_frontline": assassins_front, "warnings": analysis},
        )
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="bench_header", text="\n--- ESTADO DO BANCO ---\n", tag="board_view",
            data={"bench": after_state["bench"]},
        )
        bench = list(audit.get("bench", []))
        bench_rows = []
        for start in range(0, 9, 3):
            chars = []
            for index in range(start, min(start + 3, 9)):
                unit = bench[index] if index < len(bench) else None
                if unit and unit.get("occupied", True):
                    info = self._unit_info(unit, index, "bench")
                    char = f"[{str(info.get('name') or '?')[:3]}|{info['star']}*|i:{info['impact']:.1f}]"
                else:
                    char = "[VAZIO]"
                chars.append(char.center(14))
            bench_rows.append("".join(chars) + "\n")
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="bench_view", text="".join(bench_rows) + "----------------------------------\n",
            tag="board_view", data={"rows": [row.rstrip("\n") for row in bench_rows]},
        )
        # Item state is explicit in the text log so equipped items cannot be
        # mistaken for missing actions when inspecting a .tft file.
        item_lines = ["--- ITENS ---"]
        components = list(after_state.get("item_components") or [])
        inventory = list(after_state.get("item_inventory") or [])
        item_lines.append("  Componentes: " + (", ".join(map(str, components)) if components else "nenhum"))
        item_lines.append("  Itens na bag: " + (", ".join(map(str, inventory)) if inventory else "nenhum"))
        equipped_lines = []
        for location in ("board", "bench"):
            for unit in after_state.get(location, []) or []:
                if not isinstance(unit, dict) or not unit.get("occupied", True):
                    continue
                equipped = list(unit.get("items") or [])
                if equipped:
                    equipped_lines.append(
                        f"  {location.upper()} slot {unit.get('slot', '?')} · "
                        f"{unit.get('name') or unit.get('champion_id') or '?'}: "
                        + ", ".join(map(str, equipped))
                    )
        item_lines.extend(equipped_lines or ["  Itens equipados: nenhum"])
        self._append_entry(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage,
            event_type="item_state", text="\n".join(item_lines) + "\n",
            tag="item_state",
            data={"components": components, "inventory": inventory, "equipped": equipped_lines},
        )
        self._append_shop(
            player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
            round_number=round_number, stage=stage, round_in_stage=round_in_stage, audit=audit,
        )

    @staticmethod
    def _events_for_player(events: list[str], player_id: int) -> list[str]:
        patterns = (
            re.compile(rf"\bjogador\s+{player_id}\b", re.IGNORECASE),
            re.compile(rf"\bplayer\s+{player_id}\b", re.IGNORECASE),
        )
        relevant = []
        for event in events:
            event = str(event)
            mentions_seat = re.search(r"\b(?:jogador|player)\s+\d+\b", event, re.IGNORECASE)
            if not mentions_seat or any(pattern.search(event) for pattern in patterns):
                relevant.append(event)
        return relevant

    def record_step(self, *, before: dict, after: dict, actions: list[list[int]],
                    diagnostics: list[dict], rewards, info: dict, step: int, finished: bool):
        """Append per-seat action lines and matching board/bench/shop snapshots."""
        if self._closed:
            return
        timestamp, timestamp_iso = self._timestamp()
        round_number = int(before.get("round", 1) or 1)
        stage, round_in_stage = _round_coordinates(round_number)
        engine_events = [str(event) for event in info.get("events", [])]
        # Native costs are captured inside PlayerEnv::step, before round income.
        # Prefer this trace over net gold delta, which can be masked by round income.
        native_economic_events = {}
        for event in engine_events:
            match = re.search(
                r"ECONOMIC_ACTION player(?:=|\s+)(\d+) action_cost=(\d+) sale_proceeds=(\d+) gold_before=(-?\d+) gold_after=(-?\d+) interest_before=(\d+) interest_after=(\d+) level_before=(\d+) level_after=(\d+) xp_before=(\d+) xp_after=(\d+)",
                event,
            )
            if match:
                native_economic_events[int(match.group(1))] = {
                    "action_cost": int(match.group(2)),
                    "sale_proceeds": int(match.group(3)),
                    "gold_before": int(match.group(4)),
                    "gold_after": int(match.group(5)),
                    "interest_if_resolved_before": int(match.group(6)),
                    "interest_if_resolved_after": int(match.group(7)),
                    "level_before": int(match.group(8)),
                    "level_after": int(match.group(9)),
                    "xp_before": int(match.group(10)),
                    "xp_after": int(match.group(11)),
                }
        round_resolved = any(
            event.strip() == "ROUND_RESOLVED" or event.strip().startswith("ROUND_RESOLVED:")
            for event in engine_events
        )
        shared_round_events = [
            event for event in engine_events
            if event.strip() == "ROUND_RESOLVED" or event.strip().startswith("ROUND_NO_PVP")
            or event.strip().startswith("PLACEMENT_REWARD")
        ]
        action_rewards = _jsonable(info.get("action_rewards"))
        combat_rewards = _jsonable(info.get("combat_rewards"))
        placement_rewards = _jsonable(info.get("placement_rewards"))
        if round_resolved:
            self._pass_logged = [False] * 8

        for player_id in range(8):
            before_audit = _player_by_id(before.get("audit_players", []), player_id)
            after_audit = _player_by_id(after.get("audit_players", []), player_id)
            before_public = _player_by_id(before.get("players", []), player_id)
            after_public = _player_by_id(after.get("players", []), player_id)
            action = [int(value) for value in actions[player_id]]
            diagnostic = diagnostics[player_id] if player_id < len(diagnostics) else {}
            try:
                reward = float(rewards[player_id])
            except (TypeError, ValueError, IndexError):
                reward = 0.0
            player_events = self._events_for_player(engine_events, player_id)
            action_type = int(action[0])
            # PASS ends this player's decisions, not the shared round.
            # The engine's ROUND_RESOLVED event is the sole round boundary.
            is_round_end = round_resolved or finished
            before_state = self._player_snapshot(before_audit, before_public)
            after_state = self._player_snapshot(after_audit, after_public)
            item_before = self._item_state(before_audit)
            item_after = self._item_state(after_audit)
            item_audit = {
                "action_type": action_type,
                "action_name": ACTION_NAMES.get(action_type, "UNKNOWN"),
                "before": item_before,
                "after": item_after,
                "changed": item_before != item_after,
            }
            was_alive = before_state.get("alive") is True and not before_state.get("eliminated")
            is_eliminated = after_state.get("eliminated") is True or after_state.get("alive") is False
            if was_alive and is_eliminated:
                placement = after_state.get("placement")
                placement_text = (
                    f"colocação final #{placement}" if placement is not None
                    else "colocação final não informada pela engine"
                )
                self._append_entry(
                    player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                    round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                    event_type="player_eliminated",
                    text=f"[{timestamp}] ELIMINADO · {placement_text} · HP {after_state.get('hp', '?')}\\n",
                    tag="round_msg",
                    data={"placement": placement, "hp": after_state.get("hp"),
                          "alive_before": before_state.get("alive"), "alive_after": after_state.get("alive"),
                          "eliminated": after_state.get("eliminated")},
                )
            economic_diagnostics = self._economic_diagnostics(
                action, before_state, after_state, before_audit, after_audit
            )
            if player_id in native_economic_events:
                step_gold_after = economic_diagnostics["gold_after"]
                economic_diagnostics.update(native_economic_events[player_id])
                economic_diagnostics["gold_after_step"] = step_gold_after
                economic_diagnostics["gold_delta"] = (
                    economic_diagnostics["gold_after"] - economic_diagnostics["gold_before"]
                )
                economic_diagnostics["potential_interest_delta"] = (
                    economic_diagnostics["interest_if_resolved_after"]
                    - economic_diagnostics["interest_if_resolved_before"]
                )
                economic_diagnostics["cost_source"] = "native_action_transition"
                if action_type == 2:
                    level_up = economic_diagnostics["level_after"] > economic_diagnostics["level_before"]
                    economic_diagnostics["reason_code"] = "XP_LEVEL_UP" if level_up else "XP_NO_LEVEL_UP"
                    economic_diagnostics["measurable_improvement"] = level_up
            else:
                economic_diagnostics["cost_source"] = "gold_delta_fallback"
            primary_data = {
                "action": action, "action_name": ACTION_NAMES.get(action_type, "UNKNOWN"),
                "reward": reward,
                "action_reward": action_rewards[player_id] if isinstance(action_rewards, list) and player_id < len(action_rewards) else None,
                "combat_reward": combat_rewards[player_id] if isinstance(combat_rewards, list) and player_id < len(combat_rewards) else None,
                "placement_reward": placement_rewards[player_id] if isinstance(placement_rewards, list) and player_id < len(placement_rewards) else None,
                "reward_components": {
                    "action": action_rewards[player_id] if isinstance(action_rewards, list) and player_id < len(action_rewards) else None,
                    "combat": combat_rewards[player_id] if isinstance(combat_rewards, list) and player_id < len(combat_rewards) else None,
                    "placement": placement_rewards[player_id] if isinstance(placement_rewards, list) and player_id < len(placement_rewards) else None,
                    "returned_reward": reward,
                },
                "state_changed": before_state != after_state,
                "item_audit": item_audit,
                "economic_diagnostics": economic_diagnostics,
                "state_before": before_state, "state_after": after_state,
                "composition_diagnostics": {
                    "before": {
                        "direction": before_state.get("comp_direction"),
                        "focus": before_state.get("comp_focus"),
                        "locked": before_state.get("composition_locked", False),
                        "strength": before_state.get("composition_strength", 0.0),
                    },
                    "after": {
                        "direction": after_state.get("comp_direction"),
                        "focus": after_state.get("comp_focus"),
                        "locked": after_state.get("composition_locked", False),
                        "strength": after_state.get("composition_strength", 0.0),
                        "reason": after_state.get("strategy_reason"),
                        "core_units": after_state.get("core_units"),
                        "core_traits": after_state.get("core_traits"),
                        "active_traits": after_state.get("active_traits"),
                        "focus_weights": after_state.get("composition_focus_weights"),
                        "strategy_scores": after_state.get("strategy_scores"),
                    },
                    "direction_changed": before_state.get("comp_direction") != after_state.get("comp_direction"),
                    "direction_event": (
                        {
                            "round": after_state.get("composition_direction_change_round"),
                            "from": after_state.get("previous_composition_direction"),
                            "to": after_state.get("comp_direction"),
                            "from_strength": after_state.get("previous_composition_strength"),
                            "to_strength": after_state.get("composition_strength"),
                            "was_locked": after_state.get("composition_direction_change_was_locked"),
                            "focus_weight": after_state.get("composition_direction_change_focus_weight"),
                            "reason": after_state.get("composition_direction_change_reason"),
                            "change_count": after_state.get("composition_direction_change_count"),
                        }
                        if after_state.get("composition_direction_change_count", 0)
                        > before_state.get("composition_direction_change_count", 0)
                        else None
                    ),
                    "candidate_direction": after_state.get("composition_candidate_direction"),
                    "candidate_strength": after_state.get("composition_candidate_strength"),
                    "candidate_streak": after_state.get("composition_candidate_streak"),
                    "focus_changed": before_state.get("comp_focus") != after_state.get("comp_focus"),
                    "lock_changed": before_state.get("composition_locked") != after_state.get("composition_locked"),
                    "strength_changed": before_state.get("composition_strength") != after_state.get("composition_strength"),
                    "strategy_reason": after_state.get("strategy_reason"),
                    "opgg_meta_audit": [
                        str(note) for note in (after_state.get("planned_acquisition_notes") or [])
                        if str(note).startswith("OPGG_META_")
                    ],
                    "core_units": after_state.get("core_units"),
                    "core_traits": after_state.get("core_traits"),
                    "active_traits": after_state.get("active_traits"),
                    "focus_weights": after_state.get("composition_focus_weights"),
                    "strategy_scores": after_state.get("strategy_scores"),
                    "policy_status": diagnostic.get("status"),
                    "unit_fit": self._unit_composition_fit(action, before_audit, before_state),
                },
                "policy_diagnostics": diagnostic, "engine_events": player_events,
                "strategic_snapshot_before": self._strategic_snapshot(before_state),
                "strategic_snapshot_after": self._strategic_snapshot(after_state),
                "purchase_marginal_value": economic_diagnostics.get("purchase_marginal_value"),
            }

            # Same order as the old UI: star upgrades first, then action/round,
            # with synergy transitions recorded after the board/shop text.
            before_units = self._board_snapshot_keyed(before_audit)
            after_units = self._board_snapshot_keyed(after_audit)
            for location, previous in before_units.items():
                current = after_units.get(location)
                if current and current.get("champion_id") == previous.get("champion_id") and int(current.get("star", 1)) > int(previous.get("star", 1)):
                    self._append_entry(
                        player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                        round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                        event_type="evolution",
                        text=f"[{timestamp}] ⭐ EVOLUÇÃO: {current['name']} subiu para {current['star']} estrelas! (i:{current['impact']:.1f})\n",
                        tag="upgrade", data={"location": location, "before": previous, "after": current},
                    )

            if is_round_end:
                self._record_round_end(
                    player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                    round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                    audit=after_audit, public=after_public, action=action, reward=reward,
                    before_state=before_state, after_state=after_state,
                    diagnostics=diagnostic, engine_events=player_events + shared_round_events,
                    economic_diagnostics=economic_diagnostics,
                    combat_reward=float(combat_rewards[player_id] or 0.0)
                        if isinstance(combat_rewards, list) and player_id < len(combat_rewards) else 0.0,
                )
            elif action_type != 6 or not self._pass_logged[player_id]:
                tag = "pos_rew" if reward > 0 else "neg_rew" if reward < 0 else None
                line = (
                    f"[{timestamp}] {self._action_text(action, before_audit):28} | Rew: {reward:+.2f}\n"
                    f"    STRATEGY: {after_state.get('strategy_name', 'ECON')} | "
                    f"COMP DIRECTION: {after_state.get('comp_direction') or '—'} | "
                    f"FOCUS: {after_state.get('comp_focus') or '—'} | "
                f"LOCK: {'LOCKED' if after_state.get('composition_locked') else 'OPEN'} | "
                f"STRENGTH: {float(after_state.get('composition_strength', 0.0) or 0.0):.2f}\n"
                f"FOCUS WEIGHTS: {', '.join(f'{name} {float(weight):.2f}' for name, weight in sorted((after_state.get('composition_focus_weights') or {}).items(), key=lambda item: float(item[1]), reverse=True)[:5]) or '—'}\n"
                    f"    STRATEGY REASON: {after_state.get('strategy_reason') or '—'} | CONF: {float(after_state.get('strategy_confidence', 0.0) or 0.0):.2f}\n"
                    f"    CORE UNITS: {', '.join(map(str, after_state.get('core_units') or [])) or '—'} | CORE TRAITS: {', '.join(map(str, after_state.get('core_traits') or [])) or '—'}\n"
                    f"    COMPOSITION PLAN [{after_state.get('planner_mode', 'UNKNOWN')}]: target={after_state.get('planner_target_slots', 0)} | units={', '.join(map(str, after_state.get('planned_units') or [])) or '—'} | traits={', '.join(map(str, after_state.get('planned_traits') or [])) or '—'} | carry_id={after_state.get('planned_main_carry_id', -1)} | score={float(after_state.get('planned_composition_score', 0.0) or 0.0):.2f}\n"
                    f"    PLAN NOTE: {('level 1-8 targets the same 8-unit core; the planner is recalculated as direction/focus/owned copies change' if after_state.get('planner_mode') == 'LEVEL_8_CORE' else 'the 9th/10th slots are included in the latest recalculated plan using current direction/focus/owned copies' if str(after_state.get('planner_mode', '')).startswith('DYNAMIC_LEVEL_') else 'waiting for a valid composition direction')}\n"
                    f"    ACQUISITION CHECK: {', '.join(map(str, after_state.get('planned_acquisition_notes') or [])) or 'no missing-unit estimate available'}\n"
                    f"    OP.GG META AUDIT: {', '.join(str(note) for note in (after_state.get('planned_acquisition_notes') or []) if str(note).startswith('OPGG_META_')) or 'no catalog decision diagnostic exposed by engine'}\n"
                    f"    COMP BEFORE -> AFTER: dir={before_state.get('comp_direction') or '—'} -> {after_state.get('comp_direction') or '—'} | foco={before_state.get('comp_focus') or '—'} -> {after_state.get('comp_focus') or '—'} | lock={before_state.get('composition_locked', False)} -> {after_state.get('composition_locked', False)} | strength={float(before_state.get('composition_strength', 0.0) or 0.0):.2f} -> {float(after_state.get('composition_strength', 0.0) or 0.0):.2f}\n"
                    f"    GOLD: {after_state.get('gold', '?')} | renda base "
                    f"+{after_state.get('round_base_gold', 0)} | juros "
                    f"+{after_state.get('round_interest', 0)} | sequência "
                    f"+{after_state.get('round_streak_gold', 0)} | vitória "
                    f"+{after_state.get('round_win_gold', 0)}\n"
                    + self._unit_composition_fit_text(primary_data["composition_diagnostics"]["unit_fit"])
                )
                if action_type in (7, 8) or item_audit["changed"]:
                    line += (
                        "    ITEM AUDIT: "
                        f"componentes {item_before['components']} -> {item_after['components']} | "
                        f"bag {item_before['inventory']} -> {item_after['inventory']} | "
                        f"equipados {item_before['equipped']} -> {item_after['equipped']}\\n"
                    )
                self._append_entry(
                    player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                    round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                    event_type="action", text=line, tag=tag, data=primary_data,
                )
                if action_type == 6:
                    self._pass_logged[player_id] = True
                if action_type == 1:
                    self._append_shop(
                        player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                        round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                        audit=after_audit,
                    )

            before_traits, after_traits = self._active_traits(before_audit), self._active_traits(after_audit)
            for trait in sorted(set(before_traits) | set(after_traits)):
                old_level = _synergy_level(before_traits.get(trait, 0))
                new_level = _synergy_level(after_traits.get(trait, 0))
                if new_level > old_level:
                    event_type, arrow, tag = "synergy_up", "⬆️", "syn_up"
                elif new_level < old_level:
                    event_type, arrow, tag = "synergy_down", "⬇️", "syn_down"
                else:
                    continue
                self._append_entry(
                    player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                    round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                    event_type=event_type,
                    text=f"[{timestamp}]  {arrow} SINERGIA: {trait.upper()} nível {new_level}\n",
                    tag=tag,
                    data={"trait": trait, "old_count": before_traits.get(trait, 0),
                          "new_count": after_traits.get(trait, 0), "old_level": old_level, "new_level": new_level},
                )

            if finished:
                self._append_entry(
                    player_id, timestamp=timestamp, timestamp_iso=timestamp_iso, step=step,
                    round_number=round_number, stage=stage, round_in_stage=round_in_stage,
                    event_type="match_finished",
                    text=(
                        "\n" + "=" * 40 + "\n GAME OVER - RELATÓRIO FINAL\n" + "=" * 40 + "\n"
                        + self._final_result_text(player_id, after, after_state)
                    ),
                    tag="round_msg",
                    data={"ranking": after.get("ranking", []), "player_final_state": after_state,
                          "winner_id": after.get("winner_id")},
                )

        if round_resolved or finished or step % self.flush_interval_steps == 0:
            self.flush(force=True)


    @staticmethod
    def _final_result_text(player_id: int, snapshot: dict, player_state: dict) -> str:
        """Render the result fields supplied by the engine without guessing placements."""
        winner_id = snapshot.get("winner_id")
        try:
            is_winner = winner_id is not None and int(winner_id) == int(player_id)
        except (TypeError, ValueError):
            is_winner = False
        placement = player_state.get("placement")
        if is_winner:
            result = "RESULTADO: VITÓRIA (1º lugar)"
        elif placement is not None:
            result = f"COLOCAÇÃO FINAL: #{placement}"
        else:
            status = "ELIMINADO" if player_state.get("eliminated") or player_state.get("alive") is False else "não informado"
            result = f"RESULTADO: {status}; colocação não fornecida pela engine"
        wins = player_state.get("wins")
        losses = player_state.get("losses")
        winner_label = "não informado"
        if winner_id is not None:
            try:
                winner_label = f"JOGADOR {int(winner_id) + 1}"
            except (TypeError, ValueError):
                winner_label = str(winner_id)
        return (
            f"  VENCEDOR DA PARTIDA: {winner_label}\\n"
            f"  {result}\\n"
            f"  HP final: {player_state.get('hp', '?')} | Ouro final: {player_state.get('gold', '?')} | "
            f"Nível: {player_state.get('level', '?')}\n"
            f"  Vitórias: {wins if wins is not None else '?'} | Derrotas: {losses if losses is not None else '?'}\n"
        )

    def _render_legacy_log(self, player_id: int) -> str:
        """Render the in-memory timeline as the legacy observer's plain-text log."""
        document = self.documents[player_id]
        header = [
            "=" * 58,
            f"TFT AI LOG · {document['player_label'].upper()}",
            f"Partida: {self.match_id}",
            f"Seed: {self.seed} | Política: {'determinística' if self.deterministic else 'estocástica'}",
            f"Checkpoint SHA-256: {self.checkpoint_sha256}",
            f"Impacto (i): custo × estrelas × 2 (contribuição nativa da engine)",
            "=" * 58,
            "",
        ]
        chunks = ["\n".join(header)]
        for entry in document["entries"]:
            line = str(entry.get("text", ""))
            if not line:
                continue
            chunks.append(line)
            if not line.endswith("\n"):
                chunks.append("\n")
        return "".join(chunks).rstrip() + "\n"

    def flush(self, *, force: bool = False):
        if self._closed:
            return
        selected = range(8) if force else sorted(self._dirty)
        for player_id in selected:
            if player_id not in self._dirty and not force:
                continue
            path = self.paths[player_id]
            temporary = path.with_suffix(path.suffix + ".tmp")
            temporary.write_text(self._render_legacy_log(player_id), encoding="utf-8")
            temporary.replace(path)

            # Structured entries remain in memory for diagnostics; only the
            # legacy-compatible .tft timeline is persisted to disk.
            self._dirty.discard(player_id)

    def close(self):
        if self._closed:
            return
        self.flush(force=True)
        self._closed = True
