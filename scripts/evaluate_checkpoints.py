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


def candidate_slots_for_seed(seed: int, master_seed: int = 0) -> set[int]:
    """Deterministic balanced four-seat rotation for one paired lobby seed."""
    if isinstance(seed, bool) or not isinstance(seed, (int, np.integer)):
        raise TypeError("seed must be an integer, not bool")
    if isinstance(master_seed, bool) or not isinstance(master_seed, (int, np.integer)):
        raise TypeError("master_seed must be an integer, not bool")
    # A coprime step of 1 visits all eight rotations before repeating.
    offset = (int(seed) + int(master_seed)) % 8
    return {(offset + index) % 8 for index in range(4)}


def validate_candidate_slots(candidate_slots) -> set[int]:
    if candidate_slots is None:
        raise ValueError("candidate_slots must be explicitly derived or supplied")
    slots = set(candidate_slots)
    if len(slots) != 4 or any(
        isinstance(slot, bool) or not isinstance(slot, (int, np.integer))
        or int(slot) < 0 or int(slot) >= 8 for slot in slots
    ):
        raise ValueError("candidate_slots must contain exactly four distinct player IDs in [0, 7]")
    return {int(slot) for slot in slots}


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
                 "placement": ranking[player_id], "win": int(ranking[player_id] == 1),\n                 "candidate_slots": sorted(candidate_slots)}
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
        for version in ("baseline", "candidate"):
            player_ids = [int(row["player_id"]) for row in pair[version]]
            if len(set(player_ids)) != 4 or any(pid < 0 or pid >= 8 for pid in player_ids):
                raise ValueError(f"Seed {seed} {version} must contain four distinct player IDs in [0, 7]")
        if set(int(row["player_id"]) for row in pair["baseline"]) & set(
            int(row["player_id"]) for row in pair["candidate"]
        ):
            raise ValueError(f"Seed {seed} assigns a player to both policies")
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


def _validate_evaluation_artifact(artifact, label):
    if not isinstance(artifact, dict):
        raise TypeError(f"{label} artifact manifest must be a dict")
    checkpoint_sha = artifact.get("checkpoint_sha256")
    if not isinstance(checkpoint_sha, str) or len(checkpoint_sha) != 64:
        raise ValueError(f"{label} checkpoint SHA-256 is missing or malformed")
    lineage = artifact.get("checkpoint_contract")
    if not isinstance(lineage, dict):
        raise ValueError(f"{label} checkpoint lineage contract is required")
    digest = lineage.get("sha256")
    contract = lineage.get("contract")
    if not isinstance(digest, str) or len(digest) != 64 or not isinstance(contract, dict):
        raise ValueError(f"{label} checkpoint lineage contract is malformed")
    if contract.get("contract_id") != "tft.ppo-checkpoint-lineage.v1":
        raise ValueError(f"{label} checkpoint lineage contract ID is unsupported")
    import hashlib
    import json
    canonical = json.dumps(
        contract, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    if hashlib.sha256(canonical).hexdigest() != digest:
        raise ValueError(f"{label} checkpoint lineage hash does not match its payload")
    components = contract.get("components")
    required = {
        "action_mask_contract", "critic_mask_input_contract",
        "semantic_state_contract", "reward_contract",
    }
    if not isinstance(components, dict) or set(components) != required:
        raise ValueError(f"{label} checkpoint lineage components are incomplete")
    return lineage


def run_paired_evaluation(
    factory, baseline, candidate, baseline_artifact, candidate_artifact,
    seeds, device, *, split, master_seed=0, max_steps=10000,
):
    """Run paired, seat-rotated lobbies only for semantically identical lineages.

    This is evaluation-only: policies are called in deterministic inference mode,
    and the function never updates weights or optimizer state.
    """
    if split not in {"validation", "test"}:
        raise ValueError("split must be validation or test")
    baseline_lineage = _validate_evaluation_artifact(baseline_artifact, "baseline")
    candidate_lineage = _validate_evaluation_artifact(candidate_artifact, "candidate")
    if baseline_lineage != candidate_lineage:
        raise ValueError("baseline and candidate checkpoint lineages are not semantically compatible")
    normalized_seeds = []
    for seed in seeds:
        if isinstance(seed, bool) or not isinstance(seed, (int, np.integer)):
            raise TypeError("evaluation seeds must be integers, not bool")
        normalized_seeds.append(int(seed))
    if not normalized_seeds or len(set(normalized_seeds)) != len(normalized_seeds):
        raise ValueError("evaluation seeds must be non-empty and unique")
    raw_rows = []
    schedule = []
    for seed in normalized_seeds:
        slots = candidate_slots_for_seed(seed, master_seed)
        schedule.append({"seed": seed, "candidate_player_ids": sorted(slots)})
        raw_rows.extend(run_match(
            factory, baseline, candidate, slots, seed, device, max_steps=max_steps
        ))
    return {
        "schema_version": 1,
        "evaluation_mode": "evaluation_only",
        "split": split,
        "baseline_checkpoint_sha256": baseline_artifact["checkpoint_sha256"],
        "candidate_checkpoint_sha256": candidate_artifact["checkpoint_sha256"],
        "checkpoint_lineage_sha256": baseline_lineage["sha256"],
        "master_seed": int(master_seed),
        "seat_rotation": schedule,
        "raw_results": raw_rows,
        "summary": summarize_paired_seeds(raw_rows),
    }
