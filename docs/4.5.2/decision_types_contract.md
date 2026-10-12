# Decision Engine — Contrato de Tipos Compartilhados

## 1. Objetivo

Definir os tipos fundamentais compartilhados pelos componentes nativos do `decision_engine`, garantindo consistência entre validação de movimentos, geração de máscaras de ações e prevenção de loops.

O contrato deve permitir a integração com o ambiente Python e manter o módulo de decisões independente do motor de combate.

## 2. Namespace e organização

Os tipos compartilhados pertencem ao namespace `tft::decision`.

Arquivo principal:

`cpp/include/decision/DecisionTypes.hpp`

Os tipos devem ser declarados em um header comum para evitar definições duplicadas nos componentes nativos.

## 3. Tipos fundamentais

### ActionType

Representa os tipos de ação disponibilizados à política PPO.

| Valor | Ação |
|---:|---|
| 0 | BUY |
| 1 | REROLL |
| 2 | BUY_XP |
| 3 | MOVE_BENCH |
| 4 | MOVE_BOARD |
| 5 | SELL |
| 6 | PASS |

Os valores numéricos existentes devem ser preservados para não alterar o contrato com a política.

### MoveType

Representa as categorias de movimento consultadas pelo sistema de validação e AntiLoop.

- `BENCH_TO_BOARD`: movimento do banco para o tabuleiro.
- `BOARD_MOVE`: movimentação de uma unidade no tabuleiro.
- `BOARD_SWAP`: troca de posições entre unidades do tabuleiro.

Essas categorias descrevem movimentos internos e não substituem os índices de `ActionType`.

### BlockReason

Identifica o motivo de um movimento ter sido bloqueado:

- `NONE`
- `EXPLICIT`
- `REVERSE`
- `OSCILLATION`
- `BENCH_BOARD_LOOP`
- `CYCLE`

Os valores representam as categorias de bloqueio existentes no comportamento do AntiLoop. A precedência entre elas será definida no contrato específico do AntiLoop.

### ValidationStatus

Representa o resultado da validação de uma operação:

- `VALID`
- `INVALID`
- `ERROR`

A distinção entre entrada inválida e erro interno permite diagnósticos mais claros.

### Tipos de índice

Os aliases `BoardIndex`, `BenchIndex` e `ShopIndex` representam índices de posições do tabuleiro, banco e loja, respectivamente.

As faixas válidas são:

- Tabuleiro: 28 posições.
- Banco: 9 posições.
- Loja: 5 posições.

Os aliases não substituem a validação de limites. A validação efetiva será implementada pelos componentes responsáveis.

### MaskValue

Representa um elemento binário de máscara de ação. O valor zero indica ação indisponível; o valor um indica ação disponível.

## 4. Compatibilidade com o motor de combate

O `decision_engine` mantém seu próprio namespace e seus tipos específicos de decisão.

Os tipos de combate existentes não devem ser reutilizados automaticamente para representar movimentos, máscaras ou histórico de decisões.

Quando houver necessidade de integração entre os módulos, a conversão deve ocorrer explicitamente na camada responsável pela integração.

## 5. Dependências

A implementação deve utilizar a biblioteca padrão do C++ sempre que possível.

Não devem ser introduzidas dependências adicionais apenas para representar enums, índices ou valores binários.

## 6. Escopo desta etapa

Esta etapa define os tipos fundamentais compartilhados.

Não faz parte deste escopo:

- Modelagem completa do estado do jogador.
- Estruturas de unidades, posições e histórico.
- Estruturas de resultados detalhados.
- Convenções completas de valores ausentes e dimensões das máscaras.
- Regras de validação e diagnósticos.
- Implementação das máscaras ou do AntiLoop.

Esses pontos serão tratados nas tasks correspondentes, evitando antecipar decisões que dependem de contratos posteriores.
