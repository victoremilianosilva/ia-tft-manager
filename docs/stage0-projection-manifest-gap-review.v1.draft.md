# Stage 0 — Projection Manifest Gap Review v1

**Status:** review findings; Stage 0 remains open and runtime implementation is not authorized by this artifact.  
**Canonical branch:** `new-arquiteture`.  
**Canonical architecture:** TFT Strategic Engine.  
**Related issues:** #293, #286, #294, #288, #346; downstream coordination #281–#295.  
**Inputs reviewed:** `stage0-observation-projection-design.v1.draft.md`, `observation-projection-manifest.v1.draft.json`, `observation-projection-consumer-matrix.v1.draft.json`, `observation-schema-v2-field-source-crosswalk.v1.draft.csv`, current Actor/Critic delivery audit, Action/Mask Contract, Reward Contract, and PPO Checkpoint Contract.

## 1. Executive result

The existing Stage 0 package is a useful semantic inventory, but it is **not yet a complete tensor projection manifest and is not ready to authorize runtime work**.

The reviewed machine-readable inventory contains:
- 77 semantic feature entries;
- 24 projection groups;
- disposition totals: 34 shared Actor/Critic candidates, 17 unavailable, 7 control-metadata-only, 9 diagnostic-only, 5 unresolved and 5 critic-only/deferred;
- a 223-path Schema v2 field crosswalk with current Actor/Critic delivery classifications.

Those counts establish inventory coverage, not encoding completeness. The manifest currently records source, availability, nature, formula, unit, group, consumer disposition, treatment, blockers and notes. It does not yet specify the complete per-feature encoding contract required to deterministically construct and validate model inputs.

**Decision:** continue Stage 0 design only. Do not start native, Python, PPO, reward, checkpoint, Viewer or Overwolf runtime changes until the domain owner reviews and accepts the complete Stage 0 package.

## 2. Confirmed architecture boundaries

1. **TFT Engine** owns factual simulation state, native rules, action validation and final legality.
2. **TFT Strategic Engine** is the canonical strategic-intelligence system and contains specialized engines/managers. The former Shadow label is not used as the architecture name in new design.
3. **PPO** remains the learning algorithm and policy that selects actions; it does not imitate strategic recommendations.
4. **Observation Projection** deterministically maps a correlated semantic snapshot into model inputs.
5. **Viewer and diagnostics** remain read-only.
6. Exact native action masks are a separate side input to both Actor and Critic, bound to the same decision identity as the observation. They are not observation features and do not replace Engine validation.

## 3. Stage 0 gaps that must be closed

### 3.1 Per-feature encoding contract

For every feature admitted to the first PPO lineage, add explicit fields for:
- stable feature ID and semantic path;
- producer path and source owner;
- observed/derived/estimated nature;
- formula ID/version and exact input paths where derived;
- unit and sign convention;
- dtype and categorical vocabulary/catalog identity where applicable;
- cardinality, axes and ordering rule;
- tensor representation and whether it is a scalar, categorical token, entity field, relation, set or sequence;
- normalization method, parameters and fit-data identity;
- missing/unknown/partial/stale/incompatible/not-applicable/padding representation;
- validity and presence behavior;
- Actor/Critic consumer and any action-head-specific consumer;
- maximum cardinality and explicit overflow/truncation policy for variable collections;
- projection revision/hash inputs.

Do not fill these values with guessed defaults. If a producer or semantic rule is not proven, retain the field as unavailable/unresolved and exclude it from the initial tensor projection.

### 3.2 Identity and exact decision binding

The design requires logical match, Engine-instance plus episode scope, player seat, round/state, decision identity, source sequence and catalog fingerprint as applicable. The source audits show that this is not yet a runtime guarantee:
- native `episode_id` exists, but no Engine-instance token is produced;
- same-seed Engine resets can reproduce UnitInstance UUID sequences;
- UUID is not a globally scoped physical identity by itself;
- the wrapper currently drops native episode identity and returned masks from its training-facing reset/step result;
- masks are fetched separately and RolloutBuffer does not retain the complete native decision identity.

Stage 0 must specify the exact identity tuple and canonical hash payload, including which fields are mandatory, optional, or unavailable. Stage 1 must implement and prove it. Do not claim exact observation/mask binding exists today.

### 3.3 Producer gaps that must remain explicit

The following are not safe to fabricate in the projection:
- stable shop-offer identity/revision across rerolls;
- globally scoped physical UnitInstance identity;
- complete physical item/component identity (current inventory/equipment largely uses catalog IDs and multiplicity);
- canonical hex-board coordinates/orientation (the audited internal board is a 4×7 slot mapping);
- authoritative action-opportunity candidate set and candidate-set identity;
- projected next-round income, incoming damage and elimination-risk values without validated producers/horizons;
- typed ordered decision history with source sequence and reset/replay semantics;
- complete per-unit trait/item/combat-stat records where only aggregate or partial features are currently produced;
- fully correlated active-composition and strategic-owner snapshots where the current producer is feature-gated or diagnostic-only.

Unavailable values must not become zero, neutral posture, empty-but-complete collections, synthetic IDs or fabricated HOLD candidates.

### 3.4 Actor/Critic ownership

The first-lineage semantic decisions already established must be preserved:
- shared factual state/evidence is eligible for both Actor and Critic only after source, provenance, validity and decision correlation are proven;
- raw 9×37 inventory-fit and 100×37 recipe-fit matrices remain Actor-specific conditional action-scoring inputs initially;
- any Critic summary of compatibility evidence needs its own formula/version and must derive from the same validated facts;
- the exact same decision-correlated native masks are supplied separately to Actor and Critic;
- untyped AntiLoopEngine history and untyped action-memory scalars are deferred from the initial Critic;
- TFT Strategic Engine recommendations, evaluator rankings/scores/confidence, baseline recommendations and executor resolutions remain diagnostic-only, not PPO inputs, reward labels or imitation targets.

The current implementation does not yet conform: the Critic ignores masks, and TFT Strategic Engine context is not delivered as a structured PPO input.

### 3.5 Semantic separation and legacy removal

The projection must not recreate the legacy strategy enum or its fixed rules. Keep distinct:
- strategic direction/commitment;
- active composition;
- pivot candidate/transition;
- economic posture;
- economic progression;
- factual owned-unit/copy/star evidence;
- derived unit assessments and item/recipe compatibility;
- action candidates versus PPO action space.

A planner proposal, recommendation or heuristic score must not silently become an observed fact or learning target. Legacy feature migration must be mapped feature-by-feature to a validated new source or explicit retirement.

### 3.6 Checkpoint and reward lineage

The first-lineage checkpoint identity must bind, at minimum, the observation schema, projection manifest, feature order, encoder/heads, action contract, mask contract, reward/temporal attribution contract and relevant catalog fingerprints. Structural tensor loadability is not semantic compatibility.

The Reward Contract is documented, but its runtime migration and calibrated numeric coefficients are not accepted by this Stage 0 review. Stage 0 should identify the reward contract/version dependency without inventing coefficients or beginning reward changes.

## 4. Required Stage 0 deliverables

Before the Stage 0 exit review, produce:

1. A revised machine-readable projection manifest with an explicit encoding-contract section for every feature eligible for the first lineage.
2. An explicit inclusion/exclusion table separating semantic fields from actual tensor features, control metadata, diagnostics and unavailable fields.
3. A deterministic ordering/cardinality policy for every entity and relation family, including empty versus missing and collection completeness.
4. A versioned identity and observation/mask correlation payload specification with canonicalization/hash inputs and rejection rules.
5. A complete Actor/Critic/action-head consumer map, including the separate mask inputs.
6. A projection architecture proposal only after the preceding items are complete; compare structured/set, spatial and global/context encodings against the actual semantic families rather than inheriting legacy offsets.
7. Positive and negative fixtures covering observed zero, missing, unknown, partial, stale, incompatible schema/catalog, changed sequence, empty collections, overflow and mismatched masks.
8. A compatibility matrix connecting schema, projection, action/mask, reward, architecture, catalog and checkpoint lineage.

## 5. Stage 0 exit checklist

- [ ] All 77 semantic entries retain stable IDs and explicit dispositions.
- [ ] Every projected feature has a complete encoding, source, provenance, validity, normalization and consumer contract.
- [ ] Every non-projected field has a reason and cannot leak into the model through a default.
- [ ] Entity ordering, cardinality, padding and overflow behavior are deterministic and tested.
- [ ] Observation and masks are bound to one exact decision identity; stale/mismatched payload behavior is specified.
- [ ] Actor and Critic receive the same exact masks as separate side inputs.
- [ ] Action-head-specific conditioning is distinguished from general Actor/Critic state.
- [ ] Recommendation/evaluator/executor outputs are excluded from PPO inputs and targets.
- [ ] Checkpoint compatibility is semantic and immutable-lineage aware.
- [ ] JSON/schema/manifest validation and positive/negative fixtures pass.
- [ ] Domain owner explicitly approves the complete Stage 0 package.

## 6. Implementation boundary after review

After Stage 0 approval, implementation follows the dependency-ordered roadmap:
1. Stage 1: native identity and atomic observation/mask decision snapshot (#293/#294, with #346 producer evidence).
2. Stage 2: structured factual producers and TFT Strategic Engine integration (#346, #283, #291, #282, #284, #281).
3. Stage 3: Python transport and rollout identity.
4. Stage 4: approved PPO projection and checkpoint implementation (#286/#288).
5. Stage 5: reward migration and legacy consumer isolation (#287/#290/#285).
6. Stage 6: Viewer, integrated replay and evaluation (#292/#289/#295).
7. Stage 7: Overwolf/GEP live integration, deferred as agreed.

No stage may invent missing producers or bypass the upstream contract. A downstream issue stops when its evidence prerequisite is not met.

## 7. Architecture reconstruction review

1. **Prior problem:** the existing 77-entry inventory described semantic candidates and consumer intent but did not provide a complete per-feature encoding contract or an integrated review of the remaining producer and decision-correlation blockers.
2. **Technical rationale:** tensor construction must be deterministic and semantically reproducible; guessed normalization, ordering, missingness or identity can train PPO on inconsistent states and make checkpoints impossible to evaluate reliably.
3. **New responsibility:** this review owns Stage 0 gap identification and exit criteria; the projection manifest owns feature encoding; schema owns semantic meaning; source owners own evidence; Action/Mask owns legality; PPO owns consumption and learning.
4. **Contract and invariants:** no fabricated values/identities/candidates, no legacy offset inheritance, no recommendation imitation, no mask substitution, and no runtime implementation before explicit Stage 0 acceptance.
5. **Cross-component impacts:** Schema v2, source/entity manifests, TFT Engine, TFT Strategic Engine, pybind, Python wrapper/vector environment, Trainer/RolloutBuffer, Actor/Critic, action heads, reward lineage, checkpoints, replay and evaluation.
6. **Objective validation:** all 77 semantic fields reconciled; 223 schema paths referenced by the current crosswalk; all known producer and correlation gaps explicitly retained; no runtime source changed.

