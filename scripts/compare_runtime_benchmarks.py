"""Compare independent runtime_benchmark.py reports from two revisions.

Example:
  python scripts/compare_runtime_benchmarks.py --baseline reports/main-1.json reports/main-2.json reports/main-3.json --candidate reports/pr-1.json reports/pr-2.json reports/pr-3.json
"""
from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path


def load_reports(paths: list[Path]) -> list[dict]:
    reports = []
    for path in paths:
        if not path.is_file():
            raise ValueError(f"Arquivo não encontrado: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("benchmark") != "native_ppo_inference_loop":
            raise ValueError(f"{path}: tipo de benchmark inesperado")
        reports.append(data)
    return reports


def compatible(reports: list[dict]) -> dict:
    keys = ("num_envs", "players_per_lobby", "warmup_iterations",
            "measured_iterations", "seed", "torch_threads", "device", "engine_backend")
    first = reports[0]["configuration"]
    mismatches = []
    for index, report in enumerate(reports[1:], start=2):
        diff = {key: (first.get(key), report["configuration"].get(key))
                for key in keys if first.get(key) != report["configuration"].get(key)}
        if diff:
            mismatches.append({"run": index, "differences": diff})
    if mismatches:
        raise ValueError("Configurações incompatíveis entre execuções: " + json.dumps(mismatches))
    return {key: first.get(key) for key in keys}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", nargs="+", type=Path, required=True,
                        help="JSONs do commit baseline; use várias execuções independentes.")
    parser.add_argument("--candidate", nargs="+", type=Path, required=True,
                        help="JSONs do commit candidato; use várias execuções independentes.")
    parser.add_argument("--output", type=Path, default=Path("reports/runtime_comparison.json"))
    args = parser.parse_args()
    try:
        base = load_reports(args.baseline)
        cand = load_reports(args.candidate)
        config = compatible(base + cand)
    except (ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if len(base) < 2 or len(cand) < 2:
        parser.error("Use pelo menos duas execuções independentes por revisão; três ou mais são recomendadas.")

    metrics = ("end_to_end", "mask_retrieval", "mask_flatten",
               "policy_and_action_conversion", "environment_step")
    result = {
        "schema_version": 1,
        "benchmark": "native_ppo_inference_loop_comparison",
        "configuration": config,
        "baseline_revisions": [r.get("revision") for r in base],
        "candidate_revisions": [r.get("revision") for r in cand],
        "runs": {"baseline": len(base), "candidate": len(cand)},
        "summary": {},
        "interpretation": (
            "Percentual de redução de latência positivo significa que a candidata é mais rápida. "
            "Speedup de throughput positivo significa maior throughput. Execuções repetidas no "
            "mesmo host reduzem, mas não eliminam, ruído ambiental; confirme também CI e testes."
        ),
    }
    for metric in metrics:
        bmed = [r["metrics"][metric]["median_ms"] for r in base]
        cmed = [r["metrics"][metric]["median_ms"] for r in cand]
        bp95 = [r["metrics"][metric]["p95_ms"] for r in base]
        cp95 = [r["metrics"][metric]["p95_ms"] for r in cand]
        b = statistics.median(bmed)
        c = statistics.median(cmed)
        b95 = statistics.median(bp95)
        c95 = statistics.median(cp95)
        result["summary"][metric] = {
            "baseline_median_of_run_medians_ms": b,
            "candidate_median_of_run_medians_ms": c,
            "latency_reduction_percent": ((b - c) / b * 100.0) if b else None,
            "baseline_median_of_run_p95_ms": b95,
            "candidate_median_of_run_p95_ms": c95,
            "p95_latency_reduction_percent": ((b95 - c95) / b95 * 100.0) if b95 else None,
            "baseline_run_medians_ms": bmed,
            "candidate_run_medians_ms": cmed,
        }
    bthrough = [r["throughput"]["agents_per_second_from_median"] for r in base]
    cthrough = [r["throughput"]["agents_per_second_from_median"] for r in cand]
    b = statistics.median(bthrough)
    c = statistics.median(cthrough)
    result["throughput_agents_per_second"] = {
        "baseline_median": b,
        "candidate_median": c,
        "speedup_percent": ((c - b) / b * 100.0) if b else None,
        "baseline_runs": bthrough,
        "candidate_runs": cthrough,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Comparação: {args.output}")
    for name, values in result["summary"].items():
        print(f"{name}: redução latência mediana={values['latency_reduction_percent']:.2f}%"
              if values["latency_reduction_percent"] is not None else f"{name}: n/a")
    print(f"Throughput: speedup={result['throughput_agents_per_second']['speedup_percent']:.2f}%"
          if result["throughput_agents_per_second"]["speedup_percent"] is not None else "Throughput: n/a")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
