# Determinismo e Estado Mutável — Action Masks, AntiLoop e Política PPO

## 1. Objetivo

Identificar quais funções apenas consultam dados e quais modificam históricos, contadores, caches ou o estado da partida, estabelecendo o comportamento que deve ser preservado durante a migração para C++.

A classificação considera quatro categorias:

- **Consulta pura:** calcula ou consulta informações sem modificar o estado observado.
- **Mutação de histórico:** adiciona, remove ou altera registros usados por decisões futuras.
- **Mutação de métricas:** incrementa ou redefine contadores e dados de diagnóstico.
- **Mutação do jogo:** modifica unidades, posições, economia, jogador ou outros dados da partida.

Uma função pode pertencer a mais de uma categoria. Por exemplo, a execução de um movimento modifica o tabuleiro, registra o movimento no AntiLoop e atualiza métricas.

## 2. Estado mutável relevante

### 2.1. `AntiLoopManager`

O gerenciador mantém estruturas que influenciam decisões futuras:

| Estrutura | Conteúdo | Efeito sobre decisões futuras |
|---|---|---|
| `position_history` | Histórico limitado de assinaturas espaciais | Permite consultar a sequência recente de estados |
| `move_history` | Histórico limitado de movimentos | Influencia reversões, oscilações e ciclos |
| `blocked_moves` | Bloqueios explícitos recentes | Pode impedir movimentos no estado correspondente |
| `state_visits` | Contagem de visitas por assinatura | Permite identificar estados repetidos |
| `last_board_signature` | Última assinatura registrada | Determina a validade de bloqueios explícitos |
| `blocked_move_states` | Associação entre bloqueios e assinaturas | Vincula o bloqueio ao estado em que foi criado |
| `last_move` | Último movimento registrado | Influencia a detecção de reversões |
| `execution_metrics` | Tentativas, bloqueios e movimentos executados | Afeta diagnósticos e observabilidade, não a decisão diretamente nas regras documentadas |

Os limites configurados são `history_size=20`, `blocked_move_size=10` e `loop_threshold=2`, por padrão.

### 2.2. Estado do jogo

Além do AntiLoop, a geração das máscaras consulta dados que pertencem aos gestores do ambiente:

- Tabuleiro e unidades.
- Banco e unidades.
- Loja e ofertas disponíveis.
- Ouro e condições econômicas.
- Estado ativo ou eliminado do jogador.
- Informações necessárias para validar origens, destinos e tipos de movimento.

Esses dados não devem ser modificados pela geração de máscaras. São a entrada usada para calcular quais ações estão disponíveis naquele instante.

### 2.3. Estado temporário

Existem também estruturas temporárias, como listas de movimentos relevantes, assinaturas recém-calculadas, matrizes de máscaras e tensores de entrada da política.

A criação dessas estruturas não representa mutação do estado oficial da partida. Entretanto, referências compartilhadas a objetos mutáveis devem ser evitadas quando uma operação pretende apenas produzir um snapshot.

## 3. Classificação das funções do AntiLoopManager

### 3.1. Consultas sem mutação intencional

| Função | Comportamento |
|---|---|
| `_unit_identity()` | Deriva a identidade de uma unidade |
| `make_board_signature()` | Constrói uma assinatura ordenada do tabuleiro e banco |
| `make_move_key()` | Constrói a chave de identificação de um movimento |
| `is_move_blocked()` | Consulta bloqueios explícitos e a assinatura associada |
| `is_reverse_move()` | Compara o candidato com `last_move` |
| `is_oscillating()` | Consulta a sequência recente de movimentos |
| `is_bench_board_loop()` | Consulta movimentos recentes de banco e tabuleiro |
| `is_cycle_move()` | Consulta o histórico para detectar fechamento repetido de ciclo |
| `was_state_seen()` | Consulta `state_visits` |
| `get_state_visits()` | Lê a contagem de visitas |
| `get_block_reason()` | Avalia as regras AntiLoop e retorna o primeiro motivo aplicável |
| `should_block_move()` | Converte a existência de um motivo em um booleano |
| `evaluate_move_risk()` | Calcula uma pontuação de risco a partir das consultas |
| `get_state()` | Constrói um resumo do estado interno |
| `get_metrics()` | Retorna uma representação das métricas |

Essas funções não devem modificar históricos ou contadores durante uma consulta normal.

**Atenção:** `get_state()` e `get_metrics()` devem ser tratados como operações de leitura. Caso retornem referências diretas a estruturas internas, o consumidor poderia modificá-las indiretamente. A implementação e a interface nativa devem garantir cópias ou representações independentes sempre que necessário.

### 3.2. Funções que modificam históricos

| Função | Estruturas modificadas | Efeito |
|---|---|---|
| `reset()` | Históricos, visitas, último movimento e bloqueios | Limpa o estado histórico do AntiLoop |
| `register_state()` | `position_history`, `state_visits`, `last_board_signature` | Registra um estado e atualiza sua contagem |
| `register_move()` | `move_history`, `last_move` | Registra um movimento |
| `block_move()` | `blocked_moves`, `blocked_move_states` | Registra um bloqueio explícito |
| `clear_old_blocks()` | `blocked_moves` | Remove entradas antigas quando necessário |

O momento em que essas funções são chamadas é tão importante quanto o conteúdo registrado. Uma chamada antecipada a `register_move()`, por exemplo, faria uma ação ainda não concluída influenciar as regras de reversão e oscilação.

### 3.3. Funções que modificam métricas

| Função | Mutação |
|---|---|
| `record_execution_attempt()` | Incrementa tentativas de execução |
| `record_execution_block()` | Incrementa bloqueios e o contador específico, quando existente |
| `record_successful_move()` | Incrementa contadores de movimentos concluídos |

Essas operações são telemetria da execução, não parte da consulta de validade.

A consulta de máscaras não deve incrementar contadores de tentativas, bloqueios ou sucessos.

### 3.4. Funções mistas ou de comportamento especial

`evaluate_move_risk()` executa diversas consultas e combina seus resultados em uma pontuação. Embora não deva alterar históricos ou métricas, não é apenas um acesso a um campo: depende da semântica e da ordem dos métodos consultados.

`get_block_reason()` também combina várias consultas, mas preserva uma regra de precedência: retorna no primeiro bloqueio encontrado.

`reset()` merece atenção especial: limpa o histórico, mas as métricas acumuladas de execução são inicializadas no construtor e não são apagadas pelo reset histórico atual.

## 4. Classificação das funções de ActionMaskManager

### 4.1. Geração e validação de máscaras

As seguintes funções são destinadas a calcular disponibilidade e validade, sem alterar o estado oficial da partida:

- `get_action_masks()`
- `get_type_mask()`
- `_get_shop_mask_and_availability()`
- `_has_valid_buy()`
- `_has_valid_reroll()`
- `_has_valid_buy_xp()`
- `_get_bench_source_mask_and_sell_availability()`
- `get_shop_mask()`
- `get_bench_source_mask()`
- `_has_valid_sell()`
- `get_board_target_mask()`
- `get_bench_to_board_target_mask()`
- `_has_valid_bench_move()`
- `_is_valid_bench_board_move()`
- `get_board_source_mask()`
- `get_conditioned_board_target_mask()`
- `_is_valid_board_move()`
- `_has_valid_board_move()`
- `get_board_move_target_mask()`
- `get_bench_move_source_mask()`
- `get_board_move_masks()`
- `get_bench_move_masks()`

Essas funções podem criar e preencher arrays temporários, consultar os gestores do jogo e chamar o AntiLoop repetidamente. Isso não significa que possam registrar movimentos ou alterar o histórico.

Os arrays retornados são resultados novos. Não devem funcionar como referências mutáveis ao estado interno dos gestores.

### 4.2. Exceção importante: `_should_block_anti_loop()`

A integração entre a geração de máscaras e o AntiLoop possui um comportamento especial: se uma consulta AntiLoop lançar uma exceção, o método de integração registra o erro e permite que o candidato continue nessa camada.

O resultado é permissivo para aquela proteção, mas não elimina as validações básicas de índices, ocupação e destino.

A função não deve atualizar o histórico de movimentos ou as métricas de execução como consequência de uma consulta bem-sucedida ou de um bloqueio detectado durante a geração de máscaras.

O registro de erro pode modificar logs ou telemetria externa, mas isso não deve influenciar a validade de consultas futuras.

## 5. Classificação das funções de execução do ambiente

As funções de execução são diferentes das funções de geração de máscaras: sua responsabilidade é aplicar uma ação e atualizar o estado.

| Função | Categoria | Efeitos esperados |
|---|---|---|
| `get_action_masks()` | Consulta | Produz máscaras para o estado atual |
| `_sanitize_action()` | Validação/preparação | Valida e normaliza a representação da ação |
| `_execute_buy()` | Mutação do jogo | Compra a unidade e atualiza os estados envolvidos |
| `_execute_reroll()` | Mutação do jogo | Atualiza loja e economia |
| `_execute_buy_xp()` | Mutação do jogo | Atualiza ouro, XP e/ou nível conforme as regras atuais |
| `_execute_move_bench()` | Mutação do jogo e histórico | Move a unidade e registra tentativa, bloqueio ou sucesso |
| `_execute_move_board()` | Mutação do jogo e histórico | Move ou troca unidades e registra o resultado |
| `_execute_sell()` | Mutação do jogo | Remove a unidade e atualiza os dados associados |
| `_execute_pass()` | Fluxo da ação | Aplica a semântica de passar a vez/ação |
| `_is_valid_bench_slot()` | Consulta/validação | Verifica validade de um slot do banco |
| `_rebuild_player_state()` | Reconstrução de estado | Atualiza a representação do estado do jogador |
| `step()` | Operação composta | Seleciona o caminho de execução, atualiza o ambiente e produz os resultados da transição |

A classificação exata de cada função de compra, venda e passagem deve acompanhar os efeitos concretos do código vigente, incluindo recompensas, logs, observações e atualizações dos gestores.

### 5.1. Ordem de registro de movimentos

Para movimentações do banco e do tabuleiro, o fluxo esperado é:

1. Validar índices e unidade de origem.
2. Registrar a tentativa quando o caminho de execução alcançar esse ponto.
3. Consultar as regras AntiLoop.
4. Se houver bloqueio, registrar o motivo e a métrica correspondente, sem registrar sucesso.
5. Validar as condições finais da operação.
6. Executar o movimento ou a troca.
7. Somente após sucesso, registrar o movimento no histórico e atualizar as métricas de sucesso.

A posição exata de cada validação determina quais métricas serão atualizadas em uma falha. A migração deve preservar o comportamento real do Python, inclusive se uma falha ocorrer antes ou depois do registro da tentativa.

## 6. Determinismo da geração de máscaras

A geração de máscaras deve ser determinística para uma entrada fixa, incluindo o histórico AntiLoop.

Isso significa que, para o mesmo snapshot:

- Os mesmos slots devem ser habilitados.
- Os mesmos motivos de bloqueio devem ser retornados.
- Os indicadores de disponibilidade devem coincidir.
- Os fallbacks técnicos devem ocupar as mesmas posições.
- Nenhuma chamada deve alterar o resultado de uma chamada seguinte por meio de mutações ocultas.

Entretanto, uma máscara pode mudar entre duas chamadas se o estado oficial ou o histórico mudar. Isso é comportamento esperado, não falta de determinismo.

A assinatura espacial atual considera a ordem das posições do tabuleiro e banco e as identidades das unidades. Ela não inclui ouro, XP, loja ou HP. Assim, uma alteração econômica pode modificar máscaras de compra sem alterar a assinatura espacial do AntiLoop.

## 7. Determinismo da política PPO

A geração determinística de máscaras não torna automaticamente determinística a política.

Na `policy.py`:

- `encode()` calcula representações a partir da observação.
- `_mask_logits()` aplica as restrições da máscara e valida seu formato.
- `_validate_selected_actions()` verifica se a ação escolhida é permitida pela máscara.
- `_sample_categorical()` usa `argmax` quando `deterministic=True`, mas amostra da distribuição categórica quando `deterministic=False`.
- `get_action_and_value()` produz ações e estatísticas da política.
- `evaluate_actions()` recalcula probabilidades e entropia para as ações registradas.

A amostragem estocástica depende do estado do gerador aleatório e do contexto de execução. Para comparar exclusivamente as implementações Python e C++ das máscaras, é melhor usar snapshots idênticos e comparar as máscaras antes da amostragem da política.

A equivalência do PPO deve ser testada separadamente, com controle apropriado da aleatoriedade, observações, pesos e dispositivos.

## 8. Determinismo em execução paralela

O ambiente pode utilizar múltiplos ambientes ou processos. Nesse caso, cada jogador/ambiente precisa ter seu próprio estado consistente.

Não se deve compartilhar acidentalmente entre ambientes:

- `move_history`;
- `state_visits`;
- `last_move`;
- bloqueios explícitos;
- contadores de execução que deveriam ser locais;
- caches dependentes do estado de um jogador.

A ordem de processamento entre jogadores não pode alterar o histórico AntiLoop de outro jogador, salvo se essa dependência for parte explícita das regras atuais.

Se o C++ mantiver estado persistente internamente no futuro, cada instância precisa ter identidade e ciclo de vida definidos. Um estado nativo global compartilhado seria perigoso porque poderia misturar históricos de jogadores ou episódios diferentes.

## 9. Caches e riscos de otimização

Não se deve introduzir cache de resultados sem definir primeiro suas dependências.

Um cache de máscara que utilize apenas a assinatura do tabuleiro pode ser incorreto porque as máscaras também podem depender de:

- Banco.
- Loja.
- Ouro.
- Nível e XP.
- Estado de eliminação.
- Histórico recente de movimentos.
- Bloqueios explícitos.
- Assinatura atual associada aos bloqueios.

Mesmo um cache indexado pelo snapshot completo pode ser incorreto se a identidade ou a serialização dos campos não reproduzir exatamente as regras Python.

Se for introduzido cache, o contrato deve especificar:

1. A chave completa de dependências.
2. Quando a entrada é invalidada.
3. Se os resultados retornados são cópias independentes.
4. Se uma consulta pode atualizar estatísticas de cache.
5. Como reset e rollback afetam o cache.
6. Como provar equivalência com a implementação sem cache.

Durante a primeira migração, evitar cache persistente é uma opção mais segura até que a equivalência funcional seja demonstrada.

## 10. Testes obrigatórios de mutação

A validação deve incluir snapshots antes e depois de cada operação.

### Consultas

Para `get_action_masks()`, `get_block_reason()`, `should_block_move()`, `evaluate_move_risk()` e funções auxiliares de consulta:

- Comparar históricos antes e depois.
- Comparar `last_move` e `last_board_signature`.
- Comparar bloqueios explícitos.
- Comparar contadores de execução.
- Confirmar que o tabuleiro, banco, loja e economia não mudaram.

### Registros

Para `register_state()`:

- Confirmar incremento de visitas.
- Confirmar atualização de `position_history`.
- Confirmar atualização de `last_board_signature`.

Para `register_move()`:

- Confirmar um único novo registro.
- Confirmar atualização de `last_move`.

Para `block_move()`:

- Confirmar chave correta.
- Confirmar associação à assinatura atual.
- Confirmar remoção da entrada mais antiga quando o limite exigir.

### Execução

Para movimentos válidos, bloqueados e falhos:

- Confirmar alteração do estado somente quando apropriada.
- Confirmar que movimentos bloqueados não são registrados como sucessos.
- Confirmar que falhas não produzem registros de sucesso.
- Confirmar contadores e motivos exatos.
- Confirmar rollback de unidades quando aplicável.

### Reset

- Confirmar que os históricos definidos para limpeza são esvaziados.
- Confirmar que as métricas de execução continuam acumuladas.
- Confirmar que não restam dados de um episódio anterior influenciando decisões do novo episódio.

## 11. Requisitos para a implementação C++

A migração deve manter separação explícita entre operações de consulta e operações de registro.

Requisitos:

1. Geração de máscaras sem efeitos colaterais no histórico.
2. Consultas AntiLoop sem alteração de estado ou métricas de execução.
3. Registros de estado e movimento somente nos pontos equivalentes aos do Python.
4. Atualização de métricas somente quando o fluxo de execução correspondente ocorrer.
5. Reset com a mesma semântica seletiva do Python.
6. Snapshots independentes do estado mutável original.
7. Ausência de estado global compartilhado entre jogadores.
8. Cache desabilitado inicialmente, a menos que sua correção seja demonstrada.
9. Comparação do estado antes e depois de cada operação nos testes de equivalência.
10. Separação entre determinismo das máscaras e aleatoriedade da política PPO.

## 12. Conclusão

A geração das máscaras e as consultas AntiLoop devem ser tratadas como operações de leitura. Registros de estado, movimentos, bloqueios e métricas são mutações explícitas e devem ocorrer somente nos pontos apropriados do fluxo.

O principal risco da migração não é apenas retornar uma máscara diferente: é modificar o histórico no momento errado e, por isso, alterar as decisões de iterações futuras. A equivalência exige preservar tanto os resultados imediatos quanto o estado que cada operação deixa para as próximas decisões.