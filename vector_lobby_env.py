"""Vetorização de lobbies TFT com execução serial ou processos isolados.

O processo principal continua dono da policy/PPO. Cada worker possui uma única
instância da engine C++, evitando compartilhar objetos pybind11 entre processos.
"""
from __future__ import annotations

import multiprocessing as mp
import traceback

import numpy as np


PLAYERS_PER_LOBBY = 8


def _step_lobby(env, lobby_actions):
    """Executa uma lobby e normaliza os resultados antes de retornar ao Trainer."""
    obs, rewards, lobby_done, info = env.step(lobby_actions)
    rewards = np.asarray(rewards, dtype=np.float32)
    if rewards.shape != (PLAYERS_PER_LOBBY,):
        raise ValueError(f"Shape de rewards inválido: {rewards.shape}")

    players = getattr(env, "players", None)
    if players is not None and len(players) == PLAYERS_PER_LOBBY:
        dones = np.asarray([not player.alive for player in players], dtype=np.bool_)
    else:
        player_records = info.get("players", []) if isinstance(info, dict) else []
        dones = np.asarray(
            [not bool(player.get("alive", False)) for player in player_records],
            dtype=np.bool_,
        )
        if dones.shape != (PLAYERS_PER_LOBBY,):
            raise ValueError("A lobby não expôs os estados alive dos oito jogadores.")

    if lobby_done:
        dones[:] = True

    info = dict(info)
    info["lobby_done"] = bool(lobby_done)

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
        obs = env.reset()

    return obs, rewards, dones, info


def _lobby_worker(connection, env_factory):
    """Worker persistente: cria e destrói a engine dentro do próprio processo."""
    env = None
    try:
        env = env_factory()
        while True:
            command, payload = connection.recv()
            if command == "close":
                break
            try:
                if command == "reset":
                    result = env.reset()
                elif command == "step":
                    result = _step_lobby(env, payload)
                elif command == "method":
                    method_name, args, kwargs = payload
                    result = getattr(env, method_name)(*args, **kwargs)
                else:
                    raise ValueError(f"Comando desconhecido do worker: {command}")
                connection.send(("ok", result))
            except BaseException as exc:
                connection.send(("error", type(exc).__name__, str(exc), traceback.format_exc()))
    except EOFError:
        pass
    finally:
        if env is not None:
            close_method = getattr(env, "close", None)
            if callable(close_method):
                try:
                    close_method()
                except Exception:
                    pass
        connection.close()


class LobbyVectorEnv:
    """Ambientes vetorizados; uma instância representa uma partida de 8 jogadores."""

    PLAYERS_PER_LOBBY = PLAYERS_PER_LOBBY

    def __init__(self, env_fns, use_subprocess: bool = False, max_workers: int | None = None):
        self.num_envs = len(env_fns)
        if self.num_envs == 0:
            raise ValueError("É necessário criar pelo menos uma lobby.")

        self.use_subprocess = bool(use_subprocess)
        self.envs = []
        self._workers = []
        self._connections = []
        self._closed = False

        if not self.use_subprocess:
            self.envs = [make_env() for make_env in env_fns]
            return

        worker_count = self.num_envs if max_workers is None else int(max_workers)
        if worker_count != self.num_envs:
            raise ValueError(
                "Este vetor usa um worker persistente por lobby; "
                "max_workers deve ser igual ao número de lobbies."
            )

        # spawn funciona no Windows e evita herdar estado/GIL/objetos nativos
        # do processo principal. As factories precisam ser serializáveis.
        context = mp.get_context("spawn")
        try:
            for make_env in env_fns:
                parent_connection, child_connection = context.Pipe()
                process = context.Process(
                    target=_lobby_worker,
                    args=(child_connection, make_env),
                    daemon=True,
                )
                process.start()
                child_connection.close()
                self._connections.append(parent_connection)
                self._workers.append(process)
        except BaseException:
            self.close()
            raise

    def _dispatch(self, command, payloads=None):
        if self._closed:
            raise RuntimeError("LobbyVectorEnv já foi fechado.")
        if payloads is None:
            payloads = [None] * self.num_envs
        for connection, payload in zip(self._connections, payloads):
            connection.send((command, payload))
        results = []
        for index, connection in enumerate(self._connections):
            try:
                response = connection.recv()
            except EOFError as exc:
                worker = self._workers[index]
                raise RuntimeError(
                    f"Worker da lobby {index} encerrou inesperadamente "
                    f"(exitcode={worker.exitcode})."
                ) from exc
            if response[0] == "error":
                _, error_type, message, remote_traceback = response
                raise RuntimeError(
                    f"Erro no worker da lobby {index}: {error_type}: {message}\n"
                    f"{remote_traceback}"
                )
            results.append(response[1])
        return results

    def reset(self):
        if self.use_subprocess:
            observations = self._dispatch("reset")
        else:
            observations = [env.reset() for env in self.envs]
        return np.stack(observations).astype(np.float32, copy=False)

    def env_method(self, method_name, *args, **kwargs):
        """Executa o método em todas as lobbies, em paralelo quando habilitado."""
        if self.use_subprocess:
            payloads = [(method_name, args, kwargs)] * self.num_envs
            return self._dispatch("method", payloads)
        return [getattr(env, method_name)(*args, **kwargs) for env in self.envs]

    def step(self, actions):
        if len(actions) != self.num_envs:
            raise ValueError(
                f"Recebi ações para {len(actions)} lobbies; "
                f"esperava {self.num_envs}."
            )

        if self.use_subprocess:
            results = self._dispatch("step", actions)
        else:
            results = [
                _step_lobby(env, lobby_actions)
                for env, lobby_actions in zip(self.envs, actions)
            ]

        all_obs, all_rewards, all_dones, all_infos = zip(*results)
        return (
            np.stack(all_obs).astype(np.float32, copy=False),
            np.stack(all_rewards).astype(np.float32, copy=False),
            np.stack(all_dones).astype(np.bool_, copy=False),
            list(all_infos),
        )

    def close(self):
        if self._closed:
            return
        self._closed = True
        if self.use_subprocess:
            for connection in self._connections:
                try:
                    connection.send(("close", None))
                except (BrokenPipeError, EOFError, OSError):
                    pass
            for connection in self._connections:
                try:
                    connection.close()
                except OSError:
                    pass
            for worker in self._workers:
                worker.join(timeout=5)
                if worker.is_alive():
                    worker.terminate()
                    worker.join(timeout=2)
        else:
            for env in self.envs:
                close_method = getattr(env, "close", None)
                if callable(close_method):
                    close_method()
