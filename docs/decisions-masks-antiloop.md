# Decisões, validação, máscaras e anti-loop

## Contrato da ação

A policy emite seis inteiros: `type, shop_slot, bench_slot, board_target, board_source, board_move_target`. Os tipos estáveis são definidos em `engine_contracts.py` e em `cpp/include/decision/DecisionTypes.hpp`:

| ID | Ação | Componentes usados |
|---:|---|---|
| 0 | BUY | `shop_slot` |
| 1 | REROLL | tipo |
| 2 | BUY_XP | tipo |
| 3 | MOVE_BENCH | `bench_slot`, `board_target` |
| 4 | MOVE_BOARD | `board_source`, `board_move_target` |
| 5 | SELL | `bench_slot` |
| 6 | PASS | tipo |

Dimensões das cabeças: `[7, 5, 9, 28, 28, 28]`. A interpretação de componentes depende do tipo da ação; eles não são seis escolhas independentes.

## Validação

`MoveValidator` valida índices, ocupação e semântica do movimento: mover dentro do tabuleiro pode resultar em movimento para espaço vazio ou troca com unidade ocupante; mover do banco para o tabuleiro implanta ou substitui, devolvendo a unidade substituída ao slot de banco conforme as regras implementadas. A política anti-loop é uma etapa separada da validação estrutural.

`DecisionEngine`, `DecisionState`, `DecisionResult` e `DecisionError` definem contratos de estado/resultado/erro da camada de decisão. `ActionMaskEngine` calcula máscaras sem registrar movimentos ou alterar o histórico anti-loop.

## Máscaras

- `type_mask`: tipos de ação disponíveis.
- `shop_mask`: ofertas compráveis.
- `bench_source_mask`: slots válidos para venda/origem conforme o consumidor.
- `board_target_mask`, `board_source_mask`: posições do tabuleiro.
- `board_move_target_masks[source][target]`: destinos válidos condicionados à origem.
- `bench_to_board_target_masks[source][target]`: destino válido para cada slot do banco.
- Máscaras de fallback garantem uma distribuição categórica válida; disponibilidade real de ação é representada separadamente.

A policy aplica as máscaras durante a amostragem e a avaliação de log-probability. Ao treinar, o rollout precisa guardar as mesmas máscaras usadas na decisão; usar máscaras diferentes no update quebra a consistência matemática do PPO.

## Anti-loop

`AntiLoopEngine` mantém assinaturas de posições, histórico de movimentos e bloqueios limitados. Ele identifica inversões imediatas, oscilações, ciclos e padrões banco↔tabuleiro; pode fornecer motivo do bloqueio e risco estimado. Métricas de execução devem ser incrementadas no fluxo real de execução, não durante a simples geração de máscaras.

Testes: `cpp/tests/test_action_mask_engine.cpp`, `test_anti_loop_engine.cpp`, `test_move_validator.cpp`, `test_decision_error.cpp`, além dos testes Python de consistência de máscaras e dimensões.
