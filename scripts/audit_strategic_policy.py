"""Audit a trained TFT checkpoint's economic decisions over reproducible seeds.

Example:
  python scripts/audit_strategic_policy.py --checkpoint checkpoints/latest.pt --seeds 11,12,13 --output reports/strategic_policy.jsonl

The --output path is used as a base name; records are written to
reports/strategic_policy/player_0.jsonl through player_7.jsonl.

This is an observational audit, not a pass/fail claim that an untrained policy is strategic.
It records selected actions, masked action probabilities, masks, gold before/after,
and action/total rewards so the results can be compared across checkpoints.
"""
from __future__ import annotations

import argparse
import json
import sys
from contextlib import ExitStack
from pathlib import Path

import numpy as np
import torch

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from cpp_lobby_env import CppTFTLobbyWrapper
from policy import TFTPolicy

ACTION_DIMS = [7, 5, 9, 28, 28, 28]
PASS_ACTION = {"type": 6}


def _mask_batch(masks, indices, device):
    keys = masks[indices[0]].keys()
    return {
        key: torch.as_tensor(
            np.stack([masks[index][key] for index in indices]),
            dtype=torch.bool,
            device=device,
        )
        for key in keys
    }


def _player_gold(lobby):
    """Prefer the audit snapshot; fall back to the public state."""
    for getter_name in ("get_audit_snapshot", "get_public_state"):
        getter = getattr(lobby, getter_name, None)
        if not callable(getter):
            continue
        state = getter()
        if not isinstance(state, dict):
            continue
        players = state.get("players", [])
        result = {}
        for index, player in enumerate(players if isinstance(players, list) else []):
            if not isinstance(player, dict) or "gold" not in player:
                continue
            result[int(player.get("player_id", index))] = int(player["gold"])
        if result:
            return result
    raise RuntimeError("A engine não expôs ouro por jogador no snapshot de auditoria.")


def _action_dict(values):
    return {
        "type": int(values[0]),
        "shop_slot": int(values[1]),
        "bench_slot": int(values[2]),
        "board_target": int(values[3]),
        "board_source": int(values[4]),
        "conditioned_board_target": int(values[5]),
    }


def _json_masks(player_masks):
    return {
        key: np.asarray(value, dtype=np.int8).tolist()
        for key, value in player_masks.items()
    }


def _player_output_paths(output_path: Path):
    """Return one JSONL path per player, derived from the legacy --output path."""
    output_dir = output_path.parent / output_path.stem
    return {player_id: output_dir / f"player_{player_id}.jsonl" for player_id in range(8)}


def _write_player_record(output_handles, player_id, record):
    """Write a record only to the file owned by its player."""
    if player_id not in output_handles:
        raise ValueError(f"Não existe arquivo de saída para o jogador {player_id}.")
    output_handles[player_id].write(json.dumps(record, ensure_ascii=False) + "\n")


def load_policy(checkpoint_path: Path, obs_dim: int):
    device = torch.device("cpu")
    checkpoint = torch.load(checkpoint_path, map_location=device)
    state_dict = checkpoint.get("policy", checkpoint)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    try:
        policy.load_state_dict(state_dict)
    except RuntimeError as exc:
        raise RuntimeError(
            "Checkpoint incompatível com a nova arquitetura de decisão por candidato "
            "ou com a dimensão atual da observação. Faça um novo treinamento; "
            "não carregue silenciosamente pesos antigos."
        ) from exc
    policy.eval()
    return policy, device


def audit_seed(policy, device, seed, output_handles, max_steps):
    lobby = CppTFTLobbyWrapper(seed=seed)
    try:
        observations = np.asarray(lobby.reset(seed=seed), dtype=np.float32)
        if observations.ndim != 2 or observations.shape[0] != 8:
            raise ValueError(f"Observações inesperadas: {observations.shape}")
        total_logged = 0

        for step_index in range(max_steps):
            if getattr(lobby, "finished", False):
                break

            masks = lobby.get_action_masks()
            gold_before = _player_gold(lobby)
            alive = [
                player_id for player_id, player in enumerate(lobby.players)
                if player.alive and not player.eliminated
            ]
            chosen = {player_id: [6, 0, 0, 0, 0, 0] for player_id in range(8)}
            diagnostics_by_player = {}

            if alive:
                obs_batch = torch.as_tensor(
                    observations[alive], dtype=torch.float32, device=device
                )
                mask_batch = _mask_batch(masks, alive, device)
                with torch.no_grad():
                    actions, _, _, _, diagnostics = policy.get_action_and_value_with_diagnostics(
                        obs_batch, masks=mask_batch, deterministic=True
                    )
                actions = actions.detach().cpu().numpy()
                for row, player_id in enumerate(alive):
                    chosen[player_id] = actions[row].astype(int).tolist()
                    diagnostics_by_player[player_id] = diagnostics[row]

            action_dicts = [
                _action_dict(chosen[player_id]) if player_id in alive else dict(PASS_ACTION)
                for player_id in range(8)
            ]
            observations, rewards, done, info = lobby.step(action_dicts)
            observations = np.asarray(observations, dtype=np.float32)
            gold_after = _player_gold(lobby)
            action_rewards = np.asarray(
                info.get("action_rewards", np.zeros(8)), dtype=np.float32
            ).reshape(-1)
            total_rewards = np.asarray(rewards, dtype=np.float32).reshape(-1)

            for player_id in range(8):
                record = {
                    "seed": int(seed),
                    "step": int(step_index),
                    "round": int(info.get("round", 0)),
                    "player_id": player_id,
                    "alive_at_decision": player_id in alive,
                    "action": chosen[player_id],
                    "diagnostics": diagnostics_by_player.get(player_id, []),
                    "masks": _json_masks(masks[player_id]) if player_id in alive else {},
                    "gold_before": gold_before.get(player_id),
                    "gold_after": gold_after.get(player_id),
                    "action_reward": float(action_rewards[player_id]) if player_id < len(action_rewards) else None,
                    "total_reward": float(total_rewards[player_id]) if player_id < len(total_rewards) else None,
                }
                _write_player_record(output_handles, player_id, record)
                total_logged += 1

            if done:
                break
        else:
            raise RuntimeError(f"Seed {seed} excedeu max_steps={max_steps}.")

        return total_logged
    finally:
        lobby.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True, type=Path)
    parser.add_argument("--seeds", default="20261021,20261022,20261023")
    parser.add_argument("--max-steps", type=int, default=10000)
    parser.add_argument("--output", type=Path, default=Path("reports/strategic_policy.jsonl"))
    args = parser.parse_args()

    if not args.checkpoint.is_file():
        parser.error(f"Checkpoint não encontrado: {args.checkpoint}")
    seeds = [int(part.strip()) for part in args.seeds.split(",") if part.strip()]
    if not seeds:
        parser.error("--seeds precisa conter ao menos um inteiro.")
    if args.max_steps < 1:
        parser.error("--max-steps precisa ser >= 1")

    probe = CppTFTLobbyWrapper(seed=seeds[0])
    try:
        probe_obs = np.asarray(probe.reset(seed=seeds[0]), dtype=np.float32)
        if probe_obs.ndim != 2 or probe_obs.shape[0] != 8:
            raise ValueError(f"Observações inesperadas no probe: {probe_obs.shape}")
        obs_dim = probe_obs.shape[-1]
    finally:
        probe.close()

    policy, device = load_policy(args.checkpoint, obs_dim)
    output_paths = _player_output_paths(args.output)
    output_dir = args.output.parent / args.output.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    # Open all eight files, including players eliminated before the first action.
    with ExitStack() as stack:
        output_handles = {
            player_id: stack.enter_context(path.open("w", encoding="utf-8"))
            for player_id, path in output_paths.items()
        }
        for seed in seeds:
            logged = audit_seed(policy, device, seed, output_handles, args.max_steps)
            count += logged
            print(f"seed={seed}: {logged} registros jogador/step")

    print(f"Relatórios por jogador: {output_dir}")
    for player_id, path in output_paths.items():
        print(f"  jogador {player_id}: {path}")
    print(f"Seeds: {len(seeds)} | registros jogador/step: {count}")


if __name__ == "__main__":
    main()
