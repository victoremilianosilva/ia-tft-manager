# Análise de Efeitos Colaterais e Atualizações de Histórico — Migração AntiLoop para C++

## 1. Objetivo

A migração de `ActionMaskManager` e `AntiLoopManager` para C++ precisa preservar não apenas as máscaras retornadas, mas também os efeitos colaterais que ocorrem durante a execução das ações.

O comportamento depende de três categorias distintas:

1. **Consultas:** verificam se uma ação seria permitida, sem registrar sua execução.
2. **Atualizações de estado:** registram estados e movimentos para que decisões futuras considerem o histórico.
3. **Telemetria:** contabiliza tentativas, bloqueios e movimentos concluídos.

Misturar essas categorias pode alterar o comportamento do agente mesmo que as máscaras de uma única consulta sejam idênticas.

## 2. Estado histórico mantido pelo AntiLoopManager

O `AntiLoopManager` mantém os seguintes dados:

| Campo | Função | Limite ou comportamento |
|---|---|---|
| `position_history` | Assinaturas anteriores do tabuleiro e banco | `history_size`, padrão 20 |
| `move_history` | Movimentos registrados | `history_size`, padrão 20 |
| `blocked_moves` | Chaves de movimentos explicitamente bloqueados | `blocked_move_size`, padrão 10 |
| `state_visits` | Contagem de visitas por assinatura | Dicionário acumulado até o reset |
| `last_board_signature` | Última assinatura registrada | Atualizada por `register_state()` |
| `blocked_move_states` | Assinatura associada a cada bloqueio explícito | Precisa permanecer sincronizada com os bloqueios |
| `last_move` | Último movimento registrado | Atualizado por `register_move()` |
| `execution_metrics` | Contadores de tentativas, bloqueios e sucessos | Persistem após `reset()` |

Os limites dos históricos são parte do comportamento. Alterá-los pode mudar quais movimentos são reconhecidos como reversões, oscilações ou ciclos.

## 3. Consultas que devem ser livres de efeitos colaterais

### 3.1. Consultas AntiLoop

`should_block_move()` e `get_block_reason()` são usadas durante a geração das máscaras e devem consultar o histórico sem modificá-lo.

`get_block_reason()` avalia as proteções na seguinte ordem:

1. Bloqueio explícito.
2. Reversão.
3. Oscilação.
4. Ciclo entre banco e tabuleiro, quando aplicável.
5. Ciclo geral.
6. Nenhum bloqueio.

A primeira regra correspondente determina o motivo retornado.

A quantidade de vezes que uma consulta é feita não deve alterar o histórico, a contagem de visitas ou as métricas de execução.

### 3.2. Efeito na geração das máscaras

`ActionMaskManager._is_valid_board_move()` e `_is_valid_bench_board_move()` consultam o AntiLoop para decidir se um candidato entra na máscara.

Se uma consulta AntiLoop falhar durante a geração das máscaras, `_should_block_anti_loop()` registra a falha e permite o candidato nessa camada. As validações básicas de legalidade continuam sendo verificadas.

Esse comportamento de tolerância a falhas faz parte do fluxo atual. A migração não deve converter silenciosamente uma falha de diagnóstico em bloqueio, nem deixar de registrar as falhas.

**Importante:** gerar centenas de candidatos para montar as máscaras não equivale a executar centenas de movimentos. Essas consultas não devem incrementar `execution_attempts`, `execution_blocks` nem os contadores de movimentos concluídos.

## 4. Atualizações de histórico

### 4.1. `register_state()`

Ao registrar um estado, o sistema:

1. Constrói a assinatura do tabuleiro e do banco.
2. Adiciona a assinatura a `position_history`.
3. Incrementa `state_visits` para aquela assinatura.
4. Calcula `repeated` comparando a contagem com `loop_threshold`.
5. Atualiza `last_board_signature`.
6. Retorna a assinatura, o indicador de repetição e a quantidade de visitas.

Com `loop_threshold=2`, a segunda visita já é considerada repetição.

A assinatura considera a disposição das unidades, não o ouro, o XP ou todos os demais atributos do jogador. Por isso, estados com recursos diferentes podem contar como a mesma configuração espacial.

A frequência e os pontos exatos em que `register_state()` é chamado precisam ser preservados. Registrar estados adicionais ou deixar de registrar estados existentes pode alterar a contagem de visitas e o contexto dos bloqueios explícitos.

### 4.2. `register_move()`

Depois de um movimento concluído, `register_move()`:

1. Monta o registro com tipo, origem, destino e identidade da unidade.
2. Adiciona o registro a `move_history`.
3. Atualiza `last_move`.
4. Retorna o movimento registrado.

O momento da atualização é essencial. Registrar um movimento antes da execução bem-sucedida faria o AntiLoop acreditar que uma ação ocorreu quando, na realidade, o estado não foi alterado.

### 4.3. `block_move()`

O bloqueio explícito:

1. Constrói a chave do movimento.
2. Remove uma ocorrência anterior da mesma chave, se existir.
3. Quando o histórico atinge o limite, remove a entrada mais antiga e sua associação de estado.
4. Adiciona a chave ao histórico de bloqueios.
5. Associa a chave à assinatura atual em `blocked_move_states`.

`is_move_blocked()` só considera o bloqueio válido quando a assinatura associada coincide com `last_board_signature`.

Por isso, a chave e sua assinatura associada precisam ser atualizadas e removidas em conjunto. Um bloqueio sem a assinatura correta pode persistir indevidamente ou deixar de ser reconhecido.

A geração das máscaras não deve criar bloqueios explícitos automaticamente, a menos que isso seja feito deliberadamente para reproduzir outro comportamento já existente.

## 5. Ordem dos efeitos colaterais durante a execução

### 5.1. Movimento do banco para o tabuleiro

Em `_execute_move_bench()`, o fluxo observado é:

1. Validar os índices e obter a unidade de origem.
2. Incrementar `execution_attempts`.
3. Consultar o motivo de bloqueio AntiLoop.
4. Se houver bloqueio, incrementar as métricas de bloqueio, preencher `info["anti_loop_blocked"]` e retornar a penalidade.
5. Verificar se o destino está vazio.
6. Remover a unidade do banco.
7. Tentar adicioná-la ao tabuleiro.
8. Se a inserção falhar, tentar devolver a unidade ao slot original do banco.
9. Após o movimento bem-sucedido, registrar o movimento no histórico.
10. Incrementar o contador de movimentos bem-sucedidos.
11. Preencher as informações de sucesso e calcular a recompensa.

As falhas de validação anteriores à contagem de tentativa não incrementam `execution_attempts`. Falhas posteriores à tentativa, mas que não sejam bloqueios AntiLoop, também não devem ser contabilizadas automaticamente como bloqueios AntiLoop.

### 5.2. Movimento ou troca no tabuleiro

Em `_execute_move_board()`, o fluxo observado é:

1. Validar origem, destino e existência da unidade de origem.
2. Determinar `board_move` ou `board_swap` com base na ocupação do destino.
3. Incrementar `execution_attempts`.
4. Consultar `should_block_move()`.
5. Se houver bloqueio, obter o motivo, registrar as métricas, preencher `info["anti_loop_blocked"]` e retornar a penalidade.
6. Executar `BoardManager.move_unit()` ou `BoardManager.swap_units()`.
7. Se a operação falhar, retornar a penalidade sem registrar um movimento bem-sucedido.
8. Após o sucesso, registrar o movimento e contabilizar o sucesso.
9. Atualizar as informações de resultado e calcular a recompensa.

O motivo de bloqueio deve permanecer associado à ação que foi realmente rejeitada. Na implementação atual, o ramo de tabuleiro consulta `should_block_move()` e, em caso positivo, consulta novamente `get_block_reason()` para obter o motivo.

Uma implementação equivalente deve preservar a semântica desse processo, evitando duplicar contadores ou introduzir mutações em consultas adicionais.

## 6. Métricas que não podem ser confundidas

O `AntiLoopManager` mantém estes contadores:

- `execution_attempts`
- `execution_blocks`
- `blocked_reverse`
- `blocked_oscillation`
- `blocked_explicit`
- `blocked_bench_board_loop`
- `board_moves_executed`
- `bench_to_board_executed`
- `blocked_cycle`

`record_execution_block(reason)` incrementa `execution_blocks` e, quando existe a chave correspondente, incrementa também `blocked_<reason>`.

`record_successful_move(move_type)` incrementa:

- `board_moves_executed` para `board_move` e `board_swap`.
- `bench_to_board_executed` para `bench_to_board`.

Os contadores não são um substituto do histórico de movimentos. O histórico determina o comportamento AntiLoop; as métricas descrevem o que ocorreu.

Também é importante manter a diferença entre os nomes dos motivos e os nomes dos contadores. Por exemplo, o motivo `"cycle"` corresponde à métrica `blocked_cycle`, enquanto `"reverse"` corresponde a `blocked_reverse`.

## 7. Reset: o que é apagado e o que persiste

`AntiLoopManager.reset()` recria ou limpa:

- `position_history`
- `move_history`
- `blocked_moves`
- `state_visits`
- `last_board_signature`
- `blocked_move_states`
- `last_move`

Entretanto, **`execution_metrics` não é apagado pelo reset**. Os comentários da implementação indicam que as métricas acumulam durante a vida do ambiente.

Em `MiniTFTEnv.reset()`, o ambiente reseta seus gerenciadores, incluindo o `AntiLoopManager`, antes de criar a unidade inicial, atualizar a loja e reconstruir o estado do jogador.

Uma migração precisa preservar essa distinção: o histórico de decisão é reiniciado, mas os contadores de execução permanecem acumulados, a menos que exista uma operação explícita separada para zerá-los.

## 8. Efeitos colaterais fora do AntiLoop

A execução das ações também pode modificar:

- Ocupação do tabuleiro e do banco.
- Estado do jogador e da economia.
- Recompensa da ação.
- Dicionário `info` devolvido pelo ambiente.
- Métricas de diagnóstico.
- Estado usado na observação seguinte.

A geração de máscaras não deve executar essas alterações. O C++ pode calcular a validade de uma ação, mas o ambiente Python continua responsável pela execução real e pelos efeitos que a acompanham.

Se o C++ mantiver um histórico próprio, a integração precisa definir como esse histórico será sincronizado quando uma operação de tabuleiro falhar, quando houver rollback ou quando o ambiente for reiniciado.

## 9. Contrato recomendado de sincronização

Uma implementação equivalente deve obedecer aos seguintes princípios:

1. **Consulta não mutável:** avaliar um candidato não registra um movimento nem altera contadores.
2. **Registro após sucesso:** movimentos entram no histórico somente depois de concluídos.
3. **Bloqueio contabilizado uma vez:** uma ação bloqueada durante a execução incrementa os contadores apropriados uma única vez.
4. **Falha não é sucesso:** operações inválidas ou com rollback não geram registros de movimento bem-sucedido.
5. **Históricos sincronizados:** a ordem, os limites e as identidades dos registros são preservados.
6. **Bloqueio associado ao estado:** chave e assinatura do bloqueio permanecem consistentes.
7. **Reset seletivo:** os históricos são limpos, mas as métricas acumuladas permanecem.
8. **Fallbacks preservados:** uma falha durante a consulta AntiLoop durante a geração de máscaras continua seguindo a política atual de tolerância.
9. **Execução permanece no ambiente:** C++ calcula validade e bloqueios, enquanto Python executa as operações e produz recompensas e informações da transição.
10. **Comparação observável:** as métricas e os motivos de bloqueio devem poder ser comparados entre Python e C++ durante a validação.

## 10. Conclusão

Os principais riscos da migração não estão apenas na diferença entre duas máscaras. Estão nos efeitos colaterais e na ordem em que o histórico é atualizado.

O C++ deve reproduzir as consultas sem mutação, os registros de estado, os registros de movimentos concluídos, os bloqueios explícitos e a telemetria de execução. Também precisa preservar a ordem das validações, os rollbacks e a semântica do reset.

O critério de equivalência é que, diante da mesma sequência de estados e ações, Python e C++ produzam as mesmas máscaras, os mesmos motivos de bloqueio e o mesmo histórico relevante para as decisões futuras.