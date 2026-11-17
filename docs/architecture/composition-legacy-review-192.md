# Revisão arquitetural: CompositionDirectionPolicy e CompositionPlanner

Issue: #192  
Escopo desta revisão: inspeção estática do código atual, sem refatoração, remoção de legado ou alteração de comportamento.

## Resumo executivo

Os dois componentes legados têm responsabilidades diferentes e não devem ser tratados como uma única peça:

- `CompositionDirectionPolicy` mantém a direção ativa e aplica histerese/lock para aceitar ou rejeitar mudanças de direção.
- `CompositionPlanner` constrói uma composição-alvo concreta a partir da direção, foco, unidades próprias, loja, pool, nível, itens e disponibilidade estimada.

A arquitetura nova introduz pelo menos dois estados adicionais que precisam ser distinguidos:
- `StrategicPlanner` mantém um `StrategicCommitment` próprio para avaliar KEEP/ADAPT/PIVOT em Shadow Mode.
- `ActiveCompositionManager` mantém um snapshot versionado de composição, enquanto `UnifiedStrategicShadowRuntime` mantém o ciclo unificado de direção/pivot e sua auditoria.

**Conclusão:** ainda não há evidência suficiente para remover ou substituir os componentes legados. Há sobreposição conceitual em torno de direção/composição, mas não equivalência funcional. A direção legada ainda participa do fluxo efetivo da engine; o Strategic Planner permanece diagnóstico/Shadow. O próximo passo seguro é explicitar a autoridade de cada estado e o contrato de sincronização antes de qualquer migração.

## 1. Responsabilidades observadas no código

### 1.1 CompositionDirectionPolicy

Arquivo: `cpp/include/strategy/CompositionDirectionPolicy.hpp`

Responsabilidades implementadas:
- inicializar uma direção quando ainda não existe;
- preservar direção existente quando não há candidato utilizável;
- manter direção quando o candidato coincide com ela;
- permitir mudança imediata quando a direção não está locked;
- exigir vantagem absoluta e relativa mínimas quando locked;
- exigir persistência por múltiplas atualizações;
- liberar lock em condições de inviabilidade ou emergência;
- registrar motivo, direção anterior e contador de mudanças.

Configuração padrão observada: vantagem relativa 0.20, absoluta 0.75 e três atualizações consecutivas.

Uso efetivo: `cpp/src/lobby/TftEngine.cpp`, dentro de `update_strategy`. A engine hidrata `CompositionDirectionState` a partir de `StrategyInfo`, chama `direction_policy.update(...)` e copia o resultado de volta para `info.composition_direction`, lock, candidato, streak e diagnósticos.

Isso significa que a política não é apenas um helper histórico: ela ainda participa da manutenção da direção consumida pelo fluxo legado da engine.

### 1.2 CompositionPlanner

Arquivo: `cpp/include/strategy/CompositionPlanner.hpp`

Responsabilidades implementadas:
- produzir uma lineup-alvo concreta ancorada em uma direção;
- selecionar carry e unidades de apoio;
- considerar traits/focus, cópias próprias, nível, ofertas atuais e disponibilidade do pool;
- estimar oportunidade de aquisição e aplicar penalidades quando unidades são difíceis de obter;
- considerar contexto de itens/unidades já posicionadas;
- reter uma composição anterior quando a nova alternativa não supera os critérios de substituição;
- expor snapshot nativo e notas de aquisição para diagnóstico/comparação.

Uso efetivo em `TftEngine.cpp`:
- constrói o plano da composição ativa a partir de `info.composition_direction` e grava unidades/traits/carry planejados em `StrategyInfo`;
- também é reutilizado para construir lineups alternativas durante a geração de âncoras candidatas do Strategic Planner.

Portanto, o planner legado é hoje tanto produtor da lineup usada pelo fluxo atual quanto um mecanismo de construção de alternativas reutilizado pelo caminho Shadow. Não é apenas um seletor de direção.

### 1.3 StrategicPlanner

Arquivo: `cpp/include/strategy/StrategicPlanner.hpp`

Responsabilidades observadas:
- avaliar KEEP, ADAPT, PIVOT, ABANDON, seleção inicial e insuficiência de evidência;
- pontuar âncoras candidatas, custo de transição, unidades reutilizáveis e contestação;
- manter candidato e persistência em `StrategicCommitment`;
- classificar unidades próprias como preserváveis ou substituíveis;
- marcar as decisões como `shadow_only`.

O compromisso é um estado separado do `CompositionDirectionState`. No fluxo atual, o compromisso é hidratado usando `strategic_committed_direction`, com fallback para `info.composition_direction`. O planner pode avaliar um destino diferente, mas isso não o torna autoridade da direção ativa.

### 1.4 ActiveCompositionManager e UnifiedStrategicShadowRuntime

Arquivos:
- `cpp/include/composition_intelligence/ActiveCompositionManager.hpp`
- `cpp/include/composition_intelligence/CompositionIntelligenceRuntime.hpp`
- `cpp/include/strategy/UnifiedStrategicShadowRuntime.hpp`

O `ActiveCompositionManager` guarda uma composição ativa versionada, valida identidade, unidades e carry, e produz transições com unidades compartilhadas/adicionadas/removidas. Seu comentário declara independência dos sistemas legados de direção/foco.

O `CompositionIntelligencePlayerRuntime` mantém instâncias por jogador de active composition, transitions, recorder e snapshots.

O `UnifiedStrategicShadowRuntime` mantém a máquina unificada de direção/pivot e recorder. Seu método `refresh` contém exceções e não deixa falhas de gravação alterarem o resultado estratégico.

Esses estados têm contratos diferentes:
- direção ativa legada em `StrategyInfo`;
- compromisso KEEP/ADAPT/PIVOT do `StrategicPlanner`;
- composição externa versionada no `ActiveCompositionManager`;
- ciclo unificado Shadow no `UnifiedStrategicShadowRuntime`.

Eles não podem ser fundidos por simples renomeação.

## 2. Sobreposições e lacunas

| Área | Legado | Arquitetura nova | Avaliação |
|---|---|---|---|
| Direção ativa | `CompositionDirectionPolicy` altera/persiste `StrategyInfo.composition_direction` | Strategic Planner mantém compromisso próprio; máquina unificada tem identidade/versão própria | Sobreposição de conceito, autoridades distintas |
| Histerese/lock | Política legada com thresholds e streak | Strategic Planner com reviews KEEP/ADAPT/PIVOT; máquina unificada com ciclo próprio | Não equivalentes; thresholds e estados não devem ser combinados implicitamente |
| Lineup-alvo | `CompositionPlanner::build` gera lineup e carry | Active composition armazena snapshot candidato publicado | Builder e registro/versionamento são responsabilidades complementares |
| Alternativas | CompositionPlanner constrói planos por direção | Strategic Planner avalia âncoras e transições | O builder é reutilizado pelo Shadow, mas a decisão de pivot pertence ao planner Shadow |
| Identidade | Direção é string/trait e campos de `StrategyInfo` | IDs de composição, versão, identidade da âncora e origem | Falta contrato canônico de mapeamento |
| Unidades preservadas | Core/planned units e heurísticas de fit | Strategic Planner classifica preserve/replace | Há sinais parecidos, mas não foi demonstrada equivalência semântica |

### Riscos concretos

1. **Duas fontes para direção:** `StrategyInfo.composition_direction` continua sendo atualizada pelo caminho legado; `StrategicCommitment` e a máquina unificada têm estados próprios.
2. **Identidade incompleta no legado:** direção como trait não identifica de forma única uma composição, sua versão, carry principal ou lineup.
3. **Semânticas diferentes de histerese:** os limites e a contagem de revisões são diferentes; transferir estado entre políticas pode mudar quando uma direção troca.
4. **Builder compartilhado com múltiplos papéis:** `CompositionPlanner::build` atende tanto o plano legado quanto a geração de alternativas Shadow. Uma mudança de score pode afetar ambos os diagnósticos/consumidores.
5. **Dados ausentes não são equivalentes a inviabilidade:** qualquer futura migração precisa preservar distinção entre falta de evidência, direção inviável e alternativa comprovadamente superior.

## 3. Destino recomendado por componente

### CompositionDirectionPolicy — manter temporariamente como autoridade legada

Não remover agora. Ela ainda determina `StrategyInfo.composition_direction` e o estado de lock/histerese consumido pelo fluxo atual.

Antes de substituição:
- definir qual componente será a única autoridade da direção ativa;
- especificar migração de direction, candidate, streak, lock, previous direction e change reason;
- demonstrar que os ciclos de atualização não mudam por diferenças de cadence;
- garantir que o Viewer e auditorias continuem recebendo os campos atuais.

### CompositionPlanner — manter como builder/adaptador até existir substituto validado

Não remover agora. A arquitetura nova avalia âncoras e pivots, mas a geração de lineup concreta ainda usa `CompositionPlanner::build`.

Destino futuro possível:
- extrair a construção de lineup para um serviço independente e explicitamente read-only;
- manter uma única implementação de cálculo de aquisição/fit enquanto os dois fluxos precisarem dela;
- substituir apenas quando um builder novo produzir lineup equivalente ou superior em fixtures controladas e todos os consumidores estiverem mapeados.

Não é recomendável duplicar o algoritmo no Strategic Planner nem transformar uma intenção KEEP/ADAPT/PIVOT em ação nativa.

### StrategicPlanner e UnifiedStrategicShadowRuntime — manter isolados

Continuar como fontes diagnósticas em Shadow Mode. Não escrever sua decisão de volta em `StrategyInfo.composition_direction`, executor, PPO, masks, observations, rewards ou treinamento nesta etapa.

### ActiveCompositionManager — manter como registro versionado, não como substituto automático da direção

Seu papel é guardar uma composição identificada/versionada e suas transições. Ele pode vir a ser a autoridade da composição ativa, mas isso exige um contrato explícito que relacione:
- composition identity/version;
- direção/trait âncora;
- lineup e carry;
- origem e evidência;
- transição confirmada;
- estado de lock/histerese, se ainda necessário.

## 4. Plano de migração seguro

1. **Contrato e autoridade:** documentar matriz de autoridade para direção, composição/lineup, pivot candidato, pivot confirmado e histórico.
2. **Mapeamento de consumidores:** listar todos os leitores/escritores de `composition_direction`, `composition_locked`, `planned_unit_ids`, `core_unit_ids` e snapshots versionados, incluindo Viewer, auditorias e bindings.
3. **Identidade canônica:** especificar mapeamento determinístico entre trait/direction e composition identity/version; não inferir identidade apenas pelo nome de trait.
4. **Paridade do builder:** fixtures para loja, pool, nível, cópias, itens, unidades reutilizáveis, carry e lineup; comparar resultados e explicar diferenças intencionais.
5. **Paridade de transições:** testar inicialização, manutenção, lock, candidato persistente, perda de viabilidade, pivot avaliado e pivot confirmado.
6. **Shadow comparison:** coletar divergências reais e classificá-las; não forçar o Strategic Planner a concordar com o PPO/legado.
7. **Migração reversível:** somente após os passos anteriores, propor uma PR separada para transferir autoridade com fallback e rollback.
8. **Remoção de legado:** remover cada campo/componente somente após busca de consumidores, testes, Viewer e auditorias confirmarem ausência de dependência.

## 5. Testes necessários antes de qualquer substituição

- equivalência do plano por nível, loja, pool, cópias, itens e carry;
- estabilidade do plano sob pequenas variações de score e alto overlap;
- persistência de direção com candidato ausente;
- lock, desbloqueio por inviabilidade e transição emergencial;
- candidato alternativo que persiste por múltiplas revisões;
- pivot avaliado sem alteração da direção ativa;
- pivot confirmado com identidade/versão sincronizadas;
- composição ativa externa alterada enquanto o estado Shadow persiste;
- reset de partida e isolamento multi-player;
- consumidores Viewer/auditoria preservando campos e semânticas.

## 6. Limites desta revisão

- Foi feita inspeção estática dos headers e do fluxo de integração em `TftEngine.cpp`; não foi executada uma comparação quantitativa de partidas nesta revisão.
- Não há conclusão de que os algoritmos produzem resultados equivalentes.
- Não foi alterado código de produção, PPO, treinamento, observações, máscaras, ações, rewards, checkpoints, regras ou Viewer.
- Nenhum componente legado foi removido ou desativado.

## Conclusão

A #192 deve resultar em uma decisão de arquitetura, não em remoção imediata. Por enquanto, manter `CompositionDirectionPolicy` e `CompositionPlanner` no caminho legado; manter Strategic Planner, ActiveCompositionManager e UnifiedStrategicShadowRuntime isolados em Shadow; e abrir etapas específicas para contrato de autoridade, identidade canônica, paridade do builder e migração reversível.

A revisão estática identifica sobreposição e riscos, mas **não autoriza ativar o Strategic Planner no PPO nem substituir o legado**.
