# Item system integration contract — Phase 1

Status: **contract proposal for implementation; not yet connected to the match runtime**.

This document starts from `main`, not the rejected PR #85. It intentionally does not modify `policy.py`, the legacy six-component action vector, checkpoint loading, or PPO behavior.

## Existing architecture constraints

- The native match accepts eight `PlayerAction` values. Each currently has six integer components and dimensions `[7, 5, 9, 28, 28, 28]`.
- `trainer.py` maps those six components to the current action dictionary; `tft_engine_bindings.cpp` rejects any action that does not contain exactly six components.
- `TFTPolicy` samples autoregressive, masked action arguments; PPO later recomputes log-probabilities through `evaluate_actions`. Any eventual item action must be represented consistently in both paths and its exact masks must be saved in the rollout.
- `ItemEngine` already implements local component inventory, recipes, completed-item inventory, equip, unequip, transfer, and metrics. It is not currently owned or called by the normal `TFTEngine` match loop.
- `UnitInstance::items` and `CombatUnit::items` exist. Combat applies the numeric bonuses in `CombatEngine.cpp`, but the normal lobby-to-combat construction path still needs an explicit audit and integration test.

## Canonical per-player state

The item subsystem needs one authoritative state per player:

- `components`: ordered component IDs; repeated IDs represent separate copies.
- `inventory`: ordered completed-item IDs; repeated IDs represent separate copies.
- `equipped_by_unit_uuid`: item IDs keyed by the unique UUID of a unit instance, not by champion name or champion catalog ID.
- metrics: component receipts, crafts, equips, unequips, transfers, invalid actions, and unused-item counts.

Equipment must follow an individual unit copy through board/bench movement and duplicate champions must never share equipment. The normal combat input should receive a projection of the canonical equipment state. The implementation must not allow an independent `ItemEngine::equipped_` map and `UnitInstance::items` to drift; Phase 2 must either establish one authority with a deterministic projection or implement atomic synchronization with consistency checks.

Selling a unit, elimination, reset, and any set-specific item return/drop behavior must be explicitly specified from the active game's rules before implementation. Do not silently discard or duplicate items.

## Semantic action contract

The item subsystem supports these semantic operations:

1. `WAIT`: preserve components/items.
2. `EQUIP_FROM_INVENTORY`: equip one completed item onto an eligible unit.
3. `CRAFT_AND_EQUIP`: consume two available components, craft the catalog recipe, and equip the result atomically.
4. `TRANSFER`: move one equipped item between two distinct eligible unit instances.
5. `UNEQUIP_TO_INVENTORY`: return an equipped item to the player's completed-item inventory when the active set rules permit it.

The typed command in `cpp/include/items/ItemActionContract.hpp` uses catalog IDs and unit UUIDs after action decoding. The policy-facing vector will use bounded categorical indices; the adapter must resolve those indices against the same state snapshot used to generate masks. It must never pass display names or stale slot indices as persistent identity.

### Operation-specific fields

| Operation | Required semantic arguments |
|---|---|
| WAIT | none |
| EQUIP_FROM_INVENTORY | item ID, target unit UUID |
| CRAFT_AND_EQUIP | two component IDs, target unit UUID |
| TRANSFER | item ID, source unit UUID, target unit UUID |
| UNEQUIP_TO_INVENTORY | item ID, source unit UUID |

## Dependency audit findings (from `main`)

The dependency map has now been checked against the actual source:

- C++ `ActionType` is fixed at seven values in `cpp/include/decision/DecisionTypes.hpp`; its numeric values are guarded by static assertions. The native `PlayerActionMasks::type_mask` and Python `Trainer.MASK_SHAPES["type_mask"]` also have length seven.
- `trainer.py` defines `ACTION_DIMS` as a fixed list and constructs `TFTPolicy` from it. It also allocates action-type metrics with length seven.
- `policy.py` rejects dimensions other than `[7, 5, 9, 28, 28, 28]`. Its candidate-observation tail calculation currently derives candidate-feature length from `action_dims[1]` and `action_dims[2]`. Therefore, simply enlarging the item argument dimensions would also corrupt observation-tail interpretation unless that coupling is removed and separately tested.
- `load_compatible_state_dict()` migrates supported observation-layout changes. It does not currently provide a general migration for changed action-head shapes or PPO optimizer state. Action-head migration must be implemented explicitly if the item action space expands.
- `CppTFTLobbyWrapper`, the pybind `step()`, and `PlayerAction::values` all enforce exactly six action components.
- The repository tree has no active-set item catalog JSON. `docs/item-catalog-schema.md` explicitly requires an externally sourced, normalized catalog. The constructor currently accepts the champion catalog path, not a separate item catalog path.

This rules out a naive increase of the existing categorical dimensions: it would affect candidate-feature parsing, all mask shapes, checkpoint loading, and the optimizer. The item action adapter needs a clearly separated policy argument contract, while keeping one `TFTPolicy` and one PPO training path.

## Policy-facing mapping decision

The dependency audit supports a backward-conscious mapping without changing the action tensor's six-column shape:

- Keep the first six columns `[type, arg1, arg2, arg3, arg4, arg5]`; legacy action types 0–6 and their argument interpretation remain unchanged.
- Extend the type category with four item operations: `EQUIP_FROM_INVENTORY=7`, `CRAFT_AND_EQUIP=8`, `TRANSFER=9`, `UNEQUIP_TO_INVENTORY=10`. `PASS=6` remains unchanged.
- Item arguments are conditional on the selected type and decoded using item-specific policy heads, not by enlarging the legacy shop/bench/movement heads. This avoids coupling catalog IDs to `shop_head` / `bench_head` and avoids changing the candidate-observation tail calculation.
- For item actions, use stable catalog indices and a combined unit-candidate index: board slots `0..27`, followed by bench slots `28..36`. The C++ decoder resolves the selected unit index to the current instance UUID before applying the semantic command.
- Component selection is by component catalog ID, not by an arbitrary inventory position. The mask indicates whether at least one copy is available; the second-component mask is conditional and must ensure that two copies exist when both selected IDs are equal.
- Completed items are selected by catalog ID when taken from inventory. Transfer/unequip selects an equipped-item slot `0..2` on the chosen source unit, then resolves it to the item's catalog ID.
- New masks are conditional on the selected operation and its previous arguments: component-first, component-second, completed-item-inventory, equipped-item-slot, source-unit and target-unit masks. Their sizes come from the active catalog plus the fixed 37 board/bench candidate slots.

This is the proposed contract, not yet implemented in the policy. Before implementation, the active catalog must be supplied or generated from a pinned Set 17 source, and its component/item counts must be validated. The six-column action tensor shape can remain stable, but the action type head grows from 7 to 11 outputs, so the old checkpoint's type head needs an explicit migration that copies its original seven rows and initializes the four new rows. New item heads and their optimizer state also need explicit handling. The existing observation-feature migration alone does not cover this.

## Policy action-vector decision is intentionally gated

Do **not** assume the rejected PR #85's proposed seven-dimension contract. Before selecting the categorical dimensions/capacities, Phase 1 must inspect and record:

- the active set's real component/item catalog and maximum valid catalog indices;
- the real environment limits for component and completed-item inventories;
- the maximum unit candidate set (board + bench) and UUID-to-slot mapping;
- the existing `ActionType` enum, all masks, all action conversion points, and checkpoint migration/loading behavior.

The legacy six action components and existing checkpoints remain unchanged during this phase. The final policy-vector mapping is selected only after those dependencies and bounds are proven. If the action type cardinality grows, checkpoint compatibility must be handled explicitly rather than silently relying on `load_state_dict`.

## Legal-action and execution parity

Mask generation and execution must use the same legality predicates. A masked action must be executable for the snapshot from which its mask was built; stale/invalid actions must fail safely without consuming components or items. `CRAFT_AND_EQUIP` is atomic: a failed craft or equip must not leave components consumed or an item stranded.

## Phase exit criteria

Phase 1 is complete only when:
- the canonical state and semantic operations are represented in code and documented;
- action-vector bounds are grounded in the actual active-set/runtime constraints;
- the action decoding/mask/rollout/checkpoint dependencies have been mapped;
- the rejected PR's standalone `item_policy.py` architecture is not reused;
- no policy or checkpoint behavior has changed yet.

Subsequent phases integrate the contract into the native match runtime, combat, the existing policy/PPO, reward shaping, tests, compatibility audits, and final report.
