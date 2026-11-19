"""Canonical aggregate identity for PPO checkpoint lineages.

This manifest composes the independently owned contracts. It does not redefine
observation, action, mask, reward, catalog, or model semantics.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping

CHECKPOINT_LINEAGE_ID = "tft.ppo-checkpoint-lineage.v1"
CHECKPOINT_LINEAGE_VERSION = 1


def _canonical_hash(payload: Mapping) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _state_dict_signature(state_dict: Mapping) -> list[dict]:
    if not isinstance(state_dict, Mapping) or not state_dict:
        raise TypeError("policy state_dict deve ser um mapping não vazio.")
    signature = []
    for name, tensor in sorted(state_dict.items()):
        shape = getattr(tensor, "shape", None)
        dtype = getattr(tensor, "dtype", None)
        if shape is None or dtype is None:
            raise TypeError(f"Peso de policy inválido: {name}.")
        signature.append({
            "name": str(name),
            "shape": [int(value) for value in shape],
            "dtype": str(dtype),
        })
    return signature


def build_checkpoint_lineage_contract(
    policy_state_dict: Mapping,
    action_mask_contract: Mapping,
    critic_mask_input_contract: Mapping,
    semantic_state_contract: Mapping,
    reward_contract: Mapping,
) -> dict:
    components = {
        "action_mask_contract": dict(action_mask_contract),
        "critic_mask_input_contract": dict(critic_mask_input_contract),
        "semantic_state_contract": dict(semantic_state_contract),
        "reward_contract": dict(reward_contract),
    }
    payload = {
        "contract_id": CHECKPOINT_LINEAGE_ID,
        "version": CHECKPOINT_LINEAGE_VERSION,
        "components": components,
        "policy_state_signature": _state_dict_signature(policy_state_dict),
        "compatibility": {
            "tensor_shape_is_not_semantic_compatibility": True,
            "optimizer_restore_requires_exact_lineage": True,
            "legacy_artifacts_are_immutable_baselines": True,
        },
    }
    return {
        "manifest_version": 1,
        "contract": payload,
        "sha256": _canonical_hash(payload),
    }


def validate_checkpoint_lineage_contract(
    manifest: Mapping,
    policy_state_dict: Mapping,
    action_mask_contract: Mapping,
    critic_mask_input_contract: Mapping,
    semantic_state_contract: Mapping,
    reward_contract: Mapping,
) -> None:
    if not isinstance(manifest, Mapping):
        raise TypeError("checkpoint_contract deve ser um mapping.")
    expected = build_checkpoint_lineage_contract(
        policy_state_dict,
        action_mask_contract,
        critic_mask_input_contract,
        semantic_state_contract,
        reward_contract,
    )
    if dict(manifest) != expected:
        raise ValueError(
            "checkpoint lineage incompatível: "
            "componentes, assinatura estrutural ou hash não correspondem ao runtime."
        )
