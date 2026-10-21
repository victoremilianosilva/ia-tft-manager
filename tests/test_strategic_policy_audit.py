"""Tests for the multi-seed strategic policy audit helpers."""
import numpy as np

from scripts.audit_strategic_policy import _action_dict, _json_masks, _player_gold


class _FakeLobby:
    def get_audit_snapshot(self):
        return {"players": [{"player_id": 0, "gold": 9}, {"player_id": 1, "gold": 20}]}

    def get_public_state(self):
        raise AssertionError("public state should not be needed when audit snapshot has gold")


class _PublicOnlyLobby:
    def get_audit_snapshot(self):
        return {"players": [{"player_id": 0, "hp": 100}]}

    def get_public_state(self):
        return {"players": [{"player_id": 0, "gold": 7}]}


def test_audit_reads_gold_before_and_after_from_native_snapshots():
    assert _player_gold(_FakeLobby()) == {0: 9, 1: 20}
    assert _player_gold(_PublicOnlyLobby()) == {0: 7}


def test_audit_action_serialization_keeps_all_action_components():
    assert _action_dict([5, 4, 8, 27, 6, 19]) == {
        "type": 5,
        "shop_slot": 4,
        "bench_slot": 8,
        "board_target": 27,
        "board_source": 6,
        "conditioned_board_target": 19,
    }


def test_audit_mask_serialization_preserves_exact_mask_values():
    result = _json_masks({
        "type_mask": np.array([1, 0, 1], dtype=np.float32),
        "shop_mask": np.array([0, 1], dtype=np.bool_),
    })
    assert result == {"type_mask": [1, 0, 1], "shop_mask": [0, 1]}
