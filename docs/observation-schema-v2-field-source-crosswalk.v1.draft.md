# Observation Schema v2 Field-to-Source Crosswalk v1 — Draft

**Status:** generated schema/source-map reconciliation; field-level producer audit remains incomplete.  
**Base:** `new-arquiteture`.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).

## 1. Purpose

The structured-entity coverage matrix tracks producer field families. This crosswalk performs a separate, reproducible reconciliation between the current Schema v2 declarations and the 77-entry Schema v1 source map.

It expands the Schema v2 data paths under:
- `entities`
- `derived_context`
- `strategic_evidence`
- `legal_state_context`

The result is a machine-readable CSV with one row per schema data path. Shared `field` envelopes are treated as reusable contract definitions rather than counted repeatedly as independent semantic source fields.

- [Machine-readable field/source crosswalk](../spec/observation-schema-v2-field-source-crosswalk.v1.draft.csv)
- [Producer field-family coverage matrix](../spec/observation-structured-entity-producer-coverage.v1.draft.csv)
- [Schema v2](../spec/observation-schema.v2.draft.json)
- [77-entry source map](../spec/observation-schema.v1.source-map.json)

## 2. Reconciliation result


- 223 Schema v2 data paths enumerated across the four roots.
- 43 exact path matches to the source map.
- 164 paths mapped only through an ancestor/family entry.
- 16 paths have no source-map entry.
- The CSV carries 14 columns, including schema path/type/required status, source-map match, inherited availability/nature/source/formula/notes, field-level proof status, Python/PPO delivery status and next action.

**Important:** an ancestor/family match is not field-level producer proof. An exact source-map match is also not sufficient by itself; callsite, provenance, sequence, Python exposure and PPO delivery still need verification. The source map is an inventory, not a runtime schema validator.

## 3. Field-level reconciliation progress — 2026-11-14

The first source-backed field-level pass is now recorded in the CSV for 31 paths covering board, bench, shop, loose components and completed-item inventory. A separate disposition pass records all 16 paths that had no source-map entry. These are dispositions, not claims that all such fields are runtime-produced.

Current crosswalk status after these passes:
- 223 total Schema v2 data paths.
- 31 board/bench/shop/component/inventory paths have field-level producer and delivery dispositions.
- 19 additional combat-stat, anvil, unit-role, item-fit and recipe-fit paths have field-level dispositions.
- 16 previously unmapped paths have explicit source-backed dispositions (including not-produced, Shadow-only, diagnostic-only, unverified and static contract metadata).
- 43 exact source-map matches still require callsite/provenance/sequence/Python/PPO validation.
- 114 ancestor-only paths still require nested field-level proof.

The 31 unit/item pass deliberately distinguishes diagnostic snapshot delivery from PPO delivery. Structured UUID/champion/item identifiers in the audit snapshot are not treated as PPO tensor inputs. The 16 unmapped dispositions preserve unavailable/not-produced distinctions rather than manufacturing data.

Next work: continue the remaining 63 ancestor-only paths and validate the 43 exact matches at callsite level, then trace Python/vector-environment/rollout-buffer/Actor/Critic delivery. Issue #346 remains open.

### Additional field-level proof — 2026-11-15

The [Item Fit, Anvil and Unit Role Field Proof](observation-schema-v2-item-fit-anvil-role-field-proof.v1.draft.md) reconciles 19 further paths. It distinguishes:
- selected combat-stat features from a complete per-unit `combat_stats{}` map;
- ItemEngine's anvil queue API and TftEngine's conditional option consumer from an actual gameplay grant producer (none found in the audited TftEngine path);
- positional option IDs and aggregate anvil fit from stable option identity and per-target fit records;
- slot-aligned role/item/recipe feature matrices from typed unit, item, recipe and target identities.

Cumulative ancestor-path progress: 101 of 164 ancestor-mapped paths now have field-level dispositions; 63 remain. The 43 exact matches and 16 no-match paths are unchanged. This is a documentation audit, not an Actor/Critic leaf-delivery proof.

### Strategic evidence field-level proof — 2026-11-15

The [Strategic Evidence Field Proof](observation-schema-v2-strategic-evidence-field-proof.v1.draft.md) reconciles 31 additional paths across priorities, owned-unit assessments, anchor candidates and candidate-generation diagnostics.

Cumulative ancestor-path progress is now 81 of 164 paths with field-level dispositions; 83 remain. The audit preserves champion-keyed versus physical-unit identity, distinguishes per-slot in-memory assessment from diagnostic serialization, and flags zero-initialized rejection counters as defaults rather than measured zero values. Shadow evidence and PlayerInfo diagnostic fields are not PPO inputs.

### Strategic owner snapshot field proof — 2026-11-15

The [Strategic Owner Snapshot Field Proof](observation-schema-v2-strategic-owner-snapshot-field-proof.v1.draft.md) audits all 20 paths for StrategicPlanner commitment, Composition Intelligence and UnifiedStrategicStateMachine. The owners expose separate internal state and diagnostic artifacts, but no single common owner-snapshot envelope. Diagnostic emission/player sequences are not source decision sequences; phase, status, stale reason and transition reason remain distinct.

Cumulative ancestor-path progress: 101 of 164 paths now have field-level dispositions; 63 remain. No synthetic owner ID, payload path or decision sequence is introduced.

## 4. The 16 paths without a source-map entry

| Schema path | Why it needs an explicit disposition |
|---|---|
| `derived_context.action_opportunity.status` | Parent candidate collection has an empty source vector; status must distinguish not-produced from valid empty |
| `derived_context.action_opportunity.source_sequence` | No authoritative candidate set/sequence in the audited call path |
| `derived_context.action_opportunity.reason` | Requires producer-owned reason semantics, not a DTO default |
| `derived_context.decision_history.status` | Flat action memory exists; typed history collection does not |
| `derived_context.decision_history.source_decision_sequence` | No per-event decision sequence is delivered |
| `derived_context.decision_history.reason` | Requires explicit unavailable/partial reason producer |
| `strategic_evidence.composition_hypotheses[].hypothesis_id` | Exploratory direction hypotheses have no stable candidate/hypothesis ID contract |
| `strategic_evidence.composition_hypotheses[].direction_id` | Must distinguish direction identity from active composition and pivot identity |
| `strategic_evidence.composition_hypotheses[].composition_id` | Hypothesis-to-composition relation and lifecycle need source proof |
| `strategic_evidence.composition_hypotheses[].anchor_id` | Anchor candidate identity is not stable and cannot be inferred from composition identity |
| `strategic_evidence.composition_hypotheses[].evidence[]` | Evidence vocabulary/provenance and completeness are not represented in the source map |
| `strategic_evidence.composition_hypotheses[].quality` | Quality/confidence semantics and formula calibration need a producer contract |
| `legal_state_context.status` | Parent legal-state status and reason semantics need a source-owned completeness contract |
| `legal_state_context.source_decision_sequence` | No common legal-state decision sequence is established by the current anti-loop record model |
| `legal_state_context.reason` | Requires explicit status reason, not an inferred default |
| `legal_state_context.description` | Descriptive metadata has no audited runtime producer contract |

These are **unmapped in the current source-map artifact**, not automatically proven absent from the Engine. Each requires a source-backed classification or an explicit statement that it is contract metadata only.

## 5. How to read the match classification

- `exact`: the schema path equals a source-map field. Still requires source callsite and delivery verification.
- `ancestor`: the path inherits a broader source-map family entry. The inherited availability is contextual only; the nested field is not proven by the parent row.
- `descendant`: a narrower source-map field is the nearest mapping for a broader schema path.
- `none`: no source-map path matches; the field needs a new mapping or explicit unavailable/unverified disposition.

The CSV intentionally sets Python and PPO delivery to `not_established_by_source_map` for every row. Delivery is not inferred from source-map intended-consumer text.

## 6. Required next work

1. Audit the 16 unmapped paths against exact Engine/Shadow producers and classify them as observed, derived, Shadow-only, diagnostic-only, not-produced, not-correlated or metadata-only.
2. Review all 164 ancestor-mapped paths and determine whether the nested schema property is actually produced; do not inherit parent availability automatically.
3. For all 43 exact matches, trace callsite, formula/version, identity, source sequence, reset, Python binding and PPO rollout independently.
4. Reconcile schema-required identities with the correction proposal: raw UUID, unit assessment references, anchor candidate IDs, anvil option IDs, unit-role and item-target-fit targets.
5. Extend replay/acceptance criteria only after producers and sequence scopes are proven.

## 7. Architecture reconstruction review

1. **Prior problem:** the 77-entry source map did not expose which individual Schema v2 nested data paths were exact matches, broad family inheritance or entirely unmapped.
2. **Technical justification:** broad family matches can conceal unsupported child fields; an unmapped field can be a missing producer, a contract-only field or an incomplete source map, and those cases must not be conflated.
3. **New responsibility:** this crosswalk owns mechanical schema-path-to-source-map reconciliation; it does not claim native producer proof or PPO delivery.
4. **Contract/invariants:** 223 data paths; exact/ancestor/descendant/none distinctions; inherited availability is not field proof; no delivery claims inferred from intended consumers.
5. **Cross-component impacts:** Schema v2, source map v1, structured entity contract, strategic evidence, action opportunity, legal-state/anti-loop, Python binding, PPO rollout and replay.
6. **Objective validation:** schema traversal and source-map matching produced 223 unique paths: 43 exact, 164 ancestor, 16 none; 14-column CSV; documentation/specification only, no runtime or tensor-layout changes.

Issue #346 remains open until every path has a source-backed disposition and identity/sequence/delivery proof.


## Unmapped field dispositions — 2026-11-15

The [Schema v2 Unmapped Field Dispositions](observation-schema-v2-unmapped-field-dispositions.v1.draft.md) classifies all 16 paths without a source-map match as not-produced, Shadow-only, diagnostic-only, unverified, not-correlated or static contract metadata. This classification supplements but does not rewrite the mechanical match result.
