# Arquitetura geral

## Visão por camadas

```text
trainer.py / scripts de avaliação / viewer
                |
        TFTPolicy (PyTorch)
                |
   CppTFTLobbyWrapper (Python)
                |
         pybind11 bindings
                |
          TFTEngine (C++)
   ┌────────────┼───────────────┐
 lobby/economia/loja       decisões/máscaras
   combate/recompensas     estratégia/posicionamento
                |
       observações, rewards, dones,
       estado público, snapshots e eventos
```

O caminho principal de execução passa pela engine nativa. `engine_contracts.py` mantém enums estáveis entre Python e C++; não implementa as regras do jogo.

## Responsabilidades

- **Engine C++ (`cpp/include`, `cpp/src`)**: estado da lobby, ações, economia, loja, unidades, estoque, combate, recompensas, máscaras, validação de movimento e snapshots.
- **Bindings (`cpp/bindings`, `cpp/src/decision/decision_bindings.cpp`)**: expõem a API nativa para Python.
- **Adaptadores Python (`cpp_lobby_env.py`, `vector_lobby_env.py`)**: normalizam entradas/saídas, agrupam as oito vagas de cada lobby e conectam a engine ao loop de treino.
- **Policy/PPO (`policy.py`, `ppo.py`, `rollout.py`)**: escolhem ações autoregressivas com máscaras, calculam objetivos PPO e armazenam transições.
- **Treinador (`trainer.py`)**: cria ambientes, coleta experiências, executa atualizações e grava checkpoint/métricas.
- **Viewer (`viewer/`)**: carrega checkpoint para avaliação, chama a engine existente, mostra snapshots e registra sessões; não treina a policy.
- **Ferramentas (`scripts/`, `tests/`)**: build, avaliação head-to-head, testes de contrato e regressão.

## Ciclo de uma ação

1. A engine disponibiliza observações e máscaras para cada jogador.
2. A policy escolhe o tipo de ação e os componentes condicionais válidos.
3. O adaptador transforma as ações no formato esperado pelo binding.
4. A engine valida e aplica as oito ações da lobby no passo nativo conjunto.
5. A engine resolve eventos da rodada conforme seu ciclo interno e retorna recompensas, observações e informação de auditoria.
6. O treinador guarda a transição no buffer; o viewer, quando usado, persiste a linha do tempo da sessão.

## Contratos críticos

- Uma lobby contém 8 jogadores.
- Tabuleiro: 28 posições (4 × 7); banco: 9 slots; loja: 5 slots.
- A ação é um vetor de 6 componentes, com dimensões `[7, 5, 9, 28, 28, 28]`.
- As máscaras condicionais de movimento têm formato `[origem, destino]`.
- O estado terminal precisa preservar ranking/colocações antes de qualquer reset automático do ambiente vetorizado.

Detalhes: [contratos e dados](contracts-and-data.md), [ambientes Python](python-environments.md), [treinamento](rl-training.md).
