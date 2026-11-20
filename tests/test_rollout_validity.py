import pytest
import torch

from rollout import RolloutBuffer


def _buffer(num_steps, num_envs):
    buffer = RolloutBuffer(
        num_steps=num_steps,
        num_envs=num_envs,
        obs_dim=1,
        action_dim=1,
        device="cpu",
    )
    buffer.ptr = num_steps
    return buffer


def test_invalid_transition_does_not_leak_advantage_to_previous_valid_step():
    buffer = _buffer(num_steps=2, num_envs=1)
    buffer.rewards[:, 0] = torch.tensor([0.0, 100.0])
    buffer.values.zero_()
    buffer.dones.zero_()
    buffer.trajectory_valid[:, 0] = torch.tensor([True, False])
    buffer.optimization_valid[:, 0] = torch.tensor([True, False])

    buffer.compute_returns_and_advantages(
        next_value=torch.tensor([0.0]),
        next_done=torch.tensor([0.0]),
        gamma=1.0,
        gae_lambda=1.0,
    )

    assert buffer.advantages[0, 0].item() == 0.0
    assert buffer.advantages[1, 0].item() == 0.0


def test_invalid_transition_breaks_only_its_own_agent_recurrence():
    buffer = _buffer(num_steps=2, num_envs=2)
    buffer.rewards[:] = torch.tensor([[1.0, 1.0], [50.0, 2.0]])
    buffer.values.zero_()
    buffer.dones.zero_()
    buffer.trajectory_valid[:] = torch.tensor([[True, True], [False, True]])
    buffer.optimization_valid[:] = torch.tensor([[True, True], [False, True]])

    buffer.compute_returns_and_advantages(
        next_value=torch.tensor([0.0, 0.0]),
        next_done=torch.tensor([0.0, 0.0]),
        gamma=1.0,
        gae_lambda=1.0,
    )

    assert buffer.advantages[0, 0].item() == 1.0
    assert buffer.advantages[1, 0].item() == 0.0
    assert buffer.advantages[0, 1].item() == 3.0
    assert buffer.advantages[1, 1].item() == 2.0



def test_optimizer_ineligible_but_valid_trajectory_still_carries_temporal_credit():
    buffer = _buffer(num_steps=2, num_envs=1)
    buffer.rewards[:, 0] = torch.tensor([1.0, 2.0])
    buffer.values.zero_()
    buffer.dones.zero_()
    buffer.trajectory_valid[:, 0] = torch.tensor([True, True])
    buffer.optimization_valid[:, 0] = torch.tensor([True, False])
    buffer.compute_returns_and_advantages(
        next_value=torch.tensor([0.0]), next_done=torch.tensor([0.0]),
        gamma=1.0, gae_lambda=1.0,
    )
    assert buffer.advantages[:, 0].tolist() == [3.0, 2.0]
    batches = list(buffer.get_batches(batch_size=8))
    assert sum(batch["obs"].shape[0] for batch in batches) == 1


def test_invalid_next_trajectory_blocks_bootstrap_from_untrusted_state():
    buffer = _buffer(num_steps=2, num_envs=1)
    buffer.rewards[:, 0] = torch.tensor([1.0, 100.0])
    buffer.values[:, 0] = torch.tensor([0.0, 50.0])
    buffer.dones.zero_()
    buffer.trajectory_valid[:, 0] = torch.tensor([True, False])
    buffer.optimization_valid[:, 0] = torch.tensor([True, False])
    buffer.compute_returns_and_advantages(
        next_value=torch.tensor([0.0]), next_done=torch.tensor([0.0]),
        gamma=1.0, gae_lambda=1.0,
    )
    assert buffer.advantages[:, 0].tolist() == [1.0, 0.0]


def test_rollout_truncation_bootstraps_only_from_valid_correlated_next_state():
    valid = _buffer(num_steps=1, num_envs=1)
    valid.rewards[0, 0] = 1.0
    valid.values.zero_()
    valid.trajectory_valid[0, 0] = True
    valid.optimization_valid[0, 0] = True
    valid.compute_returns_and_advantages(
        next_value=torch.tensor([10.0]), next_done=torch.tensor([0.0]),
        next_state_valid=torch.tensor([True]), gamma=1.0, gae_lambda=1.0,
    )
    assert valid.advantages[0, 0].item() == 11.0

    invalid = _buffer(num_steps=1, num_envs=1)
    invalid.rewards[0, 0] = 1.0
    invalid.values.zero_()
    invalid.trajectory_valid[0, 0] = True
    invalid.optimization_valid[0, 0] = True
    invalid.compute_returns_and_advantages(
        next_value=torch.tensor([10.0]), next_done=torch.tensor([0.0]),
        next_state_valid=torch.tensor([False]), gamma=1.0, gae_lambda=1.0,
    )
    assert invalid.advantages[0, 0].item() == 1.0


def test_optimization_valid_must_be_subset_of_trajectory_valid():
    buffer = RolloutBuffer(num_steps=1, num_envs=1, obs_dim=1, action_dim=1, device="cpu")
    with pytest.raises(ValueError, match="subconjunto"):
        buffer.add(
            obs=torch.zeros((1, 1)), actions=torch.zeros((1, 1), dtype=torch.long),
            logprobs=torch.zeros(1), rewards=torch.zeros(1), dones=torch.zeros(1),
            values=torch.zeros(1), masks_dict={},
            trajectory_valid=torch.tensor([False]), optimization_valid=torch.tensor([True]),
        )
