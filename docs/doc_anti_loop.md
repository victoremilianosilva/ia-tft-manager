# Análise das Proteções Anti-Loop e Bloqueios de Movimento

## 1. Objetivo

O `AntiLoopManager` impede que a IA repita movimentos de posicionamento sem progresso, alternando unidades entre posições ou repetindo configurações anteriores.

O gerenciador não escolhe a estratégia, não executa movimentos e não cria as máscaras de ações. Ele mantém históricos, avalia candidatos e informa se um movimento deve ser bloqueado.

## 2. Configuração e estado interno

A configuração padrão é:

| Parâmetro | Valor | Função |
|---|---:|---|
| `history_size` | 20 | Limite de estados e movimentos mantidos nos históricos |
| `blocked_move_size` | 10 | Quantidade máxima de bloqueios explícitos armazenados |
| `loop_threshold` | 2 | Número de visitas a partir do qual um estado é considerado repetido |

O gerenciador mantém:

- `position_history`: histórico limitado de assinaturas do posicionamento.
- `move_history`: histórico limitado de movimentos executados e registrados.
- `blocked_moves`: fila limitada de bloqueios explícitos.
- `state_visits`: contador de visitas por assinatura de estado.
- `last_board_signature`: última assinatura registrada.
- `blocked_move_states`: associação entre cada bloqueio explícito e o estado em que foi criado.
- `last_move`: último movimento registrado.
- `execution_metrics`: contadores acumulados de tentativas, bloqueios e movimentos bem-sucedidos.

As métricas de execução são inicializadas no construtor e não são apagadas pelo método `reset()`. O reset limpa os históricos e estados internos, mas preserva os contadores acumulados.

## 3. Identidade das unidades

O método `_unit_identity(unit)` determina como uma unidade é reconhecida no histórico.

A regra é:

1. Se a unidade não for um dicionário, retorna `None`.
2. Se houver `uuid`, utiliza a identidade `("uuid", uuid)`.
3. Caso contrário, utiliza `("unit", id, star)`, considerando estrela 1 como padrão.

Isso permite acompanhar uma unidade ao longo dos movimentos, desde que sua identidade seja consistente.

**Limitação importante:** unidades sem UUID que tenham o mesmo `id` e a mesma estrela são consideradas equivalentes pelo anti-loop. A identidade alternativa não distingue duas cópias da mesma unidade.

## 4. Assinaturas e repetição de estados

### 4.1. `make_board_signature()`

Cria uma assinatura ordenada do tabuleiro e do banco. Para cada posição, registra:

- O índice da posição.
- `None`, se estiver vazia.
- A identidade da unidade, se estiver ocupada.

A assinatura considera somente a disposição das unidades no tabuleiro e no banco. Não inclui ouro, XP, loja, vida ou outros atributos do jogador.

Consequentemente, duas configurações com a mesma disposição das unidades são consideradas o mesmo estado de posicionamento, mesmo que outros dados do jogo tenham mudado.

### 4.2. `register_state()`

Ao registrar um estado:

1. Calcula a assinatura atual.
2. Acrescenta a assinatura a `position_history`.
3. Incrementa o contador correspondente em `state_visits`.
4. Define `repeated=True` quando o total de visitas é maior ou igual a `loop_threshold`.
5. Atualiza `last_board_signature`.

Com o valor padrão de `loop_threshold=2`, a segunda visita já classifica o estado como repetido.

**Atenção:** `register_state()` identifica e contabiliza estados repetidos, mas não bloqueia diretamente um movimento. A assinatura também é usada pelos bloqueios explícitos. Não se deve presumir que qualquer estado repetido gere automaticamente uma proibição de movimento.

Os métodos `was_state_seen()` e `get_state_visits()` permitem consultar se um estado já foi registrado e quantas vezes apareceu.

## 5. Registro de movimentos

O método `register_move()` registra uma tupla com:

- Tipo do movimento.
- Origem.
- Destino.
- Identidade da unidade.

O movimento é adicionado a `move_history` e passa a ser `last_move`.

As regras que dependem do histórico utilizam esses registros. Portanto, o momento em que um movimento é registrado influencia quais candidatos poderão ser bloqueados posteriormente.

O `AntiLoopManager` não executa a movimentação. A camada responsável pela execução deve chamar `register_move()` após o movimento ter sido concluído com sucesso.

## 6. Bloqueio explícito

### 6.1. `block_move()`

Permite registrar manualmente um movimento que não deve ser repetido no estado atual.

A chave do bloqueio é composta por:

`(move_type, source, target, unit_identity)`

O gerenciador também armazena a assinatura atual do posicionamento em `blocked_move_states`.

Se a chave já estiver na fila, ela é removida e adicionada novamente. Quando a fila atinge o limite, o bloqueio mais antigo pode ser removido para dar espaço ao novo.

### 6.2. `is_move_blocked()`

O bloqueio só é considerado ativo quando:

1. A chave exata do candidato existe em `blocked_moves`.
2. A assinatura associada ao bloqueio é igual a `last_board_signature`.

Assim, um bloqueio explícito está vinculado ao último estado de posicionamento registrado.

**Limitação:** a comparação depende da atualização correta de `last_board_signature`. Se o estado do tabuleiro mudar sem que um novo estado seja registrado, a assinatura mantida pelo gerenciador pode não representar a disposição atual.

O método `clear_old_blocks()` também existe, mas a fila já possui `maxlen`; os elementos mais antigos são descartados automaticamente quando o limite é ultrapassado.

## 7. Proteção contra movimentos reversos

### 7.1. `is_reverse_move()`

Impede a repetição imediata de um movimento no sentido contrário.

Para movimentos normais, exige:

- A mesma identidade de unidade.
- O mesmo tipo de movimento.
- Origem atual igual ao destino anterior.
- Destino atual igual à origem anterior.

Exemplo conceitual:

- Movimento registrado: unidade A de 3 para 10.
- Candidato: unidade A de 10 para 3.
- Resultado: bloqueio por `reverse`, desde que as condições sejam atendidas.

A regra consulta `last_move`, não todo o histórico.

### 7.2. Exceção para trocas

Quando o movimento atual e o anterior são ambos `board_swap`, a comparação considera apenas o par de posições, independentemente da ordem entre origem e destino e sem exigir a mesma identidade de unidade.

Exemplo:

- Troca entre as posições 3 e 10.
- Candidato de troca entre as posições 10 e 3.
- Resultado: reconhece a mesma troca como reversão.

Essa exceção existe porque, depois da primeira troca, as unidades já mudaram de lugar.

## 8. Proteção contra oscilações

### 8.1. `is_oscillating()`

Examina até os seis movimentos mais recentes de `move_history`.

Se a unidade não tiver uma identidade válida ou não houver movimentos registrados, retorna `False`.

A seleção dos movimentos relevantes depende do tipo do candidato:

- Para `board_move`, considera movimentos `board_move` da mesma unidade.
- Para `board_swap`, considera `board_swap` e `board_move` associados à mesma unidade.

Em seguida, reconstrói uma cadeia de posições a partir dos movimentos cronologicamente mais recentes. Para que a cadeia seja utilizada, o último movimento relevante precisa terminar na origem atual do candidato.

A regra retorna `True` quando o destino candidato já aparece pelo menos duas vezes na cadeia reconstruída, desconsiderando a posição final da cadeia.

### 8.2. Efeito prático

A regra tenta permitir o primeiro fechamento de um ciclo de posicionamento, bloqueando repetições posteriores que satisfaçam o critério de visitas ao destino.

Ela é diferente da reversão imediata: a reversão compara apenas o último movimento, enquanto a oscilação examina uma sequência recente.

**Limitação:** o comportamento depende da continuidade dos registros e da identidade da unidade. Movimentos ausentes no histórico, identidades inconsistentes ou mudanças na sequência podem impedir a detecção.

## 9. Proteção contra ciclos entre banco e tabuleiro

### 9.1. `is_bench_board_loop()`

Reconhece estes tipos de movimento:

- `bench_to_board`
- `board_to_bench`
- `MOVE_BENCH_TO_BOARD`
- `MOVE_BOARD_TO_BENCH`

Os nomes são normalizados para as formas `bench_to_board` e `board_to_bench`.

A regra exige uma identidade válida da unidade e pelo menos dois movimentos relevantes dessa mesma unidade.

Os dois últimos movimentos relevantes precisam:

1. Ter tipos diferentes, um de ida e outro de volta.
2. Representar transições entre as mesmas posições, em sentidos opostos.

Depois de identificar a ida e a volta, a regra bloqueia a repetição da transição anterior quando o candidato possui o mesmo tipo, origem e destino do movimento que iniciou essa ida e volta.

### 9.2. Exemplo conceitual

1. A unidade passa da reserva para o tabuleiro.
2. A unidade volta do tabuleiro para a reserva.
3. A tentativa de repetir a transição inicial pode ser bloqueada.

O objetivo é impedir que a mesma unidade continue alternando entre a reserva e o tabuleiro.

**Limitação:** essa regra depende de os tipos, índices e identidades terem sido registrados de maneira compatível. A presença dos aliases no gerenciador não garante que todos esses tipos sejam produzidos pelas demais camadas do ambiente.

## 10. Proteção contra ciclos gerais

### 10.1. `is_cycle_move()`

A regra é aplicada apenas aos tipos `board_move` e `board_swap`.

Ela:

1. Obtém a identidade da unidade candidata.
2. Filtra o histórico para movimentos de tabuleiro associados a essa identidade.
3. Considera até os oito movimentos relevantes mais recentes.
4. Procura uma sequência iniciada numa posição compatível com o destino candidato.
5. Exige continuidade entre o destino de um movimento e a origem do seguinte.
6. Verifica se o histórico já retornou ao destino candidato.
7. Só bloqueia se o ciclo tiver sido completado anteriormente e a sequência terminar na origem atual do candidato.

O primeiro fechamento de um ciclo é permitido; uma repetição posterior pode ser bloqueada.

### 10.2. Diferença em relação à oscilação

- **Oscilação:** reconstrói uma cadeia recente e verifica se o destino já foi visitado pelo menos duas vezes na cadeia.
- **Ciclo geral:** procura uma sequência contínua de movimentos da unidade e verifica se o ciclo já foi fechado no histórico.

As duas regras podem analisar sequências parecidas, mas usam critérios diferentes.

## 11. Ordem efetiva de bloqueio

O método `get_block_reason()` consulta as regras na seguinte ordem:

1. `explicit`
2. `reverse`
3. `oscillation`
4. `bench_board_loop`, para tipos de movimento banco ↔ tabuleiro reconhecidos
5. `cycle`
6. `None`, se nenhuma regra bloquear o candidato

A primeira regra satisfeita determina o motivo retornado. Por exemplo, se um candidato for simultaneamente uma reversão e uma oscilação, o motivo retornado será `reverse`.

O método `should_block_move()` transforma esse resultado em booleano:

- `True`: existe algum motivo de bloqueio.
- `False`: nenhuma das regras consultadas bloqueou o candidato.

As consultas de bloqueio são projetadas para não alterar históricos nem incrementar métricas durante a geração das máscaras.

## 12. Avaliação de risco

O método `evaluate_move_risk()` fornece uma pontuação de risco entre `0.0` e `1.0`.

| Condição detectada | Incremento de risco |
|---|---:|
| Bloqueio explícito | Retorna imediatamente `1.0` |
| Movimento reverso | `+0.7` |
| Oscilação | `+0.8` |
| Ciclo banco ↔ tabuleiro | `+0.9` |

A soma é limitada a `1.0`.

Essa avaliação não inclui diretamente `is_cycle_move()` como incremento independente. Portanto, não equivale a `get_block_reason()` e não deve ser tratada como uma cópia da decisão final de bloqueio.

O método de risco também não executa o movimento nem altera o histórico.

## 13. Métricas de execução

O gerenciador expõe contadores para acompanhar o comportamento das proteções:

- `execution_attempts`: tentativas reais de movimentação registradas.
- `execution_blocks`: bloqueios ocorridos durante a execução.
- `blocked_reverse`: bloqueios classificados como reversão.
- `blocked_oscillation`: bloqueios classificados como oscilação.
- `blocked_explicit`: bloqueios explícitos.
- `blocked_bench_board_loop`: bloqueios banco ↔ tabuleiro.
- `blocked_cycle`: bloqueios de ciclo geral.
- `board_moves_executed`: movimentos e trocas de tabuleiro bem-sucedidos.
- `bench_to_board_executed`: entradas da reserva no tabuleiro bem-sucedidas.

`record_execution_block(reason)` incrementa `execution_blocks` e o contador correspondente somente se a chave `blocked_<reason>` existir nas métricas.

`record_successful_move()` incrementa os contadores de sucesso para `board_move`, `board_swap` e `bench_to_board`.

`get_metrics()` devolve uma cópia dos contadores. Bloqueios de candidatos durante a construção das máscaras não devem ser contabilizados como tentativas reais de execução.

## 14. Reset e persistência

O método `reset()` recria os históricos limitados e limpa:

- Histórico de estados.
- Histórico de movimentos.
- Bloqueios explícitos.
- Contagem de visitas por estado.
- Última assinatura de posicionamento.
- Associação entre bloqueios e estados.
- Último movimento.

As métricas acumuladas permanecem intactas.

Após um reset, as proteções que dependem de histórico começam sem movimentos anteriores, mas as métricas continuam refletindo a vida anterior do gerenciador.

## 15. Limites e cuidados para preservar o comportamento atual

Para manter equivalência comportamental ao modificar ou portar essas proteções, devem ser preservados:

1. A identidade das unidades e o tratamento de unidades sem UUID.
2. A ordem das regras em `get_block_reason()`.
3. A diferença entre reversão, oscilação, ciclo banco ↔ tabuleiro e ciclo geral.
4. As janelas de histórico: seis movimentos para oscilação e oito movimentos relevantes para ciclo geral.
5. A exceção que compara trocas pela dupla de posições.
6. A associação de bloqueios explícitos à assinatura registrada do estado.
7. O registro do movimento somente após o sucesso da operação.
8. A diferença entre consulta de bloqueio, avaliação de risco e registro de métricas.
9. A persistência das métricas após `reset()`.
10. Os tipos e aliases reconhecidos por cada regra.

Há ainda dois pontos que exigem cuidado: `register_state()` contabiliza estados repetidos, mas não bloqueia diretamente ações; e `evaluate_move_risk()` não inclui todas as regras da decisão final. Não se deve presumir que esses métodos sejam intercambiáveis.

## 16. Conclusão

O `AntiLoopManager` possui proteções complementares: bloqueios explícitos, reversões imediatas, oscilações recentes, alternância entre banco e tabuleiro e ciclos gerais de posicionamento. Ele também mantém assinaturas de estado, contagem de visitas, métricas e uma avaliação separada de risco.

A decisão efetiva de bloqueio é determinada pela primeira regra satisfeita em `get_block_reason()`. A preservação da ordem, da identidade das unidades e do momento de registro dos movimentos é essencial para que uma implementação alternativa reproduza o comportamento atual.

Esta análise descreve as regras presentes em `ai/AntiLoopManager.py`; ela não afirma que todos os tipos de movimento e caminhos de registro são exercitados em todas as situações do ambiente.