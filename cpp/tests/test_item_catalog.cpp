#include "items/ItemCatalog.hpp"

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

        std::cout << "Loaded " << catalog.set_id << ": "
                  << catalog.components.size() << " components, "
                  << catalog.items.size() << " craftable items\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "item catalog validation failed: " << error.what() << '\n';
        return 1;
    }
}
