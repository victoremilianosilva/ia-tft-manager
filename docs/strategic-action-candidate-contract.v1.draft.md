# Strategic Action Candidate Contract v1 — Draft

**Status:** documentary specification; runtime implementation and executable acceptance blocked until Gate 8  
**Contract ID:** `tft.strategic-action-candidates.v1`  
**Target:** `new-arquiteture`  
**Related:** #281, #282, #283, #284, #289; Action/legality #294; Observation #293; PPO/checkpoint #288

> Documentation only. This contract does not implement candidate generation, execute actions, or change PPO, observations, rewards, checkpoints, masks, Engine rules, or Viewer behavior.

## 1. Purpose and normative principles

The audited `TftEngine.cpp` path invokes existing baseline and contextual evaluators, but does not populate `StrategicSharedContext::action_candidates`. Both can therefore receive empty sets, while comparison logic can report availability for two empty lists. The missing capability is a trustworthy source of concrete, snapshot-bound alternatives—not another evaluator or legality system.

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

For the new architecture's read-only Shadow pipeline, `ContextualActionEvaluator` is the canonical producer of the contextual proposal forwarded to the Shadow executor. `CompositionActionEvaluator`/`ActionEvaluator` remains an independent baseline comparator. Baseline output never silently replaces contextual output. Disagreement is preserved with independent score semantics and provenance. If no valid contextual candidate exists, result is `unavailable/no_candidates`, not an invented HOLD.

This does not imply legality: native masks and executor validation remain final. The contextual evaluator's lack of direct `EconomicControlDecision` consumption is not silently changed here. #282 must decide which economic signals should affect contextual scoring. Until then, posture may be recorded separately but must not be described as affecting a score that does not consume it.

## 7. PPO separation

Keep separately typed: actual PPO-selected action (if available for same match/player/round/sequence), baseline recommendation, contextual proposal, and executor resolution. The parameter currently named `policy_action` must not receive a baseline recommendation and then be represented as PPO output. If actual PPO action is unavailable, PPO comparison is unavailable; never infer it from either evaluator.

## 8. Comparison and executor contract

Comparison is available only when there is at least one shared valid candidate identity, the candidate set is non-empty and ready (or has an explicitly defined comparable subset), both evaluators received the same candidate-set identity and correlated snapshot, and both outputs are valid under their own semantics. Two empty lists are never comparable; `same_initial_candidate_set` cannot make them comparable. Partial sets compare only an explicit shared valid subset with exclusions explained.

The executor receives the contextual proposal, originating candidate set, and exact sequence refs. It validates match/player/round/sequences against the independently supplied current Engine snapshot; validates candidate revision and physical parameters; resolves against current native masks without modifying them; and explicitly rejects stale, ambiguous, malformed, or illegal candidates. It never issues input or mutates Engine state. A relevant sequence change within the same round and composition version can stale a candidate.

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
