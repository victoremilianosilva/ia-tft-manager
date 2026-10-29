"""Audit the real PPO -> native C++ mask -> native C++ execution path.

Example:
  python scripts/audit_native_ppo_loops.py --checkpoint tft_checkpoint.pt \
      --seeds 20261022,20261023 --max-steps 300 --output reports/native_ppo_loop_audit.jsonl

Each JSONL row includes the selected action, exact native mask, before/after board,
bench, shop, gold, composition direction/focus/core, two-star count, composition
score, execution effect, and whether a movement returned to a previously seen state.
With --fail-on-loop, an executed movement that returns to a prior board+bench state
causes a non-zero exit after its evidence has been written.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cpp_lobby_env import CppTFTLobbyWrapper
from policy import TFTPolicy

ACTION_DIMS = [9, 5, 9, 28, 28, 28]
PASS = [6, 0, 0, 0, 0, 0]
MOVEMENT_TYPES = {3, 4}


def _mask_batch(masks, player_ids, device):
    keys = masks[player_ids[0]].keys()
    return {
        key: torch.as_tensor(
            np.stack([masks[player_id][key] for player_id in player_ids]),
            dtype=torch.bool,
            device=device,
        )
        for key in keys
    }


def _json_masks(masks):
    return {key: np.asarray(value, dtype=np.int8).tolist()
            for key, value in masks.items()}


def _action_dict(action):
    return {
        "type": int(action[0]),
        "shop_slot": int(action[1]),
        "bench_slot": int(action[2]),
        "board_target": int(action[3]),
        "board_source": int(action[4]),
        "conditioned_board_target": int(action[5]),
    }


def _mask_allows(action, masks):
    """Validate all action components against the same native mask given to PPO."""
    kind = int(action[0])
    if not (0 <= kind < len(masks["type_mask"])) or not bool(masks["type_mask"][kind]):
        return False
    if kind == 0:
        slot = int(action[1])
        return 0 <= slot < 5 and bool(masks["shop_mask"][slot])
    if kind == 3:
        source, target = int(action[2]), int(action[3])
        return (
            0 <= source < 9 and 0 <= target < 28
            and bool(masks["bench_move_source_mask"][source])
            and bool(masks["bench_to_board_target_masks"][source][target])
        )
    if kind == 4:
        source, target = int(action[4]), int(action[5])
        return (
            0 <= source < 28 and 0 <= target < 28
            and bool(masks["board_source_mask"][source])
            and bool(masks["board_move_target_masks"][source][target])
        )
    if kind == 5:
        source = int(action[2])
        return 0 <= source < 9 and bool(masks["bench_source_mask"][source])
    return True


def _legal_alternatives(action, masks, player):
    """Compact, human-readable legal alternatives from the exact PPO mask."""
    alternatives = []
    type_mask = np.asarray(masks.get("type_mask", []), dtype=bool).reshape(-1)
    labels = {0: "BUY", 1: "BUY_XP", 2: "REROLL", 3: "MOVE_BENCH_TO_BOARD",
              4: "MOVE_BOARD", 5: "SELL", 6: "PASS", 7: "ITEM_COMPONENT",
              8: "ITEM_EQUIP"}
    for kind, allowed in enumerate(type_mask):
        if not allowed:
            continue
        entry = {"type": int(kind), "label": labels.get(int(kind), f"TYPE_{kind}")}
        if kind == 0:
            shop_mask = np.asarray(masks.get("shop_mask", []), dtype=bool).reshape(-1)
            offers = player.get("shop", [])
            entry["slots"] = [
                {"slot": int(slot),
                 "champion_id": (offers[slot].get("champion_id") if slot < len(offers) and isinstance(offers[slot], dict) else None)}
                for slot, allowed_slot in enumerate(shop_mask) if allowed_slot
            ]
        alternatives.append(entry)
    return alternatives


def _economy_diagnostic(player, strategy, legal_alternatives, round_index, selected_action):
    """Flag only evidence-backed candidates; legal offers are not automatically useful."""
    gold = int(player.get("gold", 0))
    hp = float(player.get("hp", 100.0))
    level = int(player.get("level", 1))
    expected_level = (4 if round_index <= 4 else 5 if round_index <= 8 else
                      6 if round_index <= 12 else 7 if round_index <= 16 else 8)
    risk = hp <= 35.0
    has_buy = any(x["type"] == 0 and x.get("slots") for x in legal_alternatives)
    has_xp = any(x["type"] == 1 for x in legal_alternatives)
    has_reroll = any(x["type"] == 2 for x in legal_alternatives)
    shop = player.get("shop", [])
    inventory = [u for u in list(player.get("board", [])) + list(player.get("bench", []))
                 if isinstance(u, dict) and u.get("occupied")]
    owned_ids = {str(u.get("champion_id")) for u in inventory}
    useful_offer = any(
        isinstance(shop[slot].get("champion_id"), (str, int)) and
        str(shop[slot].get("champion_id")) in owned_ids
        for option in legal_alternatives if option["type"] == 0
        for slot in [item.get("slot") for item in option.get("slots", [])]
        if slot is not None and slot < len(shop) and isinstance(shop[slot], dict)
    )
    action_type = int(selected_action[0]) if selected_action else -1
    action_reason = strategy.get("reason") or strategy.get("strategy_reason")
    risk_economy = risk and gold > 50 and level < expected_level
    missed_candidate = bool(risk_economy and action_type == 6 and useful_offer)
    return {
        "risk_state": risk,
        "high_gold": gold > 50,
        "expected_level": expected_level,
        "below_expected_level": level < expected_level,
        "legal_buy_available": has_buy,
        "legal_xp_available": has_xp,
        "legal_reroll_available": has_reroll,
        "useful_pair_or_upgrade_offer_detected": useful_offer,
        "selected_action_type": action_type,
        "selected_strategy_reason": action_reason,
        "potential_missed_progress": missed_candidate,
        "interpretation": (
            "PASS while at risk, above 50 gold, below the heuristic level target, and a matching copy is in shop; review whether buying is actually correct."
            if missed_candidate else
            "No strong missed-progress signal. A legal offer alone is not evidence that spending was correct."
        ),
    }


def _signature(player):
    def slots(units):
        return tuple(
            (str(unit.get("champion_id", "")), str(unit.get("uuid", "")),
             int(unit.get("star", 0)), tuple(unit.get("item_ids", [])))
            if unit.get("occupied") else None
            for unit in units
        )
    return (
        slots(player["board"]),
        slots(player["bench"]),
        tuple(player.get("item_components", [])),
        tuple(player.get("item_inventory", [])),
    )


def _cycle_signature(player, strategy):
    """Deterministic loop key: unit UUIDs, board/bench slots, items, economy and strategy."""
    strategic_fields = (
        "composition_direction", "composition_locked", "composition_focus",
        "composition_strength", "core_units", "core_unit_ids", "core_traits",
        "planned_units", "planned_unit_ids", "planned_traits",
        "composition_focus_weights", "active_traits",
    )
    context = {
        key: strategy.get(key)
        for key in strategic_fields
        if key in strategy
    }
    return (
        _signature(player),
        int(player.get("gold", 0)),
        int(player.get("xp", 0)),
        int(player.get("level", 0)),
        json.dumps(context, sort_keys=True, separators=(",", ":"), default=str),
    )


def _strategic_summary(lobby, player_id, player, strategy):
    board_units = [u for u in player["board"] if u.get("occupied")]
    bench_units = [u for u in player["bench"] if u.get("occupied")]
    score = 0.0
    scored_units = []
    for unit in board_units:
        try:
            unit_score = float(lobby._engine.get_unit_comp_score(
                int(player_id), str(unit["champion_id"]), int(unit.get("star", 1))
            ))
        except (RuntimeError, ValueError, TypeError):
            unit_score = None
        if unit_score is not None:
            score += unit_score
        scored_units.append({
            "champion_id": unit.get("champion_id"),
            "star": int(unit.get("star", 1)),
            "composition_score": unit_score,
        })
    core_units = list(strategy.get("core_units", []))
    core_traits = list(strategy.get("core_traits", []))
    active_traits = strategy.get("active_traits", {})
    board_names = {str(u.get("champion_id", "")) for u in board_units}
    bench_names = {str(u.get("champion_id", "")) for u in bench_units}
    core_trait_counts = {
        trait: int(active_traits.get(trait, 0)) for trait in core_traits
    }
    return {
        "board_composition_score": score,
        "board_unit_scores": scored_units,
        "board_unit_count": len(board_units),
        "bench_unit_count": len(bench_units),
        "board_star_counts": {
            str(star): sum(int(u.get("star", 1)) == star for u in board_units)
            for star in (1, 2, 3)
        },
        "bench_star_counts": {
            str(star): sum(int(u.get("star", 1)) == star for u in bench_units)
            for star in (1, 2, 3)
        },
        "board_two_star_count": sum(int(u.get("star", 1)) >= 2 for u in board_units),
        "bench_two_star_count": sum(int(u.get("star", 1)) >= 2 for u in bench_units),
        "composition_direction": strategy.get("composition_direction", ""),
        "composition_locked": bool(strategy.get("composition_locked", False)),
        "composition_focus": strategy.get("composition_focus", ""),
        "composition_focus_weights": strategy.get("composition_focus_weights", {}),
        "composition_strength": float(strategy.get("composition_strength", 0.0)),
        "core_units": core_units,
        "core_unit_ids": strategy.get("core_unit_ids", []),
        "core_units_on_board": sorted(board_names.intersection(map(str, core_units))),
        "core_units_in_bench": sorted(bench_names.intersection(map(str, core_units))),
        "core_traits": core_traits,
        "core_trait_counts": core_trait_counts,
        "core_traits_active_count": sum(count > 0 for count in core_trait_counts.values()),
        "active_traits": active_traits,
    }


def _effect_for_action(action, before, after):
    kind = int(action[0])
    before_sig, after_sig = _signature(before), _signature(after)
    if kind in MOVEMENT_TYPES:
        return before_sig != after_sig
    if kind == 0:
        return (before.get("gold") != after.get("gold")
                or before.get("bench") != after.get("bench"))
    if kind == 1:
        return before.get("gold") != after.get("gold") or before.get("shop") != after.get("shop")
    if kind == 2:
        return before.get("gold") != after.get("gold") or before.get("xp") != after.get("xp")
    if kind == 5:
        return before_sig != after_sig or before.get("gold") != after.get("gold")
    if kind in (7, 8):
        return before_sig != after_sig
    return False


def load_policy(checkpoint_path, obs_dim, device):
    checkpoint = torch.load(checkpoint_path, map_location=device)
    state = checkpoint.get("policy", checkpoint)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    try:
        policy.load_compatible_state_dict(state)
    except (RuntimeError, KeyError, ValueError) as exc:
        raise RuntimeError(
            "Checkpoint incompatível com a arquitetura/observação atual. "
            "Use o checkpoint do modelo correspondente."
        ) from exc
    policy.eval()
    return policy


def audit_seed(policy, device, seed, max_steps, output, fail_on_loop):
    lobby = CppTFTLobbyWrapper(seed=seed)
    visited = [dict() for _ in range(8)]
    history = [[] for _ in range(8)]
    try:
        observations = np.asarray(lobby.reset(seed=seed), dtype=np.float32)
        if observations.ndim != 2 or observations.shape[0] != 8:
            raise ValueError(f"Observações nativas inesperadas: {observations.shape}")
        initial = lobby.get_audit_snapshot()
        initial_strategies = lobby.get_strategy_snapshots()
        for player_id, player in enumerate(initial["players"]):
            visited[player_id][_cycle_signature(player, initial_strategies[player_id])] = {
                "step": -1, "action": None, "signature": repr(_cycle_signature(player, initial_strategies[player_id]))
            }

        for step_index in range(max_steps):
            before_snapshot = lobby.get_audit_snapshot()
            before_players = before_snapshot["players"]
            strategies_before = lobby.get_strategy_snapshots()
            strategic_before_all = [
                _strategic_summary(lobby, player_id, before_players[player_id], strategies_before[player_id])
                for player_id in range(8)
            ]
            masks = lobby.get_action_masks()
            metrics_before = lobby.get_anti_loop_metrics()
            alive = [
                player_id for player_id, info in enumerate(lobby.players)
                if info.alive and not info.eliminated
            ]
            actions = [list(PASS) for _ in range(8)]
            diagnostics = [[] for _ in range(8)]
            if alive:
                obs_batch = torch.as_tensor(observations[alive], dtype=torch.float32, device=device)
                with torch.no_grad():
                    chosen, _, _, _, diag = policy.get_action_and_value_with_diagnostics(
                        obs_batch, masks=_mask_batch(masks, alive, device), deterministic=True
                    )
                for row, player_id in enumerate(alive):
                    actions[player_id] = chosen[row].detach().cpu().to(torch.int64).tolist()
                    diagnostics[player_id] = diag[row]

            mask_valid = [_mask_allows(actions[i], masks[i]) if i in alive else True for i in range(8)]
            observations, rewards, done, info = lobby.step(actions)
            observations = np.asarray(observations, dtype=np.float32)
            action_rewards = np.asarray(info.get("action_rewards", np.zeros(8)), dtype=np.float32).reshape(-1)
            total_rewards = np.asarray(rewards, dtype=np.float32).reshape(-1)
            after_snapshot = lobby.get_audit_snapshot()
            after_players = after_snapshot["players"]
            strategies_after = lobby.get_strategy_snapshots()
            metrics = lobby.get_anti_loop_metrics()
            loops = []

            for player_id in range(8):
                before, after = before_players[player_id], after_players[player_id]
                action = actions[player_id]
                before_sig, after_sig = _signature(before), _signature(after)
                before_cycle_sig = _cycle_signature(before, strategies_before[player_id])
                after_cycle_sig = _cycle_signature(after, strategies_after[player_id])
                executed = _effect_for_action(action, before, after)
                action_reward = float(action_rewards[player_id]) if player_id < len(action_rewards) else None
                if executed:
                    execution_status = "state_changed"
                elif int(action[0]) == 6:
                    execution_status = "pass"
                elif action_reward is not None and action_reward < 0:
                    execution_status = "blocked_or_invalid_no_state_change"
                else:
                    execution_status = "no_state_change_observed"
                loop = None
                if int(action[0]) in MOVEMENT_TYPES and executed and after_cycle_sig in visited[player_id] and before_cycle_sig != after_cycle_sig:
                    prior = visited[player_id][after_cycle_sig]
                    loop = {
                        "previous_step": int(prior["step"]),
                        "previous_action": prior["action"],
                        "cycle_length": int(step_index - prior["step"]),
                        "sequence": [
                            entry for entry in history[player_id]
                            if int(prior["step"]) <= int(entry["step"]) <= step_index
                        ] + [{
                            "step": int(step_index), "action": action,
                            "cycle_signature_before": repr(before_cycle_sig),
                            "cycle_signature_after": repr(after_cycle_sig),
                            "action_reward": action_reward,
                            "strategy_before": strategic_before_all[player_id],
                            "strategy_after": None,
                        }],
                    }
                    loops.append({"player_id": player_id, **loop})
                # Record every post-action state, not just movement states: a move can
                # return to a state visited before a buy/sell/XP action.
                visited[player_id].setdefault(after_cycle_sig, {
                    "step": step_index, "action": action, "signature": repr(after_cycle_sig),
                })

                strategic_before = strategic_before_all[player_id]
                strategic_after = _strategic_summary(
                    lobby, player_id, after, strategies_after[player_id]
                )
                if loop is not None and loop.get("sequence"):
                    loop["sequence"][-1]["strategy_after"] = strategic_after
                record = {
                    "seed": int(seed),
                    "step": int(step_index),
                    "round_before": int(before_snapshot["round"]),
                    "round_after": int(after_snapshot["round"]),
                    "player_id": int(player_id),
                    "alive_at_decision": player_id in alive,
                    "selected_action": action,
                    "selected_action_mask_valid": bool(mask_valid[player_id]),
                    "action_effect_observed": bool(executed),
                    "execution_status": execution_status,
                    "action_reward": action_reward,
                    "total_reward": float(total_rewards[player_id]) if player_id < len(total_rewards) else None,
                    "action_diagnostics": diagnostics[player_id],
                    "legal_alternatives": _legal_alternatives(action, masks[player_id], before),
                    "economy_diagnostic": _economy_diagnostic(
                        before, strategies_before[player_id],
                        _legal_alternatives(action, masks[player_id], before),
                        int(before_snapshot["round"]), action
                    ),
                    "reward_components": info.get("reward_components", [None] * 8)[player_id]
                        if isinstance(info.get("reward_components"), (list, tuple))
                        and player_id < len(info.get("reward_components")) else None,
                    "reward_components_available": isinstance(info.get("reward_components"), (list, tuple))
                        and player_id < len(info.get("reward_components"))
                        and info.get("reward_components")[player_id] is not None,
                    "native_mask": _json_masks(masks[player_id]),
                    "board_bench_signature_before": repr(before_sig),
                    "board_bench_signature_after": repr(after_sig),
                    "cycle_signature_before": repr(before_cycle_sig),
                    "cycle_signature_after": repr(after_cycle_sig),
                    "cycle_context_before": {
                        "gold": int(before.get("gold", 0)), "xp": int(before.get("xp", 0)),
                        "level": int(before.get("level", 0)),
                        "strategy": strategic_before,
                    },
                    "cycle_context_after": {
                        "gold": int(after.get("gold", 0)), "xp": int(after.get("xp", 0)),
                        "level": int(after.get("level", 0)),
                        "strategy": strategic_after,
                    },
                    "board_before": before["board"],
                    "bench_before": before["bench"],
                    "shop_before": before["shop"],
                    "gold_before": int(before["gold"]),
                    "xp_before": int(before["xp"]),
                    "board_after": after["board"],
                    "bench_after": after["bench"],
                    "shop_after": after["shop"],
                    "item_components_before": list(before.get("item_components", [])),
                    "item_components_after": list(after.get("item_components", [])),
                    "item_inventory_before": list(before.get("item_inventory", [])),
                    "item_inventory_after": list(after.get("item_inventory", [])),
                    "gold_after": int(after["gold"]),
                    "xp_after": int(after["xp"]),
                    "strategy_before": strategic_before,
                    "strategy_after": strategic_after,
                    "anti_loop_metrics_before": metrics_before,
                    "anti_loop_metrics_after": metrics,
                    "engine_events": info.get("events", []),
                    "loop_detected": loop,
                }
                output.write(json.dumps(record, ensure_ascii=False) + "\n")
                history[player_id].append({
                    "step": int(step_index),
                    "action": action,
                    "cycle_signature_before": repr(before_cycle_sig),
                    "cycle_signature_after": repr(after_cycle_sig),
                    "action_reward": action_reward,
                    "strategy_before": strategic_before,
                    "strategy_after": strategic_after,
                })

            if loops and fail_on_loop:
                raise RuntimeError(
                    f"Loop nativo detectado no seed={seed}, step={step_index}: {loops}"
                )
            if done:
                return step_index + 1
        # A step limit is an intentional audit truncation, not a test failure.
        # A detected loop still raises above when --fail-on-loop is enabled.
        return max_steps
    finally:
        lobby.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True, type=Path)
    parser.add_argument("--seeds", default="20261022,20261023")
    parser.add_argument("--max-steps", type=int, default=300)
    parser.add_argument("--output", type=Path, default=Path("reports/native_ppo_loop_audit.jsonl"))
    parser.add_argument("--fail-on-loop", action="store_true")
    args = parser.parse_args()
    if not args.checkpoint.is_file():
        parser.error(f"Checkpoint não encontrado: {args.checkpoint}")
    if args.max_steps < 1:
        parser.error("--max-steps precisa ser >= 1")
    seeds = [int(x.strip()) for x in args.seeds.split(",") if x.strip()]
    if not seeds:
        parser.error("--seeds precisa conter ao menos um seed")

    device = torch.device("cpu")
    probe = CppTFTLobbyWrapper(seed=seeds[0])
    try:
        obs = np.asarray(probe.reset(seed=seeds[0]), dtype=np.float32)
        obs_dim = int(obs.shape[-1])
    finally:
        probe.close()
    policy = load_policy(args.checkpoint, obs_dim, device)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    total_steps = 0
    with args.output.open("w", encoding="utf-8") as output:
        for seed in seeds:
            count = audit_seed(policy, device, seed, args.max_steps, output, args.fail_on_loop)
            total_steps += count
            print(f"seed={seed}: {count} passos auditados")
    print(f"Relatório: {args.output}")
    print(f"Seeds: {len(seeds)} | passos totais: {total_steps}")


if __name__ == "__main__":
    main()
