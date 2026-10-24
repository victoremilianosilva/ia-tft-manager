import pytest
from item_action_contract import ITEM_ACTION_DIMS, ItemActionType, normalize_item_action

def test_item_action_dimensions_are_stable():
    assert ITEM_ACTION_DIMS == (5, 18, 18, 18, 37, 37, 3)

def test_wait_accepts_sequence_and_mapping():
    assert normalize_item_action([0, 0, 0, 0, 0, 0, 0]) == [0] * 7
    assert normalize_item_action({"type": ItemActionType.WAIT}) == [0] * 7

@pytest.mark.parametrize("action", [
    [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0], [0, 18, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 37, 0, 0], [0, 0, 0, 0, 0, 0, 3],
])
def test_malformed_or_out_of_range_actions_are_rejected(action):
    with pytest.raises(ValueError):
        normalize_item_action(action)

def test_transfer_to_same_unit_is_rejected():
    with pytest.raises(ValueError, match="same unit"):
        normalize_item_action([ItemActionType.TRANSFER, 0, 0, 0, 12, 12, 0])

def test_transfer_between_distinct_units_is_structurally_valid():
    assert normalize_item_action([ItemActionType.TRANSFER, 0, 0, 0, 9, 10, 0])[0] == ItemActionType.TRANSFER
