#include "items/ItemCatalog.hpp"

#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: test_item_catalog <catalog.json>\n";
        return 2;
    }

    std::ifstream input(argv[1]);
    if (!input) {
        std::cerr << "could not open active item catalog: " << argv[1] << '\n';
        return 3;
    }

    try {
        const auto catalog = tft::items::load_item_catalog(input);

        // Completeness is explicit: an empty effect list is not proof that
        // every combat passive was modeled. Exercise both asserted and
        // malformed metadata through the same production loader.
        std::stringstream complete_metadata(R"json({
            "schema_version": 1,
            "set_id": "fixture",
            "components": [
                {"id": "A", "name": "Component A"},
                {"id": "B", "name": "Component B"}
            ],
            "items": [{
                "id": "fixture_item",
                "name": "Fixture Item",
                "recipe_components": ["A", "B"],
                "stats": {"attack_damage": 10},
                "combat_effects": [],
                "combat_effects_complete": true
            }]
        })json");
        const auto complete_catalog =
            tft::items::load_item_catalog(complete_metadata);
        if (complete_catalog.items.size() != 1 ||
            !complete_catalog.items.front().combat_effects_complete ||
            !complete_catalog.items.front().combat_effects.empty()) {
            std::cerr << "explicit complete empty effect metadata was not preserved\\n";
            return 13;
        }

        std::stringstream malformed_metadata(R"json({
            "schema_version": 1,
            "set_id": "fixture",
            "components": [
                {"id": "A", "name": "Component A"},
                {"id": "B", "name": "Component B"}
            ],
            "items": [{
                "id": "fixture_item",
                "name": "Fixture Item",
                "recipe_components": ["A", "B"],
                "stats": {"attack_damage": 10},
                "combat_effects": [],
                "combat_effects_complete": "true"
            }]
        })json");
        bool rejected_malformed_completeness = false;
        try {
            (void)tft::items::load_item_catalog(malformed_metadata);
        } catch (const std::invalid_argument&) {
            rejected_malformed_completeness = true;
        }
        if (!rejected_malformed_completeness) {
            std::cerr << "non-boolean combat_effects_complete metadata was accepted\\n";
            return 14;
        }
        if (catalog.components.empty()) {
            std::cerr << "active item catalog contains no components\n";
            return 4;
        }
        if (catalog.items.empty()) {
            std::cerr << "active item catalog contains no craftable items\n";
            return 5;
        }

        // Static max-health passives are represented by generic catalog
        // effects, not by item-name branches in CombatEngine.
        for (const auto& expected : {
                 std::pair<const char*, float>{"TFT_Item_WarmogsArmor", 0.18f},
                 std::pair<const char*, float>{"TFT_Item_DragonsClaw", 0.06f},
                 std::pair<const char*, float>{"TFT_Item_BrambleVest", 0.06f},
                 std::pair<const char*, float>{"TFT_Item_RedBuff", 0.08f}}) {
            const auto found = std::find_if(catalog.items.begin(), catalog.items.end(),
                [&](const auto& item) { return item.id == expected.first; });
            if (found == catalog.items.end() || found->combat_effects_complete ||
                std::none_of(found->combat_effects.begin(), found->combat_effects.end(),
                    [&](const auto& effect) {
                        return effect.trigger == "combat_start" &&
                            effect.operation == "add_stat" &&
                            effect.stat == "max_hp" && effect.percent_of_stat &&
                            std::abs(effect.value - expected.second) < 0.0001f;
                    })) {
                std::cerr << "generic max-health effect missing or falsely complete for "
                          << expected.first << '\n';
                return 15;
            }
        }

        for (const auto& expected : {
                 std::pair<const char*, float>{"TFT_Item_Deathblade", 0.10f},
                 std::pair<const char*, float>{"TFT_Item_RabadonsDeathcap", 0.15f}}) {
            const auto found = std::find_if(catalog.items.begin(), catalog.items.end(),
                [&](const auto& item) { return item.id == expected.first; });
            if (found == catalog.items.end() || found->combat_effects_complete ||
                std::none_of(found->combat_effects.begin(), found->combat_effects.end(),
                    [&](const auto& effect) {
                        return effect.trigger == "combat_start" &&
                            effect.operation == "add_stat" &&
                            effect.stat == "damage_amplification" &&
                            std::abs(effect.value - expected.second) < 0.0001f;
                    })) {
                std::cerr << "generic damage amplification effect missing or falsely complete for "
                          << expected.first << '\n';
                return 16;
            }
        }

        const auto adaptive_helm = std::find_if(
            catalog.items.begin(), catalog.items.end(),
            [](const auto& item) { return item.id == "TFT_Item_AdaptiveHelm"; });
        if (adaptive_helm == catalog.items.end() || adaptive_helm->combat_effects_complete) {
            std::cerr << "Adaptive Helm generic role effects are missing or falsely complete\n";
            return 18;
        }
        const auto has_role_effect = [&](const char* stat, const char* role,
                                         float value, bool percent) {
            return std::any_of(adaptive_helm->combat_effects.begin(),
                adaptive_helm->combat_effects.end(), [&](const auto& effect) {
                    return effect.trigger == "combat_start" &&
                        effect.operation == "add_stat" && effect.stat == stat &&
                        effect.condition == role && effect.target == "self" &&
                        effect.percent_of_stat == percent &&
                        std::abs(effect.value - value) < 0.0001f;
                });
        };
        if (!has_role_effect("armor", "role_tank", 30.0f, false) ||
            !has_role_effect("magic_resist", "role_tank", 30.0f, false) ||
            !has_role_effect("armor", "role_fighter", 30.0f, false) ||
            !has_role_effect("magic_resist", "role_fighter", 30.0f, false) ||
            !has_role_effect("attack_damage", "role_other", 0.10f, true) ||
            !has_role_effect("ability_power", "role_other", 0.10f, true)) {
            std::cerr << "Adaptive Helm role effects are incomplete\n";
            return 19;
        }

        const auto night_harvester = std::find_if(
            catalog.items.begin(), catalog.items.end(),
            [](const auto& item) { return item.id == "TFT_Item_NightHarvester"; });
        if (night_harvester == catalog.items.end() ||
            night_harvester->combat_effects_complete ||
            std::none_of(night_harvester->combat_effects.begin(),
                night_harvester->combat_effects.end(), [](const auto& effect) {
                    return effect.trigger == "while_hp_above" &&
                        effect.operation == "add_stat" &&
                        effect.stat == "damage_reduction" &&
                        std::abs(effect.health_threshold - 0.5f) < 0.0001f &&
                        std::abs(effect.value - 0.15f) < 0.0001f;
                })) {
            std::cerr << "Night Harvester conditional effect was not normalized\n";
            return 17;
        }

        std::set<std::string> component_ids;
        for (const auto& component : catalog.components) {
            if (component.first.empty() ||
                !component_ids.insert(component.first).second) {
                std::cerr << "empty or duplicate component identifier\n";
                return 6;
            }
        }

        if (catalog.pve_loot_components.size() != 8) {
            std::cerr << "active set must expose exactly eight ordinary PvE components; got "
                      << catalog.pve_loot_components.size() << '\\n';
            return 12;
        }
        std::set<std::string> item_ids;
        std::size_t crafted_items = 0;
        std::size_t trait_granting_items = 0;
        for (const auto& item : catalog.items) {
            if (item.id.empty() || !item_ids.insert(item.id).second) {
                std::cerr << "empty or duplicate item identifier\n";
                return 7;
            }
            const bool has_first_component = !item.recipe_components[0].empty();
            const bool has_second_component = !item.recipe_components[1].empty();
            if (has_first_component || has_second_component) {
                if (!has_first_component || !has_second_component) {
                    std::cerr << "craftable item must reference exactly two components: "
                              << item.id << '\n';
                    return 8;
                }
                for (const auto& component_id : item.recipe_components) {
                    if (component_ids.find(component_id) == component_ids.end()) {
                        std::cerr << "item recipe references unknown component "
                                  << component_id << " in " << item.id << '\n';
                        return 9;
                    }
                }
                ++crafted_items;
            }
            if (!item.grants_trait.empty()) {
                ++trait_granting_items;
            }
        }

        if (crafted_items == 0) {
            std::cerr << "active item catalog has no items with recipes\n";
            return 10;
        }

        for (const auto* player_scope_id : {
                 "TFT_Item_ForceOfNature",
                 "TFT_Item_TacticiansRing",
                 "TFT_Item_TacticiansScepter"}) {
            const auto found = std::find_if(
                catalog.items.begin(), catalog.items.end(),
                [&](const auto& item) { return item.id == player_scope_id; });
            if (found == catalog.items.end() || found->unit_equipable) {
                std::cerr << "player-scope item must not be unit equipment: "
                          << player_scope_id << '\\n';
                return 11;
            }
        }

        std::cout << "Loaded active item catalog: "
                  << component_ids.size() << " components (" << catalog.pve_loot_components.size() << " PvE-eligible), "
                  << item_ids.size() << " items, "
                  << crafted_items << " recipes, "
                  << trait_granting_items << " trait-granting items\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "active item catalog validation failed: "
                  << error.what() << '\n';
        return 1;
    }
}