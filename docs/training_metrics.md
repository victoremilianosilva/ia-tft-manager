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
