# Auditoria de Fine-tuning Econômico

> Gerado a partir de `decision_trace.jsonl`. A comparação shadow usa o mesmo estado e as mesmas máscaras.

## Resumo executivo

- Estados comparados: **409600**
- Ações completas diferentes: **1867 (0.5%)**
- Mudanças de argumentos com mesmo tipo de ação: **0**
- Divergência JS média da cabeça de tipo: **0.000036**
- Cenário-alvo: **econ_gold_reserve**
- Estados fora do cenário-alvo: **392939**
- Divergência de ação nesses estados: **1779 (0.5%)**
- Status preliminar: **SEM ALERTA AUTOMÁTICO — REVISÃO DE CONSEQUÊNCIAS OBRIGATÓRIA**

O limite de 5% é apenas um alerta de triagem para mudanças fora do escopo, não um critério universal de aprovação.

## Frequência de todas as ações

| Ação | Original | Fine-tuned | Diferença |
|---|---:|---:|---:|
| BUY | 51121 | 51172 | +51 |
| REROLL | 1276 | 1247 | -29 |
| BUY_XP | 13897 | 13186 | -711 |
| MOVE_BENCH | 29355 | 29210 | -145 |
| MOVE_BOARD | 175783 | 177051 | +1268 |
| SELL | 17865 | 17882 | +17 |
| PASS | 112813 | 112366 | -447 |
| EQUIP_FROM_INVENTORY | 3179 | 3181 | +2 |
| CRAFT_AND_EQUIP | 4311 | 4305 | -6 |

## Preservação das famílias não treinadas

| Família fora do alvo | Original | Fine-tuned | Diferença |
|---|---:|---:|---:|
| MOVE_BENCH | 29355 | 29210 | -145 |
| MOVE_BOARD | 175783 | 177051 | +1268 |
| SELL | 17865 | 17882 | +17 |
| EQUIP_FROM_INVENTORY | 3179 | 3181 | +2 |
| CRAFT_AND_EQUIP | 4311 | 4305 | -6 |

## Preservação por estratégia

| Estratégia | Estados | Ações diferentes | Divergência | Estados fora do cenário | Divergências fora |
|---|---:|---:|---:|---:|---:|
| ALL_IN | 41375 | 245 | 0.6% | 41375 | 245 |
| ECON | 91944 | 94 | 0.1% | 75283 | 6 |
| FAST8 | 86960 | 374 | 0.4% | 86960 | 374 |
| LEGACY_UNUSED | 2143 | 7 | 0.3% | 2143 | 7 |
| STABILIZE | 180852 | 1091 | 0.6% | 180852 | 1091 |
| WINSTREAK | 6326 | 56 | 0.9% | 6326 | 56 |

## Cenários econômicos

| Cenário | Estados | Ações divergentes | Taxa | JS média |
|---|---:|---:|---:|---:|
| all_in_emergency | 41375 | 245 | 0.6% | 0.00004 |
| critical_hp_high_gold | 5615 | 44 | 0.8% | 0.00005 |
| econ_gold_reserve | 16661 | 88 | 0.5% | 0.00005 |
| econ_surplus_strong_board | 1198 | 6 | 0.5% | 0.00006 |
| fast8_strong_board | 84406 | 366 | 0.4% | 0.00005 |
| late_game_high_gold_underleveled | 1245 | 8 | 0.6% | 0.00007 |
| stabilize_weak_board | 38379 | 199 | 0.5% | 0.00005 |

## Partidas completas pareadas\n\n- Seeds avaliadas: **20**\n- Ambas as partidas concluídas: **20/20**\n- Estado e máscaras iniciais idênticos: **20/20**\n- Pares jogador/seed com colocação comparável: **160**\n- Diferença média de reward (fine-tuned - original): **-3.14707**\n- Colocação média (original → fine-tuned): **+4.481 → +4.519**\n- Diferença média de colocação (fine-tuned - original): **+0.037** (negativo é melhor)\n- Taxa Top 4: **48.8% → 51.2%**\n- Taxa de vitória: **15.6% → 9.4%**\n- Delta médio de HP/ouro/nível/estrutura/posição: **-2.650 / +6.250 / -0.175 / -0.033 / -0.022**\n\n| Seed | Reward delta médio | Placement delta médio | Top 4 original → fine-tuned | Ambas concluídas |\n|---:|---:|---:|:---:|:---:|\n| 20270121 | +3.66770 | -0.75 | 3/8 → 5/8 | Sim |\n| 20270122 | -0.60520 | +0.25 | 5/8 → 3/8 | Sim |\n| 20270123 | +14.23610 | -2.25 | 2/8 → 6/8 | Sim |\n| 20270124 | -16.22538 | +1.25 | 6/8 → 2/8 | Sim |\n| 20270125 | -13.03313 | +0.75 | 5/8 → 3/8 | Sim |\n| 20270126 | -10.07155 | +0.00 | 4/8 → 4/8 | Sim |\n| 20270127 | -3.99435 | +0.50 | 4/8 → 4/8 | Sim |\n| 20270128 | +7.79214 | -0.50 | 3/8 → 5/8 | Sim |\n| 20270129 | -13.13533 | +1.25 | 4/8 → 4/8 | Sim |\n| 20270130 | +0.96115 | -1.25 | 2/8 → 6/8 | Sim |\n| 20270131 | -4.79329 | +0.75 | 4/8 → 4/8 | Sim |\n| 20270132 | -1.49670 | -0.25 | 4/8 → 4/8 | Sim |\n| 20270133 | -12.51718 | +0.50 | 4/8 → 4/8 | Sim |\n| 20270134 | +11.40982 | -1.25 | 3/8 → 5/8 | Sim |\n| 20270135 | -8.41856 | -0.50 | 3/8 → 5/8 | Sim |\n| 20270136 | +8.20557 | -0.50 | 4/8 → 4/8 | Sim |\n| 20270137 | -7.37166 | +1.00 | 5/8 → 3/8 | Sim |\n| 20270138 | -9.35821 | +0.50 | 4/8 → 4/8 | Sim |\n| 20270139 | -5.71683 | +0.75 | 4/8 → 4/8 | Sim |\n| 20270140 | -2.47657 | +0.50 | 5/8 → 3/8 | Sim |\n\n### Frequência de ações nas partidas completas\n\n| Ação | Original | Fine-tuned | Diferença |\n|---|---:|---:|---:|\n| BUY | 9310 | 9393 | +83 |\n| REROLL | 391 | 450 | +59 |\n| BUY_XP | 3685 | 3313 | -372 |\n| MOVE_BENCH | 7706 | 8124 | +418 |\n| MOVE_BOARD | 35273 | 34100 | -1173 |\n| SELL | 3997 | 4138 | +141 |\n| PASS | 25325 | 26194 | +869 |\n| EQUIP_FROM_INVENTORY | 506 | 492 | -14 |\n| CRAFT_AND_EQUIP | 867 | 856 | -11 |\n\nPlacement é calculada pelo ranking terminal nativo; partidas incompletas não entram nas métricas de colocação.\n

## Proveniência do experimento\n\n- Commit do repositório/engine: `a58945f32a35edfb86e033afb2b085289dc49364`\n- SHA-256 checkpoint original: `c0fbe67a0cbee8c36b5873d29663eefb1207758a056ba825ea0eeb81e2fbba56`\n- SHA-256 checkpoint fine-tuned: `2ee2c22bb7cace9a24d0c10705ed497e900597b5bb333da3a66ad0053b5d4ba6`\n- SHA-256 RewardModel: `ab707e5cc5a32de84746a8a38e4ffff387971451c63c759755985f69f4f038e5`\n- SHA-256 TftEngine: `b6ce3845e4ec05a68cdb22c32908738116adcfe8ec093fd4a68c85532139b7e4`\n- Cenário: **econ_gold_reserve**\n- Transições do cenário: **16661**\n- PPO optimizer steps: **618**\n- SHA-256 config: `d0162a98b5c948af00c6eabb56bb9814474022454c2a820cd5442033f03eaeb6`\n- Commit usado na avaliação pareada: `a58945f32a35edfb86e033afb2b085289dc49364`\n- SHA-256 RewardModel na avaliação: `ab707e5cc5a32de84746a8a38e4ffff387971451c63c759755985f69f4f038e5`\n- SHA-256 TftEngine na avaliação: `b6ce3845e4ec05a68cdb22c32908738116adcfe8ec093fd4a68c85532139b7e4`\n- SHA-256 ActionMaskEngine na avaliação: `9f7a95cad451e5988201a358ed9741ec07c4bc29f19d85165928bb88982c357f`\n- SHA-256 policy.py na avaliação: `b704bfa8c459e41be8fae80f2295ee32e2ede78eb1af6d8a62e8fed3d7d20818`\n- batch_size: `64`\n- clip_coef: `0.1`\n- device: `cpu`\n- entropy_coef: `0.002`\n- learning_rate: `1e-05`\n- max_type_head_drift: `0.02`\n- min_scenario_transitions: `8`\n- ppo_epochs: `2`\n- rollout_steps: `512`\n- target_kl: `0.01`\n- updates: `100`\n

## Interpretação e limitações

- Ação divergente inclui mudanças em qualquer um dos seis componentes, inclusive slot, origem ou destino.
- A preservação das famílias não treinadas é medida por ação executada e divergência por estado; a tabela de frequência não prova qualidade.
- A divergência JS compara somente a distribuição da cabeça de tipo, não todas as distribuições condicionais autorregressivas.
- Cabeças de loja, venda, banco, tabuleiro e itens permanecem congeladas no treinamento padrão; ainda assim, sua seleção pode mudar se o tipo de ação mudar.
- Cenários de monitoramento não recebem recompensa artificial.
- Estados-alvo são encontrados durante simulação nativa; a engine atual não oferece injeção pública de estado inicial.
- Zero ocorrências significa **não coberto**, não preservação comprovada.
- A comparação shadow não substitui partidas completas pareadas, pois as trajetórias divergem após ações diferentes.

## Critério de aprovação

Aprovação exige ganho econômico demonstrado, amostra suficiente, ausência de regressão relevante nas decisões fora do escopo, partidas completas pareadas concluídas e generalização em seeds não usadas no treino. Este relatório isoladamente não promove o checkpoint.
