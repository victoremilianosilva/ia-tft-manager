# Strategic Owner Observation Contract v2 — Draft

**Status:** Runtime contract for Viewer/replay correlation.  
**Tracking:** #292 and #289.

## 1. Prior problem

The Viewer had access to the native player decision sequence and to strategic diagnostic records, but the latter's action-resolution identity used a separate per-player strategic context sequence. The two counters have different lifecycle semantics: the native player decision sequence advances during reset as well as steps, while the strategic context sequence advances when the strategic evidence/action pipeline evaluates a player. Deriving one from the other would create false stale matches.

## 2. Technical rationale

A diagnostic can only be shown as current when its exact source sequence is correlated with the same native player snapshot. The global JSONL emission sequence, the PPO/player decision sequence, and the strategic context sequence are separate namespaces and must never be substituted for one another.

## 3. New responsibility and owner

- `AuditStrategicOwnerSnapshot` owns the current `strategic_context_sequence` alongside the existing episode, player decision sequence, round and active-composition identity.
- `TFTEngine::get_audit_snapshot` copies the sequence from the same per-player counter consumed by strategic evidence and action resolution.
- Pybind exports the field unchanged.
- ViewerSession compares the diagnostic action-resolution `identity.source_sequence` against this native owner field before exposing the diagnostic as current.

## 4. Contract and invariants

- Nested owner contract: `tft.strategic-owner-observation`, version 2.
- `strategic_context_sequence` equals the sequence placed in `StrategicEvidenceContextInput` and `StrategicActionNativeSnapshot` for the current strategic evaluation.
- `player_decision_sequence` remains the separate native observation/decision sequence; it is not an alias and no fixed offset is inferred.
- Diagnostic JSONL `sequence` remains an emission-order counter, not a source decision sequence.
- Episode, round, strategic source sequence and active composition ID/version must match before a Viewer plan is treated as current.
- A mismatch marks the diagnostic stale; stale lineup entries are never offered as current recommendations.
- Reset clears the strategic context sequence with the owning Engine episode.

## 5. Cross-component impact

`TftEngine.hpp`, `TftEngine.cpp`, pybind snapshot serialization, ViewerSession correlation, native replay integration tests and Viewer tests. No PPO tensor, policy, reward, action-mask or execution semantics change.

## 6. Objective validation

- Snapshot-binding fixture asserts the owner contract version and distinct sequence field.
- Native multi-round replay asserts that the owner sequence equals the action-resolution source sequence.
- Viewer tests accept exact sequence matches and reject same-round stale sequences, prior rounds and composition-version mismatches.
- The integrated replay remains deterministic and emits a Viewer-loadable JSONL artifact.
