# Schema v2 Strategic Evidence Field Proof v1 — Draft

**Status:** source-backed partial field audit; Shadow/diagnostic only, not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope

This slice reconciles 31 Schema v2 paths across:
- strategic unit priorities (2);
- owned-unit assessments (5);
- generated anchor candidates (13);
- candidate-generation diagnostics (11).

It does not cover the separate `owner_snapshots` object, commitment-context exact matches, progression/pressure/uncertainty, or the composition-hypothesis fields already classified in the unmapped-path disposition. Those remain separate audit work.

## 2. Source-backed producer findings

### 2.1 Priority rows are champion-keyed Shadow intentions

`UnitPriorityPlanner::resolve` builds a `UnitPrioritySnapshot` containing `UnitPriority` rows for target composition units, missing target units and other owned champion IDs. Its lookup maps are keyed by `champion_id`; it does not retain a UnitInstance UUID or slot reference. Each row has integer `priority`, tier, confidence, contributions and reason codes. Confidence is explicitly documented as not a probability. The diagnostic recorder serializes rows as `unit_intentions[]` with `champion_id`, `priority`, confidence and supporting fields (`UnitPriorityPlanner.hpp:99-107,113-230`; `CompositionDiagnostics.hpp:133-151`).

This is a useful champion-level Shadow intention view, but it is not a physical-unit priority record. The diagnostic JSONL endpoint is exposed through pybind; this path is not the PPO observation vector or an Actor/Critic input.

### 2.2 Owned-unit assessments are per-slot in memory but lack physical identity

Inside the Shadow-only block, `TftEngine.cpp` iterates occupied board and bench UnitInstances and constructs one `StrategicUnitCandidate` per occupied slot. It copies champion/catalog ID, champion key, cost, star, champion-aggregated copies, board/bench flags, core membership, heuristic board contribution, binary composition fit, equipped-item count fit, catalog traits and item-granted traits. It does not copy UUID or slot index into the candidate (`TftEngine.cpp:3250-3296`).

The formulas are explicit:
- `is_core`: champion ID occurs in the generated active direction's `unit_ids`;
- `board_contribution`: for board units, clamp(`0.5 * cost/5 + 0.5 * star/3`, 0, 1); bench units get 0;
- `composition_fit`: 1 only if the current direction string occurs in the champion's catalog trait list, otherwise 0;
- `item_fit`: clamp(`UnitInstance.items.size()/3`, 0, 1), not ItemFitCache compatibility.

`StrategicEvidenceContextBuilder` copies the records into `observed_units`, but that name does not turn derived values into observed facts. The builder attaches match/player/round/sequence to the parent context and records coarse provenance sources; it does not add per-field formula metadata or physical identity (`StrategicEvidenceContext.hpp:35-52,69-136`).

The separate Composition Intelligence priority pipeline aggregates owned units by champion ID, and its diagnostic `unit_intentions` rows also remain champion-keyed. These two views must not be conflated: the strategic context starts with one row per occupied board/bench slot but lacks UUID; UnitPrioritySnapshot aggregates by champion.

### 2.3 Anchor candidates are generated Shadow proposals, not physical-unit candidates

`NativeStrategicCompositionGenerator` creates candidate compositions from catalog definitions, aggregated owned copies, shop champion IDs, pool counts, trait thresholds, level and gold. Its candidate identity is the string `native:<direction>`; unit lists and main carry are champion internal IDs. The generator's score is heuristic, assembled from owned copies, pair/star progress, location, shop presence, role, pool, cost, affordability and contribution. It also records string evidence such as owned unit/pair, star progress and item fit (`NativeStrategicCompositionGenerator.hpp:81-210`).

`TftEngine.cpp` maps each generated composition into `StrategicAnchorCandidate`. It copies direction label, composition identity, candidate champion IDs, main-carry champion ID, completed traits, evidence strings, heuristic score, transition cost, reusable-owned count and shop availability. It computes contestation by summing star-copy counts for matching champion IDs on living opponents' board and bench. The DTO has no `candidate_id`, candidate revision, or candidate-set identity (`TftEngine.cpp:3300-3360`; `StrategicPlanning.hpp:73-86`).

The planner emits a partial diagnostic candidate view containing champion ID, direction label, score, acceptance/reason, composition identity, candidate champion IDs, main-carry champion ID, traits and evidence. It does not preserve all raw anchor fields in the diagnostic candidate row (`StrategicPlanner.hpp:220-260`; `TftEngine.cpp:4290-4298`; `tft_engine_bindings.cpp:448-456`).

Therefore, the schema's `anchor_unit_id`, `candidate_unit_ids` and `main_carry_id` cannot be interpreted as physical unit-instance references. Direction label and composition identity are also not a stable candidate ID/revision.

### 2.4 Candidate-generation diagnostics mix real counters and DTO defaults

The audited construction path sets:
- `anchors_considered` from `NativeCompositionGenerationResult.directions_considered` (trait directions considered, not individual anchor units);
- `candidates_generated` from the generated candidate vector size;
- `no_candidate_reason` from the generator result reason;
- `rejected_missing_champion_definition` only when the TftEngine anchor-definition guard rejects a generated candidate.

The `StrategicCandidateGenerationDiagnostics` DTO has no explicit `status` field. The audited construction path does not assign `rejected_cost_below_four`, `rejected_empty_trait`, `rejected_duplicate_direction`, `rejected_direction_limit`, `rejected_empty_plan`, or `rejected_anchor_not_in_plan`; these remain zero-initialized defaults in this path. They must not be interpreted as measured zero rejections (`StrategicPlanning.hpp:122-133`; `TftEngine.cpp:3300-3312,3420-3439`).

The resulting `PlayerInfo` diagnostics are copied through pybind as step-info fields. They are not appended to `build_observations()` and are not PPO features (`tft_engine_bindings.cpp:324-344,448-487`; `TftEngine.cpp:1274-1285`).

## 3. Field-level dispositions

| Schema path | Native producer/evidence | Diagnostic/Python surface | PPO delivery | Disposition |
|---|---|---|---|---|
| `strategic_evidence.priorities[].entity_id` | UnitPriority rows keyed by champion ID | `unit_intentions[].champion_id` | None | `champion_keyed_priority_identity` |
| `strategic_evidence.priorities[].priority` | UnitPriorityPlanner integer tier/heuristic priority | `unit_intentions[].priority` | None | `shadow_heuristic_integer_priority` |
| `strategic_evidence.owned_unit_assessments[].unit_instance_id` | StrategicUnitCandidate has no UUID or slot | No UUID in this assessment record | None | `not_produced_physical_identity` |
| `strategic_evidence.owned_unit_assessments[].is_core` | Membership in active generated candidate champion IDs | Shadow context only | None | `shadow_derived_core_membership` |
| `strategic_evidence.owned_unit_assessments[].board_contribution` | Cost/star heuristic; board-only | Shadow context only | None | `shadow_derived_cost_star_heuristic` |
| `strategic_evidence.owned_unit_assessments[].composition_fit` | Binary direction-string/catalog-trait match | Shadow context only | None | `shadow_derived_binary_trait_match` |
| `strategic_evidence.owned_unit_assessments[].item_fit` | Equipped-item count divided by three | Shadow context only | None | `shadow_derived_equipped_item_count` |
| `strategic_evidence.anchor_candidates[].candidate_id` | No candidate ID/revision/set ID in DTO | Partial planner diagnostics only | None | `not_produced_stable_candidate_identity` |
| `strategic_evidence.anchor_candidates[].direction_id` | Target direction string | Diagnostic target-direction label | None | `derived_direction_label_not_stable_id` |
| `strategic_evidence.anchor_candidates[].composition_id` | Generator identity `native:<direction>` | Partial diagnostic composition identity | None | `generated_composition_identity` |
| `strategic_evidence.anchor_candidates[].anchor_unit_id` | Anchor champion internal ID | Diagnostic champion ID | None | `champion_catalog_id_not_physical_unit` |
| `strategic_evidence.anchor_candidates[].candidate_unit_ids` | Generated lineup champion-ID vector | Diagnostic champion-ID vector | None | `generated_champion_id_list` |
| `strategic_evidence.anchor_candidates[].main_carry_id` | Generated main-carry champion ID | Diagnostic main-carry ID | None | `generated_main_carry_champion_id` |
| `strategic_evidence.anchor_candidates[].candidate_traits` | Generated completed catalog traits | Diagnostic trait strings | None | `generated_completed_trait_list` |
| `strategic_evidence.anchor_candidates[].evidence[]` | Generator string evidence | Diagnostic evidence strings | None | `generated_evidence_strings` |
| `strategic_evidence.anchor_candidates[].anchor_value` | Generator heuristic candidate score | Partial combined planner score | None | `native_generator_heuristic_score` |
| `strategic_evidence.anchor_candidates[].transition_cost` | Generator heuristic transition estimate | Not preserved per candidate in complete form | None | `native_generator_heuristic_cost` |
| `strategic_evidence.anchor_candidates[].contestation` | Opponent board/bench star-copy aggregate | Not preserved per candidate in complete form | None | `opponent_copy_aggregate` |
| `strategic_evidence.anchor_candidates[].reusable_owned_units` | Candidate unit IDs matched against aggregated owned copies | Not preserved per candidate in complete form | None | `native_generator_owned_unit_count` |
| `strategic_evidence.anchor_candidates[].shop_available` | Current shop champion-ID presence | Not preserved per candidate in complete form | None | `native_generator_anchor_shop_presence` |
| `strategic_evidence.candidate_generation.status` | No status member in diagnostics DTO | No status field | None | `not_produced_explicit_status` |
| `strategic_evidence.candidate_generation.anchors_considered` | Generator directions-considered counter | PlayerInfo step-info field | None | `native_generator_directions_considered` |
| `strategic_evidence.candidate_generation.candidates_generated` | Generated candidate vector size | PlayerInfo step-info field | None | `native_generator_candidate_vector_size` |
| `strategic_evidence.candidate_generation.rejected_cost_below_four` | No assignment in audited construction path | Zero-initialized DTO/step-info field | None | `dto_default_zero_no_producer` |
| `strategic_evidence.candidate_generation.rejected_missing_champion_definition` | TftEngine anchor-definition guard | PlayerInfo step-info field | None | `tft_anchor_definition_guard_counter` |
| `strategic_evidence.candidate_generation.rejected_empty_trait` | No assignment in audited construction path | Zero-initialized DTO/step-info field | None | `dto_default_zero_no_producer` |
| `strategic_evidence.candidate_generation.rejected_duplicate_direction` | No assignment in audited construction path | Zero-initialized DTO/step-info field | None | `dto_default_zero_no_producer` |
| `strategic_evidence.candidate_generation.rejected_direction_limit` | No assignment in audited construction path | Zero-initialized DTO/step-info field | None | `dto_default_zero_no_producer` |
| `strategic_evidence.candidate_generation.rejected_empty_plan` | No assignment in audited construction path | Zero-initialized DTO/step-info field | None | `dto_default_zero_no_producer` |
| `strategic_evidence.candidate_generation.rejected_anchor_not_in_plan` | No assignment in audited construction path | Zero-initialized DTO/step-info field | None | `dto_default_zero_no_producer` |
| `strategic_evidence.candidate_generation.no_candidate_reason` | Native generator reason string | PlayerInfo step-info field | None | `native_generator_reason_string` |

## 4. Non-equivalences and invariants

1. Champion ID is a catalog key, not a physical unit identity.
2. A per-slot in-memory candidate without UUID is not a stable physical-unit assessment.
3. Champion-aggregated UnitPriority rows are not per-instance priorities.
4. A direction label or composition identity is not a stable anchor candidate ID/revision.
5. Heuristic score, confidence and priority are not calibrated probabilities.
6. Zero-initialized rejection counters are not observed zero counts.
7. A PlayerInfo/diagnostic JSON field is not a PPO observation feature.
8. Strategic evidence and candidate generation remain Shadow-only; no output here becomes PPO label/target.

## 5. Remaining proof

- Audit the 20 `strategic_evidence.owner_snapshots.*` paths against actual owner-specific snapshots and diagnostic sidecars.
- Audit the 23 exact strategic paths under progression, pressure, uncertainty, commitment context, completed traits and focus weights.
- Determine whether a stable candidate-set/revision identity is needed in addition to the parent StrategicEvidenceContext sequence.
- Reconcile the seven rejection diagnostics that currently remain DTO defaults or guard-only values; do not silently serialize defaults as observed zero.
- Trace the pybind step-info and composition-diagnostics endpoints through the Python wrapper and confirm no path leaks into Trainer observations, rollout storage or policy inputs.
- Continue the separate Actor/Critic field-consumer audit; this document makes no leaf-allocation claim.

Issue #346 remains open. No runtime/schema/tensor/PPO/reward/mask/training/checkpoint/Viewer changes are made by this audit.

## 6. Architecture reconstruction review

1. **Prior problem:** Schema v2 treated champion-keyed priorities, per-slot Shadow assessments, generated candidates and diagnostic counters as if they were one complete structured strategic-evidence entity family.
2. **Technical justification:** those records have different identity levels, formulas, owners, completeness and delivery channels; zero defaults and parent sequences cannot substitute for field-specific evidence.
3. **New responsibility:** this audit owns field-level producer/delivery classification for priorities, owned-unit assessments, anchor candidates and candidate-generation diagnostics.
4. **Contract and invariants:** champion IDs are never physical UUIDs; no synthetic candidate IDs; heuristic scores are not probabilities; absent status and default counters remain explicit gaps; Shadow diagnostics are not PPO inputs.
5. **Cross-component impacts:** TftEngine strategic context, NativeStrategicCompositionGenerator, StrategicEvidenceContextBuilder, StrategicPlanner, UnitPriorityPlanner, CompositionDiagnosticRecorder, PlayerInfo, pybind, Python wrapper, PPO observation and rollout.
6. **Objective validation:** 31 schema paths enumerated once and reconciled against native construction, planner, diagnostic serialization and pybind source; no runtime or tensor-layout changes.

