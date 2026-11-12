#include "strategy/UnifiedStrategicStateMachine.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;
using namespace tft::composition_intelligence;

namespace {
CompositionCandidate composition(const std::string& id, int carry,
                                std::vector<CompositionUnit> units) {
    CompositionCandidate value;
    value.composition_id = id;
    value.source = CompositionSource::Native;
    value.set_id = "18";
    value.patch = "18.1";
    value.units = std::move(units);
    value.main_carry_id = carry;
    value.target_board_size = 8;
    value.source_score = 80.0;
    value.source_reference = "unified-cycle-test";
    return value;
}

DirectionDiscoveryInput discovery_input() {
    DirectionDiscoveryInput input;
    input.round = 3;
    input.units = {
        {1, 1, 2, 1, false, true, false, false, true, 0.0, {"Bruiser"}},
        {2, 2, 1, 1, true, false, false, false, false, 3.0, {"Bruiser"}}
    };
    input.trait_thresholds = {{"Bruiser", 2}};
    return input;
}

StrategicPivotAnchorCandidate pivot_candidate() {
    StrategicPivotAnchorCandidate value;
    value.identity = "pivot-next";
    value.target_direction = "composition-next";
    value.target_composition_identity = "composition-next";
    value.source_direction_anchor_identity = "direction:composition:composition-current:1";
    value.source_composition_version = 1;
    value.reference_unit_ids = {1, 2, 3};
    value.evidence = {StrategicAnchorEvidenceKind::OwnedUnit,
                      StrategicAnchorEvidenceKind::TraitCompletion};
    value.confidence = 0.9;
    value.reason = "owned_core_and_reachable_traits";
    value.lifecycle = StrategicAnchorLifecycle::Evaluating;
    return value;
}

CompositionCandidate next_composition() {
    return composition("composition-next", 1,
        {{1, UnitRole::MainCarry, true, 100},
         {2, UnitRole::Frontline, true, 80},
         {3, UnitRole::Support, false, 40}});
}

PivotFeasibilityInput viable_pivot_input() {
    PivotFeasibilityInput input;
    input.candidate_composition_identity = "composition-next";
    input.source_direction_anchor_identity = "direction:composition:composition-current:1";
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

void exploration_waits_for_composition_and_then_binds_direction() {
    UnifiedStrategicStateMachine machine;
    StrategicCycleInput input;
    input.exploration = discovery_input();

    auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::Exploration);
    assert(!result.active_composition.has_value());
    assert(result.diagnostics.discovery.status == DirectionDiscoveryStatus::HypothesesFound);
    assert(!result.anchors.has_direction_anchor());

    input.initial_composition_candidate = composition(
        "composition-bruiser", 1,
        {{1, UnitRole::MainCarry, true, 100},
         {2, UnitRole::Frontline, true, 80}});
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::CompositionActive);
    assert(result.state_changed);
    assert(result.active_composition->version == 1);
    assert(result.anchors.direction_anchor.composition_identity == "composition-bruiser");
    assert(result.anchors.direction_anchor.composition_version == 1);
    assert(result.anchors.direction_anchor.direction == "composition-bruiser");
    assert(result.anchors.direction_anchor.lifecycle == StrategicAnchorLifecycle::Active);
}

void active_composition_has_authority_over_legacy_outputs() {
    UnifiedStrategicStateMachine machine;
    StrategicCycleInput input;
    input.active_composition = ActiveComposition{composition(
        "composition-current", 1,
        {{1, UnitRole::MainCarry, true, 100},
         {2, UnitRole::Frontline, true, 80}}), 7};
    CompositionDirectionState legacy_direction;
    legacy_direction.direction = "Bruiser";
    legacy_direction.locked = true;
    input.legacy_direction = legacy_direction;
    StrategicPlanDecision legacy_plan;
    legacy_plan.target_composition_direction = "composition-other";
    input.legacy_plan = legacy_plan;

    const auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::CompositionActive);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.active_composition->version == 7);
    assert(result.anchors.direction_anchor.direction == "composition-current");
    assert(result.anchors.direction_anchor.composition_version == 7);
    assert(result.diagnostics.legacy_consistency == LegacyConsistency::Divergent);
    assert(result.diagnostics.divergence_reasons.size() == 2);
}

void pivot_evaluation_does_not_mutate_then_confirms_synchronized_state() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    StrategicCycleInput input;
    input.active_composition = ActiveComposition{composition(
        "composition-current", 1,
        {{1, UnitRole::MainCarry, true, 100},
         {2, UnitRole::Frontline, true, 80}}), 1};
    auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::CompositionActive);

    input.active_composition.reset();
    input.pivot_candidate = pivot_candidate();
    input.pivot_destination = next_composition();
    input.pivot_feasibility = viable_pivot_input();

    for (std::uint64_t sequence = 1; sequence <= 2; ++sequence) {
        input.evaluation_sequence = sequence;
        result = machine.refresh(input);
        assert(result.phase == StrategicCyclePhase::PivotEvaluation);
        assert(result.active_composition->candidate.composition_id == "composition-current");
        assert(result.anchors.direction_anchor.composition_identity == "composition-current");
        assert(result.anchors.direction_anchor.composition_version == 1);
        assert(result.anchors.pivot_candidate.identity == "pivot-next");
    }

    input.evaluation_sequence = 3;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotConfirmed);
    assert(result.state_changed);
    assert(result.active_composition->candidate.composition_id == "composition-next");
    assert(result.active_composition->version == 2);
    assert(result.anchors.direction_anchor.composition_identity == "composition-next");
    assert(result.anchors.direction_anchor.composition_version == 2);
    assert(result.anchors.direction_anchor.identity == "direction:composition-next:v2");
    assert(result.anchors.pivot_candidate.identity.empty());
    assert(machine.transition_history().size() == 1);
}

void invalidated_candidate_is_removed_and_old_direction_is_preserved() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    StrategicCycleInput input;
    input.active_composition = ActiveComposition{composition(
        "composition-current", 1,
        {{1, UnitRole::MainCarry, true, 100}}), 1};
    auto result = machine.refresh(input);

    input.active_composition.reset();
    input.pivot_candidate = pivot_candidate();
    input.pivot_destination = next_composition();
    input.pivot_feasibility = viable_pivot_input();
    input.evaluation_sequence = 1;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);

    input.pivot_candidate->lifecycle = StrategicAnchorLifecycle::Invalidated;
    input.evaluation_sequence = 2;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::Invalidated);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.anchors.direction_anchor.composition_version == 1);
    assert(result.anchors.pivot_candidate.identity.empty());
}

void missing_candidate_invalidates_pending_pivot_without_mutation() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    StrategicCycleInput input;
    input.active_composition = ActiveComposition{composition(
        "composition-current", 1,
        {{1, UnitRole::MainCarry, true, 100}}), 1};
    machine.refresh(input);

    input.active_composition.reset();
    input.pivot_candidate = pivot_candidate();
    input.pivot_destination = next_composition();
    input.pivot_feasibility = viable_pivot_input();
    input.evaluation_sequence = 1;
    auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);

    input.pivot_candidate.reset();
    input.pivot_destination.reset();
    input.pivot_feasibility.reset();
    input.evaluation_sequence = 2;
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::Invalidated);
    assert(result.anchors.pivot_candidate.identity.empty());
    assert(result.active_composition->candidate.composition_id == "composition-current");
}

void insufficient_evidence_clears_pivot_and_keeps_active_composition() {
    UnifiedStrategicStateMachine machine({3, 60.0, 5});
    StrategicCycleInput input;
    input.active_composition = ActiveComposition{composition(
        "composition-current", 1,
        {{1, UnitRole::MainCarry, true, 100}}), 1};
    machine.refresh(input);

    input.active_composition.reset();
    input.pivot_candidate = pivot_candidate();
    input.pivot_destination = next_composition();
    auto insufficient = viable_pivot_input();
    insufficient.transition_economic_cost = -1.0;
    input.pivot_feasibility = insufficient;
    input.evaluation_sequence = 1;
    const auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::NoEvidence);
    assert(result.anchors.pivot_candidate.identity.empty());
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.anchors.direction_anchor.composition_version == 1);
}
} // namespace

int main() {
    exploration_waits_for_composition_and_then_binds_direction();
    active_composition_has_authority_over_legacy_outputs();
    pivot_evaluation_does_not_mutate_then_confirms_synchronized_state();
    invalidated_candidate_is_removed_and_old_direction_is_preserved();
    missing_candidate_invalidates_pending_pivot_without_mutation();
    insufficient_evidence_clears_pivot_and_keeps_active_composition();
    std::cout << "Unified strategic state machine tests passed\n";
    return 0;
}
