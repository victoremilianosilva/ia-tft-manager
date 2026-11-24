# Strategic producer reuse and cache contracts

## Previous problem

The native snapshot and planner evidence paths repeated catalog projection and item-fit work:

- The native composition producer rebuilt the compact unit catalog for each player and decision snapshot.
- `get_audit_snapshot()` created a new `ItemFitCache` for each player snapshot, so inventory-to-target and recipe-to-target compatibility results could not survive the next step.
- `PlannerEvidenceAdapters::item()` independently called `ItemEngine::item_fit()`, duplicating evaluations already performed by the snapshot producer.
- Item-fit results depend on the complete semantic `UnitProfile`, not only the unit UUID.

## Technical rationale

The unit catalog is immutable for the lifetime of the engine. Item-fit results are reusable only while the same item engine, item identifier, unit UUID, and complete semantic profile remain unchanged. Reuse must not silently retain a result after a trait, star, role, item-derived stat, position role, or composition preference changes.

## New responsibilities

- `TFTEngine::Impl` owns one item-fit cache per player, scoped to that player's `ItemEngine`.
- `ItemFitCache` keeps only the latest exact profile for each UUID and clears that UUID's item results when any profile field differs.
- Audit snapshot inventory/recipe target features, native owned-unit item-fit evidence, and planner item evidence use the same per-player cache.
- `TFTEngine::Impl` prepares the compact native composition catalog once and passes a non-owning immutable reference to the generator.
- Standalone generator callers may continue to supply the value-owned catalog.

## Contracts and invariants

- Cache ownership is per player; results are never shared across lobbies/players.
- A cache is recreated if its `ItemEngine` owner changes.
- Profile equality includes UUID, star, role, frontline/backline flags, all numeric combat/composition values, traits, and preferred traits.
- An item-fit cache hit returns exactly the result produced for the same complete profile; any changed field triggers recomputation.
- The borrowed catalog is immutable during `generate()` and its owner outlives the call.
- Candidate generation, candidate identities, sorting, evidence, and provenance remain unchanged.
- No compatibility calculation, recipe, target, strategic feature, or PPO input is removed.

## Producer/consumer map

| Producer | Consumer | Reuse boundary |
| --- | --- | --- |
| `TFTEngine::Impl::native_composition_catalog` | `NativeStrategicCompositionGenerator::generate()` | Engine/catalog lifetime |
| `semantic_item_unit_profiles()` + equipped item IDs | Native owned-unit item-fit evidence | Player + exact unit profile + item ID |
| `ItemFitCache` | `PlannerEvidenceAdapters::item()` | Same player ItemEngine and exact profile |
| `ItemFitCache` | Audit snapshot inventory/recipe target matrices | Same player ItemEngine and exact profile |
| `ItemFitCache` | Native owned-unit item-fit evidence | Same player ItemEngine and exact profile |

## Validation

- Item-fit cache tests verify same-profile hits and invalidation after a semantic trait change.
- Generator tests compare value-owned and borrowed catalog output.
- Native build and strategic tests must pass.
- Snapshot semantic fields, item-fit availability/source/uncertainty, candidate identity, and provenance remain unchanged.
- Performance measurement of hit rate, allocations, and elapsed time remains a separate follow-up; no gain is claimed without measurement.
