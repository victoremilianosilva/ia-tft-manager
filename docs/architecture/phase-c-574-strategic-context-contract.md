# Phase C — Issue #574: native strategic context contract

## Previous problem

The native audit snapshot already captures several strategic owner outputs, but the projection boundary does not expose one complete, provenance-preserving strategic context. In particular, the serialized priority rows currently retain intent/relation/priority/target-star/sale restriction/confidence only; the native `UnitPriority` also owns pair and upgrade evidence, tier, board/synergy contribution, pool availability, and physical copy counts. The lineup projection similarly publishes selected/entry/exit/deferred IDs but omits bridge and endgame-target membership. Direction and pivot anchors contain richer native state than the current serialized subset.

Python validates some of these records and derives PPO numeric features, but it does not return a complete strategic-context object to downstream consumers. The v8 tensor/hash path is not a substitute for that audit/context contract.

## Technical rationale

Keep `TFTEngine::get_audit_snapshot` as the single snapshot producer and use the existing native owners as the source of truth:

- `CompositionIntelligenceRuntime::active` owns the canonical active composition and version.
- `UnitPriorityPlanner` owns per-champion intent, strategic relation, priority tier, pair state, upgrade progress, pool evidence, and confidence.
- `LineupPlanner` owns selected board membership, entries, exits, deferred targets, bridge membership, and endgame targets.
- `StrategicPivotTransitionCoordinator` / strategic anchors own active direction and pivot-candidate identity, lifecycle, confidence, evidence, and composition binding.
- `UnitCopyProgress` produces copy progress from physical board/bench instances.
- `ContextualActionEvaluator` produces opportunity-cost evidence; absence is explicitly unavailable, not zero.

The migration serializes these already-produced values. It must not recreate them in Python, add strategy heuristics, or change planner behavior.

## Current producer → contract → consumer map

| Domain | Native producer / owner | Existing snapshot fields | Missing or incomplete projection |
|---|---|---|---|
| Active composition | `ActiveCompositionManager` | identity, version, source sequence, unit IDs, core IDs | preserve as a structured context domain and validate player/sequence/version binding |
| Direction | strategic direction anchor / planner commitment | valid, identity, selected round, reference IDs | direction value, composition binding, confidence, lifecycle, evidence |
| Pivot | pivot anchor candidate | valid, identity, target composition, source composition version, reference IDs | target direction, source direction identity, confidence, lifecycle, evidence |
| Unit priorities and relations | `UnitPriorityPlanner` | champion ID, intent, relation, priority, target star, sale restriction, confidence | tier, pair state, copies needed for pair, copies by star, upgrade progress, pool availability, board/synergy contribution |
| Upgrade progress | `UnitCopyProgress` | owned copy equivalent, copies toward next star, highest star | retain in complete structured context and validate against observed owned entities |
| Lineup | `LineupPlanner` | selected, entries, exits, deferred IDs | bridge IDs and endgame target IDs; keep outputs explicitly advisory |
| Opportunity cost | `ContextualActionEvaluator` / native opportunity-cost producer | value, uncertainty, horizon, source, forgone candidate, value basis, availability | expose in the same complete context with its evidence identity and explicit unavailable state |
| Synchronization | snapshot producer and strategic owners | episode, player, round, player decision sequence, strategic context sequence, planner sequence | validate every producer-specific sequence against the enclosing snapshot and active composition version |

## New responsibility

The strategic audit contract becomes a versioned, structured projection of the native owner state. C++ remains responsible for producing facts and planner outputs from the same player snapshot. The binding transports the complete contract. Python validates provenance, availability, ranges, identity, and sequence consistency, then exposes the structured strategic context separately from the PPO v8 numeric tensor.

The existing semantic numeric features remain unchanged in this issue. The context projection is additive metadata; it does not become a new Policy input or change checkpoint dimensions.

## Contract and invariants

- Keep the single producer `TFTEngine::get_audit_snapshot`; do not add parallel producers or recompute native planner outputs.
- Preserve the distinction between observed facts, calculated evaluations, and planner intentions/outputs.
- Preserve champion internal IDs and #573 physical entity identity; never substitute champion identity for physical unit identity.
- Pair and upgrade fields must come from `UnitPriorityPlanner` / `UnitCopyProgress`, not be inferred from aggregate counts in Python.
- Lineup, priorities, direction, and pivot are advisory context, never forced actions.
- A missing owner result is unavailable; it must not be encoded as a measured zero or a valid empty result.
- Bind planner output to the same `strategic_context_sequence`, player, episode, round, and active composition identity/version.
- Opportunity-cost rows retain source, value basis, horizon, uncertainty, and forgone-candidate identity.
- Keep semantic v8 numeric values, champion IDs, hash, PPO actions, masks, rewards, logits, sampling, checkpoints, and planner behavior unchanged.
- Keep the full Audit Context and replay data; do not reduce context to current Policy consumption.

## Impact

This adds a complete, provenance-preserving strategic-context contract for downstream Decision Context work. It removes pressure to reconstruct strategy in Python while keeping the current PPO interface stable. It does not rewrite strategy/planners, introduce economy/composition rules, execute Shadow actions, or alter Engine simulation behavior.

## Validation criteria

- Contract-version tests cover native and compatibility fixture paths.
- Producer-to-binding tests cover all priority/pair/upgrade, lineup, direction, pivot, composition, and opportunity-cost fields.
- Parity tests compare transported values to the native owner outputs from the same snapshot.
- Negative tests cover stale/mismatched sequences, composition versions, player/episode/round identity, missing versus neutral values, duplicate champion IDs, invalid enum/range values, and unavailable planner outputs.
- Tests prove the v8 numeric tensor, champion IDs, semantic hash, action/mask/reward behavior, and checkpoint contract are unchanged.
- Audit snapshot and replay remain complete.
- Benchmark the exact pre-change baseline and the implementation with PPO active, using the same workload, seeds, lobby counts, and machine; compare both to the #573-1 reference. Any relevant regression blocks completion.
