"""Factory for selecting the Python or native C++ TFT lobby backend."""
from __future__ import annotations

import os
from collections.abc import Callable
from typing import Any


SUPPORTED_BACKENDS = ("python", "cpp")


def resolve_engine_backend(engine_backend: str | None = None) -> str:
    """Resolve explicit argument > TFT_ENGINE_BACKEND > Python default."""
    selected = engine_backend
    if selected is None:
        selected = os.environ.get("TFT_ENGINE_BACKEND", "python")

    selected = str(selected).strip().lower()
    if selected not in SUPPORTED_BACKENDS:
        raise ValueError(
            "engine_backend deve ser 'python' ou 'cpp'; "
            f"recebi {selected!r}."
        )
    return selected


def make_lobby_factory(engine_backend: str | None = None) -> tuple[str, Callable[..., Any]]:
    """Return the selected backend name and a lazy-imported lobby constructor."""
    selected = resolve_engine_backend(engine_backend)

    if selected == "python":
        from lobby.TFTLobby import TFTLobby
        return selected, TFTLobby

    from cpp_lobby_env import CppTFTLobbyWrapper
    return selected, CppTFTLobbyWrapper
