import torch

from policy import TFTPolicy


ACTION_DIMS = [7, 5, 9, 28, 28, 28]
OBS_DIM = 22 + (4 * 7 * 5) + ((9 + 5) * 8)


def _policy_and_observation(batch_size=1):
    torch.manual_seed(7)
    policy = TFTPolicy(obs_dim=OBS_DIM, action_dims=ACTION_DIMS, hidden_size=64)
    obs = torch.randn(batch_size, OBS_DIM)
    return policy, obs


def _move_bench_masks(batch_size=1):
    type_mask = torch.zeros(batch_size, ACTION_DIMS[0], dtype=torch.bool)
    type_mask[:, 3] = True
    source_mask = torch.zeros(batch_size, ACTION_DIMS[2], dtype=torch.bool)
    source_mask[:, :2] = True
    target_masks = torch.zeros(
        batch_size, ACTION_DIMS[2], ACTION_DIMS[3], dtype=torch.bool
    )
    target_masks[:, :2, :3] = True
    return {
        "type_mask": type_mask,
        "bench_move_source_mask": source_mask,
        "bench_source_mask": source_mask.clone(),
        "bench_to_board_target_masks": target_masks,
    }


def test_bench_to_board_logits_include_selected_slot_and_candidate_features():
    policy, obs = _policy_and_observation()
    bench_features, _ = policy._candidate_features(obs)
    conditioned = torch.randn(1, policy.fusion[-2].out_features + policy.num_action_types)
    selected_slots = torch.tensor([1])
    captured = {}

    def capture_input(_module, args):
        captured["input"] = args[0].detach().clone()

    hook = policy.bench_to_board_head.register_forward_pre_hook(capture_input)
    try:
        policy._bench_to_board_logits(conditioned, selected_slots, bench_features)
    finally:
        hook.remove()

    actual = captured["input"]
    expected_slot = torch.nn.functional.one_hot(selected_slots, num_classes=9).float()
    expected_features = bench_features[:, 1, :]
    assert actual.shape[-1] == conditioned.shape[-1] + 9 + 8
    assert torch.equal(actual[:, conditioned.shape[-1]:conditioned.shape[-1] + 9], expected_slot)
    assert torch.allclose(actual[:, -8:], expected_features)


def test_bench_to_board_logits_change_when_selected_unit_features_change():
    policy, obs = _policy_and_observation()
    bench_features, _ = policy._candidate_features(obs)
    conditioned = torch.randn(1, policy.fusion[-2].out_features + policy.num_action_types)

    with torch.no_grad():
        first = policy._bench_to_board_logits(conditioned, torch.tensor([0]), bench_features)
        second = policy._bench_to_board_logits(conditioned, torch.tensor([1]), bench_features)

    # Distinct slot identity/features are part of the input to the destination scorer.
    assert not torch.allclose(first, second)


def test_sampling_and_evaluate_actions_use_identical_bench_target_distribution():
    policy, obs = _policy_and_observation()
    masks = _move_bench_masks()

    actions, sampled_logprob, _, _ = policy.get_action_and_value(
        obs, masks=masks, deterministic=True
    )
    evaluated_logprob, _, _ = policy.evaluate_actions(obs, actions, masks)

    assert actions.shape == (1, 6)
    assert actions[0, 0].item() == 3
    assert torch.allclose(sampled_logprob, evaluated_logprob, atol=1e-6, rtol=1e-6)
