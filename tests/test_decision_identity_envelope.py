"""Canonical Decision Identity v2 envelope tests."""
import hashlib
import json
import pytest
from decision_identity import build_player_identity_envelopes, _identity_hash

def test_adapter_builds_scoped_per_player_identity_and_separate_sequences():
    envelopes = build_player_identity_envelopes({
        "engine_instance_id": "engine-uuid-a",
        "episode_id": 3,
        "decision_sequence": 41,
        "player_decision_sequences": [101, 102, 103, 104, 105, 106, 107, 108],
        "round": 7,
    })
    assert len(envelopes) == 8
    envelope = envelopes[2]
    assert envelope["engine_match_id"] == "engine-uuid-a/episode/3"
    assert envelope["player_id"] == "player-2"
    assert envelope["decision_sequence"] == {"namespace": "tft.engine.decision", "value": 103}
    assert envelope["snapshot_sequence"] == {"namespace": "tft.engine.observation-snapshot", "value": 41}
    assert envelope["status"] == "complete"
    assert envelope["decision_identity_hash"].startswith("sha256:")

@pytest.mark.parametrize("bad", [True, -1, 1.5, "4", None])
def test_adapter_rejects_invalid_player_sequence(bad):
    with pytest.raises(ValueError):
        build_player_identity_envelopes({
            "engine_instance_id": "engine-uuid-a", "episode_id": 3,
            "decision_sequence": 41, "player_decision_sequences": [bad] + [1] * 7,
            "round": 7,
        })

def test_hash_implementation_matches_repository_rfc8785_vector():
    payload = {
        "identity_version": "tft.decision-identity.v2",
        "match_id": "match-001",
        "engine_match_id": "engine-match-001",
        "player_id": "player-2",
        "round": 12,
        "decision_sequence": {"namespace": "tft.engine.decision", "value": 184},
        "snapshot_sequence": {"namespace": "tft.engine.observation-snapshot", "value": 184},
    }
    assert _identity_hash(payload) == "sha256:db10775d5ce64a663a883591ba0303cf5da362b5b7719577216c0a0851d0c3bf"
