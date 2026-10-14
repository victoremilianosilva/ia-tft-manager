#include "strategy/SynergyCounter.hpp"

#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

namespace {
void require(bool condition, const std::string& message) {
    if (!condition) {
        std::cerr << "[FAIL] " << message << '\n';
        std::exit(EXIT_FAILURE);
    }
}
}

int main() {
    using tft::strategy::ChampionTraitEntry;
    using tft::strategy::count_unique_champion_traits;

    // Same champion with different instance identities/stars is still
    // one unique unit for SynergyManager.update() compatibility.
    const std::vector<ChampionTraitEntry> board{
        {10, {"Mage", "Scholar"}},
        {10, {"Mage", "Scholar"}},
        {11, {"Mage", "Brawler"}},
        {12, {"Brawler"}}
    };

    const auto counts = count_unique_champion_traits(board);

    require(counts.at("Mage") == 2,
            "Repeated copies of one champion must not inflate Mage count.");
    require(counts.at("Scholar") == 1,
            "Traits from a repeated champion must be counted once.");
    require(counts.at("Brawler") == 2,
            "Distinct champions sharing a trait must both count.");
    require(counts.size() == 3,
            "Unexpected trait keys were produced.");

    std::cout << "[PASS] Unique champion synergy counting matches Python semantics.\n";
    return EXIT_SUCCESS;
}
