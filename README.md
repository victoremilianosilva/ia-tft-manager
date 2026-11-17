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

## Avaliação unificada da policy

Para gerar um relatório consolidado de auditoria estratégica, ações/recompensas,
máscaras, ciclos de estado e loops nativos em um único Markdown:

~~~powershell
python scripts/evaluate_all.py --checkpoint checkpoints/latest.pt --seeds 11,12,13
~~~

O relatório final é gravado em `reports/evaluation_report.md`; os dados brutos
JSONL/JSON ficam em `reports/evaluation_data/`. Para comparar dois checkpoints,
adicione `--baseline checkpoints/base.pt --candidate checkpoints/candidato.pt --matches 20`.
Para incluir a ablação dos controles de composição, acrescente `--ablation`.
Essas avaliações opcionais podem executar partidas adicionais e demorar mais.

## Catálogo de composições OP.GG

O treino atualiza o snapshot local de meta antes de iniciar; o Viewer reutiliza o mesmo catálogo e só consulta novamente quando ele está vencido. O C++ compara composições conhecidas com o plano nativo, usando snapshots de early/mid game como informação de transição, sem tornar unidades obrigatórias. Veja [docs/opgg-meta-catalog.md](docs/opgg-meta-catalog.md).

## Componentes principais

- cpp/: engine C++, bindings e testes nativos.
- trainer.py, policy.py, ppo.py, rollout.py: treinamento PPO.
- cpp_lobby_env.py, vector_lobby_env.py: adaptadores Python.
- viewer/: interface de avaliação, sessão, logs e replay.
- scripts/, tests/: ferramentas e regressões.
