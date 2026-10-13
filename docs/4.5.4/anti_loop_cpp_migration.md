# Migração do AntiLoopManager para C++

## 1. Objetivo

Migrar a lógica do `ai/AntiLoopManager.py` para C++, preservando as regras de detecção de loops, os critérios de identidade, o histórico, os motivos de bloqueio e a ordem de avaliação.

A implementação nativa está organizada em:

* `cpp/include/decision/DecisionState.hpp`
* `cpp/include/decision/DecisionHistory.hpp`
* `cpp/include/decision/AntiLoopEngine.hpp`
* `cpp/src/decision/AntiLoopEngine.cpp`

O Python permanece como referência comportamental durante a migração.

## 2. Responsabilidades

### 2.1. Identificação de unidades

A identidade prioriza o UUID quando disponível.

Na ausência de UUID, a comparação utiliza `id` e `star`.

A implementação C++ utiliza os tipos existentes no projeto:

* `uuid`: `std::optional<std::string>`
* `id`: `std::optional<std::int64_t>`
* `star`: `std::uint8_t`

A representação nativa não abrange automaticamente todos os tipos dinâmicos aceitos pelo Python. A conversão de objetos Python para `UnitIdentity` deve preservar os valores e a distinção entre ausência de identidade e unidade identificada.

### 2.2. Chaves de movimentos

`MoveKey` representa um movimento por:

* Tipo.
* Origem.
* Destino.
* Identidade opcional da unidade.

O tipo do movimento é textual para permitir os aliases usados pela implementação Python.

### 2.3. Assinaturas de estado

`PositionSignature` representa as unidades presentes no tabuleiro e no banco.

As assinaturas são utilizadas para:

* Registrar estados visitados.
* Contabilizar repetições.
* Associar bloqueios ao estado em que foram criados.
* Verificar se um bloqueio continua válido.

A estrutura C++ usa as dimensões fixas do ambiente: 28 posições no tabuleiro e 9 no banco.

### 2.4. Histórico de movimentos

`AntiLoopHistory` mantém:

* Histórico de assinaturas de estado.
* Histórico de movimentos.
* Movimentos bloqueados.
* Contagem de visitas por estado.
* Última assinatura registrada.
* Último movimento.
* Métricas acumuladas.

Os limites de retenção são configurados por `AntiLoopConfig`.

## 3. Detectores de loops

### 3.1. Movimento inverso

`is_reverse_move()` identifica a reversão de um movimento.

Para `board_swap`, considera o par de posições, independentemente da identidade informada no movimento candidato.

Para os demais movimentos, exige correspondência do tipo e da identidade, além da inversão entre origem e destino.

### 3.2. Oscilação

`is_oscillating()` examina os seis registros mais recentes e filtra os movimentos relevantes para a unidade.

Para `board_move`, considera movimentos desse tipo.

Para `board_swap`, também considera os movimentos de tabuleiro relevantes à unidade.

O movimento candidato só caracteriza oscilação quando o destino já apareceu pelo menos duas vezes na cadeia reconstruída.

### 3.3. Movimentos entre banco e tabuleiro

`is_bench_board_loop()` normaliza os aliases:

* `MOVE_BENCH_TO_BOARD`
* `bench_to_board`
* `MOVE_BOARD_TO_BENCH`
* `board_to_bench`

A detecção exige uma ida e volta pelas mesmas posições, seguida da tentativa de repetir a transição anterior.

### 3.4. Ciclos

`is_cycle_move()` considera os oito movimentos relevantes mais recentes da unidade.

A sequência precisa ser contínua, e o histórico precisa demonstrar que o ciclo já foi completado antes de bloquear o novo fechamento.

## 4. Ordem dos motivos de bloqueio

`get_block_reason()` avalia as regras na seguinte ordem:

1. `explicit`
2. `reverse`
3. `oscillation`
4. `bench_board_loop`
5. `cycle`
6. `None`, quando nenhuma regra bloqueia o movimento

Essa ordem é parte do contrato comportamental: quando mais de uma condição é verdadeira, ela determina o motivo retornado.

## 5. Histórico e efeitos colaterais

As consultas de bloqueio não devem modificar o histórico nem as métricas.

Métodos de consulta:

* `is_move_blocked()`
* `is_reverse_move()`
* `is_oscillating()`
* `is_bench_board_loop()`
* `is_cycle_move()`
* `get_block_reason()`
* `should_block_move()`
* `evaluate_move_risk()`
* `was_state_seen()`
* `get_state_visits()`
* `get_state()`
* `get_metrics()`

Métodos de registro ou manutenção:

* `register_state()`
* `register_move()`
* `block_move()`
* `reset()`
* `clear_old_blocks()`
* `record_execution_attempt()`
* `record_execution_block()`
* `record_successful_move()`

`reset()` limpa o histórico, mas preserva as métricas acumuladas.

A chamada de `record_execution_block()` deve ocorrer no fluxo real de execução, e não para cada candidato descartado durante a construção de máscaras.

## 6. Risco de movimento

`evaluate_move_risk()` utiliza os seguintes pesos:

| Condição                     | Risco adicionado |
| ---------------------------- | ---------------: |
| Movimento inverso            |              0,7 |
| Oscilação                    |              0,8 |
| Loop entre banco e tabuleiro |              0,9 |

Um bloqueio explícito retorna risco `1,0` imediatamente. Nos demais casos, o resultado é limitado a `1,0`.

## 7. Métricas

A estrutura `ExecutionMetrics` registra:

* Tentativas de execução.
* Bloqueios durante a execução.
* Bloqueios por motivo.
* Movimentos de tabuleiro executados.
* Movimentos do banco para o tabuleiro executados.

As métricas são acumuladas durante a vida do objeto e preservadas por `reset()`.

## 8. Compatibilidade e limitações conhecidas

A implementação C++ usa estruturas tipadas, enquanto o Python recebe objetos dinâmicos e sequências que podem ter comprimentos variáveis.

Antes de declarar equivalência, será necessário verificar:

* Conversão de unidades Python para `UnitIdentity`.
* Tratamento de UUID, ID ausente e estrela.
* Equivalência das chaves de movimentos.
* Assinaturas de estado e posições vazias.
* Comportamento dos limites dos históricos.
* Todos os aliases de movimentos usados pelo ambiente.
* Precedência dos motivos quando mais de um detector é acionado.
* Compatibilidade com os consumidores atuais de `DecisionHistory.hpp`.

A representação fixa de 28 posições de tabuleiro e 9 posições de banco corresponde às dimensões previstas pelo ambiente, mas não reproduz assinaturas Python de sequências arbitrárias de comprimentos diferentes.

## 9. Integração Python/C++

A `AntiLoopEngine` é exposta pelo módulo `decision_engine` por meio do `pybind11`.

### 9.1. Tipos disponíveis

O módulo disponibiliza:

* `AntiLoopEngine`: motor nativo de detecção de loops.
* `AntiLoopConfig`: configuração dos limites do histórico.
* `UnitIdentity`, `UnitSnapshot` e `PlayerState`: identidade e estado das unidades.
* `PositionSignature`: assinatura do posicionamento.
* `MoveRecord` e `MoveKey`: registro e identificação dos movimentos.
* `StateRegistrationResult`, `AntiLoopStateSummary` e `ExecutionMetrics`: resultados, resumo e métricas.

A classe `DecisionEngine` existente continua exposta pelo mesmo módulo.

### 9.2. API disponível

A interface Python permite acessar as operações de registro, detecção, bloqueio, avaliação de risco, consulta do histórico e métricas implementadas em C++.

A conversão entre objetos Python e estruturas C++ deve respeitar os tipos e as dimensões definidos pelo ambiente: 28 posições no tabuleiro e 9 posições no banco.

### 9.3. Limite da integração

Disponibilizar a classe por meio do `pybind11` não substitui automaticamente `ai/AntiLoopManager.py`.

O gerenciador Python atual recebe listas e dicionários, enquanto a API nativa utiliza estruturas tipadas. A adoção da implementação C++ no fluxo real da IA exige um adaptador ou uma migração explícita dos consumidores, preservando os aliases de movimentos, as regras de bloqueio e as métricas.

Até essa integração ser concluída, a classe nativa pode ser importada e utilizada diretamente, mas não se deve afirmar que o ambiente Python já utiliza automaticamente o motor C++.

### 9.4. Validação da exposição

O teste CMake `decision_engine_import` verifica se o módulo pode ser importado e se as classes `DecisionEngine` e `AntiLoopEngine` estão disponíveis.

A aprovação desse teste confirma a exposição básica das classes, mas não comprova equivalência comportamental com o gerenciador Python. Os testes unitários C++ e Python e a comparação de cenários permanecem nas tasks correspondentes.


## 10. Critérios de conclusão

A migração só deverá ser marcada como concluída depois de:

* Compilar a implementação nativa.
* Criar e executar os testes unitários C++.
* Executar os testes Python correspondentes ao `AntiLoopManager`.
* Comparar resultados Python e C++ para os mesmos cenários.
* Verificar a ordem dos motivos de bloqueio.
* Confirmar que consultas não atualizam indevidamente o histórico.
* Confirmar que registros legítimos ocorrem no momento correto.
* Confirmar ausência de regressões nos consumidores das estruturas C++.

**Status:** implementação proposta para revisão. Equivalência comportamental ainda não validada.
