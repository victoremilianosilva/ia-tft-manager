# Observation Schema v2 — Identity and Evidence Boundary

**Status:** Stage 1 specification and executable contract validation; not runtime approval.
**Scope:** Observation Schema v2, Decision Identity v2, sequence namespace semantics, field provenance, fixed-slot cardinality and missingness invariants.
**Related:** #293, #294, #288, #346; PR #428 native snapshot sequence; PR #450 Action/Mask Contract v1.

## 1. Prior problem

The v1 semantic schema did not distinguish producer-local sequence domains. Decision Identity v2 proposed typed namespace/value references, but the registry described the native Engine counter as per-player even though PR #428 implements one monotonically increasing sequence per Engine instance and published ResetResult/StepResult. A single native result carries all eight player rows and their exact masks. The v2 schema also lacked an executable validator and v2 fixtures, and several presence/cardinality conditions were described but not enforced.

## 2. Technical rationale

Equal integer counters do not prove equal decision identity when they come from different producers or scopes. A global Engine snapshot ordinal cannot be promoted to a per-player decision counter. Missing identity must remain partial; a partial identity cannot authorize mask, Critic, temporal-history, or strategic-owner context. Stable board/bench/shop slot order and physical UnitInstance identity must be validated independently from array length. Derived/estimated/inferred/recommended fields require formula identity, and variable-cardinality projection blocks require explicit padding, presence and length semantics.

## 3. New responsibility and ownership

- Observation Schema v2 owns semantic field types, provenance, status/missingness, catalog fingerprints and schema evolution.
- Decision Identity v2 owns cross-source identity composition and namespaced sequence references.
- Sequence Namespace Registry owns producer, scope, monotonicity, reset boundary, availability and canonical-decision eligibility.
- Native Engine owns the actual Engine-instance snapshot publication sequence; its existing field name `decision_sequence` is not the semantic namespace or player-level meaning.
- Action/Mask Contract owns action/mask identity and legality; Observation Schema references those contracts without redefining them.
- PPO/rollout/checkpoint consumers must reject stale or incompatible contracts. This PR adds contract validation only; it does not wire a new runtime producer or change the PPO projection.

## 4. Contract and invariants

1. Native `TFTEngine::Impl::decision_sequence` maps to `snapshot_sequence` in namespace `tft.engine.observation-snapshot`; it increments once per ResetResult/StepResult, is shared by all eight player rows and continues across episode resets within one Engine instance.
2. `tft.engine.decision` is now populated from native `player_decision_sequences[player_id]` and emitted by the adapter in PR #504. It is distinct from the Engine-wide snapshot counter and remains monotonic across episode resets within one Engine instance.
3. Until authoritative logical `match_id` and per-player decision sequence are available, identity remains `partial`, decision identity hash is null, and mask/Critic/anti-loop/strategic-owner contexts cannot be marked valid.
4. Decision identity hash uses RFC 8785 canonical JSON and SHA-256 over the exact v2 scope; producer namespace is part of each sequence reference.
5. Derived, estimated, inferred and recommended field provenance requires formula ID and formula version; provenance nature must equal field nature.
6. Board, bench and shop preserve 28, 9 and 5 stable ordered slots respectively. Occupied slots carry a unit; non-occupied slots carry explicit null. Physical unit instance IDs cannot be duplicated across board and bench.
7. Variable-cardinality projection blocks declare padding policy, presence-mask path and length path. Zero is not a missing sentinel.
8. Action/mask definitions remain independent; the Engine remains final legality authority. Recommendations remain diagnostic and are not PPO actions.

## 5. Cross-component impacts

The contract affects schema/registry fixtures, schema validation CI, native identity interpretation, wrapper metadata mapping, PPO rollout correlation, checkpoint compatibility and later replay. It does not change C++/Python runtime behavior, action dimensions, masks, rewards, neural projection, training, or Viewer behavior. Real match identity and the per-player decision counter remain producer gaps; Stage 7 GEP evidence is still required for real capture provenance.

## 6. Objective validation criteria

- Draft 2020-12 schema validates itself and accepts the v2 minimal fixture.
- RFC 8785 hash vectors reproduce exact canonical bytes and SHA-256 values.
- Negative fixtures reject partial identity paired with valid masks, Engine snapshot ordinal misused as per-player decision sequence, and non-canonical slot order.
- Provenance nature/formula identity, field missingness, slot cardinality/order and physical unit uniqueness are checked.
- CI continues running the v1 validator and adds the v2 validator.
- No runtime acceptance or Stage 1 completion is claimed until producer delivery, wrapper/rollout binding, checkpoint lineage and integrated replay are proven.

## PR #504 adapter delivery

The adapter now composes `engine_match_id` from native `engine_instance_id` and `episode_id`, emits one canonical Decision Identity v2 envelope per player, maps the native per-player counter to `tft.engine.decision`, and maps the Engine-wide counter to `tft.engine.observation-snapshot`. Trainer and Rollout validate the envelope against the native snapshot before it is stored. `match_id` remains null until an authoritative logical game-match producer is available; it is not substituted with Viewer session identity.