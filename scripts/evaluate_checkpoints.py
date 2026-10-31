"""Deterministic paired-seed checkpoint evaluation helpers.

The module keeps evaluation plumbing importable independently from training.
"""
from __future__ import annotations

import numpy as np
import torch

ACTION_DIMS = [9, 5, 9, 28, 28, 28]


def action_dict(values):
    values = [int(x) for x in values]
    result = {"type": values[0], "shop_slot": values[1], "bench_slot": values[2],
              "board_target": values[3], "board_source": values[4],
              "conditioned_board_target": values[5]}
    if result["type"] == 7:
        result.update(item_slot=values[1], item_target=values[2])
    elif result["type"] == 8:
        result.update(component_first=values[1], component_second=values[2],
                      item_target=values[3])
    return result


def as_mask_batch(masks, indices, device):
    if not indices:
        return {}
    keys = masks[indices[0]].keys()
    return {key: torch.as_tensor(np.stack([masks[i][key] for i in indices]),
                                 dtype=torch.bool, device=device) for key in keys}


def policy_actions(policy, observations, masks, indices, device):
    if not indices:
        return {}
    obs = torch.as_tensor(np.asarray(observations)[indices], dtype=torch.float32, device=device)
    batch_masks = as_mask_batch(masks, indices, device)
    with torch.no_grad():
        actions = policy.get_action(obs, masks=batch_masks, deterministic=True)[0]
    actions = actions.detach().cpu().numpy()
    return {player_id: [int(v) for v in actions[row]]
            for row, player_id in enumerate(indices)}


def _ranking_from_state(info, lobby):
    players = info.get("players") if isinstance(info, dict) else None
    if isinstance(players, list):
        ranked = {int(p["player_id"]): int(p["placement"])
                  for p in players if isinstance(p, dict)
                  and p.get("player_id") is not None and p.get("placement") is not None}
        if len(ranked) == 8:
            return ranked
    getter = getattr(lobby, "get_public_state", None)
    state = getter() if callable(getter) else {}
    ranking = state.get("ranking", []) if isinstance(state, dict) else []
    if isinstance(ranking, list) and len(ranking) == 8:
        if all(isinstance(x, dict) for x in ranking):
            return {int(x["player_id"]): int(x.get("placement", i + 1))
                    for i, x in enumerate(ranking)}
        return {int(player_id): place for place, player_id in enumerate(ranking, 1)}
    raise RuntimeError("Partida terminou sem ranking completo; não vou inferir rankings ausentes.")


def run_match(factory, baseline, candidate, candidate_slots, seed, device, max_steps=10000):
    lobby = factory(seed)
    try:
        try:
            observations = lobby.reset(seed=seed)
        except TypeError:
            observations = lobby.reset()
        done = False
        info = {}
        for _ in range(max_steps):
            masks = lobby.get_action_masks()
            alive = [i for i, player in enumerate(lobby.players)
                     if getattr(player, "alive", True) and not getattr(player, "eliminated", False)]
            actions = [[6, 0, 0, 0, 0, 0] for _ in range(8)]
            for slots, policy in ((set(range(8)) - set(candidate_slots), baseline),
                                  (set(candidate_slots), candidate)):
                selected = sorted(set(alive).intersection(slots))
                chosen = policy_actions(policy, observations, masks, selected, device)
                for player_id, action in chosen.items():
                    actions[player_id] = action
            observations, rewards, done, info = lobby.step(
                [action_dict(a) for a in actions])
            if done or getattr(lobby, "finished", False):
                break
        else:
            raise RuntimeError(f"Partida excedeu max_steps={max_steps} sem terminar.")
        ranking = _ranking_from_state(info, lobby)
        if set(ranking) != set(range(8)):
            raise RuntimeError("Partida terminou sem ranking completo; não vou inferir rankings ausentes.")
        return [{"seed": int(seed), "player_id": player_id,
                 "version": "candidate" if player_id in candidate_slots else "baseline",
                 "placement": ranking[player_id], "win": int(ranking[player_id] == 1)}
                for player_id in range(8)]
    finally:
        close = getattr(lobby, "close", None)
        if callable(close):
            close()


def _metric_summary(rows):
    total_actions = sum(int(r.get("actions", 0)) for r in rows)
    item_actions = sum(int(r.get("item_actions", 0)) for r in rows)
    equip_actions = sum(int(r.get("equip_actions", 0)) for r in rows)
    craft_actions = sum(int(r.get("craft_and_equip_actions", 0)) for r in rows)
    count = max(1, len(rows))
    return {"matches": len(rows),
            "mean_placement": float(np.mean([r["placement"] for r in rows])) if rows else None,
            "win_rate": float(np.mean([r.get("win", 0) for r in rows])) if rows else None,
            "actions": total_actions, "item_actions": item_actions,
            "item_action_rate": item_actions / total_actions if total_actions else 0.0,
            "equip_actions": equip_actions, "craft_and_equip_actions": craft_actions}


def summarize_paired_seeds(rows, bootstrap_samples=2000, bootstrap_seed=0):
    grouped = {}
    for row in rows:
        version = row.get("version")
        if version not in ("baseline", "candidate"):
            raise ValueError(f"Unknown policy version: {version}")
        key = int(row["seed"])
        grouped.setdefault(key, {"baseline": [], "candidate": []})[version].append(row)
    for seed, pair in grouped.items():
        if len(pair["baseline"]) != 4 or len(pair["candidate"]) != 4:
            raise ValueError(f"Seed {seed} must contain exactly four players per policy")
    if not grouped:
        raise ValueError("No paired seed rows supplied")
    baseline_rows = [r for p in grouped.values() for r in p["baseline"]]
    candidate_rows = [r for p in grouped.values() for r in p["candidate"]]
    metrics = ("mean_placement", "win_rate")
    per_seed = []
    deltas = {key: [] for key in metrics}
    for seed, pair in sorted(grouped.items()):
        b = _metric_summary(pair["baseline"])
        c = _metric_summary(pair["candidate"])
        per_seed.append({"seed": seed, "baseline": b, "candidate": c})
        for key in metrics:
            deltas[key].append(c[key] - b[key])
    rng = np.random.default_rng(bootstrap_seed)
    paired = {}
    for key, values in deltas.items():
        arr = np.asarray(values, dtype=float)
        samples = np.asarray([rng.choice(arr, size=len(arr), replace=True).mean()
                              for _ in range(max(1, int(bootstrap_samples)))])
        paired[key] = {"mean": float(arr.mean()),
                       "bootstrap_95_ci": [float(np.quantile(samples, .025)),
                                           float(np.quantile(samples, .975))]}
    return {"seed_count": len(grouped),
            "baseline": _metric_summary(baseline_rows),
            "candidate": _metric_summary(candidate_rows),
            "paired_delta_candidate_minus_baseline": paired,
            "per_seed": per_seed}
