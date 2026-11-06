"""Compara a execução serial e paralela das lobbies nativas C++.

Exemplo:
  python scripts/benchmark_lobby_parallelism.py --lobbies 1,2,4 --steps 100
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import statistics
import time
from functools import partial
from pathlib import Path

from cpp_lobby_env import CppTFTLobbyWrapper
from vector_lobby_env import LobbyVectorEnv


def run_case(lobbies: int, steps: int, warmup: int, use_subprocess: bool) -> dict:
    factory = partial(CppTFTLobbyWrapper)
    env = LobbyVectorEnv([factory for _ in range(lobbies)], use_subprocess=use_subprocess)
    actions = [[[6, 0, 0, 0, 0, 0] for _ in range(8)] for _ in range(lobbies)]
    samples = []
    try:
        env.reset()
        for _ in range(warmup):
            env.step(actions)
        started = time.perf_counter()
        for _ in range(steps):
            step_started = time.perf_counter()
            env.step(actions)
            samples.append(time.perf_counter() - step_started)
        elapsed = time.perf_counter() - started
    finally:
        env.close()

    transitions = lobbies * 8 * steps
    return {
        "mode": "subprocess" if use_subprocess else "serial",
        "lobbies": lobbies,
        "steps": steps,
        "warmup_steps": warmup,
        "elapsed_seconds": elapsed,
        "mean_step_seconds": statistics.fmean(samples) if samples else 0.0,
        "lobbies_per_second": lobbies * steps / elapsed if elapsed else 0.0,
        "agent_transitions_per_second": transitions / elapsed if elapsed else 0.0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lobbies", default="1,2,4")
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--output", default="reports/lobby_parallelism.json")
    args = parser.parse_args()
    lobby_counts = [int(value) for value in args.lobbies.split(",") if value.strip()]
    if not lobby_counts or any(value <= 0 for value in lobby_counts):
        parser.error("--lobbies deve conter inteiros positivos.")
    if args.steps <= 0 or args.warmup < 0:
        parser.error("--steps deve ser > 0 e --warmup deve ser >= 0.")

    results = []
    for count in lobby_counts:
        for parallel in (False, True):
            result = run_case(count, args.steps, args.warmup, parallel)
            results.append(result)
            print(
                f"{result['mode']:10s} | lobbies={count:2d} | "
                f"{result['agent_transitions_per_second']:.1f} agentes/s | "
                f"{result['mean_step_seconds'] * 1000:.2f} ms/step"
            )

    report = {
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "cpu_count": os.cpu_count(),
        },
        "results": results,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Relatório salvo em: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
