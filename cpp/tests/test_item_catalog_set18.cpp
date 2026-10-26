#include "items/ItemCatalog.hpp"

#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: test_item_catalog_set18 <catalog.json>\n";
        return 2;
    }

    std::ifstream input(argv[1]);
    if (!input) {
        std::cerr << "could not open Set 18 item catalog: " << argv[1] << '\n';
        return 3;
    }

    try {
        const auto catalog = tft::items::load_item_catalog(input);
        if (catalog.set_id != "Set18") {
            std::cerr << "unexpected set_id: " << catalog.set_id << '\n';
            return 4;
        }
        if (catalog.components.size() != 10) {
            std::cerr << "expected 10 Set 18 components, got "
                      << catalog.components.size() << '\n';
            return 5;
        }
        if (catalog.items.size() != 55) {
            std::cerr << "expected 55 Set 18 craftable items, got "
                      << catalog.items.size() << '\n';
            return 6;
        }

        for (const auto& component : catalog.components) {
            if (component.first.rfind("DA_Component_", 0) != 0) {
                std::cerr << "non-DA component in Set 18 catalog: "
                          << component.first << '\n';
                return 7;
            }
        }

        int emblems_with_traits = 0;
        for (const auto& item : catalog.items) {
            if (item.id.rfind("DA_", 0) != 0) {
                std::cerr << "non-DA item in Set 18 catalog: " << item.id << '\n';
                return 8;
            }
            for (const auto& component_id : item.recipe_components) {
                if (component_id.rfind("DA_Component_", 0) != 0) {
                    std::cerr << "recipe uses non-DA component: " << component_id
                              << " in " << item.id << '\n';
                    return 9;
                }
            }
            if (item.id.find("Emblem") != std::string::npos &&
                !item.grants_trait.empty()) {
                ++emblems_with_traits;
            }
        }
        if (emblems_with_traits != 16) {
            std::cerr << "expected 16 Set 18 emblems with trait metadata, got "
                      << emblems_with_traits << '\n';
            return 10;
        }

        std::cout << "Loaded " << catalog.set_id << ": "
                  << catalog.components.size() << " DA_ components, "
                  << catalog.items.size() << " DA_ craftable items, "
                  << emblems_with_traits << " trait emblems\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "Set 18 item catalog validation failed: "
                  << error.what() << '\n';
        return 1;
    }
}
