#include "strategy/StrategicEvidenceContext.hpp"
#include "strategy/StrategicPlanner.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;

namespace {
StrategicEvidenceContextInput observed_input() {
    StrategicEvidenceContextInput input;
    input.match_id = 7001;
    input.player_id = 2;
    input.round = 9;
    input.sequence = 41;
    input.direction = "Bruiser";
    input.direction_identity = "direction:v2:Bruiser";
    input.direction_source = "native_strategic_commitment";
    input.focus_traits = {"Bruiser", "Invoker"};
    input.core_unit_ids = {10, 11};
    input.provenance = {
        {"board", "native_board_snapshot", "observed"},
        {"shop", "native_shop_snapshot", "observed"}
    };
    auto& context = input.observed_context;
    context.player_id = input.player_id;
    context.round = input.round;
    context.hp = 72.0;
    context.gold = 31;
    context.level = 7;
    context.alive = true;
    context.owned_units = {
        StrategicUnitCandidate{10, "UnitA", 3, 2, 3, true, false,
            true, 0.9, 1.0, 0.8, {"Bruiser"}},
        StrategicUnitCandidate{11, "UnitB", 2, 1, 1, false, true,
            false, 0.0, 1.0, 0.2, {"Bruiser", "Invoker"}}
    };
    return input;
}

struct LegacyStateFixture {
    std::string composition_direction;
    std::string composition_focus;
    std::vector<std::string> core_traits;
    bool locked{false};
    std::vector<std::int32_t> planned_units;
    std::string candidate;
    std::uint32_t streak{0};
};
}

int main() {
    StrategicEvidenceContextBuilder builder;

    // Legacy fields are deliberately varied but are not accepted by the
    // builder. Identical observed facts therefore produce identical context.
    const LegacyStateFixture legacy_a{
        "Duelist", "Duelist", {"Duelist"}, true, {90, 91}, "PivotA", 8
    };
    const LegacyStateFixture legacy_b{
        "Invoker", "Invoker", {"Invoker"}, false, {1}, "PivotB", 0
    };
    (void)legacy_a;
    (void)legacy_b;

    const auto first = builder.build(observed_input());
    const auto second = builder.build(observed_input());
    assert(first.schema_version == StrategicEvidenceContext::kSchemaVersion);
    assert(first.valid_for(7001, 2, 9));
    assert(first.quality == StrategicEvidenceQuality::Complete);
    assert(first.proposed_or_confirmed_direction == "Bruiser");
    assert(first.planner_context.current_composition_direction == "Bruiser");
    assert(first.planner_context.current_composition_focus == "Bruiser");
    assert((first.planner_context.current_core_traits ==
            std::vector<std::string>{"Bruiser", "Invoker"}));
    assert(!first.planner_context.composition_locked);
    assert(first.observed_units.size() == 2);
    assert(first.planner_context.owned_units.size() == 2);
    assert(first.direction_identity == second.direction_identity);
    assert(first.planner_context.current_composition_direction ==
           second.planner_context.current_composition_direction);
    assert(first.planner_context.owned_units.size() ==
           second.planner_context.owned_units.size());

    StrategicCommitment commitment;
    const auto planned = StrategicPlanner{}.evaluate(first, commitment);
    assert(planned.target_composition_direction == "Bruiser");

    // Missing new direction evidence remains unknown; no historical fallback.
    auto incomplete_input = observed_input();
    incomplete_input.direction.clear();
    incomplete_input.direction_identity.clear();
    const auto incomplete = builder.build(std::move(incomplete_input));
    assert(incomplete.quality == StrategicEvidenceQuality::Partial);
    assert(incomplete.planner_context.current_composition_direction.empty());
    assert(!incomplete.planner_context.current_direction_viable);
    StrategicCommitment empty_commitment;
    const auto no_fallback = StrategicPlanner{}.evaluate(
        incomplete, empty_commitment);
    assert(no_fallback.target_composition_direction.empty());
    assert(no_fallback.composition_decision ==
           CompositionDecision::InsufficientEvidence);

    // A stale or mismatched player/round cannot be consumed as current context.
    assert(!first.valid_for(7002, 2, 9));
    assert(!first.valid_for(7001, 3, 9));
    assert(!first.valid_for(7001, 2, 10));

    auto invalid_input = observed_input();
    invalid_input.observed_context.round = 8;
    const auto invalid = builder.build(std::move(invalid_input));
    assert(invalid.quality == StrategicEvidenceQuality::Incompatible);
    assert(!invalid.valid_for(7001, 2, 9));

    auto no_sequence_input = observed_input();
    no_sequence_input.sequence = 0;
    const auto no_sequence = builder.build(std::move(no_sequence_input));
    assert(no_sequence.quality == StrategicEvidenceQuality::Incompatible);

    std::cout << "strategic evidence context tests passed\n";
    return 0;
}
