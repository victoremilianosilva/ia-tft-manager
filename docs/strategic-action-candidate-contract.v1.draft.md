# Strategic Action Candidate Contract v1

**Status:** approved documentary specification; runtime implementation and executable acceptance blocked until Gate 8  
**Contract ID:** `tft.strategic-action-candidates.v1`  
**Target:** `new-arquiteture`  
**Related:** #281, #282, #283, #284, #289; Action/legality #294; Observation #293; PPO/checkpoint #288

> Documentation only. This contract does not implement candidate generation, execute actions, or change PPO, observations, rewards, checkpoints, masks, Engine rules, or Viewer behavior.

## 1. Purpose and normative principles

The audited TftEngine.cpp path invokes existing baseline and contextual evaluators, but does not populate StrategicSharedContext::action_candidates. Both therefore receive an empty source set in this path. The current comparison_available flag is based on evaluator staleness, and same_initial_candidate_set can be true for three empty lists; these booleans can therefore report availability/equality without any comparable candidate. The missing capability is a trustworthy source of concrete, snapshot-bound alternatives—not another evaluator or legality system.

1. A candidate describes an alternative; it is never a command or game action.
2. Native Engine rules and masks remain the sole final legality authority. Candidate prechecks cannot redefine legality.
3. Exact physical parameters are mandatory; executor-side guessing from incidental ordering is prohibited.
4. Candidate facts, parameters, costs, and benefits must share match/player/round and typed source-sequence references, or explicit validated cross-source correlation.
5. Unknown is not zero. Missing evidence stays missing/partial/unavailable.
6. Direct spend, lost interest, future income, and opportunity cost must be decomposed against one baseline and combined once.
7. Baseline and contextual scores have different semantics; do not compare them as calibrated values without separate evidence.
8. Baseline evaluator output is never labeled as PPO action.
9. Shadow evaluation and executor resolution are read-only.

## 2. Candidate envelope

Every candidate carries these logical fields (C++ naming may follow existing style):

| Field | Contract |
|---|---|
| candidate_id | Stable identity within producer and source snapshot |
| candidate_revision | Revision of this candidate; never an active composition version |
| producer_component | Component that generated it |
| candidate_kind | BUY, BUY_XP, REROLL, HOLD/PASS, SELL, MOVE/DEPLOY |
| match/episode, player, round | External game identity |
| source_sequence_refs | Typed scope + producing component + value |
| candidate_set_id | Immutable identity of the complete correlated candidate set |
| physical_parameters | Exact parameters needed for resolution |
| legality_status | Candidate precheck only; native masks remain final |
| evidence_status | valid, partial, missing, stale, invalid, unavailable |
| cost_breakdown | Direct cost, interest delta, opportunity cost, uncertainty |
| benefit_breakdown | Board/upgrade/economy/survival effects, each with source and horizon |
| provenance | Observed/derived/estimated origin, source, quality, reason |
| composition_ref | Composition ID/version only when composition-dependent |

Missing required physical parameters make a candidate invalid for resolution. A diagnostic rejection may be retained only with the missing field and reason. Empty IDs, zero versions, and unscoped sequence integers are not sentinels. Candidate revisions are namespaced by producer and candidate ID. A changed source snapshot produces a new immutable candidate set.

## 3. Physical parameters and evidence

| Family | Minimum physical parameters | Required evidence |
|---|---|---|
| BUY | Exact shop slot and champion identity | Slot contents, cost, gold, same sequence |
| BUY_XP | Exact native XP purchase parameters | Level/XP, XP-to-next, gold, cost, horizon |
| REROLL | Exact native reroll parameters and shop identity | Reroll cost, gold, shop state; refreshed shop is a later sequence |
| HOLD/PASS | Explicit no-op identity bound to candidate set | Snapshot identity, baseline and opportunity horizon |
| SELL | Exact owned unit instance and board/bench location | Ownership, star tier, item/trait/upgrade/lineup protections, sell value |
| MOVE/DEPLOY | Exact unit instance, origin, destination, position-plan identity | Ownership, board/bench, destination legality, native masks |

- BUY preserves candidate-to-shop-slot identity; do not search for the first matching champion during resolution.
- SELL identifies one exact instance. Ambiguous copies are rejected, never selected by iteration order. Eligibility must preserve pairs, star progress, items, trait completion, lineup role, and pivot requirements; coordinate with #283 and #291.
- MOVE/DEPLOY references the exact lineup/position proposal and sequence; no reconstruction from unrelated/newer snapshots.
- BUY_XP/REROLL carry exact native parameters, not estimates.
- HOLD/PASS is a first-class reference alternative, not a fabricated zero-cost action.

## 4. Candidate generation and set status

A future builder must read one correlated snapshot, validate identity externally, derive exact physical parameters, attach field-level provenance, and publish an immutable candidate set. Set status is explicit:
- `ready`: at least one valid candidate;
- `no_candidates`: generation completed, no valid alternative;
- `partial`: some alternatives unavailable due to missing evidence;
- `stale`: source identity/sequence no longer matches runtime expectation;
- `invalid`: envelope or candidate contract failed validation.

An empty vector alone does not explain why no candidates exist. Zero candidates is never a valid comparison or a confident contextual HOLD recommendation.

## 5. HOLD/PASS economic baseline

HOLD/PASS may preserve gold/interest, shop options, reroll flexibility, streak/survival position, board stability, and future timing options. It may also incur opportunity cost by delaying a time-limited offer, board-strength improvement, upgrade timing, or response to survival pressure.

Every alternative is compared against the same state baseline and horizon. Decompose direct spend/proceeds, resulting interest delta, future income, board/upgrade/survival benefit, residual opportunity cost, and uncertainty. Do not count the same effect in multiple terms. Missing evidence remains unknown/partial, not zero. Evaluator confidence is a non-probabilistic diagnostic, never a success probability.

## 6. Evaluator roles and Shadow recommendation authority

The audited paths are distinct:
- **Baseline:** `CompositionActionEvaluator` filters/enriches candidates and delegates to `strategy::ActionEvaluator`, receiving `EconomicControlDecision` and baseline recommendation input.
- **Contextual:** `ContextualActionEvaluator` independently scores contextual evidence and is currently forwarded to `StrategicActionExecutor` for Shadow resolution.

For the target architecture's read-only Shadow pipeline, `ContextualActionEvaluator` is the canonical producer of the contextual proposal that the Shadow executor is intended to validate. `CompositionActionEvaluator`/`ActionEvaluator` remains an independent baseline comparator. Baseline output never silently replaces contextual output. Disagreement is preserved with independent score semantics and provenance. If no valid contextual candidate exists, result is `unavailable/no_candidates`, not an invented HOLD.

**Current integration status:** TftEngine invokes StrategicActionExecutor::resolve(), and the current diagnostic reports executor_connected=true, execution_enabled=false, and native_action_applied=false. Connectivity proves the read-only resolver call path is wired; it does not prove per-request acceptance or game execution. The current source candidate set is empty, so no valid candidate comparison or accepted action is established. Any future end-to-end claim still requires a non-empty correlated candidate set, exact source sequences, executor input/output records, and integrated replay proof in #289.

This does not imply legality: native masks and executor validation remain final. The contextual evaluator's lack of direct `EconomicControlDecision` consumption is not silently changed here. #282 must decide which economic signals should affect contextual scoring. Until then, posture may be recorded separately but must not be described as affecting a score that does not consume it.

## 7. PPO separation

Keep separately typed: actual PPO-selected action (if available for same match/player/round/sequence), baseline recommendation, contextual proposal, and executor resolution. The parameter currently named `policy_action` must not receive a baseline recommendation and then be represented as PPO output. If actual PPO action is unavailable, PPO comparison is unavailable; never infer it from either evaluator.

## 8. Comparison and executor contract

Comparison is available only when there is at least one shared valid candidate identity, the candidate set is non-empty and ready (or has an explicitly defined comparable subset), both evaluators received the same candidate-set identity and correlated snapshot, and both outputs are valid under their own semantics. Two empty lists are never comparable; `same_initial_candidate_set` cannot make them comparable. Partial sets compare only an explicit shared valid subset with exclusions explained.

The current TftEngine call path invokes the read-only resolver with the contextual recommendation, source StrategicSharedContext and current native snapshot. In the audited path, however, the source candidate set is empty, so no valid selected candidate can be resolved. For a future non-empty candidate set, the resolver must validate match/player/round/sequences against the independently supplied current Engine snapshot; validate candidate revision and exact physical parameters; resolve against current native masks without modifying them; and explicitly reject stale, ambiguous, malformed, or illegal candidates. It never issues input or mutates Engine state. A relevant sequence change within the same round and composition version can stale a candidate.

The resolver call path is connected, but per-request resolution remains unavailable/rejected when there is no valid selected candidate. Evaluator diagnostics alone do not establish candidate validity, resolver acceptance, or execution.

## 9. Acceptance matrix — after Gate 8

| Scenario | Required result |
|---|---|
| BUY with duplicate offers | Exact shop slot preserved |
| BUY unaffordable | Rejected with explicit cost evidence |
| BUY_XP/REROLL | Exact native parameters and costs bound to snapshot |
| HOLD vs action | Same baseline/horizon; no double counting |
| SELL with multiple copies | Exact instance required; ambiguity rejected |
| SELL with pair/item/trait/lineup protection | Protected unit not eligible |
| MOVE/DEPLOY | Origin/destination bound to same lineup/position sequence |
| Empty candidate set | `no_candidates`; comparison unavailable |
| Partial evidence | Partial/unavailable; no fabricated zero |
| Stale same-round snapshot | Rejected even if composition version is unchanged |
| Baseline/contextual disagreement | Both results preserved independently |
| PPO unavailable | No PPO action inferred |
| Native mask rejects candidate | Explicit rejection; masks/rules unchanged |
| No eligible alternatives | No false confident HOLD |

Integrated replay also covers shop refresh, gold/board/bench changes, upgrade progress, pivot, and match reset. Candidate set, evaluator outputs, recommendation, and executor resolution must share source identity and typed sequence references.

## 10. Gate status

This specification closes only the documentary candidate-contract design when reviewed and merged. #281 remains open for a real producer populating `action_candidates` and executable end-to-end proof after Gate 8 and explicit implementation authorization.

No runtime code/tests, PPO, observations, rewards, checkpoints, masks, Engine rules, Viewer behavior, or game actions are changed.


## 11. Current integration evidence boundary (2026-11-14)

The current source establishes the resolver call path: TftEngine invokes StrategicActionExecutor::resolve(), and the diagnostic reports executor_connected=true. The resolver is read-only; execution_enabled=false and native_action_applied=false. Per-request acceptance remains separate and is not implied by connectivity. The current action-candidate source vector is empty, so no valid candidate comparison or accepted action is established.

**Prior problem:** the earlier wording understated the existing read-only resolver call path and did not clearly separate resolver connectivity from per-request acceptance.

**Technical rationale:** ownership defines who should produce/consume a contract; integration status requires evidence of an actual connected call path and correlated records.

**Ownership:** ContextualActionEvaluator owns contextual proposals; StrategicActionExecutor owns read-only validation/resolution when connected; diagnostics report connection/availability and must not synthesize resolution.

**Invariants:** connected is not accepted; unavailable is not HOLD; candidate proposal is not execution; no live input or Engine mutation; native masks remain final legality authority.

**Cross-component impact:** #281/#289/#294 and the dual-evaluator, replay, and ownership contracts.

**Validation:** reconciled against the current TftEngine callsite, StrategicActionExecutor read-only contract, and dual-action-evaluator-shadow.md (executor_connected=true; execution remains disabled). Post-Gate-8 acceptance requires an integrated call-path test and replay records proving proposal → executor input → resolution/rejection with identical candidate-set and typed sequence references.


## 12. Current producer and comparison integration correction (2026-11-15)

A source-backed recheck of cpp/src/lobby/TftEngine.cpp and StrategicActionExecutor.hpp establishes that the resolver call path is currently wired and invoked. The diagnostic values are:

- executor_connected=true: the read-only resolver is called;
- execution_enabled=false: no action execution is enabled;
- native_action_applied=false: the resolver does not mutate/apply a native action.

This supersedes the earlier executor_connected=false wording. It does not supersede the requirement for per-request acceptance evidence.

A second mismatch remains: the current comparison_available diagnostic is derived from evaluator staleness, while same_initial_candidate_set can be true when all candidate counts are zero. The audited StrategicSharedContext::action_candidates vector is not populated. Therefore, the current booleans can describe an empty-set comparison as available/equal even though this contract requires at least one shared valid candidate identity. Until a source producer and runtime correction are proven, consumers must treat an empty source set as no_candidates and comparison as unavailable. This is a documentation finding only; no runtime behavior is changed.

**Prior problem:** the earlier documentation understated resolver connectivity and did not clearly separate empty-set diagnostics from valid comparison.

**Technical rationale:** a wired resolver, a valid candidate set, a selected proposal, per-request acceptance, and applied execution are separate states.

**Ownership:** ContextualActionEvaluator remains the contextual proposal producer; StrategicActionExecutor remains the read-only resolver; native masks/rules remain final legality authority.

**Invariants:** resolver connectivity is not acceptance; acceptance is not execution; empty candidate sets are not comparable; no action is applied; PPO action, baseline recommendation, contextual proposal and resolver output remain distinct.

**Cross-component impact:** TftEngine, StrategicSharedContext, both action evaluators, StrategicActionExecutor, action candidate contract, producer-binding audit, replay and #281/#289/#294.

**Validation:** verified the TftEngine callsite, diagnostic booleans, executor read-only contract and candidate vector population path. Post-Gate-8 acceptance must test empty candidate sets, non-empty shared sets, stale identity, native mask rejection and explicit non-execution.
