# PvE Component Pool and Item Inventory Lifecycle Audit v1 — Draft

**Status:** source-backed lifecycle audit; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope and prior ambiguity

The previous loot/anvil audit established that normal PvE loot grants components directly rather than enqueueing an anvil. This audit follows those components after distribution: per-player PvE pool, held component copies, crafting, completed-item inventory, equipment ownership, episode reset, audit snapshot and PPO observation.

The key distinction is between (a) copies still available in the PvE distribution pool and (b) copies already granted to a player's ItemEngine. They are separate state stores and must not be represented as the same observation field.

## 2. PvE pool ownership and lifecycle

Each `PlayerEnv` owns a `items::Set18ComponentPool pve_component_pool` (`cpp/src/lobby/TftEngine.cpp:422`). It is not the shared champion pool and is not the player's collected-component inventory.

The pool implementation in `cpp/include/items/PveLootDistribution.hpp` has these semantics:
- `initialize(component_ids)` requires exactly eight entries and copies the supplied IDs into the pool (`PveLootDistribution.hpp:66-71`).
- `add_stage_refresh(component_ids)` requires eight entries and appends one more copy of every supplied ID (`PveLootDistribution.hpp:73-77`).
- `draw(rng)` selects one current vector position uniformly, returns that catalog ID, and erases exactly that position (`PveLootDistribution.hpp:79-87`). Thus a pool initialized with eight distinct IDs cannot draw the same ID twice before a refresh.
- `remaining()` reports the number of still-undrawn copies, not the number held by the player.

During PvE reward resolution, the lobby initializes the player's pool when empty; otherwise it appends a stage refresh. It then draws up to the rolled component count and grants each successful draw to that player's ItemEngine (`cpp/src/lobby/TftEngine.cpp:970-995`). Stage 1 starts with one of each component; stages 2, 3 and 4 add another copy of each before drawing. This is a per-player distribution pool, not a globally shared or cross-player depleted pool.

At episode initialization, each player's pool is replaced with a default-constructed empty pool (`TftEngine.cpp:1205-1209`). It is then initialized lazily when the first component-reward round resolves. The component pool is therefore episode-local.

## 3. Collected components and crafting

The ItemEngine stores collected components as `std::vector<std::string> components_` (`cpp/include/items/ItemEngine.hpp`). Each entry is one held copy represented by a catalog ID; repeated strings represent multiple copies, not a shared physical component entity.

- `add_component(id)` validates the ID against the loaded component catalog, appends one copy and increments `components_collected` (`ItemEngine.hpp:177-185`).
- `can_craft(first, second)` checks the recipe and availability of the required multiplicities (`ItemEngine.hpp:197-210`).
- `craft(first, second)` locates two distinct vector positions, erases exactly those two copies and appends the resulting catalog item ID to inventory (`ItemEngine.hpp:220-255`).
- Symmetric recipe keys allow either component order; two identical component IDs require two copies. Existing tests cover both symmetric order and double-copy recipes (`cpp/tests/test_item_engine.cpp:302-324`).
- `apply_action(CRAFT_AND_EQUIP)` snapshots components, inventory, equipment and metrics; if crafting or equipping fails, it restores the snapshot and rejects the action (`ItemEngine.hpp:440-479`).

There is no physical component-instance ID, acquisition event ID, source round, source sequence or per-copy provenance in this storage model. A component catalog ID and its multiplicity are the current semantics.

## 4. Completed-item inventory and equipment

Completed items are also stored as catalog-ID strings in a vector. Direct PvE completed-item rewards append one catalog ID through `add_completed_item()`; crafting appends its recipe result. Equipping removes one matching inventory entry and appends its ID under the target UnitInstance UUID in `equipped_` (`ItemEngine.hpp:188-195`, `257-278`).

Sale/merge lifecycle is distinct:
- Sale returns all equipment for the exact UUID to inventory and erases that UUID's equipment entry.
- Merge transfers equipment from consumed UUIDs to the surviving UUID, returning overflow beyond the three-item cap to inventory.
- Reset clears components, inventory, equipped ownership, pending anvils and metrics (`ItemEngine.hpp:133-139`).

The audit snapshot exposes the current collected component-ID vector and completed-item inventory vector, plus pending-anvil data (`cpp/src/lobby/TftEngine.cpp:6750-6760`). It does **not** expose the remaining PvE pool contents or its remaining count. The round event `COMPONENT_LOOT_GRANTED` includes `pool_remaining` as diagnostic text (`TftEngine.cpp:989-994`); that event field is not a persistent typed pool-state field.

## 5. PPO observation and mask projection

The current flat observation projects item state as follows (`cpp/src/lobby/TftEngine.cpp:1605-1665`):
- Ten component features follow the active catalog's component order. Each is the count of that catalog ID in the player's collected `ItemEngine::components()`, divided by six and clamped to `[0,1]` (`TftEngine.cpp:1610-1622`).
- Nine inventory slots encode semantic features for the item catalog definition at each vector position (`TftEngine.cpp:1624-1632`). These are positional inventory features, not physical item IDs.
- Recipe availability is represented by a catalog-derived matrix; exact compatibility scores are separately computed for inventory items and possible board/bench targets (`TftEngine.cpp:1634-1665` and following target-fit block).
- Pending anvils have separate flags and up to nine option feature slots; this state is conditional and does not encode the PvE pool (`TftEngine.cpp:1546-1604`).

Masks are generated from the live ItemEngine state. The inventory mask enables up to the first nine inventory positions; recipe-pair masks are derived from `can_craft()`; action types 7 and 8 are enabled only when inventory/recipe and target conditions are satisfied (`TftEngine.cpp:1060-1100`). These masks remain a separate legality input, not a replacement for item semantics.

Consequences:
- PPO receives collected component counts, not the remaining PvE pool composition or pool count.
- Component counts above six collapse to the same normalized value; exact multiplicity is not recoverable from this feature block.
- Inventory semantic features preserve useful item meaning, but the fixed nine-slot projection is positional and does not expose stable physical item-instance identity.
- The observation does not prove which PvE reward event or decision sequence produced a held component/item.
- The exact item IDs and current vectors are available in the native audit snapshot, but that diagnostic surface is not the same as the flat PPO observation path.

## 6. Existing tests and their actual coverage

The current tests provide meaningful but bounded proof:
- `cpp/tests/test_item_engine.cpp:455-499` checks stage reward table distributions, stage-1 no-duplicate draws from an initially unique eight-component pool, remaining count after five draws, and one eight-entry stage refresh.
- `cpp/tests/test_tft_engine_pool.cpp:950-1023` advances real Engine rounds and verifies direct component grants in stages 2 and 4 and direct completed-item grants in stages 5 and 6. It also asserts that direct drops do not create pending anvils and do not suspend normal PASS legality.
- ItemEngine tests cover component multiplicity, crafting, symmetric recipes, same-component recipes, inventory/equip, and reset-related behavior of the ItemEngine API.
- These tests do not establish a typed per-component identity, a pool-state observation contract, event-to-PPO provenance, or complete cross-episode replay correlation for every loot grant.

## 7. Field-level dispositions

| Data concept | Current source/representation | Disposition |
|---|---|---|
| Remaining PvE component pool | Per-player vector of catalog IDs; draw erases an entry | `native_episode_local_distribution_state_not_in_ppo` |
| Collected component copies | ItemEngine vector of catalog IDs; duplicates are multiplicity | `native_collected_catalog_counts` |
| Component observation | Ten catalog-order counts, divided by six and clamped | `lossy_aggregate_feature` |
| Completed-item inventory | Vector of catalog IDs; first nine positions projected semantically | `positional_semantic_features_no_physical_item_identity` |
| Recipe availability | Derived from recipe catalog and current component multiplicity | `derived_boolean_matrix_and_masks` |
| Crafted item | Recipe result catalog ID appended to inventory | `derived_catalog_item_no_acquisition_identity` |
| Equipped item | Catalog ID stored under UnitInstance UUID | `unit_owned_catalog_item_no_physical_item_identity` |
| Loot provenance | Round events/log text; not a typed field in item vectors | `diagnostic_event_only_not_correlated_to_ppo_decision` |

## 8. Required future proof (not authorized implementation)

Before changing the schema or claiming lossless item state:
1. Decide whether component and item copies need physical identities or whether catalog ID plus multiplicity is the intended canonical domain model.
2. If provenance is required, define typed loot/acquisition event identity, source round, player, episode scope and sequence, including craft/equip/return transitions.
3. Decide whether the remaining PvE distribution pool is strategically relevant to the policy. If not, explicitly classify it as Engine-internal distribution state rather than an observation feature.
4. Define how inventory positions remain correlated across observation, action masks, action decoding and replay when items are removed or appended.
5. Add tests for stage refresh exhaustion/reinitialization, reset between episodes, duplicate catalog validation, exact count beyond six, inventory beyond nine, sale/merge equipment return, and event-to-observation/replay correlation.
6. Keep masks separate and final for legality; do not infer legality from normalized observation values.

No runtime, schema, tensor-layout, PPO, reward, mask, training, checkpoint, Viewer or Overwolf implementation is authorized by this audit. Issue #346 remains open and Gate 8 remains blocked.

## 9. Architecture reconstruction review

1. **Prior problem:** component pool, collected components and completed-item inventory could be conflated as one generic “item state”.
2. **Technical justification:** these stores have different owners, lifecycles, semantics and observation coverage; the PPO projection is intentionally lossy and positional.
3. **New responsibility:** this audit documents the boundary from PvE distribution through collection, crafting, inventory, equipment and policy projection.
4. **Contract and invariants:** pool draws remove one available catalog copy; collected multiplicity is separate; crafting consumes exactly two required copies; failed craft-and-equip rolls back; reset clears episode-local item state; masks remain separate.
5. **Cross-component impacts:** PvE loot distribution, TFTEngine round/reset lifecycle, ItemEngine, item catalog, audit snapshot, native masks, flat observation, Python PPO consumers and replay/evaluation.
6. **Objective validation:** source locations and existing tests are enumerated; current PPO feature normalization/slot limits and absent pool projection are explicitly identified. Documentation only.

Issue #346 remains open. This document does not approve Gate 8 or runtime implementation.
