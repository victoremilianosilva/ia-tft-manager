import copy

import pytest
import torch

from checkpoint_contract import (
    CHECKPOINT_LINEAGE_ID,
    build_checkpoint_lineage_contract,
    validate_checkpoint_lineage_contract,
    validate_checkpoint_lineage_integrity,
    build_training_resume_contract,
    validate_training_resume_contract,
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

    with pytest.raises(ValueError, match="hash is invalid|linhagem incompatível"):
        validate_checkpoint_lineage_contract(changed, *inputs)


def test_checkpoint_lineage_rejects_policy_shape_change_even_when_components_match():
    inputs = _inputs()
    manifest = build_checkpoint_lineage_contract(*inputs)
    changed_policy = dict(inputs[0])
    changed_policy["actor.weight"] = torch.zeros((5, 3), dtype=torch.float32)

    with pytest.raises(ValueError, match="lineage incompatível"):
        validate_checkpoint_lineage_contract(manifest, changed_policy, *inputs[1:])


def test_checkpoint_lineage_accepts_only_retired_flat_global_mlp_weights():
    inputs = _inputs()
    historical_policy = dict(inputs[0])
    historical_policy["global_mlp.0.weight"] = torch.zeros((256, 128), dtype=torch.float32)
    historical_policy["global_mlp.0.bias"] = torch.zeros((256,), dtype=torch.float32)
    historical_policy["global_mlp.2.weight"] = torch.zeros((256, 256), dtype=torch.float32)
    historical_policy["global_mlp.2.bias"] = torch.zeros((256,), dtype=torch.float32)
    historical_manifest = build_checkpoint_lineage_contract(
        historical_policy, *inputs[1:]
    )

    # The historical manifest remains intact and hash-validated. Only its
    # retired flat-observation MLP weights are ignored by semantic-v6 runtime.
    validate_checkpoint_lineage_contract(historical_manifest, *inputs)

    changed_policy = dict(inputs[0])
    changed_policy["critic.weight"] = torch.zeros((2, 4), dtype=torch.float32)
    with pytest.raises(ValueError, match="lineage incompatível"):
        validate_checkpoint_lineage_contract(historical_manifest, changed_policy, *inputs[1:])


def test_checkpoint_lineage_rejects_missing_or_malformed_manifest():
    inputs = _inputs()
    with pytest.raises(TypeError, match="mapping"):
        validate_checkpoint_lineage_contract(None, *inputs)


def test_trainer_persists_lineage_for_periodic_and_final_checkpoints():
    from pathlib import Path

    source = (
        Path(__file__).resolve().parents[1] / "trainer.py"
    ).read_text(encoding="utf-8")
    assert source.count(
        '"checkpoint_contract": build_checkpoint_lineage_contract('
    ) == 2
    assert "TFT_ALLOW_UNVERSIONED_CHECKPOINT_LINEAGE" in source
    assert "and not legacy_checkpoint_lineage" in source
    assert "legacy_checkpoint_lineage or semantic_state_warm_start or training_contract_warm_start" in source
    assert "self.start_update = 1" in source
    assert "validate_checkpoint_lineage_contract(" in source



def test_training_resume_contract_binds_gae_and_optimizer_semantics():
    config = {
        "learning_rate": 0.0003, "adam_eps": 1e-5, "gamma": 0.99,
        "gae_lambda": 0.95, "rollout_steps": 128, "batch_size": 64,
        "ppo_epochs": 4, "checkpoint_path": "first.pt", "total_updates": 200,
    }
    manifest = build_training_resume_contract(config)
    assert validate_training_resume_contract(manifest, {
        **config, "checkpoint_path": "second.pt", "total_updates": 500
    })
    assert not validate_training_resume_contract(manifest, {**config, "gae_lambda": 0.90})
    assert not validate_training_resume_contract(manifest, {**config, "learning_rate": 0.0001})


def test_training_resume_contract_rejects_tampered_manifest():
    manifest = build_training_resume_contract({"gamma": 0.99, "gae_lambda": 0.95})
    tampered = copy.deepcopy(manifest)
    tampered["contract"]["training_config"]["gamma"] = 0.5
    with pytest.raises(ValueError, match="Hash"):
        validate_training_resume_contract(tampered, {"gamma": 0.99, "gae_lambda": 0.95})


def test_trainer_persists_and_requires_training_resume_contract():
    from pathlib import Path
    source = (Path(__file__).resolve().parents[1] / "trainer.py").read_text(encoding="utf-8")
    assert source.count('"training_resume_contract": build_training_resume_contract(self.config.to_dict())') == 2
    assert "TFT_ALLOW_TRAINING_CONFIG_WARM_START" in source
    assert "and not training_contract_warm_start" in source
    assert "TFT_WARM_START_OUTPUT_CHECKPOINT" in source
    assert source.count('"warm_start_source": warm_start_source_metadata') == 2
    assert source.count('"training_resume_contract": build_training_resume_contract(self.config.to_dict())') == 2



def test_semantic_contract_change_requires_explicit_weights_only_warm_start():
    from pathlib import Path

    source = (
        Path(__file__).resolve().parents[1] / "trainer.py"
    ).read_text(encoding="utf-8")
    assert "TFT_ALLOW_SEMANTIC_STATE_WARM_START" in source
    assert "TFT_WARM_START_OUTPUT_CHECKPOINT" in source
    assert "validate_semantic_state_warm_start_migration(" in source
    assert "semantic_policy_state_keys(checkpoint.get(\"policy\", {}))" in source
    assert "not semantic_state_warm_start" in source
    assert "Checkpoint histórico sem semantic_state v6" in source
    assert "semantic_state_warm_start = True" in source



def test_historical_lineage_integrity_can_be_checked_without_claiming_compatibility():
    inputs = _inputs()
    manifest = build_checkpoint_lineage_contract(*inputs)
    validate_checkpoint_lineage_integrity(manifest)
    tampered = copy.deepcopy(manifest)
    tampered["contract"]["components"]["semantic_state_contract"]["contract_id"] = "old-owner-v1"
    with pytest.raises(ValueError, match="hash is invalid"):
        validate_checkpoint_lineage_integrity(tampered)
