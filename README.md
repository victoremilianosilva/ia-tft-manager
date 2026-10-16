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

## Componentes principais

- cpp/: engine C++, bindings e testes nativos.
- trainer.py, policy.py, ppo.py, rollout.py: treinamento PPO.
- cpp_lobby_env.py, vector_lobby_env.py: adaptadores Python.
- viewer/: interface de avaliação, sessão, logs e replay.
- scripts/, tests/: ferramentas e regressões.
