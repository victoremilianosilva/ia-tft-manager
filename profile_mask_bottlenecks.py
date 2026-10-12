
import cProfile
import pstats
import time
import numpy as np
import torch

from trainer import Trainer


def report_times(name, samples):
    samples = np.asarray(samples, dtype=np.float64) * 1000

    print(f"\n{name}")
    print(f"  Média:   {samples.mean():.3f} ms")
    print(f"  Mediana: {np.median(samples):.3f} ms")
    print(f"  P95:     {np.percentile(samples, 95):.3f} ms")


def main():
    trainer = Trainer(num_envs=4, use_subprocess=False)
    trainer.policy.eval()

    try:
        # 📦 Prepara as observações no formato usado pelo PPO.
        obs_np = trainer._flatten_observations(
            trainer.vec_env.reset()
        )
        obs = torch.as_tensor(obs_np, dtype=torch.float32)

        # 🔥 Aquecimento com ações reais da política.
        print("🔥 Aquecendo o ambiente...")
        with torch.no_grad():
            for i in range(50):
                raw_masks = trainer.vec_env.env_method(
                    "get_action_masks"
                )
                masks = trainer._flatten_masks(raw_masks)

                actions, _, _, _ = trainer.policy.get_action(
                    obs, masks=masks
                )

                lobby_actions = trainer._actions_to_lobby_format(
                    actions
                )

                next_obs, _, _, _ = trainer.vec_env.step(
                    lobby_actions
                )

                obs = torch.as_tensor(
                    trainer._flatten_observations(next_obs),
                    dtype=torch.float32,
                )

                if (i + 1) % 10 == 0:
                    print(f"  {i + 1}/50")

        # ⏱️ Separa obtenção das máscaras e conversão.
        retrieval_times = []
        flatten_times = []
        full_times = []

        print("\n📏 Medindo 200 iterações...")
        for _ in range(200):
            start = time.perf_counter()
            raw_masks = trainer.vec_env.env_method(
                "get_action_masks"
            )
            middle = time.perf_counter()

            masks = trainer._flatten_masks(raw_masks)
            end = time.perf_counter()

            retrieval_times.append(middle - start)
            flatten_times.append(end - middle)
            full_times.append(end - start)

        report_times("Obtenção das máscaras (todas as lobbies)",
                     retrieval_times)
        report_times("Conversão _flatten_masks()", flatten_times)
        report_times("Fluxo completo das máscaras", full_times)

        # 🔬 Perfil das funções internas durante a geração.
        profiler = cProfile.Profile()
        profiler.enable()

        for _ in range(100):
            trainer.vec_env.env_method("get_action_masks")

        profiler.disable()

        print("\n🔎 FUNÇÕES INTERNAS — por tempo acumulado")
        stats = pstats.Stats(profiler)
        stats.strip_dirs().sort_stats("cumtime").print_stats(30)

        print("\n🔎 FUNÇÕES INTERNAS — por tempo próprio")
        stats.strip_dirs().sort_stats("tottime").print_stats(30)

    finally:
        trainer.vec_env.close()
        trainer.writer.close()


if __name__ == "__main__":
    main()
