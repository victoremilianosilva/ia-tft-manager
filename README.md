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

O runner exige um diretório de saída vazio, fixa as seeds por lobby, desabilita refresh externo de catálogo e não habilita migração de checkpoints antigos. Cada execução gera `native_ppo_checkpoint.pt`, `run_manifest.json` e logs TensorBoard. A bateria gera `battery_manifest.json`. Isso prepara e executa treinamento; não declara qualidade do modelo sem avaliação independente.

## Avaliação unificada da policy

Para gerar um relatório consolidado de auditoria estratégica, ações/recompensas,
máscaras, ciclos de estado e loops nativos em um único Markdown:

~~~powershell
python scripts/evaluate_all.py --checkpoint training_runs/native-battery/seed-11/native_ppo_checkpoint.pt --seeds 11,12,13
~~~

O relatório final é gravado em `reports/evaluation_report.md`; os dados brutos
JSONL/JSON ficam em `reports/evaluation_data/`. Para comparar dois checkpoints,
adicione `--baseline checkpoints/base.pt --candidate checkpoints/candidato.pt --matches 20`.
Para incluir a ablação dos controles de composição, acrescente `--ablation`.
Essas avaliações opcionais podem executar partidas adicionais e demorar mais.

## Catálogo de composições OP.GG

O treinamento nativo fixa os catálogos locais durante cada execução e registra a identidade semântica no manifesto. Atualizações externas de catálogo devem ser feitas antes de iniciar uma nova bateria, nunca durante um experimento em andamento. Veja [docs/opgg-meta-catalog.md](docs/opgg-meta-catalog.md).

## Componentes principais

- cpp/: engine C++, bindings e testes nativos.
- train_native.py, scripts/run_training_battery.py, trainer.py, policy.py, ppo.py, rollout.py: treinamento PPO nativo.
- cpp_lobby_env.py, vector_lobby_env.py: adaptadores Python.
- viewer/: interface de avaliação, sessão, logs e replay.
- scripts/, tests/: ferramentas e regressões.
