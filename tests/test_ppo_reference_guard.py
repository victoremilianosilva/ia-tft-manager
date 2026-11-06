import torch
import pytest

from ppo_protection.reference_guard import snapshot_parameters, project_to_reference


def test_projection_limits_total_relative_drift():
    policy = torch.nn.Linear(4, 2)
    reference = snapshot_parameters(policy)
    with torch.no_grad():
        for parameter in policy.parameters():
            parameter.add_(10.0)
    result = project_to_reference(policy, reference, 0.01)
    assert result["projected"] is True
    assert result["relative_drift_after"] <= 0.010001
    assert result["relative_drift_before"] > result["relative_drift_after"]


def test_projection_does_not_change_policy_inside_trust_region():
    policy = torch.nn.Linear(4, 2)
    reference = snapshot_parameters(policy)
    result = project_to_reference(policy, reference, 0.02)
    assert result["projected"] is False
    assert result["relative_drift_after"] == 0.0


def test_projection_rejects_invalid_limit():
    policy = torch.nn.Linear(2, 1)
    with pytest.raises(ValueError):
        project_to_reference(policy, snapshot_parameters(policy), 0.0)
