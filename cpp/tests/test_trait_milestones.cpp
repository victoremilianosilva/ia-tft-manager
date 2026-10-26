#include "lobby/TraitMilestones.hpp"

#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

int main(int argc, char** argv) {
    assert(argc == 2);
    std::ifstream input(argv[1]);
    assert(input && "could not open production traits catalog");

    const auto milestones = tft::load_trait_milestones(input);
    assert(!milestones.empty());

    // Validate catalog invariants without binding the test to any set's trait names
    // or milestone thresholds.
    for (const auto& [trait_id, thresholds] : milestones) {
        assert(!trait_id.empty());
        assert(!thresholds.empty());
        assert(std::all_of(thresholds.begin(), thresholds.end(),
                           [](int threshold) { return threshold > 0; }));
        assert(std::is_sorted(thresholds.begin(), thresholds.end()));
        assert(std::adjacent_find(thresholds.begin(), thresholds.end()) ==
               thresholds.end());
    }

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
              << " trait identifiers and validated their milestone sequences\n";
    return 0;
}
