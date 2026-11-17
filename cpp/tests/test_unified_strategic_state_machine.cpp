#include "strategy/UnifiedStrategicStateMachine.hpp"
#include "strategy/UnifiedStrategicShadowRuntime.hpp"

#include <cassert>
#include <filesystem>
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

DirectionDiscoveryInput competing_discovery_input(double bruiser_board, double invoker_board) {
    DirectionDiscoveryInput input;
    input.round = 3;
    input.units = {
        {10, 2, 2, 1, true, false, false, false, false, bruiser_board, {"Bruiser"}},
        {11, 2, 1, 1, false, true, false, false, false, 0.0, {"Bruiser"}},
        {20, 2, 2, 1, true, false, false, false, false, invoker_board, {"Invoker"}},
        {21, 2, 1, 1, false, true, false, false, false, 0.0, {"Invoker"}}
    };
    input.trait_thresholds = {{"Bruiser", 2}, {"Invoker", 2}};
    // This external hint must not influence the runtime-owned discovery state.
    input.previous_direction = "LegacyDirection";
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

void machine_owns_exploratory_direction_history_without_legacy_inputs() {
    UnifiedStrategicStateMachine machine;
    StrategicCycleInput input;
    input.exploration.units = {
        {10, 2, 2, 1, true, false, false, false, true, 0.0, {"Bruiser"}},
        {11, 2, 1, 1, false, true, false, false, false, 0.0, {"Bruiser"}},
        {20, 2, 2, 1, true, false, false, false, false, 0.0, {"Invoker"}},
        {21, 2, 1, 1, false, true, false, false, false, 0.0, {"Invoker"}}
    };
    input.exploration.trait_thresholds = {{"Bruiser", 2}, {"Invoker", 2}};
    // This caller-supplied hint resembles an old direction, but the machine
    // must ignore it and establish its own continuity from observed evidence.
    input.exploration.previous_direction = "Invoker";

    auto result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::Exploration);
    assert(result.diagnostics.discovery.hypotheses.size() == 2);
    assert(result.diagnostics.discovery.hypotheses.front().anchor.direction == "Bruiser");

    // Invoker gains a small evidence advantage. The machine retains its own
    // viable Bruiser hypothesis; the caller cannot steer it through a hint.
    input.exploration.units[2].board_contribution = 1.0;
    input.exploration.previous_direction = "Invoker";
    result = machine.refresh(input);
    assert(result.phase == StrategicCyclePhase::Exploration);
    assert(result.diagnostics.discovery.hypotheses.front().anchor.direction == "Bruiser");
}

void shadow_runtime_isolates_players_and_resets_its_own_direction_history() {
    const auto base = std::filesystem::temp_directory_path();
    const auto player_zero_path = base / "tft-direction-discovery-player-zero.jsonl";
    const auto player_one_path = base / "tft-direction-discovery-player-one.jsonl";
    std::error_code ignored;
    std::filesystem::remove(player_zero_path, ignored);
    std::filesystem::remove(player_one_path, ignored);

    UnifiedStrategicShadowRuntime player_zero(player_zero_path);
    UnifiedStrategicShadowRuntime player_one(player_one_path);
    const StrategicCycleAuditContext context_zero{42, 0, 3};
    const StrategicCycleAuditContext context_one{42, 1, 3};

    StrategicCycleInput zero_input;
    zero_input.exploration = competing_discovery_input(0.0, 0.0);
    auto zero_result = player_zero.refresh(context_zero, zero_input);
    assert(zero_result.diagnostics.discovery.hypotheses.front().anchor.direction == "Bruiser");

    StrategicCycleInput one_input;
    one_input.exploration = competing_discovery_input(0.0, 1.0);
    auto one_result = player_one.refresh(context_one, one_input);
    assert(one_result.diagnostics.discovery.hypotheses.front().anchor.direction == "Invoker");

    // Each player retains only its own prior hypothesis when the ranking shifts.
    zero_input.exploration = competing_discovery_input(0.0, 1.0);
    zero_result = player_zero.refresh(context_zero, zero_input);
    assert(zero_result.diagnostics.discovery.hypotheses.front().anchor.direction == "Bruiser");

    one_input.exploration = competing_discovery_input(1.0, 0.0);
    one_result = player_one.refresh(context_one, one_input);
    assert(one_result.diagnostics.discovery.hypotheses.front().anchor.direction == "Invoker");

    // A new machine lifecycle starts without the previous player's/session's hint.
    player_zero.reset_machine();
    zero_result = player_zero.refresh(context_zero, zero_input);
    assert(zero_result.diagnostics.discovery.hypotheses.front().anchor.direction == "Invoker");

    std::filesystem::remove(player_zero_path, ignored);
    std::filesystem::remove(player_one_path, ignored);
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
    machine_owns_exploratory_direction_history_without_legacy_inputs();
    shadow_runtime_isolates_players_and_resets_its_own_direction_history();
    pivot_evaluation_does_not_mutate_then_confirms_synchronized_state();
    invalidated_candidate_is_removed_and_old_direction_is_preserved();
    missing_candidate_invalidates_pending_pivot_without_mutation();
    insufficient_evidence_clears_pivot_and_keeps_active_composition();
    std::cout << "Unified strategic state machine tests passed\n";
    return 0;
}
