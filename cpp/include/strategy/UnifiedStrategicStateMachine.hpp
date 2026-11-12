#pragma once

// Shadow-only orchestration for exploration, active composition, pivot
// evaluation and atomic confirmation. Legacy mechanisms are observed through
// immutable inputs and never become writers of the unified strategic state.

#include "composition_intelligence/contracts/CompositionContracts.hpp"
#include "strategy/CompositionBoundDirectionAnchor.hpp"
#include "strategy/CompositionDirectionPolicy.hpp"
#include "strategy/InitialStrategicDirectionDiscovery.hpp"
#include "strategy/PivotFeasibilityEvaluator.hpp"
#include "strategy/StrategicPivotTransitionCoordinator.hpp"
#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cstdint>
#include <optional>
#include <string>
#include <utility>
#include <vector>

namespace tft::strategy {

enum class StrategicCyclePhase : std::uint8_t {
    Exploration = 0,
    CompositionActive = 1,
    PivotEvaluation = 2,
    PivotConfirmed = 3,
    NoEvidence = 4,
    Invalidated = 5
};

enum class LegacyConsistency : std::uint8_t {
    NotAvailable = 0,
    Consistent = 1,
    Divergent = 2
};

struct StrategicCycleInput {
    // Existing active composition, if a composition source already selected it.
    // The orchestrator takes a value snapshot and never mutates the source.
    std::optional<composition_intelligence::CompositionCandidate> active_composition;

    // Candidate generated from the selected discovery hypothesis.
    std::optional<composition_intelligence::CompositionCandidate> initial_composition_candidate;
    DirectionDiscoveryInput exploration;

    // Optional independent pivot candidate and the exact normalized evidence
    // evaluated for that candidate.
    std::optional<StrategicPivotAnchorCandidate> pivot_candidate;
    std::optional<composition_intelligence::CompositionCandidate> pivot_destination;
    std::optional<PivotFeasibilityInput> pivot_feasibility;

    // Legacy outputs are diagnostic-only. They never write the unified state.
    std::optional<CompositionDirectionState> legacy_direction;
    std::optional<StrategicPlanDecision> legacy_plan;

    std::uint64_t evaluation_sequence{0};
};

struct StrategicCycleDiagnostics {
    DirectionDiscoveryResult discovery;
    std::optional<PivotFeasibilityResult> pivot_feasibility;
    std::optional<PivotConfirmationResult> pivot_confirmation;
    LegacyConsistency legacy_consistency{LegacyConsistency::NotAvailable};
    std::vector<std::string> divergence_reasons;
    std::string transition_reason{"not_evaluated"};
    std::string previous_phase;
    std::string current_phase;
    bool shadow_only{true};
};

struct StrategicCycleResult {
    StrategicCyclePhase phase{StrategicCyclePhase::Exploration};
    StrategicAnchorState anchors;
    std::optional<composition_intelligence::ActiveComposition> active_composition;
    StrategicCycleDiagnostics diagnostics;
    bool state_changed{false};
    bool shadow_only{true};
};

// One authority per phase:
// - exploration discovery proposes; it cannot publish without a composition;
// - the versioned composition owns direction once active;
// - pivot feasibility evaluates a separate candidate;
// - StrategicPivotTransitionCoordinator is the sole promotion path;
// - legacy policy/planner outputs are read-only comparison signals.
class UnifiedStrategicStateMachine {
public:
    explicit UnifiedStrategicStateMachine(
        PivotConfirmationPolicy pivot_policy = {}
    ) : pivot_coordinator_(pivot_policy) {}

    StrategicCycleResult refresh(const StrategicCycleInput& input) {
        StrategicCycleResult out;
        out.diagnostics.previous_phase = phase_name(phase_);
        out.diagnostics.discovery = discovery_.evaluate(input.exploration);

        const bool had_active = pivot_coordinator_.active_composition().has_value();

        if (!had_active && input.active_composition.has_value()) {
            const composition_intelligence::ActiveComposition seed{
                *input.active_composition, 1};
            const auto projected = CompositionBoundDirectionAnchor::from_active_composition(seed);
            if (!projected) {
                phase_ = StrategicCyclePhase::NoEvidence;
                out.diagnostics.transition_reason = "active_composition_cannot_form_valid_direction_anchor";
                return finish(std::move(out));
            }
            const auto initialized = pivot_coordinator_.initialize(*input.active_composition, *projected);
            out.state_changed = initialized.state_changed;
            out.diagnostics.transition_reason = initialized.reason;
            phase_ = initialized.status == PivotConfirmationStatus::Initialized
                ? StrategicCyclePhase::CompositionActive : StrategicCyclePhase::NoEvidence;
        } else if (!had_active) {
            if (out.diagnostics.discovery.status == DirectionDiscoveryStatus::HypothesesFound &&
                !out.diagnostics.discovery.hypotheses.empty()) {
                const auto& hypothesis = out.diagnostics.discovery.hypotheses.front();
                if (!input.initial_composition_candidate.has_value()) {
                    phase_ = StrategicCyclePhase::Exploration;
                    out.diagnostics.transition_reason = "direction_hypothesis_waiting_for_composition_candidate";
                } else {
                    auto initial_direction = hypothesis.anchor;
                    bind_initial_direction(initial_direction, *input.initial_composition_candidate);
                    const auto initialized = pivot_coordinator_.initialize(
                        *input.initial_composition_candidate, initial_direction);
                    out.state_changed = initialized.state_changed;
                    out.diagnostics.transition_reason = initialized.reason;
                    phase_ = initialized.status == PivotConfirmationStatus::Initialized
                        ? StrategicCyclePhase::CompositionActive : StrategicCyclePhase::NoEvidence;
                }
            } else {
                phase_ = StrategicCyclePhase::NoEvidence;
                out.diagnostics.transition_reason = out.diagnostics.discovery.reason;
            }
        }

        if (pivot_coordinator_.active_composition()) {
            if (input.pivot_candidate.has_value()) {
                if (!input.pivot_destination || !input.pivot_feasibility) {
                    phase_ = StrategicCyclePhase::NoEvidence;
                    out.diagnostics.transition_reason = "pivot_candidate_missing_destination_or_feasibility_snapshot";
                } else {
                    const auto evaluated = pivot_evaluator_.evaluate(*input.pivot_feasibility);
                    out.diagnostics.pivot_feasibility = evaluated;
                    const auto confirmed = pivot_coordinator_.observe_and_confirm(
                        *input.pivot_candidate, *input.pivot_destination,
                        *input.pivot_feasibility, evaluated, input.evaluation_sequence);
                    out.diagnostics.pivot_confirmation = confirmed;
                    out.state_changed = out.state_changed || confirmed.state_changed;
                    if (confirmed.status == PivotConfirmationStatus::Confirmed) {
                        phase_ = StrategicCyclePhase::PivotConfirmed;
                    } else if (confirmed.status == PivotConfirmationStatus::ObservedPending ||
                               confirmed.status == PivotConfirmationStatus::Cooldown) {
                        phase_ = StrategicCyclePhase::PivotEvaluation;
                    } else if (confirmed.status == PivotConfirmationStatus::InsufficientEvidence) {
                        phase_ = StrategicCyclePhase::NoEvidence;
                    } else if (input.pivot_candidate->lifecycle ==
                               StrategicAnchorLifecycle::Invalidated) {
                        phase_ = StrategicCyclePhase::Invalidated;
                    } else {
                        phase_ = StrategicCyclePhase::CompositionActive;
                    }
                    out.diagnostics.transition_reason = confirmed.reason;
                }
            } else if (pivot_coordinator_.anchors().has_pivot_candidate()) {
                // Missing candidate on a subsequent refresh invalidates the
                // pending hypothesis instead of leaving a stale pivot visible.
                auto invalidated = pivot_coordinator_.anchors().pivot_candidate;
                invalidated.lifecycle = StrategicAnchorLifecycle::Invalidated;
                PivotFeasibilityInput empty_input;
                PivotFeasibilityResult empty_result;
                const composition_intelligence::CompositionCandidate empty_destination;
                const auto confirmation = pivot_coordinator_.observe_and_confirm(
                    invalidated, empty_destination, empty_input, empty_result,
                    input.evaluation_sequence);
                out.diagnostics.pivot_confirmation = confirmation;
                phase_ = StrategicCyclePhase::Invalidated;
                out.diagnostics.transition_reason = "pending_pivot_missing_from_new_snapshot";
            } else {
                phase_ = StrategicCyclePhase::CompositionActive;
                out.diagnostics.transition_reason = "active_composition_retained";
            }
        }

        compare_legacy_outputs(input, out);
        return finish(std::move(out));
    }

    const StrategicAnchorState& anchors() const noexcept {
        return pivot_coordinator_.anchors();
    }

    const std::vector<StrategicPivotTransitionRecord>& transition_history() const noexcept {
        return pivot_coordinator_.history();
    }

    const std::optional<composition_intelligence::ActiveComposition>& active_composition() const noexcept {
        return pivot_coordinator_.active_composition();
    }

private:
    static void bind_initial_direction(
        StrategicDirectionAnchor& anchor,
        const composition_intelligence::CompositionCandidate& composition
    ) {
        anchor.identity = "direction:" + composition.composition_id + ":v1";
        anchor.composition_identity = composition.composition_id;
        anchor.composition_version = 1;
        anchor.composition_bound = true;
        anchor.lifecycle = StrategicAnchorLifecycle::Active;
        anchor.reference_unit_ids.clear();
        for (const auto& unit : composition.units)
            anchor.reference_unit_ids.push_back(unit.champion_id);
        std::sort(anchor.reference_unit_ids.begin(), anchor.reference_unit_ids.end());
    }

    void compare_legacy_outputs(
        const StrategicCycleInput& input,
        StrategicCycleResult& out
    ) const {
        if (!pivot_coordinator_.active_composition()) {
            out.diagnostics.legacy_consistency = LegacyConsistency::NotAvailable;
            return;
        }
        const auto& active_direction = pivot_coordinator_.anchors().direction_anchor.direction;
        bool has_comparison = false;
        if (input.legacy_direction && !input.legacy_direction->direction.empty()) {
            has_comparison = true;
            if (input.legacy_direction->direction != active_direction)
                out.diagnostics.divergence_reasons.push_back(
                    "legacy_composition_direction_policy_disagrees_with_active_anchor");
        }
        if (input.legacy_plan &&
            !input.legacy_plan->target_composition_direction.empty()) {
            has_comparison = true;
            if (input.legacy_plan->target_composition_direction != active_direction)
                out.diagnostics.divergence_reasons.push_back(
                    "legacy_strategic_planner_target_disagrees_with_active_anchor");
        }
        out.diagnostics.legacy_consistency = !has_comparison
            ? LegacyConsistency::NotAvailable
            : out.diagnostics.divergence_reasons.empty()
                ? LegacyConsistency::Consistent : LegacyConsistency::Divergent;
    }

    static const char* phase_name(StrategicCyclePhase phase) {
        switch (phase) {
            case StrategicCyclePhase::Exploration: return "EXPLORATION";
            case StrategicCyclePhase::CompositionActive: return "COMPOSITION_ACTIVE";
            case StrategicCyclePhase::PivotEvaluation: return "PIVOT_EVALUATION";
            case StrategicCyclePhase::PivotConfirmed: return "PIVOT_CONFIRMED";
            case StrategicCyclePhase::NoEvidence: return "NO_EVIDENCE";
            case StrategicCyclePhase::Invalidated: return "INVALIDATED";
        }
        return "UNKNOWN";
    }

    StrategicCycleResult finish(StrategicCycleResult out) {
        out.phase = phase_;
        out.anchors = pivot_coordinator_.anchors();
        out.active_composition = pivot_coordinator_.active_composition();
        out.diagnostics.current_phase = phase_name(phase_);
        out.diagnostics.shadow_only = true;
        out.shadow_only = true;
        return out;
    }

    InitialStrategicDirectionDiscovery discovery_;
    PivotFeasibilityEvaluator pivot_evaluator_;
    StrategicPivotTransitionCoordinator pivot_coordinator_;
    StrategicCyclePhase phase_{StrategicCyclePhase::Exploration};
};

} // namespace tft::strategy
