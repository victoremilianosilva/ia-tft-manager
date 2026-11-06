from __future__ import annotations

from functools import partial
from types import SimpleNamespace

import numpy as np

from vector_lobby_env import LobbyVectorEnv


class FakeLobby:
    def __init__(self, lobby_id=0):
        self.lobby_id = lobby_id
        self.players = [SimpleNamespace(alive=True) for _ in range(8)]
        self.closed = False

    def reset(self):
        self.players = [SimpleNamespace(alive=True) for _ in range(8)]
        return np.full((8, 3), self.lobby_id, dtype=np.float32)

    def get_value(self):
        return self.lobby_id

    def step(self, actions):
        assert len(actions) == 8
        rewards = np.full(8, self.lobby_id, dtype=np.float32)
        info = {"players": [{"player_id": i, "alive": True} for i in range(8)]}
        return self.reset(), rewards, False, info

    def close(self):
        self.closed = True


def _exercise_vector(use_subprocess):
    vector = LobbyVectorEnv(
        [partial(FakeLobby, lobby_id=i) for i in range(2)],
        use_subprocess=use_subprocess,
    )
    try:
        observations = vector.reset()
        assert observations.shape == (2, 8, 3)
        assert observations[:, 0, 0].tolist() == [0.0, 1.0]
        assert vector.env_method("get_value") == [0, 1]

        actions = [[[6, 0, 0, 0, 0, 0] for _ in range(8)] for _ in range(2)]
        next_obs, rewards, dones, infos = vector.step(actions)
        assert next_obs.shape == (2, 8, 3)
        assert rewards.shape == (2, 8)
        assert rewards[:, 0].tolist() == [0.0, 1.0]
        assert dones.shape == (2, 8)
        assert not dones.any()
        assert [info["lobby_done"] for info in infos] == [False, False]
    finally:
        vector.close()


def test_serial_vector_env_contract():
    _exercise_vector(use_subprocess=False)


def test_subprocess_vector_env_contract():
    _exercise_vector(use_subprocess=True)
