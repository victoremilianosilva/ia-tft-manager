# Item Inventory Slot-to-Action Binding Audit v1 — Draft

**Status:** source-backed action-binding audit; documentation only.
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).
**Base:** `new-arquiteture`.

## 1. Prior ambiguity

The item audits established that inventory contents are catalog IDs and that the six-wide policy action reuses positional fields for item operations. What remained unproven was the exact relationship between the ordered inventory observed by the Engine, the item-inventory legality mask, the policy's positional action, and the native mutation that consumes an inventory entry.

This audit traces that relationship without changing runtime, masks, action dimensions, tensor layout, or training.

## 2. Authoritative inventory representation

ItemEngine owns components_, inventory_, and equipped_. The inventory is an ordered std::vector<std::string> of catalog item IDs; it is not a collection of physical item-instance records. The public inventory() accessor returns that vector by const reference (cpp/include/items/ItemEngine.hpp, constructor/reset and accessors).

Consequences:
- Repeated entries represent multiplicity of the same catalog item ID.
- An inventory position is an address into the current vector, not a durable item identity.
- The audited ItemEngine representation does not attach a unique item-instance ID, acquisition event ID, or inventory revision to each entry.
- Components are also stored as catalog ID strings in a vector. The action identifies component catalog positions, not physical component instances.

## 3. Observation and mask projection

The native observation builder writes nine positional semantic inventory feature records. For each slot in [0, 8], it reads item_state->inventory()[slot] when present and encodes the corresponding catalog definition; an unoccupied slot receives a zero-initialized feature record (cpp/src/lobby/TftEngine.cpp, semantic item-state block beginning around line 1600).

Native mask generation independently reads the current ItemEngine inventory vector and marks each position below min(9, inventory.size()) as legal (TftEngine.cpp:1060-1070). It then enables ordinary type-7 equip only when at least one inventory position and one legal target exist (TftEngine.cpp:1088-1090).

This establishes a positional correspondence at generation time:
- Observation inventory feature slot i describes the catalog definition at inventory()[i].
- item_inventory_mask[i] means that current inventory position i exists.
- Neither record carries a physical item ID/instance ID or inventory revision alongside that position.

The diagnostic audit snapshot separately copies the ordered item_inventory catalog-ID vector (TftEngine.cpp, get_audit_snapshot(), around lines 6750-6780). That is useful for inspection, but is not itself proof that the ordered vector is part of the training-facing PPO input.

## 4. Policy action to native mutation

The action remains six integers with dimensions [9, 5, 9, 28, 28, 28] (cpp/include/lobby/TftEngine.hpp). For ordinary type-7 equip:
- action[1] is interpreted as the inventory position.
- action[2] is interpreted as the board/bench target position.
- The native decoder resolves the target to a live UnitInstance, obtains its UUID, then reads inventory()[action[1]] to obtain the catalog item ID (TftEngine.cpp:5340-5380).
- The resulting ItemActionCommand is applied through ItemEngine, which finds and erases the first matching catalog ID from inventory_, then appends that ID to equipped_[target.uuid] (ItemEngine.hpp, equip(), around lines 250-280).

For type 8 craft-and-equip, action[1] and action[2] address component catalog positions, while action[3] addresses the target. The native decoder maps those positions to catalog component IDs. ItemEngine consumes component occurrences by finding matching IDs in its vector and erasing the two selected occurrences, then appends the recipe result to inventory (TftEngine.cpp:5360-5380; ItemEngine.hpp, craft(), around lines 220-250).

For pending anvil state, type 7 is not inventory equip: action[1] selects the pending queue's option position, while target index zero is a forced sentinel. The pending-anvil branch takes precedence in the native decoder. See the separate Item Action Policy-to-Native Binding Audit.

## 5. What is and is not proven

| Concern | Evidence-backed disposition |
|---|---|
| Inventory producer/storage | `native_observed`; ordered catalog-ID vector |
| Inventory semantic observation | `native_observed_positional_projection`; nine catalog-stat feature records |
| Inventory legality | `native_observed_positional_mask`; first nine current vector positions |
| Type-7 equip binding | `native_observed_positional_action_binding`; slot resolves against current vector |
| Item ownership after equip | `native_observed`; catalog ID moves from inventory vector to UUID-keyed equipped map |
| Duplicate catalog IDs | `native_observed_multiplicity`; identical IDs are not individually distinguishable |
| Durable item-instance identity | `not_produced` in audited ItemEngine inventory representation |
| Inventory revision / slot generation | `not_produced` in audited inventory contract |
| Action-to-mask decision envelope | `not_established` by the six-position action and mask structures alone |
| Diagnostic snapshot to PPO tensor delivery | `not_proven`; diagnostic snapshot and training observation are separate surfaces |

Because identical catalog IDs are semantically interchangeable in the current representation, erasing the first matching ID is not by itself evidence of incorrect item ownership. The proven limitation is that the system cannot distinguish two physical copies or identify which acquisition occurrence was selected.

This audit does not claim a stale-action race occurs. It establishes that the native positional structures themselves do not carry a shared inventory revision or typed decision identity. Whether the wrapper serializes observation, masks and action atomically for every training step must be established at the Engine-to-Python/Rollout boundary.

## 6. Cross-component implications

- **Engine / ItemEngine:** authoritative ordered catalog-ID vectors and UUID-keyed equipped ownership.
- **Observation:** semantic features are position-based and omit typed item-instance identity.
- **Masks:** legality is generated from current vector cardinality and target state; masks remain separate final legality inputs.
- **Policy:** action arguments are positional indices; they do not encode the catalog ID or inventory revision directly.
- **Native decoder:** resolves the index against current state, then applies the semantic catalog ID.
- **Diagnostics:** audit snapshot can expose the ordered catalog-ID list, but must not be confused with PPO input.
- **Replay:** reproducible replay needs the same pre-action inventory ordering, masks and action context; a catalog ID alone is insufficient to reconstruct which positional decision was sampled when repeated entries exist.

## 7. Remaining proof and acceptance scenarios

1. Trace the exact Python wrapper call order for observation, masks, action submission and next-state retrieval; record whether one native step boundary guarantees they refer to the same pre-action state.
2. Trace the exact rollout storage/replay record and determine whether inventory order, action masks and episode/player/decision identity are retained or only the flat observation/action.
3. Add native/Python replay fixtures for: one inventory item, duplicate same-ID items, different item IDs with removal of an earlier slot, craft insertion after inventory entries, equip followed by another equip, pending anvil followed by ordinary equip, and reset between episodes.
4. Verify invalid/out-of-range slot rejection at the native boundary and confirm the mask used to sample the action belongs to that same decision.
5. Decide in a future contract revision whether catalog-ID multiplicity is sufficient or whether physical item occurrences are required. Do not synthesize item-instance IDs from vector positions.
6. Keep inventory positions, component catalog positions, anvil option positions and unit UUIDs as distinct identity domains.

## 8. Architecture reconstruction review

1. **Prior problem:** the item inventory was known to be positional, but its observation/mask/action/native-consumption correspondence had not been recorded end-to-end.
2. **Technical justification:** the policy samples an index, while the Engine resolves and mutates an ordered vector; replay and identity claims must preserve that exact pre-action context.
3. **New responsibility:** this audit owns the evidence-backed binding between ItemEngine inventory storage, observation features, item masks, policy action positions and native consumption.
4. **Contract and invariants:** catalog ID is semantic item type, not physical item occurrence; vector position is ephemeral; masks are separate legality inputs; anvil option positions are a different domain; no synthetic IDs or revision values.
5. **Cross-component impacts:** ItemEngine, native observation/mask generation, action decoder, policy sampling/replay, Python wrapper, RolloutBuffer, diagnostic snapshot and future replay manifests.
6. **Objective validation:** source locations for storage, observation, masks, action decoding and mutation are identified; missing wrapper/rollout correlation and concrete replay scenarios are explicit. Documentation only.

No runtime, schema, tensor-layout, PPO architecture, reward, mask, training, checkpoint, Viewer or Overwolf implementation is authorized by this audit. Issue #346 remains open; Gate 8 remains blocked.