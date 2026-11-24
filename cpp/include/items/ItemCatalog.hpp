#pragma once

#include "items/ItemEngine.hpp"

#include <nlohmann/json.hpp>

#include <algorithm>
#include <cmath>
#include <istream>
#include <limits>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace tft::items {

struct ItemCatalog {
    std::string set_id;
    std::vector<std::pair<std::string, std::string>> components;
    // Subset eligible for the active set's normal PvE component pool.
    // Special components (for example, Set 18's Pan/Spatula) remain valid
    // recipe dimensions but are not ordinary PvE component drops.
    std::vector<std::string> pve_loot_components;
    std::vector<ItemDefinition> items;
};

// Strict loader for externally sourced, normalized active-set data.
// It intentionally ships no made-up item/recipe table: callers must provide
// the real set catalog in this versioned format.
inline ItemCatalog load_item_catalog(std::istream& input) {
    using Json = nlohmann::json;
    const Json root = Json::parse(input);
    if (!root.is_object() || root.value("schema_version", 0) != 1 ||
        !root.contains("set_id") || !root["set_id"].is_string() ||
        !root.contains("components") || !root["components"].is_array() ||
        !root.contains("items") || !root["items"].is_array()) {
        throw std::invalid_argument("Invalid item catalog root/schema_version");
    }

    ItemCatalog catalog;
    catalog.set_id = root["set_id"].get<std::string>();
    if (catalog.set_id.empty()) {
        throw std::invalid_argument("Item catalog set_id cannot be empty");
    }
    if (root.contains("source_set_number")) {
        std::string source_number;
        if (root["source_set_number"].is_number_integer())
            source_number = std::to_string(root["source_set_number"].get<int>());
        else if (root["source_set_number"].is_string())
            source_number = root["source_set_number"].get<std::string>();
        if (!source_number.empty() && catalog.set_id.rfind("Set", 0) == 0 &&
            catalog.set_id != "Set" + source_number) {
            throw std::invalid_argument(
                "Item catalog set_id does not match source_set_number");
        }
    }

    std::set<std::string> component_ids;
    for (const auto& component : root["components"]) {
        if (!component.is_object() || !component.contains("id") ||
            !component["id"].is_string() || !component.contains("name") ||
            !component["name"].is_string()) {
            throw std::invalid_argument("Each component requires string id and name");
        }
        const auto id = component["id"].get<std::string>();
        const auto name = component["name"].get<std::string>();
        if (id.empty() || name.empty() || !component_ids.insert(id).second) {
            throw std::invalid_argument("Empty or duplicate item component id/name");
        }
        catalog.components.emplace_back(id, name);
        bool pve_loot_eligible = true; // schema-v1 legacy fixtures remain compatible
        if (component.contains("pve_loot_eligible")) {
            if (!component["pve_loot_eligible"].is_boolean())
                throw std::invalid_argument("pve_loot_eligible must be boolean");
            pve_loot_eligible = component["pve_loot_eligible"].get<bool>();
        }
        if (pve_loot_eligible) catalog.pve_loot_components.push_back(id);
    }

    if (catalog.pve_loot_components.size() > 8) {
        throw std::invalid_argument("PvE component loot pool cannot exceed eight basic components");
    }

    if (catalog.components.size() > 10) {
        throw std::invalid_argument("Item catalog exceeds the ten component-type policy head");
    }

    const auto parse_effects = [](const Json& effects) {
        std::vector<CombatEffectDefinition> parsed;
        if (!effects.is_array()) {
            throw std::invalid_argument("combat_effects must be an array");
        }
        for (const auto& raw : effects) {
            if (!raw.is_object() || !raw.contains("trigger") ||
                !raw["trigger"].is_string() || !raw.contains("operation") ||
                !raw["operation"].is_string()) {
                throw std::invalid_argument("Each combat effect requires trigger and operation strings");
            }
            CombatEffectDefinition effect;
            effect.trigger = raw["trigger"].get<std::string>();
            effect.operation = raw["operation"].get<std::string>();
            const bool supported_operation =
                effect.operation == "add_stat" ||
                effect.operation == "bonus_damage" ||
                effect.operation == "heal_max_hp_pct" ||
                effect.operation == "heal_missing_hp_pct" ||
                effect.operation == "heal_damage_pct_lowest_ally" ||
                effect.operation == "grant_charges" ||
                effect.operation == "mana_regen" ||
                effect.operation == "mana_gain_multiplier" ||
                effect.operation == "mana_on_attack" ||
                effect.operation == "grant_shield" ||
                effect.operation == "restore_mana" ||
                effect.operation == "revive" ||
                effect.operation == "apply_shred" ||
                effect.operation == "apply_burn" ||
                effect.operation == "apply_wound" ||
                effect.operation == "damage_on_enemy_cast" ||
                effect.operation == "add_stat_per_nearby_enemy" ||
                effect.operation == "reflect_damage" ||
                effect.operation == "stack_stat";
            if (!supported_operation) {
                throw std::invalid_argument(
                    "Unsupported combat effect operation (not implemented by CombatEngine): " +
                    effect.operation);
            }
            const bool supported_trigger =
                effect.trigger.empty() ||
                effect.trigger == "combat_start" ||
                effect.trigger == "on_attack" ||
                effect.trigger == "on_damage_dealt" ||
                effect.trigger == "on_kill" ||
                effect.trigger == "after_delay" ||
                effect.trigger == "while_hp_below" ||
                effect.trigger == "while_hp_above" ||
                effect.trigger == "on_ally_shield" ||
                effect.trigger == "periodic" ||
                effect.trigger == "on_ability_hit" ||
                effect.trigger == "on_damage_taken" ||
                effect.trigger == "on_critical_attack" ||
                effect.trigger == "on_enemy_cast" ||
                effect.trigger == "on_stack_cap";
            if (!supported_trigger) {
                throw std::invalid_argument(
                    "Unsupported combat effect trigger (not implemented by CombatEngine): " +
                    effect.trigger);
            }
            const bool supported_pair =
                (effect.operation == "add_stat" &&
                    (effect.trigger == "combat_start" || effect.trigger == "after_delay" ||
                     effect.trigger == "while_hp_below" ||
                     effect.trigger == "while_hp_above" || effect.trigger == "on_ally_shield" ||
                     effect.trigger == "periodic")) ||
                (effect.operation == "bonus_damage" && effect.trigger == "on_attack") ||
                (effect.operation == "heal_max_hp_pct" &&
                    (effect.trigger == "on_kill" || effect.trigger == "on_attack" ||
                     effect.trigger == "periodic")) ||
                (effect.operation == "heal_missing_hp_pct" &&
                    effect.trigger == "periodic") ||
                (effect.operation == "heal_damage_pct_lowest_ally" &&
                    effect.trigger == "on_damage_dealt") ||
                (effect.operation == "grant_charges" && effect.trigger == "on_kill") ||
                (effect.operation == "mana_regen" &&
                    (effect.trigger.empty() || effect.trigger == "combat_start")) ||
                (effect.operation == "mana_gain_multiplier" &&
                    effect.trigger == "combat_start") ||
                (effect.operation == "mana_on_attack" &&
                    effect.trigger == "on_attack") ||
                (effect.operation == "grant_shield" &&
                    (effect.trigger == "combat_start" || effect.trigger == "while_hp_below")) ||
                (effect.operation == "restore_mana" &&
                    (effect.trigger == "combat_start" || effect.trigger == "while_hp_below")) ||
                (effect.operation == "revive" && effect.trigger == "while_hp_below") ||
                (effect.operation == "apply_shred" &&
                    (effect.trigger == "combat_start" || effect.trigger == "on_attack" ||
                     effect.trigger == "on_ability_hit")) ||
                (effect.operation == "apply_burn" &&
                    (effect.trigger == "on_attack" || effect.trigger == "on_ability_hit" ||
                     effect.trigger == "periodic")) ||
                (effect.operation == "apply_wound" &&
                    (effect.trigger == "on_attack" || effect.trigger == "on_ability_hit" ||
                     effect.trigger == "periodic")) ||
                (effect.operation == "damage_on_enemy_cast" && effect.trigger == "on_enemy_cast") ||
                (effect.operation == "add_stat_per_nearby_enemy" && effect.trigger == "combat_start") ||
                (effect.operation == "reflect_damage" && effect.trigger == "on_damage_taken") ||
                (effect.operation == "stack_stat" &&
                    (effect.trigger == "on_attack" || effect.trigger == "on_damage_taken" ||
                     effect.trigger == "on_critical_attack")) ||
                (effect.operation == "add_stat" && effect.trigger == "on_stack_cap") ||
                (effect.operation == "bonus_damage" && effect.trigger == "on_ability_hit");
            if (!supported_pair) {
                throw std::invalid_argument(
                    "Unsupported combat effect operation/trigger pair: " +
                    effect.operation + "/" + effect.trigger);
            }
            const auto read_string = [&](const char* key, std::string& output) {
                if (!raw.contains(key)) return;
                if (!raw[key].is_string()) {
                    throw std::invalid_argument(std::string("Combat effect field must be a string: ") + key);
                }
                output = raw[key].get<std::string>();
            };
            read_string("stat", effect.stat);
            read_string("target", effect.target);
            read_string("condition", effect.condition);
            read_string("condition_trait", effect.condition_trait);
            read_string("stack_key", effect.stack_key);
            const bool supported_condition =
                effect.condition.empty() ||
                effect.condition == "has_trait" ||
                effect.condition == "trait_count_at_least" ||
                effect.condition == "role_tank" ||
                effect.condition == "role_fighter" ||
                effect.condition == "role_assassin" ||
                effect.condition == "role_other" ||
                effect.condition == "target_role_tank";
            if (!supported_condition) {
                throw std::invalid_argument(
                    "Unsupported combat effect condition: " + effect.condition);
            }
            if ((effect.condition == "has_trait" ||
                 effect.condition == "trait_count_at_least") &&
                effect.condition_trait.empty()) {
                throw std::invalid_argument(
                    "Trait-conditioned combat effect requires condition_trait");
            }
            const bool supported_target =
                effect.target.empty() || effect.target == "self" ||
                effect.target == "allies" ||
                effect.target == "allies_same_row_within_1" ||
                effect.target == "lowest_health_ally" ||
                effect.target == "target" ||
                effect.target == "enemies_within_radius" ||
                effect.target == "nearest_enemy_within_radius";
            if (!supported_target) {
                throw std::invalid_argument(
                    "Unsupported combat effect target: " + effect.target);
            }
            if ((effect.operation == "mana_regen" ||
                 effect.operation == "grant_charges" ||
                 effect.operation == "heal_max_hp_pct" ||
                 effect.operation == "heal_missing_hp_pct") &&
                !effect.target.empty() && effect.target != "self") {
                throw std::invalid_argument(
                    "This combat effect operation only supports the self target: " +
                    effect.operation);
            }
            if (effect.operation == "heal_damage_pct_lowest_ally" &&
                effect.target != "lowest_health_ally") {
                throw std::invalid_argument(
                    "heal_damage_pct_lowest_ally requires lowest_health_ally target");
            }
            if (effect.operation == "bonus_damage" &&
                effect.target == "allies_same_row_within_1") {
                throw std::invalid_argument(
                    "bonus_damage does not support allies_same_row_within_1");
            }
            if (effect.operation == "add_stat") {
                const bool supported_stat =
                    effect.stat == "attack_damage" ||
                    effect.stat == "attack_speed" ||
                    effect.stat == "ability_power" ||
                    effect.stat == "armor" ||
                    effect.stat == "magic_resist" ||
                    effect.stat == "omnivamp" ||
                    effect.stat == "damage_amplification" ||
                    effect.stat == "damage_reduction" ||
                    effect.stat == "max_hp";
                if (!supported_stat) {
                    throw std::invalid_argument(
                        "Unsupported add_stat target (not implemented by CombatEngine): " +
                        effect.stat);
                }
            }
            if (effect.operation == "grant_charges" && effect.stack_key.empty()) {
                throw std::invalid_argument(
                    "grant_charges requires a non-empty stack_key");
            }
            if (effect.operation == "heal_max_hp_pct" &&
                effect.trigger == "on_attack" && effect.stack_key.empty()) {
                throw std::invalid_argument(
                    "on_attack heal_max_hp_pct requires a non-empty stack_key");
            }
            if (raw.contains("damage_type")) {
                if (!raw["damage_type"].is_string()) {
                    throw std::invalid_argument("combat effect damage_type must be a string");
                }
                const auto damage_type = raw["damage_type"].get<std::string>();
                if (damage_type == "PHYSICAL") effect.damage_type = DamageType::PHYSICAL;
                else if (damage_type == "MAGIC") effect.damage_type = DamageType::MAGIC;
                else if (damage_type == "TRUE_DAMAGE") effect.damage_type = DamageType::TRUE_DAMAGE;
                else throw std::invalid_argument("Unknown combat effect damage_type: " + damage_type);
            }
            const auto read_number = [&](const char* key, float& output) {
                if (!raw.contains(key)) return;
                if (!raw[key].is_number()) {
                    throw std::invalid_argument(std::string("Combat effect field must be numeric: ") + key);
                }
                const double value = raw[key].get<double>();
                if (!std::isfinite(value) || value < 0.0 ||
                    value > static_cast<double>(std::numeric_limits<float>::max())) {
                    throw std::invalid_argument(std::string("Invalid combat effect value: ") + key);
                }
                output = static_cast<float>(value);
            };
            read_number("value", effect.value);
            read_number("duration", effect.duration);
            read_number("interval", effect.interval);
            read_number("delay", effect.delay);
            read_number("health_threshold", effect.health_threshold);
            read_number("critical_value", effect.critical_value);
            read_number("max_amount", effect.max_amount);
            read_number("radius", effect.radius);
            if (effect.trigger == "periodic" &&
                (!std::isfinite(effect.interval) || effect.interval <= 0.0f)) {
                throw std::invalid_argument("Periodic combat effects require a positive interval");
            }
            if (effect.operation == "heal_missing_hp_pct" &&
                (!std::isfinite(effect.max_amount) || effect.max_amount <= 0.0f)) {
                throw std::invalid_argument(
                    "Missing-health periodic healing requires a positive max_amount");
            }
            if (raw.contains("max_stacks")) {
                if (!raw["max_stacks"].is_number_integer() ||
                    raw["max_stacks"].get<int>() < 0) {
                    throw std::invalid_argument("combat effect max_stacks must be a nonnegative integer");
                }
                effect.max_stacks = raw["max_stacks"].get<int>();
            }
            if (raw.contains("min_trait_count")) {
                if (!raw["min_trait_count"].is_number_integer() ||
                    raw["min_trait_count"].get<int>() < 0) {
                    throw std::invalid_argument("combat effect min_trait_count must be a nonnegative integer");
                }
                effect.min_trait_count = raw["min_trait_count"].get<int>();
            }
            const auto read_bool = [&](const char* key, bool& output) {
                if (!raw.contains(key)) return;
                if (!raw[key].is_boolean()) {
                    throw std::invalid_argument(std::string("Combat effect field must be boolean: ") + key);
                }
                output = raw[key].get<bool>();
            };
            read_bool("percent_of_max_health", effect.percent_of_max_health);
            read_bool("percent_of_stat", effect.percent_of_stat);
            read_bool("scale_by_base_stat", effect.scale_by_base_stat);
            if (effect.scale_by_base_stat &&
                !((effect.operation == "add_stat" &&
                   ((effect.trigger == "periodic" && effect.stat == "attack_speed") ||
                    (effect.trigger == "on_stack_cap" &&
                     (effect.stat == "attack_speed" || effect.stat == "attack_damage")))) ||
                  (effect.operation == "stack_stat" &&
                   (effect.stat == "attack_speed" || effect.stat == "attack_damage")))) {
                throw std::invalid_argument(
                    "scale_by_base_stat requires a supported base attack stat effect");
            }
            if (effect.operation == "add_stat" && effect.percent_of_max_health) {
                throw std::invalid_argument(
                    "add_stat does not support percent_of_max_health; use percent_of_stat");
            }
            if (effect.operation == "bonus_damage" &&
                effect.percent_of_max_health && effect.percent_of_stat) {
                throw std::invalid_argument(
                    "bonus_damage cannot combine percent_of_max_health and percent_of_stat");
            }
            if (effect.operation == "bonus_damage" && effect.percent_of_stat) {
                const bool supported_damage_stat =
                    effect.stat == "attack_damage" ||
                    effect.stat == "attack_speed" ||
                    effect.stat == "ability_power" ||
                    effect.stat == "max_hp" ||
                    effect.stat == "armor" ||
                    effect.stat == "magic_resist";
                if (!supported_damage_stat) {
                    throw std::invalid_argument(
                        "bonus_damage percent_of_stat requires a supported stat");
                }
            }
            if (effect.operation == "grant_shield" &&
                (effect.target != "self" || effect.value <= 0.0f ||
                 effect.duration <= 0.0f || effect.value > 1.0f ||
                 !effect.percent_of_max_health)) {
                throw std::invalid_argument(
                    "grant_shield requires self target, positive max-health fraction and duration");
            }
            if (effect.operation == "restore_mana" &&
                (effect.target != "self" || effect.value <= 0.0f)) {
                throw std::invalid_argument("restore_mana requires positive value and self target");
            }
            if (effect.operation == "revive" &&
                (effect.target != "self" || effect.health_threshold <= 0.0f ||
                 effect.health_threshold > 1.0f || effect.duration <= 0.0f ||
                 effect.value <= 0.0f || effect.value > 1.0f ||
                 effect.critical_value <= 0.0f || effect.critical_value > 1.0f)) {
                throw std::invalid_argument(
                    "revive requires self target, valid health threshold, duration and heal fractions");
            }
            if (effect.operation == "apply_shred" &&
                ((effect.stat != "armor" && effect.stat != "magic_resist") ||
                 effect.value <= 0.0f || effect.value > 1.0f || effect.duration <= 0.0f ||
                 (effect.trigger == "combat_start" && effect.target != "enemies_within_radius") ||
                 (effect.trigger != "combat_start" && effect.target != "target" &&
                  effect.target != "enemies_within_radius") ||
                 ((effect.target == "enemies_within_radius" ||
                  effect.target == "nearest_enemy_within_radius") && effect.radius <= 0.0f))) {
                throw std::invalid_argument("apply_shred requires a valid stat, target, fraction and duration");
            }
            if (effect.operation == "apply_burn" &&
                ((effect.target != "target" && effect.target != "enemies_within_radius" &&
                  effect.target != "nearest_enemy_within_radius") ||
                 effect.value <= 0.0f || effect.value > 1.0f || effect.duration <= 0.0f ||
                 !effect.percent_of_max_health ||
                 ((effect.target == "enemies_within_radius" ||
                   effect.target == "nearest_enemy_within_radius") && effect.radius <= 0.0f))) {
                throw std::invalid_argument("apply_burn requires target, max-health fraction and duration");
            }
            if (effect.operation == "apply_wound" &&
                ((effect.target != "target" && effect.target != "enemies_within_radius" &&
                  effect.target != "nearest_enemy_within_radius") ||
                 effect.duration <= 0.0f ||
                 ((effect.target == "enemies_within_radius" ||
                   effect.target == "nearest_enemy_within_radius") && effect.radius <= 0.0f))) {
                throw std::invalid_argument("apply_wound requires target and positive duration");
            }
            if (effect.operation == "damage_on_enemy_cast" &&
                (effect.target != "self" || effect.value <= 0.0f ||
                 effect.radius <= 0.0f || effect.interval <= 0.0f)) {
                throw std::invalid_argument(
                    "damage_on_enemy_cast requires self target, positive damage, radius and cooldown");
            }
            if (effect.operation == "add_stat_per_nearby_enemy" &&
                (effect.target != "self" ||
                 (effect.stat != "armor" && effect.stat != "magic_resist") ||
                 effect.value <= 0.0f || effect.radius <= 0.0f)) {
                throw std::invalid_argument(
                    "add_stat_per_nearby_enemy requires self target, armor/MR, value and radius");
            }
            if (effect.operation == "reflect_damage" &&
                (effect.target != "enemies_within_radius" || effect.value <= 0.0f ||
                 effect.radius <= 0.0f || effect.interval <= 0.0f)) {
                throw std::invalid_argument(
                    "reflect_damage requires enemy radius, positive damage and cooldown");
            }
            if (effect.operation == "stack_stat" &&
                (effect.target != "self" || effect.stat.empty() ||
                 (effect.stat != "attack_damage" && effect.stat != "attack_speed" &&
                  effect.stat != "ability_power" && effect.stat != "damage_amplification") ||
                 effect.value <= 0.0f || effect.max_stacks <= 0 ||
                 effect.stack_key.empty())) {
                throw std::invalid_argument(
                    "stack_stat requires self target, stat, positive value, max_stacks and stack_key");
            }
            if (effect.trigger == "on_stack_cap" &&
                (effect.operation != "add_stat" || effect.target != "self" ||
                 effect.stack_key.empty() || effect.max_stacks <= 0)) {
                throw std::invalid_argument(
                    "on_stack_cap add_stat requires self target, stack_key and max_stacks");
            }
            if (effect.condition == "target_role_tank" &&
                (effect.operation != "bonus_damage" || effect.target != "target")) {
                throw std::invalid_argument(
                    "target_role_tank is supported only by target-scoped bonus_damage");
            }
            if (effect.condition == "trait_count_at_least" &&
                effect.min_trait_count <= 0) {
                throw std::invalid_argument(
                    "trait_count_at_least requires positive min_trait_count");
            }
            parsed.push_back(std::move(effect));
        }
        return parsed;
    };

    std::set<std::string> item_ids;
    std::set<std::string> recipes;
    std::size_t ordinary_item_count = 0;
    std::size_t effective_item_count = 0;
    const auto number = [](const Json& object, const char* key) {
        if (!object.contains(key)) return 0.0;
        if (!object[key].is_number()) {
            throw std::invalid_argument(std::string("Item stat must be numeric: ") + key);
        }
        const double value = object[key].get<double>();
        if (!std::isfinite(value) || value < 0.0) {
            throw std::invalid_argument(std::string("Item stat must be finite/nonnegative: ") + key);
        }
        return value;
    };

    for (const auto& entry : root["items"]) {
        if (!entry.is_object() || !entry.contains("id") ||
            !entry["id"].is_string() || !entry.contains("name") ||
            !entry["name"].is_string() || !entry.contains("recipe_components") ||
            !entry["recipe_components"].is_array() ||
            (entry["recipe_components"].size() != 2 &&
             entry["recipe_components"].size() != 0)) {
            throw std::invalid_argument("Each item requires id, name and either zero or two recipe_components");
        }

        ItemDefinition item;
        item.id = entry["id"].get<std::string>();
        item.name = entry["name"].get<std::string>();
        if (item.id.empty() || item.name.empty() ||
            !item_ids.insert(item.id).second) {
            throw std::invalid_argument("Empty or duplicate finished item id/name");
        }

        if (entry.contains("grants_trait")) {
            if (!entry["grants_trait"].is_string()) {
                throw std::invalid_argument("grants_trait must be a string");
            }
            item.grants_trait = entry["grants_trait"].get<std::string>();
        }
        if (entry["recipe_components"].empty() && item.grants_trait.empty()) {
            throw std::invalid_argument(
                "An item without a recipe must grant a trait or be explicitly modeled");
        }
        for (std::size_t i = 0; i < entry["recipe_components"].size(); ++i) {
            if (!entry["recipe_components"][i].is_string()) {
                throw std::invalid_argument("Recipe component IDs must be strings");
            }
            item.recipe_components[i] = entry["recipe_components"][i].get<std::string>();
            if (!component_ids.contains(item.recipe_components[i])) {
                throw std::invalid_argument("Recipe references an unknown component: " +
                                            item.recipe_components[i]);
            }
        }

        if (entry["recipe_components"].size() == 2) {
            const auto a = item.recipe_components[0];
            const auto b = item.recipe_components[1];
            const auto recipe_key = a < b ? a + "\x1f" + b : b + "\x1f" + a;
            if (!recipes.insert(recipe_key).second) {
                throw std::invalid_argument("Duplicate item recipe in catalog");
            }
        }

        const Json empty = Json::object();
        const auto& stats = entry.contains("stats") ? entry["stats"] : empty;
        const auto& weights = entry.contains("weights") ? entry["weights"] : empty;
        if (!stats.is_object() || !weights.is_object()) {
            throw std::invalid_argument("Item stats and weights must be objects");
        }
        item.attack_damage = number(stats, "attack_damage");
        item.attack_speed = number(stats, "attack_speed");
        item.ability_power = number(stats, "ability_power");
        item.critical_strike_chance = number(stats, "critical_strike_chance");
        item.critical_strike_damage = number(stats, "critical_strike_damage");
        item.max_health = number(stats, "health");
        item.armor = number(stats, "armor");
        item.magic_resist = number(stats, "magic_resist");
        item.mana = number(stats, "mana");
        item.omnivamp = number(stats, "omnivamp");
        item.damage_amplification = number(stats, "damage_amplification");
        item.damage_reduction = number(stats, "damage_reduction");
        item.carry_weight = number(weights, "carry");
        item.tank_weight = number(weights, "tank");
        item.support_weight = number(weights, "support");
        item.utility_weight = number(weights, "utility");
        if (entry.contains("grants_trait")) {
            if (!entry["grants_trait"].is_string()) {
                throw std::invalid_argument("grants_trait must be a string");
            }
            item.grants_trait = entry["grants_trait"].get<std::string>();
        }
        if (entry.contains("granted_trait_active_count")) {
            if (!entry["granted_trait_active_count"].is_number_integer() ||
                entry["granted_trait_active_count"].get<int>() < 1) {
                throw std::invalid_argument("granted_trait_active_count must be a positive integer");
            }
            item.granted_trait_active_count =
                entry["granted_trait_active_count"].get<int>();
        }
        if (entry.contains("unit_equipable")) {
            if (!entry["unit_equipable"].is_boolean()) {
                throw std::invalid_argument("unit_equipable must be a boolean");
            }
            item.unit_equipable = entry["unit_equipable"].get<bool>();
        }
        if (entry.contains("combat_effects")) {
            item.combat_effects = parse_effects(entry["combat_effects"]);
        }
        if (entry.contains("combat_effects_complete")) {
            if (!entry["combat_effects_complete"].is_boolean()) {
                throw std::invalid_argument("combat_effects_complete must be a boolean");
            }
            item.combat_effects_complete =
                entry["combat_effects_complete"].get<bool>();
        }
        if (entry.contains("deferred_stats")) {
            if (!entry["deferred_stats"].is_array()) {
                throw std::invalid_argument("deferred_stats must be an array");
            }
            for (const auto& stat : entry["deferred_stats"]) {
                if (!stat.is_string()) {
                    throw std::invalid_argument("deferred_stats entries must be strings");
                }
                item.deferred_stats.push_back(stat.get<std::string>());
            }
        }
        if (item.grants_trait.empty()) {
            ++ordinary_item_count;
            const bool has_numeric_effect =
                item.attack_damage != 0.0 || item.attack_speed != 0.0 ||
                item.ability_power != 0.0 || item.critical_strike_chance != 0.0 ||
                item.critical_strike_damage != 0.0 || item.max_health != 0.0 ||
                item.armor != 0.0 || item.magic_resist != 0.0 || item.mana != 0.0 ||
                item.omnivamp != 0.0 || item.damage_amplification != 0.0 ||
                item.damage_reduction != 0.0;
            if (has_numeric_effect || !item.combat_effects.empty())
                ++effective_item_count;
        }
        catalog.items.push_back(std::move(item));
    }

    // A valid JSON shape is not enough: reject catalogs where ordinary finished
    // items are almost all inert. Trait emblems are measured separately because
    // their value is the granted trait rather than a numeric combat stat.
    if (ordinary_item_count > 0 &&
        effective_item_count * 2 < ordinary_item_count) {
        throw std::invalid_argument(
            "Item catalog has too few ordinary items with applied combat effects");
    }

    // Reuse the engine's validation for duplicate IDs/recipes as a final guard.
    std::vector<std::string> component_id_list;
    component_id_list.reserve(catalog.components.size());
    for (const auto& component : catalog.components) component_id_list.push_back(component.first);
    (void)ItemEngine(catalog.items, std::move(component_id_list));
    return catalog;
}

} // namespace tft::items
