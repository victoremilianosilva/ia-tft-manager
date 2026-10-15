# Auditoria — Etapa 4: Combate, recompensas e observações

Data: 2026-10-15  
Escopo: inspeção estática de `cpp/include/combat/*`, `cpp/src/combat/CombatEngine.cpp`, `cpp/src/lobby/TftEngine.cpp`, `lobby/TFTLobby.py`, `env.py` e `vector_lobby_env.py`.

**Conclusão geral: etapa parcialmente implementada; critério de conclusão ainda não atendido.** Esta é uma auditoria do código-fonte, não uma declaração de que a suíte foi compilada/executada.

## Checklist por tarefa

| Tarefa | Status | Evidência / lacuna |
|---|---|---|
| Converter unidades do estado C++ para CombatInput | Parcial | `append_combat_team()` converte unidades do tabuleiro em `CombatTeam/CombatUnit`; agora usa IDs sequenciais e o seed/configuração enviados pelo lobby Python. |
| Preservar atributos, posições, papéis e dados de combate | Parcial | Copia atributos básicos e alinha a orientação do time B com Python (espelha X), os IDs sequenciais e os fallbacks de HP/AD/AS/alcance. Habilidades, itens, traits, AP, críticos e modificadores não são preenchidos/consumidos pelo loop atual de combate; precisam de uma decisão de escopo e implementação própria. |
| Integrar CombatEngine à resolução das partidas | Implementado estruturalmente | `resolve_combats()` chama `combat_engine.simulate(input)` e rejeita resultado com `success=false` ou `completed=false`. Falta validar comportamento por testes executados. |
| Migrar pareamento dos oito jogadores | Parcial | Junta vivos, embaralha com RNG C++ e tenta evitar repetição. A equivalência exata com o pareamento Python e seu RNG não foi demonstrada. |
| Migrar controle de rodada, estágio e progressão | Parcial | Existem contadores e avanço de estágio/rodada no motor; paridade completa com a ordem da referência Python não foi provada. |
| Preservar vitória, derrota e empate | Parcial | Vitória/derrota atualiza contadores e streaks; empate pula recompensa de vitória/derrota. Necessita cenários determinísticos comparativos. |
| Aplicar dano, eliminações e ranking | Parcial | Há aplicação de dano por estágio e sobreviventes, eliminação, colocação e ranking. Deve-se comparar ordenação e dano exatos com Python, incluindo eliminações simultâneas. |
| Preservar ordem de processamento dos combates | Não comprovado | O C++ percorre os confrontos em sequência e elimina depois do loop; falta verificar se a referência Python aplica resultados na mesma ordem e com os mesmos efeitos colaterais. |
| Recompensas individuais e terminais | Parcial / lacuna crítica | Há componentes de recompensa de ação/estado e recompensa de combate. Não encontrei no caminho C++ equivalente explícito à recompensa terminal de colocação de `TFTLobby._calculate_placement_reward()` e `_apply_placement_rewards()`; precisa ser implementada ou a equivalência documentada. |
| Construir observações em C++ | Implementado estruturalmente | `build_observations()` agora emite o vetor concatenado com core, tabuleiro, banco, loja, extras, sinergias, posicionamento, traits e capacidade; dimensão dinâmica é devolvida pela API. |
| Preservar dimensão, índices, tipos e normalização das observações | Parcial; falta paridade total | O vetor C++ segue as dimensões/ordem e escalas de `env._get_state()` (248 + traits). Corrigido também o nome do método Python para chamar `evaluate_board_positioning()`. A comparação cruzada ainda exclui campos dependentes da seleção aleatória de unidade inicial/loja/traits; a dimensão e todos os valores ainda não foram comprovados em estado idêntico. |
| Preservar dados de estratégia e logging | Parcial | Há estrutura de estratégia, eventos de lobby e metadados públicos; a observação de 8 floats não carrega os dados que o vetor Python fornece ao PPO. |
| Tratar success/completed/timeout/erros | Parcial | `CombatResult` tem `success`, `completed`, `timeout` e campos de erro. O lobby trata falha/incompletude lançando exceção. Não encontrei validação de timeout como resultado específico nem política de retry/fallback comparável à Python. |
| Término da lobby e episódios individuais | Parcial | C++ termina com um jogador restante e marca colocações; `vector_lobby_env.py` define done individual por eliminação e marca todos done ao acabar a lobby. Falta contrato comparativo e recompensa terminal correspondente. |
| Testes de regressão de combate/dano/eliminações/ranking/recompensas | Parcial | Adicionado `cpp/tests/test_combat_engine.cpp` para vencedor determinístico, sobreviventes, replay, configuração inválida e timeout por limite de eventos. Dano de jogador, eliminação, ranking e recompensa terminal ainda precisam de cenário integrado. |
| Comparar observações e recompensas em cenários controlados | Parcial | `tests/test_cross_language_replay.py` foi criado para replay da lobby, mas compara estado público e recompensas em cenário PASS; não compara o vetor de observação completo com o vetor Python. Não foi executado nesta auditoria. |

## Bloqueadores prioritários

1. **Observações do PPO:** alinhar a dimensão e a ordem do vetor C++ com `env._get_state()`, incluindo normalização e traits. Enquanto C++ emitir apenas 8 valores, não é equivalente ao estado de entrada do PPO Python.
2. **Entrada de combate incompleta:** completar o mapeamento de campos de unidade suportados pelo motor e definir quais campos ainda não existem no catálogo/instância. Adicionar teste de conversão de unidade.
3. **Recompensa terminal:** reproduzir o cálculo e a aplicação única da recompensa de colocação; testar eliminação e vitória final para evitar recompensa ausente ou duplicada.
4. **Paridade de rodada/combate:** fixtures determinísticas para vitória, derrota, empate, tabuleiro vazio, dano, eliminação simultânea, ranking e mudança de estágio.
5. **Teste de integração real:** comparar observações após cada etapa e cada recompensa individual, além de estado público. Falha de import do binding não deve ser confundida com teste aprovado.

## Implementações adicionais realizadas durante a correção

- A lobby C++ agora cria uma unidade inicial de custo 1 no banco de cada jogador e desconta corretamente do pool, como `MiniTFTEnv.reset()`.
- Recompensa de colocação é aplicada uma única vez e preservada para jogadores eliminados e para o vencedor final.
- O agregado de recompensa após combate não recalcula a recompensa de estado nem aplica um segundo clamp ao total, aproximando-se do fluxo `env.step()` + `TFTLobby`.
- A orientação do time B, IDs das unidades, seed e parâmetros básicos de combate foram alinhados com `TFTLobby._build_cpp_combat_input()`.
- Criado workflow `.github/workflows/cpp-parity.yml` para compilar módulos/testes, executar CTest e executar o replay Python/C++.
- Corrigidos testes nativos de máscaras que usavam enum como índice de `std::array`, e fallback de máscaras que habilitava destinos impossíveis.

## Lacunas que permanecem

1. O RNG de loja, seleção da unidade inicial e pareamento não é compartilhado entre Python e C++; os estados aleatórios podem divergir com a mesma seed.
2. O replay atual compara apenas as features de observação independentes desses sorteios. Bench-role, loja, sinergias e vetor de traits são validados quanto a valores finitos/normalizados, mas ainda não comparados campo a campo em um estado idêntico.
3. Ainda não há fixture compartilhada com formação controlada para comparar uma vitória/derrota real, dano, eliminação, ranking e recompensa terminal.
4. Habilidades, itens, traits de combate e modificadores não são aplicados pelo loop atual de `CombatEngine`; o cabeçalho agora documenta essa limitação.
5. A suíte C++ e o replay cruzado passaram no workflow [C++ engine and cross-language parity](https://github.com/victoremilianosilva/teste-ia/actions/runs/38725932292), no commit `567d537`. O replay é limitado a ações PASS e compara os campos de observação independentes dos sorteios; ainda não prova paridade integral de combate/eliminação/recompensa terminal.

## Última execução de CI observada

- Build de módulos e executáveis nativos: **PASS**.
- CTest: **16/16 testes PASS**, incluindo o teste novo `test_combat_engine` e o soak test de combate/anti-loop.
- Replay Python/C++ `tests/test_cross_language_replay.py`: **PASS** para o cenário determinístico de três transições de rodada.
- O teste cruza recompensas por jogador, recompensa acumulada, dimensões e campos determinísticos de observação, estado público e metadados de rodada.
- Os campos dependentes do RNG da unidade inicial/loja/sinergias/traits são validados quanto a valores finitos e escala, mas ainda não são comparados entre os backends.

## Próximo critério de aceite

A Etapa 4 só deve ser marcada concluída depois que:
- a dimensão C++ for igual à dimensão Python para o mesmo catálogo;
- cada índice do vetor tiver o mesmo significado, tipo e normalização;
- os campos de combate usados pelo motor forem transferidos de forma explícita;
- recompensas de ação, combate, economia e colocação forem comparadas após cada etapa;
- os cenários controlados Python/C++ e as suítes nativas/Python forem executados em CI, com resultados anexados ao PR/commit.


## Atualização de verificação — 2026-10-15

- A reprodução cruzada foi tentada com uma ação real de mover unidade do banco para o tabuleiro. O teste revelou diferença de recompensa de posicionamento quando as unidades iniciais diferem entre backends: Python `-0.025`, C++ `0.125` no cenário observado. Isso é consequência conhecida da ausência de um estado inicial compartilhado/RNG compatível; não foi mascarado como paridade aprovada.
- O cenário de movimento foi retirado do replay de recompensas comparáveis até haver uma forma de injetar o mesmo snapshot inicial nos dois backends. Os testes de movimento de cada backend continuam sendo executados separadamente.
- O workflow agora usa `REQUIRE_CPP_PARITY=1`: falha se `tft_engine` ou `combat_engine` não puderem ser importados, em vez de marcar o replay como ignorado.
- A execução deve continuar sendo considerada parcial até que o mesmo estado inicial controlado possa ser reproduzido em Python/C++, incluindo identidade de unidades, loja, traits e papéis, e até que combate real e recompensa terminal sejam comparados em cenários integrados.


## Contrato de índices da observação (revisão)

O vetor público deve ser `float32` e possui `248 + N_traits` elementos. Os intervalos a validar contra `MiniTFTEnv._get_state()` são:

| Intervalo | Conteúdo | Dimensão |
|---|---|---:|
| `[0, 22)` | Core: HP, ouro, nível, XP relativo, streaks, progresso de rodada, ocupação e estratégia; os índices 17–21 são zeros reservados | 22 |
| `[22, 162)` | Tabuleiro: 28 slots × 5 features (ocupado, custo, estrela, papel, força) | 140 |
| `[162, 207)` | Banco: 9 slots × 5 features | 45 |
| `[207, 232)` | Loja: 5 slots × 5 features | 25 |
| `[232, 237)` | Extras: ocupação do tabuleiro/banco, ouro, nível e HP | 5 |
| `[237, 242)` | Cinco primeiras traits presentes, na ordem de inserção | 5 |
| `[242, 246)` | Score de posicionamento, proporção de frontline/backline e diversidade de papéis | 4 |
| `[246, 246 + N_traits)` | Vetor completo de traits na ordem fixa do catálogo | `N_traits` |
| `[246 + N_traits, 248 + N_traits)` | Capacidade livre do tabuleiro e do banco | 2 |

A dimensão/ordem está documentada e o replay agora verifica tipo e dimensão públicos. A igualdade de todos os valores ainda é parcial: RNG independente muda campeão inicial, loja, traits e papel derivado; esses campos não podem ser declarados equivalentes até os dois backends aceitarem o mesmo snapshot inicial.


## Instrumentação de recompensa

A API nativa agora expõe arrays separados `action_rewards`, `combat_rewards` e `placement_rewards`, além do agregado `rewards`. O replay cruzado compara cada componente por jogador e verifica que a soma dos componentes corresponde ao agregado. A lobby Python também expõe `action_reward` em `info.players` para auditoria. Isso torna omissões e duplicações detectáveis nos cenários executados; ainda falta um cenário controlado que efetivamente elimine jogadores para validar recompensa de colocação não nula em ambos os backends.


## Atualização após replay controlado — 2026-10-15

- O replay agora injeta a mesma identidade de campeão e a mesma formação de banco/tabuleiro nos dois motores por hooks explicitamente nomeados para testes. A loja continua fora da comparação campo a campo porque seus RNGs não compartilham o mesmo fluxo.
- O replay passa por uma luta PVP real entre duas equipes controladas, além de comparar recompensas totais e componentes separados de ação, combate e colocação, dimensões/tipo da observação, estado público e progressão de rodada.
- A comparação revelou e corrigiu dois desvios concretos: MiniTFTEnv._get_state() chamava PositioningManager.evaluate_board(), método inexistente, e convertia silenciosamente o score de posicionamento em zero; agora chama evaluate_board_positioning(). A observação C++ também retorna vetor todo-zero para jogador eliminado, como TFTLobby.get_observations().
- CI do replay controlado: build CMake, CTest 16/16 PASS, suítes Python selecionadas 108 passed, incluindo o replay controlado (execução https://github.com/victoremilianosilva/teste-ia/actions/runs/38747122129).
- Isso fecha um cenário de combate e recompensa real, mas NÃO prova paridade integral. Permanecem pendentes: igualdade do fluxo RNG de loja/pareamento, fixtures específicas para empate e eliminações simultâneas com ranking terminal, e validação de cada atributo de combate não consumido pelo loop atual (habilidades/itens/traits/modificadores). Não marcar a etapa inteira como concluída até esses casos terem fixtures explícitas.


## Auditoria complementar — StrategyManager.py (2026-10-15)

| Método/contrato Python | Estado C++ nesta branch | Validação |
|---|---|---|
| `decide_strategy()` | Regras prioritárias já reproduzidas por `TFTEngine::Impl::update_strategy()`; a estratégia escolhida permanece distinta da estratégia com maior score. | Replay cruzado existente. |
| `compute_strategy_confidence()` | Implementado como `StrategyInfo.state_confidence`, com os mesmos limiares e clamp [0, 1]. | Teste cruzado compara valor com o método Python após cada passo. |
| `get_strategy_score()` | Implementados os sete scores ECON, STABILIZE, FAST8, SLOWROLL, ALL_IN, WINSTREAK e LOSS_STREAK. | Teste cruzado compara cada score por ID com Python. |
| `choose_best_strategy()` | `best_scored_strategy` seleciona o score máximo; empate preserva a primeira estratégia na ordem do enum Python. Não substitui `decide_strategy()`. | Teste cruzado compara a estratégia vencedora por score. |
| `get_state()` | Snapshot exposto por `get_strategies()`, incluindo estratégia, anterior, confiança, idade, motivo, changed, scores e métricas de contexto. | Campos acessíveis pelo binding Python. |
| Contexto de `_update_strategy()` | C++ calcula board_power e bench_strength a partir das unidades possuídas; expõe quantidade de traits ativos do snapshot. A decisão Python atualmente recebe XP, round, bench_strength e composição, mas suas regras heurísticas não usam esses argumentos. | A força do banco e o comportamento de composição ainda precisam de fixtures específicas se a regra Python for ampliada. |

**Limite explícito:** isso fecha a paridade dos cálculos atualmente implementados em `StrategyManager.py`, não a migração integral de todos os managers chamados por `env.py`. A estratégia escolhida não deve ser confundida com `choose_best_strategy()`, que é um cálculo alternativo no código Python.


## Auditoria complementar — CompositionManager.py (2026-10-15)

| Método/estado Python | Implementação nativa | Validação |
|---|---|---|
| `rebuild_unit_counts()` / `count_unit()` | Contagem por ID interno, incluindo cópias equivalentes 1★=1, 2★=3, 3★=9; inclui tabuleiro e banco, exclui loja. | Replay cruzado compara `unit_counts_by_id` com `get_state()['unit_counts']`. |
| `get_active_traits()` | Contagem de traits das unidades próprias do tabuleiro e banco, preservando a ordem de inserção para desempates. | Comparação exata do dicionário de traits ativos. |
| `update_direction()` | Trait com maior contagem; empate preserva a primeira trait observada, como o `Counter` Python. | Comparação após cada passo do replay. |
| `update_focus()` / `_calculate_focus_score()` | Score por unidade usando estrelas, custo, número de traits e cópias equivalentes; foco usa ID interno como no Python. | Comparação de `composition_focus_id` após cada passo. |
| `update_core_units()` | Até três IDs internos com maior score, desempate estável pela ordem de primeira ocorrência. | Comparação do conjunto de IDs core. |
| `update_core_traits()` | Até três traits mais presentes, somente com contagem >= 2, com desempate estável. | Comparação exata do conjunto de traits core. |
| `get_unit_comp_score()` | API nativa `get_unit_comp_score(player_id, champion_api_name, star)`; replica bônus core, direção, traits core, estrelas e custo. | Testa todos os campeões do catálogo para estrelas 1/2/3, comparando com Python. |
| `is_core_unit()` / `is_core_trait()` | Consultas expostas no binding Python do motor nativo. | Comparação cruzada para campeões e traits do catálogo. |
| `get_state()` | Snapshot exposto por `get_strategies()`, com IDs internos e nomes legíveis separados. | Teste cruzado compara foco, direção, core units/traits, traits ativos e contagem de cópias. |

**Validação executada:** workflow [C++ engine and cross-language parity](https://github.com/victoremilianosilva/teste-ia/actions/runs/38760053429) aprovado: build nativo, CTest e regressões Python/C++ passaram.

**Limite explícito:** o estado de composição está integrado ao snapshot estratégico do lobby, não como uma classe C++ independente com a mesma forma de objeto do Python. As consultas públicas e os cálculos de estado são equivalentes; a API de score recebe o identificador `apiName` do campeão e estrelas, enquanto o Python recebe o dicionário da unidade.


## Auditoria complementar — PositioningManager.py (2026-10-15)

O novo cabeçalho `cpp/include/strategy/PositioningEngine.hpp` implementa a lógica de posicionamento como funções puras, sem alterar o estado real do tabuleiro. O binding `tft_engine` expõe as operações para os testes cruzados e a observação nativa reutiliza a mesma função `evaluate_board_positioning`, evitando manter uma segunda fórmula separada.

| Método Python | API C++ | Validação |
|---|---|---|
| `is_valid_position` | `positioning_is_valid_position` | posições válidas e limites |
| `position_to_row_col` / `row_col_to_position` | `positioning_position_to_row_col` / `positioning_row_col_to_position` | índices row-major do tabuleiro 4x7 |
| `get_neighbors` | `positioning_get_neighbors` | vizinhos ortogonais e diagonais |
| `evaluate_unit_placement` | `positioning_evaluate_unit_placement` | todas as roles em cada posição |
| `evaluate_protection` | `positioning_evaluate_protection` | vizinhos ocupados e tanks adjacentes |
| `evaluate_board_positioning` | `positioning_evaluate_board_positioning` | score completo, mesma fórmula e pesos |
| `find_best_position` | `positioning_find_best_position` | busca por posições vazias, sem mover unidade real |
| `find_best_swap` | `positioning_find_best_swap` | simulação temporária da troca e delta de score |
| `is_board_stable` | `positioning_is_board_stable` | limiar de melhoria padrão 0.01 |
| `get_normalized_positioning_score` | `positioning_get_normalized_score` | score dividido por quantidade de unidades × 10 e limitado a [-1, 1] |

A suíte `tests/test_positioning_parity.py` compara tabuleiros vazios, mistos e determinísticos; testa as cinco roles, vizinhos, fórmulas, busca de posição/troca e estabilidade. A execução é incluída no workflow `.github/workflows/cpp-parity.yml`.

**Limites de representação:** a API C++ recebe um vetor de 28 roles (com -1 para casa vazia), enquanto o Python recebe uma lista de dicionários de unidades. UUIDs não são necessários para as fórmulas de posicionamento; continuam relevantes para a assinatura do tabuleiro usada pelo anti-loop, que permanece separada. Valores de retorno sem posição são representados como -1 no C++ e devem ser convertidos para `None` na camada de integração.
