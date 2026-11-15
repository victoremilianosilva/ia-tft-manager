import numpy as np


class LobbyVectorEnv:
    """
    Adaptador vetorizado para TFTLobby.

    Cada ambiente representa uma lobby com 8 jogadores.
    Não cria uma policy por jogador: o Trainer continua
    compartilhando a mesma TFTPolicy entre todos.
    """

    PLAYERS_PER_LOBBY = 8

    def __init__(self, env_fns):
        self.envs = [make_env() for make_env in env_fns]
        self.num_envs = len(self.envs)

        if self.num_envs == 0:
            raise ValueError("É necessário criar pelo menos uma lobby.")

    def reset(self):
        observations = [env.reset() for env in self.envs]
        return np.stack(observations).astype(np.float32, copy=False)

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
        if len(actions) != self.num_envs:
            raise ValueError(
                f"Recebi ações para {len(actions)} lobbies; "
                f"esperava {self.num_envs}."
            )

        all_obs = []
        all_rewards = []
        all_dones = []
        all_infos = []

        for env, lobby_actions in zip(self.envs, actions):
            obs, rewards, lobby_done, info = env.step(lobby_actions)

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
            transition_snapshot = info.get("decision_snapshot")
            if transition_snapshot is not None:
                transition_snapshot = dict(transition_snapshot)
            info["transition_snapshot"] = transition_snapshot

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
                # Nunca sobrescrever transition_snapshot com essa identidade.
                obs = env.reset()
                getter = getattr(env, "get_snapshot_metadata", None)
                next_snapshot = dict(getter()) if callable(getter) else None
            else:
                next_snapshot = (
                    dict(transition_snapshot)
                    if transition_snapshot is not None
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

    def close(self):
        for env in self.envs:
            close_method = getattr(env, "close", None)
            if callable(close_method):
                close_method()
