#pragma once

#include <algorithm>
#include <array>
#include <cstddef>
#include <cstdint>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

namespace tft::items {

// Set 18 PvE loot rows, as published for patch 18.5.
// Percentages are normalized by discrete_distribution because the source
// rounds some rows (stage 3/4 totals are slightly above 100%).
struct PveLootOutcome {
    unsigned components;
    unsigned gray_orbs;
    unsigned blue_orbs;
    unsigned gold_orbs;
    unsigned prismatic_orbs;
};

struct WeightedPveLoot {
    double weight;
    PveLootOutcome outcome;
};

inline const std::vector<WeightedPveLoot>& set18_pve_loot_table(unsigned stage) {
    static const std::vector<WeightedPveLoot> stage1{
        {35,{3,3,0,0,0}}, {35,{3,0,1,0,0}},
        {8,{2,3,1,0,0}}, {8,{2,0,2,0,0}},
        {3,{5,3,0,0,0}}, {3,{5,0,1,0,0}},
        {3,{4,0,1,0,0}}, {2,{3,0,2,0,0}},
        {2,{1,3,2,0,0}}, {1,{3,5,0,0,0}}
    };
    static const std::vector<WeightedPveLoot> stage2{
        {20,{3,1,0,0,0}}, {17,{2,1,0,0,0}},
        {17,{2,0,1,0,0}}, {15,{3,0,1,0,0}},
        {13,{2,2,0,0,0}}, {5,{3,3,0,0,0}},
        {4,{2,1,0,1,0}}, {4,{2,1,1,0,0}},
        {4,{2,0,2,0,0}}, {1,{2,0,1,1,0}}
    };
    static const std::vector<WeightedPveLoot> stage3{
        {20,{4,1,0,0,0}}, {20,{4,2,0,0,0}},
        {17,{3,1,1,0,0}}, {13,{3,3,0,0,0}},
        {13,{3,0,2,0,0}}, {5,{4,0,1,0,0}},
        {4,{5,1,0,0,0}}, {3,{3,1,0,1,0}},
        {2,{3,1,0,0,1}}, {2,{2,0,2,0,0}},
        {1,{3,0,1,1,0}}, {0.25,{4,1,0,1,0}}
    };
    static const std::vector<WeightedPveLoot> stage4{
        {18,{3,2,0,0,0}}, {18,{3,1,1,0,0}},
        {18,{2,2,1,0,0}}, {15,{4,1,0,0,0}},
        {13,{3,3,0,0,0}}, {5,{5,1,0,0,0}},
        {4,{4,1,1,0,0}}, {4,{3,1,0,1,0}},
        {3,{2,0,2,0,0}}, {2,{2,2,0,0,1}},
        {1,{3,0,2,1,0}}, {0.03,{2,0,0,1,1}}
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

// Personal component pool: one copy of each component initially, then one
// additional copy of each before stages 2, 3 and 4. Augment/carousel components
// must not be inserted here because they do not consume this PvE pool.
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
