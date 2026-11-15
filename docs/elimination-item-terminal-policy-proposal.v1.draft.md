# Elimination Item Terminal Policy — Decision Proposal v1

**Status:** proposal only; not an accepted game rule or runtime contract.  
**Target:** `new-arquiteture`.  
**Tracking:** issue #346.  
**Scope:** native item ownership after a player is eliminated.

## 1. Prior problem

The current elimination path returns champion copies to the shared UnitPool and clears the eliminated player's board/bench UnitInstances. It does not clear the player's ItemEngine UUID-keyed equipment map, loose component inventory, completed-item inventory or pending anvil queue. The PlayerEnv retains its ItemEngine until Engine reset.

The result is a terminal ownership ambiguity: item state remains stored after the physical units that owned some items have left active ownership. The audit snapshot exposes some remaining item inventory/queue fields, but not the complete UUID-keyed equipment map, and AuditPlayerSnapshot has no explicit alive/eliminated field.

No source-backed game-rule contract was found that defines whether eliminated-player items should be discarded, retained for replay, or returned to that player's own bag. This proposal therefore does not claim to reproduce an authoritative TFT rule.

## 2. Technical rationale

Sale, merge and elimination are different transitions:

- **Sale** removes one active unit while the player remains active; equipment returns to that same player's usable inventory.
- **Merge** consumes two physical units while the player remains active; equipment transfers to the surviving purchased UnitInstance, with overflow returned to that same player's inventory.
- **Elimination** terminates the player's ability to make further decisions. It must not silently reuse sale semantics if that would imply the player's inventory remains active or transferable.

The item catalog currently represents catalog-ID multiplicity, not physical item-instance identity. Any terminal policy must operate on those existing owner-scoped containers and must not invent item UUIDs or move items across players.

## 3. Candidate policies

### A. Retire/discard all item state at elimination

After capturing the terminal diagnostic record, retire all item ownership for the eliminated player:
- remove UUID-keyed equipped mappings;
- clear loose component and completed-item inventories;
- clear pending anvil choices;
- prevent any further item action from being considered active;
- preserve only an immutable terminal summary if replay/diagnostics require it.

**Advantages:** no orphan UUID mappings; no ambiguity about active ownership; no accidental post-elimination action; clear reset boundary.

**Costs:** item inventory is no longer visible as live state after elimination unless a terminal snapshot is captured first; any downstream metric/reward consumer must be checked before clearing counters.

### B. Return equipment to the eliminated player's own bag, then freeze

Move every equipped catalog-ID copy back to that same player's inventory, then mark the inventory terminal/inaccessible until Engine reset. Pending choices are explicitly retired. No item is transferred to another player.

**Advantages:** preserves a complete per-player item count in one container before terminal freeze; can simplify terminal inventory accounting.

**Costs:** the bag remains stored despite being unusable; terminal snapshots still need explicit status; it does not by itself solve the need to retire the player's item state.

### C. Retain all state unchanged until Engine reset

Keep the current behavior.

**Advantages:** preserves current internal state for post-match inspection without adding a new terminal transition.

**Costs:** leaves orphaned UUID-keyed equipment mappings; does not distinguish active from terminal inventory; makes audit consumers depend on an implicit reset for cleanup; is not an explicit ownership contract.

## 4. Provisional recommendation

Prefer **Policy A — explicit retirement/discard**, with a terminal snapshot captured before retirement.

This is a recommendation, not a frozen decision. It follows from the current ownership model: the eliminated player cannot act, item inventories are player-owned rather than a shared pool, and no cross-player item transfer is supported or desired by the audited contract. It avoids pretending that a dead player's bag remains an active resource.

Before accepting Policy A, inspect all ItemEngine metric consumers and placement/reward attribution to determine whether counters must survive terminalization. If metrics are needed, terminalization should clear owned item collections while preserving the required counters in a separate terminal summary; it should not blindly call the generic `ItemEngine::reset()` if that erases evidence needed for reward or replay.

## 5. Proposed owner and boundaries

- **TFTEngine::Impl elimination coordinator:** owns the decision that a player transitions from active to eliminated and invokes one terminal item lifecycle operation exactly once.
- **ItemEngine:** remains the sole owner of item collections and performs the atomic owner-scoped retirement/terminal freeze.
- **AuditSnapshot/terminal diagnostic producer:** records the selected disposition, eliminated status, item counts by catalog ID, and the number of retired UUID-keyed equipment entries under the same Engine episode/snapshot identity.
- **Viewer/replay:** consumes the terminal summary read-only; it does not infer ownership from empty board/bench slots.
- **PPO/Actor/Critic:** no new feature or target is implied by this proposal. Any future observation delivery requires separate Gate 8 authorization and projection review.

## 6. Proposed invariants

1. Elimination retires the player's active UnitInstance ownership exactly once.
2. No equipped item, component, completed item or pending choice is transferred to another player.
3. No UUID-keyed equipped entry remains classified as active ownership after terminalization.
4. The terminal disposition is explicit: retired/discarded or returned-to-owner-bag-and-frozen; no implicit retention.
5. Terminalization is idempotent and safe under repeated elimination/reset handling.
6. ItemEngine remains the authority for item counts; no synthetic per-item IDs are introduced.
7. Terminal diagnostic data is immutable and correlated to the same Engine episode and player seat.
8. Metrics required for placement/reward attribution are preserved deliberately, not accidentally erased by a generic reset.
9. A dead player cannot receive an active item target or an ignored forced action.
10. Engine reset starts a new item lifecycle without resurrecting prior terminal ownership.

## 7. Cross-component impacts

TFTEngine elimination and reset, PlayerEnv, ItemEngine, UnitInstance lifecycle, shared champion pool separation, AuditSnapshot/public-state correlation, item-target masks, placement/reward attribution, pybind, Viewer, replay and multi-episode evaluation.

The proposal does not change the champion pool. Champion copies returned on elimination remain governed by the existing UnitPool lifecycle.

## 8. Objective validation criteria

Before implementation acceptance:

1. Eliminate a player with equipped items on board and bench, loose components, completed items and (if a producer is later added) a pending anvil.
2. Assert every champion copy is returned to UnitPool exactly once.
3. Assert the selected item policy is applied exactly once to every equipped mapping and inventory entry.
4. Assert no item becomes available to another player.
5. Assert no eliminated UUID remains in active item-target enumeration or active owner maps.
6. Assert terminal diagnostic status and disposition are correlated to the exact Engine episode/player.
7. Assert reward/placement metrics are preserved according to the chosen reward contract.
8. Assert repeated elimination handling and Engine reset are idempotent.
9. Assert two consecutive matches cannot expose prior terminal item state.
10. Assert full-match replay reproduces the same terminal item disposition.

These are future acceptance tests, not tests executed by this proposal.

## 9. Architecture reconstruction review

1. **Prior problem:** elimination cleared units but left ItemEngine ownership containers without an explicit terminal policy.
2. **Technical rationale:** sale/merge semantics do not define elimination; implicit retention creates orphaned ownership and weak diagnostics.
3. **New responsibility:** the elimination coordinator owns the terminal transition; ItemEngine owns atomic item retirement; the audit producer owns immutable terminal evidence.
4. **Contract/invariants:** no cross-player transfer, no active orphan UUID, explicit disposition, idempotence, exact Engine/player correlation, deliberate metric preservation.
5. **Cross-component impacts:** Engine, PlayerEnv, ItemEngine, UnitInstance, masks, rewards, audit snapshot, pybind, Viewer and replay.
6. **Objective validation:** the source gap and three policy alternatives are explicit; recommendation is marked provisional; acceptance criteria are testable; no runtime behavior or tensor layout is changed.

## 10. Decision and gate status

**Decision required:** accept Policy A, choose Policy B, or retain a different explicit terminal policy.

Until this decision is accepted and Gate 8 is authorized, no runtime implementation is permitted. Issue #346 remains open. Gate 8 remains blocked.
