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
- `docs/observation-schema-v2-identity-field-semantics-reconciliation.v1.draft.md`
- `docs/engine-identity-scope-reconciliation.v1.draft.md`
- `docs/observation-structured-entity-audit-coverage-status.v1.draft.md`
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
- `docs/observation-structured-entity-audit-coverage-status.v1.draft.md`

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
- `docs/observation-schema-v2-identity-field-semantics-reconciliation.v1.draft.md`
- `docs/engine-identity-scope-reconciliation.v1.draft.md`
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

## 10. Latest integrated evidence reconciliation — 2026-11-15

The documentary/source audit has advanced since the first version of this readiness review. The following evidence is now incorporated; it does not change the runtime status in the gate table.

### Identity envelope semantics are now explicit

- v2 match_id means authoritative logical game-match identity from a validated game/platform source. The Overwolf boundary's gameId is not yet proven to be per-match unique, so no canonical match_id producer is accepted in the audited main repository.
- v2 engine_match_id means a canonical Engine-episode scope that distinguishes Engine object lifetime plus episode. The current native episode_id is local to one TFTEngine::Impl and is insufficient alone.
- ViewerSession UUID maps to session_match_id only. Overwolf sessionId remains source-session metadata, not automatically the Viewer UUID. Legacy Viewer diagnostic match_id/engine_match_id fields are not copied directly into a complete v2 identity.
- Overwolf revision is a source-state revision, not an Engine decision/snapshot sequence; capturedAt is timestamp metadata.
- Native episode_id remains local metadata. Native player seat 0–7 is serialized as player-0 through player-7, scoped by engine_match_id, and is not a persistent participant UUID.
- The v2 JSON Schema and namespace registry descriptions now reflect these meanings. Existing identity hash scope and hash vectors remain unchanged.

Evidence: docs/observation-schema-v2-identity-field-semantics-reconciliation.v1.draft.md, docs/engine-identity-scope-reconciliation.v1.draft.md, docs/native-engine-instance-episode-identity-scope-audit.v1.draft.md, spec/sequence-namespace-registry.v2.draft.json and spec/decision-identity-v2-hash-vectors.draft.json.

### Source inventory and structured entity coverage

- All 125 tracked Python files were inspected for identity fields and the five native test-hook names (66 test files + 59 other Python files).
- All 127 tracked C++ files were inspected for explicit UnitInstance/UUID/generate_uuid/episode_id/test-hook references (48 C++ tests + 79 production headers/sources/bindings). This does not by itself prove every implicit C++ value-copy/assignment/destruction lifecycle path.
- The structured entity coverage matrix contains 17 unique entity kinds and 31 field-family rows. Every row has a source/status/delivery disposition, but multiple families remain unverified, Shadow-only, not produced, not correlated or not exposed to Python.
- UnitInstance UUID generation is implemented by UnitInstanceFactory; the old header comment claiming future generation is stale. UUID is still not globally unique across same-seed Engine resets/objects, and it is not a typed PPO observation/rollout identity.
- The C++ fixture hooks are concentrated in the native pool/lifecycle test. Python calls are limited to two test files. Test-hook fixture use does not prove ordinary production ownership or item lifecycle.

Evidence: docs/python-identity-test-hook-callsite-inventory.v1.draft.md, docs/cpp-identity-test-hook-caller-audit.v1.draft.md, docs/observation-structured-entity-audit-coverage-status.v1.draft.md, docs/observation-structured-entity-producer-audit.v1.draft.md and spec/observation-structured-entity-producer-coverage.v1.draft.csv.

### Remaining cross-gate blockers

1. No authoritative game-match ID producer or canonical Engine-instance scope producer is available in the audited main repository; complete v2 identity therefore remains unavailable.
2. Native episode_id is dropped by the Python training wrapper; observation, masks, action and rollout still lack one exact typed decision identity.
3. UnitInstance cross-episode scope/collision policy, complete implicit-copy lifecycle proof and elimination equipment cleanup remain open.
4. Physical item-instance identity, shop offer opportunity identity, anvil gameplay producer, action candidate producer, and typed ordered decision history remain absent or incomplete.
5. Actor/Critic and RolloutBuffer do not receive the complete structured entity/identity envelope; diagnostic availability is not PPO delivery.
6. Executable integrated replay and new-lineage evaluation remain pending.

These updates improve documentary precision and traceability only. They do not promote any gate from documentary review to runtime acceptance.

## 11. Gate 8 decision

Gate 8 remains blocked. This review does not authorize implementation.

Before Gate 8:
1. User reviews this integrated Gate 1–7 evidence and unresolved decisions.
2. Any requested documentary corrections are merged.
3. Gate-specific acceptance criteria are reconciled with the current evidence and explicitly approved.
4. User explicitly authorizes runtime implementation.

Until then, all work remains documentation/source audit only. No Engine, runtime, observation, action mask, PPO, reward, training, checkpoint, Viewer or Overwolf changes.

## 12. Architecture reconstruction review

1. **Prior problem:** each gate had a separate contract/audit, but no single evidence ledger distinguished documentary completion from executable acceptance across Gates 1–7.
2. **Technical justification:** implementation readiness depends on cross-gate contracts and integration boundaries; a locally complete document cannot prove end-to-end semantics or runtime conformance.
3. **New responsibility:** this document is the integrated readiness ledger for Gates 1–7 and the explicit Gate 8 blocker; it does not own any runtime producer.
4. **Contract and invariants:** Shadow remains canonical; PPO remains the learning algorithm; Engine masks remain final legality authority; unknown is not zero; diagnostics are not PPO labels; checkpoints are immutable; no runtime work before Gate 8 authorization.
5. **Cross-component impacts:** observation schema, action/masks, reward, PPO/checkpoints, strategic owners, legacy migration, replay/evaluation, Viewer and Overwolf inference.
6. **Objective validation:** every Gate 1–7 has current documentary evidence, current runtime gaps, remaining acceptance criteria and source links; Gate 8 remains explicitly blocked.



### UnitInstance elimination and copy-lifecycle evidence update — 2026-11-15

The focused follow-up confirms that `eliminate_players()` calls `return_eliminated_player_units()`, which returns champion copies and clears board/bench but does not invoke ItemEngine equipment return/cleanup/reset. The eliminated PlayerEnv retains its ItemEngine until the Engine reset lifecycle, so UUID-keyed equipment records can remain after their physical UnitInstances have left active ownership. Item-target enumeration still depends on live board/bench units; retained map state is not proof of an active target or cross-player transfer.

The two focused native test files establish sale return-to-inventory and merge transfer, but do not exercise elimination with equipped board/bench units. This is a scoped test gap, not a repository-wide claim that no elimination test exists.

The UnitInstance declaration also retains a stale comment saying UUID generation is future work; the factory's create/generate_uuid implementation proves generation exists. The struct declares no custom copy/move operations in the inspected declaration, so compiler-generated value copies preserve the UUID string. The complete implicit copy/ownership graph remains unproven.

These findings strengthen the existing blockers: explicit terminal item policy, exactly-once equipment cleanup, active-owner lifecycle, and scoped physical identity. They do not authorize a runtime fix or change Gate status.


### Elimination orphan observability boundary — 2026-11-15

The orphaned ItemEngine equipment map is not enumerated by the inspected structured projections: `get_audit_snapshot()` serializes equipped item IDs from live board/bench UnitInstance mirrors, while its ItemEngine section exposes components/inventory/anvil/last-action fields but not the full UUID-keyed `equipped_` map. Strategic Planner item evidence also binds only current board/bench units. Ordinary item-target masks enumerate live board/bench slots and require a live target for type-7 equip. Thus retained orphan UUID mappings are neither visible in those structured projections nor targetable through that ordinary item-target path.

This is a diagnostic/selection boundary, not proof of cross-player leakage or policy consumption. The terminal item policy and exactly-once cleanup remain unresolved. Runtime acceptance must explicitly prove the selected terminal disposition and expose enough audit evidence to verify it.


### Conditional eliminated-player pending-anvil contract risk — 2026-11-15

A source trace found that pending-anvil state overrides masks to a forced type-7 choice and Engine effective-action preparation preserves that choice for a finished player. But `PlayerEnv::step()` returns `acted=false` immediately for `info.alive == false`, before item dispatch. If a pending anvil survives into elimination, the mask advertises a choice that the executor ignores. Alive-player completion does not appear to stall on this no-op. Normal-gameplay reachability is not proven; classify this as a conditional mask/executor contract risk, not a reproduced defect. Gate acceptance requires either a deterministic reachable scenario with an explicit terminal policy or a proof/test that the state cannot occur.


### Full-match elimination test coverage refinement — 2026-11-15

The Python integration test `tests/test_full_match_terminal_ranking.py` does drive a real lobby through combat/elimination and validates terminal ranking and placement rewards while selecting actions from masks for all eight seats. It does not prove elimination-time equipment cleanup, post-elimination pending-anvil consumption, dead-player `acted` status, or an inactive-only mask contract. It also records but does not assert completed-item loot. Thus the remaining gap is not “no elimination integration test”; it is the specific interaction among elimination, item ownership, forced masks and typed execution outcome.


### Production UnitInstance transfer-path refinement — 2026-11-15

A source-backed transfer map now distinguishes physical ownership transitions from value-copy projections:

- Shop draw creates a new factory UnitInstance.
- Reroll rollback stores a temporary copy of previous offers for failure restoration; successful reroll discards the backup.
- Strategic decision-state construction copies an offer into a temporary projection input and emits UnitSnapshot metadata; it is not an ownership transfer.
- Purchase moves the shop offer into bench.
- Bench/board positioning uses move or swap.
- Merge keeps the purchased UnitInstance UUID as survivor, transfers consumed UUID equipment mappings to it, and resets consumed slots.
- Sale returns equipped items by UUID before bench removal.
- Elimination removes board/bench owners but leaves UUID-keyed equipment entries without explicit terminal cleanup.
- Engine reset reconstructs the factory from base seed, so UUID sequences can repeat across same-seed episode scopes.

This narrows the explicit production paths but does not close the implicit C++ copy/assignment/destruction proof or establish a globally scoped physical identity.


### Pending-anvil risk reachability qualification — 2026-11-15

The conditional eliminated-player pending-anvil mask/executor mismatch is not currently shown reachable through the audited main-repository gameplay path. The production C++ translation-unit audit found no call to the two ItemEngine anvil enqueue APIs; the real PvE reward path grants inventory items directly; and pybind does not expose an anvil enqueue method. Direct ItemEngine tests are not a live TFTEngine producer. Keep this as a future-producer guard, not a current production defect, unless a deterministic gameplay path is established.


### AuditSnapshot terminal player status gap — 2026-11-15

The native `AuditPlayerSnapshot` DTO has no `alive` or `eliminated` field, although the separate `get_public_state()` path exposes player elimination status. Consumers of AuditSnapshot cannot distinguish an eliminated player with cleared units from a living player with an empty board/bench using that DTO alone. A separate public-state status is useful but must be correlated to the same Engine episode/snapshot; occupancy or mask shape is not a substitute. Future diagnostic acceptance must bind terminal status and item disposition to one correlated audit record.


## 13. Final documentary reconciliation link — 2026-11-15

The six requested documentary workstreams have been consolidated in [Final Documentary Reconciliation — Gates 1–7 v1](gates-1-7-final-documentary-reconciliation.v1.draft.md). That report reconciles identity/lifecycle, GEP-to-PPO correlation, all 17 structured entity kinds / 31 field-family rows, the unresolved elimination item policy decision, CSV integrity and the Gate 1–7 readiness table.

This is a documentation closeout only. It does not change the gate table's runtime dispositions, close issue #346, select the terminal item policy, or authorize Gate 8. In particular, a complete source inventory is not proof of every implicit C++ copy/destruction path, and producer coverage is not proof of PPO delivery.


## 14. Elimination item ownership decision — 2026-11-15

The domain owner decided that **items of an eliminated player must not be transferred to anyone**. The prior alternative of returning equipment to the eliminated player's own active bag is rejected. Terminal policy is now Policy A: capture immutable non-owning terminal diagnostics, then retire/discard that player's equipped items, inventory, loose components and pending anvil options. No item returns to another player, the shared pool, shop or any redistributable source.

This resolves the domain-policy decision but not implementation acceptance. ItemEngine terminal retirement, idempotence, no-redistribution invariants and regression tests remain post-Gate 8 work. No runtime implementation is authorized by this decision.


## 15. Remaining identity/rollout reconciliation and superseding dispositions — 2026-11-15

The later [Remaining Identity, Ownership, Rollout and Gate Reconciliation](remaining-identity-rollout-gate-reconciliation.v1.draft.md) is authoritative for the remaining main-repository identity and PPO correlation status.

Corrections to earlier sections of this review:
- The eliminated-player item policy is **settled**, not undecided: terminal retirement/discard, no transfer to another player, no return to the eliminated player's active bag, and no redistribution. Runtime retirement/tests remain post-Gate 8.
- GEP real-source validation is **deferred until Overwolf integration** per user direction. The exact mapper path and synthetic behavior remain documented; real capture/reconnect validation is not a blocker for the current main-repository workstream.
- `UnitInstance` is implicitly copyable/movable by value and copies preserve UUID. `TFTEngine` is non-copyable and movable; no Engine-instance scope token is currently produced. Canonical episode scope still requires Engine-instance scope plus `episode_id`.
- Native result/pybind preserve episode ID and masks; the Python wrapper drops them; RolloutBuffer stores masks at the same index as observation/action but stores no durable native identity. Terminal auto-reset returns old-episode reward/done alongside a next-episode observation; this is not proof of a stale-mask race, but it is an uncorrelated replay boundary.

The Gate table remains unchanged in its essential disposition: documentary contracts exist, runtime acceptance for Gates 1–7 remains pending, and Gate 8 is blocked pending integrated review and explicit user authorization.
