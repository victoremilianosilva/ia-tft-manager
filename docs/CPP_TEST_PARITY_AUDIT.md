# Auditoria de paridade Python ↔ C++

Data da auditoria: 2026-10-14

## Estado real

**A paridade completa ainda não está concluída.** A presença de testes C++ com nomes semelhantes não significa que os testes Python foram portados nem que as duas implementações recebem o mesmo estado e a mesma sequência de ações.

A pasta `tests/` contém 48 arquivos Python. A pasta `cpp/tests/` contém testes nativos para subconjuntos do motor. O teste `tests/test_reward_cpp_parity.py` compara fórmulas/valores de referência; ele **não** executa uma sequência real por `env.step` e pela API de `tft_engine`, nem compara snapshots completos de estado a cada ação.

## Inventário Python por área

| Área | Testes Python existentes | Estado da paridade |
|---|---|---|
| Contrato/dimensões de ações | `test_action_contract.py`, `test_action_dimensions.py`, `test_move_board_action_contract.py`, `test_move_board_execution.py` | Parcial: existem testes C++ de validação/máscara; falta replay cruzado de entradas e saídas. |
| Máscaras e condicionais | `test_action_mask_conditionals.py`, `test_action_mask_equivalence.py`, `test_action_mask_fallback.py`, `test_action_mask_integration.py`, `test_action_mask_validation.py`, `test_ppo_mask_consistency.py` | Parcial: cobertura C++ nativa existe; não está demonstrada a igualdade de máscaras para snapshots Python/C++. |
| Anti-loop e ciclos de posição | `test_anti_loop_mask_integration.py`, `test_anti_loop_position_cycles.py`, `test_anti_loop_regression.py`, `test_anti_loop_swap_back.py`, `test_anti_loop_swap_cycles.py`, `test_anti_loop_useful_moves_audit.py` | Parcial: há testes nativos anti-loop, mas falta executar as mesmas sequências e comparar cada máscara/estado. |
| Combate e integração Python→C++ | `test_combat_engine.py`, `test_combat_events.py`, `test_combat_movement.py`, `test_combat_profile_data.py`, `test_combat_stats.py`, `test_combat_timeout.py`, `test_determinismo_combate_cpp.py`, `test_empty_team_combat.py`, `test_integracao_combate_cpp.py`, `test_lobby_combat_regression.py` | O combate Python já chama o módulo C++; isso testa principalmente a fronteira/binding e o motor, não a paridade completa de recompensas/estado do lobby. |
| Recompensas/economia/rodadas | `test_combat_economy_integration.py`, `test_reward_cpp_parity.py`, `test_reward_integration.py`, `test_round_economy_combat_flow.py`, `test_self_play_economy.py`, `test_self_play_economy_progression.py` | Parcial e crítico: existem testes de fórmulas e integração isolada; falta replay de ações real, comparando recompensas intermediárias, total e estado após cada etapa. |
| Composição/posicionamento/estratégia | `test_composition_positioning.py`, `test_strategy_integration.py` | Parcial: alguns testes C++ cobrem snapshots/composição; falta comparação cruzada dos mesmos dados e desempates. |
| Ambiente/lobby/API/fluxo completo | `test_decision_state_adapter.py`, `test_environment_contracts.py`, `test_gameplay_validation.py`, `test_lobby_end_to_end.py`, `test_lobby_learning.py`, `test_manager_integration.py`, `test_tft_engine_api.py`, `test_self_play_full_match.py` | Não demonstrado: requer cenários determinísticos comparáveis, sem aleatoriedade externa não controlada. |
| Loja/pool/upgrade | `test_shared_pool_shop_validation.py`, `test_shop_manager_odds.py`, `test_shop_manager_performance.py`, `test_unit_pool_performance.py`, `test_unit_pool_regression.py`, `test_upgrade_integration.py` | Parcial: existem testes C++ de loja/pool/instância; falta mapear cada asserção Python e validar a mesma sequência/seed. |

## Testes C++ já presentes (não equivalem automaticamente a um port completo)

- `test_action_mask_engine.cpp`
- `test_anti_loop_engine.cpp`
- `test_decision_error.cpp`
- `test_economy_engine.cpp`
- `test_move_validator.cpp`
- `test_reward_model.cpp`
- `test_shop_engine.cpp`
- `test_synergy_counter.cpp`
- `test_tft_combat_anti_loop_soak.cpp`
- `test_tft_engine_pool.cpp`
- `test_unit_instance_factory.cpp`
- `test_unit_pool.cpp`

## Critérios obrigatórios para considerar a paridade concluída

1. Cada cenário compartilhado deve definir estado inicial, seed, ações ordenadas e configuração.
2. Executar o cenário no Python e no binding C++; não calcular manualmente o resultado esperado a partir da mesma fórmula testada.
3. Registrar após **cada ação**: ação normalizada, validade/erro, ouro, HP, XP/nível, loja/bench/tabuleiro, unidades/estrelas, traits/sinergias, máscaras, round/stage e cada componente de recompensa.
4. Comparar floats com tolerância explícita e valores discretos exatamente.
5. Separar divergências intencionais de bugs; cada exceção deve ter justificativa documentada.
6. Executar testes Python e C++ em CI e publicar resultados reais. Não marcar como aprovado se o módulo C++ não tiver sido compilado ou se os testes forem ignorados por falta de binding.

## Implementação inicial adicionada

- `tests/fixtures/cross_language_replay.json`: cenário compartilhado com três barreiras de rodada em que os oito jogadores executam PASS.
- `tests/test_cross_language_replay.py`: executa a sequência pela API real de `TFTLobby` Python e pelo binding `tft_engine`; compara após cada etapa round/stage/finished, HP/ouro/nível/XP/vida/vitórias/derrotas, recompensa por jogador, recompensa acumulada, conclusão da lobby e metadados da rodada. O teste verifica também finitude das recompensas e tamanho dos lotes.
- O teste procura o módulo nativo nos diretórios atuais e no diretório Release usado por builds Windows antigos.

Esse primeiro replay é intencionalmente conservador: não depende de comprar um campeão aleatório diferente em cada motor. **Ainda não cobre compra/upgrade/movimentação real, conteúdo de tabuleiro/banco/loja, máscaras campo a campo ou componentes internos separados da recompensa.** Para isso, a API nativa precisa expor snapshots equivalentes e os cenários precisam controlar a identidade das unidades, não apenas a seed.

## Próximo passo técnico

Expandir o contrato de snapshot compartilhado para expor loja, banco, tabuleiro, estrelas, sinergias e componentes de recompensa; permitir fixtures determinísticas com seleção de campeão controlada; então portar por cenário as asserções dos 48 testes Python. Executar build CMake, testes nativos e pytest no mesmo ambiente de CI e guardar os resultados reais.

## Limitação desta auditoria

Esta é uma auditoria estática dos arquivos e nomes dos testes disponíveis no repositório. Ela não afirma que a suíte completa foi executada. Nenhum resultado de compilação/teste é declarado aqui sem uma execução reproduzível.


## Atualização de trabalho — 2026-10-15

### CI e relatórios

A branch `audit/full-cross-language-parity` amplia `.github/workflows/cpp-parity.yml` para incluir grupos adicionais de regressão de máscaras, AntiLoop, economia, loja/pool, upgrades e seleção de backend. O workflow agora grava o log do CTest, produz JUnit XML para a suíte Python e publica ambos como artifact mesmo quando um passo falha.

A variável `REQUIRE_CPP_PARITY=1` continua obrigando a importação de `tft_engine` e `combat_engine` no teste de replay, para que ausência do binding nativo não seja tratada como sucesso por skip.

### Limites confirmados no código atual

- O hook `set_unit_for_testing` permite configurar unidades no tabuleiro/banco, mas não permite definir ofertas específicas da loja nem controlar diretamente ouro/XP/nível. Por isso, ele ainda não consegue criar fixtures completas e idênticas para BUY e REROLL.
- `get_public_state()` não expõe o conteúdo completo de tabuleiro, banco, loja ou estrelas das unidades. Não é suficiente para comparar todas as transições.
- O binding devolve as máscaras completas (incluindo matrizes condicionais), mas o replay atual não compara essas máscaras após cada ação.
- A economia RNG da loja e a RNG de matchmaking são streams separados em C++; no Python, a loja/pool usa seus próprios objetos RNG. Reutilizar somente o mesmo inteiro de seed não garante as mesmas ofertas ou pareamentos.
- `state_reward()` existe no motor nativo, mas o caminho ativo de recompensa da partida continua usando recompensa de ação, combate e colocação. A auditoria deve preservar esse contrato atual até haver decisão explícita de mudança.

### Próxima implementação necessária para as fixtures das sete ações

1. Adicionar hooks exclusivos de teste para configurar ouro/XP/nível e ofertas específicas da loja, com validação de slots e sem expor esses hooks ao Trainer.
2. Expor um snapshot de auditoria equivalente nos dois backends: identidade/API do campeão, estrelas, loja, banco, tabuleiro, economia, estado de pool necessário, máscaras e componentes de recompensa.
3. Adicionar replay de uma ação por fixture para BUY, REROLL, BUY_XP, MOVE_BENCH, MOVE_BOARD, SELL e PASS. Validar tanto ações válidas quanto inválidas; comparar valores discretos exatamente e floats com tolerância documentada.
4. Comparar as oito máscaras completas, inclusive `board_move_target_masks` e `bench_to_board_target_masks`, antes e depois de cada transição.
5. Só depois ampliar para cenários determinísticos de combate, eliminação/colocação, juros, streaks, pareamento e mudanças de estágio.

**Status:** a mudança de CI está preparada nesta branch; ainda não foi executada aqui, e a paridade de transições completas permanece pendente. Não declarar o grupo aprovado até o GitHub Actions fornecer resultados reais.


### Atualização da implementação — snapshots e máscaras

A branch agora contém:

- `TFTEngine::get_audit_snapshot()` e binding Python `get_audit_snapshot()`, com round/stage, ouro/nível/XP/streaks, unidades por slot (campeão, UUID, estrelas e custo), ofertas da loja e todas as máscaras nomeadas.
- O replay cruzado compara todas as oito máscaras de cada jogador após reset e após cada transição: vetores de tipo/loja/origens/destinos e matrizes condicionais `28x28` e `9x28`.
- O replay compara slots do tabuleiro/banco, estrelas, custo e estado econômico com o snapshot nativo após cada etapa. UUIDs não são comparados porque são gerados por RNGs independentes.
- As ofertas da loja estão disponíveis no snapshot para diagnóstico, mas a comparação de conteúdo da loja ainda não é assertiva: os motores usam streams de RNG independentes. Para fechar isso, ainda falta o hook de fixture que injeta a mesma oferta nos dois backends e mantém o pool coerente.

O CI deve compilar a nova API e executar esses testes. Até o término da execução, a implementação está **adicionada, mas não validada por build/testes**.
