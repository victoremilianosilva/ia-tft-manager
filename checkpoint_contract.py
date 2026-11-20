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


TRAINING_RESUME_CONTRACT_ID = "tft.ppo-training-resume.v1"
TRAINING_RESUME_CONTRACT_VERSION = 1
ROLLOUT_TEMPORAL_CONTRACT_ID = "tft.ppo-trajectory-validity.v1"


def build_training_resume_contract(training_config: Mapping) -> dict:
    """Bind the settings that determine optimizer and temporal training continuity."""
    if not isinstance(training_config, Mapping):
        raise TypeError("training_config deve ser um mapping.")
    semantic_config = {
        str(key): value
        for key, value in training_config.items()
        if key not in {"checkpoint_path", "total_updates"}
    }
    payload = {
        "contract_id": TRAINING_RESUME_CONTRACT_ID,
        "version": TRAINING_RESUME_CONTRACT_VERSION,
        "training_config": semantic_config,
        "optimizer": "torch.optim.Adam",
        "scheduler": "cosine_clamped",
        "rollout_temporal_contract": {
            "contract_id": ROLLOUT_TEMPORAL_CONTRACT_ID,
            "version": 1,
            "trajectory_valid": "controls_td_error_and_gae_continuity",
            "optimization_valid": "controls_ppo_loss_and_advantage_normalization",
            "invalid_trajectory": "zero_td_error_and_hard_recursion_boundary",
            "termination": "disable_bootstrap_and_recursion",
            "rollout_truncation": "bootstrap_from_valid_correlated_next_state_only",
        },
    }
    return {"manifest_version": 1, "contract": payload, "sha256": _canonical_hash(payload)}


def validate_training_resume_contract(manifest: Mapping, training_config: Mapping) -> bool:
    """Validate manifest integrity and report whether it matches this run's settings."""
    if not isinstance(manifest, Mapping):
        raise TypeError("training_resume_contract deve ser um mapping.")
    if type(manifest.get("manifest_version")) is not int or manifest.get("manifest_version") != 1:
        raise ValueError("Versão do training_resume_contract desconhecida.")
    payload = manifest.get("contract")
    if not isinstance(payload, Mapping):
        raise TypeError("training_resume_contract.contract deve ser um mapping.")
    if manifest.get("sha256") != _canonical_hash(payload):
        raise ValueError("Hash do training_resume_contract inválido.")
    return dict(manifest) == build_training_resume_contract(training_config)
