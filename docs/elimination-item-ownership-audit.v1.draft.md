# Elimination Item Ownership Audit v1 — Draft

**Status:** source-backed documentation follow-up; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Purpose and boundary

The UnitInstance lifecycle follow-up (#369) established that player elimination returns champion copies and clears board/bench slots, but does not call ItemEngine's per-unit equipment-return operation. This note narrows the consequence: whether the equipped-item map remains in the eliminated PlayerEnv, whether it is reachable through active gameplay consumers, and what remains unproven.

No runtime behavior, item ownership semantics, schema, PPO, masks, training, checkpoint or tensor layout is changed or approved here.

## 2. Source trace

### 2.1 Sale and merge are explicit item lifecycle transitions

- The sale path calls `ItemEngine::return_equipped_to_inventory(sold_uuid)` before clearing the sold bench slot. If that operation fails, it attempts to roll back the champion copies returned to the pool.
- The automatic merge path calls `transfer_equipped_on_merge(consumed_uuid, surviving_uuid)` for consumed units, then synchronizes the surviving UnitInstance's item mirror.
- These are explicit ownership transitions: sale returns item catalog-ID copies to the same player's inventory; merge transfers equipped catalog-ID copies to the surviving UUID, returning overflow to that player's inventory.

Sources: `cpp/src/lobby/TftEngine.cpp` purchase/merge path around 5046–5089 and sale path around 5590–5640; `cpp/include/items/ItemEngine.hpp` methods `return_equipped_to_inventory` and `transfer_equipped_on_merge`.

### 2.2 Elimination does not perform either transition

`return_eliminated_player_units(player_index)`:
1. returns current shop offers;
2. returns champion copy counts for occupied board and bench units to the shared UnitPool;
3. resets board and bench optionals;
4. registers the now-empty position state.

It does not call `return_equipped_to_inventory`, `transfer_equipped_on_merge`, or another per-unit ItemEngine cleanup operation.

Source: `cpp/src/lobby/TftEngine.cpp`, `return_eliminated_player_units` around 4570–4603.

### 2.3 What happens to the ItemEngine state

- Each PlayerEnv owns its own ItemEngine.
- ItemEngine's `equipped_` map is keyed by UnitInstance UUID and remains allocated until `ItemEngine::reset()` or destruction.
- The audited episode/player initialization path calls `reset()`, which clears components, inventory, equipped mappings, anvils and metrics.
- Elimination clears the owning UnitInstance slots but does not clear the corresponding UUID keys from `equipped_`.

Source: `cpp/include/items/ItemEngine.hpp` reset/equipment methods; `cpp/src/lobby/TftEngine.cpp` player initialization around 1190–1230 and elimination around 4570–4603.

**Established conclusion:** after elimination, equipped item catalog IDs can remain in the eliminated player's private ItemEngine map as orphaned UUID-keyed entries until that ItemEngine is reset or destroyed. The elimination routine does not return them to that player's bag and does not return items to any shared item pool.

This is a retained per-player state entry, not evidence of item transfer to another player or duplication in the shared champion pool.

## 3. Reachability and gameplay impact

The audited active item-target profile builder enumerates only occupied board and bench units. Once elimination clears those slots, the eliminated UUIDs no longer appear as active item targets. The current item-target and policy action path therefore has no active board/bench unit to which those orphaned mappings can be applied.

The source audit does not establish a general API that enumerates all equipped UUID mappings, nor a post-elimination consumer that reattaches or transfers them. Do not claim that the retained map is semantically harmless solely because no active unit remains; its lifecycle is still incomplete and deserves an explicit terminal-owner rule.

The exact public audit-snapshot behavior for eliminated-player orphan mappings must remain separately verified before claiming that no diagnostic surface can expose them.

## 4. Required semantic decision — intentionally not frozen

The architecture must distinguish two possible terminal semantics before implementation:

- **Retire/discard:** elimination permanently retires the player's equipped items. The owner must explicitly clear the eliminated UUID mappings (and define whether item inventory/anvil state is also cleared), without returning them to a living player's inventory.
- **Return-to-owner-bag then retire:** elimination first moves every equipped catalog-ID copy back to the eliminated player's own inventory, then marks that inventory as terminal/inaccessible or clears the complete ItemEngine.

Neither behavior is proven as an intentional game rule by the current code. The current implementation is effectively "clear units, retain UUID-keyed equipped entries until reset"; that is an implementation consequence, not an accepted domain contract.

No item should be transferred to another player, and no physical item-instance ID should be invented: current ItemEngine stores catalog IDs and multiplicity only.

## 5. Missing tests and acceptance evidence

Existing sale/merge tests do not prove elimination item cleanup. Add post-Gate 8 tests before runtime acceptance:

1. Equip one and multiple items to board and bench units, then eliminate the player.
2. Assert all champion copies are returned to the shared pool exactly once.
3. Assert no eliminated unit remains in board/bench or in item-target candidate enumeration.
4. Assert the selected terminal item policy: discarded/cleared or returned to the eliminated player's own bag before terminal cleanup.
5. Assert no item becomes available to another player and no duplicate item count is created.
6. Assert repeated elimination/reset and two consecutive episodes do not retain stale UUID mappings.
7. Assert diagnostic snapshots distinguish eliminated/empty state from a living player with empty inventory.

These are future executable acceptance criteria, not tests run by this documentation-only change.

## 6. Architecture reconstruction review

1. **Prior problem:** the lifecycle audit found no ItemEngine cleanup call during elimination but had not narrowed retained-state reachability or separated implementation consequence from intended game semantics.
2. **Technical justification:** sale, merge and elimination have different ownership semantics; silently applying sale behavior to elimination could incorrectly return assets to a player that is no longer active.
3. **New responsibility:** this note owns the elimination-specific item lifecycle gap and its post-elimination reachability boundary; ItemEngine remains the native owner of current item storage.
4. **Contract/invariants:** no cross-player transfer; no synthetic physical item IDs; champion pool and item inventory remain separate; terminal semantics require explicit decision; retained UUID mappings are not active unit ownership.
5. **Cross-component impacts:** PlayerEnv, ItemEngine, UnitInstance lifecycle, elimination/ranking, audit snapshot, item-target generation, pybind, replay, reset and multi-episode evaluation.
6. **Objective validation:** every current path is tied to source references; retained-map behavior is distinguished from active target reachability; terminal semantic alternatives and required tests are explicit; no runtime or tensor decisions are made.

Issue #346 remains open. This document does not approve Gate 8 or runtime implementation.
