"""End-to-end smoke test for PPO training on the native C++ lobby backend."""
from __future__ import annotations

import os
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
for module_dir in (ROOT / "cpp" / "build" / "bin", ROOT / "cpp" / "build" / "bin" / "Release"):
    if module_dir.exists():
        import sys
        sys.path.insert(0, str(module_dir))


if os.environ.get("REQUIRE_CPP_PARITY") == "1":
    from tft_engine import TFTLobby as _NativeTFTLobby  # noqa: F401
    import combat_engine  # noqa: F401
else:
    pytest.importorskip("tft_engine", reason="Build cpp target tft_engine for native PPO smoke test")
    pytest.importorskip("combat_engine", reason="Native PPO smoke test requires combat_engine")


def test_ppo_completes_update_with_cpp_backend(tmp_path, monkeypatch):
    """Construct Trainer, collect masked rollouts, and run a real PPO update."""
    monkeypatch.chdir(tmp_path)

    from trainer import Trainer

    trainer = Trainer(
        num_envs=1,
        use_subprocess=False,
        engine_backend="cpp",
    )
    assert trainer.engine_backend == "cpp"
    try:
        trainer.train(total_updates=1, rollout_steps=2)
    finally:
        # train() normally closes these at the end; keep cleanup safe if an
        # assertion or exception interrupts the training loop.
        vec_env = getattr(trainer, "vec_env", None)
        if vec_env is not None:
            vec_env.close()
        writer = getattr(trainer, "writer", None)
        if writer is not None:
            writer.close()
