import pytest

from training_config import TrainingConfig


def test_defaults_are_valid_and_exposed():
    config = TrainingConfig.from_env({})
    config.validate()
    assert config.learning_rate == 3e-4
    assert config.batch_size == 64
    assert config.ppo_epochs == 4
    assert config.total_updates == 280
    assert config.num_lobbies == 4


def test_environment_overrides_major_parameters(monkeypatch):
    values = {
        "TFT_PPO_LR": "0.0001",
        "TFT_PPO_MIN_LR": "0.00001",
        "TFT_PPO_BATCH_SIZE": "128",
        "TFT_PPO_EPOCHS": "6",
        "TFT_PPO_TARGET_KL": "0.03",
        "TFT_PPO_ENT_COEF": "0.03",
        "TFT_PPO_ENT_COEF_FINAL": "0.01",
        "TFT_PPO_GAMMA": "0.98",
        "TFT_PPO_GAE_LAMBDA": "0.9",
        "TFT_NUM_LOBBIES": "2",
        "TFT_TOTAL_UPDATES": "500",
    }
    for key, value in values.items():
        monkeypatch.setenv(key, value)
    config = TrainingConfig.from_env()
    assert config.learning_rate == 1e-4
    assert config.min_learning_rate == 1e-5
    assert config.batch_size == 128
    assert config.ppo_epochs == 6
    assert config.target_kl == 0.03
    assert config.entropy_coef_initial == 0.03
    assert config.entropy_coef_final == 0.01
    assert config.gamma == 0.98
    assert config.gae_lambda == 0.9
    assert config.num_lobbies == 2
    assert config.total_updates == 500


def test_target_kl_can_be_disabled(monkeypatch):
    monkeypatch.setenv("TFT_PPO_TARGET_KL", "off")
    assert TrainingConfig.from_env().target_kl is None


@pytest.mark.parametrize("overrides", [
    {"learning_rate": 0}, {"min_learning_rate": 1e-3},
    {"batch_size": 0}, {"ppo_epochs": 0}, {"target_kl": 0},
    {"gamma": 1.1}, {"clip_coef": 1.0},
])
def test_invalid_configuration_is_rejected(overrides):
    with pytest.raises(ValueError):
        TrainingConfig.from_env(overrides)


def test_unknown_parameter_is_rejected():
    with pytest.raises(ValueError, match="desconhecidos"):
        TrainingConfig.from_env({"lr": 1e-4})
