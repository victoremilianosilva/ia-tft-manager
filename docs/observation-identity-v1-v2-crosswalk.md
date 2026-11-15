# Observation Identity v1 → v2 Crosswalk

**Status:** documentary migration map; v1 artifacts remain immutable.  
**Source:** `spec/observation-schema.v1.draft.json`, Observation Producer/Binding Audit v1, Action/Mask Contract v1.

| v1 field | v1 meaning/type | v2 disposition | Migration rule |
|---|---|---|---|
| `match_id` | nullable string; authoritative logical game-match identity, not Viewer session ID | Preserve | Copy only from validated game/platform source; if absent, v2 identity is incomplete |
| `engine_match_id` | nullable string; canonical Engine-episode scope (Engine-instance scope + episode) | Preserve as a distinct field | Current numeric `episode_id` alone is insufficient; require an authoritative scoped producer before marking complete |
| `player_id` | nullable string; canonical token `player-0`…`player-7` encodes the native episode-local seat/index | Preserve as a typed seat token | Required for complete v2 identity and scoped by `engine_match_id`; not a persistent player UUID |
| `round` | nullable non-negative integer | Preserve | Required for complete v2 identity |
| `decision_sequence` | nullable integer | Breaking type change to `{namespace,value}` or null | Namespace must be proven from its producer; current audit does not establish a canonical Engine decision counter |
| `snapshot_sequence` | nullable integer | Breaking type change to `{namespace,value}` or null | Namespace must be proven from the snapshot producer; no typed native observation snapshot is currently transported through the Python wrapper |
| `player_sequence` | nullable integer | Typed producer-local reference or null | Preserve owner-local meaning only after producer/scope verification; never alias Engine decision sequence |
| `event_sequence` | nullable integer | Typed producer-local reference or null | Preserve event producer namespace only after source verification; otherwise null/incomplete |
| `session_match_id` | nullable string; ViewerSession recording UUID | Preserve as session correlation metadata | Map ViewerSession.match_id here; never promote it to canonical `match_id` or `engine_match_id` |
| `episode_id` | integer/string/null; native counter local to one TFTEngine::Impl | Preserve as episode metadata | Not globally unique, not a decision counter, and excluded from decision hash; insufficient alone for `engine_match_id` |
| `captured_at` | date-time string | Preserve as capture metadata | Not a sequence and excluded from decision hash |
| `status` | complete/partial/session_only/missing/stale/incompatible | Extend in v2 | Add unsupported/conflict; non-complete statuses require reason and null identity hash |
| `reason` | optional string | Preserve; required for non-complete | Explicit reason; never silently downgrade unknown data to complete |
| `decision_identity_hash` | v1 hash or null | New v2 hash; v1 hash historical-only | Never relabel, recompute or compare v1 hash as v2 |
| `decision_identity_hash_scope` | v1 fixed scope over untyped integers | New v2 fixed scope includes namespace IDs and values | Keep v1 scope unchanged; v2 hashes include identity_version |
| `legal_state_context.mask_reference` | semantic reference; audit says not correlated | v2 exact identity + mask payload hash reference | v1 reference alone cannot prove exact observation-mask pairing |
| `player_sequence` / `event_sequence` source metadata | owner-local counters | Typed references | Unknown namespace blocks canonical correlation |
| PPO rollout timestep/batch index | not a v1 identity field | Separate training metadata | Never substitute for Engine decision identity |

## Payload hash separation

Decision identity hash answers: "which logical Engine decision/snapshot pair is this?"

Observation content hash answers: "which exact serialized observation payload is this?"

Mask content hash answers: "which exact ordered mask payload is this?"

These hashes are independent. A payload can be malformed or stale while carrying a syntactically complete identity. A payload-content change does not change decision identity hash; it must change the relevant payload hash. The current audited producers do not prove that observation or mask payload hashes are emitted, so the v2 schema's payload-hash requirements remain a future producer contract, not a present capability.

## Compatibility

- v1 schema, source/legacy/migration maps, fixtures, identity hash semantics and historical checkpoints remain unchanged.
- v1 records can be read under v1 rules only.
- v1→v2 conversion is conditional. If original producer provenance cannot establish a namespace, the converted record is incomplete for v2 canonical correlation.
- No inferred namespace based on call order, timestamps, player/round, array index or equal numeric values.
- A v1 mask reference cannot be promoted to v2 exact mask binding without reconstructing and validating source identity, ordering and payload hash.
