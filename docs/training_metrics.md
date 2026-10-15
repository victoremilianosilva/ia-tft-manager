# Auditoria do treinamento

## Teste comparável (~10 minutos)

Na raiz do projeto, com a `.venv` ativa, execute:

```powershell
.\scripts\train_10min.ps1
```

O script mantém a configuração de referência:
- Backend C++
- 4 lobbies × 8 jogadores = 32 agentes
- 300 updates adicionais
- 128 passos por rollout

O tempo é uma estimativa e varia com hardware, checkpoint e duração das partidas.

## Novas métricas no TensorBoard

### Máscaras
- `mask_audit/actions_checked`: ações verificadas em cada update.
- `mask_audit/type_invalid`: tipo de ação escolhido que não estava permitido pela máscara.
- `mask_audit/conditional_invalid`: parâmetro condicionado inválido em BUY, MOVE_BENCH ou MOVE_BOARD.
- `mask_audit/selected_invalid_rate`: proporção de escolhas incompatíveis com as máscaras usadas pela policy.

### Anti-loop
- `anti_loop_delta/*`: incremento dos contadores durante o update.
- `anti_loop/block_rate_update`: bloqueios por tentativa durante o update.
- `anti_loop/counter_reset_detected`: indica se um contador diminuiu entre snapshots.

### Resultado de partidas
- `outcomes/final_placement` e `outcomes/win`: colocação e vitória por jogador.
- `outcomes/mean_placement` e `outcomes/win_rate`: médias cumulativas.
- `outcomes/matches_completed`: partidas concluídas.
- `outcomes/match_duration_steps` e `outcomes/match_duration_rounds`: duração de cada partida.

As métricas de colocação só aparecem quando a engine expõe colocação, ranking ou recompensa de colocação utilizável. Se a engine C++ não exportar esses campos, a lacuna fica visível: a instrumentação não inventa resultados.

### PPO / KL
- `ppo/approx_kl_max`: maior KL observado entre minibatches no update.
- `ppo/target_kl`: limite configurado.
- `ppo/early_stop` e `ppo/early_stop_kl`: se houve parada antecipada e o KL que a acionou.
- `ppo/batches_processed` e `ppo/epochs_started`: minibatches processados e épocas iniciadas.

## Como ver os novos dados

```powershell
tensorboard --logdir=tft_logs
```

Abra http://localhost:6006. Use um novo treino para gerar as novas tags; o CSV antigo não será retroativamente preenchido.


## Auditoria do PPO e comparação de versões

- `ppo/approx_kl` usa o estimador `mean((ratio - 1) - logratio)`, limitado inferiormente a zero para evitar KL negativa por ruído de minibatch.
- O Early Stop é avaliado antes do backward/optimizer step. O minibatch que ultrapassa `target_kl` é descartado, sem atualizar os pesos.
- `charts/learning_rate` registra a LR efetiva depois do scheduler; a inicialização também imprime a LR restaurada do optimizer e o `last_epoch` do scheduler.
- `FAST8` e `SLOWROLL` são avaliadas antes da estratégia ECON, para que a regra genérica de economia não capture estados elegíveis para uma estratégia específica.

### Comparação com baseline fixo

Não use as métricas agregadas de uma lobby homogênea como prova de melhoria: com oito agentes da mesma versão, a média de colocação tende a 4,5 e a taxa de vitória a 12,5% por construção. Para comparar versões, use um checkpoint baseline imutável e um checkpoint candidato, coloque ambos na mesma lobby e registre resultado por política, rotação de assentos e número de partidas. O baseline deve permanecer congelado durante a avaliação. O script de avaliação usa um checkpoint explícito como baseline; execute apenas depois de salvar uma cópia do checkpoint que não será sobrescrita pelo treinamento.


### Rodada curta com taxa de aprendizado controlada

No PowerShell, ative a venv e rode:

```powershell
$env:TFT_ENGINE_BACKEND = "cpp"
$env:TFT_PPO_LR = "0.0001"
$env:TFT_PPO_MIN_LR = "0.00002"
python -c "from trainer import Trainer; t=Trainer(num_envs=4, use_subprocess=False); t.train(total_updates=20, rollout_steps=128)"
```

Esse override é opt-in e é aplicado depois da restauração de optimizer e scheduler. Compare `ppo/early_stop`, `ppo/approx_kl_max`, `ppo/epochs_started`, `ppo/batches_processed` e `charts/learning_rate`. Após o teste, limpe as variáveis com `Remove-Item Env:TFT_PPO_LR, Env:TFT_PPO_MIN_LR -ErrorAction SilentlyContinue`. O teste não foi executado nesta sessão.
