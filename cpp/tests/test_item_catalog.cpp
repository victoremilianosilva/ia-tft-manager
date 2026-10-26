#include "items/ItemCatalog.hpp"
#include "items/CombatItemAdapter.hpp"

#include <algorithm>
#include <fstream>
#include <iostream>

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: test_item_catalog <catalog.json>\n";
        return 2;
    }

    std::ifstream input(argv[1]);
    if (!input) {
        std::cerr << "could not open item catalog: " << argv[1] << '\n';
        return 3;
    }

    try {
        const auto catalog = tft::items::load_item_catalog(input);
        if (catalog.set_id != "Set17") {
            std::cerr << "unexpected set_id: " << catalog.set_id << '\n';
            return 4;
        }
        if (catalog.components.size() != 10) {
            std::cerr << "expected 10 components, got " << catalog.components.size() << '\n';
            return 5;
        }
        if (catalog.items.size() != 55) {
            std::cerr << "expected 55 craftable items, got " << catalog.items.size() << '\n';
            return 6;
        }

        bool found_expected_item = false;
        for (const auto& item : catalog.items) {
            if (item.id == "TFT17_Item_ASTraitEmblemItem") {
                found_expected_item = true;
                if (item.recipe_components[0].empty() || item.recipe_components[1].empty()) {
                    std::cerr << "expected item has an incomplete recipe\n";
                    return 7;
                }
                break;
            }
        }
        if (!found_expected_item) {
            std::cerr << "expected Set17 item was not loaded\n";
            return 8;
        }

        bool found_data_driven_brawler = false;
        for (const auto& item : catalog.items) {
            if (item.id != "TFT17_Item_HPTankEmblemItem") continue;
            found_data_driven_brawler = true;
            if (item.grants_trait != "TFT17_HPTank" || item.combat_effects.empty() ||
                item.combat_effects.front().trigger != "on_attack" ||
                item.combat_effects.front().operation != "bonus_damage" ||
                item.combat_effects.front().damage_type != tft::DamageType::MAGIC ||
                !item.combat_effects.front().percent_of_max_health) {
                std::cerr << "Brawler emblem generic effect metadata was not loaded\n";
                return 9;
            }
            const auto combat_item = tft::items::to_combat_item(item);
            if (combat_item.grants_trait != item.grants_trait ||
                combat_item.effects.size() != item.combat_effects.size()) {
                std::cerr << "combat adapter dropped trait effect metadata\n";
                return 10;
            }
            break;
        }
        if (!found_data_driven_brawler) {
            std::cerr << "Brawler emblem was not loaded\n";
            return 11;
        }

        bool found_bastion_delay = false;
        bool found_rogue_threshold = false;
        for (const auto& item : catalog.items) {
            if (item.id == "TFT17_Item_ResistTankEmblemItem") {
                found_bastion_delay = std::find(item.deferred_stats.begin(),
                    item.deferred_stats.end(), "attack_speed") != item.deferred_stats.end() &&
                    std::any_of(item.combat_effects.begin(), item.combat_effects.end(),
                        [](const auto& effect) {
                            return effect.trigger == "after_delay" &&
                                effect.stat == "attack_speed" && effect.delay == 10.0f;
                        });
            }
            if (item.id == "TFT17_Item_AssassinTraitEmblemItem") {
                found_rogue_threshold = std::find(item.deferred_stats.begin(),
                    item.deferred_stats.end(), "omnivamp") != item.deferred_stats.end() &&
                    std::any_of(item.combat_effects.begin(), item.combat_effects.end(),
                        [](const auto& effect) {
                            return effect.trigger == "while_hp_below" &&
                                effect.stat == "omnivamp" &&
                                effect.health_threshold == 0.5f;
                        });
            }
        }
        if (!found_bastion_delay || !found_rogue_threshold) {
            std::cerr << "Delayed/conditional trait effects were not loaded\n";
            return 12;
        }

        std::cout << "Loaded " << catalog.set_id << ": "
                  << catalog.components.size() << " components, "
                  << catalog.items.size() << " craftable items\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "item catalog validation failed: " << error.what() << '\n';
        return 1;
    }
}
