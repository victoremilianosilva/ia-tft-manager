"""Versioned PPO reward contract.

Reward v1 deliberately keeps action-level shaping neutral while the remaining
legacy composition-dependent signals lack a causal, calibrated contract.
Native PvP combat and one-time terminal placement remain the outcome rewards.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping

REWARD_CONTRACT_ID = "tft.ppo.outcome-reward.v1"
REWARD_CONTRACT_VERSION = 1

_REWARD_CONTRACT_PAYLOAD = {
    "contract_id": REWARD_CONTRACT_ID,
    "version": REWARD_CONTRACT_VERSION,
    "action_reward": {
        "mode": "neutral",
        "value": 0.0,
        "reason": "uncalibrated_action_shaping_disabled",
    },
    "combat_reward": {
        "owner": "TFTLobby::step",
        "source": "resolved_native_pvp_outcome",
        "credit": "once_per_player_per_resolved_pvp_round",
    },
    "placement_reward": {
        "owner": "TFTLobby::step",
        "source": "validated_final_placement",
        "credit": "once_per_player_when_placement_becomes_known",
        "formula": "1 - 2 * (placement - 1) / (lobby_size - 1)",
    },
    "invalid_transition": "contract_failure_not_player_reward",
    "temporal_credit": {
        "algorithm": "per_agent_gae",
        "validity_boundary": "invalid_transition_breaks_recursion",
    },
}


def _canonical_hash(payload: Mapping) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


REWARD_CONTRACT_HASH = _canonical_hash(_REWARD_CONTRACT_PAYLOAD)


def build_reward_checkpoint_contract() -> dict:
    return {
        "contract_id": REWARD_CONTRACT_ID,
        "version": REWARD_CONTRACT_VERSION,
        "sha256": REWARD_CONTRACT_HASH,
    }


def validate_reward_checkpoint_contract(manifest: Mapping) -> None:
    if not isinstance(manifest, Mapping):
        raise TypeError("reward_contract do checkpoint deve ser um mapping.")
    expected = build_reward_checkpoint_contract()
    if dict(manifest) != expected:
        raise ValueError(
            "reward_contract incompatível: "
            f"esperado {expected}, recebido {dict(manifest)}."
        )
