#include "strategy/CompositionPlanner.hpp"

#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using tft::ChampionDefinition;
using tft::strategy::CompositionPlanner;

static ChampionDefinition champion(int id, const char* name, int role,
                                  std::vector<std::string> traits, int cost = 2) {
    ChampionDefinition value;
    value.internal_id = id;
    value.api_name = name;
    value.name = name;
    value.cost = cost;
    value.role = role;
    value.combat_profile.role = role;
    value.traits = std::move(traits);
    return value;
}

int main() {
    // A Vanguard direction must not force an all-Vanguard lineup. The only
    // carry is connected to Vanguard through Arcanist, so the planner should
    // retain the direction while planning a real carry and complementary traits.
    std::vector<ChampionDefinition> pool{
        champion(1, "VanguardTank", 0, {"Vanguard", "Arcanist"}),
        champion(2, "SecondTank", 0, {"Vanguard", "Defender"}),
        champion(3, "MorganaCarry", 1, {"Arcanist", "Mystic"}, 3),
        champion(4, "ArcanistSupport", 2, {"Arcanist", "Mystic"}),
        champion(5, "FlexibleFighter", 3, {"Vanguard", "Mystic"}),
        champion(6, "OffTraitSupport", 2, {"Scholar", "Mystic"})
    };
    CompositionPlanner::TraitMilestones milestones{
        {"Vanguard", {2, 4, 6}},
        {"Arcanist", {2, 4, 6}},
        {"Mystic", {2, 3, 4}},
        {"Defender", {2, 4}},
        {"Scholar", {2, 4}}
    };
    CompositionPlanner::OwnedCopies owned{{1, 1}, {3, 2}};
    CompositionPlanner::FocusWeights focus{{"Vanguard", 5.0}, {"Arcanist", 3.0}};

    const auto plan = CompositionPlanner::build(
        pool, milestones, "Vanguard", focus, owned, 5);

    assert(plan.unit_ids.size() == 5);
    assert(plan.unit_ids.size() == plan.unit_names.size());
    assert(plan.main_carry_id == 3);
    assert(std::find(plan.unit_ids.begin(), plan.unit_ids.end(), 3) != plan.unit_ids.end());
    assert(std::find(plan.core_traits.begin(), plan.core_traits.end(), "Vanguard")
           != plan.core_traits.end());

    // The planned lineup is flexible: it includes units outside the direction
    // to supply damage/support rather than spending every slot on one trait.
    assert(std::any_of(plan.unit_ids.begin(), plan.unit_ids.end(), [&](int id) {
        const auto it = std::find_if(pool.begin(), pool.end(),
            [id](const ChampionDefinition& c) { return c.internal_id == id; });
        return it != pool.end() &&
            std::find(it->traits.begin(), it->traits.end(), "Vanguard") == it->traits.end();
    }));

    auto ids = plan.unit_ids;
    std::sort(ids.begin(), ids.end());
    assert(std::adjacent_find(ids.begin(), ids.end()) == ids.end());

    // With no direction, no empty-string trait should be fabricated.
    const auto open_plan = CompositionPlanner::build(pool, milestones, "", {}, {}, 4);
    assert(open_plan.unit_ids.size() == 4);
    assert(std::find(open_plan.core_traits.begin(), open_plan.core_traits.end(), "")
           == open_plan.core_traits.end());

    std::cout << "flexible composition planner tests passed\n";
    return 0;
}
