# GEP Match ID Source Path and Lifecycle Audit v1

**Status:** source-path proof complete; authoritative real-source lifecycle proof pending.  
**Repositories inspected:** `victoremilianosilva/tft-manager-ow`, reconciled into `victoremilianosilva/ia-tft-manager`.  
**Target branch:** `new-arquiteture`.  
**Scope:** documentation only; no Overwolf or runtime code changes.  
**Canonical rule:** Shadow remains strategic context; PPO remains the learning/decision algorithm.  
**Gate:** no implementation before Gate 8 and explicit user authorization.

## 1. Prior problem

The architecture contract described a canonical logical match identifier inside `tft.live-state`, but prior identity reviews had not identified the exact GEP source leaf or distinguished mapper implementation evidence from real-game producer evidence. The envelope's `gameId`, `sessionId`, `revision` and `capturedAt` could be mistaken for a match identity or decision sequence.

## 2. Source findings

### 2.1 Exact source leaf and normalization

In `tft-manager-ow/src/browser/services/gep/tft-live-state.mapper.ts`, `mapGepInfoToCanonicalState()` reads:

```ts
const rawMatchId = get(info, "match_info", "match_info", "match_id");
const matchId = textValue(rawMatchId) ??
  (numberValue(rawMatchId) === null ? null : String(numberValue(rawMatchId)));
```

It publishes the result as `state.matchId = known(matchId)`.

This proves the mapper's exact intended path and its string/number normalization. It does not prove that a real GEP baseline always contains the field or that the value is unique across real matches.

### 2.2 Synthetic test evidence

`scripts/test-tft-snapshot-manager.js` builds a local fixture containing:

```js
match_info: {
  match_info: {
    match_id: 778899,
    round_type: { stage: "2-6", type: "PVP" }
  }
}
```

The test asserts `snapshot.state.matchId.value === "778899"`. This proves the mapper's synthetic numeric-input path. The value is authored test data, not a captured GEP identifier.

### 2.3 Game ID is not match ID

`src/browser/services/gep/tft-game-id.ts` distinguishes the Overwolf game ID 28164 from the GEP supported game ID 21570 and normalizes one to the other. This is game/product identification, not one-match identity. It must not populate canonical `identity.match_id`.

### 2.4 Capture session, revision and timestamp

`src/browser/services/gep/tft-snapshot.manager.ts` establishes:
- `sessionId` is generated with `randomUUID()` when the manager is constructed;
- `revision` begins at zero;
- `reset(gameId)` creates a new `sessionId`, resets source info and revision to zero, and marks the baseline incomplete;
- merged canonical source changes increment revision and refresh `capturedAt`;
- `getSnapshot()` emits the envelope fields independently from `state.matchId`.

Thus capture session, source revision, timestamp and logical match ID are distinct producer values.

### 2.5 Recorder behavior on match changes

`src/browser/services/gep/tft-snapshot.recorder.ts` compares known `state.matchId` with its prior value. If it changes, the recorder emits a new full `state_snapshot` rather than a delta. It updates its remembered match ID and revision after a successful append.

The recorder does not itself invoke `TftSnapshotManager.reset()`. A new snapshot baseline is not equivalent to a new manager session or a revision reset.

`scripts/test-tft-capture-recorder.js` uses synthetic `match-a` and `match-b` values to verify this baseline behavior. It does not prove the production controller's event lifecycle.

## 3. Reconciled identity semantics

| Field | Meaning | Canonical v2 use |
|---|---|---|
| GEP `state.matchId` | Intended logical match identifier mapped from nested GEP match-info leaf | Candidate source for `identity.match_id`, pending real fixture/lifecycle validation |
| Envelope `gameId` | Overwolf/GEP game/product identifier | Never substitute for `match_id` |
| Envelope `sessionId` | Snapshot-manager capture session UUID | Source-session metadata only; not Viewer `session_match_id` |
| Envelope `revision` | Snapshot-manager source-state revision | Source revision only; not Engine decision/snapshot sequence |
| Envelope `capturedAt` | Snapshot generation timestamp | Audit metadata only; not a sequence |
| Viewer `session_match_id` | Viewer-owned recording/session UUID | Viewer correlation only |
| Native `episode_id` | Counter scoped to one `TFTEngine::Impl` lifetime | Native episode metadata only, not globally scoped `engine_match_id` |

## 4. Lifecycle questions still open

The mapper, manager and recorder source files do not by themselves establish when the production Overwolf event/controller invokes manager `reset()`. The following must be proven from controller source and real capture:

1. Does new TFT match start always trigger a new manager session?
2. Does game exit/re-entry or reconnect trigger reset, preserve session, or create a new manager?
3. Can two consecutive real matches share the same `state.matchId`?
4. Can the match ID be absent during initial baseline and appear later?
5. Can the field be removed or become null while old value remains merged in the baseline?
6. Does an out-of-order or delayed update from the previous match get rejected at the match boundary?
7. Does transport preserve the exact value and source provenance without replacing it?

No answer is inferred from the synthetic fixtures.

## 5. Acceptance criteria

- Sanitized real GEP baseline with the exact nested leaf and surrounding structure.
- Two consecutive real matches in one client process with expected distinct logical match values.
- New-match, reconnect, game exit/re-entry and missing-field lifecycle tests.
- Explicit proof of manager reset invocation and expected session/revision transitions.
- Tests proving absent/null/malformed values do not inherit stale prior match identity.
- End-to-end preservation of the typed source reference through canonical envelope and receiver.
- No credentials, player names, PUUIDs or account identifiers in committed fixtures.

Until those pass, canonical v2 `identity.match_id` remains unavailable even though the mapper's intended source path is now known.

## 6. Cross-component impacts

Overwolf GEP mapper, snapshot manager, capture recorder, canonical state contract, Python snapshot receiver, native live DTO/importer, Decision Identity v2, replay/Viewer correlation, and issue #346.

## 7. Gate boundary

This audit changes no Overwolf source, native Engine, Python wrapper, PPO, reward, observation, masks, training, Viewer, checkpoint, tensor layout, or runtime behavior. It does not close issue #346, accept Gates 1–7 for runtime, or authorize Gate 8.

## 8. Reconstruction review

1. **Prior problem:** the canonical state field existed in a contract without a source-path/lifecycle evidence distinction.
2. **Technical rationale:** exact mapper behavior, test fixture data, capture session, revision, timestamp and real GEP producer semantics are separate evidence levels.
3. **New responsibility:** this note owns the source-path and lifecycle evidence boundary for GEP logical match identity.
4. **Contract/invariants:** no aliasing of game ID/session/revision/timestamp to canonical match or Engine decision identity; synthetic fixtures are not real-source proof; unknown stays unavailable.
5. **Cross-component impacts:** Overwolf mapper/manager/recorder, canonical state, native importer, Python receiver, identity v2, Viewer/replay and issue #346.
6. **Objective validation:** mapper path and normalization are source-traced; synthetic test assertion is identified; manager/recorder lifecycle is source-traced; remaining real-source/controller criteria are explicit. Documentation only.
