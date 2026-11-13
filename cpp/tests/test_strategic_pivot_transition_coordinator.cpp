#include "strategy/StrategicPivotTransitionCoordinator.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;
using namespace tft::composition_intelligence;

namespace {
CompositionCandidate make_composition(const std::string& id, std::int32_t carry,
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
    value.source_reference = "test";
    return value;
}

StrategicDirectionAnchor make_direction(const std::string& id,
                                        const std::string& composition,
                                        std::uint64_t version,
                                        std::int32_t unit) {
    StrategicDirectionAnchor value;
    value.identity = id;
    value.direction = composition;
    value.composition_identity = composition;
    value.composition_version = version;
    value.reference_unit_ids = {unit};
    value.evidence = {StrategicAnchorEvidenceKind::CompositionCore};
    value.confidence = 0.8;
    value.reason = "initial";
    value.lifecycle = StrategicAnchorLifecycle::Active;
    value.composition_bound = true;
    return value;
}

StrategicPivotAnchorCandidate make_pivot() {
    StrategicPivotAnchorCandidate value;
    value.identity = "pivot-b";
    value.target_direction = "direction-b";
    value.target_composition_identity = "composition-b";
    value.source_direction_anchor_identity = "direction-a-v1";
    value.source_composition_version = 1;
    value.reference_unit_ids = {3, 4};
    value.evidence = {StrategicAnchorEvidenceKind::OwnedUnit,
                      StrategicAnchorEvidenceKind::TraitCompletion};
    value.confidence = 0.9;
    value.reason = "core_and_traits_reachable";
    value.lifecycle = StrategicAnchorLifecycle::Evaluating;
    return value;
}

PivotFeasibilityInput make_feasibility_input() {
    PivotFeasibilityInput value;
    value.candidate_composition_identity = "composition-b";
    value.source_direction_anchor_identity = "direction-a-v1";
    value.source_composition_version = 1;
    return value;
}

PivotFeasibilityResult viable_result(const PivotFeasibilityInput& input) {
    PivotFeasibilityResult value;
    value.status = PivotFeasibilityStatus::Viable;
    value.reason = "all_gates_satisfied";
    value.score = 90.0;
    value.candidate_composition_identity = input.candidate_composition_identity;
    value.source_direction_anchor_identity = input.source_direction_anchor_identity;
    value.source_composition_version = input.source_composition_version;
    value.shadow_only = true;
    return value;
}

StrategicPivotTransitionCoordinator initialized_coordinator(
    PivotConfirmationPolicy policy = {3, 60.0, 5}
) {
    StrategicPivotTransitionCoordinator coordinator(policy);
    const auto result = coordinator.initialize(
        make_composition("composition-a", 1,
            {{1, UnitRole::MainCarry, true, 100},
             {2, UnitRole::Frontline, true, 80}}),
        make_direction("direction-a-v1", "composition-a", 1, 1));
    assert(result.status == PivotConfirmationStatus::Initialized);
    return coordinator;
}

void confirms_and_synchronizes_both_identities_atomically() {
    auto coordinator = initialized_coordinator();
    const auto pivot = make_pivot();
    const auto input = make_feasibility_input();
    const auto destination = make_composition("composition-b", 3,
        {{3, UnitRole::MainCarry, true, 100},
         {4, UnitRole::Frontline, true, 80}});

    for (std::uint64_t sequence = 1; sequence <= 2; ++sequence) {
        const auto pending = coordinator.observe_and_confirm(
            pivot, destination, input, viable_result(input), sequence);
        assert(pending.status == PivotConfirmationStatus::ObservedPending);
        assert(coordinator.active_composition()->candidate.composition_id == "composition-a");
        assert(coordinator.anchors().direction_anchor.identity == "direction-a-v1");
        assert(coordinator.anchors().pivot_candidate.lifecycle == StrategicAnchorLifecycle::Evaluated);
    }

    const auto confirmed = coordinator.observe_and_confirm(
        pivot, destination, input, viable_result(input), 3);
    assert(confirmed.status == PivotConfirmationStatus::Confirmed);
    assert(confirmed.state_changed);
    assert(coordinator.active_composition()->candidate.composition_id == "composition-b");
    assert(coordinator.active_composition()->version == 2);
    assert(coordinator.anchors().direction_anchor.composition_identity == "composition-b");
    assert(coordinator.anchors().direction_anchor.composition_version == 2);
    assert(coordinator.anchors().direction_anchor.lifecycle == StrategicAnchorLifecycle::Active);
    assert(coordinator.anchors().pivot_candidate.identity.empty());
    assert(coordinator.history().size() == 1);
    assert(coordinator.history().front().previous_direction_identity == "direction-a-v1");
    assert(coordinator.history().front().new_direction_identity ==
           coordinator.anchors().direction_anchor.identity);
    assert(coordinator.history().front().previous_composition_version == 1);
    assert(coordinator.history().front().new_composition_version == 2);
}

void insufficient_or_rejected_evaluation_never_changes_direction() {
    auto coordinator = initialized_coordinator();
    const auto pivot = make_pivot();
    const auto input = make_feasibility_input();
    const auto destination = make_composition("composition-b", 3,
        {{3, UnitRole::MainCarry, true, 100}});
    auto insufficient = viable_result(input);
    insufficient.status = PivotFeasibilityStatus::InsufficientEvidence;

    auto result = coordinator.observe_and_confirm(pivot, destination, input, insufficient, 1);
    assert(result.status == PivotConfirmationStatus::InsufficientEvidence);
    assert(coordinator.active_composition()->candidate.composition_id == "composition-a");
    assert(coordinator.anchors().direction_anchor.identity == "direction-a-v1");

    auto rejected = viable_result(input);
    rejected.status = PivotFeasibilityStatus::Rejected;
    result = coordinator.observe_and_confirm(pivot, destination, input, rejected, 2);
    assert(result.status == PivotConfirmationStatus::Rejected);
    assert(coordinator.active_composition()->version == 1);
    assert(coordinator.history().empty());
}

void mismatched_or_invalidated_source_is_rejected_without_mutation() {
    auto coordinator = initialized_coordinator();
    auto pivot = make_pivot();
    pivot.source_composition_version = 9; // stale source version
    const auto result = coordinator.observe_and_confirm(
        pivot,
        make_composition("composition-b", 3, {{3, UnitRole::MainCarry, true, 100}}),
        make_feasibility_input(), viable_result(make_feasibility_input()), 1);
    assert(result.status == PivotConfirmationStatus::Rejected);
    assert(coordinator.active_composition()->candidate.composition_id == "composition-a");
    assert(coordinator.anchors().direction_anchor.composition_version == 1);
}

void stale_feasibility_result_cannot_confirm_a_different_candidate() {
    auto coordinator = initialized_coordinator();
    const auto pivot = make_pivot();
    const auto input = make_feasibility_input();
    auto stale_result = viable_result(input);
    stale_result.candidate_composition_identity = "composition-old";
    const auto result = coordinator.observe_and_confirm(
        pivot,
        make_composition("composition-b", 3, {{3, UnitRole::MainCarry, true, 100}}),
        input, stale_result, 1);
    assert(result.status == PivotConfirmationStatus::Rejected);
    assert(result.reason == "destination_or_feasibility_identity_mismatch");
    assert(coordinator.active_composition()->candidate.composition_id == "composition-a");
    assert(coordinator.anchors().direction_anchor.identity == "direction-a-v1");
    assert(coordinator.history().empty());
}

void invalidated_candidate_is_cleared_without_changing_active_direction() {
    auto coordinator = initialized_coordinator();
    auto pivot = make_pivot();
    const auto destination = make_composition("composition-b", 3,
        {{3, UnitRole::MainCarry, true, 100}});
    const auto input = make_feasibility_input();
    auto result = coordinator.observe_and_confirm(
        pivot, destination, input, viable_result(input), 1);
    assert(result.status == PivotConfirmationStatus::ObservedPending);
    assert(coordinator.anchors().pivot_candidate.identity == "pivot-b");

    pivot.lifecycle = StrategicAnchorLifecycle::Invalidated;
    result = coordinator.observe_and_confirm(
        pivot, destination, input, viable_result(input), 2);
    assert(result.status == PivotConfirmationStatus::Rejected);
    assert(coordinator.anchors().pivot_candidate.identity.empty());
    assert(coordinator.anchors().direction_anchor.identity == "direction-a-v1");
    assert(coordinator.active_composition()->candidate.composition_id == "composition-a");
    assert(coordinator.history().empty());
}

void rejects_incomplete_initial_state() {
    StrategicPivotTransitionCoordinator coordinator;
    auto invalid_direction = make_direction("direction-a-v1", "composition-a", 99, 1);
    const auto result = coordinator.initialize(
        make_composition("composition-a", 1, {{1, UnitRole::MainCarry, true, 100}}),
        invalid_direction);
    assert(result.status == PivotConfirmationStatus::Rejected);
    assert(!coordinator.active_composition().has_value());
}

void destination_conflict_and_out_of_order_updates_are_rejected() {
    auto coordinator = initialized_coordinator();
    auto pivot = make_pivot();
    auto input = make_feasibility_input();
    input.candidate_composition_identity = "some-other-composition";
    auto result = coordinator.observe_and_confirm(
        pivot,
        make_composition("composition-b", 3, {{3, UnitRole::MainCarry, true, 100}}),
        input, viable_result(input), 1);
    assert(result.status == PivotConfirmationStatus::Rejected);

    input = make_feasibility_input();
    result = coordinator.observe_and_confirm(
        pivot,
        make_composition("composition-b", 3, {{3, UnitRole::MainCarry, true, 100}}),
        input, viable_result(input), 2);
    assert(result.status == PivotConfirmationStatus::ObservedPending);
    result = coordinator.observe_and_confirm(
        pivot,
        make_composition("composition-b", 3, {{3, UnitRole::MainCarry, true, 100}}),
        input, viable_result(input), 2);
    assert(result.status == PivotConfirmationStatus::OutOfOrder);
    assert(coordinator.active_composition()->version == 1);
}

void cooldown_prevents_rapid_reverse_pivots() {
    StrategicPivotTransitionCoordinator coordinator({1, 60.0, 5});
    assert(coordinator.initialize(
        make_composition("composition-a", 1, {{1, UnitRole::MainCarry, true, 100}}),
        make_direction("direction-a-v1", "composition-a", 1, 1)
    ).status == PivotConfirmationStatus::Initialized);

    auto pivot = make_pivot();
    auto input = make_feasibility_input();
    auto result = coordinator.observe_and_confirm(
        pivot, make_composition("composition-b", 3, {{3, UnitRole::MainCarry, true, 100}}),
        input, viable_result(input), 10);
    assert(result.status == PivotConfirmationStatus::Confirmed);

    // A reverse candidate based on the new version is viable, but the minimum
    // refresh interval has not elapsed; active state remains composition B.
    StrategicPivotAnchorCandidate reverse;
    reverse.identity = "pivot-back-a";
    reverse.target_direction = "direction-a";
    reverse.target_composition_identity = "composition-a";
    reverse.source_direction_anchor_identity = coordinator.anchors().direction_anchor.identity;
    reverse.source_composition_version = 2;
    reverse.reference_unit_ids = {1};
    reverse.confidence = 0.9;
    reverse.reason = "reverse_candidate";
    reverse.lifecycle = StrategicAnchorLifecycle::Evaluating;
    PivotFeasibilityInput reverse_input;
    reverse_input.candidate_composition_identity = "composition-a";
    reverse_input.source_direction_anchor_identity = reverse.source_direction_anchor_identity;
    reverse_input.source_composition_version = 2;
    result = coordinator.observe_and_confirm(
        reverse, make_composition("composition-a", 1, {{1, UnitRole::MainCarry, true, 100}}),
        reverse_input, viable_result(reverse_input), 11);
    assert(result.status == PivotConfirmationStatus::Cooldown);
    assert(coordinator.active_composition()->candidate.composition_id == "composition-b");
    assert(coordinator.anchors().direction_anchor.composition_version == 2);
}
} // namespace

int main() {
    confirms_and_synchronizes_both_identities_atomically();
    insufficient_or_rejected_evaluation_never_changes_direction();
    mismatched_or_invalidated_source_is_rejected_without_mutation();
    invalidated_candidate_is_cleared_without_changing_active_direction();
    stale_feasibility_result_cannot_confirm_a_different_candidate();
    rejects_incomplete_initial_state();
    destination_conflict_and_out_of_order_updates_are_rejected();
    cooldown_prevents_rapid_reverse_pivots();
    std::cout << "Strategic pivot transition coordinator tests passed\n";
    return 0;
}
