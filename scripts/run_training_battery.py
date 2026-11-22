"""Run a reproducible multi-seed battery of fresh native PPO trainings."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys


def parse_seeds(value: str) -> list[int]:
    try:
        seeds = [int(part.strip()) for part in value.split(",") if part.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("seeds deve ser uma lista separada por vírgulas.") from exc
    if not seeds or any(not 0 <= seed <= 0xFFFFFFFF for seed in seeds) or len(set(seeds)) != len(seeds):
        raise argparse.ArgumentTypeError("Informe seeds únicas entre 0 e 2^32-1.")
    return seeds


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Executa treinos nativos independentes para cada seed."
    )
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--seeds", type=parse_seeds, default=parse_seeds("11,12,13"))
    parser.add_argument("--updates", type=int, default=160)
    parser.add_argument("--lobbies", type=int, default=4)
    parser.add_argument("--rollout-steps", type=int, default=128)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--ppo-epochs", type=int, default=4)
    args = parser.parse_args(argv)

    if min(args.updates, args.lobbies, args.rollout_steps, args.batch_size, args.ppo_epochs) <= 0:
        parser.error("updates, lobbies, rollout-steps, batch-size e ppo-epochs devem ser > 0.")

    output_root = Path(args.output_root).expanduser().resolve()
    if output_root.exists() and any(output_root.iterdir()):
        parser.error(f"O diretório {output_root} não está vazio; não sobrescrever execuções anteriores.")
    output_root.mkdir(parents=True, exist_ok=True)

    script = Path(__file__).resolve().parents[1] / "train_native.py"
    runs = []
    for seed in args.seeds:
        run_dir = output_root / f"seed-{seed}"
        command = [
            sys.executable, str(script),
            "--output-dir", str(run_dir),
            "--seed", str(seed),
            "--updates", str(args.updates),
            "--lobbies", str(args.lobbies),
            "--rollout-steps", str(args.rollout_steps),
            "--batch-size", str(args.batch_size),
            "--ppo-epochs", str(args.ppo_epochs),
        ]
        print("Executando:", " ".join(command), flush=True)
        subprocess.run(command, check=True)
        run_manifest_path = run_dir / "run_manifest.json"
        run_manifest = json.loads(run_manifest_path.read_text(encoding="utf-8"))
        runs.append({
            "seed": seed,
            "run_dir": run_dir.name,
            "checkpoint": f"{run_dir.name}/native_ppo_checkpoint.pt",
            "manifest": f"{run_dir.name}/run_manifest.json",
            "manifest_sha256": run_manifest["manifest_sha256"],
            "identity_sha256": run_manifest["identity_sha256"],
        })
        battery_manifest = {
            "manifest_id": "tft.ppo.native-training-battery",
            "version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "configuration": {
                "updates": args.updates,
                "lobbies": args.lobbies,
                "rollout_steps": args.rollout_steps,
                "batch_size": args.batch_size,
                "ppo_epochs": args.ppo_epochs,
            },
            "runs": runs,
        }
        (output_root / "battery_manifest.json").write_text(
            json.dumps(battery_manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(f"Bateria concluída: {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
