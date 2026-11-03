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
      },
      "unit_equipable": true,
      "combat_effects": [
        {
          "trigger": "combat_start",
          "operation": "add_stat",
          "stat": "attack_damage",
          "target": "self",
          "value": 0.15,
          "percent_of_stat": true
        }
      ]
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
- `unit_equipable` defaults to true. Player-scope items (such as items whose source effect is `MaxArmySizeIncrease`) must set it to false until the lobby implements their player-level behavior; they are not offered as champion equipment, craft targets, or completed-item anvil choices.
- This schema describes data, not yet a full live item economy. Item drops, lobby persistence, PPO actions/masks and Viewer telemetry are separate integration tasks.

## Source-effect coverage metadata

Generated items include `effect_coverage` with four arrays:
- `source_keys`: non-zero source keys retained from CommunityDragon.
- `generic_stat_keys`: keys normalized into the generic numeric stat fields.
- `generic_combat_keys`: keys normalized into generic CombatEngine effects.
- `not_generic_normalized_keys`: source keys that need a separate review for a tested item-specific handler or future generic implementation.

The last list is **not automatically a list of broken items**: some entries are parameters for a passive or are covered by existing ID-specific handlers in `CombatEngine.cpp`. It makes the coverage gap explicit per item and prevents raw source metadata from being mistaken for a normalized combat effect.

## Supported combat-effect contract

The runtime loader accepts only effects that have a matching handler in `CombatEngine`. Supported operations are:

- `add_stat`: `combat_start`, `after_delay`, `while_hp_below`, `on_ally_shield`.
- `bonus_damage`: `on_attack`.
- `heal_max_hp_pct`: `on_attack` (charged healing) or `on_kill`.
- `grant_charges`: `on_kill`.
- `mana_regen`: empty trigger or `combat_start`.

Supported conditions are `has_trait`, `trait_count_at_least`, `role_tank`, `role_fighter`, `role_assassin`, and `role_other`. Supported targets are empty, `self`, `allies`, and `allies_same_row_within_1`. For `add_stat`, the runtime supports attack damage, attack speed, ability power, armor, magic resistance, omnivamp, damage amplification, damage reduction, and max HP.

Unknown operations, unsupported operation/trigger pairs, stat names, conditions, or targets are rejected by the C++ loader. This is intentional: raw `source_effects` are provenance, not proof that an effect is implemented. A source passive must not be treated as active until it is normalized into this contract or covered by a tested item-specific CombatEngine handler.
