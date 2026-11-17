# Set 18 PvE item loot

Reference: Set 18 patch 18.5 weighted PvE component distribution.

## Reward rounds

| Round | Direct reward in the native engine |
|---|---|
| 1-2, 1-3, 1-4 | Opening PvE encounters; stage 1 weighted component package resolves after 1-4 |
| 2-7 | Stage 2 weighted component package |
| 3-7 | Stage 3 weighted component package |
| 4-7 | Stage 4 weighted component package; no guaranteed component anvil |
| 5-7 and later PvE boss rounds | One completed item granted directly to inventory |

No orb objects, orb counters, orb events, or pending orb-opening states are created.
Stages 1-4 grant only the component count from the weighted stage table.
From stage 5 onward, the PvE boss reward is one random unit-equipable completed
item, inserted directly into the player's item inventory.

## Weighted component packages

The published rows contain component counts plus orb outcomes. The native
simulation intentionally strips the orb portion and retains the published
weight and direct component count. Percentages are normalized at sampling time
because the published stage 3 and stage 4 rows include rounding that makes
their displayed totals slightly exceed 100%.

### Stage 1

- 35%: 3 components
- 35%: 3 components
- 8%: 2 components
- 8%: 2 components
- 3%: 5 components
- 3%: 5 components
- 3%: 4 components
- 2%: 3 components
- 2%: 1 component
- 1%: 3 components

### Stage 2

- 20%: 3 components
- 17%: 2 components
- 17%: 2 components
- 15%: 3 components
- 13%: 2 components
- 5%: 3 components
- 4%: 2 components
- 4%: 2 components
- 4%: 2 components
- 1%: 2 components

### Stage 3

- 20%: 4 components
- 20%: 4 components
- 17%: 3 components
- 13%: 3 components
- 13%: 3 components
- 5%: 4 components
- 4%: 5 components
- 3%: 3 components
- 2%: 3 components
- 2%: 2 components
- 1%: 3 components
- 0.25%: 4 components

### Stage 4

- 18%: 3 components
- 18%: 3 components
- 18%: 2 components
- 15%: 4 components
- 13%: 3 components
- 5%: 5 components
- 4%: 4 components
- 4%: 3 components
- 3%: 2 components
- 2%: 2 components
- 1%: 3 components
- 0.03%: 2 components

## Component pool

- Eight basic components, one copy each at the beginning.
- Every component dropped is removed from that player's PvE component pool.
- Before stages 2, 3 and 4, one copy of each basic component is added.
- Pool draws are per-player and deterministic from the match seed; the
  weighted component count is shared across players.

## Direct completed-item reward

At each PvE boss reward round from stage 5 onward, each living player receives
one random unit-equipable completed item directly in the item inventory. The
item is immediately available to the existing policy equip action; there is no
anvil choice and no orb reward event.
