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


## 7. Follow-up source and reachability verification — 2026-11-15

### Exact elimination path

The current native path is confirmed in `cpp/src/lobby/TftEngine.cpp`:

1. `eliminate_players()` marks the player dead/eliminated, assigns placement, and calls `return_eliminated_player_units(i)`.
2. `return_eliminated_player_units()` returns current shop offers, returns champion copies from board and bench to the shared champion pool, and resets those board/bench optionals.
3. It does **not** call `ItemEngine::return_equipped_to_inventory()`, clear the corresponding UUID entries, or invoke `ItemEngine::reset()`.
4. The eliminated player's `item_engine` remains owned by its PlayerEnv. `ItemEngine::reset()` is called in the later Engine reset lifecycle, not in this elimination helper.
5. Consequently, UUID-keyed equipment entries survive after the corresponding UnitInstances have been removed from active board/bench ownership. The entries are orphaned relative to active unit ownership; this does not prove they are exposed as active item targets or transferred to another player.

The exact active-target boundary remains: item-target generation enumerates current board/bench UnitInstances, so removed units are no longer valid active targets through that path. Retained diagnostic/internal map state and active target reachability are distinct.

### Stale source comment

`cpp/include/lobby/TftEngine.hpp` still says “A geração efetiva do UUID será implementada posteriormente.” This is stale: `UnitInstanceFactory::create()` assigns `unit.uuid = generate_uuid()`, and `generate_uuid()` is implemented in `cpp/src/lobby/UnitInstanceFactory.cpp`. This is a documentation/source-comment discrepancy only; no header edit is included here.

### Regression evidence boundary

The inspected `cpp/tests/test_item_engine.cpp` verifies explicit return-to-inventory for a sold/removed UUID and verifies merge transfer. The inspected `cpp/tests/test_tft_engine_pool.cpp` covers pool reset, invalid sale, and item diagnostics/combat propagation, but contains no elimination-specific equipped-item cleanup case and no direct assertion against `return_eliminated_player_units()`. These tests therefore do not establish terminal elimination semantics.

This follow-up narrows the previous finding: retained equipment is confirmed by the implementation path; cross-player transfer is not observed; active target reachability is separate; elimination cleanup is not regression-tested in the inspected test files.

### Updated acceptance criteria

- Equip items on both board and bench units, eliminate the player while other players remain active, and inspect the eliminated PlayerEnv's ItemEngine state.
- Assert the selected terminal policy explicitly: return items to that eliminated player's own bag before terminal disposal, or retire/clear them; do not transfer to another player.
- Assert all UUID-keyed entries for eliminated physical units are handled exactly once.
- Assert removed UUIDs are absent from active item-target enumeration while the match continues.
- Assert the policy is stable across elimination, full-match completion, reset, and consecutive episodes.
- Assert audit output distinguishes retained terminal state from active ownership.

## 8. Architecture reconstruction review

1. **Prior problem:** the original audit identified missing cleanup but needed stronger source-path and test-coverage boundaries.
2. **Technical justification:** elimination happens during a continuing lobby, so waiting for full Engine reset leaves a period where orphaned item state persists; sale and merge semantics cannot be assumed to define elimination.
3. **New responsibility:** this addendum owns the exact elimination call chain, retained-state reachability, stale UUID comment discrepancy, and elimination-specific test gap.
4. **Contract/invariants:** champion pool accounting is separate from item ownership; no cross-player transfer; no active target without a live UnitInstance; terminal item policy must be explicit and exactly-once.
5. **Cross-component impacts:** TFTEngine elimination, PlayerEnv, ItemEngine, UnitInstance, masks/item-target generation, audit snapshot, reset, replay and multi-episode evaluation.
6. **Objective validation:** call chain traced through native source; item engine reset boundary identified; two relevant test files checked for elimination coverage; no runtime behavior changed.

Issue #346 remains open. Gate 8 remains blocked.


## 9. Follow-up: orphan observability and mask reachability — 2026-11-15

A second source pass narrows what can be observed after elimination:

- `get_audit_snapshot()` serializes board and bench units through `describe_unit()`; equipped IDs there come from each live `UnitInstance::items` mirror. After elimination clears those optionals, the orphaned `ItemEngine::equipped_` map is not serialized as a complete UUID-keyed collection.
- The same audit snapshot separately exposes ItemEngine components, inventory, pending anvil and last-item-action metadata. It does not enumerate every `equipped_` map entry.
- Strategic Planner item evidence builds `equipped_by_unit_uuid` only while iterating current board and bench UnitInstances. Eliminated UUIDs therefore do not enter that evidence binding.
- Item mask target generation calls `item_target_unit()` for each board/bench target slot. A cleared slot cannot target the retained orphan UUID. Type-7 equip is enabled only when both inventory and a live target are available.
- This establishes a visibility/reachability gap: retained orphan entries are not exposed by these two structured projections and are not selectable through the ordinary active target mask. It does not prove they are leaked to another player or used by the policy.

The terminal-state decision remains unresolved. If the chosen policy is discard, the Engine needs explicit owner-scoped cleanup and a way to prove the orphan mapping was retired. If the chosen policy is return-to-owner-bag, the return must occur before the terminal inventory is frozen/cleared. In either case, observability must report the terminal disposition without exposing eliminated items as active equipment.

