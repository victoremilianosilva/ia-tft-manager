import numpy as np
import pytest

from vector_lobby_env import LobbyVectorEnv


class SeedRecordingEnv:
    def __init__(self):
        self.seeds = []

    def reset(self, seed=None):
        self.seeds.append(seed)
        return np.asarray([len(self.seeds)], dtype=np.float32)


def test_vector_reset_offsets_seed_per_lobby():
    envs = [SeedRecordingEnv() for _ in range(3)]
    vector = LobbyVectorEnv([lambda env=env: env for env in envs])

    result = vector.reset(seed=700)

    assert result.shape == (3, 1)
    assert [env.seeds for env in envs] == [[700], [701], [702]]


def test_vector_reset_without_seed_preserves_environment_default():
    envs = [SeedRecordingEnv() for _ in range(2)]
    vector = LobbyVectorEnv([lambda env=env: env for env in envs])

    vector.reset()

    assert [env.seeds for env in envs] == [[None], [None]]


@pytest.mark.parametrize("seed", [-1, True, 1.5, 0xFFFFFFFF])
def test_vector_reset_rejects_invalid_seed(seed):
    envs = [SeedRecordingEnv()]
    vector = LobbyVectorEnv([lambda: envs[0]])

    with pytest.raises(ValueError, match="seed"):
        vector.reset(seed=seed)
