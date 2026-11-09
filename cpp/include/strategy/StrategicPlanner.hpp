#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>
#include <unordered_set>

namespace tft::strategy {

struct StrategicPlannerConfig {
    double minimum_absolute_advantage{0.75};
    double minimum_relative_advantage{0.20};
    double minimum_anchor_score{0.01};
    double preserve_board_contribution{0.50};
    double preserve_item_fit{0.70};
    double preserve_target_trait_fit{0.50};
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
        out.target_composition_direction = context.current_composition_direction;

        if (!context.alive) {
            out.reason = StrategicReason::InsufficientEvidence;
            return out;
        }

        const auto best = best_anchor(context);
        const bool has_current = !context.current_composition_direction.empty();

        if (commitment.composition_direction.empty() && has_current) {
            commitment.composition_direction = context.current_composition_direction;
            commitment.selected_round = context.round;
        }

        if (!has_current) {
            if (best.valid) {
                out.composition_decision = CompositionDecision::Adapt;
                out.reason = StrategicReason::AnchorOpportunity;
                out.target_composition_direction = best.direction;
                out.anchor_champion_id = best.champion_id;
                out.confidence = best.confidence;
                out.estimated_transition_cost = best.transition_cost;
                commitment.composition_direction = best.direction;
                commitment.selected_round = context.round;
                commitment.selection_reason = out.reason;
                clear_candidate(commitment);
            } else {
                out.reason = StrategicReason::InsufficientEvidence;
            }
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        if (!best.valid) {
            if (!context.current_direction_viable) {
                out.composition_decision = CompositionDecision::Abandon;
                out.reason = StrategicReason::BoardDeficit;
                out.confidence = 0.65;
                commitment.composition_direction.clear();
                commitment.selection_reason = out.reason;
                clear_candidate(commitment);
            } else {
                out.reason = StrategicReason::InsufficientEvidence;
                clear_candidate(commitment);
            }
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        out.anchor_champion_id = best.champion_id;
        out.confidence = best.confidence;
        out.estimated_transition_cost = best.transition_cost;

        if (best.direction == context.current_composition_direction) {
            out.composition_decision = best.shop_available
                ? CompositionDecision::Adapt : CompositionDecision::Keep;
            out.reason = best.shop_available
                ? StrategicReason::AnchorOpportunity
                : StrategicReason::InsufficientEvidence;
            out.target_composition_direction = context.current_composition_direction;
            clear_candidate(commitment);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        out.target_composition_direction = context.current_composition_direction;
        const double required_advantage = std::max(
            config_.minimum_absolute_advantage,
            std::abs(context.current_direction_score) *
                config_.minimum_relative_advantage);
        const double advantage = best.score - context.current_direction_score;

        if (!context.current_direction_viable) {
            out.composition_decision = CompositionDecision::Pivot;
            out.reason = StrategicReason::BoardDeficit;
            out.target_composition_direction = best.direction;
            commitment.composition_direction = best.direction;
            commitment.selected_round = context.round;
            commitment.selection_reason = out.reason;
            commitment.confidence = best.confidence;
            clear_candidate(commitment);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        if (advantage < required_advantage) {
            out.reason = StrategicReason::InsufficientEvidence;
            clear_candidate(commitment);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        if (commitment.candidate_composition_direction == best.direction &&
            commitment.candidate_anchor_id == best.champion_id) {
            ++commitment.consecutive_reviews;
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
        if (commitment.consecutive_reviews < required_reviews) {
            out.reason = StrategicReason::AnchorOpportunity;
            out.confidence = std::min(best.confidence, 0.55);
            classify_owned_units(context, out, out.target_composition_direction);
            return out;
        }

        out.composition_decision = CompositionDecision::Pivot;
        out.reason = StrategicReason::AnchorOpportunity;
        out.target_composition_direction = best.direction;
        commitment.composition_direction = best.direction;
        commitment.selected_round = context.round;
        commitment.selection_reason = out.reason;
        commitment.confidence = best.confidence;
        clear_candidate(commitment);
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

    AnchorScore best_anchor(const StrategicSharedContext& context) const {
        AnchorScore best;
        for (const auto& candidate : context.anchor_candidates) {
            const auto& unit = candidate.unit;
            if (candidate.target_composition_direction.empty() ||
                unit.champion_id < 0 || !std::isfinite(candidate.anchor_value) ||
                !std::isfinite(candidate.transition_cost) ||
                !std::isfinite(candidate.contestation) ||
                !std::isfinite(unit.board_contribution) ||
                !std::isfinite(unit.composition_fit) ||
                !std::isfinite(unit.item_fit)) continue;

            const double reusable = static_cast<double>(
                std::clamp(candidate.reusable_owned_units, 0, 5));
            const double score =
                candidate.anchor_value +
                0.30 * unit.board_contribution +
                0.25 * unit.composition_fit +
                0.20 * unit.item_fit +
                0.35 * reusable -
                0.50 * std::max(0.0, candidate.transition_cost) -
                0.30 * std::max(0.0, candidate.contestation) +
                (candidate.shop_available ? 0.20 : 0.0);
            if (score < config_.minimum_anchor_score || score <= best.score)
                continue;

            best.valid = true;
            best.direction = candidate.target_composition_direction;
            best.champion_id = unit.champion_id;
            best.score = score;
            best.transition_cost = std::max(0.0, candidate.transition_cost);
            best.shop_available = candidate.shop_available;
            best.confidence = std::clamp(
                0.5 + score / (2.0 * (1.0 + std::abs(score))),
                0.5, 0.95);
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
            const bool preserve = unit.is_core ||
                unit.board_contribution >= config_.preserve_board_contribution ||
                unit.item_fit >= config_.preserve_item_fit ||
                (target_trait_fit &&
                 unit.composition_fit >= config_.preserve_target_trait_fit);
            (preserve ? out.preserve_unit_ids : out.replaceable_unit_ids)
                .push_back(unit.champion_id);
        }
    }
};

} // namespace tft::strategy
