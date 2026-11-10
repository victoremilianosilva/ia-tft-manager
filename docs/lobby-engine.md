# Engine de lobby

## Ponto de entrada

A API central é `tft::TFTEngine`, declarada em `cpp/include/lobby/TftEngine.hpp` e implementada em `cpp/src/lobby/TftEngine.cpp`. Ela mantém o estado completo de uma lobby de oito jogadores e coordena subsistemas especializados.

Operações públicas relevantes:

- `reset(seed)`: inicia/reinicia um episódio e retorna observações, máscaras e identificador do episódio.
- `step(actions)`: recebe uma ação por vaga e retorna observações, recompensas, componentes de recompensa, dones, máscaras, jogadores, rodada/estágio e eventos.
- `get_action_masks()`, `get_public_state()`, `get_audit_snapshot()`: consultas de decisão, estado público e auditoria.
- Consultas de estoque, estratégias, estado de recompensa e métricas anti-loop: interfaces auxiliares para treino e diagnóstico.

## Subsistemas coordenados

- `ChampionCatalog`: definições estáticas dos campeões.
- `UnitInstanceFactory`: cria cópias com identidade própria.
- `UnitPool` e `ShopEngine`: disponibilidade global e ofertas individuais.
- `EconomyEngine`: ouro, XP, nível, juros e sequências.
- Camada de decisão: validação, máscaras e anti-loop.
- Camada de estratégia: contadores de sinergia e avaliação de posicionamento.
- Camada de combate e recompensa: resolve confrontos e produz sinais de retorno.

## Estado e resultados

`PublicState` representa informações de partida/jogadores que podem ser consumidas pela interface. `AuditSnapshot` expõe detalhes de tabuleiro, banco, loja e máscaras para depuração. São contratos diferentes: não presumir que todos os detalhes do snapshot de auditoria fazem parte da observação de treinamento.

`StepResult` mantém recompensas totais e seus componentes (`action_rewards`, `combat_rewards`, `placement_rewards`) separados, além de `dones` individuais e `lobby_done`.

## Determinismo e testes

A engine recebe seed e contém hooks `*_for_testing` para fixtures controladas de unidade, economia, loja e vida do jogador. Esses hooks são para testes de paridade, não para fluxo normal de jogo. Testes relevantes incluem `cpp/tests/test_tft_engine_pool.cpp`, `test_tft_combat_anti_loop_soak.cpp` e testes de lobby Python em `tests/`.

Veja também: [economia e loja](economy-shop.md), [decisões](decisions-masks-antiloop.md), [build/testes](build-and-tests.md).
