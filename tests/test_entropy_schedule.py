import math

import pytest

from ppo import exponential_schedule_value


def test_entropy_schedule_starts_at_initial_value():
    assert exponential_schedule_value(0.0, 0.02, 0.005, 2.0) == pytest.approx(0.02)


def test_entropy_schedule_reaches_final_value_at_end():
    assert exponential_schedule_value(1.0, 0.02, 0.005, 2.0) == pytest.approx(0.005)


def test_entropy_schedule_is_monotonic_and_clamps_progress():
    values = [
        exponential_schedule_value(progress, 0.02, 0.005, 2.0)
        for progress in (0.0, 0.25, 0.5, 0.75, 1.0)
    ]
    assert all(math.isfinite(value) for value in values)
    assert all(left > right for left, right in zip(values, values[1:]))
    assert exponential_schedule_value(-1.0, 0.02, 0.005, 2.0) == pytest.approx(0.02)
    assert exponential_schedule_value(2.0, 0.02, 0.005, 2.0) == pytest.approx(0.005)


def test_entropy_schedule_rejects_invalid_parameters():
    with pytest.raises(ValueError):
        exponential_schedule_value(0.5, 0.005, 0.02, 2.0)
    with pytest.raises(ValueError):
        exponential_schedule_value(0.5, 0.02, 0.005, 0.0)
