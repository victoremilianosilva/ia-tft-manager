# PR 4 — Compra, venda, posicionamento e consumidores do Engine

## Problema anterior

A geração de candidatos e os owners nativos já existem, mas a integração ainda precisa provar que decisões de compra/venda e propostas físicas de posicionamento usam os mesmos snapshots, identidade de unidade, lineup e versão de composição. Há também consumidores no Engine que calculam métricas de composição durante o ciclo de ação e precisam ser classificados entre decisão, legalidade e reward histórico para não remover dependências PPO por acidente.

As projeções econômicas de renda futura, dano recebido e risco de eliminação permanecem indisponíveis no contexto integrado. A presença de fórmulas de dano de rodada e de um simulador determinístico não basta, isoladamente, para declarar previsão confiável.

## Racional técnico

- UnitPriorityPlanner é a autoridade de prioridade, cópias físicas por tier, progresso de upgrade e restrições de venda.
- LineupPlanner é a autoridade da seleção de unidades possuídas para o board atual, incluindo capacidade, bridge, entradas, saídas e alvos adiados.
- ContextualActionEvaluator avalia candidatos contra HOLD com custos econômicos e evidências disponíveis.
- StrategicPositionPlanner propõe destino físico; StrategicActionExecutor revalida identidade, sequência, estado físico e masks.
- BoardEvaluation do #509 é reutilizado; nenhuma segunda avaliação de tabuleiro deve ser criada.
- PPO continua sendo o algoritmo de decisão. Engine/masks continuam sendo a autoridade de legalidade.
- CombatEngine documenta limitações de modelagem (scripts específicos de campeões, buffs/debuffs, traits e passivas únicas ainda incompletos). Resultados desse simulador não podem ser rotulados como dano esperado calibrado sem validação de cobertura e calibração.
- EconomyEngine contém regras determinísticas de renda base, juros e XP de rodada. Componentes condicionais a resultados de combate (streak e crédito de vitória) devem ser separados de componentes determinísticos e não apresentados como garantidos.

## Novas responsabilidades e contratos

1. Compra: comparar cada oferta e upgrade com o estado-base/HOLD usando prioridade nativa, composição ativa, custo direto, liquidez e juros válidos; não usar StrategyInfo.
2. Venda: proteger unidades com base em UnitPriority, cópias físicas, progresso de upgrade, itens e LineupPlan; uma ausência de prioridade válida não autoriza vender.
3. Lineup e posicionamento: somente unidades selecionadas no LineupPlan podem ser promovidas como alvo de deploy/move. A proposta deve carregar match/player/round/sequence, composition ID/version, unidade física (UUID), origem e destino. Qualquer divergência ou dado stale deve falhar fechado.
4. Executor: resolver somente a proposta associada ao candidato contextual selecionado, revalidando UUID, slot, champion, composição, lineup, sequência, destino vazio e masks atuais. A resolução continua Shadow/read-only.
5. Economia:
   - Renda determinística: projetar apenas componentes calculáveis a partir do EconomyEngine e do snapshot atual, com separação entre base/juros observados e bônus condicionais de streak/vitória.
   - Dano: não inferir dano esperado a partir apenas de stage_damage ou de uma simulação incompleta. Um produtor só pode ser promovido se o matchup, entradas de combate, cobertura do modelo e horizonte forem válidos e auditáveis.
   - Eliminação: não emitir probabilidade sem modelo calibrado. Se houver apenas HP atual e dano máximo condicional conhecido, publicar exposição/limite condicional com nome e contrato próprios, não elimination_risk.
   - Cada projeção deve ter source, source round, expected round, horizon, validity/quality, uncertainty e distinção observado/derivado/estimado. Ausência permanece unavailable/null.
6. Remoção de unit_composition_score: retirar somente dos caminhos de decisão Engine que ainda reconstruam composição antiga. Não alterar reward/observations/PPO ou contratos de checkpoint neste PR.

## Impactos

- Os consumidores decisórios de compra/venda/posicionamento passam a depender dos owners nativos e de snapshots coerentes.
- Diagnósticos podem ganhar campos de identidade do lineup e projeções econômicas por componente, sem promover defaults a fatos.
- Nenhuma mudança de dimensão/ordem PPO, reward, checkpoint, máscara, regra ou execução real é permitida.

## Critérios de validação

- Compra por substituição, upgrade e custo marginal contra HOLD.
- Venda de unidade protegida por lineup, pares/cópias, upgrade e itens.
- Entrada/saída do lineup, bridge, unidade adiada e limite de capacidade.
- Integração priorities → lineup → contextual recommendation → position proposal → executor resolution.
- Rejeição de UUID substituído, origem/destino inválidos, destino ocupado, lineup/composição stale e sequence/version divergentes.
- Ausência de consumidores Shadow em StrategyInfo/planned_units.
- Projeção de renda com componentes determinísticos e condicionais separados.
- Dano/eliminação: cenários com produtor válido, modelo incompleto, ausência de matchup, HP extremo e incerteza; nenhum valor artificial tratado como previsão.
- Regressões provam PPO/rewards/observations/checkpoints inalterados e masks/Engine como autoridade de legalidade.
