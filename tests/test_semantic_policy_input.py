import torch

from action_contract import MASK_SHAPES
from policy import ACTION_DIMS, TFTPolicy
from semantic_observation import SEMANTIC_ENTITY_SLOTS, SEMANTIC_NUMERIC_DIM


def _batch(batch_size=2):
    # Native production layout: core + board + anvil/item blocks + candidate tail.
    item_semantic = 17
    item_target = 18
    item_global = 10 + 9 * item_semantic + 100 * item_semantic + 37 * item_target
    item_compatibility = (9 + 100) * 37
    item_state = item_global + item_compatibility
    anvil = 3 + 9 * 11
    candidate = (9 + 5) * 8
    obs_dim = 22 + 4 * 7 * 5 + anvil + item_state + candidate
    obs = torch.zeros(batch_size, obs_dim, dtype=torch.float32)
    masks = {
        name: torch.zeros((batch_size, *shape), dtype=torch.bool)
        for name, shape in MASK_SHAPES.items()
    }
    masks["type_mask"][:, 6] = True
    semantic = {
        "numeric": torch.zeros(batch_size, SEMANTIC_NUMERIC_DIM, dtype=torch.float32),
        "champion_ids": torch.zeros(batch_size, SEMANTIC_ENTITY_SLOTS, dtype=torch.long),
    }
    return obs, masks, semantic


def test_semantic_side_input_preserves_legacy_output_until_encoder_learns():
    torch.manual_seed(20261118)
    obs, masks, semantic = _batch()
    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    ).eval()

    with torch.no_grad():
        legacy_values = policy.get_value(obs, masks=masks)
        semantic_values = policy.get_value(obs, masks=masks, semantic_state=semantic)
    assert torch.allclose(legacy_values, semantic_values, atol=1e-7, rtol=1e-7)


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

    changed = {
        "numeric": torch.ones_like(semantic["numeric"]),
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


def test_historical_policy_checkpoint_migrates_with_neutral_semantic_encoder():
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
        if not key.startswith(("semantic_id_embedding.", "semantic_encoder."))
    }

    migrated = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=list(ACTION_DIMS),
        hidden_size=32,
        semantic_vocab_size=64,
    ).eval()
    assert migrated.load_compatible_state_dict(legacy_state) is True
    with torch.no_grad():
        before = source.get_value(obs, masks=masks)
        after = migrated.get_value(obs, masks=masks, semantic_state=semantic)
    assert torch.allclose(before, after, atol=1e-6, rtol=1e-6)
