# Phase C — zero-copy transport of native item feature blocks

## Previous problem

The native audit snapshot stored six fixed-size item feature blocks in C++ but serialized them as nested Python lists. That materialized every numeric element before the semantic projection could validate and flatten the data, adding allocation and conversion overhead to the PPO observation path.

## Technical rationale

The authoritative values already live in fixed-size arrays inside an immutable `AuditSnapshot`. The transport should expose those exact buffers as read-only NumPy views, rather than copying them into intermediate Python containers. The view must retain shared ownership of the exact snapshot so its lifetime is independent of the Engine, wrapper, mapping, and caller.

The current architecture lazily projects each player through `NativeAuditSnapshotHandle.player(index)`. The zero-copy contract is therefore implemented at that per-player boundary, not by bypassing the lazy player owner or replacing the current snapshot architecture.

## New responsibility

- C++ `NativeAuditSnapshotHandle.player(index)` creates a shared-owner capsule and exposes the six item blocks as read-only NumPy views.
- The player serializer emits the views directly when an owner is supplied; list serialization remains available for existing non-native snapshot serialization paths.
- `semantic_observation.py` validates native arrays for exact `float32` dtype, exact shape, C-contiguity, read-only status, finite values, and the existing [0, 1] range.
- The semantic v8 projection converts the validated arrays to the canonical ordered Python-float sequence only at the existing projection/hash boundary. This preserves the v8 numeric order and hash contract.
- Dict-backed fixtures and external sequence producers retain their recursive compatibility path.

## Contract and invariants

The six blocks and required shapes are:

| Field | Shape |
| --- | --- |
| `item_component_features` | `(10,)` |
| `item_inventory_features` | `(9, 17)` |
| `item_recipe_features` | `(100, 17)` |
| `item_inventory_target_fit` | `(9, 37)` |
| `item_recipe_target_fit` | `(100, 37)` |
| `pending_anvil_option_features` | `(9, 11)` |

Every native view is `float32`, C-contiguous, and non-writeable. Its base capsule owns a `shared_ptr<const AuditSnapshot>`; no pointer into a temporary player dictionary or mutable Engine buffer is exposed. The six values, dimensions, order, and semantic v8 hash remain unchanged.

## Impacts

The change is limited to the native item-feature transport and its semantic projection boundary. It does not change item feature producers, values, action masks, actions, rewards, PPO policy/model contracts, training objectives, checkpoints, or the strategic owners. The existing lazy per-player snapshot interface remains authoritative.

## Validation criteria

- Native binding tests assert all six shapes, dtype, contiguity, read-only status, and that retained views remain readable after wrapper/Engine release.
- Semantic projection tests compare list-backed and NumPy-backed v8 numeric output, champion IDs, and SHA-256; writable and non-finite arrays are rejected.
- Full CI must pass, including native compilation, Python tests, sanitizers, and the PPO training smoke.
- Baseline/post-change performance profiles, including a PPO-active profile, remain a separate evidence gate. CI success alone is not performance evidence.


## Performance follow-up

The initial 4-lobby profile showed a regression relative to its baseline. Inspection found that native item views were validated with three NumPy passes per block, creating temporary boolean arrays before the required canonical v8 conversion. The follow-up in the #573 implementation uses scalar min/max reductions to validate finiteness and [0, 1] bounds without those temporary arrays. It also shares one snapshot-pinning capsule across the eight player mappings rather than allocating one capsule per player. The v8 projection still materializes canonical Python floats at its hash/tensor boundary; the native views remain read-only and lifetime-pinned. These changes are hypotheses to reduce overhead and must be measured with repeated, matched benchmarks.
