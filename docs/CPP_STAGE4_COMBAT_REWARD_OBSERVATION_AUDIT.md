# Auditoria — Etapa 4: Combate, recompensas e observações

Data: 2026-10-15  
Escopo: inspeção estática de `cpp/include/combat/*`, `cpp/src/combat/CombatEngine.cpp`, `cpp/src/lobby/TftEngine.cpp`, `lobby/TFTLobby.py`, `env.py` e `vector_lobby_env.py`.

**Conclusão geral: etapa parcialmente implementada; critério de conclusão ainda não atendido.** Esta é uma auditoria do código-fonte, não uma declaração de que a suíte foi compilada/executada.

## Checklist por tarefa

| Tarefa | Status | Evidência / lacuna |
|---|---|---|
| Converter unidades do estado C++ para CombatInput | Parcial | `append_combat_team()` converte unidades do tabuleiro em `CombatTeam/CombatUnit`. |
| Preservar atributos, posições, papéis e dados de combate | Parcial | Copia ID, nome, estrelas, papel inferido do perfil, posição, HP, AD, velocidade/alcance, armadura e resistência mágica. Não copia para a entrada montada pelo lobby a habilidade, itens, traits, AP, críticos, modificadores, mana e vários campos já existentes em `CombatUnit`; isso pode alterar combates. |
| Integrar CombatEngine à resolução das partidas | Implementado estruturalmente | `resolve_combats()` chama `combat_engine.simulate(input)` e rejeita resultado com `success=false` ou `completed=false`. Falta validar comportamento por testes executados. |
| Migrar pareamento dos oito jogadores | Parcial | Junta vivos, embaralha com RNG C++ e tenta evitar repetição. A equivalência exata com o pareamento Python e seu RNG não foi demonstrada. |
| Migrar controle de rodada, estágio e progressão | Parcial | Existem contadores e avanço de estágio/rodada no motor; paridade completa com a ordem da referência Python não foi provada. |
| Preservar vitória, derrota e empate | Parcial | Vitória/derrota atualiza contadores e streaks; empate pula recompensa de vitória/derrota. Necessita cenários determinísticos comparativos. |
| Aplicar dano, eliminações e ranking | Parcial | Há aplicação de dano por estágio e sobreviventes, eliminação, colocação e ranking. Deve-se comparar ordenação e dano exatos com Python, incluindo eliminações simultâneas. |
| Preservar ordem de processamento dos combates | Não comprovado | O C++ percorre os confrontos em sequência e elimina depois do loop; falta verificar se a referência Python aplica resultados na mesma ordem e com os mesmos efeitos colaterais. |
| Recompensas individuais e terminais | Parcial / lacuna crítica | Há componentes de recompensa de ação/estado e recompensa de combate. Não encontrei no caminho C++ equivalente explícito à recompensa terminal de colocação de `TFTLobby._calculate_placement_reward()` e `_apply_placement_rewards()`; precisa ser implementada ou a equivalência documentada. |
| Construir observações em C++ | Implementado, mas incompatível | `build_observations()` e `write_observation()` existem. |
| Preservar dimensão, índices, tipos e normalização das observações | **Não implementado** | C++ declara `kObservationDim = 8` e emite HP, ouro, nível, XP, alive, wins, losses e round sem normalização. Python `env._get_state()` concatena core=22, board=140, bench=45, shop=25, extra=5, synergy=5, positioning=4, trait_vector=`len(_trait_to_idx)` e capacity=2: dimensão total **248 + número de traits**. As escalas também são diferentes. |
| Preservar dados de estratégia e logging | Parcial | Há estrutura de estratégia, eventos de lobby e metadados públicos; a observação de 8 floats não carrega os dados que o vetor Python fornece ao PPO. |
| Tratar success/completed/timeout/erros | Parcial | `CombatResult` tem `success`, `completed`, `timeout` e campos de erro. O lobby trata falha/incompletude lançando exceção. Não encontrei validação de timeout como resultado específico nem política de retry/fallback comparável à Python. |
| Término da lobby e episódios individuais | Parcial | C++ termina com um jogador restante e marca colocações; `vector_lobby_env.py` define done individual por eliminação e marca todos done ao acabar a lobby. Falta contrato comparativo e recompensa terminal correspondente. |
| Testes de regressão de combate/dano/eliminações/ranking/recompensas | Parcial | Existem testes nativos e testes Python de combate/integracão, mas a cobertura cruzada de todas essas regras não foi demonstrada. |
| Comparar observações e recompensas em cenários controlados | Parcial | `tests/test_cross_language_replay.py` foi criado para replay da lobby, mas compara estado público e recompensas em cenário PASS; não compara o vetor de observação completo com o vetor Python. Não foi executado nesta auditoria. |

## Bloqueadores prioritários

1. **Observações do PPO:** alinhar a dimensão e a ordem do vetor C++ com `env._get_state()`, incluindo normalização e traits. Enquanto C++ emitir apenas 8 valores, não é equivalente ao estado de entrada do PPO Python.
2. **Entrada de combate incompleta:** completar o mapeamento de campos de unidade suportados pelo motor e definir quais campos ainda não existem no catálogo/instância. Adicionar teste de conversão de unidade.
3. **Recompensa terminal:** reproduzir o cálculo e a aplicação única da recompensa de colocação; testar eliminação e vitória final para evitar recompensa ausente ou duplicada.
4. **Paridade de rodada/combate:** fixtures determinísticas para vitória, derrota, empate, tabuleiro vazio, dano, eliminação simultânea, ranking e mudança de estágio.
5. **Teste de integração real:** comparar observações após cada etapa e cada recompensa individual, além de estado público. Falha de import do binding não deve ser confundida com teste aprovado.

## Próximo critério de aceite

A Etapa 4 só deve ser marcada concluída depois que:
- a dimensão C++ for igual à dimensão Python para o mesmo catálogo;
- cada índice do vetor tiver o mesmo significado, tipo e normalização;
- os campos de combate usados pelo motor forem transferidos de forma explícita;
- recompensas de ação, combate, economia e colocação forem comparadas após cada etapa;
- os cenários controlados Python/C++ e as suítes nativas/Python forem executados em CI, com resultados anexados ao PR/commit.
