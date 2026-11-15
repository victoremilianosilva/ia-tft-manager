# Gates 1–7 Integrated Readiness Review v1 — Draft

**Status:** documentary integration review; no gate is accepted for runtime implementation by this document.  
**Architecture:** Shadow is canonical; PPO remains the learning/decision algorithm.  
**Target branch:** `new-arquiteture`.  
**Hard boundary:** no runtime implementation before Gate 8 and explicit user authorization.

## 1. Purpose

This review consolidates the documentary contracts, source audits and current integration evidence for Gates 1–7. It answers two separate questions:

1. What is documented and source-audited?
2. What is implemented and executable end-to-end?

A documented contract is not proof of runtime conformance. A source-level producer is not proof of Python/PPO delivery. A passing unit test is not proof of multi-round integration. A Shadow recommendation is not a PPO label or a reward target.

## 2. Current gate status

| Gate | Documentary status | Runtime/evidence status | Current disposition |
|---|---|---|---|
| 1 — Observation schema/context (#293) | Schema v2, canonical JSON/hash contract, source crosswalk and field-level audit documented | Flat legacy observation remains active; no structured v2 producer/adapter/validator or sequence-bound delivery; many fields explicitly unavailable/not produced | **Docs reviewed; runtime pending** |
| 2 — Action and legality (#294) | Strategic Action Candidate Contract and mask/legality contracts documented | Audited source candidate vector is empty; mask arrays have no runtime contract/hash/decision identity; masks are Actor-only in current policy and Critic ignores them | **Docs reviewed; runtime pending** |
| 3 — Reward/credit assignment (#287) | Reward Contract v1 documented | Existing legacy reward path remains active; no v1 event identity, temporal attribution, deduplication, normalization and per-player acceptance implementation | **Docs reviewed; runtime pending** |
| 4 — PPO/checkpoint (#286/#288) | PPO Architecture and Checkpoint Contract v1 documented | No new semantic projection, Actor/Critic layout, checkpoint manifest/loader lineage or executable migration; old checkpoints remain immutable baselines | **Docs reviewed; runtime pending** |
| 5 — Strategic authority/integration (#281–#284 and #306–#316) | Ownership, candidate, economic, unit, transition and replay contracts documented | Runtime gaps remain: empty action candidates, default Flexible progression, missing projected income/incoming damage/elimination risk, non-authoritative hardcoded false lock, partial owner snapshots | **Docs reviewed; runtime pending** |
| 6 — Legacy audit/shutdown (#301) | Static consumer inventory and migration matrix complete; #301 closed | `StrategyInfo` still feeds active PPO/reward/evaluation/Viewer paths; no migration or shutdown proof | **Static audit complete; runtime migration blocked** |
| 7 — Replay/evaluation (#289/#295) | Strategic Shadow Integrated Replay Contract and PPO Evaluation Protocol documented (#315/#317) | No executable end-to-end multi-round replay or new-lineage PPO evaluation acceptance; no approved run manifest/artifacts for a migrated policy | **Docs reviewed; executable acceptance pending** |
| 8 — Implementation approval | Not granted | Requires integrated Gates 1–7 review and explicit user authorization | **Blocked** |

## 3. Gate 1 — Observation schema and context

### Evidence completed

- Schema v2 defines the intended structured roots and decision identity envelope.
- Canonical JSON/hash rules and crosswalk artifacts exist.
- The field/source CSV now contains 223 unique schema paths and 16 columns.
- All 164 ancestor-matched paths have individual dispositions.
- All 43 exact source-map matches have callsite/formula/delivery dispositions.
- All 16 no-source-map paths have explicit classifications.
- All 223 paths have current Actor/Critic delivery classifications.

Relevant evidence:
- `spec/observation-schema.v2.draft.json`
- `spec/observation-schema-v2-field-source-crosswalk.v1.draft.csv`
- `docs/observation-schema-v2-field-source-crosswalk.v1.draft.md`
- `docs/observation-schema-v2-actor-critic-current-delivery.v1.draft.md`
- Unit/item, strategic, owner-snapshot, action-opportunity, derived-context and legal-state field-proof documents.

### Remaining acceptance

- Implement the approved structured producer/adapter and validators after Gate 8.
- Preserve field-level provenance, quality, completeness, identity and typed sequence.
- Reject stale, partial, mismatched and uncorrelated snapshots rather than manufacturing defaults.
- Define the actual projection manifest and feature ordering only after the source/consumer decisions are accepted.
- Prove the full native → pybind → Python → vector environment → rollout → policy path with deterministic fixtures.

**Current blocking facts:** the current Python policy still consumes a flat observation vector. Diagnostic snapshots and Shadow owner records are not a structured Schema v2 payload. Projected next-round income, incoming damage and elimination risk remain unpopulated defaults; these are not observed zeros.

## 4. Gate 2 — Action and legality

### Evidence completed

- Candidate contract defines immutable snapshot-bound alternatives, exact physical parameters, producer identity, candidate-set identity, source sequences, provenance and cost/benefit breakdown.
- Native Engine rules and masks remain final legality authority.
- Candidate, PPO action, baseline recommendation, contextual proposal and executor resolution are separate concepts.

Relevant evidence:
- `docs/strategic-action-candidate-contract.v1.draft.md`
- `docs/observation-schema-v2-action-opportunity-temporal-field-proof.v1.draft.md`
- `docs/observation-schema-v2-legal-state-critic-context-field-proof.v1.draft.md`
- `docs/observation-schema-v2-actor-critic-current-delivery.v1.draft.md`

### Remaining acceptance

- Populate real candidates from an authoritative producer with stable candidate ID/revision/set identity and exact physical parameters.
- Make empty candidate sets distinguishable from valid empty comparisons and no-eligible-candidate results.
- Bind observations and masks to the same match/player/round/decision identity and typed sequence.
- Version/hash the action and mask contracts and reject stale/mismatched mask snapshots.
- Supply masks to the Critic/value path as required by the target contract, or approve a proven lossless alternative.
- Test native legality rejection, stale masks, missing parameters, duplicate physical units and every action head.

**Current blocking facts:** the audited `StrategicSharedContext.action_candidates` source vector is empty. Current masks are raw arrays without contract/hash/decision identity. Actor consumes masks; current `get_value()` ignores them.

## 5. Gate 3 — Reward and credit assignment

### Evidence completed

Reward Contract v1 specifies outcome-based reward, event ownership, per-player trajectory semantics, temporal attribution, deduplication, normalization and isolation from Shadow confidence/recommendations.

Relevant evidence:
- `docs/reward-contract.v1.draft.md`
- `docs/legacy-strategic-consumer-migration-matrix.md`

### Remaining acceptance

- Replace active strategy-ID and legacy composition-based reward shaping with the approved consequence-based components.
- Give each event a stable identity, owner, source, unit, time window and deduplication key.
- Implement per-player reward/done/bootstrap/GAE isolation.
- Prove action, round, terminal and optional potential-shaping attribution without double payment.
- Add tests for duplicate events, missing evidence, truncation, simultaneous player outcomes and episode reset.
- Record reward contract hash/version in every new checkpoint and evaluation manifest.

**Current blocking fact:** the contract is documentary; the old reward path remains active. Existing reward formulas are historical evidence, not v1 authority.

## 6. Gate 4 — PPO architecture and checkpoint

### Evidence completed

- PPO Architecture and Checkpoint Contract v1 separates structural loadability, inference-semantic compatibility, training-resume compatibility and historical evaluability.
- Old checkpoints remain immutable; backward compatibility with the new semantic lineage is not required.
- The current Actor/Critic consumer path is now traced for all 223 Schema v2 paths.

Relevant evidence:
- `docs/ppo-checkpoint-contract.v1.draft.md`
- `docs/observation-schema-v2-actor-critic-current-delivery.v1.draft.md`
- `docs/observation-projection-consumer-matrix.v1.draft.md`

### Remaining acceptance

- Decide the future semantic projection and Actor/Critic consumers from evidence; no tensor layout is selected in this review.
- Resolve whether item/recipe compatibility matrices should also be available to the Critic.
- Decide whether Critic needs additional history/context independently of masks.
- Implement architecture identity, observation/action/reward/catalog hashes and checkpoint manifests.
- Implement new-lineage loader, save/resume and evaluation-only validation.
- Prove no silent semantic migration from legacy checkpoints.

**Current blocking facts:** Actor and Critic share `encode(obs)`, but item compatibility matrices are Actor-only and masks are Actor-only. The current value head consumes the shared observation representation and ignores masks. No new projection or checkpoint manifest is integrated.

## 7. Gate 5 — Strategic authority and integration

### Evidence completed

- Canonical ownership and transition contracts distinguish direction commitment, active composition, candidate generation, economic posture/progression, unit evidence, action candidates and diagnostic Shadow observers.
- Candidate and executor contracts prohibit turning proposals into commands or bypassing native legality.
- Strategic source audits now identify the exact current gaps.

Relevant evidence:
- PRs #306–#316 and associated contracts.
- `docs/strategic-action-candidate-contract.v1.draft.md`
- `docs/observation-schema-v2-strategic-evidence-field-proof.v1.draft.md`
- `docs/observation-schema-v2-strategic-owner-snapshot-field-proof.v1.draft.md`
- `docs/observation-schema-v2-strategic-evidence-exact-source-proof.v1.draft.md`

### Remaining acceptance

- Build a real action-candidate producer; do not add another evaluator.
- Populate progression/economic evidence from authoritative producers and preserve unknown values.
- Replace hardcoded false composition lock with an authoritative lock source or explicit unknown/unavailable.
- Complete owner-specific immutable snapshots with stable owner identity and source decision sequences.
- Integrate generated candidate → canonical commitment → active composition → unit/lineup/economy → positioning → diagnostics without parallel authority.
- Prove the complete chain with multi-round replay.

**Current blocking facts:** action candidates remain empty; progression plan remains default Flexible; projected income, incoming damage and elimination risk remain unpopulated; owner snapshots are split across separate diagnostic surfaces; lock is hardcoded false in the new context.

## 8. Gate 6 — Legacy migration and shutdown

### Evidence completed

- Static producer/consumer inventory is complete and issue #301 is closed.
- Migration matrix classifies active legacy consumers and dependencies.
- The six-part documentation review standard is normative.

Relevant evidence:
- `docs/legacy-strategic-consumer-migration-matrix.md`
- `docs/architecture-reconstruction-review-standard.md`
- Issue #301.

### Remaining acceptance

- Migrate every active consumer to an accepted canonical producer and contract.
- Prove PPO, reward, Viewer, evaluation, fine-tuning and logs no longer depend on legacy StrategyInfo semantics.
- Keep compatibility/read-only historical readers only where justified.
- Remove legacy producer/runtime code only after consumer and replay proof; do not remove it merely because a static inventory exists.

**Current blocking fact:** `StrategyInfo` still feeds active PPO/reward/evaluation/Viewer paths. Static audit completion is not runtime migration completion.

## 9. Gate 7 — Replay and evaluation

### Evidence completed

- Replay contract defines deterministic fixture/seed/config/code/catalog identity, distinct sequence namespaces, Engine↔session correlation and the full strategic chain.
- Evaluation protocol defines immutable lineage manifests, paired seeds, seat rotation, independent RNG streams, data splits, metrics/uncertainty, ablations and promotion/rollback rules.
- Shadow outcomes remain diagnostic and are not PPO reward labels.

Relevant evidence:
- `docs/strategic-shadow-integrated-replay-contract.v1.draft.md`
- `docs/current-replay-correlation-evaluation-gap-audit.v1.draft.md`
- `docs/ppo-evaluation-protocol.v1.draft.md`
- `docs/evaluation-tooling.md`
- Issues #289 and #295; documentary PRs #315 and #317.

### Remaining acceptance

- Implement deterministic multi-round replay fixtures and the full producer/consumer chain.
- Add negative fixtures for stale snapshots, missing identity, incomplete shop/pool, duplicate unit copies, mask mismatch, empty candidates and episode reset.
- Prove Engine↔session correlation with explicit identity and typed sequence references.
- Implement new-lineage PPO evaluation with immutable manifests, paired seeds, seat rotation, independent RNG, train/validation/test separation and report artifacts.
- Evaluate outcome, behavior, legality, stability and uncertainty separately; do not promote based on internal reward alone.
- Produce replay and evaluation artifacts that can be independently reproduced.

**Current blocking facts:** the replay/evaluation documents are approved contracts, not executable acceptance. Viewer log playback does not re-execute Engine/policy; the cross-language fixture covers only round barriers and BUY_XP; rollout has no decision identity; masks are separately fetched; Viewer `identity_complete` does not require Engine match ID. No full multi-round integrated replay or new-lineage PPO evaluation is accepted by this review.

## 10. Gate 8 decision

Gate 8 remains blocked. This review does not authorize implementation.

Before Gate 8:
1. User reviews this integrated Gate 1–7 evidence and unresolved decisions.
2. Any requested documentary corrections are merged.
3. Gate-specific acceptance criteria are reconciled with the current evidence and explicitly approved.
4. User explicitly authorizes runtime implementation.

Until then, all work remains documentation/source audit only. No Engine, runtime, observation, action mask, PPO, reward, training, checkpoint, Viewer or Overwolf changes.

## 11. Architecture reconstruction review

1. **Prior problem:** each gate had a separate contract/audit, but no single evidence ledger distinguished documentary completion from executable acceptance across Gates 1–7.
2. **Technical justification:** implementation readiness depends on cross-gate contracts and integration boundaries; a locally complete document cannot prove end-to-end semantics or runtime conformance.
3. **New responsibility:** this document is the integrated readiness ledger for Gates 1–7 and the explicit Gate 8 blocker; it does not own any runtime producer.
4. **Contract and invariants:** Shadow remains canonical; PPO remains the learning algorithm; Engine masks remain final legality authority; unknown is not zero; diagnostics are not PPO labels; checkpoints are immutable; no runtime work before Gate 8 authorization.
5. **Cross-component impacts:** observation schema, action/masks, reward, PPO/checkpoints, strategic owners, legacy migration, replay/evaluation, Viewer and Overwolf inference.
6. **Objective validation:** every Gate 1–7 has current documentary evidence, current runtime gaps, remaining acceptance criteria and source links; Gate 8 remains explicitly blocked.

