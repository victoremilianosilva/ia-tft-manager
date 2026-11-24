import math

import torch
import time
import os
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter


def exponential_schedule_value(progress, initial, final, decay_rate=2.0):
    """Exponential decay normalized to reach `initial` at 0 and `final` at 1."""
    values = (progress, initial, final, decay_rate)
    if not all(math.isfinite(float(value)) for value in values):
        raise ValueError("Os parâmetros do schedule devem ser finitos.")
    if initial < final or final < 0.0 or decay_rate <= 0.0:
        raise ValueError("Esperado initial >= final >= 0 e decay_rate > 0.")

    progress = min(1.0, max(0.0, float(progress)))
    decay_end = math.exp(-float(decay_rate))
    decay = (math.exp(-float(decay_rate) * progress) - decay_end) / (1.0 - decay_end)
    return float(final + (initial - final) * decay)


class PPOTrainer:

    def __init__(
        self,
        policy,
        optimizer,
        writer,
        clip_coef=0.2,
        ent_coef=0.02,
        vf_coef=0.5,
        max_grad_norm=0.5,
        target_kl=0.02
    ):
        """
        PPO Trainer compatível com Self-Play.

        ================================================================
        SELF-PLAY
        ================================================================

        A policy é compartilhada entre todos os jogadores.

            Player 0 ─┐
            Player 1  │
            Player 2  │
            ...       ├──> mesma TFTPolicy
            Player 7  │
                      │
                      └──> PPOTrainer

        O RolloutBuffer transforma:

            lobbies × 8 jogadores

        em um batch de agentes.

        Portanto, este trainer não precisa conhecer diretamente
        o conceito de lobby.
        """

        self.policy = policy
        self.optimizer = optimizer

        # ============================================================
        # PPO CONFIG
        # ============================================================

        self.clip_coef = clip_coef
        self.ent_coef = ent_coef
        self.vf_coef = vf_coef

        self.max_grad_norm = max_grad_norm
        self.target_kl = target_kl
        if not 0.0 < float(clip_coef) < 1.0:
            raise ValueError("clip_coef deve estar entre 0 e 1.")
        if float(vf_coef) < 0.0 or float(max_grad_norm) <= 0.0:
            raise ValueError("vf_coef deve ser >= 0 e max_grad_norm deve ser > 0.")
        if target_kl is not None and float(target_kl) <= 0.0:
            raise ValueError("target_kl deve ser > 0 ou None.")
        if float(ent_coef) < 0.0:
            raise ValueError("ent_coef deve ser >= 0.")

        # ============================================================
        # TENSORBOARD
        # ============================================================

        self.writer = writer
        self.update_step = 0

    # =================================================================
    # PPO LOSS
    # =================================================================

    def compute_loss(
        self,
        obs,
        actions,
        old_logprobs,
        old_values,
        advantages,
        returns,
        masks,
        semantic_state=None,
    ):
        """
        Calcula a loss PPO de um mini-batch.

        O batch pode conter experiências de vários jogadores,
        vários lobbies e vários rounds.

        A policy continua sendo compartilhada.
        """

        # ============================================================
        # POLICY EVALUATION
        # ============================================================

        (
            new_logprob,
            entropy,
            new_values
        ) = self.policy.evaluate_actions(
            obs,
            actions,
            masks=masks,
            semantic_state=semantic_state,
        )

        # ============================================================
        # GARANTIR SHAPES
        # ============================================================

        new_values = new_values.reshape(-1)
        old_values = old_values.reshape(-1)

        old_logprobs = old_logprobs.reshape(-1)

        advantages = advantages.reshape(-1)
        returns = returns.reshape(-1)

        new_logprob = new_logprob.reshape(-1)
        entropy = entropy.reshape(-1)

        # ============================================================
        # PPO RATIO
        # ============================================================

        logratio = (
            new_logprob
            - old_logprobs
        )

        ratio = logratio.exp()

        # ============================================================
        # POLICY LOSS
        # ============================================================

        pg_loss1 = (
            -advantages * ratio
        )

        pg_loss2 = (
            -advantages
            * torch.clamp(
                ratio,
                1.0 - self.clip_coef,
                1.0 + self.clip_coef
            )
        )

        pg_loss = torch.max(
            pg_loss1,
            pg_loss2
        ).mean()

        # ============================================================
        # VALUE CLIPPING
        # ============================================================

        value_pred_clipped = (
            old_values
            + torch.clamp(
                new_values - old_values,
                -self.clip_coef,
                self.clip_coef
            )
        )

        value_loss_unclipped = (
            returns - new_values
        ).pow(2)

        value_loss_clipped = (
            returns - value_pred_clipped
        ).pow(2)

        v_loss = (
            0.5
            * torch.max(
                value_loss_unclipped,
                value_loss_clipped
            ).mean()
        )

        # ============================================================
        # ENTROPY
        # ============================================================

        entropy_loss = entropy.mean()

        # ============================================================
        # TOTAL LOSS
        # ============================================================

        loss = (
            pg_loss
            - self.ent_coef * entropy_loss
            + self.vf_coef * v_loss
        )

        # ============================================================
        # METRICS
        # ============================================================

        with torch.no_grad():

            # --------------------------------------------------------
            # Approximate KL
            # --------------------------------------------------------

            # Estimador não negativo: E[(r - 1) - log(r)].
            # Mais estável que mean(old_logprob - new_logprob), que pode
            # ficar negativo por ruído amostral e mascarar divergência.
            approx_kl = (
                (ratio - 1.0) - logratio
            ).mean().clamp_min(0.0)

            # --------------------------------------------------------
            # Clip fraction
            # --------------------------------------------------------

            clip_fraction = (
                (
                    torch.abs(
                        ratio - 1.0
                    ) > self.clip_coef
                )
                .float()
                .mean()
            )

            # --------------------------------------------------------
            # Ratio médio
            # --------------------------------------------------------

            batch_ratio = ratio.mean()

        return (
            loss,
            pg_loss.detach(),
            v_loss.detach(),
            entropy_loss.detach(),
            approx_kl.detach(),
            clip_fraction.detach(),
            batch_ratio.detach()
        )

    # =================================================================
    # UPDATE
    # =================================================================

    def update(
        self,
        rollout,
        batch_size=256,
        epochs=4
    ):
        """
        Executa uma atualização PPO completa.

        ================================================================
        SELF-PLAY
        ================================================================

        O rollout pode conter:

            8 jogadores
            16 jogadores
            32 jogadores
            ...

        dependendo de quantos lobbies o Trainer estiver executando.

        O PPO não precisa saber a origem das experiências.
        """

        profile_update_start_ns = time.perf_counter_ns()
        profile_normalize_ms = 0.0
        profile_loss_ms = 0.0
        profile_backward_optimizer_ms = 0.0
        profile_metrics_ms = 0.0
        profile_batch_materialization_ms = 0.0
        profile_backward_ms = 0.0
        profile_gradient_clip_ms = 0.0
        profile_optimizer_step_ms = 0.0
        profile_minibatches = 0
        profile_cuda_device = next(self.policy.parameters()).device
        profile_gpu_enabled = (
            os.environ.get("TFT_PROFILE_GPU") == "1"
            and torch.cuda.is_available()
            and profile_cuda_device.type == "cuda"
        )
        profile_loss_cuda_events = []
        profile_backward_cuda_events = []

        # ============================================================
        # VALIDAR ROLLOUT
        # ============================================================

        if rollout.ptr <= 0:
            print("⚠️ PPO Update ignorado: rollout vazio.")
            return {}
        if batch_size <= 0 or epochs <= 0:
            raise ValueError("batch_size e epochs devem ser > 0.")

        # ============================================================
        # NORMALIZAÇÃO DAS ADVANTAGES
        # ============================================================

        normalize_start_ns = time.perf_counter_ns()
        rollout.normalize_advantages()
        profile_normalize_ms = (time.perf_counter_ns() - normalize_start_ns) / 1_000_000.0

        # ============================================================
        # MÉTRICAS
        # ============================================================

        mean_loss = 0.0
        mean_pg = 0.0
        mean_v = 0.0
        mean_entropy = 0.0
        mean_kl = 0.0
        mean_clipfrac = 0.0
        mean_ratio = 0.0
        max_kl = 0.0
        early_stop_kl = 0.0
        early_stop_triggered = False
        epochs_started = 0

        total_batches = 0
        attempted_batches = 0
        optimizer_steps = 0
        grad_norm_sum = 0.0
        grad_norm_max = 0.0

        stop_early = False

        def profiled_batches():
            nonlocal profile_batch_materialization_ms
            iterator = iter(rollout.get_batches(
                batch_size=batch_size,
                normalize_advantages=False,
                include_metadata=False,
            ))
            while True:
                batch_start_ns = time.perf_counter_ns()
                try:
                    batch = next(iterator)
                except StopIteration:
                    break
                profile_batch_materialization_ms += (time.perf_counter_ns() - batch_start_ns) / 1_000_000.0
                yield batch

        # ============================================================
        # PPO EPOCHS
        # ============================================================

        for epoch in range(epochs):

            if stop_early:
                break
            epochs_started = epoch + 1

            for batch in profiled_batches():
                attempted_batches += 1
                profile_minibatches += 1

                # ====================================================
                # COMPUTE LOSS
                # ====================================================

                loss_start_ns = time.perf_counter_ns()
                loss_cuda_start = loss_cuda_end = None
                if profile_gpu_enabled:
                    loss_cuda_start = torch.cuda.Event(enable_timing=True)
                    loss_cuda_end = torch.cuda.Event(enable_timing=True)
                    loss_cuda_start.record()
                (
                    loss,
                    pg_loss,
                    v_loss,
                    entropy_loss,
                    approx_kl,
                    clip_fraction,
                    batch_ratio
                ) = self.compute_loss(

                    batch["obs"],
                    batch["actions"],

                    batch["logprobs"],
                    batch["values"],

                    batch["advantages"],
                    batch["returns"],

                    batch["masks"],
                    semantic_state=batch["semantic_state"],
                )
                profile_loss_ms += (time.perf_counter_ns() - loss_start_ns) / 1_000_000.0
                if profile_gpu_enabled:
                    loss_cuda_end.record()
                    profile_loss_cuda_events.append((loss_cuda_start, loss_cuda_end))

                max_kl = max(max_kl, float(approx_kl.item()))

                # ====================================================
                # KL EARLY STOP — ANTES DO OPTIMIZER STEP
                # ====================================================
                # O minibatch que excede o limite não deve atualizar os pesos.
                # A checagem ocorre após avaliar a policy atual e antes do backward.
                if self.target_kl is not None and approx_kl.item() > self.target_kl:
                    stop_early = True
                    early_stop_triggered = True
                    early_stop_kl = float(approx_kl.item())
                    print(
                        f"🛑 PPO Early Stop | KL={approx_kl.item():.5f} "
                        f"> {self.target_kl:.5f}; minibatch ignorado"
                    )
                    break

                # ====================================================
                # SEGURANÇA NUMÉRICA
                # ====================================================

                if not torch.isfinite(loss):

                    print(
                        "⚠️ PPO: loss inválida. "
                        "Update interrompido."
                    )

                    stop_early = True
                    break

                # ====================================================
                # BACKPROP
                # ====================================================

                optimizer_stage_start_ns = time.perf_counter_ns()
                self.optimizer.zero_grad(
                    set_to_none=True
                )

                backward_cuda_start = backward_cuda_end = None
                if profile_gpu_enabled:
                    backward_cuda_start = torch.cuda.Event(enable_timing=True)
                    backward_cuda_end = torch.cuda.Event(enable_timing=True)
                    backward_cuda_start.record()
                backward_start_ns = time.perf_counter_ns()
                loss.backward()
                profile_backward_ms += (time.perf_counter_ns() - backward_start_ns) / 1_000_000.0

                # ====================================================
                # GRADIENT CLIPPING
                # ====================================================

                clip_start_ns = time.perf_counter_ns()
                grad_norm = torch.nn.utils.clip_grad_norm_(
                    self.policy.parameters(),
                    self.max_grad_norm,
                )
                profile_gradient_clip_ms += (time.perf_counter_ns() - clip_start_ns) / 1_000_000.0
                grad_norm_value = float(grad_norm.detach().item())
                grad_norm_sum += grad_norm_value
                grad_norm_max = max(grad_norm_max, grad_norm_value)

                optimizer_step_start_ns = time.perf_counter_ns()
                self.optimizer.step()
                profile_optimizer_step_ms += (time.perf_counter_ns() - optimizer_step_start_ns) / 1_000_000.0
                profile_backward_optimizer_ms += (time.perf_counter_ns() - optimizer_stage_start_ns) / 1_000_000.0
                if profile_gpu_enabled:
                    backward_cuda_end.record()
                    profile_backward_cuda_events.append((backward_cuda_start, backward_cuda_end))
                optimizer_steps += 1

                # ====================================================
                # MÉTRICAS
                # ====================================================

                metrics_stage_start_ns = time.perf_counter_ns()
                mean_loss += loss.item()
                mean_pg += pg_loss.item()
                mean_v += v_loss.item()
                mean_entropy += entropy_loss.item()
                mean_kl += approx_kl.item()
                mean_clipfrac += clip_fraction.item()

                # ====================================================
                # CORREÇÃO:
                #
                # O valor retornado pelo batch agora é chamado
                # batch_ratio, enquanto mean_ratio continua sendo
                # apenas o acumulador.
                # ====================================================

                mean_ratio += batch_ratio.item()

                total_batches += 1
                profile_metrics_ms += (time.perf_counter_ns() - metrics_stage_start_ns) / 1_000_000.0


        # ============================================================
        # TENSORBOARD
        # ============================================================

        if total_batches > 0:

            mean_loss /= total_batches
            mean_pg /= total_batches
            mean_v /= total_batches
            mean_entropy /= total_batches
            mean_kl /= total_batches
            mean_clipfrac /= total_batches
            mean_ratio /= total_batches

            # --------------------------------------------------------
            # LOSS
            # --------------------------------------------------------

            self.writer.add_scalar(
                "loss/total",
                mean_loss,
                self.update_step
            )

            self.writer.add_scalar(
                "loss/policy",
                mean_pg,
                self.update_step
            )

            self.writer.add_scalar(
                "loss/value",
                mean_v,
                self.update_step
            )

            self.writer.add_scalar(
                "loss/entropy",
                mean_entropy,
                self.update_step
            )

            # --------------------------------------------------------
            # PPO
            # --------------------------------------------------------

            self.writer.add_scalar(
                "ppo/approx_kl",
                mean_kl,
                self.update_step
            )

            self.writer.add_scalar(
                "ppo/clip_fraction",
                mean_clipfrac,
                self.update_step
            )

            self.writer.add_scalar(
                "ppo/mean_ratio",
                mean_ratio,
                self.update_step
            )

            self.writer.add_scalar("ppo/approx_kl_max", max_kl, self.update_step)
            if self.target_kl is not None:
                self.writer.add_scalar("ppo/target_kl", float(self.target_kl), self.update_step)
            self.writer.add_scalar("ppo/attempted_batches", attempted_batches, self.update_step)
            self.writer.add_scalar("ppo/optimizer_steps", optimizer_steps, self.update_step)
            self.writer.add_scalar("ppo/grad_norm_mean", grad_norm_sum / max(1, optimizer_steps), self.update_step)
            self.writer.add_scalar("ppo/grad_norm_max", grad_norm_max, self.update_step)
            self.writer.add_scalar("ppo/early_stop_rate", float(early_stop_triggered), self.update_step)
            self.writer.add_scalar("ppo/early_stop", float(early_stop_triggered), self.update_step)
            self.writer.add_scalar("ppo/early_stop_kl", early_stop_kl, self.update_step)
            self.writer.add_scalar("ppo/batches_processed", total_batches, self.update_step)
            self.writer.add_scalar("ppo/epochs_started", epochs_started, self.update_step)

            # --------------------------------------------------------
            # SELF-PLAY / ROLLOUT
            # --------------------------------------------------------

            valid_mask = rollout.valid[:rollout.ptr]

            valid_rewards = (
                rollout.rewards[:rollout.ptr][valid_mask]
            )

            valid_dones = (
                rollout.dones[:rollout.ptr][valid_mask]
            )

            valid_transitions = int(
                valid_mask.sum().item()
            )

            self.writer.add_scalar(
                "rollout/num_agents",
                rollout.num_envs,
                self.update_step
            )

            self.writer.add_scalar(
                "rollout/transitions",
                valid_transitions,
                self.update_step
            )

            self.writer.add_scalar(
                "rollout/mean_reward",
                valid_rewards.mean().item(),
                self.update_step
            )

            self.writer.add_scalar(
                "rollout/mean_done",
                valid_dones.mean().item(),
                self.update_step
            )

            # --------------------------------------------------------
            # TRAINING
            # --------------------------------------------------------

            self.writer.add_scalar(
                "training/epochs",
                epochs,
                self.update_step
            )

            self.writer.add_scalar(
                "training/batch_size",
                batch_size,
                self.update_step
            )

        if profile_gpu_enabled and (profile_loss_cuda_events or profile_backward_cuda_events):
            torch.cuda.synchronize(profile_cuda_device)
        if hasattr(self, "writer") and self.writer is not None:
            self.writer.add_scalar("performance/ppo/advantage_normalization_ms", profile_normalize_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/batch_materialization_ms", profile_batch_materialization_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/backward_ms", profile_backward_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/gradient_clip_ms", profile_gradient_clip_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/optimizer_step_ms", profile_optimizer_step_ms, self.update_step)
            if profile_gpu_enabled:
                self.writer.add_scalar("performance/gpu/ppo_compute_loss_ms", sum(a.elapsed_time(b) for a, b in profile_loss_cuda_events), self.update_step)
                self.writer.add_scalar("performance/gpu/ppo_backward_clip_optimizer_ms", sum(a.elapsed_time(b) for a, b in profile_backward_cuda_events), self.update_step)
            self.writer.add_scalar("performance/ppo/compute_loss_total_ms", profile_loss_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/backward_optimizer_total_ms", profile_backward_optimizer_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/metric_sync_total_ms", profile_metrics_ms, self.update_step)
            self.writer.add_scalar("performance/ppo/profiled_minibatches", profile_minibatches, self.update_step)
            self.writer.add_scalar("performance/ppo/update_internal_total_ms", (time.perf_counter_ns() - profile_update_start_ns) / 1_000_000.0, self.update_step)

        # ============================================================
        # UPDATE COUNTER
        # ============================================================

        self.update_step += 1
        return {
            "approx_kl_mean": mean_kl,
            "approx_kl_max": max_kl,
            "early_stop": early_stop_triggered,
            "early_stop_kl": early_stop_kl,
            "batches_processed": total_batches,
            "attempted_batches": attempted_batches,
            "optimizer_steps": optimizer_steps,
            "grad_norm_mean": grad_norm_sum / max(1, optimizer_steps),
            "grad_norm_max": grad_norm_max,
            "epochs_started": epochs_started,
        }
