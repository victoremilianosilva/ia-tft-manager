# Schema v2 Item Fit, Anvil and Unit Role Field Proof v1 — Draft

**Status:** source-backed field-level audit; documentary only, not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope and prior gap

This slice audits 19 nested Schema v2 paths:
- the dynamic `combat_stats{}` child under board, bench and shop units;
- pending-anvil state and all declared option/target-fit fields;
- derived per-unit roles;
- inventory-item-to-unit fit;
- recipe-to-unit fit.

The prior crosswalk inherited availability from broad parent paths. That obscured whether the Engine emits a complete structured record, a partial flat feature projection, or only a conditional API path.

## 2. Evidence and producer boundaries

### 2.1 Combat statistics are partial projections, not complete maps

The PPO observation builder's board/bench unit target block selects role, board/bench location, star, composition fit, attack damage, attack speed, max HP, armor, magic resistance and equipped-item count (`cpp/src/lobby/TftEngine.cpp:1640-1674`). The shop block elsewhere emits occupancy, cost and role, with its strength slot intentionally zero (`cpp/src/lobby/TftEngine.cpp:1416-1427`).

The audit snapshot's per-unit record contains occupancy, champion ID, UUID, star, cost and item IDs; it does not serialize a per-unit combat-stat map (`cpp/src/lobby/TftEngine.cpp:6687-6700`; `cpp/bindings/tft_engine_bindings.cpp:807-815`). Therefore:
- board/bench `combat_stats{}` has selected catalog-derived numeric features, not a complete field map;
- shop `combat_stats{}` has no equivalent stats projection;
- the generic schema child does not identify a stable key set, source path, unit, or formula per dynamic entry.

### 2.2 Anvil API, conditional projection and live production are distinct

`ItemEngine` defines a pending anvil as a kind plus an ordered vector of catalog IDs. Its grant methods validate 1–9 unique known options and append to a queue; selection grants one catalog ID and consumes the queue head only on success (`cpp/include/items/ItemEngine.hpp:84-87,141-175,606-627`). The queue has no stable anvil ID, option ID, revision, or source decision sequence.

The Engine has a conditional action branch for selecting an anvil option (`cpp/src/lobby/TftEngine.cpp:5342-5356`). Its observation builder also emits pending/kind flags and up to the fixed option slots. Component choices become catalog-position one-hot features; completed items become ten selected normalized stat features; both use one aggregate best-fit feature normalized by 20 (`cpp/src/lobby/TftEngine.cpp:1546-1609`).

The read-only audit snapshot serializes pending flag, kind and ordered option IDs; pybind exposes them through `get_audit_snapshot` (`cpp/src/lobby/TftEngine.cpp:6750-6760`; `cpp/bindings/tft_engine_bindings.cpp:851-856`). Python exposes that snapshot as a separate observer method (`cpp_lobby_env.py:248-250`), while normal `reset` and `step` return the native observation vector (`cpp_lobby_env.py:120-127,129-145`).

**Critical boundary:** no call to `grant_component_anvil` or `grant_completed_item_anvil` exists in the audited `TftEngine.cpp` gameplay path. The ItemEngine API and conditional consumer/projection are real, but this audit does not establish an in-game producer that populates the queue. Consequently, the conditional PPO features must not be reported as operationally available in ordinary gameplay.

### 2.3 Unit roles are classifier outputs aligned to slots

The observation builder derives a role from `UnitCombatClassifier::classify` using base role, attack range, health, defenses, damage, attack speed, ability text, planned-carry identity and item stat contributions (`cpp/src/lobby/TftEngine.cpp:1315-1342`). Role values are projected into board/bench slot features and the item-target profile block (`cpp/src/lobby/TftEngine.cpp:1390-1414,1640-1674`).

No typed `unit_roles[]` array with `instance_id` and field envelope is emitted to Python or PPO. The flat role features are slot-aligned; they are not a physical-unit identity relation. The classifier output is a derived categorical role, not a calibrated probability.

### 2.4 Inventory item and recipe target fit are slot-indexed heuristic matrices

For each observation, the Engine builds unit profiles and resolves board/bench target slots through UUID lookup (`cpp/src/lobby/TftEngine.cpp:1556-1559,1680-1694`). For each of up to nine inventory positions, it computes fit against 37 board/bench target slots and emits `clamp(fit / 50, 0, 1)` (`cpp/src/lobby/TftEngine.cpp:1696-1707`).

Recipe availability is calculated from catalog component pairs. The recipe-target matrix then emits fit only when the recipe is available, the catalog result exists and the target profile exists, using the same normalization/clamp (`cpp/src/lobby/TftEngine.cpp:1709-1737`). Recipe rows follow catalog-derived recipe ordering. These are useful PPO numeric features, but the vector does not carry raw item/recipe IDs or target UUIDs in each cell. Target identity is implicit in board/bench slot order. The score is heuristic, not a probability or calibrated confidence.

## 3. Field-level dispositions

| Schema path | Native producer/evidence | Diagnostic/Python surface | PPO projection | Disposition |
|---|---|---|---|---|
| `entities.board[].unit.combat_stats{}` | Selected ChampionDefinition stats and combat profile | No complete stats map in unit audit record | Selected attack damage/speed, HP, armor and MR in target features | `partial_catalog_combat_profile_only` |
| `entities.bench[].unit.combat_stats{}` | Selected ChampionDefinition stats and combat profile | No complete stats map in unit audit record | Selected attack damage/speed, HP, armor and MR in target features | `partial_catalog_combat_profile_only` |
| `entities.shop[].unit.combat_stats{}` | Champion catalog lookup exists | No complete stats map in unit audit record | Shop emits cost, role and occupancy; no combat-stat map | `not_projected_as_combat_stats` |
| `entities.items.pending_anvil` | ItemEngine queue API; audited TftEngine grant callsite absent | Pending flag/kind/options if queue populated | Conditional pending/kind/option features; live gameplay producer unproven | `conditional_projection_no_gameplay_producer` |
| `entities.items.anvil_options[].option_id` | Ordered catalog ID in queue; no stable option identity | Raw option ID strings in audit snapshot | Catalog one-hot or semantic item stats by positional option slot | `positional_option_id_in_queue` |
| `entities.items.anvil_options[].kind` | Component/completed-item enum | Integer kind | Two kind indicator features | `two_kind_indicator_features` |
| `entities.items.anvil_options[].component_id` | Component catalog ID when component anvil | Raw option ID string | Catalog-position one-hot | `component_catalog_one_hot` |
| `entities.items.anvil_options[].item_id` | Completed-item catalog ID when completed-item anvil | Raw option ID string | Ten selected normalized stats, not raw ID | `selected_item_stats_not_raw_id` |
| `entities.items.anvil_options[].stats` | ItemDefinition stat values for completed items | No typed stats object | Ten selected normalized/clamped numeric features; no equivalent component stat object | `conditional_selected_stats_only` |
| `entities.items.anvil_options[].target_fits[].target_instance_id` | Not computed per target; best fit is reduced across all owned profiles | No target-fit records | No target identity | `not_produced_per_target_for_anvil` |
| `entities.items.anvil_options[].target_fits[].score` | Aggregate maximum ItemFitCache score | No per-target score records | One aggregate score normalized by 20 and clamped, conditionally | `aggregate_best_fit_only` |
| `derived_context.unit_roles[].instance_id` | Unit role is calculated while iterating physical board/bench/shop slots | No typed role-entity list | Slot-aligned features; no UUID in role record | `no_instance_id_in_role_projection` |
| `derived_context.unit_roles[].role` | UnitCombatClassifier derived role | No typed role-entity list | Role features in board/bench/shop and target blocks | `slot_aligned_derived_role` |
| `derived_context.item_target_fit[].item_id` | Inventory catalog ID per slot | Audit snapshot exposes ordered inventory IDs | Semantic feature matrix; raw ID not repeated in matrix | `semantic_slot_features_not_raw_item_id` |
| `derived_context.item_target_fit[].target_instance_id` | UnitProfile is joined to physical unit by UUID before slot projection | Audit snapshot has UUID separately | Implicit board/bench target slot; UUID omitted | `implicit_board_bench_target_slot` |
| `derived_context.item_target_fit[].score` | ItemFitCache heuristic | No typed fit records | 9×37 slot-indexed matrix; fit/50 clamped | `flat_heuristic_fit_matrix` |
| `derived_context.recipe_target_fit[].recipe_id` | Catalog-derived recipe result ordering | No typed recipe-ID records in wrapper | Implicit recipe matrix row index | `implicit_catalog_recipe_index` |
| `derived_context.recipe_target_fit[].target_instance_id` | UnitProfile UUID resolved to board/bench slot | Audit snapshot has UUID separately | Implicit board/bench target slot | `implicit_board_bench_target_slot` |
| `derived_context.recipe_target_fit[].score` | ItemFitCache, only if recipe available and target exists | No typed fit records | 100×37 recipe/target matrix; fit/50 clamped | `flat_conditional_recipe_fit_matrix` |

## 4. Non-equivalences and invariants

1. A conditional consumer is not proof that a producer populates its input.
2. Anvil option position is not a stable option ID or revision.
3. An aggregate best fit across units is not a per-unit `target_fits[]` collection.
4. Selected combat features are not a complete `combat_stats{}` map.
5. A role feature at a fixed slot is not a typed `instance_id → role` record.
6. A target matrix column is not a UUID-bearing target entity.
7. ItemFitCache output is a heuristic score; it must not be interpreted as probability.
8. Native masks remain independent legality inputs; these feature matrices do not replace them.

## 5. Remaining proof

- Trace the actual gameplay producer for anvil grants, including reward/PvE callsites and episode reset; until found, keep pending-anvil operational availability unproven.
- Define whether Schema v2 needs per-target anvil fits or an aggregate best-fit field; do not fabricate per-target records.
- Enumerate and version the exact dynamic combat-stat key set if a complete map remains required.
- Decide the explicit role vocabulary and whether roles include board, bench and shop entities; preserve physical identity if emitted structurally.
- Trace the flat matrices through Python vector environment, rollout buffer, Actor and Critic independently. This audit proves native vector construction and wrapper delivery only, not Actor/Critic leaf allocation.
- Keep all raw IDs, target UUIDs, catalog fingerprints, source sequences and status/provenance envelopes distinct from positional matrix indices.

Issue #346 remains open. This document does not approve runtime/schema/tensor changes or Gate 8.

## 6. Architecture reconstruction review

1. **Prior problem:** broad family matches conflated a complete structured record, a conditional API path and a lossy numeric projection.
2. **Technical justification:** false availability or identity claims would break replay correlation and overstate what PPO can distinguish.
3. **New responsibility:** this audit owns field-level evidence for combat-stat maps, anvil choices, unit roles and item/recipe target-fit projections.
4. **Contract and invariants:** no synthetic IDs; no per-target fit inferred from aggregate maxima; no calibrated-probability claim; masks remain independent; diagnostic snapshot and PPO vector remain separate.
5. **Cross-component impacts:** ItemEngine, TftEngine, ItemCatalog, UnitCombatClassifier, ItemFitCache, pybind audit snapshot, Python wrapper, PPO observation projection, schema and replay.
6. **Objective validation:** 19 schema paths enumerated exactly once; source callsites and formulas cited; 19 CSV dispositions reconcile to the same paths; no runtime or tensor-layout changes.

