# Contexto Técnico — Migração das Masks e dos Gargalos de Decisão do TFT para C++

**Projeto:** `victoremilianosilva/teste-ia`  
**Roadmap:** `4.5 — Migração das Masks e dos Gargalos de Decisão para C++`  
**Status atual:** inventário inicial das funções concluído; auditoria detalhada das regras e dependências ainda pendente.  
**Objetivo:** permitir que outra sessão do ChatGPT continue a análise sem depender de todo o histórico da conversa.

---

## 1. Instruções obrigatórias para continuar o trabalho

1. Trabalhar **um item do roadmap por vez**.
2. Ao concluir um item, informar explicitamente que ele foi concluído e **parar, aguardando autorização antes de iniciar o próximo**.
3. Não modificar, criar, editar, fazer commit ou push de arquivos no repositório sem autorização explícita.
4. A inspeção do repositório pode ser feita em modo somente leitura.
5. Não afirmar que testes passaram sem que tenham sido efetivamente executados e seus resultados verificados.
6. Não declarar equivalência entre Python e C++ antes de testes comparativos.
7. Preservar o comportamento atual da IA, incluindo PPO, máscaras condicionais, regras anti-loop, histórico de movimentos e efeitos colaterais.
8. A implementação Python deve continuar disponível até que a implementação C++ tenha equivalência comprovada.
9. Não iniciar uma migração ou otimização antecipadamente enquanto a auditoria e o contrato não estiverem concluídos.
10. Quando uma análise depender de detalhes exatos do código que não estão documentados aqui, consultar somente os arquivos necessários, em modo de leitura. Não presumir detalhes desconhecidos.

## 2. Contexto do projeto

O projeto é uma IA de um ambiente inspirado em Teamfight Tactics, implementada em Python e treinada com PPO.

A política PPO deve continuar em Python. A migração planejada para C++ é direcionada aos gargalos de decisão, especialmente:

- Geração de máscaras de ações.
- Validação de movimentos candidatos.
- Verificações anti-loop.
- Detecção de movimentos reversos, oscilações e ciclos.
- Operações repetitivas sobre identidade de unidades e histórico de estados.

O objetivo não é mudar a estratégia da IA, mas reduzir o custo computacional preservando as regras existentes.

### Estrutura de ação conhecida

O projeto utiliza uma ação composta, com dimensões conhecidas:

`[7, 5, 9, 28, 28, 28]`

O ambiente possui um tabuleiro de 4 × 7 posições, totalizando 28 casas, e uma reserva de 9 posições.

As dimensões correspondem a componentes condicionais da ação, envolvendo tipo, loja, reserva e posições do tabuleiro. A correspondência exata entre cada dimensão e seus índices deve ser confirmada no código atual antes de congelar o contrato nativo.

O projeto já passou por uma implementação DQN e foi posteriormente adaptado para PPO. A migração descrita neste documento se refere à implementação PPO atual.

---

## 3. Arquitetura atual identificada

O fluxo de decisão envolve cinco componentes principais:

1. `TFTLobby`: integra as máscaras por jogador.
2. `ActionMaskManager`: gera as máscaras e verifica movimentos candidatos.
3. `AntiLoopManager`: bloqueia movimentos de acordo com as regras anti-loop e mantém informações de histórico.
4. `TFTPolicy`: aplica máscaras à política PPO e seleciona ações.
5. `MiniTFTEnv`: recebe, sanitiza, valida e executa ações, atualizando o estado.

O fluxo é dependente do estado: a execução de uma ação modifica o ambiente e o histórico, que serão utilizados na próxima geração de máscaras.

A geração de máscaras não é apenas uma enumeração de posições vazias. Ela pode depender da unidade, origem, destino, estado atual, histórico e regras de bloqueio.

### Arquivos envolvidos

| Arquivo | Responsabilidade |
|---|---|
| `ai/ActionMaskManager.py` | Geração de máscaras e validação de movimentos candidatos. |
| `ai/AntiLoopManager.py` | Detecção de ciclos, bloqueios e gerenciamento do histórico anti-loop. |
| `lobby/TFTLobby.py` | Integração das máscaras e processamento das ações na lobby. |
| `env.py` | Interface do ambiente, sanitização, validação e execução das ações. |
| `policy.py` | Seleção de ações com PPO, aplicação das máscaras e avaliação de ações. |
| `trainer.py` | Integração com o treinamento PPO e coleta das decisões. |
| `tests/test_ppo_mask_consistency.py` | Testes relacionados à consistência das máscaras no PPO. |
| `tests/test_action_mask_conditionals.py` | Testes relacionados às máscaras condicionais. |
| `roadmap_ia_tft.md` | Roadmap e acompanhamento das etapas de migração. |

Essa é a lista dos principais pontos identificados, não uma garantia de que todos os chamadores indiretos e dependências auxiliares já tenham sido mapeados.

---

## 4. Inventário das funções identificadas

### 4.1. `ai/ActionMaskManager.py`

#### Coordenação e ações econômicas

- `get_action_masks`
  - Coordena a geração do conjunto de máscaras.
- `get_type_mask`
  - Determina quais tipos de ação estão disponíveis.
- `_get_shop_mask_and_availability`
  - Gera a máscara da loja e verifica disponibilidade.
- `_has_valid_buy`
  - Verifica se existe uma compra válida.
- `_has_valid_reroll`
  - Verifica se existe uma nova rolagem válida.
- `_has_valid_buy_xp`
  - Verifica se comprar experiência é válido.
- `_get_bench_source_mask_and_sell_availability`
  - Produz informações sobre as posições da reserva e disponibilidade de venda.
- `get_shop_mask`
  - Gera a máscara das opções da loja.
- `get_bench_source_mask`
  - Gera a máscara das posições da reserva usadas como origem.
- `_has_valid_sell`
  - Verifica se existe uma venda válida.

#### Movimentos envolvendo a reserva

- `get_board_target_mask`
  - Gera a máscara das posições de destino no tabuleiro.
- `get_bench_to_board_target_mask`
  - Gera os destinos para movimentar uma unidade da reserva ao tabuleiro.
- `_has_valid_bench_move`
  - Verifica a existência de movimento válido envolvendo a reserva.
- `_is_valid_bench_board_move`
  - Valida um movimento entre reserva e tabuleiro.
- `get_bench_move_source_mask`
  - Gera a máscara das origens para movimentos envolvendo a reserva.
- `get_bench_move_masks`
  - Coordena as máscaras específicas de movimentação da reserva.

#### Movimentos dentro do tabuleiro

- `get_board_source_mask`
  - Gera a máscara das posições de origem no tabuleiro.
- `get_conditioned_board_target_mask`
  - Gera destinos condicionados à origem selecionada.
- `_is_valid_board_move`
  - Valida movimentos candidatos dentro do tabuleiro.
- `_has_valid_board_move`
  - Verifica a existência de pelo menos um movimento válido.
- `get_board_move_target_mask`
  - Gera a máscara dos destinos de movimentos no tabuleiro.
- `get_board_move_masks`
  - Coordena a geração das máscaras de movimentos dentro do tabuleiro.

### 4.2. `ai/AntiLoopManager.py`

#### Decisão e detecção de bloqueios

- `should_block_move`
  - Decide se um movimento deve ser bloqueado.
- `get_block_reason`
  - Determina o motivo do bloqueio.
- `is_move_blocked`
  - Verifica se um movimento está bloqueado.
- `is_reverse_move`
  - Detecta movimentos reversos.
- `is_oscillating`
  - Detecta oscilações repetitivas.
- `is_bench_board_loop`
  - Detecta ciclos envolvendo reserva e tabuleiro.
- `is_cycle_move`
  - Detecta movimentos que fazem parte de ciclos.
- `evaluate_move_risk`
  - Avalia o risco de um movimento de acordo com as regras implementadas.

#### Identidade e representação

- `_unit_identity`
  - Produz a identidade usada para reconhecer unidades.
- `make_move_key`
  - Cria uma chave que representa um movimento.
- `make_board_signature`
  - Cria uma assinatura da configuração do tabuleiro.

#### Histórico e mutações de estado

- `block_move`
  - Registra ou aplica um bloqueio.
- `clear_old_blocks`
  - Limpa bloqueios antigos conforme as regras existentes.
- `register_state`
  - Registra um estado observado.
- `register_move`
  - Registra um movimento.
- `was_state_seen`
  - Verifica se um estado já foi observado.
- `get_state_visits`
  - Consulta o número de visitas a um estado.
- `get_state`
  - Recupera informações do estado mantidas pelo gerenciador.
- `record_execution_attempt`
  - Registra uma tentativa de execução.
- `record_execution_block`
  - Registra uma execução bloqueada.
- `record_successful_move`
  - Registra um movimento bem-sucedido.
- `get_metrics`
  - Expõe métricas do sistema anti-loop.
- `reset`
  - Reinicializa o estado interno.
- `debug_print`
  - Exibe informações de diagnóstico.

**Atenção:** esta lista é o inventário inicial levantado na inspeção. A semântica detalhada, as estruturas internas e os efeitos colaterais ainda precisam ser documentados antes da migração.

### 4.3. `lobby/TFTLobby.py`

- `get_action_masks`
  - Obtém e organiza as máscaras dos jogadores.
- `_dead_player_mask`
  - Produz as máscaras aplicáveis a jogadores eliminados ou inativos, conforme as regras existentes.
- `step`
  - Processa o avanço da lobby e integra as ações ao ambiente.

As chaves de máscara identificadas no resultado são:

- `type_mask`
- `shop_mask`
- `bench_source_mask`
- `board_target_mask`
- `board_source_mask`
- `board_move_target_masks`
- `bench_move_source_mask`
- `bench_to_board_target_masks`

Devem ser preservados os nomes, dimensões, tipos de dados e semântica dos índices, ou implementada uma conversão explícita e testada.

### 4.4. `env.py`

#### Interface e estado

- `get_action_masks`
  - Expõe as máscaras do ambiente.
- `step`
  - Processa uma ação e retorna a transição do ambiente.
- `_sanitize_action`
  - Sanitiza ou normaliza a ação recebida.
- `_rebuild_player_state`
  - Reconstrói ou atualiza a representação do estado do jogador.

#### Execução das ações

- `_execute_buy`
  - Executa uma compra.
- `_execute_reroll`
  - Executa uma nova rolagem da loja.
- `_execute_buy_xp`
  - Executa a compra de experiência.
- `_execute_move_bench`
  - Executa um movimento envolvendo a reserva.
- `_execute_move_board`
  - Executa um movimento ou troca no tabuleiro.
- `_execute_sell`
  - Executa uma venda.
- `_execute_pass`
  - Executa a ação de passar.
- `_is_valid_bench_slot`
  - Valida uma posição da reserva.

A geração de máscaras não substitui a validação durante a execução. O ambiente precisa continuar protegido contra ações inválidas, inclusive em caso de inconsistência de estado ou erro de integração.

### 4.5. `policy.py`

- `get_action`
  - Seleciona ações com a política PPO.
- `_mask_logits`
  - Aplica máscaras aos logits da política.
- `_validate_selected_actions`
  - Verifica a consistência das ações selecionadas.
- `_sample_categorical`
  - Realiza a amostragem categórica.
- `get_action_and_value`
  - Obtém a ação e as informações de valor utilizadas pelo PPO.
- `evaluate_actions`
  - Avalia ações existentes para o treinamento.

**Decisão arquitetural:** a rede neural e o treinamento PPO permanecem em Python. O objetivo é acelerar as operações de decisão sem mudar a política de aprendizado.

---

## 5. Ordem das regras anti-loop identificada

A ordem observada no fluxo de bloqueio é:

1. Bloqueio explícito.
2. Movimento reverso.
3. Oscilação.
4. Ciclo envolvendo reserva e tabuleiro.
5. Ciclo geral.
6. Ausência de bloqueio pelas verificações anteriores.

Essa ordem precisa ser confirmada diretamente no código antes da implementação C++.

Um movimento pode satisfazer mais de uma regra. Alterar a precedência pode mudar o motivo registrado e, dependendo da implementação, o resultado da decisão.

### Tratamento de exceções

Foi identificado que `_should_block_anti_loop()` captura exceções e permite que o candidato continue na geração da máscara em determinadas falhas, registrando o erro.

Esse comportamento precisa ser documentado e reproduzido ou alterado deliberadamente em uma etapa separada. Não deve mudar silenciosamente durante a migração.

---

## 6. Máscaras condicionais

A política usa uma ação composta, com dimensões conhecidas:

`[7, 5, 9, 28, 28, 28]`

O produto das dimensões é:

`7 × 5 × 9 × 28 × 28 × 28 = 26.438.400`

Esse número representa o produto das possibilidades dimensionais, não a quantidade de ações que a política precisa enumerar explicitamente.

As máscaras condicionais restringem as opções conforme as seleções anteriores.

Regras a preservar:

- Uma máscara posterior pode depender da seleção anterior.
- As máscaras devem corresponder ao estado atual.
- As posições de origem e destino devem manter o significado.
- Máscaras da reserva e do tabuleiro não podem ser confundidas.
- Um bit de fallback não significa necessariamente que existe um movimento real válido.
- A lógica de seleção e avaliação do PPO deve continuar consistente.

A correspondência exata de cada dimensão com o campo de ação precisa ser confirmada no código atual.

---

## 7. Benchmarks e profiling já executados pelo usuário

Os números a seguir foram fornecidos pelo usuário após executar os benchmarks no projeto. Não foram executados independentemente nesta análise.

### 7.1. Custo de `get_action_masks()`

Benchmark por jogador:

- 8 jogadores ativos.
- 500 amostras por jogador.
- Médias individuais aproximadamente entre 0,1765 ms e 0,1999 ms.
- Média geral: 0,1860 ms.
- Mediana: 0,1755 ms.
- P95: 0,3248 ms.

A estimativa por multiplicação da média para oito jogadores foi aproximadamente 1,4881 ms.

**Limitação:** essa estimativa representa o custo calculado a partir da média por jogador, não necessariamente o custo total da chamada de lobby, incluindo agregação, comunicação entre processos e conversões.

### 7.2. `env.step()` e combate

Com a ação `PASS`:

| Operação | Média | Mediana | P95 |
|---|---:|---:|---:|
| `MiniTFTEnv.step()` | 0,2877 ms | 0,2821 ms | 0,3080 ms |
| `TFTLobby.resolve_combat()` | 0,1005 ms | 0,0978 ms | 0,1173 ms |

Foram utilizadas 500 amostras e o HP foi restaurado antes de cada combate.

O teste de combate utilizou apenas uma unidade por lado. Ele mede o caminho de `resolve_combat()` nesse cenário, não apenas o motor C++ isoladamente.

### 7.3. Throughput inicial

Benchmark com `PASS`, quatro lobbies e oito jogadores por lobby, com 500 chamadas:

- Média por chamada vetorizada: 341,8654 ms.
- Mediana: 343,4781 ms.
- P95: 364,1867 ms.
- Tempo total: 170,933 s.
- Chamadas vetorizadas: 500.
- Passos de lobby: 2.000.
- Passos de jogadores: 16.000.
- Throughput: 2,93 chamadas vetorizadas/s.
- Throughput: 11,70 passos de lobby/s.
- Throughput: 93,60 passos de jogador/s.

Esse benchmark foi considerado insuficiente para caracterizar o fluxo real de decisão PPO, porque utilizava `PASS` e não exercitava de maneira representativa as máscaras e ações reais.

### 7.4. Benchmark do fluxo PPO real

Com checkpoint carregado e fluxo real de decisão:

| Etapa | Média | P95 |
|---|---:|---:|
| Máscaras | 69,602 ms | 103,353 ms |
| Política | 5,305 ms | 6,338 ms |
| Conversão | 0,057 ms | 0,074 ms |
| `env_step` | 46,140 ms | 126,949 ms |
| Total | 121,137 ms | 217,930 ms |

Outros resultados:

- 8,26 iterações/s.
- 264,16 decisões/s.
- 500 iterações em 60,57 s.
- Cada iteração representava 32 agentes.

A etapa de máscaras inclui `env_method("get_action_masks")` e `_flatten_masks()`. Portanto, os 69,602 ms não representam exclusivamente o cálculo interno de `ActionMaskManager`.

O P95 elevado de `env_step` indica variação de custo entre etapas, possivelmente associada a eventos diferentes no ambiente. A causa exata ainda precisa ser investigada.

### 7.5. Profiling dos gargalos

Resultados de `profile_mask_bottlenecks.py`:

| Operação | Média | Mediana | P95 |
|---|---:|---:|---:|
| Máscaras de todas as lobbies | 34,993 ms | 34,461 ms | 38,056 ms |
| `_flatten_masks()` | 2,330 ms | 2,232 ms | 2,624 ms |
| Fluxo combinado | 37,323 ms | 36,714 ms | 41,970 ms |

O profiling instrumentado abrangeu 100 chamadas a `env_method`, quatro lobbies e 400 chamadas a `TFTLobby.get_action_masks()`.

Tempos cumulativos observados:

| Função | Tempo cumulativo |
|---|---:|
| `ActionMaskManager.get_board_move_masks()` | 6,831 s |
| `_is_valid_board_move()` | 6,345 s |
| `_should_block_anti_loop()` | 6,345 s |
| `AntiLoopManager.should_block_move()` | 6,036 s |
| `AntiLoopManager.get_block_reason()` | 5,812 s |
| `_unit_identity()` | 1,676 s |
| `is_cycle_move()` | 1,660 s |
| `is_oscillating()` | 1,427 s |
| `ShopManager.get_shop()` | 0,832 s |
| `deepcopy` associado ao caminho da loja | 0,823 s |
| `get_bench_move_masks()` | 0,793 s |
| `_is_valid_bench_board_move()` | 0,724 s |

Os tempos cumulativos são inclusivos e se sobrepõem. Não devem ser somados como custos independentes.

### 7.6. Conclusão de desempenho

O principal candidato à otimização é a repetição de verificações anti-loop durante a geração de movimentos candidatos no tabuleiro.

O caminho identificado inclui:

`get_board_move_masks()` → `_is_valid_board_move()` → `_should_block_anti_loop()` → `should_block_move()` → `get_block_reason()` → verificações de ciclos e identidade.

A hipótese principal é que identidades, chaves, assinaturas e condições de histórico estejam sendo recalculadas para muitos candidatos.

O custo de `deepcopy` no caminho da loja é um candidato secundário.

`_flatten_masks()` tem custo comparativamente menor e não deve ser o primeiro alvo sem novos dados.

Esses resultados justificam investigar o fluxo antes de escolher a granularidade da migração. Eles não provam que uma implementação C++ específica será mais rápida ou comportamentalmente equivalente.

---