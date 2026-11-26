# Phase C — Issue #573: typed entity identity projection

## Previous problem

The native audit snapshot already owned the board (28), bench (9), and shop (5) slot records, but the Python semantic projection consumed them only as mappings. Physical unit identity and shop offer lifecycle were not surfaced as a dedicated, slot-aligned projection result.

## Technical rationale

Keep the existing `TFTEngine::get_audit_snapshot` as the single producer. A physical unit is identified by its native `UnitInstance::uuid`; a shop offer is additionally scoped to its slot revision from `ShopEngine::offer_revisions()`. Champion identity is not physical identity: repeated copies of the same champion must retain distinct UUIDs.

## New responsibility

The native audit record now carries `champion_internal_id` alongside the champion API name, populated directly from the same `UnitInstance`. The pybind mapping exposes that integer without re-deriving physical identity from a string lookup. Python checks it against the loaded catalog when that catalog entry is available; dict-backed fixtures without the native integer retain the compatibility lookup.

The semantic projection emits a separate `entity_identity` sequence in canonical slot order: board 0–27, bench 0–8, shop 0–4. It validates occupied-unit UUID presence and uniqueness within the player's snapshot, rejects UUIDs on empty slots, and attaches the exact shop offer revision to each shop slot. `build_semantic_batch` now exposes this projection as a per-player `entity_identity` collection, so the 42-row projection is retained for downstream typed-context consumers instead of being built and discarded.

## Contract and invariants

- Exactly 42 identity rows, aligned with the existing 45-feature entity slots.
- Each row carries location, slot, occupancy, and physical unit UUID.
- Native occupied unit records carry a non-negative `champion_internal_id` from `UnitInstance`; when Python has the matching catalog entry, the values must agree.
- Shop rows carry their slot-aligned non-negative offer revision; board/bench rows carry no offer revision.
- UUID denotes a physical unit copy, not a champion definition or player ownership relation.
- Shop offer revision denotes the current lifecycle generation of a slot, not physical unit identity.
- Empty slots have an empty UUID.
- This identity metadata is deliberately excluded from semantic v8 numeric features, champion IDs, and SHA-256 input. The PPO tensor/checkpoint contract remains unchanged.
- The existing dict-backed projection remains the parity oracle; native snapshot serialization already provides UUIDs and offer revisions from the same immutable snapshot owner.

## Impact

Adds an explicit identity result for audit and subsequent typed-context integration without changing actions, masks, rewards, logits, sampling, checkpoints, or Engine behavior. No duplicate UUID generator or shop revision producer is introduced.

## Validation criteria

- Verify native champion internal IDs are populated from the same physical UnitInstance and checked against catalog identity.
- Verify all 42 rows and stable slot ordering, including propagation through `build_semantic_batch`.
- Verify distinct UUIDs for repeated champion copies and across board/bench/shop.
- Reject missing occupied UUIDs, duplicate UUIDs, UUIDs on empty slots, and malformed shop revision arrays.
- Change UUIDs/revisions and prove v8 numeric features, champion IDs, and hash remain unchanged.
- Run the semantic projection test module and native binding/Engine test suite.
- Capture a repeated baseline-versus-branch benchmark with identical PPO configuration; report per-scenario results rather than claiming a gain from a single run.


## Profiling follow-up (#572 and #573)

The first 4-lobby profile showed a regression already present after #572, before the #573 identity work. The #572 native-view path performed three NumPy validation passes per item block (`isfinite`, lower-bound `any`, upper-bound `any`), each creating temporary boolean arrays, before converting values at the canonical v8 list/hash boundary. This follow-up replaces those temporary-array checks with scalar min/max reductions while preserving rejection of NaN, infinities, and values outside [0, 1]. The native binding also shares one snapshot-pinning capsule across all player views instead of allocating one capsule per player. These changes target allocation/validation overhead; only repeated benchmarks can establish whether they improve end-to-end 4-lobby performance.
