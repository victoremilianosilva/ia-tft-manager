# Structured Item Ownership Snapshot Contract v1 — Draft

**Status:** bounded Stage 1 producer delivery; review required.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem
The native snapshot exposed loose components and completed-item inventory as flat catalog-ID vectors, while equipped items were visible only nested under live board/bench UnitInstance records. Consumers had to reconstruct multiplicity and ownership scope independently.

## 2. Technical rationale
ItemEngine stores catalog IDs and multiplicity, not physical item-instance identities. Inventing a UUID per item would falsely imply provenance and lifecycle guarantees absent from the source. This contract reports counted catalog copies for component/inventory stores and links equipped catalog copies to the current live unit UUID and board/bench slot.

## 3. New responsibility and owner
ItemEngine remains authoritative for component and completed-item inventory vectors. UnitInstance remains the active equipment owner. TFTEngine::get_audit_snapshot() creates a read-only projection. Pybind transports it; the wrapper validates it; rollout retains it as non-tensor metadata.

## 4. Contract
Each player record adds item_component_counts (unique catalog_id/count rows), item_inventory_counts (unique catalog_id/count rows), and equipped_items (unit_uuid, location board/bench, slot and catalog_id) derived only from live UnitInstances. Existing flat vectors and UnitInstance mirrors remain unchanged. Count rows preserve multiplicity; they are not physical IDs. Anvil options are choices, not owned items until selected. Equipment is reported only for live board/bench units and does not expose orphaned UUID-keyed ItemEngine entries after elimination.

Invariants: nonempty unique catalog IDs and positive integer counts; equipment requires a nonempty unit UUID, valid board/bench slot and catalog ID; no synthetic item IDs; no cross-player transfer; no inference that catalog count establishes physical provenance.

## 5. Cross-component impact
Changes AuditPlayerSnapshot, native capture, pybind serialization, wrapper validation and rollout sidecar metadata. It does not change ItemEngine storage, crafting/equip/sale/merge/elimination behavior, masks, Actor/Critic tensors, rewards, policy, checkpoint semantics, Viewer or Overwolf.

## 6. Objective validation
Wrapper fixtures validate required arrays and reject malformed count/equipment rows. Native API tests verify the fields are present alongside the existing item snapshot. Full producer-to-rollout lifecycle replay and elimination terminal ownership remain separate acceptance requirements.

## 7. Explicit limitations
No physical item/component IDs, mutation event sequence, anvil producer identity, pool lifecycle, catalog fingerprint or terminal elimination disposition is added. Equipment rows are active-unit projections, not a complete dump of ItemEngine's private equipped map. #346 and Stage 1 remain open.
