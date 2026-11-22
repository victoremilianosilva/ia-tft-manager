from types import SimpleNamespace

import torch

from training_config import TrainingConfig
from training_run_manifest import build_training_run_manifest, write_training_run_manifest


class FakeNativeEngine:
    pass


class FakePolicy:
    obs_dim = 1
    action_dims = [9, 5, 9, 28, 28, 28]
    fusion = [SimpleNamespace(out_features=16)]

    def __init__(self):
        self.value_head = SimpleNamespace(in_features=80)

    def state_dict(self):
        return {
            "fusion.0.weight": torch.zeros((16, 100)),
            "value_head.weight": torch.zeros((1, 80)),
        }


def test_run_manifest_records_native_lineage_and_is_stable(tmp_path, monkeypatch):
    monkeypatch.setenv("TFT_SOURCE_REVISION", "test-revision")
    monkeypatch.setenv("TFT_DISABLE_LEGACY_STRATEGY_PROJECTION", "1")
    monkeypatch.setenv("TFT_OPGG_DISABLE_REFRESH", "1")
    config = TrainingConfig(
        seed=77,
        checkpoint_path=str(tmp_path / "model.pt"),
        log_dir=str(tmp_path / "logs"),
        run_manifest_path=str(tmp_path / "run_manifest.json"),
    )
    semantic_contract = {
        "manifest_version": 1,
        "contract": {"contract_id": "tft.test.semantic.v1"},
        "sha256": "a" * 64,
    }

    first = build_training_run_manifest(
        config=config,
        policy=FakePolicy(),
        semantic_state_contract=semantic_contract,
        engine=FakeNativeEngine(),
    )
    second = build_training_run_manifest(
        config=config,
        policy=FakePolicy(),
        semantic_state_contract=semantic_contract,
        engine=FakeNativeEngine(),
    )

    assert first["algorithm"] == "PPO"
    assert first["seed"] == 77
    assert first["source"]["revision"] == "test-revision"
    assert first["engine"]["module"] == FakeNativeEngine.__module__
    assert first["contracts"]["semantic_state"] == semantic_contract
    assert first["contracts"]["checkpoint_lineage"]["contract"]["contract_id"]
    assert first["contracts"]["training_resume"]["contract"]["contract_id"]
    assert first["policy"]["architecture_id"] == "tft.policy.native-semantic-ppo"
    assert first["runtime_features"]["legacy_strategy_projection_disabled"] is True
    assert first["runtime_features"]["external_catalog_refresh_disabled"] is True
    assert first["identity_sha256"] == second["identity_sha256"]
    assert first["manifest_sha256"] != ""


def test_run_manifest_writer_creates_parent_and_round_trips(tmp_path):
    path = tmp_path / "nested" / "run.json"
    manifest = {"manifest_id": "tft.test", "identity_sha256": "abc"}

    write_training_run_manifest(path, manifest)

    import json
    assert json.loads(path.read_text(encoding="utf-8")) == manifest
