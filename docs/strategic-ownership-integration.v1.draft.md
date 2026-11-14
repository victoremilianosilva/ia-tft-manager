# Strategic Ownership and Integration Contract v1 — Draft

**Status:** strategic ownership decisions approved for the documentary contract; runtime acceptance remains pending  
**Contract ID:** `tft.strategic-ownership.v1`  
**Target architecture:** `new-arquiteture`  
**Related issues:** #281, #282, #283, #284, #289, #300  
**Coordinates with:** Observation #293, Action #294, PPO/checkpoint #288

> This document consolidates the static integration audit and the approved Gate 5 authority decisions. It does not authorize runtime implementation, change strategic behavior, generate/execute actions, or modify PPO, rewards, observations, checkpoints, masks, Engine rules, or Viewer behavior.

## 1. Purpose

The new architecture contains multiple strategic state owners and several partially connected planning/evaluation components. Their existence and unit tests do not prove that the integrated runtime has one unambiguous authority or that each recommendation is based on the same fresh snapshot.

This contract establishes:
- distinct meanings for observed facts, derived evidence, commitments, hypotheses, active composition, and recommendations;
- the current ownership map and boundaries;
- integration invariants for identity, version, sequence, provenance, and stale data;
- approved ownership decisions and cross-contract requirements, with executable acceptance explicitly deferred until after Gate 8;
- replay and acceptance evidence required after Gate 8.

## 2. Normative principles

1. **Observed game state is authoritative for facts.** Board, bench, shop, items, economy, HP, level, XP, round, and masks must originate from the matching Engine snapshot or a validated source.
2. **Inference is not observation.** Direction discovery, focus, core traits, priorities, economic posture, lineup, and risk estimates must retain derived/estimated/committed provenance.
3. **A hypothesis is not an active composition.** Pivot candidates and planner recommendations cannot replace the current active composition before an explicit transition is accepted by its owner.
4. **One concept, one declared authority.** Parallel components may exist for comparison, but their state must be labeled experimental/diagnostic and must not silently overwrite the canonical state.
5. **Identity is end-to-end and typed.** Every decision/evidence chain must preserve the match/episode and player identity, round, and a typed source-sequence reference. Composition identity/version are additionally required only for composition-dependent records; candidate-only and pre-composition records must remain valid without an active composition.
6. **Freshness is stronger than internal consistency.** A snapshot must be checked against the identity/sequence expected by the receiving runtime, not only against values copied from the snapshot itself.
7. **Missing is not zero.** Unknown, unavailable, stale, partial, invalid, and observed zero remain distinct.
8. **Shadow stays read-only.** The strategic architecture may recommend and resolve diagnostic proposals, but Engine legality/masks remain final and no action is executed.
9. **No PPO imitation coupling.** Shadow recommendations, scores, confidence proxies, or outcomes do not become PPO targets/rewards by virtue of being recorded.
10. **No score comparability by assumption.** Independent evaluators with different baselines, evidence, and score semantics must be compared diagnostically, not treated as interchangeable.

## 3. Current owner map — audited facts, not final authority approval

| Component | Current responsibility observed in code/docs | Boundary / limitation |
|---|---|---|
| Engine snapshot and native masks | Source of observed game facts and final action legality | A strategic recommendation cannot override them |
| NativeStrategicCompositionGenerator | Generates candidate composition hypotheses from current evidence | A generated candidate is not an accepted active composition |
| StrategicPlanner | Owns the canonical product-facing direction commitment and reasons from StrategicEvidenceContext | Commitment remains distinct from the CI-owned active composition; preserve commitment/inference provenance |
| CompositionIntelligencePlayerRuntime + ActiveCompositionManager / TransitionManager | Sole canonical owner/commit path for active composition, transition hysteresis, recorder, history, and player sequence | Direction commitment remains owned by StrategicPlanner; immutable transition records correlate the two authorities |
| EconomicController | Produces contextual economic posture/decision and diagnostics | Posture is not a fixed strategy ID or executable action |
| UnitPriorityPlanner | Resolves unit priorities against active composition identity/version | Depends on canonical copy/progress evidence and fresh source snapshots |
| LineupPlanner | Produces a deployable lineup from active composition and priorities | Its output is not currently the direct source for the position snapshot in the audited callsite |
| CompositionActionEvaluator | Baseline evaluator path; filters/enriches candidates and delegates to ActionEvaluator with economic decision/policy argument | Its score/baseline semantics differ from ContextualActionEvaluator |
| ContextualActionEvaluator | Independent contextual evaluation using board, priority, lineup, upgrade and economic evidence | Does not consume EconomicControlDecision directly; its score is not interchangeable with baseline score |
| StrategicPositionPlanner | Produces a constrained physical position proposal using owned units, legal masks and snapshot evidence | Must be tied to the exact deployable lineup and same sequence |
| StrategicActionExecutor | Resolves Shadow proposal against native state/masks and snapshot sequence | Does not execute a real game action |
| UnifiedStrategicStateMachine / UnifiedStrategicShadowRuntime | Separate diagnostic-only Shadow state machine for comparison/audit and isolated pivot transitions | Maintains its own namespace; must not publish canonical state to CI, Planner, PPO, Engine, or Viewer |
| Viewer/JSONL diagnostics | Persists provenance, correlation, sequences and diagnostic results | Telemetry is not a state authority |

### 3.1 Authority boundary — approved decision

The audit establishes that at least three strategic states coexist:
- `strategic_planner_commitments[i]`;
- `composition_intelligence_players[i].active`;
- `strategic_shadow_runtimes[i].machine().active_composition()`.

They are not one shared state. The canonical production-facing direction is the `StrategicPlanner` commitment. The canonical active composition is owned and committed only by the Composition Intelligence transition path (`CompositionIntelligencePlayerRuntime` through `ActiveCompositionManager` / `TransitionManager`). These are related but distinct authorities: the planner owns its direction commitment; the composition owner owns the accepted concrete composition and its composition-scoped state. A transition record correlates them without one component silently overwriting the other.

`UnifiedStrategicStateMachine` and `UnifiedStrategicShadowRuntime` are diagnostic-only parallel state. They may independently evaluate/record candidate transitions in their own namespace, but cannot publish canonical direction, active composition, lock, or progression state to CI, Planner, PPO, Engine, or Viewer. Divergence is diagnostic evidence, not a last-writer-wins conflict.

This authority decision is approved for the documentary contract. It does not authorize runtime migration or prove that the existing runtime already conforms.

## 3.2 Approved Gate 5 ownership decision matrix

This matrix records the approved documentary ownership decisions; it is not runtime migration authorization. It distinguishes the component that discovers/proposes a value from the component that commits authoritative state.

| Concept | Canonical owner | Proposal / evidence producers | Mutation authority | Consumers and synchronization rule | Decision status |
|---|---|---|---|---|---|
| Strategic direction / commitment | `StrategicPlanner` commitment state, scoped to match/player | `NativeStrategicCompositionGenerator` supplies direction hypotheses; evidence adapters supply validated facts | Only the planner may create, revise, or withdraw its commitment. Consumers cannot write it back. | Publish a versioned commitment record with provenance and source-sequence refs. Active composition owner may accept/reject a related transition but cannot silently rewrite the planner commitment. | **Approved:** canonical product-facing direction commitment. |
| Active composition ID / version | `CompositionIntelligencePlayerRuntime` through `ActiveCompositionManager` / `TransitionManager` | Native composition generator and CI evaluators produce candidate compositions | Only the active-composition transition path may activate, replace, or version the active composition. Candidate generation/evaluation is non-mutating. | Publish an accepted transition event carrying match/player, composition ID/version, typed source sequence, and prior identity. Consumers accept only matching lineage and freshness. | **Approved:** sole canonical active-composition commit authority. |
| Pivot candidate | Candidate record owned by the component coordinating pivot evaluation; `StrategicPivotTransitionCoordinator` for Unified Shadow diagnostics, CI candidate state for CI transitions | Composition generator, pivot discovery, feasibility/economic evidence | Candidate producer may create/revise/withdraw its own candidate revision; it cannot mutate active composition or confirmed direction. | Candidate identity/revision and evidence refs travel separately from active composition version. Candidate rejection/expiry is explicit. | **Approved:** separate CI and Unified diagnostic streams; shared schema, isolated state. |
| Confirmed transition | The same active-composition transition authority that owns the target active composition; Unified Shadow machine remains diagnostic unless separately approved | Pivot coordinator proposes; transition validator checks identity, evidence, feasibility, and expected prior version | Only the active-composition owner may commit the transition. The Unified Shadow machine may confirm only its isolated diagnostic state and must not publish to CI/PPO. | Commit is atomic at the contract level: accepted transition links prior and next composition lineage, direction association, reason, source sequences, and resulting version. Rejected transitions leave active state unchanged. | **Approved:** CI transition path is canonical; Unified Shadow is diagnostic-only. |
| Focus | Active composition owner stores the accepted focus snapshot; generator/planner may propose it | Composition generator and trait/evidence analysis | Proposal producers may revise candidate focus; only accepted composition transition may publish active focus. | Preserve ranked/weighted focus separately from core traits; include provenance, identity/version, and sequence. | **Approved:** composition-scoped ranked/weighted priorities. |
| Core traits | Active composition owner stores the accepted core-trait set; generator computes candidate traits | Native composition generator and trait evaluation | Generator owns candidate calculation; active-composition transition authority owns the accepted active set. | Do not derive core traits by copying focus or taking its first element. Keep criterion, source, identity/version, and sequence explicit. | **Approved:** distinct composition membership set; criterion must be explicit in each composition definition. |
| Composition lock | Active-composition owner (`ActiveCompositionManager` / `TransitionManager`) | A dedicated policy/evidence evaluator may recommend lock/unlock; no hardcoded default is authoritative | Until a real authority and transition rule are approved, lock is **unavailable**, not false. Once approved, only its owner may change it through an explicit versioned event. | Planner and evaluators consume the lock only when identity/version and provenance match. Missing/stale lock must not be interpreted as unlocked. | **Approved:** active composition owner; tri-state; policy decision required before changing from unknown. |
| Economic posture | `EconomicController` decision for the current player snapshot | Engine economy facts plus explicitly sourced estimates and progression evidence | EconomicController owns its derived posture decision; it does not mutate active composition, direction, or lock. | Emit posture as a derived, time-bounded decision with evidence refs, horizon, quality, and sequence. Strategic components consume it read-only. | **Approved:** canonical economic posture producer; evidence completeness remains tracked by #282. |
| Progression hypothesis / plan | `EconomicController` (or a separately named progression planner only if a future design explicitly introduces one) | Economy, board strength, level/XP, round, projected income/damage and risk evidence | The designated progression decision producer may revise its hypothesis; consumers cannot promote defaults into a plan. | Keep plan distinct from posture and action recommendation. Missing projected values remain unknown; include horizon and provenance. | **Approved:** same producer, distinct decision contracts; evidence completeness remains tracked by #282. |

### 3.3 Mutation and synchronization protocol

The following protocol is normative for all canonical strategic state changes:

1. **Read one correlated input set.** A decision cycle captures the expected engine match/episode, player, round, and all typed source-sequence refs. Facts from different sequence scopes require an explicit validated correlation; bare integers from different namespaces are not comparable.
2. **Validate before evaluation.** Reject or mark unavailable any input with mismatched match/player, stale round/sequence, invalid quality, or incompatible composition/candidate lineage. Internal snapshot consistency is not a substitute for validation against the receiving runtime's expected identity.
3. **Propose without mutation.** Generators, evaluators, planners, and pivot discovery may emit hypotheses/candidate revisions. These records cannot overwrite canonical active state.
4. **Commit through exactly one owner.** The canonical owner validates the expected prior identity/version and performs the state transition. A failed precondition produces an explicit rejected/stale result and leaves prior canonical state unchanged.
5. **Publish an immutable transition record.** Record actor/owner, operation, prior and resulting identities/versions, candidate identity/revision where relevant, reason, provenance, and all source-sequence refs. Consumers update from this record; no blind field copying or implicit cross-owner mutation.
6. **Make consumers read-only.** Planner, lineup, evaluator, positioning, executor, and diagnostics consume the committed state plus its identity. They may produce their own derived outputs, but cannot write upstream state.
7. **Handle disagreement explicitly.** Parallel/diagnostic owners (especially `UnifiedStrategicStateMachine`) retain their own namespace and are labeled diagnostic. Divergence is recorded as a comparison result; it is not resolved by whichever component writes last.
8. **Reset by episode boundary.** A new Engine episode starts a new identity/sequence lineage and clears active/candidate/recorder state. UUID-shaped unit IDs and local sequence counters are not globally unique without their declared scope.

### 3.4 Authority and state-transition invariants

- A candidate pivot never changes active composition ID/version, active direction, accepted focus/core traits, or lock.
- A rejected, stale, or infeasible pivot leaves all canonical active state unchanged.
- A confirmed pivot is one correlated transition; consumers must not observe a partially updated combination of old direction and new composition (or vice versa).
- Composition version increments only within the same `(engine_match_id, player_id, composition_id)` lineage as defined in the identity contract. A new composition ID or match starts a distinct lineage; candidate revisions use `candidate_id + candidate_revision`.
- Direction, composition ID, anchor identity, focus, core traits, lock, economic posture, and progression plan remain distinct typed fields.
- Lock absence is `unavailable/unknown`, never an inferred unlocked state.
- Derived posture/progression cannot mutate strategic ownership; they are inputs to decisions with explicit horizon and provenance.
- Every recommendation carries the exact source-sequence refs of its context and candidate set. Executor validation must compare those refs against the expected current snapshot.
- Shadow remains read-only: no proposal or transition record executes an in-game action, changes Engine legality, or overrides native masks.

### 3.5 Approved authority decisions

The following decisions are normative for the new architecture's documentary contract:

1. **Direction:** `StrategicPlanner` owns the canonical product-facing direction commitment. It may revise or withdraw only its own commitment; the composition owner references the applicable commitment revision but cannot rewrite it.
2. **Active composition:** `ActiveCompositionManager` / `TransitionManager`, through `CompositionIntelligencePlayerRuntime`, is the sole canonical active-composition commit authority. `UnifiedStrategicStateMachine` remains diagnostic-only and isolated.
3. **Pivot candidates:** CI and Unified Shadow use separate candidate streams with a shared typed envelope schema. Candidate IDs/revisions are namespaced by producer; no candidate stream mutates canonical active state.
4. **Focus and core traits:** focus is a composition-scoped ordered/weighted priority set; core traits are a separate set derived only from explicit composition criteria. Missing criteria yield unavailable evidence, never a guessed set.
5. **Composition lock:** the active-composition owner owns the lock lifecycle. The contract is tri-state (`locked`, `unlocked`, `unknown`); initial/unsupported/missing state is unknown. A separately specified evidence policy must propose changes, and only the active-composition transition path may commit them.
6. **Economy:** `EconomicController` owns both economic posture and progression hypothesis as separate, independently versioned outputs with their own evidence/horizon. Neither can mutate strategic direction, active composition, or lock.
7. **Synchronization:** all cross-component canonical changes use the immutable transition-event envelope defined below. Typed source-sequence references and explicit correlation are mandatory; direct field copying and last-writer-wins synchronization are prohibited.

### 3.6 Canonical transition-event envelope

Every accepted canonical transition must publish an immutable record containing, at minimum:

- `event_id` and idempotency key;
- `owner_component` and transition type;
- engine match/episode identity and player identity;
- round plus every typed source-sequence reference used, including explicit cross-scope correlation metadata where required;
- expected prior state identity/version and resulting state identity/version;
- planner commitment identity/revision when direction is affected;
- candidate identity/revision and candidate producer namespace when applicable;
- accepted/rejected outcome, reason, provenance, evidence quality, and decision horizon where relevant.

The receiver must validate expected prior state and all identity/sequence references before applying an event. Duplicate event IDs are idempotent. Stale, conflicting, incomplete, or out-of-lineage events are rejected with an explicit diagnostic and cannot partially mutate canonical state. A confirmed pivot is one logical transition: direction association and active composition become visible as one correlated committed result. The CI owner publishes canonical events; Unified Shadow publishes only diagnostic events in its own namespace.

This event contract is normative for future implementation. It does not authorize implementation before Gate 8.

## 4. Semantic distinctions

The following identifiers and concepts must remain separate:

- **Direction:** strategic archetype/category or directional hypothesis; not a composition ID.
- **Composition ID:** identity of a concrete active/candidate composition.
- **Anchor identity:** identity of the unit/trait/evidence anchoring a composition hypothesis.
- **Composition version:** revision of an accepted active-composition state, monotonic within one `(engine_match_id, player_id, composition_id)` lineage. It is not a global counter and is not comparable across matches, players, or different composition IDs. A new match starts a new version namespace; a pivot to a different composition ID starts a new lineage. Candidate revisions use candidate identity/revision and must not be presented as active-composition versions.
- **Focus:** ranked/weighted priorities; not automatically identical to core traits.
- **Core traits:** trait set satisfying a defined composition/core criterion.
- **Lock:** explicit authoritative state with source and version; unavailable when no authority exists.
- **Commitment:** planner output/recommendation with provenance; not a directly observed fact.
- **Economic posture:** contextual assessment; not an action mandate or legacy strategy ID.
- **Progression plan:** contextual hypothesis with supporting evidence; default Flexible must not imply that evidence was evaluated.

A pivot candidate must not mutate current direction/composition/lock before transition acceptance. A confirmed pivot must update the relevant owner through an explicit, correlated transition record.

## 5. Provenance and validity contract

Each field/source must carry enough metadata to distinguish:
- origin: observed, derived, inferred, committed, recommended, estimated, or unknown;
- quality: valid, partial, missing, stale, invalid, or unavailable;
- source/component and source version;
- match/episode, player, round, and a typed source-sequence reference;
- composition ID/version when composition-dependent; candidate identity/revision when candidate-dependent;
- reason and horizon for estimates.

Audited provenance gaps:
- The ContextBridge currently classifies planner/generator-produced direction, focus, core traits, and lock as `Observed`, although these values are derived/committed.
- The context builder currently hardcodes `composition_locked = false`; that must not be exposed as an observed unlocked state.
- The current bridge tests do not assert origin/quality/source/reason for every strategic field.
- `CompositionEvaluationContext` leaves match/player identity at defaults in the audited callsite, despite TransitionManager using them to scope hysteresis.
- The planner evidence envelope factory can leave match/player at defaults; the receiving boundary must not rely on implicit mutation or per-instance isolation as a substitute for explicit identity.

No consumer may promote a recommendation, inferred direction, or default value to observed fact.

## 6. Identity, version, sequence, and lifecycle

The base correlation identity for every decision/evidence record is:

`engine_match_id + player_id + round + source_sequence_ref`

The typed `source_sequence_ref` must identify both the sequence namespace/scope and its producing component, for example:

`{ scope: "player_local_ci", source_component: "CompositionIntelligencePlayerRuntime", value: 42 }`

The scope and component names above are illustrative; implementations must use the canonical identifiers declared by the runtime contract. A bare integer named `source_sequence` is insufficient at cross-component boundaries.

Composition-dependent records additionally require:

`composition_id + composition_version`

Candidate-dependent records that do not yet belong to an accepted active composition instead carry `candidate_id + candidate_revision`; they must not fabricate an active `composition_id` or `composition_version`. Records that are not composition-dependent omit those fields and explicitly declare that dependency as absent/not-applicable, rather than using empty IDs or zero versions as sentinels.

Session IDs and Engine episode IDs are different namespaces and must be linked explicitly, not compared as if they were the same value.

Sequence fields with different scopes must remain distinct:
- lobby-wide JSONL ordering sequence;
- player-local Composition Intelligence sequence;
- native strategic snapshot sequence;
- ContextBridge/player sequence;
- Viewer/session correlation sequence.

Each sequence reference must retain its namespace/scope, producing component, and value. Conversion or propagation between scopes requires an explicit mapping/correlation; values from different scopes must never be compared directly.

A recommendation must carry the exact typed source-sequence reference(s) for its context and candidate set. If those inputs originate from multiple sequence domains, preserve each reference and the validated correlation between them. Executor-side validation against a separately supplied current sequence is insufficient if the recommendation itself does not record its origin sequence.

Lifecycle audit:
- `TFTEngine::reset()` recreates per-player Composition Intelligence runtimes, clears candidates/diagnostics/sequences/commitments, and resets the optional Unified Shadow runtimes at episode boundaries.
- This is a valid reset path but requires a regression test running two episodes through the same Engine instance.
- `begin_cycle()` is not a substitute for episode reset.

Any identity/version/sequence mismatch must produce an explicit stale/unavailable result, never a fallback recommendation.

## 7. Integration chain and audited gaps

The intended diagnostic chain is:

`observed snapshot → candidate generation → composition transition → unit priorities → lineup → contextual evaluation → position proposal → Shadow executor resolution → correlated diagnostics/outcomes`

The audit identified the following unresolved integration gaps; they are not implementation authorization:

### 7.1 Candidate generation and evaluator authority (#281)

- `StrategicSharedContext::action_candidates` is read/serialized/compared in the audited `TftEngine.cpp` path, but no population/append was found before the evaluators are called.
- Both evaluators can receive an empty candidate set; current comparison logic can report comparison available even when zero candidates were evaluated.
- `policy_action` is populated with the baseline ActionEvaluator recommendation, not a PPO-selected action.
- Candidate DTO lacks physical parameters such as shop slot, exact bench instance, move origin/destination, horizon, risk, and estimate provenance; executor reconstructs some parameters ambiguously from other snapshots.
- SELL evidence fields are not populated in the audited builder, preventing the current SELL eligibility chain from producing a valid candidate.
- Baseline and contextual HOLD score/confidence semantics differ; their scores are not directly comparable.

Contract decision recorded in #312: candidate identity/physical parameters and baseline-vs-contextual evaluator roles are specified. Remaining work is runtime producer integration and executable proof after Gate 8. A no-candidate state is explicit, never a valid comparison or confident HOLD recommendation.

### 7.2 Economic evidence (#282)

- Projected next-round income, estimated incoming damage, and elimination risk were not populated in the audited integrated context.
- Progression plan remains Flexible in the audited path.
- Some signals are computed but not consumed (including streak strength).
- Plausible numeric defaults (HP 100, gold 0, level 1, risk/damage 0, relative board power 0) can be mistaken for observed values.
- ContextualActionEvaluator does not directly consume EconomicControlDecision, unlike CompositionActionEvaluator's baseline path.

Contract decision recorded in #313: source/horizon/quality, evidence sufficiency, consumer mapping, and marginal cost vs HOLD requirements are specified. Runtime source validation, consumer wiring, and executable proof remain post-Gate-8 work.

### 7.3 Unit-copy and upgrade evidence (#283)

- Current equivalent-copy aggregation can lose progress information for mixed 1★/2★ collections.
- `copies_in_shop`, `unit_cost`, and `gold_available` were not populated in the audited UnitPriority builder/context.
- Board/bench ownership, shop opportunity, and pool availability must remain distinct.

Contract decision recorded in #314: lossless unit instances, tier-specific progress, shop/pool separation, and shared consumer semantics are specified. Runtime migration and executable proof remain post-Gate-8 work.

### 7.4 State ownership and synchronization (#284)

- StrategicPlanner commitments, CI active composition, and Unified Shadow machine hold parallel state.
- Direction, composition ID, anchor identity, focus/core traits and lock have distinct semantics that must not be collapsed.
- Contextual recommendation lacks its originating sequence in the audited contract.
- CompositionEvaluationContext identity fields are not explicitly filled in the audited callsite.
- The bridge provenance and lock issues above remain unresolved.

Ownership and transition decisions are approved in sections 3.1–3.6 and PR #311. Runtime identity validation, sequence binding, stale handling, and reset regression proof remain post-Gate-8 acceptance work.

### 7.5 Lineup to positioning (#289)

- LineupPlanner output is passed to action evaluators, but the audited position snapshot is built from active composition candidate units rather than the resulting `lineup.selected_board/entries/exits/deferred_target_ids`.
- Unit tests exist separately for LineupPlanner and StrategicPositionPlanner; they do not prove the integrated lineup→recommendation→position→executor chain.
- Position proposals must be bound to the same lineup identity/version/sequence and must be recomputed incrementally after state changes.

Required evidence: integrated replay with capacity, bridge units, entries/exits, deferred targets, stale sequence and legal masks.

### 7.6 Outcome correlation and replay (#289)

- `CompositionDiagnosticRecorder::capture` accepts an optional outcome observation, but the audited runtime callsite does not pass one; runtime outcome fields remain null.
- Replay must correlate recommendation and later observed outcome by match/player/sequence/composition version, with explicit windows and missing outcomes.
- Results are correlational diagnostics, not causal claims or Shadow reward targets.
- Feature flag `TFT_COMPOSITION_INTELLIGENCE_SHADOW` must be recorded and tested in both enabled and disabled paths.

## 8. Replay and acceptance matrix

After Gate 8, executable acceptance evidence must cover:

1. One approved owner per strategic concept and explicit non-authoritative/diagnostic components.
2. Candidate pivot does not mutate active state; rejected/confirmed transitions have correct version changes.
3. Direction, composition ID, anchor, focus, core traits, lock, posture and progression remain semantically distinct.
4. Provenance tests reject commitment/inference/recommendation mislabeled as observed.
5. External match/player/round/sequence identity validation rejects internally consistent stale snapshots.
6. Two sequential matches in one Engine instance do not share active state, recorder, history, sequence or commitments.
7. Empty, partial, invalid, stale and valid candidate sets produce distinct states.
8. Baseline recommendation, PPO action (if genuinely available), and contextual recommendation have separate fields and provenance.
9. Candidate physical parameters resolve against the same snapshot and current masks; ambiguous SELL/BUY/MOVE parameters are rejected.
10. Economic evidence source/horizon/quality and cost-vs-HOLD decomposition are auditable without double counting.
11. Per-star-tier copies, shop offers, affordability and pool uncertainty are consistent across all consumers.
12. Lineup selected board and deferred targets constrain position proposals in the same sequence/version.
13. Recommendation sequence mismatch is rejected even within the same round and composition version; sequence comparisons require matching scope/component or an explicit validated cross-scope correlation.
14. Pre-composition and candidate-only records are valid without an active composition ID/version; composition-dependent records require both. Candidate revisions cannot masquerade as active-composition versions.
15. Composition versions are monotonic only within the declared match/player/composition lineage; reset and pivot tests prove namespace changes and prevent cross-lineage comparisons.
16. Outcome correlation handles delayed outcomes, pivots, missing data and match end without causal/reward claims.
17. Multi-round deterministic replay covers early game, stable composition, economy pressure, upgrade, pivot, incomplete evidence and match reset.
18. All behavior remains Shadow/read-only; Engine masks/rules remain final legality authority.

## 9. Gate status and implementation boundary

**Audit status:** Audit E (#300) is closed as a static audit deliverable; the related implementation issues #281–#284 and replay issue #289 remain open.

**Documentary status:** the ownership decisions in sections 3.1–3.6 are approved and normative. The remaining issues #281, #282, #283, #284 and #289 track contract elaboration and executable acceptance evidence; they are not permission to begin runtime work.

**Gate 5 documentary status:** the authority decisions and candidate, economic, unit, and integrated replay contracts are now merged. The remaining Gate 5 work is the post-merge consistency review and any resulting documentary clarification; the executable acceptance matrix below is deferred until after Gate 8. Runtime implementation/tests remain blocked until Gate 8 and explicit user approval.

No runtime files, PPO, observations, rewards, checkpoints, masks, Engine rules, Viewer, or game actions are changed by this document.
