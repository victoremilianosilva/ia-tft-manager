import pytest

from policy import ACTION_DIMS, LEGACY_ACTION_DIMS
from viewer.session import ACTION_NAMES, _resolve_action_dims


def test_viewer_defaults_missing_action_metadata_to_current_contract():
    assert _resolve_action_dims({}) == [9, 5, 9, 28, 28, 28]


def test_viewer_migrates_legacy_seven_action_metadata():
    assert _resolve_action_dims({"action_dims": LEGACY_ACTION_DIMS}) == ACTION_DIMS


def test_viewer_preserves_current_action_metadata():
    assert _resolve_action_dims({"action_dims": [9, 5, 9, 28, 28, 28]}) == ACTION_DIMS


def test_viewer_has_names_for_item_actions():
    assert ACTION_NAMES[7] == "EQUIP_FROM_INVENTORY"
    assert ACTION_NAMES[8] == "CRAFT_AND_EQUIP"


def test_viewer_rejects_malformed_action_metadata():
    with pytest.raises(ValueError, match="action_dims inválidos"):
        _resolve_action_dims({"action_dims": "not-a-dimension-list"})
