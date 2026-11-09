#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>

namespace tft::strategy {

// Ranks only the candidate actions supplied by the caller. The result is an
// audit recommendation: it is not an action mask, override, or PPO input.
class ActionEvaluator {
public:
    ActionEvaluation evaluate(
        const StrategicSharedContext& c,
        const EconomicControlDecision& posture,
        StrategicActionKind policy_action = StrategicActionKind::None) const noexcept {
        ActionEvaluation out;
        out.recommended_action = StrategicActionKind::Hold;
        out.reason = StrategicReason::InsufficientEvidence;
        out.confidence = 0.0;

        double best_score = -1.0e9;
        double second_score = -1.0e9;
        for (const auto& candidate : c.action_candidates) {
            if (!candidate.available) continue;
            const double board_gain = std::max(0.0, candidate.expected_board_delta);
            const double survival_multiplier = 0.75 + posture.survival_pressure * 0.90;
            const double streak_multiplier =
                (c.win_streak >= 2 || c.loss_streak >= 2) ? 1.12 : 1.0;
            const double fit_bonus = std::clamp(candidate.composition_fit, 0.0, 1.0) * 0.18;
            const double upgrade_bonus = std::clamp(candidate.upgrade_value, 0.0, 1.0) * 0.28;

            double posture_bonus = 0.0;
            switch (posture.posture) {
                case EconomicPosture::AccumulateResources:
                    if (candidate.kind == StrategicActionKind::Hold) posture_bonus = 0.24;
                    break;
                case EconomicPosture::PreserveWinStreak:
                case EconomicPosture::PreserveLossStreak:
                    if (candidate.kind == StrategicActionKind::BuyUnit ||
                        candidate.kind == StrategicActionKind::DeployOrMove)
                        posture_bonus = board_gain > 0.20 ? 0.18 : -0.08;
                    break;
                case EconomicPosture::InvestExperience:
                    if (candidate.kind == StrategicActionKind::BuyExperience)
                        posture_bonus = 0.22;
                    break;
                case EconomicPosture::RollForUpgrades:
                    if (candidate.kind == StrategicActionKind::RerollShop ||
                        candidate.kind == StrategicActionKind::BuyUnit)
                        posture_bonus = 0.18;
                    break;
                case EconomicPosture::StabilizeBoard:
                case EconomicPosture::EmergencyInvestment:
                    if (candidate.kind == StrategicActionKind::BuyUnit ||
                        candidate.kind == StrategicActionKind::BuyExperience ||
                        candidate.kind == StrategicActionKind::DeployOrMove)
                        posture_bonus = 0.24;
                    break;
            }

            const double cost = std::max(0.0, candidate.expected_economy_cost);
            const double score = (board_gain * survival_multiplier * streak_multiplier) +
                fit_bonus + upgrade_bonus + posture_bonus - cost * 0.055;

            if (score > best_score) {
                second_score = best_score;
                best_score = score;
                out.recommended_action = candidate.kind;
                out.reason = reason_for(candidate);
                out.expected_board_delta = candidate.expected_board_delta;
                out.expected_hp_preservation = board_gain *
                    (0.10 + posture.survival_pressure * 0.35);
                out.expected_economy_cost = cost;
                out.expected_streak_value = board_gain *
                    ((c.win_streak > 0 || c.loss_streak > 0) ? 0.20 : 0.05);
            } else {
                second_score = std::max(second_score, score);
            }
        }

        if (best_score <= -1.0e8) return out;
        out.confidence = std::clamp(
            0.50 + (best_score - std::max(-0.5, second_score)) * 0.30,
            0.50, 0.90);
        out.differs_from_policy_action =
            policy_action != StrategicActionKind::None &&
            out.recommended_action != policy_action;
        return out;
    }

private:
    static StrategicReason reason_for(
        const StrategicActionCandidate& candidate) noexcept {
        if (candidate.upgrade_value > 0.5)
            return StrategicReason::UpgradeOpportunity;
        if (candidate.composition_fit > 0.6)
            return StrategicReason::AnchorOpportunity;
        if (candidate.gold_cost > 0)
            return StrategicReason::EconomyConstraint;
        return StrategicReason::InsufficientEvidence;
    }
};

} // namespace tft::strategy
