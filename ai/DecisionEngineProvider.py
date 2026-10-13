
"""Seleção do backend de decisões do TFT.

Configuração:
    TFT_DECISION_ENGINE=python  -> implementação Python (padrão)
    TFT_DECISION_ENGINE=cpp     -> extensão nativa decision_engine

A seleção é explícita: se C++ for solicitado e a extensão não puder
ser carregada, o erro será reportado sem fallback silencioso.
"""

from __future__ import annotations

import importlib
import os
from dataclasses import dataclass
from types import ModuleType
from typing import Literal


BackendName = Literal["python", "cpp"]

_ENVIRONMENT_VARIABLE = "TFT_DECISION_ENGINE"

_REQUIRED_CPP_API = (
    "ActionMaskEngine",
    "AntiLoopEngine",
    "PlayerState",
)


@dataclass(frozen=True)
class DecisionEngineBackend:
    """Representa o backend selecionado para o motor de decisões."""

    name: BackendName
    native_module: ModuleType | None = None

    @property
    def is_cpp(self) -> bool:
        return self.name == "cpp"

    @property
    def is_python(self) -> bool:
        return self.name == "python"

    def require_native_module(self) -> ModuleType:
        """Retorna a extensão nativa ou explica por que ela não existe."""
        if self.native_module is None:
            raise RuntimeError(
                "O backend C++ não está carregado. "
                "Configure TFT_DECISION_ENGINE=cpp."
            )

        return self.native_module


def get_decision_engine_backend(
    backend: str | None = None,
) -> DecisionEngineBackend:
    """Resolve o backend por argumento ou variável de ambiente.

    A prioridade é:
    1. argumento `backend`;
    2. variável TFT_DECISION_ENGINE;
    3. Python, como padrão seguro durante a migração.
    """
    selected = (
        backend
        if backend is not None
        else os.getenv(_ENVIRONMENT_VARIABLE, "python")
    ).strip().lower()

    if selected not in ("python", "cpp"):
        raise ValueError(
            f"Backend inválido: {selected!r}. "
            "Valores aceitos: 'python' ou 'cpp'."
        )

    if selected == "python":
        return DecisionEngineBackend(name="python")

    try:
        native_module = importlib.import_module("decision_engine")
    except ImportError as exc:
        raise RuntimeError(
            "O backend C++ foi solicitado, mas o módulo "
            "'decision_engine' não pôde ser importado. "
            "Compile a extensão e verifique o PYTHONPATH "
            "do ambiente Python ativo."
        ) from exc

    missing_api = [
        name
        for name in _REQUIRED_CPP_API
        if not hasattr(native_module, name)
    ]

    if missing_api:
        missing = ", ".join(missing_api)
        raise RuntimeError(
            "O módulo 'decision_engine' foi importado, "
            f"mas faltam componentes obrigatórios: {missing}."
        )

    return DecisionEngineBackend(
        name="cpp",
        native_module=native_module,
    )