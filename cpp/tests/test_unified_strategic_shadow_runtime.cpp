#include "strategy/UnifiedStrategicShadowRuntime.hpp"

#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>

using namespace tft::strategy;
using namespace tft::composition_intelligence;

namespace {

CompositionCandidate composition(const std::string& id, std::int32_t carry_id) {
    CompositionCandidate value;
    value.composition_id = id;
    value.source = CompositionSource::Native;
    value.set_id = "18";
    value.patch = "18.1";
    value.units = {
        {carry_id, UnitRole::MainCarry, true, 100},
        {2, UnitRole::Frontline, true, 80},
        {3, UnitRole::Support, false, 40}
    };
    value.main_carry_id = carry_id;
    value.target_board_size = 8;
    value.source_score = 80.0;
    value.source_reference = "native-runtime-pivot-test";
    return value;
}

StrategicCycleInput initial_input() {
    StrategicCycleInput input;
    input.active_composition = ActiveComposition{composition("composition-current", 1), 1};
    return input;
}

StrategicPivotAnchorCandidate pivot_candidate() {
    StrategicPivotAnchorCandidate pivot;
    pivot.identity = "pivot-next";
    pivot.target_direction = "Invoker";
    pivot.target_composition_identity = "composition-next";
    pivot.source_direction_anchor_identity =
        "direction:composition:composition-current:1";
    pivot.source_composition_version = 1;
    pivot.reference_unit_ids = {1, 2, 3};
    pivot.evidence = {StrategicAnchorEvidenceKind::OwnedUnit,
                      StrategicAnchorEvidenceKind::TraitCompletion};
    pivot.confidence = 0.9;
    pivot.reason = "owned_core_and_reachable_traits";
    pivot.lifecycle = StrategicAnchorLifecycle::Evaluating;
    return pivot;
}

PivotFeasibilityInput feasibility_input() {
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

StrategicCycleInput pivot_input() {
    StrategicCycleInput input;
    input.pivot_candidate = pivot_candidate();
    input.pivot_destination = composition("composition-next", 1);
    input.pivot_feasibility = feasibility_input();
    return input;
}

void runtime_advances_confirmation_only_for_new_evidence_sequences() {
    ActiveCompositionManager active;
    StrategicCommitment commitment;
    commitment.composition_direction = "Bruiser";
    UnifiedStrategicShadowRuntime runtime(active, commitment, {}, {3, 60.0, 5});
    const StrategicCycleAuditContext context{20261120, 0, 12};

    auto result = runtime.refresh(context, initial_input());
    assert(result.phase == StrategicCyclePhase::CompositionActive);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.active_composition->version == 1);

    auto input = pivot_input();
    input.evaluation_sequence = 1;
    result = runtime.refresh(context, input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);
    assert(result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 1);

    // An identical observation is deduplicated and cannot advance hysteresis.
    const auto duplicate = runtime.refresh(context, input);
    assert(duplicate.phase == StrategicCyclePhase::PivotEvaluation);
    assert(duplicate.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 1);

    // A new sequence with identical facts is still a duplicate observation.
    input.evaluation_sequence = 2;
    const auto same_facts = runtime.refresh(context, input);
    assert(same_facts.phase == StrategicCyclePhase::PivotEvaluation);
    assert(same_facts.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 1);

    // Confirmation advances only after the evidence itself changes.
    input.pivot_feasibility->gold_available = 39;
    input.evaluation_sequence = 3;
    result = runtime.refresh(context, input);
    assert(result.phase == StrategicCyclePhase::PivotEvaluation);
    assert(result.diagnostics.pivot_confirmation->consecutive_viable_evaluations == 2);
    assert(result.active_composition->candidate.composition_id == "composition-current");
    assert(result.active_composition->version == 1);

    input.pivot_feasibility->gold_available = 38;
    input.evaluation_sequence = 4;
    result = runtime.refresh(context, input);
    assert(result.phase == StrategicCyclePhase::PivotConfirmed);
    assert(result.state_changed);
    assert(result.active_composition->candidate.composition_id == "composition-next");
    assert(result.active_composition->version == 2);
    assert(result.anchors.direction_anchor.direction == "Invoker");
    assert(result.anchors.direction_anchor.composition_identity == "composition-next");
    assert(result.anchors.direction_anchor.composition_version == 2);
    assert(commitment.composition_direction == "Invoker");
    assert(runtime.machine().transition_history().size() == 1);
    const auto& transition = runtime.machine().transition_history().front();
    assert(transition.previous_composition_version == 1);
    assert(transition.new_composition_version == 2);
    assert(transition.previous_composition_identity == "composition-current");
    assert(transition.new_composition_identity == "composition-next");
}

} // namespace

int main() {
    runtime_advances_confirmation_only_for_new_evidence_sequences();
    std::cout << "Unified strategic shadow runtime pivot lifecycle passed\\n";
    return 0;
}
