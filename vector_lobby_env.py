import numpy as np


class LobbyVectorEnv:
    """
    Adaptador vetorizado para TFTLobby.

    Cada ambiente representa uma lobby com 8 jogadores.
    Não cria uma policy por jogador: o Trainer continua
    compartilhando a mesma TFTPolicy entre todos.
    """

    PLAYERS_PER_LOBBY = 8

    def __init__(self, env_fns, *, batch_manager=None):
        self.envs = [make_env() for make_env in env_fns]
        self.num_envs = len(self.envs)
        self._requires_full_reset = False
        self._batch_manager = batch_manager
        self._last_native_batch = None

        if self.num_envs == 0:
            raise ValueError("É necessário criar pelo menos uma lobby.")

    def _validate_native_batch(self, native_batch):
        """Validate the single native batch without rebuilding a list of lobby dicts."""
        contract_id = getattr(native_batch, "contract_id", None)
        if contract_id is None:
            # Keep Python fixture managers usable; production C++ always returns v1.
            return False
        if contract_id != "tft.native-decision-batch":
            raise RuntimeError(f"Contrato nativo desconhecido: {contract_id!r}")
        if int(native_batch.contract_version) != 1:
            raise RuntimeError(
                f"Versao NativeDecisionBatch nao suportada: {native_batch.contract_version}"
            )
        if int(native_batch.lobby_count) != self.num_envs:
            raise RuntimeError("NativeDecisionBatch retornou quantidade incorreta de lobbies.")
        observations = np.asarray(native_batch.observations)
        masks = np.asarray(native_batch.action_masks)
        if observations.ndim != 3 or observations.shape[:2] != (self.num_envs, self.PLAYERS_PER_LOBBY):
            raise RuntimeError(f"Shape de observations do NativeDecisionBatch invalido: {observations.shape}")
        if masks.ndim != 3 or masks.shape[:2] != (self.num_envs, self.PLAYERS_PER_LOBBY):
            raise RuntimeError(f"Shape de action_masks do NativeDecisionBatch invalido: {masks.shape}")
        if not observations.flags.c_contiguous or not masks.flags.c_contiguous:
            raise RuntimeError("Buffers numericos do NativeDecisionBatch devem ser contiguos.")
        return True

    def _invalidate_all_wrapper_snapshots(self):
        for env in self.envs:
            invalidate = getattr(env, "_invalidate_current_snapshot", None)
            if callable(invalidate):
                invalidate()

    def reset(self, seed=None):
        """Reset every lobby; a supplied seed is deterministically offset per lobby."""
        observations = []
        try:
            if self._batch_manager is not None:
                if seed is not None and (
                    isinstance(seed, bool)
                    or not isinstance(seed, (int, np.integer))
                    or not 0 <= int(seed) <= 0xFFFFFFFF
                    or int(seed) + self.num_envs - 1 > 0xFFFFFFFF
                ):
                    raise ValueError("seed e offsets por lobby devem caber em uint32.")
                # A failed batch reset must invalidate every wrapper's prior
                # masks and snapshot before native state can partially advance.
                for env in self.envs:
                    invalidate = getattr(env, "_invalidate_current_snapshot", None)
                    if callable(invalidate):
                        invalidate()
                native_batch = self._batch_manager.reset(seed=seed)
                self._last_native_batch = native_batch
                if self._validate_native_batch(native_batch):
                    observations = [
                        env._consume_reset_result(native_batch.lobby_result(index))
                        for index, env in enumerate(self.envs)
                    ]
                else:
                    if len(native_batch) != self.num_envs:
                        raise RuntimeError("LobbyBatchManager retornou quantidade incorreta de resets.")
                    observations = [
                        env._consume_reset_result(result)
                        for env, result in zip(self.envs, native_batch)
                    ]
            else:
                for lobby_index, env in enumerate(self.envs):
                    if seed is None:
                        observations.append(env.reset())
                    else:
                        if (
                            isinstance(seed, bool)
                            or not isinstance(seed, (int, np.integer))
                            or not 0 <= int(seed) <= 0xFFFFFFFF
                            or int(seed) + self.num_envs - 1 > 0xFFFFFFFF
                        ):
                            raise ValueError("seed e offsets por lobby devem caber em uint32.")
                        observations.append(env.reset(seed=int(seed) + lobby_index))
        except Exception:
            # A partial reset cannot restore a known vector boundary. Clear
            # every wrapper, including those not reached by the failing loop.
            self._invalidate_all_wrapper_snapshots()
            self._requires_full_reset = True
            raise

        # Building the vector batch is part of reset success. If stacking
        # fails (for example, incompatible observation shapes), callers must
        # not continue with stale observations and newly reset lobbies.
        try:
            stacked_observations = np.stack(observations).astype(
                np.float32, copy=False
            )
        except Exception:
            self._requires_full_reset = True
            raise

        self._requires_full_reset = False
        return stacked_observations

    def semantic_projection_available(self):
        """Whether the latest vector snapshot is owned by a projectable native batch."""
        batch = self._last_native_batch
        if batch is None or not callable(getattr(batch, "semantic_projection", None)):
            return False
        return not (batch.kind == "step" and bool(np.asarray(batch.lobby_done).any()))

    def semantic_projection(self, catalog_map, contract_hash):
        """Project the latest immutable native batch without rebuilding Python player rows."""
        batch = self._last_native_batch
        if not self.semantic_projection_available():
            return None
        return batch.semantic_projection(catalog_map, contract_hash)

    def env_method(self, method_name, *args, **kwargs):
        """Mantém compatibilidade com as chamadas do Trainer."""
        return [
            getattr(env, method_name)(*args, **kwargs)
            for env in self.envs
        ]

    def get_snapshot_metadata(self):
        """Retorna a identidade do snapshot atualmente exposto por cada lobby."""
        snapshots = []
        for env in self.envs:
            getter = getattr(env, "get_snapshot_metadata", None)
            snapshots.append(dict(getter()) if callable(getter) else None)
        return snapshots

    def step(self, actions):
        """
        Entrada:
            actions: [lobby][jogador]

        Saídas:
            observations: (lobbies, 8, obs_dim)
            rewards:      (lobbies, 8)
            dones:        (lobbies, 8)
            infos:        uma info por lobby

        Em auto-reset terminal, info mantém separados o snapshot que
        produziu reward/done e o snapshot da nova observação retornada.
        """
        if self._requires_full_reset:
            raise RuntimeError(
                "LobbyVectorEnv está em estado inconsistente após falha parcial; "
                "chame reset() em todas as lobbies antes de continuar."
            )

        if len(actions) != self.num_envs:
            raise ValueError(
                f"Recebi ações para {len(actions)} lobbies; "
                f"esperava {self.num_envs}."
            )

        try:
            all_obs = []
            all_rewards = []
            all_dones = []
            all_infos = []

            if self._batch_manager is not None:
                prepared = [
                    env._prepare_batch_step(lobby_actions)
                    for env, lobby_actions in zip(self.envs, actions)
                ]
                native_batch = self._batch_manager.step([entry[0] for entry in prepared])
                self._last_native_batch = native_batch
                if self._validate_native_batch(native_batch):
                    step_results = [
                        env._consume_step_result(
                            native_batch.lobby_result(index), prepared[index][1]
                        )
                        for index, env in enumerate(self.envs)
                    ]
                else:
                    if len(native_batch) != self.num_envs:
                        raise RuntimeError("LobbyBatchManager retornou quantidade incorreta de steps.")
                    step_results = [
                        env._consume_step_result(result, prepared[index][1])
                        for index, (env, result) in enumerate(zip(self.envs, native_batch))
                    ]
            else:
                step_results = [
                    env.step(lobby_actions)
                    for env, lobby_actions in zip(self.envs, actions)
                ]

            for env, (obs, rewards, lobby_done, info) in zip(self.envs, step_results):
                rewards = np.asarray(rewards, dtype=np.float32)
                if rewards.shape != (self.PLAYERS_PER_LOBBY,):
                    raise ValueError(
                        f"Shape de rewards inválido: {rewards.shape}"
                    )

                dones = np.asarray(
                    [not player.alive for player in env.players],
                    dtype=np.bool_,
                )
                if lobby_done:
                    dones[:] = True

                info = dict(info)
                info["lobby_done"] = bool(lobby_done)

                # Este é o snapshot produzido pelo step: rewards/dones pertencem
                # a esta transição, mesmo quando a lobby termina.
                step_result_snapshot = info.get("decision_snapshot")
                if step_result_snapshot is not None:
                    step_result_snapshot = dict(step_result_snapshot)
                info["step_result_snapshot"] = step_result_snapshot

                if lobby_done:
                    get_public_state = getattr(env, "get_public_state", None)
                    if callable(get_public_state):
                        info["final_state"] = get_public_state()
                    else:
                        info["final_state"] = {
                            "players": info.get("players", []),
                            "round": info.get("round"),
                            "stage": info.get("stage"),
                            "ranking": info.get("ranking", []),
                            "winner_id": info.get("winner_id"),
                        }

                obs = np.asarray(obs, dtype=np.float32)

                if lobby_done:
                    # O reset muda a identidade/episódio da observação retornada.
                    # Nunca sobrescrever step_result_snapshot com essa identidade.
                    obs = env.reset()
                    getter = getattr(env, "get_snapshot_metadata", None)
                    next_snapshot = dict(getter()) if callable(getter) else None
                else:
                    next_snapshot = (
                        dict(step_result_snapshot)
                        if step_result_snapshot is not None
                        else None
                    )

                info["next_snapshot"] = next_snapshot

                all_obs.append(obs)
                all_rewards.append(rewards)
                all_dones.append(dones)
                all_infos.append(info)

            return (
                np.stack(all_obs).astype(np.float32, copy=False),
                np.stack(all_rewards).astype(np.float32, copy=False),
                np.stack(all_dones).astype(np.bool_, copy=False),
                all_infos,
            )

        except Exception as exc:
            # The failing env.step may itself have advanced before raising.
            # Clear every wrapper so no stale or partially published snapshot
            # remains observable while the vector is in its recovery state.
            self._invalidate_all_wrapper_snapshots()
            self._requires_full_reset = True
            raise RuntimeError(
                "LobbyVectorEnv interrompido durante step; o estado das lobbies "
                "pode estar dessincronizado. Chame reset() completo antes de continuar."
            ) from exc

    def close(self):
        if self._batch_manager is not None:
            self._batch_manager.close()
            return
        for env in self.envs:
            close_method = getattr(env, "close", None)
            if callable(close_method):
                close_method()