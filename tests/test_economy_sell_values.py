"""Sale-value regression tests for the current TFT Set 18 rules."""

import pytest

from economy.EconomyManager import EconomyManager


@pytest.mark.parametrize(
    ("cost", "star", "expected"),
    [
        (1, 1, 1), (1, 2, 3), (1, 3, 9),
        (2, 1, 2), (2, 2, 5), (2, 3, 17),
        (3, 1, 3), (3, 2, 8), (3, 3, 26),
        (4, 1, 4), (4, 2, 11), (4, 3, 35),
        (5, 1, 5), (5, 2, 14), (5, 3, 44),
    ],
)
def test_sell_value_matches_tft_combine_fee(cost, star, expected):
    economy = EconomyManager()
    assert economy.get_sell_value({"cost": cost, "star": star}) == expected


def test_selling_none_returns_zero():
    assert EconomyManager().get_sell_value(None) == 0
