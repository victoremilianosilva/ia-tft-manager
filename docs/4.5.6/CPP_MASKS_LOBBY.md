# Máscaras de ação da lobby — backend C++

## Objetivo

Quando `TFT_DECISION_ENGINE=cpp`, todas as máscaras de ação devem ser geradas pelo `ActionMaskEngine` nativo. A lobby não deve chamar os geradores de máscara do `ActionMaskManager` Python.

## Fluxo C++

1. A lobby obtém o runtime do jogador.
2. O `DecisionStateAdapter` converte o estado atual para `PlayerState`.
3. `ActionMaskEngine.generate_masks()` gera o lote nativo completo.
4. A lobby converte os arrays nativos para o formato consumido pelo PPO.
5. As matrizes condicionadas de movimento são entregues junto das máscaras gerais.

O jogador eliminado também passa pelo motor nativo, com `is_alive=False`.

## Compatibilidade

O argumento `include_board_target` permite preservar o contrato da lobby. Quando desabilitado, o C++ não preenche a máscara geral de destinos com posições reais, mas continua calculando as matrizes condicionadas do banco.

O backend Python permanece inalterado e continua sendo o padrão.

## Validação obrigatória

- Recompilar a extensão C++ após a mudança de assinatura.
- Executar os testes de equivalência das máscaras.
- Executar os testes de integração da lobby.
- Executar os benchmarks com ambos os backends.
- Confirmar que o caminho C++ não chama `get_board_move_masks()`, `get_bench_move_masks()` ou o gerador Python de máscaras da lobby.
- Confirmar que jogadores eliminados recebem apenas `PASS` como tipo de ação válido.

Não alterar o backend padrão antes de validar equivalência e desempenho.
