"""Unit tests for the native PPO loop audit's mask and state accounting."""
import numpy as np

from scripts.audit_native_ppo_loops import (
    _effect_for_action,
    _mask_allows,
    _signature,
)


def _masks():
    return {
        "type_mask": np.array([0, 0, 0, 0, 1, 0, 1], dtype=np.bool_),
        "shop_mask": np.zeros(5, dtype=np.bool_),
        "bench_source_mask": np.zeros(9, dtype=np.bool_),
        "board_source_mask": np.array([False] * 3 + [True] + [False] * 24),
        "board_move_target_masks": np.zeros((28, 28), dtype=np.bool_),
        "bench_move_source_mask": np.zeros(9, dtype=np.bool_),
        "bench_to_board_target_masks": np.zeros((9, 28), dtype=np.bool_),
    }


def _player(board=None, bench=None, gold=10):
    empty = {"occupied": False, "champion_id": "", "uuid": "", "star": 0}
    return {
        "gold": gold,
        "xp": 0,
        "board": list(board or [dict(empty) for _ in range(28)]),
        "bench": list(bench or [dict(empty) for _ in range(9)]),
        "shop": [],
    }


def test_native_audit_rejects_a_selected_reverse_move_when_native_mask_disables_it():
    masks = _masks()
    masks["board_move_target_masks"][3, 10] = True
    action = [4, 0, 0, 10, 3, 10]
    assert _mask_allows(action, masks)

    reverse = [4, 0, 0, 3, 10, 3]
    assert not _mask_allows(reverse, masks)


def test_native_audit_signature_includes_board_bench_slot_identity_and_star():
    state_a = _player()
    state_b = _player()
    state_a["board"][3] = {
        "occupied": True, "champion_id": "Nasus", "uuid": "n-1", "star": 1
    }
    state_b["board"][3] = dict(state_a["board"][3])
    assert _signature(state_a) == _signature(state_b)

    state_b["board"][3]["star"] = 2
    assert _signature(state_a) != _signature(state_b)
    state_b["board"][3]["star"] = 1
    state_b["bench"][2] = {
        "occupied": True, "champion_id": "Briar", "uuid": "b-1", "star": 1
    }
    assert _signature(state_a) != _signature(state_b)


def test_native_audit_detects_movement_effect_but_not_a_blocked_move():
    before = _player()
    after = _player()
    after["board"][3] = {
        "occupied": True, "champion_id": "Nasus", "uuid": "n-1", "star": 1
    }
    assert _effect_for_action([4, 0, 0, 10, 3, 10], before, after)
    assert not _effect_for_action([4, 0, 0, 10, 3, 10], before, before)
    assert not _effect_for_action([6, 0, 0, 0, 0, 0], before, after)
