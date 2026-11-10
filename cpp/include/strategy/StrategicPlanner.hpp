#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>

namespace tft::strategy {

struct StrategicPlannerConfig {
    double minimum_absolute_advantage{0.75};
    double minimum_relative_advantage{0.20};
    double minimum_anchor_score{0.01};
    double minimum_adapt_advantage{0.10};
    double preserve_board_contribution{0.50};
    double preserve_item_fit{0.60};
    std::uint32_t required_reviews_unlocked{2};
    std::uint32_t required_reviews_locked{3};
};

class StrategicPlanner {
public:
    explicit StrategicPlanner(StrategicPlannerConfig config = {})
        : config_(config) {}

    StrategicPlanDecision evaluate(
        const StrategicSharedContext& context,
        StrategicCommitment& commitment) const {
        StrategicPlanDecision out;
        out.shadow_only = true;
        out.composition_decision = CompositionDecision::InsufficientEvidence;
        out.reason = StrategicReason::InsufficientEvidence;
        out.target_composition_direction = context.current_composition_direction;
        out.current_direction_score = context.current_direction_score;
        out.current_direction_viable = context.current_direction_viable;
        out.candidate_generation = context.candidate_generation;
        out.minimum_adapt_advantage = config_.minimum_adapt_advantage;
        out.required_pivot_advantage = std::max(
            config_.minimum_absolute_advantage,
            std::abs(context.current_direction_score) *
                config_.minimum_relative_advantage);
        out.current_direction_confidence =
            context.current_composition_direction.empty() ? 0.0 : std::clamp(
                0.5 + context.current_direction_score /
                    (2.0 * (1.0 + std::abs(context.current_direction_score))),
                0.5, 0.95);

        if (!context.alive) {
            out.decision_path_reason = "player_not_alive";
            return out;
        }

        const auto best = best_anchor(context, out.candidate_diagnostics);
        const bool has_current = !context.current_composition_direction.empty();
        out.has_anchor_candidate = best.valid;
        out.best_anchor_score = best.valid ? best.score : 0.0;
        out.anchor_confidence = best.valid ? best.confidence : 0.0;

        if (has_current &&
            commitment.composition_direction != context.current_composition_direction) {
            commitment.composition_direction = context.current_composition_direction;
            commitment.selected_round = context.round;
            clear_candidate(commitment);
        }

        if (!has_current) {
            if (best.valid) {
                out.composition_decision = CompositionDecision::InitialSelection;
                out.reason = StrategicReason::AnchorOpportunity;
                out.target_composition_direction = best.direction;
                out.anchor_champion_id = best.champion_id;
                out.confidence = best.confidence;
                out.estimated_transition_cost = best.transition_cost;
                commitment.composition_direction = best.direction;
                commitment.selected_round = context.round;
                commitment.selection_reason = out.reason;
                clear_candidate(commitment);
            }
            out.decision_path_reason = best.valid
                ? "initial_direction_selected" : "no_initial_anchor_available";
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        if (!best.valid) {
            if (!context.current_direction_viable) {
                out.composition_decision = CompositionDecision::Abandon;
                out.reason = StrategicReason::BoardDeficit;
                out.confidence = 0.65;
                commitment.composition_direction.clear();
                out.target_composition_direction.clear();
                commitment.selection_reason = out.reason;
                clear_candidate(commitment);
                out.decision_path_reason = "current_direction_unviable_without_alternative";
            } else {
                out.composition_decision = CompositionDecision::Keep;
                out.reason = StrategicReason::BoardAdvantage;
                out.target_composition_direction = context.current_composition_direction;
                out.decision_path_reason = "current_direction_viable_without_alternative";
                clear_candidate(commitment);
            }
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        out.anchor_champion_id = best.champion_id;
        out.confidence = best.confidence;
        out.estimated_transition_cost = best.transition_cost;

        if (best.direction == context.current_composition_direction) {
            out.composition_decision = CompositionDecision::Keep;
            out.reason = StrategicReason::BoardAdvantage;
            out.target_composition_direction = context.current_composition_direction;
            out.decision_path_reason = "best_anchor_matches_current_direction";
            clear_candidate(commitment);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        const double required_advantage = out.required_pivot_advantage;
        const double advantage = best.score - context.current_direction_score;
        out.alternative_advantage = advantage;

        if (!context.current_direction_viable) {
            out.composition_decision = CompositionDecision::Pivot;
            out.reason = StrategicReason::BoardDeficit;
            out.target_composition_direction = best.direction;
            out.decision_path_reason = "current_direction_not_viable";
            commitment.selection_reason = out.reason;
            commitment.confidence = best.confidence;
            clear_candidate(commitment);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        if (advantage < config_.minimum_adapt_advantage) {
            out.composition_decision = CompositionDecision::Keep;
            out.reason = StrategicReason::BoardAdvantage;
            out.target_composition_direction = context.current_composition_direction;
            out.decision_path_reason = "alternative_below_minimum_adapt_advantage";
            clear_candidate(commitment);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        if (commitment.candidate_composition_direction == best.direction) {
            if (context.round > commitment.last_review_round)
                ++commitment.consecutive_reviews;
            commitment.candidate_anchor_id = best.champion_id;
        } else {
            commitment.candidate_composition_direction = best.direction;
            commitment.candidate_anchor_id = best.champion_id;
            commitment.candidate_score = best.score;
            commitment.consecutive_reviews = 1;
        }
        commitment.candidate_score = best.score;
        commitment.last_review_round = context.round;

        const auto required_reviews = context.composition_locked
            ? config_.required_reviews_locked
            : config_.required_reviews_unlocked;
        if (advantage < required_advantage ||
            commitment.consecutive_reviews < required_reviews) {
            out.composition_decision = CompositionDecision::Adapt;
            out.reason = best.transition_cost > 0.65
                ? StrategicReason::TransitionCost
                : StrategicReason::AnchorOpportunity;
            out.target_composition_direction = best.direction;
            out.confidence = std::min(best.confidence, 0.65);
            out.decision_path_reason = advantage < required_advantage
                ? "alternative_below_required_advantage"
                : "alternative_waiting_for_persistence";
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        out.composition_decision = CompositionDecision::Pivot;
        out.reason = StrategicReason::AnchorOpportunity;
        out.target_composition_direction = best.direction;
        out.decision_path_reason = "pivot_thresholds_and_persistence_satisfied";
        commitment.selection_reason = out.reason;
        commitment.confidence = best.confidence;
        classify_owned_units(context, out, out.target_composition_direction);
        return out;
    }

private:
    struct AnchorScore {
        bool valid{false};
        std::string direction;
        std::int32_t champion_id{-1};
        double score{0.0};
        double confidence{0.0};
        double transition_cost{0.0};
        bool shop_available{false};
    };

    StrategicPlannerConfig config_;

    AnchorScore best_anchor(
        const StrategicSharedContext& context,
        std::vector<StrategicCandidateDiagnostic>& diagnostics) const {
        AnchorScore best;
        std::size_t best_index = static_cast<std::size_t>(-1);
        diagnostics.reserve(context.anchor_candidates.size());
        for (const auto& candidate : context.anchor_candidates) {
            const auto& unit = candidate.unit;
            StrategicCandidateDiagnostic diagnostic;
            diagnostic.champion_id = unit.champion_id;
            diagnostic.target_composition_direction =
                candidate.target_composition_direction;
            const bool finite = unit.champion_id >= 0 &&
                !candidate.target_composition_direction.empty() &&
                std::isfinite(candidate.anchor_value) &&
                std::isfinite(candidate.transition_cost) &&
                std::isfinite(candidate.contestation) &&
                std::isfinite(unit.board_contribution) &&
                std::isfinite(unit.composition_fit) &&
                std::isfinite(unit.item_fit);
            if (!finite) {
                diagnostic.evaluation_reason = "invalid_candidate_data";
                diagnostics.push_back(std::move(diagnostic));
                continue;
            }

            const double reusable = static_cast<double>(
                std::clamp(candidate.reusable_owned_units, 0, 5));
            const double score =
                candidate.anchor_value +
                0.30 * unit.board_contribution +
                0.25 * unit.composition_fit +
                0.20 * unit.item_fit +
                0.35 * reusable -
                1.50 * std::max(0.0, candidate.transition_cost) -
                0.30 * std::max(0.0, candidate.contestation) +
                (candidate.shop_available ? 0.20 : 0.0);
            diagnostic.score = score;
            if (score < config_.minimum_anchor_score) {
                diagnostic.evaluation_reason = "below_minimum_anchor_score";
                diagnostics.push_back(std::move(diagnostic));
                continue;
            }
            if (score <= best.score) {
                diagnostic.evaluation_reason = "not_best_scoring_candidate";
                diagnostics.push_back(std::move(diagnostic));
                continue;
            }

            if (best_index != static_cast<std::size_t>(-1)) {
                diagnostics[best_index].accepted = false;
                diagnostics[best_index].evaluation_reason =
                    "valid_but_not_selected";
            }
            best.valid = true;
            best.direction = candidate.target_composition_direction;
            best.champion_id = unit.champion_id;
            best.score = score;
            best.transition_cost = std::max(0.0, candidate.transition_cost);
            best.shop_available = candidate.shop_available;
            best.confidence = std::clamp(
                0.5 + score / (2.0 * (1.0 + std::abs(score))),
                0.5, 0.95);
            diagnostic.accepted = true;
            diagnostic.evaluation_reason = "selected_best_candidate";
            diagnostics.push_back(std::move(diagnostic));
            best_index = diagnostics.size() - 1;
        }
        return best;
    }

    static void clear_candidate(StrategicCommitment& commitment) {
        commitment.candidate_composition_direction.clear();
        commitment.candidate_anchor_id = -1;
        commitment.candidate_score = 0.0;
        commitment.consecutive_reviews = 0;
    }

    void classify_owned_units(
        const StrategicSharedContext& context,
        StrategicPlanDecision& out,
        const std::string& target_direction) const {
        for (const auto& unit : context.owned_units) {
            if (unit.champion_id < 0) continue;
            const bool target_trait_fit = !target_direction.empty() &&
                std::find(unit.traits.begin(), unit.traits.end(), target_direction)
                    != unit.traits.end();
            const bool transitioning =
                out.composition_decision == CompositionDecision::Pivot ||
                out.composition_decision == CompositionDecision::Abandon;
            const bool preserve =
                unit.board_contribution >= config_.preserve_board_contribution ||
                unit.item_fit >= config_.preserve_item_fit ||
                target_trait_fit ||
                (unit.is_core && !transitioning);
            (preserve ? out.preserve_unit_ids : out.replaceable_unit_ids)
                .push_back(unit.champion_id);
        }
    }
};

} // namespace tft::strategy
