"""Configuração central, validada e auditável do treinamento PPO."""
from __future__ import annotations

import os
from dataclasses import asdict, dataclass, fields
from typing import Any


@dataclass
class TrainingConfig:
    learning_rate: float = 3e-4
    min_learning_rate: float = 5e-5
    lr_schedule_updates: int = 1000
    adam_eps: float = 1e-5

    clip_coef: float = 0.2
    entropy_coef_initial: float = 0.02
    entropy_coef_final: float = 0.005
    entropy_decay_rate: float = 2.0
    entropy_schedule_updates: int = 1000
    vf_coef: float = 0.5
    max_grad_norm: float = 0.5
    target_kl: float | None = 0.02

    batch_size: int = 64
    ppo_epochs: int = 4
    rollout_steps: int = 128

    gamma: float = 0.99
    gae_lambda: float = 0.95

    checkpoint_path: str = "tft_checkpoint.pt"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def validate(self) -> None:
        for name in (
            "learning_rate", "adam_eps", "lr_schedule_updates",
            "entropy_schedule_updates", "batch_size", "ppo_epochs", "rollout_steps",
        ):
            if getattr(self, name) <= 0:
                raise ValueError(f"{name} deve ser > 0.")
        if not 0 <= self.min_learning_rate <= self.learning_rate:
            raise ValueError("min_learning_rate deve estar entre 0 e learning_rate.")
        if not 0 <= self.entropy_coef_final <= self.entropy_coef_initial:
            raise ValueError("entropy_coef_final deve estar entre 0 e entropy_coef_initial.")
        if self.entropy_decay_rate <= 0:
            raise ValueError("entropy_decay_rate deve ser > 0.")
        if not 0 < self.clip_coef < 1:
            raise ValueError("clip_coef deve estar entre 0 e 1.")
        if self.vf_coef < 0 or self.max_grad_norm <= 0:
            raise ValueError("vf_coef deve ser >= 0 e max_grad_norm deve ser > 0.")
        if self.target_kl is not None and self.target_kl <= 0:
            raise ValueError("target_kl deve ser > 0 ou None.")
        if not 0 <= self.gamma <= 1 or not 0 <= self.gae_lambda <= 1:
            raise ValueError("gamma e gae_lambda devem estar entre 0 e 1.")
        if not self.checkpoint_path.strip():
            raise ValueError("checkpoint_path não pode ser vazio.")

    @classmethod
    def from_env(cls, base: TrainingConfig | dict[str, Any] | None = None) -> TrainingConfig:
        if isinstance(base, cls):
            values = base.to_dict()
        elif isinstance(base, dict):
            values = dict(base)
        elif base is None:
            values = {}
        else:
            raise TypeError("config deve ser TrainingConfig, dict ou None.")
        allowed = {field.name for field in fields(cls)}
        unknown = set(values) - allowed
        if unknown:
            raise ValueError(f"Parâmetros desconhecidos: {sorted(unknown)}")
        config = cls(**values)

        env_fields = {
            "learning_rate": ("TFT_PPO_LR", float),
            "min_learning_rate": ("TFT_PPO_MIN_LR", float),
            "lr_schedule_updates": ("TFT_PPO_LR_SCHEDULE_UPDATES", int),
            "adam_eps": ("TFT_PPO_ADAM_EPS", float),
            "clip_coef": ("TFT_PPO_CLIP_COEF", float),
            "entropy_coef_initial": ("TFT_PPO_ENT_COEF", float),
            "entropy_coef_final": ("TFT_PPO_ENT_COEF_FINAL", float),
            "entropy_decay_rate": ("TFT_PPO_ENT_DECAY_RATE", float),
            "entropy_schedule_updates": ("TFT_PPO_ENT_SCHEDULE_UPDATES", int),
            "vf_coef": ("TFT_PPO_VF_COEF", float),
            "max_grad_norm": ("TFT_PPO_MAX_GRAD_NORM", float),
            "batch_size": ("TFT_PPO_BATCH_SIZE", int),
            "ppo_epochs": ("TFT_PPO_EPOCHS", int),
            "rollout_steps": ("TFT_ROLLOUT_STEPS", int),
            "gamma": ("TFT_PPO_GAMMA", float),
            "gae_lambda": ("TFT_PPO_GAE_LAMBDA", float),
        }
        for name, (env_name, converter) in env_fields.items():
            raw = os.getenv(env_name)
            if raw is not None and raw.strip():
                try:
                    setattr(config, name, converter(raw))
                except ValueError as exc:
                    raise ValueError(f"{env_name} inválido: {raw!r}") from exc

        raw_kl = os.getenv("TFT_PPO_TARGET_KL")
        if raw_kl is not None and raw_kl.strip():
            config.target_kl = None if raw_kl.strip().lower() in {"none", "off", "disabled"} else float(raw_kl)
        raw_checkpoint = os.getenv("TFT_CHECKPOINT_PATH")
        if raw_checkpoint:
            config.checkpoint_path = raw_checkpoint
        config.validate()
        return config
