#include "composition_intelligence/ActiveCompositionManager.hpp"

#include <algorithm>
#include <cassert>
#include <iostream>

using namespace tft::composition_intelligence;

namespace {
CompositionCandidate candidate(
    const std::string& id,
    CompositionSource source,
    std::vector<CompositionUnit> units,
    std::int32_t carry = 1
) {
    CompositionCandidate value;
    value.composition_id = id;
    value.source = source;
    value.set_id = "18";
    value.patch = "18.1";
    value.units = std::move(units);
    value.main_carry_id = carry;
    value.target_board_size = 8;
    value.source_score = 10.0;
    return value;
}

void publishes_initial_opgg_composition() {
    ActiveCompositionManager manager;
    const auto input = candidate(
        "opgg-carry-comp",
        CompositionSource::Oppg,
        {{1, UnitRole::MainCarry, true, 100}, {2, UnitRole::Frontline, true, 80}}
    );
    const auto result = manager.publish(input);

    assert(result.status == PublishStatus::Published);
    assert(result.active.version == 1);
    assert(result.active.candidate.source == CompositionSource::Oppg);
    assert(result.has_transition);
    assert(result.transition.reason == CompositionTransitionReason::InitialSelection);
    assert(result.transition.previous_version == 0);
    assert(result.transition.new_version == 1);
    assert(result.transition.added_unit_ids.size() == 2);
    assert(result.transition.removed_unit_ids.empty());
}

void publishes_native_composition_using_same_contract() {
    ActiveCompositionManager manager;
    const auto input = candidate(
        "native-comp",
        CompositionSource::Native,
        {{1, UnitRole::MainCarry, true, 100}, {3, UnitRole::Support, false, 50}}
    );
    const auto result = manager.publish(input);

    assert(result.status == PublishStatus::Published);
    assert(result.active.candidate.source == CompositionSource::Native);
    assert(result.active.candidate.units.size() == 2);
}

void unchanged_candidate_does_not_increment_version() {
    ActiveCompositionManager manager;
    const auto input = candidate(
        "same-comp",
        CompositionSource::Native,
        {{1, UnitRole::MainCarry, true, 100}}
    );
    const auto first = manager.publish(input);
    const auto second = manager.publish(input);

    assert(first.active.version == 1);
    assert(second.status == PublishStatus::Unchanged);
    assert(second.active.version == 1);
    assert(!second.has_transition);
}

void pivot_publishes_new_version_and_classifies_units() {
    ActiveCompositionManager manager;
    const auto first = candidate(
        "composition-a",
        CompositionSource::Oppg,
        {{1, UnitRole::MainCarry, true, 100}, {2, UnitRole::Frontline, true, 80}}
    );
    const auto second = candidate(
        "composition-b",
        CompositionSource::Native,
        {{1, UnitRole::MainCarry, true, 100}, {3, UnitRole::Support, true, 70}}
    );

    manager.publish(first);
    const auto result = manager.publish(second, CompositionTransitionReason::StrategicPivot);

    assert(result.status == PublishStatus::Published);
    assert(result.active.version == 2);
    assert(result.transition.previous_version == 1);
    assert(result.transition.new_version == 2);
    assert(result.transition.previous_composition_id == "composition-a");
    assert(result.transition.new_composition_id == "composition-b");
    assert(result.transition.reason == CompositionTransitionReason::StrategicPivot);
    assert((result.transition.shared_unit_ids == std::vector<std::int32_t>{1}));
    assert((result.transition.added_unit_ids == std::vector<std::int32_t>{3}));
    assert((result.transition.removed_unit_ids == std::vector<std::int32_t>{2}));
    assert(result.transition.unit_evidence.size() == 3);
    const auto retained = std::find_if(result.transition.unit_evidence.begin(),
        result.transition.unit_evidence.end(), [](const auto& item) { return item.champion_id == 1; });
    const auto added = std::find_if(result.transition.unit_evidence.begin(),
        result.transition.unit_evidence.end(), [](const auto& item) { return item.champion_id == 3; });
    const auto removed = std::find_if(result.transition.unit_evidence.begin(),
        result.transition.unit_evidence.end(), [](const auto& item) { return item.champion_id == 2; });
    assert(retained != result.transition.unit_evidence.end());
    assert(retained->disposition == CompositionUnitDisposition::RetainedInDestination);
    assert(added != result.transition.unit_evidence.end());
    assert(added->disposition == CompositionUnitDisposition::AddedForDestination);
    assert(removed != result.transition.unit_evidence.end());
    assert(removed->disposition == CompositionUnitDisposition::NoLongerRequiredByDestination);
    assert(removed->reason.find("requires_individual_utility_review") != std::string::npos);
}

void invalid_candidate_does_not_mutate_active_composition() {
    ActiveCompositionManager manager;
    const auto valid = candidate(
        "valid",
        CompositionSource::Native,
        {{1, UnitRole::MainCarry, true, 100}}
    );
    manager.publish(valid);

    auto invalid = candidate(
        "invalid",
        CompositionSource::Native,
        {{2, UnitRole::MainCarry, true, 100}, {2, UnitRole::Flex, false, 10}}
    );
    const auto result = manager.publish(invalid);

    assert(result.status == PublishStatus::RejectedInvalidCandidate);
    assert(!result.validation_error.empty());
    assert(manager.current().has_value());
    assert(manager.current()->candidate.composition_id == "valid");
    assert(manager.current()->version == 1);
}

void invalid_main_carry_is_rejected() {
    ActiveCompositionManager manager;
    auto invalid = candidate(
        "invalid-carry",
        CompositionSource::Native,
        {{2, UnitRole::Frontline, true, 100}},
        99
    );
    const auto result = manager.publish(invalid);
    assert(result.status == PublishStatus::RejectedInvalidCandidate);
    assert(!manager.current().has_value());
}

} // namespace

int main() {
    publishes_initial_opgg_composition();
    publishes_native_composition_using_same_contract();
    unchanged_candidate_does_not_increment_version();
    pivot_publishes_new_version_and_classifies_units();
    invalid_candidate_does_not_mutate_active_composition();
    invalid_main_carry_is_rejected();
    std::cout << "ActiveCompositionManager tests passed\n";
    return 0;
}
