
# ============================================================
# 🔬 scripts/profile_env_step.py
#
# Perfil de desempenho do env_step / TFTLobby.step.
#
# Uso:
#   python scripts/profile_env_step.py
#
# O backend é selecionado por TFT_DECISION_ENGINE.
# O script NÃO calcula máscaras nem altera a lógica do ambiente.
# ============================================================

from __future__ import annotations

import cProfile
import os
import pstats
import sys
from pathlib import Path

import numpy as np

# Permite executar o script diretamente a partir da pasta scripts.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lobby.TFTLobby import TFTLobby


def profile_lobby_steps(
    *,
    measured_steps: int = 1_000,
    seed: int = 2026,
) -> None:
    """Perfila passos da lobby, excluindo reset e inicialização."""

    backend = os.getenv("TFT_DECISION_ENGINE", "python").lower()

    print("=" * 72)
    print("🔬 PROFILING DO ENV_STEP")
    print("=" * 72)
    print(f"Backend: {backend}")
    print(f"Passos medidos: {measured_steps}")
    print(f"Seed: {seed}")
    print("Ações: PASS para todos os jogadores")
    print("Reset e inicialização ficam fora da medição.")
    print()

    lobby = TFTLobby(seed=seed)
    profiler = cProfile.Profile()

    actions = [{"type": 6} for _ in range(lobby.PLAYERS_PER_LOBBY)]

    completed_steps = 0
    completed_matches = 0

    try:
        while completed_steps < measured_steps:
            # Mede somente a execução do passo da lobby.
            profiler.enable()
            try:
                _, _, finished, _ = lobby.step(actions)
            finally:
                profiler.disable()

            completed_steps += 1

            if finished:
                completed_matches += 1

                # Não incluir o custo de reset no perfil.
                if completed_steps < measured_steps:
                    lobby.reset()

    finally:
        # Não é necessário manter o profiler ativo após o loop.
        profiler.disable()

    print(f"Passos concluídos: {completed_steps}")
    print(f"Partidas concluídas: {completed_matches}")
    print()

    stats = pstats.Stats(profiler)
    stats.strip_dirs()

    print("=" * 72)
    print("⏱️ TOP 40 — TEMPO CUMULATIVO")
    print("Inclui o tempo das funções chamadas.")
    print("=" * 72)
    stats.sort_stats("cumtime").print_stats(40)

    print()
    print("=" * 72)
    print("⚙️ TOP 30 — TEMPO PRÓPRIO")
    print("Exclui o tempo gasto dentro de outras funções.")
    print("=" * 72)
    stats.sort_stats("tottime").print_stats(30)


if __name__ == "__main__":
    steps = int(os.getenv("TFT_PROFILE_STEPS", "1000"))

    if steps <= 0:
        raise ValueError("TFT_PROFILE_STEPS precisa ser maior que zero.")

    profile_lobby_steps(measured_steps=steps)
