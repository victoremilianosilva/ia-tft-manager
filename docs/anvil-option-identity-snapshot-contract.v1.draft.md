# Anvil Option Identity and Lifecycle Snapshot Contract v1 — Draft

**Status:** bounded Stage 1 native producer delivery; review required.  
**Tracking:** #346, #293 and #294.

## 1. Prior problem
The native snapshot exposed pending-anvil kind and option catalog IDs, but did not identify which granted choice set those options belonged to. Two consecutive anvils with identical options were therefore indistinguishable in a correlated sidecar/replay.

## 2. Technical rationale
An anvil is a temporary choice set, not an owned item. ItemEngine is the authoritative queue owner, so a monotonic sequence identifies each accepted grant without fabricating physical item/component IDs.

## 3. New responsibility and owner
ItemEngine assigns a monotonically increasing sequence when a validated anvil is accepted. The sequence is ItemEngine-local and survives reset(); reset clears pending choices but does not recycle identities. TFTEngine projects the pending sequence into the atomic native-state snapshot; pybind transports it and the wrapper validates it.

## 4. Contract and invariants
A player record exposes pending_anvil, pending_anvil_sequence, pending_anvil_kind and pending_anvil_options. A pending anvil must have a positive sequence and nonempty options. With no pending anvil, the snapshot sequence is zero. Identity is scoped by the enclosing Engine instance and player row plus ItemEngine sequence. Option identity is the anvil identity plus option index; catalog ID remains the option value, not a physical instance ID.

Sequence overflow fails explicitly; it never wraps or silently reuses an identity. Invalid grants do not consume a sequence. Selecting an option consumes the pending anvil; it does not turn the anvil or option into a persistent physical entity.

## 5. Cross-component impact
Changes ItemEngine, AuditPlayerSnapshot capture, pybind serialization, wrapper validation and native/wrapper fixtures. No action dimensions, masks, PPO tensors, reward, policy behavior, item storage model or automatic execution changes.

## 6. Objective validation
Native tests verify accepted anvils receive positive increasing identities, invalid choices preserve the pending anvil, and identity is not reused across ItemEngine reset. Wrapper validation rejects missing/invalid sequence values and inconsistent pending state.

## 7. Explicit limitations
This is current pending-choice identity, not a full anvil grant/selection event ledger. It does not add physical item/component IDs or Stage 7 live-capture proof. #346 and Stage 1 remain open.
