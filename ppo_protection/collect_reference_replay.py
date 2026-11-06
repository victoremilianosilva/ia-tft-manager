"""Collect real C++ states and reference actions for approved fine-tuning scenarios.

Run only after the ten-scenario chain has been reviewed. No state is fabricated:
scenarios are matched against observations naturally reached by the native engine.
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
from economy_finetuning.finetune import ACTION_DIMS, MASK_SHAPES, _actions_to_native, _flatten_masks
from economy_finetuning.scenario_generator import SCENARIOS, decode_observation, matching_scenarios


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output", default="ppo_protection/reference_replay.pt")
    parser.add_argument("--steps", type=int, default=100000)
    parser.add_argument("--min-per-scenario", type=int, default=64)
    parser.add_argument("--max-per-scenario", type=int, default=2048)
    parser.add_argument("--seed", type=int, default=20270101)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    args = parser.parse_args()
    if args.steps <= 0 or args.min_per_scenario <= 0 or args.max_per_scenario < args.min_per_scenario:
        parser.error("steps/min-per-scenario/max-per-scenario inválidos")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA solicitada, mas indisponível.")
    device = torch.device(args.device)
    checkpoint_path = Path(args.checkpoint).expanduser().resolve()
    if not checkpoint_path.is_file():
        raise FileNotFoundError(checkpoint_path)
    payload = torch.load(checkpoint_path, map_location=device, weights_only=False)
    if not isinstance(payload, dict) or "policy" not in payload:
        raise ValueError("Checkpoint deve conter a chave policy.")
    env = CppTFTLobbyWrapper(seed=args.seed)
    rows_obs, rows_actions, rows_masks, rows_labels = [], [], {key: [] for key in MASK_SHAPES}, []
    counts = {item.scenario_id: 0 for item in SCENARIOS if item.trainable}
    try:
        obs = env.reset(seed=args.seed)
        if obs.ndim != 2 or obs.shape[0] != 8:
            raise RuntimeError(f"Shape nativo inesperado: {obs.shape}")
        policy = TFTPolicy(int(obs.shape[-1]), ACTION_DIMS).to(device)
        policy.load_compatible_state_dict(payload["policy"])
        policy.eval()
        for step in range(args.steps):
            raw_masks = env.get_action_masks()
            masks = _flatten_masks(raw_masks, device)
            obs_tensor = torch.as_tensor(obs, dtype=torch.float32, device=device)
            with torch.no_grad():
                actions, _, _, _ = policy.get_action_and_value(obs_tensor, masks=masks, deterministic=True)
            action_array = actions.cpu().numpy().astype(np.int64)
            for player_id in range(8):
                state = decode_observation(obs[player_id], player_id=player_id)
                labels = [item.scenario_id for item in matching_scenarios(state) if item.trainable]
                labels = [label for label in labels if counts.get(label, 0) < args.max_per_scenario]
                if not labels:
                    continue
                rows_obs.append(np.asarray(obs[player_id], dtype=np.float32).copy())
                rows_actions.append(action_array[player_id].copy())
                rows_labels.append(labels)
                for key in MASK_SHAPES:
                    rows_masks[key].append(masks[key][player_id].detach().cpu().numpy().astype(np.bool_, copy=True))
                for label in labels:
                    counts[label] += 1
            obs, _, done, _ = env.step(_actions_to_native(action_array))
            if done:
                obs = env.reset(seed=args.seed + step + 1)
            if step and step % 5000 == 0:
                print(f"coleta {step}/{args.steps}: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
            if counts and all(value >= args.min_per_scenario for value in counts.values()):
                break
    finally:
        env.close()
    if not rows_obs:
        raise RuntimeError("Nenhum estado de cenário treinável foi encontrado; replay não foi salvo.")
    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "schema_version": 1,
        "source_checkpoint": str(checkpoint_path),
        "source_checkpoint_sha256": __import__("hashlib").sha256(checkpoint_path.read_bytes()).hexdigest(),
        "seed": args.seed,
        "steps": step + 1,
        "observations": np.asarray(rows_obs, dtype=np.float32),
        "actions": np.asarray(rows_actions, dtype=np.int64),
        "masks": {key: np.asarray(value, dtype=np.bool_) for key, value in rows_masks.items()},
        "scenario_ids": rows_labels,
        "scenario_counts": counts,
        "minimum_per_scenario": args.min_per_scenario,
    }
    torch.save(data, output)
    report = {key: {"samples": value, "meets_minimum": value >= args.min_per_scenario} for key, value in counts.items()}
    report_path = output.with_suffix(".coverage.json")
    report_path.write_text(json.dumps({"steps": step + 1, "rows": len(rows_obs), "coverage": report}, indent=2), encoding="utf-8")
    print(f"Replay salvo: {output}")
    print(f"Cobertura: {report_path}")
    for key, value in report.items():
        print(f"{key}: {value['samples']} {'OK' if value['meets_minimum'] else 'SEM COBERTURA SUFICIENTE'}")


if __name__ == "__main__":
    main()
