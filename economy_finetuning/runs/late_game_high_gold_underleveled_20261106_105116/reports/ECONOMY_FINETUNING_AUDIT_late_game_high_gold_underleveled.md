# Auditoria de Fine-tuning Econômico

> Gerado a partir de `decision_trace.jsonl`. A comparação shadow usa o mesmo estado e as mesmas máscaras.

## Resumo executivo

- Estados comparados: **409600**
- Ações completas diferentes: **903 (0.2%)**
- Mudanças de argumentos com mesmo tipo de ação: **0**
- Divergência JS média da cabeça de tipo: **0.000013**
- Cenário-alvo: **late_game_high_gold_underleveled**
- Estados fora do cenário-alvo: **408171**
- Divergência de ação nesses estados: **898 (0.2%)**
- Status preliminar: **SEM ALERTA AUTOMÁTICO — REVISÃO DE CONSEQUÊNCIAS OBRIGATÓRIA**

O limite de 5% é apenas um alerta de triagem para mudanças fora do escopo, não um critério universal de aprovação.

## Frequência de todas as ações

| Ação | Original | Fine-tuned | Diferença |
|---|---:|---:|---:|
| BUY | 51313 | 51063 | -250 |
| REROLL | 1182 | 1224 | +42 |
| BUY_XP | 12366 | 12658 | +292 |
| MOVE_BENCH | 30325 | 30229 | -96 |
| MOVE_BOARD | 176600 | 176272 | -328 |
| SELL | 17974 | 18295 | +321 |
| PASS | 112547 | 112548 | +1 |
| EQUIP_FROM_INVENTORY | 3048 | 3059 | +11 |
| CRAFT_AND_EQUIP | 4245 | 4252 | +7 |

## Preservação das famílias não treinadas

| Família fora do alvo | Original | Fine-tuned | Diferença |
|---|---:|---:|---:|
| MOVE_BENCH | 30325 | 30229 | -96 |
| MOVE_BOARD | 176600 | 176272 | -328 |
| SELL | 17974 | 18295 | +321 |
| EQUIP_FROM_INVENTORY | 3048 | 3059 | +11 |
| CRAFT_AND_EQUIP | 4245 | 4252 | +7 |

## Preservação por estratégia

| Estratégia | Estados | Ações diferentes | Divergência | Estados fora do cenário | Divergências fora |
|---|---:|---:|---:|---:|---:|
| ALL_IN | 42430 | 130 | 0.3% | 42430 | 130 |
| ECON | 92005 | 54 | 0.1% | 92005 | 54 |
| FAST8 | 86843 | 167 | 0.2% | 85815 | 163 |
| LOSS_STREAK | 1950 | 8 | 0.4% | 1950 | 8 |
| STABILIZE | 178646 | 524 | 0.3% | 178245 | 523 |
| WINSTREAK | 7726 | 20 | 0.3% | 7726 | 20 |

## Cenários econômicos

| Cenário | Estados | Ações divergentes | Taxa | JS média |
|---|---:|---:|---:|---:|
| all_in_gold_hoarding | 5422 | 14 | 0.3% | 0.00002 |
| bench_deployment_quality | 63357 | 187 | 0.3% | 0.00002 |
| carry_protection_positioning | 177735 | 448 | 0.3% | 0.00002 |
| core_sale_retention | 40610 | 112 | 0.3% | 0.00002 |
| critical_hp_high_gold | 6098 | 16 | 0.3% | 0.00002 |
| gold_above_50_any_strategy | 10714 | 33 | 0.3% | 0.00002 |
| late_game_high_gold_underleveled | 1429 | 5 | 0.3% | 0.00002 |
| low_hp_fast8_high_gold | 38 | 0 | 0.0% | 0.00001 |
| movement_no_progress | 255855 | 699 | 0.3% | 0.00002 |
| player8_all_in_gold_hoarding | 699 | 1 | 0.1% | 0.00001 |
| s4_fast8_lvl6_gold60_hp_ok | 40 | 0 | 0.0% | 0.00001 |
| s4_fast8_lvl6_gold80 | 8 | 0 | 0.0% | 0.00001 |
| s4_fast8_lvl7_gold60 | 224 | 1 | 0.4% | 0.00001 |

## Partidas completas pareadas\n\n- Seeds avaliadas: **20**\n- Ambas as partidas concluídas: **20/20**\n- Estado e máscaras iniciais idênticos: **20/20**\n- Pares jogador/seed com colocação comparável: **160**\n- Diferença média de reward (fine-tuned - original): **-1.05595**\n- Colocação média (original → fine-tuned): **+4.450 → +4.550**\n- Diferença média de colocação (fine-tuned - original): **+0.100** (negativo é melhor)\n- Taxa Top 4: **49.4% → 50.6%**\n- Taxa de vitória: **14.4% → 10.6%**\n- Delta médio de HP/ouro/nível/estrutura/posição: **-1.256 / -0.125 / +0.000 / -0.026 / -0.011**\n\n| Seed | Reward delta médio | Placement delta médio | Top 4 original → fine-tuned | Ambas concluídas |\n|---:|---:|---:|:---:|:---:|\n| 20261201 | +12.72439 | -0.25 | 4/8 → 4/8 | Sim |\n| 20261202 | +9.67191 | -1.00 | 3/8 → 5/8 | Sim |\n| 20261203 | -12.06981 | +1.00 | 5/8 → 3/8 | Sim |\n| 20261204 | -2.29227 | -0.50 | 3/8 → 5/8 | Sim |\n| 20261205 | -3.32753 | +0.50 | 4/8 → 4/8 | Sim |\n| 20261206 | -11.63132 | +0.75 | 4/8 → 4/8 | Sim |\n| 20261207 | +9.97286 | -0.75 | 3/8 → 5/8 | Sim |\n| 20261208 | +1.75467 | +0.25 | 4/8 → 4/8 | Sim |\n| 20261209 | +2.86464 | -0.50 | 3/8 → 5/8 | Sim |\n| 20261210 | -17.69351 | +0.50 | 4/8 → 4/8 | Sim |\n| 20261211 | -2.38304 | +0.50 | 4/8 → 4/8 | Sim |\n| 20261212 | -3.70626 | +1.00 | 4/8 → 4/8 | Sim |\n| 20261213 | +4.47478 | -1.00 | 3/8 → 5/8 | Sim |\n| 20261214 | +11.31398 | -0.75 | 4/8 → 4/8 | Sim |\n| 20261215 | -0.68199 | -0.50 | 4/8 → 4/8 | Sim |\n| 20261216 | -2.87997 | +0.50 | 4/8 → 4/8 | Sim |\n| 20261217 | -3.40879 | +0.75 | 5/8 → 3/8 | Sim |\n| 20261218 | -5.03043 | +0.25 | 4/8 → 4/8 | Sim |\n| 20261219 | -12.35874 | +1.50 | 6/8 → 2/8 | Sim |\n| 20261220 | +3.56746 | -0.25 | 4/8 → 4/8 | Sim |\n\n### Frequência de ações nas partidas completas\n\n| Ação | Original | Fine-tuned | Diferença |\n|---|---:|---:|---:|\n| BUY | 9211 | 9190 | -21 |\n| REROLL | 435 | 396 | -39 |\n| BUY_XP | 3366 | 3395 | +29 |\n| MOVE_BENCH | 8944 | 8842 | -102 |\n| MOVE_BOARD | 34809 | 34278 | -531 |\n| SELL | 3868 | 3843 | -25 |\n| PASS | 26674 | 27385 | +711 |\n| EQUIP_FROM_INVENTORY | 498 | 479 | -19 |\n| CRAFT_AND_EQUIP | 875 | 872 | -3 |\n\nPlacement é calculada pelo ranking terminal nativo; partidas incompletas não entram nas métricas de colocação.\n

## Proveniência do experimento\n\n- Commit do repositório/engine: `35404e55676295ea3d2d5d82a2d6eb32b5289684`\n- SHA-256 checkpoint original: `b4bc7f3515fcec275410f077fa9caa611452922ad7529a55673266ea2a775a4d`\n- SHA-256 checkpoint fine-tuned: `c0fbe67a0cbee8c36b5873d29663eefb1207758a056ba825ea0eeb81e2fbba56`\n- SHA-256 RewardModel: `f671db86306a0dc61f3d7b2016fed87c7c8f9d6902a77e028de26ad8c958cd4a`\n- SHA-256 TftEngine: `edf042486a3c7bcaf6bdb12e74886cfc88751544a8cecdc94d53832c85d159cb`\n- Cenário: **late_game_high_gold_underleveled**\n- Transições do cenário: **1429**\n- PPO optimizer steps: **76**\n- SHA-256 config: `d0162a98b5c948af00c6eabb56bb9814474022454c2a820cd5442033f03eaeb6`\n- Commit usado na avaliação pareada: `35404e55676295ea3d2d5d82a2d6eb32b5289684`\n- SHA-256 RewardModel na avaliação: `f671db86306a0dc61f3d7b2016fed87c7c8f9d6902a77e028de26ad8c958cd4a`\n- SHA-256 TftEngine na avaliação: `edf042486a3c7bcaf6bdb12e74886cfc88751544a8cecdc94d53832c85d159cb`\n- SHA-256 ActionMaskEngine na avaliação: `9f7a95cad451e5988201a358ed9741ec07c4bc29f19d85165928bb88982c357f`\n- SHA-256 policy.py na avaliação: `b704bfa8c459e41be8fae80f2295ee32e2ede78eb1af6d8a62e8fed3d7d20818`\n- batch_size: `64`\n- clip_coef: `0.1`\n- device: `cpu`\n- entropy_coef: `0.002`\n- learning_rate: `1e-05`\n- max_type_head_drift: `0.02`\n- min_scenario_transitions: `8`\n- ppo_epochs: `2`\n- rollout_steps: `512`\n- target_kl: `0.01`\n- updates: `100`\n

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
