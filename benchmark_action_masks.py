# 📊 Benchmark de geração de máscaras de ações por jogador
# Execute na raiz do projeto:
# python benchmark_action_masks.py

import time
import statistics
import numpy as np

from lobby.TFTLobby import TFTLobby


WARMUP = 50
SAMPLES = 500


def percentile(values, p):
    return float(np.percentile(values, p))


def benchmark_player(lobby, player, samples=SAMPLES):
    """Mede a geração de máscaras de um jogador ativo."""

    # 🔥 Aquecimento: reduz o impacto de custos iniciais.
    for _ in range(WARMUP):
        lobby.get_action_masks()

    # ⏱️ Mede o custo individual, mantendo o estado do jogo.
    # As máscaras dos outros jogadores também são calculadas
    # durante esta chamada; por isso, isolamos o jogador abaixo
    # para medir seu custo diretamente.
    manager = player.env.action_mask_manager

    timings_ms = []

    for _ in range(samples):
        start = time.perf_counter()

        # Reproduz o cálculo de máscaras desse jogador,
        # seguindo a implementação de TFTLobby.get_action_masks().
        (
            board_source_mask,
            move_target_masks,
            has_board_move,
        ) = manager.get_board_move_masks()

        (
            bench_move_source_mask,
            bench_to_board_target_masks,
            has_bench_move,
        ) = manager.get_bench_move_masks()

        raw = player.env.get_action_masks(
            include_conditioned_board_target=False,
            include_board_target=False,
            board_source_mask=board_source_mask,
            board_move_available=has_board_move,
            bench_move_available=has_bench_move,
        )

        # Consome os resultados para manter o benchmark representativo.
        _ = (
            raw,
            move_target_masks,
            bench_move_source_mask,
            bench_to_board_target_masks,
        )

        elapsed_ms = (time.perf_counter() - start) * 1000
        timings_ms.append(elapsed_ms)

    return timings_ms


def main():
    print("🚀 Criando lobby para benchmark...")
    lobby = TFTLobby(seed=42)
    lobby.reset()

    active_players = [p for p in lobby.players if p.alive]
    eliminated_players = [p for p in lobby.players if not p.alive]

    print(f"👥 Jogadores ativos: {len(active_players)}")
    print(f"💀 Jogadores eliminados: {len(eliminated_players)}")
    print(f"🔥 Aquecimento: {WARMUP} chamadas por jogador")
    print(f"📏 Amostras: {SAMPLES} por jogador")
    print()

    all_times = []

    for player in active_players:
        timings = benchmark_player(lobby, player)
        all_times.extend(timings)

        print(
            f"Jogador {player.player_id}: "
            f"média={statistics.mean(timings):.4f} ms | "
            f"mediana={statistics.median(timings):.4f} ms | "
            f"P95={percentile(timings, 95):.4f} ms"
        )

    if all_times:
        print("\n📊 RESUMO")
        print(f"Média por jogador: {statistics.mean(all_times):.4f} ms")
        print(f"Mediana:           {statistics.median(all_times):.4f} ms")
        print(f"P95:               {percentile(all_times, 95):.4f} ms")
        print(
            "Média estimada para 8 jogadores ativos: "
            f"{statistics.mean(all_times) * 8:.4f} ms"
        )

    print("\n✅ Benchmark concluído.")


if __name__ == "__main__":
    main()


#🚀 Criando lobby para benchmark...
#[UnitManager] 64 unidades carregadas.
#[UnitManager] Catálogo: C:\Users\Victor\Desktop\dev\Projects\TFT\units_gerado.json
#👥 Jogadores ativos: 8
#💀 Jogadores eliminados: 0
#🔥 Aquecimento: 50 chamadas por jogador
#📏 Amostras: 500 por jogador

#Jogador 0: média=0.1807 ms | mediana=0.1783 ms | P95=0.1855 ms
#Jogador 1: média=0.1887 ms | mediana=0.1758 ms | P95=0.3380 ms
#Jogador 2: média=0.1765 ms | mediana=0.1733 ms | P95=0.1896 ms
#Jogador 3: média=0.1765 ms | mediana=0.1702 ms | P95=0.2118 ms
#Jogador 4: média=0.1853 ms | mediana=0.1785 ms | P95=0.2170 ms
#Jogador 5: média=0.1999 ms | mediana=0.1763 ms | P95=0.3469 ms
#Jogador 6: média=0.1867 ms | mediana=0.1675 ms | P95=0.3262 ms
#Jogador 7: média=0.1937 ms | mediana=0.1713 ms | P95=0.3355 ms

#📊 RESUMO
#Média por jogador: 0.1860 ms
#Mediana:           0.1755 ms
#P95:               0.3248 ms
#Média estimada para 8 jogadores ativos: 1.4881 ms

#✅ Benchmark concluído.