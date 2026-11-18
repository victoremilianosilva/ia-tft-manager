# Stage 1 Architecture Dependency and Redundancy Disposition Map v1

**Status:** source-backed audit baseline; implementation decisions are separated from unresolved hypotheses.  
**Base:** `new-arquiteture` plus the consolidation work in PR #485.  
**Scope:** native strategic state, PPO-facing legacy projections, Viewer/replay diagnostics, identity envelopes, sequences, revisions, and temporal histories.

## 1. Decision rule

Every structure receives one disposition:

- **Keep:** it has a distinct owner, consumer, or semantic meaning that cannot be represented safely by an existing canonical structure.
- **Incorporate:** its information belongs in an already-owned canonical structure and does not need a parallel representation.
- **Simplify:** retain the responsibility but remove proven duplicate fields, wrappers, or lifecycle.
- **Eliminate:** no required consumer or replay purpose exists, and removal preserves behavior and provenance.

A matching value is not enough to prove duplication. Sequence domains, identity scope, event ordering, and persistence lifetime must be compared before removal.

## 2. Source-backed dispositions

| Structure / information | Actual producer and consumer evidence | Disposition | Decision and invariant |
|---|---|---|---|
| Engine instance + episode identity | Native Engine creates the identity; reset/step results, wrapper, Trainer and rollout validate it. | **Keep** | Canonical identity for one Engine instance and episode. Never substitute Viewer session identity. |
| Lobby decision sequence | Native Engine increments it once per published decision result. | **Keep** | Lobby-wide ordering is distinct from each player's decision sequence. |
| Player decision sequence | Native per-player counters are published atomically in reset/step and validated by wrapper/Trainer/RolloutBuffer. | **Keep** | Player-local ordering must remain monotonic and correlated with the same result row. |
| AuditSnapshot envelope | Native factual snapshot groups board/bench/shop and correlated state for consumers. | **Keep** | One atomic factual snapshot remains the source of truth; do not split it into independently sampled facts. |
| Nested child event identity envelopes | #484 consolidated inherited Engine/episode/snapshot/player identity into the parent envelope; child records retain event-specific ordering. | **Incorporate** | Child events inherit parent identity. Keep only event-local sequence/type/payload where independently meaningful. |
| Combat event sequence | Combat event ordering is local to a combat stream, not interchangeable with lobby/player decision ordering. | **Keep** | Preserve event order and its source-specific scope. |
| Economy/PvP event identity | #481/#482 publish event records correlated to player/round and exact balance transitions. | **Keep** | Do not collapse PvP win credit into round income; their timing and accounting semantics differ. |
| Candidate set identity | Native candidate generation binds a set to producer, player, round and source decision sequence. | **Keep** | Required to correlate alternatives and reject stale candidates. |
| `candidate_revision` | #474 assigned it from the same `source_sequence` for the same candidate set. No distinct same-decision revision producer was found. | **Eliminate** | Removed in #483. Keep `source_sequence` and `candidate_set_id`; do not restore a mirror counter without a real revision lifecycle. |
| AntiLoop operational position/move/block/state-visit history | AntiLoop uses these stores to prevent reversals, repeated moves and cycles; metrics are consumed by Trainer diagnostics. | **Keep** | These are operational decision state, not a replaceable event log. Preserve retention/reset behavior and mask legality. |
| Additional typed AntiLoop event tail | #475 added a bounded 64-event copy; no Trainer, rollout, Viewer or Python adapter callsite consumed its JSONL binding. It omitted most player actions and was not a complete replay. | **Eliminate** | PR #485 removes only this unused parallel diagnostic stream. Operational AntiLoop history and metrics remain. |
| `StrategyInfo` strategic fields | `update_strategy()` writes direction, focus, core/planned units/traits, lock/strength and strategy ID; PPO observation/reward and Viewer still consume some of them. | **Keep temporarily as compatibility** | It is not canonical for the new architecture. Do not delete until every legacy consumer has a tested projection from canonical owners. |
| `CompositionDirectionPolicy` | Legacy direction state is hydrated from and written back to `StrategyInfo` inside `update_strategy()`; it still affects the current legacy observation/reward path. | **Keep temporarily as compatibility** | Must not become an input/fallback for new strategic owners. Retire only after consumers are migrated. |
| Legacy `CompositionPlanner` | `update_strategy()` calls `CompositionPlanner::build` to populate `planned_*`; the old fields feed PPO and Viewer. Separate native candidate generation exists, but does not yet replace every legacy consumer. | **Keep temporarily as compatibility** | Do not remove before PPO and Viewer projections are migrated. New strategic decisions must not use its output as authority. |
| `NativeStrategicCompositionGenerator` | Generates candidate lineups from catalog and observed owned/shop/pool facts without `StrategyInfo` or `CompositionPlanner`. | **Keep** | Native proposal producer; candidate output remains a proposal, not active state or PPO command. |
| `StrategicEvidenceContextBuilder` / `StrategicEvidenceContext` | Builds identity-bound evidence from observed facts and the new strategic commitment; StrategicPlanner consumes its validated context. | **Keep** | Canonical boundary for new strategic evidence. Missing/stale/incompatible inputs must remain explicit. |
| `StrategicPlanner` commitment | Per-player commitment is stored separately from legacy `StrategyInfo`; decision is Shadow-only in the audited flow. | **Keep** | Owns strategic direction/commitment decisions; never hydrate from legacy fallback as authority. |
| `ActiveCompositionManager` | Per-player Composition Intelligence runtime publishes versioned active composition and transitions. | **Keep** | Owns active composition snapshots. A candidate or pivot proposal cannot mutate it without the owner’s publish step. |
| `TransitionManager` | Per-player runtime tracks transition/hysteresis for composition changes. | **Keep** | Retain only if it continues to own transition policy; do not duplicate active composition state. |
| `StrategicContextBridge` | Projects validated strategic/economic/active-composition values into diagnostic JSON with origin and quality metadata. | **Keep, consumer-scoped** | It is a read-only bridge, not a second owner. Keep provenance distinctions (observed/derived/recommended). |
| Composition diagnostic snapshot and runtime envelope | Runtime owns player/match/round/sequence; bridge no longer owns a second identity envelope after #484. | **Simplify** | Keep one snapshot envelope and stage-specific sequence. Avoid reintroducing nested correlation metadata. |
| Stage sequence vs player sequence | Stage sequence orders steps within one runtime evaluation; player sequence orders published player snapshots. | **Keep both** | They represent different ordering domains, not duplicate counters. |
| Item profile preferred traits | Current `item_unit_profiles()` derives preferred traits from legacy core/planned traits, direction, focus and active traits. | **Migrate** | Use observed catalog traits and canonical active-composition/evidence only when a validated owner supplies them; preserve explicit absence instead of a legacy fallback. |
| PPO strategic observation features | `build_observations()` reads `StrategyInfo` for strategy one-hot, direction, core traits, composition fit, planned carry, focus, lock and strength. | **Migrate under approved projection contract** | This is an active legacy dependency, not diagnostic-only. Replace only with a versioned projection and aligned Actor/Critic/action-head tests. |
| PPO reward strategy branches | `PlayerEnv::step` reward/action shaping reads legacy strategy identity for selected branches. | **Migrate under reward contract** | Replace with outcome/evidence-based reward semantics; preserve PPO/GAE and avoid turning strategic recommendations into labels. |
| Viewer strategy fields | Viewer cards/dialog/logs still read legacy strategy snapshots; Composition Intelligence diagnostics are a separate surface. | **Compatibility projection** | Project from canonical owners; mark unavailable/inferred values honestly. Preserve historical log readability. |
| DTOs that only forward fields | A structure is redundant only if callsites prove no validation, normalization, ownership, or lifecycle responsibility. | **Audit individually** | No blanket deletion. Remove only after producer→transform→consumer tracing and tests. |

## 3. Proven findings versus unresolved hypotheses

### Proven

1. `candidate_revision` duplicated `source_sequence` in the same candidate-set lifecycle; #483 removed it.
2. Nested child envelopes duplicated parent snapshot identity; #484 consolidated them while retaining event-local ordering.
3. The typed AntiLoop event tail had no active application consumer and was not a complete replay; #485 removes it while preserving operational AntiLoop state.
4. PPO observations are still built from legacy `StrategyInfo` fields in `TftEngine.cpp::build_observations()`.
5. `update_strategy()` still invokes legacy `CompositionPlanner::build` to populate `planned_*`.
6. `item_unit_profiles()` still derives item affinity from legacy core/planned traits, direction and focus.
7. Viewer factual snapshots and legacy strategy snapshots are separate inputs; the current UI/log path still uses legacy strategy fields.
8. The new native candidate generator and StrategicEvidenceContext path exist independently, but their existence does not prove all consumers have migrated.

### Unresolved — do not remove without further evidence

1. Whether `producer` and `source_namespace` are semantically identical at every event producer and consumer.
2. Whether every event-local `contract_id`/`contract_version` is redundant with the containing snapshot schema. Independently persisted/transported events may need their own contract version.
3. Whether any intermediate DTO performs validation/normalization not obvious from its name.
4. Whether `derived_core_unit_ids` and per-unit `is_core` are redundant across all consumers; they may represent different aggregate/entity projections.
5. Whether all diagnostic snapshot stages have a concrete downstream consumer or are retained only for exploratory telemetry.
6. Whether additional local histories have replay consumers not covered by the current static callsite audit.

## 4. Migration boundaries and order

1. Keep the factual Engine, decision identity, action masks and final legality authoritative.
2. Make new strategic owners independent of `StrategyInfo`, `CompositionDirectionPolicy` and legacy `CompositionPlanner`.
3. Build explicit compatibility projections for old Viewer consumers; never read those projections back into new decision owners.
4. Migrate PPO observation semantics only with the approved versioned projection contract and exact Actor/Critic/action-head alignment tests.
5. Migrate reward semantics separately from policy recommendations; preserve outcome credit and invalid-transition handling.
6. Retire legacy producers only after all remaining consumers have moved and absence-of-legacy tests pass.
7. Validate multi-round replay with identity, sequence, provenance, masks and no synthetic fallback before Stage 1 acceptance.

## 5. Six-point architecture review

1. **Prior problem:** strategic truth, legacy compatibility, diagnostics and replay data were spread across overlapping structures with unclear authority.
2. **Technical rationale:** source tracing shows some structures are true duplicates (#483/#484/#475), while other similarly named values have distinct identity, ordering, ownership or consumer semantics.
3. **New responsibility:** native strategic owners produce canonical commitments/compositions; Engine remains factual/legality owner; compatibility projections serve old consumers.
4. **Contracts/invariants:** one owner per canonical value; preserve identity domains, event order, provenance, missingness, immutable snapshots and action-mask legality.
5. **Cross-component impact:** native Engine, strategic runtime, PPO projection/reward, Viewer, replay, wrapper and diagnostics. No UI, reward or tensor behavior is changed by this map.
6. **Objective validation:** each disposition is linked to source/consumer evidence; proven removals have regression tests; unresolved items remain explicitly open rather than being removed by assumption.

## 6. Acceptance status

This map is an audit artifact, not proof of completed migration. Stage 1 remains **not globally accepted** until:

- the remaining event/DTO ownership audit is closed;
- new strategic owners no longer read legacy strategic producers;
- PPO observation/reward compatibility boundaries are explicitly migrated under their contracts;
- Viewer compatibility is sourced from canonical owners;
- multi-round replay proves identity/provenance continuity with legacy strategic producers unavailable;
- Actor and Critic receive the exact decision-correlated masks as independent inputs.
