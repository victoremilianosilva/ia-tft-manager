# Phase C — Integrated audit for #574–#578

## Scope and implementation boundary

This audit treats #574, #575, #576, #577 and #578 as one coordinated Decision Context migration on the existing #583 branch. The implementation preserves the current PPO policy input and behavior. Native context is metadata/audit input; it is not an implicit planner execution path.

The Engine remains authoritative for game state, action legality, action execution, and factual outcomes. The migration adds read-only projections and event transport without changing simulation rules, lifecycle, ordering, RNG, determinism, rewards, masks, action sampling, PPO updates, or checkpoint compatibility.

## Producer → contract → consumer matrix

| Domain | Authoritative producer | Versioned transport | Adapter / consumer | Boundary |
|---|---|---|---|---|
| Entity identity (#573) | Native board, bench and shop snapshots | `AuditUnitSnapshot`, stable UUID and champion internal ID | Native snapshot binding; semantic v8 projection; Decision Context player view | UUID identifies the physical entity. Champion ID is not a substitute for physical identity. |
| Strategic context (#574) | `ActiveCompositionManager`, `UnitPriorityPlanner`, `LineupPlanner`, direction/pivot anchors, `UnitCopyProgress`, opportunity-cost owner | `AuditStrategicOwnerSnapshot` v4 | Binding → Python structured strategic projection → `decision_context["strategic"]` | Planner output is advisory metadata, never an action. Missing evidence stays unavailable. |
| Positioning (#575) | Existing board slots, `PositioningEngine` geometry and native unit role facts | `AuditBoardRelationSnapshot` v1 rows on `AuditPlayerSnapshot` | Binding → `decision_context["positioning"]` | Relation rows reference stable board slots; UUID remains owned by the unit row. No second tactical evaluator or invented bench coordinates. |
| Action execution (#576) | `TFTEngine::step`, action handler and native transition/item owners | `ActionExecutionTrace` / `tft.action-execution-event` v1 | Wrapper → `build_action_outcome_events` parity oracle → matching outcome row in Decision Context | Requested, effective and applied action remain distinct. Native unit/economy/shop/item facts are checked against paired snapshots where observable. |
| Temporal context (#577) | Engine/episode/player decision sequences, round/stage, combat/economy/PvP producers | `AuditActionDecisionReference`, `tft.player-action-history` v1, bounded 32-entry ring | Binding → Trainer identity/sequence validation → `decision_context["temporal"]` | History is player/episode scoped and reset with the episode. Combat correlation is same-player/round context, not exclusive causality from one action. |
| Decision Context (#578) | Shared native lobby snapshot plus per-player native snapshot rows | `tft.decision-context.lobby` and `tft.decision-context.player` v1 | Trainer metadata, rollout/audit consumers | One lobby envelope is shared across its player rows; player views retain their own identity and sequence. PPO tensor input remains unchanged. |

## Implementation status

- **#574 — Strategic context:** the native v4 contract transports composition identity/version, direction and pivot anchors, priorities, pair/upgrade evidence, lineup membership and opportunity-cost provenance. Python validates and exposes the structured context separately from semantic v8.
- **#575 — Positioning:** compact relation rows expose occupied slot, 4x7 row/column, role, adjacent occupied slots, frontline slots in front, and tank/fighter counts. The implementation reuses native geometry and raw role facts. It does not alter BoardEvaluation, movement legality, or placement behavior.
- **#576 — Action Context:** native trace v1 binds requested/effective action, handler result, source/outcome snapshot and player sequences, round/stage, economic transition facts, shop revisions, item-action metadata, and unit add/remove/move/upgrade deltas. Unit identity capture is limited to action families that can change identity/location/star. The Python snapshot-diff producer remains a parity oracle and rejects native unit-delta mismatches. Round refresh and PvP credit overlap are kept distinct from direct action attribution.
- **#577 — Temporal context:** each player carries a fixed ring of up to 32 action decision references. It preserves source/outcome identities and round/stage, is reset per episode, and is validated before entering Decision Context. Delayed combat facts are joined by engine/episode/player/round/combat sequence without claiming single-action causality.
- **#578 — Decision Context:** Trainer creates one lobby envelope shared by the player rows and separate player views referencing their frozen native player subtree. Strategic, positioning, action and temporal blocks remain metadata; semantic v8 remains the compatibility policy input.

## Validation evidence

- Native strategic owner v4 contract, producer parity, sequence isolation and legacy-removal checks.
- Positioning projection tests cover partial and full 4x7 boards, empty boards, bench-only entities, stable slot references, geometry and adjacency bounds.
- Temporal history test advances 34 decisions, verifies the 32-entry ring retains the latest ordered references, checks per-player sequence alignment, and verifies reset clears the ring.
- Native movement integration verifies both sides of a board swap are emitted as UUID-bound move deltas; the Python snapshot-diff producer checks native facts against the paired snapshots.
- Action-outcome producer tests cover purchase, reroll, XP purchase, sale, positioning, item assignment/removal, round-income overlap, shop refresh overlap, PvP credit overlap, and unavailable causal attribution.
- PPO integration and deterministic replay tests preserve semantic v8 values, champion IDs/hash, masks, rewards, dones, rollout identity and checkpoint lineage.
- CI for code head `6059d14` passed all three required workflows: C++ native engine (including native integration, PPO training smoke, multi-seed battery and deterministic replay), strategic/economic native tests, and combat ownership sanitizers. The following commit updates documentation only; it does not change tested code.

## Invariants

- PPO remains the decision and learning algorithm; no autonomous Shadow execution.
- No changes to actions, masks, rewards, logits, sampling, GAE, rollout semantics or checkpoints.
- Preserve semantic v8 numeric values, champion IDs, hash and dimensions.
- No changes to simulation rules, lifecycle, order, RNG or deterministic Engine behavior.
- Preserve Audit Context and replay; new context is typed metadata, not a forced action.
- Missing information remains distinct from zero/neutral.
- Do not invent tactical exposure or causal attribution when the native producer cannot establish it.

## Performance work included (not yet benchmarked)

The integrated implementation also includes low-risk hot-path changes intended to reduce transient objects and Python/native boundary work:

- Batch semantic projection accumulates final columns directly instead of retaining every complete per-player projection dictionary.
- Copy-progress projection uses compact tuples rather than one temporary dictionary per champion.
- Semantic alignment validation can bind identity/hash/contract metadata during its existing validation pass.
- CPU diagnostic reads reuse the PPO semantic tensor's NumPy view instead of rebuilding a duplicate array; GPU diagnostics stay on-device.
- Native snapshot wrappers cache immutable keys and player count, expose lazy owner-pinned unit views, and initialize frozen shallow containers through built-in C-level constructors.
- Repeated reads of nested frozen mappings reuse cached views; scalar leaves remain uncached.
- NumPy-backed recipe fingerprints use native array comparison where possible, and semantic finite-value validation is performed by the canonical JSON serialization path.

These are implementation changes and performance hypotheses only. The final PPO-active benchmark decides whether they improve end-to-end training; no speedup is claimed from CI or microbenchmarks.

## Remaining acceptance gate

The remaining gate is the end-to-end PPO-active benchmark on the user's benchmark environment, compared with baseline **573-1** and the immediately preceding integrated profile using the same workload and lobby counts. The most recent committed benchmark profile remains `final-1`; the later wrapper/view-cache optimizations and the additional context validation tests need a fresh run before any performance claim is made.

No gain is claimed until the final benchmark is measured. Do not merge the PR or close #574–#578 until that evidence is reviewed.
