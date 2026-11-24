import argparse

import pytest

from scripts.run_training_battery import parse_seeds


def test_parse_seeds_preserves_order_and_requires_unique_nonnegative_values():
    assert parse_seeds("11, 12,13") == [11, 12, 13]


@pytest.mark.parametrize("value", ["", "-1,2", "4294967296", "1,1", "one,2"])
def test_parse_seeds_rejects_invalid_seed_lists(value):
    with pytest.raises(argparse.ArgumentTypeError):
        parse_seeds(value)
