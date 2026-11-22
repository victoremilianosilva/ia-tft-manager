# Treinamento PPO nativo

O runtime operacional é iniciado por train_native.py ou scripts/run_training_battery.py. O PPO aprende a partir da projeção semântica dos snapshots produzidos pela Engine nativa. A Engine e as action masks continuam sendo a autoridade final de legalidade.

## Arquivos centrais

- trainer.py: orquestra Engine, policy, rollout, otimizador, scheduler, métricas e checkpoints.
- policy.py: encoder semântico, encoder espacial, cabeças condicionais de ação e value head.
- semantic_observation.py: projeção versionada dos fatos e owners nativos.
- rollout.py: transições sincronizadas, identidade, máscaras, validade, retornos e vantagens.
- ppo.py: loss e atualização PPO.
- vector_lobby_env.py: lobbies nativas independentes e seed determinística por lobby.
- training_run_manifest.py: identidade da execução, revisão do código, binário nativo, configuração e contratos.

## Início de treino

Smoke test:

```powershell
python train_native.py --output-dir training_runs/smoke-seed-42 --seed 42 --updates 2 --lobbies 1 --rollout-steps 8
```

Bateria multi-seed:

```powershell
python scripts/run_training_battery.py --output-root training_runs/native-battery --seeds 11,12,13 --updates 160 --lobbies 4 --rollout-steps 128
```

Cada seed recebe um diretório próprio. O runner exige diretório vazio, desabilita refresh externo de catálogo, não habilita migração histórica e registra um manifesto por execução. O checkpoint final inclui policy, optimizer, scheduler, contratos e manifesto.

## Escala de coleta

Trainer.num_envs representa o número de lobbies, não o número de jogadores. Cada lobby contém oito agentes e todos compartilham a mesma policy. As observações têm formato de lote (lobbies, 8, obs_dim) antes do flatten. As máscaras seguem o mesmo ordenamento de agentes.

## Policy, ações e masks

A policy amostra o tipo da ação e apenas os argumentos condicionais relevantes. As masks exatas da decisão são consumidas pelo actor e pelo critic como side input independente. A Engine valida novamente a ação; recomendações estratégicas não substituem nem contornam esse contrato.

## PPO e rollout

O buffer mantém observação, ação, log-probability, reward, done, value, máscaras e identidade de cada transição. A projeção semântica e os hashes de identidade acompanham as transições até a atualização PPO. O GAE é calculado por jogador, respeitando fronteiras de episódio e validade.

## Checkpoint e linhagem

Cada execução grava native_ppo_checkpoint.pt e run_manifest.json. O manifesto registra revisão do código, hash do módulo C++ carregado, runtime Python/PyTorch/NumPy, seed, configuração, arquitetura, catálogo semântico e contratos de observação, ação/mask, reward e retomada. A retomada exige identidade de execução idêntica; checkpoints históricos não são importados pelo runner nativo.

## Limite de avaliação

Uma bateria multi-seed comprova execução reproduzível, não qualidade ou superioridade. O benchmark final ainda exige avaliação independente por episódios/seeds, métricas de placement/top-4/top-1, retorno, sobrevivência, estabilidade, comportamento de ações/masks, análise de incerteza e comparação com baseline imutável. O Viewer fica fora desta etapa.