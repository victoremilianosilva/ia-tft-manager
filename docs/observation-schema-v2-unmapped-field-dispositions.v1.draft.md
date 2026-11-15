# Schema v2 Unmapped Field Dispositions v1 — Draft

**Status:** source-backed disposition proposal for 16 paths absent from the 77-entry source map; not runtime-approved.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Crosswalk:** [Schema v2 Field-to-Source Crosswalk](observation-schema-v2-field-source-crosswalk.v1.draft.md).

## 1. Purpose

The crosswalk identified 16 Schema v2 data paths under `derived_context`, `strategic_evidence` and `legal_state_context` with no matching entry in the current source map. "Unmapped" is not itself a producer status. This document classifies each path against the current producer/ownership evidence and identifies the contract correction required.

## 2. Disposition of all 16 paths

| Schema path | Source-backed owner/evidence | Disposition | Why it is not a normal observed PPO field |
|---|---|---|---|
| `derived_context.action_opportunity.status` | `StrategicSharedContext::action_candidates` is empty in the audited TftEngine construction path; both evaluators receive the empty set | `not_produced` | No authoritative candidate-set producer exists in the audited path; collection status cannot claim availability |
| `derived_context.action_opportunity.source_sequence` | Candidate contract requires typed source sequences, but no candidate rows/set are populated | `not_produced` | No source candidate set exists to bind to a sequence |
| `derived_context.action_opportunity.reason` | No producer-owned parent status/reason envelope is emitted | `not_produced` | A reason must explain a real producer status, not be inferred from an empty vector or default |
| `derived_context.decision_history.status` | PPO receives flat action-memory count and board-slot ages; no typed decision-history collection | `not_produced` | Flat scalars do not establish collection completeness/status |
| `derived_context.decision_history.source_decision_sequence` | No per-event decision identity is carried by the flat memory block | `not_produced` | Round, board slot age and observation call order are not decision-sequence identity |
| `derived_context.decision_history.reason` | No structured history producer/status envelope | `not_produced` | No authoritative reason for unavailable/partial history is emitted |
| `strategic_evidence.composition_hypotheses[].hypothesis_id` | NativeStrategicCompositionGenerator and InitialStrategicDirectionDiscovery create Shadow candidates/hypotheses; no stable hypothesis ID/revision contract is emitted | `shadow_only` for hypotheses; `not_produced` for stable ID | A generated candidate or direction identity is not a stable hypothesis identity |
| `strategic_evidence.composition_hypotheses[].direction_id` | Direction discovery and direction anchors have their own identities in the isolated Shadow state/sidecar | `shadow_only` | This is diagnostic hypothesis context, not canonical PPO commitment delivery; mapping to this schema field is not approved |
| `strategic_evidence.composition_hypotheses[].composition_id` | Composition candidates and active composition identities exist in separate owner lifecycles | `shadow_only` | Candidate composition is not accepted active composition; owner/transition state must remain explicit |
| `strategic_evidence.composition_hypotheses[].anchor_id` | StrategicAnchorCandidate and direction-anchor identities exist in Shadow, but no single stable hypothesis-anchor reference contract exists | `shadow_only` | Candidate anchor identity cannot be silently equated with physical UnitInstance identity or active anchor |
| `strategic_evidence.composition_hypotheses[].evidence[]` | Candidate/sidecar paths carry evidence strings, unit support and shop evidence | `diagnostic_only` | Strings and sidecar evidence do not provide the typed provenance, source namespace, completeness or consumer contract required by v2 |
| `strategic_evidence.composition_hypotheses[].quality` | Candidate scoring/confidence is heuristic and varies by producer; no shared hypothesis quality contract is established | `unverified` | Do not treat heuristic score/confidence as calibrated probability or generic quality |
| `legal_state_context.status` | Native ActionMaskBatch/ActionMasks carry mask availability/diagnostics, but not a unified v2 legal-state envelope bound to decision identity/hash | `not_correlated` | Native legality exists; v2 envelope status is not proven to be emitted/correlated |
| `legal_state_context.source_decision_sequence` | ActionMask structures do not carry the proposed v2 decision identity/sequence envelope | `not_produced` | No accepted legal-state decision sequence can be copied from the current mask payload |
| `legal_state_context.reason` | DecisionResult and mask diagnostics contain local errors/reasons, but no unified legal-state reason producer | `not_correlated` | Local validation reason is not a complete parent legal-state status reason |
| `legal_state_context.description` | Static schema description/contract text, not an Engine observation value | `contract_metadata` | Keep as schema documentation; do not serialize as dynamic state or treat as a missing runtime producer |

## 3. Key owner distinctions

### 3.1 Composition hypotheses are diagnostic proposals

The strategic ownership contract distinguishes generated hypotheses, canonical StrategicPlanner commitment, active composition, pivot candidate and recommendations. NativeStrategicCompositionGenerator supplies hypotheses; only the canonical owners commit direction/composition state. The Unified direction/pivot sidecar is a diagnostic observer and does not publish its private state to PPO.

Therefore the schema's `composition_hypotheses` path must not be populated by copying active composition or pivot state into a generic hypothesis array. If a future canonical evidence projection needs hypothesis context, it must define:
- stable hypothesis identity and revision;
- producer namespace and source sequence;
- explicit relationship to direction and composition identities;
- evidence items with typed provenance and completeness;
- quality semantics that distinguish heuristic score from calibrated probability;
- status and lifecycle separate from accepted commitment/active composition.

### 3.2 Action opportunity and decision history remain unavailable

The action opportunity parent collection is empty in the audited source path. The schema must preserve `not_produced` separately from a valid empty candidate set and from no eligible candidates. Evaluator staleness/equality flags do not prove candidate comparison.

The temporal decision history schema must not infer event IDs or decision sequences from the existing flat action-memory scalars. Those values are delivered to PPO, but they are not a typed ordered history.

### 3.3 Legal-state envelope is not the action-mask payload

Native masks are the final legality authority. The current mask structures do not transport the full v2 decision identity, mask contract hashes and snapshot hash. Local mask diagnostics are not equivalent to a correlated parent legal-state envelope. This path remains a correlation gap, not an excuse to reconstruct masks or sequence identity from anti-loop history.

## 4. Crosswalk update requirements

The CSV crosswalk remains a mechanical match report: 16 rows have no source-map entry. This document adds a producer disposition, but does not rewrite the original source-map match classification.

Before closing the unmapped-path work:
1. Add each disposition to a versioned source-map/crosswalk revision with exact evidence references.
2. Verify composition-hypothesis field producers and their identity/revision lifecycle.
3. Verify parent status/reason semantics for action opportunity and decision history.
4. Keep legal-state status/reason separate from mask-local diagnostics and require explicit identity correlation.
5. Keep schema description text as static metadata, not runtime observation.

## 5. Architecture reconstruction review

1. **Prior problem:** the 16 unmapped paths were known only as absent from the source map; absence did not distinguish no producer, Shadow-only evidence, diagnostic strings, uncorrelated mask metadata or static schema text.
2. **Technical justification:** these categories have different owners and delivery guarantees; treating all as available or all as absent would lose important semantics.
3. **New responsibility:** this document owns the source-backed disposition proposal for the 16 unmapped paths; the crosswalk continues to own mechanical path matching.
4. **Contract/invariants:** no synthetic hypothesis IDs or decision sequences; Shadow hypotheses are not active commitments; diagnostic strings are not typed provenance; masks remain independent legality inputs.
5. **Cross-component impacts:** NativeStrategicCompositionGenerator, InitialStrategicDirectionDiscovery, StrategicPlanner, ActiveCompositionManager/TransitionManager, UnifiedStrategicShadowRuntime, action evaluators, ActionMaskEngine, DecisionResult, Python binding, PPO projection and replay.
6. **Objective validation:** all 16 no-match paths from the 223-path crosswalk appear exactly once in the table; every path has an explicit disposition and owner/evidence statement. Documentation-only; no runtime or tensor-layout changes.

Issue #346 remains open.
