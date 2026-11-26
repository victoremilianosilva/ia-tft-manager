# Phase C — Issue #574: native strategic context contract

## Previous problem

The native audit snapshot already captures several strategic owner outputs, but the projection boundary does not expose one complete, provenance-preserving strategic context. The serialized priority rows retain intent, relation, priority, target star, sale restriction, and confidence only; native `UnitPriority` also owns priority tier, pair state, upgrade evidence, pool availability, and board/synergy contribution. The lineup projection omits bridge and endgame-target membership. Direction and pivot anchors contain richer native state than the current serialized subset.

Python validates some records and derives PPO numeric features, but it does not return a complete strategic-context object to downstream consumers. The v8 tensor/hash path is not a substitute for that audit/context contract.

## Technical rationale

Keep `TFTEngine::get_audit_snapshot` as the single snapshot producer and use existing native owners as the source of truth:

- `ActiveCompositionManager`: canonical active composition and version.
- `UnitPriorityPlanner`: intent, strategic relation, priority tier, pair state, upgrade progress, pool evidence, and confidence.
- `LineupPlanner`: selected board membership, entries, exits, deferred targets, bridge membership, and endgame targets.
- `StrategicPivotTransitionCoordinator` / strategic anchors: active direction and pivot-candidate identity, lifecycle, confidence, evidence, and composition binding.
- `UnitCopyProgress`: copy progress from physical board/bench instances.
- `ContextualActionEvaluator`: opportunity-cost evidence; absence is unavailable, not zero.

The migration serializes these already-produced values. It must not recreate them in Python, add strategy heuristics, or change planner behavior.

## Producer → contract → consumer map

| Domain | Native producer / owner | Existing snapshot fields | Completion required |
|---|---|---|---|
| Active composition | `ActiveCompositionManager` | identity, version, source sequence, unit IDs, core IDs | structured context and snapshot binding |
| Direction | direction anchor / planner commitment | valid, identity, selected round, reference IDs | direction value, composition binding, confidence, lifecycle, evidence |
| Pivot | pivot anchor candidate | valid, identity, target composition, source version, reference IDs | target direction, source direction identity, confidence, lifecycle, evidence |
| Unit priorities and relations | `UnitPriorityPlanner` | champion ID, intent, relation, priority, target star, sale restriction, confidence | tier, pair state, copies needed for pair, copies by star, upgrade progress, pool availability, board/synergy contribution |
| Upgrade progress | `UnitCopyProgress` | owned copy equivalent, copies toward next star, highest star | preserve in structured context; validate against observed owned entities |
| Lineup | `LineupPlanner` | selected, entries, exits, deferred IDs | bridge IDs and endgame-target IDs; outputs remain advisory |
| Opportunity cost | `ContextualActionEvaluator` | value, uncertainty, horizon, source, forgone candidate, value basis, availability | preserve with strategic context sequence |
| Synchronization | snapshot producer and strategic owners | episode, player, round, player decision sequence, strategic context sequence, planner sequence | validate producer-specific sequence and composition bindings |

## New responsibility

The strategic audit contract is versioned and structured. C++ remains responsible for producing facts and planner outputs from the same player snapshot. The binding transports the complete contract. Python validates provenance, availability, ranges, identity, and sequence consistency, then exposes structured strategic context separately from the PPO v8 numeric tensor.

## Contract and invariants

- Keep `TFTEngine::get_audit_snapshot` as the single producer; do not add parallel producers or recompute native planner outputs.
- Preserve observed facts, calculated evaluations, and planner intentions/outputs as distinct provenance classes.
- Preserve champion internal IDs and #573 physical entity identity; never substitute champion identity for physical unit identity.
- Pair and upgrade fields come from `UnitPriorityPlanner` / `UnitCopyProgress`, not Python inference from aggregate counts.
- Lineup, priorities, direction, and pivot are advisory context, never forced actions.
- Missing owner results are unavailable; never encode them as measured zero or valid empty results.
- Bind planner output to the same strategic context sequence, player, episode, round, and active composition version.
- Opportunity-cost rows retain source, value basis, horizon, uncertainty, and forgone-candidate identity.
- Keep semantic v8 numeric values, champion IDs, hash, PPO actions, masks, rewards, logits, sampling, and checkpoints unchanged.
- Keep the full Audit Context and replay data; do not reduce context to current Policy consumption.

## Impact

Adds a complete, provenance-preserving strategic-context contract for downstream Decision Context work. It reduces reconstruction in Python while keeping the current PPO interface stable. It does not rewrite strategy/planners, introduce economy/composition rules, execute Shadow actions, or alter Engine simulation behavior.

## Validation criteria

- Contract-version tests cover native v4 and compatibility v3 fixture paths.
- Producer-to-binding tests cover priority/pair/upgrade, lineup, direction, pivot, composition, and opportunity-cost fields.
- Parity tests compare transported values to native owner outputs from the same snapshot.
- Negative tests cover stale/mismatched sequences, composition versions, player/episode/round identity, missing versus neutral values, duplicate champion IDs, invalid enum/range values, and unavailable planner outputs.
- Tests prove the v8 numeric tensor, champion IDs, semantic hash, action/mask/reward behavior, and checkpoint contract are unchanged.
- Audit snapshot and replay remain complete.
- Benchmark exact pre-change baseline and implementation with PPO active, same workload/seeds/lobby counts/machine; compare with #573-1. Any relevant regression blocks completion.
