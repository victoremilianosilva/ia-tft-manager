import torch
import pytest

from item_policy import ItemPPOHead


def _masks(batch=4):
    masks = {
        "type": torch.ones(batch, 5, dtype=torch.bool),
        "first_component": torch.ones(batch, 18, dtype=torch.bool),
        "second_component": torch.ones(batch, 18, dtype=torch.bool),
        "inventory_item": torch.ones(batch, 18, dtype=torch.bool),
        "source_unit": torch.ones(batch, 37, dtype=torch.bool),
        "target_unit": torch.ones(batch, 37, dtype=torch.bool),
        "equipped_item": torch.ones(batch, 3, dtype=torch.bool),
    }
    masks["type"][:, 0] = True
    return masks


def test_item_policy_sample_and_evaluate_logprob_match():
    torch.manual_seed(7)
    policy = ItemPPOHead(feature_dim=16)
    features = torch.randn(4, 16)
    masks = _masks()
    actions, logp, entropy = policy(features, masks=masks)
    eval_logp, eval_entropy = policy.evaluate_actions(features, actions, masks)
    assert actions.shape == (4, 7)
    assert torch.isfinite(logp).all()
    assert torch.isfinite(entropy).all()
    assert torch.allclose(logp, eval_logp, atol=1e-5)
    assert torch.allclose(entropy, eval_entropy, atol=1e-5)


def test_item_policy_respects_type_mask():
    policy = ItemPPOHead(feature_dim=8)
    features = torch.randn(3, 8)
    masks = _masks(3)
    masks["type"][:] = False
    masks["type"][:, 0] = True
    actions, _, _ = policy(features, masks=masks, deterministic=True)
    assert torch.equal(actions[:, 0], torch.zeros(3, dtype=torch.long))


def test_item_policy_rejects_empty_mask():
    policy = ItemPPOHead(feature_dim=8)
    features = torch.randn(2, 8)
    masks = _masks(2)
    masks["type"][0] = False
    with pytest.raises(ValueError, match="no legal choices"):
        policy(features, masks=masks)
