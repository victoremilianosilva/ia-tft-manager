# Phase C — Issue #573: typed entity identity projection

## Previous problem

The native audit snapshot already owned the board (28), bench (9), and shop (5) slot records, but the Python semantic projection consumed them only as mappings. Physical unit identity and shop offer lifecycle were not surfaced as a dedicated, slot-aligned projection result.

## Technical rationale

Keep the existing `TFTEngine::get_audit_snapshot` as the single producer. A physical unit is identified by its native `UnitInstance::uuid`; a shop offer is additionally scoped to its slot revision from `ShopEngine::offer_revisions()`. Champion identity is not physical identity: repeated copies of the same champion must retain distinct UUIDs.

## New responsibility

The semantic projection emits a separate `entity_identity` sequence in canonical slot order: board 0–27, bench 0–8, shop 0–4. It validates occupied-unit UUID presence and uniqueness within the player's snapshot, rejects UUIDs on empty slots, and attaches the exact shop offer revision to each shop slot.

## Contract and invariants

- Exactly 42 identity rows, aligned with the existing 45-feature entity slots.
- Each row carries location, slot, occupancy, and physical unit UUID.
- Shop rows carry their slot-aligned non-negative offer revision; board/bench rows carry no offer revision.
- UUID denotes a physical unit copy, not a champion definition or player ownership relation.
- Shop offer revision denotes the current lifecycle generation of a slot, not physical unit identity.
- Empty slots have an empty UUID.
- This identity metadata is deliberately excluded from semantic v8 numeric features, champion IDs, and SHA-256 input. The PPO tensor/checkpoint contract remains unchanged.
- The existing dict-backed projection remains the parity oracle; native snapshot serialization already provides UUIDs and offer revisions from the same immutable snapshot owner.

## Impact

Adds an explicit identity result for audit and subsequent typed-context integration without changing actions, masks, rewards, logits, sampling, checkpoints, or Engine behavior. No duplicate UUID generator or shop revision producer is introduced.

## Validation criteria

- Verify all 42 rows and stable slot ordering.
- Verify distinct UUIDs for repeated champion copies and across board/bench/shop.
- Reject missing occupied UUIDs, duplicate UUIDs, UUIDs on empty slots, and malformed shop revision arrays.
- Change UUIDs/revisions and prove v8 numeric features, champion IDs, and hash remain unchanged.
- Run the semantic projection test module and native binding/Engine test suite.
- Capture a repeated baseline-versus-branch benchmark with identical PPO configuration; report per-scenario results rather than claiming a gain from a single run.
