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
    const auto brawler = milestones.find("DA_18_Brawler");
    assert(brawler != milestones.end());
    assert((brawler->second == std::vector<int>{2, 4, 6}));

    const auto blackthorn = milestones.find("DA_18_Blackthorn");
    assert(blackthorn != milestones.end());
    assert((blackthorn->second == std::vector<int>{2, 4, 6}));

    // Localized names are not used as canonical keys; API names remain usable.
    assert(milestones.find("DA_18_Summoner") != milestones.end());
    assert(milestones.find("Lutador") == milestones.end());

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
              << " trait identifiers with real Set 18 milestones\n";
    return 0;
}
