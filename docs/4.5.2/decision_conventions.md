# Decision Engine — Convenções de Tipos e Interfaces

## 1. Objetivo

Padronizar índices, enums, valores ausentes, máscaras e erros entre os componentes nativos do `decision_engine` e as interfaces Python.

Este contrato preserva a compatibilidade com as dimensões de ação atuais e evita ambiguidades na validação.

## 2. Enums

Os enums que fazem parte do contrato devem utilizar um tipo subjacente explícito e valores numéricos estáveis.

`ActionType` mantém os seguintes valores:

| Valor | Ação |
|---:|---|
| 0 | BUY |
| 1 | REROLL |
| 2 | BUY_XP |
| 3 | MOVE_BENCH |
| 4 | MOVE_BOARD |
| 5 | SELL |
| 6 | PASS |

Mudanças de nome ou de implementação não devem alterar esses valores sem uma migração coordenada da política e do ambiente.

`MoveType`, `BlockReason` e `ValidationStatus` representam conceitos diferentes e não devem ser usados como substitutos uns dos outros.

## 3. Índices

Os índices válidos são:

- Tabuleiro: 0 a 27.
- Banco: 0 a 8.
- Loja: 0 a 4.

`RawIndex` representa um valor ainda não validado, recebido de uma camada externa.

`BoardIndex`, `BenchIndex` e `ShopIndex` representam índices que passaram pela validação de faixa.

Nenhum valor externo deve ser convertido diretamente para um tipo de índice compacto antes da validação.

A conversão deve produzir um resultado explícito: índice válido ou ausência de resultado.

O índice zero é válido e nunca deve representar, implicitamente, ausência de valor.

## 4. Valores ausentes

Campos opcionais devem utilizar `std::optional<T>`.

A ausência de uma unidade em um slot deve ser representada por `std::nullopt`.

A ausência de um índice ou identificador não deve ser representada por zero, string vazia ou um sentinel numérico implícito.

Quando um campo obrigatório estiver ausente, o componente responsável deve devolver um resultado inválido ou um erro, conforme a natureza do problema.

## 5. Máscaras

Os valores permitidos são:

- `0`: ação ou candidato indisponível.
- `1`: ação ou candidato disponível.

As dimensões principais, na ordem consumida pela política, são:

`[7, 5, 9, 28, 28, 28]`

Correspondem a tipo de ação, slot da loja, slot do banco, destino do tabuleiro, origem do tabuleiro e destino condicionado.

As máscaras auxiliares condicionadas por origem continuam disponíveis para a integração interna, mas não devem alterar a ordem das seis dimensões principais.

Uma máscara que utiliza fallback técnico para evitar uma distribuição vazia não prova que existe uma ação real válida. A disponibilidade da ação deve ser determinada separadamente.

## 6. Resultados e erros

Os resultados distinguem:

- Validação válida.
- Entrada inválida.
- Erro interno.

Motivos de bloqueio são informações específicas sobre decisões recusadas e não devem ser usados para indicar falhas internas.

As consultas de candidatos e máscaras devem ser somente de leitura. Não devem registrar movimentos executados nem alterar métricas de execução.

A interface Python deve receber resultados com semântica consistente, sem depender de exceções para representar entradas inválidas esperadas.

## 7. Compatibilidade

O contrato deve preservar:

- Valores numéricos de `ActionType`.
- Dimensões e ordem das máscaras principais.
- Limites do tabuleiro, banco e loja.
- Distinção entre slot vazio, índice inválido e índice zero.
- Semântica do histórico e das métricas de execução.

Qualquer alteração incompatível deve ser acompanhada por atualização explícita da integração Python e dos testes de contrato.

## 8. Critérios de aceitação

- Índices negativos são rejeitados antes da conversão.
- Índices iguais ao limite superior são rejeitados.
- O índice zero continua válido.
- Valores de `ActionType` são protegidos por verificações estáticas.
- Máscaras aceitam apenas valores binários.
- Fallbacks técnicos não são confundidos com ações reais disponíveis.
- Os contratos permanecem independentes da implementação da lógica de decisão.
