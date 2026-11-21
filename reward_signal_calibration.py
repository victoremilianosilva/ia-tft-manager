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
    action_ids = set()
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
        event_id = str(event.get("event_id", "")).strip()
        if not event_id or event_id in action_ids:
            raise ValueError("Action event_id ausente ou duplicado.")
        action_ids.add(event_id)
        if event.get("action", {}).get("handler_applied") is not True:
            continue
        _identity(event)
        _sequence(event.get("source_decision", {}), "player_decision_sequence")
        _sequence(event.get("outcome_snapshot", {}), "player_decision_sequence")
        actions.append(event)

    outcomes = []
    outcome_ids = set()
    for event in outcome_events:
        if not isinstance(event, Mapping):
            raise ValueError("Outcome event inválido.")
        if event.get("source") not in ("native_pvp_resolution", "validated_terminal_placement"):
            raise ValueError("Outcome sem produtor nativo aceito.")
        _identity(event)
        event_id = str(event.get("event_id", "")).strip()
        if not event_id or event_id in outcome_ids:
            raise ValueError("Outcome event_id ausente ou duplicado.")
        outcome_ids.add(event_id)
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


def analyze_action_lifecycles(*, action_events, outcome_events=(), pivot_lookahead=3):
    """Audit delayed outcomes, purchase reversals and pivot evidence without reward shaping."""
    if isinstance(pivot_lookahead, bool) or not isinstance(pivot_lookahead, int) or pivot_lookahead < 1:
        raise ValueError("pivot_lookahead inválido.")
    if not isinstance(action_events, Sequence) or not isinstance(outcome_events, Sequence):
        raise TypeError("Coleções de eventos são obrigatórias.")
    actions, action_ids = [], set()
    for event in action_events:
        if not isinstance(event, Mapping) or event.get("contract_id") != "tft.reward-action-outcome.v1":
            raise ValueError("Action event inválido para lifecycle audit.")
        event_id = str(event.get("event_id", "")).strip()
        if not event_id or event_id in action_ids:
            raise ValueError("Action event_id ausente ou duplicado.")
        action_ids.add(event_id)
        identity = _identity(event)
        family = event.get("action", {}).get("family")
        if family not in FAMILY_POLICIES and family not in _NON_ACTION_FAMILIES:
            raise ValueError(f"Família sem política causal: {family!r}.")
        source_seq = _sequence(event.get("source_decision", {}), "player_decision_sequence")
        outcome_seq = _sequence(event.get("outcome_snapshot", {}), "player_decision_sequence")
        if outcome_seq <= source_seq:
            raise ValueError("Outcome snapshot não sucede a decisão de origem.")
        if event.get("causal_attribution") != "not_established" or event.get("reward_eligible") is not False:
            raise ValueError("Lifecycle audit aceita somente eventos neutros.")
        actions.append((identity, source_seq, event))
    actions.sort(key=lambda row: (row[0], row[1]))
    if len({(identity, seq) for identity, seq, _ in actions}) != len(actions):
        raise ValueError("Mais de um action event para a mesma decisão/jogador.")
    outcomes, outcome_ids = [], set()
    for event in outcome_events:
        if not isinstance(event, Mapping) or event.get("source") not in ("native_pvp_resolution", "validated_terminal_placement"):
            raise ValueError("Outcome sem produtor nativo aceito.")
        identity = _identity(event)
        event_id = str(event.get("event_id", "")).strip()
        if not event_id or event_id in outcome_ids:
            raise ValueError("Outcome event_id ausente ou duplicado.")
        outcome_ids.add(event_id)
        seq = _sequence(event, "player_decision_sequence")
        reward = event.get("reward")
        if isinstance(reward, bool) or not isinstance(reward, (int, float)) or not math.isfinite(float(reward)):
            raise ValueError("Outcome reward inválido.")
        outcomes.append((identity, seq, event))
    acquisitions, reversals, pivots, delayed = {}, [], [], []
    for identity, seq, event in actions:
        family, facts = event["action"]["family"], event.get("facts", {})
        if not isinstance(facts, Mapping):
            raise ValueError("Facts inválidos no action event.")
        if family == "purchase" and event["action"].get("handler_applied") is True:
            for unit in facts.get("units_added", []) or []:
                if not isinstance(unit, Mapping) or not str(unit.get("uuid", "")).strip():
                    raise ValueError("Aquisição sem UUID físico.")
                uuid = str(unit["uuid"])
                acquisition_key = (identity, uuid)
                if acquisition_key in acquisitions:
                    raise ValueError("UUID físico adquirido mais de uma vez sem transição explícita.")
                acquisitions[acquisition_key] = {"identity": identity, "sequence": seq, "event_id": event["event_id"],
                    "champion_id": str(unit.get("champion_id", ""))}
        if family == "sale" and event["action"].get("handler_applied") is True:
            removed, sold_champions = facts.get("units_removed", []) or [], set()
            for unit in removed:
                if not isinstance(unit, Mapping):
                    raise ValueError("Unidade removida inválida.")
                champion = str(unit.get("champion_id", ""))
                if champion:
                    sold_champions.add(champion)
                acquired = acquisitions.get((identity, str(unit.get("uuid", ""))))
                if acquired and acquired["identity"] == identity and seq > acquired["sequence"]:
                    reversals.append({"contract_id": "tft.reward-action-lifecycle.v1", "kind": "purchase_reversed_by_sale",
                        "source_action_event_id": acquired["event_id"], "reversal_action_event_id": event["event_id"],
                        "unit_uuid": str(unit["uuid"]), "champion_id": acquired["champion_id"],
                        "decision_gap": seq-acquired["sequence"], "causal_attribution": "not_established", "reward": None})
            if sold_champions:
                for candidate_identity, candidate_seq, candidate in actions:
                    if candidate_identity != identity or not seq < candidate_seq <= seq + pivot_lookahead:
                        continue
                    if candidate["action"]["family"] != "purchase" or candidate["action"].get("handler_applied") is not True:
                        continue
                    added_champions = sorted({str(unit.get("champion_id", "")) for unit in
                        (candidate.get("facts", {}).get("units_added", []) or [])
                        if isinstance(unit, Mapping) and str(unit.get("champion_id", ""))})
                    changed = [champion for champion in added_champions if champion and champion not in sold_champions]
                    if changed:
                        pivots.append({"contract_id": "tft.reward-action-lifecycle.v1", "kind": "pivot_candidate",
                            "sale_event_id": event["event_id"], "later_purchase_event_id": candidate["event_id"],
                            "sold_champions": sorted(sold_champions), "new_champions": changed,
                            "decision_gap": candidate_seq-seq, "causal_attribution": "not_established", "reward": None})
                        break
    for identity, seq, event in actions:
        family = event["action"]["family"]
        if family not in FAMILY_POLICIES:
            continue
        for outcome_identity, outcome_seq, outcome in outcomes:
            gap = outcome_seq-seq
            if outcome_identity == identity and 0 < gap <= FAMILY_POLICIES[family]["max_decision_gap"]:
                delayed.append({"contract_id": "tft.reward-action-lifecycle.v1", "action_event_id": event["event_id"],
                    "outcome_event_id": outcome["event_id"], "action_family": family, "decision_gap": gap,
                    "horizon": FAMILY_POLICIES[family]["max_decision_gap"], "status": "temporal_candidate_only",
                    "causal_attribution": "not_established", "reward": None, "reward_moved": False})
    return {"contract_id": "tft.reward-action-lifecycle.v1", "status": "audit_only",
        "delayed_outcome_candidates": delayed, "reversals": reversals, "pivot_candidates": pivots,
        "reward_moved": False, "reward": None}


def audit_reward_hacking_patterns(action_events):
    """Flag adversarial action loops for tests/review; never creates a score or penalty."""
    if not isinstance(action_events, Sequence):
        raise TypeError("Action events devem ser uma sequência.")
    rows, seen = [], set()
    for event in action_events:
        if not isinstance(event, Mapping) or event.get("contract_id") != "tft.reward-action-outcome.v1":
            raise ValueError("Action event inválido para reward-hacking audit.")
        event_id = str(event.get("event_id", "")).strip()
        if not event_id or event_id in seen:
            raise ValueError("Action event_id ausente ou duplicado.")
        seen.add(event_id)
        if event.get("action", {}).get("handler_applied") is not True:
            continue
        identity = _identity(event)
        seq = _sequence(event.get("source_decision", {}), "player_decision_sequence")
        family = event.get("action", {}).get("family")
        if family not in FAMILY_POLICIES and family not in _NON_ACTION_FAMILIES:
            raise ValueError(f"Família sem política causal: {family!r}.")
        rows.append((identity, seq, family, event))
    rows.sort(key=lambda row: (row[0], row[1]))
    findings = []
    for identity, seq, family, event in rows:
        window = [row for row in rows if row[0] == identity and seq-3 <= row[1] <= seq]
        pattern = None
        if family == "reroll" and sum(row[2] == "reroll" for row in window) >= 3:
            pattern = "repeated_reroll_farming_candidate"
        elif family == "positioning" and sum(row[2] == "positioning" for row in window) >= 3:
            pattern = "repeated_positioning_farming_candidate"
        elif family == "pass" and sum(row[2] == "pass" for row in window) >= 4:
            pattern = "pass_streak_candidate"
        if pattern:
            findings.append({"contract_id": "tft.reward-hacking-audit.v1", "pattern": pattern,
                "engine_instance_id": identity[0], "episode_id": identity[1], "player_id": identity[2],
                "through_decision_sequence": seq, "trigger_event_id": event["event_id"],
                "status": "synthetic_pattern_detected_not_reward", "reward": None, "reward_moved": False})
    return findings
