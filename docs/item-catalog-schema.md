# Item catalog contract

The engine intentionally does not ship a made-up TFT set catalog. Supply a normalized JSON file from the active set's authoritative data source, then pass its parsed `items` into `tft::items::ItemEngine`.

The current header-only loader is `cpp/include/items/ItemCatalog.hpp` and accepts schema version 1:

```json
{
  "schema_version": 1,
  "set_id": "active-set-id",
  "components": [
    { "id": "component-id-a", "name": "Component A" },
    { "id": "component-id-b", "name": "Component B" }
  ],
  "items": [
    {
      "id": "finished-item-id",
      "name": "Finished Item",
      "recipe_components": ["component-id-a", "component-id-b"],
      "stats": {
        "attack_damage": 10,
        "attack_speed": 0.15,
        "ability_power": 0,
        "critical_strike_chance": 0,
        "critical_strike_damage": 0,
        "health": 0,
        "armor": 0,
        "magic_resist": 0,
        "mana": 0,
        "omnivamp": 0,
        "damage_amplification": 0,
        "damage_reduction": 0
      },
      "weights": {
        "carry": 1,
        "tank": 0,
        "support": 0,
        "utility": 0
      }
    }
  ]
}
```

## Normalization rules

- `set_id` identifies the source set; the loader does not infer or choose a set.
- Component and finished-item IDs must be unique and non-empty.
- Every finished item must name exactly two known components. Duplicate recipes are rejected.
- Stats and weights are optional and default to zero; supplied values must be finite, numeric and non-negative.
- Percentage-like bonuses are represented as fractions where applicable (for example, `0.15` means +15%). The source adapter must normalize the source format to this contract.
- This schema describes data, not yet a full live item economy. Item drops, lobby persistence, PPO actions/masks and Viewer telemetry are separate integration tasks.
