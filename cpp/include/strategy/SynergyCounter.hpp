#pragma once

#include <cstdint>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace tft::strategy {

// Mirrors SynergyManager.update(): Python deduplicates by unit["id"].
// In the C++ catalog, that identifier is champion_internal_id, not UUID.
// Multiple copies of the same champion therefore contribute traits once.
using ChampionTraitEntry =
    std::pair<std::int32_t, std::vector<std::string>>;

inline std::unordered_map<std::string, int> count_unique_champion_traits(
    const std::vector<ChampionTraitEntry>& entries
) {
    std::unordered_map<std::string, int> counts;
    std::unordered_set<std::int32_t> seen;

    for (const auto& [champion_id, traits] : entries) {
        if (!seen.insert(champion_id).second) {
            continue;
        }

        for (const auto& trait : traits) {
            ++counts[trait];
        }
    }

    return counts;
}

} // namespace tft::strategy
