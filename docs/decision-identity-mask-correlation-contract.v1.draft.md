# Decision Identity and Mask Correlation Contract v1 — design specification

**Status:** documentary design proposal; no runtime changes and no implementation authorization.  
**Target:** `new-arquiteture`  
**Related:** Observation Schema v1, Action / Mask Contract v1, Observation Tensor Projection Requirements v1, PPO Architecture and Checkpoint Contract v1, Strategic Shadow Integrated Replay Contract v1; issues #286, #289, #293, #294.

> This contract closes a cross-boundary identity gap found by the producer-to-PPO binding audit. It specifies how one decision is identified and how observations, masks, critic context, evidence snapshots, rollouts and replay records prove that they refer to that same decision. It does not change Engine, wrapper, Policy, rollout, masks, rewards, Viewer, checkpoints or training.

## 1. Problem and technical rationale

The current Observation Schema has a `decision_identity_hash`, but its declared hash scope contains `match_id`, `engine_match_id`, `player_id`, `round`, `decision_sequence` and `snapshot_sequence` without identifying the namespace that owns either sequence number.

The replay contract correctly states that native strategic snapshot, player-local Composition Intelligence, global JSONL append, ContextBridge/player and Viewer session sequences are different namespaces and must not be compared numerically across scopes. The current schema does not encode that distinction in the identity hash contract.

The current PPO binding audit also found that observations and masks are transported through separate wrapper/trainer reads. Rollout stores masks with transitions, but there is no typed decision envelope proving that the observation and mask came from the same native decision. Call ordering alone is not a durable correlation guarantee. The critic additionally requires the exact masks as an independent side input, correlated to that same decision.

A numeric sequence without its namespace is ambiguous. A mask hash without the decision identity it belongs to is insufficient. Matching round numbers, timestamps, player IDs, or array positions are not substitutes for exact decision correlation.

## 2. Canonical decision identity

A canonical decision identity is scoped to one player decision in one Engine match:

- canonical Engine match identity;
- player identity;
- round/stage identity as represented by the Observation Schema;
- typed decision sequence reference: `(namespace, value)`;
- typed source snapshot sequence reference: `(namespace, value)`.

The canonical Engine match identity is mandatory for a complete decision identity. Preserve both existing `match_id` and `engine_match_id` in the identity envelope and hash, because the current v1 scope includes both; do not assume they are aliases or silently substitute one for the other. `session_match_id` and `episode_id` remain separate correlation metadata until a separately reviewed schema revision defines any mapping.

### 2.1 Typed sequence reference

Every sequence used for cross-component correlation must be represented as a typed pair:

| Field | Meaning |
|---|---|
| `namespace` | Stable identifier of the producer/domain that owns the counter |
| `value` | Non-negative monotonic integer within that namespace and declared scope |

The namespace is part of identity, not display metadata. A sequence value from one namespace must never be compared, ordered, deduplicated, or joined directly with a value from another namespace.

At minimum, the implementation manifest must identify the namespaces for:
- canonical Engine decision sequence;
- native observation/source snapshot sequence;
- action-mask snapshot sequence;
- each strategic/economic owner snapshot sequence consumed as evidence;
- replay/recorder sequence;
- Overwolf/GEP source sequence, when present;
- Viewer/session sequence, used only through an explicit correlation record.

Producer-local counters remain producer-local. A correlation record must preserve both original typed references and the validated mapping; it must not rewrite one producer's sequence as if it were another producer's native counter.

### 2.2 Decision identity hash

The next versioned identity definition must compute a deterministic SHA-256 over RFC 8785 canonical JSON containing, at minimum:

- `match_id`;
- `engine_match_id`;
- `player_id`;
- `round`;
- `decision_sequence.namespace`;
- `decision_sequence.value`;
- `snapshot_sequence.namespace`;
- `snapshot_sequence.value`.

The hash excludes itself, timestamps, Viewer/session IDs, append-order counters, diagnostics, and mutable payload contents. Those values may be recorded as correlation or audit metadata, but they do not redefine the identity of the decision.

The current schema's hash scope is not silently reinterpreted. Adding typed namespaces changes identity semantics and therefore requires an explicit schema/identity revision, deterministic fixtures, updated hash examples and migration classification. Until that revision is approved and implemented, a record whose sequence namespace cannot be established is not eligible for a complete canonical decision identity.

A decision identity hash identifies the decision envelope; it is not a content hash for the observation, masks, evidence, or action.

## 3. Decision-bound payload references

Each payload retains its own content identity and points to the exact canonical decision identity:

| Payload | Required binding |
|---|---|
| Observation snapshot | Canonical decision identity hash, schema ID/version/hash, projection ID/version/hash when projected, source snapshot reference |
| Action masks | Same decision identity hash, Action Contract ID/version/hash, Mask Contract ID/version/hash, mask snapshot hash, exact typed source reference |
| Critic mask context | Same decision identity hash and exact mask snapshot hash; exact masks or provably lossless encoding |
| Strategic/economic evidence | Same Engine match/player scope plus exact typed source-sequence references and owner/version/provenance; stale or uncorrelated owner snapshots remain unavailable |
| PPO transition/rollout row | Same decision identity hash; observation, masks, selected action, log-probability, value, reward/validity and next-state references remain associated with that row |
| Replay/Viewer record | Original decision identity plus explicit session/replay correlation; local session sequence never substitutes for Engine identity |

The observation content hash and mask snapshot hash are independent of the decision identity hash. Two different payload contents must not be treated as the same payload merely because they refer to the same decision.

Catalog, rules, action/mask contract, configuration, policy and projection identities are compatibility/control metadata. They must be bound to the transition/checkpoint manifest as appropriate, but must not be appended indiscriminately to the decision identity hash. A catalog or contract mismatch makes the payload incompatible for the requested consumer; it does not create a different historical decision.

## 4. Exact observation-mask correlation

A decision is eligible for policy consumption only when all required conditions hold:

1. Observation and masks identify the same canonical Engine match and player.
2. Their round and canonical decision identity hash match exactly.
3. Their decision sequence references match as typed pairs, including namespace.
4. Their source snapshot references are either identical or connected by an explicit, validated correlation record whose contract defines why the two payloads represent the same decision.
5. The mask snapshot hash verifies the exact mask payload and its ordering.
6. Action Contract and Mask Contract IDs, versions and hashes match the policy's declared contract set.
7. Required catalog/configuration identities are compatible with the observation and policy lineage.
8. No newer accepted decision has superseded the payload before consumption.

No fallback is allowed from missing identity to matching timestamps, round/player only, array index, call order, or “latest available masks”. A stale or mismatched mask must not be paired with a newer observation.

The Engine remains the final authority for legality. This contract governs correlation and freshness; it does not make masks authoritative over Engine validation.

## 5. Actor, Critic and rollout requirements

- Actor receives the exact masks correlated with the observation decision.
- Critic receives those same exact masks as an independent side input, or a representation proven lossless for every mask value and ordering.
- Markov-sufficient state, recurrent history, anti-loop history or other critic context is additional context; none replaces exact masks.
- The value estimate stored for a transition must use the same decision-bound observation and critic mask context as the action/value evaluation contract specifies.
- Rollout rows must preserve the decision identity and mask snapshot identity through storage, minibatch selection, action-log-probability recomputation, value evaluation and replay.
- A transition with missing, stale, incompatible or mismatched identity/masks is not silently repaired by fetching current masks. Its trajectory/optimization eligibility follows the Reward and PPO rollout contracts; this document does not redefine those semantics.

Reset observations require the exact initial-state masks for the same decision identity. The current wrapper behavior that returns reset observations without delivering their paired masks to the trainer is an identified migration concern, not permission to reuse masks from a later step.

## 6. Ordering, duplicate delivery, reset and stale handling

Within one declared Engine match/player/sequence namespace:

- decision sequence values are monotonic and never reused for a different decision;
- an identical duplicate delivery with the same identity and payload hashes may be treated idempotently;
- the same typed sequence with a different decision identity or conflicting payload hash is invalid and must be surfaced;
- a lower sequence arriving after a newer accepted decision is stale and must not roll the consumer backward;
- a gap is not automatically filled by copying the latest observation or masks; the consumer records missing evidence and follows its declared eligibility policy.

At episode/match reset, the Engine match identity changes. Sequence counters may restart only under that new identity. A reset must clear pending observation-mask pairings, temporal state, cached owner snapshots and stale correlation records from the prior episode.

If a counter can roll over, the namespace contract must define an explicit epoch/generation component before rollover can occur. Silent wraparound is forbidden. The same numeric sequence in a new namespace or Engine match is not the same decision.

## 7. Failure states and required behavior

| Condition | Required classification | Required behavior |
|---|---|---|
| Missing Engine match/player/typed decision reference | incomplete identity | Do not claim canonical correlation; no policy consumption as a complete decision |
| Namespace missing or unknown | incomplete identity | Never compare the bare sequence number |
| Observation/mask decision hash mismatch | mismatch | Reject the pair; do not substitute latest masks |
| Mask content hash mismatch | invalid payload | Reject mask payload |
| Contract/catalog/config identity mismatch | incompatible | Reject for that policy lineage with field-level reason |
| Older sequence after newer accepted sequence | stale | Reject stale payload; preserve diagnostic |
| Same sequence with conflicting identity/content | conflict | Reject and surface producer/correlation fault |
| Owner evidence from another sequence | stale/unrelated evidence | Exclude it or mark unavailable; do not relabel as current |
| Session-only identity | session-only | Permit display/diagnostics only under explicit policy; not canonical PPO decision binding |

Failure classification must be retained in diagnostics and replay artifacts. Missing identity is not sequence zero; stale is not missing; incompatible is not a valid but low-confidence observation.

## 8. Deterministic acceptance evidence — post-Gate 8

The executable suite must include positive and negative cases for:

1. Exact observation/mask match with identical typed decision references.
2. Same numeric sequence but different namespaces — rejected.
3. Same player/round but different Engine match — rejected.
4. Same match/player/round but different decision sequence — rejected.
5. Same decision identity but wrong mask snapshot hash — rejected.
6. Correct masks with changed Action/Mask Contract hash — incompatible.
7. Observation and mask arriving out of order — stale handling is deterministic.
8. Duplicate identical delivery — idempotent handling.
9. Duplicate sequence with conflicting payload — explicit conflict.
10. Reset followed by sequence restart under a new Engine match — accepted as a new identity.
11. Reset with delayed prior-match masks/evidence — rejected as stale.
12. Missing initial/reset masks — no reuse of later masks.
13. Actor and Critic receive the same exact mask snapshot identity.
14. Rollout/minibatch/replay preserve the original decision identity and mask hash.
15. Owner snapshots with distinct namespaces are correlated only through validated mappings.
16. Deterministic RFC 8785 hash vectors, including namespace changes and null/incomplete identity cases.

These tests belong to the authorized runtime migration and integrated replay/evaluation work. This specification does not authorize implementing them before Gate 8.

## 9. Migration and versioning

The current Observation Schema v1 hash scope does not include sequence namespaces. The current binding audit also found no typed decision envelope connecting the separately retrieved masks to the observation transition. These are contract gaps, not evidence that the runtime is already correlated.

Before implementation:
1. Review the identity extension against Observation Schema, Action/Mask, PPO checkpoint and replay contracts.
2. Define the schema/identity revision and exact machine-readable field names for typed sequence references.
3. Update the source map and fixtures to distinguish namespace/value pairs from unrelated local counters.
4. Define mask and observation content-hash canonicalization independently from decision identity.
5. Define wrapper/trainer/rollout/replay transport so the envelope travels atomically with the observation and exact masks.
6. Bind the Critic side input to the same decision and mask hashes.
7. Add compatibility classification and checkpoint lineage references; never infer compatibility from tensor shape or sequence integer equality.
8. Execute deterministic integration tests only after Gate 8 and explicit authorization.

This identity extension is a semantic contract change. It must not be slipped into Observation Schema v1 as an editorial patch or implemented by silently changing the existing hash scope. The precise schema versioning decision is part of the follow-up review.

## 10. Architecture reconstruction review

1. **Prior problem:** the current schema hashes sequence values without their namespaces, and the current wrapper/trainer path does not prove that separately retrieved masks belong to the exact observation decision.
2. **Technical rationale:** producer-local counters are incomparable; call ordering and matching round/player metadata do not establish decision identity or payload freshness.
3. **New responsibility:** this contract owns cross-component decision correlation and freshness rules; Observation Schema owns semantic fields; Action/Mask owns legality/mask definitions; PPO/rollout owns consumption and transition storage; replay owns deterministic evidence.
4. **Contract and invariants:** typed sequence references; exact observation-mask identity; independent payload hashes; no latest-mask fallback; reset/stale/conflict handling; Actor/Critic mask consistency; Engine remains legality authority.
5. **Cross-component impact:** native Engine, Python wrapper, trainer, Policy Actor/Critic, rollout, checkpoint manifest, strategic/economic owners, replay and Viewer correlation.
6. **Objective validation:** compared the current schema sequenceIdentity definition, Action/Mask contract mask-reference and critic-context fields, producer-to-PPO binding audit, and replay namespace rules. No runtime code or existing schema was changed.

## 11. Status

This document is a design proposal for review. It does not close #286, #289, #293 or #294, does not approve a concrete tensor projection, and does not complete any runtime acceptance gate. The next review must reconcile this contract with the existing schema's current identity hash scope and decide the exact schema revision before any implementation.
