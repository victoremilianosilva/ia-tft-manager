# Análise de Dependências — Action Masks, AntiLoop e Estado do Jogador

## 1. Visão geral

A geração das máscaras de ação depende diretamente do estado atual do jogador, das unidades presentes na reserva e no tabuleiro, das posições ocupadas, dos recursos econômicos e do histórico mantido pelo `AntiLoopManager`.

As principais classes envolvidas são:

- `ActionMaskManager`: consulta o estado do jogador, determina as ações possíveis e consulta o anti-loop para validar movimentos candidatos.
- `AntiLoopManager`: mantém o histórico de movimentos, as assinaturas dos estados de posicionamento, os bloqueios explícitos e as métricas das execuções.
- `BoardManager`: fornece o estado do tabuleiro, as posições ocupadas ou vazias e as operações de movimentação.
- `BenchManager`: fornece o estado da reserva e as operações de remoção e inserção de unidades.
- `EconomyManager`: fornece as condições econômicas para compras, rolagens e compra de experiência.
- `ShopManager`: fornece as unidades disponíveis para compra.
- `MiniTFTEnv`: integra os gerenciadores, expõe as máscaras e executa as ações.
- `TFTLobby`: coordena a geração das máscaras e a execução das ações dos jogadores.

A relação mais importante para a geração das máscaras de movimentação é:

`Estado atual → unidades e posições → candidatos a movimento → validação → AntiLoopManager → máscaras finais`

A execução de uma ação altera o estado do jogador e registra o movimento no histórico. Essas alterações influenciam a geração das máscaras das decisões seguintes.

---

## 2. Grafo de dependências

```text
MiniTFTEnv
│
├── BoardManager
│   ├── board[28]
│   ├── posições ocupadas
│   ├── posições vazias
│   ├── validação de posições
│   ├── move_unit()
│   └── swap_units()
│
├── BenchManager
│   ├── bench[9]
│   ├── unidades disponíveis
│   ├── posições livres
│   ├── remove_unit()
│   └── add_unit()
│
├── ShopManager
│   └── unidades disponíveis na loja
│
├── EconomyManager
│   ├── gold
│   ├── nível e experiência
│   ├── can_spend()
│   └── can_buy_xp()
│
├── ActionMaskManager
│   ├── consulta BoardManager
│   ├── consulta BenchManager
│   ├── consulta ShopManager
│   ├── consulta EconomyManager
│   └── consulta AntiLoopManager
│       ├── blocked_moves
│       ├── last_board_signature
│       ├── last_move
│       ├── move_history
│       ├── position_history
│       └── state_visits
│
└── execução de ações
    ├── validação da ação recebida
    ├── validação anti-loop
    ├── alteração de posições e unidades
    ├── registro do movimento
    └── métricas de execução

TFTLobby
│
├── obtém máscaras de cada jogador
├── solicita máscaras condicionais de movimentos
├── monta máscaras nomeadas
└── encaminha ações para MiniTFTEnv
```

O grafo representa as dependências funcionais identificadas. Não implica que todos os componentes sejam consultados em todas as ações.

---

## 3. Dependências do `ActionMaskManager`

O construtor de `ActionMaskManager` recebe as seguintes dependências:

| Dependência | Uso na geração das máscaras |
|---|---|
| `board_manager` | Consulta posições, unidades, ocupação e capacidade de movimentação do tabuleiro. |
| `bench_manager` | Consulta unidades da reserva, posições livres e disponibilidade de unidades para movimentação ou venda. |
| `shop_manager` | Obtém as unidades disponíveis na loja. |
| `economy_manager` | Verifica se compras, rolagens e compra de experiência são possíveis. |
| `composition_manager` | Dependência injetada; o uso direto nos métodos de geração de máscaras precisa ser confirmado por função. |
| `positioning_manager` | Dependência injetada; o uso direto nos métodos de geração de máscaras precisa ser confirmado por função. |
| `anti_loop_manager` | Determina se movimentos candidatos devem ser bloqueados pelo histórico e pelas regras anti-loop. |
| `unit_manager` | Dependência injetada; o uso direto nos métodos de geração de máscaras precisa ser confirmado por função. |

O gerenciador também mantém constantes para os tamanhos do tabuleiro, da reserva e da loja, além de um contador de erros nas consultas ao anti-loop.

### 3.1. Dependências por tipo de ação

#### Compra

A máscara de compra depende de:

1. Unidades disponíveis na loja.
2. Espaço livre na reserva.
3. Custo de cada unidade.
4. Saldo disponível no `EconomyManager`.

A existência de uma compra válida é calculada separadamente da máscara técnica. Se não houver opção válida, a máscara da loja habilita o índice zero como fallback, mas esse fallback não significa que uma compra real esteja disponível.

#### Venda

A máscara da reserva identifica posições ocupadas. A disponibilidade de venda é calculada a partir da existência de pelo menos uma unidade real na reserva.

Quando a reserva está vazia, o índice zero pode ser habilitado como fallback técnico, sem habilitar a ação `SELL`.

#### Movimentação da reserva para o tabuleiro

A geração depende de:

1. Unidade presente na posição de origem da reserva.
2. Validade do índice de origem.
3. Existência de espaço no tabuleiro.
4. Posição de destino válida.
5. Resultado da consulta ao `AntiLoopManager`.

O método `_is_valid_bench_board_move()` não exige que a posição de destino esteja vazia por si só. Essa condição é tratada pelo fluxo que gera os candidatos, que utiliza as posições vazias do tabuleiro.

#### Movimentação dentro do tabuleiro

A geração depende de:

1. Posição de origem dentro dos limites.
2. Unidade presente na origem.
3. Posição de destino dentro dos limites.
4. Origem e destino diferentes.
5. Ocupação da posição de destino.
6. Tipo de movimento resultante.
7. Resultado da consulta ao `AntiLoopManager`.

Se o destino estiver vazio, o tipo utilizado na consulta é `board_move`.

Se o destino estiver ocupado, o tipo utilizado é `board_swap`.

Na implementação observada, a troca de duas unidades é permitida pelo validador de movimentos desde que não seja bloqueada pelo anti-loop. A decisão de permitir uma troca não depende de o destino estar vazio.

---

## 4. Dependências do `AntiLoopManager`

O `AntiLoopManager` mantém estado próprio, independente das listas atuais do tabuleiro e da reserva.

As principais estruturas identificadas são:

| Estrutura | Finalidade |
|---|---|
| `position_history` | Histórico limitado de assinaturas de estados de posicionamento. |
| `move_history` | Histórico limitado de movimentos registrados. |
| `blocked_moves` | Coleção limitada de movimentos bloqueados explicitamente. |
| `state_visits` | Contagem de visitas por assinatura de estado. |
| `last_board_signature` | Última assinatura de posicionamento registrada. |
| `blocked_move_states` | Associação entre movimentos bloqueados e a assinatura de estado em que foram bloqueados. |
| `last_move` | Último movimento registrado. |
| `execution_metrics` | Contadores de tentativas, bloqueios e movimentos executados. |

Os limites de histórico são configuráveis pelo construtor. Os valores padrão identificados são `history_size=20`, `blocked_move_size=10` e `loop_threshold=2`.

As métricas de execução são mantidas separadamente do histórico de posicionamento e não são apagadas pelo método `reset()`.

### 4.1. Dependência da identidade da unidade

O método `_unit_identity()` utiliza a seguinte regra:

1. Se a unidade for um dicionário com `uuid`, a identidade será baseada no UUID.
2. Caso não exista UUID, a identidade será baseada em `id` e `star`.
3. Se o objeto não for um dicionário, a identidade será `None`.

Essa identidade é utilizada na criação de chaves de movimento e assinaturas de estado, bem como na comparação de movimentos anteriores.

**Consequência:** unidades com o mesmo `id` e a mesma estrela, mas sem UUID, são tratadas como equivalentes pelo mecanismo de identidade. Com UUID disponível, unidades individuais podem ser distinguidas.

A equivalência usada pelo anti-loop não deve ser confundida com a identidade completa da unidade em todos os outros sistemas do jogo.

### 4.2. Dependência das assinaturas de estado

`make_board_signature(board, bench)` cria uma representação ordenada das posições do tabuleiro e da reserva.

Para cada posição, registra:

- O índice da posição.
- `None`, se estiver vazia.
- A identidade da unidade, se estiver ocupada.

Portanto, a assinatura depende tanto da identidade das unidades quanto de suas posições.

A inclusão do tabuleiro e da reserva permite distinguir configurações que possuem as mesmas unidades, mas distribuições diferentes entre posições ou entre as duas áreas.

A assinatura não representa necessariamente todo o estado do jogador: ouro, experiência, loja, HP e outros atributos não aparecem diretamente nessa estrutura.

### 4.3. Dependência do histórico de movimentos

Cada movimento registrado contém:

- Tipo do movimento.
- Origem.
- Destino.
- Identidade da unidade.

`register_move()` acrescenta o movimento a `move_history` e atualiza `last_move`.

As regras anti-loop consultam esse histórico para identificar padrões de repetição.

O histórico de movimentos não é derivado automaticamente das posições atuais. Ele depende de os pontos de execução registrarem corretamente os movimentos que realmente ocorreram.

---

## 5. Dependências entre as regras anti-loop

O método `get_block_reason()` consulta as regras nesta ordem:

1. Bloqueio explícito.
2. Movimento reverso.
3. Oscilação.
4. Ciclo entre reserva e tabuleiro, quando aplicável.
5. Ciclo geral.
6. Ausência de bloqueio.

### 5.1. Bloqueio explícito

`is_move_blocked()` compara a chave do movimento candidato com as chaves armazenadas em `blocked_moves`.

A chave é composta pelo tipo, origem, destino e identidade da unidade.

O bloqueio só é considerado ativo quando a assinatura associada ao movimento coincide com `last_board_signature`.

Logo, essa regra depende simultaneamente de:

- Identidade da unidade.
- Tipo de movimento.
- Origem e destino.
- Coleção de movimentos bloqueados.
- Última assinatura de estado registrada.

Um bloqueio pode deixar de ser aplicável quando a assinatura de estado muda. Entretanto, a atualização dessa assinatura depende de `register_state()` ser chamado em outro ponto do fluxo.

### 5.2. Movimento reverso

`is_reverse_move()` depende de `last_move`.

Para movimentos normais, exige correspondência do tipo e da identidade da unidade, além da inversão de origem e destino.

Para `board_swap`, a regra é diferente: considera a mesma dupla de posições, independentemente da ordem entre origem e destino e da identidade da unidade que estava na origem.

Portanto, o significado de uma reversão depende do tipo de movimento e não pode ser reduzido a uma única comparação genérica de posições.

### 5.3. Oscilação

`is_oscillating()` examina os seis movimentos mais recentes do histórico.

Para movimentos `board_move`, considera movimentos do mesmo tipo e da mesma unidade.

Para `board_swap`, também considera movimentos `board_move` no histórico da unidade e reconstrói uma sequência de posições.

A sequência precisa chegar à origem do candidato. A regra então verifica se o destino candidato já aparece pelo menos duas vezes na cadeia anterior.

Essa verificação depende de:

- Identidade da unidade.
- Tipo de movimento.
- Ordem cronológica dos registros.
- Origem e destino dos movimentos anteriores.
- Continuidade da sequência.

### 5.4. Ciclo entre reserva e tabuleiro

`is_bench_board_loop()` reconhece os tipos `bench_to_board` e `board_to_bench`, incluindo aliases com nomes alternativos.

A regra filtra o histórico para a mesma unidade e precisa encontrar pelo menos dois movimentos relevantes.

Em seguida, verifica se os dois últimos movimentos representam uma ida e uma volta entre as mesmas posições.

O candidato é bloqueado quando tenta repetir a transição anterior.

A identidade da unidade e a correspondência entre origem e destino são fundamentais para essa detecção.

### 5.5. Ciclo geral

`is_cycle_move()` considera apenas `board_move` e `board_swap`.

A regra analisa os oito movimentos mais recentes relevantes para a mesma identidade de unidade, procurando uma sequência contínua que já tenha fechado um ciclo.

O primeiro fechamento de um ciclo é permitido. A regra procura impedir um novo fechamento quando o histórico já demonstra a repetição do ciclo.

Essa lógica depende da sequência de movimentos efetivamente registrada, não apenas da comparação entre o tabuleiro atual e um estado anterior.

---

## 6. Relação entre geração de máscaras e histórico

A geração de máscaras consulta o `AntiLoopManager` repetidamente enquanto avalia candidatos.

Para movimentos do tabuleiro, `_is_valid_board_move()` determina o tipo de movimento e chama `_should_block_anti_loop()`.

Para movimentos da reserva, `_is_valid_bench_board_move()` consulta o anti-loop usando o tipo `bench_to_board`.

A consulta de bloqueio é realizada por `should_block_move()`, que utiliza `get_block_reason()` e não deve modificar o histórico nem os contadores de execução.

Essa separação é importante: gerar máscaras envolve avaliar vários candidatos que podem nunca ser executados.

### Comportamento em caso de exceção

`_should_block_anti_loop()` captura exceções da consulta ao anti-loop, registra o erro e retorna `False`.

Como o chamador interpreta `True` como bloqueio, esse retorno permite que o candidato passe pela verificação anti-loop naquela camada.

Isso não significa que a ação esteja garantidamente válida em todas as camadas. A execução possui suas próprias validações.

Esse comportamento cria uma dependência operacional: uma falha na consulta anti-loop pode ampliar o conjunto de candidatos que passam pela geração de máscaras, tornando importante preservar ou redefinir explicitamente essa semântica em qualquer implementação alternativa.

---

## 7. Dependências entre máscaras e estado real do tabuleiro

As máscaras de movimentação são derivadas do estado atual do `BoardManager` e do `BenchManager`.

### Máscaras de origem

A máscara de origem do tabuleiro habilita uma posição ocupada quando existe pelo menos um destino real válido para aquela origem.

A máscara de origem da reserva habilita uma posição ocupada quando existe pelo menos um destino válido no tabuleiro para a unidade.

Assim, a mera presença de uma unidade não garante que sua posição seja habilitada como origem de movimento.

### Máscaras de destino

As máscaras de destino são condicionadas às origens e aos movimentos válidos.

Uma origem pode ter destinos diferentes dependendo:

- Da unidade presente.
- Da ocupação das posições.
- Do tipo de movimento.
- Do histórico anti-loop.

As máscaras condicionais permitem que a política escolha uma origem e, depois, selecione um destino compatível com essa origem.

### Fallback técnico

Quando não há opções reais, algumas máscaras habilitam o índice zero para manter uma distribuição categórica válida.

Esse fallback não deve ser interpretado como prova de que a posição zero está livre, contém uma unidade válida ou representa um movimento executável.

Por isso, o código mantém verificações separadas para a existência de movimentos válidos, como `_has_valid_board_move()` e `_has_valid_bench_move()`.

A disponibilidade de `MOVE_BOARD` e `MOVE_BENCH` é calculada a partir desses resultados reais, e não apenas da existência de um bit habilitado em uma máscara auxiliar.

---

## 8. Dependências durante a execução das ações

A validação durante a execução é uma etapa distinta da geração de máscaras.

### 8.1. Reserva para tabuleiro

O método `_execute_move_bench()`:

1. Lê a origem na reserva e o destino no tabuleiro.
2. Valida os índices.
3. Obtém a unidade da reserva.
4. Registra uma tentativa real no `AntiLoopManager`.
5. Consulta `get_block_reason()`.
6. Registra o bloqueio e retorna uma penalidade se a regra impedir o movimento.
7. Verifica se o destino está vazio.
8. Remove a unidade da reserva.
9. Insere a unidade no tabuleiro.
10. Registra o movimento concluído com `register_move()`.
11. Atualiza as métricas de movimento bem-sucedido.

Se a inserção no tabuleiro falhar, o código tenta restaurar a unidade à reserva antes de retornar.

### 8.2. Movimentação dentro do tabuleiro

O método `_execute_move_board()`:

1. Lê a origem e o destino.
2. Valida os índices e verifica se são diferentes.
3. Obtém a unidade da origem.
4. Verifica se o destino está ocupado.
5. Determina `board_move` ou `board_swap`.
6. Registra a tentativa de execução.
7. Consulta o anti-loop.
8. Se houver bloqueio, registra o motivo e retorna uma penalidade.
9. Se não houver bloqueio, executa um movimento ou uma troca.
10. Registra o movimento após a execução bem-sucedida.

A implementação também registra métricas para tentativas, bloqueios e movimentos executados.

### Consequência

As máscaras antecipam quais movimentos são aceitáveis segundo o estado consultado. A execução confirma a legalidade e volta a consultar o anti-loop antes de modificar o estado.

Essa segunda verificação é necessária porque o estado pode mudar entre a geração das máscaras e a execução, ou porque a ação recebida pode não corresponder às opções anteriormente calculadas.

---

## 9. Ciclo de vida do estado e do histórico

O método `MiniTFTEnv.reset()` reinicializa:

- `BoardManager`.
- `BenchManager`.
- `EconomyManager`.
- `CompositionManager`.
- `PositioningManager`.
- `StrategyManager`.
- `AntiLoopManager`.
- `RewardManager`.

Em seguida, cria a unidade inicial, atualiza a loja e reconstrói o estado do jogador.

O reset do anti-loop limpa os históricos de posicionamento e movimentos, os bloqueios, as contagens de visitas, a última assinatura e o último movimento.

As métricas acumuladas de execução, entretanto, são mantidas pelo `AntiLoopManager.reset()` atual.

Esse comportamento precisa ser levado em conta ao reproduzir o ciclo de vida do ambiente: reinicializar o histórico não equivale necessariamente a reinicializar todos os contadores de diagnóstico.

### Registro de estados

`register_state()`:

1. Calcula a assinatura do tabuleiro e da reserva.
2. Acrescenta a assinatura a `position_history`.
3. Incrementa a contagem em `state_visits`.
4. Atualiza `last_board_signature`.
5. Informa se o estado alcançou o limite de visitas.

A análise identificou o método e sua semântica, mas a localização e a frequência exatas de todas as chamadas a `register_state()` precisam ser verificadas antes de determinar quando os bloqueios associados a um estado são atualizados.

Não se deve assumir que cada movimento executado provoca automaticamente um registro de estado.

---

## 10. Dependências diretas versus dependências indiretas

### Dependências diretas das máscaras

- Estado de `BoardManager`.
- Estado de `BenchManager`.
- Estado de `ShopManager`.
- Estado de `EconomyManager`.
- Resultado das regras de validação de movimentos.
- Resultado de `AntiLoopManager.should_block_move()`.

### Dependências indiretas das máscaras

- Identidade estável das unidades.
- Histórico de movimentos executados.
- Último movimento registrado.
- Assinaturas de estados previamente registradas.
- Bloqueios explícitos associados a uma assinatura.
- Ordem dos movimentos armazenados no histórico.
- Limites dos históricos e critérios de detecção de repetição.

### Dependências da execução

- Ação selecionada pela política.
- Estado real no momento da execução.
- Validações do ambiente.
- Resultado da consulta anti-loop.
- Sucesso ou falha das operações de movimentação.
- Atualizações do histórico e das métricas após a execução.

---

## 11. Implicações para uma implementação equivalente em C++

Uma implementação alternativa precisa reproduzir não apenas os resultados booleanos das funções, mas também as relações entre os componentes.

### Estado que precisa ser consistente

1. Representação do tabuleiro e da reserva.
2. Identidade das unidades.
3. Tipos de movimento.
4. Origem e destino.
5. Histórico de movimentos.
6. Último movimento.
7. Assinaturas de estado.
8. Contagens de visitas.
9. Bloqueios explícitos e estado associado.
10. Limites e regras de expiração dos históricos.

### Semântica que precisa ser preservada

- Uma consulta de máscara não deve registrar um movimento executado.
- Uma tentativa de execução não deve ser confundida com um movimento bem-sucedido.
- Um movimento só deve entrar no histórico de movimentos quando o fluxo atual determinar que ele foi executado.
- A identidade usada na comparação de movimentos deve permanecer estável.
- A distinção entre movimento normal e troca deve ser preservada.
- A ordem das verificações anti-loop deve ser a mesma.
- A geração das máscaras deve continuar separada da validação final da execução.
- Os fallbacks técnicos não devem ser interpretados como ações reais válidas.
- As mutações de estado e histórico devem ocorrer nos mesmos pontos lógicos do fluxo.

### O que não deve ser presumido

- Que todo o estado do jogador é necessário em cada chamada nativa.
- Que todas as funções injetadas em `ActionMaskManager` são usadas na validação de movimentação.
- Que o histórico anti-loop contém um registro para cada mudança possível de estado.
- Que a assinatura de posicionamento representa o estado completo do jogo.
- Que uma máscara válida garante a execução bem-sucedida da ação.
- Que a identidade de duas unidades é sempre equivalente em todos os subsistemas.

---

## 12. Conclusão da análise

A dependência central é o acoplamento entre a representação atual das unidades e posições, o gerador de máscaras e o histórico mantido pelo anti-loop.

`ActionMaskManager` consulta o estado atual para gerar candidatos, e cada candidato pode provocar verificações de histórico em `AntiLoopManager`. A execução de movimentos modifica as estruturas do tabuleiro e da reserva e registra movimentos bem-sucedidos, alterando os dados consultados nas decisões seguintes.

O histórico anti-loop possui estado próprio e não pode ser substituído apenas pela leitura do tabuleiro atual. Ele guarda informações temporais necessárias para distinguir um movimento legítimo de uma reversão, oscilação ou repetição de ciclo.

Portanto, a equivalência comportamental depende de preservar tanto o estado espacial — unidades e posições — quanto o estado temporal — sequência de movimentos, bloqueios e visitas a estados.

A principal oportunidade de otimização está na repetição dessas consultas durante a geração das máscaras. Antes de implementar caches ou mover as regras para C++, é necessário identificar quais informações podem ser calculadas uma vez por estado sem alterar a semântica temporal do anti-loop, e quais consultas precisam continuar refletindo o histórico atualizado.