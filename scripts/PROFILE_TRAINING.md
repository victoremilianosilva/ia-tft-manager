# Perfil de desempenho: treino do zero vs retomada

Esta branch adiciona `scripts/profile_training.py`. O script instrumenta as principais fases em tempo de execução sem modificar a implementação do Trainer/PPO. Ele grava JSON localmente; os relatórios não são enviados ao GitHub automaticamente.

## 1. Atualizar e entrar na branch

```powershell
git fetch origin
git switch debug/profile-resume-training
git pull
```

Use o mesmo checkout, build C++, ambiente Python, quantidade de lobbies e `rollout_steps` nos dois testes.

## 2. Rodar 40 updates do zero

Feche outros treinos antes de executar. O modo `fresh` remove temporariamente o checkpoint existente para garantir que o Trainer inicie sem ele. Se havia um checkpoint, ele é preservado em `tft_checkpoint.pre_profile_backup.pt`; o novo treino produz `tft_checkpoint.pt`, que será usado no teste de retomada.

```powershell
python scripts/profile_training.py --mode fresh --updates 40 --num-envs 1 --rollout-steps 8 --output reports/profile_fresh.json
```

Espere o processo terminar e confira se o relatório diz `Updates medidos: 40/40` e se `tft_checkpoint.pt` existe.

## 3. Retomar por mais 40 updates

Não apague nem substitua o checkpoint criado no passo anterior. Use exatamente os mesmos parâmetros:

```powershell
python scripts/profile_training.py --mode resume --updates 40 --num-envs 1 --rollout-steps 8 --output reports/profile_resumed.json
```

O segundo teste carrega o checkpoint salvo no primeiro teste e continua a partir do update seguinte. Os dois JSONs ficam em `reports/`.

## 4. O que comparar

- `training_wall_seconds`: tempo total dos 40 updates.
- `per_update[].measured_wall_seconds`: tempo aproximado por update.
- `phase_totals`: total, quantidade de chamadas e média por chamada de `environment_step`, `mask_retrieval`, `mask_flatten`, inferência da policy, conversão de ações e `ppo_update`.
- `per_update[].phase_seconds`: tempo acumulado por fase em cada update.
- Metadados: commit, versões de Python/PyTorch/NumPy, quantidade de lobbies e `rollout_steps`.

O profiler adiciona um pequeno overhead. Para uma comparação justa, mantenha o computador sem outras tarefas pesadas e não compare execuções com parâmetros ou builds diferentes.

## Recuperação se o modo fresh for interrompido

Se o treino falhar antes de criar um novo `tft_checkpoint.pt`, restaure a cópia anterior:

```powershell
Copy-Item tft_checkpoint.pre_profile_backup.pt tft_checkpoint.pt
```

Não execute isso se quiser manter o checkpoint novo gerado pelo treino fresh.
