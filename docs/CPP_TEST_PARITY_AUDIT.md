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

## Próximo passo técnico

Criar um formato de fixture compartilhado (JSON) e um replay determinístico de ações. O lado Python exporta snapshots e recompensas; o lado C++ executa a mesma sequência e exporta os próprios snapshots; um comparador aponta o primeiro campo divergente. Começar por recompensa/compra-posicionamento e, em seguida, máscaras, sinergias, composição e fluxo de rodada/combate.

## Limitação desta auditoria

Esta é uma auditoria estática dos arquivos e nomes dos testes disponíveis no repositório. Ela não afirma que a suíte completa foi executada. Nenhum resultado de compilação/teste é declarado aqui sem uma execução reproduzível.
