#pragma once

#include <cstddef>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

namespace tft::items {

// Set 18 patch 18.5 weighted PvE component counts. Orb rewards are
// intentionally resolved as direct stage rewards by the lobby, never spawned.
struct PveLootOutcome {
    unsigned components;
};

struct WeightedPveLoot {
    double weight;
    PveLootOutcome outcome;
};

inline const std::vector<WeightedPveLoot>& set18_pve_loot_table(unsigned stage) {
    static const std::vector<WeightedPveLoot> stage1{
        {35,{3}}, {35,{3}}, {8,{2}}, {8,{2}}, {3,{5}},
        {3,{5}}, {3,{4}}, {2,{3}}, {2,{1}}, {1,{3}}
    };
    static const std::vector<WeightedPveLoot> stage2{
        {20,{3}}, {17,{2}}, {17,{2}}, {15,{3}}, {13,{2}},
        {5,{3}}, {4,{2}}, {4,{2}}, {4,{2}}, {1,{2}}
    };
    static const std::vector<WeightedPveLoot> stage3{
        {20,{4}}, {20,{4}}, {17,{3}}, {13,{3}}, {13,{3}},
        {5,{4}}, {4,{5}}, {3,{3}}, {2,{3}}, {2,{2}},
        {1,{3}}, {0.25,{4}}
    };
    static const std::vector<WeightedPveLoot> stage4{
        {18,{3}}, {18,{3}}, {18,{2}}, {15,{4}}, {13,{3}},
        {5,{5}}, {4,{4}}, {4,{3}}, {3,{2}}, {2,{2}},
        {1,{3}}, {0.03,{2}}
    };
    switch (stage) {
        case 1: return stage1;
        case 2: return stage2;
        case 3: return stage3;
        case 4: return stage4;
        default: throw std::out_of_range("Set 18 random component loot exists only through stage 4");
    }
}

template <class Rng>
inline PveLootOutcome roll_set18_pve_loot(unsigned stage, Rng& rng) {
    const auto& table = set18_pve_loot_table(stage);
    std::vector<double> weights;
    weights.reserve(table.size());
    for (const auto& row : table) weights.push_back(row.weight);
    std::discrete_distribution<std::size_t> choose(weights.begin(), weights.end());
    return table[choose(rng)].outcome;
}

// Per-player pool: one copy of each basic component initially, then one
// additional copy of each before stages 2, 3 and 4.
class Set18ComponentPool {
public:
    void initialize(const std::vector<std::string>& component_ids) {
        if (component_ids.size() != 8)
            throw std::invalid_argument("Set 18 requires exactly eight basic components");
        components_ = component_ids;
    }

    void add_stage_refresh(const std::vector<std::string>& component_ids) {
        if (component_ids.size() != 8)
            throw std::invalid_argument("Set 18 requires exactly eight basic components");
        components_.insert(components_.end(), component_ids.begin(), component_ids.end());
    }

    template <class Rng>
    std::string draw(Rng& rng) {
        if (components_.empty()) return {};
        std::uniform_int_distribution<std::size_t> pick(0, components_.size() - 1);
        const auto index = pick(rng);
        auto result = components_[index];
        components_.erase(components_.begin() + static_cast<std::ptrdiff_t>(index));
        return result;
    }

    std::size_t remaining() const noexcept { return components_.size(); }
    bool empty() const noexcept { return components_.empty(); }

private:
    std::vector<std::string> components_;
};

} // namespace tft::items
