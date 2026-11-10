# Strategic Planner — auditoria de INSUFFICIENT_EVIDENCE

## Objetivo

Instrumentar, em shadow mode, cada ocorrência de `INSUFFICIENT_EVIDENCE` e explicar separadamente:

1. ausência de direção atual ou de âncora utilizável;
2. candidatos não gerados devido aos filtros do `TftEngine.cpp`;
3. candidatos gerados, mas rejeitados pelo avaliador;
4. alternativa válida encontrada, porém com vantagem abaixo do mínimo de `ADAPT`;
5. direção atual inviável.

A instrumentação é observacional. Não muda decisões, thresholds, histerese, PPO, recompensas, observações, máscaras ou ações.

## Evidência de referência

Auditoria `match-20261110-073956-aa5d7664`:

- 1.753 registros estratégicos;
- 1.534 `INSUFFICIENT_EVIDENCE`;
- 684 registros com candidato/âncora e confiança da âncora em 0,950;
- 850 registros sem candidato/âncora utilizável.

O valor 0,950 é a confiança heurística da âncora, derivada do score dela. Não é probabilidade calibrada e não descreve a confiança da composição atual.

## Instrumentação implementada

### Por avaliação do Strategic Planner

Os campos são transportados por `StrategicPlanDecision`, `StrategyInfo`, binding Python e `shadow_planning` nos logs do Viewer:

- `decision_path_reason`: caminho específico da decisão;
- `current_direction_score`: score usado para a direção atual;
- `best_anchor_score`: score da melhor âncora válida;
- `alternative_advantage`: score da âncora menos score da direção atual;
- `minimum_adapt_advantage`: limite mínimo para considerar ADAPT;
- `required_pivot_advantage`: limite absoluto/relativo usado para completar PIVOT;
- `anchor_confidence`: confiança heurística da âncora;
- `current_direction_confidence`: transformação do score da direção atual, separada da âncora;
- `current_direction_viable` e `has_anchor_candidate`.

As duas confianças são derivadas de score e explicitamente não calibradas. Quando não há direção atual, `current_direction_confidence` é zero.

### Geração de candidatos em TftEngine.cpp

Contadores exportados:

- anchors/unidades de alto custo examinados;
- rejeições por custo abaixo de 4;
- trait vazio;
- direção duplicada;
- limite de duas direções;
- plano alternativo vazio;
- âncora ausente do plano;
- candidatos efetivamente gerados.

`candidate_generation_reason` classifica o resultado da geração, por exemplo `no_high_cost_anchor_units_seen`, `no_cost_four_or_five_anchor`, `composition_planner_returned_empty_plan`, `anchor_not_in_generated_plan`, `no_new_eligible_anchor_trait` ou `candidate_generated`.

### Caminhos do Planner

Os caminhos instrumentados incluem:

- `no_initial_anchor_available`;
- `current_direction_unviable_without_alternative`;
- motivo da geração quando não há candidato para direção ativa viável;
- `all_anchor_candidates_rejected`;
- `best_anchor_matches_current_direction`;
- `alternative_below_minimum_adapt_advantage`;
- `alternative_below_required_advantage` e `alternative_waiting_for_persistence` (ADAPT);
- `current_direction_not_viable`;
- `pivot_thresholds_and_persistence_satisfied`.

O Viewer exibe contagens agregadas por motivo, filtros da geração e amostras com score, vantagem, limites e confianças. O relatório Markdown `audit_estrategia.md` inclui uma tabela dedicada a cada ocorrência registrada de `INSUFFICIENT_EVIDENCE`.

## Interpretação e limitações

- Snapshots emitidos após ações podem repetir a mesma revisão do Planner; não devem ser tratados como revisões independentes.
- Contadores de geração descrevem filtros observados no caminho nativo; não provam que uma composição alternativa seria competitiva.
- Scores e confianças são heurísticos, não probabilidades ou garantias de resultado.
- Sessões antigas sem esses campos continuam compatíveis: valores ausentes permanecem indisponíveis, não são convertidos em zero como se fossem medições.

## Testes

- Testes C++ cobrem o caminho de vantagem abaixo do mínimo, a separação das confianças e o caso de direção inviável sem alternativa.
- Testes Python cobrem persistência dos campos no snapshot do Viewer.
- Testes da auditoria cobrem agregação por motivo e presença dos diagnósticos no Markdown.

## Restrições e dependências

- Shadow/auditoria somente.
- Este PR não corrige a semântica KEEP versus INSUFFICIENT_EVIDENCE.
- Não altera thresholds, persistência, histerese, `CompositionDirectionPolicy` ou `CompositionPlanner`.
- A Issue #192 continua bloqueando ativação do Strategic Planner no PPO.
- A Issue #196 continua sendo o débito técnico para revisão da confiança e persistência após coleta de evidências.

## Critério de conclusão

Uma nova partida gravada com o binding nativo atualizado deve permitir explicar cada ocorrência de `INSUFFICIENT_EVIDENCE` com caminho, score atual, score da âncora, vantagem, limites, motivo de geração e confiança de cada lado. A correção semântica de KEEP deve ser avaliada somente depois dessa coleta e em mudança comportamental separada.
