#include "strategy/PivotFeasibilityEvaluator.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;

static PivotFeasibilityInput viable_input() {
    PivotFeasibilityInput input;
    input.candidate_composition_identity = "comp-next";
    input.source_direction_anchor_identity = "direction-current";
    input.source_composition_version = 7;
    input.gold_available = 40;
    input.protected_gold_floor = 20;
    input.transition_economic_cost = 12.0;
    input.required_units = {
        {1, 4, true, true, {"Invoker", "Arcanist"}},
        {2, 3, true, false, {"Invoker"}},
        {3, 2, false, false, {"Arcanist"}}
    };
    input.observed_units = {
        {1, 1, 1, 1, 8},
        {2, 1, 1, 0, 7},
        {3, 0, 1, 1, 9}
    };
    input.required_traits = {
        {"Invoker", 2},
        {"Arcanist", 2}
    };
    return input;
}

int main() {
    PivotFeasibilityEvaluator evaluator;

    {
        const auto result = evaluator.evaluate(viable_input());
        assert(result.shadow_only);
        assert(result.status == PivotFeasibilityStatus::Viable);
        assert(result.carry_eligible); // 4-cost carry is eligible, not automatic approval.
        assert(result.score > 49.0);
        assert(!result.favorable_evidence.empty());
    }

    {
        auto input = viable_input();
        input.required_units[0].cost = 2;
        input.observed_units[0].star = 1;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::Rejected);
        assert(!result.carry_eligible);
        assert(!result.blockers.empty());
    }

    {
        auto input = viable_input();
        input.observed_units[0].shop_copies = 0;
        input.observed_units[0].owned_copies = 0;
        input.observed_units[0].pool_remaining = -1;
        // Keep remaining owned/shop evidence sufficient for trait gates so this
        // case isolates unknown carry availability rather than trait failure.
        input.required_traits[0].minimum_units = 1;
        input.required_traits[1].minimum_units = 1;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::InsufficientEvidence);
        assert(!result.missing_data.empty());
        assert(result.status != PivotFeasibilityStatus::Viable);
    }

    {
        auto input = viable_input();
        // Zero pool means unavailable only when no copies are already owned
        // and none are currently offered in the shop.
        input.observed_units[0].owned_copies = 0;
        input.observed_units[0].shop_copies = 0;
        input.observed_units[0].pool_remaining = 0;
        input.required_traits[0].minimum_units = 1;
        input.required_traits[1].minimum_units = 1;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::Rejected);
        assert(!result.blockers.empty());
    }

    {
        auto input = viable_input();
        input.required_traits[0].minimum_units = 3;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::Rejected);
        assert(!result.blockers.empty());
    }

    {
        auto input = viable_input();
        input.protected_gold_floor = 35;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::Rejected);
        assert(result.reason == "candidate_has_explicit_feasibility_blockers");
    }

    {
        auto input = viable_input();
        input.transition_economic_cost = -1.0;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::InsufficientEvidence);
        assert(!result.missing_data.empty());
    }

    {
        auto input = viable_input();
        // One required trait member is neither observed nor known to be absent
        // from the pool. This must remain unknown, not become a false rejection.
        input.observed_units[2].pool_remaining = -1;
        input.observed_units[2].owned_copies = 0;
        input.observed_units[2].shop_copies = 0;
        input.required_traits = {{"Arcanist", 2}};
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::InsufficientEvidence);
        assert(std::find(result.missing_data.begin(), result.missing_data.end(),
            "trait_reachability_unknown_Arcanist") != result.missing_data.end());
        assert(std::find(result.blockers.begin(), result.blockers.end(),
            "trait_not_reachable_Arcanist") == result.blockers.end());
    }

    {
        const auto input = viable_input();
        const auto result = evaluator.evaluate(input);
        assert(result.candidate_composition_identity == input.candidate_composition_identity);
        assert(result.source_direction_anchor_identity == input.source_direction_anchor_identity);
        assert(result.source_composition_version == input.source_composition_version);
    }

    {
        auto input = viable_input();
        input.source_composition_version = 0;
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::InsufficientEvidence);
    }

    {
        auto input = viable_input();
        input.observed_units.push_back(input.observed_units.front());
        const auto result = evaluator.evaluate(input);
        assert(result.status == PivotFeasibilityStatus::Rejected);
    }

    std::cout << "Pivot feasibility evidence tests passed\n";
    return 0;
}
