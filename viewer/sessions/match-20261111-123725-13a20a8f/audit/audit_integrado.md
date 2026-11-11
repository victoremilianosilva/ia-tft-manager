# Índice integrado de auditoria

- Schema do índice: v1
- Match: 13a20a8f-ccb5-4ba2-a7bf-145ee939104c
- Jogadores: 1, 2, 3, 4, 5, 6, 7, 8
- Grupos jogador/round: 237

## Integridade dos produtores

| Produtor | Registros | Disponível |
|---|---:|---|
| Strategic Planner | 2796 | sim |
| Economic Controller | 2796 | sim |
| Economy evidence records | 1743 | sim |
| Economy evidence valid | 1035 | sim |
| Board evidence records | 1743 | sim |
| Board evidence valid | 1035 | sim |
| Item evidence records | 1743 | sim |
| Item evidence valid | 1035 | sim |
| Unit Priority | 1743 | sim |
| Lineup Planner | 1743 | sim |
| Composition Intelligence | 1743 | sim |
| Action Evaluator baseline | 1743 | sim |
| Contextual Action Evaluator | 1743 | sim |
| Ações PPO observadas | 1053 | sim |
| Outcomes | 235 | sim |

## Integridade do stream

- Envelopes de composição incompletos: 0
- Divergências de identidade no Context Bridge: 0
- Sequências duplicadas: 0
- Inversões de sequência: 0
- Lacunas de sequência: 0
- Eventos duplicados no log de jogadores: 0
- Conflitos de sequência no log de jogadores: 0
- Conflitos de sequência Composition Intelligence: 0
- Comparações baseline/contextual disponíveis: 1035
- Divergências baseline/contextual: 209
- Registros sem versão (legado): 0
- Schemas incompatíveis: 0
- Erros de parsing: 0

## Comparação observacional com PPO

| Evaluator | Comparáveis | Concordâncias | Divergências | Indisponíveis |
|---|---:|---:|---:|---:|
| Baseline | 0 | 0 | 0 | 1053 |
| Contextual | 0 | 0 | 0 | 1053 |

## Timeline correlacionada

### Jogador 1 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=1]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=57]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=65]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=73]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 7 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=81]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=161]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=169]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=177]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=19]: PASS → HOLD
- PPO observado [player_1_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 5 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=185]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=265]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=273]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=281]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=30]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=31]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=32]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=33]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=34]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 3 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=44]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=289]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=353]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=361]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=369]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=44]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=48]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 5 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=58]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=377]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=425]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=433]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=441]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=58]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=60]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=61]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=62]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=63]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 9 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=73]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=449]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=513]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=521]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=529]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=80]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=81]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=82]: SELL → SELL
- PPO observado [player_1_log.json seq=85]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=86]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 7 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=96]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=537]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=593]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=601]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=609]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=100]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=101]: SELL → SELL
- PPO observado [player_1_log.json seq=102]: SELL → SELL
- PPO observado [player_1_log.json seq=103]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=104]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=114]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=617]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=673]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=681]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=689]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=117]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=119]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=120]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=121]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=122]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 9 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=132]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=135]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=697]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=705]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=713]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=721]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=729]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=132]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=134]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=135]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 10 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=146]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=147]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=148]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=149]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=150]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=151]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=152]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=737]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=785]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=793]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=801]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=148]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=149]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=150]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=151]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=152]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 11 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=162]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=164]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=165]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=166]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=167]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=168]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=809]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=849]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=857]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=865]: baseline=MOVE · contextual=MOVE
- PPO observado [player_1_log.json seq=164]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=165]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=166]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=167]: PASS → HOLD
- PPO observado [player_1_log.json seq=168]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=178]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=180]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=873]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=881]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=889]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=897]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=178]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=180]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 13 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=190]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=192]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=193]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=194]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=197]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=198]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=199]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=905]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=953]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=961]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=969]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=193]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=194]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=197]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=198]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=199]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=209]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=977]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=977]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=985]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=993]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=209]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 15 (same_player_round)
- Strategic reviews únicos: 6 (observações=13) · PPO actions: 5 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=219]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=220]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=222]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=223]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=224]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1001]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1041]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1049]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1057]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=219]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=220]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=222]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=223]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=224]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 16 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=234]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=236]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1065]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1073]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1081]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1089]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=234]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=236]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 17 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=246]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=248]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=250]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=251]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=252]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1097]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1129]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1137]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1145]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=246]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=248]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=250]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=251]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=252]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 18 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=262]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=264]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=265]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1153]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1169]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1177]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1185]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=262]: SELL → SELL
- PPO observado [player_1_log.json seq=264]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=265]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=275]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=276]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=277]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=278]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=279]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1193]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1225]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1233]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1241]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=275]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=276]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=277]: SELL → SELL
- PPO observado [player_1_log.json seq=278]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=279]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=290]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=291]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=293]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1249]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1265]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1273]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1281]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=290]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=291]: SELL → SELL
- PPO observado [player_1_log.json seq=293]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 21 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=304]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=306]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=308]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=310]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=312]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1289]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1321]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1329]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1337]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=304]: SELL → SELL
- PPO observado [player_1_log.json seq=306]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=308]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=310]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=312]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 22 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=322]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=324]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=325]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1345]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1361]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1369]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1377]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=322]: SELL → SELL
- PPO observado [player_1_log.json seq=324]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=325]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 23 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=335]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=337]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=339]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=340]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=341]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1385]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1417]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1425]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1433]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=335]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=337]: SELL → SELL
- PPO observado [player_1_log.json seq=339]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=340]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=341]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 24 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@2
- Strategic Planner [shadow_planning seq=351]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=352]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=354]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1441]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1457]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1465]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1473]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_1_log.json seq=351]: SELL → SELL
- PPO observado [player_1_log.json seq=352]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=354]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 25 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@2
- Strategic Planner [shadow_planning seq=364]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=366]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=368]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=369]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=371]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1479]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1503]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1509]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1515]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_1_log.json seq=364]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=366]: SELL → SELL
- PPO observado [player_1_log.json seq=368]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=369]: REROLL → REROLL
- PPO observado [player_1_log.json seq=371]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 26 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Adaptador@3
- Strategic Planner [shadow_planning seq=381]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=383]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=384]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1521]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1533]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1539]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1545]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_1_log.json seq=381]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=383]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=384]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Adaptador@3
- Strategic Planner [shadow_planning seq=394]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=395]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=397]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1551]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1563]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1569]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1575]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_1_log.json seq=394]: SELL → SELL
- PPO observado [player_1_log.json seq=395]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=397]: SELL → SELL
- PPO observado [player_1_log.json seq=398]: BUY → BUY_UNIT
- Outcome observado: placement=6 (correlação, não causalidade)

### Jogador 2 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=2]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=58]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=66]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=74]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 5 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=82]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=162]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=170]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=178]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=14]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=15]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=17]: PASS → HOLD
- PPO observado [player_2_log.json seq=18]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 4 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=28]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=186]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=266]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=274]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=282]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=28]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=29]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=30]: PASS → HOLD
- PPO observado [player_2_log.json seq=31]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 7 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=41]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=290]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=354]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=362]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=370]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=46]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=47]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=48]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=49]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=50]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=60]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=378]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=426]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=434]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=442]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=63]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=64]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=65]: SELL → SELL
- PPO observado [player_2_log.json seq=66]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=67]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 9 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=77]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=450]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=514]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=522]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=530]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=84]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=85]: SELL → SELL
- PPO observado [player_2_log.json seq=87]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=88]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=89]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=99]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=538]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=594]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=602]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=610]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=99]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=100]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=101]: PASS → HOLD
- PPO observado [player_2_log.json seq=102]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=112]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=618]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=674]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=682]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=690]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=115]: SELL → SELL
- PPO observado [player_2_log.json seq=116]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=117]: SELL → SELL
- PPO observado [player_2_log.json seq=118]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=120]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 9 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=130]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=132]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=698]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=706]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=714]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=722]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=730]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=130]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=132]: SELL → SELL
- PPO observado [player_2_log.json seq=133]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 10 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=143]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=144]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=145]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=147]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=148]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=149]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=151]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=738]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=786]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=794]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=802]: baseline=HOLD · contextual=BUY_XP
- PPO observado [player_2_log.json seq=145]: SELL → SELL
- PPO observado [player_2_log.json seq=147]: SELL → SELL
- PPO observado [player_2_log.json seq=148]: SELL → SELL
- PPO observado [player_2_log.json seq=149]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=151]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 11 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=161]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=162]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=163]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=164]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=165]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=166]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=810]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=850]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=858]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=866]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=162]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=163]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=164]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=165]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=166]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 12 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=176]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=874]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=882]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=890]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=898]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=176]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=177]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 13 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=187]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=906]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=954]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=962]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=970]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=190]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=191]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=192]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=193]: SELL → SELL
- PPO observado [player_2_log.json seq=194]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=204]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=978]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=978]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=986]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=994]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=204]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 15 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=214]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1002]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1042]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1050]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1058]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=216]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=217]: SELL → SELL
- PPO observado [player_2_log.json seq=219]: SELL → SELL
- PPO observado [player_2_log.json seq=221]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=223]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 16 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=234]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1066]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1074]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1082]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1090]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=234]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=235]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 17 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=247]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1098]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1130]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1138]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1146]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=247]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=250]: SELL → SELL
- PPO observado [player_2_log.json seq=253]: SELL → SELL
- PPO observado [player_2_log.json seq=254]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=256]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 18 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=267]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1154]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1170]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1178]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1186]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=267]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=269]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=270]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=280]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=283]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=284]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=285]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=286]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1194]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1226]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1234]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1242]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=280]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=283]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=284]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=285]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=286]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 20 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=296]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1250]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1266]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1274]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1282]: baseline=MOVE · contextual=MOVE
- PPO observado [player_2_log.json seq=296]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=298]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=299]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 21 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=309]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1290]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1322]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1330]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1338]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=309]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=310]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=311]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=313]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=314]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 22 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=324]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1346]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1362]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1370]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1378]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=324]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=326]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=327]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 23 (same_player_round)
- Strategic reviews únicos: 2 (observações=11) · PPO actions: 4 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=337]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1386]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1418]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1426]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1434]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=337]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=338]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=339]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=340]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 24 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=350]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1442]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1458]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1466]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1474]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=350]: SELL → SELL
- PPO observado [player_2_log.json seq=352]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=356]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 25 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@3
- Strategic Planner [shadow_planning seq=366]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1480]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1504]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1510]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1516]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=366]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=367]: SELL → SELL
- PPO observado [player_2_log.json seq=368]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=369]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=370]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 26 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@3
- Strategic Planner [shadow_planning seq=380]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=381]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=382]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1522]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1534]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1540]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1546]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_2_log.json seq=380]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=381]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=382]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 27 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@3
- Strategic Planner [shadow_planning seq=392]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=393]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=394]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=395]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1552]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1564]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1570]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1576]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_2_log.json seq=392]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=393]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=394]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=395]: REROLL → REROLL
- Outcome observado: placement=5 (correlação, não causalidade)

### Jogador 3 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=3]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=59]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=67]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=75]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=4]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=5]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=19) · PPO actions: 6 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=15]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=83]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=163]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=171]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=179]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=16]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=17]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=19]: PASS → HOLD
- PPO observado [player_3_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=19) · PPO actions: 6 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=187]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=267]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=275]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=283]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=31]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=32]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=33]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=34]: PASS → HOLD
- PPO observado [player_3_log.json seq=35]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 5 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=45]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=291]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=355]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=363]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=371]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=46]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=47]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=48]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=49]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=59]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=379]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=427]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=435]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=443]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=61]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=62]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=63]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=64]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=65]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 3 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=75]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=451]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=515]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=523]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=531]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=75]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=78]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=80]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=90]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=539]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=595]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=603]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=611]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=90]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=91]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=92]: BUY_XP → BUY_XP
- PPO observado [player_3_log.json seq=93]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=103]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=619]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=675]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=683]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=691]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=106]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=107]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=108]: BUY_XP → BUY_XP
- PPO observado [player_3_log.json seq=109]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=110]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 9 (same_player_round)
- Strategic reviews únicos: 6 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0, native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=120]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=121]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=122]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=699]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=707]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=731]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=715]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=723]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=731]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=120]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=121]: BUY_XP → BUY_XP
- PPO observado [player_3_log.json seq=122]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=132]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=136]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=137]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=138]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=739]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=787]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=795]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=803]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=134]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=135]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=136]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=137]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=138]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 11 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=148]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=150]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=151]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=152]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=153]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=154]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=811]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=851]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=859]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=867]: baseline=MOVE · contextual=MOVE
- PPO observado [player_3_log.json seq=150]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=151]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=152]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=153]: BUY_XP → BUY_XP
- PPO observado [player_3_log.json seq=154]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=164]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=165]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=875]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=883]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=891]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=899]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=164]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=165]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 13 (same_player_round)
- Strategic reviews únicos: 7 (observações=15) · PPO actions: 6 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=175]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=176]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=177]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=178]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=179]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=180]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=907]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=955]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=963]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=971]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=176]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=177]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=178]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=179]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=180]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=190]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=979]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=979]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=987]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=995]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=190]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 15 (same_player_round)
- Strategic reviews únicos: 7 (observações=13) · PPO actions: 5 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=200]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=202]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=203]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=204]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=205]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1003]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1059]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1043]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1051]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1059]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=200]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=202]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=203]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=204]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=205]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 16 (same_player_round)
- Strategic reviews únicos: 4 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=215]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=216]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1067]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1075]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1075]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1083]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1091]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=215]: SELL → SELL
- PPO observado [player_3_log.json seq=216]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 17 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=227]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=228]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=229]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=230]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=231]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1099]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1131]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1139]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1147]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=227]: SELL → SELL
- PPO observado [player_3_log.json seq=228]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=229]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=230]: SELL → SELL
- PPO observado [player_3_log.json seq=231]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 18 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=241]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=242]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=243]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1155]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1171]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1179]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1187]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=241]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=242]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=243]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=253]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=254]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=255]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=256]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=257]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1195]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1227]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1235]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1243]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=253]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=254]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=255]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=256]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=257]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=267]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=269]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=270]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1251]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1267]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1275]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1283]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=267]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=269]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_3_log.json seq=270]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=10) · PPO actions: 3 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=280]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=281]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=282]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1291]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1323]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1331]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1339]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=280]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=281]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=282]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 22 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=292]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=293]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=294]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1347]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1363]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1371]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1379]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=292]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=293]: SELL → SELL
- PPO observado [player_3_log.json seq=294]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 23 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=304]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=305]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=306]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=307]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=308]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1387]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1419]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1427]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1435]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=304]: SELL → SELL
- PPO observado [player_3_log.json seq=305]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=306]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=307]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=308]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 24 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=318]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=320]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=322]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1443]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1459]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1467]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1475]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=318]: SELL → SELL
- PPO observado [player_3_log.json seq=320]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=322]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 25 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=333]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=335]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=337]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=338]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=340]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1481]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1505]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1511]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1517]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_3_log.json seq=333]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=335]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=337]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=338]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=340]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 26 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=350]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=352]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=353]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1523]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1535]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1541]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1547]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_3_log.json seq=350]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=352]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=353]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 27 (same_player_round)
- Strategic reviews únicos: 3 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=363]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=367]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1553]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1571]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1577]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1581]: baseline=MOVE · contextual=MOVE
- PPO observado [player_3_log.json seq=363]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=364]: SELL → SELL
- PPO observado [player_3_log.json seq=366]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=367]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 28 (same_player_round)
- Strategic reviews únicos: 2 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=378]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1584]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1593]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1596]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1599]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=378]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=380]: SELL → SELL
- PPO observado [player_3_log.json seq=381]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=383]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 29 (same_player_round)
- Strategic reviews únicos: 4 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=394]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=397]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=399]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1601]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1607]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1609]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1611]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=394]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=395]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=397]: SELL → SELL
- PPO observado [player_3_log.json seq=399]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 30 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=410]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=412]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=413]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=414]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1613]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1623]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1619]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1621]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1623]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=410]: SELL → SELL
- PPO observado [player_3_log.json seq=412]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=413]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=414]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 31 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=424]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=426]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=428]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=430]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1625]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1627]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1631]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1633]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1635]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=424]: SELL → SELL
- PPO observado [player_3_log.json seq=426]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=428]: SELL → SELL
- PPO observado [player_3_log.json seq=430]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 32 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=440]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=441]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=443]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=444]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1637]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1643]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1645]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1647]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=440]: SELL → SELL
- PPO observado [player_3_log.json seq=441]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=443]: SELL → SELL
- PPO observado [player_3_log.json seq=444]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 33 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=455]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=456]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=458]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=461]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1649]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1655]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1657]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1659]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=455]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_3_log.json seq=456]: SELL → SELL
- PPO observado [player_3_log.json seq=458]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=461]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 34 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=472]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=474]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=475]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=477]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1661]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1667]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1669]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1671]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=472]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=474]: SELL → SELL
- PPO observado [player_3_log.json seq=475]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=477]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 35 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=488]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=489]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=490]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=492]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1673]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1683]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1679]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1681]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1683]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=488]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=489]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=490]: SELL → SELL
- PPO observado [player_3_log.json seq=492]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 36 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=502]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=503]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=504]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=505]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1685]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1691]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1693]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1695]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=502]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=503]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=504]: SELL → SELL
- PPO observado [player_3_log.json seq=505]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 37 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=516]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=518]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=519]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=520]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1697]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1703]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1705]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1707]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_3_log.json seq=516]: SELL → SELL
- PPO observado [player_3_log.json seq=518]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=519]: SELL → SELL
- PPO observado [player_3_log.json seq=520]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 38 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=530]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=531]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=533]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=534]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1709]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1719]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1715]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1717]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1719]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_3_log.json seq=530]: SELL → SELL
- PPO observado [player_3_log.json seq=531]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=533]: SELL → SELL
- PPO observado [player_3_log.json seq=534]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 39 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=544]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=545]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=547]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=549]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1721]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1723]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1727]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1729]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1731]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_3_log.json seq=544]: SELL → SELL
- PPO observado [player_3_log.json seq=545]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=547]: SELL → SELL
- PPO observado [player_3_log.json seq=549]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 40 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 0
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=560]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=561]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=563]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=564]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1733]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1739]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1741]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1743]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_3_log.json seq=560]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_3_log.json seq=561]: SELL → SELL
- PPO observado [player_3_log.json seq=563]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=564]: SELL → SELL

### Jogador 4 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=4]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=60]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=68]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=76]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=4]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=5]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=19) · PPO actions: 6 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=15]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=84]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=164]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=172]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=180]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=16]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=17]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=19]: PASS → HOLD
- PPO observado [player_4_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 5 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=188]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=268]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=276]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=284]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=30]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=31]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=32]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=33]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=34]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 3 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=44]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=292]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=356]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=364]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=372]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=44]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=47]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 5 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=57]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=380]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=428]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=436]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=444]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=57]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=60]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=61]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=62]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=63]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 3 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=73]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=452]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=516]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=524]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=532]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=73]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=74]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=75]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 7 (same_player_round)
- Strategic reviews únicos: 3 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=85]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=540]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Strategic Planner [context_bridge seq=612]: INITIAL_SELECTION (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=596]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=604]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=612]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=89]: SELL → SELL
- PPO observado [player_4_log.json seq=91]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=92]: SELL → SELL
- PPO observado [player_4_log.json seq=93]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=94]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 8 (same_player_round)
- Strategic reviews únicos: 4 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=104]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=105]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=620]: INITIAL_SELECTION (reason unavailable)
- Strategic Planner [context_bridge seq=628]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=676]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=684]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=692]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=107]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=108]: SELL → SELL
- PPO observado [player_4_log.json seq=109]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=110]: SELL → SELL
- PPO observado [player_4_log.json seq=111]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 9 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=121]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=122]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=123]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=700]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=708]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=716]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=724]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=732]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=121]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=122]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=123]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 10 (same_player_round)
- Strategic reviews únicos: 5 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=139]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=142]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=740]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=788]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=796]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=804]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=135]: SELL → SELL
- PPO observado [player_4_log.json seq=137]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=139]: SELL → SELL
- PPO observado [player_4_log.json seq=141]: SELL → SELL
- PPO observado [player_4_log.json seq=142]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 11 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=152]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=153]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=154]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=155]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=156]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=157]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=812]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=852]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=860]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=868]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=153]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=154]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=155]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=156]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=157]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=167]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=168]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=876]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=884]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=892]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=900]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=167]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=168]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 13 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=178]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=908]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=956]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=964]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=972]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=181]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=182]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=183]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=185]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=186]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=197]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=980]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=980]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=988]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=996]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=197]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 15 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=208]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=211]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=212]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=213]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=215]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=216]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1004]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1044]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1052]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1060]: baseline=HOLD · contextual=HOLD
- PPO observado [player_4_log.json seq=211]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=212]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=213]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=215]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=216]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 16 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=226]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=227]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1068]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1076]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1084]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1092]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=226]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=227]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 17 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=237]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=238]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=239]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=240]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=241]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1100]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1132]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1140]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1148]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=237]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=238]: SELL → SELL
- PPO observado [player_4_log.json seq=239]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=240]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=241]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 18 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=251]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=253]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=254]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1156]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1172]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1180]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1188]: baseline=HOLD · contextual=HOLD
- PPO observado [player_4_log.json seq=251]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=253]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=254]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=264]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=265]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=266]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=267]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=269]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1196]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1228]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1236]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1244]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=264]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=265]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=266]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=267]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=269]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=279]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=280]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=281]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1252]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1268]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1276]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1284]: baseline=BUY_UNIT · contextual=HOLD
- PPO observado [player_4_log.json seq=279]: SELL → SELL
- PPO observado [player_4_log.json seq=280]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=281]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 21 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=291]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1292]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1324]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1332]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1340]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=291]: SELL → SELL
- PPO observado [player_4_log.json seq=292]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=293]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=294]: SELL → SELL
- PPO observado [player_4_log.json seq=295]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 22 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=307]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1348]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1364]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1372]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1380]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=307]: SELL → SELL
- PPO observado [player_4_log.json seq=308]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=310]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 23 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=320]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=321]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=322]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=323]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=324]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1388]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1420]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1428]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1436]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=320]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=321]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=322]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=323]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=324]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 24 (same_player_round)
- Strategic reviews únicos: 2 (observações=7) · PPO actions: 3 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@2
- Strategic Planner [shadow_planning seq=334]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1444]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1452]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1460]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1468]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=334]: SELL → SELL
- PPO observado [player_4_log.json seq=335]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=336]: SELL → SELL
- Outcome observado: placement=8 (correlação, não causalidade)

### Jogador 5 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=5]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=61]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=69]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=77]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 7 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=85]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=165]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=173]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=181]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=19]: PASS → HOLD
- PPO observado [player_5_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 2 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=189]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=269]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=277]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=285]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=30]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=31]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 3 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=41]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=293]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=357]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=365]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=373]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=41]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=42]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=44]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 6 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=54]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=381]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=429]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=437]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=445]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=56]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=57]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=58]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=59]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=60]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 3 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=70]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=453]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=517]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=525]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=533]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=70]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=71]: BUY_XP → BUY_XP
- PPO observado [player_5_log.json seq=72]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 7 (same_player_round)
- Strategic reviews únicos: 3 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0, e79e0b44fb8b780e395642c6c706fc35@1
- Strategic Planner [shadow_planning seq=82]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=541]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Strategic Planner [context_bridge seq=613]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=597]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=605]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=613]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=85]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=87]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=88]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=89]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=90]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: e79e0b44fb8b780e395642c6c706fc35@1
- Strategic Planner [shadow_planning seq=101]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=621]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=677]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=685]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=693]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=105]: SELL → SELL
- PPO observado [player_5_log.json seq=106]: SELL → SELL
- PPO observado [player_5_log.json seq=107]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=108]: SELL → SELL
- PPO observado [player_5_log.json seq=109]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 9 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: e79e0b44fb8b780e395642c6c706fc35@1
- Strategic Planner [shadow_planning seq=120]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=122]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=123]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=701]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=709]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=717]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=725]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=733]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_5_log.json seq=120]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=122]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=123]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 10 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Espinhos Negros@2
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=135]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=137]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=138]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=139]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=140]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=141]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=741]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=789]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=797]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=805]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=137]: SELL → SELL
- PPO observado [player_5_log.json seq=138]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=139]: SELL → SELL
- PPO observado [player_5_log.json seq=140]: SELL → SELL
- PPO observado [player_5_log.json seq=141]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 11 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Espinhos Negros@2
- Strategic Planner [shadow_planning seq=151]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=154]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=155]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=156]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=158]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=159]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=813]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=853]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=861]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=869]: baseline=MOVE · contextual=MOVE
- PPO observado [player_5_log.json seq=154]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=155]: SELL → SELL
- PPO observado [player_5_log.json seq=156]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=158]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=159]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=169]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=170]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=877]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=885]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=893]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=901]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=169]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=170]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 13 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=180]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=181]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=182]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=183]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=184]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=186]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=187]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=909]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=957]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=965]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=973]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=182]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=183]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=184]: SELL → SELL
- PPO observado [player_5_log.json seq=186]: BUY_XP → BUY_XP
- PPO observado [player_5_log.json seq=187]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=197]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=981]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=981]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=989]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=997]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=197]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 15 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=209]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=210]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=212]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=214]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=215]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=216]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1005]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1045]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1053]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1061]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=210]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=212]: SELL → SELL
- PPO observado [player_5_log.json seq=214]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=215]: SELL → SELL
- PPO observado [player_5_log.json seq=216]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 16 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=227]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=229]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1069]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1077]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1085]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1093]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=227]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=229]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 17 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=240]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=242]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=244]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=246]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=247]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1101]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1133]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1141]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1149]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=240]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=242]: SELL → SELL
- PPO observado [player_5_log.json seq=244]: SELL → SELL
- PPO observado [player_5_log.json seq=246]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=247]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 18 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=257]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=259]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=261]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1157]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1173]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1181]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1189]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=257]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=259]: SELL → SELL
- PPO observado [player_5_log.json seq=261]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=271]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=274]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=276]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=277]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=278]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1197]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1229]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1237]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1245]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=271]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=274]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=276]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=277]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=278]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=288]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=290]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=292]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1253]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1269]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1277]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1285]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=288]: SELL → SELL
- PPO observado [player_5_log.json seq=290]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=292]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 21 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=302]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=303]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=305]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=307]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=309]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1293]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1325]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1333]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1341]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=302]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=303]: SELL → SELL
- PPO observado [player_5_log.json seq=305]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=307]: SELL → SELL
- PPO observado [player_5_log.json seq=309]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 22 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=321]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=322]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=323]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1349]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1365]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1373]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1381]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=321]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=322]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=323]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 23 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=334]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=336]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=337]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=339]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=340]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1389]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1421]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1429]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1437]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_5_log.json seq=334]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=336]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=337]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=339]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=340]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 24 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=351]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=352]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=355]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1445]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1461]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1469]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1476]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_5_log.json seq=351]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=352]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=355]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 25 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@4
- Strategic Planner [shadow_planning seq=365]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=367]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=369]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=370]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=372]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1482]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1506]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1512]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1518]: baseline=MOVE · contextual=MOVE
- PPO observado [player_5_log.json seq=365]: SELL → SELL
- PPO observado [player_5_log.json seq=367]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=369]: SELL → SELL
- PPO observado [player_5_log.json seq=370]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=372]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 26 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@5
- Strategic Planner [shadow_planning seq=382]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=384]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=385]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1524]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1536]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1542]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1548]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=382]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=384]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=385]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 27 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@5
- Strategic Planner [shadow_planning seq=395]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=398]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=399]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=400]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1554]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1572]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1578]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1582]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=395]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=398]: SELL → SELL
- PPO observado [player_5_log.json seq=399]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=400]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Vivaz@5
- Strategic Planner [shadow_planning seq=411]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=412]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=413]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=414]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1585]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1591]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1594]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1597]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=411]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=412]: SELL → SELL
- PPO observado [player_5_log.json seq=413]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=414]: BUY → BUY_UNIT
- Outcome observado: placement=3 (correlação, não causalidade)

### Jogador 6 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=6]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=62]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=70]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=78]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 4 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=86]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=166]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=174]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=182]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=14]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=15]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=16]: PASS → HOLD
- PPO observado [player_6_log.json seq=17]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=19) · PPO actions: 6 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=27]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=190]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=270]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=278]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=286]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=28]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=29]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=30]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=31]: PASS → HOLD
- PPO observado [player_6_log.json seq=32]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 2 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=42]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=294]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=358]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=366]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=374]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=42]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=43]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 5 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=53]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=382]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=430]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=438]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=446]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=53]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=54]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=55]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=57]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=58]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 5 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=68]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=454]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=518]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=526]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=534]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=68]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=69]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=71]: SELL → SELL
- PPO observado [player_6_log.json seq=72]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=73]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=83]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=542]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=598]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=606]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=614]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=84]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=87]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=88]: SELL → SELL
- PPO observado [player_6_log.json seq=90]: SELL → SELL
- PPO observado [player_6_log.json seq=91]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=101]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=622]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=678]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=686]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=694]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=107]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=108]: SELL → SELL
- PPO observado [player_6_log.json seq=109]: SELL → SELL
- PPO observado [player_6_log.json seq=111]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=112]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 9 (same_player_round)
- Strategic reviews únicos: 6 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0, native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=122]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=123]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=125]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=702]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=710]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=718]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=718]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=726]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=734]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=122]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=123]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=125]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 10 (same_player_round)
- Strategic reviews únicos: 5 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=135]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=136]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=138]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=141]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=742]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=790]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=798]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=806]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=138]: SELL → SELL
- PPO observado [player_6_log.json seq=141]: SELL → SELL
- PPO observado [player_6_log.json seq=142]: SELL → SELL
- PPO observado [player_6_log.json seq=144]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=146]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 11 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=157]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=814]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=854]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=862]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=870]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=158]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=160]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=161]: SELL → SELL
- PPO observado [player_6_log.json seq=163]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=164]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=174]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=175]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=878]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=886]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=894]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=902]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=174]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=175]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 13 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=185]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=910]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=958]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=966]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=974]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=187]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=188]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=189]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=190]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=192]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=202]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=982]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=982]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=990]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=998]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=202]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 15 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=212]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=214]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=215]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=216]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=217]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=218]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1006]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1046]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1054]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1062]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=214]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=215]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=216]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=217]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=218]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 16 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=228]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=230]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1070]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1078]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1086]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1094]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=228]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=230]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 17 (same_player_round)
- Strategic reviews únicos: 7 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=241]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=242]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=243]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=244]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=245]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1102]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1150]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1134]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1142]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1150]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=241]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=242]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=243]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=244]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=245]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 18 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=255]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=256]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=258]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1158]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1174]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1182]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1190]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=255]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=256]: SELL → SELL
- PPO observado [player_6_log.json seq=258]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=268]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=271]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=272]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=273]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=274]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1198]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1230]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1238]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1246]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=268]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=271]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=272]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=273]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_6_log.json seq=274]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=284]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=286]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=287]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1254]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1270]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1278]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1286]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_6_log.json seq=284]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=286]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=287]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 21 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=297]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=299]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=300]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=301]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=302]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1294]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1326]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1334]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1342]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_6_log.json seq=297]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=299]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=300]: SELL → SELL
- PPO observado [player_6_log.json seq=301]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=302]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 22 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=312]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=313]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=314]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1350]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1366]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1374]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1382]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=312]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=313]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=314]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 23 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=324]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=326]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=327]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=328]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=330]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1390]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1422]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1430]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1438]: baseline=MOVE · contextual=MOVE
- PPO observado [player_6_log.json seq=324]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=326]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=327]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=328]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=330]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 24 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=340]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=342]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=344]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1446]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1462]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1470]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1477]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=340]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=342]: SELL → SELL
- PPO observado [player_6_log.json seq=344]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 25 (same_player_round)
- Strategic reviews únicos: 7 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=354]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=356]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=358]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=360]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=361]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1483]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1519]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1507]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1513]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1519]: baseline=MOVE · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=354]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=356]: SELL → SELL
- PPO observado [player_6_log.json seq=358]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=360]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=361]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 26 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=371]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=372]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=373]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1525]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1531]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1537]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1543]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1549]: baseline=MOVE · contextual=MOVE
- PPO observado [player_6_log.json seq=371]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=372]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=373]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 27 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=383]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=384]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=385]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=386]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1555]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1567]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1573]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1579]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_6_log.json seq=383]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=384]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=385]: SELL → SELL
- PPO observado [player_6_log.json seq=386]: BUY → BUY_UNIT
- Outcome observado: placement=4 (correlação, não causalidade)

### Jogador 7 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 2 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=7]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=63]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=71]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=79]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=3]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=21) · PPO actions: 8 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=13]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=87]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=167]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=175]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=183]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=19]: PASS → HOLD
- PPO observado [player_7_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=19) · PPO actions: 6 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=191]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=271]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=279]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=287]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=32]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=33]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=34]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=35]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=36]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 5 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=46]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=295]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=359]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=367]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=375]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=46]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=47]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=49]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=50]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=51]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 5 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=61]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=383]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=431]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=439]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=447]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=61]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=63]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=64]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=65]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=66]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 9 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=76]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=455]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=519]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=527]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=535]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=81]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=82]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=83]: SELL → SELL
- PPO observado [player_7_log.json seq=84]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=85]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 7 (same_player_round)
- Strategic reviews únicos: 3 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=95]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=543]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Strategic Planner [context_bridge seq=615]: INITIAL_SELECTION (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=599]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=607]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=615]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=99]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=101]: SELL → SELL
- PPO observado [player_7_log.json seq=102]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=103]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=104]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 8 (same_player_round)
- Strategic reviews únicos: 5 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=114]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=115]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=117]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=118]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [context_bridge seq=623]: INITIAL_SELECTION (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=679]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=687]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=695]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=114]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=115]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=117]: PASS → HOLD
- PPO observado [player_7_log.json seq=118]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 9 (same_player_round)
- Strategic reviews únicos: 6 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0, native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=128]: PIVOT (current_direction_not_viable)
- Strategic Planner [shadow_planning seq=130]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=131]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=703]: PIVOT (reason unavailable)
- Strategic Planner [context_bridge seq=711]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=735]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=719]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=727]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=735]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=128]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=130]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=131]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 10 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=141]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=143]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=145]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=146]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=147]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=148]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=150]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=743]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=791]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=799]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=807]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_7_log.json seq=145]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=146]: SELL → SELL
- PPO observado [player_7_log.json seq=147]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=148]: SELL → SELL
- PPO observado [player_7_log.json seq=150]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 11 (same_player_round)
- Strategic reviews únicos: 8 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=160]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=161]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=162]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=163]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=164]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=165]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=815]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=823]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=855]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=863]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=871]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=161]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=162]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=163]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=164]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=165]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=175]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=177]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=879]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=887]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=895]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=903]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=175]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=177]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 13 (same_player_round)
- Strategic reviews únicos: 5 (observações=13) · PPO actions: 4 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=187]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=189]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=190]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=191]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=911]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=959]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=967]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=975]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=187]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=189]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=190]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=191]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=201]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=983]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=983]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=991]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=999]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=201]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 15 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=211]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=214]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=216]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=217]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=218]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=219]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1007]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1047]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1055]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1063]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=214]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=216]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=217]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=218]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=219]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 16 (same_player_round)
- Strategic reviews únicos: 4 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=229]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=233]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1071]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1095]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1079]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1087]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1095]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=229]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=233]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 17 (same_player_round)
- Strategic reviews únicos: 7 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=243]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=245]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=246]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=247]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=248]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1103]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1151]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1135]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1143]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1151]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=243]: SELL → SELL
- PPO observado [player_7_log.json seq=245]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=246]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=247]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=248]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 18 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=258]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=259]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=260]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1159]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1191]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1175]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1183]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1191]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=258]: SELL → SELL
- PPO observado [player_7_log.json seq=259]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=260]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=270]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=271]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=272]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=273]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=274]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1199]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1231]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1239]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1247]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_7_log.json seq=270]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=271]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=272]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=273]: SELL → SELL
- PPO observado [player_7_log.json seq=274]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=284]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=285]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=287]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1255]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1271]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1279]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1287]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_7_log.json seq=284]: SELL → SELL
- PPO observado [player_7_log.json seq=285]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=287]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 21 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=297]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=298]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=299]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=300]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=301]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1295]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1327]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1335]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1343]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=297]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=298]: SELL → SELL
- PPO observado [player_7_log.json seq=299]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=300]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=301]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 22 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=311]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=312]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=313]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1351]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1367]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1375]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1383]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=311]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=312]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=313]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 23 (same_player_round)
- Strategic reviews únicos: 7 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=323]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=324]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=325]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=327]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=329]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1391]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1439]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1423]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1431]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1439]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=323]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=324]: SELL → SELL
- PPO observado [player_7_log.json seq=325]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=327]: SELL → SELL
- PPO observado [player_7_log.json seq=329]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 24 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=340]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=342]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=344]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1447]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1478]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1463]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1471]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1478]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=340]: SELL → SELL
- PPO observado [player_7_log.json seq=342]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=344]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 25 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=356]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=357]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=359]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=360]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=361]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1484]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1508]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1514]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1520]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=356]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=357]: SELL → SELL
- PPO observado [player_7_log.json seq=359]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=360]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=361]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 26 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=372]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=374]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=375]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1526]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1538]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1544]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1550]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=372]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=374]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=375]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 27 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=385]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=387]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=389]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=391]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1556]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1574]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1580]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1583]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=385]: SELL → SELL
- PPO observado [player_7_log.json seq=387]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=389]: SELL → SELL
- PPO observado [player_7_log.json seq=391]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=401]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=402]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=403]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=404]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1586]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1595]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1598]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1600]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=401]: SELL → SELL
- PPO observado [player_7_log.json seq=402]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=403]: SELL → SELL
- PPO observado [player_7_log.json seq=404]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 29 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=415]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=417]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=418]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=419]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1602]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1608]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1608]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1610]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1612]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=415]: SELL → SELL
- PPO observado [player_7_log.json seq=417]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=418]: SELL → SELL
- PPO observado [player_7_log.json seq=419]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=430]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=432]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=433]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=434]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1614]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1620]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1622]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1624]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=430]: SELL → SELL
- PPO observado [player_7_log.json seq=432]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=433]: SELL → SELL
- PPO observado [player_7_log.json seq=434]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 31 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=445]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=447]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=449]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=451]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1626]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1632]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1634]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1636]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=445]: SELL → SELL
- PPO observado [player_7_log.json seq=447]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=449]: SELL → SELL
- PPO observado [player_7_log.json seq=451]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 32 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=461]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=462]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=463]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=464]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1638]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1648]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1644]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1646]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1648]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_7_log.json seq=461]: SELL → SELL
- PPO observado [player_7_log.json seq=462]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=463]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=464]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 33 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=474]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=475]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=476]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=477]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1650]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1660]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1656]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1658]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1660]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=474]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=475]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=476]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=477]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 34 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=487]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=488]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=489]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=491]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1662]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1666]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1668]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1670]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1672]: baseline=MOVE · contextual=MOVE
- PPO observado [player_7_log.json seq=487]: SELL → SELL
- PPO observado [player_7_log.json seq=488]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=489]: SELL → SELL
- PPO observado [player_7_log.json seq=491]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 35 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=503]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=506]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=507]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=508]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1674]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1680]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1682]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1684]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_7_log.json seq=503]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=506]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=507]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=508]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 36 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=518]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=520]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=522]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=523]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1686]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1688]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1692]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1694]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1696]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=518]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=520]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=522]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=523]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 37 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=534]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=536]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=537]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=538]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1698]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1708]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1704]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1706]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1708]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=534]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=536]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=537]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=538]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 38 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=548]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=550]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=551]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=552]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1710]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1720]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1716]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1718]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1720]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=548]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=550]: SELL → SELL
- PPO observado [player_7_log.json seq=551]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=552]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 39 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=562]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=564]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=566]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=567]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1722]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1732]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1728]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1730]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1732]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=562]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=564]: SELL → SELL
- PPO observado [player_7_log.json seq=566]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=567]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 40 (same_player_round)
- Strategic reviews únicos: 6 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 0
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=577]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=578]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=579]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=580]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1734]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1740]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1738]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1740]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1742]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=577]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=578]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=579]: SELL → SELL
- PPO observado [player_7_log.json seq=580]: BUY → BUY_UNIT

### Jogador 8 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=8]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=64]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=72]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=80]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 7 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=88]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=168]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=176]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=184]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=19]: PASS → HOLD
- PPO observado [player_8_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 3 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=192]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=272]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=280]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=288]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=30]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=32]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=34]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 6 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=44]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=296]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=360]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=368]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=376]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=47]: SELL → SELL
- PPO observado [player_8_log.json seq=49]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=50]: SELL → SELL
- PPO observado [player_8_log.json seq=51]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=61]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=384]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=432]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=440]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=448]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=64]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=65]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=66]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=68]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=69]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=20) · PPO actions: 9 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=79]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=456]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=520]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=528]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=536]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=84]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=85]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=86]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=87]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=88]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=98]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=544]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=600]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=608]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=616]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=106]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=107]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=108]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=109]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=110]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=120]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=624]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=680]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=688]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=696]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=124]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=125]: BUY_XP → BUY_XP
- PPO observado [player_8_log.json seq=126]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=127]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=128]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 9 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=138]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=140]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=704]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=712]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=720]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=728]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=736]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=138]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=140]: SELL → SELL
- PPO observado [player_8_log.json seq=141]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 10 (same_player_round)
- Strategic reviews únicos: 3 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0, native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=152]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=744]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=808]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=792]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=800]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=808]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=156]: SELL → SELL
- PPO observado [player_8_log.json seq=158]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=160]: SELL → SELL
- PPO observado [player_8_log.json seq=161]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=164]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 11 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=174]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=816]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=856]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=864]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=872]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=175]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=176]: SELL → SELL
- PPO observado [player_8_log.json seq=178]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=180]: SELL → SELL
- PPO observado [player_8_log.json seq=182]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=192]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=193]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=880]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=888]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=896]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=904]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=192]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=193]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 13 (same_player_round)
- Strategic reviews únicos: 8 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=203]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=204]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=206]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=207]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=208]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=210]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=212]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=912]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=960]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=968]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=976]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=206]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=207]: SELL → SELL
- PPO observado [player_8_log.json seq=208]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=210]: SELL → SELL
- PPO observado [player_8_log.json seq=212]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=4) · PPO actions: 1 · Composition snapshots: 3 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=222]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=984]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=984]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=992]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1000]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=222]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 15 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=232]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=234]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=235]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=236]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=237]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=238]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1008]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1048]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1056]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1064]: baseline=HOLD · contextual=BUY_XP
- PPO observado [player_8_log.json seq=234]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=235]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=236]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=237]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=238]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 16 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=249]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=250]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1072]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1080]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1088]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1096]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=249]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=250]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 17 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=261]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=263]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=265]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=267]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=268]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1104]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1136]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1144]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1152]: baseline=MOVE · contextual=MOVE
- PPO observado [player_8_log.json seq=261]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=263]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=265]: SELL → SELL
- PPO observado [player_8_log.json seq=267]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_8_log.json seq=268]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 18 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=278]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=280]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=281]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1160]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1176]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1184]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1192]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=278]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=280]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=281]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 19 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=291]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=294]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=295]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=296]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=297]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1200]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1232]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1240]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1248]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=291]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=294]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_8_log.json seq=295]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=296]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=297]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 20 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=307]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=309]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=310]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1256]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1272]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1280]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1288]: baseline=BUY_UNIT · contextual=HOLD
- PPO observado [player_8_log.json seq=307]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=309]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=310]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 21 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=320]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=321]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=322]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=324]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=325]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1296]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1328]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1336]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1344]: baseline=BUY_UNIT · contextual=HOLD
- PPO observado [player_8_log.json seq=320]: SELL → SELL
- PPO observado [player_8_log.json seq=321]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=322]: SELL → SELL
- PPO observado [player_8_log.json seq=324]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=325]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 22 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=335]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=336]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=337]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1352]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1368]: baseline=BUY_UNIT · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1376]: baseline=BUY_UNIT · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1384]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=335]: SELL → SELL
- PPO observado [player_8_log.json seq=336]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=337]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 23 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=348]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=349]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=350]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=352]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=353]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1392]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1424]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1432]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1440]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_8_log.json seq=348]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=349]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=350]: REROLL → REROLL
- PPO observado [player_8_log.json seq=352]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=353]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 24 (same_player_round)
- Strategic reviews únicos: 4 (observações=7) · PPO actions: 3 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=363]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=365]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=366]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1448]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1456]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1464]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1472]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_8_log.json seq=363]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=365]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=366]: BUY → BUY_UNIT
- Outcome observado: placement=7 (correlação, não causalidade)

## Limitações explícitas

- Associação por match/player/round não demonstra causalidade.
- Comparação com PPO usa a ação observada no log e a recomendação temporalmente mais próxima no mesmo jogador/round.
- Ação PPO não é ground truth; concordância não é métrica de qualidade.
- Snapshots sem identidade ou timestamp suficiente permanecem unavailable e não são reconstruídos.
- Sessões antigas podem não conter o envelope completo; são preservadas como dados legados não correlacionáveis.
- Fontes ausentes, stale, partial ou invalid não são convertidas em zero nem substituídas por decisões artificiais.
