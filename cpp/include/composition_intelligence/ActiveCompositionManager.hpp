#pragma once

#include "composition_intelligence/contracts/CompositionContracts.hpp"

#include <algorithm>
#include <cmath>
#include <optional>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

namespace tft::composition_intelligence {

// Owns the authoritative composition snapshot for the new shadow architecture.
// It has no dependency on the legacy composition-direction/focus systems.
class ActiveCompositionManager {
public:
    PublishResult publish(
        const CompositionCandidate& candidate,
        CompositionTransitionReason reason = CompositionTransitionReason::StrategicPivot
    ) {
        const auto validation_error = validate(candidate);
        if (!validation_error.empty()) {
            return {PublishStatus::RejectedInvalidCandidate, validation_error,
                    active_.value_or(ActiveComposition{}), false, {}};
        }

        if (active_ && equivalent(active_->candidate, candidate)) {
            return {PublishStatus::Unchanged, {}, *active_, false, {}};
        }

        const std::uint64_t previous_version = active_ ? active_->version : 0;
        const std::string previous_id = active_ ? active_->candidate.composition_id : std::string{};
        const auto previous_units = active_
            ? unit_ids(active_->candidate)
            : std::unordered_set<std::int32_t>{};

        ActiveComposition next{candidate, previous_version + 1};
        CompositionTransition transition;
        transition.previous_version = previous_version;
        transition.new_version = next.version;
        transition.previous_composition_id = previous_id;
        transition.new_composition_id = candidate.composition_id;
        transition.reason = active_ ? reason : CompositionTransitionReason::InitialSelection;

        const auto next_units = unit_ids(candidate);
        for (const auto id : next_units) {
            if (previous_units.count(id) != 0) {
                transition.shared_unit_ids.push_back(id);
                transition.unit_evidence.push_back({
                    id, CompositionUnitDisposition::RetainedInDestination,
                    "unit_remains_required_by_destination_composition"});
            } else {
                transition.added_unit_ids.push_back(id);
                transition.unit_evidence.push_back({
                    id, CompositionUnitDisposition::AddedForDestination,
                    "unit_is_required_by_destination_composition"});
            }
        }
        for (const auto id : previous_units) {
            if (next_units.count(id) == 0) {
                transition.removed_unit_ids.push_back(id);
                transition.unit_evidence.push_back({
                    id, CompositionUnitDisposition::NoLongerRequiredByDestination,
                    "unit_is_not_in_destination_target_and_requires_individual_utility_review"});
            }
        }

        sort_ids(transition.shared_unit_ids);
        sort_ids(transition.added_unit_ids);
        sort_ids(transition.removed_unit_ids);
        std::sort(transition.unit_evidence.begin(), transition.unit_evidence.end(),
            [](const auto& lhs, const auto& rhs) { return lhs.champion_id < rhs.champion_id; });

        active_ = next;
        return {PublishStatus::Published, {}, *active_, true, std::move(transition)};
    }

    // Hydrates an already-versioned snapshot into an empty manager. This is
    // intentionally separate from publish(): importing a snapshot must
    // preserve its source version rather than silently resetting it to v1.
    bool restore(const ActiveComposition& snapshot) {
        if (active_ || snapshot.version == 0 || !validate(snapshot.candidate).empty())
            return false;
        active_ = snapshot;
        return true;
    }

    const std::optional<ActiveComposition>& current() const noexcept {
        return active_;
    }

    void reset() noexcept {
        active_.reset();
    }

    static std::string validate(const CompositionCandidate& candidate) {
        if (candidate.composition_id.empty())
            return "composition_id must not be empty";
        if (candidate.set_id.empty())
            return "set_id must not be empty";
        if (candidate.units.empty())
            return "composition must contain at least one unit";
        if (candidate.target_board_size == 0 || candidate.target_board_size > 10)
            return "target_board_size must be between 1 and 10";
        if (!std::isfinite(candidate.source_score))
            return "source_score must be finite";

        std::unordered_set<std::int32_t> ids;
        bool has_main_carry = candidate.main_carry_id < 0;
        for (const auto& unit : candidate.units) {
            if (unit.champion_id < 0)
                return "champion_id must be non-negative";
            if (!ids.insert(unit.champion_id).second)
                return "composition contains duplicate champion_id";
            if (unit.priority < 0)
                return "unit priority must be non-negative";
            if (unit.champion_id == candidate.main_carry_id)
                has_main_carry = true;
        }
        if (!has_main_carry)
            return "main_carry_id must reference a unit in the composition";
        if (candidate.units.size() > candidate.target_board_size)
            return "composition unit count exceeds target_board_size";
        return {};
    }

private:
    static std::unordered_set<std::int32_t> unit_ids(
        const CompositionCandidate& candidate
    ) {
        std::unordered_set<std::int32_t> ids;
        for (const auto& unit : candidate.units)
            ids.insert(unit.champion_id);
        return ids;
    }

    static void sort_ids(std::vector<std::int32_t>& ids) {
        std::sort(ids.begin(), ids.end());
    }

    static bool equivalent(
        const CompositionCandidate& lhs,
        const CompositionCandidate& rhs
    ) {
        return lhs.composition_id == rhs.composition_id &&
            lhs.source == rhs.source &&
            lhs.set_id == rhs.set_id &&
            lhs.patch == rhs.patch &&
            lhs.units == rhs.units &&
            lhs.main_carry_id == rhs.main_carry_id &&
            lhs.target_board_size == rhs.target_board_size &&
            lhs.source_score == rhs.source_score &&
            lhs.source_reference == rhs.source_reference;
    }

    std::optional<ActiveComposition> active_;
};

} // namespace tft::composition_intelligence
