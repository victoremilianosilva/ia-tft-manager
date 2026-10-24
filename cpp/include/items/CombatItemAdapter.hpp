#pragma once

#include "combat/CombatInput.hpp"
#include "items/ItemEngine.hpp"

#include <string>

namespace tft::items {

// Converts normalized catalog values to the combat input contract.
// Percentage-like fields are fractions (0.15 means +15%). A data loader
// must normalize the active set's source format before constructing ItemDefinition.
inline CombatItem to_combat_item(const ItemDefinition& definition) {
    CombatItem item{};
    item.api_name = definition.id;
    item.name = definition.name;
    item.attack_damage = static_cast<float>(definition.attack_damage);
    item.ability_power = static_cast<float>(definition.ability_power);
    item.attack_speed = static_cast<float>(definition.attack_speed);
    item.critical_strike_chance =
        static_cast<float>(definition.critical_strike_chance);
    item.critical_strike_damage =
        static_cast<float>(definition.critical_strike_damage);
    item.health = static_cast<float>(definition.max_health);
    item.armor = static_cast<float>(definition.armor);
    item.magic_resist = static_cast<float>(definition.magic_resist);
    item.mana = static_cast<float>(definition.mana);
    item.omnivamp = static_cast<float>(definition.omnivamp);
    item.damage_amplification =
        static_cast<float>(definition.damage_amplification);
    item.damage_reduction =
        static_cast<float>(definition.damage_reduction);
    return item;
}

} // namespace tft::items
