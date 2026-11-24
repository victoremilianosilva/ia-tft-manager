#!/usr/bin/env python3
"""Benchmark the native TFT lobby engine separately from its Python adapter.

Examples (PowerShell):
    python scripts/benchmark_engine.py
    python scripts/benchmark_engine.py --lobbies 1 4 --warmup 10 --iterations 100
    python scripts/benchmark_engine.py --mode native --lobbies 1 4 --json-out engine-native.json
    python scripts/benchmark_engine.py --mode wrapper --lobbies 1 --csv-out engine-wrapper.csv

The native mode times the pybind call to TFTLobby.step() and therefore includes
native execution plus result conversion at the binding boundary. The wrapper
mode additionally includes CppTFTLobbyWrapper's Python-side snapshot,
validation, reward-audit and outcome-event work. Lobbies are deliberately
stepped sequentially, matching LobbyVectorEnv's current execution model.
No PPO, policy inference, semantic batch construction or optimizer work runs.
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


PASS_ACTIONS = [[6, 0, 0, 0, 0, 0] for _ in range(8)]


def _percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * percentile)))
    return ordered[index]


def _stats(samples_ms: list[float]) -> dict[str, float | int]:
    total_seconds = sum(samples_ms) / 1000.0
    return {
        "calls": len(samples_ms),
        "total_ms": round(sum(samples_ms), 3),
        "mean_ms": round(statistics.fmean(samples_ms), 3) if samples_ms else 0.0,
        "median_ms": round(statistics.median(samples_ms), 3) if samples_ms else 0.0,
        "p95_ms": round(_percentile(samples_ms, 0.95), 3),
        "p99_ms": round(_percentile(samples_ms, 0.99), 3),
        "min_ms": round(min(samples_ms), 3) if samples_ms else 0.0,
        "max_ms": round(max(samples_ms), 3) if samples_ms else 0.0,
        "calls_per_second": round(len(samples_ms) / total_seconds, 2) if total_seconds else 0.0,
    }


def _make_native(seed: int, item_catalog: str | None):
    # Import through the same module that resolves the repository's native
    # extension search paths, but instantiate the pybind class directly.
    from cpp_lobby_env import _NativeTFTLobby

    return _NativeTFTLobby(seed, "", item_catalog or str(
        Path(__file__).resolve().parents[1] / "data" / "itens.json"
    ))


def _make_wrapper(seed: int, item_catalog: str | None):
    from cpp_lobby_env import CppTFTLobbyWrapper
    return CppTFTLobbyWrapper(seed=seed, item_catalog_path=item_catalog)


def _reset(target, seed: int, native: bool) -> None:
    target.reset(seed)


def _step_native(engine, _seed: int) -> bool:
    result = engine.step(PASS_ACTIONS, False, False)
    return bool(result.get("lobby_done", False))


def _step_wrapper(env, _seed: int) -> bool:
    _observations, _rewards, done, _info = env.step(PASS_ACTIONS)
    return bool(done)


def _run_case(
    mode: str,
    lobby_count: int,
    warmup: int,
    iterations: int,
    seed: int,
    item_catalog: str | None,
) -> dict:
    native = mode == "native"
    factory = _make_native if native else _make_wrapper
    step_fn: Callable = _step_native if native else _step_wrapper
    targets = []
    try:
        for index in range(lobby_count):
            target = factory((seed + index) & 0xFFFFFFFF, item_catalog)
            targets.append(target)
            _reset(target, (seed + index) & 0xFFFFFFFF, native)

        # Warm-up is intentionally excluded from all reported samples.
        for iteration in range(warmup):
            for index, target in enumerate(targets):
                if step_fn(target, seed + index):
                    _reset(target, (seed + index) & 0xFFFFFFFF, native)

        per_lobby_samples = [[] for _ in targets]
        batch_samples = []
        completed_lobby_steps = 0
        terminal_resets = 0

        for _ in range(iterations):
            batch_start = time.perf_counter()
            for index, target in enumerate(targets):
                start = time.perf_counter()
                done = step_fn(target, seed + index)
                elapsed_ms = (time.perf_counter() - start) * 1000.0
                per_lobby_samples[index].append(elapsed_ms)
                completed_lobby_steps += 1
                if done:
                    _reset(target, (seed + index) & 0xFFFFFFFF, native)
                    terminal_resets += 1
            batch_samples.append((time.perf_counter() - batch_start) * 1000.0)

        return {
            "mode": mode,
            "lobbies": lobby_count,
            "players_per_lobby": 8,
            "warmup_iterations_per_lobby": warmup,
            "measured_iterations_per_lobby": iterations,
            "total_lobby_steps": completed_lobby_steps,
            "terminal_resets_during_measurement": terminal_resets,
            "sequential_batch": _stats(batch_samples),
            "per_lobby": [_stats(samples) for samples in per_lobby_samples],
            "interpretation": (
                "pybind native TFTLobby.step call (native engine + binding result conversion)"
                if native else
                "CppTFTLobbyWrapper.step (native call + Python validation, snapshots, "
                "reward audit and action outcome event construction)"
            ),
        }
    finally:
        for target in targets:
            close = getattr(target, "close", None)
            if callable(close):
                close()


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mede o custo da engine C++ e, separadamente, do wrapper Python."
    )
    parser.add_argument("--mode", choices=("both", "native", "wrapper"), default="both")
    parser.add_argument("--lobbies", nargs="+", type=int, default=[1, 4])
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20261124)
    parser.add_argument("--item-catalog", default=None)
    parser.add_argument("--json-out", default=None)
    parser.add_argument("--csv-out", default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.warmup < 0 or args.iterations <= 0:
        raise SystemExit("--warmup deve ser >= 0 e --iterations deve ser > 0.")
    if not args.lobbies or any(value <= 0 for value in args.lobbies):
        raise SystemExit("--lobbies deve conter apenas valores > 0.")
    if not 0 <= args.seed <= 0xFFFFFFFF:
        raise SystemExit("--seed deve estar entre 0 e 2^32-1.")
    if args.item_catalog and not Path(args.item_catalog).expanduser().is_file():
        raise SystemExit(f"Catálogo de itens não encontrado: {args.item_catalog}")

    modes = ("native", "wrapper") if args.mode == "both" else (args.mode,)
    report = {
        "benchmark_id": "tft.native-engine-cost",
        "version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "processor": platform.processor(),
            "logical_cpu_count": __import__("os").cpu_count(),
        },
        "configuration": {
            "seed": args.seed,
            "warmup_iterations": args.warmup,
            "measured_iterations": args.iterations,
            "lobbies": args.lobbies,
            "lobby_execution": "sequential",
            "ppo_enabled": False,
            "semantic_batch_enabled": False,
        },
        "results": [],
    }

    for mode in modes:
        for lobby_count in args.lobbies:
            print(
                f"[{mode}] {lobby_count} lobby(s): "
                f"{args.warmup} warmup + {args.iterations} measured iterations",
                flush=True,
            )
            result = _run_case(
                mode, lobby_count, args.warmup, args.iterations,
                args.seed, args.item_catalog,
            )
            report["results"].append(result)
            batch = result["sequential_batch"]
            print(
                f"  batch mean={batch['mean_ms']:.2f} ms | "
                f"p95={batch['p95_ms']:.2f} ms | "
                f"{batch['calls_per_second']:.2f} batches/s",
                flush=True,
            )
            for index, stats in enumerate(result["per_lobby"]):
                print(
                    f"  lobby {index}: mean={stats['mean_ms']:.2f} ms | "
                    f"p95={stats['p95_ms']:.2f} ms | "
                    f"{stats['calls_per_second']:.2f} steps/s",
                    flush=True,
                )

    if args.json_out:
        output = Path(args.json_out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"JSON: {output.resolve()}")

    if args.csv_out:
        output = Path(args.csv_out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=(
                    "mode", "lobbies", "scope", "calls", "total_ms", "mean_ms",
                    "median_ms", "p95_ms", "p99_ms", "min_ms", "max_ms",
                    "calls_per_second",
                ),
            )
            writer.writeheader()
            for result in report["results"]:
                for scope, stats in (
                    ("sequential_batch", result["sequential_batch"]),
                    *[(f"lobby_{i}", item) for i, item in enumerate(result["per_lobby"])],
                ):
                    writer.writerow({
                        "mode": result["mode"],
                        "lobbies": result["lobbies"],
                        "scope": scope,
                        **stats,
                    })
        print(f"CSV: {output.resolve()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
