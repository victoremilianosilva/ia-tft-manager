# Treinamento PPO

## Arquivos centrais

- `trainer.py`: orquestra ambientes, policy, buffer, otimizador, scheduler, métricas e checkpoints.
- `policy.py`: `TFTPolicy`, encoder de observações, cabeças de ação condicionais, valor e avaliação de ações.
- `rollout.py`: `RolloutBuffer` para transições sincronizadas, máscaras, retornos e vantagens.
- `ppo.py`: cálculo da loss e atualização PPO.
- `vector_lobby_env.py`: agrupa lobbies e empilha resultados para coleta.
- `tft_logs/`: eventos TensorBoard por execução.
- `tft_checkpoint.pt`: checkpoint de treino principal esperado pelo trainer.

## Escala de coleta

`Trainer.num_envs` representa o número de lobbies, não o número de jogadores. Cada lobby contém oito agentes e todos compartilham a mesma policy. As observações têm formato de lote `(lobbies, 8, obs_dim)` antes do flatten. As máscaras seguem o mesmo ordenamento de agentes.

## Policy e ações condicionais

A policy escolhe o tipo da ação e depois apenas as cabeças relevantes para aquele tipo. Máscaras condicionais limitam opções de loja, banco e tabuleiro. `get_action_and_value_with_diagnostics` expõe distribuições pós-máscara para o viewer; os testes de diagnóstico garantem que a instrumentação não altere ações, valores ou consumo de RNG em relação à inferência normal.

## PPO e buffer

O buffer valida shapes e sincronização de transições. Armazena observações, ações, log-probabilities, recompensas, dones, valores e as máscaras originais. Retornos e vantagens são calculados sobre transições válidas; a normalização e o batching ocorrem antes da atualização. `PPOTrainer` calcula a loss clipped e atualiza a policy com limite de gradiente e parada opcional por KL alvo.

## Checkpoint e retomada

O trainer persiste os pesos da policy e, quando aplicável, estados de otimizador/scheduler e número de update. O viewer é somente leitura e não restaura o otimizador. A arquitetura do checkpoint precisa corresponder à versão de `TFTPolicy`, às dimensões das ações e à dimensão da observação.

## Métricas

O trainer usa TensorBoard em `tft_logs/AkameIA_V2` e inclui métricas de desempenho/treino e diagnósticos da engine. Use [avaliação](evaluation-tooling.md) para comparar checkpoints sem continuar o treino.
