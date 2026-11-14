# Strategic Ownership and Integration Contract v1 — Draft

**Status:** documentary specification; authority decisions and runtime acceptance remain pending  
**Contract ID:** `tft.strategic-ownership.v1`  
**Target architecture:** `new-arquiteture`  
**Related issues:** #281, #282, #283, #284, #289, #300  
**Coordinates with:** Observation #293, Action #294, PPO/checkpoint #288

> This document consolidates the static integration audit. It does not select an unapproved runtime owner, change strategic behavior, generate/execute actions, or modify PPO, rewards, observations, checkpoints, masks, Engine rules, or Viewer behavior.

## 1. Purpose

The new architecture contains multiple strategic state owners and several partially connected planning/evaluation components. Their existence and unit tests do not prove that the integrated runtime has one unambiguous authority or that each recommendation is based on the same fresh snapshot.

This contract establishes:
- distinct meanings for observed facts, derived evidence, commitments, hypotheses, active composition, and recommendations;
- the current ownership map and boundaries;
- integration invariants for identity, version, sequence, provenance, and stale data;
- explicit gaps that must be resolved before Gate 5 can be approved;
- replay and acceptance evidence required after Gate 8.

## 2. Normative principles

1. **Observed game state is authoritative for facts.** Board, bench, shop, items, economy, HP, level, XP, round, and masks must originate from the matching Engine snapshot or a validated source.
2. **Inference is not observation.** Direction discovery, focus, core traits, priorities, economic posture, lineup, and risk estimates must retain derived/estimated/committed provenance.
3. **A hypothesis is not an active composition.** Pivot candidates and planner recommendations cannot replace the current active composition before an explicit transition is accepted by its owner.
4. **One concept, one declared authority.** Parallel components may exist for comparison, but their state must be labeled experimental/diagnostic and must not silently overwrite the canonical state.
5. **Identity is end-to-end.** Every decision/evidence chain must preserve match/episode, player, round, sequence, composition ID, and composition version as applicable.
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
| StrategicPlanner | Produces strategic commitments/direction and reasons from StrategicEvidenceContext | Must retain commitment/inference provenance; does not automatically own CI active composition |
| CompositionIntelligencePlayerRuntime + ActiveCompositionManager / TransitionManager | Per-player CI runtime owns active composition, transition hysteresis, recorder, history, player sequence; publishes approved transitions | This is the active composition used by the CI planning chain; final architecture-wide ownership of direction vs composition is still unresolved |
| EconomicController | Produces contextual economic posture/decision and diagnostics | Posture is not a fixed strategy ID or executable action |
| UnitPriorityPlanner | Resolves unit priorities against active composition identity/version | Depends on canonical copy/progress evidence and fresh source snapshots |
| LineupPlanner | Produces a deployable lineup from active composition and priorities | Its output is not currently the direct source for the position snapshot in the audited callsite |
| CompositionActionEvaluator | Baseline evaluator path; filters/enriches candidates and delegates to ActionEvaluator with economic decision/policy argument | Its score/baseline semantics differ from ContextualActionEvaluator |
| ContextualActionEvaluator | Independent contextual evaluation using board, priority, lineup, upgrade and economic evidence | Does not consume EconomicControlDecision directly; its score is not interchangeable with baseline score |
| StrategicPositionPlanner | Produces a constrained physical position proposal using owned units, legal masks and snapshot evidence | Must be tied to the exact deployable lineup and same sequence |
| StrategicActionExecutor | Resolves Shadow proposal against native state/masks and snapshot sequence | Does not execute a real game action |
| UnifiedStrategicStateMachine / UnifiedStrategicShadowRuntime | Separate Shadow state machine used for comparison/audit and pivot transitions | Maintains parallel state; must not silently publish back to CI/PPO or be treated as canonical without explicit decision |
| Viewer/JSONL diagnostics | Persists provenance, correlation, sequences and diagnostic results | Telemetry is not a state authority |

### 3.1 Authority decision still required

The audit establishes that at least three strategic states coexist:
- `strategic_planner_commitments[i]`;
- `composition_intelligence_players[i].active`;
- `strategic_shadow_runtimes[i].machine().active_composition()`.

They are not one shared state. Current runtime re-anchors the Unified Shadow machine when the external CI identity/version changes, then keeps its own state for isolated comparison. This is acceptable only while it is explicitly diagnostic.

**Gate 5 cannot be marked complete until the intended production authority is explicitly approved for each distinct concept**, at minimum:
- strategic direction / commitment;
- active composition identity and version;
- pivot candidate;
- confirmed transition;
- focus and core traits;
- composition lock;
- economic posture / progression hypothesis.

Do not solve this by copying all fields into one class or by allowing one machine to overwrite another. Define event/transition ownership and synchronization rules per concept.

## 4. Semantic distinctions

The following identifiers and concepts must remain separate:

- **Direction:** strategic archetype/category or directional hypothesis; not a composition ID.
- **Composition ID:** identity of a concrete active/candidate composition.
- **Anchor identity:** identity of the unit/trait/evidence anchoring a composition hypothesis.
- **Composition version:** monotonic version of an accepted composition state.
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
- match/episode, player, round, sequence;
- composition ID/version when composition-dependent;
- reason and horizon for estimates.

Audited provenance gaps:
- The ContextBridge currently classifies planner/generator-produced direction, focus, core traits, and lock as `Observed`, although these values are derived/committed.
- The context builder currently hardcodes `composition_locked = false`; that must not be exposed as an observed unlocked state.
- The current bridge tests do not assert origin/quality/source/reason for every strategic field.
- `CompositionEvaluationContext` leaves match/player identity at defaults in the audited callsite, despite TransitionManager using them to scope hysteresis.
- The planner evidence envelope factory can leave match/player at defaults; the receiving boundary must not rely on implicit mutation or per-instance isolation as a substitute for explicit identity.

No consumer may promote a recommendation, inferred direction, or default value to observed fact.

## 6. Identity, version, sequence, and lifecycle

The minimum correlation identity for a decision chain is:

`engine_match_id + player_id + round + source_sequence + composition_id + composition_version`

Session IDs and Engine episode IDs are different namespaces and must be linked explicitly, not compared as if they were the same value.

Sequence fields with different scopes must remain distinct:
- lobby-wide JSONL ordering sequence;
- player-local Composition Intelligence sequence;
- native strategic snapshot sequence;
- ContextBridge/player sequence;
- Viewer/session correlation sequence.

A recommendation must carry the exact source sequence of its context and candidate set. Executor-side validation against a separately supplied current sequence is insufficient if the recommendation itself does not record its origin sequence.

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

Required decision: define candidate identity/physical parameters and the relationship between baseline evaluator and contextual evaluator. A no-candidate state must be explicit, not a valid comparison or confident HOLD recommendation.

### 7.2 Economic evidence (#282)

- Projected next-round income, estimated incoming damage, and elimination risk were not populated in the audited integrated context.
- Progression plan remains Flexible in the audited path.
- Some signals are computed but not consumed (including streak strength).
- Plausible numeric defaults (HP 100, gold 0, level 1, risk/damage 0, relative board power 0) can be mistaken for observed values.
- ContextualActionEvaluator does not directly consume EconomicControlDecision, unlike CompositionActionEvaluator's baseline path.

Required decision: source/horizon/quality for each economic estimate; evidence sufficiency rules; which economic signals reach each evaluator and why; marginal cost vs HOLD without double counting.

### 7.3 Unit-copy and upgrade evidence (#283)

- Current equivalent-copy aggregation can lose progress information for mixed 1★/2★ collections.
- `copies_in_shop`, `unit_cost`, and `gold_available` were not populated in the audited UnitPriority builder/context.
- Board/bench ownership, shop opportunity, and pool availability must remain distinct.

Required decision: canonical per-star-tier progress representation shared by generator, priority, pivot feasibility, lineup and evaluators, with tests for mixed stars, affordable/unaffordable offers and unknown pool.

### 7.4 State ownership and synchronization (#284)

- StrategicPlanner commitments, CI active composition, and Unified Shadow machine hold parallel state.
- Direction, composition ID, anchor identity, focus/core traits and lock have distinct semantics that must not be collapsed.
- Contextual recommendation lacks its originating sequence in the audited contract.
- CompositionEvaluationContext identity fields are not explicitly filled in the audited callsite.
- The bridge provenance and lock issues above remain unresolved.

Required decision: approved owner per concept, transition protocol, external identity validation, sequence binding, stale handling and reset proof.

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

Before Gate 5 can be accepted, executable evidence after Gate 8 must cover:

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
13. Recommendation sequence mismatch is rejected even within the same round and composition version.
14. Outcome correlation handles delayed outcomes, pivots, missing data and match end without causal/reward claims.
15. Multi-round deterministic replay covers early game, stable composition, economy pressure, upgrade, pivot, incomplete evidence and match reset.
16. All behavior remains Shadow/read-only; Engine masks/rules remain final legality authority.

## 9. Gate status and implementation boundary

**Audit status:** Audit E (#300) is closed as a static audit deliverable; the related implementation issues #281–#284 and replay issue #289 remain open.

**Documentary status:** this draft consolidates the known ownership map, integration gaps, semantic boundaries and required evidence. It deliberately does not choose between parallel state owners where the product authority decision has not yet been approved.

**Gate 5 is not complete.** Approval requires an explicit owner decision per concept and closure of the remaining documentary ambiguities. Runtime implementation/tests remain blocked until Gate 8 and explicit user approval.

No runtime files, PPO, observations, rewards, checkpoints, masks, Engine rules, Viewer, or game actions are changed by this document.
