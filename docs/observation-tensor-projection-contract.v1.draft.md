# Observation Tensor Projection Contract v1 — Design Requirements

**Status:** draft design requirements; no concrete tensor projection or encoder architecture is approved.  
**Scope:** documentary contract only. Runtime projection, PPO, Engine, masks, rewards, training, Viewer, and checkpoints remain unchanged until Gate 8 and explicit authorization.  
**Depends on:** Observation Schema v1, Action / Mask Contract v1, Reward Contract v1, Strategic Ownership and Integration Contract v1, and PPO Architecture and Checkpoint Contract v1.

## 1. Purpose and boundary

The Observation Schema defines semantic facts and evidence. It does not, by itself, define a tensor layout. The tensor projection is a separately versioned transformation from a validated semantic snapshot into explicitly typed model inputs.

This contract defines the information that a future concrete projection must specify and the evidence required to approve it. It deliberately does **not** select feature offsets, tensor dimensions, normalization constants, categorical vocabularies, encoder families, or actor/critic sharing.

The following existing artifacts have distinct roles:

- `observation-schema.v1.draft.json`: semantic snapshot schema and a projection identity/envelope.
- `observation-schema.v1.source-map.json`: current producer availability, provenance, units, and current-scale observations. It is not a tensor layout.
- `observation-schema.v1.migration-map.json`: semantic destination and disposition for legacy features. It is not a projection recipe.
- `observation-schema.v1.legacy-feature-map.json`: historical offsets and encodings for the audited legacy tensor only. It is not a target layout.
- `ppo-checkpoint-contract.v1.draft.md`: requires projection identity and deterministic feature/normalization manifests in checkpoint lineage.

The `schema.projection` object is an identity-bearing envelope attached to a snapshot. Its current `blocks` vocabulary is not a complete per-feature projection manifest: it does not yet require stable feature IDs, explicit per-feature normalization/missingness semantics, categorical vocabulary identity, temporal encoding, or an unambiguous actor/critic consumer map. Presence of this envelope must not be described as proof that a concrete projection has been designed.

## 2. Required projection manifest

A concrete projection proposal must provide a deterministic, machine-readable manifest. Every projected feature must declare:

| Attribute | Required meaning |
|---|---|
| `feature_id` | Stable semantic feature identity, independent of tensor offset and display name |
| `source_paths` | Exact Observation Schema paths; multiple paths require a documented derivation |
| `nature` | Observed, derived, estimated, or inferred; recommended/diagnostic outputs are not promoted to facts |
| `provenance_policy` | Required owner/source, formula/version where derived, catalog identity where relevant, and exact source-sequence correlation |
| `validity_policy` | Explicit behavior for valid, partial, missing, unknown, not-applicable, stale, and incompatible states |
| `unit` | Physical/game unit or explicit dimensionless meaning |
| `encoding` | Numeric, boolean, categorical, set/entity, spatial, relation, or temporal encoding with exact semantics |
| `normalization` | Formula, parameters, bounds/clipping, fit source, and immutable normalization ID; raw/unscaled must be explicit |
| `missingness_encoding` | How validity/status is represented separately from the value; zero is not an implicit missing sentinel |
| `catalog_binding` | Stable catalog ID/version/content hash/order hash for any categorical/entity vocabulary |
| `shape_and_order` | Exact shape, axis meanings, deterministic ordering rule, and offset only if the representation is a flat tensor |
| `cardinality_policy` | Fixed/variable cardinality, maximum or packing rule, padding/truncation behavior, length/presence mask, and overflow handling |
| `formula_identity` | Immutable formula ID/version and declared inputs for every derived or estimated feature |
| `consumers` | Exact consumer role(s): board/spatial encoder, entity/set encoder, global/context encoder, candidate encoder, actor, critic, or diagnostics |
| `availability` | Current producer availability and the behavior when the source is not produced; no default may be promoted to observed evidence |

The manifest must also declare projection-level `projection_id`, semantic version, deterministic canonicalization, dtype policy, ordered feature manifest hash, normalization manifest hash, formula manifest hash, output shapes, and projection hash. Hash scope must be explicit and exclude only the hash field itself and non-semantic editorial metadata.

A feature's semantic identity must not be derived from its offset. Reordering features, changing axes, changing a formula, changing normalization, changing vocabulary order, changing missingness behavior, or changing a consumer boundary changes projection identity even when output dimensions remain equal.

## 3. Semantic and provenance preservation

1. Preserve the distinction between observed, derived, estimated, and inferred values.
2. Preserve status and reason. Missing, unknown, stale, incompatible, and not-applicable are not interchangeable.
3. A valid numeric zero remains distinguishable from absent evidence.
4. A derived feature requires an explicit formula/version, input paths, units, validity rule, and provenance. Heuristic scores must not be represented as calibrated probabilities.
5. Correlated inputs must refer to the same match, player, decision identity, and source sequence. Stale or cross-episode values are rejected or explicitly marked unavailable; they are never silently carried forward.
6. Defaults in DTOs, constructors, or legacy serializers are not evidence. If a producer is absent, the projection emits the declared missing/unknown representation.
7. Do not infer flexible units, core traits, focus, progression, pressure, risk, or uncertainty from complements, ordering, enum defaults, or convenient zero values without an authoritative producer and documented formula.

## 4. Structured entities, catalogs, and ordering

Board units, bench units, shop offers, item instances, components, recipes, traits, and strategic candidates have different identity and cardinality semantics. A projection must not collapse them into one undifferentiated champion-ID count.

For each entity/set block, specify:
- entity identity and ownership domain;
- stable catalog identifiers and catalog fingerprints;
- slot/position identity where slot order is semantically meaningful;
- deterministic ordering where order is not inherently meaningful;
- set aggregation or padding/packing policy;
- presence/length masks and overflow behavior;
- relations (for example unit-to-item, unit-to-trait, candidate-to-evidence) without fabricating missing edges.

Champion ID may be a grouping key, but it is not a physical unit-instance identity. Shop offers are opportunities, not owned units. Unknown pool/shop availability must remain unknown rather than becoming zero.

Spatial layout must define board axes, coordinate origin, orientation, and the mapping between logical slot identity and tensor position. The legacy `4 × 7 × 5` board layout is historical evidence only and is not automatically normative.

Categorical IDs must use a stable, versioned vocabulary. Ordinal numeric encoding is forbidden unless the order itself has a documented semantic meaning. Any catalog order change updates the relevant fingerprint and projection identity.

## 5. Actor, critic, and mask boundary

The projection must map each feature to its intended consumer without assuming that every feature belongs in every network path.

- Actor inputs and critic/value inputs must be declared separately, including any shared blocks and their explicit sharing contract.
- The future critic receives the exact decision-correlated action masks (or a provably lossless encoding) as a separate side input, as required by Action / Mask Contract v1. Those masks are not replaced by a Markov-sufficient state/history representation and are not silently copied into the observation feature vector.
- Any additional critic state/history context is separately identified, sequenced, and versioned.
- Action masks retain their independent action/legality ownership. The Engine remains final legality authority.
- PPO may consume validated factual/evidence fields from canonical strategic, composition, unit, and economic owners as context.
- Shadow recommendations, evaluator scores/rankings/confidence, baseline recommendations, executor resolutions, and diagnostic-only Unified Strategic State Machine outputs are excluded from PPO observation features, labels, reward targets, and imitation losses.

A feature that is available only behind a diagnostic/Shadow feature flag must carry that availability condition. Its absence must not be silently substituted by a baseline recommendation or legacy alias.

## 6. Temporal and history representation

For every temporal feature, declare:
- event/decision/round time basis;
- source sequence namespace and correlation key;
- window or history horizon;
- ordering and truncation policy;
- reset/episode-boundary behavior;
- stale-data behavior;
- whether the feature is current evidence, accumulated history, or a derived summary.

Lobby, player, engine, Viewer session, and event sequence namespaces are not interchangeable. History must not cross match or episode boundaries unless the contract explicitly defines a persistent state and its identity.

## 7. Normalization and data leakage controls

Normalization is part of semantic projection identity, not an implementation detail.

- Declare units before normalization.
- Declare formula, parameters, clipping, and behavior outside expected ranges.
- If statistics are learned from data, record the exact training split/source and immutable statistics artifact; validation/test data must not fit or update normalization.
- Do not infer a normalization scale from current legacy code or a convenient maximum.
- Do not normalize categorical identifiers as continuous quantities.
- Keep validity/missingness separate from normalized values.
- Any change to normalization parameters or fit data changes the normalization manifest hash and projection hash.

## 8. Required review artifacts

A concrete proposal is not reviewable until it includes:

1. Machine-readable projection manifest with stable feature IDs and exact source paths.
2. Semantic-field → feature → tensor-block/axis/offset → actor/critic consumer crosswalk.
3. Per-feature provenance, status/missingness, units, formula, normalization, and catalog policy.
4. Entity/set and temporal/history encoding specifications.
5. Explicit actor/critic input map and separate exact-mask side-input map.
6. Deterministic canonicalization and hash-generation procedure.
7. Valid, missing, unknown, stale, incompatible, zero-valued, partial, and out-of-range fixtures.
8. Tests proving stable output and hashes across repeated runs and input object/map iteration order.
9. Negative tests proving that changed feature order, formula, normalization, catalog order, consumer mapping, or mask sequence changes identity or is rejected.
10. A coverage report showing every schema field is either projected, intentionally excluded with rationale, or diagnostic-only; no field is silently omitted.
11. A coverage report showing every projected feature has an authoritative source and a declared consumer.
12. An explicit list of unresolved producer gaps. Unavailable fields remain unavailable; a projection proposal cannot invent producers.

Only after this review may the projection be frozen and used to choose encoder dimensions and architecture ablations. Architecture selection remains subject to PPO Evaluation Protocol v1.

## 9. Current audit disposition

The current repository provides a strong semantic foundation and legacy migration evidence, but it does not yet provide the concrete target projection required by this contract:

| Artifact | What it establishes | What it does not establish |
|---|---|---|
| Observation Schema v1 | Typed semantic fields, identity, provenance, status, catalog references | Tensor feature list, offsets, normalization, model consumers |
| Source map (97 typed-field references) | Current source, availability, nature, units, current-scale notes, intended semantic consumer | Final tensor encoding or a guarantee that every source is runtime-valid |
| Legacy feature map (66 inventoried features) | Historical tensor blocks, offsets, encodings, legacy consumers | New-lineage offsets, feature order, or target architecture |
| Migration map (66/66 legacy features) | Preserve/rebuild/split/drop decisions and semantic destinations | Tensor layout or normalization parameters |
| Schema projection envelope | Projection identity, hash, dtype, blocks, shape/encoding hooks | Complete per-feature manifest and concrete projection approval |
| PPO checkpoint contract | Requires projection and normalization identities in lineage | A populated projection manifest |

**Disposition:** concrete tensor projection remains an open documentary dependency. Do not mark the projection approved, freeze PPO dimensions/encoder architecture, or claim Gate 1's semantic schema approval also approves tensor projection.

## 10. Architecture reconstruction review

1. **Prior problem:** the approved semantic schema and historical feature/migration maps could be mistaken for a complete target tensor projection. The schema's projection envelope did not require all per-feature encoding, normalization, missingness, catalog, temporal, and actor/critic consumer details.
2. **Technical rationale:** tensor shape compatibility does not establish semantic compatibility. The new lineage must preserve typed evidence and provenance while separating actor/critic inputs and exact action masks.
3. **New responsibility:** this document defines the minimum design and acceptance requirements for a concrete tensor projection. Observation Schema owns semantic meaning; the projection manifest owns tensor representation; PPO architecture owns encoder/actor/critic structure; Action / Mask owns masks and legality; checkpoint manifest records the complete identities.
4. **Contract and invariants:** no legacy offsets or encodings are inherited by default; every feature has stable identity, source, validity, unit, encoding, normalization, shape/order, and consumer; missingness is distinct from zero; masks remain separate; Shadow recommendations never become PPO targets.
5. **Cross-component impact:** Observation Schema and source/migration maps, PPO actor/critic, Action / Mask, Reward/GAE, checkpoint lineage, replay, and evaluation. Documentary only; no runtime wiring or architecture family is selected.
6. **Objective validation:** compared the machine-readable schema's projection envelope, 97-entry source map, 66-feature legacy map, 66/66 migration crosswalk, and PPO checkpoint requirements. Confirmed that these artifacts do not contain a populated target tensor layout. Concrete projection and executable validation remain pending.

