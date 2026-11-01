import torch

from policy import TFTPolicy


ACTION_DIMS = [9, 5, 9, 28, 28, 28]
OBS_DIM = 22 + (4 * 7 * 5) + (1 + 4 * 7) + ((9 + 5) * 8)


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


def test_legacy_checkpoint_migrates_new_observation_and_bench_target_inputs():
    policy, _ = _policy_and_observation()
    old_state = policy.state_dict()
    old_global = old_state["global_mlp.0.weight"][:, :-29].clone()
    old_bench_target = old_state["bench_to_board_head.weight"][:, :-17].clone()
    old_state["global_mlp.0.weight"] = old_global
    old_state["bench_to_board_head.weight"] = old_bench_target

    restored = TFTPolicy(obs_dim=OBS_DIM, action_dims=ACTION_DIMS, hidden_size=64)
    assert restored.load_compatible_state_dict(old_state)

    migrated_global = restored.state_dict()["global_mlp.0.weight"]
    insertion = old_global.shape[1] - restored.candidate_observation_dim
    assert torch.allclose(migrated_global[:, :insertion], old_global[:, :insertion])
    assert torch.count_nonzero(migrated_global[:, insertion:insertion + 29]) == 0
    assert torch.allclose(
        migrated_global[:, insertion + 29:],
        old_global[:, insertion:],
    )

    migrated_target = restored.state_dict()["bench_to_board_head.weight"]
    assert torch.allclose(migrated_target[:, :-17], old_bench_target)
    assert torch.count_nonzero(migrated_target[:, -17:]) == 0


def test_economic_phase_features_reach_the_policy_encoder():
    policy, obs = _policy_and_observation()
    obs.zero_()
    # Round 4-1, level 7, 75 gold, healthy FAST8 plan.
    obs[:, 0] = 0.80
    obs[:, 1] = 1.50
    obs[:, 2] = 7.0 / 9.0
    obs[:, 6] = 19.0 / 29.0
    obs[:, 12] = 1.0

    features = policy._economic_context_features(obs)
    assert torch.allclose(features[0, 0], torch.tensor(0.8))
    assert torch.allclose(features[0, 1], torch.tensor(1.0 / 8.0))
    assert torch.allclose(features[0, 2], torch.tensor(10.0 / 50.0))
    assert torch.allclose(features[0, 3], torch.tensor(65.0 / 200.0))
    assert torch.allclose(features[0, 4], torch.tensor(1.0 / 6.0), atol=1e-6)

    # The same phase under SLOWROLL exposes its level-6 target and roll reserve.
    obs[:, 12] = 0.0
    obs[:, 13] = 1.0
    slowroll = policy._economic_context_features(obs)
    assert torch.allclose(slowroll[0, 0], torch.tensor(0.6))
    assert torch.allclose(slowroll[0, 1], torch.tensor(0.0))
    assert torch.allclose(slowroll[0, 2], torch.tensor(25.0 / 50.0))


def test_entropy_only_diagnostics_are_compact_and_finite():
    policy, obs = _policy_and_observation()
    with torch.no_grad():
        _, _, _, _, diagnostics = policy.get_action_and_value_with_entropy_diagnostics(obs)
    assert diagnostics and diagnostics[0]
    for record in diagnostics[0]:
        assert torch.isfinite(torch.tensor(record["entropy_nats"]))
        assert 0.0 <= record["entropy_normalized"] <= 1.00001
        assert "probabilities" not in record
