# TFT-like RL Engine

Projeto de ambiente TFT-like para treinamento e avaliação de uma policy PPO compartilhada entre os oito jogadores de cada lobby. A engine de regras é C++ e é acessada por Python via bindings nativos.

## Documentação

A documentação técnica está em [docs/README.md](docs/README.md). Ela descreve arquitetura, subsistemas da engine, contrato de ações/máscaras, treinamento, viewer, logs, avaliação e build/testes.

## Build rápida

No Windows PowerShell, com CMake, compilador C++ e dependências Python instaladas:

~~~powershell
python -m pip install -r requirements.txt
python scripts/build_native.py
~~~

Para o viewer desktop, instale também viewer/requirements.txt e execute:

~~~powershell
python -m pip install -r viewer/requirements.txt
python -m viewer.main
~~~

Consulte [build e testes](docs/build-and-tests.md) para os pré-requisitos e [viewer](docs/viewer.md) para checkpoints e limitações.

## Treinamento PPO nativo

Para iniciar um treino novo e isolado, sem importar checkpoints históricos:

~~~powershell
python train_native.py --output-dir training_runs/smoke-seed-42 --seed 42 --updates 2 --lobbies 1 --rollout-steps 8
~~~

Para executar uma bateria multi-seed, com checkpoint e manifesto separados por execução:

~~~powershell
python scripts/run_training_battery.py --output-root training_runs/native-battery --seeds 11,12,13 --updates 160 --lobbies 4 --rollout-steps 128
~~~

O runner exige um diretório de saída vazio, fixa as seeds por lobby, desabilita refresh externo de catálogo e não habilita migração de checkpoints antigos. Cada execução gera `native_ppo_checkpoint.pt`, `run_manifest.json`, `artifact_manifest.json` com o SHA-256 do modelo e logs TensorBoard. A bateria gera `battery_manifest.json` com os hashes dos checkpoints. Isso prepara e executa treinamento; não declara qualidade do modelo sem avaliação independente.

## Benchmark isolado da engine

Para medir a engine C++ sem PPO, policy, construção de batch semântico ou otimizador, execute:

~~~powershell
python scripts/benchmark_engine.py --mode both --lobbies 1 4 --warmup 10 --iterations 100 --json-out training_runs/engine-benchmark.json --csv-out training_runs/engine-benchmark.csv
~~~

O modo `native` mede a chamada pybind de `TFTLobby.step()` (execução C++ e conversão do resultado na fronteira Python). O modo `wrapper` mede também o custo Python de validação, snapshots, auditoria de recompensa e eventos de outcome. As lobbies são executadas sequencialmente, como no `LobbyVectorEnv` atual. O relatório apresenta média, mediana, P95/P99, mínimo, máximo e throughput. Esse benchmark não mede PPO nem representa execução paralela.

## Avaliação de checkpoints

O módulo scripts/evaluate_checkpoints.py contém helpers de avaliação pareada e publicação de artefatos, mas ainda não oferece um entrypoint CLI completo. O protocolo de avaliação independente, splits sem vazamento e promoção de modelo permanece parte da trilha #523; não trate o smoke de treinamento como benchmark.

## Catálogo de composições OP.GG

O treinamento nativo fixa os catálogos locais durante cada execução e registra a identidade semântica no manifesto. Atualizações externas de catálogo devem ser feitas antes de iniciar uma nova bateria, nunca durante um experimento em andamento. Veja [docs/opgg-meta-catalog.md](docs/opgg-meta-catalog.md).

## Componentes principais

- cpp/: engine C++, bindings e testes nativos.
- train_native.py, scripts/run_training_battery.py, trainer.py, policy.py, ppo.py, rollout.py: treinamento PPO nativo.
- cpp_lobby_env.py, vector_lobby_env.py: adaptadores Python.
- viewer/: interface de avaliação, sessão, logs e replay.
- scripts/, tests/: ferramentas e regressões.
