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



def test_infer_trait_count_uses_full_observation_layout():
    from scripts.evaluate_composition_ablation import infer_trait_count_from_observation_dim

    # 433 fixed features + 4 trait vectors + 14 candidate records * 8 features.
    obs_dim = 433 + (4 * 12) + (14 * 8)
    assert infer_trait_count_from_observation_dim(obs_dim) == 12


def test_infer_trait_count_rejects_incompatible_observation_dimension():
    from scripts.evaluate_composition_ablation import infer_trait_count_from_observation_dim

    try:
        infer_trait_count_from_observation_dim(433 + 4 * 12 + 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Incompatible observation dimension should raise ValueError.")


def test_zero_composition_controls_zeros_all_controls_and_preserves_candidate_tail():
    trait_count = 12
    candidate_dim = 14 * 8
    obs_dim = 433 + 4 * trait_count + candidate_dim
    observations = torch.arange(2 * obs_dim, dtype=torch.float32).reshape(2, obs_dim)

    ablated = zero_composition_controls(observations, trait_count, candidate_dim)
    candidate_start = obs_dim - candidate_dim
    control_start = candidate_start - (trait_count + 2)

    assert torch.all(ablated[:, control_start:candidate_start] == 0)
    assert torch.equal(ablated[:, :control_start], observations[:, :control_start])
    assert torch.equal(ablated[:, candidate_start:], observations[:, candidate_start:])
