# Phase C — zero-copy item feature transport (#572)

## Previous problem

The six numeric item blocks already lived in `AuditPlayerSnapshot`, but the generic snapshot serializer expanded them into nested Python lists. The semantic projection then traversed each scalar in Python to validate shape, finiteness, and the `[0, 1]` range. This added allocation and interpreter overhead without adding information.

## Technical rationale

Keep the native snapshot as the single owner and expose its fixed-size `float32` arrays as NumPy views. A capsule retains a `shared_ptr<const AuditSnapshot>`, so each view pins the exact immutable snapshot independently of the engine, wrapper, mapping, and intermediate references. NumPy validates the six blocks in vectorized operations; conversion to the ordered Python-float sequence remains at the v8 canonicalization boundary so the hash input is unchanged.

## New responsibility

- C++ binding: publish read-only, C-contiguous NumPy views for the six existing item blocks.
- Snapshot mapping: retain the native owner through the capsule and preserve view identity when metadata is deep-copied.
- Semantic projection: use vectorized validation for native arrays and retain the strict recursive path for dict-backed fixtures and external audit data.

## Contracts and invariants

| Block | Shape | dtype |
| --- | ---: | --- |
| `item_component_features` | `(10,)` | `float32` |
| `item_inventory_features` | `(9, 17)` | `float32` |
| `item_recipe_features` | `(100, 17)` | `float32` |
| `item_inventory_target_fit` | `(9, 37)` | `float32` |
| `item_recipe_target_fit` | `(100, 37)` | `float32` |
| `pending_anvil_option_features` | `(9, 11)` | `float32` |

All views are read-only and C-contiguous. Values, row/column order, dimensions, and meanings remain sourced from the same native arrays. The complete AuditSnapshot and dict-backed fallback remain available. No item feature, hash algorithm, observation, mask, reward, action, Policy, GAE, loss, optimizer, or checkpoint contract is intentionally changed.

## Impacts

The generic Python list expansion is bypassed for these six blocks on the native handle path. Snapshot serialization for all other fields is unchanged. The semantic v8 hash continues to consume the same ordered scalar values; this change only changes transport and validation.

## Validation criteria

- CI must compile the pybind11 extension and run native/Python tests.
- Projection tests compare numeric output, entity IDs, and v8 SHA-256 between list-backed and immutable NumPy-backed inputs.
- Native-view tests must cover shape, dtype, contiguity, read-only flags, exact values, and owner lifetime after wrapper/engine references are dropped.
- Performance gate requires same-workload baseline and post-change profiles, including semantic projection and PPO-active end-to-end measurements. CI success alone is not a performance profile.

## Current evidence

The implementation adds pinned NumPy views, vectorized validation, and projection parity coverage. The PR's CI run is the build/test gate. The performance gate remains open until comparable baseline and post-change profiles are recorded; #572 must not be closed before that evidence is available.
