# Engine Identity Scope Reconciliation v1 — Draft

**Status:** documentary reconciliation proposal; no runtime changes and no implementation authorization.  
**Target:** `new-arquiteture`.  
**Related:** Decision Identity Schema v2 Design, Native Engine Instance and Episode Identity Scope Audit, Engine Episode Identity Reset Reconciliation, Viewer/Engine Session Correlation Audit, Python Wrapper/Rollout Decision Correlation Audit, UnitInstance Copy/Test Hook Audit.  
**Tracking:** issue #346 for the broader structured-entity producer audit; this note does not close it.

> This document reconciles the identity scopes already proven in source. It does not select a concrete ID-generation algorithm, alter Schema v2, or authorize runtime implementation.

## 1. Prior problem

The Decision Identity Schema v2 design requires both `match_id` and `engine_match_id` for a complete identity, but the source audits establish several distinct identifiers with overlapping names and incomplete transport:

- `TFTEngine::Impl::episode_id` is a numeric episode counter local to one Engine implementation object.
- No Engine-instance UUID/token or process-wide Engine scope token was found in the audited constructor, reset, move, native result or binding paths.
- ViewerSession creates its own UUID `match_id`; this is not the native Engine episode identity.
- Some diagnostic records explicitly carry both Viewer `match_id` and native `engine_match_id`, but that mapping is not a universal native identity contract.
- Native reset/step result structs and pybind preserve `episode_id`; `cpp_lobby_env.py` drops it from the training-facing return values.
- The eight-player `player_id` is represented by a seat/index in native arrays and wrapper structures. It is not a globally stable player identity.
- UnitInstance UUIDs are deterministic factory outputs and may repeat after same-seed reset or across independent same-seed Engine instances.

Consequently, a numeric episode counter, Viewer session UUID, player seat, or UnitInstance UUID cannot independently identify a physical Engine/player/episode scope across all relevant boundaries.

## 2. Technical rationale

Identity must distinguish *which Engine object*, *which episode within that object*, *which player seat/participant*, and *which decision within that episode*. These dimensions solve different collision and correlation problems:

1. An Engine-instance scope distinguishes two independently constructed Engine objects that both begin at episode zero.
2. An episode identity distinguishes successive resets of one Engine object.
3. A player identity distinguishes the eight participants within an episode. A seat index can serve as an episode-local slot, but must not be mislabeled as a persistent player UUID.
4. A decision sequence distinguishes ordered decisions within the player/episode scope and must retain its producer namespace.
5. UnitInstance UUID remains an instance token; it must be interpreted inside the appropriate Engine/episode/player ownership scope and must not be promoted to a globally unique identifier.

This separation prevents false joins across resets, independent Engine objects, Viewer sessions, player seats, or replay files.

## 3. Reconciled identity model (proposal)

The following is a semantic model for future review, not a committed JSON shape:

| Dimension | Meaning | Current source status | Proposed interpretation |
|---|---|---|---|
| Engine instance scope | One constructed native Engine object lifetime | **Not produced** as a distinct token in audited paths | Required outer scope if multiple Engine objects can coexist or their records can be combined |
| Episode | One match/episode created by reset lifecycle within an Engine object | Native numeric `episode_id` exists and increments on reset | Episode-local identity; insufficient without Engine-instance scope |
| Viewer session | One Viewer-owned recording/session | Viewer UUID `match_id` exists | Session identity only; map explicitly to native Engine episode |
| Player seat | One of eight player positions in an episode | Native/wrapper player index exists | Episode-local participant slot, not persistent player identity |
| Decision | One player decision in one episode | No canonical native decision sequence proven | Requires a typed, producer-owned sequence namespace |
| Snapshot | One observation/source snapshot | No canonical native snapshot sequence proven | Requires a typed, producer-owned sequence namespace |
| Unit instance | One physical UnitInstance lineage | UUID-shaped factory token exists | Local instance token, scoped by Engine/episode/ownership; not global |
| Shop opportunity | One particular offer in a shop generation | No offer ID/revision/generation | Separate from physical UnitInstance and positional slot |

### 3.1 Engine instance and episode must remain separate

The native Engine's `episode_id` starts at zero in each `TFTEngine::Impl` and increments on reset. Independent Engine objects can therefore share the same numeric episode value. Defaulted move operations transfer/replace Impl state but do not mint a new Engine scope token.

A future canonical Engine episode reference therefore needs an unambiguous composite scope equivalent to:

`(engine_instance_scope, episode_id)`

This notation expresses required semantics only. It does not prescribe whether the scope is a UUID, monotonic process token, opaque random token, or another collision-resistant value. That producer and generation policy require a separate reviewed decision.

### 3.2 Viewer session is a correlated observer, not the Engine owner

ViewerSession's UUID `match_id` and Viewer `sequence_id` are owned by the Viewer. They may be useful for recording and navigation, but they cannot replace native Engine identity. When a Viewer record refers to a native episode, it must preserve both identifiers and an explicit validated mapping.

### 3.3 Player seat is episode-local

The current eight-player Engine uses array positions and `player_id` values in the range of the lobby seats. This is adequate for indexing one Engine episode's arrays, but not a persistent identity across independent lobbies, reset boundaries, or replay aggregation.

Until an authoritative participant identity exists, records must describe this value as an episode-local seat/index and carry the full Engine episode scope. Consumers must not infer a stable user/player identity from the seat number.

### 3.4 UnitInstance UUID remains subordinate to episode scope

The UnitInstance factory is seeded from the base Engine seed and rebuilt from that seed on reset. Same-seed Engine objects/resets can reproduce UUID sequences. A copied UnitInstance also preserves its UUID. Therefore a bare UUID is not a globally unique physical identity.

For cross-episode/replay joins, the minimum semantic reference is the scoped instance token, not the token alone. Ownership location (shop/bench/board), slot, and diagnostic copies remain separate attributes and do not redefine physical identity.

## 4. Ownership and boundaries

| Responsibility | Owner/boundary | Required behavior |
|---|---|---|
| Engine-instance scope production | Native Engine lifecycle owner (future decision) | Mint/assign once per Engine object lifetime; expose immutably |
| Episode progression | Native Engine reset lifecycle | Preserve existing episode increment semantics; never use episode number without Engine scope |
| Player seat | Native lobby/player collection | Identify seat within the scoped episode; do not claim cross-match persistence |
| Decision/snapshot sequence | Actual native decision and observation producers (not yet proven) | Own distinct typed namespaces and reset/monotonicity rules |
| Viewer correlation | Viewer/recorder | Preserve Viewer UUID and explicit native Engine episode mapping |
| Python transport | `CppTFTLobbyWrapper` and vector adapter | Carry identity references without deriving or replacing them |
| PPO transition binding | Trainer/RolloutBuffer | Store the exact typed references for each observation/mask/action transition |
| UnitInstance lifecycle | UnitInstanceFactory and authoritative Engine ownership transactions | Preserve instance token on ownership transfer; scope it; retire consumed/sold/eliminated instances explicitly |

No adapter, Viewer, Trainer, or replay consumer may invent an Engine identity, reinterpret a seat index as a player UUID, or promote a local counter into another producer's namespace.

## 5. Required invariants

1. Engine-instance scope is stable for one native Engine object lifetime and differs between independently created Engine objects within the collision domain the system promises to support.
2. Episode identity is the pair of Engine-instance scope and native `episode_id`; reset advances the episode component without changing the Engine-instance component.
3. A moved Engine implementation retains its existing scope; a newly constructed Engine receives a new scope.
4. Viewer session identity remains distinct and is joined to native episode identity only through an explicit mapping.
5. Player seat is valid only within the scoped episode; no global persistence is implied.
6. Decision and snapshot counters are distinct typed namespaces. A value from one namespace is never compared directly with another.
7. UnitInstance UUID is never used alone for cross-episode identity.
8. Observation, masks, action, rollout row, and replay record must reference the same canonical Engine episode and player seat, plus the exact decision identity.
9. Missing scope or sequence information is represented as incomplete/unavailable with a reason; it is not repaired using timestamp, array index, call order, or latest-value fallback.
10. This identity contract does not alter native action legality, PPO action selection, reward semantics, observation tensor layout, or Shadow's read-only role.

## 6. Cross-component impact

- **Native Engine:** currently owns episode progression but lacks a distinct Engine-instance scope token in the audited paths.
- **Native result/pybind:** already exposes `episode_id`; future scope transport must preserve it alongside the new Engine scope.
- **Python wrapper:** currently discards native `episode_id` in reset/step return paths; must not become an identity authority.
- **Vector environment:** array order and automatic reset behavior are not durable identity. Terminal reward/done and next-episode observation must remain distinguishable through explicit episode references.
- **Trainer/RolloutBuffer:** current storage pointer and flattened agent index are storage coordinates, not durable identity. Transition metadata needs typed episode/player/decision references.
- **Viewer/JSONL/replay:** Viewer UUID and append/event sequence remain independent namespaces; mappings must preserve both source and destination references.
- **Unit and shop entities:** UnitInstance UUID, shop slot and offer opportunity remain distinct identity classes.
- **Schema v2 and namespace registry:** the current proposed `match_id`/`engine_match_id` meanings must be explicitly reconciled with native Engine scope and episode. Do not silently reinterpret existing fields or change hash scope without a versioned schema decision.

## 7. Objective validation criteria

Before this proposal can become an implementation contract, source and tests must prove:

1. Two simultaneously alive Engine objects have distinct Engine-instance scopes even when constructed with the same seed.
2. Reset increments `episode_id` while retaining the same Engine-instance scope.
3. Moving an Engine object preserves its scope; reconstructing one creates a new scope.
4. Same-seed reset and independent Engine instances cannot collide in canonical episode identity even if UnitInstance UUIDs repeat.
5. Native reset/step result structs, pybind, wrapper, vector environment and Trainer preserve the same identity values without re-derivation.
6. Terminal auto-reset keeps the terminal transition bound to its old episode while the returned next observation is bound to the new episode.
7. Each of eight player seats is bound to the same episode scope; seat numbers from different episodes cannot join without the episode reference.
8. Viewer/JSONL correlation preserves Viewer session UUID and native Engine episode reference separately.
9. Observation, masks, sampled action and rollout row share exact decision identity; stale or mismatched data is rejected rather than paired by call order.
10. Replay covers two sequential episodes, two independent Engine objects with identical seeds, terminal auto-reset, and repeated UnitInstance UUID sequences.

These are future acceptance tests. No runtime changes or tests are added by this proposal.

## 8. Architecture reconstruction review

1. **Prior problem:** existing audits found Engine-local episode counters, Viewer session IDs and repeated UnitInstance UUID sequences, but their combined scope implications were not reconciled into one explicit identity model.
2. **Technical justification:** each identifier has a different owner and reset boundary; omitting Engine-instance scope permits collisions between independent Engines, while treating seat/session/UUID as global identity creates invalid joins.
3. **New responsibility:** this note owns the semantic reconciliation of Engine instance, episode, Viewer session, player seat, decision/snapshot sequence and UnitInstance identity boundaries.
4. **Contract and invariants:** canonical episode identity requires Engine scope plus episode; player seat is episode-local; Viewer and UnitInstance identifiers remain distinct; typed sequences preserve namespace.
5. **Cross-component impacts:** native Engine lifecycle, pybind, Python wrapper/vector env, Trainer/RolloutBuffer, Viewer/JSONL/replay, UnitInstance/shop lifecycle, Schema v2 and namespace registry.
6. **Objective validation:** the ten source-backed acceptance criteria above must pass before implementation acceptance; this document itself changes no runtime behavior.

## 9. Gate status

This is a design proposal only. Gate 1 observation identity and Gate 2 mask correlation remain runtime-pending; Gate 7 replay acceptance remains executable-test-pending. Gate 8 remains blocked until the integrated review of Gates 1–7 and explicit user authorization.

Issue #346 remains open. This note does not claim the 17 structured entity kinds or their end-to-end producers are complete.
