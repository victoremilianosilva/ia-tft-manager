import copy

import pytest
import torch

from checkpoint_contract import (
    CHECKPOINT_LINEAGE_ID,
    build_checkpoint_lineage_contract,
    validate_checkpoint_lineage_contract,
)


def _inputs():
    policy = {
        "actor.weight": torch.zeros((4, 3), dtype=torch.float32),
        "critic.weight": torch.zeros((1, 4), dtype=torch.float32),
    }
    return (
        policy,
        {"manifest_version": 1, "action_contract": {"id": "action-v1"}},
        {"manifest_version": 1, "contract": {"id": "critic-mask-v1"}},
        {"manifest_version": 1, "contract": {"id": "semantic-state-v1"}},
        {"contract_id": "reward-v1", "version": 1, "sha256": "a" * 64},
    )


def test_checkpoint_lineage_binds_all_component_contracts_and_policy_shape():
    inputs = _inputs()
    manifest = build_checkpoint_lineage_contract(*inputs)

    assert manifest["contract"]["contract_id"] == CHECKPOINT_LINEAGE_ID
    assert manifest["contract"]["components"]["reward_contract"] == inputs[-1]
    validate_checkpoint_lineage_contract(manifest, *inputs)


def test_checkpoint_lineage_rejects_component_substitution():
    inputs = _inputs()
    manifest = build_checkpoint_lineage_contract(*inputs)
    changed = copy.deepcopy(manifest)
    changed["contract"]["components"]["reward_contract"]["sha256"] = "b" * 64

    with pytest.raises(ValueError, match="linhagem incompatível"):
        validate_checkpoint_lineage_contract(changed, *inputs)


def test_checkpoint_lineage_rejects_policy_shape_change_even_when_components_match():
    inputs = _inputs()
    manifest = build_checkpoint_lineage_contract(*inputs)
    changed_policy = dict(inputs[0])
    changed_policy["actor.weight"] = torch.zeros((5, 3), dtype=torch.float32)

    with pytest.raises(ValueError, match="linhagem incompatível"):
        validate_checkpoint_lineage_contract(manifest, changed_policy, *inputs[1:])


def test_checkpoint_lineage_rejects_missing_or_malformed_manifest():
    inputs = _inputs()
    with pytest.raises(TypeError, match="mapping"):
        validate_checkpoint_lineage_contract(None, *inputs)
