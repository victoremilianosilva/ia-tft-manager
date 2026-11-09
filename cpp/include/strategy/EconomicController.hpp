#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>

namespace tft::strategy {

// Deterministic shadow-only posture selection. Scores are relative heuristics,
// not calibrated probabilities and never restrict the action space.
class EconomicController {
public:
    EconomicControlDecision evaluate(const StrategicSharedContext& c) const noexcept {
        EconomicControlDecision out;
        out.shadow_only = true;
        if (!c.alive) {
            out.reason = StrategicReason::InsufficientEvidence;
            return out;
        }

        const double hp_pressure = clamp01((70.0 - c.hp) / 70.0);
        const double incoming_pressure = clamp01(c.estimated_incoming_damage / 18.0);
        const double elimination_pressure = clamp01(c.elimination_risk);
        const double board_pressure = clamp01((1.05 - c.relative_board_power) / 0.75);
        const double economy_pressure = clamp01(
            static_cast<double>(c.gold - 30) / 50.0);
        const double streak_strength = clamp01(
            static_cast<double>(std::max(c.win_streak, c.loss_streak)) / 6.0);

        out.survival_pressure = clamp01(
            0.50 * hp_pressure + 0.25 * incoming_pressure +
            0.25 * elimination_pressure);
        out.board_pressure = board_pressure;
        out.economy_pressure = economy_pressure;

        double scores[7] = {};
        scores[static_cast<int>(EconomicPosture::AccumulateResources)] =
            0.20 * (1.0 - out.survival_pressure) +
            0.25 * (1.0 - board_pressure) +
            0.10 * (1.0 - economy_pressure);

        scores[static_cast<int>(EconomicPosture::PreserveWinStreak)] =
            c.win_streak > 0
                ? 0.35 + 0.45 * clamp01(c.win_streak / 6.0) +
                  0.35 * clamp01((c.relative_board_power - 0.90) / 0.60) +
                  0.15 * (1.0 - out.survival_pressure)
                : 0.0;

        scores[static_cast<int>(EconomicPosture::PreserveLossStreak)] =
            c.loss_streak > 0
                ? 0.20 + 0.30 * clamp01(c.loss_streak / 6.0) +
                  0.25 * (1.0 - out.survival_pressure) -
                  0.20 * clamp01(c.relative_board_power)
                : 0.0;

        const double experience_plan_weight =
            c.progression_plan == ProgressionPlan::LevelToEight ? 0.48 :
            (c.progression_plan == ProgressionPlan::LevelToNine ? 0.56 : 0.0);
        scores[static_cast<int>(EconomicPosture::InvestExperience)] =
            experience_plan_weight +
            0.20 * clamp01((c.stage - 3.0) / 3.0) +
            0.18 * clamp01((8.0 - c.level) / 4.0) +
            0.14 * economy_pressure -
            0.28 * out.survival_pressure;

        scores[static_cast<int>(EconomicPosture::RollForUpgrades)] =
            (c.progression_plan == ProgressionPlan::RerollForThreeStar ? 0.52 : 0.0) +
            0.18 * clamp01((c.gold - 20.0) / 40.0) +
            0.16 * clamp01((c.level - 4.0) / 3.0) -
            0.22 * out.survival_pressure;

        scores[static_cast<int>(EconomicPosture::StabilizeBoard)] =
            0.45 * out.survival_pressure + 0.55 * board_pressure +
            0.25 * economy_pressure * board_pressure +
            0.10 * clamp01(c.estimated_incoming_damage / 12.0);

        scores[static_cast<int>(EconomicPosture::EmergencyInvestment)] =
            0.80 * out.survival_pressure + 0.20 * board_pressure +
            0.15 * elimination_pressure + 0.20 * hp_pressure;

        int best = 0;
        double second = -1.0;
        for (int i = 1; i < 7; ++i) {
            if (scores[i] > scores[best]) {
                second = scores[best];
                best = i;
            } else {
                second = std::max(second, scores[i]);
            }
        }
        out.posture = static_cast<EconomicPosture>(best);
        out.confidence = std::clamp(
            0.50 + (scores[best] - std::max(0.0, second)) * 0.45,
            0.50, 0.90);

        switch (out.posture) {
            case EconomicPosture::AccumulateResources:
                out.reason = StrategicReason::EconomyConstraint; break;
            case EconomicPosture::PreserveWinStreak:
                out.reason = StrategicReason::BoardAdvantage; break;
            case EconomicPosture::PreserveLossStreak:
                out.reason = StrategicReason::BoardDeficit; break;
            case EconomicPosture::InvestExperience:
                out.reason = StrategicReason::ProgressionTiming; break;
            case EconomicPosture::RollForUpgrades:
                out.reason = StrategicReason::UpgradeOpportunity; break;
            case EconomicPosture::StabilizeBoard:
            case EconomicPosture::EmergencyInvestment:
                out.reason = out.survival_pressure >= out.board_pressure
                    ? StrategicReason::SurvivalPressure
                    : StrategicReason::BoardDeficit;
                break;
        }
        return out;
    }

private:
    static double clamp01(double value) noexcept {
        return std::clamp(value, 0.0, 1.0);
    }
};

} // namespace tft::strategy
