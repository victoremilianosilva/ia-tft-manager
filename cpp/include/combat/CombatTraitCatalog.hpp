#pragma once

#include "combat/CombatInput.hpp"

#include <nlohmann/json.hpp>

#include <algorithm>
#include <cmath>
#include <istream>
#include <map>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

namespace tft::combat {

struct TraitCombatTier {
    int min_units{0};
    std::vector<CombatEffectDefinition> effects;
};

struct TraitCombatDefinition {
    std::string api_name;
    bool effects_complete{false};
    std::vector<TraitCombatTier> tiers;
};

struct TraitCombatCatalog {
    std::string set_id;
    std::map<std::string, TraitCombatDefinition> traits;
};

inline TraitCombatCatalog load_trait_combat_catalog(std::istream& input) {
    using Json = nlohmann::json;
    const auto root = Json::parse(input);
    if (!root.is_object() || root.value("schema_version", 0) != 1 ||
        !root.contains("set_id") || !root["set_id"].is_string() ||
        !root.contains("traits") || !root["traits"].is_array()) {
        throw std::invalid_argument("Invalid trait combat catalog root/schema");
    }

    TraitCombatCatalog catalog;
    catalog.set_id = root["set_id"].get<std::string>();
    if (catalog.set_id.empty()) throw std::invalid_argument("Trait catalog set_id is empty");

    for (const auto& raw_trait : root["traits"]) {
        if (!raw_trait.is_object() || !raw_trait.contains("api_name") ||
            !raw_trait["api_name"].is_string() ||
            !raw_trait.contains("effects_complete") ||
            !raw_trait["effects_complete"].is_boolean() ||
            !raw_trait.contains("tiers") || !raw_trait["tiers"].is_array()) {
            throw std::invalid_argument("Trait entry requires api_name, effects_complete and tiers");
        }

        TraitCombatDefinition definition;
        definition.api_name = raw_trait["api_name"].get<std::string>();
        definition.effects_complete = raw_trait["effects_complete"].get<bool>();
        if (definition.api_name.empty() || catalog.traits.contains(definition.api_name))
            throw std::invalid_argument("Empty or duplicate trait combat api_name");

        int previous_min_units = 0;
        for (const auto& raw_tier : raw_trait["tiers"]) {
            if (!raw_tier.is_object() || !raw_tier.contains("min_units") ||
                !raw_tier["min_units"].is_number_integer() ||
                raw_tier["min_units"].get<int>() <= previous_min_units ||
                !raw_tier.contains("effects") || !raw_tier["effects"].is_array()) {
                throw std::invalid_argument("Trait tiers require increasing min_units and effects");
            }
            TraitCombatTier tier;
            tier.min_units = raw_tier["min_units"].get<int>();
            previous_min_units = tier.min_units;

            for (const auto& raw_effect : raw_tier["effects"]) {
                if (!raw_effect.is_object() ||
                    !raw_effect.contains("trigger") || !raw_effect["trigger"].is_string() ||
                    !raw_effect.contains("operation") || !raw_effect["operation"].is_string()) {
                    throw std::invalid_argument("Trait combat effect requires trigger and operation");
                }
                CombatEffectDefinition effect;
                effect.trigger = raw_effect["trigger"].get<std::string>();
                effect.operation = raw_effect["operation"].get<std::string>();
                const auto read_string = [&](const char* key, std::string& value) {
                    if (!raw_effect.contains(key)) return;
                    if (!raw_effect[key].is_string())
                        throw std::invalid_argument(std::string("Trait effect field must be string: ") + key);
                    value = raw_effect[key].get<std::string>();
                };
                read_string("stat", effect.stat);
                read_string("target", effect.target);
                read_string("condition", effect.condition);
                read_string("condition_trait", effect.condition_trait);

                const auto read_number = [&](const char* key, float& value) {
                    if (!raw_effect.contains(key)) return;
                    if (!raw_effect[key].is_number())
                        throw std::invalid_argument(std::string("Trait effect field must be numeric: ") + key);
                    const auto parsed = raw_effect[key].get<double>();
                    if (!std::isfinite(parsed) ||
                        std::abs(parsed) > static_cast<double>(std::numeric_limits<float>::max()))
                        throw std::invalid_argument(std::string("Invalid trait effect value: ") + key);
                    value = static_cast<float>(parsed);
                };
                read_number("value", effect.value);
                read_number("duration", effect.duration);
                read_number("interval", effect.interval);
                read_number("delay", effect.delay);
                read_number("health_threshold", effect.health_threshold);
                read_number("critical_value", effect.critical_value);
                read_number("max_amount", effect.max_amount);
                if (raw_effect.contains("max_stacks")) {
                    if (!raw_effect["max_stacks"].is_number_integer() ||
                        raw_effect["max_stacks"].get<int>() <= 0)
                        throw std::invalid_argument("Trait effect max_stacks must be a positive integer");
                    effect.max_stacks = raw_effect["max_stacks"].get<int>();
                }

                const auto read_bool = [&](const char* key, bool& value) {
                    if (!raw_effect.contains(key)) return;
                    if (!raw_effect[key].is_boolean())
                        throw std::invalid_argument(std::string("Trait effect field must be boolean: ") + key);
                    value = raw_effect[key].get<bool>();
                };
                read_bool("percent_of_stat", effect.percent_of_stat);
                read_bool("percent_of_max_health", effect.percent_of_max_health);
                read_bool("scale_by_active_trait_count", effect.scale_by_active_trait_count);
                read_bool("scale_by_base_stat", effect.scale_by_base_stat);

                const bool valid_stat = effect.stat == "attack_damage" ||
                    effect.stat == "critical_strike_chance" ||
                    effect.stat == "attack_speed" || effect.stat == "ability_power" ||
                    effect.stat == "armor" || effect.stat == "magic_resist" ||
                    effect.stat == "omnivamp" || effect.stat == "damage_amplification" ||
                    effect.stat == "damage_reduction" || effect.stat == "max_hp";
                const bool valid_condition = effect.condition == "has_trait" ||
                    effect.condition == "trait_count_at_least";
                const bool valid_trigger = effect.trigger == "combat_start" ||
                    effect.trigger == "on_attack" || effect.trigger == "on_kill" ||
                    effect.trigger == "after_delay" || effect.trigger == "while_hp_below" ||
                    effect.trigger == "while_hp_above" || effect.trigger == "on_ally_shield" ||
                    effect.trigger == "periodic" || effect.trigger.empty();
                const bool valid_add_stat = effect.operation == "add_stat" && valid_stat &&
                    (effect.trigger == "combat_start" || effect.trigger == "after_delay" ||
                     effect.trigger == "while_hp_below" || effect.trigger == "while_hp_above" ||
                     effect.trigger == "on_ally_shield" || effect.trigger == "periodic");
                const bool valid_mana_regen = effect.operation == "mana_regen" &&
                    (effect.trigger.empty() || effect.trigger == "combat_start") &&
                    (effect.target.empty() || effect.target == "self" || effect.target == "allies");
                const bool valid_bonus_damage = effect.operation == "bonus_damage" &&
                    effect.trigger == "on_attack";
                const bool valid_heal =
                    ((effect.operation == "heal_max_hp_pct" &&
                      (effect.trigger == "on_kill" || effect.trigger == "on_attack" ||
                       effect.trigger == "periodic")) ||
                     (effect.operation == "heal_missing_hp_pct" &&
                      effect.trigger == "periodic"));
                const bool valid_charges = effect.operation == "grant_charges" &&
                    effect.trigger == "on_kill";
                if (!valid_trigger || !(valid_add_stat || valid_mana_regen ||
                    valid_bonus_damage || valid_heal || valid_charges) ||
                    (effect.target != "" && effect.target != "self" &&
                     effect.target != "allies" && effect.target != "allies_same_row_within_1") ||
                    (!effect.condition.empty() && !valid_condition) ||
                    ((effect.condition == "has_trait" ||
                      effect.condition == "trait_count_at_least") &&
                     effect.condition_trait != definition.api_name)) {
                    throw std::invalid_argument("Unsupported or incomplete trait combat effect contract");
                }
                if (effect.condition == "trait_count_at_least")
                    effect.min_trait_count = tier.min_units;
                if (effect.trigger == "periodic" &&
                    (!std::isfinite(effect.interval) || effect.interval <= 0.0f))
                    throw std::invalid_argument("Periodic trait effect requires a positive interval");
                if (effect.operation == "heal_missing_hp_pct" &&
                    (!std::isfinite(effect.max_amount) || effect.max_amount <= 0.0f))
                    throw std::invalid_argument(
                        "Missing-health trait healing requires a positive max_amount");
                tier.effects.push_back(std::move(effect));
            }
            definition.tiers.push_back(std::move(tier));
        }
        if (definition.effects_complete && definition.tiers.empty())
            throw std::invalid_argument("Complete trait combat metadata requires at least one tier");
        catalog.traits.emplace(definition.api_name, std::move(definition));
    }
    return catalog;
}

inline void apply_trait_combat_metadata(
    CombatTrait& trait, const TraitCombatCatalog& catalog
) {
    trait.effects.clear();
    trait.effects_complete = false;
    if (!trait.active || trait.active_count <= 0) return;

    const auto found = catalog.traits.find(trait.api_name);
    if (found == catalog.traits.end()) return;

    const TraitCombatTier* selected = nullptr;
    for (const auto& tier : found->second.tiers) {
        if (tier.min_units <= trait.active_count) selected = &tier;
        else break;
    }
    if (!selected) return;
    trait.effects = selected->effects;
    trait.effects_complete = found->second.effects_complete;
}

} // namespace tft::combat
