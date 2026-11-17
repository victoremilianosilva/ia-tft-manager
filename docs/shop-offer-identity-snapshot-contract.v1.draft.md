# Shop Offer Identity and Lifecycle Snapshot Contract v1 — Draft

**Status:** bounded Stage 1 native producer delivery; review required.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem
The native audit snapshot exposed five shop slots as UnitInstance records. Their UUIDs identify champion copies, but the snapshot had no native generation for the offer occupying a particular player's shop slot.

## 2. Technical rationale
A champion-copy UUID and a shop-offer identity answer different questions. The copy UUID follows the physical UnitInstance when purchased and moved to the bench/board. The offer generation is temporary and scoped to one Engine instance, player, shop slot and monotonically increasing slot revision. The composite tuple avoids inventing a second physical-unit identity.

## 3. New responsibility and owner
ShopEngine owns per-slot offer revisions and advances them when an offer is created, replaced, cleared or purchased. TFTEngine::get_audit_snapshot projects the five revisions beside the existing five shop UnitInstance records. Pybind transports them; CppTFTLobbyWrapper validates and retains them as non-tensor snapshot metadata.

## 4. Contract and invariants
Each player snapshot includes exactly five unsigned shop_offer_revisions, aligned by index with shop. An occupied offer must have a positive revision and a nonempty UnitInstance UUID. Offer identity is the tuple (engine_instance_id, player_id, shop_slot, shop_offer_revision). The unit UUID remains the champion-copy identity and follows a successful purchase out of the shop. A cleared slot retains its latest revision. A locked roll that changes nothing must not advance revisions.

Revisions are monotonic per ShopEngine slot and are not reset to zero when a match resets. The enclosing Engine/episode/snapshot sequence remains authoritative for temporal correlation.

## 5. Cross-component impacts
Changes ShopEngine, AuditPlayerSnapshot capture, pybind serialization, wrapper validation and ShopEngine/wrapper tests. Action catalog, masks, observation tensors, reward, PPO policy and automatic execution remain unchanged. This is not a full historical offer event log.

## 6. Objective validation
Native ShopEngine tests verify revision advancement on roll/reroll and purchase, and no advancement on a locked no-op. Wrapper fixtures reject malformed revision arrays and occupied offers without a revision.

## 7. Explicit limitations
The contract exposes current slot generation and current UnitInstance UUID, not every historical offer event. It does not solve authoritative match identity or Stage 7 live GEP validation. #346 and Stage 1 remain open.
