#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>

namespace tft::strategy {

// Ranks diagnostic candidates only. All numerical components are heuristic
// proxies; none represents a calibrated HP/streak prediction or changes PPO.
class ActionEvaluator {
public:
    ActionEvaluation evaluate(
        const StrategicSharedContext& c,
        const EconomicControlDecision& posture,
        StrategicActionKind policy_action = StrategicActionKind::None) const {
        ActionEvaluation out;
        out.recommended_action = StrategicActionKind::Hold;
        out.reason = StrategicReason::InsufficientEvidence;
        if (!c.alive) return out;

        double best_score = 0.0; // HOLD is the explicit zero-cost baseline.
        double second_score = -1.0e9;
        for (const auto& candidate : c.action_candidates) {
            ActionCandidateScore breakdown;
            breakdown.kind = candidate.kind;
            breakdown.champion_id = candidate.champion_id;
            breakdown.available = candidate.available &&
                candidate.gold_cost <= c.gold;
            breakdown.direct_gold_cost = candidate.direct_gold_cost;
            breakdown.lost_interest_cost = candidate.lost_interest_cost;
            breakdown.opportunity_cost = candidate.opportunity_cost;
            if (!breakdown.available) {
                breakdown.total_score = -1.0e9;
                breakdown.available = false;
                out.candidate_scores.push_back(breakdown);
                continue;
            }

            const double board_gain = candidate.expected_board_delta;
            const double positive_board_gain = std::max(0.0, board_gain);
            const double survival_multiplier = 0.75 +
                std::clamp(posture.survival_pressure, 0.0, 1.0) * 0.90;
            const double streak_multiplier =
                (c.win_streak >= 2 || c.loss_streak >= 2) ? 1.12 : 1.0;
            breakdown.board_component = board_gain * 0.75;
            breakdown.survival_component = board_gain *
                (survival_multiplier - 0.75);
            breakdown.streak_component = board_gain * survival_multiplier *
                (streak_multiplier - 1.0);
            breakdown.composition_component =
                std::clamp(candidate.composition_fit, 0.0, 1.0) * 0.18;
            breakdown.upgrade_component =
                std::clamp(candidate.upgrade_value, 0.0, 1.0) * 0.28;

            switch (posture.posture) {
                case EconomicPosture::AccumulateResources:
                    if (candidate.kind == StrategicActionKind::Hold)
                        breakdown.posture_component = 0.24;
                    break;
                case EconomicPosture::PreserveWinStreak:
                case EconomicPosture::PreserveLossStreak:
                    if (candidate.kind == StrategicActionKind::BuyUnit ||
                        candidate.kind == StrategicActionKind::DeployOrMove)
                        breakdown.posture_component = board_gain > 0.20 ? 0.18 : -0.08;
                    break;
                case EconomicPosture::InvestExperience:
                    if (candidate.kind == StrategicActionKind::BuyExperience)
                        breakdown.posture_component = 0.22;
                    break;
                case EconomicPosture::RollForUpgrades:
                    if (candidate.kind == StrategicActionKind::RerollShop ||
                        candidate.kind == StrategicActionKind::BuyUnit)
                        breakdown.posture_component = 0.18;
                    break;
                case EconomicPosture::StabilizeBoard:
                case EconomicPosture::EmergencyInvestment:
                    if (candidate.kind == StrategicActionKind::BuyUnit ||
                        candidate.kind == StrategicActionKind::BuyExperience ||
                        candidate.kind == StrategicActionKind::DeployOrMove)
                        breakdown.posture_component = 0.24;
                    break;
            }

            const double direct_cost = candidate.direct_gold_cost != 0.0
                ? std::max(0.0, candidate.direct_gold_cost)
                : std::max(0.0, candidate.expected_economy_cost);
            const double gold_gain = std::max(0.0, -candidate.direct_gold_cost);
            const double lost_interest = std::max(0.0, candidate.lost_interest_cost);
            const double opportunity_cost = std::max(0.0, candidate.opportunity_cost);
            breakdown.direct_cost_component = -direct_cost * 0.055 + gold_gain * 0.035;
            breakdown.lost_interest_component = -lost_interest * 0.10;
            breakdown.opportunity_cost_component = -opportunity_cost * 0.10;
            breakdown.total_score =
                breakdown.board_component + breakdown.survival_component +
                breakdown.streak_component + breakdown.composition_component +
                breakdown.upgrade_component +
                breakdown.posture_component + breakdown.direct_cost_component +
                breakdown.lost_interest_component +
                breakdown.opportunity_cost_component;

            if (breakdown.total_score > best_score) {
                second_score = best_score;
                best_score = breakdown.total_score;
                out.recommended_action = candidate.kind;
                out.recommended_champion_id = candidate.champion_id;
                out.reason = reason_for(candidate, c);
                out.expected_board_delta = candidate.expected_board_delta;
                // These are deliberately named as proxies in the audit schema.
                out.expected_hp_preservation = positive_board_gain *
                    (0.10 + posture.survival_pressure * 0.35);
                out.expected_direct_gold_cost = candidate.direct_gold_cost;
                out.expected_lost_interest_cost = lost_interest;
                out.expected_opportunity_cost = opportunity_cost;
                out.expected_economy_cost = direct_cost + lost_interest +
                    opportunity_cost - gold_gain;
            } else {
                second_score = std::max(second_score, breakdown.total_score);
            }
            out.candidate_scores.push_back(breakdown);
        }

        for (auto& candidate : out.candidate_scores) {
            candidate.selected = candidate.kind == out.recommended_action &&
                candidate.champion_id == out.recommended_champion_id &&
                ((best_score > 0.0 && candidate.total_score == best_score) ||
                 (best_score <= 0.0 && candidate.kind == StrategicActionKind::Hold));
        }
        if (best_score <= 0.0) {
            out.recommended_action = StrategicActionKind::Hold;
            out.recommended_champion_id = -1;
            out.expected_board_delta = 0.0;
            out.expected_hp_preservation = 0.0;
            out.expected_economy_cost = 0.0;
            out.expected_direct_gold_cost = 0.0;
            out.expected_lost_interest_cost = 0.0;
            out.expected_opportunity_cost = 0.0;
            out.expected_streak_value = 0.0;
            out.confidence = 0.0;
        } else {
            out.confidence = std::clamp(
                0.50 + (best_score - std::max(0.0, second_score)) * 0.30,
                0.50, 0.90);
            out.expected_streak_value = std::max(0.0, out.expected_board_delta) *
                ((c.win_streak > 0 || c.loss_streak > 0) ? 0.20 : 0.05);
        }
        out.differs_from_policy_action =
            policy_action != StrategicActionKind::None &&
            out.recommended_action != policy_action;
        return out;
    }

private:
    static StrategicReason reason_for(
        const StrategicActionCandidate& candidate,
        const StrategicSharedContext& context) noexcept {
        switch (candidate.kind) {
            case StrategicActionKind::BuyExperience:
                return StrategicReason::ProgressionTiming;
            case StrategicActionKind::RerollShop:
                return StrategicReason::UpgradeOpportunity;
            case StrategicActionKind::BuyUnit:
                if (candidate.upgrade_value > 0.5)
                    return StrategicReason::UpgradeOpportunity;
                if (candidate.composition_fit > 0.6)
                    return StrategicReason::AnchorOpportunity;
                return StrategicReason::EconomyConstraint;
            case StrategicActionKind::Hold:
                return (context.win_streak > 0 || context.loss_streak > 0)
                    ? StrategicReason::BoardAdvantage
                    : StrategicReason::EconomyConstraint;
            case StrategicActionKind::DeployOrMove:
                return StrategicReason::BoardDeficit;
            case StrategicActionKind::SellUnit:
                return StrategicReason::EconomyConstraint;
            case StrategicActionKind::None:
                break;
        }
        return StrategicReason::InsufficientEvidence;
    }
};

} // namespace tft::strategy
