# Phase C — Issue #573: typed entity identity projection

## Previous problem

The native audit snapshot already owned the board (28), bench (9), and shop (5) slot records, but the Python semantic projection consumed them only as mappings. Physical unit identity and shop offer lifecycle were not surfaced as a dedicated, slot-aligned projection result.

## Technical rationale

Keep the existing `TFTEngine::get_audit_snapshot` as the single producer. A physical unit is identified by its native `UnitInstance::uuid`; a shop offer is additionally scoped to its slot revision from `ShopEngine::offer_revisions()`. Champion identity is not physical identity: repeated copies of the same champion must retain distinct UUIDs.

## New responsibility

The native audit record now carries `champion_internal_id` alongside the champion API name, populated directly from the same `UnitInstance`. The pybind mapping exposes that integer without re-deriving physical identity from a string lookup. Python checks it against the loaded catalog when that catalog entry is available; dict-backed fixtures without the native integer retain the compatibility lookup.

The semantic projection emits a compact, columnar `entity_identity` value. Its 42-element `occupied` and `unit_uuids` tuples use canonical indices: board 0–27, bench 28–36, shop 37–41. The five `shop_offer_revisions` are kept slot-aligned with shop indices 37–41. Location and local slot are derived from the canonical index rather than repeated in every row. It validates occupied-unit UUID presence and uniqueness within the player's snapshot and rejects UUIDs on empty slots. `build_semantic_batch` exposes the per-player projection for downstream typed-context consumers.

## Contract and invariants

- Exactly 42 slot-aligned occupancy values and physical UUIDs, aligned with the existing 45-feature entity slots.
- Canonical index determines location/slot: board 0–27, bench 28–36, shop 37–41.
- Exactly five shop offer revisions, aligned with shop indices 37–41.
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
- Verify all 42 compact identity entries and stable slot ordering, including propagation through `build_semantic_batch`.
- Verify distinct UUIDs for repeated champion copies and across board/bench/shop.
- Reject missing occupied UUIDs, duplicate UUIDs, UUIDs on empty slots, and malformed shop revision arrays.
- Change UUIDs/revisions and prove v8 numeric features, champion IDs, and hash remain unchanged.
- Run the semantic projection test module and native binding/Engine test suite.
- Capture a repeated baseline-versus-branch benchmark with identical PPO configuration; report per-scenario results rather than claiming a gain from a single run.


## Profiling follow-up (#572 and #573)

The first 4-lobby profile showed a regression already present after #572, before the #573 identity work. The #572 native-view path performed three NumPy validation passes per item block (`isfinite`, lower-bound `any`, upper-bound `any`), each creating temporary boolean arrays, before converting values at the canonical v8 list/hash boundary. This follow-up replaces those temporary-array checks with scalar min/max reductions while preserving rejection of NaN, infinities, and values outside [0, 1]. The native binding also shares one snapshot-pinning capsule across all player views instead of allocating one capsule per player. These changes target allocation/validation overhead; only repeated benchmarks can establish whether they improve end-to-end 4-lobby performance.


## Typed entity buffers (contract v1)

The native snapshot owns a struct-of-arrays projection for all 42 canonical slots. The entity_numeric_features buffer is a C-contiguous read-only float64 view with shape (42, 11), ordered as occupied, star, cost, item count, static trait count, role, attack damage, attack speed, max health, armor, and magic resist. The entity_champion_internal_ids buffer is a C-contiguous read-only int32 view with shape (42,); empty slots use -1. Both views use canonical board (0-27), bench (28-36), shop (37-41) ordering and share the immutable snapshot capsule with item views.

Python validates version, dtype, shape, contiguity, read-only state, finiteness, slot alignment, occupancy, champion identity, and item/trait cardinalities. The numeric buffer is consumed directly on the native path: the C++ producer derives it from the exact immutable AuditUnitSnapshot records already captured for that player, so rereading and comparing ten scalar fields per occupied slot in Python would duplicate work without adding an independent source of truth. Structured records remain authoritative for champion names, UUIDs, item IDs, and trait memberships; the Python dict-backed path remains the compatibility/parity oracle. Float64 preserves the original double-valued combat attributes and v8 semantic values. No v8 feature order, numeric value, champion embedding, digest, PPO action/reward, or checkpoint contract changes.
