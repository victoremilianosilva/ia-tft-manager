#include "strategy/NativeStrategicCompositionGenerator.hpp"

#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <cmath>

using namespace tft::strategy;

int main() {
    NativeCompositionGenerationInput input;
    input.level = 6;
    input.gold = 20;
    input.target_slots = 4;
    input.maximum_candidates = 4;
    input.catalog = {
        {1, "BruiserTank", 2, {"Bruiser"}, false, true, false},
        {2, "BruiserCarry", 3, {"Bruiser"}, true, false, false},
        {3, "BruiserSupport", 2, {"Bruiser", "Invoker"}, false, false, true},
        {4, "InvokerCarry", 4, {"Invoker"}, true, false, false},
        {5, "InvokerFront", 3, {"Invoker"}, false, true, false},
        {6, "InvokerSupport", 2, {"Invoker"}, false, false, true},
        {7, "Unavailable", 5, {"Invoker"}, true, false, false}
    };
    input.owned = {
        {1, 2, 1, true, false, 0.8, 0.0},
        {2, 1, 1, false, true, 0.0, 0.6}
    };
    input.owned[0].copies_by_star[1] = 2;
    input.owned[1].copies_by_star[1] = 1;
    input.shop_ids = {4, 6};
    input.pool_remaining = {{1, 10}, {2, 8}, {3, 12}, {4, 5}, {5, 7}, {6, 9}, {7, 0}};
    input.trait_thresholds = {{"Bruiser", 2}, {"Invoker", 2}};
    input.currently_owned_unit_ids = {1, 2};

    const auto result = NativeStrategicCompositionGenerator{}.generate(input);
    assert(result.reason == "native_candidates_generated");
    assert(result.candidates.size() == 2);
    const auto bruiser = std::find_if(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) { return candidate.direction == "Bruiser"; });
    const auto invoker = std::find_if(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) { return candidate.direction == "Invoker"; });
    assert(bruiser != result.candidates.end());
    assert(invoker != result.candidates.end());
    assert(bruiser->identity.find("native:Bruiser:") == 0);
    assert(bruiser->main_carry_id == 2);
    assert(bruiser->reusable_owned_units >= 2);
    assert(std::any_of(bruiser->evidence.begin(), bruiser->evidence.end(),
        [](const auto& item) { return item == "owned_pair:1"; }));
    assert(std::any_of(bruiser->evidence.begin(), bruiser->evidence.end(),
        [](const auto& item) { return item == "item_fit:2"; }));
    auto mixed_tiers = input;
    mixed_tiers.owned[0].copies = 5; // One 2-star plus two 1-star instances.
    mixed_tiers.owned[0].star = 2;
    mixed_tiers.owned[0].copies_by_star = {};
    mixed_tiers.owned[0].copies_by_star[1] = 2;
    mixed_tiers.owned[0].copies_by_star[2] = 1;
    const auto mixed_result = NativeStrategicCompositionGenerator{}.generate(mixed_tiers);
    const auto mixed_bruiser = std::find_if(mixed_result.candidates.begin(),
        mixed_result.candidates.end(), [](const auto& candidate) {
            return candidate.direction == "Bruiser";
        });
    assert(mixed_bruiser != mixed_result.candidates.end());
    assert(std::find(mixed_bruiser->evidence.begin(), mixed_bruiser->evidence.end(),
        "owned_pair:1") == mixed_bruiser->evidence.end());

    mixed_tiers.owned[0].copies_by_star[1] = 3;
    const auto complete_three_star_progress =
        NativeStrategicCompositionGenerator{}.generate(mixed_tiers);
    const auto complete_bruiser = std::find_if(complete_three_star_progress.candidates.begin(),
        complete_three_star_progress.candidates.end(), [](const auto& candidate) {
            return candidate.direction == "Bruiser";
        });
    assert(complete_bruiser != complete_three_star_progress.candidates.end());
    assert(std::find(complete_bruiser->evidence.begin(), complete_bruiser->evidence.end(),
        "owned_pair:1") != complete_bruiser->evidence.end());

    assert(bruiser->transition_cost > 0.0 && bruiser->transition_cost < 1.0);
    assert(std::find(bruiser->completed_traits.begin(), bruiser->completed_traits.end(),
                     "Bruiser") != bruiser->completed_traits.end());
    assert(invoker->anchor_available_in_shop);
    assert(std::find(invoker->unit_ids.begin(), invoker->unit_ids.end(), 7) ==
           invoker->unit_ids.end());

    // Level controls target capacity, not the identity or source of strategy.
    auto lower_level = input;
    lower_level.level = 2;
    lower_level.target_slots = 8;
    const auto lower_level_result =
        NativeStrategicCompositionGenerator{}.generate(lower_level);
    assert(std::all_of(lower_level_result.candidates.begin(),
        lower_level_result.candidates.end(), [](const auto& candidate) {
            return candidate.unit_ids.size() <= 2;
        }));

    // Gold, star progress and item fit contribute to candidate estimates.
    auto poor_economy = input;
    poor_economy.gold = 0;
    const auto poor_economy_result =
        NativeStrategicCompositionGenerator{}.generate(poor_economy);
    const auto poor_invoker = std::find_if(
        poor_economy_result.candidates.begin(), poor_economy_result.candidates.end(),
        [](const auto& candidate) { return candidate.direction == "Invoker"; });
    assert(poor_invoker != poor_economy_result.candidates.end());
    assert(poor_invoker->score < invoker->score);

    auto upgraded = input;
    upgraded.owned[0].star = 2;
    upgraded.owned[0].copies_by_star = {};
    upgraded.owned[0].copies_by_star[2] = 1;
    const auto upgraded_result =
        NativeStrategicCompositionGenerator{}.generate(upgraded);
    const auto upgraded_bruiser = std::find_if(
        upgraded_result.candidates.begin(), upgraded_result.candidates.end(),
        [](const auto& candidate) { return candidate.direction == "Bruiser"; });
    assert(upgraded_bruiser != upgraded_result.candidates.end());
    assert(upgraded_bruiser->score > baseline_bruiser->score);

    auto without_items = input;
    without_items.owned[1].item_fit = 0.0;
    const auto without_items_result =
        NativeStrategicCompositionGenerator{}.generate(without_items);
    const auto no_item_bruiser = std::find_if(
        without_items_result.candidates.begin(), without_items_result.candidates.end(),
        [](const auto& candidate) { return candidate.direction == "Bruiser"; });
    assert(no_item_bruiser != without_items_result.candidates.end());
    assert(no_item_bruiser->score < bruiser->score);

    // Missing pool data is not interpreted as an exhausted pool.
    input.pool_remaining.erase(4);
    const auto missing_pool = NativeStrategicCompositionGenerator{}.generate(input);
    assert(std::any_of(missing_pool.candidates.begin(), missing_pool.candidates.end(),
        [](const auto& candidate) {
            return candidate.direction == "Invoker" &&
                std::find(candidate.unit_ids.begin(), candidate.unit_ids.end(), 4) !=
                    candidate.unit_ids.end();
        }));

    // A catalog without observed trait evidence cannot invent a direction.
    NativeCompositionGenerationInput empty;
    empty.catalog = input.catalog;
    const auto no_evidence = NativeStrategicCompositionGenerator{}.generate(empty);
    assert(no_evidence.candidates.empty());
    assert(no_evidence.reason == "no_candidate_from_observed_traits");

    // Candidate identity and ordering are deterministic for equivalent facts,
    // even when catalog and owned-unit input order changes.
    auto reordered = input;
    std::reverse(reordered.catalog.begin(), reordered.catalog.end());
    std::reverse(reordered.owned.begin(), reordered.owned.end());
    const auto reordered_result = NativeStrategicCompositionGenerator{}.generate(reordered);
    assert(reordered_result.candidates.size() == missing_pool.candidates.size());
    for (std::size_t index = 0; index < missing_pool.candidates.size(); ++index) {
        assert(reordered_result.candidates[index].identity == missing_pool.candidates[index].identity);
        assert(reordered_result.candidates[index].unit_ids == missing_pool.candidates[index].unit_ids);
        assert(reordered_result.candidates[index].direction == missing_pool.candidates[index].direction);
    }

    // Candidate caps are respected.
    auto capped = input;
    capped.maximum_candidates = 1;
    const auto capped_result = NativeStrategicCompositionGenerator{}.generate(capped);
    assert(capped_result.candidates.size() == 1);
    assert(capped_result.directions_considered == 1);

    // An exhausted pool excludes unowned, non-shop copies, but never erases
    // evidence for a unit already owned by the player.
    auto exhausted = input;
    exhausted.pool_remaining[3] = 0;
    exhausted.pool_remaining[4] = 0;
    exhausted.shop_ids.clear();
    const auto exhausted_result = NativeStrategicCompositionGenerator{}.generate(exhausted);
    for (const auto& candidate : exhausted_result.candidates) {
        assert(std::find(candidate.unit_ids.begin(), candidate.unit_ids.end(), 3) == candidate.unit_ids.end());
        assert(std::find(candidate.unit_ids.begin(), candidate.unit_ids.end(), 4) == candidate.unit_ids.end());
    }
    assert(std::any_of(exhausted_result.candidates.begin(), exhausted_result.candidates.end(),
        [](const auto& candidate) {
            return std::find(candidate.unit_ids.begin(), candidate.unit_ids.end(), 1) != candidate.unit_ids.end();
        }));

    // Malformed catalog rows and NaN owned evidence cannot poison scores.
    auto malformed = input;
    malformed.catalog.push_back({-1, "Invalid", 0, {"Bruiser"}, true, false, false});
    malformed.owned.push_back({99, 2, 1, true, false, 0.0,
        std::numeric_limits<double>::quiet_NaN()});
    const auto malformed_result = NativeStrategicCompositionGenerator{}.generate(malformed);
    assert(std::all_of(malformed_result.candidates.begin(), malformed_result.candidates.end(),
        [](const auto& candidate) {
            return std::isfinite(candidate.score) &&
                std::all_of(candidate.unit_ids.begin(), candidate.unit_ids.end(),
                    [](std::int32_t id) { return id >= 0; });
        }));

    // Snapshot-bound candidate sets carry an explicit player/round/sequence
    // envelope, and every proposal retains that exact provenance.
    auto correlated = input;
    correlated.match_id = 7001;
    correlated.player_id = 3;
    correlated.round = 5;
    correlated.sequence = 42;
    const auto correlated_result =
        NativeStrategicCompositionGenerator{}.generate(correlated);
    assert(correlated_result.reason == "native_candidates_generated");
    assert(correlated_result.candidate_set_id ==
        "native-candidate-set:v1:7001:3:5:42");
    assert(correlated_result.match_id == 7001);
    assert(correlated_result.player_id == 3);
    assert(correlated_result.round == 5);
    assert(correlated_result.source_sequence == 42);
    assert(!correlated_result.candidates.empty());
    for (const auto& candidate : correlated_result.candidates) {
        assert(candidate.candidate_set_id == correlated_result.candidate_set_id);
        assert(candidate.producer_id == "native-strategic-composition-generator");
        assert(candidate.match_id == 7001);
        assert(candidate.player_id == 3);
        assert(candidate.round == 5);
        assert(candidate.source_sequence == 42);
        assert(candidate.identity.find(candidate.candidate_set_id + ":") == 0);
    }

    // The same semantic alternatives from a later decision are a different
    // candidate set; candidate IDs cannot silently be reused across snapshots.
    auto next_decision = correlated;
    next_decision.sequence = 43;
    const auto next_result =
        NativeStrategicCompositionGenerator{}.generate(next_decision);
    assert(next_result.candidate_set_id != correlated_result.candidate_set_id);
    assert(next_result.candidates.front().identity !=
        correlated_result.candidates.front().identity);

    // Partial identity envelopes fail closed instead of publishing unbound
    // candidate proposals.
    auto incomplete_identity = input;
    incomplete_identity.match_id = 7001;
    incomplete_identity.player_id = 3;
    incomplete_identity.round = 5;
    const auto invalid_identity_result =
        NativeStrategicCompositionGenerator{}.generate(incomplete_identity);
    assert(invalid_identity_result.candidates.empty());
    assert(invalid_identity_result.reason == "invalid_candidate_set_identity");

    std::cout << "native strategic composition generator tests passed\n";
    return 0;
}
