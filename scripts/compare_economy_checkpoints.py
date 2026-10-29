"""Paired-seed comparison of baseline and candidate TFT checkpoints.

Both checkpoints are evaluated on the same seeds and all eight players. This is
an evaluation/ablation harness; it does not train either checkpoint. Train the
candidate from the same starting checkpoint after changing reward shaping.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_audit(checkpoint: Path, seeds: str, max_steps: int, output: Path) -> None:
    command = [
        sys.executable, str(ROOT / "scripts" / "audit_native_ppo_loops.py"),
        "--checkpoint", str(checkpoint),
        "--seeds", seeds,
        "--max-steps", str(max_steps),
        "--output", str(output),
    ]
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def summarize(trace: Path, output: Path) -> dict:
    command = [
        sys.executable, str(ROOT / "scripts" / "summarize_economy_audit.py"),
        str(trace), "--output", str(output),
    ]
    subprocess.run(command, cwd=ROOT, check=True)
    return json.loads(output.read_text(encoding="utf-8"))


def numeric(value):
    return float(value) if isinstance(value, (int, float)) else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, type=Path,
                        help="Checkpoint before reward changes")
    parser.add_argument("--candidate", required=True, type=Path,
                        help="Checkpoint trained from the same starting checkpoint")
    parser.add_argument("--seeds", default="20261022,20261023")
    parser.add_argument("--max-steps", type=int, default=300)
    parser.add_argument("--output-dir", type=Path, default=Path("reports/economy_ablation"))
    args = parser.parse_args()
    for checkpoint in (args.baseline, args.candidate):
        if not checkpoint.is_file():
            parser.error(f"Checkpoint not found: {checkpoint}")
    if args.max_steps < 1:
        parser.error("--max-steps must be positive")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    baseline_trace = args.output_dir / "baseline.jsonl"
    candidate_trace = args.output_dir / "candidate.jsonl"
    baseline_summary_path = args.output_dir / "baseline_summary.json"
    candidate_summary_path = args.output_dir / "candidate_summary.json"

    run_audit(args.baseline, args.seeds, args.max_steps, baseline_trace)
    run_audit(args.candidate, args.seeds, args.max_steps, candidate_trace)
    baseline = summarize(baseline_trace, baseline_summary_path)
    candidate = summarize(candidate_trace, candidate_summary_path)

    def index(summary):
        return {(int(row["seed"]), int(row["player_id"])): row
                for row in summary.get("players", [])}

    b_rows, c_rows = index(baseline), index(candidate)
    comparisons = []
    metrics = (
        ("final.gold", lambda r: numeric((r.get("final") or {}).get("gold"))),
        ("final.level", lambda r: numeric((r.get("final") or {}).get("level"))),
        ("final.hp", lambda r: numeric((r.get("final") or {}).get("hp"))),
        ("final.board_composition_score",
         lambda r: numeric((r.get("final") or {}).get("board_composition_score"))),
        ("final.board_two_star_count",
         lambda r: numeric((r.get("final") or {}).get("board_two_star_count"))),
        ("buys", lambda r: numeric(r.get("buys"))),
        ("xp_buys", lambda r: numeric(r.get("xp_buys"))),
        ("sells", lambda r: numeric(r.get("sells"))),
        ("upgrade_steps_heuristic", lambda r: numeric(r.get("upgrade_steps_heuristic"))),
        ("confirmed_buy_sell_reversals_by_uuid",
         lambda r: numeric(r.get("confirmed_buy_sell_reversals_by_uuid"))),
        ("passes_with_50plus_gold", lambda r: numeric(r.get("passes_with_50plus_gold"))),
        ("economy_missed_progress_candidates",
         lambda r: numeric(r.get("economy_missed_progress_candidates"))),
        ("final.placement", lambda r: numeric((r.get("final") or {}).get("placement"))),
    )
    for key in sorted(set(b_rows) | set(c_rows)):
        b, c = b_rows.get(key), c_rows.get(key)
        item = {"seed": key[0], "player_id": key[1], "baseline_present": b is not None,
                "candidate_present": c is not None, "deltas": {}}
        for name, getter in metrics:
            bv, cv = getter(b) if b else None, getter(c) if c else None
            item["deltas"][name] = {
                "baseline": bv, "candidate": cv,
                "delta": (cv - bv) if bv is not None and cv is not None else None,
            }
        comparisons.append(item)

    all_seeds = sorted({key[0] for key in set(b_rows) | set(c_rows)})
    result = {
        "seeds": args.seeds,
        "max_steps": args.max_steps,
        "baseline_checkpoint": str(args.baseline),
        "candidate_checkpoint": str(args.candidate),
        "same_seed_and_player_pairing": True,
        "all_eight_players_present_for_each_seed": all(
            all((seed, player_id) in b_rows and (seed, player_id) in c_rows
                for player_id in range(8)) for seed in all_seeds
        ),
        "baseline_coverage": baseline.get("coverage"),
        "candidate_coverage": candidate.get("coverage"),
        "paired_player_comparisons": comparisons,
        "interpretation_note": (
            "Reward changes influence policy behavior only after training. "
            "For a meaningful candidate checkpoint, start from the same baseline "
            "checkpoint and train with the changed reward implementation."
        ),
    }
    output = args.output_dir / "paired_comparison.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Paired comparison written to {output}")
    print(json.dumps({
        "all_eight_players_present_for_each_seed": result["all_eight_players_present_for_each_seed"],
        "paired_player_comparisons": len(comparisons),
        "output": str(output),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
