# Relatório final — sistema de itens da engine TFT (Fase 8)

**Data do relatório:** 2026-10-24  
**Escopo:** integração de itens na engine C++ e no caminho de ação/PPO, recompensas, validação e auditoria.  
**Status geral:** infraestrutura e testes de integração implementados e PRs das fases 2–7 mesclados; a integração de dados reais do set e a validação estratégica ponta a ponta ainda não estão concluídas.

## Resumo executivo

O projeto agora tem um contrato de catálogo externo, estado de itens por jogador, ações de item na policy PPO unificada, integração com a entrada de combate, recompensa estratégica, avaliação de checkpoints e um auditor de compatibilidade/partida completa. Os PRs #87–#92 estão mesclados e os checks registrados nos commits desses PRs terminaram com sucesso.

**Isso não significa que o sistema de itens esteja pronto para uma partida real de TFT.** O repositório ainda não contém um catálogo autoritativo do set ativo, e o fluxo de lobby não resolve drops de itens de PvE/armory para as APIs de concessão de componentes/itens. Sem catálogo real configurado, as ações de item ficam mascaradas. Também não há resultado antes/depois de treinamento comprovado por checkpoints pareados e partidas reais neste relatório.

## O que está integrado

### Runtime e catálogo
- Catálogo JSON versionado com validação de esquema, IDs, receitas, estatísticas e pesos de função.
- Estado de itens separado por jogador e propriedade de equipamento associada ao UUID da unidade.
- Máscaras para inventário, pares de componentes e alvos no tabuleiro/banco.
- Ações nativas EQUIP_FROM_INVENTORY (ID 7) e CRAFT_AND_EQUIP (ID 8).
- Validação de transição antes da mutação e proteção contra perda de itens em venda/fusão não suportada.
- APIs nativas de concessão de componente e item completo disponíveis para um futuro resolvedor de loot.

### Combate
- Adaptador converte a definição normalizada do catálogo para o contrato CombatItem.
- Itens equipados são encaminhados pela instância de unidade para a entrada normal de combate.
- O teste de integração valida a passagem de um item equipado pela entrada normal de simulação; isso não valida efeitos de estatísticas que o simulador ainda não calcula.

### Policy PPO e treinamento
- Ações de item usam a policy, o rollout, as máscaras e o caminho de reward compartilhados; não foi criada uma policy de itens separada.
- O tensor de ação continua com seis inteiros; os IDs 0–6 mantêm seus significados e 7–8 são as ações de item.
- As cabeças condicionais e o cálculo de log-probabilidade são testados em coleta e reavaliação.
- Checkpoints antigos podem passar por migração de compatibilidade para as dimensões novas. Isso preserva compatibilidade de inferência, mas **não treina retroativamente as cabeças novas**.

### Recompensa e avaliação
- Recompensa de item combina uma estimativa normalizada de força imediata com adequação à composição, função da unidade e estágio.
- A recompensa é limitada; a ponderação relativa entre composição e força imediata varia com o estágio.
- O avaliador de checkpoints registra ações totais e ações de item, além de resultados de colocação para comparação pareada.
- O auditor da Fase 7 registra hash do checkpoint, contrato de máscaras, ações, recompensas, eventos, uso de itens e colocação final dos oito jogadores.

## Histórico de implementação e CI

| PR | Escopo | Estado observado |
|---|---|---|
| [#87](https://github.com/victoremilianosilva/teste-ia/pull/87) | Runtime e caminho unificado de ações de item | Mesclado; checks concluídos com sucesso |
| [#88](https://github.com/victoremilianosilva/teste-ia/pull/88) | Validação de item equipado na simulação de combate | Mesclado; checks concluídos com sucesso |
| [#89](https://github.com/victoremilianosilva/teste-ia/pull/89) | Ações de item no caminho principal PPO | Mesclado; checks concluídos com sucesso |
| [#90](https://github.com/victoremilianosilva/teste-ia/pull/90) | Recompensa estratégica | Mesclado; checks concluídos com sucesso |
| [#91](https://github.com/victoremilianosilva/teste-ia/pull/91) | Contratos PPO, argumentos de ações e métricas | Mesclado; checks concluídos com sucesso |
| [#92](https://github.com/victoremilianosilva/teste-ia/pull/92) | Auditoria de compatibilidade e partida completa | Mesclado; checks concluídos com sucesso |

Os checks acima se referem às execuções associadas aos commits de cada PR, não a um experimento de treinamento. Na consulta para este relatório, o check da ponta atual de main ainda estava em execução; portanto, este documento não declara que o CI atual de main está verde.

## Testes e evidências disponíveis

Os PRs mesclados passaram pelos jobs de CI registrados nos respectivos commits. A suíte cobre, entre outros:
- contrato e validação de catálogo/receitas;
- inventário, equipagem, combinação e alvo;
- passagem do item equipado para a entrada de combate;
- máscara de nove tipos de ação e máscaras de item;
- consistência entre ação amostrada e log-probabilidade recalculada no PPO;
- serialização dos argumentos de EQUIP_FROM_INVENTORY e CRAFT_AND_EQUIP;
- cálculo e limites da recompensa estratégica;
- métricas do avaliador de checkpoints;
- contrato do auditor e garantia de que uma partida truncada não seja marcada como aprovada.

O teste do auditor usa um lobby simulado para verificar o protocolo de relatório. **Não é evidência de que uma partida real com a engine C++ e um checkpoint real terminou com sucesso.** Nenhum resultado de partida real, quantidade real de equipagens ou melhoria de colocação é afirmado aqui.

## Pendências que bloqueiam a conclusão funcional

### P0 — Necessárias para habilitar o sistema real
1. Fornecer e revisar um catálogo autoritativo do set ativo: componentes, receitas, IDs, estatísticas, normalização de porcentagens e pesos de função.
2. Integrar a origem real de loot/armory do lobby às APIs grant_item_component e grant_completed_item.
3. Confirmar que os efeitos de cada atributo de item relevante são consumidos pelo simulador de combate; o adaptador sozinho não implementa efeitos ausentes.

### P1 — Necessárias para comprovar a aprendizagem
4. Executar scripts/audit_item_system_e2e.py com módulo C++ compilado e checkpoint real, gerando audit.json e trace.jsonl.
5. Verificar que pelo menos um cenário controlado torna componentes/itens disponíveis e exercita as duas ações. Zero ações de item numa partida não prova que o caminho esteja quebrado, mas não prova que equipagem/combinação foi exercitada.
6. Executar comparação pareada antes/depois com checkpoints compatíveis, mesmas seeds e mesmo número de partidas; arquivar CSV/JSON, checkpoints, configuração e commit.
7. Examinar tentativas versus transições realmente aplicadas: o contador de ações é uma contagem de ações escolhidas/enviadas, não necessariamente de mutações bem-sucedidas. Se os eventos atuais não confirmarem sucesso, adicionar uma métrica/evento explícito ou comparar o estado nativo antes/depois.

### P2 — Regras de jogo e lifecycle ainda não implementados
8. Não existe ação de transferir item entre unidades nem ação de desequipar. Venda de unidade equipada e fusão que poderia perder propriedade são bloqueadas por segurança. Validar regras exatas do set antes de habilitar esses caminhos.
9. Confirmar se o contrato atual de inventário e capacidade de itens corresponde ao set ativo e ajustar após validar os dados oficiais.
10. Repetir testes e auditoria após ligar catálogo e loot reais; a fixture de testes é sintética e não substitui dados de produção.

## Comandos de validação

A partir da raiz do repositório:

~~~bash
python -m pytest \
  tests/test_ppo_mask_consistency.py \
  tests/test_viewer_items.py \
  tests/test_evaluate_checkpoints.py \
  tests/test_audit_item_system_e2e.py -q
~~~

Com o build C++ configurado:

~~~bash
ctest --test-dir cpp/build --output-on-failure -R 'item_engine|test_reward_model'
~~~

Auditoria com o módulo nativo compilado e um checkpoint compatível:

~~~bash
python scripts/audit_item_system_e2e.py \
  --checkpoint tft_checkpoint.pt \
  --seed 20261024 \
  --max-steps 5000 \
  --out-dir reports/item_system_phase7
~~~

Comparação estratégica somente depois de obter checkpoints compatíveis de baseline e candidato:

~~~bash
python scripts/evaluate_checkpoints.py \
  --baseline checkpoints/baseline.pt \
  --candidate checkpoints/items_phase5.pt \
  --matches 40 \
  --output reports/items_phase6_head_to_head.csv
~~~

Ajuste caminhos e nomes aos artefatos reais disponíveis. Não interprete o comando como evidência de execução; os arquivos de saída e os logs precisam ser guardados e revisados.

## Critério final de aceite

A infraestrutura de software e os contratos estão integrados, com CI aprovado nos PRs citados. O sistema completo só deve ser declarado funcional após todos os pontos abaixo:
- catálogo oficial carregado sem fixture;
- loot real conectado;
- efeitos de combate dos itens suportados verificados;
- auditoria com checkpoint e engine reais concluída, oito colocações válidas e trace preservado;
- ações de item aplicadas confirmadas no estado/eventos nativos;
- comparação pareada de treinamento publicada, sem inventar métricas.

**Conclusão:** Fase 8 documenta o estado real do código e as lacunas restantes. Ela não transforma pendências de dados, loot ou experimento em funcionalidades concluídas.
