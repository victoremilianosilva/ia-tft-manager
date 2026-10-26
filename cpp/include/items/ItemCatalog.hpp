#pragma once

#include "items/ItemEngine.hpp"

#include <nlohmann/json.hpp>

#include <algorithm>
#include <cmath>
#include <istream>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace tft::items {

struct ItemCatalog {
    std::string set_id;
    std::vector<std::pair<std::string, std::string>> components;
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
            if (raw.contains("max_stacks")) {
                if (!raw["max_stacks"].is_number_integer() ||
                    raw["max_stacks"].get<int>() < 0) {
                    throw std::invalid_argument("combat effect max_stacks must be a nonnegative integer");
                }
                effect.max_stacks = raw["max_stacks"].get<int>();
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
            parsed.push_back(std::move(effect));
        }
        return parsed;
    };

    std::set<std::string> item_ids;
    std::set<std::string> recipes;
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
            entry["recipe_components"].size() != 2) {
            throw std::invalid_argument("Each finished item requires id, name and two recipe_components");
        }

        ItemDefinition item;
        item.id = entry["id"].get<std::string>();
        item.name = entry["name"].get<std::string>();
        if (item.id.empty() || item.name.empty() ||
            !item_ids.insert(item.id).second) {
            throw std::invalid_argument("Empty or duplicate finished item id/name");
        }

        for (std::size_t i = 0; i < 2; ++i) {
            if (!entry["recipe_components"][i].is_string()) {
                throw std::invalid_argument("Recipe component IDs must be strings");
            }
            item.recipe_components[i] = entry["recipe_components"][i].get<std::string>();
            if (!component_ids.contains(item.recipe_components[i])) {
                throw std::invalid_argument("Recipe references an unknown component: " +
                                            item.recipe_components[i]);
            }
        }

        const auto a = item.recipe_components[0];
        const auto b = item.recipe_components[1];
        const auto recipe_key = a < b ? a + "\x1f" + b : b + "\x1f" + a;
        if (!recipes.insert(recipe_key).second) {
            throw std::invalid_argument("Duplicate item recipe in catalog");
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
        if (entry.contains("combat_effects")) {
            item.combat_effects = parse_effects(entry["combat_effects"]);
        }
        catalog.items.push_back(std::move(item));
    }

    // Reuse the engine's validation for duplicate IDs/recipes as a final guard.
    std::vector<std::string> component_id_list;
    component_id_list.reserve(catalog.components.size());
    for (const auto& component : catalog.components) component_id_list.push_back(component.first);
    (void)ItemEngine(catalog.items, std::move(component_id_list));
    return catalog;
}

} // namespace tft::items
