import torch

from scripts.evaluate_composition_ablation import zero_composition_controls


def test_zero_composition_controls_preserves_candidate_tail():
    observations = torch.arange(2 * 200, dtype=torch.float32).reshape(2, 200)
    trait_count = 10
    candidate_dim = 16

    ablated = zero_composition_controls(observations, trait_count, candidate_dim)
    start = 200 - candidate_dim - (trait_count + 2)

    assert torch.all(ablated[:, start:start + trait_count + 2] == 0)
    assert torch.equal(ablated[:, :start], observations[:, :start])
    assert torch.equal(ablated[:, start + trait_count + 2:], observations[:, start + trait_count + 2:])


def test_zero_composition_controls_rejects_invalid_layout():
    observations = torch.zeros(1, 20)

    try:
        zero_composition_controls(observations, trait_count=12, candidate_dim=10)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid observation layout should raise ValueError.")
