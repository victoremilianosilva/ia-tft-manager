# Schema v2 Strategic Owner Snapshot Field Proof v1 — Draft

**Status:** source-backed field-level audit of diagnostic owners; documentary only, not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.

## 1. Scope and core finding

This slice audits all 20 paths under `strategic_evidence.owner_snapshots`:
- `planner_commitment` (5 fields);
- `composition_intelligence` (8 fields);
- `unified_state_machine` (7 fields).

The three owners do have separate native state and diagnostic paths. They do **not** currently emit one uniform, typed `owner_snapshots` envelope with common owner ID, status, payload path and source decision sequence. Some values can be found in different diagnostic objects, but those values must not be silently combined into a synthetic snapshot.

## 2. Owner-by-owner evidence

### 2.1 StrategicPlanner commitment

`TftEngine.cpp` owns a per-player `strategic_planner_commitments` array. The commitment contains direction, core/flexible champion IDs, selected/review rounds, selection/revision reasons, confidence, review streak and candidate direction/anchor/score. The strategic evidence context receives match/player/round and a monotonically incremented `strategic_context_sequences[i]`, but that sequence is passed into the evaluation context and is not stored in `StrategicCommitment` itself (`TftEngine.cpp:3363-3401`; `StrategicPlanning.hpp:169-183`).

After evaluation, selected commitment/decision details are mirrored into `PlayerInfo` diagnostic fields. The code explicitly labels the candidate mirror as diagnostic-only compatibility telemetry; the planner does not read those fields back (`TftEngine.cpp:4300-4317`). Pybind exports these values as step-info fields, not as an owner snapshot and not in the PPO observation vector (`tft_engine_bindings.cpp:324-352,475-487`).

Consequences:
- no explicit `status`, `owner_id` or `payload_path` field exists for this owner;
- no source decision sequence is retained on the commitment;
- selection/revision reason and decision-path reason exist, but not as a single owner-snapshot reason envelope;
- diagnostic mirrors do not become canonical commitment state.

The commitment array and `strategic_context_sequences` are reset on Engine episode reset (`TftEngine.cpp:6177-6190`).

### 2.2 Composition Intelligence owner

`CompositionIntelligencePlayerRuntime` is explicitly one instance per player. It owns `ActiveCompositionManager`, `TransitionManager`, a diagnostic recorder and JSON snapshots. `begin_cycle` records match/player/round and resets stage sequence. `mark_stage` emits stage/status/reason, match/player/round, stage sequence and active composition identity/version. `append_snapshot` attaches match/player/round and a per-player diagnostic `player_sequence`; duplicate snapshots are deduplicated. `reset` clears active state, transitions, recorder, snapshots and sequences (`CompositionIntelligenceRuntime.hpp:12-105`).

The recorder's `CompositionDiagnosticSnapshot` serializes schema version, emission sequence, round, composition ID/version, stale flag/reason and diagnostic payload. The payload includes source metadata, composition decision, transition plan, optional published transition, unit intentions, lineup, evidence and action recommendation (`CompositionDiagnostics.hpp:22-51,61-131,133-195`).

These are real Shadow diagnostic surfaces, but:
- the diagnostic `sequence` and runtime `player_sequence` are emission/correlation counters, not a native decision sequence;
- no explicit `owner_id` is serialized (the owner is implied by the player-scoped runtime);
- `stale`/stage status and reasons are not a uniform owner status/reason envelope;
- active composition identity/version and transition plan/published transition are separate payload fields, not one canonical `active_composition`/ `transition_state` owner snapshot.

The pybind exposes `get_composition_diagnostics_jsonl`, but that endpoint is diagnostic export; it is not merged into reset/step observations or Trainer PPO inputs.

### 2.3 UnifiedStrategicShadowRuntime owner

`UnifiedStrategicShadowRuntime` refreshes a player-scoped `UnifiedStrategicStateMachine` and writes through `StrategicDirectionPivotAuditRecorder`. `StrategicCycleResult` contains a machine phase, anchor state, optional active composition, diagnostics, state-changed flag and `shadow_only` marker (`UnifiedStrategicStateMachine.hpp:59-66`).

The recorder writes a JSONL record with:
- `match_id`, `player_id`, round and per-player emission `sequence`;
- `phase` (the machine phase);
- `observed_context.evaluation_sequence`;
- optional active composition identity/version;
- direction anchor, pivot candidate, support/shop/carry/feasibility diagnostics;
- optional transition emitted only after pivot confirmation and state change;
- a reason string and `shadow_only=true`.

It deduplicates unchanged evidence, and its emission sequence is not a decision sequence (`StrategicDirectionPivotAuditRecorder.hpp:33-73,125-163,273-317`). The `evaluation_sequence` is supplied from the Composition Intelligence runtime's next player sequence in the TftEngine callsite, so it is a diagnostic evaluation correlation token, not a native decision sequence (`TftEngine.cpp:3872-3887,4115-4120`).

The sidecar does not serialize a generic `owner_id` or owner `status`. `phase` is the machine state. A pivot candidate is the pending destination evidence; the recorder's `transition` field is emitted only after confirmation, so it is not a `pending_transition` object. `reason` is the transition reason, separate from phase/status. Runtime reset clears the machine and recorder session state; Engine reset recreates the runtime and resets strategic context sequences (`UnifiedStrategicShadowRuntime.hpp:20-55`; `TftEngine.cpp:6184-6195`).

## 3. Field-level dispositions

| Schema path | Actual source/evidence | Closest diagnostic surface | Disposition |
|---|---|---|---|
| `strategic_evidence.owner_snapshots.planner_commitment.status` | No status member on StrategicCommitment | Decision path/reason mirror only | `no_explicit_commitment_status` |
| `strategic_evidence.owner_snapshots.planner_commitment.owner_id` | Per-player commitment array index | Player index context | `player_scoped_without_owner_id` |
| `strategic_evidence.owner_snapshots.planner_commitment.payload_path` | No payload path member | None | `not_produced` |
| `strategic_evidence.owner_snapshots.planner_commitment.source_decision_sequence` | Parent evidence context has sequence; commitment does not retain it | None | `parent_sequence_not_bound_to_commitment` |
| `strategic_evidence.owner_snapshots.planner_commitment.reason` | Selection/revision reason and decision path exist separately | PlayerInfo reason/path diagnostics | `separate_reason_fields_not_owner_envelope` |
| `strategic_evidence.owner_snapshots.composition_intelligence.status` | Runtime stages have status; recorder has stale flag | Stage trace and diagnostic stale status | `diagnostic_status_only` |
| `strategic_evidence.owner_snapshots.composition_intelligence.owner_id` | One runtime per player; no owner ID field | Match/player metadata | `per_player_runtime_without_owner_id` |
| `strategic_evidence.owner_snapshots.composition_intelligence.source_decision_sequence` | Recorder/runtime emission sequence | Diagnostic sequence/player_sequence | `emission_sequence_not_decision_sequence` |
| `strategic_evidence.owner_snapshots.composition_intelligence.active_composition` | ActiveCompositionManager state | Source metadata and composition diagnostics | `active_composition_diagnostic_partial` |
| `strategic_evidence.owner_snapshots.composition_intelligence.composition_identity` | Active composition ID | Top-level composition_id | `diagnostic_composition_identity` |
| `strategic_evidence.owner_snapshots.composition_intelligence.composition_version` | Active composition version | Top-level composition_version | `diagnostic_composition_version` |
| `strategic_evidence.owner_snapshots.composition_intelligence.transition_state` | Transition proposal and optional published transition | transition_plan/published_transition payloads | `split_transition_diagnostics` |
| `strategic_evidence.owner_snapshots.composition_intelligence.reason` | Stage, proposal and stale reasons | Stage trace and stale_reason | `multiple_reasons_no_owner_reason` |
| `strategic_evidence.owner_snapshots.unified_state_machine.status` | Machine phase and pivot feasibility status | Sidecar phase/feasibility | `phase_not_owner_status` |
| `strategic_evidence.owner_snapshots.unified_state_machine.owner_id` | Player-scoped runtime; no owner ID field | Match/player context | `no_serialized_machine_owner_id` |
| `strategic_evidence.owner_snapshots.unified_state_machine.source_decision_sequence` | Evaluation sequence and emission sequence only | observed_context.evaluation_sequence and sequence | `diagnostic_sequences_not_decision_sequence` |
| `strategic_evidence.owner_snapshots.unified_state_machine.machine_state` | StrategicCycleResult.phase | Sidecar phase string | `machine_phase_available` |
| `strategic_evidence.owner_snapshots.unified_state_machine.active_composition` | Optional active composition in cycle result | Sidecar active_composition identity/version | `active_identity_version_diagnostic` |
| `strategic_evidence.owner_snapshots.unified_state_machine.pending_transition` | Pivot candidate while pending; transition only after confirmation | pivot_candidate and optional transition | `pivot_candidate_not_pending_transition` |
| `strategic_evidence.owner_snapshots.unified_state_machine.reason` | StrategicCycleDiagnostics.transition_reason | Sidecar reason string | `transition_reason_diagnostic` |

## 4. Non-equivalences and invariants

1. A per-player array index is not a serialized owner ID.
2. A diagnostic emission sequence is not a source decision sequence.
3. Parent StrategicEvidenceContext sequence is not automatically retained by a mutable commitment.
4. Composition stale status, stage status, machine phase and transition reason are different fields.
5. A pivot candidate is not a published transition; a confirmed transition is not a pending transition.
6. Composition identity/version in a diagnostic snapshot is not a complete canonical owner snapshot.
7. None of these owner diagnostic paths is a PPO observation or Actor/Critic input.

## 5. Remaining proof

- Define whether Schema v2 should model three independent owner records or one aggregate owner snapshot; do not synthesize fields from different sidecars without explicit correlation.
- Define owner identity semantics (stable class/instance identity vs player-scoped owner role).
- Define a true source decision sequence for each owner, distinct from recorder emission/player sequence and evaluation sequence.
- If the schema requires `payload_path`, specify a stable serialization contract; current in-memory commitment has none.
- Preserve the distinct lifecycle/status/reason vocabularies of StrategicPlanner, Composition Intelligence and UnifiedStrategicStateMachine.
- Trace diagnostic pybind endpoints through the Python wrapper and confirm their exclusion from Trainer/rollout/policy inputs.

Issue #346 remains open. This is documentation only; no runtime, schema, tensor, PPO, reward, mask, training, checkpoint or Viewer changes.

## 6. Architecture reconstruction review

1. **Prior problem:** Schema v2 presented three independent state owners as if they emitted one uniform owner snapshot with common status, identity, path and decision sequence.
2. **Technical justification:** the owners have different state lifecycles and diagnostic protocols; combining emission sequence, phase, stale flag or parent context sequence would fabricate correlation.
3. **New responsibility:** this audit owns field-level proof of the current owner state and diagnostic surfaces without defining a new runtime envelope.
4. **Contract and invariants:** preserve three owners; no synthetic owner ID/payload path/decision sequence; phase is not status; pending candidate is not transition; diagnostic output is not PPO input.
5. **Cross-component impacts:** StrategicPlanner commitment, CompositionIntelligencePlayerRuntime/ActiveCompositionManager/TransitionManager/CompositionDiagnosticRecorder, UnifiedStrategicStateMachine/Recorder, TftEngine reset, pybind, Python wrapper, schema and replay.
6. **Objective validation:** all 20 owner-snapshot paths are enumerated and compared against owner declarations, runtime serialization and Engine callsites; no runtime or schema changes.

