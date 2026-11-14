# Shadow Capability & Migration Inventory v1 (draft)

- **Status:** static audit / draft; not an implementation contract
- **Branch:** `docs/shadow-capability-migration-inventory`
- **Related issue:** #308
- **Baseline audited:** `new-arquiteture`, commit `0794040c24b5558918a0d7b2298b31b8eabd8344`
- **Scope:** C++/Python source and repository documentation inventory; no runtime behavior changed

## 1. Purpose and reading rules

This inventory answers a different question from the architecture/ownership contracts:

> What capabilities and information does the existing Shadow/Engine ecosystem already provide, what evidence supports them, and what must the new architecture preserve, adapt, or explicitly leave behind?

A class with a similar name in the new architecture is not proof of migration. A capability is considered represented only when its information, semantics, identity, provenance, lifecycle, and limitations are mapped.

### Status vocabulary

| Status | Meaning |
|---|---|
| **Implemented (static evidence)** | Source code contains the capability; this does not assert production correctness or current-set parity. |
| **Partial** | Some behavior exists, but inputs, consumers, lifecycle, or semantics are incomplete. |
| **Documented** | A repository document describes a contract or limitation; runtime conformance may still be unverified. |
| **Test present** | A relevant test file exists; this inventory does not claim it was run or passed. |
| **Unproven integration** | Components/tests exist separately, but the complete end-to-end chain is not demonstrated. |
| **Unknown / needs audit** | The current static pass did not establish the behavior or its source of truth. |
| **Blocked** | Requires a product/authority decision or post-Gate-8 evidence. |

The test references below are test-discovery evidence only. No test suite was executed as part of this documentation-only inventory.

## 2. High-level capability matrix

| Concept | What Shadow/Engine can do today | Implementation evidence | Test evidence present | Existing documentation | New-architecture representation | Migration/preservation requirement | Status / open question |
|---|---|---|---|---|---|---|---|
| Unit catalog and identity | Separate static champion definitions from owned unit instances; instances carry UUID and star state | `TftEngine.hpp`, `ChampionCatalog`, `UnitInstanceFactory` | `test_unit_instance_factory.cpp`, `test_tft_engine_pool.cpp` | `units-catalog.md` | Observed catalog reference + owned UnitInstance identity | Keep definition ID, instance UUID, star tier, and catalog version distinct | **Implemented / documented**; verify UUID guarantees across every creation/merge path |
| Unit ownership and placement | Represent board, bench, and shop as distinct collections; unit identity can follow board/bench movement | `TftEngine.hpp`, `DecisionState.hpp`, lobby engine | `test_unit_pool.cpp`, `test_lobby_end_to_end.py`, decision/movement tests | `units-catalog.md` | Unit ownership snapshot with zone/slot and source sequence | Preserve board vs bench vs shop semantics; never infer ownership from champion ID alone when duplicate copies exist | **Implemented / partial**; cross-component identity contract needed |
| Star progress / upgrades | Track star level per instance; aggregate equivalent copies for strategic evidence | `UnitPriorityPlanner.hpp`, `UnitInstance` | `test_unit_priority_planner.cpp`, lobby merge/pool tests | Issue #283; `units-catalog.md` | Per-champion, per-star-tier owned-copy evidence + explicit upgrade progress | Replace lossy aggregate counts with a canonical tier distribution; distinguish 1★→2★ and 2★→3★ progress | **Partial / blocked**; mixed-star aggregation and merge lineage require proof |
| Unit acquisition | Buy/sell and shop/pool operations are represented in lobby engine | `ShopEngine.cpp`, `UnitPool.cpp`, `TftEngine.cpp` | `test_shop_engine.cpp`, `test_unit_pool.cpp`, `test_lobby_end_to_end.py` | `economy-shop.md`, issue #283 | Shop offer evidence separate from owned units and global pool evidence | Preserve offer slot, champion identity, cost, affordability, pool certainty, and acquisition event | **Partial**; UnitPriority evidence does not currently populate all shop/cost/gold fields in audited path |
| Unit priorities | Score units against active composition and current evidence | `UnitPriorityPlanner.hpp`, planner evidence adapters | `test_unit_priority_planner.cpp`, `test_planner_evidence_adapters.cpp` | `composition-intelligence-planner-evidence.md` | Derived UnitPriority records tied to composition/candidate identity and input sequence | Preserve reason, confidence/quality, source evidence, and identity/version | **Partial**; missing shop copies, unit cost, and gold availability were previously identified |
| Lineup planning | Selects a deployable board from active composition and priorities, with entries/exits/deferred targets | `LineupPlanner.hpp` | `test_lineup_planner.cpp` | Ownership integration draft | Derived Lineup proposal with exact selected board, entries, exits, deferred IDs | Positioning/evaluation must consume the exact resulting lineup, not reconstruct from candidate composition units | **Unproven integration** |
| Board quality | Scores positional, structural, synergy, strategic fit, frontline coverage, carry exposure, isolated/fragile frontline, and unplayed bench value | `BoardEvaluation.hpp`, `TftEngine.hpp` diagnostics | `test_board_evaluation.cpp`, `test_board_quality_audit.py` | `strategy-synergies-positioning.md` | Derived BoardEvaluation tied to observed board + strategy evidence | Preserve component scores and diagnostic counters; never treat heuristic score as observed combat strength | **Implemented / partial**; calibration and set-specific role quality need validation |
| Tactical positioning | 4×7 board coordinates, role placement, neighbors, placement/swap scoring | `PositioningEngine.hpp`, `BoardEvaluation.hpp` | `test_board_evaluation.cpp`, combat movement tests | `strategy-synergies-positioning.md` | Board coordinates + role/position proposal | Preserve coordinate convention, role semantics, and distinction between planning score and combat movement | **Implemented**; role-derived heuristics are not full tactical simulation |
| Strategic positioning proposal | Produces read-only placement proposals, checks snapshot identity, alive state, owned units, and native masks | `StrategicPositionPlanner.hpp`, `StrategicActionExecutor.hpp` | `test_strategic_position_planner.cpp`, executor tests | Ownership integration draft | Position proposal bound to lineup identity/version and typed source sequence | Use exact lineup and unique unit-instance identity; reject ambiguous duplicates/stale masks | **Partial / unproven integration**; current snapshot uses champion IDs and refuses duplicate ambiguity |
| Items catalog and recipes | Data-driven item definitions, recipes, stats, effects, equipability metadata | `ItemCatalog.hpp`, `ItemEngine.hpp` | `test_item_catalog.cpp`, `test_default_item_catalog.py` | `item-catalog-schema.md`, `item-catalog-generator.md` | Versioned ItemCatalog reference scoped to active set | Preserve set/catalog version, recipe identity, supported effect metadata, and unsupported-effect state | **Implemented / partial**; authoritative active-set data remains a dependency |
| Item inventory and components | Track components and completed items per player; expose conditional item masks | `ItemEngine.hpp`, `ItemActionContract.hpp`, `TftEngine.hpp` | `test_item_engine.cpp`, item mask tests | `item-system-integration-contract.md` | Observed component/inventory state + legal action candidates | Preserve component counts, item IDs, inventory capacity, and native legality | **Implemented** for modeled catalog/flows; current-set parity not assumed |
| Equipment ownership | Attach equipped items to unit UUID; project items into combat input; support internal merge transfer and sale return-to-inventory | `ItemEngine.hpp`, `CombatItemAdapter.hpp`, `TftEngine.hpp` | `test_item_engine.cpp`, `test_audit_item_system_e2e.py`, combat tests | `item-system-integration-contract.md`, `item-system-final-report.md` | Equipment association keyed by UnitInstance UUID | Preserve ownership through movement; explicitly model merge/sale/transfer/unequip rules or mark unsupported | **Partial**; no general policy transfer/unequip action; internal merge/sale lifecycle paths exist |
| Item compatibility and combat effects | Score compatibility by unit profile/role and supported effects; pass equipped items to combat | `ItemEngine.hpp`, `CombatItemAdapter.hpp`, combat engine | `test_item_engine.cpp`, combat item tests | Item system docs | Derived item-fit evidence + supported combat-effect projection | Separate compatibility heuristic from verified combat effect; carry unsupported/deferred stats | **Partial**; adapter presence does not prove every stat/effect is simulated |
| PvE loot / anvils | Expose grant APIs and model selected simulated component/item-anvil flows | `PveLootDistribution.hpp`, `ItemEngine.hpp`, lobby engine | item engine/lobby tests | `item-system-integration-contract.md`, `set18-pve-loot.md` | Observed reward offer + acquisition event with source provenance | Do not invent official drop odds; represent unknown/unavailable loot source explicitly | **Partial / blocked**; production loot resolver remains dependency |
| Economy state | Track gold, level, XP, costs, income-related game state and lobby actions | `EconomyEngine.hpp`, `TftEngine.hpp` | `test_economy_engine.cpp`, `test_buy_xp_coverage_audit.py` | `economy-shop.md` | Observed economy snapshot with per-field provenance | Preserve raw values and distinguish observed zero from missing/default | **Implemented** for core state; full strategic interpretation incomplete |
| Economic posture / progression | Derive posture and progression hypotheses from economic/strategic context | `EconomicController.hpp`, strategic context | `test_strategic_economic_comparison.py`, strategic tests | `strategic-economic-planning.md`, `economic-action-audit.md` | Derived EconomicPosture + ProgressionHypothesis | Preserve source, horizon, uncertainty, reason, and cost decomposition; not a strategy ID or executable action | **Partial**; projected income/damage/elimination evidence and consumer wiring incomplete |
| Shop / pool availability | Represent five shop slots and finite champion pool with buy/sell stock changes | `ShopEngine.hpp`, `UnitPool.hpp`, `TftEngine.cpp` | `test_shop_engine.cpp`, `test_unit_pool.cpp`, `test_tft_engine_pool.cpp` | `economy-shop.md`, `units-catalog.md` | ShopOffer and PoolAvailability as separate evidence domains | Do not collapse shop offer, owned copies, and global pool; unknown pool is not zero | **Implemented / partial**; strategic consumers need consistent uncertainty semantics |
| Action candidates | Evaluators accept candidate records and score/filter action options | `CompositionActionEvaluator.hpp`, `ContextualActionEvaluator.hpp` | `test_composition_action_evaluator.cpp`, `test_contextual_action_evaluator.cpp` | `dual-action-evaluator-shadow.md`, ownership draft | Typed ActionCandidate with candidate ID/revision and physical parameters | Define exact source slot, target slot, cost, horizon, risk, and evidence; distinguish empty set from HOLD | **Partial / blocked**; audited call path did not populate candidate collection |
| Action evaluation | Baseline and contextual evaluators score board, economy, priorities, upgrades, composition | same as above; `ActionEvaluator.hpp` | evaluator tests | `dual-action-evaluator-shadow.md` | Separate evaluation records with evaluator identity and score semantics | Keep scores incomparable unless calibrated; HOLD must be explicit and consistent | **Partial**; baseline/contextual score semantics differ |
| Shadow action resolution | Resolve a proposal against native state/masks without applying game actions | `StrategicActionExecutor.hpp` | executor tests | ownership integration draft | Read-only resolution result referencing exact snapshot/masks | Preserve Engine mask as final authority; stale/ambiguous proposals rejected | **Implemented / partial**; complete recommendation-to-resolution trace still needed |
| Outcomes and replay | Record composition diagnostics and stage/snapshot traces; outcome observation is optional | `CompositionDiagnostics.hpp`, CI runtime | `test_composition_diagnostics.cpp`, replay/audit tests | `sessions-logs-replay.md`, ownership draft | Correlated Recommendation, ActionObservation, OutcomeObservation, ReplayTrace | Use typed sequence references, explicit outcome windows and missingness; correlation is not causation/reward | **Partial / unproven integration**; audited runtime capture does not supply outcome observation |
| Strategic direction and composition | Planner commitments, CI active composition, pivot candidates/transitions, focus/core traits and lock-like fields | strategic planner, ActiveCompositionManager, pivot coordinator, context bridge | strategic planner/transition/bridge tests | `strategic-ownership-integration.v1.draft.md` | Distinct typed concepts with one approved owner each | Preserve semantic distinctions and provenance; no parallel owner may silently publish canonical state | **Implemented / ownership blocked**; see Gate 5 |
| Traits and synergies | Count traits, compute active/breakpoint state and score marginal synergy | `SynergyCounter.hpp`, `SynergyEngine.hpp`, trait milestones | `test_synergy_counter.cpp`, `test_trait_milestones.cpp` | `strategy-synergies-positioning.md`, `units-catalog.md` | Observed unit traits + derived trait counts/breakpoints | Bind to active set's trait catalog and preserve partial/active/breakpoint semantics | **Implemented / set-dependent**; validate catalog version and trait changes |
| Combat projection/simulation | Convert lobby units/items/profiles into combat input and simulate combat outcomes | `CombatInput.hpp`, `CombatEngine.hpp`, combat sources | combat engine, determinism, integration tests | `combat.md`, item docs | Separate observed pre-combat state, simulation inputs, simulated outcomes, and observed match outcomes | Never conflate simulated estimate with actual TFT result; preserve combat model/version | **Implemented / scope-limited**; simulator fidelity vs live TFT needs separate validation |
| Health, elimination, placement | Track player HP/alive/eliminated/placement and damage fields | `TftEngine.hpp`, lobby engine | full-match/terminal ranking tests | lobby/replay docs | Observed player status + event timestamps/sequences | Preserve elimination transition and terminal placement semantics | **Implemented** in simulated lobby; live-source mapping unknown |
| Action legality and anti-loop | Generate native masks, validate moves, track repeated states/reversals/oscillation | `ActionMaskEngine.hpp`, `MoveValidator.hpp`, `AntiLoopEngine.hpp`, `DecisionHistory.hpp` | mask, move, anti-loop, PPO consistency tests | `action-mask-contract.v1.draft.md`, `decisions-masks-antiloop.md` | Native legality/mask interface remains final authority; loop diagnostics separate | Do not migrate strategic heuristic as legality; preserve exact mask semantics and sequence/state scope | **Implemented / contract in progress**; runtime changes remain outside this audit |
| Observation and reward boundary | Engine emits observations/masks and reward state for PPO | TftEngine, observation/reward sources | dimension, mask, reward tests | observation/reward contracts | Separate observed facts, derived Shadow evidence, PPO observation/reward contracts | No Shadow recommendation/outcome becomes PPO target/reward without separate approval | **Existing contracts / protected boundary** |
| Identity and provenance | Some runtimes carry match/player/round/sequence; newer strategic contract defines typed sequence references and provenance classes | CI runtime, context bridge, strategic evidence | identity/bridge/sequence tests | ownership integration draft | Common identity envelope + typed source-sequence refs | Preserve scope/namespace, producing component, value, quality, origin, and composition/candidate lineage | **Partial**; older sequence domains and default identity/provenance gaps remain |
| Lifecycle and reset | Engine reset clears/recreates player runtimes and state; item/units have reset paths | `TftEngine::reset`, CI runtime reset, ItemEngine lifecycle | reset-related lobby/item/strategic tests | units/item/ownership docs | Explicit episode lifecycle events and per-subsystem reset contract | Prove two episodes on same Engine do not leak state, identity, counters, equipment, diagnostics, or sequence | **Partial / evidence blocked**; same-instance two-match regression still required |

## 3. Detailed findings and migration notes

### 3.1 Units — required first-class capability

Units are not just a list of champion IDs. The current system contains at least these distinct layers:

1. **ChampionDefinition:** static catalog facts (internal ID, API name, cost, traits, stats, role/profile, ability and icons).
2. **UnitInstance:** a specific owned copy with UUID, champion reference, star level, and equipped items.
3. **Ownership location:** board slot or bench slot; shop offers are not owned copies.
4. **Shop offer:** a temporary acquisition opportunity with slot and cost.
5. **Pool availability:** global finite-stock state, which may be unavailable to an external observer.
6. **Star-tier distribution:** counts of owned 1★, 2★, and 3★ instances, not only a scalar equivalent-copy total.
7. **Upgrade progress:** progress toward the next star tier, computed from eligible same-tier copies under the set's merge rules.
8. **Strategic priority:** derived value of owning/seeking/keeping/upgrading a unit for a specific composition/candidate.
9. **Lineup intent:** desired deployable board, entries, exits, and deferred targets.
10. **Equipment association:** items belong to a unit instance, not merely to a champion definition.

Previously identified gap in issue #283 is confirmed in the current `TftEngine.cpp` callsite: board+bench copies are aggregated by champion ID, `highest_star` is tracked separately, and `copies_toward_next_star` is calculated from the aggregate total using the highest star tier. A mixed 1★/2★ collection can therefore lose tier-specific progress. The same callsite constructs `UnitPriorityEvidence` without populating `copies_in_shop` or `unit_cost`, and the inspected `UnitPriorityContext` construction does not supply `gold_available` (its default is the explicit unknown sentinel -1). These are not cosmetic omissions: they affect affordability, upgrade feasibility, pivot feasibility, and whether a recommendation can be executed.

**Migration rule:** the new architecture must retain raw per-instance facts and derive tier progress from a canonical distribution. Do not serialize only a single aggregate copy count. Keep owned copies, shop offers, and pool availability in separate structures. An unknown pool must remain unknown.

**Identity rule:** champion ID identifies a definition; UUID identifies an owned instance. Any proposal that needs a physical source/target must resolve to an instance identity and exact zone/slot. Champion-only positioning snapshots must reject duplicate ambiguity rather than choose an arbitrary copy.

**Required evidence after Gate 8:** mixed-tier upgrade cases; 1★→2★ and 2★→3★ boundaries; board+bench combinations; duplicate copies in shop; affordable/unaffordable offers; unknown pool; sale/merge item preservation; pivot and lineup consumers using the same tier evidence.

### 3.2 Board and Positioning

The code has two related but different layers:
- `PositioningEngine` provides 4×7 coordinate and role-placement heuristics.
- `BoardEvaluation` evaluates structural/positional quality, frontline lanes, carry exposure, isolated/fragile frontline, strategic fit, trait coherence, and important bench units left unused.
- `StrategicPositionPlanner` produces a read-only proposal tied to a match/player/round/sequence and composition identity/version, checks native masks, and rejects duplicate champion IDs when it cannot identify a unique physical copy.

Do not collapse board quality into positioning score. A board may have a good role placement but poor frontline coverage or composition fit. Conversely, a strategic position proposal is not proof of combat outcome.

**Migration rule:** represent observed board slots separately from derived board-quality features and from proposed placement. The proposal must be tied to the exact lineup selected by LineupPlanner and the same source snapshot/mask sequence. Preserve role classification uncertainty and the fact that the current strategic position DTO identifies champion IDs rather than unique UUIDs.

### 3.3 Items and Equipment

The repository already has substantial item infrastructure and documentation, but its own final report explicitly distinguishes integrated infrastructure from readiness for a real active-set match. Catalog, recipes, per-player inventory, component masks, equipment keyed by unit UUID, and combat projection exist. Some player-level items are deliberately not unit-equipable. Internal equipment lifecycle helpers exist: merge transfers equipped items to the upgraded UUID (with overflow returned to inventory), and sale returns equipped items to the player's inventory before removing the unit. There is no general policy transfer/unequip action. The lobby also has an explicit Set 18 weighted PvE table and stage-based component/item rewards; that is a project simulation contract, not evidence that the live external loot source or official odds are being observed.

**Migration rule:** preserve item catalog/set version, recipe and component identity, inventory, equipped-item ownership by unit UUID, supported effect metadata, deferred/unsupported stats, and acquisition provenance. Keep compatibility scores separate from combat-effect simulation. Model unsupported lifecycle actions as unsupported rather than silently approximating them.

**Open questions:** active-set authoritative catalog; production/live loot source parity; effect coverage in combat simulation (including deferred stats and trait-count-gated effects); exact sale/merge rules against the active set; whether future product requirements need explicit transfer/unequip actions; inventory/capacity rules for the active set.

### 3.4 Economy, Progression, Shop, and Pool

Observed lobby economy (gold, level, XP, costs) is different from strategic economic interpretation (posture, progression hypothesis, projected income, survival risk, opportunity cost). The shop and global pool are also different sources from owned units.

**Migration rule:** retain raw observed economy values and attach provenance/validity per field. Derived estimates require horizon and uncertainty. Do not convert missing values to zero or treat default values as observed. Keep direct gold cost, lost interest, opportunity cost, board/survival/streak/composition/upgrade components separately so consumers can inspect double counting.

**Open questions:** complete evidence source for projected income, incoming damage and elimination risk; consistent streak consumption; progression evidence sufficiency; economic evidence delivered to both baseline and contextual evaluators; pool availability when source is unavailable.

### 3.5 Action candidates and evaluators

The baseline `CompositionActionEvaluator` and `ContextualActionEvaluator` are distinct evaluation paths with different score semantics. Existing audit found that the candidate vector was not populated in the inspected integrated call path; empty candidates could still appear comparison-available. A baseline ActionEvaluator recommendation must not be labeled as a PPO-selected action. Some physical parameters (shop slot, exact bench instance, movement source/destination, risk/horizon) are not fully represented in the candidate DTO, and SELL evidence was incomplete in the audited builder.

**Migration rule:** a candidate must have identity/revision, action kind, exact physical parameters, source snapshot/sequence, legality result, cost decomposition, expected benefit/horizon, risk, and evidence quality. Distinguish no candidates, invalid candidates, stale candidates, and an explicit HOLD candidate. Keep PPO action, baseline recommendation, and contextual recommendation separate.

### 3.6 Outcomes and Replay

Diagnostic recorders and stage/snapshot traces exist, but the audited runtime path does not pass an outcome observation to the recorder. A trace being serialized is not proof that a later real-world outcome is correlated correctly.

**Migration rule:** correlate recommendation → observed/applied action → later outcome with match/player identity, typed sequence references, candidate/composition lineage, and an explicit outcome window. Preserve missing outcomes and delayed outcomes. These records are diagnostic/correlational, not causal claims, imitation labels, or PPO rewards.

### 3.7 Cross-cutting identity, provenance, and lifecycle

The strategic ownership draft now defines a typed `source_sequence_ref` with scope/namespace, producing component, and value. It also separates match/episode identity, player, round, composition lineage, and candidate revision. This is the direction to reuse, not an excuse to retrofit all old integer sequences as comparable.

The inspected `TFTEngine::reset()` increments the episode ID, recreates CI/native candidate/diagnostic state, resets strategic Shadow executors/sequences/commitments, returns shop offers before resetting the pool, recreates the unit factory, and reinitializes players. `ItemEngine::reset()` clears components, inventory, equipped ownership, pending anvils, and metrics. These are concrete reset paths, but the inventory does not treat them as proven isolation: a regression that runs two matches through the same Engine instance is still required.

**Migration rule:** every observation/evidence/recommendation/outcome must declare identity, origin, quality, source, sequence scope, and applicable composition/candidate lineage. Every subsystem must declare reset ownership and what survives or is cleared at match, round, composition transition, and player elimination boundaries.

## 4. Additional capabilities found and boundaries to preserve

| Capability | Existing evidence | Migration note |
|---|---|---|
| Traits and breakpoints | `SynergyCounter.hpp`, `SynergyEngine.hpp`, `TraitMilestones.hpp` | Set-versioned catalog facts vs derived active/partial breakpoint counts |
| Combat model | `CombatEngine.hpp`, `CombatInput.hpp`, combat tests | Keep simulated combat inputs/results distinct from observed TFT combat results |
| PvE reward flow | `PveLootDistribution.hpp`, item/lobby integration | Preserve source and uncertainty; no invented live drop schedule |
| Health/elimination/placement | `PlayerInfo`, lobby engine and terminal ranking tests | Match/player lifecycle events need sequence and terminal-state provenance |
| Native action legality | `ActionMaskEngine.hpp`, `MoveValidator.hpp` | Engine masks remain final legality authority; Shadow only proposes |
| Anti-loop history | `AntiLoopEngine.hpp`, `DecisionHistory.hpp` | Keep legality and loop prevention separate from strategic preferences |
| Observation/reward | Engine observation/reward contracts and PPO tests | Protected boundary; Shadow diagnostics do not become PPO inputs/targets by implication |
| Viewer/telemetry | Viewer and JSONL diagnostic paths | Presentation/logging is not a state authority or proof of source freshness |

This is a discovery inventory, not a claim that every subsystem above belongs in the first live-inference payload. The eventual product boundary must be decided explicitly.

## 5. Existing documentation map

| Document | What it already covers | What it does not settle by itself |
|---|---|---|
| `docs/units-catalog.md` | Definition vs instance, catalog, pool, UUID invariants | Strategic tier-progress, shop/pool uncertainty, priority and pivot evidence |
| Issue #283 | Unit copies, pairs, star progress and evidence gaps | Complete unit migration contract |
| `docs/strategy-synergies-positioning.md` | Role placement and synergy/positioning concepts | End-to-end lineup→position→executor migration |
| `docs/item-system-integration-contract.md` | Item actions, catalog, inventory, equipment lifecycle, tests and limits | Live active-set/loot correctness and full combat effect parity |
| `docs/item-system-final-report.md` | Implemented infrastructure and explicit blockers | Proof of real-match outcomes or trained improvement |
| `docs/economy-shop.md`, `docs/economic-action-audit.md` | Economy/shop behavior and audit signals | Complete economic evidence provenance and evaluator wiring |
| `docs/dual-action-evaluator-shadow.md` | Baseline/contextual evaluator distinction | Candidate population and comparable score semantics |
| `docs/sessions-logs-replay.md` | Session/log/replay concepts | Outcome capture and full typed cross-domain correlation |
| `docs/strategic-ownership-integration.v1.draft.md` | Ownership, semantic distinctions, provenance, identity, sequence and known integration gaps | Final owner decision and runtime proof |
| Observation/action/reward contract drafts | PPO-facing boundaries | Whether every Shadow capability is represented in the live-inference DTO |

## 6. Evidence still required

### Static follow-up before this inventory can be called complete
- Trace every capability from declaration to production callsite, not only its header/API.
- Inspect implementation files for item sale/merge, unit merge, pool reset, shop refresh, economy updates, combat item effect dispatch, and diagnostic outcome capture.
- Map each test to the behavior it asserts; distinguish unit-level tests from integrated replay.
- Search for additional player-state domains (augments, portals/encounters, artifacts, consumables, rerolls/armory, tactician/player equipment, opponent scouting) and mark absent vs not observed.
- Confirm current catalog/set assumptions and which data sources are authoritative.

### Additional domain discovery result
The recursive source/test/doc path inventory at the audited baseline found dedicated modules for units, items, shop/pool, economy, combat, traits, positioning, rewards, and strategic composition. It did **not** find dedicated runtime modules or test suites named for augments, portals/encounters, artifacts, consumables, tactician/player equipment, or opponent scouting. This is a repository-path discovery result only: it means **not found in this pass**, not proof that the concepts are impossible or absent from generic DTOs, catalog metadata, or unsearched data. These domains remain explicit unknowns until source-level searches confirm whether they are out of scope, represented indirectly, or missing.

### Runtime evidence after Gate 8 only
- Execute relevant focused C++/Python tests and record exact commit, command, and result.
- Add/execute integrated replays for Units, item lifecycle, lineup-to-positioning, candidate generation/evaluation, outcome correlation, and same-Engine two-match reset.
- Validate that native masks are used at the final resolution boundary and that no Shadow proposal mutates game state.
- Validate the live snapshot's completeness and explicit unknown/stale/partial states.

## 7. Gate relationship and implementation boundary

This inventory is a prerequisite input to the remaining Gate 5 decisions; it does not close Gate 5 and does not replace issues #281–#284 or #289. In particular, unit evidence (#283) and the cross-cutting identity/provenance requirements must be reconciled before approving strategic ownership.

**No implementation authorization is implied.** Until Gate 8 and explicit user approval:
- do not change C++ or Python runtime;
- do not change PPO, training, observations, rewards, action masks, Engine rules, Viewer, checkpoints, or historical artifacts;
- do not migrate or disable legacy systems;
- do not declare compatibility or runtime acceptance.

## 8. Audit conclusion (initial static pass)

The Shadow/Engine contains materially more reusable capability than the strategic composition subsystem alone: Units, shop/pool, items/equipment, board quality, positioning, economy, traits, combat projection, legality, anti-loop, and diagnostic replay all have existing implementation surfaces.

However, **existence is not migration readiness**. The highest-risk gaps are:
1. Unit copy/star progress and separation of owned/shop/pool evidence.
2. Equipment ownership and incomplete/blocked item lifecycle semantics.
3. Lineup-to-positioning integration and physical unit identity.
4. Candidate population/physical parameters and evaluator score semantics.
5. Economic evidence completeness and provenance.
6. Outcome capture/correlation.
7. Cross-domain sequence identity and same-Engine reset proof.
8. Active-set data and live TFT source parity.

This document is a first static inventory based on repository source/docs at the baseline commit. It intentionally marks unresolved implementation paths as partial or unknown rather than filling gaps with assumptions. Follow-up source/callsite/test tracing is required before declaring the audit complete.


## 9. Source-to-consumer trace — second static pass

This section records callsite-level findings from the baseline source. It narrows several earlier "needs trace" items and corrects any overly broad interpretation.

### 9.1 Unit evidence and lineup identity

- `TFTEngine.cpp` builds `copies_by_unit` by champion definition ID and adds `star_copies(unit.star)` across board and bench. It separately tracks the highest star, then the CI evidence builder computes `copies_toward_next_star` from the aggregate total and highest star. The mixed-tier ambiguity is therefore in the actual producer path, not only a theoretical concern.
- The same collection reduces multiple physical instances into one champion-keyed `OwnedUnitEvidence`, `UnitPriorityOwnedUnit`, and `UnitPriorityEvidence`. Equipped item IDs are deduplicated at champion level for strategic evidence. This is suitable for some composition-level heuristics but is not a lossless ownership/instance snapshot.
- `LineupPlanner` keys priorities, current board membership, selected slots, entries, exits, and deferred targets by champion ID. It selects at most one `LineupSlot` per champion ID. It therefore describes a composition-level target lineup, not an exact physical deployment plan when multiple copies of the same champion exist.
- `StrategicPositionPlanner` receives board/bench champion IDs, not UUIDs. It explicitly rejects duplicate champion IDs as ambiguous and does not propose implicit swaps. This is a safe failure mode, but it means exact instance-level positioning is not yet represented end-to-end.
- Native composition generation does ingest owned board/bench summaries, shop champion IDs, and pool counts. Those are separate inputs at generation time, but the CI unit-priority evidence path is less complete. Do not generalize the CI evidence gap to every native strategic subsystem.

**Migration conclusion:** retain a lossless list of unit instances (UUID, champion definition, star tier, zone, slot, equipment) and derive champion-level aggregates as separate views. Lineup plans must either reference exact instance IDs or explicitly declare that they are abstract champion-level targets awaiting instance resolution.

### 9.2 Shop, pool, and uncertainty

- `ShopEngine` has exactly five offer slots, a lock state, reroll behavior, and returns prior offers to the pool before drawing replacements. Offer slots and shop lock are part of the observed state and must not be reduced to a set of champion IDs.
- `UnitPool` exposes per-champion available count and a reset operation. In this local simulator, pool count is known from the modeled pool. A live external snapshot may not expose this value; the new DTO must preserve unknown/unavailable separately from numeric zero.
- Native composition generation consumes `shop_ids` and `pool_remaining`; the CI priority evidence builder does not populate `copies_in_shop` or `unit_cost` in the inspected callsite. A champion present in shop is represented as a boolean/set in some strategic flows, losing duplicate offer slots.
- The strategic pivot discovery path also sees shop presence and pool count, but its feasibility input deliberately leaves protected reserve floor and transition economic cost at missing sentinels. Do not treat a proposed pivot as economically approved.

**Migration conclusion:** model each shop slot as an offer record (slot, champion, cost, availability/lock context), pool evidence as a separate optional source, and owned copies as instances. Include freshness and confidence/availability; never infer pool count from absence in shop.

### 9.3 Economy and progression input completeness

The inspected `StrategicSharedContext` producer explicitly fills gold, level, XP, XP-to-next, current interest, win/loss streak, board power, relative board power, direction, and alive state. In the inspected producer path, it does not assign `progression_plan`, `projected_next_round_income`, `estimated_incoming_damage`, or `elimination_risk`; these retain struct defaults. Consequently, `EconomicController` reads zero/default incoming-damage and elimination pressure and the default `Flexible` progression plan in that path. This is a concrete producer/consumer contract gap, not proof those values are unavailable elsewhere in the Engine.

The action-evaluation path consumes an independently built `EconomicControlDecision` and `PlannerEvidenceSnapshot`. The CI priority context does not receive shop-copy count, unit cost, or populated gold-available evidence in the inspected builder. The `UnitPriorityContext` default for unavailable gold is a sentinel, not an observed zero.

**Migration conclusion:** each field needs source, observed/derived classification, validity, and explicit unknown. The DTO must not make a default value look like a real observation. Progression plan and economic posture remain derived hypotheses with their own evidence and horizon.

### 9.4 Action candidates and evaluator comparison

- `StrategicSharedContext` defines `action_candidates`, and both evaluators consume that vector.
- In the inspected `TFTEngine.cpp` producer, the strategic context is populated with owned units and anchor candidates, but no action-candidate records are appended or assigned before the evaluators run. The source file only reads the vector for evaluation/comparison. On this path, the candidate set therefore remains empty unless another producer mutates it outside the inspected flow.
- The baseline `CompositionActionEvaluator` and independent `ContextualActionEvaluator` both explicitly handle an empty candidate list; their default/hold behavior can still yield a non-stale evaluator result. Therefore `comparison_available = true` is not equivalent to "real candidates were compared." The emitted `same_initial_candidate_set` and three candidate counts must be interpreted together.
- Candidate DTOs primarily identify action kind and champion ID with coarse cost/value fields; they do not consistently encode physical source slot, exact UnitInstance UUID, destination slot, offer slot, or a complete executable parameter set.
- The policy action is explicitly labeled as not ground truth in the comparison diagnostic. Evaluator recommendations are Shadow diagnostics and are not PPO actions.

**Migration conclusion:** represent candidate-set status separately (not-produced, empty, populated, rejected), require physical parameters where an action targets an instance/slot, and make "comparison available" require a non-empty, identity-matched candidate set if the product intends a meaningful comparison.

### 9.5 Outcomes and replay capture

- `CompositionDiagnosticRecorder::capture` accepts an optional `CompositionOutcomeObservation` and serializes either the supplied observation or explicit null.
- The inspected runtime call in `TFTEngine.cpp` calls `runtime.recorder.capture(..., published_transition)` without an outcome argument. No later outcome is passed in this capture call.
- The diagnostic payload classifies outcome as observed and recommendation-to-later-outcome as correlated, but those fields remain null when the runtime does not supply the optional outcome. The schema capability is present; the runtime outcome producer/correlation chain is not demonstrated.

**Migration conclusion:** separate schema support from runtime capture. Require an outcome producer, explicit later-round window, match/player identity, and typed source sequences before calling this a functioning recommendation-to-outcome replay.

### 9.6 Item lifecycle and reset trace

- `ItemEngine::reset()` clears components, inventory, equipped ownership, anvils, and metrics while retaining the configured item/component catalog.
- Unit sale returns champion copies to the pool, returns equipment to inventory, removes the bench instance, and credits sale gold only when the pool/equipment return path succeeds.
- Unit merge transfers equipped items from consumed instance UUIDs to the upgraded instance UUID; excess items beyond the target capacity return to inventory.
- `TFTEngine::reset()` increments episode ID, clears CI/native candidate/diagnostic collections and strategic sequences/commitments, resets strategic executors, returns shop offers before pool reset, recreates the unit factory, and calls player initialization. Player initialization clears board/bench, resets economy, resets the ItemEngine, resets anti-loop state, clears recent purchases and round/action state, and deals a new starting unit.
- This is meaningful static reset coverage. It still does not prove that every future subsystem or external recorder has no cross-episode leakage; a same-engine two-episode regression remains runtime evidence for after Gate 8.

### 9.7 Scope of domain discovery

A repository path search at the audited baseline found no dedicated modules/tests with names for augments, portals/encounters, consumables, armory, tactician equipment, or opponent scouting. The path "artifacts" match is only a cross-language parity XML artifact, not a TFT in-game artifact subsystem. These are **not found in dedicated paths in this pass**, not confirmed absent from all generic state or data sources.

### 9.8 Revised highest-risk findings

1. Unit instance identity is lost in composition-level aggregation; mixed-star progress is calculated from aggregate equivalent copies and highest star.
2. Lineup and positioning are champion-ID-based; exact duplicate-instance deployment is not represented, with positioning safely rejecting ambiguity.
3. Shop slots/lock and pool availability are separate facts; some strategic paths preserve them, while CI priority evidence omits shop copies and unit cost.
4. Economic controller receives defaults for progression plan, projected income, incoming damage, and elimination risk in the inspected producer path.
5. Action evaluators consume a candidate vector that the inspected producer path does not populate; empty comparison can still be non-stale.
6. Outcome schema supports later outcomes, but the inspected runtime capture passes no outcome.
7. Reset has substantial explicit cleanup, but same-instance multi-episode isolation is not runtime-proven.


### 9.9 Test-coverage interpretation and remaining proof gaps

The static test inventory was refined against test bodies (not executed):

- `test_unit_priority_planner.cpp` covers planner-level pair/star-progress rules and a shop-copy upgrade-priority scenario. It does not exercise the `TFTEngine.cpp` producer's mixed 1★/2★ aggregation path, nor prove the producer populates the missing shop/cost/gold fields.
- `test_lineup_planner.cpp` validates abstract champion-ID lineup selection, board capacity, role gaps, and stale evidence. It does not assert exact UnitInstance UUID selection when duplicate champion copies exist; the current LineupPlan DTO has no UUID field.
- `test_strategic_position_planner.cpp` explicitly asserts that duplicate champion instances are not guessed. This proves safe rejection, not successful UUID-aware positioning.
- `test_composition_diagnostics.cpp` supplies an outcome directly to the recorder in a unit test and verifies correlation-only labeling. It does not prove the runtime producer supplies outcomes; the inspected runtime call does not.
- `test_item_engine.cpp` covers catalog validation, compatibility, selected combat passives, and item behavior. The final item-system report still states that some stats (including deferred attack speed/omnivamp paths) are not computed by the combat simulator and that real active-set catalog/loot parity remains outstanding.
- `BoardEvaluation.hpp` explicitly computes frontline counts/lanes, carry exposure, fragile/isolated frontline, missing frontline/backline, trait coherence and role adjacency. `PositioningEngine.hpp` provides role-placement/protection heuristics on a 4×7 board. These are heuristic evaluations, not tactical pathfinding or proof of live combat outcomes.

### 9.10 Item-effect and opponent-information boundaries

The item catalog validates a finite set of supported effect operations, triggers, and condition combinations; unsupported effect operations/triggers are rejected at catalog load. `CombatItemAdapter` deliberately maps stats listed as deferred (currently including attack speed and omnivamp in the adapter) to zero in the combat projection. This is a useful explicit limitation and must survive migration as unsupported/deferred metadata rather than being silently interpreted as zero observed value.

The local simulator's strategic context computes contestation by scanning other simulated players' board and bench copies. That is simulated full-lobby state, not a dedicated live opponent-scouting feed with visibility, freshness, scouting scope, and uncertainty. The new architecture must not assume it can observe every opponent's bench or private shop in a real match.

### 9.11 Audit closure criteria refinement

Before declaring this static inventory complete, the remaining review is now focused on:
1. Confirm whether any non-`TFTEngine.cpp` producer populates `StrategicSharedContext.action_candidates` in the production Shadow path; the inspected Engine producer does not.
2. Search generic DTOs/data adapters for the in-game domains not found by path name (augments, portals/encounters, artifacts, armory/consumables, tactician equipment, scouting), and decide whether each is unsupported, out of scope, or represented indirectly.
3. Confirm whether the active-set catalog and live GEP/Overwolf source can supply item/augment/portal/opponent facts; repository simulation fixtures are not evidence of live source availability.
4. Finish callsite/test mapping for economy update and outcome capture; no runtime tests are part of this audit.


### 9.12 Unit UUID scope and episode identity

`UnitInstanceFactory` generates UUID-shaped identifiers from its seeded PRNG. `TFTEngine::reset()` recreates the factory using `impl_->seed` before initializing the next episode. With the same Engine seed, the factory's UUID sequence restarts; therefore a unit UUID must not be treated as globally unique across episodes solely because it has UUID syntax.

This does not by itself imply an in-match collision: the intended identity scope must be explicit. The strategic ownership contract already separates match/episode identity from player and source sequence; unit-instance references in the new architecture should likewise be scoped by match/episode (and player where ownership requires it), or use a generator whose uniqueness scope is explicitly guaranteed.

There is also a stale comment in `TftEngine.hpp` saying effective UUID generation will be implemented later, while `UnitInstanceFactory.cpp` already implements UUID-shaped generation. This is documentation drift, not a runtime defect, and is recorded here without changing source.

### 9.13 Existing generic state coverage for unmodeled domains

The inspected public state DTOs are focused on champion definitions/instances, board/bench/shop slots, action masks, economy, and player health/alive/placement/opponent identity. `DecisionState::PlayerState` has explicit board, bench, and shop arrays, but no dedicated augment, portal/encounter, artifact, consumable, armory, tactician-equipment, or scouting-evidence collection. `PlayerInfo` likewise exposes basic player/combat/lobby status rather than those domains.

This strengthens the finding that those capabilities are not currently first-class in the inspected native state contract. It still does not establish what an external live GEP feed may provide or whether some metadata exists in uninspected raw catalog blobs. Treat them as **not represented in the inspected native DTOs**, pending Overwolf/GEP source verification.
