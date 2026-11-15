# Overwolf GEP live-state integration boundary

**Status:** approved architectural boundary; production import and live inference acceptance remain unimplemented.

## Purpose and scope

This document reconciles the Overwolf capture repositories with the canonical Shadow/PPO architecture in this repository. It defines the ownership and evidence boundary between GEP capture, canonical live-state transport, native Engine import, PPO inference, and read-only recommendations.

This is an integration contract and audit record. It does not claim that a live Overwolf match currently reaches native observations or PPO inference.

## Canonical ownership

1. **Overwolf/Electron application** is the sole interpreter of Overwolf Game Events Provider (GEP) paths. It merges GEP deltas, reconciles its capture baseline, applies privacy filtering, and emits the canonical `tft.live-state` contract.
2. **Python inference boundary** validates the canonical envelope, schema version, revision ordering, privacy constraints, finite values, and structural shape. It must not contain GEP path mappings.
3. **Native Engine live importer** owns conversion from the validated, GEP-independent DTO into coherent native state. It must not interpret GEP paths or silently simulate missing state.
4. **Native Engine rules and masks** remain the final authority for action legality. Live inference is read-only and recommendation-only.
5. **PPO policy** consumes only the approved observation projection and matching masks. Shadow recommendations, evaluator scores/rankings, diagnostic Unified Shadow state, and executor diagnostics are not PPO labels, reward targets, or imitation targets.
6. **Viewer/diagnostics** may display and record correlated observations and recommendations, but must preserve provenance, missingness, and source sequence.

## Canonical transport contract

The current Overwolf integration contract uses envelope schema v2 with:
- `schemaVersion`, `gameId`, `sessionId`, `revision`, `capturedAt`, `complete`, and `state`;
- `state.contract = "tft.live-state"` and `state.contractVersion = 1`;
- known/unknown wrappers for scalar values;
- explicit known-empty versus unknown board, bench, and shop slots;
- local-player index and roster positions without names or account identifiers;
- only opponent fields actually reported by the source.

Schema v1, which carried raw GEP `info`, is rejected. A producer/consumer version mismatch must fail closed.

Unknown values must remain unknown. In particular, absent gold is not zero, an unknown slot group is not an empty board, carousel suggestions are not inventory, and historical match-stat boards are not current opponent boards.

## Capture and privacy boundary

- GEP event-path interpretation, delta merging, baseline reconciliation, and feature allowlisting belong exclusively to Overwolf/Electron.
- Python and C++ must not map raw GEP paths such as `me.me.gold`, `board.board_pieces`, or `cell_N`.
- Raw capture and canonical payload audit streams are separate evidence artifacts; they must be sanitized before persistence.
- Credentials, tokens, passwords, authorization values, PUUIDs, account identifiers, and other sensitive identity fields must not enter logs or inference payloads.
- Raw event volume is not equivalent to meaningful state transitions. Any deduplication policy must preserve revision/sequence provenance and must not discard a change that affects the canonical state.
- Capture-only JSONL output does not prove that an inference transport, native importer, or live recommendation path exists.

## Native import: required behavior and current gap

The integration repository documents a GEP-independent `LiveState` DTO and validation layer. That is a useful foundation, but it is not a production importer.

The existing simulated `TFTEngine` API exposes `reset()`, `step()`, observations, masks, and diagnostics. The inspected integration audit does not identify a production API that imports a canonical live snapshot into a coherent native match state. Test-only setters are not production import APIs.

A production importer must reconcile, as one validated snapshot:
- match/player identity and source revision;
- board and bench unit instances, stars, slots, and equipment;
- local shop offers and their exact source revision;
- economy and progression values;
- loose item/component inventory and item ownership;
- round/stage and player liveness;
- all derived strategy/composition state and action-mask inputs.

Importing only board/bench arrays is insufficient. The current native lobby also owns shop, item, pool, strategy, and mask state; an importer must either reconcile each relevant domain or mark dependent observation features unavailable.

The importer must:
1. validate catalog IDs, dimensions, ranges, uniqueness, and identity;
2. preserve unknown versus known-empty versus known-zero;
3. correlate match/session/player/revision and reject stale or out-of-order snapshots;
4. rebuild or invalidate all derived state affected by the import;
5. avoid drawing from pools, granting PvE rewards, advancing rounds, running combat, applying economy transitions, spending currency, or executing actions;
6. expose unavailable observation features rather than synthesizing defaults;
7. be idempotent for a repeated revision and reset its correlation state only at an explicit match/session boundary.

**Current status:** DTO validation is documented; production import into `TFTEngine::Impl` is not established by the inspected integration audit. Native simulation observations/masks must not be represented as live-match observations/masks until this importer and its acceptance tests exist.

## Live recommendation sequence

The intended read-only sequence is:

```text
GEP events
  -> Overwolf delta/baseline reconciliation
  -> canonical tft.live-state v2 envelope
  -> Python schema/privacy/revision validation
  -> native LiveState DTO validation
  -> dedicated native production import API
  -> approved observation projection + native legality masks
  -> PPO inference
  -> immutable recommendation with source identity/revision
  -> Viewer/overlay presentation
```

No recommendation is sent back as a TFT game action. No `step()` or simulated-lobby transition is allowed in the live path.

Every recommendation must retain the exact source match/session/player/revision and the observation/contract version used to produce it. A newer imported revision invalidates recommendations derived from older state.

## Evidence required before claiming live integration

The following are separate acceptance claims and must not be conflated:

| Claim | Minimum evidence |
|---|---|
| GEP capture works | Sanitized real-game GEP fixture with documented source paths, types, slot conventions, and null/removal semantics |
| Canonical producer works | Deterministic tests for baseline + deltas, known/unknown semantics, revision ordering, match changes, and privacy redaction |
| Transport works | Authenticated/local transport contract and integration test proving the exact v2 envelope reaches the intended consumer; capture-only JSONL is insufficient |
| Native DTO works | Unit tests for validation and malformed/unknown values |
| Native import works | Production API integration tests proving coherent board, bench, shop, items, economy, identities, derived state, masks, stale rejection, idempotency, and two consecutive matches |
| Live observations work | Feature-by-feature provenance showing each observation comes from the imported revision or is explicitly unavailable |
| PPO inference works | Checkpoint/observation/action-mask contract hashes, deterministic inference fixture, and source-revision correlation |
| End-to-end recommendation works | Sanitized real-match fixture/replay from GEP through recommendation, with no call to `reset()`/`step()`, no action execution, and stale recommendation rejection |

A native DTO test, a simulated Viewer session, a JSONL capture, or a green CI workflow alone does not satisfy end-to-end live integration.

## Cross-repository responsibilities

- `tft-manager-ow`: GEP capture, Electron lifecycle, privacy sanitization, canonical state construction, and capture audit artifacts.
- `ia-tftmanager-ow`: production inference host, Python validation, native DTO/import integration, checkpoint loading, and read-only recommendation delivery.
- `ia-tft-manager`: canonical Engine/observation/action-mask/PPO contracts, training lineage, evaluation protocol, and Shadow strategic context.

The repositories must share versioned schemas and fixtures, not duplicate GEP interpretation or independently redefine field semantics.

## Reconstruction review

1. **Prior problem:** native simulation APIs and GEP capture artifacts could be mistaken for a complete live inference path; a DTO foundation could be mistaken for a production importer; the GEP mapping ownership was not stated in this repository's canonical architecture index.
2. **Technical rationale:** separate capture, transport, import, observation projection, inference, and recommendation acceptance into independently verifiable boundaries.
3. **New responsibility:** this document owns the cross-repository live-state boundary and acceptance evidence map; it does not implement or replace any runtime component.
4. **Contracts and invariants:** Overwolf alone interprets GEP; unknown remains unknown; source revisions are correlated; native rules/masks own legality; the Engine never advances a live match; recommendations remain read-only; Shadow diagnostic outputs are not PPO supervision.
5. **Cross-component impact:** Overwolf GEP producer, canonical transport schema, Python validation, native LiveState DTO/importer, observation schema, action/mask contract, PPO checkpoint contract, Viewer/overlay, replay, and privacy logs.
6. **Objective validation:** static reconciliation against `ia-tftmanager-ow/docs/GEP_MAPPING.md`, `docs/NATIVE_ENGINE_LIVE_IMPORT_AUDIT.md`, `tft-manager-ow/docs/CANONICAL_TFT_LIVE_STATE.md`, and the approved canonical contracts in this repository. This PR is documentation-only and does not claim runtime acceptance.

## GEP match identity: exact source field and lifecycle remain unverified

The envelope-level `gameId` is the Overwolf game/product identifier and must not be copied into canonical Decision Identity v2 `match_id` merely because the names are similar. The canonical contract separately describes a logical match identifier inside the live-state state model when the source reports one. These are distinct claims:

- `gameId`: envelope/source metadata; not accepted as per-match identity.
- `sessionId`: Overwolf capture/transport session metadata; not Viewer `session_match_id`.
- `revision`: source-state revision within its producer scope; not Engine decision or observation sequence.
- `capturedAt`: timestamp metadata; not a sequence.
- canonical state match identifier: may populate v2 `match_id` only after the exact GEP leaf path, type, uniqueness across consecutive matches, reconnect behavior, reset boundary, and transport preservation are demonstrated from a sanitized real-game fixture.

The mapper implementation now identifies the exact intended source leaf: `info.match_info.match_info.match_id` in `src/browser/services/gep/tft-live-state.mapper.ts`. It converts a textual value directly or a numeric value to its decimal string. The automated snapshot-manager test supplies a synthetic `778899` value at that path and asserts the canonical `state.matchId.value`. This proves the mapper path and conversion behavior against a synthetic fixture, not that a real GEP payload reliably supplies the field. Until a sanitized real-game fixture and lifecycle tests exist, v2 `match_id` remains unavailable for canonical identity. Do not synthesize it from `gameId`, `sessionId`, timestamps, directory names, or Viewer UUIDs.

## Gate boundary

No runtime, Engine, PPO, observations, masks, rewards, training, Viewer, checkpoint, or artifact changes. This document does not close integration issues or advance a gate. Gate 8 remains blocked until Gates 1–7 are fully reviewed and explicit implementation authorization is given.



## Live-state source identifiers versus canonical Engine identity

The envelope fields gameId, sessionId, revision and capturedAt are source/capture metadata. They must not be promoted to canonical Decision Identity v2 fields solely because their names look similar:

- gameId is not assumed to identify one match; it must be proven per-match unique before it can populate canonical match_id.
- sessionId identifies the Overwolf capture/transport session. It is not automatically the ViewerSession UUID or the v2 session_match_id.
- revision orders source live-state updates within the producer's declared session/scope. It is not the native Engine episode_id, canonical decision_sequence, observation snapshot_sequence, or mask sequence.
- capturedAt is timestamp metadata, not a substitute for any typed sequence.
- local-player index may be mapped to the v2 player-N seat token only after the source contract confirms it represents the same 0–7 seat domain.

A native importer must preserve source game/session/revision references and native Engine-instance/episode identity as distinct fields. Any mapping between them must be explicit, versioned, and validated across reconnect, reset, stale delivery and consecutive matches. Missing canonical match_id or engine_match_id keeps the v2 decision identity incomplete; capture-only identifiers cannot make it complete.


## GEP match ID source-path and lifecycle evidence — 2026-11-15

A focused source pass in `tft-manager-ow` establishes the following implementation facts:

| Concern | Source evidence | What it proves | What it does not prove |
|---|---|---|---|
| Logical match leaf | `src/browser/services/gep/tft-live-state.mapper.ts`, `mapGepInfoToCanonicalState()`, reads `info.match_info.match_info.match_id` | Exact current mapper path | That every real GEP baseline/update contains this leaf |
| Type normalization | Same mapper uses `textValue(rawMatchId)`, then numeric conversion to decimal string | String and numeric inputs are normalized to canonical string | Uniqueness or stability of the value across actual matches/reconnects |
| Automated fixture | `scripts/test-tft-snapshot-manager.js` supplies `match_info.match_info.match_id: 778899` and asserts `state.matchId.value === "778899"` | Mapper behavior for a synthetic numeric value | Real-game capture; the fixture is authored test data |
| Source game ID | `src/browser/services/gep/tft-game-id.ts` normalizes Overwolf game ID 28164 to GEP supported game ID 21570 | `gameId` is game/product identification | Per-match identity; it must not populate canonical `match_id` |
| Capture session | `src/browser/services/gep/tft-snapshot.manager.ts` initializes `sessionId = randomUUID()`; `reset(gameId)` creates a new UUID and resets revision to zero | Capture-session identity and explicit reset behavior | That every logical match transition invokes reset |
| Revision/timestamp | Same manager increments revision and refreshes `capturedAt` when merged canonical source info changes | Revision is a manager-local update counter and timestamp is capture metadata | Native Engine decision/snapshot sequence |
| Match-change recording | `src/browser/services/gep/tft-snapshot.recorder.ts` treats a changed known `state.matchId` as a new full snapshot baseline | Recorder notices a changed logical match value | That manager session/revision scope was reset at that point |
| Recorder test | `scripts/test-tft-capture-recorder.js` uses synthetic `match-a`/`match-b` and expects a new snapshot for the changed match | Recorder baseline behavior under synthetic match change | Production event lifecycle or actual GEP match semantics |

### Lifecycle interpretation

The source currently separates:
- `gameId`: normalized Overwolf/GEP game identifier;
- `sessionId`: random capture-manager session identifier, regenerated by explicit `TftSnapshotManager.reset()`;
- `revision`: manager-local counter reset by that same method and incremented on canonical state changes;
- `capturedAt`: timestamp refreshed when revision increments;
- `state.matchId`: mapped from the nested GEP match-info leaf.

The recorder recognizes a changed `state.matchId` and writes a full snapshot, but the inspected recorder logic does not itself reset the manager's `sessionId` or `revision`. The event/controller path that decides when `reset()` is called for a new match or reconnect still needs direct lifecycle proof. A changed logical match value and a new capture session are not interchangeable.

### Acceptance still required

1. Capture a sanitized real GEP baseline containing the exact nested leaf, with privacy-safe surrounding structure.
2. Capture two consecutive real matches in the same client process and compare the leaf values.
3. Exercise reconnect, game exit/re-entry, and a new-match transition; prove when the controller invokes manager reset.
4. Verify the expected relationship among `state.matchId`, `sessionId`, `revision`, and `capturedAt` across each transition.
5. Prove missing/null/malformed leaf behavior remains unknown and cannot reuse a previous match identifier.
6. Preserve the fixture and lifecycle expectations as deterministic regression tests without committing personal identifiers.

**Disposition:** exact mapper source path and synthetic conversion test are now proven. Real-source availability, uniqueness, reconnect semantics and reset invocation remain unproven. Canonical v2 `match_id` remains unavailable until those acceptance cases pass.

