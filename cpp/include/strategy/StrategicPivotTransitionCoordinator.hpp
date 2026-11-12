#pragma once

#include "composition_intelligence/ActiveCompositionManager.hpp"
#include "strategy/PivotFeasibilityEvaluator.hpp"
#include "strategy/StrategicAnchorContracts.hpp"

#include <algorithm>
#include <cstdint>
#include <string>
#include <utility>
#include <vector>

namespace tft::strategy {

enum class PivotConfirmationStatus : std::uint8_t {
    Initialized = 0,
    ObservedPending = 1,
    Confirmed = 2,
    Rejected = 3,
    InsufficientEvidence = 4,
    Cooldown = 5,
    OutOfOrder = 6
};

struct PivotConfirmationPolicy {
    std::uint32_t required_consecutive_viable_evaluations{3};
    double minimum_viable_score{60.0};
    std::uint64_t minimum_refreshes_between_pivots{5};
};

struct StrategicPivotTransitionRecord {
    std::string pivot_identity;
    std::string previous_direction_identity;
    std::string new_direction_identity;
    std::string previous_composition_identity;
    std::string new_composition_identity;
    std::uint64_t previous_composition_version{0};
    std::uint64_t new_composition_version{0};
    std::uint64_t evaluation_sequence{0};
    double feasibility_score{0.0};
    std::string reason;
    std::vector<StrategicAnchorEvidenceKind> evidence;
};

struct PivotConfirmationResult {
    PivotConfirmationStatus status{PivotConfirmationStatus::InsufficientEvidence};
    std::string reason;
    std::uint32_t consecutive_viable_evaluations{0};
    std::uint64_t active_composition_version{0};
    bool state_changed{false};
    bool shadow_only{true};
};

// Owns the composition and direction-anchor transition as one shadow-state
// transaction. Evaluation alone never changes the active composition/direction.
class StrategicPivotTransitionCoordinator {
public:
    explicit StrategicPivotTransitionCoordinator(
        PivotConfirmationPolicy policy = {}
    ) : policy_(policy) {
        if (policy_.required_consecutive_viable_evaluations == 0)
            policy_.required_consecutive_viable_evaluations = 1;
        if (!std::isfinite(policy_.minimum_viable_score))
            policy_.minimum_viable_score = 60.0;
        policy_.minimum_viable_score = std::clamp(policy_.minimum_viable_score, 0.0, 100.0);
    }

    PivotConfirmationResult initialize(
        const composition_intelligence::CompositionCandidate& composition,
        const StrategicDirectionAnchor& direction
    ) {
        if (composition_manager_.current())
            return {PivotConfirmationStatus::Rejected, "already_initialized"};
        auto staged_manager = composition_manager_;
        const auto published = staged_manager.publish(composition);
        if (published.status != composition_intelligence::PublishStatus::Published)
            return {PivotConfirmationStatus::Rejected, "initial_composition_rejected"};
        if (!direction.is_valid() || !direction.composition_bound ||
            direction.composition_identity != published.active.candidate.composition_id ||
            direction.composition_version != published.active.version ||
            direction.lifecycle != StrategicAnchorLifecycle::Active) {
            return {PivotConfirmationStatus::Rejected, "initial_direction_not_bound_to_composition"};
        }
        composition_manager_ = std::move(staged_manager);
        anchors_.direction_anchor = direction;
        anchors_.pivot_candidate = {};
        return {PivotConfirmationStatus::Initialized, "initial_state_initialized",
                0, published.active.version, true};
    }

    PivotConfirmationResult observe_and_confirm(
        const StrategicPivotAnchorCandidate& pivot,
        const composition_intelligence::CompositionCandidate& destination,
        const PivotFeasibilityInput& feasibility_input,
        const PivotFeasibilityResult& feasibility,
        std::uint64_t evaluation_sequence
    ) {
        const auto* active = composition_manager_.current()
            ? &*composition_manager_.current() : nullptr;
        if (!active || !anchors_.direction_anchor.is_valid())
            return rejected("active_direction_or_composition_missing");
        if (evaluation_sequence == 0 || evaluation_sequence <= last_evaluation_sequence_)
            return {PivotConfirmationStatus::OutOfOrder, "evaluation_sequence_not_monotonic",
                    viable_streak_, active->version, false};
        last_evaluation_sequence_ = evaluation_sequence;

        if (!pivot.is_valid() ||
            pivot.source_direction_anchor_identity != anchors_.direction_anchor.identity ||
            pivot.source_composition_version != active->version ||
            anchors_.direction_anchor.composition_identity != active->candidate.composition_id ||
            anchors_.direction_anchor.composition_version != active->version) {
            reset_streak();
            return rejected("pivot_candidate_conflicts_with_active_source");
        }
        if (destination.composition_id != pivot.target_composition_identity ||
            feasibility_input.candidate_composition_identity != pivot.target_composition_identity ||
            feasibility_input.source_direction_anchor_identity != pivot.source_direction_anchor_identity ||
            feasibility_input.source_composition_version != pivot.source_composition_version) {
            reset_streak();
            return rejected("destination_or_feasibility_identity_mismatch");
        }
        if (feasibility.status == PivotFeasibilityStatus::Rejected) {
            reset_streak();
            return {PivotConfirmationStatus::Rejected, "pivot_feasibility_rejected",
                    0, active->version, false};
        }
        if (feasibility.status != PivotFeasibilityStatus::Viable ||
            !feasibility.shadow_only || !std::isfinite(feasibility.score) ||
            feasibility.score < policy_.minimum_viable_score) {
            reset_streak();
            return {PivotConfirmationStatus::InsufficientEvidence,
                    "pivot_not_stably_viable_or_score_below_threshold",
                    0, active->version, false};
        }

        if (streak_candidate_identity_ != pivot.identity) {
            streak_candidate_identity_ = pivot.identity;
            viable_streak_ = 0;
        }
        ++viable_streak_;
        anchors_.pivot_candidate = pivot;
        anchors_.pivot_candidate.lifecycle = StrategicAnchorLifecycle::Evaluating;

        if (viable_streak_ < policy_.required_consecutive_viable_evaluations) {
            return {PivotConfirmationStatus::ObservedPending,
                    "awaiting_consecutive_viable_evaluations",
                    viable_streak_, active->version, false};
        }

        if (last_confirmed_sequence_ != 0 &&
            evaluation_sequence - last_confirmed_sequence_ <
                policy_.minimum_refreshes_between_pivots) {
            return {PivotConfirmationStatus::Cooldown, "minimum_refresh_cooldown_not_elapsed",
                    viable_streak_, active->version, false};
        }

        auto staged_manager = composition_manager_;
        const auto published = staged_manager.publish(
            destination, composition_intelligence::CompositionTransitionReason::StrategicPivot);
        if (published.status != composition_intelligence::PublishStatus::Published ||
            published.active.version != active->version + 1) {
            reset_streak();
            return rejected("destination_publish_failed_or_version_conflict");
        }

        StrategicDirectionAnchor next_direction;
        next_direction.identity = "direction:" + destination.composition_id +
            ":v" + std::to_string(published.active.version);
        next_direction.direction = pivot.target_direction;
        next_direction.composition_identity = destination.composition_id;
        next_direction.composition_version = published.active.version;
        next_direction.confidence = std::clamp(feasibility.score / 100.0, 0.0, 1.0);
        next_direction.reason = "confirmed_pivot:" + pivot.reason + ":" + feasibility.reason;
        next_direction.lifecycle = StrategicAnchorLifecycle::Active;
        next_direction.composition_bound = true;
        for (const auto& unit : destination.units)
            next_direction.reference_unit_ids.push_back(unit.champion_id);
        std::sort(next_direction.reference_unit_ids.begin(),
                  next_direction.reference_unit_ids.end());
        next_direction.evidence = pivot.evidence;
        next_direction.evidence.push_back(StrategicAnchorEvidenceKind::CompositionCore);
        if (!next_direction.is_valid()) {
            reset_streak();
            return rejected("synchronized_direction_anchor_invalid");
        }

        StrategicPivotTransitionRecord record;
        record.pivot_identity = pivot.identity;
        record.previous_direction_identity = anchors_.direction_anchor.identity;
        record.new_direction_identity = next_direction.identity;
        record.previous_composition_identity = active->candidate.composition_id;
        record.new_composition_identity = destination.composition_id;
        record.previous_composition_version = active->version;
        record.new_composition_version = published.active.version;
        record.evaluation_sequence = evaluation_sequence;
        record.feasibility_score = feasibility.score;
        record.reason = next_direction.reason;
        record.evidence = pivot.evidence;

        // Commit both related states only after every validation succeeds.
        composition_manager_ = std::move(staged_manager);
        anchors_.direction_anchor = std::move(next_direction);
        anchors_.pivot_candidate = {};
        history_.push_back(std::move(record));
        last_confirmed_sequence_ = evaluation_sequence;
        reset_streak();
        return {PivotConfirmationStatus::Confirmed, "composition_and_direction_committed_atomically",
                0, published.active.version, true};
    }

    const std::optional<composition_intelligence::ActiveComposition>& active_composition() const noexcept {
        return composition_manager_.current();
    }

    const StrategicAnchorState& anchors() const noexcept { return anchors_; }
    const std::vector<StrategicPivotTransitionRecord>& history() const noexcept { return history_; }

private:
    PivotConfirmationResult rejected(const std::string& reason) const {
        const auto version = composition_manager_.current()
            ? composition_manager_.current()->version : 0;
        return {PivotConfirmationStatus::Rejected, reason, viable_streak_, version, false};
    }

    void reset_streak() {
        viable_streak_ = 0;
        streak_candidate_identity_.clear();
    }

    PivotConfirmationPolicy policy_;
    composition_intelligence::ActiveCompositionManager composition_manager_;
    StrategicAnchorState anchors_;
    std::vector<StrategicPivotTransitionRecord> history_;
    std::uint64_t last_evaluation_sequence_{0};
    std::uint64_t last_confirmed_sequence_{0};
    std::uint32_t viable_streak_{0};
    std::string streak_candidate_identity_;
};

} // namespace tft::strategy
