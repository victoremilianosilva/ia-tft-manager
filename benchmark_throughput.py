# 🚀 benchmark_throughput.py
# Mede o throughput do ambiente vetorizado, sem inferência PPO.

import time
import numpy as np

from lobby.TFTLobby import TFTLobby
from vector_lobby_env import LobbyVectorEnv

NUM_LOBBIES = 4
PLAYERS_PER_LOBBY = 8
WARMUP = 50
SAMPLES = 500


def summarize(name, values):
    values = np.asarray(values, dtype=np.float64)

    print(f"\n📊 {name}")
    print(f"   Amostras: {len(values)}")
    print(f"   Média:    {values.mean():.4f} ms")
    print(f"   Mediana:  {np.median(values):.4f} ms")
    print(f"   P95:      {np.percentile(values, 95):.4f} ms")


def main():
    print("🚀 Inicializando ambientes...")

    env = LobbyVectorEnv(
        [TFTLobby for _ in range(NUM_LOBBIES)]
    )

    try:
        env.reset()

        # 🎮 PASS para os 8 jogadores de cada lobby.
        actions = [
            [{"type": 6} for _ in range(PLAYERS_PER_LOBBY)]
            for _ in range(NUM_LOBBIES)
        ]

        print(f"🏟️ Lobbies: {NUM_LOBBIES}")
        print(f"👥 Jogadores por lobby: {PLAYERS_PER_LOBBY}")
        print(f"🤖 Jogadores totais: {NUM_LOBBIES * PLAYERS_PER_LOBBY}")

        # 🔥 Aquecimento: não entra nas estatísticas.
        for _ in range(WARMUP):
            env.step(actions)

        timings = []

        print(f"\n⏱️ Medindo {SAMPLES} chamadas de step()...")

        for _ in range(SAMPLES):
            start = time.perf_counter()
            env.step(actions)
            elapsed = time.perf_counter() - start
            timings.append(elapsed)

        total_seconds = sum(timings)
        total_calls = len(timings)

        # 📈 Cada chamada avança uma etapa em cada lobby.
        lobby_steps = total_calls * NUM_LOBBIES

        # 📈 Cada lobby executa uma ação para cada jogador.
        player_steps = lobby_steps * PLAYERS_PER_LOBBY

        print("\n" + "=" * 48)
        print("📈 RESULTADO DO THROUGHPUT")
        print("=" * 48)

        summarize("Tempo por chamada vetorizada", 
                  [t * 1000 for t in timings])

        print(f"\n   Tempo total:          {total_seconds:.3f} s")
        print(f"   Chamadas vetorizadas: {total_calls}")
        print(f"   Lobby-steps:          {lobby_steps}")
        print(f"   Player-steps:         {player_steps}")

        print(f"\n⚡ Vetorizadas/s: {total_calls / total_seconds:.2f}")
        print(f"⚡ Lobby-steps/s: {lobby_steps / total_seconds:.2f}")
        print(f"⚡ Player-steps/s: {player_steps / total_seconds:.2f}")

        print("\n✅ Benchmark concluído.")

    finally:
        env.close()


if __name__ == "__main__":
    main()

#🏟️ Lobbies: 4
#👥 Jogadores por lobby: 8
#🤖 Jogadores totais: 32

#⏱️ Medindo 500 chamadas de step()...

#================================================
#📈 RESULTADO DO THROUGHPUT
#================================================

#📊 Tempo por chamada vetorizada
#   Amostras: 500
#   Média:    341.8654 ms
#   Mediana:  343.4781 ms
#   P95:      364.1867 ms

#   Tempo total:          170.933 s
#   Chamadas vetorizadas: 500
#   Lobby-steps:          2000
#   Player-steps:         16000

#⚡ Vetorizadas/s: 2.93
#⚡ Lobby-steps/s: 11.70
#⚡ Player-steps/s: 93.60

#✅ Benchmark concluído.