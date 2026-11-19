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
    buffer.valid[:, 0] = torch.tensor([True, False])

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
    buffer.valid[:] = torch.tensor([[True, True], [False, True]])

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
