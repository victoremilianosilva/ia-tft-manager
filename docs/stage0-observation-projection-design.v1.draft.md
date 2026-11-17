# Stage 0 — Observation Projection Design v1

**Status:** first Stage 0 proposal; pending domain-owner review.  
**Canonical architecture:** TFT Strategic Engine.  
**Machine-readable inventory:** `spec/observation-projection-manifest.v1.draft.json`.  
**Base branch:** `new-arquiteture`.

## 1. Purpose

The prior work established a semantic Observation Schema, a source map, a legacy feature crosswalk and a proposed Actor/Critic consumer matrix. Those artifacts did not yet define a concrete, versioned representation for the first new PPO lineage.

This Stage 0 package turns the 77-field semantic consumer matrix into a machine-readable projection inventory and groups the eligible evidence into explicit model-input families. It is the first design baseline, not runtime implementation and not yet a frozen tensor layout.

## 2. Architecture naming and authority

The canonical strategic-intelligence architecture is now named **TFT Strategic Engine**. It is the main strategic system and contains multiple specialized engines/managers. The former “Shadow” label is retired as an architecture name.

- **TFT Engine:** factual game simulation/state, native rules, action validation and final legality.
- **TFT Strategic Engine:** strategic intelligence and its specialized engines, including direction/commitment, active composition, economy, unit/item intelligence, pivot, positioning and action evaluation.
- **PPO:** policy learning and action selection from the validated observation/context representation.
- **Observation Projection:** deterministic transformation from the correlated semantic snapshot into Actor/Critic inputs.
- **Viewer/diagnostics:** read-only inspection; no strategic authority.

Legacy C++ identifiers, historical audit filenames, schema paths and serialized keys containing `Shadow` are not silently renamed in this package. They remain traceable until a dedicated compatibility/migration change can update code and persisted formats safely. In new documentation and new APIs, use **TFT Strategic Engine**. The historical schema field `shadow_recommendations` remains a stable diagnostic-only path until a versioned schema migration changes it.

The PPO must not copy TFT Strategic Engine recommendations. It consumes validated factual and owner-produced strategic evidence as context, then learns its own policy. Recommendation scores, rankings, confidence, baseline proposals and executor resolutions remain diagnostic-only.

## 3. What the machine-readable inventory contains

The JSON manifest includes all 77 entries from the existing semantic consumer matrix, preserving their stable feature IDs, semantic paths, current source, availability, nature, unit, target disposition, consumers and blockers.

Current disposition totals:

| Disposition | Count | Treatment |
|---|---:|---|
| Shared Actor/Critic candidate | 34 | Eligible semantic inputs after producer, provenance, identity and encoding gates |
| Unavailable | 17 | Not projected until an authoritative producer exists |
| Control metadata only | 7 | Validation/correlation/checkpoint/replay metadata, never neural scalar features |
| Diagnostic only | 9 | Excluded from Actor, Critic, reward targets and imitation labels |
| Unresolved | 5 | Withheld pending semantic/producer resolution |
| Critic-only candidate | 5 | Deferred from the initial lineage; not included until typed history, reset/replay proof and ablation |

The counts are dispositions, not a claim that all 34 shared candidates are already delivered to PPO. Availability and blocking conditions remain attached to each entry.

## 4. Initial projection groups

The manifest defines semantic groups for:

1. Player lifecycle and state.
2. Board physical-unit entities.
3. Bench physical-unit entities.
4. Shop opportunity entities.
5. Item, component, recipe and anvil context.
6. Economic context.
7. Positioning and per-unit role evidence.
8. Capacity and trait context.
9. Item/recipe-to-unit compatibility.
10. Decision-local action count and movement-age context.
11. Strategic direction and active-composition commitment.
12. Owned-unit assessments and anchor-candidate evidence.
13. Candidate-generation status.
14. Decision identity and mask-correlation metadata.

These are semantic input families, not a decision to flatten all data into one vector. The first lineage should preserve entity and relation structure until a reviewed encoder projection specifies how each family is represented.

### Entity cardinality and ordering

- Board: 28 stable slots; never compact empty slots.
- Bench: 9 stable slots; never compact empty slots.
- Shop: 5 stable slots; each offer is a temporary opportunity, not an owned copy. A stable offer identity/revision producer is still missing.
- Items/components/recipes/traits: catalog-bound sets with explicit collection completeness and deterministic ordering. Do not invent physical item-instance IDs where the Engine currently stores catalog IDs.
- Candidate sets: variable cardinality with explicit completeness and stable candidate-set identity. The action-opportunity producer is currently absent; do not synthesize a HOLD candidate from an empty collection.
- Spatial features: preserve unit and slot identity. Do not treat the legacy 4×7 array as canonical TFT hex geometry without validating coordinate/orientation semantics.

## 5. Actor, Critic and action-mask design

- Shared semantic state candidates may feed both Actor and Critic only when they refer to the same validated decision snapshot.
- Actor-specific conditional action scoring remains separate from general state encoding.
- The raw 9×37 inventory-fit and 100×37 recipe-fit matrices remain Actor-specific in the initial lineage. The Critic does not receive those raw matrices.
- Any Critic compatibility summary must be separately specified, formula-versioned and derived from the same validated item/component and unit-target evidence.
- The Critic receives the exact same decision-correlated native action masks as the Actor, through a separate side input. Masks are not flattened into observation features and are not a substitute for strategic context.
- AntiLoopEngine history and untyped action memory are deferred from the initial Critic. The five matrix entries currently marked critic-only are explicitly deferred until typed event identity, source sequence, reset semantics, replay fixtures and a controlled ablation exist.
- The native TFT Engine remains final legality authority. A policy proposal never bypasses Engine validation.

## 6. Identity and validity rules

Every projected value must be bound to the same:
- logical game match;
- Engine-instance + episode scope;
- player seat;
- round/state;
- decision identity;
- source sequence and, where applicable, catalog fingerprint.

Observation and mask payloads must carry the same decision identity. A mismatch or stale sequence is rejected before Actor sampling or Critic evaluation.

The projection preserves:
- observed vs derived vs estimated vs inferred nature;
- valid, partial, missing, unknown, not-applicable, stale and incompatible states;
- explicit reason and provenance;
- physical unit identity vs champion catalog identity;
- owned unit vs shop opportunity vs shared-pool availability.

Numeric zero is a valid value only when the source explicitly observed/derived zero. DTO defaults are not evidence.

## 7. Decisions intentionally not frozen yet

This proposal does not invent or freeze:
- scalar normalization constants or training-fit statistics;
- categorical vocabulary indexes;
- entity embedding widths;
- exact tensor axes, dimensions, padding/truncation or overflow limits for variable collections;
- spatial encoder topology or canonical hex coordinates;
- Critic summaries of Actor-specific compatibility data;
- heuristic calibration for board power, positioning, roles, item/recipe fit or anchor estimates;
- action candidate cardinality until the authoritative producer exists.

These are explicit Stage 0 review items. Encoder architecture and PPO dimensions must be selected only after the complete feature manifest and source/validity contracts are accepted. Do not copy the legacy tensor offsets or dimensions.

## 8. Stage 0 completion criteria

Stage 0 is complete only when the domain owner approves:

1. The full 77-entry feature inventory and its dispositions.
2. The exact v2 identity and observation/mask correlation contract.
3. The semantic group representation, entity cardinality and ordering rules.
4. The complete per-feature provenance, status, unit, formula and normalization specification.
5. The exact Actor/Critic consumer map and separate mask side-input contract.
6. The unresolved producer list and explicit no-default behavior.
7. The resulting tensor shapes/axes/embedding widths and deterministic projection hashes.
8. Positive and negative fixtures for valid, zero, partial, missing, unknown, stale, incompatible, changed catalog and changed sequence inputs.

Only after this package is reviewed and approved may Stage 1 native runtime implementation begin. PPO runtime implementation remains later, after Stage 4 prerequisites.

## 9. Architecture reconstruction review

1. **Prior problem:** the semantic schema and consumer matrix identified candidate inputs but did not provide a single machine-readable inventory tying feature identity, source availability, consumer disposition and initial treatment together.
2. **Technical rationale:** PPO cannot safely learn from ambiguous, stale, synthetic-default or semantically conflated values. Actor/Critic differences and mask correlation must be explicit.
3. **New responsibility:** the projection manifest owns the feature inventory and projection-group mapping; Observation Schema owns semantic meaning; TFT Strategic Engine owners produce strategic evidence; Action/Mask owns exact masks; PPO owns model consumption and learning.
4. **Contract and invariants:** no recommendation imitation, no invented producer, no zero-as-missing, no identity namespace conflation, no mask substitution, and no legacy layout inheritance.
5. **Cross-component impacts:** schema, native Engine, TFT Strategic Engine, pybind/wrapper/rollout, Actor/Critic, action heads, checkpoint lineage, replay and evaluation.
6. **Objective validation:** manifest generated from the existing 77-field consumer matrix; all 77 feature IDs retained; disposition counts match 34/17/7/9/5/5; machine-readable JSON parses; no runtime source changed.
