# Item PPO action contract (migration stage)

The legacy economy/board action remains unchanged at six components. Item actions are defined separately with seven categorical components:

| Index | Meaning | Dimension |
|---:|---|---:|
| 0 | WAIT, CRAFT, EQUIP, TRANSFER, UNEQUIP | 5 |
| 1 | First component slot | 18 |
| 2 | Second component slot | 18 |
| 3 | Item inventory slot | 18 |
| 4 | Source unit (bench 0–8, then board 9–36) | 37 |
| 5 | Target unit (bench 0–8, then board 9–36) | 37 |
| 6 | Equipped item slot | 3 |

These are schema bounds, not proof that a slot is occupied or an operation is legal. The native engine must construct state-derived masks and revalidate identities before mutation. Invalid actions must not mutate components, inventory, or equipment.

**Scope warning:** this commit defines the representation and structural validation only. Per-player ItemEngine ownership, live item drops, native masks/observations, PPO heads and rollout storage, combat synchronization, and checkpoint migration still need wiring. Do not train or deploy a policy using these dimensions until those integrations land.
