## Auditoria econômica por ação

| Jogador | Ações | Ouro gasto | Ouro recuperado | Juros potenciais perdidos | XP sem level-up | Level-up sem unidade implantada | Rerolls sem ganho imediato | Reroll → PASS | Ouro final | Força final |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 163 | 190 | 96 | 3 | 7 | 0 | 0 | 0 | 231 | 48.0 |
- Jogador 1 — gasto por ação: BUY: 158g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 1 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 28g, stage 4: 29g, stage 5: 42g, stage 6: 37g
| Jogador 2 | 105 | 97 | 60 | 4 | 1 | 1 | 1 | 0 | 132 | 20.0 |
- Jogador 2 — gasto por ação: BUY: 87g, BUY_XP: 8g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 2 — gasto por estágio: stage 1: 7g, stage 2: 38g, stage 3: 37g, stage 4: 15g
| Jogador 3 | 130 | 113 | 67 | 3 | 2 | 0 | 0 | 0 | 189 | 26.0 |
- Jogador 3 — gasto por ação: BUY: 105g, BUY_XP: 8g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 3 — gasto por estágio: stage 1: 7g, stage 2: 31g, stage 3: 25g, stage 4: 27g, stage 5: 23g
| Jogador 4 | 118 | 119 | 52 | 3 | 5 | 1 | 2 | 0 | 124 | 22.0 |
- Jogador 4 — gasto por ação: BUY: 91g, BUY_XP: 24g, CRAFT_AND_EQUIP: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 4g, SELL: 0g
- Jogador 4 — gasto por estágio: stage 1: 6g, stage 2: 46g, stage 3: 32g, stage 4: 27g, stage 5: 8g
| Jogador 5 | 142 | 151 | 95 | 6 | 3 | 0 | 1 | 0 | 233 | 34.0 |
- Jogador 5 — gasto por ação: BUY: 133g, BUY_XP: 16g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, REROLL: 2g, SELL: 0g
- Jogador 5 — gasto por estágio: stage 1: 7g, stage 2: 37g, stage 3: 38g, stage 4: 25g, stage 5: 33g, stage 6: 11g
| Jogador 6 | 126 | 166 | 60 | 9 | 12 | 0 | 0 | 0 | 123 | 44.0 |
- Jogador 6 — gasto por ação: BUY: 114g, BUY_XP: 52g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 6 — gasto por estágio: stage 1: 5g, stage 2: 44g, stage 3: 60g, stage 4: 34g, stage 5: 23g
| Jogador 7 | 168 | 184 | 101 | 6 | 8 | 0 | 0 | 0 | 232 | 40.0 |
- Jogador 7 — gasto por ação: BUY: 152g, BUY_XP: 32g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 7 — gasto por estágio: stage 1: 6g, stage 2: 48g, stage 3: 40g, stage 4: 29g, stage 5: 36g, stage 6: 25g
| Jogador 8 | 141 | 129 | 85 | 6 | 0 | 0 | 0 | 0 | 204 | 32.0 |
- Jogador 8 — gasto por ação: BUY: 129g, CRAFT_AND_EQUIP: 0g, EQUIP_FROM_INVENTORY: 0g, MOVE_BENCH: 0g, MOVE_BOARD: 0g, PASS: 0g, SELL: 0g
- Jogador 8 — gasto por estágio: stage 1: 7g, stage 2: 36g, stage 3: 32g, stage 4: 32g, stage 5: 22g

Os motivos ficam em economic_diagnostics.reason_code. 'Sem ganho imediato' não significa automaticamente uma decisão ruim; o relatório não modifica a recompensa PPO.

### Janelas de XP e estabilização para revisão

| Jogador | Compras de XP | Janelas de revisão |
|---|---:|---:|
| Jogador 1 | 8 | 1 |
- Jogador 1 · 3-3 · step 105: PASS com 15g, HP 93, nível 6/8 (STABILIZE).
| Jogador 2 | 2 | 1 |
- Jogador 2 · 3-7 · step 126: REROLL com 78g, HP 47, nível 6/8 (STABILIZE).
| Jogador 3 | 2 | 0 |
| Jogador 4 | 6 | 3 |
- Jogador 4 · 4-2 · step 136: PASS com 58g, HP 46, nível 6/8 (STABILIZE).
- Jogador 4 · 4-6 · step 156: REROLL com 98g, HP 14, nível 6/8 (ALL_IN).
- Jogador 4 · 4-7 · step 160: REROLL com 108g, HP 3, nível 6/8 (ALL_IN).
| Jogador 5 | 4 | 1 |
- Jogador 5 · 5-3 · step 175: REROLL com 169g, HP 51, nível 6/8 (STABILIZE).
| Jogador 6 | 13 | 0 |
| Jogador 7 | 8 | 1 |
- Jogador 7 · 4-2 · step 136: PASS com 36g, HP 56, nível 6/8 (STABILIZE).
| Jogador 8 | 0 | 0 |

Janelas candidatas não são penalidades nem provam que XP era a melhor ação. Compare loja, pares, upgrades, HP, nível-alvo, reserva de juros e estratégia; SLOWROLL é excluído.

## Auditoria de mudanças de composição

| Jogador | Mudanças | Com ganho mensurável | Sem ganho mensurável | Taxa sem ganho |
|---|---:|---:|---:|---:|
| Jogador 1 | 3 | 3 | 0 | 0.0% |
| Jogador 2 | 1 | 1 | 0 | 0.0% |
| Jogador 3 | 2 | 1 | 1 | 50.0% |
| Jogador 4 | 2 | 2 | 0 | 0.0% |
| Jogador 5 | 1 | 1 | 0 | 0.0% |
| Jogador 6 | 2 | 2 | 0 | 0.0% |
| Jogador 7 | 1 | 1 | 0 | 0.0% |
| Jogador 8 | 1 | 1 | 0 | 0.0% |

Os detalhes por transição permanecem nos dados estruturados de origem. ‘Sem ganho mensurável’ indica falta de evidência nos campos disponíveis, não prova de decisão ruim.

## Qualidade estrutural e posicionamento do tabuleiro

| Jogador | Ações com métrica | Ganhos | Pioras | Neutras | Δ score combinado | Estrutural médio | Δ estrutural médio | Posicional médio | Δ posicional médio | Δ score c/ combate + | Δ score c/ combate - |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 163 | 32 | 28 | 103 | -0.0005 | 0.3595 | -0.0017 | 0.2180 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 1 — ganho médio por ação: BUY: Δ -0.0268 (68 ações), BUY_XP: Δ 0.0061 (8 ações), CRAFT_AND_EQUIP: Δ 0.0619 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (4 ações), MOVE_BENCH: Δ 0.0103 (17 ações), MOVE_BOARD: Δ 0.0419 (17 ações), PASS: Δ 0.0000 (7 ações), SELL: Δ 0.0106 (35 ações)
| Jogador 2 | 105 | 17 | 15 | 73 | 0.0005 | 0.1574 | -0.0054 | 0.3912 | 0.0058 | 0.0000 | 0.0000 |
- Jogador 2 — ganho médio por ação: BUY: Δ -0.0127 (47 ações), BUY_XP: Δ 0.0244 (2 ações), CRAFT_AND_EQUIP: Δ 0.0000 (5 ações), MOVE_BENCH: Δ 0.0289 (10 ações), MOVE_BOARD: Δ 0.0142 (9 ações), PASS: Δ 0.0000 (5 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0069 (26 ações)
| Jogador 3 | 130 | 31 | 27 | 72 | 0.0015 | 0.1925 | 0.0002 | 0.2213 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 3 — ganho médio por ação: BUY: Δ -0.0279 (53 ações), BUY_XP: Δ 0.0000 (2 ações), CRAFT_AND_EQUIP: Δ 0.0135 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (1 ações), MOVE_BENCH: Δ 0.0422 (17 ações), MOVE_BOARD: Δ 0.0205 (21 ações), PASS: Δ 0.0000 (6 ações), SELL: Δ 0.0184 (23 ações)
| Jogador 4 | 118 | 23 | 23 | 72 | 0.0005 | 0.1334 | -0.0025 | 0.2515 | 0.0030 | 0.0000 | 0.0000 |
- Jogador 4 — ganho médio por ação: BUY: Δ -0.0232 (47 ações), BUY_XP: Δ 0.0081 (6 ações), CRAFT_AND_EQUIP: Δ 0.0043 (7 ações), MOVE_BENCH: Δ 0.0444 (14 ações), MOVE_BOARD: Δ 0.0179 (15 ações), PASS: Δ 0.0000 (7 ações), REROLL: Δ 0.0000 (2 ações), SELL: Δ 0.0090 (20 ações)
| Jogador 5 | 142 | 18 | 18 | 106 | 0.0025 | 0.1035 | -0.0004 | 0.3512 | 0.0029 | 0.0000 | 0.0000 |
- Jogador 5 — ganho médio por ação: BUY: Δ -0.0101 (64 ações), BUY_XP: Δ 0.0122 (4 ações), CRAFT_AND_EQUIP: Δ 0.0035 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0216 (12 ações), MOVE_BOARD: Δ 0.0739 (5 ações), PASS: Δ 0.0000 (6 ações), REROLL: Δ 0.0000 (1 ações), SELL: Δ 0.0075 (40 ações)
| Jogador 6 | 126 | 27 | 27 | 72 | 0.0055 | -0.9697 | 0.0043 | 0.5183 | 0.0012 | 0.0000 | 0.0000 |
- Jogador 6 — ganho médio por ação: BUY: Δ 0.0033 (48 ações), BUY_XP: Δ 0.0009 (13 ações), CRAFT_AND_EQUIP: Δ 0.0709 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (2 ações), MOVE_BENCH: Δ -0.0005 (17 ações), MOVE_BOARD: Δ -0.0702 (8 ações), PASS: Δ 0.0000 (7 ações), SELL: Δ 0.0250 (24 ações)
| Jogador 7 | 168 | 27 | 31 | 110 | -0.0017 | 0.1390 | -0.0034 | 0.2901 | 0.0017 | 0.0000 | 0.0000 |
- Jogador 7 — ganho médio por ação: BUY: Δ -0.0233 (65 ações), BUY_XP: Δ 0.0000 (8 ações), CRAFT_AND_EQUIP: Δ 0.0086 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0040 (15 ações), MOVE_BENCH: Δ 0.0137 (16 ações), MOVE_BOARD: Δ 0.0162 (22 ações), PASS: Δ 0.0000 (7 ações), SELL: Δ 0.0193 (28 ações)
| Jogador 8 | 141 | 30 | 22 | 89 | 0.0065 | 0.2140 | 0.0031 | 0.3552 | 0.0033 | 0.0000 | 0.0000 |
- Jogador 8 — ganho médio por ação: BUY: Δ -0.0046 (71 ações), CRAFT_AND_EQUIP: Δ 0.0245 (7 ações), EQUIP_FROM_INVENTORY: Δ 0.0000 (3 ações), MOVE_BENCH: Δ 0.0140 (16 ações), MOVE_BOARD: Δ 0.0723 (5 ações), PASS: Δ 0.0000 (4 ações), SELL: Δ 0.0137 (35 ações)
- Jogador 1 — rounds avaliados: 37; correlação estrutural/combate: -0.125; posicional/combate: 0.032.
- Jogador 1 — combate positive: score estrutural prévio 0.378
  score posicional prévio 0.230
- Jogador 1 — combate negative: score estrutural prévio 0.521
  score posicional prévio 0.221
- Jogador 2 — rounds avaliados: 23; correlação estrutural/combate: 0.032; posicional/combate: -0.111.
- Jogador 2 — combate positive: score estrutural prévio 0.459
  score posicional prévio 0.408
- Jogador 2 — combate negative: score estrutural prévio 0.243
  score posicional prévio 0.415
- Jogador 3 — rounds avaliados: 30; correlação estrutural/combate: 0.128; posicional/combate: 0.116.
- Jogador 3 — combate positive: score estrutural prévio 0.226
  score posicional prévio 0.243
- Jogador 3 — combate negative: score estrutural prévio 0.189
  score posicional prévio 0.226
- Jogador 4 — rounds avaliados: 27; correlação estrutural/combate: 0.101; posicional/combate: -0.069.
- Jogador 4 — combate positive: score estrutural prévio 0.197
  score posicional prévio 0.275
- Jogador 4 — combate negative: score estrutural prévio 0.151
  score posicional prévio 0.264
- Jogador 5 — rounds avaliados: 34; correlação estrutural/combate: -0.230; posicional/combate: -0.069.
- Jogador 5 — combate positive: score estrutural prévio 0.093
  score posicional prévio 0.357
- Jogador 5 — combate negative: score estrutural prévio 0.198
  score posicional prévio 0.366
- Jogador 6 — rounds avaliados: 30; correlação estrutural/combate: -0.200; posicional/combate: 0.210.
- Jogador 6 — combate positive: score estrutural prévio -1.040
  score posicional prévio 0.548
- Jogador 6 — combate negative: score estrutural prévio -0.843
  score posicional prévio 0.495
- Jogador 7 — rounds avaliados: 37; correlação estrutural/combate: 0.110; posicional/combate: -0.222.
- Jogador 7 — combate positive: score estrutural prévio 0.217
  score posicional prévio 0.281
- Jogador 7 — combate negative: score estrutural prévio 0.160
  score posicional prévio 0.336
- Jogador 8 — rounds avaliados: 31; correlação estrutural/combate: 0.250; posicional/combate: -0.358.
- Jogador 8 — combate positive: score estrutural prévio 0.577
  score posicional prévio 0.334
- Jogador 8 — combate negative: score estrutural prévio 0.249
  score posicional prévio 0.387

A pontuação é uma heurística para auditoria. A correlação usa o estado pré-combate e a recompensa real do round; amostras pequenas são descritivas e correlação não prova causalidade.

## Auditoria de itens e componentes

| Jogador | Snapshots | Com evidência | Itens equipados no tabuleiro | Itens no banco | Itens na bolsa | Componentes | Pico de itens equipados | Pico bolsa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 200 | OK (200) | 8 | 0 | 0 | 0 | 8 | 3 |
- Jogador 1 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_HextechGunblade, TFT_Item_InfinityEdge, TFT_Item_IonicSpark, TFT_Item_Morellonomicon, TFT_Item_RapidFireCannon, TFT_Item_RedBuff, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 1 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_TearOfTheGoddess.
| Jogador 2 | 127 | OK (127) | 5 | 0 | 0 | 1 | 5 | 0 |
- Jogador 2 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_Crownguard, TFT_Item_LastWhisper, TFT_Item_PowerGauntlet, TFT_Item_RunaansHurricane; eventos: COMPONENT_LOOT_GRANTED: 24.
- Jogador 2 — bigornas: 0 escolhas; craft/equip: 5 (conversões observadas: 2); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 3 | 159 | OK (159) | 7 | 0 | 0 | 0 | 7 | 1 |
- Jogador 3 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_InfinityEdge, TFT_Item_NightHarvester, TFT_Item_Redemption, TFT_Item_SteraksGage, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 3 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 4 | 144 | OK (144) | 7 | 0 | 0 | 0 | 7 | 0 |
- Jogador 4 — IDs equipados observados: TFT_Item_Bloodthirster, TFT_Item_BlueBuff, TFT_Item_JeweledGauntlet, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 4 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 5 | 175 | OK (175) | 8 | 0 | 0 | 0 | 8 | 2 |
- Jogador 5 — IDs equipados observados: TFT_Item_Crownguard, TFT_Item_GuinsoosRageblade, TFT_Item_IonicSpark, TFT_Item_MadredsBloodrazor, TFT_Item_NightHarvester, TFT_Item_PowerGauntlet, TFT_Item_SpectralGauntlet; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 5 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves.
| Jogador 6 | 155 | OK (155) | 4 | 3 | 0 | 0 | 7 | 2 |
- Jogador 6 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_ArchangelsStaff, TFT_Item_GargoyleStoneplate, TFT_Item_HextechGunblade, TFT_Item_PowerGauntlet, TFT_Item_SteraksGage; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 6 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 7 | 205 | OK (205) | 8 | 0 | 0 | 0 | 8 | 4 |
- Jogador 7 — IDs equipados observados: TFT_Item_Quicksilver, TFT_Item_RabadonsDeathcap, TFT_Item_RedBuff, TFT_Item_Redemption, TFT_Item_SpectralGauntlet, TFT_Item_StatikkShiv, TFT_Item_TitansResolve; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 7 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_ChainVest, TFT_Item_GiantsBelt, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.
| Jogador 8 | 171 | OK (171) | 7 | 0 | 0 | 0 | 7 | 3 |
- Jogador 8 — IDs equipados observados: TFT_Item_AdaptiveHelm, TFT_Item_DragonsClaw, TFT_Item_GuinsoosRageblade, TFT_Item_RabadonsDeathcap, TFT_Item_SteraksGage, TFT_Item_ThiefsGloves; eventos: COMPONENT_LOOT_GRANTED: 31.
- Jogador 8 — bigornas: 0 escolhas; craft/equip: 7 (conversões observadas: 3); componentes persistentes entre rounds: TFT_Item_BFSword, TFT_Item_GiantsBelt, TFT_Item_NeedlesslyLargeRod, TFT_Item_NegatronCloak, TFT_Item_RecurveBow, TFT_Item_SparringGloves, TFT_Item_TearOfTheGoddess.

Os totais finais vêm do último snapshot disponível; picos e IDs distintos são métricas de observação, não inventário atual.

## Evolução estratégica por jogador e estágio

| Jogador | Estágio | Ações | Força tabuleiro Δ | Potencial banco Δ | 2★+ no tabuleiro | Pares totais | Ocupação | Ouro início → fim | Gasto | Nível início → fim | Δ posicionamento médio | Recompensa combate média |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---:|
| Jogador 1 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.110 | 0.000 |
| Jogador 1 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.001 | 0.000 |
| Jogador 1 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 1 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.012 | 0.000 |
| Jogador 1 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 6 | 5 | 4 → 4 | -0.012 | 0.366 |
| Jogador 1 | 2-2 | 9 | 2.000 | 0.000 | 0 → 0 | 3 → 3 | 14% → 18% | 6 → 8 | 9 | 4 → 5 | -0.030 | 0.293 |
| Jogador 1 | 2-3 | 8 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 8 → 5 | 11 | 5 → 5 | 0.000 | -0.323 |
| Jogador 1 | 2-4 | 4 | 2.000 | 4.000 | 0 → 1 | 3 → 2 | 18% → 18% | 5 → 6 | 4 | 5 → 5 | 0.007 | 0.000 |
| Jogador 1 | 2-5 | 8 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 8 | 10 | 5 → 6 | 0.006 | 0.320 |
| Jogador 1 | 2-6 | 7 | 6.000 | -2.000 | 1 → 1 | 2 → 3 | 18% → 21% | 8 → 9 | 8 | 6 → 6 | 0.065 | 0.393 |
| Jogador 1 | 2-7 | 3 | -2.000 | 2.000 | 1 → 2 | 3 → 2 | 21% → 18% | 9 → 14 | 1 | 6 → 6 | 0.069 | 0.000 |
| Jogador 1 | 3-1 | 7 | 4.000 | -4.000 | 2 → 2 | 2 → 2 | 18% → 21% | 14 → 13 | 8 | 6 → 6 | -0.001 | 0.402 |
| Jogador 1 | 3-2 | 3 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 21% → 21% | 13 → 18 | 3 | 6 → 6 | 0.104 | 0.983 |
| Jogador 1 | 3-3 | 5 | 0.000 | 6.000 | 2 → 2 | 2 → 2 | 21% → 21% | 18 → 24 | 3 | 6 → 6 | -0.101 | 0.553 |
| Jogador 1 | 3-4 | 3 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 24 → 31 | 2 | 6 → 6 | 0.160 | 0.000 |
| Jogador 1 | 3-5 | 7 | 2.000 | 0.000 | 2 → 2 | 2 → 1 | 21% → 21% | 31 → 39 | 3 | 6 → 6 | -0.001 | 0.409 |
| Jogador 1 | 3-6 | 3 | 0.000 | 6.000 | 2 → 2 | 1 → 2 | 21% → 21% | 39 → 44 | 3 | 6 → 6 | 0.000 | -0.894 |
| Jogador 1 | 3-7 | 6 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 44 → 52 | 6 | 6 → 6 | 0.023 | 0.000 |
| Jogador 1 | 4-1 | 4 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 52 → 61 | 2 | 6 → 6 | 0.000 | -0.681 |
| Jogador 1 | 4-2 | 6 | 4.000 | -4.000 | 2 → 2 | 2 → 1 | 21% → 21% | 61 → 72 | 4 | 6 → 6 | -0.040 | -0.477 |
| Jogador 1 | 4-3 | 4 | 0.000 | 6.000 | 2 → 2 | 1 → 2 | 21% → 21% | 72 → 80 | 3 | 6 → 7 | 0.012 | 0.746 |
| Jogador 1 | 4-4 | 6 | 4.000 | -6.000 | 2 → 2 | 2 → 2 | 21% → 25% | 80 → 91 | 3 | 7 → 7 | 0.018 | 0.000 |
| Jogador 1 | 4-5 | 4 | 0.000 | 16.000 | 2 → 2 | 2 → 2 | 25% → 25% | 91 → 95 | 8 | 7 → 7 | 0.008 | 0.778 |
| Jogador 1 | 4-6 | 6 | 0.000 | 0.000 | 2 → 2 | 2 → 4 | 25% → 25% | 95 → 107 | 6 | 7 → 7 | -0.054 | 0.502 |
| Jogador 1 | 4-7 | 4 | 0.000 | -8.000 | 2 → 2 | 4 → 4 | 25% → 25% | 107 → 122 | 3 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 5-1 | 6 | 6.000 | 0.000 | 2 → 3 | 4 → 3 | 25% → 25% | 122 → 127 | 6 | 7 → 7 | 0.043 | 0.000 |
| Jogador 1 | 5-2 | 4 | 0.000 | 6.000 | 3 → 3 | 3 → 3 | 25% → 25% | 127 → 134 | 6 | 7 → 7 | 0.000 | -0.675 |
| Jogador 1 | 5-3 | 5 | 4.000 | -2.000 | 3 → 4 | 3 → 2 | 25% → 25% | 134 → 142 | 6 | 7 → 7 | -0.036 | 0.601 |
| Jogador 1 | 5-4 | 5 | 2.000 | 2.000 | 4 → 4 | 2 → 2 | 25% → 25% | 142 → 150 | 5 | 7 → 7 | -0.116 | 0.000 |
| Jogador 1 | 5-5 | 5 | 0.000 | 2.000 | 4 → 4 | 2 → 2 | 25% → 25% | 150 → 161 | 7 | 7 → 7 | 0.000 | 0.601 |
| Jogador 1 | 5-6 | 5 | 0.000 | 0.000 | 4 → 4 | 2 → 2 | 25% → 25% | 161 → 173 | 6 | 7 → 7 | 0.000 | 0.591 |
| Jogador 1 | 5-7 | 5 | 0.000 | 0.000 | 4 → 4 | 2 → 2 | 25% → 25% | 173 → 184 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-1 | 5 | 6.000 | -12.000 | 4 → 5 | 2 → 2 | 25% → 25% | 184 → 196 | 5 | 7 → 7 | 0.010 | 0.604 |
| Jogador 1 | 6-2 | 5 | 0.000 | 8.000 | 5 → 5 | 2 → 2 | 25% → 25% | 196 → 205 | 5 | 7 → 7 | -0.012 | 0.604 |
| Jogador 1 | 6-3 | 5 | 0.000 | 6.000 | 5 → 5 | 2 → 3 | 25% → 25% | 205 → 212 | 7 | 7 → 7 | 0.012 | -0.600 |
| Jogador 1 | 6-4 | 5 | 0.000 | -2.000 | 5 → 5 | 3 → 3 | 25% → 25% | 212 → 220 | 6 | 7 → 7 | 0.000 | 0.000 |
| Jogador 1 | 6-5 | 5 | 0.000 | 8.000 | 5 → 5 | 3 → 3 | 25% → 25% | 220 → 229 | 10 | 7 → 7 | 0.012 | -0.600 |
| Jogador 1 | 6-6 | 4 | 0.000 | -4.000 | 5 → 5 | 3 → 3 | 25% → 25% | 229 → 231 | 4 | 7 → 7 | 0.000 | 0.000 |
- Jogador 1 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 17, COMPOSITION_COMPATIBILITY: 29, IMMEDIATE_UPGRADE: 9, PAIR_POTENTIAL: 13; mudanças de composição: 2; posicionamento melhorou em 40 ações e piorou em 29.
- Jogador 1 — estado final: ouro 231, nível 7, vida 11.0, colocação None.
| Jogador 2 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.161 | 0.000 |
| Jogador 2 | 1-2 | 6 | 4.000 | 0.000 | 0 → 0 | 0 → 1 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.109 | 0.000 |
| Jogador 2 | 1-3 | 5 | 0.000 | 2.000 | 0 → 1 | 1 → 0 | 11% → 7% | 2 → 3 | 2 | 3 → 3 | 0.080 | 0.000 |
| Jogador 2 | 1-4 | 8 | 2.000 | 4.000 | 1 → 1 | 0 → 1 | 7% → 11% | 3 → 4 | 3 | 3 → 4 | -0.005 | 0.000 |
| Jogador 2 | 2-1 | 9 | 2.000 | 6.000 | 1 → 1 | 1 → 2 | 11% → 14% | 4 → 5 | 5 | 4 → 4 | -0.003 | -0.257 |
| Jogador 2 | 2-2 | 9 | 0.000 | 2.000 | 1 → 1 | 2 → 1 | 14% → 14% | 5 → 6 | 8 | 4 → 4 | 0.011 | -0.276 |
| Jogador 2 | 2-3 | 5 | 2.000 | 0.000 | 1 → 1 | 1 → 1 | 14% → 18% | 6 → 7 | 5 | 4 → 5 | 0.015 | 0.551 |
| Jogador 2 | 2-4 | 4 | 0.000 | 8.000 | 1 → 1 | 1 → 2 | 18% → 18% | 7 → 8 | 4 | 5 → 5 | 0.015 | 0.000 |
| Jogador 2 | 2-5 | 8 | 0.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 8 → 13 | 9 | 5 → 5 | -0.000 | -0.323 |
| Jogador 2 | 2-6 | 7 | 0.000 | -4.000 | 1 → 1 | 2 → 2 | 18% → 18% | 13 → 22 | 6 | 5 → 5 | 0.000 | -0.332 |
| Jogador 2 | 2-7 | 3 | 0.000 | 0.000 | 1 → 1 | 2 → 3 | 18% → 18% | 22 → 30 | 1 | 5 → 5 | 0.001 | 0.000 |
| Jogador 2 | 3-1 | 7 | 0.000 | -14.000 | 1 → 1 | 3 → 2 | 18% → 18% | 30 → 46 | 2 | 5 → 5 | -0.000 | -0.411 |
| Jogador 2 | 3-2 | 3 | 0.000 | 2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 46 → 54 | 2 | 5 → 5 | -0.043 | -0.862 |
| Jogador 2 | 3-3 | 7 | 0.000 | 8.000 | 1 → 1 | 2 → 2 | 18% → 18% | 54 → 62 | 8 | 5 → 5 | 0.081 | 0.409 |
| Jogador 2 | 3-4 | 3 | 0.000 | 6.000 | 1 → 1 | 2 → 2 | 18% → 18% | 62 → 69 | 3 | 5 → 6 | 0.016 | 0.000 |
| Jogador 2 | 3-5 | 7 | 6.000 | -10.000 | 1 → 1 | 2 → 2 | 18% → 21% | 69 → 83 | 5 | 6 → 6 | 0.002 | 0.395 |
| Jogador 2 | 3-6 | 3 | 0.000 | 8.000 | 1 → 1 | 2 → 3 | 21% → 21% | 83 → 89 | 4 | 6 → 6 | 0.000 | -0.925 |
| Jogador 2 | 3-7 | 6 | 0.000 | 22.000 | 1 → 1 | 3 → 3 | 21% → 21% | 89 → 86 | 13 | 6 → 6 | 0.000 | 0.000 |
| Jogador 2 | 4-1 | 4 | 0.000 | -4.000 | 1 → 1 | 3 → 3 | 21% → 21% | 86 → 99 | 0 | 6 → 6 | 0.000 | -0.691 |
| Jogador 2 | 4-2 | 6 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 21% → 21% | 99 → 108 | 7 | 6 → 6 | 0.000 | -0.454 |
| Jogador 2 | 4-3 | 4 | 0.000 | -4.000 | 1 → 1 | 4 → 4 | 21% → 21% | 108 → 121 | 2 | 6 → 6 | 0.000 | -0.737 |
| Jogador 2 | 4-4 | 6 | 0.000 | -4.000 | 1 → 1 | 4 → 3 | 21% → 21% | 121 → 134 | 4 | 6 → 6 | -0.103 | 0.000 |
| Jogador 2 | 4-5 | 4 | -18.000 | -32.000 | 1 → 0 | 3 → 0 | 21% → 0% | 134 → 132 | 2 | 6 → 6 | -0.114 | -0.737 |
- Jogador 2 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 22, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 9; mudanças de composição: 0; posicionamento melhorou em 21 ações e piorou em 17.
- Jogador 2 — estado final: ouro 132, nível 6, vida 11.0, colocação 8.
| Jogador 3 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 3 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.060 | 0.000 |
| Jogador 3 | 1-3 | 7 | 2.000 | 0.000 | 0 → 1 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.004 | 0.000 |
| Jogador 3 | 1-4 | 6 | 0.000 | 6.000 | 1 → 1 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.002 | 0.000 |
| Jogador 3 | 2-1 | 9 | 4.000 | 4.000 | 1 → 1 | 0 → 0 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.004 | 0.290 |
| Jogador 3 | 2-2 | 4 | 0.000 | 10.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.641 |
| Jogador 3 | 2-3 | 5 | 0.000 | 6.000 | 1 → 1 | 1 → 1 | 14% → 14% | 8 → 6 | 7 | 4 → 5 | 0.006 | -0.484 |
| Jogador 3 | 2-4 | 4 | 4.000 | -2.000 | 1 → 1 | 1 → 2 | 14% → 18% | 6 → 6 | 5 | 5 → 5 | 0.026 | 0.000 |
| Jogador 3 | 2-5 | 8 | 2.000 | 0.000 | 1 → 1 | 2 → 2 | 18% → 18% | 6 → 9 | 3 | 5 → 5 | -0.042 | 0.336 |
| Jogador 3 | 2-6 | 7 | 2.000 | 6.000 | 1 → 2 | 2 → 1 | 18% → 18% | 9 → 11 | 5 | 5 → 5 | 0.003 | 0.352 |
| Jogador 3 | 2-7 | 3 | 0.000 | -4.000 | 2 → 2 | 1 → 2 | 18% → 18% | 11 → 21 | 2 | 5 → 5 | 0.020 | 0.000 |
| Jogador 3 | 3-1 | 7 | 0.000 | 6.000 | 2 → 2 | 2 → 1 | 18% → 18% | 21 → 23 | 4 | 5 → 5 | -0.010 | -0.390 |
| Jogador 3 | 3-2 | 3 | 0.000 | 2.000 | 2 → 2 | 1 → 1 | 18% → 18% | 23 → 30 | 1 | 5 → 5 | 0.015 | -0.925 |
| Jogador 3 | 3-3 | 7 | 4.000 | 0.000 | 2 → 2 | 1 → 1 | 18% → 18% | 30 → 37 | 6 | 5 → 5 | 0.028 | -0.383 |
| Jogador 3 | 3-4 | 3 | 2.000 | -2.000 | 2 → 2 | 1 → 1 | 18% → 18% | 37 → 46 | 0 | 5 → 6 | 0.018 | 0.000 |
| Jogador 3 | 3-5 | 7 | 6.000 | 2.000 | 2 → 2 | 1 → 2 | 18% → 21% | 46 → 52 | 6 | 6 → 6 | 0.024 | 0.388 |
| Jogador 3 | 3-6 | 3 | 0.000 | -4.000 | 2 → 2 | 2 → 3 | 21% → 21% | 52 → 64 | 1 | 6 → 6 | 0.000 | -0.862 |
| Jogador 3 | 3-7 | 6 | -4.000 | 10.000 | 2 → 2 | 3 → 2 | 21% → 21% | 64 → 68 | 7 | 6 → 6 | -0.030 | 0.000 |
| Jogador 3 | 4-1 | 4 | 0.000 | -12.000 | 2 → 2 | 2 → 2 | 21% → 21% | 68 → 87 | 0 | 6 → 6 | 0.015 | 0.733 |
| Jogador 3 | 4-2 | 6 | 0.000 | 6.000 | 2 → 2 | 2 → 4 | 21% → 21% | 87 → 96 | 7 | 6 → 6 | 0.000 | 0.460 |
| Jogador 3 | 4-3 | 4 | 0.000 | -6.000 | 2 → 2 | 4 → 4 | 21% → 21% | 96 → 111 | 3 | 6 → 6 | 0.000 | 0.725 |
| Jogador 3 | 4-4 | 6 | 0.000 | 4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 111 → 120 | 5 | 6 → 6 | 0.005 | 0.000 |
| Jogador 3 | 4-5 | 4 | 0.000 | -4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 120 → 134 | 2 | 6 → 6 | 0.000 | 0.690 |
| Jogador 3 | 4-6 | 6 | 0.000 | 4.000 | 2 → 2 | 4 → 4 | 21% → 21% | 134 → 142 | 6 | 6 → 6 | 0.000 | -0.475 |
| Jogador 3 | 4-7 | 4 | -2.000 | -4.000 | 2 → 2 | 4 → 2 | 21% → 21% | 142 → 151 | 4 | 6 → 6 | -0.054 | 0.000 |
| Jogador 3 | 5-1 | 6 | 0.000 | 8.000 | 2 → 2 | 2 → 2 | 21% → 21% | 151 → 158 | 4 | 6 → 6 | -0.017 | -0.450 |
| Jogador 3 | 5-2 | 4 | 0.000 | -14.000 | 2 → 2 | 2 → 3 | 21% → 21% | 158 → 178 | 1 | 6 → 6 | 0.031 | 0.721 |
| Jogador 3 | 5-3 | 5 | 0.000 | 6.000 | 2 → 2 | 3 → 3 | 21% → 21% | 178 → 185 | 6 | 6 → 6 | 0.000 | -0.600 |
| Jogador 3 | 5-4 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 2 | 21% → 21% | 185 → 195 | 3 | 6 → 6 | 0.003 | 0.000 |
| Jogador 3 | 5-5 | 5 | -26.000 | -28.000 | 2 → 0 | 2 → 0 | 21% → 0% | 195 → 189 | 9 | 6 → 6 | -0.085 | -0.540 |
- Jogador 3 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 23, IMMEDIATE_UPGRADE: 8, PAIR_POTENTIAL: 11; mudanças de composição: 1; posicionamento melhorou em 36 ações e piorou em 30.
- Jogador 3 — estado final: ouro 189, nível 6, vida 13.0, colocação 6.
| Jogador 4 | 1-1 | 5 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.001 | 0.000 |
| Jogador 4 | 1-2 | 7 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.065 | 0.000 |
| Jogador 4 | 1-3 | 6 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | -0.010 | 0.000 |
| Jogador 4 | 1-4 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | 0.013 | 0.000 |
| Jogador 4 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 1 → 2 | 11% → 14% | 5 → 5 | 5 | 4 → 4 | -0.018 | -0.346 |
| Jogador 4 | 2-2 | 5 | 2.000 | 0.000 | 0 → 0 | 2 → 3 | 14% → 18% | 5 → 6 | 5 | 4 → 5 | 0.027 | 0.547 |
| Jogador 4 | 2-3 | 9 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 18% → 18% | 6 → 6 | 9 | 5 → 5 | -0.004 | -0.264 |
| Jogador 4 | 2-4 | 4 | 0.000 | 0.000 | 0 → 0 | 3 → 3 | 18% → 18% | 6 → 7 | 8 | 5 → 5 | 0.000 | 0.000 |
| Jogador 4 | 2-5 | 8 | 0.000 | -6.000 | 0 → 0 | 3 → 3 | 18% → 18% | 7 → 12 | 9 | 5 → 6 | 0.003 | -0.322 |
| Jogador 4 | 2-6 | 7 | 2.000 | -2.000 | 0 → 0 | 3 → 3 | 18% → 21% | 12 → 14 | 6 | 6 → 6 | -0.000 | -0.369 |
| Jogador 4 | 2-7 | 3 | 0.000 | 6.000 | 0 → 1 | 3 → 2 | 21% → 18% | 14 → 17 | 4 | 6 → 6 | -0.054 | 0.000 |
| Jogador 4 | 3-1 | 7 | 6.000 | 4.000 | 1 → 1 | 2 → 2 | 18% → 21% | 17 → 19 | 5 | 6 → 6 | 0.040 | 0.416 |
| Jogador 4 | 3-2 | 3 | -2.000 | 4.000 | 1 → 1 | 2 → 1 | 21% → 18% | 19 → 23 | 2 | 6 → 6 | -0.053 | -0.925 |
| Jogador 4 | 3-3 | 7 | 0.000 | 10.000 | 1 → 3 | 1 → 1 | 18% → 18% | 23 → 24 | 6 | 6 → 6 | 0.014 | -0.383 |
| Jogador 4 | 3-4 | 3 | 6.000 | 2.000 | 3 → 3 | 1 → 2 | 18% → 21% | 24 → 28 | 4 | 6 → 6 | 0.031 | 0.000 |
| Jogador 4 | 3-5 | 7 | 0.000 | 10.000 | 3 → 3 | 2 → 1 | 21% → 21% | 28 → 29 | 7 | 6 → 6 | -0.010 | -0.383 |
| Jogador 4 | 3-6 | 3 | 0.000 | -2.000 | 3 → 3 | 1 → 2 | 21% → 21% | 29 → 40 | 3 | 6 → 6 | 0.020 | 0.954 |
| Jogador 4 | 3-7 | 6 | -2.000 | 6.000 | 3 → 3 | 2 → 1 | 21% → 21% | 40 → 43 | 5 | 6 → 6 | -0.062 | 0.000 |
| Jogador 4 | 4-1 | 4 | 0.000 | 2.000 | 3 → 3 | 1 → 2 | 21% → 21% | 43 → 53 | 1 | 6 → 6 | 0.004 | 0.713 |
| Jogador 4 | 4-2 | 6 | 0.000 | -6.000 | 3 → 3 | 2 → 2 | 21% → 21% | 53 → 68 | 3 | 6 → 6 | 0.010 | -0.430 |
| Jogador 4 | 4-3 | 4 | 0.000 | 4.000 | 3 → 3 | 2 → 3 | 21% → 21% | 68 → 77 | 3 | 6 → 6 | 0.022 | -0.704 |
| Jogador 4 | 4-4 | 6 | 0.000 | -2.000 | 3 → 3 | 3 → 3 | 21% → 21% | 77 → 89 | 4 | 6 → 6 | 0.000 | 0.000 |
| Jogador 4 | 4-5 | 4 | 0.000 | 2.000 | 3 → 3 | 3 → 3 | 21% → 21% | 89 → 99 | 4 | 6 → 6 | 0.000 | -0.646 |
| Jogador 4 | 4-6 | 6 | 0.000 | 2.000 | 3 → 3 | 3 → 3 | 21% → 21% | 99 → 107 | 8 | 6 → 6 | 0.000 | -0.454 |
| Jogador 4 | 4-7 | 4 | 0.000 | -2.000 | 3 → 3 | 3 → 4 | 21% → 21% | 107 → 117 | 4 | 6 → 7 | 0.012 | 0.000 |
| Jogador 4 | 5-1 | 6 | 2.000 | -2.000 | 3 → 3 | 4 → 4 | 21% → 25% | 117 → 128 | 2 | 7 → 7 | 0.011 | 0.477 |
| Jogador 4 | 5-2 | 4 | -22.000 | -40.000 | 3 → 0 | 4 → 0 | 25% → 0% | 128 → 124 | 6 | 7 → 7 | -0.125 | -0.683 |
- Jogador 4 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 11, COMPOSITION_COMPATIBILITY: 17, IMMEDIATE_UPGRADE: 6, PAIR_POTENTIAL: 13; mudanças de composição: 1; posicionamento melhorou em 31 ações e piorou em 25.
- Jogador 4 — estado final: ouro 124, nível 7, vida 3.0, colocação 7.
| Jogador 5 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.112 | 0.000 |
| Jogador 5 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.018 | 0.000 |
| Jogador 5 | 1-3 | 3 | 0.000 | 4.000 | 0 → 0 | 0 → 0 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 5 | 1-4 | 4 | 0.000 | 6.000 | 0 → 0 | 0 → 0 | 11% → 11% | 3 → 4 | 3 | 3 → 4 | -0.003 | 0.000 |
| Jogador 5 | 2-1 | 7 | 2.000 | 6.000 | 0 → 0 | 0 → 1 | 11% → 14% | 4 → 6 | 4 | 4 → 4 | -0.000 | 0.347 |
| Jogador 5 | 2-2 | 4 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 14% → 14% | 6 → 8 | 5 | 4 → 4 | 0.000 | 0.628 |
| Jogador 5 | 2-3 | 9 | 6.000 | -6.000 | 0 → 0 | 2 → 1 | 14% → 18% | 8 → 11 | 7 | 4 → 5 | -0.007 | 0.285 |
| Jogador 5 | 2-4 | 4 | 0.000 | 8.000 | 0 → 0 | 1 → 1 | 18% → 18% | 11 → 13 | 5 | 5 → 5 | 0.000 | 0.000 |
| Jogador 5 | 2-5 | 8 | 0.000 | 0.000 | 0 → 0 | 1 → 1 | 18% → 18% | 13 → 12 | 12 | 5 → 5 | 0.038 | 0.344 |
| Jogador 5 | 2-6 | 7 | 0.000 | -8.000 | 0 → 0 | 1 → 1 | 18% → 18% | 12 → 22 | 2 | 5 → 5 | 0.000 | -0.339 |
| Jogador 5 | 2-7 | 3 | 2.000 | 0.000 | 0 → 1 | 1 → 1 | 18% → 18% | 22 → 27 | 2 | 5 → 6 | -0.000 | 0.000 |
| Jogador 5 | 3-1 | 7 | 6.000 | 4.000 | 1 → 1 | 1 → 1 | 18% → 21% | 27 → 30 | 7 | 6 → 6 | 0.015 | 0.433 |
| Jogador 5 | 3-2 | 3 | 0.000 | 10.000 | 1 → 1 | 1 → 3 | 21% → 21% | 30 → 34 | 5 | 6 → 6 | 0.000 | 0.983 |
| Jogador 5 | 3-3 | 7 | 0.000 | -2.000 | 1 → 1 | 3 → 3 | 21% → 21% | 34 → 44 | 9 | 6 → 6 | -0.016 | 0.409 |
| Jogador 5 | 3-4 | 3 | 0.000 | 4.000 | 1 → 1 | 3 → 4 | 21% → 21% | 44 → 52 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 3-5 | 7 | 0.000 | 0.000 | 1 → 1 | 4 → 4 | 21% → 21% | 52 → 62 | 7 | 6 → 6 | 0.000 | -0.404 |
| Jogador 5 | 3-6 | 3 | 0.000 | 6.000 | 1 → 1 | 4 → 4 | 21% → 21% | 62 → 70 | 3 | 6 → 6 | 0.000 | 0.954 |
| Jogador 5 | 3-7 | 6 | 0.000 | -2.000 | 1 → 1 | 4 → 5 | 21% → 21% | 70 → 81 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 4-1 | 4 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 21% → 21% | 81 → 90 | 3 | 6 → 6 | 0.004 | 0.725 |
| Jogador 5 | 4-2 | 6 | -4.000 | 6.000 | 1 → 1 | 5 → 5 | 21% → 21% | 90 → 101 | 5 | 6 → 6 | -0.046 | 0.483 |
| Jogador 5 | 4-3 | 4 | 2.000 | -2.000 | 1 → 0 | 5 → 4 | 21% → 21% | 101 → 111 | 3 | 6 → 6 | -0.021 | -0.681 |
| Jogador 5 | 4-4 | 6 | 0.000 | -8.000 | 0 → 0 | 4 → 4 | 21% → 21% | 111 → 126 | 1 | 6 → 6 | 0.010 | 0.000 |
| Jogador 5 | 4-5 | 4 | 6.000 | -4.000 | 0 → 0 | 4 → 3 | 21% → 21% | 126 → 135 | 2 | 6 → 6 | 0.055 | -0.716 |
| Jogador 5 | 4-6 | 6 | 0.000 | 8.000 | 0 → 0 | 3 → 4 | 21% → 21% | 135 → 143 | 7 | 6 → 6 | 0.010 | -0.430 |
| Jogador 5 | 4-7 | 4 | 0.000 | 0.000 | 0 → 0 | 4 → 4 | 21% → 21% | 143 → 154 | 4 | 6 → 6 | -0.000 | 0.000 |
| Jogador 5 | 5-1 | 6 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 154 → 163 | 5 | 6 → 6 | 0.000 | 0.477 |
| Jogador 5 | 5-2 | 4 | 0.000 | -4.000 | 0 → 0 | 4 → 4 | 21% → 21% | 163 → 175 | 1 | 6 → 6 | 0.000 | 0.000 |
| Jogador 5 | 5-3 | 5 | 0.000 | 8.000 | 0 → 0 | 4 → 3 | 21% → 21% | 175 → 179 | 8 | 6 → 6 | -0.012 | 0.614 |
| Jogador 5 | 5-4 | 5 | 0.000 | 2.000 | 0 → 0 | 3 → 3 | 21% → 21% | 179 → 190 | 7 | 6 → 7 | 0.022 | 0.000 |
| Jogador 5 | 5-5 | 5 | 8.000 | -4.000 | 0 → 0 | 3 → 3 | 21% → 25% | 190 → 198 | 3 | 7 → 7 | 0.032 | -0.600 |
| Jogador 5 | 5-6 | 5 | 0.000 | 0.000 | 0 → 0 | 3 → 5 | 25% → 25% | 198 → 209 | 4 | 7 → 7 | 0.000 | -0.560 |
| Jogador 5 | 5-7 | 5 | 0.000 | 2.000 | 0 → 0 | 5 → 4 | 25% → 25% | 209 → 219 | 5 | 7 → 7 | 0.000 | 0.000 |
| Jogador 5 | 6-1 | 5 | 0.000 | -6.000 | 0 → 0 | 4 → 5 | 25% → 25% | 219 → 233 | 4 | 7 → 7 | 0.000 | -0.570 |
| Jogador 5 | 6-2 | 5 | -34.000 | -40.000 | 0 → 0 | 5 → 0 | 25% → 0% | 233 → 233 | 7 | 7 → 7 | -0.144 | -0.570 |
- Jogador 5 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 20, COMPOSITION_COMPATIBILITY: 25, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 14; mudanças de composição: 0; posicionamento melhorou em 22 ações e piorou em 19.
- Jogador 5 — estado final: ouro 233, nível 7, vida 3.0, colocação 3.
| Jogador 6 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.163 | 0.000 |
| Jogador 6 | 1-2 | 5 | 2.000 | 2.000 | 0 → 0 | 0 → 0 | 4% → 7% | 2 → 2 | 2 | 3 → 3 | 0.067 | 0.000 |
| Jogador 6 | 1-3 | 7 | 2.000 | 2.000 | 0 → 0 | 0 → 1 | 7% → 11% | 2 → 3 | 2 | 3 → 3 | -0.039 | 0.000 |
| Jogador 6 | 1-4 | 3 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 1 | 3 → 4 | 0.009 | 0.000 |
| Jogador 6 | 2-1 | 7 | 2.000 | 0.000 | 0 → 0 | 2 → 2 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.018 | -0.353 |
| Jogador 6 | 2-2 | 6 | 0.000 | 12.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | -0.010 | -0.430 |
| Jogador 6 | 2-3 | 7 | 0.000 | 6.000 | 0 → 0 | 2 → 2 | 14% → 14% | 6 → 9 | 5 | 4 → 5 | -0.005 | -0.369 |
| Jogador 6 | 2-4 | 4 | 6.000 | 2.000 | 0 → 0 | 2 → 2 | 14% → 18% | 9 → 11 | 4 | 5 → 5 | -0.020 | 0.000 |
| Jogador 6 | 2-5 | 8 | 0.000 | -10.000 | 0 → 0 | 2 → 3 | 18% → 18% | 11 → 19 | 7 | 5 → 5 | 0.016 | -0.303 |
| Jogador 6 | 2-6 | 7 | 0.000 | -4.000 | 0 → 0 | 3 → 4 | 18% → 18% | 19 → 25 | 9 | 5 → 5 | 0.008 | -0.346 |
| Jogador 6 | 2-7 | 3 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 18% → 18% | 25 → 26 | 7 | 5 → 6 | 0.010 | 0.000 |
| Jogador 6 | 3-1 | 7 | 4.000 | -4.000 | 0 → 0 | 4 → 4 | 18% → 21% | 26 → 21 | 12 | 6 → 6 | 0.027 | 0.436 |
| Jogador 6 | 3-2 | 3 | 4.000 | -8.000 | 0 → 0 | 4 → 3 | 21% → 21% | 21 → 32 | 1 | 6 → 6 | 0.010 | 0.922 |
| Jogador 6 | 3-3 | 7 | 0.000 | 10.000 | 0 → 0 | 3 → 4 | 21% → 21% | 32 → 25 | 13 | 6 → 6 | 0.000 | -0.370 |
| Jogador 6 | 3-4 | 3 | 0.000 | 2.000 | 0 → 0 | 4 → 4 | 21% → 21% | 25 → 31 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 6 | 3-5 | 7 | 6.000 | 0.000 | 0 → 0 | 4 → 5 | 21% → 25% | 31 → 19 | 19 | 6 → 7 | -0.021 | 0.429 |
| Jogador 6 | 3-6 | 3 | 0.000 | 6.000 | 0 → 0 | 5 → 5 | 25% → 25% | 19 → 24 | 3 | 7 → 7 | 0.079 | 0.922 |
| Jogador 6 | 3-7 | 6 | 0.000 | 0.000 | 0 → 0 | 5 → 4 | 25% → 25% | 24 → 32 | 9 | 7 → 7 | -0.010 | 0.000 |
| Jogador 6 | 4-1 | 4 | 0.000 | 6.000 | 0 → 0 | 4 → 4 | 25% → 25% | 32 → 39 | 3 | 7 → 7 | -0.015 | 0.725 |
| Jogador 6 | 4-2 | 6 | 0.000 | -18.000 | 0 → 0 | 4 → 3 | 25% → 25% | 39 → 59 | 3 | 7 → 7 | 0.020 | 0.483 |
| Jogador 6 | 4-3 | 4 | 0.000 | 12.000 | 0 → 0 | 3 → 4 | 25% → 25% | 59 → 66 | 6 | 7 → 7 | -0.076 | 0.778 |
| Jogador 6 | 4-4 | 6 | 0.000 | 14.000 | 0 → 0 | 4 → 4 | 25% → 25% | 66 → 71 | 7 | 7 → 7 | -0.018 | 0.000 |
| Jogador 6 | 4-5 | 4 | 0.000 | 4.000 | 0 → 0 | 4 → 4 | 25% → 25% | 71 → 79 | 3 | 7 → 7 | 0.000 | -0.694 |
| Jogador 6 | 4-6 | 6 | 0.000 | 10.000 | 0 → 0 | 4 → 4 | 25% → 25% | 79 → 85 | 9 | 7 → 7 | -0.020 | 0.483 |
| Jogador 6 | 4-7 | 4 | -2.000 | -4.000 | 0 → 0 | 4 → 3 | 25% → 25% | 85 → 95 | 3 | 7 → 7 | -0.027 | 0.000 |
| Jogador 6 | 5-1 | 6 | 0.000 | 8.000 | 0 → 1 | 3 → 2 | 25% → 21% | 95 → 99 | 6 | 7 → 7 | 0.131 | -0.450 |
| Jogador 6 | 5-2 | 4 | 6.000 | 0.000 | 1 → 1 | 2 → 2 | 21% → 25% | 99 → 107 | 3 | 7 → 7 | 0.087 | -0.708 |
| Jogador 6 | 5-3 | 5 | -2.000 | 2.000 | 1 → 1 | 2 → 0 | 25% → 18% | 107 → 114 | 4 | 7 → 7 | 0.059 | -0.580 |
| Jogador 6 | 5-4 | 5 | 8.000 | 0.000 | 1 → 1 | 0 → 0 | 18% → 21% | 114 → 121 | 4 | 7 → 7 | 0.011 | 0.000 |
| Jogador 6 | 5-5 | 5 | -38.000 | -58.000 | 1 → 0 | 0 → 0 | 21% → 0% | 121 → 123 | 6 | 7 → 7 | -0.102 | -0.570 |
- Jogador 6 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 15, COMPOSITION_COMPATIBILITY: 18, IMMEDIATE_UPGRADE: 5, PAIR_POTENTIAL: 10; mudanças de composição: 1; posicionamento melhorou em 32 ações e piorou em 31.
- Jogador 6 — estado final: ouro 123, nível 7, vida 10.0, colocação 5.
| Jogador 7 | 1-1 | 3 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | -0.026 | 0.000 |
| Jogador 7 | 1-2 | 9 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | 0.043 | 0.000 |
| Jogador 7 | 1-3 | 7 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.028 | 0.000 |
| Jogador 7 | 1-4 | 6 | 0.000 | 4.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 5 | 2 | 3 → 4 | -0.077 | 0.000 |
| Jogador 7 | 2-1 | 7 | 2.000 | 4.000 | 0 → 0 | 2 → 3 | 11% → 14% | 5 → 8 | 3 | 4 → 4 | -0.014 | 0.391 |
| Jogador 7 | 2-2 | 9 | 4.000 | -2.000 | 0 → 0 | 3 → 2 | 14% → 14% | 8 → 8 | 8 | 4 → 4 | 0.000 | -0.269 |
| Jogador 7 | 2-3 | 8 | 2.000 | 6.000 | 0 → 1 | 2 → 2 | 14% → 14% | 8 → 9 | 5 | 4 → 5 | 0.072 | 0.342 |
| Jogador 7 | 2-4 | 4 | 6.000 | 8.000 | 1 → 1 | 2 → 2 | 14% → 18% | 9 → 7 | 7 | 5 → 5 | -0.003 | 0.000 |
| Jogador 7 | 2-5 | 8 | 0.000 | -2.000 | 1 → 1 | 2 → 2 | 18% → 18% | 7 → 7 | 12 | 5 → 5 | 0.043 | 0.342 |
| Jogador 7 | 2-6 | 7 | 0.000 | 2.000 | 1 → 1 | 2 → 3 | 18% → 18% | 7 → 9 | 8 | 5 → 5 | 0.000 | 0.359 |
| Jogador 7 | 2-7 | 3 | 0.000 | 10.000 | 1 → 1 | 3 → 3 | 18% → 18% | 9 → 10 | 5 | 5 → 6 | 0.016 | 0.000 |
| Jogador 7 | 3-1 | 7 | 6.000 | 4.000 | 1 → 1 | 3 → 3 | 18% → 21% | 10 → 6 | 9 | 6 → 6 | -0.050 | -0.376 |
| Jogador 7 | 3-2 | 3 | 0.000 | 2.000 | 1 → 1 | 3 → 4 | 21% → 21% | 6 → 11 | 3 | 6 → 6 | 0.000 | -0.862 |
| Jogador 7 | 3-3 | 7 | 0.000 | 2.000 | 1 → 1 | 4 → 4 | 21% → 21% | 11 → 8 | 12 | 6 → 6 | 0.070 | 0.402 |
| Jogador 7 | 3-4 | 3 | 0.000 | -2.000 | 1 → 1 | 4 → 5 | 21% → 21% | 8 → 14 | 2 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 3-5 | 7 | 0.000 | 4.000 | 1 → 1 | 5 → 5 | 21% → 21% | 14 → 13 | 8 | 6 → 6 | -0.014 | -0.362 |
| Jogador 7 | 3-6 | 3 | 0.000 | 0.000 | 1 → 1 | 5 → 6 | 21% → 21% | 13 → 20 | 3 | 6 → 6 | 0.000 | 0.983 |
| Jogador 7 | 3-7 | 6 | 0.000 | -8.000 | 1 → 1 | 6 → 6 | 21% → 21% | 20 → 31 | 3 | 6 → 6 | 0.000 | 0.000 |
| Jogador 7 | 4-1 | 4 | 0.000 | 4.000 | 1 → 1 | 6 → 6 | 21% → 21% | 31 → 36 | 2 | 6 → 6 | 0.000 | -0.669 |
| Jogador 7 | 4-2 | 6 | 0.000 | 0.000 | 1 → 1 | 6 → 6 | 21% → 21% | 36 → 45 | 2 | 6 → 6 | -0.112 | -0.454 |
| Jogador 7 | 4-3 | 4 | 0.000 | -4.000 | 1 → 1 | 6 → 6 | 21% → 21% | 45 → 57 | 4 | 6 → 7 | 0.012 | -0.691 |
| Jogador 7 | 4-4 | 6 | 4.000 | 8.000 | 1 → 1 | 6 → 5 | 21% → 25% | 57 → 58 | 9 | 7 → 7 | 0.017 | 0.000 |
| Jogador 7 | 4-5 | 4 | 0.000 | 6.000 | 1 → 1 | 5 → 5 | 25% → 25% | 58 → 66 | 3 | 7 → 7 | -0.005 | 0.758 |
| Jogador 7 | 4-6 | 6 | -8.000 | -4.000 | 1 → 1 | 5 → 2 | 25% → 18% | 66 → 77 | 7 | 7 → 7 | -0.042 | 0.000 |
| Jogador 7 | 4-7 | 4 | 10.000 | -10.000 | 1 → 2 | 2 → 1 | 18% → 21% | 77 → 85 | 2 | 7 → 7 | 0.006 | 0.000 |
| Jogador 7 | 5-1 | 6 | 10.000 | 10.000 | 2 → 2 | 1 → 1 | 21% → 25% | 85 → 87 | 10 | 7 → 7 | -0.001 | 0.489 |
| Jogador 7 | 5-2 | 4 | 0.000 | 10.000 | 2 → 2 | 1 → 3 | 25% → 25% | 87 → 94 | 5 | 7 → 7 | 0.011 | 0.715 |
| Jogador 7 | 5-3 | 5 | 0.000 | -10.000 | 2 → 2 | 3 → 3 | 25% → 25% | 94 → 113 | 1 | 7 → 7 | 0.012 | 0.634 |
| Jogador 7 | 5-4 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 3 | 25% → 25% | 113 → 125 | 2 | 7 → 7 | 0.012 | 0.000 |
| Jogador 7 | 5-5 | 5 | 0.000 | -6.000 | 2 → 2 | 3 → 4 | 25% → 25% | 125 → 143 | 3 | 7 → 7 | 0.047 | 0.637 |
| Jogador 7 | 5-6 | 5 | 0.000 | 4.000 | 2 → 2 | 4 → 3 | 25% → 25% | 143 → 152 | 6 | 7 → 7 | -0.031 | 0.617 |
| Jogador 7 | 5-7 | 5 | 0.000 | 0.000 | 2 → 2 | 3 → 2 | 25% → 25% | 152 → 164 | 9 | 7 → 7 | 0.002 | 0.000 |
| Jogador 7 | 6-1 | 5 | 0.000 | 10.000 | 2 → 2 | 2 → 2 | 25% → 25% | 164 → 170 | 7 | 7 → 7 | -0.012 | 0.000 |
| Jogador 7 | 6-2 | 5 | 0.000 | -12.000 | 2 → 2 | 2 → 2 | 25% → 25% | 170 → 191 | 0 | 7 → 7 | 0.012 | 0.000 |
| Jogador 7 | 6-3 | 5 | 0.000 | 4.000 | 2 → 2 | 2 → 4 | 25% → 25% | 191 → 204 | 6 | 7 → 7 | 0.012 | 0.639 |
| Jogador 7 | 6-4 | 5 | 0.000 | 2.000 | 2 → 2 | 4 → 3 | 25% → 25% | 204 → 213 | 6 | 7 → 7 | -0.016 | 0.000 |
| Jogador 7 | 6-5 | 5 | 0.000 | -2.000 | 2 → 2 | 3 → 3 | 25% → 25% | 213 → 230 | 5 | 7 → 7 | 0.012 | 0.639 |
| Jogador 7 | 6-6 | 4 | -2.000 | -4.000 | 2 → 2 | 3 → 2 | 25% → 21% | 230 → 232 | 1 | 7 → 7 | -0.065 | 0.000 |
- Jogador 7 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 16, COMPOSITION_COMPATIBILITY: 21, IMMEDIATE_UPGRADE: 12, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 35 ações e piorou em 31.
- Jogador 7 — estado final: ouro 232, nível 7, vida 33.0, colocação None.
| Jogador 8 | 1-1 | 4 | 2.000 | -2.000 | 0 → 0 | 0 → 0 | 0% → 4% | 0 → 2 | 0 | 2 → 3 | 0.113 | 0.000 |
| Jogador 8 | 1-2 | 8 | 4.000 | 0.000 | 0 → 0 | 0 → 0 | 4% → 11% | 2 → 2 | 2 | 3 → 3 | -0.074 | 0.000 |
| Jogador 8 | 1-3 | 4 | 0.000 | 4.000 | 0 → 0 | 0 → 1 | 11% → 11% | 2 → 3 | 2 | 3 → 3 | 0.000 | 0.000 |
| Jogador 8 | 1-4 | 7 | 0.000 | 2.000 | 0 → 0 | 1 → 2 | 11% → 11% | 3 → 6 | 3 | 3 → 4 | 0.007 | 0.000 |
| Jogador 8 | 2-1 | 9 | 6.000 | 0.000 | 0 → 2 | 2 → 0 | 11% → 14% | 6 → 6 | 5 | 4 → 4 | -0.002 | -0.287 |
| Jogador 8 | 2-2 | 9 | 0.000 | 12.000 | 2 → 1 | 0 → 0 | 14% → 14% | 6 → 6 | 7 | 4 → 4 | 0.002 | -0.264 |
| Jogador 8 | 2-3 | 9 | 2.000 | 8.000 | 1 → 1 | 0 → 0 | 14% → 14% | 6 → 6 | 6 | 4 → 4 | 0.035 | 0.279 |
| Jogador 8 | 2-4 | 4 | 0.000 | 4.000 | 1 → 1 | 0 → 1 | 14% → 14% | 6 → 10 | 4 | 4 → 4 | 0.015 | 0.000 |
| Jogador 8 | 2-5 | 8 | 0.000 | 4.000 | 1 → 1 | 1 → 2 | 14% → 14% | 10 → 13 | 7 | 4 → 5 | -0.057 | -0.316 |
| Jogador 8 | 2-6 | 7 | 8.000 | -6.000 | 1 → 2 | 2 → 3 | 14% → 18% | 13 → 19 | 4 | 5 → 5 | 0.150 | 0.366 |
| Jogador 8 | 2-7 | 3 | 0.000 | 0.000 | 2 → 2 | 3 → 4 | 18% → 18% | 19 → 25 | 3 | 5 → 5 | 0.000 | 0.000 |
| Jogador 8 | 3-1 | 7 | 0.000 | 4.000 | 2 → 2 | 4 → 4 | 18% → 18% | 25 → 30 | 8 | 5 → 5 | 0.000 | -0.409 |
| Jogador 8 | 3-2 | 3 | 0.000 | -2.000 | 2 → 2 | 4 → 5 | 18% → 18% | 30 → 40 | 1 | 5 → 5 | 0.000 | 0.922 |
| Jogador 8 | 3-3 | 7 | 0.000 | 2.000 | 2 → 2 | 5 → 3 | 18% → 18% | 40 → 47 | 7 | 5 → 5 | 0.000 | -0.377 |
| Jogador 8 | 3-4 | 3 | 0.000 | -2.000 | 2 → 2 | 3 → 2 | 18% → 18% | 47 → 56 | 1 | 5 → 5 | -0.020 | 0.000 |
| Jogador 8 | 3-5 | 7 | 0.000 | 12.000 | 2 → 2 | 2 → 3 | 18% → 18% | 56 → 59 | 10 | 5 → 5 | 0.000 | -0.370 |
| Jogador 8 | 3-6 | 3 | 2.000 | -10.000 | 2 → 2 | 3 → 2 | 18% → 18% | 59 → 74 | 1 | 5 → 5 | -0.011 | -0.894 |
| Jogador 8 | 3-7 | 6 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 18% → 18% | 74 → 84 | 4 | 5 → 5 | 0.010 | 0.000 |
| Jogador 8 | 4-1 | 4 | 0.000 | 2.000 | 2 → 2 | 2 → 1 | 18% → 18% | 84 → 92 | 3 | 5 → 6 | 0.041 | -0.681 |
| Jogador 8 | 4-2 | 6 | 6.000 | 8.000 | 2 → 2 | 1 → 1 | 18% → 21% | 92 → 96 | 7 | 6 → 6 | 0.000 | 0.506 |
| Jogador 8 | 4-3 | 4 | 0.000 | -4.000 | 2 → 2 | 1 → 2 | 21% → 21% | 96 → 111 | 3 | 6 → 6 | 0.015 | 0.733 |
| Jogador 8 | 4-4 | 6 | 0.000 | 4.000 | 2 → 2 | 2 → 2 | 21% → 21% | 111 → 120 | 6 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 4-5 | 4 | 0.000 | -4.000 | 2 → 2 | 2 → 3 | 21% → 21% | 120 → 134 | 2 | 6 → 6 | 0.000 | 0.738 |
| Jogador 8 | 4-6 | 6 | 2.000 | -8.000 | 2 → 2 | 3 → 2 | 21% → 21% | 134 → 148 | 6 | 6 → 6 | -0.003 | 0.460 |
| Jogador 8 | 4-7 | 4 | 0.000 | 8.000 | 2 → 2 | 2 → 2 | 21% → 21% | 148 → 155 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-1 | 6 | 0.000 | -2.000 | 2 → 2 | 2 → 3 | 21% → 21% | 155 → 166 | 3 | 6 → 6 | 0.000 | -0.464 |
| Jogador 8 | 5-2 | 4 | 0.000 | 4.000 | 2 → 2 | 3 → 4 | 21% → 21% | 166 → 175 | 5 | 6 → 6 | 0.001 | 0.746 |
| Jogador 8 | 5-3 | 5 | 0.000 | 0.000 | 2 → 2 | 4 → 4 | 21% → 21% | 175 → 185 | 3 | 6 → 6 | 0.000 | -0.570 |
| Jogador 8 | 5-4 | 5 | 0.000 | 2.000 | 2 → 2 | 4 → 3 | 21% → 21% | 185 → 194 | 5 | 6 → 6 | 0.000 | 0.000 |
| Jogador 8 | 5-5 | 5 | 0.000 | -4.000 | 2 → 2 | 3 → 4 | 21% → 21% | 194 → 207 | 2 | 6 → 6 | 0.000 | 0.572 |
| Jogador 8 | 5-6 | 5 | -32.000 | -42.000 | 2 → 0 | 4 → 0 | 21% → 0% | 207 → 204 | 4 | 6 → 6 | -0.209 | -0.586 |
- Jogador 8 — valor marginal das compras: BENCH_POTENTIAL_ONLY: 20, COMPOSITION_COMPATIBILITY: 24, IMMEDIATE_UPGRADE: 11, PAIR_POTENTIAL: 16; mudanças de composição: 0; posicionamento melhorou em 34 ações e piorou em 24.
- Jogador 8 — estado final: ouro 204, nível 6, vida 3.0, colocação 4.

Força do banco e pares representam potencial futuro, não força atual de combate. Classificações marginais são diagnósticas e não alteram a recompensa PPO; valide-as contra resultados de combate.

## Auditoria de compras e vendas

| Jogador | Compras | Vendas | Impulsivas ≤1 ação | ≤2 ações | ≤4 ações | Par/upgrade | Experimentais | Mudança comp. | Banco cheio | Necessidade econômica | Revisão | Ouro perdido |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jogador 1 | 68 | 35 | 0 | 0 | 0 | 0 | 0 | 1 | 14 | 1 | 1 | 0 |
| Jogador 2 | 47 | 26 | 0 | 2 | 3 | 0 | 1 | 0 | 4 | 1 | 5 | 0 |
| Jogador 3 | 53 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| Jogador 4 | 47 | 20 | 1 | 1 | 1 | 0 | 0 | 0 | 5 | 2 | 2 | 0 |
| Jogador 5 | 64 | 40 | 0 | 0 | 1 | 2 | 0 | 1 | 15 | 0 | 1 | 0 |
| Jogador 6 | 48 | 24 | 0 | 1 | 1 | 2 | 1 | 1 | 2 | 0 | 2 | 0 |
| Jogador 7 | 65 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| Jogador 8 | 71 | 35 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 1 | 0 |
- Jogador 1 — venda DA_18_Akali_AD (2-5, step 79): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 1 — venda DA_18_Akali_AD (4-2, step 135): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 2 — venda DA_18_RekSai (3-1, step 97): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 3 — venda DA_18_RekSai (3-7, step 122): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 3 — venda DA_Scuttlecrab18 (4-5, step 150): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_KogMaw18_AD (2-5, step 79): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 4 — venda DA_Karma18 (2-6, step 86): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 4 — venda DA_18_Cassiopeia (4-5, step 149): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Rakan (2-6, step 85): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Tristana (4-3, step 138): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 5 — venda DA_18_RekSai (4-4, step 142): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_18_Kobuko (5-2, step 170): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 5 — venda DA_CrimsonRaptor18 (5-7, step 192): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_Gromp18_AP (2-5, step 78): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Sentry (3-2, step 100): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 6 — venda DA_18_Yorick (3-7, step 125): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_KogMaw18_AD (4-2, step 135): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Kayle (4-2, step 136): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 6 — venda DA_18_Tristana (5-5, step 183): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 7 — venda DA_18_Camille (2-6, step 84): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rammus (3-7, step 124): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Hecarim (5-3, step 172): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_18_Rakan (5-4, step 177): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 7 — venda DA_KogMaw18_AD (5-5, step 183): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Veigar (2-5, step 75): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=1.
- Jogador 8 — venda DA_18_Tristana (3-3, step 102): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_Karma18 (3-5, step 114): core=False, par=True, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=3.
- Jogador 8 — venda DA_18_Rakan (3-7, step 124): core=True, par=False, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.
- Jogador 8 — venda DA_18_Cassiopeia (4-6, step 154): core=True, par=False, compensada=True; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=2.
- Jogador 8 — venda DA_18_LeBlanc (5-4, step 179): core=False, par=True, compensada=False; ganho tabuleiro=False, sinergia=False, posicionamento=False, compensações posteriores=0.

Vendas de core/pares ignoradas antes da decisão da composição: **3**.
Round da decisão por jogador: Jogador 1: 2-5, Jogador 2: 2-5, Jogador 3: 2-5, Jogador 4: 2-5, Jogador 5: 2-5, Jogador 6: 2-5, Jogador 7: 2-5, Jogador 8: 2-5.
As classificações detalhadas e sequências correlacionadas permanecem nos dados estruturados de origem.
Compra/venda impulsiva exige baixo fit e baixo valor estratégico, sem par/upgrade, alternativa melhor ainda possuída, transição de composição, implantação, banco cheio ou venda que financie uma ação necessária.
Compras de alto fit sem justificativa observável ficam em UNJUSTIFIED_REVIEW, não são tratadas como impulsivas. Uma venda sem compra correspondente na janela é UNKNOWN; identidades ambíguas nunca são penalizadas automaticamente.

## Achados

| Severidade | Jogador | Round | Step | Código | Descrição |
|---|---|---:|---:|---|---|
| LOW | Jogador 1 | 2-3 | 64 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 1 | 2-5 | 79 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Akali_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 1 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 2-2 | 57 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-1 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-2 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-3 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-4 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-5 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-6 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 5-7 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 207 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 208 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 209 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 210 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-3 | 211 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 212 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 213 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 214 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 215 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-4 | 216 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-5 | 217 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-5 | 218 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-5 | 219 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-5 | 220 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-5 | 221 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-6 | 222 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-6 | 223 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-6 | 224 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 6-6 | 225 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 1 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 1 | 2-2 | 528 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-3 | 635 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-4 | 698 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-5 | 810 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 1 | 2-6 | 906 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-1 | 1052 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-2 | 1101 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-3 | 1174 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-4 | 1224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-5 | 1323 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-6 | 1375 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 3-7 | 1462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-1 | 1525 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-2 | 1619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-3 | 1682 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-4 | 1769 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-5 | 1830 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-6 | 1917 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 4-7 | 1978 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-1 | 2067 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-2 | 2132 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 2208 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-3 | 2209 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-4 | 2286 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-4 | 2287 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-5 | 2361 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-5 | 2362 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-6 | 2438 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-6 | 2439 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 5-7 | 2515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 5-7 | 2516 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-1 | 2594 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-1 | 2595 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-2 | 2674 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-2 | 2675 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-3 | 2751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-3 | 2752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-4 | 2827 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-4 | 2828 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 1 | 6-5 | 2904 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 4 tank(s) posicionados atrás. |
| LOW | Jogador 1 | 6-5 | 2905 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| MEDIUM | Jogador 1 | 3-2 | 1151 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 2 | 2-5 | 79 | PURCHASE_SALE_REVIEW | Compra de DA_18_Azir foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 2-6 | 83 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rengar) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 2 | 2-6 | 84 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_KogMaw18_AD) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 2-6 | 86 | PURCHASE_SALE_REVIEW | Compra de DA_18_Sejuani foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 2 | 3-1 | 94 | PURCHASE_SALE_REVIEW | Compra de DA_18_Teemo foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 3-1 | 97 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_RekSai' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 2 | 3-3 | 107 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| LOW | Jogador 2 | 3-5 | 114 | PURCHASE_SALE_REVIEW | Compra de DA_18_Warwick foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 2 | 3-5 | 115 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Teemo) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 2 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 2 | 1-2 | 140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 2 | 4-5 | 1862 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 2 | 4-5 | 1863 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 3 | 4-5 | 150 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Scuttlecrab18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 3 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-5 | 770 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-6 | 866 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 2-7 | 914 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-1 | 1013 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-2 | 1064 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 3-4 | 1216 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-5 | 1316 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-6 | 1367 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 3-7 | 1454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-1 | 1517 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-2 | 1603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 4-3 | 1666 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 3 | 5-5 | 2359 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 3 | 5-5 | 2360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 2-5 | 75 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_Fiddlesticks18) vendida após 1 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 4 | 2-5 | 78 | PURCHASE_SALE_REVIEW | Compra de DA_18_Yunara foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 4 | 2-5 | 79 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 2-6 | 84 | PURCHASE_SALE_REVIEW | Compra de DA_18_Veigar foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 4 | 4-5 | 149 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Cassiopeia' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 4 | 1-1 | 68 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 2-7 | 910 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 3-4 | 1204 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-5 | 1305 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-6 | 1355 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 3-7 | 1442 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-1 | 1506 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-1 | 1507 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-2 | 1597 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-2 | 1598 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 4-3 | 1663 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-4 | 1751 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-5 | 1815 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-6 | 1901 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 4-7 | 1963 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-1 | 2051 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 4 | 5-2 | 2115 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 4 | 5-2 | 2116 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 4 | 4-1 | 1574 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| MEDIUM | Jogador 5 | 2-6 | 85 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rakan' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 2-6 | 85 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_Rakan) vendida após 3 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| LOW | Jogador 5 | 3-1 | 95 | PURCHASE_SALE_REVIEW | Compra de DA_18_Teemo foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 5 | 4-4 | 142 | SOLD_CORE_UNIT | Venda de 'DA_18_RekSai' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-2 | 170 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kobuko' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 5 | 5-7 | 192 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_CrimsonRaptor18' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 5 | 2-1 | 47 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 48 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-1 | 51 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-2 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 67 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 68 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-3 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-5 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-6 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 2-7 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-1 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-2 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-3 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-4 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-5 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-6 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 3-7 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-3 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-4 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-5 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-6 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 4-7 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-1 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-2 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-2 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-2 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-2 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 172 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 173 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 174 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 175 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-3 | 176 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 177 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 178 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 179 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 180 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-4 | 181 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 182 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 183 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 184 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 185 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-5 | 186 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 187 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 188 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 189 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 190 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-6 | 191 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-7 | 192 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-7 | 193 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-7 | 194 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-7 | 195 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 5-7 | 196 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-1 | 197 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-1 | 198 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-1 | 199 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-1 | 200 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-1 | 201 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 202 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 203 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 204 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 205 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 6-2 | 206 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 5 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 5 | 2-3 | 547 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 2-4 | 608 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-2 | 1549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 1615 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-3 | 1616 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-4 | 1709 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 5 | 4-4 | 1710 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-5 | 1772 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-6 | 1863 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 4-7 | 1925 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-1 | 2016 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-2 | 2080 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-3 | 2157 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-4 | 2233 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-5 | 2311 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-6 | 2387 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 5-7 | 2462 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-1 | 2539 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 5 | 6-2 | 2618 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 5 | 6-2 | 2619 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 2-3 | 65 | PURCHASE_SALE_REVIEW | Compra de DA_18_Varus foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 2-5 | 78 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_Gromp18_AP' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-6 | 85 | PURCHASE_SALE_REVIEW | Compra de DA_KogMaw18_AD foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| MEDIUM | Jogador 6 | 3-7 | 124 | PURCHASE_REVERSED | Compra de baixo valor estratégico (DA_18_GnarSmall) vendida após 2 ação(ões), sem par, alternativa melhor, transição de composição ou necessidade econômica demonstrada. |
| MEDIUM | Jogador 6 | 3-7 | 125 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Yorick' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-2 | 135 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_KogMaw18_AD' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 6 | 4-2 | 136 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Kayle' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 6 | 2-2 | 52 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 53 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 54 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 55 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 56 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-2 | 60 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 61 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 62 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 63 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 64 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 65 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 66 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-3 | 69 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 70 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-5 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-6 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 2-7 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-1 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-2 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 3-7 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 6 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-1 | 57 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 6 | 1-2 | 128 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-3 | 223 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 1-4 | 270 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-1 | 367 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-2 | 451 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-3 | 549 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-4 | 611 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-5 | 719 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-6 | 818 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 2-7 | 866 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-1 | 960 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-2 | 1014 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-3 | 1111 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-4 | 1162 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-5 | 1256 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-6 | 1305 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 3-7 | 1394 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-1 | 1457 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-2 | 1543 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-3 | 1607 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-4 | 1693 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-5 | 1755 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-6 | 1843 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 4-7 | 1904 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-1 | 1991 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-2 | 2056 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 2135 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-3 | 2136 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-4 | 2215 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 6 | 5-4 | 2216 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 6 | 5-5 | 2293 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 6 | 5-5 | 2294 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| MEDIUM | Jogador 7 | 2-6 | 84 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Camille' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 7 | 3-7 | 124 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_Rammus' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-3 | 172 | SOLD_CORE_UNIT | Venda de 'DA_18_Hecarim' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-4 | 177 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| HIGH | Jogador 7 | 5-5 | 183 | SOLD_CORE_UNIT | Venda de 'DA_KogMaw18_AD' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 7 | 2-4 | 71 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 72 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-4 | 73 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 74 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 75 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 76 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 77 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 78 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 79 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 80 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-5 | 81 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 82 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 83 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 84 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 85 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 86 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 87 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-6 | 88 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 89 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 90 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 2-7 | 91 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 92 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 93 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 94 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 95 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 96 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 97 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-1 | 98 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 99 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 100 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-2 | 101 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 102 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 103 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 104 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 105 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 106 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 107 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-3 | 108 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 109 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 110 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-4 | 111 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 112 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 113 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 114 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 115 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 116 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 117 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-5 | 118 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 119 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 120 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-6 | 121 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 122 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 123 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 124 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 125 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 126 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 3-7 | 127 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 128 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 129 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 130 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-1 | 131 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 132 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 133 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 134 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 135 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 136 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-2 | 137 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 138 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 139 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 140 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-3 | 141 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 142 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 143 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 144 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 145 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 146 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-4 | 147 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 148 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 149 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 150 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-5 | 151 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 152 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 153 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 154 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 155 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 156 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-6 | 157 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 158 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 159 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 160 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 4-7 | 161 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 162 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 163 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 164 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 165 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 166 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-1 | 167 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-2 | 168 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-2 | 169 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-2 | 170 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 5-2 | 171 | FOCUS_NOT_IN_CORE_UNITS | comp_focus não aparece em core_units; confirmar se os campos deveriam coincidir. |
| LOW | Jogador 7 | 1-1 | 44 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 7 | 1-4 | 343 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-1 | 441 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 565 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 2-2 | 566 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-3 | 677 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-4 | 738 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-5 | 847 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-6 | 946 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 2-7 | 995 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-1 | 1091 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-2 | 1140 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-3 | 1235 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-4 | 1284 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-5 | 1382 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-6 | 1430 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 3-7 | 1515 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-1 | 1577 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-2 | 1661 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-2 | 1662 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-3 | 1723 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-3 | 1724 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-4 | 1814 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-4 | 1815 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-5 | 1878 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-5 | 1879 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-6 | 1972 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-6 | 1973 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 4-7 | 2034 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 4-7 | 2035 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-1 | 2122 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-1 | 2123 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-2 | 2187 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-2 | 2188 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-3 | 2267 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-3 | 2268 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-4 | 2346 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-4 | 2347 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-5 | 2423 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-5 | 2424 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-6 | 2502 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-6 | 2503 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 5-7 | 2584 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 5-7 | 2585 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-1 | 2662 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-1 | 2663 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-2 | 2743 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-2 | 2744 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-3 | 2822 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-3 | 2823 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-4 | 2900 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-4 | 2901 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| LOW | Jogador 7 | 6-5 | 2978 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 7 | 6-5 | 2979 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 3 tank(s) posicionados atrás. |
| MEDIUM | Jogador 7 | 4-1 | 1638 | STABILIZE_PASS_WITH_GOLD_REVIEW | Possível divergência entre estratégia observada e ação; revisar HP, nível, valor marginal e alternativas que não estão totalmente disponíveis no log legado. |
| LOW | Jogador 8 | 1-4 | 38 | PURCHASE_SALE_REVIEW | Compra de DA_18_RekSai foi vendida sem justificativa confirmada; manter como revisão, não como compra impulsiva. |
| HIGH | Jogador 8 | 3-7 | 124 | SOLD_CORE_UNIT | Venda de 'DA_18_Rakan' removeu a última cópia de uma unidade core após a decisão da composição; conferir substituição e evolução de estrelas. |
| MEDIUM | Jogador 8 | 5-4 | 179 | SOLD_UPGRADE_PAIR_COPY | Venda de 'DA_18_LeBlanc' removeu uma das cópias que formavam um par do mesmo campeão/estrela após a decisão da composição; conferir substituição e evolução de estrelas. |
| LOW | Jogador 8 | 1-1 | 56 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |
| LOW | Jogador 8 | 1-2 | 163 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-3 | 224 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 1-4 | 321 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-1 | 445 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-3 | 691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-4 | 752 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-5 | 864 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-6 | 962 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 2-7 | 1010 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-1 | 1110 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-2 | 1159 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-3 | 1256 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-4 | 1305 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-5 | 1403 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-6 | 1454 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 3-7 | 1542 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 1603 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-1 | 1604 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-2 | 1691 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-2 | 1692 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-3 | 1754 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-3 | 1755 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-4 | 1844 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-4 | 1845 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-5 | 1909 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 1 carry(s) expostos na frontline. |
| LOW | Jogador 8 | 4-5 | 1910 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-6 | 1997 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 4-7 | 2060 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-1 | 2148 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-2 | 2211 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-3 | 2285 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-4 | 2360 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-5 | 2434 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: 2 tank(s) posicionados atrás. |
| LOW | Jogador 8 | 5-6 | 2511 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem frontline. |
| LOW | Jogador 8 | 5-6 | 2512 | TEXT_POSITION_WARNING | Warning de posicionamento emitido pelo Viewer: sem backline. |

## Como interpretar

- Achados CRITICAL/HIGH são sinais fortes para investigar, não prova isolada da causa.
- Troca de comp direction pode ser legítima conforme loja, unidades, nível e economia.
- A checagem de fusão conta apenas unidades compradas no tabuleiro+banco, nunca as da loja.
- Os registros estruturados são a fonte primária para estado de decisão, máscaras, política e recompensas; registros textuais legados são usados apenas quando faltam dados estruturados.
- A auditoria não pode decidir se uma compra era ótima sem comparar loja, ouro, limite do banco, máscaras e avaliação de composição no mesmo estado.
- Uma fusão só pode ser confirmada com segurança se o log registrar cópias elegíveis antes/depois e o evento de merge; contar cópias é apenas um indício.
- Alertas de posicionamento dependem de role/row nos dados; em tabuleiro achatado assume-se grade 4x7 com rows 0-1 na frontline, convenção a validar no Viewer.
- Alertas de unidade core ausente exigem três snapshots consecutivos; podem indicar estratégia em transição, então revise o contexto antes de concluir que é bug.
