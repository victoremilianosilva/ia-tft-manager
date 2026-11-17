# Elimination Item Terminal Retirement Contract v1 — Draft

**Status:** bounded Stage 1 runtime delivery; review required.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem

When a player was eliminated, TFTEngine returned champion copies to the shared champion pool and cleared board/bench slots. The player's ItemEngine remained alive with loose components, completed inventory, equipped ownership keyed by now-removed unit UUIDs, and pending anvil choices. This left terminal item ownership orphaned in a still-published player snapshot.

## 2. Technical rationale

An eliminated player's items must be retired, not transferred, returned to a shared pool, or redistributed. Catalog IDs and counts are the only physical-item evidence currently owned by ItemEngine; the implementation must preserve that evidence without inventing physical instance IDs. Pending anvils are choice sets, not owned items, and are recorded separately from retired ownership.

## 3. New responsibility and owner

- ItemEngine owns the retirement transition and immutable terminal summary.
- TFTEngine::return_eliminated_player_units() invokes retirement exactly once before clearing the player's unit instances.
- TFTEngine::get_audit_snapshot() projects the terminal summary as read-only structured evidence.
- Pybind transports the fields; CppTFTLobbyWrapper validates the terminal/live-state invariant; rollout keeps the snapshot as non-tensor metadata.

## 4. Contract and invariants

At elimination, ItemEngine::retire_all_owned_state() captures component copies, completed inventory copies, equipped catalog IDs grouped by owning UnitInstance UUID, and all pending anvil choice-set identities/options. It then clears all live component, inventory, equipment and anvil stores and marks ownership as retired.

- Retired item copies are never credited to another player or shared pool.
- Live item ownership must be empty whenever item_ownership_retired=true.
- A retired engine rejects new component/item grants, anvil grants, crafting, equipping and ownership transfers.
- Retirement is idempotent; repeated calls do not duplicate terminal evidence.
- reset() clears the terminal summary for the next episode while preserving the existing monotonic anvil sequence policy.
- Catalog IDs/counts remain catalog-level evidence; no physical item/component UUID is fabricated.
- Pending anvil choice sets are retained as terminal choice evidence, not counted as owned items.

## 5. Cross-component impact

Changes ItemEngine, native elimination, AuditPlayerSnapshot, pybind serialization, Python snapshot validation and native/wrapper/API tests. It does not change champion pool behavior, item recipes, action catalog/dimensions, action masks, PPO tensors, rewards, policy selection, checkpoints, Viewer behavior or Overwolf capture.

## 6. Objective validation

- Native ItemEngine tests prove component/inventory/equipment/anvil evidence is captured, live stores are cleared, repeated retirement is idempotent, post-retirement grants are rejected, and reset reopens the next episode.
- Native lobby integration test drives an actual elimination and checks that the terminal snapshot carries retired component counts while live ownership is empty and other players receive no copies.
- Wrapper tests accept a valid terminal summary and reject live ownership after retirement or malformed retired rows.

## 7. Explicit limitations

This records catalog multiplicity and equipment owner UUID, not physical item/component instance identity or a complete mutation event ledger. It does not establish real GEP match identity or live capture validation. #346 and Stage 1 remain open pending the remaining structured producers and integrated replay acceptance.
