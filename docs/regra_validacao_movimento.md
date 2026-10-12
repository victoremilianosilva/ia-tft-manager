# Regras de Validação de Movimentos — Tabuleiro e Banco

## 1. Estrutura e conceitos

O ambiente utiliza um tabuleiro de 28 posições (4 × 7) e um banco, também chamado de reserva, com até 9 posições.

Existem dois tipos principais de movimentação:

- **Banco → Tabuleiro (`bench_to_board`):** transfere uma unidade da reserva para uma posição vazia do tabuleiro.
- **Tabuleiro → Tabuleiro (`board_move` ou `board_swap`):** move uma unidade para uma posição vazia ou troca duas unidades de posição.

A validação ocorre em duas etapas:

1. **Geração das máscaras:** `ActionMaskManager` determina quais movimentos podem ser selecionados pela política.
2. **Execução:** `MiniTFTEnv` valida novamente a ação recebida, consulta o anti-loop e realiza a alteração de estado.

Uma ação habilitada na máscara não tem garantia absoluta de execução bem-sucedida. O estado pode ter mudado, a ação pode conter índices inválidos ou uma validação posterior pode rejeitá-la.

---

## 2. Regras para movimentos do banco ao tabuleiro

### 2.1. Validação do candidato

O método `_is_valid_bench_board_move(bench_slot, target, bench=None)` considera um candidato válido quando todas estas condições são atendidas:

1. O índice de origem existe dentro do tamanho atual da lista do banco.
2. A posição de origem contém uma unidade.
3. A posição de destino é válida segundo `BoardManager.is_valid_position()`, com fallback para os limites configurados quando ocorre uma exceção.
4. O `AntiLoopManager` não bloqueia o movimento com o tipo `bench_to_board`.

O método não verifica diretamente se o destino está vazio. Essa condição é garantida pelo gerador de candidatos, que percorre as posições retornadas por `BoardManager.get_empty_positions()`.

### 2.2. Disponibilidade de espaço

O banco só pode enviar unidades ao tabuleiro quando há pelo menos uma posição vazia.

O método `_has_free_board_slot()` consulta `get_empty_positions()`. Se essa consulta gerar uma exceção, verifica diretamente se existe algum elemento `None` na representação do tabuleiro.

Se não houver espaço, o sistema não gera movimentos reais do banco para o tabuleiro.

### 2.3. Geração das máscaras

O método `get_bench_move_masks()` retorna:

- `source_mask`: vetor de 9 posições.
- `target_masks`: matriz de 9 × 28.
- `has_valid_move`: indicador booleano de existência de pelo menos um movimento real.

Para cada posição da reserva:

1. Se estiver vazia, não é uma origem válida.
2. Se estiver ocupada, são examinadas as posições vazias do tabuleiro.
3. Cada destino é submetido a `_is_valid_bench_board_move()`.
4. Se houver pelo menos um destino válido, a origem é habilitada e os destinos válidos são marcados.
5. Se não houver destinos válidos, a linha de destinos recebe o índice zero como fallback técnico.

Se nenhum movimento real for encontrado, `source_mask[0]` também recebe um fallback técnico. Nesse caso, `has_valid_move` continua sendo `False`.

Portanto, um bit habilitado no índice zero não comprova que exista uma unidade válida para movimentar.

### 2.4. Máscaras auxiliares

`get_bench_move_source_mask()` habilita uma origem somente quando a unidade possui pelo menos um destino vazio válido.

`get_bench_to_board_target_mask(bench_slot)` gera os destinos de uma origem específica. Se o índice for inválido, a origem estiver vazia ou não houver espaço no tabuleiro, retorna uma máscara com o índice zero habilitado como fallback.

`get_board_target_mask()` reúne os destinos válidos de todas as unidades da reserva. Não substitui a máscara condicionada à origem selecionada pela política.

### 2.5. Validação durante a execução

O método `_execute_move_bench()` aplica as seguintes verificações, nesta ordem:

1. A origem está dentro dos limites do banco.
2. O destino é uma posição válida no tabuleiro.
3. Existe uma unidade na origem.
4. O sistema registra uma tentativa de execução.
5. O `AntiLoopManager` consulta o motivo de bloqueio para `bench_to_board`.
6. Se houver bloqueio, registra o motivo, atualiza as métricas e retorna uma penalidade de `-0.10`.
7. O destino está vazio.
8. A unidade é removida do banco.
9. A unidade é adicionada ao tabuleiro.
10. Se a inserção falhar, o código tenta devolver a unidade à posição original do banco.
11. Após o sucesso, o movimento é registrado no histórico e nas métricas.

A recompensa da ação é calculada depois da movimentação bem-sucedida.

---

## 3. Regras para movimentos dentro do tabuleiro

### 3.1. Validação do candidato

O método `_is_valid_board_move(source, target, board=None)` aplica estas regras:

1. A origem deve estar dentro dos limites do tabuleiro.
2. O destino deve estar dentro dos limites do tabuleiro.
3. Origem e destino não podem ser iguais.
4. A origem precisa conter uma unidade.
5. Se o destino estiver ocupado, o candidato será tratado como `board_swap`.
6. Se o destino estiver vazio, o candidato será tratado como `board_move`.
7. O `AntiLoopManager` não pode bloquear o movimento.

Se todas as verificações forem atendidas, o candidato é considerado válido pela camada de geração das máscaras.

### 3.2. Movimento para uma posição vazia

Quando o destino está vazio:

- O tipo utilizado na validação anti-loop é `board_move`.
- A unidade da origem é a unidade associada ao candidato.
- O movimento é rejeitado nessa camada se o anti-loop indicar bloqueio.

A máscara não exige que a unidade tenha um papel específico, que melhore a composição ou que aumente o poder do tabuleiro. Essas regras estratégicas não fazem parte da validação básica desse método.

### 3.3. Troca de posições ocupadas

Quando o destino contém outra unidade:

- O tipo utilizado na validação anti-loop é `board_swap`.
- A unidade enviada ao anti-loop é a unidade que está na origem.
- Se o anti-loop não bloquear o candidato, a troca é considerada válida.

O validador não exige que o destino esteja vazio e não avalia a qualidade estratégica da troca.

### 3.4. Geração das máscaras de movimento

O método `get_board_move_masks()` retorna:

- `source_mask`: vetor de 28 posições.
- `target_masks`: matriz de 28 × 28.
- `has_valid_move`: indicador booleano de existência de pelo menos um movimento real.

Para cada posição de origem:

1. Se a posição não existir na lista do tabuleiro ou estiver vazia, não é considerada uma origem real.
2. A origem é comparada com todos os destinos.
3. A própria posição é ignorada.
4. Cada par origem/destino é validado por `_is_valid_board_move()`.
5. Os destinos válidos são marcados na linha correspondente da matriz.
6. Uma origem com pelo menos um destino válido é habilitada.
7. Se uma linha não possuir destinos válidos, seu índice zero recebe um fallback técnico.

Se não existir nenhum movimento real, `source_mask[0]` recebe um fallback, mas `has_valid_move` permanece `False`.

Esse indicador separado impede que o fallback técnico seja interpretado como evidência de que `MOVE_BOARD` está disponível.

### 3.5. Máscaras auxiliares

`get_board_source_mask()` habilita origens ocupadas que possuem pelo menos um destino válido.

`get_conditioned_board_target_mask()` reúne os destinos válidos de todas as origens ocupadas. É uma máscara geral auxiliar; a política deve utilizar a máscara condicionada à origem selecionada.

`get_board_move_target_mask(source)` calcula os destinos válidos de uma origem específica. Se a origem for inválida, estiver vazia ou não possuir destinos válidos, retorna uma máscara com o índice zero habilitado como fallback.

---

## 4. Validação de movimentos do tabuleiro durante a execução

O método `_execute_move_board()` recebe a origem de `board_source` e o destino de `conditioned_board_target`.

A validação ocorre nesta ordem:

1. A origem é uma posição válida do tabuleiro.
2. O destino é uma posição válida do tabuleiro.
3. Origem e destino são diferentes.
4. Existe uma unidade na origem.
5. O destino é consultado para determinar se está ocupado.
6. O tipo de movimento é determinado:
   - Destino vazio: `board_move`.
   - Destino ocupado: `board_swap`.
7. A tentativa de execução é registrada.
8. O `AntiLoopManager` consulta se deve bloquear o movimento.
9. Se houver bloqueio, o motivo é registrado, as métricas são atualizadas e a ação retorna uma penalidade de `-0.10`.
10. Se o destino estiver vazio, é chamado `BoardManager.move_unit(source, target)`.
11. Se estiver ocupado, é chamado `BoardManager.swap_units(source, target)`.
12. Se a operação falhar, a ação retorna uma penalidade de `-0.10`.
13. Se for bem-sucedida, o movimento é registrado no histórico e nas métricas.

O histórico registra a unidade que estava na origem antes da operação. Isso é relevante para a detecção posterior de reversões e ciclos.

---

## 5. Regras anti-loop aplicadas à validação

O `AntiLoopManager` utiliza o histórico para bloquear movimentos que correspondam a determinadas regras.

A ordem de avaliação é:

1. Bloqueio explícito (`explicit`).
2. Movimento reverso (`reverse`).
3. Oscilação (`oscillation`).
4. Ciclo entre banco e tabuleiro (`bench_board_loop`), para os tipos aplicáveis.
5. Ciclo geral (`cycle`).
6. Nenhum bloqueio, quando todas as regras anteriores falham.

O primeiro motivo encontrado é retornado.

### 5.1. Bloqueio explícito

O movimento é comparado com os bloqueios armazenados. O bloqueio depende da chave do movimento e da assinatura de estado associada.

### 5.2. Movimento reverso

Para movimentos normais, exige o mesmo tipo e identidade de unidade, com origem e destino invertidos em relação ao último movimento.

Para `board_swap`, considera a mesma dupla de posições, independentemente da ordem entre origem e destino.

### 5.3. Oscilação

Examina os seis movimentos mais recentes. A lógica varia conforme o tipo:

- `board_move`: acompanha movimentos da mesma unidade.
- `board_swap`: considera movimentos de troca e de movimento da unidade, reconstruindo uma sequência de posições.

A regra verifica se o candidato fecha uma sequência repetitiva segundo o histórico disponível.

### 5.4. Ciclo entre banco e tabuleiro

Considera movimentos `bench_to_board` e `board_to_bench`, incluindo os aliases reconhecidos pelo gerenciador.

Exige pelo menos dois movimentos relevantes da mesma unidade, formando uma ida e uma volta entre as mesmas posições. A repetição da transição anterior pode ser bloqueada.

A execução descrita neste documento utiliza diretamente `bench_to_board` para a entrada da reserva no tabuleiro. Não se deve presumir que a movimentação inversa esteja disponível ou seja executada pelo mesmo método sem verificar os demais caminhos do ambiente.

### 5.5. Ciclo geral

Considera `board_move` e `board_swap` da mesma identidade de unidade, usando até os oito movimentos relevantes mais recentes.

A regra verifica a continuidade da sequência e se um ciclo já havia sido completado. O primeiro fechamento é permitido; uma repetição que satisfaça as condições do histórico é bloqueada.

### 5.6. Falha na consulta anti-loop durante a geração das máscaras

`ActionMaskManager._should_block_anti_loop()` captura exceções durante a consulta e permite o candidato nessa camada, registrando a falha.

Isso não garante que a execução seja aceita: o ambiente ainda realiza validações próprias.

Durante a execução, as chamadas ao anti-loop seguem o tratamento específico de cada método e não devem ser consideradas equivalentes ao fallback permissivo da geração das máscaras.

---

## 6. Diferenças importantes entre geração e execução

| Regra | Geração de máscaras | Execução |
|---|---|---|
| Origem ocupada | Verificada | Verificada novamente |
| Índices válidos | Verificados | Verificados novamente |
| Origem diferente do destino | Verificada | Verificada novamente |
| Destino vazio para `bench_to_board` | Garantido pela lista de destinos vazios | Verificado explicitamente |
| Destino vazio para `board_move` | Determina o tipo do candidato | Determina a operação a executar |
| Destino ocupado para `board_swap` | Troca permitida se não houver bloqueio | Troca executada por `swap_units()` |
| Anti-loop | Consultado para cada candidato | Consultado novamente |
| Registro de tentativa | Não deve ocorrer na consulta normal | Ocorre durante a execução |
| Registro de movimento | Não deve ocorrer na consulta normal | Ocorre após sucesso |
| Fallback de máscara | Pode habilitar índice zero | Não torna a ação válida |

---

## 7. Resumo das regras efetivas

Um movimento do banco para o tabuleiro é candidato válido quando há uma unidade na origem, a posição de destino é válida e o anti-loop não o bloqueia. O gerador de máscaras limita esses destinos às posições vazias.

Um movimento dentro do tabuleiro é candidato válido quando os índices são válidos, a origem contém uma unidade, origem e destino são diferentes e o anti-loop não bloqueia o movimento. Destino vazio representa movimentação; destino ocupado representa troca.

Na execução, o ambiente repete as validações fundamentais, consulta novamente o anti-loop e só registra o movimento como bem-sucedido depois que a operação de movimentação ou troca termina com sucesso.

As máscaras condicionais podem conter índices de fallback sem que exista um movimento real válido. Por isso, a disponibilidade efetiva das ações depende dos indicadores de validade calculados separadamente, e não apenas dos bits habilitados nas máscaras.

**Limite desta documentação:** ela descreve as regras encontradas nos métodos analisados de `ActionMaskManager`, `MiniTFTEnv` e `AntiLoopManager`. Regras adicionais internas a `BoardManager.move_unit()`, `BoardManager.swap_units()` ou outras camadas devem ser consultadas separadamente caso sejam necessárias para definir o contrato completo de equivalência.