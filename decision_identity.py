"""Canonical Decision Identity v2 envelope construction for native lobby rows.

The native Engine owns the Engine-instance token, episode counter, and both
sequence counters. This adapter composes those authoritative values; it does
not infer identity from seeds, timestamps, object addresses, or rollout order.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping

MAX_SAFE_JSON_INTEGER = (1 << 53) - 1

IDENTITY_VERSION = "tft.decision-identity.v2"
DECISION_NAMESPACE = "tft.engine.decision"
SNAPSHOT_NAMESPACE = "tft.engine.observation-snapshot"
IDENTITY_HASH_SCOPE = (
    "RFC8785-SHA256:v2:identity_version,match_id,engine_match_id,player_id,round,"
    "decision_sequence.namespace,decision_sequence.value,"
    "snapshot_sequence.namespace,snapshot_sequence.value"
)


def _canonical_identity_bytes(payload: Mapping[str, Any]) -> bytes:
    """Serialize the restricted identity payload using RFC 8785-compatible JSON.

    The hashed payload contains ASCII keys, strings, null, and non-negative
    integers only. Sorted compact UTF-8 JSON is canonical for this subset.
    """
    return json.dumps(
        dict(payload), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False,
    ).encode("utf-8")


def _identity_hash(payload: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical_identity_bytes(payload)).hexdigest()


def build_player_identity_envelopes(metadata: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Build one canonical v2 identity envelope per native player decision row."""
    engine_instance_id = metadata.get("engine_instance_id")
    episode_id = metadata.get("episode_id")
    snapshot_sequence = metadata.get("decision_sequence")
    player_sequences = metadata.get("player_decision_sequences")
    round_number = metadata.get("round")

    if not isinstance(engine_instance_id, str) or not engine_instance_id.strip():
        raise ValueError("engine_instance_id nativo ausente ou inválido")
    for name, value in (("episode_id", episode_id), ("decision_sequence", snapshot_sequence), ("round", round_number)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= MAX_SAFE_JSON_INTEGER:
            raise ValueError(f"{name} deve ser inteiro não negativo")
    if not isinstance(player_sequences, (list, tuple)) or len(player_sequences) != 8:
        raise ValueError("player_decision_sequences deve conter oito contadores")

    engine_match_id = f"{engine_instance_id}/episode/{episode_id}"
    snapshot_ref = {"namespace": SNAPSHOT_NAMESPACE, "value": snapshot_sequence}
    envelopes = []
    for player_id, decision_sequence in enumerate(player_sequences):
        if isinstance(decision_sequence, bool) or not isinstance(decision_sequence, int) or not 0 <= decision_sequence <= MAX_SAFE_JSON_INTEGER:
            raise ValueError(f"player_decision_sequences[{player_id}] deve ser inteiro não negativo")
        decision_ref = {"namespace": DECISION_NAMESPACE, "value": decision_sequence}
        hash_payload = {
            "identity_version": IDENTITY_VERSION,
            "match_id": None,
            "engine_match_id": engine_match_id,
            "player_id": f"player-{player_id}",
            "round": round_number,
            "decision_sequence": decision_ref,
            "snapshot_sequence": snapshot_ref,
        }
        envelopes.append({
            **hash_payload,
            "status": "complete",
            "decision_identity_hash": _identity_hash(hash_payload),
            "decision_identity_hash_scope": IDENTITY_HASH_SCOPE,
            "episode_id": episode_id,
        })
    return envelopes


def validate_player_identity_envelope(
    envelope: Mapping[str, Any], *, engine_instance_id: str, episode_id: int,
    snapshot_sequence: int, player_decision_sequence: int, player_id: int, round_number: int,
) -> None:
    """Reject an envelope that is not the exact canonical identity for a native row."""
    if isinstance(player_id, bool) or not isinstance(player_id, int) or not 0 <= player_id < 8:
        raise ValueError("player_id deve estar no intervalo nativo 0..7")
    expected = build_player_identity_envelopes({
        "engine_instance_id": engine_instance_id,
        "episode_id": episode_id,
        "decision_sequence": snapshot_sequence,
        "player_decision_sequences": [
            player_decision_sequence if index == player_id else 0 for index in range(8)
        ],
        "round": round_number,
    })[player_id]
    if dict(envelope) != expected:
        raise ValueError("envelope canônico diverge da identidade/sequence nativa")
