#include "composition_intelligence/UnitPriorityPlanner.hpp"
#include "strategy/UnifiedStrategicStateMachine.hpp"

#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace tft::strategy;
using namespace tft::composition_intelligence;

namespace {

CompositionCandidate make_composition(const std::string& id) {
    CompositionCandidate value;
    value.composition_id = id;
    value.source = CompositionSource::Native;
    value.set_id = "18";
    value.patch = "18.1";
    value.units = {
        {1, UnitRole::MainCarry, true, 100},
        {2, UnitRole::Frontline, true, 80},
        {3, UnitRole::Support, false, 40}
    };
    value.main_carry_id = 1;
    value.target_board_size = 8;
    value.source_score = 80.0;
    value.source_reference = "strategic-e2e-fixture";
    return value;
}

DirectionDiscoveryInput make_early_snapshot() {
    DirectionDiscoveryInput input;
    input.round = 3;
    input.gold_available = 12;
    input.units = {
        {1, 1, 2, 1, false, true, false, false, true, 0.0, {"Bruiser"}},
        {2, 2, 1, 1, true, false, false, false, false, 3.0, {"Bruiser"}}
    };
    input.trait_thresholds = {{"Bruiser", 2}};
    return input;
}

ActiveComposition make_active(const std::string& id = "composition-current") {
    return ActiveComposition{make_composition(id), 1};
}

StrategicPivotAnchorCandidate make_pivot() {
    StrategicPivotAnchorCandidate value;
    value.identity = "pivot-next";
    value.target_direction = "composition-next";
    value.target_composition_identity = "composition-next";
    value.source_direction_anchor_identity =
        "direction:composition:composition-current:1";
    value.source_composition_version = 1;
    value.reference_unit_ids = {1, 2, 3};
    value.evidence = {StrategicAnchorEvidenceKind::OwnedUnit,
                      StrategicAnchorEvidenceKind::TraitCompletion};
    value.confidence = 0.9;
    value.reason = "owned_core_and_reachable_traits";
    value.lifecycle = StrategicAnchorLifecycle::Evaluating;
    return value;
}

PivotFeasibilityInput make_feasibility() {
    PivotFeasibilityInput input;
    input.candidate_composition_identity = "composition-next";
    input.source_direction_anchor_identity =
        "direction:composition:composition-current:1";
    input.source_composition_version = 1;
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
    input.required_traits = {{"Invoker", 2}, {"Arcanist", 2}};
    return input;
}

CompositionCandidate make_destination() {
    return make_composition("composition-next");
}

StrategicCycleInput make_active_input() {
    StrategicCycleInput input;
    input.active_composition = make_active();
    return input;
}

void early_pairs_create_a_cheap_unbound_direction() {
    const auto result = InitialStrategicDirectionDiscovery{}.evaluate(make_early_snapshot());
    assert(result.status == DirectionDiscoveryStatus::HypothesesFound);
    assert(!result.hypotheses.empty());
    const auto& hypothesis = result.hypotheses.front();
    assert(hypothesis.anchor.direction == "Bruiser");
    assert(!hypothesis.anchor.composition_bound);
    assert(hypothesis.anchor.lifecycle == StrategicAnchorLifecycle::Proposed);
    assert(std::find(hypothesis.anchor.evidence.begin(), hypothesis.anchor.evidence.end(),
                     StrategicAnchorEvidenceKind::PairProgress) != hypothesis.anchor.evidence.end());

    UnifiedStrategicStateMachine machine;
    StrategicCycleInput input;
    input.exploration = make_early_snapshot();
    auto cycle = machine.refresh(input);
    assert(cycle.phase == StrategicCyclePhase::Exploration);
    assert(!cycle.active_composition);
    input.initial_composition_candidate = make_composition("composition-bruiser");
    cycle = machine.refresh(input);
    assert(cycle.phase == StrategicCyclePhase::CompositionActive);
    assert(cycle.anchors.direction_anchor.composition_identity == "composition-bruiser");
}

void composition_hierarchy_beats_an_easy_external_two_star() {
    auto candidate = make_composition("comp-A");
    candidate.units.push_back({4, UnitRole::Flex, false, 30});
    ActiveCompositionManager manager;
    assert(manager.publish(candidate).status == PublishStatus::Published);
    const auto active = *manager.current();

    UnitPriorityContext context;
    context.composition_id = active.candidate.composition_id;
    context.composition_version = active.version;
    context.owned_units = {
        {1, 1, 1, true, {}},
        {4, 1, 1, false, {}},
        {9, 2, 2, true, {}}
    };
    context.evidence = {
        {1, 0.2, 0.2, 0.9, 1, 1, -1, false},
        {4, 0.2, 0.2, 0.9, 0, 0, -1, false},
        {9, 1.0, 1.0, 1.0, 0, 0, -1, false}
    };
    const auto result = UnitPriorityPlanner{}.resolve(active, context);
    const auto carry = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.champion_id == 1; });
    const auto flex = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.champion_id == 4; });
    const auto external = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.champion_id == 9; });
    assert(carry != result.units.end() && carry->tier == UnitPriorityTier::Carry);
    assert(carry->intent == UnitIntent::Upgrade && carry->target_star == 2);
    assert(flex != result.units.end());
    assert(external != result.units.end());
    assert(external->priority < flex->priority);
}

void pivot_requires_carry_and_support_not_just_shop_synergies() {
    PivotFeasibilityEvaluator evaluator;
    auto low_cost_carry = make_feasibility();
    low_cost_carry.required_units[0].cost = 2;
    auto result = evaluator.evaluate(low_cost_carry);
    assert(result.status == PivotFeasibilityStatus::Rejected);
    assert(std::find(result.blockers.begin(), result.blockers.end(),
        "main_carry_not_two_star_and_below_four_cost") != result.blockers.end());

    auto high_cost_without_support = make_feasibility();
    high_cost_without_support.required_traits = {{"Invoker", 3}};
    result = evaluator.evaluate(high_cost_without_support);
    assert(result.carry_eligible); // 4-cost satisfies only the carry gate.
    assert(result.status == PivotFeasibilityStatus::Rejected);
    assert(std::find(result.blockers.begin(), result.blockers.end(),
        "trait_not_reachable_Invoker") != result.blockers.end());
}

void carry_two_star_is_an_alternative_to_four_or_five_cost() {
    PivotFeasibilityEvaluator evaluator;
    auto input = make_feasibility();
    input.required_units[0].cost = 2;
    input.observed_units[0].star = 2;
    const auto result = evaluator.evaluate(input);
    assert(result.carry_eligible);
    assert(result.status == PivotFeasibilityStatus::Viable);
    assert(std::find(result.favorable_evidence.begin(), result.favorable_evidence.end(),
        "main_carry_already_two_star") != result.favorable_evidence.end());
}

void evaluation_preserves_the_current_direction() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    auto input = make_active_input();
    auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::CompositionActive);
    const auto original_identity = result.anchors.direction_anchor.identity;
    const auto original_version = result.anchors.direction_anchor.composition_version;

    input.active_composition.reset();
    input.pivot_candidate = make_pivot();
    input.pivot_destination = make_destination();
    input.pivot_feasibility = make_feasibility();
    input.evaluation_sequence = 1;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.anchors.direction_anchor.identity == original_identity);
    assert(result.anchors.direction_anchor.composition_version == original_version);
    assert(result.anchors.pivot_candidate.identity == "pivot-next");
}

void confirmed_pivot_commits_composition_and_direction_together() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    auto input = make_active_input();
    machine.refresh(input);
    input.active_composition.reset();
    input.pivot_candidate = make_pivot();
    input.pivot_destination = make_destination();
    input.pivot_feasibility = make_feasibility();

    StrategicCycleResult result;
    for (std::uint64_t sequence = 1; sequence <= 3; ++sequence) {
        input.evaluation_sequence = sequence;
        result = machine.refresh(input);
    }
    assert(result.phase == StrategicCyclePhase::PivotConfirmed);
    assert(result.active_composition->candidate.composition_id == "composition-next");
    assert(result.active_composition->version == 2);
    assert(result.anchors.direction_anchor.composition_identity == "composition-next");
    assert(result.anchors.direction_anchor.composition_version == 2);
    assert(result.anchors.direction_anchor.identity == "direction:composition-next:v2");
    assert(!result.anchors.has_pivot_candidate());
    assert(machine.transition_history().size() == 1);
    const auto& transition = machine.transition_history().front();
    assert(transition.previous_composition_version == 1);
    assert(transition.new_composition_version == 2);
    assert(transition.previous_direction_identity == "direction:composition:composition-current:1");
    assert(transition.new_direction_identity == "direction:composition-next:v2");
}

void unknown_pool_data_never_approves_a_pivot() {
    auto input = make_feasibility();
    input.required_traits = {{"Invoker", 2}};
    input.observed_units[2] = {3, 0, 1, 0, -1};
    const auto result = PivotFeasibilityEvaluator{}.evaluate(input);
    assert(result.status == PivotFeasibilityStatus::InsufficientEvidence);
    assert(std::find(result.missing_data.begin(), result.missing_data.end(),
        "pool_availability_unknown_for_unit_3") != result.missing_data.end());
    assert(result.score <= 49.0);
}

void invalidated_or_stale_candidate_cannot_be_confirmed() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    auto input = make_active_input();
    machine.refresh(input);
    input.active_composition.reset();
    input.pivot_candidate = make_pivot();
    input.pivot_destination = make_destination();
    input.pivot_feasibility = make_feasibility();
    input.pivot_candidate->lifecycle = StrategicAnchorLifecycle::Invalidated;
    input.evaluation_sequence = 1;
    const auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::Invalidated);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.active_composition->version == 1);
    assert(result.anchors.direction_anchor.composition_version == 1);
    assert(!result.anchors.has_pivot_candidate());
}

void interrupted_evidence_resets_confirmation_streak() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    auto input = make_active_input();
    machine.refresh(input);
    input.active_composition.reset();
    input.pivot_candidate = make_pivot();
    input.pivot_destination = make_destination();
    input.pivot_feasibility = make_feasibility();

    input.evaluation_sequence = 1;
    auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);

    auto insufficient = make_feasibility();
    insufficient.transition_economic_cost = -1.0;
    input.pivot_feasibility = insufficient;
    input.evaluation_sequence = 2;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::NoEvidence);
    assert(result.active_composition->candidate.composition_id == "composition-current");

    input.pivot_feasibility = make_feasibility();
    input.evaluation_sequence = 3;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);
    assert(result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 1);
    input.evaluation_sequence = 4;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);
    assert(result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 2);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.active_composition->version == 1);
}

} // namespace

int main() {
    early_pairs_create_a_cheap_unbound_direction();
    composition_hierarchy_beats_an_easy_external_two_star();
    pivot_requires_carry_and_support_not_just_shop_synergies();
    carry_two_star_is_an_alternative_to_four_or_five_cost();
    evaluation_preserves_the_current_direction();
    confirmed_pivot_commits_composition_and_direction_together();
    unknown_pool_data_never_approves_a_pivot();
    invalidated_or_stale_candidate_cannot_be_confirmed();
    interrupted_evidence_resets_confirmation_streak();
    std::cout << "Strategic direction/pivot E2E scenarios passed: 9 deterministic scenarios\n";
    return 0;
}
