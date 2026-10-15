"""End-to-end comparison of the Python and native C++ lobby backends.

Run after building the native modules:
    python benchmark_engine_backends.py --steps 500 --seed 42

This benchmark uses the same fixed PASS policy for both backends. It reports
latency, throughput, observation/reward deltas, masks and anti-loop metrics.
It does not assume exact parity: differences are reported for investigation.
"""
from __future__ import annotations

import argparse
import json
import statistics
import time
from typing import Any

import numpy as np

from vector_lobby_env import LobbyVectorEnv


PLAYERS = 8
PASS_ACTION = [6, 0, 0, 0, 0, 0]


def _summary(values: list[float]) -> dict[str, float]:
    if not values:
        return {}
    return {
        "mean_ms": float(statistics.mean(values)),
        "median_ms": float(statistics.median(values)),
        "p95_ms": float(np.percentile(values, 95)),
        "min_ms": float(min(values)),
        "max_ms": float(max(values)),
        "steps_per_second": float(1000.0 / statistics.mean(values)),
    }


def _flatten_masks(masks: Any) -> list[np.ndarray]:
    arrays: list[np.ndarray] = []
    for player_masks in masks:
        for key in sorted(player_masks):
            arrays.append(np.asarray(player_masks[key], dtype=np.bool_).reshape(-1))
    return arrays


def _mask_stats(masks: Any) -> dict[str, Any]:
    per_key: dict[str, dict[str, Any]] = {}
    for key in sorted(masks[0]):
        values = np.stack(
            [np.asarray(player[key], dtype=np.bool_) for player in masks]
        )
        per_key[key] = {
            "shape_per_player": list(values.shape[1:]),
            "valid_total": int(values.sum()),
            "valid_per_player": values.reshape(PLAYERS, -1).sum(axis=1).tolist(),
        }
    return per_key


def run_backend(backend: str, steps: int, seed: int, warmup: int) -> dict[str, Any]:
    if backend == "python":
        from lobby.TFTLobby import TFTLobby

        factory = lambda: TFTLobby(seed=seed)
    else:
        from cpp_lobby_env import CppTFTLobbyWrapper

        factory = lambda: CppTFTLobbyWrapper(seed=seed)

    vec = LobbyVectorEnv([factory])
    reset_ms: list[float] = []
    step_ms: list[float] = []
    mask_ms: list[float] = []
    rewards_seen: list[float] = []
    rounds_seen: list[int] = []
    done_count = 0
    observation = None
    final_info: dict[str, Any] = {}

    try:
        start = time.perf_counter()
        observation = vec.reset()
        reset_ms.append((time.perf_counter() - start) * 1000)

        for index in range(warmup + steps):
            actions = [[PASS_ACTION[:] for _ in range(PLAYERS)]]

            start = time.perf_counter()
            obs, rewards, dones, infos = vec.step(actions)
            elapsed = (time.perf_counter() - start) * 1000

            start_masks = time.perf_counter()
            masks_by_lobby = vec.env_method("get_action_masks")
            mask_elapsed = (time.perf_counter() - start_masks) * 1000

            if index >= warmup:
                step_ms.append(elapsed)
                mask_ms.append(mask_elapsed)
                rewards_seen.extend(np.asarray(rewards).reshape(-1).astype(float).tolist())
                done_count += int(np.asarray(dones).sum())
                final_info = infos[0] if infos else {}
                rounds_seen.append(int(final_info.get("round", 0)))

            observation = obs

        masks = masks_by_lobby[0]
        metrics_by_lobby = vec.env_method("get_anti_loop_metrics")
        metrics = metrics_by_lobby[0] if metrics_by_lobby else {}
        strategies_by_lobby = vec.env_method("get_strategies")
        strategies = strategies_by_lobby[0] if strategies_by_lobby else []

        return {
            "backend": backend,
            "seed": seed,
            "steps": len(step_ms),
            "reset_ms": reset_ms[0],
            "step_latency": _summary(step_ms),
            "mask_latency": _summary(mask_ms),
            "observation_shape": list(np.asarray(observation).shape),
            "observation_mean": float(np.asarray(observation).mean()),
            "observation_std": float(np.asarray(observation).std()),
            "reward_mean": float(np.mean(rewards_seen)) if rewards_seen else 0.0,
            "reward_std": float(np.std(rewards_seen)) if rewards_seen else 0.0,
            "reward_sum": float(np.sum(rewards_seen)),
            "done_count": done_count,
            "round_min": min(rounds_seen, default=0),
            "round_max": max(rounds_seen, default=0),
            "mask_stats": _mask_stats(masks),
            "anti_loop_metrics": metrics,
            "strategy_counts": {
                str(getattr(item, "name", item)): sum(
                    1 for candidate in strategies
                    if getattr(candidate, "name", candidate) == getattr(item, "name", item)
                )
                for item in set(strategies)
            },
            "last_lobby_done": bool(final_info.get("lobby_done", False)),
        }
    finally:
        vec.close()


def compare(python_result: dict[str, Any], cpp_result: dict[str, Any]) -> dict[str, Any]:
    py_shape = python_result["observation_shape"]
    cpp_shape = cpp_result["observation_shape"]
    py_masks = python_result["mask_stats"]
    cpp_masks = cpp_result["mask_stats"]

    return {
        "observation_shape_equal": py_shape == cpp_shape,
        "observation_mean_delta_cpp_minus_python": (
            cpp_result["observation_mean"] - python_result["observation_mean"]
        ),
        "observation_std_delta_cpp_minus_python": (
            cpp_result["observation_std"] - python_result["observation_std"]
        ),
        "reward_mean_delta_cpp_minus_python": (
            cpp_result["reward_mean"] - python_result["reward_mean"]
        ),
        "reward_sum_delta_cpp_minus_python": (
            cpp_result["reward_sum"] - python_result["reward_sum"]
        ),
        "step_speedup_python_over_cpp": (
            python_result["step_latency"]["mean_ms"]
            / cpp_result["step_latency"]["mean_ms"]
            if cpp_result["step_latency"]["mean_ms"] > 0 else None
        ),
        "mask_shapes_equal": {
            key: py_masks.get(key, {}).get("shape_per_player")
            == cpp_masks.get(key, {}).get("shape_per_player")
            for key in sorted(set(py_masks) | set(cpp_masks))
        },
        "mask_valid_total_delta_cpp_minus_python": {
            key: cpp_masks.get(key, {}).get("valid_total", 0)
            - py_masks.get(key, {}).get("valid_total", 0)
            for key in sorted(set(py_masks) | set(cpp_masks))
        },
        "anti_loop_metrics": {
            "python": python_result["anti_loop_metrics"],
            "cpp": cpp_result["anti_loop_metrics"],
        },
        "note": (
            "Diferenças são sinalizadas para investigação; resultados iguais "
            "não são presumidos apenas por usar a mesma seed."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=500)
    parser.add_argument("--warmup", type=int, default=30)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="engine_backend_comparison.json")
    args = parser.parse_args()

    if args.steps <= 0 or args.warmup < 0:
        parser.error("--steps deve ser > 0 e --warmup deve ser >= 0")

    results = {}
    for backend in ("python", "cpp"):
        print(f"\nExecutando backend {backend.upper()}...")
        results[backend] = run_backend(
            backend=backend,
            steps=args.steps,
            seed=args.seed,
            warmup=args.warmup,
        )
        print(json.dumps(results[backend], ensure_ascii=False, indent=2))

    report = {
        "configuration": vars(args),
        "results": results,
        "comparison": compare(results["python"], results["cpp"]),
    }
    with open(args.output, "w", encoding="utf-8") as output:
        json.dump(report, output, ensure_ascii=False, indent=2)

    print("\n=== COMPARAÇÃO ===")
    print(json.dumps(report["comparison"], ensure_ascii=False, indent=2))
    print(f"\nRelatório salvo em: {args.output}")


if __name__ == "__main__":
    main()
