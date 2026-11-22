"""Reproducible identity and provenance for native PPO training runs."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

import numpy as np
import torch

from action_contract import (
    build_action_mask_checkpoint_contract,
    build_critic_mask_input_checkpoint_contract,
)
from reward_contract import build_reward_checkpoint_contract
from checkpoint_contract import build_training_resume_contract


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _source_identity() -> dict[str, Any]:
    root = Path(__file__).resolve().parent
    revision = os.environ.get("TFT_SOURCE_REVISION", "").strip()
    if not revision:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0 or not result.stdout.strip():
            raise RuntimeError(
                "Não foi possível identificar a revisão Git do treinamento. "
                "Execute a partir de um checkout versionado ou defina TFT_SOURCE_REVISION."
            )
        revision = result.stdout.strip()

    diff = subprocess.run(
        ["git", "diff", "--binary", "HEAD"],
        cwd=root,
        capture_output=True,
        check=False,
    )
    diff_bytes = diff.stdout if diff.returncode == 0 else b""
    return {
        "revision": revision,
        "working_tree_dirty": bool(diff_bytes),
        "tracked_diff_sha256": hashlib.sha256(diff_bytes).hexdigest(),
    }


def _engine_identity(engine: Any) -> dict[str, str]:
    module_name = type(engine).__module__
    module = sys.modules.get(module_name)
    if module is None:
        module = importlib.import_module(module_name)
    module_path = getattr(module, "__file__", None)
    if not module_path:
        raise RuntimeError(
            f"Não foi possível localizar o binário nativo do Engine: {module_name}."
        )
    path = Path(module_path).resolve()
    if not path.is_file():
        raise RuntimeError(f"Artefato nativo do Engine não encontrado: {path}.")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return {"module": module_name, "artifact_sha256": digest}


def _policy_identity(policy: Any) -> dict[str, Any]:
    state_schema = [
        {
            "name": name,
            "shape": list(tensor.shape),
            "dtype": str(tensor.dtype),
        }
        for name, tensor in sorted(policy.state_dict().items())
    ]
    return {
        "architecture_id": "tft.policy.native-semantic-ppo",
        "architecture_version": 1,
        "implementation": type(policy).__qualname__,
        "observation_carrier_dim": int(policy.obs_dim),
        "action_dimensions": [int(value) for value in policy.action_dims],
        "hidden_size": int(policy.fusion[0].out_features),
        "state_dict_schema": state_schema,
        "state_dict_schema_sha256": _canonical_hash(state_schema),
    }


def build_training_run_manifest(
    *,
    config: Any,
    policy: Any,
    semantic_state_contract: dict,
    engine: Any,
) -> dict[str, Any]:
    identity = {
        "manifest_id": "tft.ppo.native-training-run",
        "manifest_version": 1,
        "algorithm": "PPO",
        "seed": int(config.seed),
        "source": _source_identity(),
        "engine": _engine_identity(engine),
        "runtime": {
            "python": sys.version.split()[0],
            "torch": str(torch.__version__),
            "numpy": str(np.__version__),
        },
        "training_config": config.to_dict(),
        "policy": _policy_identity(policy),
        "contracts": {
            "semantic_state": semantic_state_contract,
            "action_mask": build_action_mask_checkpoint_contract(),
            "critic_mask_input": build_critic_mask_input_checkpoint_contract(),
            "reward": build_reward_checkpoint_contract(),
            "training_resume": build_training_resume_contract(config.to_dict()),
        },
    }
    manifest = {
        **identity,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "identity_sha256": _canonical_hash(identity),
    }
    manifest["manifest_sha256"] = _canonical_hash(manifest)
    return manifest


def write_training_run_manifest(path: str | Path, manifest: dict[str, Any]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(target)
