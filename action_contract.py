"""Independent, immutable PPO action and action-mask contracts for v1.

This module owns semantic identities and canonical payload hashing. It does
not implement Engine legality; the native Engine remains the final authority.
"""
from __future__ import annotations

import hashlib
import json
from math import prod
from collections.abc import Mapping

import torch

ACTION_CONTRACT_ID = "tft.ppo-action.v1"
ACTION_CONTRACT_VERSION = 1
MASK_CONTRACT_ID = "tft.ppo-action-mask.v1"
MASK_CONTRACT_VERSION = 1
MASK_SNAPSHOT_HASH_ALGORITHM = "tft-action-mask-snapshot-v1"
CRITIC_MASK_INPUT_CONTRACT_ID = "tft.ppo-critic-mask-input.v1"
CRITIC_MASK_INPUT_CONTRACT_VERSION = 1
MASK_SHAPES = {
    "type_mask": (9,),
    "shop_mask": (5,),
    "bench_source_mask": (9,),
    "board_target_mask": (28,),
    "board_source_mask": (28,),
    "board_move_target_masks": (28, 28),
    "bench_move_source_mask": (9,),
    "bench_to_board_target_masks": (9, 28),
    "item_inventory_mask": (9,),
    "item_component_first_mask": (10,),
    "item_component_pair_masks": (10, 10),
    "item_target_mask": (37,),
}

CRITIC_MASK_EMBED_DIM = 64
CRITIC_MASK_FEATURE_DIM = sum(
    prod(shape) for shape in MASK_SHAPES.values()
)

ACTION_CONTRACT_PAYLOAD = {
    "contract_id": ACTION_CONTRACT_ID,
    "version": ACTION_CONTRACT_VERSION,
    "record": ["type", "shop_slot", "bench_slot", "board_target", "board_source", "board_move_target"],
    "record_dtype": "int64",
    "base_action_dims": [9, 5, 9, 28, 28, 28],
    "argument_head_dimensions": {
        "shop_slot": 5,
        "bench_slot": 9,
        "board_target": 28,
        "board_source": 28,
        "board_move_target": 28,
        "item_inventory": 9,
        "item_component_first": 10,
        "item_component_second": 10,
        "item_target": 37,
    },
    "actions": [
        {"id": 0, "name": "BUY", "arguments": {"shop_slot": 1}},
        {"id": 1, "name": "REROLL", "arguments": {}},
        {"id": 2, "name": "BUY_XP", "arguments": {}},
        {"id": 3, "name": "MOVE_BENCH", "arguments": {"bench_slot": 2, "board_target": 3}},
        {"id": 4, "name": "MOVE_BOARD", "arguments": {"board_source": 4, "board_move_target": 5}},
        {"id": 5, "name": "SELL", "arguments": {"bench_slot": 2}},
        {"id": 6, "name": "PASS", "arguments": {}},
        {"id": 7, "name": "EQUIP_FROM_INVENTORY", "arguments": {"inventory_slot": 1, "item_target": 2}},
        {"id": 8, "name": "CRAFT_AND_EQUIP", "arguments": {"first_component": 1, "second_component": 2, "item_target": 3}},
    ],
    "inactive_argument_policy": "zero",
}

MASK_CONTRACT_PAYLOAD = {
    "contract_id": MASK_CONTRACT_ID,
    "version": MASK_CONTRACT_VERSION,
    "fields": [{"name": name, "shape": list(shape)} for name, shape in MASK_SHAPES.items()],
    "conditional_rules": [
        {"action": "BUY", "mask": "shop_mask"},
        {"action": "SELL", "mask": "bench_source_mask"},
        {"action": "MOVE_BENCH", "source": "bench_move_source_mask", "target": "bench_to_board_target_masks[source, target]"},
        {"action": "MOVE_BOARD", "source": "board_source_mask", "target": "board_move_target_masks[source, target]"},
        {"action": "EQUIP_FROM_INVENTORY", "source": "item_inventory_mask", "target": "item_target_mask"},
        {"action": "CRAFT_AND_EQUIP", "first": "item_component_first_mask", "second": "item_component_pair_masks[first, second]", "target": "item_target_mask"},
    ],
}

def _canonical_hash(payload: Mapping) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

ACTION_CONTRACT_HASH = _canonical_hash(ACTION_CONTRACT_PAYLOAD)
MASK_CONTRACT_HASH = _canonical_hash(MASK_CONTRACT_PAYLOAD)

def build_action_mask_checkpoint_contract() -> dict:
    return {
        "manifest_version": 1,
        "action_contract": {"id": ACTION_CONTRACT_ID, "version": ACTION_CONTRACT_VERSION, "sha256": ACTION_CONTRACT_HASH},
        "mask_contract": {"id": MASK_CONTRACT_ID, "version": MASK_CONTRACT_VERSION, "sha256": MASK_CONTRACT_HASH},
    }

def validate_action_mask_checkpoint_contract(manifest: Mapping) -> None:
    if not isinstance(manifest, Mapping):
        raise TypeError("action_mask_contract do checkpoint deve ser um mapping.")
    if type(manifest.get("manifest_version")) is not int or manifest.get("manifest_version") != 1:
        raise ValueError("Versão do manifesto Action/Mask desconhecida.")
    expected = build_action_mask_checkpoint_contract()
    for section in ("action_contract", "mask_contract"):
        actual = manifest.get(section)
        if not isinstance(actual, Mapping) or dict(actual) != expected[section]:
            raise ValueError(f"{section} incompatível: esperado {expected[section]}, recebido {actual}.")

def build_critic_mask_input_checkpoint_contract() -> dict:
    """Identity for the Critic's independent, decision-correlated mask side input."""
    payload = {
        "contract_id": CRITIC_MASK_INPUT_CONTRACT_ID,
        "version": CRITIC_MASK_INPUT_CONTRACT_VERSION,
        "mask_contract": {
            "contract_id": MASK_CONTRACT_ID,
            "version": MASK_CONTRACT_VERSION,
            "sha256": MASK_CONTRACT_HASH,
        },
        "feature_order": [
            {
                "name": name,
                "shape": list(shape),
                "flatten_order": "C",
            }
            for name, shape in MASK_SHAPES.items()
        ],
        "input_encoding": "boolean_to_observation_dtype",
        "input_dim": CRITIC_MASK_FEATURE_DIM,
        "encoder": {
            "kind": "linear_tanh",
            "output_dim": CRITIC_MASK_EMBED_DIM,
            "initialization": "zero",
        },
        "critic_fusion": {
            "kind": "concatenate",
            "order": ["observation_latent", "mask_embedding"],
        },
        "actor_input": "unchanged",
    }
    return {
        "manifest_version": 1,
        "contract": payload,
        "sha256": _canonical_hash(payload),
    }


def validate_critic_mask_input_checkpoint_contract(manifest: Mapping) -> None:
    if not isinstance(manifest, Mapping):
        raise TypeError("critic_mask_input_contract do checkpoint deve ser um mapping.")
    expected = build_critic_mask_input_checkpoint_contract()
    if dict(manifest) != expected:
        raise ValueError(
            "critic_mask_input_contract incompatível: "
            f"esperado {expected}, recebido {manifest}."
        )


def hash_mask_row(mask_row: Mapping, mask_shapes: Mapping = MASK_SHAPES) -> str:
    if not isinstance(mask_row, Mapping) or set(mask_row) != set(mask_shapes):
        raise ValueError("Snapshot de masks deve conter exatamente os campos do contrato.")
    digest = hashlib.sha256()
    digest.update(b"tft-action-mask-snapshot-v1\\x00")
    for name, shape in mask_shapes.items():
        row = mask_row[name]
        if not isinstance(row, torch.Tensor):
            raise TypeError(f"Máscara '{name}' deve ser torch.Tensor.")
        if row.dtype != torch.bool:
            raise TypeError(f"Máscara '{name}' deve usar torch.bool.")
        if tuple(row.shape) != tuple(shape):
            raise ValueError(f"Shape inválido para máscara '{name}': {tuple(row.shape)}; esperado {tuple(shape)}.")
        canonical = row.detach().to(device="cpu").contiguous()
        digest.update(name.encode("utf-8"))
        digest.update(b"\\x00")
        digest.update(",".join(str(dim) for dim in shape).encode("ascii"))
        digest.update(b"\\x00")
        digest.update(canonical.numpy().tobytes(order="C"))
    return digest.hexdigest()

def hash_mask_rows(masks: Mapping, mask_shapes: Mapping = MASK_SHAPES) -> list[str]:
    if not isinstance(masks, Mapping) or set(masks) != set(mask_shapes):
        raise ValueError("Batch de masks deve conter exatamente os campos do contrato.")
    batch_size = None
    for name, shape in mask_shapes.items():
        tensor = masks[name]
        if not isinstance(tensor, torch.Tensor):
            raise TypeError(f"Máscara '{name}' deve ser torch.Tensor.")
        if tensor.dtype != torch.bool:
            raise TypeError(f"Máscara '{name}' deve usar torch.bool.")
        if tensor.ndim != len(shape) + 1 or tuple(tensor.shape[1:]) != tuple(shape):
            raise ValueError(f"Shape inválido para batch de máscara '{name}': {tuple(tensor.shape)}.")
        if batch_size is None:
            batch_size = int(tensor.shape[0])
        elif int(tensor.shape[0]) != batch_size:
            raise ValueError("Batch de masks desalinhado durante o hash.")
    return [
        hash_mask_row({name: masks[name][index] for name in mask_shapes}, mask_shapes)
        for index in range(batch_size or 0)
    ]
