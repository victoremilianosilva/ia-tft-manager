"""Validated, scenario-balanced behavior replay for PPO."""
from __future__ import annotations

from pathlib import Path

import torch

from economy_finetuning.scenario_generator import SCENARIOS


class ReferenceReplayBuffer:
    MASK_SHAPES = {
        "type_mask": (9,), "shop_mask": (5,), "bench_source_mask": (9,),
        "board_target_mask": (28,), "board_source_mask": (28,),
        "board_move_target_masks": (28, 28), "bench_move_source_mask": (9,),
        "bench_to_board_target_masks": (9, 28), "item_inventory_mask": (9,),
        "item_component_first_mask": (10,), "item_component_pair_masks": (10, 10),
        "item_target_mask": (37,),
    }
    REQUIRED_MASKS = {
        "type_mask", "shop_mask", "bench_source_mask", "board_target_mask",
        "board_source_mask", "board_move_target_masks", "bench_move_source_mask",
        "bench_to_board_target_masks", "item_inventory_mask",
        "item_component_first_mask", "item_component_pair_masks", "item_target_mask",
    }

    def __init__(self, payload, device):
        if payload.get("schema_version") != 1:
            raise ValueError("Versão de replay não suportada; esperado schema_version=1.")
        self.device = torch.device(device)
        self.source_checkpoint_sha256 = payload.get("source_checkpoint_sha256")
        if not isinstance(self.source_checkpoint_sha256, str) or len(self.source_checkpoint_sha256) != 64:
            raise ValueError("Replay sem SHA-256 válido do checkpoint de referência.")
        self.observations = torch.as_tensor(payload["observations"], dtype=torch.float32, device=self.device)
        self.actions = torch.as_tensor(payload["actions"], dtype=torch.long, device=self.device)
        raw_masks = payload["masks"]
        missing = self.REQUIRED_MASKS - set(raw_masks)
        if missing:
            raise ValueError(f"Replay sem máscaras obrigatórias: {sorted(missing)}")
        self.masks = {key: torch.as_tensor(value, dtype=torch.bool, device=self.device) for key, value in raw_masks.items()}
        self.scenario_ids = payload["scenario_ids"]
        count = self.observations.shape[0]
        if self.observations.ndim != 2 or count == 0 or self.actions.shape != (count, 6) or len(self.scenario_ids) != count:
            raise ValueError("Replay vazio ou com shapes inconsistentes.")
        if not bool(torch.isfinite(self.observations).all()):
            raise ValueError("Replay contém observações NaN/Inf.")
        action_limits = (9, 5, 9, 28, 28, 28)
        if any(bool(((self.actions[:, index] < 0) | (self.actions[:, index] >= limit)).any()) for index, limit in enumerate(action_limits)):
            raise ValueError("Replay contém componentes de ação fora dos limites.")
        for key, shape in self.MASK_SHAPES.items():
            if key not in self.masks or tuple(self.masks[key].shape) != (count, *shape):
                raise ValueError(f"Shape de máscara inválido no replay: {key}")
        coverage = payload.get("scenario_counts", {})
        minimum = int(payload.get("minimum_per_scenario", 1))
        expected_scenarios = {item.scenario_id for item in SCENARIOS if item.trainable}
        missing_coverage = sorted(
            key for key in expected_scenarios
            if int(coverage.get(key, 0)) < minimum
        )
        if missing_coverage:
            raise ValueError(
                "Replay sem cobertura mínima para todos os cenários treináveis: "
                + ", ".join(missing_coverage)
                + ". Execute novamente o coletor com mais steps/seeds."
            )
        self.groups = {}
        for index, labels in enumerate(self.scenario_ids):
            for label in labels:
                self.groups.setdefault(str(label), []).append(index)
        self.groups = {key: values for key, values in self.groups.items() if values}
        if not self.groups:
            raise ValueError("Replay não contém cenários treináveis rotulados.")
        missing_groups = sorted(key for key in expected_scenarios if len(self.groups.get(key, [])) < minimum)
        if missing_groups:
            raise ValueError("Replay sem amostras rotuladas suficientes: " + ", ".join(missing_groups))
        self.labels = sorted(self.groups)

    @classmethod
    def load(cls, path: str | Path, device):
        source = Path(path).expanduser().resolve()
        if not source.is_file():
            raise FileNotFoundError(f"Replay de referência não encontrado: {source}")
        payload = torch.load(source, map_location="cpu", weights_only=False)
        if not isinstance(payload, dict):
            raise ValueError("Arquivo de replay deve conter um dicionário.")
        return cls(payload, device)

    def sample(self, batch_size: int) -> dict:
        if batch_size <= 0:
            raise ValueError("batch_size deve ser > 0.")
        selected = []
        for _ in range(batch_size):
            label_index = int(torch.randint(len(self.labels), (1,)).item())
            label = self.labels[label_index]
            group = self.groups[label]
            row_index = int(torch.randint(len(group), (1,)).item())
            selected.append(group[row_index])
        indices = torch.as_tensor(selected, dtype=torch.long, device=self.device)
        return {
            "obs": self.observations.index_select(0, indices),
            "actions": self.actions.index_select(0, indices),
            "masks": {key: value.index_select(0, indices) for key, value in self.masks.items()},
        }
