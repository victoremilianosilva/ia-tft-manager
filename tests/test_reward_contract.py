import copy

import pytest

from reward_contract import (
    REWARD_CONTRACT_HASH,
    build_reward_checkpoint_contract,
    validate_reward_checkpoint_contract,
)


def test_reward_checkpoint_contract_is_stable_and_versioned():
    contract = build_reward_checkpoint_contract()
    assert contract["contract_id"] == "tft.ppo.outcome-reward.v1"
    assert contract["version"] == 1
    assert contract["sha256"] == REWARD_CONTRACT_HASH
    validate_reward_checkpoint_contract(contract)


def test_reward_checkpoint_contract_rejects_unknown_version_or_hash():
    contract = build_reward_checkpoint_contract()
    changed = copy.deepcopy(contract)
    changed["version"] = 2
    with pytest.raises(ValueError, match="reward_contract incompatível"):
        validate_reward_checkpoint_contract(changed)

    changed = copy.deepcopy(contract)
    changed["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="reward_contract incompatível"):
        validate_reward_checkpoint_contract(changed)


def test_reward_checkpoint_contract_rejects_missing_manifest():
    with pytest.raises(TypeError, match="mapping"):
        validate_reward_checkpoint_contract(None)



def test_trainer_binds_reward_contract_and_requires_explicit_legacy_opt_in():
    from pathlib import Path

    source = (
        Path(__file__).resolve().parents[1] / "trainer.py"
    ).read_text(encoding="utf-8")
    assert 'saved_reward_contract = checkpoint.get("reward_contract")' in source
    assert "TFT_ALLOW_UNVERSIONED_REWARD_CHECKPOINT" in source
    assert "and not legacy_reward_checkpoint" in source
    assert source.count(
        '"reward_contract": build_reward_checkpoint_contract()'
    ) == 2
