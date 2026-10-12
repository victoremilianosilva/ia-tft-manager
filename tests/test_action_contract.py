
# 🧪 tests/test_action_contract.py

import numpy as np
import pytest
import torch

from trainer import Trainer
from env import MiniTFTEnv


# 🎮 1. A política precisa preservar a ordem das seis dimensões.
def test_actions_to_lobby_format_preserves_all_six_dimensions():
    trainer = Trainer.__new__(Trainer)
    trainer.num_envs = 2
    trainer.num_agents = 16

    # Cada agente recebe valores válidos e identificáveis.
    dims = Trainer.ACTION_DIMS
    actions = torch.tensor([
        [i % dim for dim in dims]
        for i in range(trainer.num_agents)
    ])

    result = trainer._actions_to_lobby_format(actions)

    assert len(result) == 2
    assert len(result[0]) == 8
    assert len(result[1]) == 8

    expected_keys = {
        "type",
        "shop_slot",
        "bench_slot",
        "board_target",
        "board_source",
        "board_move_target",
    }

    for lobby_idx, lobby in enumerate(result):
        for player_idx, action in enumerate(lobby):
            agent_idx = lobby_idx * 8 + player_idx

            assert set(action.keys()) == expected_keys
            assert action["type"] == agent_idx % 7
            assert action["shop_slot"] == agent_idx % 5
            assert action["bench_slot"] == agent_idx % 9
            assert action["board_target"] == agent_idx % 28
            assert action["board_source"] == agent_idx % 28
            assert action["board_move_target"] == agent_idx % 28


# 🛡️ 2. O Trainer precisa rejeitar vetores com shape incorreto.
def test_actions_to_lobby_format_rejects_invalid_shape():
    trainer = Trainer.__new__(Trainer)
    trainer.num_envs = 1
    trainer.num_agents = 8

    invalid_actions = torch.zeros((8, 5), dtype=torch.long)

    with pytest.raises(ValueError):
        trainer._actions_to_lobby_format(invalid_actions)


# 🔄 3. O ambiente precisa normalizar o vetor na mesma ordem.
def test_sanitize_action_preserves_six_dimension_contract():
    env = MiniTFTEnv.__new__(MiniTFTEnv)

    action = [4, 3, 8, 27, 12, 19]
    result = env._sanitize_action(action)

    assert result == {
        "type": 4,
        "shop_slot": 3,
        "bench_slot": 8,
        "board_target": 27,
        "board_source": 12,
        "conditioned_board_target": 19,
    }


# 🔗 4. O campo do Trainer deve ser reconhecido pelo ambiente.
def test_sanitize_action_accepts_board_move_target_alias():
    env = MiniTFTEnv.__new__(MiniTFTEnv)

    result = env._sanitize_action({
        "type": 4,
        "shop_slot": 0,
        "bench_slot": 0,
        "board_target": 5,
        "board_source": 10,
        "board_move_target": 20,
    })

    assert result["type"] == 4
    assert result["board_target"] == 5
    assert result["board_source"] == 10
    assert result["conditioned_board_target"] == 20


# 🎯 5. Cada tipo de ação deve chamar somente seu executor correto.
from types import SimpleNamespace
from unittest.mock import Mock

from ai.ActionMaskManager import ActionType


@pytest.mark.parametrize(
    "action_type, executor_name, receives_action",
    [
        (ActionType.BUY, "buy", True),
        (ActionType.REROLL, "reroll", False),
        (ActionType.BUY_XP, "buy_xp", False),
        (ActionType.MOVE_BENCH, "move_bench", True),
        (ActionType.MOVE_BOARD, "move_board", True),
        (ActionType.SELL, "sell", True),
        (ActionType.PASS, "pass", False),
    ],
)
def test_step_dispatches_to_correct_executor(
    action_type,
    executor_name,
    receives_action,
):
    # 🧪 Ambiente mínimo: não inicializa managers nem partida.
    env = MiniTFTEnv.__new__(MiniTFTEnv)
    env.done = False
    env.player_id = 3
    env.hp = 100
    env.action_count = 0
    env.round_action_count = 0
    env.total_actions = 0
    env.last_reward = 0.0
    env.economy_manager = SimpleNamespace(
        gold=10,
        level=2,
    )

    # 🔧 Isola os efeitos colaterais.
    env._get_state = Mock(return_value={"test": True})
    env._rebuild_player_state = Mock()

    executors = {
        "buy": Mock(return_value=0.1),
        "reroll": Mock(return_value=0.2),
        "buy_xp": Mock(return_value=0.3),
        "move_bench": Mock(return_value=0.4),
        "move_board": Mock(return_value=0.5),
        "sell": Mock(return_value=0.6),
        "pass": Mock(return_value=0.0),
    }

    for name, executor in executors.items():
        setattr(env, f"_execute_{name}", executor)

    # 🎮 Valores identificáveis para conferir o encaminhamento.
    action = {
        "type": int(action_type),
        "shop_slot": 2,
        "bench_slot": 4,
        "board_target": 7,
        "board_source": 11,
        "board_move_target": 19,
    }

    _, reward, done, info = env.step(action)

    # ✅ O executor esperado foi chamado uma vez.
    expected_executor = executors[executor_name]
    expected_executor.assert_called_once()

    # 🚫 Nenhum outro executor pode ser chamado.
    for name, executor in executors.items():
        if name != executor_name:
            executor.assert_not_called()

    # 📦 Executores que dependem dos argumentos recebem a ação sanitizada.
    if receives_action:
        passed_action = expected_executor.call_args.args[0]
        assert passed_action["type"] == int(action_type)
        assert passed_action["shop_slot"] == 2
        assert passed_action["bench_slot"] == 4
        assert passed_action["board_target"] == 7
        assert passed_action["board_source"] == 11
        assert passed_action["conditioned_board_target"] == 19

    assert reward == {
        "buy": 0.1,
        "reroll": 0.2,
        "buy_xp": 0.3,
        "move_bench": 0.4,
        "move_board": 0.5,
        "sell": 0.6,
        "pass": 0.0,
    }[executor_name]

    assert done is False
    assert info["player_id"] == 3
    assert info["action_type"] == int(action_type)
    assert env._rebuild_player_state.call_count == 1
