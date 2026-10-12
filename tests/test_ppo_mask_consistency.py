
import torch

from policy import TFTPolicy
from trainer import Trainer


def create_test_batch():
    """Cria um lote que exercita diferentes caminhos da política."""
    batch_size = 5
    obs_dim = 162

    obs = torch.randn(batch_size, obs_dim)

    # BUY, MOVE_BENCH, MOVE_BOARD, SELL e PASS.
    action_types = [0, 3, 4, 5, 6]

    masks = {
        "type_mask": torch.zeros(batch_size, 7, dtype=torch.bool),
        "shop_mask": torch.zeros(batch_size, 5, dtype=torch.bool),
        "bench_source_mask": torch.zeros(
            batch_size, 9, dtype=torch.bool
        ),
        "board_target_mask": torch.zeros(
            batch_size, 28, dtype=torch.bool
        ),
        "board_source_mask": torch.zeros(
            batch_size, 28, dtype=torch.bool
        ),
        "board_move_target_masks": torch.zeros(
            batch_size, 28, 28, dtype=torch.bool
        ),
        "bench_move_source_mask": torch.zeros(
            batch_size, 9, dtype=torch.bool
        ),
        "bench_to_board_target_masks": torch.zeros(
            batch_size, 9, 28, dtype=torch.bool
        ),
    }

    for i, action_type in enumerate(action_types):
        masks["type_mask"][i, action_type] = True

    # BUY: apenas o slot 2 é permitido.
    masks["shop_mask"][:, 2] = True

    # SELL: apenas o slot 7 do banco é permitido.
    masks["bench_source_mask"][:, 7] = True

    # MOVE_BENCH: origem 4 e destino 17.
    masks["bench_move_source_mask"][:, 4] = True
    masks["bench_to_board_target_masks"][:, 4, 17] = True

    # MOVE_BOARD: origem 9 e destino condicionado 18.
    masks["board_source_mask"][:, 9] = True
    masks["board_move_target_masks"][:, 9, 18] = True

    # Máscara genérica de destino, para compatibilidade.
    masks["board_target_mask"][:, 17] = True

    return obs, masks, action_types


def test_collection_and_evaluation_logprobs_match():
    torch.manual_seed(42)

    obs, masks, expected_types = create_test_batch()

    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )

    policy.eval()

    with torch.no_grad():
        actions, collected_logprobs, _, values = (
            policy.get_action_and_value(
                obs,
                masks=masks,
                deterministic=True,
            )
        )

        evaluated_logprobs, entropy, evaluated_values = (
            policy.evaluate_actions(
                obs,
                actions,
                masks=masks,
            )
        )

    # Todos os caminhos de ação planejados foram exercitados.
    assert actions[:, 0].tolist() == expected_types

    # Coleta e avaliação precisam calcular a mesma probabilidade.
    assert torch.allclose(
        collected_logprobs,
        evaluated_logprobs,
        atol=1e-5,
        rtol=1e-5,
    )

    assert torch.allclose(values, evaluated_values, atol=1e-5)

    assert torch.isfinite(collected_logprobs).all()
    assert torch.isfinite(evaluated_logprobs).all()
    assert torch.isfinite(entropy).all()
    assert torch.isfinite(values).all()


def test_sampled_actions_respect_masks():
    torch.manual_seed(123)

    obs, masks, expected_types = create_test_batch()

    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )

    policy.eval()

    with torch.no_grad():
        actions, logprobs, entropy, values = policy.get_action_and_value(
            obs,
            masks=masks,
            deterministic=False,
        )

    assert actions[:, 0].tolist() == expected_types

    # BUY
    assert actions[0, 1].item() == 2

    # MOVE_BENCH: origem e destino condicionais
    assert actions[1, 2].item() == 4
    assert actions[1, 3].item() == 17

    # MOVE_BOARD: origem e destino condicionais
    assert actions[2, 4].item() == 9
    assert actions[2, 5].item() == 18

    # SELL
    assert actions[3, 2].item() == 7

    assert torch.isfinite(logprobs).all()
    assert torch.isfinite(entropy).all()
    assert torch.isfinite(values).all()


def test_reroll_and_buy_xp_logprobs_match():
    torch.manual_seed(42)

    # 🔄 REROLL, ⭐ BUY_XP e ⏭️ PASS
    expected_types = [1, 2, 6]
    batch_size = len(expected_types)

    obs = torch.randn(batch_size, 162)

    masks = {
        "type_mask": torch.zeros(batch_size, 7, dtype=torch.bool),
        "shop_mask": torch.zeros(batch_size, 5, dtype=torch.bool),
        "bench_source_mask": torch.zeros(batch_size, 9, dtype=torch.bool),
        "board_target_mask": torch.zeros(batch_size, 28, dtype=torch.bool),
        "board_source_mask": torch.zeros(batch_size, 28, dtype=torch.bool),
        "board_move_target_masks": torch.zeros(
            batch_size, 28, 28, dtype=torch.bool
        ),
        "bench_move_source_mask": torch.zeros(
            batch_size, 9, dtype=torch.bool
        ),
        "bench_to_board_target_masks": torch.zeros(
            batch_size, 9, 28, dtype=torch.bool
        ),
    }

    for i, action_type in enumerate(expected_types):
        masks["type_mask"][i, action_type] = True

    policy = TFTPolicy(
        obs_dim=162,
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )
    policy.eval()

    with torch.no_grad():
        actions, logprobs, _, values = policy.get_action_and_value(
            obs, masks=masks, deterministic=True
        )

        evaluated_logprobs, entropy, evaluated_values = (
            policy.evaluate_actions(obs, actions, masks)
        )

    assert actions[:, 0].tolist() == expected_types
    assert torch.allclose(logprobs, evaluated_logprobs, atol=1e-5)
    assert torch.allclose(values, evaluated_values, atol=1e-5)
    assert torch.isfinite(logprobs).all()
    assert torch.isfinite(entropy).all()


def test_nontrivial_masked_logprobs_match_collection_and_evaluation():
    torch.manual_seed(2026)

    obs, masks, expected_types = create_test_batch()

    # 🛒 BUY: duas opções possíveis.
    masks["shop_mask"][0, 1] = True

    # 🔄 MOVE_BENCH: duas origens e dois destinos por origem.
    masks["bench_move_source_mask"][1, 3] = True
    masks["bench_to_board_target_masks"][1, 4, 16] = True
    masks["bench_to_board_target_masks"][1, 3, 16] = True
    masks["bench_to_board_target_masks"][1, 3, 17] = True

    # ♟️ MOVE_BOARD: duas origens e destinos condicionais.
    masks["board_source_mask"][2, 8] = True
    masks["board_move_target_masks"][2, 8, 17] = True
    masks["board_move_target_masks"][2, 8, 18] = True
    masks["board_move_target_masks"][2, 9, 17] = True

    # 💰 SELL: duas opções possíveis.
    masks["bench_source_mask"][3, 6] = True

    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )
    policy.eval()

    with torch.no_grad():
        actions, collected_logprobs, _, _ = (
            policy.get_action_and_value(
                obs,
                masks=masks,
                deterministic=True,
            )
        )

        evaluated_logprobs, entropy, _ = policy.evaluate_actions(
            obs, actions, masks
        )

    # ✅ Os dois caminhos devem calcular a mesma log-probabilidade.
    assert torch.allclose(
        collected_logprobs,
        evaluated_logprobs,
        atol=1e-5,
        rtol=1e-5,
    )

    # ✅ As ações selecionadas precisam respeitar as máscaras.
    assert masks["shop_mask"][0, actions[0, 1]]
    assert masks["bench_move_source_mask"][1, actions[1, 2]]
    assert masks["bench_to_board_target_masks"][
        1, actions[1, 2], actions[1, 3]
    ]
    assert masks["board_source_mask"][2, actions[2, 4]]
    assert masks["board_move_target_masks"][
        2, actions[2, 4], actions[2, 5]
    ]
    assert masks["bench_source_mask"][3, actions[3, 2]]

    # ✅ Log-probabilidades e entropias devem ser finitas.
    assert torch.isfinite(collected_logprobs).all()
    assert torch.isfinite(evaluated_logprobs).all()
    assert torch.isfinite(entropy).all()

    # 📊 Escolhas com alternativas devem ter entropia positiva.
    assert (entropy[:4] > 0).all()

def test_masked_probabilities_match_manual_calculation():
    import math
    from torch.distributions import Categorical

    # 🎯 Logits conhecidos e máscara com três opções válidas.
    logits = torch.tensor([[2.0, 1.0, 0.0, 3.0]])
    mask = torch.tensor([[True, True, False, True]])

    masked_logits = TFTPolicy._mask_logits(logits, mask)
    dist = Categorical(logits=masked_logits)

    # 🧮 Referência independente: softmax somente sobre opções válidas.
    valid_logits = [2.0, 1.0, 3.0]
    denominator = sum(math.exp(x) for x in valid_logits)
    expected_probs = torch.tensor([[
        math.exp(2.0) / denominator,
        math.exp(1.0) / denominator,
        0.0,
        math.exp(3.0) / denominator,
    ]])

    assert torch.allclose(
        dist.probs,
        expected_probs,
        atol=1e-6,
        rtol=1e-6,
    )

    # 📊 Confere o log-probability de uma ação válida.
    selected_action = torch.tensor([0])
    expected_logprob = math.log(math.exp(2.0) / denominator)

    assert torch.allclose(
        dist.log_prob(selected_action),
        torch.tensor([expected_logprob]),
        atol=1e-6,
        rtol=1e-6,
    )

    # 🚫 A opção bloqueada precisa ter probabilidade zero.
    assert dist.probs[0, 2].item() == 0.0
    assert torch.isfinite(dist.log_prob(selected_action)).all()

def test_ppo_compute_loss_with_conditional_masks():
    import torch
    from ppo import PPOTrainer

    torch.manual_seed(2026)

    obs, masks, _ = create_test_batch()

    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )

    optimizer = torch.optim.Adam(
        policy.parameters(),
        lr=3e-4,
    )

    ppo = PPOTrainer(
        policy=policy,
        optimizer=optimizer,
        writer=None,
    )

    # 🎮 Coleta ações e seus log-probabilities originais.
    actions, old_logprobs, _, old_values = (
        policy.get_action_and_value(
            obs,
            masks=masks,
            deterministic=True,
        )
    )

    batch_size = obs.shape[0]

    advantages = torch.linspace(
        -1.0, 1.0, batch_size
    )

    returns = old_values.detach() + advantages

    # 🧠 Executa a loss usada pelo treinamento PPO.
    result = ppo.compute_loss(
        obs=obs,
        actions=actions,
        old_logprobs=old_logprobs.detach(),
        old_values=old_values.detach(),
        advantages=advantages,
        returns=returns,
        masks=masks,
    )

    loss = result[0]

    assert torch.isfinite(loss)

    # 🔙 Confirma que a loss permite backpropagation.
    optimizer.zero_grad(set_to_none=True)
    loss.backward()

    gradients = [
        parameter.grad
        for parameter in policy.parameters()
        if parameter.grad is not None
    ]

    assert gradients
    assert all(torch.isfinite(grad).all() for grad in gradients)

    # 🔧 Confirma que o otimizador consegue atualizar os pesos.
    optimizer.step()

def test_sampled_actions_are_valid_and_numerically_stable():
    torch.manual_seed(2026)

    obs, masks, _ = create_test_batch()

    # 🔀 Torna algumas escolhas não determinísticas.
    masks["shop_mask"][0, 1] = True
    masks["bench_move_source_mask"][1, 3] = True
    masks["bench_to_board_target_masks"][1, 3, 16] = True
    masks["board_source_mask"][2, 8] = True
    masks["board_move_target_masks"][2, 8, 17] = True
    masks["bench_source_mask"][3, 6] = True

    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )
    policy.eval()

    # 🔎 Toda decisão condicional precisa ter uma opção válida.
    assert masks["type_mask"].any(dim=1).all()
    assert masks["shop_mask"][0].any()
    assert masks["bench_move_source_mask"][1].any()
    assert masks["board_source_mask"][2].any()
    assert masks["bench_source_mask"][3].any()

    with torch.no_grad():
        for _ in range(100):
            actions, logprobs, entropy, values = (
                policy.get_action_and_value(
                    obs,
                    masks=masks,
                    deterministic=False,
                )
            )

            # 📊 Nenhum resultado numérico inválido.
            assert torch.isfinite(logprobs).all()
            assert torch.isfinite(entropy).all()
            assert torch.isfinite(values).all()

            # 🛒 BUY
            assert masks["shop_mask"][0, actions[0, 1]]

            # 🪑 MOVE_BENCH: origem e destino correspondentes.
            bench_source = actions[1, 2].item()
            bench_target = actions[1, 3].item()

            assert masks["bench_move_source_mask"][1, bench_source]
            assert masks[
                "bench_to_board_target_masks"
            ][1, bench_source, bench_target]

            # ♟️ MOVE_BOARD: origem e destino correspondentes.
            board_source = actions[2, 4].item()
            board_target = actions[2, 5].item()

            assert masks["board_source_mask"][2, board_source]
            assert masks[
                "board_move_target_masks"
            ][2, board_source, board_target]

            # 💰 SELL
            assert masks["bench_source_mask"][3, actions[3, 2]]

def test_full_ppo_update_with_conditional_masks():
    import torch
    from ppo import PPOTrainer
    from rollout import RolloutBuffer

    torch.manual_seed(2026)

    # 🎮 Prepara experiências com diferentes tipos de ação.
    obs, masks, _ = create_test_batch()
    batch_size = obs.shape[0]

    policy = TFTPolicy(
        obs_dim=obs.shape[-1],
        action_dims=Trainer.ACTION_DIMS,
        hidden_size=32,
    )

    optimizer = torch.optim.Adam(
        policy.parameters(),
        lr=3e-4,
    )

    class TestWriter:
        def add_scalar(self, *args, **kwargs):
            pass

    ppo = PPOTrainer(
        policy=policy,
        optimizer=optimizer,
        writer=TestWriter(),
        target_kl=100.0,
    )

    # 📦 Coleta as experiências usando a própria política.
    with torch.no_grad():
        actions, logprobs, _, values = (
            policy.get_action_and_value(
                obs,
                masks=masks,
                deterministic=True,
            )
        )

    rollout = RolloutBuffer(
        num_steps=1,
        num_envs=batch_size,
        obs_dim=obs.shape[-1],
        action_dim=actions.shape[-1],
        device="cpu",
    )

    rewards = torch.arange(
        batch_size,
        dtype=torch.float32,
    )

    dones = torch.ones(batch_size)

    rollout.add(
        obs=obs,
        actions=actions,
        logprobs=logprobs.detach(),
        rewards=rewards,
        dones=dones,
        values=values.detach().reshape(-1),
        masks_dict=masks,
    )

    rollout.compute_returns_and_advantages(
        next_value=torch.zeros(batch_size),
        next_done=dones,
    )

    # 💾 Guarda os pesos antes da atualização.
    params_before = [
        parameter.detach().clone()
        for parameter in policy.parameters()
    ]

    # 🚀 Executa o fluxo real de atualização do PPO.
    ppo.update(
        rollout,
        batch_size=batch_size,
        epochs=1,
    )

    # ✅ Confirma que os parâmetros continuam válidos.
    params_after = list(policy.parameters())

    assert all(
        torch.isfinite(parameter).all()
        for parameter in params_after
    )

    # 🔧 Confirma que pelo menos algum peso foi atualizado.
    assert any(
        not torch.equal(before, after.detach())
        for before, after in zip(params_before, params_after)
    )