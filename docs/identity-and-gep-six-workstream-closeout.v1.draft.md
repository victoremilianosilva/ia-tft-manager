# Identity and GEP Six-Workstream Closeout v1

**Status:** documentary reconciliation; no runtime acceptance.  
**Branch:** `new-arquiteture`.  
**Architecture:** Shadow remains canonical strategic context; PPO remains the learning/decision algorithm.  
**Implementation boundary:** no runtime changes before Gate 8 and explicit user authorization.  
**Tracking:** issue #346.

## Executive result

The six requested workstreams have been reconciled against the existing source-audit documents and the current cross-repository contracts. Several workstreams were already documented in earlier PRs; this closeout consolidates their actual coverage and prevents their documentary completion from being mistaken for runtime readiness.

| # | Workstream | Documentary disposition | Remaining blocker |
|---|---|---|---|
| 1 | Python identity and test-hook call sites | Complete for 125/125 tracked Python files in the audited tree snapshot | No runtime identity transport; no tests executed by this inventory |
| 2 | C++ identity and test-hook callers | Complete for 48/48 tracked C++ test files; explicit identity/test-hook references reconciled across 127/127 tracked C++ files | Not proof of every implicit copy/assignment/destruction path or all indirect production callers |
| 3 | Canonical identity namespace proposal | Semantic contract exists: logical game match, Engine-instance-plus-episode scope, Viewer session, episode counter, player seat, and typed sequences remain distinct | No authoritative game-match producer, no Engine-instance scope producer, no canonical decision/snapshot sequence |
| 4 | GEP match identity producer | Cross-repository envelope/state contract reconciled; envelope `gameId`, `sessionId`, `revision`, and `capturedAt` are not canonical Engine identity | Exact GEP leaf path is now source-traced and numeric-to-string conversion is tested synthetically; real-game availability, per-match uniqueness and controller reset/reconnect lifecycle remain unproven |
| 5 | Schema v2 and producer reconciliation | Schema v2 identity semantics, namespace registry, crosswalk, field/source CSV and structured-entity matrix are cross-linked | Schema/CSV are documentary; structured records and exact identity are not delivered to PPO/rollout |
| 6 | Issue #346 and producer audit status | Evidence and remaining criteria consolidated; item-elimination domain decision is settled separately | #346 remains open until every entity producer/delivery and end-to-end acceptance criteria are proven |

## 1. Python identity and test-hook inventory

The Python inventory enumerates all 125 tracked `.py` files in the audited `new-arquiteture` tree: 66 test files and 59 other Python files.

Observed test-hook calls:
- `set_unit_for_testing`: two test files only.
- `set_shop_offer_for_testing`: one test file only.
- `set_next_shop_roll_for_testing`, `set_unit_items_for_testing`, and `get_combat_team_for_testing`: no Python call sites found.

The inventory distinguishes native episode metadata, Viewer-owned session UUID, diagnostic UnitInstance UUID consumers, and synthetic test identifiers. It does not claim that Python creates canonical native identity. The schema validator can verify envelope completeness/hash consistency, but cannot create missing producer-owned namespaces.

Source record: `docs/python-identity-test-hook-callsite-inventory.v1.draft.md`.

## 2. C++ test-hook and identity caller audit

All 48 tracked C++ test files were inspected for the five test-hook names and identity references. Direct Engine test-hook calls are concentrated in `cpp/tests/test_tft_engine_pool.cpp`. The test inventory and binding audit distinguish three pybind-exposed fixture hooks from C++-only item/combat fixture helpers.

The broader 127-file C++ reconciliation covers explicit identity/test-hook references. It does **not** prove every implicit value copy, assignment, destructor, or indirect production caller. The production lifecycle evidence for UnitInstance transfer, rollback copies, projection copies, merge, sale, elimination and reset remains in the dedicated lifecycle audits.

Source record: `docs/cpp-identity-test-hook-caller-audit.v1.draft.md`.

## 3. Canonical identity namespace decision

The accepted semantic distinction is:

- `match_id`: validated logical game-match identity from an authoritative game/platform producer.
- `engine_match_id`: canonical Engine episode scope with semantics equivalent to `(engine_instance_scope, episode_id)`.
- `session_match_id`: Viewer recording/session UUID only.
- `episode_id`: native counter local to one `TFTEngine::Impl` lifetime.
- `player_id`: episode-local seat token `player-0` through `player-7`, scoped by Engine episode.
- UnitInstance `uuid`: seeded physical-instance token; it may repeat across same-seed Engine resets/objects and is not globally unique.
- GEP `revision`, Viewer sequence, JSONL append sequence, native strategic sequence and PPO rollout index remain separate namespaces.

No concrete UUID/token algorithm is selected. No producer is claimed for the currently missing canonical Engine scope or decision/snapshot sequences.

Source records: `docs/observation-schema-v2-identity-field-semantics-reconciliation.v1.draft.md`, `docs/engine-identity-scope-reconciliation.v1.draft.md`, and `docs/decision-identity-schema-v2-design.v1.draft.md`.

## 4. GEP source identity reconciliation

The Overwolf mapper source now confirms the intended logical match leaf `info.match_info.match_info.match_id`, with numeric-to-string normalization. Its automated fixture uses synthetic value `778899`; this is not a real GEP capture. The envelope also exposes metadata `gameId`, `sessionId`, `revision`, and `capturedAt`. These are not interchangeable:

- `gameId` is not accepted as a per-match identifier.
- `sessionId` identifies capture/transport session, not Viewer session.
- `revision` orders source updates in its declared scope; it is not an Engine decision/snapshot sequence.
- `capturedAt` is timestamp metadata.

The exact source leaf and conversion are now proven at mapper level, but only against synthetic test input. The audited evidence set still lacks a sanitized real-game fixture proving source availability, uniqueness across consecutive matches, reconnect behavior, controller invocation of manager reset, and transport preservation. The recorder emits a new full snapshot when the known match ID changes, but this alone does not reset the manager session/revision. Therefore `identity.match_id` remains unavailable for canonical Decision Identity v2 until real-source and lifecycle acceptance pass.

No GEP path mapping is moved into Python or C++; Overwolf/Electron remains the sole GEP interpreter. The native live importer and transport remain unimplemented; capture-only JSONL and the Python loopback receiver do not prove live inference.

Source records: `docs/overwolf-live-state-integration-boundary.md`, plus the cross-repository `GEP_MAPPING.md`, `NATIVE_ENGINE_LIVE_IMPORT_AUDIT.md`, and `CANONICAL_TFT_LIVE_STATE.md`.

## 5. Schema v2 and machine-readable reconciliation

Schema v2 remains a draft contract, not a runtime payload. The field/source crosswalk and structured-entity coverage CSV are indexes of evidence and dispositions; they do not promote a field to available merely because a schema declares it.

The current evidence continues to distinguish:
- native observed/derived data;
- diagnostic-only and Shadow-only data;
- unavailable or not-produced data;
- data present natively but not exposed to Python;
- data whose source sequence/identity is not correlated;
- PPO's current flat observation and separately fetched masks.

The identity hash cannot be complete when authoritative `match_id`, Engine-instance scope, or typed decision/snapshot sequences are absent. The wrapper/rollout path still lacks the exact shared identity needed to bind observation, masks, action, reward, next state and replay.

Source records: `spec/observation-schema.v2.draft.json`, `spec/sequence-namespace-registry.v2.draft.json`, `spec/decision-identity-v2-hash-vectors.draft.json`, `spec/observation-schema-v2-field-source-crosswalk.v1.draft.csv`, and `spec/observation-structured-entity-producer-coverage.v1.draft.csv`.

## 6. Issue #346 disposition

Issue #346 must remain open. Documentary coverage now spans all 17 structured entity kinds and the enumerated field families, but source presence, diagnostic serialization, Python exposure, PPO delivery and integrated replay are different acceptance levels.

The issue can only be closed after:
1. every declared entity/field has a source-backed producer or explicit accepted unavailable disposition;
2. identity, ownership, cardinality, completeness, provenance, source sequence, lifecycle and reset semantics are proven;
3. native → pybind → wrapper → vector environment → rollout delivery is correlated to one exact typed decision;
4. the sanitized GEP match identity and source lifecycle are validated, or canonical `match_id` remains explicitly unavailable and the relevant live integration scope is adjusted;
5. deterministic multi-round replay proves the full supported chain and negative cases;
6. all dependent schema, CSV, producer and gate documents are internally consistent.

### Separate resolved domain decision: eliminated-player items

The domain owner decided that eliminated-player items must not be transferred to anyone. The accepted direction is terminal retirement/discard: no transfer to another player, no return to the eliminated player's active bag, and no redistribution to shared pool, shop or PvE reward sources. This resolves the domain-choice question, **not** the implementation or issue #346 acceptance. Required regression tests remain post-Gate 8.

Source record: `docs/elimination-item-terminal-policy-proposal.v1.draft.md`; decision recorded in PR #416.

## 7. Gate and implementation boundary

This closeout does not accept Gates 1–7 for runtime and does not authorize Gate 8. Existing documentary contracts can be reviewed as a coherent set, but implementation acceptance still requires the integrated gate review and explicit user authorization.

No Engine, PPO, reward, observation, action-mask, training, Viewer, checkpoint, Overwolf or runtime source is changed by this document.

## 8. Reconstruction review

1. **Prior problem:** six audit workstreams existed across separate documents, with differing scopes and the risk of treating a documented field or source reference as end-to-end proof.
2. **Technical rationale:** source identity, transport identity, Engine episode scope, decision correlation and PPO delivery have different owners and failure boundaries.
3. **New responsibility:** this closeout owns the consolidated status and explicit limitations for the six workstreams.
4. **Contract/invariants:** no synthetic identity; no aliasing of GEP/session/Viewer/Engine namespaces; no source-to-PPO claim without delivery proof; unavailable stays unavailable; no item redistribution after elimination.
5. **Cross-component impacts:** Overwolf capture, canonical envelope, native Engine, pybind, Python wrapper, vector environment, PPO rollout, Viewer, Schema v2, structured-entity matrix and issue #346.
6. **Objective validation:** references are cross-linked to the underlying audits; coverage counts and limitations are explicit; no runtime files or tensor layouts are changed.



## 9. GEP match identity evidence refinement — 2026-11-15

The exact mapper path is no longer an unknown: `info.match_info.match_info.match_id` is read by the Overwolf mapper and numeric values are normalized to strings. The test fixture uses synthetic `778899`. The snapshot manager's `sessionId` is generated independently and regenerated only by explicit `reset()`; revision resets with it. The recorder treats a changed known match ID as a new snapshot baseline without independently resetting that manager session.

This narrows, but does not close, the blocker: real-game source presence, per-match uniqueness, reconnect/reset invocation and sanitized fixture evidence remain outstanding. See [Overwolf GEP live-state integration boundary](overwolf-live-state-integration-boundary.md), section “GEP match ID source-path and lifecycle evidence”.
