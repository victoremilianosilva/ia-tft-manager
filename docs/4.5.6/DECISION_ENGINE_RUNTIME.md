# Decision Engine Runtime — Etapa D.1

## Objetivo

Integrar o motor nativo C++ ao ambiente Python, preservando o comportamento existente quando o backend Python estiver selecionado.

## Arquivos envolvidos

- `ai/DecisionEngineRuntime.py`
- `ai/ActionMaskManager.py`
- `env.py`

## Seleção do backend

A seleção é feita pela variável de ambiente `TFT_DECISION_ENGINE`.

- `python`: mantém o caminho original do `ActionMaskManager`.
- `cpp`: utiliza `ActionMaskEngine` e `AntiLoopEngine` nativos.

O backend Python continua sendo o padrão. Se o backend C++ for solicitado e não puder ser carregado, a inicialização deve informar o erro, sem fallback silencioso.

## Sincronização do histórico

O runtime nativo é reiniciado junto com o histórico anti-loop Python.

Movimentos são sincronizados somente depois que o ambiente executa o movimento com sucesso. O estado é sincronizado depois do registro do estado Python.

A geração de máscaras é uma consulta e não deve alterar o histórico anti-loop.

## Contrato das máscaras

O runtime retorna seis máscaras, na ordem utilizada pela política:

1. `type_mask`: 7 posições.
2. `shop_mask`: 5 posições.
3. `bench_mask`: 9 posições.
4. `board_target_mask`: 28 posições.
5. `board_source_mask`: 28 posições.
6. `conditioned_target_mask`: 28 posições.

As máscaras usam `numpy.float32`, preservando o formato esperado pela implementação Python.

Os fallbacks técnicos devem continuar distintos da disponibilidade real de uma ação. Em particular, o fallback `[0]` de uma máscara não pode, por si só, habilitar um tipo de ação.

## Regra de compatibilidade

O comportamento Python é a referência. Esta integração não deve alterar regras de compra, economia, movimento, anti-loop ou recompensa para se adequar ao C++.

Qualquer divergência deve ser corrigida na implementação C++ ou na camada de integração. Mudanças intencionais de regra devem ser tratadas em uma etapa independente.

## Validação

Executar primeiro os testes existentes do adaptador e da equivalência de máscaras:

```bash
python -m pytest tests/test_decision_state_adapter.py -v
python -m pytest tests/test_action_mask_equivalence.py -v
```

Depois, executar a suíte completa com o backend Python e com o backend C++ em processos separados.

O teste de equivalência deve confirmar não apenas dimensões e fallbacks, mas também estados com histórico anti-loop, movimentos reversos, trocas e movimentos entre banco e tabuleiro.

Esta etapa só pode ser considerada concluída depois que os testes forem executados e os resultados forem revisados.