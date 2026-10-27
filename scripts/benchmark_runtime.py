"""Reproducible runtime benchmark for the complete native PPO inference loop.

Measures mask retrieval/flattening, policy inference + action conversion, environment
step, and end-to-end iteration latency. This is a runtime benchmark, not a policy
quality evaluation. Run the same command on both revisions on the same machine.

Example (PowerShell):
  python scripts/benchmark_runtime.py --num-envs 4 --warmup 50 --iterations 300 --output reports/runtime_benchmark.json

For a useful comparison, run at least 3 independent processes per revision and compare
median end-to-end ms/iteration and agents/sec. Avoid running other CPU-heavy workloads.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from trainer import Trainer


def percentile(values: list[float], q: float) -> float:
    return float(np.percentile(np.asarray(values, dtype=np.float64), q))


def summarize_ms(values: list[float], bootstrap_samples: int, seed: int) -> dict:
    arr = np.asarray(values, dtype=np.float64) * 1000.0
    if arr.size == 0:
        raise ValueError("No benchmark samples collected")
    rng = np.random.default_rng(seed)
    if bootstrap_samples > 0 and arr.size > 1:
        indices = rng.integers(0, arr.size, size=(bootstrap_samples, arr.size))
        means = arr[indices].mean(axis=1)
        ci = [float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))]
    else:
        ci = [float(arr.mean()), float(arr.mean())]
    return {
        "samples": int(arr.size),
        "mean_ms": float(arr.mean()),
        "median_ms": float(np.median(arr)),
        "p95_ms": percentile(arr.tolist(), 95),
        "min_ms": float(arr.min()),
        "max_ms": float(arr.max()),
        "stddev_ms": float(arr.std(ddof=1)) if arr.size > 1 else 0.0,
        "bootstrap_95_ci_mean_ms": ci,
    }


def git_revision() -> str | None:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
            capture_output=True, text=True, timeout=3,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def benchmark(args) -> dict:
    # Keep execution deterministic where possible. Environment dynamics are still
    # measured, so compare the same seeds/configuration and report the revision.
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.set_num_threads(args.torch_threads)
    trainer = Trainer(num_envs=args.num_envs, use_subprocess=False)
    trainer.policy.eval()
    samples = {key: [] for key in (
        "mask_retrieval", "mask_flatten", "policy_and_action_conversion",
        "environment_step", "end_to_end",
    )}
    agent_steps = 0
    completed_iterations = 0
    observations = trainer._flatten_observations(trainer.vec_env.reset())
    obs = torch.as_tensor(observations, dtype=torch.float32)

    def one_iteration(record: bool):
        nonlocal observations, obs, agent_steps, completed_iterations
        tick = time.perf_counter()

        t0 = time.perf_counter()
        raw_masks = trainer.vec_env.env_method("get_action_masks")
        t1 = time.perf_counter()
        masks = trainer._flatten_masks(raw_masks)
        t2 = time.perf_counter()

        with torch.no_grad():
            actions, _, _, _ = trainer.policy.get_action(obs, masks=masks)
        lobby_actions = trainer._actions_to_lobby_format(actions)
        t3 = time.perf_counter()

        next_obs, _, dones, _ = trainer.vec_env.step(lobby_actions)
        t4 = time.perf_counter()

        observations = trainer._flatten_observations(next_obs)
        obs = torch.as_tensor(observations, dtype=torch.float32)
        # Vec envs may signal done per lobby; reset only finished environments if
        # supported, otherwise reset the vector environment as a whole.
        if np.asarray(dones).any():
            reset_obs = trainer.vec_env.reset()
            observations = trainer._flatten_observations(reset_obs)
            obs = torch.as_tensor(observations, dtype=torch.float32)

        if record:
            samples["mask_retrieval"].append(t1 - t0)
            samples["mask_flatten"].append(t2 - t1)
            samples["policy_and_action_conversion"].append(t3 - t2)
            samples["environment_step"].append(t4 - t3)
            samples["end_to_end"].append(t4 - tick)
            agent_steps += args.num_envs * 8
            completed_iterations += 1

    try:
        print(f"Aquecimento: {args.warmup} iterações; medição: {args.iterations}.", flush=True)
        with torch.no_grad():
            for _ in range(args.warmup):
                one_iteration(False)
            for index in range(args.iterations):
                one_iteration(True)
                if (index + 1) % max(1, args.iterations // 10) == 0:
                    print(f"  {index + 1}/{args.iterations}", flush=True)
    finally:
        trainer.vec_env.close()
        trainer.writer.close()

    elapsed = sum(samples["end_to_end"])
    metrics = {key: summarize_ms(vals, args.bootstrap_samples, args.seed + idx)
               for idx, (key, vals) in enumerate(samples.items())}
    median_s = metrics["end_to_end"]["median_ms"] / 1000.0
    return {
        "schema_version": 1,
        "benchmark": "native_ppo_inference_loop",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "revision": git_revision(),
        "configuration": {
            "num_envs": args.num_envs,
            "players_per_lobby": 8,
            "agents_per_iteration": args.num_envs * 8,
            "warmup_iterations": args.warmup,
            "measured_iterations": args.iterations,
            "seed": args.seed,
            "torch_threads": args.torch_threads,
            "device": "cpu",
            "engine_backend": "C++",
        },
        "system": {
            "platform": platform.platform(),
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "torch": torch.__version__,
            "cpu_count": os.cpu_count(),
            "torch_num_threads": torch.get_num_threads(),
        },
        "metrics": metrics,
        "throughput": {
            "agents_per_second_from_median": (
                (args.num_envs * 8) / (median_s) if median_s > 0 else None
            ),
            "agent_steps_per_second_from_total": (
                agent_steps / elapsed if elapsed > 0 else None
            ),
            "iterations_per_second_from_median": (
                1.0 / median_s if median_s > 0 else None
            ),
            "note": "Throughput uses measured inference+step iterations; excludes warmup and initialization. Agent steps are vectorized observations processed per iteration, not full training updates.",
        },
        "limitations": [
            "Does not measure PPO optimization/backpropagation or checkpoint I/O.",
            "CPU scheduling, thermal state, and background load affect results.",
            "Run multiple independent processes per revision; compare medians and confidence intervals.",
            "A faster runtime does not imply a stronger policy; use evaluate_checkpoints.py for policy quality.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--num-envs", type=int, default=4, help="Number of parallel lobbies (serial vector wrapper).")
    parser.add_argument("--warmup", type=int, default=50)
    parser.add_argument("--iterations", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20261027)
    parser.add_argument("--torch-threads", type=int, default=1)
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    parser.add_argument("--output", type=Path, default=Path("reports/runtime_benchmark.json"))
    parser.add_argument("--csv-output", type=Path, default=None, help="Optional per-iteration timing CSV.")
    args = parser.parse_args()
    if args.num_envs < 1 or args.warmup < 0 or args.iterations < 2:
        parser.error("--num-envs must be >= 1, --warmup >= 0, --iterations >= 2")
    if args.torch_threads < 1 or args.bootstrap_samples < 0:
        parser.error("--torch-threads must be >= 1 and --bootstrap-samples >= 0")

    report = benchmark(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"JSON: {args.output}")
    for key, value in report["metrics"].items():
        print(f"{key}: median={value['median_ms']:.3f} ms, p95={value['p95_ms']:.3f} ms, mean={value['mean_ms']:.3f} ms")
    print("Throughput: " + json.dumps(report["throughput"], ensure_ascii=False))
    if args.csv_output:
        args.csv_output.parent.mkdir(parents=True, exist_ok=True)
        with args.csv_output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["iteration", *report["metrics"].keys()])
            for idx in range(args.iterations):
                writer.writerow([idx + 1, *[
                    report["metrics"][key]["median_ms"] for key in report["metrics"]
                ]])
        print(f"CSV agregado: {args.csv_output} (medianas; use JSON para estatísticas por amostra)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
