# Decision Identity Schema v2 — Versioning Boundary and Migration Design

**Status:** documentary design decision proposal; no runtime changes or implementation authorization.  
**Target:** `new-arquiteture`  
**Related:** #338, Observation Schema v1, Decision Identity and Mask Correlation Contract v1, Action / Mask Contract v1, PPO Architecture and Checkpoint Contract v1, Observation Tensor Projection Requirements v1, Strategic Shadow Integrated Replay Contract v1.

> This document resolves the versioning boundary for typed decision sequences. It is a design proposal for review, not a populated production schema or runtime implementation.

## 1. Decision

Adopt **both**:
1. a new **Observation Schema v2** for the breaking semantic envelope change; and
2. an independently versioned **Decision Identity Envelope v2** embedded in that schema and referenced by masks, PPO transitions, checkpoints and replay.

Do not retrofit typed sequence objects into Observation Schema v1. The current v1 schema defines `decision_sequence` and `snapshot_sequence` as nullable integers and hashes those untyped values. Replacing those integers with objects changes field types, required structure, validation, hash semantics and compatibility. That is a breaking schema change, not an editorial correction.

Observation Schema v1 and its historical hashes, fixtures, source maps and artifacts remain immutable. New-lineage producers must emit v2; consumers must not silently reinterpret v1 payloads as v2.

The existing `decision-identity-mask-correlation-contract.v1.draft.md` remains the conceptual cross-boundary contract. Its identity-envelope semantics are superseded for new payloads by this v2 design once approved. The v1 document remains useful as migration rationale and must not be represented as the active v2 field definition.

## 2. Ownership boundaries

| Concern | Canonical owner | Responsibility |
|---|---|---|
| Semantic observation fields | Observation Schema | Field meaning, types, provenance, validity and source semantics |
| Decision identity | Decision Identity Envelope | Match/player/round scope, typed sequence references, canonical identity hash |
| Observation payload hash | Observation producer/serializer | Exact canonical observation content identity, independent of decision identity |
| Mask payload and mask hash | Action/Mask producer | Exact legal-action mask content, ordering and contract identity |
| Mask legality | Native Engine | Final validation of action legality against current state |
| PPO consumption and transition row | PPO Policy/rollout | Atomic binding of observation, masks, action/value and decision identity |
| Checkpoint compatibility | Checkpoint manifest | Immutable references to schema, identity, projection, action/mask, reward and policy lineage |
| Cross-domain/session correlation | Replay/recorder | Explicit mappings between typed producer sequences and Viewer/session/replay sequences |

No owner may rewrite another owner's sequence number or claim its namespace. A correlation record maps typed references; it does not replace them.

## 3. Machine-readable identity v2

The v2 schema must define the following exact envelope. This is a normative design shape, not a committed runtime JSON Schema:

```json
{
  "identity_version": "tft.decision-identity.v2",
  "status": "complete",
  "match_id": "match-identity",
  "engine_match_id": "engine-match-identity",
  "player_id": "player-2",
  "round": 12,
  "decision_sequence": {
    "namespace": "tft.engine.decision",
    "value": 184
  },
  "snapshot_sequence": {
    "namespace": "tft.engine.observation-snapshot",
    "value": 184
  },
  "decision_identity_hash": "sha256:<64-lowercase-hex>"
}
```

### 3.1 Field rules

- `identity_version` is required and equals `tft.decision-identity.v2`.
- `player_id` is the episode-local seat token encoded as `player-0` through `player-7`; it is not a persistent user/player UUID.
- `status` is required. A complete identity requires non-empty `match_id`, `engine_match_id`, `player_id`, a non-negative `round`, and both typed sequence references.
- `match_id` and `engine_match_id` remain distinct required identifiers. Neither is silently derived from or substituted for the other.
- `decision_sequence` and `snapshot_sequence` are objects with exactly `namespace` and `value`; additional properties are rejected.
- `namespace` is a stable, non-empty identifier naming the producer and counter domain. It is part of identity, not display metadata.
- `value` is a non-negative integer, monotonic only within the namespace's declared scope.
- `session_match_id`, `episode_id`, timestamps, event counters, JSONL append counters and Viewer session counters remain separate correlation/audit metadata. They are not substitutes for canonical Engine identity.
- Incomplete identities have a status and reason, and their decision hash is null. They are not eligible for canonical PPO consumption.

### 3.1.1 Source semantics of identity fields

The field names are not interchangeable. Their canonical meanings for v2 are:

| Field | Canonical meaning | Current source status | Rule |
|---|---|---|---|
| `match_id` | Authoritative logical game-match identity supplied by a validated game/platform source | No authoritative producer was proven in the audited main-repository path | Never fill it with the ViewerSession UUID or infer it from seed, timestamp, seat, or episode counter; if absent, identity is incomplete |
| `engine_match_id` | Canonical Engine-episode scope, uniquely distinguishing one Engine object lifetime and one episode within it | Not currently produced; native `episode_id` alone is only Impl-local and collides across independent Engine objects | Future producer must bind Engine-instance scope + native episode; exact wire encoding remains a separate decision |
| `session_match_id` | Viewer recording/session UUID | Produced by `ViewerSession` | Correlation/display metadata only; excluded from canonical identity and hash |
| `episode_id` | Native numeric episode counter within one `TFTEngine::Impl` lifetime | Produced by native reset/step results and pybind; dropped by the Python training wrapper | Preserve as diagnostic/correlation metadata; never use alone as `engine_match_id` |
| `player_id` | Episode-local seat token encoded as `player-{seat_index}` (`player-0`…`player-7`) | Native eight-player arrays and wrappers use integer seat positions | Deterministic representation only; not a persistent user/player UUID |

The current Viewer correlation path writes the Viewer UUID into the record's `match_id` field and separately copies native `episode_id` into `engine_match_id`. That is a **legacy/session correlation shape**, not proof that those values satisfy the v2 canonical field meanings above. A v2 adapter must map the Viewer UUID to `session_match_id`; it must not promote it into `match_id`. Likewise, the current numeric native episode value cannot populate the v2 `engine_match_id` until an Engine-instance scope is included.

If either authoritative game-match identity or canonical Engine-episode scope is unavailable, the v2 identity must remain non-complete with an explicit reason and null decision hash. Do not weaken the required v2 fields or silently reinterpret historical v1/session records to make them pass validation.

### 3.2 Namespace registry

A versioned namespace registry must declare for each namespace:
- stable namespace ID;
- producer/owner and counter meaning;
- scope (global, match, player, or another explicitly defined scope);
- monotonicity and duplicate-delivery semantics;
- reset boundary;
- whether it can be used as canonical decision sequence or only as a source reference.

Proposed namespace identifiers and current availability are defined in [Sequence Namespace Registry v2](../spec/sequence-namespace-registry.v2.draft.json) and its human-readable companion. In particular, `tft.engine.decision`, `tft.engine.observation-snapshot`, and `tft.engine.action-mask-snapshot` are **proposed_not_implemented**: the current producer-binding audit does not prove that these counters are emitted or transported. Existing CI, native strategic snapshot, ContextBridge, diagnostic JSONL, Viewer and PPO rollout sequence domains remain owner-local references and are not canonical decision identity. A namespace cannot be promoted to canonical eligibility until its producer, scope, monotonicity, reset behavior and exact correlation are proven.

### 3.3 Reset and rollover

- Sequence values never identify a decision without their namespace and Engine match identity.
- A new Engine match identity establishes a new sequence scope; counters may restart only under that new identity.
- A counter must not wrap or be silently reused within one declared scope.
- If rollover is unavoidable, a separately versioned namespace generation must be introduced before rollover. It must not be inferred from timestamps or appended informally by consumers.
- Viewer/session reset does not reset or redefine Engine identity.

## 4. Canonical decision hash v2

Compute SHA-256 over RFC 8785 canonical JSON containing exactly:

- `identity_version`;
- `match_id`;
- `engine_match_id`;
- `player_id`;
- `round`;
- `decision_sequence.namespace`;
- `decision_sequence.value`;
- `snapshot_sequence.namespace`;
- `snapshot_sequence.value`.

The hash field itself is excluded. The canonical input must not contain timestamps, session IDs, episode IDs, append-order counters, diagnostics, mutable observation contents, masks, catalog hashes or policy metadata.

Including `identity_version` makes the version boundary explicit. Changing either namespace while retaining the same numeric value changes the hash. Changing payload content without changing the decision envelope does not change the decision identity hash.

Payload hashes are separate:
- observation content hash covers the canonical observation payload under its declared schema/canonicalization;
- mask content hash covers the exact ordered mask payload under its declared Action/Mask contract;
- evidence payload hashes, when needed, cover their own canonical owner payloads.

Every content hash must declare its own canonicalization and exclusion scope. A decision identity hash is never a substitute for a payload hash, and vice versa.

## 5. Decision-bound references

| Payload | Required v2 binding |
|---|---|
| Observation | Full decision identity v2, schema ID/version/hash, observation content hash, source snapshot reference |
| Action masks | Same decision identity hash, Action Contract ID/version/hash, Mask Contract ID/version/hash, mask content hash and exact typed source reference |
| Critic context | Same decision identity hash and exact mask content hash/reference; masks remain a separate side input |
| Strategic/economic evidence | Match/player scope, owner/version/provenance and typed owner source sequence; explicit correlation to the decision |
| PPO transition/rollout row | One identity v2 plus exact observation/mask hashes, sampled action, log-probability, value and reward/validity references |
| Checkpoint | Schema v2, identity v2, projection, action/mask, reward and architecture identities as independent manifest entries |
| Replay/Viewer | Original Engine decision identity plus explicit mapping to replay/session sequence; never replace it with a session-local sequence |

The Actor and Critic must consume the exact same decision-correlated mask snapshot. Additional critic history/Markov context is separately versioned and never substitutes for masks.

## 6. Correlation and failure behavior

A pair is consumable only when:
1. observation and masks have the same Engine match, player, round and full decision identity hash;
2. both typed sequence references match exactly, including namespaces, or an explicit validated correlation record proves the source mapping;
3. mask content hash and ordering verify;
4. Action/Mask contract identities match the consumer's declared lineage;
5. required schema/catalog/config identities are compatible; and
6. the payload has not been superseded by a newer accepted decision.

No fallback to timestamps, player/round alone, array index, call order, or latest available masks is permitted.

| Condition | Classification | Required behavior |
|---|---|---|
| Missing Engine match/player/typed reference | incomplete identity | Do not claim canonical correlation or consume as complete PPO decision |
| Unknown namespace | unsupported identity | Reject for canonical correlation; preserve raw diagnostic |
| Same value, different namespace | different sequence | Reject direct equality/join |
| Observation/mask identity mismatch | mismatch | Reject pair; never fetch latest masks as repair |
| Payload hash mismatch | invalid payload | Reject payload |
| Contract/catalog/config mismatch | incompatible | Reject for that lineage with explicit reason |
| Older sequence after newer accepted sequence | stale | Reject and retain diagnostic |
| Same typed sequence with conflicting identity/content | conflict | Reject and surface producer fault |
| Session-only identity | session-only | Diagnostics/display only under explicit policy |
| Reset with delayed prior-match data | stale prior episode | Reject; clear pending pairings and cached evidence |

Engine legality remains final. This contract governs identity, correlation and freshness; it does not authorize policy or Shadow to override native validation.

## 7. v1 migration classification

| v1 field/artifact | v2 disposition | Migration rule |
|---|---|---|
| `match_id`, `engine_match_id`, `player_id`, `round` | Preserve semantics | Copy only after source validation; do not alias IDs |
| Integer `decision_sequence` | Rebuild typed reference | Namespace must be proven from the original producer; never guess from call order |
| Integer `snapshot_sequence` | Rebuild typed reference | Namespace must be proven from the original producer; otherwise mark incomplete |
| v1 `decision_identity_hash` | Historical-only | Preserve unchanged for v1 artifacts; never relabel or recompute as v2 |
| v1 `decision_identity_hash_scope` | Superseded in v2 | Keep v1 scope immutable; use v2 scope only for v2 payloads |
| `player_sequence`, `event_sequence` | Producer-local metadata | Assign typed namespaces only when owner/scope is verified |
| `session_match_id`, `episode_id`, `captured_at` | Correlation/audit metadata | Do not include in canonical decision hash |
| v1 mask references | Historical v1 binding | Cannot satisfy v2 exact binding unless source identity and payload hashes are independently reconstructed and validated |
| v1 checkpoints/artifacts | Immutable historical lineage | Evaluate as v1 baselines; no automatic semantic compatibility with v2 |

A missing namespace is not recoverable by inventing one. If provenance cannot establish the namespace, the migrated record remains incomplete for v2 canonical use.

## 8. Cross-contract responsibilities and changes

- **Observation Schema:** introduce v2 typed fields and status rules; retain v1 schema, maps, fixtures and hashes unchanged.
- **Action/Mask:** reference identity v2 and bind the exact mask content hash; keep action catalog, mask semantics and Engine legality ownership independent.
- **PPO/rollout:** transport the envelope atomically with observations and exact masks; reset must deliver its own masks; minibatch/update/replay retain identity and mask hash.
- **Critic:** receive exact masks as separate correlated side input; additional history is separate.
- **Checkpoint:** record schema/identity versions and hashes independently from projection and action/mask identities; v1 checkpoint remains historical.
- **Tensor projection:** consumes validated v2 semantic snapshots but does not redefine identity or include the identity hash as an ordinary scalar feature.
- **Replay/Viewer:** preserve original typed references and explicit session correlation; test reset, stale delivery, duplicate delivery and conflicting sequence records.
- **Shadow strategic/economic owners:** publish their own typed source references and provenance; they do not own or rewrite canonical Engine decision identity.

## 9. Required documentary artifacts before approval

1. Machine-readable Observation Schema v2 proposal with exact typed definitions and validation rules.
2. Namespace registry with owner, scope, reset and availability evidence.
3. v1→v2 field crosswalk and compatibility matrix.
4. RFC 8785 deterministic hash vectors, including namespace-change, match-change, reset and incomplete cases.
5. Separate observation/mask payload hash definitions and examples.
6. Cross-contract updates for Action/Mask, checkpoint, projection, producer binding and replay.
7. README/index update identifying v1 as historical immutable and v2 as proposed.
8. A consistency review confirming no runtime guarantee is claimed.

## 10. Phase boundary

This design does not approve a concrete tensor projection, PPO encoder, action-space change or runtime transport. No Engine, wrapper, Policy, Actor/Critic, rollout, masks, rewards, training, checkpoints, Viewer or game behavior may change before Gate 8 and explicit authorization.

## 11. Architecture reconstruction review

1. **Prior problem:** v1 sequences are bare integers and the current wrapper/trainer path does not prove exact observation-mask pairing.
2. **Technical rationale:** namespace-free sequence equality is ambiguous; changing field types and hash semantics is a breaking semantic schema change.
3. **New responsibility:** Decision Identity owns canonical decision correlation; each producer owns its sequence; payload producers own content hashes; Engine owns legality; PPO owns consumption; replay owns cross-session correlation.
4. **Contract/invariants:** typed references, versioned hash, independent content hashes, no latest-mask fallback, no silent v1 reinterpretation, reset/stale/conflict handling, exact Actor/Critic mask pairing.
5. **Cross-component impact:** schema, source map, Action/Mask, wrapper/trainer, Policy, rollout, checkpoint, tensor projection, strategic/economic producers, replay and Viewer.
6. **Objective validation:** compare v1 JSON Schema field types/hash scope against v2 proposed shape; verify the migration table preserves every v1 identity field and forbids namespace guessing; specify deterministic hash vectors and cross-contract checks.

## 12. Status

**Proposed decision:** Observation Schema v2 plus Decision Identity Envelope v2. The machine-readable `spec/observation-schema.v2.draft.json`, namespace registry, hash vectors and v1→v2 crosswalk are now draft review artifacts under issue #340. They are not approved for runtime use. Issue #338 tracks the versioning-boundary decision; issue #340 tracks the detailed v2 schema/registry/hash specification. Gate 8 and explicit authorization remain mandatory for runtime work.
