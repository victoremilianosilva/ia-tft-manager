"""Regression tests for candidate-aware purchase/sale policy heads."""
import torch

from policy import TFTPolicy


ACTION_DIMS = [9, 5, 9, 28, 28, 28]


def _make_candidate_scorer_prefer_feature(head, hidden_size, feature_index, sign=1.0):
    """Configure a tiny deterministic scorer for controlled candidate-ranking tests."""
    first, second = head[0], head[2]
    with torch.no_grad():
        first.weight.zero_()
        first.bias.zero_()
        second.weight.zero_()
        second.bias.zero_()
        first.weight[0, hidden_size + ACTION_DIMS[0] + feature_index] = 1.0
        second.weight[0, 0] = sign


def test_candidate_features_are_aligned_with_bench_and_shop_slots():
    policy = TFTPolicy(obs_dim=400, action_dims=ACTION_DIMS, hidden_size=16)
    obs = torch.zeros(2, 400)
    tail = obs[:, -policy.candidate_observation_dim:]
    tail[:, : 9 * 8] = 1.0
    tail[:, 9 * 8:] = 2.0

    bench, shop = policy._candidate_features(obs)

    assert bench.shape == (2, 9, 8)
    assert shop.shape == (2, 5, 8)
    assert torch.all(bench == 1.0)
    assert torch.all(shop == 2.0)


def test_purchase_head_can_rank_the_best_offer_by_slot_local_fit():
    hidden_size = 16
    policy = TFTPolicy(obs_dim=400, action_dims=ACTION_DIMS, hidden_size=hidden_size)
    _make_candidate_scorer_prefer_feature(policy.shop_head, hidden_size, feature_index=0)

    context = torch.zeros(1, hidden_size + ACTION_DIMS[0])
    candidates = torch.zeros(1, 5, 8)
    candidates[0, :, 0] = torch.tensor([0.1, 0.9, 0.2, 0.4, 0.3])

    logits = policy._candidate_logits(policy.shop_head, context, candidates)

    assert int(logits.argmax(dim=-1).item()) == 1
    assert logits[0, 1] > logits[0, 0]


def test_sale_head_can_prefer_the_least_compatible_unit():
    hidden_size = 16
    policy = TFTPolicy(obs_dim=400, action_dims=ACTION_DIMS, hidden_size=hidden_size)
    # A low compatibility score should produce a larger sale logit in this
    # controlled scorer; learned weights are evaluated separately by the audit script.
    _make_candidate_scorer_prefer_feature(policy.sell_head, hidden_size, feature_index=0, sign=-1.0)

    context = torch.zeros(1, hidden_size + ACTION_DIMS[0])
    candidates = torch.zeros(1, 9, 8)
    candidates[0, :, 0] = torch.tensor([0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5])

    logits = policy._candidate_logits(policy.sell_head, context, candidates)
    # The action head is conditional: empty bench slots are excluded by the
    # same validity mask used by the real action-selection path.
    valid_candidates = torch.tensor(
        [[True, True, True, False, False, False, False, False, False]]
    )
    logits = policy._mask_logits(logits, valid_candidates)

    assert int(logits.argmax(dim=-1).item()) == 1
    assert logits[0, 1] > logits[0, 0]


def test_sale_head_can_preserve_core_and_upgrade_copies():
    hidden_size = 16
    policy = TFTPolicy(obs_dim=400, action_dims=ACTION_DIMS, hidden_size=hidden_size)
    first, second = policy.sell_head[0], policy.sell_head[2]
    with torch.no_grad():
        first.weight.zero_()
        first.bias.zero_()
        second.weight.zero_()
        second.bias.zero_()
        # Penalize core flag (feature 4) and owned-copy count (feature 5).
        first.weight[0, hidden_size + ACTION_DIMS[0] + 4] = 1.0
        first.weight[1, hidden_size + ACTION_DIMS[0] + 5] = 1.0
        second.weight[0, 0] = -1.0
        second.weight[0, 1] = -1.0

    context = torch.zeros(1, hidden_size + ACTION_DIMS[0])
    candidates = torch.zeros(1, 9, 8)
    candidates[0, 0, 4:6] = torch.tensor([1.0, 0.9])  # core + upgrade copies
    candidates[0, 1, 4:6] = torch.tensor([0.0, 0.1])  # non-core + few copies
    candidates[0, 2, 4:6] = torch.tensor([0.0, 0.2])

    logits = policy._candidate_logits(policy.sell_head, context, candidates)
    # Only the first three bench slots contain units in this scenario. Apply
    # the same validity mask as the production SELL action path before ranking.
    valid_candidates = torch.tensor(
        [[True, True, True, False, False, False, False, False, False]]
    )
    logits = policy._mask_logits(logits, valid_candidates)

    assert int(logits.argmax(dim=-1).item()) == 1


def test_policy_forward_accepts_new_candidate_observation_contract():
    obs_dim = 400
    policy = TFTPolicy(obs_dim=obs_dim, action_dims=ACTION_DIMS, hidden_size=32)
    observations = torch.zeros(2, obs_dim)
    masks = {
        "type_mask": torch.tensor([[True, False, False, False, False, False, False]] * 2),
        "shop_mask": torch.ones(2, 5, dtype=torch.bool),
        "bench_source_mask": torch.ones(2, 9, dtype=torch.bool),
        "board_target_mask": torch.ones(2, 28, dtype=torch.bool),
        "board_source_mask": torch.ones(2, 28, dtype=torch.bool),
        "board_move_target_masks": torch.ones(2, 28, 28, dtype=torch.bool),
        "bench_move_source_mask": torch.ones(2, 9, dtype=torch.bool),
        "bench_to_board_target_masks": torch.ones(2, 9, 28, dtype=torch.bool),
    }

    actions, logprob, entropy, value, diagnostics = policy.get_action_and_value_with_diagnostics(
        observations, masks=masks, deterministic=True
    )

    assert actions.shape == (2, 6)
    assert torch.isfinite(logprob).all()
    assert torch.isfinite(entropy).all()
    assert torch.isfinite(value).all()
    assert all(any(item["head"] == "shop_slot" for item in row) for row in diagnostics)
