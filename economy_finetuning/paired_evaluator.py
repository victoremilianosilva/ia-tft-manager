"""Paired full-lobby evaluation: original and fine-tuned policies, same seeds."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cpp_lobby_env import CppTFTLobbyWrapper
from engine_contracts import ActionType
from policy import TFTPolicy
from economy_finetuning.finetune import ACTION_DIMS, _actions_to_native, _flatten_masks


def load_policy(checkpoint_path: Path, obs_dim: int, device):
    payload = torch.load(checkpoint_path, map_location=device, weights_only=False)
    state = payload.get("policy", payload)
    policy = TFTPolicy(obs_dim, ACTION_DIMS).to(device)
    policy.load_compatible_state_dict(state)
    policy.eval()
    return policy


def run_match(policy, seed: int, max_steps: int, device):
    env = CppTFTLobbyWrapper(seed=seed)
    try:
        obs = env.reset(seed=seed)
        initial_observation_sha256 = hashlib.sha256(
            np.asarray(obs, dtype=np.float32).tobytes()
        ).hexdigest()
        totals = np.zeros(8, dtype=np.float64)
        actions = [Counter() for _ in range(8)]
        final_info = None
        for step in range(max_steps):
            masks = _flatten_masks(env.get_action_masks(), device)
            obs_tensor = torch.as_tensor(obs, dtype=torch.float32, device=device)
            with torch.no_grad():
                selected, _, _, _ = policy.get_action_and_value(
                    obs_tensor, masks=masks, deterministic=True
                )
            action_array = selected.cpu().numpy().astype(np.int64)
            for player_id, row in enumerate(action_array):
                actions[player_id][ActionType(int(row[0])).name] += 1
            obs, rewards, done, info = env.step(_actions_to_native(action_array))
            totals += np.asarray(rewards, dtype=np.float64)
            if done:
                final_info = env.get_public_state()
                return {
                    "seed": seed, "steps": step + 1, "completed": True,
                    "initial_observation_sha256": initial_observation_sha256,
                    "total_rewards": totals.tolist(),
                    "action_counts": [dict(counter) for counter in actions],
                    "final_state": final_info,
                }
        final_info = env.get_public_state()
        return {
            "seed": seed, "steps": max_steps, "completed": False,
            "initial_observation_sha256": initial_observation_sha256,
            "total_rewards": totals.tolist(),
            "action_counts": [dict(counter) for counter in actions],
            "final_state": final_info,
        }
    finally:
        env.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", required=True)
    parser.add_argument("--finetuned", required=True)
    parser.add_argument("--seeds", default="20261105,20261106,20261107,20261108")
    parser.add_argument("--max-steps", type=int, default=2500)
    parser.add_argument("--output", required=True, help="JSONL de saída dentro do diretório da execução")
    args = parser.parse_args()
    original_path = Path(args.original).expanduser().resolve()
    tuned_path = Path(args.finetuned).expanduser().resolve()
    if not original_path.is_file() or not tuned_path.is_file():
        raise FileNotFoundError("Os dois checkpoints precisam existir.")
    seeds = [int(value.strip()) for value in args.seeds.split(",") if value.strip()]
    if not seeds or args.max_steps <= 0:
        parser.error("Informe ao menos uma seed e max-steps positivo.")

    device = torch.device("cpu")
    probe = CppTFTLobbyWrapper(seed=seeds[0])
    try:
        initial = probe.reset(seed=seeds[0])
        obs_dim = int(initial.shape[-1])
    finally:
        probe.close()
    original = load_policy(original_path, obs_dim, device)
    tuned = load_policy(tuned_path, obs_dim, device)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as stream:
        for seed in seeds:
            original_result = run_match(original, seed, args.max_steps, device)
            tuned_result = run_match(tuned, seed, args.max_steps, device)
            same_initial_state = (
                original_result["initial_observation_sha256"]
                == tuned_result["initial_observation_sha256"]
            )
            if not same_initial_state:
                raise RuntimeError(
                    f"Seed {seed}: os modelos não começaram da mesma observação; "
                    "comparação pareada inválida."
                )
            reward_deltas = [
                round(b - a, 6)
                for a, b in zip(original_result["total_rewards"], tuned_result["total_rewards"])
            ]
            row = {
                "seed": seed,
                "original": original_result,
                "finetuned": tuned_result,
                "reward_delta_per_player": reward_deltas,
                "mean_reward_delta": float(np.mean(reward_deltas)),
                "both_completed": original_result["completed"] and tuned_result["completed"],
                "same_initial_state": same_initial_state,
            }
            stream.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
            print(
                f"seed={seed} original_steps={original_result['steps']} "
                f"finetuned_steps={tuned_result['steps']} "
                f"mean_reward_delta={row['mean_reward_delta']:.4f}"
            )
    print(f"Resultados pareados: {output}")


if __name__ == "__main__":
    main()
