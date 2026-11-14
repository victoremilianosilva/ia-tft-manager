# Strategic Shadow Integrated Replay Contract v1 — Draft

**Status:** documentary specification; executable replay and runtime integration blocked until Gate 8  
**Contract ID:** `tft.strategic-shadow-replay.v1`  
**Target:** `new-arquiteture`  
**Related:** #289, #281, #282, #283, #284, #294; Observation #293; Reward #287

> This document defines deterministic integration evidence. It does not implement runtime changes, execute game actions, or modify PPO, observations, rewards, checkpoints, masks, Engine rules, or Viewer behavior.

## 1. Purpose

Unit tests exist for several components, but they do not prove the end-to-end multi-round chain. The replay contract must exercise observed evidence through candidate generation, canonical composition transitions, unit priorities, lineup, economic evidence, contextual evaluation, positioning, Shadow executor resolution, diagnostics, and later outcomes.

Replays are diagnostic and correlational. Shadow recommendations are not executed, are not PPO targets, and do not become reward labels.

## 2. Replay identity and determinism

Every replay fixture and emitted record must preserve:
- fixture/replay ID and deterministic seed;
- Engine match/episode ID and player ID;
- round and timestamp/order within the replay;
- typed sequence references for each source domain;
- session ID separately from Engine episode ID, with explicit correlation;
- composition ID/version only for composition-dependent records;
- candidate ID/revision and producer namespace for candidate-only records;
- feature-flag configuration and relevant runtime/config/catalog versions.

Sequence namespaces are not interchangeable. At minimum preserve:
- native strategic snapshot sequence;
- player-local Composition Intelligence sequence;
- global JSONL append sequence;
- ContextBridge/player sequence;
- Viewer session correlation sequence.

Cross-scope sequence values are never directly compared. A validated correlation record is required. A complete Engine↔session correlation requires valid Engine episode identity in addition to session/player/round/sequence. Error or partial snapshots must not be labeled fully correlated merely because some integer fields exist.

Replay ordering must be deterministic. Given the same fixture, seed, config, catalog, and code version, the same state transitions and diagnostic outputs should be reproducible.

## 3. Required replay chain

The replay must exercise this chain where the relevant feature is enabled:

`observed snapshot → evidence/provenance validation → candidate generation → candidate set → canonical direction commitment → active composition transition → unit evidence/priorities → lineup → economic posture/progression → baseline and contextual evaluation → position proposal → Shadow executor resolution → diagnostics → later observed outcome`

The chain must preserve exact input/output identities and sequence references at every boundary. Missing capabilities are recorded as unavailable; a replay must not silently substitute legacy state or fabricated defaults.

## 4. Scenario coverage

The deterministic suite must include:
1. Early-game discovery with incomplete evidence.
2. Composition stabilization over several rounds.
3. Shop opportunity and purchase alternatives.
4. XP and reroll alternatives with economic tradeoffs.
5. Pair/upgrade progress across board and bench.
6. Item/trait/lineup-protected units that must not become SELL candidates.
7. Economic pressure and survival urgency with supported and missing estimates.
8. Candidate pivot, rejected pivot, and confirmed pivot.
9. Multiple concrete compositions sharing one strategic direction.
10. Composition change without direction change.
11. Lineup entry/exit, bridge unit, deferred target, capacity, and positioning proposal.
12. Shop/gold/board change within the same round and same composition version.
13. Stale snapshot, incomplete shop, unknown pool, and contradictory evidence.
14. Match/episode reset and two sequential matches through the same Engine process.
15. No-candidate and no-eligible-candidate states.
16. Native mask rejection of an otherwise generated candidate.

## 5. Candidate/evaluator comparison

A replay distinguishes:
- `no_candidates`;
- `no_eligible_candidates`;
- `comparison_unavailable`;
- `comparison_available`.

A comparison is valid only when at least one common valid candidate was actually evaluated from the same candidate-set identity and correlated snapshot. Two empty lists are never comparable. HOLD/PASS emitted as a default because no candidates exist is not a strategic recommendation.

The replay records separate fields for:
- actual PPO-selected action, if available for the exact same match/player/round/sequence;
- baseline ActionEvaluator recommendation;
- contextual ContextualActionEvaluator proposal;
- Shadow executor resolution.

If no actual PPO action is available, PPO comparison is unavailable. A baseline recommendation must never be substituted for PPO output. Divergence from PPO is diagnostic and is not a failure by itself.

## 6. Temporal economics and outcomes

Replays must follow costs and benefits across declared horizons:
- purchases that become valuable only after a pair/upgrade or board change;
- XP/reroll/purchase spending and later gold, interest, level, board strength, survival, and option changes;
- action reversal and buy/sell cycles;
- HOLD/PASS versus acting under the same baseline;
- delayed or missing outcomes.

Do not count the same benefit/cost in consecutive snapshots. Every estimate carries source, horizon, quality, and uncertainty. Outcomes correlate by Engine match, player, source sequence, and composition lineage. A pivot between recommendation and outcome must be represented explicitly.

Placement, HP delta, and board-score delta are observed outcomes only when their source and time window are available. Before match end or without a compatible prior snapshot, outcome remains unavailable. Correlation does not prove causality and does not create a Shadow reward target.

## 7. Lineup and positioning integration

The replay must prove the complete chain:
`unit priorities → LineupPlan → contextual candidate → position proposal → executor resolution`.

It must verify that:
- the recommended unit belongs to `LineupPlan.selected_board`;
- capacity and deferred targets are respected;
- entries/exits and bridge units are represented correctly;
- exact unit instance, origin, destination, lineup identity/version, and sequence are bound together;
- position proposals are recomputed incrementally after state changes;
- native masks remain final legality authority.

Existing isolated tests for LineupPlanner and StrategicPositionPlanner do not satisfy this integrated proof. A proposal derived directly from active composition units without validating the resulting LineupPlan is insufficient.

## 8. Feature flags and configuration

Every replay records `TFT_COMPOSITION_INTELLIGENCE_SHADOW` and all relevant feature/config versions.

- Flag disabled: verify that the opt-in CI/Shadow chain does not run or emit misleading artifacts; distinguish this from a component failure.
- Flag enabled: exercise the complete configured chain and prove candidate, evaluator, position, and executor records are correlated.
- StrategicPlanner/EconomicController paths that run outside the CI feature-flag block must be identified separately in the report.
- Weight/threshold sensitivity must be recorded for documented deterministic parameters. Small evidence changes, missing inputs, and catalog/patch changes must be tested.
- Heuristic confidence is not probability. Do not tune weights to imitate PPO decisions.

## 9. Lifecycle and provenance assertions

The replay must assert:
- candidate pivot never mutates active state;
- rejected/stale/infeasible transition leaves canonical state unchanged;
- confirmed transition is one correlated atomic logical event;
- Planner direction, CI active composition, and Unified diagnostic state remain separate authorities;
- Unified divergence is diagnostic, never last-writer-wins;
- focus, core traits, lock, economic posture, and progression retain distinct semantics;
- field-level provenance never labels inference/commitment/default as observed;
- lock unknown is not false;
- composition versions are scoped to match/player/composition lineage;
- two episodes in one Engine instance do not share state, recorder, history, or sequences.

## 10. Feature and artifact outputs

Each replay run must emit:
- machine-readable per-cycle records;
- a summary with fixture/seed/config/code/catalog versions;
- candidate-set status and counts by action family;
- evaluator outputs and comparison availability/reasons;
- transition events and prior/resulting identities;
- provenance/quality and stale/rejection reasons;
- lineup/position/executor resolution chain;
- outcome correlation status and observation window;
- feature flags and parameter sensitivity;
- explicit assertion failures and missing evidence.

Artifacts must be deterministic and suitable for CI comparison. Do not include credentials or private client fields. Do not treat telemetry as an authority source.

## 11. Acceptance matrix — after Gate 8

| Area | Required proof |
|---|---|
| Multi-round chain | Same identities and typed sequences across every stage |
| Candidate generation | Eligible alternatives appear; missing/empty states are explicit |
| Candidate comparison | Empty sets unavailable; shared valid candidates required |
| PPO separation | Actual PPO action distinct or comparison unavailable |
| Pivot | Candidate/rejected/confirmed semantics and version lineage correct |
| Unit/economy | Tier progress, affordability, unknown pool, marginal cost and horizon coherent |
| Lineup/position | Integrated selected-board/deferred-target/physical destination proof |
| Staleness | Same-round sequence change rejects stale recommendation |
| Lifecycle | Two sequential episodes isolated in same Engine process |
| Outcomes | Delayed/missing/pivoted outcomes correlated without causal claims |
| Feature flag | Enabled and disabled paths both correctly reported |
| Determinism | Same fixture/seed/config produces reproducible artifacts |
| Read-only | No action execution; native masks/rules unchanged |

## 12. Gate status and implementation boundary

This document defines the replay acceptance contract. Issue #289 remains open until replay fixtures, integration tests, deterministic artifacts, and all post-Gate-8 acceptance proofs exist.

No runtime code/tests, PPO, observations, rewards, checkpoints, masks, Engine rules, Viewer behavior, or game actions are changed. Gate 8 and explicit implementation authorization remain mandatory.
