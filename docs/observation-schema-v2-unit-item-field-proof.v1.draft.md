# Schema v2 Field-Level Producer Proof — Units and Item Inventory v1 (Draft)

**Status:** documentation-only source audit; no runtime or schema changes authorized.  
**Base:** `new-arquiteture`.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Scope:** Schema v2 board, bench and shop unit records; loose item components and completed-item inventory. This slice does not claim completion of the remaining entity paths.

## 1. Purpose and boundary

PR #355 reconciled schema paths with the 77-entry source map, but an ancestor match is not proof that each nested field is produced. This slice follows the concrete native state, the diagnostic snapshot, the flat observation builder and the Python boundary separately.

The authoritative runtime path remains native C++ `TftEngine` → flat observation vector and independent action masks → pybind → `CppTFTLobbyWrapper` → PPO. The public/audit snapshot is a separate diagnostic surface. Its richer records must not be described as PPO inputs.

## 2. Source evidence

### 2.1 Board, bench and shop

- Native capacities are 28 board slots, 9 bench slots and 5 shop slots (`cpp/include/lobby/TftEngine.hpp`, constants `kBoardSlots`, `kBenchSlots`, `kShopSlots`).
- The decision snapshot builder copies each occupied board/bench unit's UUID, internal champion ID, textual champion ID and star tier. It also resolves catalog cost. Shop offers are copied from the current shop slot into the same snapshot shape (`cpp/src/lobby/TftEngine.cpp:730-790`).
- The flat observation builder emits five values per board and bench slot: occupancy, normalized champion cost, normalized star tier, role encoding and heuristic strength. Shop slots emit occupancy, cost, a constant star feature, role and a constant zero strength feature (`cpp/src/lobby/TftEngine.cpp:1390-1430`).
- The audit snapshot is separately converted by pybind into dictionaries with `occupied`, `champion_id`, `uuid`, `star`, `cost` and `items`, then grouped into board/bench/shop arrays (`cpp/bindings/tft_engine_bindings.cpp:800-870`). This is not the PPO observation tensor.
- The Python wrapper returns the native reset/step `observations` array to the trainer. `get_audit_snapshot()` is a separate method for observers; it is not merged into `reset()` or `step()` observations (`cpp_lobby_env.py`, methods `reset`, `step`, `get_audit_snapshot`).

### 2.2 Unit identity and slot semantics

- A physical `UnitInstance` has `champion_internal_id`, `champion_id`, `uuid`, `star` and an item vector (`cpp/include/lobby/TftEngine.hpp`, `UnitInstance`).
- The decision snapshot preserves UUID and both champion identifiers, but it is an internal decision/audit representation. The flat PPO board/bench slot block does not encode UUID or champion ID as typed values; it encodes the five aggregate/normalized values listed above.
- The shop snapshot copies an offered `UnitInstance`, but the audited record has only the slot position as its offer locator. No stable shop-offer ID, offer revision or reroll-generation identity is established by this slice.
- The UUID factory is seeded and deterministic. Therefore UUID must not be promoted to a cross-episode or globally unique schema identity without the scope/uniqueness contract already identified in the UnitInstance lifecycle audit (#348). This slice does not reverse that finding.

### 2.3 Components and completed-item inventory

- `ItemEngine` stores loose components and completed item IDs as vectors of catalog IDs. Adding a component appends its ID; adding a completed item appends its item ID. Crafting consumes two matching component entries and appends the resulting catalog item ID (`cpp/include/items/ItemEngine.hpp:175-260`).
- Equipped items are stored separately in a map keyed by unit UUID. Equip consumes an inventory item and appends the item catalog ID to that UUID's equipped vector; merge transfers the equipped catalog IDs between UUID keys (`cpp/include/items/ItemEngine.hpp:260-313`).
- Reset clears components, inventory, equipped mappings, pending anvils and metrics (`cpp/include/items/ItemEngine.hpp:130-139`).
- The PPO observation builder iterates the active component catalog and emits normalized counts, then encodes each of nine inventory positions using the corresponding item's semantic stats. It does not emit typed component/item entity records, acquisition event IDs, physical item-instance IDs or a source decision sequence (`cpp/src/lobby/TftEngine.cpp:1615-1633`).
- The audit snapshot exposes item components, item inventory, component catalog and pending-anvil fields through pybind, but those diagnostic fields are not the same as the PPO vector (`cpp/bindings/tft_engine_bindings.cpp:851-855`).

## 3. Field-level dispositions

| Schema family/path | Native producer proof | Diagnostic/Python surface | PPO delivery | Disposition |
|---|---|---|---|---|
| `entities.board[].slot_index` | Physical array index, 0–27 | Board array order in audit snapshot | Implicit slot position through fixed five-value block order; no explicit integer field | `derived_from_container_position`; not a standalone typed field |
| `entities.board[].presence` | Optional occupied slot | `occupied` boolean | Occupancy scalar | `observed`, representation differs |
| `entities.board[].unit.champion_id` | `UnitInstance::champion_id` | Explicit string | Not emitted as categorical ID in board block | `diagnostic_snapshot_only` for typed identity |
| `entities.board[].unit.instance_id` | Raw `UnitInstance::uuid` | Explicit UUID | Not emitted | `diagnostic_snapshot_only`; UUID scope limitation remains |
| `entities.board[].unit.star` | `UnitInstance::star` | Explicit integer | Normalized scalar | `observed_projected` |
| `entities.board[].unit.position` | Board slot index; internal 4×7 mapping | Implicit array position | Slot order and coarse front/back features elsewhere | `slot_derived`; canonical TFT hex semantics unproven |
| `entities.board[].unit.items[]` | Per-unit equipment is tracked by UUID in ItemEngine and/or UnitInstance item state | Audit snapshot item IDs | Board item count/profile features, not a typed item list | `aggregate_projected`; per-item identity not delivered |
| `entities.board[].unit.traits[]` | Champion catalog membership; item-granted traits are a distinct derived source | No typed per-unit trait list in this audit snapshot contract | Aggregate trait features/counts only | `catalog_derived_or_aggregate`; source scope must remain explicit |
| `entities.board[].unit.combat_stats` | Static champion base stats/combat profile; item effects are separately modeled | No full per-instance combat-stat map in unit audit record | Selected normalized target-profile stats, not a complete stat map | `partial_derived_projection`; not a complete observed object |
| `entities.bench[].slot_index` | Physical array index, 0–8 | Bench array order | Implicit fixed slot position | `derived_from_container_position` |
| `entities.bench[].presence` | Optional occupied slot | `occupied` boolean | Occupancy scalar | `observed`, representation differs |
| `entities.bench[].unit.champion_id` | `UnitInstance::champion_id` | Explicit string | Not emitted as categorical ID in bench block | `diagnostic_snapshot_only` |
| `entities.bench[].unit.instance_id` | Raw `UnitInstance::uuid` | Explicit UUID | Not emitted | `diagnostic_snapshot_only`; UUID scope limitation remains |
| `entities.bench[].unit.star` | `UnitInstance::star` | Explicit integer | Normalized scalar | `observed_projected` |
| `entities.bench[].unit.position` | Bench slot index, not board geometry | Implicit array position | Fixed slot order | `container_position_only` |
| `entities.bench[].unit.items[]` | Equipment keyed by unit UUID | Audit snapshot item IDs | Aggregate equipped-count and item-target features | `aggregate_projected` |
| `entities.bench[].unit.traits[]` | Catalog membership plus separately derived item-granted traits | No typed per-unit trait list in this audit snapshot contract | Aggregate trait features/counts | `catalog_derived_or_aggregate` |
| `entities.bench[].unit.combat_stats` | Static catalog profile plus item effects | No complete per-instance map | Selected normalized target-profile stats | `partial_derived_projection` |
| `entities.shop[].slot_index` | Current shop array index, 0–4 | Shop array order | Implicit fixed slot position | `derived_from_container_position` |
| `entities.shop[].presence` | Null/non-null shop offer | `occupied` boolean | Occupancy scalar | `observed` |
| `entities.shop[].unit.champion_id` | Offered UnitInstance champion ID | Explicit string | Shop block has cost/role/occupancy but no categorical champion ID | `diagnostic_snapshot_only` |
| `entities.shop[].unit.instance_id` | Offered UnitInstance UUID | Explicit UUID in snapshot | Not emitted | `diagnostic_snapshot_only`; no offer lifecycle identity |
| `entities.shop[].unit.star` | Shop block emits a constant 1.0 star feature | Snapshot carries star | Constant feature, not read from offer star in this projection | `projection_constant`; do not claim field-level PPO delivery |
| `entities.shop[].unit.position` | Shop slot, not board position | Implicit array position | Fixed slot order | `container_position_only` |
| `entities.shop[].unit.items[]` | Shop offer is copied from shop UnitInstance; normal offers are catalog units | Audit snapshot item list | No typed item list in shop PPO block | `not_established_as_shop_item_state` |
| `entities.shop[].unit.traits[]` | Champion catalog membership | No typed shop trait list | Shop role/cost/occupancy only in slot block | `not_projected_as_shop_traits` |
| `entities.shop[].unit.combat_stats` | Static champion profile available by catalog lookup | No complete per-offer combat map | Role and cost only in shop block | `not_projected_as_complete_combat_stats` |
| `entities.items.components[].component_id` | Component catalog ID repeated in vector | Audit snapshot exposes ordered IDs | Component catalog-index counts | `catalog_index_aggregate`; no physical component identity |
| `entities.items.components[].count` | Count can be computed from repeated IDs | Diagnostic vector preserves multiplicity | Count normalized by 6 and clamped to [0,1] | `derived_aggregate`; normalization loses exact counts above cap |
| `entities.items.inventory[].item_id` | Completed-item catalog ID in inventory vector | Audit snapshot exposes ordered IDs | Semantic feature vector per inventory slot | `catalog_semantic_projection`; raw ID/order is not typed PPO input |
| `entities.items.inventory[].slot` | Vector index, up to nine projected positions | Inventory array order | Implicit position in nine fixed feature blocks | `derived_from_container_position` |

**Important correction:** the PPO vector does receive meaningful item semantics and aggregate unit/item-target features. The gap is not “no item information”; the gap is loss of typed identity, provenance, event/decision sequence and exact collection semantics. Likewise, board/bench/shop state is represented in PPO as fixed-position features, but not as structured unit entities.

## 4. Explicit non-equivalences

1. Audit snapshot UUID/champion strings are not PPO inputs merely because pybind exposes them to the observer.
2. A slot index is not a physical unit identity.
3. A shop slot is not a stable shop-offer identity across rerolls.
4. A component catalog ID plus multiplicity is not a physical component instance or acquisition history.
5. An inventory item catalog ID is not a physical item-instance ID.
6. A normalized count capped at 1.0 is not an exact count above its normalization threshold.
7. A partial combat target profile is not a complete per-unit `combat_stats` object.
8. A fixed slot's PPO feature block is not evidence that every nested Schema v2 field is delivered.

## 5. Remaining work in this slice

- Reconcile these 31 paths against the crosswalk CSV with per-path proof labels, rather than leaving all ancestor rows in the inherited placeholder state.
- Trace exact trait and item-granted-trait formulas and distinguish board-only versus board+bench scopes for each consumer.
- Verify the exact construction of the audit snapshot's per-unit `items` list and whether it reads UnitInstance or ItemEngine equipment state in every lifecycle path.
- Complete Python → vector environment → rollout buffer → Actor/Critic delivery proof for each feature block. This document only establishes the native vector and wrapper boundary; it does not claim Actor/Critic leaf-level allocation.
- Continue the remaining Schema v2 entity families and all derived/strategic/legal paths.

## 6. Architecture reconstruction review

1. **Prior problem:** family-level source-map matches obscured the difference between structured diagnostic snapshots and the lossy fixed-position PPO observation.
2. **Technical justification:** treating a diagnostic UUID or catalog ID as a PPO feature, or treating a slot-derived value as a physical identity, would create false guarantees for replay, correlation and learning.
3. **New responsibility:** this audit owns field-level evidence/disposition for board, bench, shop and basic item-inventory schema paths; the source map remains an index, not proof.
4. **Contract and invariants:** native state is authoritative; diagnostic snapshots and PPO vectors are separate products; slot order is not identity; raw UUID remains scope-limited; masks remain separate legality inputs; no fabricated IDs/sequences.
5. **Cross-component impacts:** TftEngine, UnitInstanceFactory, ShopEngine, ItemEngine, ChampionCatalog, pybind audit snapshot, Python wrapper, vector environment, rollout buffer, Actor/Critic, Schema v2 and replay fixtures.
6. **Objective validation:** all 31 listed paths have an explicit evidence-based disposition; source line ranges are recorded above; no runtime/schema/tensor/checkpoint changes are made; unresolved fields remain explicitly open rather than inferred as available.

Issue #346 remains open. This slice is not Gate 8 approval.
