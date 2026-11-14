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

## Gate boundary

No runtime, Engine, PPO, observations, masks, rewards, training, Viewer, checkpoint, or artifact changes. This document does not close integration issues or advance a gate. Gate 8 remains blocked until Gates 1–7 are fully reviewed and explicit implementation authorization is given.
