"""Offline, fail-closed attribution and calibration gates for action outcomes.

This module deliberately does not emit PPO rewards. It creates auditable
attribution candidates from native events; coefficients can only be approved
by a separate replay experiment with immutable train/validation/test manifests.
"""
from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from typing import Any


CONTRACT_ID = "tft.reward-causal-attribution.v1"
# Horizons are measured in the acting player's decision sequence, not wall time.
# They bound candidate discovery; they are not claims that an effect lasts this long.
FAMILY_POLICIES = {
    "purchase": {"max_decision_gap": 2, "outcomes": ("combat", "placement")},
    "reroll": {"max_decision_gap": 1, "outcomes": ("combat", "placement")},
    "xp_purchase": {"max_decision_gap": 2, "outcomes": ("combat", "placement")},
    "deploy": {"max_decision_gap": 1, "outcomes": ("combat", "placement")},
    "positioning": {"max_decision_gap": 1, "outcomes": ("combat", "placement")},
    "sale": {"max_decision_gap": 1, "outcomes": ("combat", "placement")},
    "item_action": {"max_decision_gap": 2, "outcomes": ("combat", "placement")},
}
_NON_ACTION_FAMILIES = {"pass"}


def _identity(record: Mapping[str, Any]) -> tuple[str, int, int]:
    engine = str(record.get("engine_instance_id", "")).strip()
    episode = record.get("episode_id")
    player = record.get("player_id")
    if not engine or isinstance(episode, bool) or not isinstance(episode, int) or episode < 0:
        raise ValueError("Identidade Engine/episódio inválida.")
    if isinstance(player, bool) or not isinstance(player, int) or not 0 <= player < 8:
        raise ValueError("player_id inválido.")
    return engine, episode, player


def _sequence(record: Mapping[str, Any], key: str) -> int:
    value = record.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{key} inválida.")
    return value


def build_attribution_candidates(
    *, action_events: Sequence[Mapping[str, Any]],
    outcome_events: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Return exclusive action→outcome candidates; ambiguous cases fail closed.

    Any later non-PASS action by the same player inside the candidate horizon
    invalidates attribution. Outcomes remain owned by their native combat or
    terminal-placement event; this function never duplicates or moves reward.
    """
    if not isinstance(action_events, Sequence) or not isinstance(outcome_events, Sequence):
        raise TypeError("Coleções de eventos são obrigatórias.")
    actions = []
    for event in action_events:
        if not isinstance(event, Mapping):
            raise ValueError("Action event inválido.")
        if event.get("contract_id") != "tft.reward-action-outcome.v1":
            raise ValueError("Contrato de action event não suportado.")
        if event.get("causal_attribution") != "not_established" or event.get("reward_eligible") is not False:
            raise ValueError("Action event já contém decisão de atribuição/reward.")
        family = event.get("action", {}).get("family")
        if family not in FAMILY_POLICIES and family not in _NON_ACTION_FAMILIES:
            raise ValueError(f"Família sem política causal: {family!r}.")
        if event.get("action", {}).get("handler_applied") is not True:
            continue
        _identity(event)
        _sequence(event.get("source_decision", {}), "player_decision_sequence")
        _sequence(event.get("outcome_snapshot", {}), "player_decision_sequence")
        actions.append(event)

    outcomes = []
    for event in outcome_events:
        if not isinstance(event, Mapping):
            raise ValueError("Outcome event inválido.")
        if event.get("source") not in ("native_pvp_resolution", "validated_terminal_placement"):
            raise ValueError("Outcome sem produtor nativo aceito.")
        _identity(event)
        if not isinstance(event.get("reward"), (int, float)) or isinstance(event.get("reward"), bool):
            raise ValueError("Outcome reward inválido.")
        if not math.isfinite(float(event["reward"])):
            raise ValueError("Outcome reward não finito.")
        outcomes.append(event)

    results = []
    for outcome in outcomes:
        identity = _identity(outcome)
        outcome_seq = _sequence(outcome, "player_decision_sequence")
        kind = "combat" if outcome["source"] == "native_pvp_resolution" else "placement"
        prior = [
            action for action in actions
            if _identity(action) == identity
            and _sequence(action.get("source_decision", {}), "player_decision_sequence") < outcome_seq
            and action.get("action", {}).get("family") in FAMILY_POLICIES
            and kind in FAMILY_POLICIES[action["action"]["family"]]["outcomes"]
            and 0 < outcome_seq - _sequence(action["source_decision"], "player_decision_sequence")
                <= FAMILY_POLICIES[action["action"]["family"]]["max_decision_gap"]
        ]
        if len(prior) == 1:
            selected = prior[0]
            source_seq = _sequence(selected["source_decision"], "player_decision_sequence")
            intervening = [
                action for action in actions
                if _identity(action) == identity
                and source_seq < _sequence(action["source_decision"], "player_decision_sequence") < outcome_seq
                and action is not selected
                and action["action"]["family"] not in _NON_ACTION_FAMILIES
            ]
        else:
            selected = None
            intervening = []
        if selected is not None and not intervening:
            results.append({
                "contract_id": CONTRACT_ID,
                "outcome_event_id": outcome.get("event_id"),
                "action_event_id": selected.get("event_id"),
                "attribution": "exclusive_candidate",
                "causal_attribution": "candidate_not_proven",
                "decision_gap": outcome_seq - _sequence(selected["source_decision"], "player_decision_sequence"),
                "horizon": FAMILY_POLICIES[selected["action"]["family"]]["max_decision_gap"],
                "reward_moved": False,
                "reward": None,
                "reason": "single_action_without_intervening_non_pass_action",
            })
        else:
            results.append({
                "contract_id": CONTRACT_ID,
                "outcome_event_id": outcome.get("event_id"),
                "action_event_id": None,
                "attribution": "ambiguous" if prior else "unattributed",
                "causal_attribution": "not_established",
                "decision_gap": None,
                "horizon": None,
                "reward_moved": False,
                "reward": None,
                "reason": "multiple_or_intervening_actions" if prior else "no_action_in_family_horizon",
            })
    return results



def extract_native_outcome_events(reward_audit: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Normalize native combat/placement audit records for attribution analysis."""
    if not isinstance(reward_audit, Mapping):
        raise TypeError("Reward audit deve ser um objeto.")
    if reward_audit.get("contract_id") != "tft.ppo.reward-audit.v1":
        raise ValueError("Reward audit contract não suportado.")
    engine = str(reward_audit.get("engine_instance_id", "")).strip()
    episode = reward_audit.get("episode_id")
    rows = reward_audit.get("player_rewards")
    if not engine or isinstance(episode, bool) or not isinstance(episode, int):
        raise ValueError("Identidade do reward audit inválida.")
    if not isinstance(rows, Sequence) or len(rows) != 8:
        raise ValueError("Reward audit deve conter oito jogadores.")
    result = []
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("Player reward audit inválido.")
        player_id = row.get("player_id")
        sequence = row.get("outcome_player_decision_sequence")
        if isinstance(player_id, bool) or not isinstance(player_id, int):
            raise ValueError("player_id inválido no reward audit.")
        if isinstance(sequence, bool) or not isinstance(sequence, int):
            raise ValueError("Sequência de outcome inválida no reward audit.")
        for key in ("combat_outcome", "terminal_placement"):
            outcome = row.get(key)
            if outcome is None:
                continue
            if not isinstance(outcome, Mapping):
                raise ValueError("Outcome nativo inválido no reward audit.")
            result.append({
                "event_id": outcome.get("event_id"),
                "engine_instance_id": engine,
                "episode_id": episode,
                "player_id": player_id,
                "player_decision_sequence": sequence,
                "source": outcome.get("source"),
                "reward": outcome.get("reward"),
                "combat_sequence": outcome.get("combat_sequence"),
                "placement": outcome.get("placement"),
            })
    return result


def validate_calibration_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Validate evidence prerequisites; never fit or approve coefficients."""
    if not isinstance(manifest, Mapping):
        raise TypeError("Calibration manifest deve ser um objeto.")
    required = (
        "dataset_hash", "code_revision", "engine_revision", "catalog_hash",
        "train_episode_ids", "validation_episode_ids", "test_episode_ids",
        "seed_manifest_hash", "pre_registered_hypothesis",
        "baseline_report_hash", "candidate_report_hash", "ablation_report_hash",
    )
    missing = [key for key in required if not manifest.get(key)]
    if missing:
        raise ValueError("Calibration sem evidência obrigatória: " + ", ".join(missing))
    splits = [set(manifest[key]) for key in
              ("train_episode_ids", "validation_episode_ids", "test_episode_ids")]
    if any(not split for split in splits):
        raise ValueError("Train/validation/test não podem ser vazios.")
    if splits[0] & splits[1] or splits[0] & splits[2] or splits[1] & splits[2]:
        raise ValueError("Episodes de train/validation/test se sobrepõem.")
    return {
        "contract_id": "tft.reward-calibration-evidence.v1",
        "status": "evidence_complete_pending_statistical_review",
        "coefficients_approved": False,
        "reward_activation_allowed": False,
        "missing": [],
    }
