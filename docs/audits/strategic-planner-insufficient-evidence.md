# Strategic Planner — auditoria de INSUFFICIENT_EVIDENCE

## Objetivo

Instrumentar, em shadow mode, as decisões `INSUFFICIENT_EVIDENCE` para separar:

1. ausência real de evidência para avaliar uma direção;
2. ausência de candidatos porque a geração/filtros não produziram anchors;
3. alternativa válida encontrada, mas sem vantagem suficiente para justificar adaptação;
4. direção atual inviável sem alternativa utilizável.

Este trabalho é exclusivamente observacional. Não altera a decisão retornada, thresholds, histerese, compromisso estratégico, PPO, recompensas, observações, máscaras ou ações executadas.

## Evidência de referência

Auditoria da partida `match-20261110-073956-aa5d7664`:

- 1.753 registros estratégicos.
- 1.534 registros `INSUFFICIENT_EVIDENCE`.
- 684 registros tinham candidato selecionado, âncora válida e confiança reportada de 0,950.
- Nos 684 registros, a direção ativa e a direção alvo eram iguais; o motivo exportado era `insufficient_evidence`.
- 850 registros não apresentavam candidato/âncora utilizável.

A confiança de 0,950 é derivada da pontuação da âncora no `StrategicPlanner::best_anchor`; ela não representa probabilidade calibrada de que a composição atual seja correta. Portanto, não deve ser interpretada como confiança na direção atual.

## Hipótese a validar

Em `cpp/include/strategy/StrategicPlanner.hpp`, quando a melhor âncora aponta para outra direção, mas a vantagem é inferior a `minimum_adapt_advantage`, o código define `reason = InsufficientEvidence` e retorna sem alterar o valor inicial de `composition_decision`, que também é `InsufficientEvidence`.

Esse caminho pode representar semanticamente “alternativa avaliada, vantagem insuficiente para adaptar”, e não necessariamente “não há evidência para continuar”. A auditoria deve confirmar a frequência e os valores desse caminho antes de qualquer correção de semântica.

Também existe um caminho distinto em `TftEngine.cpp` que limita a geração de anchors por custo, traits/direções avaliadas e sucesso de `CompositionPlanner::build`. A ausência de candidatos não prova, por si só, que não havia alternativa estratégica possível.

## Contrato de instrumentação proposto

Adicionar diagnósticos somente de leitura ao resultado shadow e exportá-los pelo binding Python e pelos logs do Viewer.

### Campos por avaliação

- `current_direction`
- `current_direction_viable`
- `current_direction_score`
- `best_candidate_direction`
- `best_candidate_champion_id`
- `best_candidate_score`
- `candidate_confidence` (explicitamente identificada como confiança da âncora, não da direção atual)
- `advantage` = score da melhor alternativa menos score da direção atual
- `minimum_adapt_advantage`
- `required_advantage` (limite absoluto/relativo usado para a decisão)
- `composition_locked`
- `decision_path` / `insufficient_evidence_reason`

### Contadores de geração de candidatos

Registrar contagens separadas para:

- anchors examinados;
- descartados por custo abaixo do mínimo;
- descartados por direção/trait vazio ou repetido;
- descartados porque o plano alternativo não foi construído ou não incluiu a unidade-âncora;
- candidatos construídos;
- candidatos enviados ao Strategic Planner.

Não colapsar essas causas em uma única contagem de “sem candidato”. Se algum filtro não puder ser observado sem refatoração invasiva, registrar como não instrumentado em vez de inferir zero.

### Classificação analítica

Os relatórios devem distinguir pelo menos:

- `NO_CURRENT_DIRECTION`
- `NO_GENERATED_CANDIDATE`
- `ALL_CANDIDATES_INVALID`
- `ALTERNATIVE_BELOW_MINIMUM_ADAPT_ADVANTAGE`
- `ALTERNATIVE_BELOW_REQUIRED_ADVANTAGE`
- `CURRENT_DIRECTION_UNVIABLE_NO_ALTERNATIVE`
- `OTHER`

A classificação é diagnóstica; não deve mudar `CompositionDecision` nem `StrategicReason` nesta etapa.

## Testes necessários

1. Direção atual viável, sem candidatos: classificar como ausência de candidato; manter a decisão existente.
2. Direção atual viável, alternativa válida na mesma direção: registrar âncora e caminho KEEP atual.
3. Direção atual viável, alternativa de outra direção com vantagem abaixo de `minimum_adapt_advantage`: registrar score, vantagem, limite e caminho correspondente sem mudar a decisão.
4. Alternativa acima do mínimo de adaptação, mas abaixo do limite absoluto/relativo: registrar o limite e manter ADAPT.
5. Direção atual inviável sem alternativa: distinguir esse caso de falta genérica de candidatos.
6. Dados numéricos inválidos: registrar descarte sem contaminar scores/limites.
7. Binding e Viewer: preservar os campos novos e manter compatibilidade com sessões antigas sem esses campos.

## Restrições e dependências

- Shadow/auditoria somente.
- Não corrigir KEEP versus INSUFFICIENT_EVIDENCE neste PR.
- Não alterar thresholds, persistência ou histerese.
- Não alterar `CompositionDirectionPolicy` ou `CompositionPlanner`.
- A revisão arquitetural da [Issue #192](https://github.com/victoremilianosilva/ia-tft-manager/issues/192) continua obrigatória antes de ativação no PPO.
- Consolidar os resultados de confiança e persistência na [Issue #196](https://github.com/victoremilianosilva/ia-tft-manager/issues/196).

## Critério de conclusão da auditoria

Uma nova partida deve permitir explicar cada ocorrência de `INSUFFICIENT_EVIDENCE` com o caminho percorrido, scores, limites e motivo da geração/ausência de candidatos. Só depois dessa coleta deve ser proposta uma alteração semântica de KEEP, em PR separado.
