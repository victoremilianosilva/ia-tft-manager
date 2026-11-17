# Sequence Namespace Registry v2 — Proposal

**Status:** proposed documentary registry; no namespace is approved for canonical runtime use by this document alone.  
**Identity envelope:** `tft.decision-identity.v2`  
**Schema:** Observation Schema v2 proposal.

A namespace identifies one producer-owned counter domain. The integer value has no cross-namespace meaning. A namespace entry is not evidence that its producer currently emits a suitable counter.

## Availability classifications

- `observed_in_audit`: a sequence-like value/domain was found in the audited code or diagnostic model; this does not establish canonical PPO correlation.
- `proposed_not_implemented`: intended future namespace; no current producer guarantee is claimed.
- `requires_runtime_verification`: the domain exists in the audited design, but exact reset/monotonicity/transport behavior is not sufficiently proven for canonical use.

## Identity envelope scope fields

The registry's `engine_match_id` scope means a canonical Engine episode identity that distinguishes both the native Engine object lifetime and its `episode_id` within that object. The current native `episode_id` alone is not sufficient: independent Engine objects can share the same numeric episode value, and same-seed UnitInstance UUID sequences can repeat across Engine resets/objects.

The other identity fields have separate owners and meanings:

| Envelope field | Meaning | Current status |
|---|---|---|
| `match_id` | Authoritative logical game-match identity from a validated game/platform source; never the Viewer session UUID | No authoritative producer proven in the audited main-repository path |
| `engine_match_id` | Canonical Engine-instance + episode scope | Not currently produced; `episode_id` alone is insufficient |
| `session_match_id` | ViewerSession recording/session UUID | Produced by Viewer; correlation only |
| `episode_id` | Native counter local to one `TFTEngine::Impl` lifetime | Produced by native Engine and pybind; wrapper drops it from training-facing reset/step |
| `player_id` | Native seat index encoded as `player-0` through `player-7` | Episode-local token; not a persistent player UUID |

The current Viewer logger writes its own UUID into the legacy `match_id` property and separately carries native `episode_id` as `engine_match_id`. This is a session-correlation record, not a valid source for populating the v2 canonical fields. A v2 adapter must place the Viewer UUID in `session_match_id`; if authoritative `match_id` or scoped `engine_match_id` is missing, identity status remains incomplete. Native player seat N is serialized as the canonical string `player-N` (N=0…7) because the v2 field is a string; this does not imply a persistent participant identity.

## Registry

| Namespace ID | Producer / owner | Scope and meaning | Reset / monotonicity | Availability | Canonical decision eligible |
|---|---|---|---|---|---|
| `tft.engine.decision` | Native Engine; proposed owner | Per-player decision counter within one `engine_match_id` | Must be monotonic for that player/match; reset only with new Engine match identity; no wrap | `proposed_not_implemented`; current PPO path does not transport it | No, until implemented and proven |
| `tft.engine.observation-snapshot` | Native Engine observation producer; proposed owner | Exact observation snapshot for one player decision | Must bind atomically to decision identity; reset with Engine match identity | `proposed_not_implemented`; current wrapper returns observations without typed identity | No, until implemented and proven |
| `tft.engine.action-mask-snapshot` | Native ActionMaskEngine; proposed owner | Exact ordered mask payload for one decision | Must be generated/bound to the same decision identity as observation; reset with Engine match identity | `proposed_not_implemented`; current masks are retrieved separately and have no typed identity/hash envelope | No, until implemented and proven |
| `tft.composition-intelligence.player-sequence` | Composition Intelligence player runtime | Player-local CI runtime sequence | Audit identifies player-local sequence and Engine reset clears CI runtime state; monotonicity and serialized transport require runtime verification | `observed_in_audit` / `requires_runtime_verification` | No; owner-local evidence reference only |
| `tft.shadow.native-strategic-snapshot` | Native strategic snapshot producer | Strategic snapshot sequence domain | Namespace is distinct from CI/player and JSONL sequences; exact reset/monotonicity requires runtime verification | `observed_in_audit` / `requires_runtime_verification` | No; owner-local evidence reference only |
| `tft.shadow.context-bridge.player-sequence` | ContextBridge/player adapter | Player-scoped bridge correlation sequence | Must not be equated with Engine, CI or Viewer counters; reset and monotonicity require runtime verification | `observed_in_audit` / `requires_runtime_verification` | No; bridge correlation only |
| `tft.shadow.diagnostic-jsonl-append` | Diagnostic recorder / JSONL writer | Append order in one recorder stream/file | Recorder/file lifecycle defines scope; not a game decision counter | `observed_in_audit` / `requires_runtime_verification` | No; recorder ordering only |
| `tft.viewer.session-sequence` | Viewer session/replay adapter | Session-local display/replay ordering | Resets with Viewer session; never replaces Engine identity | `observed_in_audit` | No; session correlation only |
| `tft.ppo.rollout-timestep` | PPO collector/rollout | Position in a rollout collection stream | Resets/advances according to collector lifecycle; batch position is not a source decision counter | `observed_in_audit` | No; training-order metadata only |

## Registration and promotion rules

1. Namespace IDs are stable and never reused for a different producer, counter meaning or scope.
2. Every namespace must declare one accountable producer/owner, scope, monotonicity, duplicate-delivery semantics, reset boundary and availability evidence.
3. A namespace marked `proposed_not_implemented` cannot appear in a complete runtime decision identity.
4. A namespace marked `observed_in_audit` is not automatically eligible for canonical decision or mask correlation.
5. A producer-local reference may be attached to evidence as a typed source reference, but it cannot replace the Engine decision/snapshot references.
6. Promotion to canonical eligibility requires producer implementation, typed serialization, reset/stale/conflict tests, exact correlation evidence and an explicit registry revision.
7. Unknown namespace IDs are rejected for canonical correlation and retained only as diagnostics.
8. Sequence equality requires both namespace and value equality plus matching declared scope. No code may compare bare integer values across namespaces.
9. Engine match identity scopes per-match counters. Viewer/session, recorder, CI and rollout reset boundaries do not redefine Engine identity.
10. No timestamp, array index, synchronous call order or "latest available" lookup may synthesize a missing sequence reference.

## Current audit conclusion

The current native→Python PPO path has no typed decision identity envelope joining observation and masks. Native reset/step results expose masks and episode metadata, but the Python wrapper returns observations and retrieves masks through a separate call. The audit does not establish a canonical per-player Engine decision counter or an independently hashed mask snapshot. Therefore the three `tft.engine.*` entries above are future producer requirements, not current capabilities.

## Change control

Any change to producer ownership, scope, counter meaning, reset behavior or canonical eligibility requires a registry version change and the six-point architecture reconstruction review. Runtime implementation remains blocked until Gate 8 and explicit authorization.


## Native Engine sequence reconciliation (PR #428)

The native `TFTEngine::Impl::decision_sequence` is **not** a per-player decision counter. It increments once for each `ResetResult` or `StepResult`, is shared by all eight player observation rows, remains monotonic across episode resets, and is scoped to one Engine instance. In Decision Identity v2 it maps to `snapshot_sequence` under `tft.engine.observation-snapshot`.

The namespace `tft.engine.decision` remains reserved for a future authoritative per-player decision counter and is not populated from the native snapshot counter. Until that counter and authoritative `match_id` are available, identity remains `partial`, its decision identity hash remains null, and mask/Critic/anti-loop/strategic-owner contexts cannot be marked valid by matching local integer values.
