#!/usr/bin/env python3
"""End-to-end profiler for the native TFT PPO training pipeline.

Runs a fresh, isolated training lineage and records inclusive timings for:
Engine/pybind calls, wrapper, vector dispatch, semantic projection/alignment,
policy inference, rollout storage, GAE, PPO update/loss, and optimizer steps.
Also records tracemalloc peak, process RSS/CPU, runtime versions and git revision.

This is an instrumentation run, not a policy-quality benchmark. Use the same
machine, catalogs, seed and configuration when comparing revisions.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import platform
import statistics
import subprocess
import sys
import time
import tracemalloc
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class Profiler:
    def __init__(self):
        self.samples = defaultdict(list)
        self.calls = defaultdict(int)
        self.started = time.perf_counter()

    def measure(self, name, fn, *args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            self.samples[name].append((time.perf_counter() - start) * 1000.0)
            self.calls[name] += 1

    def wrap(self, owner, attribute, metric, *, descriptor=None):
        if descriptor == "classmethod":
            original = owner.__dict__[attribute].__func__

            def wrapped(cls, *args, **kwargs):
                return self.measure(metric, original, cls, *args, **kwargs)

            setattr(owner, attribute, classmethod(wrapped))
        else:
            original = getattr(owner, attribute)

            def wrapped(*args, **kwargs):
                return self.measure(metric, original, *args, **kwargs)
            setattr(owner, attribute, wrapped)
        return original

    @staticmethod
    def summarize(values):
        if not values:
            return {"calls": 0, "total_ms": 0.0, "mean_ms": 0.0,
                    "median_ms": 0.0, "p95_ms": 0.0, "p99_ms": 0.0,
                    "min_ms": 0.0, "max_ms": 0.0}
        ordered = sorted(values)

        def pct(q):
            return ordered[min(len(ordered) - 1, round((len(ordered) - 1) * q))]

        return {
            "calls": len(values),
            "total_ms": round(sum(values), 3),
            "mean_ms": round(statistics.fmean(values), 3),
            "median_ms": round(statistics.median(values), 3),
            "p95_ms": round(pct(0.95), 3),
            "p99_ms": round(pct(0.99), 3),
            "min_ms": round(min(values), 3),
            "max_ms": round(max(values), 3),
        }

    def report(self):
        return {name: self.summarize(values)
                for name, values in sorted(self.samples.items())}


class NativeCallProxy:
    """Transparent proxy that times calls crossing the pybind object boundary."""
    def __init__(self, target, profiler):
        object.__setattr__(self, "_target", target)
        object.__setattr__(self, "_profiler", profiler)

    def __getattr__(self, name):
        value = getattr(self._target, name)
        if not callable(value):
            return value

        def call(*args, **kwargs):
            return self._profiler.measure("binding." + name, value, *args, **kwargs)
        return call

    def __setattr__(self, name, value):
        setattr(self._target, name, value)


def git_revision():
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def process_memory():
    result = {}
    try:
        import psutil
        process = psutil.Process()
        info = process.memory_info()
        result["rss_bytes"] = int(info.rss)
        result["vms_bytes"] = int(info.vms)
    except (ImportError, OSError):
        result["rss_bytes"] = None
        result["vms_bytes"] = None
    try:
        import resource
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        result["peak_rss_platform_units"] = int(peak)
        result["peak_rss_units"] = "bytes" if sys.platform == "darwin" else "KiB"
    except (ImportError, OSError):
        result["peak_rss_platform_units"] = None
        result["peak_rss_units"] = None
    return result


def install_instrumentation(profiler):
    import torch
    import trainer as trainer_module
    import cpp_lobby_env
    import vector_lobby_env
    import semantic_observation
    from cpp_lobby_env import CppTFTLobbyWrapper, _NativeSnapshotMapping
    from vector_lobby_env import LobbyVectorEnv
    from rollout import RolloutBuffer
    from ppo import PPOTrainer
    from policy import TFTPolicy

    # Replace only the native handle reference after normal construction.
    original_init = CppTFTLobbyWrapper.__init__

    def profiled_init(self, *args, **kwargs):
        profiler.measure("wrapper.initialize", original_init, self, *args, **kwargs)
        self._engine = NativeCallProxy(self._engine, profiler)

    CppTFTLobbyWrapper.__init__ = profiled_init

    # Split the first lazy materialization into native conversion and freezing.
    # This monkeypatch is confined to the profiler process; production wrapper
    # code and snapshot validation rules remain untouched.
    def profiled_base_dict(self):
        def materialize():
            if self._base is None:
                native_value = profiler.measure(
                    "snapshot.materialization.native_to_dict",
                    self._handle.to_dict,
                )
                self._base = profiler.measure(
                    "snapshot.materialization.freeze_snapshot",
                    cpp_lobby_env.freeze_snapshot,
                    native_value,
                )
            return self._base

        return profiler.measure(
            "snapshot.materialization.base_dict_total", materialize
        )

    _NativeSnapshotMapping._base_dict = profiled_base_dict

    profiler.wrap(CppTFTLobbyWrapper, "step", "wrapper.step")
    profiler.wrap(CppTFTLobbyWrapper, "reset", "wrapper.reset")
    profiler.wrap(CppTFTLobbyWrapper, "_copy_native_state_snapshot",
                  "wrapper.snapshot_validation", descriptor="classmethod")
    profiler.wrap(LobbyVectorEnv, "step", "vector.step_total")
    profiler.wrap(LobbyVectorEnv, "reset", "vector.reset_total")
    profiler.wrap(RolloutBuffer, "add", "rollout.add")
    profiler.wrap(RolloutBuffer, "compute_returns_and_advantages", "rollout.gae")
    profiler.wrap(PPOTrainer, "update", "ppo.update_total")
    profiler.wrap(PPOTrainer, "compute_loss", "ppo.compute_loss")
    profiler.wrap(TFTPolicy, "get_action", "policy.get_action")
    profiler.wrap(TFTPolicy, "get_action_and_value_with_entropy_diagnostics",
                  "policy.get_action_with_diagnostics")
    profiler.wrap(TFTPolicy, "get_value", "policy.get_value")
    profiler.wrap(TFTPolicy, "evaluate_actions", "policy.evaluate_actions")

    # These are module-level imports used by Trainer.train().
    profiler.wrap(trainer_module, "build_semantic_batch", "semantic.build_batch")
    profiler.wrap(trainer_module, "validate_semantic_batch_alignment",
                  "semantic.validate_alignment")
    profiler.wrap(semantic_observation, "project_native_player_state",
                  "semantic.project_player")
    profiler.wrap(cpp_lobby_env, "build_action_outcome_events",
                  "outcomes.build_factual_events")

    # Deepcopy is looked up through the shared copy module by all participating
    # modules. Count/time it without inspecting or mutating copied values.
    original_deepcopy = copy.deepcopy

    def timed_deepcopy(*args, **kwargs):
        return profiler.measure("python.deepcopy", original_deepcopy, *args, **kwargs)

    copy.deepcopy = timed_deepcopy

    return torch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="New, empty directory for this isolated run.")
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=20261124)
    parser.add_argument("--updates", type=int, default=2)
    parser.add_argument("--lobbies", type=int, nargs="+", default=[1, 2, 4])
    parser.add_argument("--rollout-steps", type=int, default=16)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--ppo-epochs", type=int, default=4)
    args = parser.parse_args()

    if not 0 <= args.seed <= 0xFFFFFFFF:
        parser.error("--seed must fit uint32")
    if min(args.updates, args.rollout_steps, args.batch_size, args.ppo_epochs) <= 0:
        parser.error("updates, rollout-steps, batch-size and ppo-epochs must be > 0")
    if not args.lobbies or any(value <= 0 for value in args.lobbies):
        parser.error("--lobbies must contain positive values")

    output_dir = args.output_dir.expanduser().resolve()
    if output_dir.exists() and any(output_dir.iterdir()):
        parser.error(f"output directory is not empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = (args.report or output_dir / "phase-a-profile.json").expanduser().resolve()

    profiler = Profiler()
    tracemalloc.start()
    memory_before = process_memory()
    cpu_before = time.process_time()
    wall_start = time.perf_counter()
    reports = []

    torch = install_instrumentation(profiler)
    from trainer import Trainer

    optimizer_step_types = set()

    for lobby_count in args.lobbies:
        profiler.samples.clear()
        profiler.calls.clear()
        run_dir = output_dir / f"lobbies-{lobby_count}"
        run_dir.mkdir(parents=True, exist_ok=True)
        os.environ.update({
            "TFT_TRAIN_SEED": str(args.seed),
            "TFT_NUM_LOBBIES": str(lobby_count),
            "TFT_TOTAL_UPDATES": str(args.updates),
            "TFT_ROLLOUT_STEPS": str(args.rollout_steps),
            "TFT_PPO_BATCH_SIZE": str(args.batch_size),
            "TFT_PPO_EPOCHS": str(args.ppo_epochs),
            "TFT_CHECKPOINT_PATH": str(run_dir / "native_ppo_checkpoint.pt"),
            "TFT_TRAIN_LOG_DIR": str(run_dir / "tensorboard"),
            "TFT_RUN_MANIFEST_PATH": str(run_dir / "run_manifest.json"),
            "TFT_OPGG_DISABLE_REFRESH": "1",
            "TFT_COMPOSITION_INTELLIGENCE_ENABLED": "1",
        })

        init_start = time.perf_counter()
        trainer = Trainer(num_envs=lobby_count, use_subprocess=False)
        init_ms = (time.perf_counter() - init_start) * 1000.0
        optimizer_type = type(trainer.optimizer)
        if optimizer_type not in optimizer_step_types:
            original_optimizer_step = optimizer_type.step

            def timed_optimizer_step(self, *step_args, **step_kwargs):
                return profiler.measure(
                    "optimizer.step", original_optimizer_step,
                    self, *step_args, **step_kwargs
                )

            optimizer_type.step = timed_optimizer_step
            optimizer_step_types.add(optimizer_type)
        try:
            train_start = time.perf_counter()
            trainer.train(total_updates=args.updates, rollout_steps=args.rollout_steps)
            train_ms = (time.perf_counter() - train_start) * 1000.0
        finally:
            trainer.vec_env.close()
            trainer.writer.close()

        reports.append({
            "lobbies": lobby_count,
            "players": lobby_count * 8,
            "initialization_ms": round(init_ms, 3),
            "training_wall_ms": round(train_ms, 3),
            "run_dir": str(run_dir),
            "timings": profiler.report(),
        })

    wall_ms = (time.perf_counter() - wall_start) * 1000.0
    cpu_ms = (time.process_time() - cpu_before) * 1000.0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_after = process_memory()

    report = {
        "schema_version": 1,
        "benchmark": "tft.phase-a.full-training-profile",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "revision": git_revision(),
        "system": {
            "platform": platform.platform(),
            "python": sys.version,
            "processor": platform.processor(),
            "logical_cpu_count": os.cpu_count(),
            "torch": __import__("torch").__version__,
            "numpy": __import__("numpy").__version__,
        },
        "configuration": {
            "seed": args.seed,
            "updates": args.updates,
            "lobby_counts": args.lobbies,
            "players_per_lobby": 8,
            "rollout_steps": args.rollout_steps,
            "batch_size": args.batch_size,
            "ppo_epochs": args.ppo_epochs,
            "device": "cpu",
            "ppo_enabled": True,
            "semantic_batch_enabled": True,
            "lobby_execution": "sequential-current-vector-env",
        },
        "runs": reports,
        "process": {
            "wall_ms": round(wall_ms, 3),
            "cpu_ms": round(cpu_ms, 3),
            "python_tracemalloc_current_bytes": int(current),
            "python_tracemalloc_peak_bytes": int(peak),
            "memory_before": memory_before,
            "memory_after": memory_after,
        },
        "limitations": [
            "binding.* timings are inclusive pybind call times; internal native engine work and C++ result conversion are not separated yet",
            "wrapper.step is inclusive and contains binding calls; do not sum inclusive timing rows",
            "tracemalloc excludes native C++ allocations and some allocator-owned memory",
            "RSS is process-wide and sampled before/after; use an external sampler for peak RSS over time",
            "profiling hooks add overhead; compare revisions using the same script and configuration",
            "snapshot.materialization.base_dict_total contains native_to_dict and freeze_snapshot; do not sum nested timings or add them to wrapper.snapshot_validation",
            "each lobby-count run uses a separate fresh checkpoint/log directory",
        ],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps({
        "report": str(report_path),
        "revision": report["revision"],
        "wall_ms": report["process"]["wall_ms"],
        "tracemalloc_peak_bytes": report["process"]["python_tracemalloc_peak_bytes"],
        "timing_keys_by_lobby_count": {
            str(run["lobbies"]): sorted(run["timings"])
            for run in reports
        },
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
