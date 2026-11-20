import copy

from decision_identity import validate_player_identity_envelope

import torch

from action_contract import (
    MASK_SHAPES,
    MASK_SNAPSHOT_HASH_ALGORITHM,
    ACTION_CONTRACT_ID, ACTION_CONTRACT_VERSION, ACTION_CONTRACT_HASH,
    MASK_CONTRACT_ID, MASK_CONTRACT_VERSION, MASK_CONTRACT_HASH,
    hash_mask_row,
)
from semantic_observation import SEMANTIC_NUMERIC_DIM, SEMANTIC_ENTITY_SLOTS


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
        mask_shapes=None,
        semantic_numeric_dim=SEMANTIC_NUMERIC_DIM,
        semantic_entity_slots=SEMANTIC_ENTITY_SLOTS,
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
        self.semantic_numeric_dim = int(semantic_numeric_dim)
        self.semantic_entity_slots = int(semantic_entity_slots)
        if self.semantic_numeric_dim <= 0 or self.semantic_entity_slots <= 0:
            raise ValueError("semantic projection dimensions must be positive")

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

        self.semantic_numeric = torch.zeros(
            (self.num_steps, self.num_envs, self.semantic_numeric_dim),
            dtype=torch.float32,
            device=self.device,
        )
        self.semantic_champion_ids = torch.zeros(
            (self.num_steps, self.num_envs, self.semantic_entity_slots),
            dtype=torch.long,
            device=self.device,
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

        self.trajectory_valid = torch.zeros(
            (self.num_steps, self.num_envs),
            dtype=torch.bool,
            device=self.device,
        )
        self.optimization_valid = torch.zeros_like(self.trajectory_valid)
        # Backwards-compatible alias for historical PPO batch eligibility.
        self.valid = self.optimization_valid

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
        semantic_state=None,
        trajectory_valid=None,
        optimization_valid=None,
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

        if valid is not None and optimization_valid is not None:
            raise ValueError("Use valid (legado) ou optimization_valid, não ambos.")
        if optimization_valid is None:
            optimization_valid = valid
        if optimization_valid is None:
            optimization_valid = torch.ones(
                self.num_envs, dtype=torch.bool, device=self.device
            )
        else:
            optimization_valid = self._to_tensor(optimization_valid, dtype=torch.bool)

        if trajectory_valid is None:
            trajectory_valid = optimization_valid
        else:
            trajectory_valid = self._to_tensor(trajectory_valid, dtype=torch.bool)

        expected_valid_shape = (self.num_envs,)
        if tuple(trajectory_valid.shape) != expected_valid_shape:
            raise ValueError("Shape inválido para trajectory_valid.")
        if tuple(optimization_valid.shape) != expected_valid_shape:
            raise ValueError("Shape inválido para optimization_valid.")
        if bool((optimization_valid & ~trajectory_valid).any()):
            raise ValueError("optimization_valid deve ser subconjunto de trajectory_valid.")

        self.trajectory_valid[self.ptr].copy_(trajectory_valid)
        self.optimization_valid[self.ptr].copy_(optimization_valid)

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

        if semantic_state is None:
            semantic_numeric = torch.zeros(
                (self.num_envs, self.semantic_numeric_dim),
                dtype=torch.float32,
                device=self.device,
            )
            semantic_champion_ids = torch.zeros(
                (self.num_envs, self.semantic_entity_slots),
                dtype=torch.long,
                device=self.device,
            )
        else:
            if not isinstance(semantic_state, dict):
                raise TypeError("semantic_state must be a mapping")
            semantic_numeric = self._to_tensor(semantic_state.get("numeric"), dtype=torch.float32)
            semantic_champion_ids = self._to_tensor(semantic_state.get("champion_ids"), dtype=torch.long)
            if tuple(semantic_numeric.shape) != (self.num_envs, self.semantic_numeric_dim):
                raise ValueError("semantic numeric batch has an incompatible shape")
            if tuple(semantic_champion_ids.shape) != (self.num_envs, self.semantic_entity_slots):
                raise ValueError("semantic champion ID batch has an incompatible shape")
            if not torch.isfinite(semantic_numeric).all():
                raise ValueError("semantic numeric batch contains NaN or infinity")
            if semantic_champion_ids.numel() and (semantic_champion_ids < 0).any():
                raise ValueError("semantic champion IDs must be non-negative")

        self.semantic_numeric[self.ptr].copy_(semantic_numeric)
        self.semantic_champion_ids[self.ptr].copy_(semantic_champion_ids)

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
                        "decision_sequence", "player_decision_sequence", "player_id", "lobby_index",
                    )
                    missing = [key for key in required if key not in metadata]
                    if missing:
                        raise ValueError(
                            f"{group_name}[{index}] sem campos obrigatórios: {missing}"
                        )
                    engine_instance_id = metadata["engine_instance_id"]
                    if not isinstance(engine_instance_id, str) or not engine_instance_id.strip():
                        raise ValueError(
                            f"{group_name}[{index}].engine_instance_id deve ser texto não vazio."
                        )
                    for identity_field in ("episode_id", "decision_sequence", "player_id", "lobby_index"):
                        identity_value = metadata[identity_field]
                        if (
                            isinstance(identity_value, bool)
                            or not isinstance(identity_value, int)
                            or identity_value < 0
                        ):
                            raise ValueError(
                                f"{group_name}[{index}].{identity_field} deve ser inteiro não negativo."
                            )
                    envelope = metadata.get("identity")
                    if envelope is not None:
                        try:
                            validate_player_identity_envelope(
                                envelope,
                                engine_instance_id=engine_instance_id,
                                episode_id=metadata["episode_id"],
                                snapshot_sequence=metadata["decision_sequence"],
                                player_decision_sequence=metadata["player_decision_sequence"],
                                player_id=metadata["player_id"],
                                round_number=metadata.get("round", 0),
                            )
                        except (TypeError, ValueError) as exc:
                            raise ValueError(
                                f"{group_name}[{index}].identity inválida: {exc}"
                            ) from exc
                    normalized.append(copy.deepcopy(metadata))
                normalized_groups[group_name] = normalized

            identity_presence = [
                metadata.get("identity") is not None
                for group in normalized_groups.values()
                for metadata in group
            ]
            if any(identity_presence) and not all(identity_presence):
                raise ValueError(
                    "O rollout não pode misturar linhas com e sem envelope canônico de identidade."
                )

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
                if result["player_decision_sequence"] <= decision["player_decision_sequence"]:
                    raise ValueError(f"Sequência individual do resultado não avança na transição {index}.")
                action_trace = result.get("action_trace")
                if action_trace is None:
                    raise ValueError(
                        f"result_snapshot_metadata[{index}].action_trace é obrigatório para transições identificadas."
                    )
                if not isinstance(action_trace, dict):
                    raise TypeError(
                        f"result_snapshot_metadata[{index}].action_trace deve ser um dicionário."
                    )
                trace_player_id = action_trace.get("player_id")
                if (
                    isinstance(trace_player_id, bool)
                    or not isinstance(trace_player_id, int)
                    or trace_player_id != decision["player_id"]
                ):
                    raise ValueError(
                        f"result_snapshot_metadata[{index}].action_trace.player_id "
                        "não corresponde ao jogador da transição."
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
                    if next_state["player_decision_sequence"] != result["player_decision_sequence"]:
                        raise ValueError(f"Próxima sequência individual não corresponde ao resultado na transição {index}.")
                elif (
                    next_state["episode_id"] <= result["episode_id"]
                    or next_state["decision_sequence"] <= result["decision_sequence"]
                    or next_state["player_decision_sequence"] <= result["player_decision_sequence"]
                ):
                    raise ValueError(f"Auto-reset não avança identidade na transição {index}.")

                mask_hash = decision.get("mask_snapshot_hash")
                if not isinstance(mask_hash, str) or len(mask_hash) != 64 or any(
                    char not in "0123456789abcdef" for char in mask_hash
                ):
                    raise ValueError(
                        f"snapshot_metadata[{index}].mask_snapshot_hash deve ser SHA-256 hexadecimal."
                    )
                if decision.get("mask_snapshot_hash_algorithm") != MASK_SNAPSHOT_HASH_ALGORITHM:
                    raise ValueError(
                        f"snapshot_metadata[{index}] usa algoritmo de hash de mask desconhecido."
                    )

                # Production collection supplies the complete bundle. Recompute
                # its digest at the storage boundary instead of trusting a
                # well-formed SHA-256 string detached from the actual tensors.
                if self.masks:
                    expected_contract = {
                        "action_contract_id": ACTION_CONTRACT_ID,
                        "action_contract_version": ACTION_CONTRACT_VERSION,
                        "action_contract_hash": ACTION_CONTRACT_HASH,
                        "mask_contract_id": MASK_CONTRACT_ID,
                        "mask_contract_version": MASK_CONTRACT_VERSION,
                        "mask_contract_hash": MASK_CONTRACT_HASH,
                    }
                    for field, expected_value in expected_contract.items():
                        if decision.get(field) != expected_value:
                            raise ValueError(
                                f"snapshot_metadata[{index}].{field} ausente ou incompatível."
                            )
                    if set(masks_dict) != set(MASK_SHAPES):
                        raise ValueError(
                            "Rollout exige exatamente as 12 action masks do contrato v1."
                        )
                    for mask_name, mask_shape in MASK_SHAPES.items():
                        mask_tensor = masks_dict[mask_name]
                        if not isinstance(mask_tensor, torch.Tensor):
                            raise TypeError(f"Máscara '{mask_name}' deve ser torch.Tensor.")
                        if mask_tensor.dtype != torch.bool:
                            raise TypeError(f"Máscara '{mask_name}' deve usar torch.bool.")
                        if tuple(mask_tensor.shape) != (self.num_envs, *mask_shape):
                            raise ValueError(
                                f"Shape inválido para máscara '{mask_name}' no rollout: "
                                f"{tuple(mask_tensor.shape)}."
                            )
                    actual_mask_hash = hash_mask_row({
                        name: masks_dict[name][index]
                        for name in MASK_SHAPES
                    })
                    if actual_mask_hash != mask_hash:
                        raise ValueError(
                            f"Hash da máscara não corresponde ao conteúdo armazenado "
                            f"na transição {index}."
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
        gae_lambda=0.95,
        next_state_valid=None,
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
            if next_state_valid is None:
                next_state_valid = torch.ones(
                    self.num_envs, dtype=torch.bool, device=self.device
                )
            else:
                next_state_valid = self._to_tensor(
                    next_state_valid, dtype=torch.bool
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

                # Trajectory integrity controls TD/GAE. Optimizer eligibility
                # is independent: a trustworthy row may carry temporal credit
                # without entering a PPO minibatch.
                trajectory_valid_t = self.trajectory_valid[t]
                if t == self.num_steps - 1:
                    next_state_is_valid = next_state_valid
                else:
                    next_state_is_valid = self.trajectory_valid[t + 1]

                bootstrap_mask = (
                    next_non_terminal * next_state_is_valid.to(dtype=torch.float32)
                )
                delta = (
                    self.rewards[t]
                    + gamma * next_values * bootstrap_mask
                    - self.values[t]
                )
                gae = trajectory_valid_t.to(dtype=torch.float32) * (
                    delta + gamma * gae_lambda * bootstrap_mask * gae
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

        valid_mask = self.optimization_valid[:self.ptr]

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
            self.optimization_valid[:steps].reshape(-1),
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
        flat_semantic_numeric = self.semantic_numeric[:steps].reshape(
            total_transitions, self.semantic_numeric_dim
        )
        flat_semantic_champion_ids = self.semantic_champion_ids[:steps].reshape(
            total_transitions, self.semantic_entity_slots
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
                "semantic_state": {
                    "numeric": flat_semantic_numeric[batch_idx],
                    "champion_ids": flat_semantic_champion_ids[batch_idx],
                },
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
            result.append(copy.deepcopy(step_metadata[env_index]))
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
            "trajectory_valid_count": int(self.trajectory_valid[:self.ptr].sum().item()),
            "optimization_valid_count": int(self.optimization_valid[:self.ptr].sum().item()),
            "num_agents": self.num_envs,
            "total_transitions": self.size(),
            "obs_dim": self.obs_dim,
            "action_dim": self.action_dim,
            "semantic_numeric_dim": self.semantic_numeric_dim,
            "semantic_entity_slots": self.semantic_entity_slots,
            "ptr": self.ptr,
            "full": self.is_full(),
            "mask_names": list(self.masks.keys()),
        }