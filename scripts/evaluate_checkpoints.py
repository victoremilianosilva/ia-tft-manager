"""Head-to-head evaluation of two fixed TFT policy checkpoints.

Example (PowerShell):
  $env:TFT_ENGINE_BACKEND = "cpp"
  python scripts/evaluate_checkpoints.py --baseline checkpoints/baseline.pt --candidate tft_checkpoint.pt --matches 40 --output reports/head_to_head.csv

Each match puts four seats on each policy and rotates the candidate seats between matches.
The script does not train either policy or write to the training checkpoint.
"""
from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path

import numpy as np
import torch

from engine_backend import make_lobby_factory
from policy import TFTPolicy


ACTION_DIMS = [7, 5, 9, 28, 28, 28]
PASS_ACTION = {"type": 6}


def load_policy(path: Path, obs_dim: int, device: torch.device) -> TFTPolicy:
    checkpoint = torch.load(path, map_location=device)
    state = checkpoint.get("policy", checkpoint)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    policy.load_state_dict(state)
    policy.eval()
    return policy


def as_mask_batch(mask_list, indices, device):
    keys = mask_list[0].keys()
    return {
        key: torch.as_tensor(
            np.stack([mask_list[i][key] for i in indices]),
            dtype=torch.bool,
            device=device,
        )
        for key in keys
    }


def policy_actions(policy, observations, masks, indices, device):
    if not indices:
        return {}
    obs_batch = torch.as_tensor(
        np.asarray(observations[indices], dtype=np.float32),
        dtype=torch.float32,
        device=device,
    )
    mask_batch = as_mask_batch(masks, indices, device)
    with torch.no_grad():
        actions = policy.get_action(
            obs_batch,
            masks=mask_batch,
            deterministic=True,
        )[0].detach().cpu().numpy()
    return {idx: actions[row].astype(int).tolist() for row, idx in enumerate(indices)}


def action_dict(values):
    return {
        "type": int(values[0]),
        "shop_slot": int(values[1]),
        "bench_slot": int(values[2]),
        "board_target": int(values[3]),
        "board_source": int(values[4]),
        "conditioned_board_target": int(values[5]),
    }


def run_match(factory, baseline, candidate, candidate_slots, seed, device, max_steps):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    lobby = factory(seed=seed)
    try:
        observations = np.asarray(lobby.reset(), dtype=np.float32)
        if observations.ndim != 2 or observations.shape[0] != 8:
            raise ValueError(f"Observações inesperadas: {observations.shape}")
        obs_dim = observations.shape[-1]

        # Checkpoint models are loaded by the caller after the first lobby establishes obs_dim.
        policies = {"baseline": baseline, "candidate": candidate}
        rows = []
        final_info = {}
        for step in range(max_steps):
            if getattr(lobby, "finished", False):
                break
            masks = lobby.get_action_masks()
            if len(masks) != 8:
                raise ValueError(f"Esperava 8 máscaras; recebi {len(masks)}")

            candidate_indices = sorted(candidate_slots)
            baseline_indices = [i for i in range(8) if i not in candidate_slots]
            chosen = {}
            chosen.update(policy_actions(policies["candidate"], observations, masks, candidate_indices, device))
            chosen.update(policy_actions(policies["baseline"], observations, masks, baseline_indices, device))

            actions = [
                action_dict(chosen[i]) if lobby.players[i].alive else dict(PASS_ACTION)
                for i in range(8)
            ]
            observations, _, done, info = lobby.step(actions)
            final_info = info if isinstance(info, dict) else {}
            observations = np.asarray(observations, dtype=np.float32)
            if done:
                break
        else:
            raise RuntimeError(f"Partida excedeu max_steps={max_steps}; resultado não será contabilizado.")

        get_public_state = getattr(lobby, "get_public_state", None)
        state = get_public_state() if callable(get_public_state) else final_info
        ranking = state.get("ranking") or state.get("final_ranking") or getattr(lobby, "final_ranking", [])
        placement_by_id = {}
        if isinstance(ranking, list):
            for rank, item in enumerate(ranking, start=1):
                player_id = item.get("player_id") if isinstance(item, dict) else item
                try:
                    placement_by_id[int(player_id)] = rank
                except (TypeError, ValueError):
                    continue

        players = state.get("players", [])
        if isinstance(players, list):
            for idx, player in enumerate(players):
                if not isinstance(player, dict):
                    continue
                pid = int(player.get("player_id", idx))
                place = player.get("placement")
                if place is not None:
                    try:
                        placement_by_id[pid] = int(place)
                    except (TypeError, ValueError):
                        pass

        if len(placement_by_id) < 8:
            raise RuntimeError(
                "A engine não expôs colocação para todos os jogadores; "
                "não vou inferir rankings ausentes."
            )

        for player_id in range(8):
            version = "candidate" if player_id in candidate_slots else "baseline"
            placement = placement_by_id[player_id]
            rows.append({
                "seed": seed,
                "player_id": player_id,
                "version": version,
                "placement": placement,
                "win": int(placement == 1),
                "round": state.get("round", getattr(lobby, "round", "")),
                "candidate_seats": ",".join(map(str, sorted(candidate_slots))),
            })
        return rows
    finally:
        close = getattr(lobby, "close", None)
        if callable(close):
            close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--matches", type=int, default=40)
    parser.add_argument("--seed", type=int, default=20261015)
    parser.add_argument("--max-steps", type=int, default=10000)
    parser.add_argument("--output", type=Path, default=Path("reports/head_to_head.csv"))
    args = parser.parse_args()
    if args.matches < 1:
        parser.error("--matches precisa ser >= 1")
    if not args.baseline.is_file() or not args.candidate.is_file():
        parser.error("Os caminhos dos dois checkpoints precisam existir.")

    device = torch.device("cpu")
    backend, factory = make_lobby_factory()
    print(f"Engine: {backend.upper()} | partidas: {args.matches} | device: CPU")

    # Establish observation dimensions using the selected engine.
    probe = factory(seed=args.seed)
    try:
        probe_obs = np.asarray(probe.reset(), dtype=np.float32)
        if probe_obs.ndim != 2 or probe_obs.shape[0] != 8:
            raise ValueError(f"Observações inesperadas no probe: {probe_obs.shape}")
        obs_dim = probe_obs.shape[-1]
    finally:
        close = getattr(probe, "close", None)
        if callable(close):
            close()

    baseline = load_policy(args.baseline, obs_dim, device)
    candidate = load_policy(args.candidate, obs_dim, device)

    rows = []
    for match_idx in range(args.matches):
        # Rotate which seats use the candidate to reduce seat-order bias.
        offset = match_idx % 8
        candidate_slots = {(offset + j) % 8 for j in range(4)}
        match_seed = args.seed + match_idx
        result = run_match(
            factory, baseline, candidate, candidate_slots,
            match_seed, device, args.max_steps,
        )
        rows.extend(result)
        print(f"[{match_idx + 1}/{args.matches}] seed={match_seed} concluída")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV: {args.output}")
    for version in ("baseline", "candidate"):
        group = [row for row in rows if row["version"] == version]
        avg_place = sum(row["placement"] for row in group) / len(group)
        wins = sum(row["win"] for row in group)
        win_rate = wins / len(group)
        top4 = sum(row["placement"] <= 4 for row in group) / len(group)
        print(
            f"{version}: n={len(group)} avg_placement={avg_place:.3f} "
            f"wins={wins} win_rate={win_rate:.3%} top4_rate={top4:.3%}"
        )


if __name__ == "__main__":
    main()
