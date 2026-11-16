import torch


class RolloutBuffer:
    """
    RolloutBuffer para PPO com Self-Play.

    ================================================================
    MODELO DE DADOS
    ================================================================

    O buffer NÃO precisa conhecer diretamente o conceito de "lobby".

    O Trainer pode transformar:

        N lobbies × 8 jogadores

    em:

        N * 8 agentes

    Exemplo:

        4 lobbies × 8 jogadores = 32 agentes

    O buffer então trabalha com:

        num_steps × 32

    Cada agente possui seu próprio:

        - observation
        - action
        - reward
        - done
        - value
        - advantage
        - return
        - action masks

    ================================================================
    SELF-PLAY
    ================================================================

    É importante que `dones` seja individual.

    Exemplo:

        Player 0 -> eliminado
        Player 1 -> vivo
        Player 2 -> vivo
        ...

    Então:

        dones = [1, 0, 0, 0, 0, 0, 0, 0]

    O GAE do Player 0 termina naquele ponto enquanto os outros
    continuam normalmente.

    ================================================================
    """

    def __init__(
        self,
        num_steps,
        num_envs,
        obs_dim,
        action_dim,
        device,
        mask_shapes=None
    ):
        self.device = device

        self.num_steps = int(num_steps)

        # ============================================================
        # AGENTES
        # ============================================================
        #
        # IMPORTANTE:
        #
        # No self-play, `num_envs` representa o número de agentes
        # simultaneamente coletados pelo Trainer.
        #
        # Exemplo:
        #
        #   4 lobbies × 8 jogadores = 32
        #
        #   num_envs = 32
        #
        # ============================================================

        self.num_envs = int(num_envs)

        self.obs_dim = int(obs_dim)
        self.action_dim = int(action_dim)

        self.total_transitions = (
            self.num_steps * self.num_envs
        )

        self.ptr = 0
        # Non-tensor correlation metadata, indexed exactly like rollout transitions.
        self.snapshot_metadata = [None for _ in range(self.num_steps)]
        self.result_snapshot_metadata = [None for _ in range(self.num_steps)]
        self.next_snapshot_metadata = [None for _ in range(self.num_steps)]

        # ============================================================
        # DADOS PRINCIPAIS
        # ============================================================

        self.obs = torch.zeros(
            (
                self.num_steps,
                self.num_envs,
                self.obs_dim
            ),
            dtype=torch.float32,
            device=self.device
        )

        self.actions = torch.zeros(
            (
                self.num_steps,
                self.num_envs,
                self.action_dim
            ),
            dtype=torch.long,
            device=self.device
        )

        self.logprobs = torch.zeros(
            (
                self.num_steps,
                self.num_envs
            ),
            dtype=torch.float32,
            device=self.device
        )

        self.rewards = torch.zeros(
            (
                self.num_steps,
                self.num_envs
            ),
            dtype=torch.float32,
            device=self.device
        )

        # ============================================================
        # DONE INDIVIDUAL
        # ============================================================
        #
        # Cada jogador possui seu próprio episódio.
        #
        # Isso é essencial no self-play.
        #
        # Exemplo:
        #
        # P0 morreu:
        #
        # dones[t] =
        # [1, 0, 0, 0, 0, 0, 0, 0]
        #
        # O GAE do P0 é interrompido.
        # Os outros jogadores continuam.
        #
        # ============================================================

        self.dones = torch.zeros(
            (
                self.num_steps,
                self.num_envs
            ),
            dtype=torch.float32,
            device=self.device
        )

        self.values = torch.zeros(
            (
                self.num_steps,
                self.num_envs
            ),
            dtype=torch.float32,
            device=self.device
        )

        # ============================================================
        # GAE / RETURNS
        # ============================================================

        self.advantages = torch.zeros(
            (
                self.num_steps,
                self.num_envs
            ),
            dtype=torch.float32,
            device=self.device
        )

        self.returns = torch.zeros(
            (
                self.num_steps,
                self.num_envs
            ),
            dtype=torch.float32,
            device=self.device
        )

        self.valid = torch.zeros(
            (self.num_steps, self.num_envs),
            dtype=torch.bool,
            device=self.device,
        )

        # ============================================================
        # ACTION MASKS
        # ============================================================

        self.masks = {}

        if mask_shapes is not None:

            for name, shape in mask_shapes.items():

                self.masks[name] = torch.zeros(
                    (
                        self.num_steps,
                        self.num_envs,
                        *shape
                    ),
                    dtype=torch.bool,
                    device=self.device
                )

    # =================================================================
    # ADD
    # =================================================================

    def add(
        self,
        obs,
        actions,
        logprobs,
        rewards,
        dones,
        values,
        masks_dict,
        valid=None,
        snapshot_metadata=None,
        result_snapshot_metadata=None,
        next_snapshot_metadata=None,
    ):
        """
        Adiciona uma transição de todos os agentes.

        No self-play:

            obs.shape
                [num_agents, obs_dim]

            actions.shape
                [num_agents, action_dim]

            rewards.shape
                [num_agents]

            dones.shape
                [num_agents]

        Onde:

            num_agents = num_lobbies * 8
        """
        if self.ptr >= self.num_steps:
            raise RuntimeError(
                f"RolloutBuffer cheio: "
                f"ptr={self.ptr}, "
                f"num_steps={self.num_steps}"
            )

        if valid is None:
            valid = torch.ones(
                self.num_envs,
                dtype=torch.bool,
                device=self.device,
            )
        else:
            valid = self._to_tensor(
                valid,
                dtype=torch.bool,
            )

        if tuple(valid.shape) != (self.num_envs,):
            raise ValueError(
                f"Shape inválido para valid: {tuple(valid.shape)}"
            )

        self.valid[self.ptr].copy_(valid)

        # ============================================================
        # CONVERSÃO PARA TENSOR
        # ============================================================

        obs = self._to_tensor(
            obs,
            dtype=torch.float32
        )

        actions = self._to_tensor(
            actions,
            dtype=torch.long
        )

        logprobs = self._to_tensor(
            logprobs,
            dtype=torch.float32
        )

        rewards = self._to_tensor(
            rewards,
            dtype=torch.float32
        )

        dones = self._to_tensor(
            dones,
            dtype=torch.float32
        )

        values = self._to_tensor(
            values,
            dtype=torch.float32
        )

        # ============================================================
        # VALIDAR BATCH
        # ============================================================

        self._validate_step_shapes(
            obs,
            actions,
            logprobs,
            rewards,
            dones,
            values
        )

        metadata_groups = (
            ("snapshot_metadata", snapshot_metadata),
            ("result_snapshot_metadata", result_snapshot_metadata),
            ("next_snapshot_metadata", next_snapshot_metadata),
        )
        supplied_groups = [value is not None for _, value in metadata_groups]
        if any(supplied_groups) and not all(supplied_groups):
            raise ValueError(
                "Identidade da decisão, resultado e próxima observação devem ser "
                "armazenadas juntas."
            )

        if self.ptr > 0:
            previous_has_identity = self.snapshot_metadata[0] is not None
            if previous_has_identity != all(supplied_groups):
                raise ValueError(
                    "O rollout não pode misturar transições com e sem identidade."
                )

        normalized_groups = {}
        if all(supplied_groups):
            for group_name, group in metadata_groups:
                if len(group) != self.num_envs:
                    raise ValueError(
                        f"{group_name} deve conter uma identidade por agente: "
                        f"{len(group)} != {self.num_envs}"
                    )
                normalized = []
                for index, metadata in enumerate(group):
                    if not isinstance(metadata, dict):
                        raise TypeError(f"{group_name}[{index}] deve ser um dicionário.")
                    required = (
                        "engine_instance_id", "episode_id",
                        "decision_sequence", "player_id", "lobby_index",
                    )
                    missing = [key for key in required if key not in metadata]
                    if missing:
                        raise ValueError(
                            f"{group_name}[{index}] sem campos obrigatórios: {missing}"
                        )
                    sequence = metadata["decision_sequence"]
                    if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 0:
                        raise ValueError(
                            f"{group_name}[{index}].decision_sequence deve ser inteiro não negativo."
                        )
                    normalized.append(dict(metadata))
                normalized_groups[group_name] = normalized

            for index, (decision, result, next_state) in enumerate(zip(
                normalized_groups["snapshot_metadata"],
                normalized_groups["result_snapshot_metadata"],
                normalized_groups["next_snapshot_metadata"],
            )):
                if decision["player_id"] != result["player_id"] or decision["player_id"] != next_state["player_id"]:
                    raise ValueError(f"Identidade de player divergente na transição {index}.")
                if decision["lobby_index"] != result["lobby_index"] or decision["lobby_index"] != next_state["lobby_index"]:
                    raise ValueError(f"Identidade de lobby divergente na transição {index}.")
                if decision["engine_instance_id"] != result["engine_instance_id"] or decision["engine_instance_id"] != next_state["engine_instance_id"]:
                    raise ValueError(f"Engine divergente na transição {index}.")
                if decision["episode_id"] != result["episode_id"]:
                    raise ValueError(f"Episode divergente entre decisão e resultado na transição {index}.")
                action_trace = result.get("action_trace")
                if action_trace is None:
                    raise ValueError(
                        f"result_snapshot_metadata[{index}].action_trace é obrigatório para transições identificadas."
                    )
                if not isinstance(action_trace, dict):
                    raise TypeError(
                        f"result_snapshot_metadata[{index}].action_trace deve ser um dicionário."
                    )
                for action_field in ("requested_action", "effective_action"):
                    action_values = action_trace.get(action_field)
                    if not isinstance(action_values, (list, tuple)) or len(action_values) != actions.shape[1]:
                        raise ValueError(
                            f"result_snapshot_metadata[{index}].action_trace.{action_field} "
                            f"deve conter {actions.shape[1]} parâmetros."
                        )
                    try:
                        normalized_values = [int(value) for value in action_values]
                    except (TypeError, ValueError, OverflowError) as exc:
                        raise ValueError(
                            f"result_snapshot_metadata[{index}].action_trace.{action_field} "
                            "deve conter inteiros."
                        ) from exc
                    if any(isinstance(value, bool) or int(value) != value for value in action_values):
                        raise ValueError(
                            f"result_snapshot_metadata[{index}].action_trace.{action_field} "
                            "deve conter inteiros sem coerção."
                        )
                    if action_field == "requested_action":
                        stored_action = actions[index].detach().cpu().tolist()
                        if normalized_values != stored_action:
                            raise ValueError(
                                f"Ação PPO diverge da ação solicitada à Engine na transição {index}: "
                                f"{stored_action} != {normalized_values}."
                            )
                if not isinstance(action_trace.get("handler_applied"), bool):
                    raise ValueError(
                        f"result_snapshot_metadata[{index}].action_trace.handler_applied deve ser booleano."
                    )
                status_reason = action_trace.get("status_reason")
                if not isinstance(status_reason, str) or not status_reason.strip():
                    raise ValueError(
                        f"result_snapshot_metadata[{index}].action_trace.status_reason deve ser texto não vazio."
                    )
                if result["decision_sequence"] <= decision["decision_sequence"]:
                    raise ValueError(f"Sequência do resultado não avança na transição {index}.")
                if next_state["episode_id"] == result["episode_id"]:
                    if next_state["decision_sequence"] != result["decision_sequence"]:
                        raise ValueError(f"Próximo snapshot não corresponde ao resultado na transição {index}.")
                elif next_state["episode_id"] <= result["episode_id"] or next_state["decision_sequence"] <= result["decision_sequence"]:
                    raise ValueError(f"Auto-reset não avança identidade na transição {index}.")

                mask_hash = decision.get("mask_snapshot_hash")
                if not isinstance(mask_hash, str) or len(mask_hash) != 64 or any(
                    char not in "0123456789abcdef" for char in mask_hash
                ):
                    raise ValueError(
                        f"snapshot_metadata[{index}].mask_snapshot_hash deve ser SHA-256 hexadecimal."
                    )
                if decision.get("mask_snapshot_hash_algorithm") != "tft-action-mask-snapshot-v1":
                    raise ValueError(
                        f"snapshot_metadata[{index}] usa algoritmo de hash de mask desconhecido."
                    )

            for group_name, group in normalized_groups.items():
                by_lobby = {}
                for metadata in group:
                    key = metadata["lobby_index"]
                    identity = (
                        metadata["engine_instance_id"],
                        metadata["episode_id"],
                        metadata["decision_sequence"],
                    )
                    previous = by_lobby.setdefault(key, identity)
                    if previous != identity:
                        raise ValueError(
                            f"Snapshot inconsistente em {group_name} dentro da lobby {key}."
                        )

        for group_name, normalized in normalized_groups.items():
            getattr(self, group_name)[self.ptr] = normalized
        if not all(supplied_groups):
            self.snapshot_metadata[self.ptr] = None
            self.result_snapshot_metadata[self.ptr] = None
            self.next_snapshot_metadata[self.ptr] = None

        # ============================================================
        # SALVAR
        # ============================================================

        self.obs[self.ptr].copy_(obs)
        self.actions[self.ptr].copy_(actions)
        self.logprobs[self.ptr].copy_(logprobs)
        self.rewards[self.ptr].copy_(rewards)
        self.dones[self.ptr].copy_(dones)
        self.values[self.ptr].copy_(values)

        # ============================================================
        # MÁSCARAS
        # ============================================================

        if masks_dict is None:
            masks_dict = {}

        for key, mask_tensor in masks_dict.items():

            mask_tensor = self._to_tensor(
                mask_tensor,
                dtype=torch.bool
            )

            # --------------------------------------------------------
            # Se a máscara ainda não existe, cria dinamicamente.
            # --------------------------------------------------------

            if key not in self.masks:

                if mask_tensor.ndim < 2:
                    raise ValueError(
                        f"Máscara '{key}' inválida. "
                        f"Esperado pelo menos 2 dimensões."
                    )

                self.masks[key] = torch.zeros(
                    (
                        self.num_steps,
                        self.num_envs,
                        *mask_tensor.shape[1:]
                    ),
                    dtype=torch.bool,
                    device=self.device
                )

            # --------------------------------------------------------
            # Validação
            # --------------------------------------------------------

            expected_shape = (
                self.num_envs,
                *self.masks[key].shape[2:]
            )

            if tuple(mask_tensor.shape) != expected_shape:

                raise ValueError(
                    f"Shape inválido para máscara '{key}': "
                    f"recebido={tuple(mask_tensor.shape)}, "
                    f"esperado={expected_shape}"
                )

            self.masks[key][self.ptr].copy_(mask_tensor)

        # ============================================================
        # PRÓXIMO PASSO
        # ============================================================

        self.ptr += 1

    # =================================================================
    # TENSOR HELPER
    # =================================================================

    def _to_tensor(
        self,
        value,
        dtype
    ):
        """
        Converte numpy/list/tensor para tensor no device correto.
        """

        if isinstance(value, torch.Tensor):

            return value.to(
                device=self.device,
                dtype=dtype
            )

        return torch.as_tensor(
            value,
            dtype=dtype,
            device=self.device
        )

    # =================================================================
    # VALIDATE
    # =================================================================

    def _validate_step_shapes(
        self,
        obs,
        actions,
        logprobs,
        rewards,
        dones,
        values
    ):
        """
        Garante que todos os agentes estejam sincronizados.

        Isso ajuda bastante a detectar problemas quando o lobby
        possuir jogadores eliminados.
        """

        expected_obs = (
            self.num_envs,
            self.obs_dim
        )

        expected_actions = (
            self.num_envs,
            self.action_dim
        )

        expected_vector = (
            self.num_envs,
        )

        if tuple(obs.shape) != expected_obs:

            raise ValueError(
                f"obs com shape inválido: "
                f"{tuple(obs.shape)} != {expected_obs}"
            )

        if tuple(actions.shape) != expected_actions:

            raise ValueError(
                f"actions com shape inválido: "
                f"{tuple(actions.shape)} != {expected_actions}"
            )

        if tuple(logprobs.shape) != expected_vector:

            raise ValueError(
                f"logprobs com shape inválido: "
                f"{tuple(logprobs.shape)} != {expected_vector}"
            )

        if tuple(rewards.shape) != expected_vector:

            raise ValueError(
                f"rewards com shape inválido: "
                f"{tuple(rewards.shape)} != {expected_vector}"
            )

        if tuple(dones.shape) != expected_vector:

            raise ValueError(
                f"dones com shape inválido: "
                f"{tuple(dones.shape)} != {expected_vector}"
            )

        if tuple(values.shape) != expected_vector:

            raise ValueError(
                f"values com shape inválido: "
                f"{tuple(values.shape)} != {expected_vector}"
            )

    # =================================================================
    # GAE
    # =================================================================

    def compute_returns_and_advantages(
        self,
        next_value,
        next_done,
        gamma=0.99,
        gae_lambda=0.95
    ):
        """
        Calcula GAE separadamente para cada agente.

        ==============================================================
        SELF-PLAY
        ==============================================================

        `num_envs` pode representar:

            lobby_count × 8

        Cada índice é tratado independentemente.

        Exemplo:

            agent 0 -> morreu
            agent 1 -> vivo
            agent 2 -> vivo

        O done do agent 0 não interfere nos demais.

        ==============================================================
        """

        with torch.no_grad():

            # --------------------------------------------------------
            # Converter entradas
            # --------------------------------------------------------

            next_value = self._to_tensor(
                next_value,
                dtype=torch.float32
            ).reshape(self.num_envs)

            next_done = self._to_tensor(
                next_done,
                dtype=torch.float32
            ).reshape(self.num_envs)

            # --------------------------------------------------------
            # GAE atual de cada agente
            # --------------------------------------------------------

            gae = torch.zeros(
                self.num_envs,
                dtype=torch.float32,
                device=self.device
            )

            # --------------------------------------------------------
            # Backward pass
            # --------------------------------------------------------

            for t in range(
                self.num_steps - 1,
                -1,
                -1
            ):

                if t == self.num_steps - 1:

                    # Depois do último passo coletado
                    next_non_terminal = (
                        1.0 - next_done
                    )

                    next_values = next_value

                else:

                    # ------------------------------------------------
                    # O done produzido pela ação t determina se
                    # podemos utilizar V(s[t+1]).
                    # ------------------------------------------------

                    next_non_terminal = (
                        1.0 - self.dones[t]
                    )

                    next_values = (
                        self.values[t + 1]
                    )

                # ----------------------------------------------------
                # TD ERROR
                # ----------------------------------------------------

                delta = (
                    self.rewards[t]
                    + gamma
                    * next_values
                    * next_non_terminal
                    - self.values[t]
                )

                # ----------------------------------------------------
                # GAE
                # ----------------------------------------------------

                gae = (
                    delta
                    + gamma
                    * gae_lambda
                    * next_non_terminal
                    * gae
                )

                self.advantages[t] = gae

            # ========================================================
            # RETURNS
            # ========================================================

            self.returns = (
                self.advantages
                + self.values
            )

    # =================================================================
    # NORMALIZE ADVANTAGES
    # =================================================================

    def normalize_advantages(self, eps=1e-8):
        """
        Normaliza vantagens somente das transições válidas.
        As transições inválidas não participam da média/desvio.
        """
        if self.ptr <= 0:
            return

        valid_mask = self.valid[:self.ptr]

        if not valid_mask.any():
            return

        valid_advantages = self.advantages[:self.ptr][valid_mask]

        mean = valid_advantages.mean()
        std = valid_advantages.std(unbiased=False)

        normalized = (
            valid_advantages - mean
        ) / (
            std + eps
        )

        self.advantages[:self.ptr][valid_mask] = normalized

    # =================================================================
    # BATCHES
    # =================================================================

    def get_batches(
        self,
        batch_size,
        normalize_advantages=False
    ):
        """
        Gera mini-lotes contendo exclusivamente transições válidas.
        """

        if self.ptr <= 0:
            raise RuntimeError(
                "Não é possível gerar batches: RolloutBuffer está vazio."
            )

        steps = self.ptr
        total_transitions = steps * self.num_envs

        # 🔎 Seleciona apenas experiências válidas.
        valid_indices = torch.nonzero(
            self.valid[:steps].reshape(-1),
            as_tuple=False,
        ).squeeze(-1)

        if valid_indices.numel() == 0:
            return

        # 🎲 Embaralha somente os índices válidos.
        indices = valid_indices[
            torch.randperm(
                valid_indices.numel(),
                device=self.device,
            )
        ]

        flat_obs = self.obs[:steps].reshape(
            total_transitions, self.obs_dim
        )

        flat_actions = self.actions[:steps].reshape(
            total_transitions, self.action_dim
        )

        flat_logprobs = self.logprobs[:steps].reshape(
            total_transitions
        )

        flat_advantages = self.advantages[:steps].reshape(
            total_transitions
        )

        flat_returns = self.returns[:steps].reshape(
            total_transitions
        )

        flat_values = self.values[:steps].reshape(
            total_transitions
        )

        flat_masks = {
            key: tensor[:steps].reshape(
                total_transitions,
                *tensor.shape[2:]
            )
            for key, tensor in self.masks.items()
        }

        # 📦 Cria mini-lotes apenas com os índices válidos.
        for start in range(0, indices.numel(), batch_size):
            batch_idx = indices[start:start + batch_size]

            batch_advantages = flat_advantages[batch_idx]

            if normalize_advantages:
                batch_advantages = (
                    batch_advantages - batch_advantages.mean()
                ) / (
                    batch_advantages.std(unbiased=False) + 1e-8
                )

            yield {
                "obs": flat_obs[batch_idx],
                "actions": flat_actions[batch_idx],
                "logprobs": flat_logprobs[batch_idx],
                "advantages": batch_advantages,
                "returns": flat_returns[batch_idx],
                "values": flat_values[batch_idx],
                "masks": {
                    key: value[batch_idx]
                    for key, value in flat_masks.items()
                },
                "snapshot_metadata": self._metadata_for_batch(
                    self.snapshot_metadata, batch_idx
                ),
                "result_snapshot_metadata": self._metadata_for_batch(
                    self.result_snapshot_metadata, batch_idx
                ),
                "next_snapshot_metadata": self._metadata_for_batch(
                    self.next_snapshot_metadata, batch_idx
                ),
            }

    @staticmethod
    def _metadata_for_batch(metadata_by_step, batch_indices):
        if not metadata_by_step or metadata_by_step[0] is None:
            return None
        num_envs = len(metadata_by_step[0])
        result = []
        for flat_index in batch_indices.detach().cpu().tolist():
            step_index, env_index = divmod(int(flat_index), num_envs)
            step_metadata = metadata_by_step[step_index]
            if step_metadata is None:
                raise RuntimeError("Metadata parcial dentro do RolloutBuffer.")
            result.append(dict(step_metadata[env_index]))
        return result

    # =================================================================
    # READY
    # =================================================================

    def is_full(self):
        """Indica se o rollout atingiu num_steps."""

        return self.ptr >= self.num_steps

    # =================================================================
    # SIZE
    # =================================================================

    def size(self):
        """
        Retorna o número de transições armazenadas.
        """

        return self.ptr * self.num_envs

    # =================================================================
    # RESET
    # =================================================================

    def reset(self):
        """
        Limpa o rollout atual.

        Os tensores são reutilizados para evitar alocações
        desnecessárias a cada rollout.
        """

        for index in range(self.ptr):
            self.snapshot_metadata[index] = None
            self.result_snapshot_metadata[index] = None
            self.next_snapshot_metadata[index] = None
        self.ptr = 0

        # ------------------------------------------------------------
        # Não precisamos zerar todos os tensores aqui.
        #
        # O próximo rollout sobrescreverá as posições utilizadas.
        # ------------------------------------------------------------

    # =================================================================
    # DEBUG
    # =================================================================

    def debug_info(self):
        """
        Informações úteis para verificar o self-play.
        """

        return {
            "num_steps": self.num_steps,
            "num_agents": self.num_envs,
            "total_transitions": self.size(),
            "obs_dim": self.obs_dim,
            "action_dim": self.action_dim,
            "ptr": self.ptr,
            "full": self.is_full(),
            "mask_names": list(self.masks.keys()),
        }