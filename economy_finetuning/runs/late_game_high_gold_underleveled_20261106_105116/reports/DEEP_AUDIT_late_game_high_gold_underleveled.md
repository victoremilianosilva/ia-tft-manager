# Auditoria complementar de fine-tuning — late_game_high_gold_underleveled

> Gerado por economy_finetuning/deep_audit.py. Os JSONL são processados em streaming; os dados brutos não são copiados para este Markdown.

## Resumo executivo

- Cenário: **late_game_high_gold_underleveled**
- Transições do cenário no treino: **1429**
- Checkpoint original SHA-256: b4bc7f3515fcec275410f077fa9caa611452922ad7529a55673266ea2a775a4d
- Checkpoint fine-tuned SHA-256: c0fbe67a0cbee8c36b5873d29663eefb1207758a056ba825ea0eeb81e2fbba56
- Campos ausentes no trace: **nenhum**

## Análise shadow por estado

- Estados comparados: **409600**
- Ações divergentes: **903 (0.2%)**
- Estados do cenário late_game_high_gold_underleveled: **1429**, divergência **0.3%**
- Estados fora do cenário: **408171**, divergência **0.2%**

### Frequência de ações
| Ação | Original | Fine-tuned | Δ |
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

### Economia por coorte
| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |
|---|---:|---:|---:|---:|---:|---:|
| ouro ≥50 | 11121 | 0.3% | -7 | +13 | +7 | +0 |
| ouro ≥50 + HP ≤30 | 6098 | 0.3% | -4 | +2 | +7 | +0 |
| FAST8 + ouro ≥50 | 1985 | 0.3% | -1 | +3 | +0 | +0 |
| ouro <50 | 398479 | 0.2% | -243 | +279 | +35 | +1 |
| ouro 50–59 | 3600 | 0.2% | -2 | +2 | +2 | +0 |
| ouro 60–79 | 4587 | 0.3% | -2 | +7 | +1 | +0 |
| ouro 80+ | 2934 | 0.4% | -3 | +4 | +4 | +0 |
| HP ≤20 | 107085 | 0.1% | -13 | +20 | +31 | +0 |
| HP 21–40 | 38110 | 0.3% | -21 | +45 | +8 | +0 |
| HP >40 | 264405 | 0.3% | -216 | +227 | +3 | +1 |

### Decisões por estratégia
| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |
|---|---:|---:|---:|---:|---:|---:|
| ALL_IN | 42430 | 0.3% | -18 | +30 | +39 | +0 |
| ECON | 92005 | 0.1% | -8 | +28 | +3 | -2 |
| FAST8 | 86843 | 0.2% | -35 | +91 | +0 | +1 |
| LOSS_STREAK | 1950 | 0.4% | -2 | +1 | +0 | -1 |
| STABILIZE | 178646 | 0.3% | -185 | +132 | +0 | +3 |
| WINSTREAK | 7726 | 0.3% | -2 | +10 | +0 | +0 |

### Cobertura observada dos cenários
| Cenário | Estados |
|---|---:|
| all_in_gold_hoarding | 5422 |
| bench_deployment_quality | 63357 |
| carry_protection_positioning | 177735 |
| core_sale_retention | 40610 |
| critical_hp_high_gold | 6098 |
| gold_above_50_any_strategy | 10714 |
| late_game_high_gold_underleveled | 1429 |
| low_hp_fast8_high_gold | 38 |
| movement_no_progress | 255855 |
| player8_all_in_gold_hoarding | 699 |
| s4_fast8_lvl6_gold60_hp_ok | 40 |
| s4_fast8_lvl6_gold80 | 8 |
| s4_fast8_lvl7_gold60 | 224 |

As contagens não provam qualidade por si só. O trace registra HP, ouro, nível, estágio, round e estratégia, mas não qualidade da loja, campeões disponíveis, pares ou upgrades.


## Partidas completas pareadas

- Seeds: **20**
- Pares concluídos: **20/20**
- Estados iniciais idênticos: **20/20**
- Seeds com colocação melhor / pior / igual: **9 / 11 / 0**
- Delta médio de colocação por seed: **+0.100**
- IC 95% aproximado por seed: **[-0.223, +0.423]**
- Delta médio de Top4 por seed: **+0.013**

| Seed | Reward Δ | Placement Δ | Top4 Δ | Concluída | Estado inicial igual |
|---:|---:|---:|---:|:---:|:---:|
| 20261201 | +12.724 | -0.250 | +0.000 | Sim | Sim |
| 20261202 | +9.672 | -1.000 | +0.250 | Sim | Sim |
| 20261203 | -12.070 | +1.000 | -0.250 | Sim | Sim |
| 20261204 | -2.292 | -0.500 | +0.250 | Sim | Sim |
| 20261205 | -3.328 | +0.500 | +0.000 | Sim | Sim |
| 20261206 | -11.631 | +0.750 | +0.000 | Sim | Sim |
| 20261207 | +9.973 | -0.750 | +0.250 | Sim | Sim |
| 20261208 | +1.755 | +0.250 | +0.000 | Sim | Sim |
| 20261209 | +2.865 | -0.500 | +0.250 | Sim | Sim |
| 20261210 | -17.694 | +0.500 | +0.000 | Sim | Sim |
| 20261211 | -2.383 | +0.500 | +0.000 | Sim | Sim |
| 20261212 | -3.706 | +1.000 | +0.000 | Sim | Sim |
| 20261213 | +4.475 | -1.000 | +0.250 | Sim | Sim |
| 20261214 | +11.314 | -0.750 | +0.000 | Sim | Sim |
| 20261215 | -0.682 | -0.500 | +0.000 | Sim | Sim |
| 20261216 | -2.880 | +0.500 | +0.000 | Sim | Sim |
| 20261217 | -3.409 | +0.750 | -0.250 | Sim | Sim |
| 20261218 | -5.030 | +0.250 | +0.000 | Sim | Sim |
| 20261219 | -12.359 | +1.500 | -0.500 | Sim | Sim |
| 20261220 | +3.567 | -0.250 | +0.000 | Sim | Sim |

### Métricas terminais
| Métrica | Delta médio por jogador pareado |
|---|---:|
| Colocação (negativo é melhor) | +0.100 |
| HP | -1.256 |
| Ouro final | -0.125 |
| Nível | +0.000 |
| Poder do tabuleiro | -2.100 |
| Qualidade do tabuleiro | -0.037 |
| Posicionamento | -0.011 |
| Estrutura | -0.026 |

### Ações nas partidas completas
| Ação | Original | Fine-tuned | Δ |
|---|---:|---:|---:|
| BUY | 9211 | 9190 | -21 |
| REROLL | 435 | 396 | -39 |
| BUY_XP | 3366 | 3395 | +29 |
| MOVE_BENCH | 8944 | 8842 | -102 |
| MOVE_BOARD | 34809 | 34278 | -531 |
| SELL | 3868 | 3843 | -25 |
| PASS | 26674 | 27385 | +711 |
| EQUIP_FROM_INVENTORY | 498 | 479 | -19 |
| CRAFT_AND_EQUIP | 875 | 872 | -3 |

O intervalo usa seed como unidade amostral, não cada jogador individual, para evitar pseudorreplicação dentro da mesma lobby. É uma aproximação normal.


## Limitações e parecer

1. O trace não registra unidades da loja, pares, upgrades, composição planejada ou qualidade da oportunidade. Não é possível afirmar se uma compra específica era melhor que XP.
2. Não registra a identidade estratégica da unidade vendida. A preservação de pares/core não pode ser provada com estes arquivos.
3. Zero estados em uma coorte significa **não coberto**, não aprovado.
4. As métricas de lobby medem o resultado completo; não isolam causalmente uma ação individual.
5. O intervalo de confiança é aproximado e exige mais seeds inéditas para conclusões robustas.

- Estados SLOWROLL com ouro ≥50: **0**
- Estados FAST8 com ouro ≥50: **1985**
- Estados com ouro ≥50 e HP ≤30: **6098**
- Amostra mínima de 20 seeds concluídas: **ATINGIDA**

**Este relatório não altera evaluation_review.json, não aprova o checkpoint e não libera o próximo cenário.**
