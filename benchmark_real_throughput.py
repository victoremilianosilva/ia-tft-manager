# 🚀 benchmark_real_throughput.py
# Mede o fluxo real de decisão do PPO, sem atualizar os pesos.

import time
import numpy as np
import torch

from trainer import Trainer

NUM_LOBBIES = 4
WARMUP = 50
SAMPLES = 500


def main():
    trainer = None

    try:
        print("🚀 Inicializando Trainer e policy...")

        trainer = Trainer(
            num_envs=NUM_LOBBIES,
            use_subprocess=False,
        )

        trainer.policy.eval()

        # 🔄 Estado inicial das lobbies.
        raw_obs = trainer.vec_env.reset()
        obs_np = trainer._flatten_observations(raw_obs)

        obs = torch.as_tensor(
            obs_np,
            dtype=torch.float32,
            device=trainer.device,
        )

        timings = {
            "masks": [],
            "policy": [],
            "conversion": [],
            "env_step": [],
            "total": [],
        }

        def run_iteration(measure=False):
            nonlocal obs

            total_start = time.perf_counter()

            # 🎭 1. Máscaras reais de todos os jogadores.
            start = time.perf_counter()

            gym_masks = trainer.vec_env.env_method(
                "get_action_masks"
            )

            masks = trainer._flatten_masks(gym_masks)

            mask_elapsed = time.perf_counter() - start

            # 🧠 2. Inferência PPO com as máscaras.
            start = time.perf_counter()

            with torch.no_grad():
                actions, _, _, _ = trainer.policy.get_action(
                    obs,
                    masks=masks,
                )

            policy_elapsed = time.perf_counter() - start

            # 🔄 3. Conversão para o formato de cada lobby.
            start = time.perf_counter()

            lobby_actions = trainer._actions_to_lobby_format(
                actions
            )

            conversion_elapsed = time.perf_counter() - start

            # 🎮 4. Executa as ações no ambiente real.
            start = time.perf_counter()

            next_obs_raw, _, _, _ = trainer.vec_env.step(
                lobby_actions
            )

            step_elapsed = time.perf_counter() - start

            # 👀 Atualiza as observações para a próxima decisão.
            next_obs_np = trainer._flatten_observations(
                next_obs_raw
            )

            obs = torch.as_tensor(
                next_obs_np,
                dtype=torch.float32,
                device=trainer.device,
            )

            total_elapsed = time.perf_counter() - total_start

            if measure:
                timings["masks"].append(mask_elapsed)
                timings["policy"].append(policy_elapsed)
                timings["conversion"].append(conversion_elapsed)
                timings["env_step"].append(step_elapsed)
                timings["total"].append(total_elapsed)

        print("\n🔥 Aquecimento...")
        for _ in range(WARMUP):
            run_iteration()

        print(f"⏱️ Medindo {SAMPLES} decisões completas...")

        for i in range(SAMPLES):
            run_iteration(measure=True)

            if (i + 1) % 100 == 0:
                print(f"   Progresso: {i + 1}/{SAMPLES}")

        total_seconds = sum(timings["total"])
        num_agents = trainer.num_agents
        player_decisions = SAMPLES * num_agents

        print("\n" + "=" * 52)
        print("📈 THROUGHPUT REAL — FLUXO DE DECISÃO PPO")
        print("=" * 52)

        print(f"🏟️ Lobbies: {NUM_LOBBIES}")
        print(f"👥 Jogadores por lobby: {trainer.PLAYERS_PER_LOBBY}")
        print(f"🤖 Agentes por decisão: {num_agents}")
        print(f"🔁 Iterações medidas: {SAMPLES}")

        print("\n⏱️ TEMPO POR ETAPA")
        for name, values in timings.items():
            ms = np.asarray(values) * 1000

            print(
                f"   {name:12s} "
                f"Média: {ms.mean():8.3f} ms | "
                f"P95: {np.percentile(ms, 95):8.3f} ms"
            )

        print("\n⚡ THROUGHPUT")
        print(f"   Iterações/s:       {SAMPLES / total_seconds:.2f}")
        print(
            f"   Decisões/s:        "
            f"{player_decisions / total_seconds:.2f}"
        )
        print(f"   Tempo medido:      {total_seconds:.2f} s")

        # 🔬 Proporção aproximada do tempo por etapa.
        print("\n🔍 PARTICIPAÇÃO NO TEMPO")
        for name in ("masks", "policy", "conversion", "env_step"):
            stage_total = sum(timings[name])
            percentage = stage_total / total_seconds * 100

            print(f"   {name:12s}: {percentage:6.2f}%")

        print("\n✅ Benchmark concluído.")

    finally:
        if trainer is not None:
            trainer.vec_env.close()
            trainer.writer.close()


if __name__ == "__main__":
    main()