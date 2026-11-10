# Auditoria complementar de fine-tuning — econ_gold_reserve

> Gerado por economy_finetuning/deep_audit.py. Os JSONL são processados em streaming; os dados brutos não são copiados para este Markdown.

## Resumo executivo

- Cenário: **econ_gold_reserve**
- Transições do cenário no treino: **16661**
- Checkpoint original SHA-256: c0fbe67a0cbee8c36b5873d29663eefb1207758a056ba825ea0eeb81e2fbba56
- Checkpoint fine-tuned SHA-256: 2ee2c22bb7cace9a24d0c10705ed497e900597b5bb333da3a66ad0053b5d4ba6
- Campos ausentes no trace: **nenhum**

## Análise shadow por estado

- Estados comparados: **409600**
- Ações divergentes: **1867 (0.5%)**
- Estados do cenário econ_gold_reserve: **16661**, divergência **0.5%**
- Estados fora do cenário: **392939**, divergência **0.5%**

### Frequência de ações
| Ação | Original | Fine-tuned | Δ |
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

### Economia por coorte
| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |
|---|---:|---:|---:|---:|---:|---:|
| ouro ≥50 | 11287 | 0.7% | +1 | -31 | -6 | +0 |
| ouro ≥50 + HP ≤30 | 5615 | 0.8% | -1 | -11 | -6 | +0 |
| FAST8 + ouro ≥50 | 2382 | 0.3% | +1 | -5 | +0 | +0 |
| ouro <50 | 398313 | 0.4% | +50 | -680 | -23 | -447 |
| ouro 50–59 | 3919 | 0.8% | +2 | -13 | -1 | +0 |
| ouro 60–79 | 4161 | 0.4% | -1 | -4 | -3 | +0 |
| ouro 80+ | 3207 | 0.9% | +0 | -14 | -2 | +0 |
| HP ≤20 | 106200 | 0.2% | -1 | -59 | -25 | +0 |
| HP 21–40 | 40895 | 0.5% | +3 | -112 | -4 | +0 |
| HP >40 | 262505 | 0.6% | +49 | -540 | +0 | -447 |

### Decisões por estratégia
| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |
|---|---:|---:|---:|---:|---:|---:|
| ALL_IN | 41375 | 0.6% | +2 | -77 | -28 | +0 |
| ECON | 91944 | 0.1% | -2 | -64 | +0 | -8 |
| FAST8 | 86960 | 0.4% | -9 | -224 | +0 | -3 |
| LEGACY_UNUSED | 2143 | 0.3% | +2 | -3 | +0 | -3 |
| STABILIZE | 180852 | 0.6% | +57 | -295 | -1 | -433 |
| WINSTREAK | 6326 | 0.9% | +1 | -48 | +0 | +0 |

### Cobertura observada dos cenários
| Cenário | Estados |
|---|---:|
| all_in_emergency | 41375 |
| critical_hp_high_gold | 5615 |
| econ_gold_reserve | 16661 |
| econ_surplus_strong_board | 1198 |
| fast8_strong_board | 84406 |
| late_game_high_gold_underleveled | 1245 |
| stabilize_weak_board | 38379 |

As contagens não provam qualidade por si só. O trace registra HP, ouro, nível, estágio, round e estratégia, mas não qualidade da loja, campeões disponíveis, pares ou upgrades.


## Partidas completas pareadas

- Seeds: **20**
- Pares concluídos: **20/20**
- Estados iniciais idênticos: **20/20**
- Seeds com colocação melhor / pior / igual: **8 / 11 / 1**
- Delta médio de colocação por seed: **+0.037**
- IC 95% aproximado por seed: **[-0.370, +0.445]**
- Delta médio de Top4 por seed: **+0.025**

| Seed | Reward Δ | Placement Δ | Top4 Δ | Concluída | Estado inicial igual |
|---:|---:|---:|---:|:---:|:---:|
| 20270121 | +3.668 | -0.750 | +0.250 | Sim | Sim |
| 20270122 | -0.605 | +0.250 | -0.250 | Sim | Sim |
| 20270123 | +14.236 | -2.250 | +0.500 | Sim | Sim |
| 20270124 | -16.225 | +1.250 | -0.500 | Sim | Sim |
| 20270125 | -13.033 | +0.750 | -0.250 | Sim | Sim |
| 20270126 | -10.072 | +0.000 | +0.000 | Sim | Sim |
| 20270127 | -3.994 | +0.500 | +0.000 | Sim | Sim |
| 20270128 | +7.792 | -0.500 | +0.250 | Sim | Sim |
| 20270129 | -13.135 | +1.250 | +0.000 | Sim | Sim |
| 20270130 | +0.961 | -1.250 | +0.500 | Sim | Sim |
| 20270131 | -4.793 | +0.750 | +0.000 | Sim | Sim |
| 20270132 | -1.497 | -0.250 | +0.000 | Sim | Sim |
| 20270133 | -12.517 | +0.500 | +0.000 | Sim | Sim |
| 20270134 | +11.410 | -1.250 | +0.250 | Sim | Sim |
| 20270135 | -8.419 | -0.500 | +0.250 | Sim | Sim |
| 20270136 | +8.206 | -0.500 | +0.000 | Sim | Sim |
| 20270137 | -7.372 | +1.000 | -0.250 | Sim | Sim |
| 20270138 | -9.358 | +0.500 | +0.000 | Sim | Sim |
| 20270139 | -5.717 | +0.750 | +0.000 | Sim | Sim |
| 20270140 | -2.477 | +0.500 | -0.250 | Sim | Sim |

### Métricas terminais
| Métrica | Delta médio por jogador pareado |
|---|---:|
| Colocação (negativo é melhor) | +0.037 |
| HP | -2.650 |
| Ouro final | +6.250 |
| Nível | -0.175 |
| Poder do tabuleiro | -3.600 |
| Qualidade do tabuleiro | -0.056 |
| Posicionamento | -0.022 |
| Estrutura | -0.033 |

### Ações nas partidas completas
| Ação | Original | Fine-tuned | Δ |
|---|---:|---:|---:|
| BUY | 9310 | 9393 | +83 |
| REROLL | 391 | 450 | +59 |
| BUY_XP | 3685 | 3313 | -372 |
| MOVE_BENCH | 7706 | 8124 | +418 |
| MOVE_BOARD | 35273 | 34100 | -1173 |
| SELL | 3997 | 4138 | +141 |
| PASS | 25325 | 26194 | +869 |
| EQUIP_FROM_INVENTORY | 506 | 492 | -14 |
| CRAFT_AND_EQUIP | 867 | 856 | -11 |

O intervalo usa seed como unidade amostral, não cada jogador individual, para evitar pseudorreplicação dentro da mesma lobby. É uma aproximação normal.


## Limitações e parecer

1. O trace não registra unidades da loja, pares, upgrades, composição planejada ou qualidade da oportunidade. Não é possível afirmar se uma compra específica era melhor que XP.
2. Não registra a identidade estratégica da unidade vendida. A preservação de pares/core não pode ser provada com estes arquivos.
3. Zero estados em uma coorte significa **não coberto**, não aprovado.
4. As métricas de lobby medem o resultado completo; não isolam causalmente uma ação individual.
5. O intervalo de confiança é aproximado e exige mais seeds inéditas para conclusões robustas.

- Estados SLOWROLL com ouro ≥50: **0**
- Estados FAST8 com ouro ≥50: **2382**
- Estados com ouro ≥50 e HP ≤30: **5615**
- Amostra mínima de 20 seeds concluídas: **ATINGIDA**

**Este relatório não altera evaluation_review.json, não aprova o checkpoint e não libera o próximo cenário.**
