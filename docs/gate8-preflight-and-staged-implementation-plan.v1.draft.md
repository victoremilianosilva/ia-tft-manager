# Gate 8 Preflight — Integrated Decision and Staged Implementation Plan v1

**Status:** ready for domain-owner review; Gate 8 is not approved or activated.  
**Architecture:** Shadow remains the canonical strategic context; PPO remains the learning/decision algorithm.  
**Target branch:** `new-arquiteture`.  
**Hard boundary:** no runtime implementation before explicit Gate 8 authorization.  
**GEP scope:** real capture and lifecycle validation is deferred until the Overwolf integration workstream, per the user's direction.

## 1. Purpose

This document is the final preflight package for reviewing Gates 1–7 together and deciding whether to authorize the next phase. It consolidates what is ready, what is deliberately deferred, the decisions already made, and the exact staged order after authorization.

"Ready for Gate 8 review" does not mean that Gates 1–7 have runtime acceptance, that all producers exist, that a tensor layout is selected, or that the project is authorized to change runtime code.

## 2. Gate 8 entry checklist

| Entry condition | Current evidence | Preflight disposition |
|---|---|---|
| Canonical architecture and authority | Shadow is canonical; PPO remains the policy-learning algorithm; native Engine/masks retain final legality | Ready for review |
| Observation semantics | Schema v2 draft, 223-path source crosswalk, 77-entry source map, legacy crosswalk and Actor/Critic delivery matrix | Documentary package ready; source gaps remain explicit |
| Identity and correlation | v2 identity proposal, 9-namespace registry, 7 synthetic hash vectors, Engine/UnitInstance lifecycle audits, wrapper/rollout loss audit | Semantics and gaps documented; runtime producer absent |
| Action and masks | Action/Mask Contract v1 and Strategic Action Candidate Contract v1 | Contract ready; real candidate producer and exact identity-bound mask delivery absent |
| Reward | Reward Contract v1 and temporal/GAE audit | Contract ready; legacy runtime reward remains active |
| PPO/checkpoint | Architecture/checkpoint contract, Actor/Critic consumer matrix, evaluation protocol | Lineage rules ready; concrete projection and architecture manifest not frozen |
| Strategic owners | Strategic ownership, economic, unit, candidate and replay contracts | Authority decisions ready; runtime producers/integration incomplete |
| Legacy shutdown | Static consumer inventory and migration matrix | Audit ready; active consumers remain and must migrate later |
| Replay/evaluation | Deterministic replay and PPO evaluation protocols | Acceptance design ready; executable integrated evidence absent |
| Domain decisions | No-transfer elimination item rule; GEP real-source work deferred to OW | Decisions recorded |
| Phase boundary | Runtime work remains prohibited until explicit user authorization | Preserved |

## 3. Decisions closed for the next phase

These decisions are not to be reopened without new source evidence or an explicit domain-owner change:

1. **Architecture:** Shadow is the canonical strategic context, not a disposable parallel AI. PPO remains responsible for learning and selecting policy actions.
2. **Legality:** native Engine rules and exact action masks remain the final legality authority. Shadow candidates/recommendations never execute actions.
3. **Strategic ownership:** StrategicPlanner owns direction commitment; ActiveCompositionManager/TransitionManager owns active composition; candidate producers cannot mutate active state; Unified Shadow remains diagnostic-only.
4. **Economy:** posture and progression are separate outputs. Missing projections/risk remain unknown; no synthetic defaults.
5. **Elimination items:** terminal discard/retirement; no transfer to another player, no return to the eliminated player's active bag, and no redistribution to any pool/shop/PvE source.
6. **Checkpoints:** historical checkpoints remain immutable baselines. No automatic semantic compatibility or implicit legacy migration.
7. **GEP:** real capture, consecutive-match and reconnect/reset validation is deferred until Overwolf integration. It is not a blocker for the main-repository preflight.

## 4. PPO Actor/Critic contract decisions

The current implementation and future contract must not be conflated. The following semantic consumer decisions are recommended for the first new PPO lineage and are independent of any tensor layout:

### 4.1 Exact action masks

- Actor and Critic receive the exact same decision-correlated native mask snapshot as a separate side input.
- The Critic must not silently ignore masks, reconstruct them from the observation, or fetch a later mask.
- Mask arrays remain distinct from observation features and remain subordinate to final Engine validation.
- The only acceptable alternative would be a separately reviewed representation proven lossless for every mask value, ordering and conditional-head meaning. No such alternative is currently established; therefore exact masks are the default normative requirement.

### 4.2 Item and recipe compatibility

- The underlying factual inputs (owned item/component inventory, physical unit targets, target profiles and catalog/recipe semantics) are shared semantic state and are eligible for both Actor and Critic context when producer evidence is valid.
- The current 9×37 inventory-fit and 100×37 recipe-fit matrices are Actor action-conditioning structures. They are not required to be copied raw into the Critic in the first projection.
- The Critic may consume a separately encoded/aggregated representation derived from the same validated factual inputs, but only if its feature identity, formula, provenance and target meaning are explicit. It must not receive a different or stale state snapshot.
- Any expansion of Critic compatibility context beyond those factual inputs requires a controlled ablation; no matrix dimensions or encoder structure are selected here.

### 4.3 Additional Critic history

- No separate AntiLoopEngine history or untyped action-history block is required in the initial projection.
- Current AntiLoopHistory is bounded internal legality/movement history without per-record decision sequence and is not exposed as a typed ordered event stream. It cannot be projected as canonical decision history.
- The initial Critic uses validated current-state evidence plus exact masks. Additional temporal/history context is a later, separately versioned feature family requiring an authoritative producer, typed sequence, reset semantics, replay fixtures and evaluation ablation.
- This decision does not claim the current observation is a fully Markov-sufficient state. It prevents an uncorrelated legacy history stream from being promoted prematurely.

### 4.4 Encoder and tensor layout

Shared versus separate encoders, feature ordering, tensor dimensions, offsets, padding, normalization values, board geometry encoding, entity encoders and action-head dimensions remain deliberately unselected. The concrete projection must be a reviewed artifact before any PPO runtime implementation PR. Gate 8 authorizes the staged program to produce and review that artifact; it does not waive the projection review.

## 5. Unresolved facts accepted as post-authorization implementation work

The following are not hidden blockers or documentation omissions. They are known runtime gaps with owners and acceptance tests:

- Engine-instance scope token and typed decision/observation/mask sequence producers.
- Exact native → pybind → wrapper → vector environment → Trainer → RolloutBuffer identity transport.
- Real action-candidate production and candidate-set completeness.
- Missing projected income, incoming damage and elimination risk; explicit unknown handling.
- Full structured entity producers/delivery for all unavailable or diagnostic-only fields.
- Terminal ItemEngine retirement, no-redistribution invariants and regression tests.
- Legacy StrategyInfo/PPO/reward/Viewer consumer migration and safe shutdown.
- Deterministic multi-round replay and new-lineage PPO evaluation.
- New checkpoint manifest/loader and compatibility validation.

These gaps are why Gates 1–7 do not have runtime acceptance today. They are not a reason to fabricate values or perform premature partial migrations.

## 6. Staged implementation order after Gate 8

Authorization starts a controlled program, not an unrestricted runtime rewrite. Each stage has its own reviewable PRs, tests, evidence and rollback point.

### Stage 0 — Freeze the semantic design inputs (documentation/design only)

1. Review/approve Schema v2 identity semantics and namespace registry; preserve v1 artifacts unchanged.
2. Approve the exact decision-identity envelope and independent observation/mask content-hash procedures.
3. Produce the concrete tensor projection manifest: feature IDs, exact source paths, consumers, status/missingness, units, formula IDs, normalization, entity cardinality, ordering, shape and deterministic hashes.
4. Complete the semantic feature → projection → Actor/Critic consumer/head map.
5. Select encoder/actor/critic architecture only after the projection exists; record ablation questions rather than guessing from legacy shapes.
6. Freeze Action/Mask and Reward/temporal contract identities and their cross-contract compatibility matrix.
7. Review every checkpoint load/save path against the manifest policy.

**Exit:** approved immutable design artifacts; no runtime implementation until this stage is reviewed and accepted.

### Stage 1 — Native identity and atomic decision snapshot

1. Introduce Engine-instance scope owned by native Engine lifecycle; moves preserve scope, new Engine instances get distinct scope.
2. Define typed episode/player/round/decision/observation/mask sequence references with explicit owners, reset and monotonicity.
3. Bind observation and exact mask payloads atomically to one decision envelope.
4. Add content hashes and fail-closed stale/mismatch behavior.
5. Preserve native Engine legality as final authority.

**Exit:** deterministic native tests prove scope uniqueness, reset/move semantics, mask correlation and stale rejection.

### Stage 2 — Structured entity and strategic evidence producers

1. Implement only authoritative producers with explicit ownership, cardinality, completeness, provenance, formula/catalog version and source sequence.
2. Preserve distinct board/bench/shop/pool/item/component/trait/position domains.
3. Implement the settled eliminated-player item terminal-discard policy exactly once, with no transfer or redistribution.
4. Build the real StrategicActionCandidate producer; empty/incomplete sets remain explicit and never become confident HOLD.
5. Complete direction/composition/economic/unit/position owner snapshots without parallel authority or Shadow execution.

**Exit:** native producer tests and source-to-schema audit show no fabricated values, duplicate active owners or cross-player item transfer.

### Stage 3 — Python transport and rollout identity

1. Preserve native decision envelopes and masks through pybind/wrapper/vector environment/Trainer.
2. Bind terminal reward/done to the old episode and reset observation/masks to the new episode.
3. Store identity, observation/mask hashes, action and outcome references in RolloutBuffer.
4. Preserve per-player reward components, validity and terminal/truncation boundaries according to Reward Contract.
5. Ensure Actor and Critic consume the same exact decision-bound mask snapshot.

**Exit:** deterministic wrapper/Trainer/Rollout tests prove exact transition correlation across normal step, reset, auto-reset, vector failure and minibatch/replay.

### Stage 4 — PPO projection, architecture and checkpoint lineage

1. Implement only the approved projection manifest.
2. Implement Actor/Critic consumers according to the approved semantic matrix and exact mask side-input contract.
3. Remove old policy-side nominal strategy/reserve derivations only after replacement sources are wired and tested.
4. Implement checkpoint manifests, semantic compatibility classification, save/load/resume and immutable legacy baseline handling.
5. Do not transfer optimizer/scheduler state unless the manifest explicitly proves compatibility.

**Exit:** projection fixtures, policy/action-head tests, checkpoint compatibility tests and new-lineage smoke training pass.

### Stage 5 — Reward migration and legacy isolation

1. Replace legacy strategy-ID reward shaping with consequence-based events from authoritative producers.
2. Prove event identity, deduplication, temporal credit and per-player GAE isolation.
3. Migrate PPO, reward, evaluation, fine-tuning, Viewer and logs to their declared new sources.
4. Retain historical readers where justified; remove active legacy producers only after consumer and replay proof.

**Exit:** reward regression suite and consumer inventory prove no active decision/reward path depends on legacy strategic semantics.

### Stage 6 — Viewer, integrated replay and evaluation

1. Preserve required Viewer presentation compatibility through a read-only projection; historical logs remain readable.
2. Run deterministic multi-round strategic replay across the full producer → candidate → owner transition → lineup → economy → positioning → evaluator → diagnostics chain.
3. Run PPO evaluation using immutable baseline, paired seeds, seat rotation, train/validation/test separation, uncertainty, ablations and promotion/rollback criteria.
4. Publish replay and evaluation manifests plus raw/aggregate reports.

**Exit:** Gates 1–7 receive runtime acceptance evidence; only then can the new lineage be considered promotion-ready.

### Stage 7 — Overwolf integration (separate workstream)

1. Validate real sanitized GEP payloads and match-ID leaf.
2. Prove new-match/reconnect/game-exit/re-entry reset invocation and stale/missing behavior.
3. Bind GEP source metadata to the native live-state adapter without treating GEP revision/session as Engine decision identity.
4. Prove the live path produces read-only recommendations and never calls simulation reset/step or executes gameplay actions.

**Exit:** live integration acceptance is independently recorded. This stage does not redefine the main-repository contracts.

## 7. Cross-stage invariants

- No second AI, no replacement of PPO with Shadow, and no autonomous gameplay execution.
- Shadow remains canonical strategic context and read-only recommendation source.
- Engine/masks remain final legality authority.
- No synthetic identity, candidate, item, pool, economic risk, history or position values.
- Unknown/missing/stale/partial/incompatible remain distinct from numeric zero.
- No legacy checkpoint overwrite; no silent semantic migration.
- Every implementation PR must include tests and traceable source/contract changes; runtime changes are not governed by the six-point documentation template unless the PR changes documentation.
- Rollback preserves prior artifacts and restores the last accepted contract-compatible stage.
- GEP real-source validation stays deferred until Stage 7.

## 8. Gate 8 authorization decision

Gate 8 is ready for the user's integrated review when:
- this preflight and the Gates 1–7 readiness ledger have been reviewed together;
- the user accepts the stated post-authorization gaps and staged order;
- the user explicitly authorizes Stage 0 / the implementation program.

No authorization is inferred from this document, a PR merge, a green CI run or a statement that the work is "ready". Until explicit authorization, all changes remain documentary/source-audit only.

## 9. Architecture reconstruction review

1. **Prior problem:** the gate ledger showed documentary contracts and runtime blockers but did not provide one ordered, cross-component execution plan or settle remaining Actor/Critic consumer ambiguities.
2. **Technical rationale:** identity, masks, structured entities, PPO projection, reward, legacy migration, replay and live Overwolf integration have strict dependency order; premature parallel implementation would create incompatible producers and consumers.
3. **New responsibility:** this document owns the Gate 8 preflight, closed design decisions, accepted runtime gaps, staged implementation order and explicit authorization boundary.
4. **Contract/invariants:** exact masks to Actor/Critic; no uncorrelated history; item/recipe facts shared while raw action-conditioning matrices remain Actor-specific initially; no tensor layout frozen here; no implementation without explicit Gate 8 authorization.
5. **Cross-component impacts:** Schema v2, identity/namespace registry, Engine, masks, structured entities, strategic owners, Python wrapper/vector env, Trainer, RolloutBuffer, Actor/Critic, rewards, checkpoints, Viewer, replay and Overwolf.
6. **Objective validation:** checked 223 schema-path dispositions, 77 source-map entries, 66 legacy mappings, 17 entity kinds/31 rows, nine sequence namespaces, seven synthetic hash vectors, current Actor/Critic delivery and the Gate 1–7 issue set. JSON and CSV artifacts parse with consistent structure. No runtime file is changed.
