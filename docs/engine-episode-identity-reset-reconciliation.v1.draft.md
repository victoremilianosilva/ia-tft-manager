# Engine Episode Identity and Factory Reset Reconciliation v1 — Draft

**Status:** source-backed identity correction; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Purpose and correction

Earlier UnitInstance audits correctly found that the factory is reseeded from `impl_->seed` during reset, so the same-seed reset can reproduce UUIDs. However, the previous wording that no Engine match/episode namespace exists was too broad.

The current Engine does have `episode_id`:
- it is stored by TFTEngine::Impl as a numeric counter;
- it is included in Engine results and multiple diagnostic/strategic contexts as `match_id` or `engine_match_id`;
- `TFTEngine::reset()` increments it before reinitializing the episode.

This is a real per-Engine-object episode discriminator. It does **not** prove a globally unique Engine instance identity across separately constructed TFTEngine objects or processes. The contract must preserve that distinction.

## 2. Source-backed lifecycle

### 2.1 Engine construction

The audited implementation stores a numeric `episode_id` in TFTEngine::Impl, initialized as a value member. No UUID/session nonce or process-global registry is present in the audited field/constructor path. The initial episode therefore starts from the default counter value for each newly constructed Engine object.

### 2.2 Reset

`TFTEngine::reset(optional_seed)`:
1. optionally replaces the Engine base seed;
2. increments `episode_id`;
3. clears strategic owner/runtime state and resets per-player strategic context sequences;
4. reseeds matchmaking with `seed + episode_id`;
5. returns current shop offers and resets the shared UnitPool;
6. reconstructs `UnitInstanceFactory(catalog, seed)`;
7. reinitializes players and their shops/starter units.

The factory is seeded with the base `seed`, not `seed + episode_id`. Consequently, a same-seed reset increments episode_id but restarts the UnitInstance UUID sequence from the same factory seed. The same initial factory call order can reproduce the same UUIDs in a later episode of the same Engine object.

Sources: `cpp/src/lobby/TftEngine.cpp` — Impl episode_id field near line 487; reset near lines 6162–6235; Engine strategic context uses episode_id near lines 3364, 3570, 3879 and sidecar metadata near 4135; `UnitInstanceFactory.cpp` constructor seeds mt19937_64 directly from its seed.

### 2.3 Distinct Engine objects

The audited identity source for `episode_id` is a per-Impl numeric counter. A newly constructed Engine object begins from its own initial counter state. No globally unique Engine-instance token was found in the audited fields and reset path.

Therefore, the pair `(engine_instance_scope, episode_id)` would be needed to distinguish the same numeric episode value produced by two independent Engine objects, unless a higher-level session/match identity provides and validates that scope. The current numeric `episode_id` alone is not a globally unique match ID.

### 2.4 Identity fields in current diagnostics

Current code uses `episode_id` as:
- `match_id` in several strategic evidence/Composition Intelligence inputs;
- `engine_match_id` in selected diagnostic JSON records;
- `StepResult.episode_id` in native step/reset result structures.

These uses establish a numeric Engine-episode reference, not an external session UUID and not a universal decision sequence. Viewer session UUID, Engine episode ID, strategic-context sequence, Composition Intelligence player sequence, recorder emission sequence and PPO rollout index remain separate namespaces.

## 3. Reconciled conclusions

| Question | Evidence-backed conclusion |
|---|---|
| Does Engine have an episode identity? | Yes: numeric `episode_id` scoped to one TFTEngine::Impl lifetime |
| Does reset advance it? | Yes: incremented before player reinitialization |
| Does same-seed reset produce new UnitInstance UUID sequence? | No: factory is reconstructed from the unchanged base seed |
| Can the pair `episode_id + UnitInstance.uuid` distinguish episodes within one Engine object? | Yes, assuming episode_id is transported and not dropped |
| Does `episode_id` alone distinguish independent Engine objects/processes? | Not proven; each object has its own counter |
| Is there a globally unique Engine-instance ID in the audited source? | Not found |
| Is Viewer `match_id` interchangeable with Engine `episode_id`? | No; Viewer uses a session UUID and needs an explicit mapping |
| Is episode identity a decision sequence? | No; decision/snapshot/owner sequences remain separate typed namespaces |

## 4. Schema and documentation consequences

1. Correct the identity description: current `engine_match_id` is backed by Engine `episode_id`, scoped to one Engine object; it is not absent.
2. Do not claim `episode_id` is globally unique across independent Engine objects.
3. Do not require raw UnitInstance UUID to be unique across episodes if the canonical identity is a composite that includes validated Engine/session scope. Do require uniqueness among simultaneously owned physical instances within the declared episode/player scope.
4. Keep Viewer session UUID and Engine episode ID distinct; the correlation envelope must require both and validate the mapping.
5. The current Decision Identity v2 design must explicitly state the producer and uniqueness scope of `engine_match_id`; if cross-process/replay collision resistance is required, it needs an additional Engine-instance/session namespace or a stronger externally assigned match identity.
6. Preserve the existing factory UUID as an instance token; do not silently change its generation or seed in this documentation pass.

## 5. Remaining proof

- Trace the TFTEngine constructor and all Engine creation sites to determine whether a higher-level caller supplies a unique session/match ID outside the Impl counter.
- Trace ViewerSession's Engine correlation mapping and verify whether every replay/diagnostic path retains both the Viewer UUID and numeric Engine episode ID.
- Verify reset with same seed produces repeated initial UnitInstance UUIDs while episode_id advances; this is a future executable regression, not run here.
- Define the canonical Engine-instance scope and reset policy before accepting the decision identity hash contract.
- Reconcile schema v2 `match_id`, `engine_match_id`, `session_match_id` and `episode_id` fields without aliasing them by name alone.

## 6. Architecture reconstruction review

1. **Prior problem:** earlier identity notes recognized UUID reuse but described Engine match/episode namespace as absent, overlooking the numeric per-Impl episode counter.
2. **Technical justification:** reset increments episode_id while reseeding UnitInstanceFactory from the unchanged base seed; independent Engine objects can begin with the same numeric counter.
3. **New responsibility:** this note owns the source-backed distinction between Engine-object scope, episode identity, factory UUID lineage and Viewer session identity.
4. **Contract and invariants:** episode_id is per Engine object; reset increments it; factory UUIDs can repeat across same-seed episodes; no global Engine ID is inferred; Viewer and Engine identities require explicit mapping.
5. **Cross-component impacts:** TFTEngine construction/reset, UnitInstanceFactory, strategic evidence, Composition Intelligence, Unified sidecar, pybind StepResult, ViewerSession, replay, decision identity schema and PPO rollout.
6. **Objective validation:** construction/reset source paths and identity consumers are traced; prior overbroad claim is corrected; remaining external-scope questions and executable reset regression are explicit; no runtime or tensor changes.

Issue #346 remains open. Gate 8 remains blocked.
