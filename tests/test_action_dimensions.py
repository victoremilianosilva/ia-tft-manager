import pytest
import torch

from policy import TFTPolicy
from trainer import Trainer


def test_action_dimensions_match_the_environment_contract():
    assert Trainer.ACTION_DIMS == [7, 5, 9, 28, 28, 28]
    assert Trainer.ACTION_DIM == len(Trainer.ACTION_DIMS)


def test_policy_heads_match_action_dimensions():
    policy = TFTPolicy(
        obs_dim=162,
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )

    assert policy.type_head.out_features == 7
    assert policy.shop_head[-1].out_features == 1
    assert policy.shop_head[0].in_features == 32 + 7 + 8
    assert policy.sell_head[-1].out_features == 1
    assert policy.sell_head[0].in_features == 32 + 7 + 8
    assert policy.bench_head.out_features == 9
    assert policy.bench_to_board_head.out_features == 28
    assert policy.board_source_head.out_features == 28
    assert policy.board_move_target_head.out_features == 28


def test_policy_rejects_invalid_action_dimensions():
    invalid_dimensions = [
        [7, 5, 9, 28, 28],
        [7, 5, 9, 28, 28, 27],
        [7, 5, 9, 28, 28, 28, 1],
    ]

    for dimensions in invalid_dimensions:
        with pytest.raises(ValueError):
            TFTPolicy(
                obs_dim=162,
                action_dims=dimensions,
                hidden_size=32,
            )


def _configure_candidate_ranker(head, hidden_size, feature_indices, signs):
    first, second = head[0], head[2]
    with torch.no_grad():
        first.weight.zero_()
        first.bias.zero_()
        second.weight.zero_()
        second.bias.zero_()
        for neuron, (feature_index, sign) in enumerate(zip(feature_indices, signs)):
            first.weight[neuron, hidden_size + Trainer.ACTION_DIMS[0] + feature_index] = 1.0
            second.weight[0, neuron] = sign


def test_candidate_policy_ranks_shop_slots_by_local_compatibility():
    hidden_size = 16
    policy = TFTPolicy(obs_dim=400, action_dims=Trainer.ACTION_DIMS, hidden_size=hidden_size)
    _configure_candidate_ranker(policy.shop_head, hidden_size, [0], [1.0])
    context = torch.zeros(1, hidden_size + Trainer.ACTION_DIMS[0])
    candidates = torch.zeros(1, 5, 8)
    candidates[0, :, 0] = torch.tensor([0.1, 0.9, 0.2, 0.4, 0.3])

    logits = policy._candidate_logits(policy.shop_head, context, candidates)

    assert int(logits.argmax(dim=-1).item()) == 1


def test_candidate_policy_avoids_selling_core_upgrade_copies():
    hidden_size = 16
    policy = TFTPolicy(obs_dim=400, action_dims=Trainer.ACTION_DIMS, hidden_size=hidden_size)
    _configure_candidate_ranker(policy.sell_head, hidden_size, [4, 5], [-1.0, -1.0])
    context = torch.zeros(1, hidden_size + Trainer.ACTION_DIMS[0])
    candidates = torch.zeros(1, 9, 8)

    # Two valid sale candidates: slot 0 is core and contributes to an upgrade;
    # slot 1 is non-core and has fewer copies. Other slots are marked protected
    # so this unit test evaluates candidate ranking rather than empty-slot masking.
    candidates[0, :, 4:6] = torch.tensor([1.0, 0.9])
    candidates[0, 0, 4:6] = torch.tensor([1.0, 0.9])
    candidates[0, 1, 4:6] = torch.tensor([0.0, 0.1])

    logits = policy._candidate_logits(policy.sell_head, context, candidates)

    assert int(logits.argmax(dim=-1).item()) == 1


def test_candidate_observation_tail_aligns_bench_and_shop_slots():
    policy = TFTPolicy(obs_dim=400, action_dims=Trainer.ACTION_DIMS, hidden_size=16)
    observations = torch.zeros(2, 400)
    tail = observations[:, -policy.candidate_observation_dim:]
    tail[:, :9 * 8] = 1.0
    tail[:, 9 * 8:] = 2.0

    bench, shop = policy._candidate_features(observations)

    assert bench.shape == (2, 9, 8)
    assert shop.shape == (2, 5, 8)
    assert torch.all(bench == 1.0)
    assert torch.all(shop == 2.0)



def test_checkpoint_migration_inserts_composition_features_before_candidate_tail():
    old_obs_dim = 400
    added_composition_features = 20
    new_obs_dim = old_obs_dim + added_composition_features
    hidden_size = 16

    old_policy = TFTPolicy(
        obs_dim=old_obs_dim,
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=hidden_size,
    )
    new_policy = TFTPolicy(
        obs_dim=new_obs_dim,
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=hidden_size,
    )

    old_weight = old_policy.global_mlp[0].weight.detach().clone()
    migrated = new_policy.load_compatible_state_dict(old_policy.state_dict())

    assert migrated is True
    new_weight = new_policy.global_mlp[0].weight.detach()
    candidate_tail_dim = new_policy.candidate_observation_dim
    insertion = old_weight.shape[1] - candidate_tail_dim

    # Existing non-candidate columns are preserved exactly; the newly added
    # composition fields are zero-initialized; candidate columns shift intact.
    assert torch.equal(new_weight[:, :insertion], old_weight[:, :insertion])
    assert torch.count_nonzero(
        new_weight[:, insertion:insertion + added_composition_features]
    ).item() == 0
    assert torch.equal(
        new_weight[:, insertion + added_composition_features:],
        old_weight[:, insertion:],
    )


def test_policy_accepts_observation_with_composition_control_features():
    obs_dim = 420
    policy = TFTPolicy(
        obs_dim=obs_dim,
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )
    observations = torch.zeros(2, obs_dim)
    values = policy.get_value(observations)
    actions, log_prob, entropy, values_again = policy.get_action_and_value(
        observations,
        deterministic=True,
    )

    assert values.shape == (2,)
    assert values_again.shape == (2,)
    assert actions.shape == (2, Trainer.ACTION_DIM)
    assert log_prob.shape == (2,)
    assert entropy.shape == (2,)
