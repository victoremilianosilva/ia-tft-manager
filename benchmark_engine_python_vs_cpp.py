"""Benchmark the current full Python game engine against the native C++ engine.

Both backends are created through engine_backend.make_lobby_factory(), the same
LobbyVectorEnv adapter is used, and both receive the same fixed PASS actions.
The PPO policy and optimizer are deliberately excluded: this measures the game
engine, action-mask generation, and Python/C++ adapter overhead.

Run from the repository root after building the native C++ module:
    python benchmark_engine_python_vs_cpp.py
    python benchmark_engine_python_vs_cpp.py --lobbies 4 --steps 500 --warmup 50 --repeats 3
"""
from __future__ import annotations

import argparse
import json
import statistics
import time
from pathlib import Path
from typing import Any

import numpy as np

from engine_backend import make_lobby_factory
from vector_lobby_env import LobbyVectorEnv

PLAYERS_PER_LOBBY = 8
PASS_ACTION = {"type": 6}


def summarize(samples_ms: list[float]) -> dict[str, float]:
    if not samples_ms:
        return {}
    mean_ms = float(statistics.mean(samples_ms))
    return {
        "samples": len(samples_ms),
        "mean_ms": mean_ms,
        "median_ms": float(statistics.median(samples_ms)),
        "p95_ms": float(np.percentile(samples_ms, 95)),
        "min_ms": float(min(samples_ms)),
        "max_ms": float(max(samples_ms)),
        "calls_per_second": 1000.0 / mean_ms if mean_ms else 0.0,
    }


def summarize_masks(masks_by_lobby: list[Any]) -> dict[str, Any]:
    """Summarize mask shape and valid entries without assuming parity."""
    per_key: dict[str, dict[str, Any]] = {}
    for lobby_masks in masks_by_lobby:
        for player_masks in lobby_masks:
            for key, raw_mask in player_masks.items():
                mask = np.asarray(raw_mask, dtype=np.bool_)
                entry = per_key.setdefault(
                    key,
                    {"shapes": [], "valid_total": 0, "player_count": 0},
                )
                entry["shapes"].append(list(mask.shape))
                entry["valid_total"] += int(mask.sum())
                entry["player_count"] += 1

    for entry in per_key.values():
        shapes = entry.pop("shapes")
        entry["shape_per_player"] = shapes[0] if shapes else []
        entry["all_player_shapes_equal"] = all(shape == entry["shape_per_player"] for shape in shapes)

    return per_key


def make_vector_env(backend: str, lobbies: int, seed: int) -> LobbyVectorEnv:
    selected, lobby_factory = make_lobby_factory(backend)
    if selected != backend:
        raise RuntimeError(f"Backend selecionado inesperadamente: {selected}")

    factories = [
        (lambda factory=lobby_factory, lobby_seed=seed + index: factory(seed=lobby_seed))
        for index in range(lobbies)
    ]
    return LobbyVectorEnv(factories)


def run_once(
    backend: str,
    *,
    lobbies: int,
    steps: int,
    warmup: int,
    seed: int,
) -> dict[str, Any]:
    vec = make_vector_env(backend, lobbies, seed)
    timings: dict[str, list[float]] = {
        "reset": [],
        "action_masks": [],
        "env_step": [],
        "masks_plus_step": [],
    }
    rewards: list[float] = []
    done_count = 0
    observation: np.ndarray | None = None
    masks_by_lobby: list[Any] = []

    # Same PASS action and shape for each backend.
    actions = [
        [dict(PASS_ACTION) for _ in range(PLAYERS_PER_LOBBY)]
        for _ in range(lobbies)
    ]

    try:
        start = time.perf_counter()
        observation = vec.reset()
        timings["reset"].append((time.perf_counter() - start) * 1000)

        for index in range(warmup + steps):
            combined_start = time.perf_counter()

            start = time.perf_counter()
            masks_by_lobby = vec.env_method("get_action_masks")
            masks_elapsed = (time.perf_counter() - start) * 1000

            start = time.perf_counter()
            next_obs, step_rewards, dones, infos = vec.step(actions)
            step_elapsed = (time.perf_counter() - start) * 1000

            combined_elapsed = (time.perf_counter() - combined_start) * 1000

            if index >= warmup:
                timings["action_masks"].append(masks_elapsed)
                timings["env_step"].append(step_elapsed)
                timings["masks_plus_step"].append(combined_elapsed)
                rewards.extend(np.asarray(step_rewards, dtype=np.float64).reshape(-1).tolist())
                done_count += int(np.asarray(dones).sum())

            observation = next_obs

        return {
            "backend": backend,
            "seed": seed,
            "lobbies": lobbies,
            "players_per_lobby": PLAYERS_PER_LOBBY,
            "measured_steps_per_lobby": steps,
            "warmup_steps_per_lobby": warmup,
            "timings": {name: summarize(values) for name, values in timings.items()},
            "player_actions_per_second": (
                lobbies * PLAYERS_PER_LOBBY * 1000.0
                / summarize(timings["env_step"])["mean_ms"]
                if timings["env_step"] and summarize(timings["env_step"])["mean_ms"] > 0
                else 0.0
            ),
            "observation_shape": list(np.asarray(observation).shape),
            "observation_mean": float(np.asarray(observation).mean()),
            "observation_std": float(np.asarray(observation).std()),
            "reward_mean": float(np.mean(rewards)) if rewards else 0.0,
            "reward_sum": float(np.sum(rewards)),
            "done_count": done_count,
            "action_masks": summarize_masks(masks_by_lobby),
        }
    finally:
        vec.close()


def compare(python_result: dict[str, Any], cpp_result: dict[str, Any]) -> dict[str, Any]:
    speedups: dict[str, float | None] = {}
    for key in ("action_masks", "env_step", "masks_plus_step"):
        py_mean = python_result["timings"][key].get("mean_ms")
        cpp_mean = cpp_result["timings"][key].get("mean_ms")
        speedups[key] = (
            py_mean / cpp_mean
            if py_mean is not None and cpp_mean is not None and cpp_mean > 0
            else None
        )

    py_masks = python_result["action_masks"]
    cpp_masks = cpp_result["action_masks"]
    mask_keys = sorted(set(py_masks) | set(cpp_masks))

    return {
        "python_over_cpp_speedup": speedups,
        "python_vs_cpp_mean_latency_delta_ms": {
            key: (
                python_result["timings"][key].get("mean_ms", 0.0)
                - cpp_result["timings"][key].get("mean_ms", 0.0)
            )
            for key in ("action_masks", "env_step", "masks_plus_step")
        },
        "observation_shape_equal": (
            python_result["observation_shape"] == cpp_result["observation_shape"]
        ),
        "action_mask_keys_equal": set(py_masks) == set(cpp_masks),
        "action_mask_valid_count_delta_cpp_minus_python": {
            key: cpp_masks.get(key, {}).get("valid_total", 0)
            - py_masks.get(key, {}).get("valid_total", 0)
            for key in mask_keys
        },
        "note": (
            "Throughput uses the same fixed PASS workload and excludes PPO inference/training. "
            "A matching seed does not guarantee identical game states across independent engines; "
            "reward and observation statistics are diagnostics, not proof of full parity."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lobbies", type=int, default=1, help="Concurrent serial lobbies per benchmark process.")
    parser.add_argument("--steps", type=int, default=200, help="Measured steps per lobby.")
    parser.add_argument("--warmup", type=int, default=30, help="Unmeasured warmup steps per lobby.")
    parser.add_argument("--repeats", type=int, default=3, help="Independent repetitions per backend.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="engine_python_vs_cpp_comparison.json")
    args = parser.parse_args()

    if args.lobbies < 1 or args.steps < 1 or args.warmup < 0 or args.repeats < 1:
        parser.error("--lobbies, --steps e --repeats devem ser > 0; --warmup deve ser >= 0")

    # Alternate order between repetitions to reduce systematic order/thermal bias.
    collected: dict[str, list[dict[str, Any]]] = {"python": [], "cpp": []}
    for repetition in range(args.repeats):
        order = ("python", "cpp") if repetition % 2 == 0 else ("cpp", "python")
        for backend in order:
            print(
                f"\n[{repetition + 1}/{args.repeats}] "
                f"Executando engine {backend.upper()} "
                f"({args.lobbies} lobby(s), {args.steps} steps)...",
                flush=True,
            )
            result = run_once(
                backend,
                lobbies=args.lobbies,
                steps=args.steps,
                warmup=args.warmup,
                seed=args.seed,
            )
            collected[backend].append(result)
            print(json.dumps(result["timings"], ensure_ascii=False, indent=2), flush=True)

    def aggregate(backend: str) -> dict[str, Any]:
        runs = collected[backend]
        aggregated_timings: dict[str, Any] = {}
        for metric in ("reset", "action_masks", "env_step", "masks_plus_step"):
            means = [
                run["timings"][metric]["mean_ms"]
                for run in runs
                if run["timings"][metric]
            ]
            aggregated_timings[metric] = summarize(means)
            aggregated_timings[metric]["repetition_mean_ms"] = means

        latest = runs[-1]
        return {
            "backend": backend,
            "repeats": len(runs),
            "timings": aggregated_timings,
            "player_actions_per_second": float(statistics.mean(
                run["player_actions_per_second"] for run in runs
            )),
            "observation_shape": latest["observation_shape"],
            "observation_mean_per_repeat": [run["observation_mean"] for run in runs],
            "observation_std_per_repeat": [run["observation_std"] for run in runs],
            "reward_mean_per_repeat": [run["reward_mean"] for run in runs],
            "reward_sum_per_repeat": [run["reward_sum"] for run in runs],
            "done_count_per_repeat": [run["done_count"] for run in runs],
            "action_masks": latest["action_masks"],
        }

    python_result = aggregate("python")
    cpp_result = aggregate("cpp")
    comparison = compare(python_result, cpp_result)
    report = {
        "configuration": vars(args),
        "workload": {
            "action": "PASS",
            "players_per_lobby": PLAYERS_PER_LOBBY,
            "ppo_included": False,
            "python_backend": "TFTLobby (full Python game engine)",
            "cpp_backend": "CppTFTLobbyWrapper + native tft_engine",
            "shared_adapter": "LobbyVectorEnv",
        },
        "results": {"python": python_result, "cpp": cpp_result},
        "comparison": comparison,
    }

    output_path = Path(args.output)
    output_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("\n=== COMPARAÇÃO PYTHON FULL × C++ NATIVO ===")
    print(json.dumps(comparison, ensure_ascii=False, indent=2))
    print(f"\nRelatório salvo em: {output_path.resolve()}")


if __name__ == "__main__":
    main()
