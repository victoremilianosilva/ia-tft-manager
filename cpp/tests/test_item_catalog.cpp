#include "items/ItemCatalog.hpp"

#include <fstream>
#include <iostream>
#include <set>
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
        if (catalog.components.empty()) {
            std::cerr << "active item catalog contains no components\n";
            return 4;
        }
        if (catalog.items.empty()) {
            std::cerr << "active item catalog contains no craftable items\n";
            return 5;
        }

        std::set<std::string> component_ids;
        for (const auto& component : catalog.components) {
            if (component.first.empty() ||
                !component_ids.insert(component.first).second) {
                std::cerr << "empty or duplicate component identifier\n";
                return 6;
            }
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

        std::cout << "Loaded active item catalog: "
                  << component_ids.size() << " components, "
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