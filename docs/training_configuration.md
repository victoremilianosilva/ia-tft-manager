# Configuração do treinamento PPO nativo

O runtime operacional de treinamento é iniciado por train_native.py. Ele sempre cria uma nova execução em um diretório exclusivo, usa a projeção semântica dos snapshots nativos, fixa as seeds e não importa checkpoints históricos.

## Treino isolado

```powershell
python train_native.py --output-dir training_runs/native-seed-42 --seed 42 --updates 160 --lobbies 4 --rollout-steps 128 --batch-size 64 --ppo-epochs 4
```

Para uma bateria com execuções independentes:

```powershell
python scripts/run_training_battery.py --output-root training_runs/native-battery --seeds 11,12,13 --updates 160 --lobbies 4 --rollout-steps 128
```

No PowerShell, .\train_cycle.ps1 chama o runner multi-seed e registra a saída com Start-Transcript.

Cada execução produz:
- native_ppo_checkpoint.pt: pesos, optimizer, scheduler e contratos.
- run_manifest.json: revisão do código, hash do binário C++, seed, configuração, arquitetura e contratos.
- tensorboard/: métricas e diagnósticos PPO.

A bateria produz battery_manifest.json, relacionando as seeds e os artefatos gerados. Os diretórios precisam estar vazios; o runner não sobrescreve modelos anteriores.

## Parâmetros

| Argumento | Finalidade |
|---|---|
| --output-dir | Diretório exclusivo de uma execução |
| --seed | Seed global, com offset determinístico por lobby |
| --updates | Quantidade de updates PPO |
| --lobbies | Quantidade de lobbies C++ simultâneas |
| --rollout-steps | Decisões coletadas por update |
| --batch-size | Tamanho do minibatch PPO |
| --ppo-epochs | Épocas de otimização por update |
| --learning-rate | Learning rate inicial |
| --min-learning-rate | Piso do scheduler |
| --lr-schedule-updates | Horizonte do scheduler |
| --target-kl | Limite de KL para early stop |

A configuração também é persistida no manifesto de cada execução. A execução é CPU por enquanto; a disponibilidade de GPU é registrada, mas não selecionada automaticamente pelo trainer.

## Retomada e checkpoints históricos

O runner de treinamento novo não oferece importação implícita nem warm-start de checkpoints históricos. A retomada exige a mesma identidade de execução, incluindo seed, revisão do código, binário nativo, configuração e contratos. Checkpoints antigos devem permanecer como baselines imutáveis e ser avaliados em um fluxo separado.

## Interpretação dos resultados

Uma bateria multi-seed comprova que o treino foi executado em condições identificadas. Ela não comprova, por si só, que a policy melhorou. Placement, top-4/top-1, retorno, sobrevivência, estabilidade, métricas econômicas, variância entre seeds e avaliação em episódios independentes ainda precisam ser medidos antes de promover um modelo.
