# Item system integration contract — Phase 2

Status: **runtime and unified policy path implemented behind an explicit item-catalog input; active-set loot integration and full CI verification remain pending.**

This branch continues from the item contract already merged to `main`. It does not use the rejected PR #85 or introduce a separate item policy.

## Unified action architecture

- One `TFTPolicy` and one PPO rollout/training path choose all actions.
- The action tensor remains six integers: `[type, arg1, arg2, arg3, arg4, arg5]`.
- Existing action IDs 0–6 keep their meanings. Item actions are IDs 7 and 8:
  - `EQUIP_FROM_INVENTORY = 7`
  - `CRAFT_AND_EQUIP = 8`
- There is no item-specific `WAIT`, no transfer action, no unequip action, no heuristic item action selector, and no separate item reward. Item actions use the same environment/PPO reward path as every other action.
- Item-specific policy heads are conditional on the sampled action type. Existing shop, bench and movement heads keep their old dimensions. `evaluate_actions` recomputes the same conditional log-probabilities as action collection.
- The native C++ type mask and Python mask contract both have nine entries. Item masks are included in the rollout mask dictionary and the trainer's selected-action audit.

## Item catalog and per-player state

`TFTEngine` accepts a separate `item_catalog_path` after the champion `catalog_path`. The catalog is parsed with `load_item_catalog()` from the versioned schema in `docs/item-catalog-schema.md`. The training adapter accepts the path through `TFT_ITEM_CATALOG_PATH` or the optional trainer argument.

The repository has **no authoritative active-set item catalog JSON**, so this branch does not fabricate live item stats or recipes. The normalized fixture at `cpp/tests/fixtures/items_test_catalog.json` is test data only. Without a configured catalog, item actions remain masked off.

Each player owns one `ItemEngine`. Masks are built from its actual component stack, completed-item inventory, recipe table, and the current board/bench UUIDs. The policy selects catalog component types (not transient component-stack positions), then C++ resolves the target index to the unit UUID and validates the same legal transition before mutation.

Runtime mask contract:
- `item_inventory_mask`: up to nine completed-item inventory candidates.
- `item_component_first_mask`: component catalog choices that have a craftable pair.
- `item_component_pair_masks[first, second]`: available recipe and copies, including two copies of the same component.
- `item_target_mask`: board slots 0–27, then bench slots 28–36, excluding units already at item capacity.

The native event API exposes `grant_item_component` and `grant_completed_item` so the authoritative loot/armory source can populate item state. The current lobby does not yet simulate PvE item drops, so these entry points are not called by an actual drop resolver. Do not infer that live item acquisition is complete from the test fixture.

## Equipment ownership and lifecycle safety

Equipment is keyed by unit UUID and projected to `UnitInstance::items`, which is copied into the normal combat input. Board/bench movement preserves UUID and therefore equipment ownership.

- There is no policy transfer or unequip.
- A bench unit carrying equipment cannot be sold, because sale would orphan its items.
- A purchase that would auto-merge copies carrying equipment is masked until a merge rule can preserve ownership.
- Episode reset clears each player's item state. Elimination ends that player's actions and clears its units; no equipment is moved to another unit.
- Craft-and-equip is validated before mutation and includes rollback if a later transition unexpectedly fails.

These restrictions are deliberate safety behavior, not a claim that all real TFT sale/merge item rules have been modeled. The active set's exact lifecycle rules must be confirmed before loosening them.

## Tests and phase exit criteria

The C++ lobby integration test uses a normalized fixture catalog to verify:
1. valid recipe/component/target state enables `CRAFT_AND_EQUIP`;
2. the action consumes components and attaches the resulting `CombatItem` to the exact unit instance;
3. a completed item grant enables `EQUIP_FROM_INVENTORY`;
4. the item becomes visible through the same combat/audit path.

Python tests verify the nine-way type mask, item masks, action sampling, and parity between collected and reevaluated PPO log-probabilities. Old seven-row type-head checkpoints are migrated by copying the original seven rows and initializing the two new rows; new item heads use their module initialization when loading an older checkpoint.

Phase 2 should not be marked complete until CI passes and the active-set catalog is supplied/validated. The missing production loot/drop resolver remains a dependency for end-to-end item acquisition; it must not be replaced with invented drop rates or recipes.
