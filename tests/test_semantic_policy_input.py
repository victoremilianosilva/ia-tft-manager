import torch

from action_contract import MASK_SHAPES
from policy import ACTION_DIMS, TFTPolicy
from semantic_observation import SEMANTIC_ENTITY_FEATURES, SEMANTIC_ENTITY_SLOTS, SEMANTIC_GLOBAL_FEATURES, SEMANTIC_ITEM_OFFSET, SEMANTIC_NUMERIC_DIM, SEMANTIC_TRAIT_VOCAB_SIZE, semantic_item_state_tensors


def _batch(batch_size=2):
    # Native production layout: core + board + anvil/item blocks + candidate tail.
    item_semantic = 17
    item_target = 17
    item_global = 10 + 9 * item_semantic + 100 * item_semantic + 37 * item_target
    item_compatibility = (9 + 100) * 37
    item_state = item_global + item_compatibility
    anvil = 3 + 9 * 11
    candidate = (9 + 5) * 6
    obs_dim = 10 + 4 * 7 * 5 + anvil + item_state + candidate
    obs = torch.zeros(batch_size, obs_dim, dtype=torch.float32)
    masks = {
        name: torch.zeros((batch_size, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    semantic_numeric = torch.zeros(batch_size, SEMANTIC_NUMERIC_DIM, dtype=torch.float32)
    semantic = {
        "numeric": semantic_numeric,
        "items": semantic_item_state_tensors(semantic_numeric),
        "champion_ids": torch.zeros(batch_size, SEMANTIC_ENTITY_SLOTS, dtype=torch.long),
    }
    return obs, masks, semantic



def test_native_semantic_entities_drive_board_cnn_and_action_candidates():
    obs, _, semantic = _batch(batch_size=1)
    policy = TFTPolicy(obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS), hidden_size=32, semantic_vocab_size=64).eval()
    entities = semantic["numeric"][:, SEMANTIC_GLOBAL_FEATURES:].view(1, SEMANTIC_ENTITY_SLOTS, SEMANTIC_ENTITY_FEATURES)
    entities[0, 0, 0] = 1.0
    entities[0, 0, 1] = 2.0 / 3.0
    entities[0, 0, 2] = 4.0 / 5.0
    entities[0, 0, 3] = 1.0 / 3.0
    entities[0, 0, 4] = 0.2
    entities[0, 28, 0] = 1.0
    entities[0, 28, 1] = 1.0
    entities[0, 28, 2] = 3.0 / 5.0
    entities[0, 28, 3] = 2.0 / 3.0
    entities[0, 28, 4] = 0.3
    entities[0, 28, 10] = 4.0 / 9.0
    entities[0, 37, 0] = 1.0
    entities[0, 37, 1] = 1.0 / 3.0
    entities[0, 37, 2] = 2.0 / 5.0
    entities[0, 37, 10] = 2.0 / 9.0
    captured = {}
    def capture_board(_module, args):
        captured["board"] = args[0].detach().clone()
    handle = policy.board_cnn[0].register_forward_pre_hook(capture_board)
    with torch.no_grad():
        policy.encode(obs, semantic_state=semantic)
        bench, shop = policy._candidate_features(obs, semantic_state=semantic)
    handle.remove()
    assert captured["board"].shape == (1, 5, 4, 7)
    assert torch.allclose(captured["board"][0, :, 0, 0], torch.tensor([1.0, 0.8, 2.0 / 3.0, 1.0 / 3.0, 0.2]))
    assert torch.allclose(bench[0, 0], torch.tensor([1.0, 0.6, 1.0 / 3.0, 2.0 / 3.0, 0.3, 4.0 / 9.0]))
    assert torch.allclose(shop[0, 0], torch.tensor([1.0, 0.4, 1.0 / 3.0, 0.0, 2.0 / 9.0, 0.0]))
    entities[0, 0, 12] = 1.0
    entities[0, 0, 13] = 1.0
    entities[0, 0, 15] = 2.0 / 3.0
    entities[0, 0, 16] = 1.0
    entities[0, 0, 23] = 0.5
    _, _, _, targets, _, _, _, _, _ = policy._item_state_features(obs, semantic_state=semantic)
    assert targets[0, 0, 0].item() == 1.0
    assert targets[0, 0, 1].item() == 1.0
    assert targets[0, 0, 2].item() == 0.0
    assert targets[0, 0, 4].item() == 1.0
    assert targets[0, 0, 11].item() == 0.5


def test_native_semantic_global_encoder_produces_finite_features():
    torch.manual_seed(20261118)
    obs, masks, semantic = _batch()
    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    ).eval()

    with torch.no_grad():
        semantic_values = policy.get_value(obs, masks=masks, semantic_state=semantic)
    assert semantic_values.shape == (obs.shape[0],)
    assert torch.isfinite(semantic_values).all()




def test_historical_anvil_scorer_weights_migrate_with_zero_kind_columns():
    obs, _, _ = _batch(batch_size=1)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    )
    state = {key: value.detach().clone() for key, value in policy.state_dict().items()}
    current = state["item_anvil_candidate_head.0.weight"]
    historical = torch.arange(
        current.shape[0] * (current.shape[1] - 2), dtype=torch.float32
    ).reshape(current.shape[0], current.shape[1] - 2)
    state["item_anvil_candidate_head.0.weight"] = historical

    assert policy.load_compatible_state_dict(state) is True
    migrated = policy.item_anvil_candidate_head[0].weight.detach()
    assert torch.equal(migrated[:, :-2], historical)
    assert torch.count_nonzero(migrated[:, -2:]) == 0


def test_anvil_candidate_scorer_distinguishes_component_and_completed_item_options():
    obs, _, _ = _batch(batch_size=1)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    )
    with torch.no_grad():
        policy.item_anvil_candidate_head[0].weight[:, -2].fill_(1.0)
        policy.item_anvil_candidate_head[0].weight[:, -1].fill_(2.0)
        policy.item_anvil_candidate_head[0].bias.zero_()
        policy.item_anvil_candidate_head[-1].weight.fill_(1.0)
        policy.item_anvil_candidate_head[-1].bias.zero_()
    conditioned = torch.zeros(1, 32 + len(ACTION_DIMS))
    option_features = torch.zeros(1, 9, 11)
    pending = torch.ones(1, dtype=torch.bool)
    component_kind = torch.tensor([[1.0, 0.0]])
    completed_kind = torch.tensor([[0.0, 1.0]])

    component_scores = policy._item_inventory_logits(
        conditioned, torch.zeros(1, 9, 17), torch.zeros(1, 9, 37),
        option_features, pending, component_kind,
    )
    completed_scores = policy._item_inventory_logits(
        conditioned, torch.zeros(1, 9, 17), torch.zeros(1, 9, 37),
        option_features, pending, completed_kind,
    )
    assert not torch.allclose(component_scores, completed_scores)

def test_semantic_global_encoder_embeds_trait_identity_and_receives_gradients():
    obs, _, semantic = _batch(batch_size=1)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    )
    trait_offset = SEMANTIC_GLOBAL_FEATURES + 29
    semantic["numeric"][0, trait_offset] = 123.0 / SEMANTIC_TRAIT_VOCAB_SIZE
    semantic["numeric"][0, trait_offset + 1] = 456.0 / SEMANTIC_TRAIT_VOCAB_SIZE
    semantic["items"] = semantic_item_state_tensors(semantic["numeric"])

    latent = policy.encode(obs, semantic_state=semantic)
    latent.square().mean().backward()

    gradient = policy.semantic_trait_embedding.weight.grad
    assert gradient is not None
    assert gradient[123].abs().sum().item() > 0.0
    assert gradient[456].abs().sum().item() > 0.0

def test_native_semantic_consumers_ignore_legacy_flat_board_item_and_candidate_blocks():
    obs, _, semantic = _batch(batch_size=2)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    )
    policy.eval()
    unrelated_flat = torch.randn_like(obs) * 100.0

    assert torch.equal(
        policy.encode(obs, semantic_state=semantic),
        policy.encode(unrelated_flat, semantic_state=semantic),
    )
    candidates = policy._candidate_features(obs, semantic_state=semantic)
    changed_candidates = policy._candidate_features(
        unrelated_flat, semantic_state=semantic
    )
    for left, right in zip(candidates, changed_candidates):
        assert torch.equal(left, right)

    item_features = policy._item_state_features(obs, semantic_state=semantic)
    changed_item_features = policy._item_state_features(
        unrelated_flat, semantic_state=semantic
    )
    for left, right in zip(item_features, changed_item_features):
        assert torch.equal(left, right)


def test_semantic_side_input_changes_actor_and_critic_and_receives_gradients():
    torch.manual_seed(20261119)
    obs, masks, semantic = _batch()
    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    )
    with torch.no_grad():
        policy.semantic_encoder[0].weight.fill_(0.001)
        policy.semantic_encoder[0].bias.fill_(0.1)
        policy.semantic_encoder[-1].weight.fill_(0.01)
        policy.semantic_encoder[-1].bias.zero_()
        policy.type_head.weight.fill_(0.01)
        policy.type_head.bias.zero_()
        policy.value_head.weight[:, :32].fill_(0.01)

    changed_numeric = torch.ones_like(semantic["numeric"])
    changed = {
        "numeric": changed_numeric,
        "items": semantic_item_state_tensors(changed_numeric),
        "champion_ids": torch.ones_like(semantic["champion_ids"]),
    }
    policy.eval()
    with torch.no_grad():
        base_features = policy.encode(obs, semantic_state=semantic)
        enriched_features = policy.encode(obs, semantic_state=changed)
        base_logits = policy.type_head(base_features)
        enriched_logits = policy.type_head(enriched_features)
        base_values = policy.get_value(obs, masks=masks, semantic_state=semantic)
        enriched_values = policy.get_value(obs, masks=masks, semantic_state=changed)
    assert not torch.allclose(base_values, enriched_values)
    assert not torch.allclose(base_logits, enriched_logits)

    policy.train()
    policy.zero_grad(set_to_none=True)
    policy.get_value(obs, masks=masks, semantic_state=changed).sum().backward()
    gradient = policy.semantic_encoder[-1].weight.grad
    assert gradient is not None
    assert float(gradient.abs().sum()) > 0.0


def test_historical_policy_checkpoint_loads_with_native_semantic_encoder():
    torch.manual_seed(20261120)
    obs, masks, semantic = _batch()
    source = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    ).eval()
    legacy_state = {
        key: value.detach().clone()
        for key, value in source.state_dict().items()
        if not key.startswith(("semantic_id_embedding.", "semantic_trait_embedding.", "semantic_encoder."))
    }

    migrated = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    ).eval()
    assert migrated.load_compatible_state_dict(legacy_state) is True
    with torch.no_grad():
        after = migrated.get_value(obs, masks=masks, semantic_state=semantic)
    assert after.shape == (obs.shape[0],)
    assert torch.isfinite(after).all()

def test_v1_semantic_encoder_checkpoint_maps_old_feature_offsets():
    torch.manual_seed(20261121)
    obs, _, _ = _batch()
    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    )
    old_numeric_dim = 269
    old_weight = torch.arange(
        256 * (old_numeric_dim + SEMANTIC_ENTITY_SLOTS * 16), dtype=torch.float32
    ).reshape(256, old_numeric_dim + SEMANTIC_ENTITY_SLOTS * 16)
    state = {
        key: value.detach().clone()
        for key, value in policy.state_dict().items()
        if not key.startswith(("semantic_encoder.", "semantic_trait_embedding."))
    }
    state["semantic_encoder.0.weight"] = old_weight
    state["semantic_encoder.0.bias"] = torch.zeros(256)
    state["semantic_encoder.2.weight"] = policy.semantic_encoder[2].weight.detach().clone()
    state["semantic_encoder.2.bias"] = policy.semantic_encoder[2].bias.detach().clone()

    assert policy.load_compatible_state_dict(state) is True
    migrated = policy.semantic_encoder[0].weight.detach()
    assert torch.equal(migrated[:, :17], old_weight[:, :17])
    for slot in range(SEMANTIC_ENTITY_SLOTS):
        old_start = 17 + slot * 6
        new_start = SEMANTIC_GLOBAL_FEATURES + slot * SEMANTIC_ENTITY_FEATURES
        assert torch.equal(migrated[:, new_start:new_start + 6], old_weight[:, old_start:old_start + 6])
        assert torch.count_nonzero(migrated[:, new_start + 6:new_start + SEMANTIC_ENTITY_FEATURES]) == 0
    champion_end = SEMANTIC_ITEM_OFFSET + SEMANTIC_ENTITY_SLOTS * 16
    assert torch.equal(
        migrated[:, SEMANTIC_ITEM_OFFSET:champion_end], old_weight[:, old_numeric_dim:]
    )
    assert torch.count_nonzero(migrated[:, champion_end:]) == 0




def test_semantic_v6_warm_start_resets_only_reinterpreted_consumer_columns():
    obs, _, _ = _batch(batch_size=1)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    )
    with torch.no_grad():
        policy.board_cnn[0].weight.fill_(1.0)
        policy.shop_head[0].weight.fill_(1.0)
        policy.sell_head[0].weight.fill_(1.0)
        policy.bench_to_board_head.weight.fill_(1.0)

    policy.reset_migrated_semantic_consumer_columns()

    assert torch.count_nonzero(policy.board_cnn[0].weight[:, :3, :, :]) > 0
    assert torch.count_nonzero(policy.board_cnn[0].weight[:, 3:5, :, :]) == 0
    assert torch.count_nonzero(policy.shop_head[0].weight[:, :-6]) > 0
    assert torch.count_nonzero(policy.shop_head[0].weight[:, -6:]) == 0
    assert torch.count_nonzero(policy.sell_head[0].weight[:, -6:]) == 0
    assert torch.count_nonzero(policy.bench_to_board_head.weight[:, -6:]) == 0
    assert torch.count_nonzero(policy.item_anvil_candidate_head[0].weight[:, -2:]) == 0

def test_v2_semantic_encoder_checkpoint_maps_global_target_item_and_trait_extensions():
    torch.manual_seed(20261122)
    obs, _, _ = _batch()
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    )
    old_numeric_dim = 21 + SEMANTIC_ENTITY_SLOTS * 12
    old_weight = torch.arange(
        256 * (old_numeric_dim + SEMANTIC_ENTITY_SLOTS * 16),
        dtype=torch.float32,
    ).reshape(256, old_numeric_dim + SEMANTIC_ENTITY_SLOTS * 16)
    state = {
        key: value.detach().clone()
        for key, value in policy.state_dict().items()
        if not key.startswith(("semantic_encoder.", "semantic_trait_embedding."))
    }
    state["semantic_encoder.0.weight"] = old_weight
    state["semantic_encoder.0.bias"] = torch.zeros(256)
    state["semantic_encoder.2.weight"] = policy.semantic_encoder[2].weight.detach().clone()
    state["semantic_encoder.2.bias"] = policy.semantic_encoder[2].bias.detach().clone()

    assert policy.load_compatible_state_dict(state) is True
    migrated = policy.semantic_encoder[0].weight.detach()
    assert torch.equal(migrated[:, :21], old_weight[:, :21])
    assert torch.count_nonzero(migrated[:, 21:SEMANTIC_GLOBAL_FEATURES]) == 0
    for slot in range(SEMANTIC_ENTITY_SLOTS):
        old_start = 21 + slot * 12
        new_start = SEMANTIC_GLOBAL_FEATURES + slot * SEMANTIC_ENTITY_FEATURES
        assert torch.equal(migrated[:, new_start:new_start + 12], old_weight[:, old_start:old_start + 12])
        assert torch.count_nonzero(migrated[:, new_start + 12:new_start + SEMANTIC_ENTITY_FEATURES]) == 0
    champion_end = SEMANTIC_ITEM_OFFSET + SEMANTIC_ENTITY_SLOTS * 16
    assert torch.equal(
        migrated[:, SEMANTIC_ITEM_OFFSET:champion_end], old_weight[:, old_numeric_dim:]
    )
    assert torch.count_nonzero(migrated[:, champion_end:]) == 0

def test_compact_observation_prefix_has_no_strategy_or_padding_slots():
    obs, _, _ = _batch(batch_size=3)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    )
    assert policy.pre_board_dim == 10
    assert policy.board_flat_dim == 4 * 7 * 5
    assert policy.obs_dim == obs.shape[-1]

    with torch.no_grad():
        context = policy._economic_context_features(obs)

    assert context.shape == (obs.shape[0], 5)
    assert torch.count_nonzero(context) == 0



def test_sampling_value_and_action_re_evaluation_share_the_same_semantic_row():
    torch.manual_seed(20261120)
    obs, masks, semantic = _batch(batch_size=1)
    policy = TFTPolicy(
        obs_dim=obs.shape[-1], action_dims=list(ACTION_DIMS),
        hidden_size=32, semantic_vocab_size=64,
    ).eval()
    with torch.no_grad():
        policy.semantic_encoder[0].weight.fill_(0.001)
        policy.semantic_encoder[0].bias.fill_(0.1)
        policy.semantic_encoder[-1].weight.fill_(0.01)
        policy.semantic_encoder[-1].bias.zero_()

    with torch.no_grad():
        actions, sampled_logprob, _, sampled_value = policy.get_action(
            obs, masks=masks, deterministic=True, semantic_state=semantic
        )
        replay_logprob, replay_entropy, replay_value = policy.evaluate_actions(
            obs, actions, masks=masks, semantic_state=semantic
        )
        missing_context_value = policy.get_value(obs, masks=masks, semantic_state={
            "numeric": torch.ones_like(semantic["numeric"]),
            "champion_ids": torch.ones_like(semantic["champion_ids"]),
        })

    assert actions[0, 0].item() == 6
    assert torch.allclose(sampled_logprob, replay_logprob, atol=1e-7, rtol=1e-7)
    assert torch.allclose(sampled_value, replay_value, atol=1e-7, rtol=1e-7)
    assert replay_entropy.shape == (1,)
    assert not torch.allclose(sampled_value, missing_context_value)
