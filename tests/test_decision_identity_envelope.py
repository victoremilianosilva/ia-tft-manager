"""Canonical Decision Identity v2 envelope tests."""
import hashlib
import json
import pytest
from decision_identity import build_player_identity_envelopes

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
