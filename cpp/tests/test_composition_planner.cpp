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
    // The planner should know the full level-8 core before the player reaches
    // level 8, then add flexible slots at levels 9 and 10.
    for (int level = 1; level <= 8; ++level)
        assert(CompositionPlanner::target_slots_for_level(level) == 8);
    assert(CompositionPlanner::target_slots_for_level(9) == 9);
    assert(CompositionPlanner::target_slots_for_level(10) == 10);
    assert(CompositionPlanner::target_slots_for_level(11) == 10);

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

    // At level 6, an unowned cost-1 carry with only a few copies left
    // should lose to an obtainable cost-3 carry, even when its trait fit is high.
    std::vector<ChampionDefinition> acquisition_pool{
        champion(11, "MissingCheapCarry", 1, {"Replicator"}, 1),
        champion(12, "ObtainableCarry", 1, {"Replicator"}, 3),
        champion(13, "Frontline", 0, {"Replicator"}, 2),
        champion(14, "Support", 2, {"Mystic"}, 2),
        champion(15, "OtherCheapUnit", 3, {"Scholar"}, 1)
    };
    CompositionPlanner::OwnedCopies none_owned;
    CompositionPlanner::AvailableCopies availability{
        {11, 1}, {12, 9}, {13, 9}, {14, 9}, {15, 99}
    };
    const auto viable_plan = CompositionPlanner::build(
        acquisition_pool, {{"Replicator", {2, 4, 6}}}, "Replicator",
        {{"Replicator", 5.0}}, none_owned, 4, 6, availability);
    assert(viable_plan.main_carry_id == 12);
    assert(std::find(viable_plan.unit_ids.begin(), viable_plan.unit_ids.end(), 11)
           == viable_plan.unit_ids.end());
    assert(std::any_of(viable_plan.acquisition_notes.begin(), viable_plan.acquisition_notes.end(),
        [](const std::string& note) { return note.find("ObtainableCarry") != std::string::npos; }));

    // With no direction, no empty-string trait should be fabricated.
    const auto open_plan = CompositionPlanner::build(pool, milestones, "", {}, {}, 4);
    assert(open_plan.unit_ids.size() == 4);
    assert(std::find(open_plan.core_traits.begin(), open_plan.core_traits.end(), "")
           == open_plan.core_traits.end());

    std::cout << "flexible composition planner tests passed\n";
    return 0;
}
