# Auditoria complementar de fine-tuning — critical_hp_high_gold

> Gerado por economy_finetuning/deep_audit.py. Os JSONL são processados em streaming; os dados brutos não são copiados para este Markdown.

## Resumo executivo

- Cenário: **critical_hp_high_gold**
- Transições do cenário no treino: **4685**
- Checkpoint original SHA-256: 2cb097f284849b572c30178c174caacd646479212e770abf10a51f5f11eb30a4
- Checkpoint fine-tuned SHA-256: b4bc7f3515fcec275410f077fa9caa611452922ad7529a55673266ea2a775a4d
- Campos ausentes no trace: **nenhum**

## Análise shadow por estado

- Estados comparados: **409600**
- Ações divergentes: **1755 (0.4%)**
- Estados do cenário critical_hp_high_gold: **4685**, divergência **0.9%**
- Estados fora do cenário: **404915**, divergência **0.4%**

### Frequência de ações
| Ação | Original | Fine-tuned | Δ |
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

### Economia por coorte
| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |
|---|---:|---:|---:|---:|---:|---:|
| ouro ≥50 | 9484 | 0.8% | +1 | +33 | +2 | +0 |
| ouro ≥50 + HP ≤30 | 4685 | 0.9% | -2 | +12 | +2 | +0 |
| FAST8 + ouro ≥50 | 1886 | 0.4% | +0 | +7 | +0 | +0 |
| ouro <50 | 400116 | 0.4% | +12 | +762 | +20 | -66 |
| ouro 50–59 | 3326 | 0.6% | +1 | +10 | -1 | +0 |
| ouro 60–79 | 3759 | 0.7% | +0 | +11 | +1 | +0 |
| ouro 80+ | 2399 | 1.3% | +0 | +12 | +2 | +0 |
| HP ≤20 | 105810 | 0.2% | +0 | +73 | +16 | -4 |
| HP 21–40 | 39105 | 0.6% | +2 | +127 | +5 | -1 |
| HP >40 | 264685 | 0.5% | +11 | +595 | +1 | -61 |

### Decisões por estratégia
| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |
|---|---:|---:|---:|---:|---:|---:|
| ALL_IN | 40635 | 0.7% | -1 | +98 | +21 | -4 |
| ECON | 90970 | 0.1% | +1 | +77 | -1 | -2 |
| FAST8 | 88234 | 0.5% | +3 | +246 | +0 | -2 |
| LOSS_STREAK | 2330 | 0.4% | -1 | +3 | +0 | +0 |
| STABILIZE | 179798 | 0.5% | +8 | +326 | +0 | -57 |
| WINSTREAK | 7633 | 0.8% | +3 | +45 | +2 | -1 |

### Cobertura observada dos cenários
| Cenário | Estados |
|---|---:|
| all_in_gold_hoarding | 4071 |
| bench_deployment_quality | 60916 |
| carry_protection_positioning | 176985 |
| core_sale_retention | 38434 |
| critical_hp_high_gold | 4685 |
| gold_above_50_any_strategy | 8961 |
| late_game_high_gold_underleveled | 1170 |
| low_hp_fast8_high_gold | 16 |
| movement_no_progress | 255745 |
| player8_all_in_gold_hoarding | 452 |
| s4_fast8_lvl6_gold60_hp_ok | 91 |
| s4_fast8_lvl6_gold80 | 5 |
| s4_fast8_lvl7_gold60 | 269 |

As contagens não provam qualidade por si só. O trace registra HP, ouro, nível, estágio, round e estratégia, mas não qualidade da loja, campeões disponíveis, pares ou upgrades.


## Partidas completas pareadas

- Seeds: **20**
- Pares concluídos: **20/20**
- Estados iniciais idênticos: **20/20**
- Seeds com colocação melhor / pior / igual: **11 / 6 / 3**
- Delta médio de colocação por seed: **-0.312**
- IC 95% aproximado por seed: **[-0.666, +0.041]**
- Delta médio de Top4 por seed: **+0.075**

| Seed | Reward Δ | Placement Δ | Top4 Δ | Concluída | Estado inicial igual |
|---:|---:|---:|---:|:---:|:---:|
| 20261201 | +14.290 | -1.500 | +0.250 | Sim | Sim |
| 20261202 | +20.659 | -2.000 | +0.500 | Sim | Sim |
| 20261203 | +11.657 | -0.750 | +0.250 | Sim | Sim |
| 20261204 | +8.098 | +0.000 | +0.000 | Sim | Sim |
| 20261205 | +8.837 | -0.250 | +0.000 | Sim | Sim |
| 20261206 | -19.276 | +1.250 | -0.250 | Sim | Sim |
| 20261207 | +1.668 | -0.500 | +0.000 | Sim | Sim |
| 20261208 | +12.005 | -1.000 | +0.250 | Sim | Sim |
| 20261209 | +3.249 | +0.000 | +0.250 | Sim | Sim |
| 20261210 | +8.966 | -0.750 | +0.250 | Sim | Sim |
| 20261211 | -1.327 | +0.250 | +0.000 | Sim | Sim |
| 20261212 | -2.501 | +0.500 | +0.000 | Sim | Sim |
| 20261213 | -13.442 | +1.000 | -0.500 | Sim | Sim |
| 20261214 | -0.077 | -0.250 | +0.000 | Sim | Sim |
| 20261215 | -11.511 | +0.000 | +0.000 | Sim | Sim |
| 20261216 | -2.705 | +0.250 | +0.000 | Sim | Sim |
| 20261217 | +0.421 | +0.250 | +0.000 | Sim | Sim |
| 20261218 | +9.227 | -0.750 | +0.000 | Sim | Sim |
| 20261219 | +2.264 | -1.000 | +0.250 | Sim | Sim |
| 20261220 | +16.435 | -1.000 | +0.250 | Sim | Sim |

### Métricas terminais
| Métrica | Delta médio por jogador pareado |
|---|---:|
| Colocação (negativo é melhor) | -0.312 |
| HP | -0.106 |
| Ouro final | -10.531 |
| Nível | +0.131 |
| Poder do tabuleiro | +2.675 |
| Qualidade do tabuleiro | +0.032 |
| Posicionamento | +0.014 |
| Estrutura | +0.018 |

### Ações nas partidas completas
| Ação | Original | Fine-tuned | Δ |
|---|---:|---:|---:|
| BUY | 9316 | 9181 | -135 |
| REROLL | 434 | 392 | -42 |
| BUY_XP | 3195 | 3426 | +231 |
| MOVE_BENCH | 9036 | 8314 | -722 |
| MOVE_BOARD | 33532 | 35956 | +2424 |
| SELL | 4028 | 3868 | -160 |
| PASS | 27949 | 26398 | -1551 |
| EQUIP_FROM_INVENTORY | 518 | 445 | -73 |
| CRAFT_AND_EQUIP | 852 | 880 | +28 |

O intervalo usa seed como unidade amostral, não cada jogador individual, para evitar pseudorreplicação dentro da mesma lobby. É uma aproximação normal.


## Limitações e parecer

1. O trace não registra unidades da loja, pares, upgrades, composição planejada ou qualidade da oportunidade. Não é possível afirmar se uma compra específica era melhor que XP.
2. Não registra a identidade estratégica da unidade vendida. A preservação de pares/core não pode ser provada com estes arquivos.
3. Zero estados em uma coorte significa **não coberto**, não aprovado.
4. As métricas de lobby medem o resultado completo; não isolam causalmente uma ação individual.
5. O intervalo de confiança é aproximado e exige mais seeds inéditas para conclusões robustas.

- Estados SLOWROLL com ouro ≥50: **0**
- Estados FAST8 com ouro ≥50: **1886**
- Estados com ouro ≥50 e HP ≤30: **4685**
- Amostra mínima de 20 seeds concluídas: **ATINGIDA**

**Este relatório não altera evaluation_review.json, não aprova o checkpoint e não libera o próximo cenário.**
