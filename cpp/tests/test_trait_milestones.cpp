#include "lobby/TraitMilestones.hpp"

#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>

int main(int argc, char** argv) {
    assert(argc == 2);
    std::ifstream input(argv[1]);
    assert(input && "could not open production traits catalog");

    const auto milestones = tft::load_trait_milestones(input);
    const auto shepherd = milestones.find("Shepherd");
    assert(shepherd != milestones.end());
    assert((shepherd->second == std::vector<int>{3, 5, 7}));

    const auto admin = milestones.find("Arbiter");
    assert(admin != milestones.end());
    assert(!admin->second.empty());

    // Localized names are not used as canonical keys; API names remain usable.
    assert(milestones.find("TFT17_SummonTrait") != milestones.end());
    assert(milestones.find("Pastor") == milestones.end());

    std::istringstream malformed("{not valid json");
    bool rejected = false;
    try {
        (void)tft::load_trait_milestones(malformed);
    } catch (const std::runtime_error&) {
        rejected = true;
    }
    assert(rejected);

    std::istringstream wrong_shape(R"({"traits":{}})");
    rejected = false;
    try {
        (void)tft::load_trait_milestones(wrong_shape);
    } catch (const std::runtime_error&) {
        rejected = true;
    }
    assert(rejected);

    std::cout << "Loaded " << milestones.size()
              << " trait identifiers with real Set 17 milestones\n";
    return 0;
}
