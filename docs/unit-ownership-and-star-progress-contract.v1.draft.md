# Unit Ownership and Star Progress Contract v1

**Status:** approved documentary specification; runtime implementation and executable acceptance blocked until Gate 8  
**Contract ID:** `tft.unit-evidence.v1`  
**Target:** `new-arquiteture`  
**Related:** #283, #281, #282, #284, #289, #291; Observation #293

> Documentation only. This contract does not change unit rules, Engine legality, runtime code, PPO, observations, rewards, checkpoints, masks, or Viewer behavior.

## 1. Purpose

The audit found that the integrated path aggregates board and bench units into equivalent-copy counts (1★ = 1, 2★ = 3, 3★ = 9), then derives progress toward the next star using the highest observed star and integer division/modulo. This scalar representation can lose progress information in mixed 1★/2★ inventories. The audited UnitPriority builder also does not populate shop copies or unit cost, and UnitPriorityContext does not populate available gold; affordability therefore cannot reliably include shop offers.

This contract defines lossless unit ownership, tier-specific upgrade progress, shop opportunity, pool availability, and the evidence boundary shared by composition generation, priorities, pivot feasibility, lineup, candidate evaluation, and SELL protection.

## 2. Normative principles

1. **Physical instances are canonical.** Preserve each owned unit instance and its location. Aggregated counts are derived indexes, not replacements for instance identity.
2. **Board and bench are owned inventory.** Shop offers are temporary opportunities, not owned copies. Pool availability is a separate external estimate/state.
3. **Star tiers are not interchangeable scalar copies.** Keep physical counts by star tier; equivalent-copy totals may be diagnostic only.
4. **Unknown pool/shop data is not zero.** Missing, stale, or unavailable evidence remains explicit.
5. **One snapshot lineage.** Unit instances, shop offers, gold, and pool evidence carry matching match/player/round and typed source-sequence references or validated correlation.
6. **No double counting.** A unit instance contributes to exactly one owned location and one star tier. A shop offer is never added to owned inventory.
7. **Upgrade projections are recipes, not facts.** Projected combinations must identify source instances/offers and units consumed; they do not mutate inventory.
8. **Protection precedes sale.** SELL candidates require complete pair, star-progress, item, trait, lineup, and pivot evidence.
9. **No rule duplication.** Native Engine rules/masks remain final authority; this contract describes evidence only.

## 3. Unit identity and ownership envelope

Each owned unit instance must preserve:
- stable instance identifier when the source provides one; otherwise a documented scoped identity derived from source slot and snapshot, never champion ID alone;
- champion/unit definition ID;
- star tier;
- location: board or bench;
- exact board coordinate or bench slot;
- item association per instance;
- source match/player/round and typed sequence refs;
- observed/derived origin, quality, source component, and reason.

A champion ID is a grouping key, not a physical instance identity. Two copies of the same champion in different slots remain distinct. Board and bench are disjoint ownership locations. Moving a unit changes its location in a later snapshot; it does not create another copy.

The canonical owned inventory is the lossless set of instances. Derived aggregates by champion and star tier must be reproducible from that set.

## 4. Star-tier progress contract

For each champion ID, preserve at least:
- `owned_1_star_instances`;
- `owned_2_star_instances`;
- `owned_3_star_instances`;
- `shop_1_star_offers` (and other shop tiers only if source rules support them);
- `pool_available` as value plus evidence quality, or unknown;
- explicit upgrade recipes/projections and source instances consumed.

Progress must be tier-specific:
- **Toward 2★:** count actual 1★ instances eligible to combine; preserve the remainder and the exact instances that would be consumed.
- **Toward 3★:** count actual 2★ instances eligible to combine; preserve the remainder and exact instances. If the system projects first creating additional 2★ units from 1★ instances, represent that as a multi-step recipe with separate inputs, not as a scalar conversion.
- **Existing 3★:** no further star-upgrade progress; retain instances and copies for ownership/diagnostics but do not count them as available 1★ or 2★ units.

A total equivalent-copy value may be emitted for diagnostics, but must never be used alone to infer the next upgrade, pair protection, or 3★ progress. Mixed-star inventories must not lose remainders through integer division. The upgrade planner must specify which target tier is being evaluated and the recipe that reaches it.

## 5. Shop and pool evidence

### 5.1 Shop offers

Each shop offer is a separate record:
- exact shop slot;
- champion ID and offer tier;
- unit cost from the current rules/version;
- availability/validity;
- same match/player/round/source sequence as the shop snapshot.

Shop offers are not owned units. They may count as temporary potential progress only in a separate projection that proves affordability and identifies the exact offer slot. They must not be added to owned copies.

Affordability requires observed available gold and known unit cost from the same correlated snapshot. Missing gold or cost makes affordability unknown, not false/zero.

### 5.2 Pool availability

Pool availability is separate from ownership and shop offers. It must carry source, observation time/sequence, quality, and uncertainty. If pool data is unavailable or not permitted by the source, represent it as unknown. Do not infer pool count from owned units, shop visibility, or absence of offers.

## 6. Shared consumer contract

All consumers must use the same tier-aware evidence semantics:

| Consumer | Required use |
|---|---|
| NativeStrategicCompositionGenerator | Candidate composition feasibility uses owned tier counts and explicit shop/pool uncertainty |
| UnitPriorityPlanner | Progress-to-target uses tier-specific owned instances; shop opportunity and affordability remain separate |
| PivotFeasibilityEvaluator | Pivot cost/feasibility includes exact units and upgrade recipes without double counting |
| LineupPlanner | Uses owned instance identities and board/bench location; no duplicate champion-ID pseudo-instances |
| Candidate evaluators | BUY/SELL candidates reference exact shop offer or owned unit instance |
| SELL protection | Pair/star progress, items, traits, lineup, and pivot dependencies are evaluated on exact instances |

A consumer may derive a view optimized for its task, but must preserve source instance references and must not redefine the underlying count semantics.

## 7. SELL and pair protection

A unit is not sell-eligible merely because it is outside the active composition target. Before producing SELL evidence, the pipeline must evaluate:
- whether the instance is part of a 1★ pair or 2★ upgrade recipe;
- whether it is a component of a 3★ progression path;
- whether its items make it strategically distinct or costly to replace;
- whether it completes or materially contributes to active/core traits;
- whether it is selected by the current lineup or is a deferred/bridge unit;
- whether it is needed by an active or candidate pivot;
- whether the exact instance and sell value are known.

Protection decisions must include reasons and evidence refs. If any required protection evidence is missing, SELL eligibility is unknown/rejected for recommendation purposes, not optimistically assumed safe. Coordinate with #281 candidate physical parameters and existing #291 protections; do not weaken safeguards to make SELL candidates appear.

## 8. Snapshot and provenance requirements

All ownership, shop, gold, and pool records must carry:
- engine match/episode and player;
- round;
- typed source-sequence refs;
- source component/version;
- field-level origin and quality.

A shop refresh or gold change within the same round can invalidate affordability and candidate projections even if composition ID/version is unchanged. Consumers must validate sequence freshness against the expected current snapshot.

Observed zero shop offers is different from unavailable shop data. Observed empty pool is different from unknown pool. Empty owned inventory is valid only when the ownership snapshot itself is valid and complete.

## 9. Acceptance matrix — after Gate 8

| Scenario | Required result |
|---|---|
| All owned units on board | Exact instances and tiers preserved |
| Copies split board/bench | Aggregate equals instance set without duplication |
| Mixed 1★ and 2★ copies | Tier-specific progress retains all remainders |
| Multiple 2★ copies toward 3★ | Exact 2★ instances and progress are represented |
| 3★ unit present | Not counted as lower-tier upgrade copies |
| Shop offer for owned champion | Separate temporary opportunity, not owned copy |
| Affordable shop offer | Affordability uses same-snapshot gold and cost |
| Unaffordable offer | Not counted as purchasable progress |
| Duplicate shop offers | Each exact slot preserved |
| Pool unknown | Unknown, never zero or owned count |
| Pair/star progress protected | SELL candidate rejected or explicitly protected |
| Item/trait/lineup/pivot dependency | Exact instance not sold without complete evidence |
| Stale shop/gold/board sequence | Projection and candidates rejected as stale |
| Two players/matches | Instance and aggregate namespaces do not leak |

Integrated replay must prove that generator, priority planner, pivot feasibility, lineup, candidate evaluators, and SELL protection produce coherent results from the same snapshots.

## 10. Gate status and implementation boundary

This specification defines the documentary unit evidence contract. #283 remains open until all consumers adopt the same semantics and post-Gate-8 executable tests prove tier-aware progress, shop affordability, pool uncertainty, and protection behavior.

No runtime code/tests, unit rules, PPO, observations, rewards, checkpoints, masks, Engine rules, Viewer behavior, or game actions are changed. Gate 8 and explicit implementation authorization remain mandatory.
