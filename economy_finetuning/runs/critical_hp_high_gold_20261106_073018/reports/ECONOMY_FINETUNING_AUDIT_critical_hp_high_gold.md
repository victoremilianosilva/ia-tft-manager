# Auditoria de Fine-tuning Econômico

> Gerado a partir de `decision_trace.jsonl`. A comparação shadow usa o mesmo estado e as mesmas máscaras.

## Resumo executivo

- Estados comparados: **409600**
- Ações completas diferentes: **1755 (0.4%)**
- Mudanças de argumentos com mesmo tipo de ação: **0**
- Divergência JS média da cabeça de tipo: **0.000048**
- Cenário-alvo: **critical_hp_high_gold**
- Estados fora do cenário-alvo: **404915**
- Divergência de ação nesses estados: **1712 (0.4%)**
- Status preliminar: **SEM ALERTA AUTOMÁTICO — REVISÃO DE CONSEQUÊNCIAS OBRIGATÓRIA**

O limite de 5% é apenas um alerta de triagem para mudanças fora do escopo, não um critério universal de aprovação.

## Frequência de todas as ações

| Ação | Original | Fine-tuned | Diferença |
|---|---:|---:|---:|
| BUY | 51120 | 51133 | +13 |
| REROLL | 1108 | 1130 | +22 |
| BUY_XP | 12311 | 13106 | +795 |
| MOVE_BENCH | 30571 | 29949 | -622 |
| MOVE_BOARD | 176678 | 176056 | -622 |
| SELL | 17982 | 18444 | +462 |
| PASS | 112619 | 112553 | -66 |
| EQUIP_FROM_INVENTORY | 3012 | 3016 | +4 |
| CRAFT_AND_EQUIP | 4199 | 4213 | +14 |

## Preservação das famílias não treinadas

| Família fora do alvo | Original | Fine-tuned | Diferença |
|---|---:|---:|---:|
| MOVE_BENCH | 30571 | 29949 | -622 |
| MOVE_BOARD | 176678 | 176056 | -622 |
| SELL | 17982 | 18444 | +462 |
| EQUIP_FROM_INVENTORY | 3012 | 3016 | +4 |
| CRAFT_AND_EQUIP | 4199 | 4213 | +14 |

## Preservação por estratégia

| Estratégia | Estados | Ações diferentes | Divergência | Estados fora do cenário | Divergências fora |
|---|---:|---:|---:|---:|---:|
| ALL_IN | 40635 | 291 | 0.7% | 36564 | 253 |
| ECON | 90970 | 107 | 0.1% | 90970 | 107 |
| FAST8 | 88234 | 402 | 0.5% | 88234 | 402 |
| LOSS_STREAK | 2330 | 10 | 0.4% | 2330 | 10 |
| STABILIZE | 179798 | 882 | 0.5% | 179184 | 877 |
| WINSTREAK | 7633 | 63 | 0.8% | 7633 | 63 |

## Cenários econômicos

| Cenário | Estados | Ações divergentes | Taxa | JS média |
|---|---:|---:|---:|---:|
| all_in_gold_hoarding | 4071 | 38 | 0.9% | 0.00011 |
| bench_deployment_quality | 60916 | 343 | 0.6% | 0.00010 |
| carry_protection_positioning | 176985 | 1004 | 0.6% | 0.00008 |
| core_sale_retention | 38434 | 238 | 0.6% | 0.00010 |
| critical_hp_high_gold | 4685 | 43 | 0.9% | 0.00011 |
| gold_above_50_any_strategy | 8961 | 78 | 0.9% | 0.00012 |
| late_game_high_gold_underleveled | 1170 | 7 | 0.6% | 0.00013 |
| low_hp_fast8_high_gold | 16 | 0 | 0.0% | 0.00008 |
| movement_no_progress | 255745 | 1449 | 0.6% | 0.00007 |
| player8_all_in_gold_hoarding | 452 | 2 | 0.4% | 0.00008 |
| s4_fast8_lvl6_gold60_hp_ok | 91 | 0 | 0.0% | 0.00003 |
| s4_fast8_lvl6_gold80 | 5 | 0 | 0.0% | 0.00002 |
| s4_fast8_lvl7_gold60 | 269 | 0 | 0.0% | 0.00014 |

## Partidas completas pareadas\n\n- Seeds avaliadas: **20**\n- Ambas as partidas concluídas: **20/20**\n- Estado e máscaras iniciais idênticos: **20/20**\n- Pares jogador/seed com colocação comparável: **160**\n- Diferença média de reward (fine-tuned - original): **3.34687**\n- Colocação média (original → fine-tuned): **+4.656 → +4.344**\n- Diferença média de colocação (fine-tuned - original): **-0.312** (negativo é melhor)\n- Taxa Top 4: **46.2% → 53.8%**\n- Taxa de vitória: **10.6% → 14.4%**\n- Delta médio de HP/ouro/nível/estrutura/posição: **-0.106 / -10.531 / +0.131 / +0.018 / +0.014**\n\n| Seed | Reward delta médio | Placement delta médio | Top 4 original → fine-tuned | Ambas concluídas |\n|---:|---:|---:|:---:|:---:|\n| 20261201 | +14.29015 | -1.50 | 3/8 → 5/8 | Sim |\n| 20261202 | +20.65941 | -2.00 | 2/8 → 6/8 | Sim |\n| 20261203 | +11.65688 | -0.75 | 3/8 → 5/8 | Sim |\n| 20261204 | +8.09791 | +0.00 | 4/8 → 4/8 | Sim |\n| 20261205 | +8.83686 | -0.25 | 4/8 → 4/8 | Sim |\n| 20261206 | -19.27565 | +1.25 | 5/8 → 3/8 | Sim |\n| 20261207 | +1.66799 | -0.50 | 4/8 → 4/8 | Sim |\n| 20261208 | +12.00545 | -1.00 | 3/8 → 5/8 | Sim |\n| 20261209 | +3.24906 | +0.00 | 3/8 → 5/8 | Sim |\n| 20261210 | +8.96556 | -0.75 | 3/8 → 5/8 | Sim |\n| 20261211 | -1.32720 | +0.25 | 4/8 → 4/8 | Sim |\n| 20261212 | -2.50134 | +0.50 | 4/8 → 4/8 | Sim |\n| 20261213 | -13.44193 | +1.00 | 6/8 → 2/8 | Sim |\n| 20261214 | -0.07681 | -0.25 | 4/8 → 4/8 | Sim |\n| 20261215 | -11.51119 | +0.00 | 4/8 → 4/8 | Sim |\n| 20261216 | -2.70492 | +0.25 | 4/8 → 4/8 | Sim |\n| 20261217 | +0.42133 | +0.25 | 4/8 → 4/8 | Sim |\n| 20261218 | +9.22722 | -0.75 | 4/8 → 4/8 | Sim |\n| 20261219 | +2.26351 | -1.00 | 3/8 → 5/8 | Sim |\n| 20261220 | +16.43506 | -1.00 | 3/8 → 5/8 | Sim |\n\n### Frequência de ações nas partidas completas\n\n| Ação | Original | Fine-tuned | Diferença |\n|---|---:|---:|---:|\n| BUY | 9316 | 9181 | -135 |\n| REROLL | 434 | 392 | -42 |\n| BUY_XP | 3195 | 3426 | +231 |\n| MOVE_BENCH | 9036 | 8314 | -722 |\n| MOVE_BOARD | 33532 | 35956 | +2424 |\n| SELL | 4028 | 3868 | -160 |\n| PASS | 27949 | 26398 | -1551 |\n| EQUIP_FROM_INVENTORY | 518 | 445 | -73 |\n| CRAFT_AND_EQUIP | 852 | 880 | +28 |\n\nPlacement é calculada pelo ranking terminal nativo; partidas incompletas não entram nas métricas de colocação.\n

## Proveniência do experimento\n\n- Commit do repositório/engine: `f316e06ce1913c2673184ca5d5dfdf3c7236ddfb`\n- SHA-256 checkpoint original: `2cb097f284849b572c30178c174caacd646479212e770abf10a51f5f11eb30a4`\n- SHA-256 checkpoint fine-tuned: `b4bc7f3515fcec275410f077fa9caa611452922ad7529a55673266ea2a775a4d`\n- SHA-256 RewardModel: `f671db86306a0dc61f3d7b2016fed87c7c8f9d6902a77e028de26ad8c958cd4a`\n- SHA-256 TftEngine: `edf042486a3c7bcaf6bdb12e74886cfc88751544a8cecdc94d53832c85d159cb`\n- Cenário: **critical_hp_high_gold**\n- Transições do cenário: **4685**\n- PPO optimizer steps: **214**\n- SHA-256 config: `d0162a98b5c948af00c6eabb56bb9814474022454c2a820cd5442033f03eaeb6`\n- Commit usado na avaliação pareada: `f316e06ce1913c2673184ca5d5dfdf3c7236ddfb`\n- SHA-256 RewardModel na avaliação: `f671db86306a0dc61f3d7b2016fed87c7c8f9d6902a77e028de26ad8c958cd4a`\n- SHA-256 TftEngine na avaliação: `edf042486a3c7bcaf6bdb12e74886cfc88751544a8cecdc94d53832c85d159cb`\n- SHA-256 ActionMaskEngine na avaliação: `9f7a95cad451e5988201a358ed9741ec07c4bc29f19d85165928bb88982c357f`\n- SHA-256 policy.py na avaliação: `b704bfa8c459e41be8fae80f2295ee32e2ede78eb1af6d8a62e8fed3d7d20818`\n- batch_size: `64`\n- clip_coef: `0.1`\n- device: `cpu`\n- entropy_coef: `0.002`\n- learning_rate: `1e-05`\n- max_type_head_drift: `0.02`\n- min_scenario_transitions: `8`\n- ppo_epochs: `2`\n- rollout_steps: `512`\n- target_kl: `0.01`\n- updates: `100`\n

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
