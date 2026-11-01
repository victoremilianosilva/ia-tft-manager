import torch

from policy import TFTPolicy


ACTION_DIMS = [9, 5, 9, 28, 28, 28]


def _policy_with_native_item_block():
    hidden = 64
    candidate_dim = (ACTION_DIMS[2] + ACTION_DIMS[1]) * 8
    item_dim = 10 + 9 * 17 + 100 * 17 + 37 * 18
    anvil_dim = 3 + 9 * 11
    obs_dim = 22 + 4 * 7 * 5 + anvil_dim + item_dim + candidate_dim
    policy = TFTPolicy(obs_dim=obs_dim, action_dims=ACTION_DIMS, hidden_size=hidden)
    return policy, torch.zeros(1, obs_dim)


def test_item_observation_exposes_components_inventory_recipes_and_all_targets():
    policy, obs = _policy_with_native_item_block()
    candidate_dim = policy.candidate_observation_dim
    item_dim = policy.item_state_observation_dim
    start = obs.shape[-1] - candidate_dim - item_dim
    obs[0, start] = 0.5  # component count feature
    obs[0, start + 10] = 0.75  # first bag item semantic feature
    recipe_start = start + 10 + 9 * 17
    obs[0, recipe_start + 4 * 17 + 2] = 0.6  # recipe [0,4], AP feature
    target_start = recipe_start + 100 * 17
    obs[0, target_start + 28 * 18 + 4 + 1] = 1.0  # first bench target role

    components, inventory, recipes, targets, pending_anvil = policy._item_state_features(obs)

    assert components.shape == (1, 10)
    assert inventory.shape == (1, 9, 17)
    assert recipes.shape == (1, 100, 17)
    assert targets.shape == (1, 37, 18)
    assert components[0, 0].item() == 0.5
    assert inventory[0, 0, 0].item() == 0.75
    assert recipes[0, 4, 2].item() == 0.6
    assert targets[0, 28, 5].item() == 1.0
    assert pending_anvil.tolist() == [False]


def test_item_target_scorer_uses_each_candidates_role_and_position_features():
    policy, _ = _policy_with_native_item_block()
    conditioned = torch.zeros(1, 64 + len(ACTION_DIMS) * 0 + 9)
    target_context = torch.zeros(1, 20)
    item_features = torch.zeros(1, 17)
    target_features = torch.zeros(1, 37, 18)

    first = policy.item_target_candidate_head[0]
    last = policy.item_target_candidate_head[-1]
    with torch.no_grad():
        policy.item_target_head.weight.zero_()
        policy.item_target_head.bias.zero_()
        first.weight.zero_()
        first.bias.zero_()
        target_feature_start = conditioned.shape[-1] + target_context.shape[-1] + item_features.shape[-1]
        first.weight[0, target_feature_start + 1] = 0.2  # board/bench location
        first.weight[0, target_feature_start + 5] = 1.0  # role one-hot
        last.weight.zero_()
        last.bias.zero_()
        last.weight[0, 0] = 1.0
        target_features[0, 0, 1] = 1.0  # board
        target_features[0, 0, 5] = 0.1  # role score
        target_features[0, 1, 2] = 1.0  # bench
        target_features[0, 1, 5] = 0.9  # role score

    logits = policy._item_target_logits(
        conditioned, target_context, item_features, target_features,
        torch.tensor([False]),
    )
    assert logits[0, 1] > logits[0, 0]


def test_inventory_candidate_scorer_uses_item_semantics():
    policy, _ = _policy_with_native_item_block()
    conditioned = torch.zeros(1, 64 + len(ACTION_DIMS))
    inventory_features = torch.zeros(1, 9, 17)
    inventory_features[0, 0, 0] = 0.1
    inventory_features[0, 1, 0] = 0.9
    first = policy.item_inventory_candidate_head[0]
    last = policy.item_inventory_candidate_head[-1]
    with torch.no_grad():
        policy.item_inventory_head.weight.zero_()
        policy.item_inventory_head.bias.zero_()
        first.weight.zero_()
        first.bias.zero_()
        first.weight[0, -17] = 1.0
        last.weight.zero_()
        last.bias.zero_()
        last.weight[0, 0] = 1.0

    logits = policy._item_inventory_logits(
        conditioned, inventory_features, torch.tensor([False])
    )
    assert logits[0, 1] > logits[0, 0]


def test_old_checkpoint_migrates_item_observation_and_neutral_candidate_heads():
    new_policy, _ = _policy_with_native_item_block()
    old_obs_dim = new_policy.obs_dim - new_policy.item_state_observation_dim
    old_policy = TFTPolicy(
        obs_dim=old_obs_dim, action_dims=ACTION_DIMS, hidden_size=64
    )
    legacy_state = {
        key: value.detach().clone()
        for key, value in old_policy.state_dict().items()
        if not key.startswith((
            "item_inventory_candidate_head.",
            "item_component_candidate_head.",
            "item_target_candidate_head.",
        ))
    }

    restored, _ = _policy_with_native_item_block()
    assert restored.load_compatible_state_dict(legacy_state)
    old_global = old_policy.state_dict()["global_mlp.0.weight"]
    old_global_input = old_global.shape[1]
    insertion = (
        old_global_input - restored.candidate_observation_dim
        - restored.economic_context_dim
    )
    added_columns = restored.item_state_observation_dim
    migrated_global = restored.state_dict()["global_mlp.0.weight"]
    assert torch.count_nonzero(
        migrated_global[:, insertion:insertion + added_columns]
    ) == 0
    assert torch.equal(migrated_global[:, :insertion], old_global[:, :insertion])
    assert torch.equal(
        migrated_global[:, insertion + added_columns:
                        insertion + added_columns + restored.economic_context_dim],
        old_global[:, insertion:insertion + restored.economic_context_dim],
    )
    assert torch.equal(
        migrated_global[:, insertion + added_columns + restored.economic_context_dim:],
        old_global[:, insertion + restored.economic_context_dim:],
    )
    for head in (
        restored.item_inventory_candidate_head,
        restored.item_component_candidate_head,
        restored.item_target_candidate_head,
    ):
        assert torch.count_nonzero(head[-1].weight) == 0
        assert torch.count_nonzero(head[-1].bias) == 0

def test_item_sampling_and_ppo_replay_use_identical_conditioned_distributions():
    policy, obs = _policy_with_native_item_block()
    type_mask = torch.zeros(1, 9, dtype=torch.bool)
    type_mask[0, 7] = True
    inventory_mask = torch.zeros(1, 9, dtype=torch.bool)
    inventory_mask[0, 0] = True
    target_mask = torch.zeros(1, 37, dtype=torch.bool)
    target_mask[0, 0] = True
    masks = {
        "type_mask": type_mask,
        "item_inventory_mask": inventory_mask,
        "item_target_mask": target_mask,
    }
    actions, sampled_logprob, _, _ = policy.get_action_and_value(
        obs, masks=masks, deterministic=True
    )
    replay_logprob, _, _ = policy.evaluate_actions(obs, actions, masks)
    assert actions[0, 0].item() == 7
    assert torch.allclose(sampled_logprob, replay_logprob, atol=1e-6, rtol=1e-6)


def test_craft_sampling_and_ppo_replay_use_same_recipe_target_context():
    policy, obs = _policy_with_native_item_block()
    type_mask = torch.zeros(1, 9, dtype=torch.bool)
    type_mask[0, 8] = True
    first_mask = torch.zeros(1, 10, dtype=torch.bool)
    first_mask[0, 0] = True
    pair_mask = torch.zeros(1, 10, 10, dtype=torch.bool)
    pair_mask[0, 0, 1] = True
    target_mask = torch.zeros(1, 37, dtype=torch.bool)
    target_mask[0, 0] = True
    masks = {
        "type_mask": type_mask,
        "item_component_first_mask": first_mask,
        "item_component_pair_masks": pair_mask,
        "item_target_mask": target_mask,
    }
    actions, sampled_logprob, _, _ = policy.get_action_and_value(
        obs, masks=masks, deterministic=True
    )
    replay_logprob, _, _ = policy.evaluate_actions(obs, actions, masks)
    assert actions[0, 0].item() == 8
    assert actions[0, 1].item() == 0
    assert actions[0, 2].item() == 1
    assert torch.allclose(sampled_logprob, replay_logprob, atol=1e-6, rtol=1e-6)
