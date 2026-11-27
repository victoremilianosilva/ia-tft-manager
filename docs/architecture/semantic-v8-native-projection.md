# Native semantic projection v8

## Contract

The production decision path consumes `tft.ppo.semantic-native-state.v8` from the native snapshot producer. The projection is computed from the authoritative `NativeAuditSnapshotHandle` held by the native batch; it does not reconstruct per-player dictionaries to calculate semantic features.

The v8 numeric carrier is contiguous `float32` with shape `[lobby_count, 8, 7958]`. Its layout remains:

- 70 global features;
- 42 entity slots × 45 features (28 board, 9 bench, 5 shop);
- 5,998 item/anvil features.

Champion IDs are transported separately as contiguous `int64` with shape `[lobby_count, 8, 42]`. Trait IDs are transported separately as contiguous `int64` with shape `[lobby_count, 8, 42, 10]`; the normalized trait values remain in the v8 numeric carrier for checkpoint and feature-layout compatibility.

## Item views and ownership

The native binding exposes six named item feature blocks as read-only, C-contiguous NumPy views into the numeric carrier:

| Block | Shape per player |
| --- | --- |
| `components` | `[10]` |
| `inventory` | `[9, 17]` |
| `recipes` | `[100, 17]` |
| `inventory_target_fit` | `[9, 37]` |
| `recipe_target_fit` | `[100, 37]` |
| `anvil_options` | `[9, 11]` |

The `anvil_state` view has shape `[3]` per player. All views share the numeric carrier's allocation as their NumPy base. They do not allocate or copy per-block storage; retaining any view retains the carrier. The Trainer validates dtype, shape, contiguity, read-only status and shared memory before flattening lobby/player dimensions with views.

The carrier is materialized once as `float32` for the Torch-facing contract. This does not claim that CPU→device transfer is zero-copy.

## Identity and hashes

The producer returns:
- decision identity (engine instance, episode, snapshot sequence, player decision sequence, player and round);
- physical entity identity (42 occupancy flags, UUIDs and five shop-offer revisions);
- item-state identity and item catalog fingerprint;
- strategic-owner provenance;
- semantic SHA-256 hashes.

Canonical JSON uses sorted object keys, compact separators and UTF-8 strings without ASCII escaping, matching the Python reference. Shared Python/C++ fixtures cover Unicode, empty arrays, null optionals, integer limits and float formatting. The snapshot parity test additionally compares full numeric rows, champion IDs, trait IDs, semantic hashes and identities.

## Production and reference paths

The Trainer requires native projection whenever the vector environment advertises native support. If the native producer is unavailable or returns an invalid carrier, production fails closed; it does not fall back to `project_native_player_state` or `build_semantic_batch`.

The Python projector remains as a test oracle and compatibility/reference implementation. It is not part of the production native hot path. Python still performs lightweight boundary validation and rollout metadata bookkeeping; loops over native players and entity slots remain in C++ and are not described as eliminated globally.

## Compatibility

The contract remains v8. Numeric feature order, normalization, champion IDs, normalized trait slots, item-state identity and semantic hash inputs are preserved. Checkpoint compatibility and the existing explicit warm-start migrations remain unchanged.
