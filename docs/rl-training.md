# Treinamento PPO

> **Runtime de treinamento PPO da arquitetura nativa.** O caminho operacional é `train_native.py` / `scripts/run_training_battery.py`. O PPO aprende a partir da projeção semântica produzida pelos snapshots nativos; a Engine e as action masks permanecem autoridade de legalidade. Checkpoints históricos não são aceitos como resume nesta entrada de treinamento.

## Arquivos centrais

- `trainer.py`: orquestra ambientes, policy, buffer, otimizador, scheduler, métricas e checkpoints.
- `policy.py`: `TFTPolicy`, encoder de observações, cabeças de ação condicionais, valor e avaliação de ações.
- `rollout.py`: `RolloutBuffer` para transições sincronizadas, máscaras, retornos e vantagens.
- `ppo.py`: cálculo da loss e atualização PPO.
- `vector_lobby_env.py`: agrupa lobbies e empilha resultados para coleta.
- `tft_logs/`: eventos TensorBoard por execução.
- `checkpoints/native_ppo/` ou o diretório informado em `--output-dir`: artefatos isolados da linhagem nativa.

## Início de treino e bateria multi-seed\n\nTreino curto (smoke):\n\n```powershell\npython train_native.py --output-dir training_runs/smoke-seed-42 --seed 42 --updates 2 --lobbies 1 --rollout-steps 8\n```\n\nBateria de treino: `python scripts/run_training_battery.py --output-root training_runs/native-battery --seeds 11,12,13 --updates 160 --lobbies 4 --rollout-steps 128`. Cada seed usa um diretório, checkpoint e TensorBoard próprios. O manifesto registra revisão do código, hash do binário nativo, runtime, configuração, seed, arquitetura e contratos. O diretório precisa estar vazio; nenhuma execução sobrescreve artefatos anteriores.\n\nA bateria é treino, não benchmark final: placement/top-4/top-1 e promoção do modelo exigem avaliação independente e split de episódios sem vazamento.\n\n## Escala de coleta

`Trainer.num_envs` representa o número de lobbies, não o número de jogadores. Cada lobby contém oito agentes e todos compartilham a mesma policy. As observações têm formato de lote `(lobbies, 8, obs_dim)` antes do flatten. As máscaras seguem o mesmo ordenamento de agentes.

## Policy e ações condicionais

A policy escolhe o tipo da ação e depois apenas as cabeças relevantes para aquele tipo. Máscaras condicionais limitam opções de loja, banco e tabuleiro. `get_action_and_value_with_diagnostics` expõe distribuições pós-máscara para o viewer; os testes de diagnóstico garantem que a instrumentação não altere ações, valores ou consumo de RNG em relação à inferência normal.

## PPO e buffer

O buffer valida shapes e sincronização de transições. Armazena observações, ações, log-probabilities, recompensas, dones, valores e as máscaras originais. Retornos e vantagens são calculados sobre transições válidas; a normalização e o batching ocorrem antes da atualização. `PPOTrainer` calcula a loss clipped e atualiza a policy com limite de gradiente e parada opcional por KL alvo.

## Checkpoint e retomada

O trainer persiste os pesos da policy e, quando aplicável, estados de otimizador/scheduler e número de update. O viewer é somente leitura e não restaura o otimizador. No runtime atual, o loader exige compatibilidade estrutural com `TFTPolicy`, as dimensões de ação e a observação. Para a nova linhagem, isso é apenas uma condição estrutural necessária: a aceitação também exige identidade/hash dos contratos e compatibilidade semântica conforme [PPO Checkpoint Contract v1](ppo-checkpoint-contract.v1.draft.md).

## Métricas

O trainer usa TensorBoard em `tft_logs/AkameIA_V2` e inclui métricas de desempenho/treino e diagnósticos da engine. Use [avaliação](evaluation-tooling.md) para comparar checkpoints sem continuar o treino.
