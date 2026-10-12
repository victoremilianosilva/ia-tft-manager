# 📊 Benchmark de env.step() e combate C++
# Execute com: python benchmark_step_combat.py

import time
import statistics
import numpy as np

from lobby.TFTLobby import TFTLobby
from ai.ActionMaskManager import ActionType


WARMUP = 50
SAMPLES = 500


def summarize(label, timings):
    """Exibe estatísticas em milissegundos."""

    if not timings:
        print(f"⚠️ Nenhuma amostra para {label}")
        return

    print(f"\n📊 {label}")
    print(f"   Amostras: {len(timings)}")
    print(f"   Média:    {statistics.mean(timings):.4f} ms")
    print(f"   Mediana:  {statistics.median(timings):.4f} ms")
    print(f"   P95:      {np.percentile(timings, 95):.4f} ms")
    print(f"   Mínimo:   {min(timings):.4f} ms")
    print(f"   Máximo:   {max(timings):.4f} ms")


def benchmark_env_step(player, samples=SAMPLES):
    """Mede somente MiniTFTEnv.step(), sem combate do lobby."""

    action = {"type": int(ActionType.PASS)}

    # 🔥 Aquecimento
    for _ in range(WARMUP):
        player.env.step(action)

    timings = []

    for _ in range(samples):
        start = time.perf_counter()
        player.env.step(action)
        timings.append((time.perf_counter() - start) * 1000)

    return timings


def prepare_combat(lobby):
    """Move uma unidade do banco para o tabuleiro de cada jogador."""

    players = [p for p in lobby.players if p.alive]

    if len(players) < 2:
        raise RuntimeError("São necessários pelo menos dois jogadores.")

    player_a, player_b = players[0], players[1]

    for player, position in ((player_a, 0), (player_b, 27)):
        env = player.env
        bench = env.bench_manager
        board = env.board_manager

        slots = bench.get_occupied_positions()

        if not slots:
            raise RuntimeError(
                f"Jogador {player.player_id} não possui unidades no banco."
            )

        unit = bench.remove_unit(slots[0])

        if not board.add_unit(unit, position):
            raise RuntimeError(
                f"Não foi possível posicionar unidade do jogador "
                f"{player.player_id}."
            )

        env._rebuild_player_state()

    return player_a, player_b

def benchmark_combat(lobby, player_a, player_b, samples=SAMPLES):
    """Mede combates sem deixar o HP acumular dano entre amostras."""

    # 💚 Salva o HP inicial dos dois jogadores.
    initial_hp_a = max(1, player_a.env.hp)
    initial_hp_b = max(1, player_b.env.hp)

    def run_combat():
        # 🔄 Restaura o HP antes de cada simulação.
        player_a.env.hp = initial_hp_a
        player_b.env.hp = initial_hp_b

        return lobby.resolve_combat(player_a, player_b)

    # 🔥 Aquecimento
    for _ in range(WARMUP):
        run_combat()

    timings = []

    for _ in range(samples):
        start = time.perf_counter()
        result = run_combat()
        elapsed_ms = (time.perf_counter() - start) * 1000

        if result is None:
            raise RuntimeError("O combate não retornou um resultado.")

        timings.append(elapsed_ms)

    return timings


def main():
    print("🚀 Inicializando lobby...")
    lobby = TFTLobby(seed=42)
    lobby.reset()

    players = [p for p in lobby.players if p.alive]
    print(f"👥 Jogadores ativos: {len(players)}")

    # 1️⃣ env.step(): mede um jogador, sem executar combates do lobby.
    print("\n⏱️ Medindo MiniTFTEnv.step()...")
    step_times = benchmark_env_step(players[0])
    summarize("MiniTFTEnv.step() — ação PASS", step_times)

    # 2️⃣ Combate: garante unidades nos dois tabuleiros.
    print("\n⚔️ Preparando combate real...")
    player_a, player_b = prepare_combat(lobby)

    print(
        f"   Jogador {player_a.player_id}: "
        f"{player_a.env.board_manager.get_unit_count()} unidade(s)"
    )
    print(
        f"   Jogador {player_b.player_id}: "
        f"{player_b.env.board_manager.get_unit_count()} unidade(s)"
    )

    print("\n⏱️ Medindo resolução de combate...")
    combat_times = benchmark_combat(lobby, player_a, player_b)
    summarize("TFTLobby.resolve_combat() — motor de combate", combat_times)

    print("\n✅ Benchmark concluído.")


if __name__ == "__main__":
    main()


#👥 Jogadores ativos: 8

#⏱️ Medindo MiniTFTEnv.step()...

#📊 MiniTFTEnv.step() — ação PASS
#   Amostras: 500
#   Média:    0.2877 ms
#   Mediana:  0.2821 ms
#   P95:      0.3080 ms
#   Mínimo:   0.2769 ms
#   Máximo:   0.6114 ms

#⚔️ Preparando combate real...
#   Jogador 0: 1 unidade(s)
#   Jogador 1: 1 unidade(s)

#⏱️ Medindo resolução de combate...

#📊 TFTLobby.resolve_combat() — motor de combate
#   Amostras: 500
#   Média:    0.1005 ms
#   Mediana:  0.0978 ms
#   P95:      0.1173 ms
#   Mínimo:   0.0958 ms
#   Máximo:   0.2246 ms

#✅ Benchmark concluído.