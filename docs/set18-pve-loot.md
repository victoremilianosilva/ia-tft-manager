# Set 18 PvE item loot

Reference: TFTClimb Set 18 loot distribution, patch 18.5 (checked 2026-10-29).
The implementation stores the per-stage weighted outcomes in
`cpp/include/items/PveLootDistribution.hpp`. The percentages are normalized at
sampling time because the published stage 3 and stage 4 rows include rounding
that makes their displayed totals slightly exceed 100%.

## Reward rounds

| Round | Set 18 reward |
|---|---|
| 1-2, 1-3, 1-4 | Opening PvE encounters; the stage 1 weighted loot package is resolved after 1-4 |
| 2-7 | Stage 2 weighted component/orb package |
| 3-7 | Stage 3 weighted component/orb package |
| 4-7 | Stage 4 weighted component/orb package; this is not a guaranteed component anvil |
| 5-7 and later PvE boss rounds | Threshold orbs at 66% and 33%; completed-item anvil on victory |

Random component drops stop after stage 4. The completed-item anvil is granted
for the later PvE boss rounds, rather than only 5-7 and 6-7.

## Weighted component/orb packages

Each row is `weight%: components / gray / blue / gold / prismatic`.

### Stage 1

- 35: 3 / 3 / 0 / 0 / 0
- 35: 3 / 0 / 1 / 0 / 0
- 8: 2 / 3 / 1 / 0 / 0
- 8: 2 / 0 / 2 / 0 / 0
- 3: 5 / 3 / 0 / 0 / 0
- 3: 5 / 0 / 1 / 0 / 0
- 3: 4 / 0 / 1 / 0 / 0
- 2: 3 / 0 / 2 / 0 / 0
- 2: 1 / 3 / 2 / 0 / 0
- 1: 3 / 5 / 0 / 0 / 0

### Stage 2

- 20: 3 / 1 / 0 / 0 / 0
- 17: 2 / 1 / 0 / 0 / 0
- 17: 2 / 0 / 1 / 0 / 0
- 15: 3 / 0 / 1 / 0 / 0
- 13: 2 / 2 / 0 / 0 / 0
- 5: 3 / 3 / 0 / 0 / 0
- 4: 2 / 1 / 0 / 1 / 0
- 4: 2 / 1 / 1 / 0 / 0
- 4: 2 / 0 / 2 / 0 / 0
- 1: 2 / 0 / 1 / 1 / 0

### Stage 3

- 20: 4 / 1 / 0 / 0 / 0
- 20: 4 / 2 / 0 / 0 / 0
- 17: 3 / 1 / 1 / 0 / 0
- 13: 3 / 3 / 0 / 0 / 0
- 13: 3 / 0 / 2 / 0 / 0
- 5: 4 / 0 / 1 / 0 / 0
- 4: 5 / 1 / 0 / 0 / 0
- 3: 3 / 1 / 0 / 1 / 0
- 2: 3 / 1 / 0 / 0 / 1
- 2: 2 / 0 / 2 / 0 / 0
- 1: 3 / 0 / 1 / 1 / 0
- 0.25: 4 / 1 / 0 / 1 / 0

### Stage 4

- 18: 3 / 2 / 0 / 0 / 0
- 18: 3 / 1 / 1 / 0 / 0
- 18: 2 / 2 / 1 / 0 / 0
- 15: 4 / 1 / 0 / 0 / 0
- 13: 3 / 3 / 0 / 0 / 0
- 5: 5 / 1 / 0 / 0 / 0
- 4: 4 / 1 / 1 / 0 / 0
- 4: 3 / 1 / 0 / 1 / 0
- 3: 2 / 0 / 2 / 0 / 0
- 2: 2 / 2 / 0 / 0 / 1
- 1: 3 / 0 / 2 / 1 / 0
- 0.03: 2 / 0 / 0 / 1 / 1

## Component pool

- Eight basic components, one copy each at the beginning.
- Every component dropped is removed from that player's PvE component pool.
- Before stages 2, 3 and 4, one copy of each basic component is added.
- Pool draws are per-player and deterministic from the match seed; the package
  (component count and orb quality/counts) is shared across players.

## Implementation boundary

The current C++ lobby has no general orb-opening/reward resolver. The new code
applies the weighted component drops and completed-item anvil schedule, and
records orb counts/thresholds in events for audit. It does **not** yet materialize
the contents of gray/blue/gold/prismatic orbs (gold, champions, duplicators,
reforgers, etc.). Those rewards must not be counted as granted inventory until
a generic orb reward resolver is implemented.
