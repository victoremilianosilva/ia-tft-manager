# Shop Offer Identity and Reroll Lifecycle Audit v1 — Draft

**Status:** source-backed static audit; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.  
**Related:** [Board/Bench/Shop Producer Audit](board-bench-shop-producer-audit.v1.draft.md); [Unit Instance Copy and Test Hook Audit](unit-instance-copy-test-hook-audit.v1.draft.md); [Native Engine Instance and Episode Identity Scope Audit](native-engine-instance-episode-identity-scope-audit.v1.draft.md).

## 1. Purpose

Clarify what identity actually exists for a shop offer, how an offer changes through roll, reroll, purchase and reset, and distinguish the physical `UnitInstance` identity from the identity of a shop opportunity/snapshot.

This is a documentation-only audit. No shop, Engine, observation, PPO, mask, schema or runtime code is changed.

## 2. Native shop representation

`ShopEngine` stores exactly `kShopSlots` optional `UnitInstance` values in `offers_`. A slot is an array position, not a separately identified offer record. The class has:
- a reference to the shared `UnitPool`;
- a reference to the Engine's `UnitInstanceFactory`;
- its own seeded `std::mt19937_64`;
- the five optional physical unit instances;
- a lock flag and test-only next-roll fixture.

There is no offer ID, offer revision, reroll generation, snapshot ID, creation sequence, or explicit offer provenance field in the ShopEngine state.

### 2.1 What identity does exist

Every normally drawn offer is created through `UnitInstanceFactory::create()`, which assigns a UUID-shaped `UnitInstance::uuid`. This identifies the physical unit instance generated for the offer under the already documented UUID lifecycle constraints.

The audit snapshot copies the shop's UnitInstance into the corresponding shop slot snapshot; therefore the diagnostic snapshot can expose the physical UUID. This does **not** make that UUID an offer-generation ID, nor does it establish a typed offer lifecycle/revision contract.

The distinction is:
- **Unit instance identity:** identifies the physical champion instance represented by the offer and can continue after purchase.
- **Offer opportunity identity:** identifies that this particular instance was offered to this player in this shop generation, at this slot and snapshot.
- **Offer slot:** current positional location only; it can refer to a different physical instance after reroll.

The first exists as `UnitInstance::uuid`; the second is not separately modeled; the third is the array index.

## 3. Generation, reroll and reset lifecycle

### 3.1 Initial shop creation

During player initialization, the Engine constructs each player's ShopEngine with seed:

`Engine seed + player index + episode_id`

It immediately rolls the shop at the player's starting level. Each shop has its own RNG, while all shops share the Engine's UnitInstanceFactory and UnitPool.

### 3.2 Normal roll and reroll

`ShopEngine::roll()`:
1. returns all current offers to the shared champion pool;
2. selects a cost using level-dependent odds and the ShopEngine RNG;
3. draws a champion ID from the pool;
4. creates a new UnitInstance through the shared factory;
5. stores that instance at the positional shop slot.

A locked shop skips a non-forced roll. `reroll()` calls `roll(level, true)`, bypassing the lock. A successful reroll replaces the old physical offer instances; it does not increment or publish an offer generation counter.

The old offers' champion copies return to the pool. The old offer objects/UUIDs are not retained in a shop history by this class. A new draw creates new UnitInstances, subject to the factory's deterministic seeded UUID sequence.

### 3.3 Purchase

The BUY action carries a positional `shop_slot`. The native action path obtains the offer with `shop.take_unit(shop_slot)`, which moves the existing UnitInstance out of the offer array and clears that slot. On successful purchase, the same UnitInstance is moved to the player's bench.

Thus the physical UnitInstance UUID survives the shop→bench ownership transfer. The slot does not survive as identity and may later contain a different offer.

### 3.4 Engine reset

Engine reset destroys each player's current ShopEngine after returning its offers, then reconstructs the player shops. The new ShopEngine RNG seed includes the incremented episode ID, while the shared UnitInstanceFactory is reconstructed from the base Engine seed. Therefore:
- the random offer draw stream is episode/player-seeded;
- the UUID stream is factory-seeded independently of episode ID;
- an offer UUID is not a globally unique episode/offer key.

## 4. Evidence and delivery boundaries

| Surface | Proven capability | Missing capability |
|---|---|---|
| Native ShopEngine | Five optional UnitInstances; positional slots; lock; seeded draw/reroll | Offer ID, revision, generation, source sequence |
| UnitInstance | Physical UUID, champion ID, star tier | Offer-opportunity identity/provenance |
| Native audit snapshot | Copies shop UnitInstance into slot snapshot, including unit fields | Typed offer-generation envelope |
| Native strategic action snapshot | Shop champion IDs by slot for diagnostic resolution | Stable offer identity; it stores champion IDs in positional slots |
| PPO observation | Fixed numeric shop slot feature blocks, as documented by prior producer audit | Physical UUID, offer ID/revision, exact offer snapshot identity |
| BUY action | Shop slot index plus action type | Bound reference to a specific immutable offer snapshot |

The prior board/bench/shop and PPO projection audits remain authoritative for the flat observation finding. This note refines the identity interpretation: a diagnostic shop snapshot can carry a physical UnitInstance UUID even though the PPO feature projection does not carry it, and neither surface currently establishes a distinct offer-generation identity.

## 5. Correct semantic status

- Physical shop UnitInstance: **native observed** in the native/audit snapshot surfaces.
- UnitInstance UUID: **native observed**, subject to deterministic same-seed repetition and Engine/episode scoping constraints already documented.
- Shop slot index: **native observed positional metadata**, not stable identity.
- Offer ID: **not produced**.
- Offer revision/reroll generation: **not produced**.
- Offer snapshot/decision sequence binding: **not correlated** to the current PPO observation/mask/action transition contract.
- Offer provenance beyond the current native shop state: **not established**.
- PPO delivery of physical UUID or offer identity: **not exposed to PPO** in the audited flat feature projection.

No synthetic offer ID, revision or generation may be inferred from slot, champion ID, UUID, RNG draw order, timestamps or observation array position.

## 6. Required post-Gate-8 acceptance

1. A reroll must invalidate prior offer-opportunity references even if the same champion appears again.
2. A slot reused after reroll must not be mistaken for the prior offer.
3. A purchased offer must retain the physical UnitInstance identity while its ownership domain changes from shop to bench.
4. An empty slot must remain distinct from a missing/unavailable shop snapshot.
5. Locking must preserve the exact current offer snapshot; forced reroll must advance it.
6. Same champion in multiple shop slots must remain distinguishable as separate physical instances/opportunities.
7. Same-seed Engine resets and independent Engine instances must not create cross-episode joins through repeated UnitInstance UUIDs.
8. The exact offer snapshot, observations, masks, selected BUY action and resulting ownership transfer must share an explicit decision correlation.
9. Replay must prove reroll, lock, purchase, failed/invalid purchase, empty shop slot, terminal reset and consecutive episodes.

These are acceptance requirements, not authorization to implement them now.

## 7. Architecture reconstruction review

1. **Prior problem:** prior audits established that no explicit shop offer ID/revision existed, but did not sufficiently distinguish the physical UnitInstance UUID available in native diagnostics from the missing offer-opportunity identity.
2. **Technical justification:** a physical unit may move from shop to bench while a slot is reused by reroll; conflating UUID, slot and offer generation breaks snapshot-bound BUY decisions and replay joins.
3. **New responsibility:** this note owns the distinction between physical UnitInstance identity, positional shop slot and offer-opportunity lifecycle, including generation, purchase and reset behavior.
4. **Contract and invariants:** UUID identifies the physical instance, slot identifies only current position, and offer generation/decision correlation remain unavailable until explicitly produced; no synthetic identity is allowed.
5. **Cross-component impacts:** ShopEngine, UnitInstanceFactory, UnitPool, PlayerEnv BUY action, audit snapshots, strategic action diagnostics, flat PPO shop features, masks, replay and rollout identity.
6. **Objective validation:** constructor seed, roll/reroll, return, take, purchase transfer, reset reconstruction and diagnostic snapshot are source-traced; each identity category has an explicit status; no runtime or tensor change is made.

Issue #346 remains open. Gate 7 executable acceptance remains pending. Gate 8 remains blocked.
