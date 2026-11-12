#pragma once

// Shadow-only orchestration for exploration, active composition, pivot
// evaluation and atomic confirmation. Legacy mechanisms are observed through
// immutable inputs and never become writers of the unified strategic state.

#include "composition_intelligence/contracts/CompositionContracts.hpp"
#include "strategy/CompositionBoundDirectionAnchor.hpp"
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

struct StrategicCycleInput {
    // Existing active composition, if a composition source already selected it.
    // The orchestrator takes a value snapshot and never mutates the source.
    std::optional<composition_intelligence::ActiveComposition> active_composition;

    // Candidate generated from the selected discovery hypothesis.
    std::optional<composition_intelligence::CompositionCandidate> initial_composition_candidate;
    DirectionDiscoveryInput exploration;

    // Optional independent pivot candidate and the exact normalized evidence
    // evaluated for that candidate.
    std::optional<StrategicPivotAnchorCandidate> pivot_candidate;
    std::optional<composition_intelligence::CompositionCandidate> pivot_destination;
    std::optional<PivotFeasibilityInput> pivot_feasibility;

    std::uint64_t evaluation_sequence{0};
};

struct StrategicCycleDiagnostics {
    DirectionDiscoveryResult discovery;
    std::optional<PivotFeasibilityResult> pivot_feasibility;
    std::optional<PivotConfirmationResult> pivot_confirmation;
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
        auto discovery_input = input.exploration;
        // Exploratory continuity is owned by this machine. Caller-provided hints
        // are ignored so legacy direction state cannot bias the new discovery.
        discovery_input.previous_direction = previous_discovery_direction_;
        const bool had_active = pivot_coordinator_.active_composition().has_value();
        if (input.active_composition.has_value()) {
            discovery_input.composition_defined = true;
            discovery_input.active_composition_identity = input.active_composition->candidate.composition_id;
        } else if (had_active) {
            discovery_input.composition_defined = true;
            discovery_input.active_composition_identity =
                pivot_coordinator_.active_composition()->candidate.composition_id;
        }
        out.diagnostics.discovery = discovery_.evaluate(discovery_input);
        if (out.diagnostics.discovery.status == DirectionDiscoveryStatus::HypothesesFound &&
            !out.diagnostics.discovery.hypotheses.empty()) {
            previous_discovery_direction_ =
                out.diagnostics.discovery.hypotheses.front().anchor.direction;
        }

        if (!had_active && input.active_composition.has_value()) {
            const auto projected = CompositionBoundDirectionAnchor::from_active_composition(
                *input.active_composition);
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
                } else if (!composition_contains_units(
                               *input.initial_composition_candidate,
                               hypothesis.anchor.reference_unit_ids)) {
                    phase_ = StrategicCyclePhase::Exploration;
                    out.diagnostics.transition_reason =
                        "initial_composition_does_not_contain_discovered_support_units";
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
                    auto invalidated = *input.pivot_candidate;
                    invalidated.lifecycle = StrategicAnchorLifecycle::Invalidated;
                    PivotFeasibilityInput empty_input;
                    PivotFeasibilityResult empty_result;
                    const composition_intelligence::CompositionCandidate empty_destination;
                    const auto confirmation = pivot_coordinator_.observe_and_confirm(
                        invalidated, empty_destination, empty_input, empty_result,
                        input.evaluation_sequence);
                    out.diagnostics.pivot_confirmation = confirmation;
                    phase_ = StrategicCyclePhase::Invalidated;
                    out.diagnostics.transition_reason =
                        "pivot_candidate_missing_destination_or_feasibility_snapshot";
                } else if (!pivot_candidate_matches_destination(
                               *input.pivot_candidate, *input.pivot_destination,
                               *input.pivot_feasibility)) {
                    auto invalidated = *input.pivot_candidate;
                    invalidated.lifecycle = StrategicAnchorLifecycle::Invalidated;
                    PivotFeasibilityInput empty_input;
                    PivotFeasibilityResult empty_result;
                    const composition_intelligence::CompositionCandidate empty_destination;
                    const auto confirmation = pivot_coordinator_.observe_and_confirm(
                        invalidated, empty_destination, empty_input, empty_result,
                        input.evaluation_sequence);
                    out.diagnostics.pivot_confirmation = confirmation;
                    phase_ = StrategicCyclePhase::Invalidated;
                    out.diagnostics.transition_reason =
                        "pivot_candidate_destination_units_or_carry_contract_mismatch";
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
    static bool composition_contains_units(
        const composition_intelligence::CompositionCandidate& composition,
        const std::vector<std::int32_t>& unit_ids
    ) {
        if (unit_ids.empty()) return false;
        for (const auto id : unit_ids) {
            const auto found = std::find_if(composition.units.begin(), composition.units.end(),
                [&](const auto& unit) { return unit.champion_id == id; });
            if (found == composition.units.end()) return false;
        }
        return true;
    }

    static bool pivot_candidate_matches_destination(
        const StrategicPivotAnchorCandidate& pivot,
        const composition_intelligence::CompositionCandidate& destination,
        const PivotFeasibilityInput& feasibility
    ) {
        if (destination.composition_id != pivot.target_composition_identity ||
            feasibility.candidate_composition_identity != destination.composition_id ||
            !composition_contains_units(destination, pivot.reference_unit_ids) ||
            destination.units.size() != feasibility.required_units.size()) {
            return false;
        }
        std::size_t carry_count = 0;
        for (const auto& unit : destination.units) {
            const auto required = std::find_if(
                feasibility.required_units.begin(), feasibility.required_units.end(),
                [&](const auto& item) { return item.champion_id == unit.champion_id; });
            if (required == feasibility.required_units.end() || required->core != unit.core)
                return false;
            const bool is_carry = unit.champion_id == destination.main_carry_id;
            if (required->carry != is_carry) return false;
            if (is_carry) ++carry_count;
        }
        return destination.main_carry_id < 0 ? carry_count == 0 : carry_count == 1;
    }

    static void bind_initial_direction(
        StrategicDirectionAnchor& anchor,
        const composition_intelligence::CompositionCandidate& composition
    ) {
        const auto discovered_direction = anchor.direction;
        anchor.identity = "direction:" + composition.composition_id + ":v1";
        anchor.direction = composition.composition_id;
        anchor.reason = "initial_composition_selected_from_discovery:" + discovered_direction;
        anchor.composition_identity = composition.composition_id;
        anchor.composition_version = 1;
        anchor.composition_bound = true;
        anchor.lifecycle = StrategicAnchorLifecycle::Active;
        anchor.reference_unit_ids.clear();
        for (const auto& unit : composition.units)
            anchor.reference_unit_ids.push_back(unit.champion_id);
        std::sort(anchor.reference_unit_ids.begin(), anchor.reference_unit_ids.end());
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
    std::string previous_discovery_direction_;
    PivotFeasibilityEvaluator pivot_evaluator_;
    StrategicPivotTransitionCoordinator pivot_coordinator_;
    StrategicCyclePhase phase_{StrategicCyclePhase::Exploration};
};

} // namespace tft::strategy
