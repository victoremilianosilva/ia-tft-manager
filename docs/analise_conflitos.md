# Análise de Precedência e Conflitos entre Regras de Bloqueio — Action Masks e AntiLoop

## 1. Objetivo

Documentar o comportamento atual quando múltiplas regras de validação ou proteções AntiLoop se aplicam ao mesmo candidato, identificando:

- A ordem de avaliação.
- O motivo que prevalece.
- As regras que podem coexistir.
- A diferença entre rejeição por ilegalidade e bloqueio AntiLoop.
- As diferenças entre geração de máscaras e execução.
- As métricas e os efeitos colaterais associados ao resultado.

A implementação Python atual é a referência de equivalência para o módulo C++.

## 2. Precedência principal do AntiLoop

O método `AntiLoopManager.get_block_reason()` avalia as proteções na seguinte ordem:

| Prioridade | Regra | Motivo retornado | Condição resumida |
|---:|---|---|---|
| 1 | Bloqueio explícito | `explicit` | A chave do movimento está bloqueada e a assinatura associada coincide com o estado registrado atual |
| 2 | Movimento inverso | `reverse` | O candidato desfaz o último movimento de acordo com as regras de identidade e tipo |
| 3 | Oscilação | `oscillation` | O histórico recente da unidade indica repetição de destinos na sequência contínua |
| 4 | Ciclo banco ↔ tabuleiro | `bench_board_loop` | O tipo do candidato é reconhecido e a sequência recente confirma a ida e volta correspondente |
| 5 | Ciclo no tabuleiro | `cycle` | O histórico confirma o fechamento repetido de um ciclo de movimentos no tabuleiro |
| — | Nenhuma regra reconhece o candidato | `None` | O AntiLoop não identifica motivo de bloqueio |

**Regra determinante:** a primeira proteção que retorna verdadeiro define o motivo final. As regras posteriores não são consultadas por `get_block_reason()` depois que uma correspondência é encontrada.

A ordem acima deve ser reproduzida exatamente pelo C++, inclusive em situações em que duas ou mais proteções reconheceriam o mesmo candidato se fossem avaliadas isoladamente.

## 3. Conflitos entre proteções AntiLoop

### 3.1. Bloqueio explícito versus qualquer outra regra

Se o candidato estiver bloqueado explicitamente no estado atual, o resultado será `explicit`, mesmo que ele também seja uma reversão, oscilação ou ciclo.

As demais proteções não alteram esse motivo.

Se a assinatura do estado não corresponder à assinatura associada ao bloqueio, a proteção explícita não prevalece; a avaliação continua para a próxima regra.

### 3.2. Reversão versus oscilação

Se o mesmo candidato for reconhecido como movimento inverso e oscilação, prevalece `reverse`.

A avaliação de oscilação só determina o resultado se a proteção de reversão não bloquear o candidato.

### 3.3. Oscilação versus ciclo banco ↔ tabuleiro

Quando o candidato pertence a um ciclo banco ↔ tabuleiro, mas também é reconhecido como oscilação pela lógica atual, prevalece `oscillation`.

A proteção `bench_board_loop` só é avaliada se as regras anteriores não retornarem bloqueio.

### 3.4. Ciclo banco ↔ tabuleiro versus ciclo no tabuleiro

Se a proteção banco ↔ tabuleiro reconhecer o candidato, o motivo será `bench_board_loop`. O método retorna imediatamente e não consulta a regra de ciclo geral.

Além disso, `is_cycle_move()` aceita somente os tipos `board_move` e `board_swap`. Portanto, um candidato banco ↔ tabuleiro não é bloqueado por essa regra geral na implementação atual.

### 3.5. Ciclo geral isolado

O motivo `cycle` só prevalece quando:

- O bloqueio explícito não se aplica.
- A reversão não se aplica.
- A oscilação não se aplica.
- O ciclo banco ↔ tabuleiro não se aplica.
- `is_cycle_move()` reconhece o ciclo para `board_move` ou `board_swap`.

### 3.6. Matriz de precedência

Quando as regras indicadas nas linhas e colunas reconhecem o mesmo candidato, a seguinte ordem determina o motivo:

| Regra reconhecida | Explicit | Reverse | Oscillation | Bench-board | Cycle |
|---|---|---|---|---|---|
| Explicit | `explicit` | `explicit` | `explicit` | `explicit` | `explicit` |
| Reverse | `explicit` | `reverse` | `reverse` | `reverse` | `reverse` |
| Oscillation | `explicit` | `reverse` | `oscillation` | `oscillation` | `oscillation` |
| Bench-board | `explicit` | `reverse` | `oscillation` | `bench_board_loop` | `bench_board_loop` |
| Cycle | `explicit` | `reverse` | `oscillation` | `bench_board_loop` | `cycle` |

A matriz expressa a precedência do método `get_block_reason()`, não garante que toda combinação seja possível para os tipos de movimento aceitos.

## 4. A precedência AntiLoop não substitui a validação básica

As regras AntiLoop são apenas uma parte da validação de movimentos. Antes ou depois dessa consulta, conforme o caminho de execução, existem condições de legalidade que também podem rejeitar uma ação.

### 4.1. Movimento banco → tabuleiro

Na geração das máscaras, `_is_valid_bench_board_move()` verifica:

1. O índice da origem existe no banco.
2. Existe uma unidade na origem.
3. O destino é uma posição válida.
4. O AntiLoop não bloqueia o candidato.

A geração das máscaras percorre as posições vazias do tabuleiro como destinos candidatos.

Na execução, `_execute_move_bench()` verifica índices, validade do destino e existência da unidade; registra uma tentativa; consulta `get_block_reason()`; e, se não houver bloqueio AntiLoop, verifica se o destino continua vazio antes de efetuar a movimentação.

**Consequência:** se o destino estiver ocupado, mas não houver motivo AntiLoop, a execução pode rejeitar a ação por ilegalidade sem definir `anti_loop_blocked`.

### 4.2. Movimento ou troca no tabuleiro

Na geração das máscaras, `_is_valid_board_move()` verifica:

1. Origem e destino dentro dos limites do tabuleiro.
2. Origem diferente do destino.
3. Existência de unidade na origem.
4. Se o destino está ocupado, consulta `board_swap`; se estiver vazio, consulta `board_move`.
5. Rejeita o candidato se o AntiLoop o bloquear.

Na execução, `_execute_move_board()` realiza as validações básicas, determina `board_move` ou `board_swap` com base na ocupação atual do destino e consulta o AntiLoop antes de efetuar a operação.

A validade do movimento pode mudar entre a geração da máscara e a execução se o estado for alterado nesse intervalo. Por isso, a execução precisa revalidar o candidato.

## 5. Diferença entre bloqueio na máscara e bloqueio na execução

| Situação | Resultado | Histórico de execução |
|---|---|---|
| Candidato ilegal durante geração de máscaras | Não habilitado | Não registra tentativa ou bloqueio de execução |
| Candidato bloqueado pelo AntiLoop durante geração de máscaras | Não habilitado | Não incrementa métricas de execução |
| Consulta AntiLoop lança exceção na geração de máscaras | `_should_block_anti_loop()` permite o candidato nessa camada e registra o erro | Não registra movimento executado |
| Ação chega à execução e é bloqueada pelo AntiLoop | A execução retorna penalidade e inclui o motivo em `info["anti_loop_blocked"]` | Incrementa tentativa, bloqueio total e contador específico quando existente |
| Ação passa pelo AntiLoop, mas falha na operação de movimento | A execução retorna penalidade | A tentativa é registrada; não há registro de movimento bem-sucedido |
| Movimento concluído | Estado atualizado e ação marcada como bem-sucedida | Registra movimento e métrica de sucesso |

A exceção na geração de máscaras tem comportamento permissivo: `_should_block_anti_loop()` retorna `False` quando a consulta falha. Isso não elimina as validações básicas do método chamador, mas significa que a proteção AntiLoop pode não ser aplicada àquele candidato durante a geração da máscara.

## 6. Diferença entre `get_block_reason()` e `evaluate_move_risk()`

Os dois métodos não são equivalentes.

`get_block_reason()` usa precedência e retorna o primeiro motivo de bloqueio encontrado.

`evaluate_move_risk()` calcula uma pontuação separada:

- Bloqueio explícito: retorna `1.0` imediatamente.
- Reversão: soma `0.7`.
- Oscilação: soma `0.8`.
- Ciclo banco ↔ tabuleiro: soma `0.9`.
- Resultado final: limitado a `1.0`.

O método de risco não consulta `is_cycle_move()` como incremento independente. Assim, um candidato bloqueado por `cycle` pode ter risco `0.0` se nenhuma das condições consideradas pela pontuação for verdadeira.

Também é importante que o método de risco não retorna o motivo de bloqueio e não substitui `get_block_reason()`.

A implementação C++ deve manter essa diferença caso ambos os comportamentos sejam migrados.

## 7. Efeitos nas métricas

Na execução, `record_execution_block(reason)` incrementa:

1. `execution_blocks`.
2. `blocked_<reason>`, se a chave existir em `execution_metrics`.

As métricas específicas inicializadas atualmente são:

- `blocked_reverse`
- `blocked_oscillation`
- `blocked_explicit`
- `blocked_bench_board_loop`
- `blocked_cycle`

O método de registro não normaliza nomes arbitrários para chaves conhecidas. Se o motivo não corresponder a uma chave existente, o bloqueio total ainda é contabilizado, mas o contador específico não é incrementado.

No caminho de execução de movimento no tabuleiro, se `should_block_move()` retornar verdadeiro, o código consulta novamente `get_block_reason()` para obter o motivo. Se o resultado não for uma string, substitui-o por `unknown`. Como não existe `blocked_unknown` nas métricas atuais, esse caso incrementa o total, mas não um contador específico.

No caminho banco → tabuleiro, a execução usa diretamente o motivo retornado por `get_block_reason()`.

As máscaras, por outro lado, não devem incrementar essas métricas apenas por avaliar candidatos.

## 8. Casos obrigatórios para testes de conflito

Para validar a equivalência entre Python e C++, devem existir casos determinísticos para:

1. Bloqueio explícito + reversão: motivo `explicit`.
2. Bloqueio explícito + oscilação: motivo `explicit`.
3. Reversão + oscilação: motivo `reverse`.
4. Oscilação + ciclo geral: motivo `oscillation`.
5. Ciclo banco ↔ tabuleiro + outra proteção anterior: prevalece a proteção anterior.
6. Ciclo banco ↔ tabuleiro isolado: motivo `bench_board_loop`.
7. Ciclo geral isolado: motivo `cycle`.
8. Nenhuma proteção aplicável: resultado `None`.
9. Destino ocupado no banco → tabuleiro sem bloqueio AntiLoop: rejeição por legalidade, sem motivo AntiLoop.
10. Falha na consulta AntiLoop durante geração de máscaras: candidato permitido nessa camada e erro registrado.
11. Bloqueio na execução: motivo em `info`, métricas atualizadas e nenhuma movimentação bem-sucedida registrada.
12. Consulta repetida ao motivo: sem alterações de histórico ou métricas.

Cada caso deve comparar o motivo exato, não somente o valor booleano de bloqueio.

## 9. Requisitos para a migração C++

A implementação nativa deve preservar:

- A ordem exata das regras em `get_block_reason()`.
- As condições de identidade e tipo de cada proteção.
- A diferença entre validação básica e proteção AntiLoop.
- A distinção entre geração de máscaras e execução.
- A semântica de exceções na camada Python de integração.
- A precedência dos motivos e os nomes usados para métricas.
- A ausência de efeitos colaterais durante consultas.
- A revalidação durante a execução, que continua sob responsabilidade do Python.

Não se deve otimizar a avaliação executando todas as proteções e selecionando o motivo depois, a menos que isso preserve integralmente os resultados e não introduza efeitos colaterais. Na implementação atual, a avaliação para na primeira correspondência.

## 10. Conclusão

A precedência atual é determinística: `explicit` → `reverse` → `oscillation` → `bench_board_loop` → `cycle` → `None`.

O motivo final não é necessariamente a única regra aplicável, mas a primeira que corresponde segundo essa ordem. A legalidade básica é avaliada separadamente e pode rejeitar uma ação sem gerar um motivo AntiLoop.

Para a migração, a equivalência exige preservar tanto o bloqueio final quanto seu motivo, o caminho em que ocorreu, as métricas resultantes e a ausência de efeitos colaterais nas consultas.