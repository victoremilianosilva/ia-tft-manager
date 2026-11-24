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
import gc
import tracemalloc
from concurrent.futures import ThreadPoolExecutor
import csv
import json
import os
import platform
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
try:
    import psutil
except ImportError:
    psutil = None


REPO_ROOT = Path(__file__).resolve().parents[1]
# Running a file under scripts/ puts that directory, not the repository root,
# at sys.path[0]. The adapter and its sibling modules live at the root.
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


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


def _step_native(engine, _seed: int):
    call_start = time.perf_counter()
    result = engine.step(PASS_ACTIONS, False, False)
    pybind_call_ms = (time.perf_counter() - call_start) * 1000.0
    profile = dict(result.pop("_binding_profile", {}))
    profile["pybind_call_inclusive"] = pybind_call_ms
    profile["binding_gil_held_ms"] = pybind_call_ms
    for key, value in result.pop("_engine_profile_ms", {}).items():
        profile[f"native_{key}"] = float(value)
    for key, value in result.pop("_engine_profile_counts", {}).items():
        profile[f"native_count_{key}"] = int(value)
    return bool(result.get("lobby_done", False)), profile


def _step_wrapper(env, _seed: int):
    _observations, _rewards, done, info = env.step(PASS_ACTIONS)
    return bool(done), info.get("performance_profile", {})


def _run_case(
    mode: str,
    lobby_count: int,
    warmup: int,
    iterations: int,
    seed: int,
    item_catalog: str | None,
    memory_profile: bool = False,
) -> dict:
    native = mode == "native"
    os.environ["TFT_PROFILE_STEPS"] = "1"
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
                done, _profile = step_fn(target, seed + index)
                if done:
                    _reset(target, (seed + index) & 0xFFFFFFFF, native)

        per_lobby_samples = [[] for _ in targets]
        stage_samples = [{} for _ in targets]
        counter_samples = [{} for _ in targets]
        batch_samples = []
        completed_lobby_steps = 0
        terminal_resets = 0
        memory_before = None
        rss_before = None
        if memory_profile:
            gc.collect()
            tracemalloc.start()
            tracemalloc.reset_peak()
            memory_before = tracemalloc.get_traced_memory()
            if psutil is not None:
                rss_before = psutil.Process(os.getpid()).memory_info().rss

        for _ in range(iterations):
            batch_start = time.perf_counter()
            for index, target in enumerate(targets):
                start = time.perf_counter()
                done, profile = step_fn(target, seed + index)
                elapsed_ms = (time.perf_counter() - start) * 1000.0
                per_lobby_samples[index].append(elapsed_ms)
                if isinstance(profile, dict) and profile:
                    binding_total = float(profile.get("binding_total_ms", 0.0))
                    if mode == "wrapper":
                        if "python_wrapper_total" in profile:
                            profile["python_wrapper_exclusive_ms"] = max(
                                0.0, float(profile["python_wrapper_total"]) - binding_total
                            )
                        if "pybind_call_inclusive" in profile:
                            profile["pybind_argument_conversion_overhead_ms"] = max(
                                0.0, float(profile["pybind_call_inclusive"]) - binding_total
                            )
                    else:
                        profile["native_pybind_boundary_overhead_ms"] = max(
                            0.0, elapsed_ms - binding_total
                        )
                for stage_name, stage_ms in profile.items():
                    destination = counter_samples if stage_name.startswith("native_count_") else stage_samples
                    destination[index].setdefault(stage_name, []).append(float(stage_ms))
                completed_lobby_steps += 1
                if done:
                    _reset(target, (seed + index) & 0xFFFFFFFF, native)
                    terminal_resets += 1
            batch_samples.append((time.perf_counter() - batch_start) * 1000.0)

        memory_metrics = {}
        if memory_profile:
            current_bytes, peak_bytes = tracemalloc.get_traced_memory()
            before_current, _before_peak = memory_before or (0, 0)
            memory_metrics = {
                "python_tracemalloc_current_delta_bytes": current_bytes - before_current,
                "python_tracemalloc_peak_bytes": peak_bytes,
                "python_tracemalloc_peak_delta_bytes": max(0, peak_bytes - before_current),
            }
            if psutil is not None and rss_before is not None:
                rss_after = psutil.Process(os.getpid()).memory_info().rss
                memory_metrics["process_rss_before_bytes"] = rss_before
                memory_metrics["process_rss_after_bytes"] = rss_after
                memory_metrics["process_rss_delta_bytes"] = rss_after - rss_before
            tracemalloc.stop()

        return {
            "mode": mode,
            "memory": memory_metrics,
            "lobbies": lobby_count,
            "players_per_lobby": 8,
            "warmup_iterations_per_lobby": warmup,
            "measured_iterations_per_lobby": iterations,
            "total_lobby_steps": completed_lobby_steps,
            "terminal_resets_during_measurement": terminal_resets,
            "sequential_batch": _stats(batch_samples),
            "per_lobby": [_stats(samples) for samples in per_lobby_samples],
            "stage_metrics_per_lobby": [
                {name: _stats(values) for name, values in stages.items()}
                for stages in stage_samples
            ],
            "counter_metrics_per_lobby": [
                {name: _stats(values) for name, values in counters.items()}
                for counters in counter_samples
            ],
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


def _run_parallel_case(
    mode: str,
    lobby_count: int,
    warmup: int,
    iterations: int,
    seed: int,
    item_catalog: str | None,
) -> dict:
    """Run independent lobbies concurrently; exposes GIL/native scaling limits."""
    native = mode == "native"
    factory = _make_native if native else _make_wrapper
    step_fn: Callable = _step_native if native else _step_wrapper
    targets = []
    try:
        for index in range(lobby_count):
            target = factory((seed + index) & 0xFFFFFFFF, item_catalog)
            targets.append(target)
            _reset(target, (seed + index) & 0xFFFFFFFF, native)

        def step_one(index, target, submitted_at):
            started = time.perf_counter()
            dispatch_wait_ms = (started - submitted_at) * 1000.0
            done, profile = step_fn(target, seed + index)
            elapsed_ms = (time.perf_counter() - started) * 1000.0
            profile["thread_dispatch_wait_ms"] = dispatch_wait_ms
            return index, done, profile, elapsed_ms

        def run_parallel_iteration(executor, pairs):
            futures = []
            for index, target in pairs:
                submitted_at = time.perf_counter()
                futures.append(executor.submit(step_one, index, target, submitted_at))
            return [future.result() for future in futures]

        with ThreadPoolExecutor(max_workers=lobby_count) as executor:
            pairs = list(enumerate(targets))
            for _ in range(warmup):
                results = run_parallel_iteration(executor, pairs)
                for index, done, _profile, _elapsed in results:
                    if done:
                        _reset(targets[index], (seed + index) & 0xFFFFFFFF, native)

            per_lobby_samples = [[] for _ in targets]
            stage_samples = [{} for _ in targets]
            counter_samples = [{} for _ in targets]
            batch_samples = []
            terminal_resets = 0
            for _ in range(iterations):
                batch_start = time.perf_counter()
                results = run_parallel_iteration(executor, pairs)
                batch_samples.append((time.perf_counter() - batch_start) * 1000.0)
                for index, done, profile, elapsed_ms in results:
                    per_lobby_samples[index].append(elapsed_ms)
                    binding_total = float(profile.get("binding_total_ms", 0.0))
                    if mode == "wrapper":
                        if "python_wrapper_total" in profile:
                            profile["python_wrapper_exclusive_ms"] = max(
                                0.0, float(profile["python_wrapper_total"]) - binding_total
                            )
                        if "pybind_call_inclusive" in profile:
                            profile["pybind_argument_conversion_overhead_ms"] = max(
                                0.0, float(profile["pybind_call_inclusive"]) - binding_total
                            )
                    else:
                        profile["native_pybind_boundary_overhead_ms"] = max(
                            0.0, elapsed_ms - binding_total
                        )
                    for stage_name, stage_ms in profile.items():
                        destination = counter_samples if stage_name.startswith("native_count_") else stage_samples
                        destination[index].setdefault(stage_name, []).append(float(stage_ms))
                    if done:
                        _reset(targets[index], (seed + index) & 0xFFFFFFFF, native)
                        terminal_resets += 1

        return {
            "mode": mode,
            "lobbies": lobby_count,
            "execution": "thread_pool_independent_engines",
            "max_workers": lobby_count,
            "terminal_resets_during_measurement": terminal_resets,
            "concurrent_batch": _stats(batch_samples),
            "per_lobby": [_stats(samples) for samples in per_lobby_samples],
            "stage_metrics_per_lobby": [
                {name: _stats(values) for name, values in stages.items()}
                for stages in stage_samples
            ],
            "counter_metrics_per_lobby": [
                {name: _stats(values) for name, values in counters.items()}
                for counters in counter_samples
            ],
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
    parser.add_argument("--memory-profile", action="store_true", help="Mede alocações Python via tracemalloc (altera o custo medido).")
    parser.add_argument("--parallel-check", action="store_true", help="Compara steps em threads independentes para evidenciar contenção do GIL.")
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
        "version": 3,
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
            "step_profiling_enabled": True,
            "profiling_env_var": "TFT_PROFILE_STEPS=1",
            "memory_profile_enabled": args.memory_profile,
            "parallel_check_enabled": args.parallel_check,
            "gil_policy": "held_during_pybind_call",
        },
        "results": [],
        "parallel_results": [],
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
                args.seed, args.item_catalog, args.memory_profile,
            )
            report["results"].append(result)
            if result.get("memory"):
                print(f"  memory: {result['memory']}", flush=True)
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
                for stage_name, stage_stats in result["stage_metrics_per_lobby"][index].items():
                    print(
                        f"    {stage_name}: mean={stage_stats['mean_ms']:.3f} ms | "
                        f"p95={stage_stats['p95_ms']:.3f} ms",
                        flush=True,
                    )

            if args.parallel_check and lobby_count > 1:
                parallel_result = _run_parallel_case(
                    mode, lobby_count, args.warmup, args.iterations,
                    args.seed, args.item_catalog,
                )
                serial_mean = result["sequential_batch"]["mean_ms"]
                parallel_mean = parallel_result["concurrent_batch"]["mean_ms"]
                parallel_result["sequential_batch_mean_ms"] = serial_mean
                parallel_result["speedup_vs_sequential"] = (
                    serial_mean / parallel_mean if parallel_mean > 0 else 0.0
                )
                report["parallel_results"].append(parallel_result)
                print(
                    f"  threaded: mean={parallel_mean:.2f} ms | "
                    f"serial={serial_mean:.2f} ms | "
                    f"speedup={parallel_result['speedup_vs_sequential']:.2f}x",
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
                    "calls_per_second", "stage",
                ),
            )
            writer.writeheader()
            for result in report["results"]:
                for scope, stats in (
                    ("sequential_batch", result["sequential_batch"]),
                    *[(f"lobby_{i}", item) for i, item in enumerate(result["per_lobby"])],
                ):
                    writer.writerow({
                        "mode": result["mode"], "lobbies": result["lobbies"],
                        "scope": scope, "stage": "total_step", **stats,
                    })
                for lobby_index, stage_map in enumerate(result["stage_metrics_per_lobby"]):
                    for stage_name, stats in stage_map.items():
                        writer.writerow({
                            "mode": result["mode"], "lobbies": result["lobbies"],
                            "scope": f"lobby_{lobby_index}", "stage": stage_name, **stats,
                        })
                for lobby_index, counter_map in enumerate(result["counter_metrics_per_lobby"]):
                    for counter_name, stats in counter_map.items():
                        writer.writerow({
                            "mode": result["mode"], "lobbies": result["lobbies"],
                            "scope": f"lobby_{lobby_index}", "stage": counter_name, **stats,
                        })
        print(f"CSV: {output.resolve()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
