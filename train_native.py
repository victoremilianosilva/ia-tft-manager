"""Start one fresh, isolated PPO run on the native strategic architecture."""
from __future__ import annotations

import argparse
import os
from pathlib import Path


_CONFIG_ENV_KEYS = (
    "TFT_PPO_LR", "TFT_PPO_MIN_LR", "TFT_PPO_LR_SCHEDULE_UPDATES",
    "TFT_PPO_ADAM_EPS", "TFT_PPO_ADAM_BETA1", "TFT_PPO_ADAM_BETA2",
    "TFT_PPO_WEIGHT_DECAY", "TFT_PPO_CLIP_COEF", "TFT_PPO_ENT_COEF",
    "TFT_PPO_ENT_COEF_FINAL", "TFT_PPO_ENT_DECAY_RATE",
    "TFT_PPO_ENT_SCHEDULE_UPDATES", "TFT_PPO_VF_COEF",
    "TFT_PPO_MAX_GRAD_NORM", "TFT_PPO_TARGET_KL", "TFT_PPO_BATCH_SIZE",
    "TFT_PPO_EPOCHS", "TFT_ROLLOUT_STEPS", "TFT_NUM_LOBBIES",
    "TFT_TOTAL_UPDATES", "TFT_PPO_GAMMA", "TFT_PPO_GAE_LAMBDA",
    "TFT_TRAIN_SEED", "TFT_CHECKPOINT_PATH", "TFT_TRAIN_LOG_DIR",
    "TFT_RUN_MANIFEST_PATH",
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Executa um treino PPO novo, isolado e identificado pela arquitetura nativa."
    )
    parser.add_argument("--output-dir", required=True, help="Diretório novo e exclusivo desta execução.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--updates", type=int, default=1)
    parser.add_argument("--lobbies", type=int, default=1)
    parser.add_argument("--rollout-steps", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--ppo-epochs", type=int, default=4)
    parser.add_argument("--learning-rate", type=float, default=3e-4)
    parser.add_argument("--min-learning-rate", type=float, default=5e-5)
    parser.add_argument("--lr-schedule-updates", type=int, default=1000)
    parser.add_argument("--target-kl", type=float, default=0.02)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if not 0 <= args.seed <= 0xFFFFFFFF:
        raise SystemExit("--seed deve estar entre 0 e 2^32-1.")
    if min(args.updates, args.lobbies, args.rollout_steps, args.batch_size, args.ppo_epochs) <= 0:
        raise SystemExit("updates, lobbies, rollout-steps, batch-size e ppo-epochs devem ser > 0.")
    if args.learning_rate <= 0 or not 0 <= args.min_learning_rate <= args.learning_rate:
        raise SystemExit("Learning rates inválidos.")
    if args.lr_schedule_updates <= 0 or args.target_kl <= 0:
        raise SystemExit("lr-schedule-updates e target-kl devem ser > 0.")

    output_dir = Path(args.output_dir).expanduser().resolve()
    if output_dir.exists() and any(output_dir.iterdir()):
        raise SystemExit(
            f"O diretório {output_dir} já contém arquivos. "
            "Cada execução precisa de um diretório exclusivo; nenhum checkpoint será sobrescrito."
        )
    output_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_path = output_dir / "native_ppo_checkpoint.pt"
    log_dir = output_dir / "tensorboard"
    manifest_path = output_dir / "run_manifest.json"

    # This entrypoint always starts a new native lineage. It never imports old
    # optimizer state or enables historical checkpoint migration switches.
    for key in _CONFIG_ENV_KEYS:
        os.environ.pop(key, None)
    os.environ.setdefault(
        "TFT_OPGG_META_CATALOG",
        str(Path(__file__).resolve().parent / "data" / "opgg_tft_meta.json"),
    )
    os.environ["TFT_OPGG_DISABLE_REFRESH"] = "1"
    os.environ["TFT_TOTAL_UPDATES"] = str(args.updates)
    os.environ["TFT_NUM_LOBBIES"] = str(args.lobbies)
    os.environ["TFT_ROLLOUT_STEPS"] = str(args.rollout_steps)
    os.environ["TFT_PPO_BATCH_SIZE"] = str(args.batch_size)
    os.environ["TFT_PPO_EPOCHS"] = str(args.ppo_epochs)
    os.environ["TFT_PPO_LR"] = str(args.learning_rate)
    os.environ["TFT_PPO_MIN_LR"] = str(args.min_learning_rate)
    os.environ["TFT_PPO_LR_SCHEDULE_UPDATES"] = str(args.lr_schedule_updates)
    os.environ["TFT_PPO_TARGET_KL"] = str(args.target_kl)
    os.environ["TFT_TRAIN_SEED"] = str(args.seed)
    os.environ["TFT_CHECKPOINT_PATH"] = str(checkpoint_path)
    os.environ["TFT_TRAIN_LOG_DIR"] = str(log_dir)
    os.environ["TFT_RUN_MANIFEST_PATH"] = str(manifest_path)

    from trainer import Trainer

    trainer = Trainer(num_envs=args.lobbies, use_subprocess=False)
    trainer.train(total_updates=args.updates, rollout_steps=args.rollout_steps)

    if not checkpoint_path.is_file() or not manifest_path.is_file():
        raise RuntimeError("Treino terminou sem checkpoint e manifesto de execução.")
    print(f"Checkpoint: {checkpoint_path}")
    print(f"Manifesto:  {manifest_path}")
    print(f"TensorBoard: {log_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
