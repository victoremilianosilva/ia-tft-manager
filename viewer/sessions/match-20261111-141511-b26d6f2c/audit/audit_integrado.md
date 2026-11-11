# Índice integrado de auditoria

- Schema do índice: v1
- Match: b26d6f2c-a8f2-40df-aba8-30b2b7945d61
- Jogadores: 1, 2, 3, 4, 5, 6, 7, 8
- Grupos jogador/round: 251

## Integridade dos produtores

| Produtor | Registros | Disponível |
|---|---:|---|
| Strategic Planner | 2880 | sim |
| Economic Controller | 2880 | sim |
| Economy evidence records | 1787 | sim |
| Economy evidence valid | 1143 | sim |
| Board evidence records | 1787 | sim |
| Board evidence valid | 1143 | sim |
| Item evidence records | 1787 | sim |
| Item evidence valid | 1143 | sim |
| Unit Priority | 1787 | sim |
| Lineup Planner | 1787 | sim |
| Composition Intelligence | 1787 | sim |
| Action Evaluator baseline | 1787 | sim |
| Contextual Action Evaluator | 1787 | sim |
| Ações PPO observadas | 1093 | sim |
| Outcomes | 249 | sim |

## Integridade do stream

- Envelopes de composição incompletos: 0
- Divergências de identidade no Context Bridge: 0
- Sequências duplicadas: 0
- Inversões de sequência: 0
- Lacunas de sequência: 0
- Eventos duplicados no log de jogadores: 0
- Conflitos de sequência no log de jogadores: 0
- Conflitos de sequência Composition Intelligence: 0
- Comparações baseline/contextual disponíveis: 1143
- Divergências baseline/contextual: 219
- Registros sem versão (legado): 0
- Schemas incompatíveis: 0
- Erros de parsing: 0

## Comparação observacional com PPO

| Evaluator | Comparáveis | Concordâncias | Divergências | Indisponíveis |
|---|---:|---:|---:|---:|
| Baseline | 0 | 0 | 0 | 1093 |
| Contextual | 0 | 0 | 0 | 1093 |

### Comparação com taxonomia semântica normalizada

- Versão da taxonomia: v1
| Evaluator | Correspondência direta | Compatibilidade parcial | Incompatibilidade | Não comparável |
|---|---:|---:|---:|---:|
| Baseline | 0 | 0 | 0 | 1093 |
| Contextual | 0 | 0 | 0 | 1093 |

## Timeline correlacionada

### Jogador 1 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 3 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=1]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=81]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=89]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=97]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 7 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=105]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=169]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=177]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=185]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=19]: PASS → HOLD
- PPO observado [player_1_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 5 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=193]: INSUFFICIENT_EVIDENCE (reason unavailable)
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
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=44]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=289]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=345]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=353]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=361]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=44]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=48]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=58]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=369]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=425]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=433]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=441]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=60]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=61]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=62]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=63]: PASS → HOLD
- PPO observado [player_1_log.json seq=64]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=74]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=449]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=505]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=513]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=521]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=80]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=81]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=82]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=83]: SELL → SELL
- PPO observado [player_1_log.json seq=86]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 7 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=96]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=529]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=585]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=593]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=601]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=100]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=101]: SELL → SELL
- PPO observado [player_1_log.json seq=102]: SELL → SELL
- PPO observado [player_1_log.json seq=103]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=104]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=114]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=609]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=625]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=633]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=641]: baseline=NONE · contextual=HOLD
- PPO observado [player_1_log.json seq=114]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=117]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=119]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 9 (same_player_round)
- Strategic reviews únicos: 9 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@1
- Strategic Planner [shadow_planning seq=129]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=131]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=135]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=136]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=138]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=139]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=649]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=657]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=697]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=705]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=713]: baseline=MOVE · contextual=MOVE
- PPO observado [player_1_log.json seq=133]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=135]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=136]: SELL → SELL
- PPO observado [player_1_log.json seq=138]: SELL → SELL
- PPO observado [player_1_log.json seq=139]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 10 (same_player_round)
- Strategic reviews únicos: 5 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=150]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=151]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=152]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=156]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=721]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=761]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=769]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=777]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=151]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=152]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=153]: SELL → SELL
- PPO observado [player_1_log.json seq=155]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=156]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@3
- Strategic Planner [shadow_planning seq=166]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=168]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=785]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=793]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=801]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=809]: baseline=MOVE · contextual=MOVE
- PPO observado [player_1_log.json seq=166]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=168]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 12 (same_player_round)
- Strategic reviews únicos: 8 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@3
- Strategic Planner [shadow_planning seq=178]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=179]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=180]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=181]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=182]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=183]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=817]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=873]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=857]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=865]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=873]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=179]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=180]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=181]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=182]: BUY_XP → BUY_XP
- PPO observado [player_1_log.json seq=183]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 13 (same_player_round)
- Strategic reviews únicos: 4 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@3
- Strategic Planner [shadow_planning seq=193]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=194]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=881]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=905]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=889]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=897]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=905]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=193]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=194]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 14 (same_player_round)
- Strategic reviews únicos: 5 (observações=12) · PPO actions: 4 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@3
- Strategic Planner [shadow_planning seq=204]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=206]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=207]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=208]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=913]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=953]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=961]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=969]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=204]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=206]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=207]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=208]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 15 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=218]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=220]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=977]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=985]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=993]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1001]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=218]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=220]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 16 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=230]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=232]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=233]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=234]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=236]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=237]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1009]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1049]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1057]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1065]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=232]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=233]: MOVE_BENCH → MOVE
- PPO observado [player_1_log.json seq=234]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=236]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=237]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 17 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=247]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=250]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1073]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1081]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1089]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1097]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=247]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=250]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 18 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=261]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=263]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=264]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=265]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=267]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1105]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1137]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1145]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1153]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=261]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=263]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=264]: MOVE_BOARD → MOVE
- PPO observado [player_1_log.json seq=265]: SELL → SELL
- PPO observado [player_1_log.json seq=267]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 19 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=277]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=278]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=279]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1161]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1177]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1185]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1193]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=277]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=278]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=279]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=289]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=290]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=294]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=296]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=298]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1201]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1233]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1241]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1249]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_1_log.json seq=289]: SELL → SELL
- PPO observado [player_1_log.json seq=290]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=294]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=296]: SELL → SELL
- PPO observado [player_1_log.json seq=298]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=308]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=310]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=312]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1257]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1273]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1281]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1289]: baseline=MOVE · contextual=MOVE
- PPO observado [player_1_log.json seq=308]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=310]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=312]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=322]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=323]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=324]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=325]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=326]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1297]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1329]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1337]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1345]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=322]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_1_log.json seq=323]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_1_log.json seq=324]: SELL → SELL
- PPO observado [player_1_log.json seq=325]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=326]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=337]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=338]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=339]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1353]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1369]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1377]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1385]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=337]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=338]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=339]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=349]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=350]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=351]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=352]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=355]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1392]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1420]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1427]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1434]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=349]: SELL → SELL
- PPO observado [player_1_log.json seq=350]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=351]: SELL → SELL
- PPO observado [player_1_log.json seq=352]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=355]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 25 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=365]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=366]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=367]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1441]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1455]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1462]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1469]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=365]: SELL → SELL
- PPO observado [player_1_log.json seq=366]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=367]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 26 (same_player_round)
- Strategic reviews únicos: 7 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=377]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=380]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=381]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=382]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=383]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1476]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1518]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1504]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1511]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1518]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=377]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=380]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=381]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=382]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_1_log.json seq=383]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 27 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=393]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=395]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=397]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1525]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1553]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1539]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1546]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1553]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=393]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=395]: SELL → SELL
- PPO observado [player_1_log.json seq=397]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=408]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=410]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=411]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=413]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1559]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1577]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1583]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1589]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=408]: SELL → SELL
- PPO observado [player_1_log.json seq=410]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=411]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=413]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 29 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@4
- Strategic Planner [shadow_planning seq=423]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=425]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=427]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=429]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1595]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1613]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1619]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1625]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_1_log.json seq=423]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=425]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=427]: SELL → SELL
- PPO observado [player_1_log.json seq=429]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=439]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=440]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=441]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=442]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1631]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1649]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1655]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1661]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=439]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=440]: SELL → SELL
- PPO observado [player_1_log.json seq=441]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=442]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 31 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=452]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=453]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=454]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=456]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1665]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1677]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1681]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1685]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=452]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=453]: SELL → SELL
- PPO observado [player_1_log.json seq=454]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=456]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 32 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=467]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=469]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=471]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=472]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1688]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1697]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1700]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1703]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_1_log.json seq=467]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=469]: SELL → SELL
- PPO observado [player_1_log.json seq=471]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=472]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 33 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=482]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=484]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=485]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=486]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1706]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1715]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1718]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1721]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=482]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=484]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_1_log.json seq=485]: SELL → SELL
- PPO observado [player_1_log.json seq=486]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 34 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=496]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=498]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=500]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=503]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1724]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1733]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1736]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1739]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=496]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=498]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=500]: SELL → SELL
- PPO observado [player_1_log.json seq=503]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 35 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=513]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=514]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=515]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=517]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1741]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1751]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1747]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1749]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1751]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=513]: SELL → SELL
- PPO observado [player_1_log.json seq=514]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=515]: SELL → SELL
- PPO observado [player_1_log.json seq=517]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 36 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=527]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=528]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=529]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=530]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1753]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1757]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1759]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1761]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1763]: baseline=HOLD · contextual=HOLD
- PPO observado [player_1_log.json seq=527]: SELL → SELL
- PPO observado [player_1_log.json seq=528]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=529]: SELL → SELL
- PPO observado [player_1_log.json seq=530]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 37 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=540]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=541]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=542]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=544]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1765]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1771]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1773]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1775]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_1_log.json seq=540]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=541]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=542]: SELL → SELL
- PPO observado [player_1_log.json seq=544]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 1 · round 38 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 0
- Composition identity/version: native-set-18-Inferno@5
- Strategic Planner [shadow_planning seq=554]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=555]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=557]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=558]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1777]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1781]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1783]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1785]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_1_log.json seq=554]: SELL → SELL
- PPO observado [player_1_log.json seq=555]: BUY → BUY_UNIT
- PPO observado [player_1_log.json seq=557]: SELL → SELL
- PPO observado [player_1_log.json seq=558]: BUY → BUY_UNIT

### Jogador 2 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 3 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=2]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=82]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=90]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=98]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 5 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=106]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=170]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=178]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=186]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=14]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=15]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=17]: PASS → HOLD
- PPO observado [player_2_log.json seq=18]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 4 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=28]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=194]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=266]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=274]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=282]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=28]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=29]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=30]: PASS → HOLD
- PPO observado [player_2_log.json seq=31]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 7 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=41]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=290]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=346]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=354]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=362]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=46]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=47]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=48]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=49]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=50]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=60]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=370]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=426]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=434]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=442]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=64]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=65]: SELL → SELL
- PPO observado [player_2_log.json seq=66]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=67]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=68]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=78]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=450]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=506]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=514]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=522]: baseline=NONE · contextual=HOLD
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
- Strategic Planner [context_bridge seq=530]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=586]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=594]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=602]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=99]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=100]: BUY_XP → BUY_XP
- PPO observado [player_2_log.json seq=101]: PASS → HOLD
- PPO observado [player_2_log.json seq=102]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=112]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=610]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=626]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=634]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=642]: baseline=NONE · contextual=HOLD
- PPO observado [player_2_log.json seq=112]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=113]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=114]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 9 (same_player_round)
- Strategic reviews únicos: 9 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=124]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=126]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=127]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=129]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=130]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=132]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=650]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=658]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=698]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=706]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=714]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=127]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=129]: SELL → SELL
- PPO observado [player_2_log.json seq=130]: SELL → SELL
- PPO observado [player_2_log.json seq=132]: SELL → SELL
- PPO observado [player_2_log.json seq=134]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=144]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=145]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=146]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=147]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=149]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=151]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=722]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=762]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=770]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=778]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=145]: SELL → SELL
- PPO observado [player_2_log.json seq=146]: SELL → SELL
- PPO observado [player_2_log.json seq=147]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=149]: SELL → SELL
- PPO observado [player_2_log.json seq=151]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=161]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=164]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=786]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=794]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=802]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=810]: baseline=HOLD · contextual=HOLD
- PPO observado [player_2_log.json seq=161]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=164]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 12 (same_player_round)
- Strategic reviews únicos: 3 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=174]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=176]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=818]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=858]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=866]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=874]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=175]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=176]: SELL → SELL
- PPO observado [player_2_log.json seq=177]: SELL → SELL
- PPO observado [player_2_log.json seq=178]: SELL → SELL
- PPO observado [player_2_log.json seq=180]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 13 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=192]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=882]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=890]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=898]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=906]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_2_log.json seq=192]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=193]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=205]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=914]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=954]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=962]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=970]: baseline=BUY_UNIT · contextual=BUY_XP
- PPO observado [player_2_log.json seq=206]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=207]: SELL → SELL
- PPO observado [player_2_log.json seq=209]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=210]: MOVE_BOARD → MOVE
- PPO observado [player_2_log.json seq=211]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 15 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=221]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=978]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=986]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=994]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1002]: baseline=MOVE · contextual=MOVE
- PPO observado [player_2_log.json seq=221]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=223]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 16 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=233]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1010]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1050]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1058]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1066]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=235]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=236]: SELL → SELL
- PPO observado [player_2_log.json seq=237]: SELL → SELL
- PPO observado [player_2_log.json seq=238]: SELL → SELL
- PPO observado [player_2_log.json seq=239]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 17 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=249]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1074]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1082]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1090]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1098]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_2_log.json seq=249]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=251]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 18 (same_player_round)
- Strategic reviews únicos: 3 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=261]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=265]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1106]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1138]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1146]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1154]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=261]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=262]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=263]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=264]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=265]: REROLL → REROLL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 19 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=276]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1162]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1178]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1186]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1194]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_2_log.json seq=276]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=277]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_2_log.json seq=278]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 20 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=288]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1202]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1234]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1242]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1250]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_2_log.json seq=288]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=290]: SELL → SELL
- PPO observado [player_2_log.json seq=291]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=292]: SELL → SELL
- PPO observado [player_2_log.json seq=293]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 21 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=303]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1258]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1274]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1282]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1290]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=303]: SELL → SELL
- PPO observado [player_2_log.json seq=304]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=305]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=315]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=317]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=318]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=319]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=320]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1298]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1330]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1338]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1346]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_2_log.json seq=315]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=317]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=318]: MOVE_BENCH → MOVE
- PPO observado [player_2_log.json seq=319]: SELL → SELL
- PPO observado [player_2_log.json seq=320]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 2 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=7) · PPO actions: 3 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@2
- Strategic Planner [shadow_planning seq=330]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=331]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=332]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1354]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1362]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1370]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1378]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_2_log.json seq=330]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=331]: BUY → BUY_UNIT
- PPO observado [player_2_log.json seq=332]: MOVE_BENCH → MOVE
- Outcome observado: placement=8 (correlação, não causalidade)

### Jogador 3 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 4 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=3]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=83]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=91]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=99]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=4]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=5]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 6 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=15]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=107]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=171]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=179]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=187]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=16]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=17]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=19]: PASS → HOLD
- PPO observado [player_3_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 6 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=195]: INSUFFICIENT_EVIDENCE (reason unavailable)
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
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 5 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=45]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=291]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=347]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=355]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=363]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=46]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=47]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=48]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=49]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=59]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=371]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=427]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=435]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=443]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=62]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=63]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=64]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=65]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=66]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=76]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=451]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=507]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=515]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=523]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=76]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=79]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=81]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=91]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=531]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=587]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=595]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=603]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=91]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=92]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=93]: BUY_XP → BUY_XP
- PPO observado [player_3_log.json seq=94]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=104]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=611]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=627]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=635]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=643]: baseline=NONE · contextual=HOLD
- PPO observado [player_3_log.json seq=104]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=105]: BUY_XP → BUY_XP
- PPO observado [player_3_log.json seq=106]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 9 (same_player_round)
- Strategic reviews únicos: 9 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=116]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=117]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=118]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=119]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=120]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=121]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=122]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=651]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=659]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=699]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=707]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=715]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=118]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=119]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=120]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=121]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=122]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=132]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=135]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=136]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=137]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=723]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=763]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=771]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=779]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=133]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=134]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=135]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=136]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=137]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=147]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=148]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=787]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=795]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=803]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=811]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=147]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=148]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 12 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=158]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=159]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=160]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=161]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=162]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=163]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=819]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=859]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=867]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=875]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=159]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=160]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=161]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=162]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=163]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 13 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=173]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=174]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=883]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=891]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=899]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=907]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=173]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=174]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 14 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=184]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=185]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=186]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=187]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=188]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=189]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=915]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=955]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=963]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=971]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_3_log.json seq=185]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=186]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=187]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=188]: SELL → SELL
- PPO observado [player_3_log.json seq=189]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 15 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=199]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=200]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=979]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=987]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=995]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1003]: baseline=MOVE · contextual=MOVE
- PPO observado [player_3_log.json seq=199]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=200]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 16 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=210]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=211]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=214]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=215]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=217]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=218]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1011]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1051]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1059]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1067]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=211]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=214]: SELL → SELL
- PPO observado [player_3_log.json seq=215]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=217]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=218]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 17 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=228]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=230]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1075]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1083]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1091]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1099]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=228]: SELL → SELL
- PPO observado [player_3_log.json seq=230]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 18 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=241]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=242]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=245]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=246]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=247]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1107]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1139]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1147]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1155]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=241]: SELL → SELL
- PPO observado [player_3_log.json seq=242]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=245]: MOVE_BENCH → MOVE
- PPO observado [player_3_log.json seq=246]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=247]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 19 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=257]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=258]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=259]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1163]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1179]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1187]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1195]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=257]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=258]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=259]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=269]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=270]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=271]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=273]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=274]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1203]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1235]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1243]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1251]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=269]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=270]: SELL → SELL
- PPO observado [player_3_log.json seq=271]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=273]: SELL → SELL
- PPO observado [player_3_log.json seq=274]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=284]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=285]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=287]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1259]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1275]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1283]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1291]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=284]: SELL → SELL
- PPO observado [player_3_log.json seq=285]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=287]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=298]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=300]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=302]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=303]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=304]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1299]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1331]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1339]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1347]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=298]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=300]: SELL → SELL
- PPO observado [player_3_log.json seq=302]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=303]: MOVE_BOARD → MOVE
- PPO observado [player_3_log.json seq=304]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=314]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=315]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=317]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1355]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1371]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1379]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1386]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=314]: SELL → SELL
- PPO observado [player_3_log.json seq=315]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=317]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=328]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=330]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=332]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=334]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=336]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1393]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1421]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1428]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1435]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=328]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=330]: SELL → SELL
- PPO observado [player_3_log.json seq=332]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=334]: SELL → SELL
- PPO observado [player_3_log.json seq=336]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 25 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=346]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=347]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=349]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1442]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1456]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1463]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1470]: baseline=HOLD · contextual=HOLD
- PPO observado [player_3_log.json seq=346]: SELL → SELL
- PPO observado [player_3_log.json seq=347]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=349]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 26 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=360]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=361]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=362]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=364]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=366]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1477]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1505]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1512]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1519]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=360]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=361]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_3_log.json seq=362]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=364]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=366]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@2
- Strategic Planner [shadow_planning seq=376]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=379]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=382]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1526]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1540]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1547]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1554]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=376]: SELL → SELL
- PPO observado [player_3_log.json seq=379]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=382]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@3
- Strategic Planner [shadow_planning seq=392]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=393]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=395]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=397]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1560]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1578]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1584]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1590]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_3_log.json seq=392]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=393]: SELL → SELL
- PPO observado [player_3_log.json seq=395]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=397]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 29 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@3
- Strategic Planner [shadow_planning seq=407]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=408]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=410]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=411]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1596]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1614]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1620]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1626]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_3_log.json seq=407]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=408]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=410]: SELL → SELL
- PPO observado [player_3_log.json seq=411]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 3 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Devastador@3
- Strategic Planner [shadow_planning seq=421]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=422]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=424]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=425]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1632]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1644]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1650]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1656]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_3_log.json seq=421]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=422]: BUY → BUY_UNIT
- PPO observado [player_3_log.json seq=424]: SELL → SELL
- PPO observado [player_3_log.json seq=425]: BUY → BUY_UNIT
- Outcome observado: placement=6 (correlação, não causalidade)

### Jogador 4 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 4 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=4]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=84]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=92]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=100]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=4]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=5]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 6 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=15]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=108]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=172]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=180]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=188]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=16]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=17]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=19]: PASS → HOLD
- PPO observado [player_4_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=17) · PPO actions: 5 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=196]: INSUFFICIENT_EVIDENCE (reason unavailable)
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
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=44]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=292]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=348]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=356]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=364]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=44]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=47]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=57]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=372]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=428]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=436]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=444]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=60]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=61]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=62]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=63]: PASS → HOLD
- PPO observado [player_4_log.json seq=64]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 4 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=74]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=452]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=508]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=516]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=524]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=74]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=75]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=76]: PASS → HOLD
- PPO observado [player_4_log.json seq=77]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 7 (same_player_round)
- Strategic reviews únicos: 3 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=87]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=532]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Strategic Planner [context_bridge seq=604]: INITIAL_SELECTION (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=588]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=596]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=604]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=91]: SELL → SELL
- PPO observado [player_4_log.json seq=93]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=94]: SELL → SELL
- PPO observado [player_4_log.json seq=95]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=96]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 8 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=106]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=107]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=612]: INITIAL_SELECTION (reason unavailable)
- Strategic Planner [context_bridge seq=620]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=628]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=636]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=644]: baseline=NONE · contextual=HOLD
- PPO observado [player_4_log.json seq=106]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=107]: SELL → SELL
- PPO observado [player_4_log.json seq=108]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 9 (same_player_round)
- Strategic reviews únicos: 7 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: unavailable@0, native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=118]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=120]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=122]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=123]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=652]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=660]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=668]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=700]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=708]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=716]: baseline=MOVE · contextual=MOVE
- PPO observado [player_4_log.json seq=122]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=123]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=124]: SELL → SELL
- PPO observado [player_4_log.json seq=125]: SELL → SELL
- PPO observado [player_4_log.json seq=127]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Florescer@1
- Strategic Planner [shadow_planning seq=137]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=138]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=140]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=142]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=143]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=144]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=724]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=764]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=772]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=780]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=138]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=140]: SELL → SELL
- PPO observado [player_4_log.json seq=142]: BUY_XP → BUY_XP
- PPO observado [player_4_log.json seq=143]: SELL → SELL
- PPO observado [player_4_log.json seq=144]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 11 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=154]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=788]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=796]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=804]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=812]: baseline=MOVE · contextual=MOVE
- PPO observado [player_4_log.json seq=154]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=155]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 12 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=166]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=820]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=860]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=868]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=876]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=167]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=168]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=169]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=170]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=171]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 13 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=181]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=884]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=892]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=900]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=908]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=181]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=182]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=192]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=916]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=956]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=964]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=972]: baseline=MOVE · contextual=MOVE
- PPO observado [player_4_log.json seq=193]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=195]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=196]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=197]: MOVE_BENCH → MOVE
- PPO observado [player_4_log.json seq=198]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 15 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=208]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=980]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=988]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=996]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1004]: baseline=HOLD · contextual=HOLD
- PPO observado [player_4_log.json seq=208]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=209]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 16 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=219]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1012]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1052]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1060]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1068]: baseline=HOLD · contextual=HOLD
- PPO observado [player_4_log.json seq=221]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=222]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=223]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=224]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=225]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 17 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3, native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=235]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1076]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1084]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1084]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1092]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1100]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_4_log.json seq=235]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=237]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 18 (same_player_round)
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=248]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1108]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1140]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1148]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1156]: baseline=HOLD · contextual=HOLD
- PPO observado [player_4_log.json seq=248]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=249]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=250]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=251]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=252]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 19 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=262]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1164]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1180]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1188]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1196]: baseline=HOLD · contextual=HOLD
- PPO observado [player_4_log.json seq=262]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=263]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=264]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=276]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=277]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=280]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=281]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=282]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1204]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1236]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1244]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1252]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=276]: SELL → SELL
- PPO observado [player_4_log.json seq=277]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=280]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=281]: MOVE_BOARD → MOVE
- PPO observado [player_4_log.json seq=282]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=292]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=295]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=296]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1260]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1276]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1284]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1292]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=292]: SELL → SELL
- PPO observado [player_4_log.json seq=295]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=296]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=306]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=308]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=309]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=310]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=312]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1300]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1332]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1340]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1348]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=306]: SELL → SELL
- PPO observado [player_4_log.json seq=308]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=309]: SELL → SELL
- PPO observado [player_4_log.json seq=310]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=312]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=323]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=325]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=327]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1356]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1372]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1380]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1387]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_4_log.json seq=323]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=325]: SELL → SELL
- PPO observado [player_4_log.json seq=327]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=338]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=340]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=341]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=342]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=343]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1394]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1422]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1429]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1436]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_4_log.json seq=338]: SELL → SELL
- PPO observado [player_4_log.json seq=340]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=341]: SELL → SELL
- PPO observado [player_4_log.json seq=342]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=343]: REROLL → REROLL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 25 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=354]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=355]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=357]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1443]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1457]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1464]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1471]: baseline=MOVE · contextual=MOVE
- PPO observado [player_4_log.json seq=354]: SELL → SELL
- PPO observado [player_4_log.json seq=355]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=357]: REROLL → REROLL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 26 (same_player_round)
- Strategic reviews únicos: 3 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=368]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=369]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1478]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1506]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1513]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1520]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=368]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=369]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_4_log.json seq=370]: SELL → SELL
- PPO observado [player_4_log.json seq=372]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=373]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 4 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=7) · PPO actions: 3 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@4
- Strategic Planner [shadow_planning seq=383]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=385]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=386]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1527]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1534]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1541]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1548]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_4_log.json seq=383]: BUY → BUY_UNIT
- PPO observado [player_4_log.json seq=385]: SELL → SELL
- PPO observado [player_4_log.json seq=386]: BUY → BUY_UNIT
- Outcome observado: placement=7 (correlação, não causalidade)

### Jogador 5 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 3 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=5]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=85]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=93]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=101]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 7 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=109]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=173]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=181]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=189]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=19]: PASS → HOLD
- PPO observado [player_5_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 2 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=197]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=269]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=277]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=285]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=30]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=31]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=41]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=293]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=349]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=357]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=365]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=41]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=42]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=44]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=54]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=373]: INSUFFICIENT_EVIDENCE (reason unavailable)
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
- Strategic reviews únicos: 2 (observações=13) · PPO actions: 3 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=70]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=453]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=509]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=517]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=525]: baseline=NONE · contextual=HOLD
- PPO observado [player_5_log.json seq=70]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=71]: BUY_XP → BUY_XP
- PPO observado [player_5_log.json seq=72]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 7 (same_player_round)
- Strategic reviews únicos: 3 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0, e79e0b44fb8b780e395642c6c706fc35@1
- Strategic Planner [shadow_planning seq=82]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=533]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Strategic Planner [context_bridge seq=605]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=589]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=597]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=605]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=85]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=87]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=88]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=89]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=90]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: e79e0b44fb8b780e395642c6c706fc35@1
- Strategic Planner [shadow_planning seq=101]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=613]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=629]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=637]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=645]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=101]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=102]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=104]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 9 (same_player_round)
- Strategic reviews únicos: 9 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: e79e0b44fb8b780e395642c6c706fc35@1
- Strategic Planner [shadow_planning seq=114]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=116]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=118]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=119]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=120]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=122]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=123]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=653]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=661]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=701]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=709]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=717]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_5_log.json seq=118]: BUY_XP → BUY_XP
- PPO observado [player_5_log.json seq=119]: BUY_XP → BUY_XP
- PPO observado [player_5_log.json seq=120]: SELL → SELL
- PPO observado [player_5_log.json seq=122]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=123]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=136]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=137]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=139]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=140]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=725]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=765]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=773]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=781]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=134]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=136]: SELL → SELL
- PPO observado [player_5_log.json seq=137]: SELL → SELL
- PPO observado [player_5_log.json seq=139]: SELL → SELL
- PPO observado [player_5_log.json seq=140]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=150]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=153]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=789]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=797]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=805]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=813]: baseline=MOVE · contextual=MOVE
- PPO observado [player_5_log.json seq=150]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=153]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 12 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=163]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=164]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=165]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=166]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=167]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=169]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=821]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=861]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=869]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=877]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=164]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=165]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=166]: SELL → SELL
- PPO observado [player_5_log.json seq=167]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=169]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 13 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=179]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=180]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=885]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=893]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=901]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=909]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=179]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=180]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 14 (same_player_round)
- Strategic reviews únicos: 8 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=190]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=192]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=193]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=194]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=195]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=196]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=917]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=925]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=957]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=965]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=973]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=192]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=193]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=194]: MOVE_BOARD → MOVE
- PPO observado [player_5_log.json seq=195]: SELL → SELL
- PPO observado [player_5_log.json seq=196]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 15 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=207]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=209]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=981]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=989]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=997]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1005]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=207]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=209]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 16 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=219]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=222]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=223]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=224]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=225]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=226]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1013]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1053]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1061]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1069]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=222]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=223]: SELL → SELL
- PPO observado [player_5_log.json seq=224]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=225]: SELL → SELL
- PPO observado [player_5_log.json seq=226]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 17 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=238]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=239]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1077]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1085]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1093]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1101]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=238]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=239]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 18 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=251]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=254]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=256]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=257]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=259]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1109]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1141]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1149]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1157]: baseline=BUY_UNIT · contextual=HOLD
- PPO observado [player_5_log.json seq=251]: SELL → SELL
- PPO observado [player_5_log.json seq=254]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=256]: SELL → SELL
- PPO observado [player_5_log.json seq=257]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=259]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 19 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=270]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=272]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=273]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1165]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1181]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1189]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1197]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=270]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=272]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=273]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=283]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=284]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=287]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=290]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=291]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1205]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1237]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1245]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1253]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=283]: SELL → SELL
- PPO observado [player_5_log.json seq=284]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=287]: SELL → SELL
- PPO observado [player_5_log.json seq=290]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=291]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=301]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=303]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=306]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1261]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1277]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1285]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1293]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=301]: SELL → SELL
- PPO observado [player_5_log.json seq=303]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=306]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=316]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=318]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=320]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=321]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=322]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1301]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1333]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1341]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1349]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=316]: SELL → SELL
- PPO observado [player_5_log.json seq=318]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=320]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_5_log.json seq=321]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_5_log.json seq=322]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=334]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=336]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=337]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1357]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1373]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1381]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1388]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=334]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=336]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=337]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=347]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=350]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=353]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=355]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=356]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1395]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1423]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1430]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1437]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=347]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=350]: SELL → SELL
- PPO observado [player_5_log.json seq=353]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=355]: SELL → SELL
- PPO observado [player_5_log.json seq=356]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 25 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=367]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=369]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=370]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1444]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1458]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1465]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1472]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=367]: SELL → SELL
- PPO observado [player_5_log.json seq=369]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=370]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 26 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=380]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=383]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=384]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=385]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=388]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1479]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1507]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1514]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1521]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=380]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=383]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=384]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_5_log.json seq=385]: SELL → SELL
- PPO observado [player_5_log.json seq=388]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=398]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=399]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=401]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1528]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1542]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1549]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1555]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_5_log.json seq=398]: SELL → SELL
- PPO observado [player_5_log.json seq=399]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=401]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 28 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=412]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=414]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=416]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=418]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1561]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1591]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1579]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1585]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1591]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_5_log.json seq=412]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=414]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=416]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=418]: REROLL → REROLL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 29 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@3
- Strategic Planner [shadow_planning seq=429]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=430]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=431]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=432]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1597]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1615]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1621]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1627]: baseline=MOVE · contextual=MOVE
- PPO observado [player_5_log.json seq=429]: SELL → SELL
- PPO observado [player_5_log.json seq=430]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=431]: SELL → SELL
- PPO observado [player_5_log.json seq=432]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@4
- Strategic Planner [shadow_planning seq=444]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=445]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=448]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=451]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1633]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1651]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1657]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1662]: baseline=HOLD · contextual=HOLD
- PPO observado [player_5_log.json seq=444]: MOVE_BENCH → MOVE
- PPO observado [player_5_log.json seq=445]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=448]: SELL → SELL
- PPO observado [player_5_log.json seq=451]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 31 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@4
- Strategic Planner [shadow_planning seq=461]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=463]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=465]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=466]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1666]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1678]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1682]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1686]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_5_log.json seq=461]: SELL → SELL
- PPO observado [player_5_log.json seq=463]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=465]: SELL → SELL
- PPO observado [player_5_log.json seq=466]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 32 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@4
- Strategic Planner [shadow_planning seq=476]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=477]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=478]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=479]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1689]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1698]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1701]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1704]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_5_log.json seq=476]: SELL → SELL
- PPO observado [player_5_log.json seq=477]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=478]: SELL → SELL
- PPO observado [player_5_log.json seq=479]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 33 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@4
- Strategic Planner [shadow_planning seq=490]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=491]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=493]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=494]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1707]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1716]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1719]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1722]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_5_log.json seq=490]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_5_log.json seq=491]: SELL → SELL
- PPO observado [player_5_log.json seq=493]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=494]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 5 · round 34 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@4
- Strategic Planner [shadow_planning seq=505]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=507]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=509]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=511]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1725]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1731]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1734]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1737]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_5_log.json seq=505]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=507]: SELL → SELL
- PPO observado [player_5_log.json seq=509]: BUY → BUY_UNIT
- PPO observado [player_5_log.json seq=511]: SELL → SELL
- Outcome observado: placement=3 (correlação, não causalidade)

### Jogador 6 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 3 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=6]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=86]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=94]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=102]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 4 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=110]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=174]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=182]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=190]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=14]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=15]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=16]: PASS → HOLD
- PPO observado [player_6_log.json seq=17]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 6 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=27]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=198]: INSUFFICIENT_EVIDENCE (reason unavailable)
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
- Strategic reviews únicos: 2 (observações=12) · PPO actions: 2 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=42]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=294]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=350]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=358]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=366]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=42]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=43]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=53]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=374]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=430]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=438]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=446]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=54]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=55]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=57]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=58]: PASS → HOLD
- PPO observado [player_6_log.json seq=59]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 5 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=69]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=454]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=510]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=518]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=526]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=69]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=70]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=72]: SELL → SELL
- PPO observado [player_6_log.json seq=73]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=74]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=84]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=534]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=590]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=598]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=606]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=85]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=88]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=89]: SELL → SELL
- PPO observado [player_6_log.json seq=91]: SELL → SELL
- PPO observado [player_6_log.json seq=92]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=102]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=614]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=630]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=638]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=646]: baseline=NONE · contextual=HOLD
- PPO observado [player_6_log.json seq=102]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=104]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=106]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 9 (same_player_round)
- Strategic reviews únicos: 9 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=116]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=117]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=118]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=119]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=120]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=121]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=123]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=654]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=662]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=702]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=710]: baseline=HOLD · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=718]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=118]: SELL → SELL
- PPO observado [player_6_log.json seq=119]: SELL → SELL
- PPO observado [player_6_log.json seq=120]: SELL → SELL
- PPO observado [player_6_log.json seq=121]: SELL → SELL
- PPO observado [player_6_log.json seq=123]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=133]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=134]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=136]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=137]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=139]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=141]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=726]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=766]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=774]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=782]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=134]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=136]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=137]: SELL → SELL
- PPO observado [player_6_log.json seq=139]: SELL → SELL
- PPO observado [player_6_log.json seq=141]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=152]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=154]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=790]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=798]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=806]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=814]: baseline=MOVE · contextual=MOVE
- PPO observado [player_6_log.json seq=152]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=154]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 12 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Feérico@1
- Strategic Planner [shadow_planning seq=164]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=165]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=166]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=167]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=168]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=169]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=822]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=862]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=870]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=878]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=165]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=166]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=167]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=168]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=169]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 13 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@2
- Strategic Planner [shadow_planning seq=179]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=886]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=894]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=902]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=910]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=179]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=181]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@2
- Strategic Planner [shadow_planning seq=191]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=918]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=958]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=966]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=974]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=192]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_6_log.json seq=193]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_6_log.json seq=194]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=196]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=197]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 15 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@2
- Strategic Planner [shadow_planning seq=207]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=209]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=982]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=990]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=998]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1006]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=207]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=209]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 16 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@2
- Strategic Planner [shadow_planning seq=220]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1014]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1054]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1062]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1070]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=222]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=223]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=224]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=225]: BUY_XP → BUY_XP
- PPO observado [player_6_log.json seq=226]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 17 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@2
- Strategic Planner [shadow_planning seq=236]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1078]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1102]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1086]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1094]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1102]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=236]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=237]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 18 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@2
- Strategic Planner [shadow_planning seq=247]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=250]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=251]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=254]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=255]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1110]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1142]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1150]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1158]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=247]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=250]: SELL → SELL
- PPO observado [player_6_log.json seq=251]: SELL → SELL
- PPO observado [player_6_log.json seq=254]: SELL → SELL
- PPO observado [player_6_log.json seq=255]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 19 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@3
- Strategic Planner [shadow_planning seq=265]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=266]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=267]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1166]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1182]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1190]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1198]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=265]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=266]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=267]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@3
- Strategic Planner [shadow_planning seq=277]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=278]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=279]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=280]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=281]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1206]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1238]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1246]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1254]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=277]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=278]: SELL → SELL
- PPO observado [player_6_log.json seq=279]: SELL → SELL
- PPO observado [player_6_log.json seq=280]: SELL → SELL
- PPO observado [player_6_log.json seq=281]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@3
- Strategic Planner [shadow_planning seq=292]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=294]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=295]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1262]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1278]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1286]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1294]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=292]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=294]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=295]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 22 (same_player_round)
- Strategic reviews únicos: 7 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@3
- Strategic Planner [shadow_planning seq=305]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=307]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=308]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=309]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=310]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1302]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1350]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1334]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1342]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1350]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=305]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=307]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=308]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=309]: MOVE_BOARD → MOVE
- PPO observado [player_6_log.json seq=310]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 23 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@3
- Strategic Planner [shadow_planning seq=320]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=321]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=323]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1358]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1374]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1374]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1382]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1389]: baseline=HOLD · contextual=HOLD
- PPO observado [player_6_log.json seq=320]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=321]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=323]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@3
- Strategic Planner [shadow_planning seq=333]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=334]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=336]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=338]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=340]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1396]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1424]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1431]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1438]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=333]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=334]: SELL → SELL
- PPO observado [player_6_log.json seq=336]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=338]: SELL → SELL
- PPO observado [player_6_log.json seq=340]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 25 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@4
- Strategic Planner [shadow_planning seq=350]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=351]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=352]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1445]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1459]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1466]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1473]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=350]: SELL → SELL
- PPO observado [player_6_log.json seq=351]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=352]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 26 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@4
- Strategic Planner [shadow_planning seq=362]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=363]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=364]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=365]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=366]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1480]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1508]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1515]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1522]: baseline=MOVE · contextual=MOVE
- PPO observado [player_6_log.json seq=362]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=363]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=364]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_6_log.json seq=365]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=366]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@4
- Strategic Planner [shadow_planning seq=376]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=377]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=379]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1529]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1543]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1550]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1556]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_6_log.json seq=376]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=377]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=379]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@4
- Strategic Planner [shadow_planning seq=389]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=391]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=394]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=395]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1562]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1580]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1586]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1592]: baseline=MOVE · contextual=MOVE
- PPO observado [player_6_log.json seq=389]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=391]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=394]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=395]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 29 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@4
- Strategic Planner [shadow_planning seq=405]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=407]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=408]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=409]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1598]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1616]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1622]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1628]: baseline=MOVE · contextual=MOVE
- PPO observado [player_6_log.json seq=405]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=407]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=408]: MOVE_BENCH → MOVE
- PPO observado [player_6_log.json seq=409]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 6 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Fumegante@4
- Strategic Planner [shadow_planning seq=419]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=420]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=422]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [shadow_planning seq=424]: KEEP (best_anchor_matches_current_direction)
- Strategic Planner [context_bridge seq=1634]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1646]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1652]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1658]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_6_log.json seq=419]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=420]: SELL → SELL
- PPO observado [player_6_log.json seq=422]: BUY → BUY_UNIT
- PPO observado [player_6_log.json seq=424]: MOVE_BENCH → MOVE
- Outcome observado: placement=5 (correlação, não causalidade)

### Jogador 7 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 2 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=7]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=87]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=95]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=103]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=3]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=19) · PPO actions: 8 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=13]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=111]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=175]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=183]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=191]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=19]: PASS → HOLD
- PPO observado [player_7_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 6 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=199]: INSUFFICIENT_EVIDENCE (reason unavailable)
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
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 5 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=46]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=295]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=351]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=359]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=367]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=46]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=47]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=49]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=50]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=51]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=61]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=375]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=431]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=439]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=447]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=63]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=64]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=65]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=66]: PASS → HOLD
- PPO observado [player_7_log.json seq=67]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=77]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=455]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=511]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=519]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=527]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=81]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=82]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=83]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=84]: SELL → SELL
- PPO observado [player_7_log.json seq=85]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 7 (same_player_round)
- Strategic reviews únicos: 3 (observações=17) · PPO actions: 7 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=95]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=535]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Strategic Planner [context_bridge seq=607]: INITIAL_SELECTION (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=591]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=599]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=607]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=98]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=99]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=100]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=102]: PASS → HOLD
- PPO observado [player_7_log.json seq=103]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 8 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=113]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=114]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [shadow_planning seq=116]: INITIAL_SELECTION (initial_direction_selected)
- Strategic Planner [context_bridge seq=615]: INITIAL_SELECTION (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=631]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=639]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=647]: baseline=NONE · contextual=HOLD
- PPO observado [player_7_log.json seq=113]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=114]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=116]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 9 (same_player_round)
- Strategic reviews únicos: 9 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=126]: PIVOT (current_direction_not_viable)
- Strategic Planner [shadow_planning seq=128]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=129]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=131]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=133]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=134]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=135]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=655]: PIVOT (reason unavailable)
- Strategic Planner [context_bridge seq=663]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=703]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=711]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=719]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=129]: SELL → SELL
- PPO observado [player_7_log.json seq=131]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=133]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=134]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=135]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 10 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=145]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=147]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=149]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=150]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=151]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=152]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=727]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=767]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=775]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=783]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_7_log.json seq=147]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=149]: SELL → SELL
- PPO observado [player_7_log.json seq=150]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=151]: SELL → SELL
- PPO observado [player_7_log.json seq=152]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=164]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=165]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=791]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=799]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=807]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=815]: baseline=MOVE · contextual=MOVE
- PPO observado [player_7_log.json seq=164]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=165]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 12 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=176]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=177]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=178]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=179]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=180]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=181]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=823]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=863]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=871]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=879]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=177]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=178]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=179]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=180]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=181]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 13 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=191]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=193]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=887]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=895]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=903]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=911]: baseline=HOLD · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=191]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=193]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 14 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=203]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=205]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=206]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=207]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=208]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=209]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=919]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=959]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=967]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=975]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=205]: SELL → SELL
- PPO observado [player_7_log.json seq=206]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=207]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=208]: BUY_XP → BUY_XP
- PPO observado [player_7_log.json seq=209]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 15 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=219]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=220]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=983]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=991]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=999]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1007]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=219]: SELL → SELL
- PPO observado [player_7_log.json seq=220]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 16 (same_player_round)
- Strategic reviews únicos: 8 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=231]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=233]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=235]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=236]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=238]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=239]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1015]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1071]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1055]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1063]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1071]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=233]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=235]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=236]: SELL → SELL
- PPO observado [player_7_log.json seq=238]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=239]: BUY_XP → BUY_XP
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 17 (same_player_round)
- Strategic reviews únicos: 4 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=249]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=250]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1079]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1103]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1087]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1095]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1103]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=249]: SELL → SELL
- PPO observado [player_7_log.json seq=250]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 18 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@1
- Strategic Planner [shadow_planning seq=260]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=262]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=263]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=264]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=265]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1111]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1143]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1151]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1159]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=260]: SELL → SELL
- PPO observado [player_7_log.json seq=262]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=263]: SELL → SELL
- PPO observado [player_7_log.json seq=264]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=265]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 19 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=275]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=276]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=277]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1167]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1183]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1191]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1199]: baseline=HOLD · contextual=BUY_XP
- PPO observado [player_7_log.json seq=275]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=276]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=277]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=287]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=288]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=289]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=290]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=291]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1207]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1239]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1247]: baseline=HOLD · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1255]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_7_log.json seq=287]: SELL → SELL
- PPO observado [player_7_log.json seq=288]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=289]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=290]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=291]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=301]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=302]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=303]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1263]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1279]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1287]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1295]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=301]: SELL → SELL
- PPO observado [player_7_log.json seq=302]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=303]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=313]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=315]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=316]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=317]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=320]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1303]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1335]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1343]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1351]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=313]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=315]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=316]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=317]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=320]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=330]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=331]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=332]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1359]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1375]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1383]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1390]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=330]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=331]: MOVE_BOARD → MOVE
- PPO observado [player_7_log.json seq=332]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=342]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=345]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=347]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=349]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=350]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1397]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1425]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1432]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1439]: baseline=BUY_UNIT · contextual=MOVE
- PPO observado [player_7_log.json seq=342]: SELL → SELL
- PPO observado [player_7_log.json seq=345]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=347]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=349]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=350]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 25 (same_player_round)
- Strategic reviews únicos: 5 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=360]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=361]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=362]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1446]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1474]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1460]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1467]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1474]: baseline=MOVE · contextual=MOVE
- PPO observado [player_7_log.json seq=360]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=361]: MOVE_BENCH → MOVE
- PPO observado [player_7_log.json seq=362]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 26 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=372]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=373]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=375]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=376]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=377]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1481]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1509]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1516]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1523]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=372]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=373]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=375]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=376]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_7_log.json seq=377]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=387]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=388]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=390]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1530]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1544]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1551]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1557]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=387]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=388]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=390]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@2
- Strategic Planner [shadow_planning seq=400]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=402]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=403]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=404]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1563]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1581]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1587]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1593]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=400]: SELL → SELL
- PPO observado [player_7_log.json seq=402]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=403]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=404]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 29 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=414]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=415]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=416]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=417]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1599]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1617]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1623]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1629]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=414]: SELL → SELL
- PPO observado [player_7_log.json seq=415]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=416]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=417]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=427]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=428]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=429]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=432]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1635]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1653]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1659]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1663]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=427]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=428]: SELL → SELL
- PPO observado [player_7_log.json seq=429]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=432]: MOVE_BOARD → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 31 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=442]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=444]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=445]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=447]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1667]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1679]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1683]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1687]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=442]: SELL → SELL
- PPO observado [player_7_log.json seq=444]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=445]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=447]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 32 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=457]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=458]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=459]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=462]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1690]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1705]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1699]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1702]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1705]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=457]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=458]: SELL → SELL
- PPO observado [player_7_log.json seq=459]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=462]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 33 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=473]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=475]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=478]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=479]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1708]: KEEP (reason unavailable)
- Strategic Planner [context_bridge seq=1723]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1717]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1720]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1723]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=473]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=475]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=478]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=479]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 34 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=489]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=490]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=491]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=492]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1726]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1735]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1738]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1740]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=489]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=490]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=491]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=492]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 35 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=503]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=506]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=507]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=509]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1742]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1748]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1750]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1752]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=503]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=506]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=507]: SELL → SELL
- PPO observado [player_7_log.json seq=509]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 36 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=519]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=521]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=522]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=523]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1754]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1760]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1762]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1764]: baseline=HOLD · contextual=HOLD
- PPO observado [player_7_log.json seq=519]: SELL → SELL
- PPO observado [player_7_log.json seq=521]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=522]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=523]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 37 (same_player_round)
- Strategic reviews únicos: 6 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=533]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=534]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=535]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=536]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1766]: ADAPT (reason unavailable)
- Strategic Planner [context_bridge seq=1768]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1772]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1774]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1776]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_7_log.json seq=533]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=534]: SELL → SELL
- PPO observado [player_7_log.json seq=535]: BUY → BUY_UNIT
- PPO observado [player_7_log.json seq=536]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 7 · round 38 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 0
- Composition identity/version: native-set-18-Colosso@3
- Strategic Planner [shadow_planning seq=546]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=547]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=548]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [shadow_planning seq=549]: ADAPT (alternative_below_required_advantage)
- Strategic Planner [context_bridge seq=1778]: ADAPT (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1784]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1786]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1787]: baseline=MOVE · contextual=MOVE
- PPO observado [player_7_log.json seq=546]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=547]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_7_log.json seq=548]: SELL → SELL
- PPO observado [player_7_log.json seq=549]: BUY → BUY_UNIT

### Jogador 8 · round 1 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 3 · Composition snapshots: 13 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=2]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=8]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=88]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=96]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=104]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=2]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=3]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=4]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 2 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 7 · Composition snapshots: 11 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=14]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=112]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=176]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=184]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=192]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=16]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=17]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=18]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=19]: PASS → HOLD
- PPO observado [player_8_log.json seq=20]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 3 (same_player_round)
- Strategic reviews únicos: 2 (observações=15) · PPO actions: 3 · Composition snapshots: 12 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=30]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=200]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=272]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=280]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=288]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=30]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=32]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=34]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 4 (same_player_round)
- Strategic reviews únicos: 2 (observações=16) · PPO actions: 6 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=44]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=296]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=352]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=360]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=368]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=45]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=47]: SELL → SELL
- PPO observado [player_8_log.json seq=49]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=50]: SELL → SELL
- PPO observado [player_8_log.json seq=51]: PASS → HOLD
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 5 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=61]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=376]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=432]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=440]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=448]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=65]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=66]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=68]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=69]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=70]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 6 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=80]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=456]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=512]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=520]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=528]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=84]: SELL → SELL
- PPO observado [player_8_log.json seq=85]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=86]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=87]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=88]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 7 (same_player_round)
- Strategic reviews únicos: 2 (observações=18) · PPO actions: 8 · Composition snapshots: 10 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=98]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=536]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=592]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=600]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=608]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=106]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=107]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=108]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=109]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=110]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 8 (same_player_round)
- Strategic reviews únicos: 2 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: unavailable@0
- Strategic Planner [shadow_planning seq=120]: INSUFFICIENT_EVIDENCE (no_initial_anchor_available)
- Strategic Planner [context_bridge seq=616]: INSUFFICIENT_EVIDENCE (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=632]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=640]: baseline=NONE · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=648]: baseline=NONE · contextual=HOLD
- PPO observado [player_8_log.json seq=120]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=122]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=123]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 9 (same_player_round)
- Strategic reviews únicos: 4 (observações=16) · PPO actions: 7 · Composition snapshots: 9 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=133]: ABANDON (current_direction_unviable_without_alternative)
- Strategic Planner [shadow_planning seq=135]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=656]: ABANDON (reason unavailable)
- Strategic Planner [context_bridge seq=664]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=704]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=712]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=720]: baseline=MOVE · contextual=MOVE
- PPO observado [player_8_log.json seq=136]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=138]: SELL → SELL
- PPO observado [player_8_log.json seq=140]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=142]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=143]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 10 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=153]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=728]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=768]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=776]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=784]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=154]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=155]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=156]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=159]: MOVE_BOARD → MOVE
- PPO observado [player_8_log.json seq=160]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 11 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=170]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=171]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=792]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=800]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=808]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=816]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=170]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=171]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 12 (same_player_round)
- Strategic reviews únicos: 7 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=181]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=182]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=183]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=184]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=186]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=188]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=824]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=864]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=872]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=880]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=182]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=183]: SELL → SELL
- PPO observado [player_8_log.json seq=184]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=186]: SELL → SELL
- PPO observado [player_8_log.json seq=188]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 13 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=199]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=201]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=888]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=896]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=904]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=912]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=199]: SELL → SELL
- PPO observado [player_8_log.json seq=201]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 14 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=211]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=920]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=960]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=968]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=976]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=212]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=213]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=214]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=215]: SELL → SELL
- PPO observado [player_8_log.json seq=217]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 15 (same_player_round)
- Strategic reviews únicos: 2 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=227]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=984]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=992]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1000]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1008]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=227]: SELL → SELL
- PPO observado [player_8_log.json seq=228]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 16 (same_player_round)
- Strategic reviews únicos: 2 (observações=14) · PPO actions: 6 · Composition snapshots: 8 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=239]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1016]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1056]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1064]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1072]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=240]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=242]: SELL → SELL
- PPO observado [player_8_log.json seq=244]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=245]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=246]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 17 (same_player_round)
- Strategic reviews únicos: 3 (observações=6) · PPO actions: 2 · Composition snapshots: 4 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=256]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=257]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1080]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1088]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1096]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1104]: baseline=BUY_XP · contextual=BUY_XP
- PPO observado [player_8_log.json seq=256]: SELL → SELL
- PPO observado [player_8_log.json seq=257]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 18 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=268]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=269]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=270]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=271]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=272]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1112]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1144]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1152]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1160]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=268]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=269]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=270]: SELL → SELL
- PPO observado [player_8_log.json seq=271]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_8_log.json seq=272]: EQUIP_FROM_INVENTORY → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 19 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=282]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=283]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [shadow_planning seq=284]: KEEP (current_direction_viable_without_alternative)
- Strategic Planner [context_bridge seq=1168]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1184]: baseline=MOVE · contextual=MOVE
- Evaluators [composition_diagnostics.jsonl seq=1192]: baseline=BUY_XP · contextual=BUY_XP
- Evaluators [composition_diagnostics.jsonl seq=1200]: baseline=MOVE · contextual=MOVE
- PPO observado [player_8_log.json seq=282]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=283]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=284]: CRAFT_AND_EQUIP → unavailable
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 20 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=294]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=296]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=297]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=298]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=299]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1208]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1240]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1248]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1256]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=294]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=296]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=297]: EQUIP_FROM_INVENTORY → unavailable
- PPO observado [player_8_log.json seq=298]: MOVE_BENCH → MOVE
- PPO observado [player_8_log.json seq=299]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 21 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=309]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=310]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=312]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1264]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1280]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1288]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1296]: baseline=BUY_UNIT · contextual=HOLD
- PPO observado [player_8_log.json seq=309]: SELL → SELL
- PPO observado [player_8_log.json seq=310]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=312]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 22 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=322]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=323]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=324]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=326]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=328]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1304]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1336]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1344]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1352]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=322]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=323]: SELL → SELL
- PPO observado [player_8_log.json seq=324]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=326]: SELL → SELL
- PPO observado [player_8_log.json seq=328]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 23 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=340]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=343]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=345]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1360]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1376]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1384]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1391]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=340]: SELL → SELL
- PPO observado [player_8_log.json seq=343]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=345]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 24 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@1
- Strategic Planner [shadow_planning seq=355]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=356]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=358]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=360]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=361]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1398]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1426]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1433]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1440]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=355]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=356]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=358]: SELL → SELL
- PPO observado [player_8_log.json seq=360]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=361]: MOVE_BENCH → MOVE
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 25 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=371]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=372]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=374]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1447]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1461]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1468]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1475]: baseline=HOLD · contextual=HOLD
- PPO observado [player_8_log.json seq=371]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=372]: SELL → SELL
- PPO observado [player_8_log.json seq=374]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 26 (same_player_round)
- Strategic reviews únicos: 6 (observações=12) · PPO actions: 5 · Composition snapshots: 7 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=385]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=386]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=387]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=388]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=390]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1482]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1510]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1517]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1524]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=385]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=386]: CRAFT_AND_EQUIP → unavailable
- PPO observado [player_8_log.json seq=387]: SELL → SELL
- PPO observado [player_8_log.json seq=388]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=390]: SELL → SELL
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 27 (same_player_round)
- Strategic reviews únicos: 4 (observações=8) · PPO actions: 3 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=400]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=402]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=403]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1531]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1545]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1552]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1558]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=400]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=402]: SELL → SELL
- PPO observado [player_8_log.json seq=403]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 28 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=413]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=414]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=415]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=416]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1564]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1582]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1588]: baseline=HOLD · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1594]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_8_log.json seq=413]: SELL → SELL
- PPO observado [player_8_log.json seq=414]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=415]: SELL → SELL
- PPO observado [player_8_log.json seq=416]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 29 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=426]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=427]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=428]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=430]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1600]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1618]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1624]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1630]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=426]: SELL → SELL
- PPO observado [player_8_log.json seq=427]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=428]: SELL → SELL
- PPO observado [player_8_log.json seq=430]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 30 (same_player_round)
- Strategic reviews únicos: 5 (observações=10) · PPO actions: 4 · Composition snapshots: 6 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=440]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=441]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=442]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=443]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1636]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1654]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1660]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1664]: baseline=BUY_UNIT · contextual=BUY_UNIT
- PPO observado [player_8_log.json seq=440]: SELL → SELL
- PPO observado [player_8_log.json seq=441]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=442]: SELL → SELL
- PPO observado [player_8_log.json seq=443]: BUY → BUY_UNIT
- Outcome observado: placement=None (correlação, não causalidade)

### Jogador 8 · round 31 (same_player_round)
- Strategic reviews únicos: 5 (observações=9) · PPO actions: 4 · Composition snapshots: 5 · Outcomes: 1
- Composition identity/version: native-set-18-Enfeitiçador@2
- Strategic Planner [shadow_planning seq=453]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=454]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=456]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [shadow_planning seq=458]: KEEP (alternative_below_minimum_adapt_advantage)
- Strategic Planner [context_bridge seq=1668]: KEEP (reason unavailable)
- Evaluators [composition_diagnostics.jsonl seq=1676]: baseline=BUY_UNIT · contextual=BUY_UNIT
- Evaluators [composition_diagnostics.jsonl seq=1680]: baseline=BUY_XP · contextual=HOLD
- Evaluators [composition_diagnostics.jsonl seq=1684]: baseline=BUY_XP · contextual=HOLD
- PPO observado [player_8_log.json seq=453]: SELL → SELL
- PPO observado [player_8_log.json seq=454]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=456]: BUY → BUY_UNIT
- PPO observado [player_8_log.json seq=458]: BUY → BUY_UNIT
- Outcome observado: placement=4 (correlação, não causalidade)

## Limitações explícitas

- Associação por match/player/round não demonstra causalidade.
- Comparação com PPO usa a ação observada no log e a recomendação temporalmente mais próxima no mesmo jogador/round.
- Ação PPO não é ground truth; concordância não é métrica de qualidade.
- Taxonomia semântica v1 é uma relação diagnóstica; compatibilidade parcial não equivale a execução idêntica.
- Snapshots sem identidade ou timestamp suficiente permanecem unavailable e não são reconstruídos.
- Sessões antigas podem não conter o envelope completo; são preservadas como dados legados não correlacionáveis.
- Fontes ausentes, stale, partial ou invalid não são convertidas em zero nem substituídas por decisões artificiais.
