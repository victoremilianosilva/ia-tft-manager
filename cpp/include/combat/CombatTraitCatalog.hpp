#pragma once

#include "combat/CombatInput.hpp"

#include <nlohmann/json.hpp>

#include <algorithm>
#include <cmath>
#include <istream>
#include <map>
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
                read_number("health_threshold", effect.health_threshold);

                if (raw_effect.contains("percent_of_stat")) {
                    if (!raw_effect["percent_of_stat"].is_boolean())
                        throw std::invalid_argument("Trait effect percent_of_stat must be boolean");
                    effect.percent_of_stat = raw_effect["percent_of_stat"].get<bool>();
                }
                if (raw_effect.contains("scale_by_active_trait_count")) {
                    if (!raw_effect["scale_by_active_trait_count"].is_boolean())
                        throw std::invalid_argument("Trait effect scale_by_active_trait_count must be boolean");
                    effect.scale_by_active_trait_count =
                        raw_effect["scale_by_active_trait_count"].get<bool>();
                }

                const bool valid_stat = effect.stat == "attack_damage" ||
                    effect.stat == "attack_speed" || effect.stat == "ability_power" ||
                    effect.stat == "armor" || effect.stat == "magic_resist" ||
                    effect.stat == "omnivamp" || effect.stat == "damage_amplification" ||
                    effect.stat == "damage_reduction" || effect.stat == "max_hp";
                const bool valid_condition = effect.condition == "has_trait" ||
                    effect.condition == "trait_count_at_least";
                if (effect.trigger != "combat_start" || effect.operation != "add_stat" ||
                    !valid_stat || (effect.target != "self" && effect.target != "allies") ||
                    !valid_condition || effect.condition_trait.empty() ||
                    effect.condition_trait != definition.api_name) {
                    throw std::invalid_argument("Unsupported or incomplete trait combat effect contract");
                }
                if (effect.condition == "trait_count_at_least") {
                    effect.min_trait_count = tier.min_units;
                }
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
