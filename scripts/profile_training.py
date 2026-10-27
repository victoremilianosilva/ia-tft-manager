#!/usr/bin/env python3
"""Profile training phases without changing Trainer/PPO implementation.

Examples:
  python scripts/profile_training.py --mode fresh --updates 40 --num-envs 1 --rollout-steps 8 --output reports/profile_fresh.json
  python scripts/profile_training.py --mode resume --updates 40 --num-envs 1 --rollout-steps 8 --output reports/profile_resumed.json

The fresh mode safely backs up an existing tft_checkpoint.pt before starting.
The checkpoint produced by the fresh run remains as tft_checkpoint.pt for resume.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import statistics
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import torch


class Profiler:
    def __init__(self, updates: int, rollout_steps: int):
        self.updates = updates
        self.rollout_steps = rollout_steps
        self.phase_seconds: dict[str, float] = {}
        self.phase_calls: dict[str, int] = {}
        self.per_update_phases = [dict() for _ in range(updates)]
        self.per_update_wall = []
        self.completed_env_steps = 0
        self.active_update = None
        self.active_started = None
        self.enabled = True

    def current_bucket(self):
        if self.active_update is None:
            return None
        return self.active_update

    def timed(self, name, fn, *args, **kwargs):
        if not self.enabled:
            return fn(*args, **kwargs)
        if name == "mask_retrieval" and self.active_update is None:
            idx = min(self.completed_env_steps // self.rollout_steps, self.updates - 1)
            if idx >= 0 and len(self.per_update_wall) < self.updates:
                self.active_update = idx
                self.active_started = time.perf_counter()
        started = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - started
            self.phase_seconds[name] = self.phase_seconds.get(name, 0.0) + elapsed
            self.phase_calls[name] = self.phase_calls.get(name, 0) + 1
            idx = self.current_bucket()
            if idx is not None and idx < self.updates:
                row = self.per_update_phases[idx]
                row[name] = row.get(name, 0.0) + elapsed
            if name == "environment_step":
                self.completed_env_steps += 1

    def finish_update(self):
        if self.active_update is not None and self.active_started is not None:
            elapsed = time.perf_counter() - self.active_started
            self.per_update_wall.append(elapsed)
        self.active_update = None
        self.active_started = None

    def report(self, args, trainer, output_path):
        phases = {}
        for name, seconds in sorted(self.phase_seconds.items()):
            calls = self.phase_calls[name]
            phases[name] = {
                "total_seconds": round(seconds, 6),
                "calls": calls,
                "mean_ms_per_call": round(seconds * 1000 / calls, 4) if calls else 0,
            }
        per_update = []
        for idx, phases_for_update in enumerate(self.per_update_phases):
            row = {"update_index_in_run": idx + 1, "phase_seconds": {
                key: round(value, 6) for key, value in sorted(phases_for_update.items())
            }}
            if idx < len(self.per_update_wall):
                row["measured_wall_seconds"] = round(self.per_update_wall[idx], 6)
            per_update.append(row)
        git_commit = None
        try:
            git_commit = subprocess.run(
                ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
            ).stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            pass
        report = {
            "profile_version": 1,
            "mode": args.mode,
            "requested_updates": args.updates,
            "completed_updates_measured": len(self.per_update_wall),
            "num_envs": args.num_envs,
            "players_per_lobby": getattr(trainer, "PLAYERS_PER_LOBBY", 8),
            "num_agents": getattr(trainer, "num_agents", None),
            "rollout_steps": args.rollout_steps,
            "start_update": getattr(trainer, "start_update", None),
            "checkpoint_loaded": args.mode == "resume",
            "checkpoint_path": str(Path("tft_checkpoint.pt").resolve()),
            "git_commit": git_commit,
            "python": sys.version,
            "platform": platform.platform(),
            "torch_version": torch.__version__,
            "numpy_version": np.__version__,
            "device": str(getattr(trainer, "device", "unknown")),
            "phase_totals": phases,
            "per_update": per_update,
            "notes": [
                "Times are observational; instrumentation adds a small overhead.",
                "environment_step includes the complete vector environment step.",
                "measured_wall_seconds runs from first mask retrieval to mean-reward logging for each update.",
                "Compare fresh and resume runs with identical num_envs, rollout_steps, machine, build and settings.",
            ],
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("fresh", "resume"), required=True)
    parser.add_argument("--updates", type=int, default=40)
    parser.add_argument("--num-envs", type=int, default=1)
    parser.add_argument("--rollout-steps", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.updates < 1 or args.num_envs < 1 or args.rollout_steps < 1:
        parser.error("updates, num-envs e rollout-steps devem ser >= 1")

    checkpoint = Path("tft_checkpoint.pt")
    backup = Path("tft_checkpoint.pre_profile_backup.pt")
    if args.mode == "fresh":
        if checkpoint.exists():
            if backup.exists():
                parser.error(
                    f"{backup} já existe. Guarde/remova esse backup manualmente antes de iniciar "
                    "para não sobrescrever uma cópia anterior."
                )
            shutil.copy2(checkpoint, backup)
            checkpoint.unlink()
            print(f"Checkpoint anterior preservado em: {backup}")
        print("Modo fresh: Trainer iniciará sem tft_checkpoint.pt.")
    elif not checkpoint.exists():
        parser.error("Modo resume exige tft_checkpoint.pt. Rode primeiro o modo fresh e conclua os 40 updates.")

    from trainer import Trainer
    trainer = Trainer(num_envs=args.num_envs, use_subprocess=False)
    profiler = Profiler(args.updates, args.rollout_steps)

    def wrap_obj_method(obj, attr, phase, transform=None):
        original = getattr(obj, attr)
        def wrapped(*call_args, **call_kwargs):
            result = profiler.timed(phase, original, *call_args, **call_kwargs)
            if transform is not None:
                transform(call_args, call_kwargs, result)
            return result
        setattr(obj, attr, wrapped)

    wrap_obj_method(trainer, "_flatten_masks", "mask_flatten")
    wrap_obj_method(trainer, "_flatten_observations", "observation_conversion")
    wrap_obj_method(trainer, "_actions_to_lobby_format", "action_conversion")

    original_flatten_vector = trainer._flatten_vector
    def timed_flatten_vector(values, name):
        phase = "reward_conversion" if name == "rewards" else "done_conversion"
        return profiler.timed(phase, original_flatten_vector, values, name)
    trainer._flatten_vector = timed_flatten_vector

    original_env_method = trainer.vec_env.env_method
    def timed_env_method(method_name, *call_args, **call_kwargs):
        phase = {
            "get_action_masks": "mask_retrieval",
            "get_strategies": "strategy_retrieval",
            "get_anti_loop_metrics": "anti_loop_metrics",
        }.get(str(method_name), "other_env_method")
        return profiler.timed(phase, original_env_method, method_name, *call_args, **call_kwargs)
    trainer.vec_env.env_method = timed_env_method

    original_step = trainer.vec_env.step
    def timed_step(*call_args, **call_kwargs):
        return profiler.timed("environment_step", original_step, *call_args, **call_kwargs)
    trainer.vec_env.step = timed_step

    for method_name, phase in (
        ("get_action", "policy_inference"),
        ("get_action_and_value_with_entropy_diagnostics", "policy_inference_with_entropy_diagnostics"),
        ("get_value", "value_inference"),
        ("evaluate_actions", "policy_evaluate_actions"),
    ):
        if hasattr(trainer.policy, method_name):
            wrap_obj_method(trainer.policy, method_name, phase)

    wrap_obj_method(trainer.ppo, "update", "ppo_update")

    original_add_scalar = trainer.writer.add_scalar
    def timed_add_scalar(tag, scalar_value, *call_args, **call_kwargs):
        started = time.perf_counter()
        try:
            return original_add_scalar(tag, scalar_value, *call_args, **call_kwargs)
        finally:
            elapsed = time.perf_counter() - started
            profiler.phase_seconds["tensorboard_logging"] = profiler.phase_seconds.get("tensorboard_logging", 0.0) + elapsed
            profiler.phase_calls["tensorboard_logging"] = profiler.phase_calls.get("tensorboard_logging", 0) + 1
            if tag == "charts/mean_reward":
                profiler.finish_update()
    trainer.writer.add_scalar = timed_add_scalar

    try:
        started = time.perf_counter()
        trainer.train(total_updates=args.updates, rollout_steps=args.rollout_steps)
        total_seconds = time.perf_counter() - started
        report = profiler.report(args, trainer, args.output)
        report["training_wall_seconds"] = round(total_seconds, 6)
        args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Perfil salvo em: {args.output}")
        print(f"Tempo total do treino: {total_seconds:.2f}s")
        print(f"Updates medidos: {report['completed_updates_measured']}/{args.updates}")
        for name, metrics in report["phase_totals"].items():
            print(f"  {name}: {metrics['total_seconds']:.3f}s total | {metrics['mean_ms_per_call']:.2f}ms/chamada")
    finally:
        trainer.writer.close()


if __name__ == "__main__":
    main()
