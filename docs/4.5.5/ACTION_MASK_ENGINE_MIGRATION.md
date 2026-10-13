# ActionMaskEngine — Migração para C++

## 1. Objetivo

Migrar a geração das máscaras de ações do `ai/ActionMaskManager.py` para C++, disponibilizando a API via pybind11 e preservando a compatibilidade com a política PPO atual.

A implementação deve processar candidatos internamente, gerar as máscaras em lote e reutilizar os componentes nativos de validação e anti-loop.

## 2. Arquivos envolvidos

| Arquivo                                     | Alteração                                                           |
| ------------------------------------------- | ------------------------------------------------------------------- |
| `cpp/include/decision/ActionMaskEngine.hpp` | Declarar a engine e a estrutura de saída.                           |
| `cpp/src/decision/ActionMaskEngine.cpp`     | Implementar a geração em lote.                                      |
| `cpp/include/decision/DecisionState.hpp`    | Representar o nível máximo na economia.                             |
| `cpp/src/decision/decision_bindings.cpp`    | Expor a API e as máscaras pelo pybind11.                            |
| `cpp/CMakeLists.txt`                        | Compilar a engine e incluir o validador como dependência do módulo. |
| `ai/ActionMaskManager.py`                   | Futuro adaptador entre os managers Python e o estado nativo.        |
| `lobby/TFTLobby.py`                         | Futuro ponto de integração para substituir a geração Python.        |

## 3. Contrato de saída

A API nativa retorna `ActionMaskBatch`, contendo oito máscaras nomeadas:

| Campo                         |   Dimensão |
| ----------------------------- | ---------: |
| `type_mask`                   |     `(7,)` |
| `shop_mask`                   |     `(5,)` |
| `bench_source_mask`           |     `(9,)` |
| `board_target_mask`           |    `(28,)` |
| `board_source_mask`           |    `(28,)` |
| `board_move_target_masks`     | `(28, 28)` |
| `bench_move_source_mask`      |     `(9,)` |
| `bench_to_board_target_masks` |  `(9, 28)` |

As máscaras utilizam valores `0` e `1`. O consumidor Python pode convertê-las para `numpy.bool_`, preservando as dimensões e a ordem dos índices.

A dimensão das cabeças de ação permanece `[7, 5, 9, 28, 28, 28]`.

## 4. Regras de geração

### Tipos de ação

* `BUY`: exige slot da loja disponível, espaço no banco e ouro suficiente.
* `REROLL`: exige ouro suficiente para o custo configurado.
* `BUY_XP`: exige ouro suficiente e nível inferior ao máximo.
* `MOVE_BENCH`: exige ao menos um movimento válido do banco para o tabuleiro.
* `MOVE_BOARD`: exige ao menos um movimento ou troca válida.
* `SELL`: exige pelo menos uma unidade no banco.
* `PASS`: permanece disponível para jogadores ativos; é a única ação permitida a jogadores eliminados.

### Loja e banco

A máscara da loja considera os slots ocupados, a disponibilidade de espaço no banco e o custo de cada unidade.

A máscara genérica do banco identifica unidades ocupadas e pode ser usada para venda. A máscara específica de movimentação identifica somente unidades com pelo menos um destino válido no tabuleiro.

### Tabuleiro

Cada origem ocupada possui uma linha de destinos válidos. Movimentos para a própria origem são inválidos.

* Destino vazio: classificado como `board_move`.
* Destino ocupado: classificado como `board_swap`.
* Origem vazia ou índice inválido: movimento rejeitado.

A movimentação do banco para o tabuleiro exige uma origem ocupada e um destino vazio.

### Máscaras condicionais

A matriz de movimentos do tabuleiro é condicionada à origem selecionada. A matriz de movimentação do banco é condicionada ao slot escolhido no banco.

A política PPO deve continuar selecionando primeiro a origem e depois o destino, sem substituir as máscaras condicionais por máscaras genéricas.

## 5. Integração com o validador e o AntiLoopEngine

`MoveValidator` verifica os requisitos básicos de legalidade dos movimentos.

`AntiLoopEngine` consulta os bloqueios de movimentos, reversões, oscilações e ciclos.

A geração de máscaras deve utilizar somente operações de consulta do anti-loop. Não deve registrar movimentos, atualizar históricos, contabilizar execuções nem modificar métricas durante a avaliação dos candidatos.

O histórico consultado precisa ser o mesmo utilizado pelo fluxo real de execução. Uma instância nativa independente e vazia não pode substituir silenciosamente o histórico do `AntiLoopManager` atual.

## 6. Desempenho

A engine calcula as matrizes de destinos e as máscaras de origem dentro do C++. O objetivo é evitar chamadas individuais Python → C++ para cada combinação de origem e destino.

A interface Python deve transferir o estado do jogador em lote e receber o resultado completo em uma chamada.

O ganho de desempenho ainda precisa ser medido com os benchmarks existentes após a integração.

## 7. Fallbacks e estados inconsistentes

As cabeças categóricas devem receber um fallback técnico quando não houver opções reais, evitando distribuições vazias.

O fallback não pode habilitar artificialmente `BUY`, `SELL`, `MOVE_BENCH` ou `MOVE_BOARD`.

Estados econômicos inválidos devem produzir um erro explícito, e não máscaras aparentemente válidas. Os dados de entrada precisam ser normalizados e validados antes da geração.

## 8. Checklist da implementação

* [x] Migrar a geração das máscaras de tipos de ação.
* [x] Migrar a geração das máscaras de seleção da loja.
* [x] Migrar a geração das máscaras do banco.
* [x] Migrar a geração das máscaras de origem no tabuleiro.
* [x] Migrar a geração das máscaras de destino no tabuleiro.
* [x] Migrar a geração das máscaras de movimentação entre banco e tabuleiro.
* [x] Migrar a geração das máscaras condicionais.
* [x] Preservar a dependência entre as etapas autoregressivas da política.
* [x] Preservar as restrições econômicas e de estado representadas na entrada nativa.
* [x] Preservar os casos de borda e os fallbacks documentados.
* [x] Integrar o validador de movimentos e o AntiLoopEngine sem duplicar a validação básica.
* [x] Evitar chamadas individuais Python → C++ para cada candidato.
* [x] Processar candidatos internamente em C++ e retornar resultados em lote.
* [x] Definir o formato de saída esperado pela política atual.
* [x] Preservar dimensões, ordem dos índices e semântica das máscaras implementadas.
* [x] Rejeitar estados econômicos inconsistentes em vez de gerar resultados silenciosamente.
* [ ] Integrar a conversão do estado real dos managers Python para `PlayerState`.
* [ ] Garantir que a engine utilize o histórico anti-loop real do jogador.
* [ ] Integrar a nova API ao `ActionMaskManager` e ao `TFTLobby`.
* [ ] Compilar o módulo e verificar a importação da API.
* [ ] Executar testes de equivalência entre as máscaras Python e C++.
* [ ] Executar os testes de integração e os benchmarks.

## 9. Critério de conclusão

A engine e sua interface nativa estarão implementadas quando o módulo compilar e expuser a API.

A migração funcional estará concluída somente depois que o fluxo real do treinamento utilizar essa API, compartilhar corretamente o histórico anti-loop e produzir máscaras equivalentes às da implementação Python nos cenários cobertos pelos testes.

A implementação Python deve permanecer disponível até a conclusão da validação integrada.
