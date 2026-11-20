#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cmath>
#include <initializer_list>
#include <utility>

namespace tft::strategy {

// Deterministic shadow-only posture selection. Missing evidence is excluded
// from scoring rather than interpreted as a measured zero/default.
class EconomicController {
public:
    EconomicControlDecision evaluate(const StrategicSharedContext& c) const {
        EconomicControlDecision out;
        out.shadow_only = true;
        if (!c.alive) {
            out.reason = StrategicReason::InsufficientEvidence;
            out.evidence_missing.push_back("player_alive");
            return out;
        }

        // Reject contradictory or out-of-domain evidence before scoring. A
        // clamped invalid value would look plausible and conceal a producer bug.
        const auto reject_if = [&](bool invalid, const char* field) {
            if (invalid) out.evidence_invalid.emplace_back(field);
        };
        reject_if(c.evidence.hp &&
            (!std::isfinite(c.hp) || c.hp < 0.0 || c.hp > 100.0), "hp");
        reject_if(c.evidence.gold && c.gold < 0, "gold");
        reject_if(c.evidence.level && (c.level < 1 || c.level > 10), "level");
        reject_if(c.evidence.xp && c.xp < 0, "xp");
        reject_if(c.evidence.xp_to_next && c.xp_to_next < 0, "xp_to_next");
        reject_if(c.evidence.interest_if_resolved_now &&
            c.interest_if_resolved_now < 0, "interest_if_resolved_now");
        reject_if(c.evidence.streaks &&
            (c.win_streak < 0 || c.loss_streak < 0 ||
                (c.win_streak > 0 && c.loss_streak > 0)), "win_loss_streaks");
        reject_if(c.evidence.board_power &&
            (!std::isfinite(c.board_power) || c.board_power < 0.0), "board_power");
        reject_if(c.evidence.relative_board_power &&
            (!std::isfinite(c.relative_board_power) || c.relative_board_power < 0.0),
            "relative_board_power");
        reject_if(c.evidence.projected_next_round_income &&
            c.projected_next_round_income < 0, "projected_next_round_income");
        reject_if(c.evidence.estimated_incoming_damage &&
            (!std::isfinite(c.estimated_incoming_damage) ||
                c.estimated_incoming_damage < 0.0), "estimated_incoming_damage");
        reject_if(c.evidence.elimination_risk &&
            (!std::isfinite(c.elimination_risk) || c.elimination_risk < 0.0 ||
                c.elimination_risk > 1.0), "elimination_risk");
        if (!out.evidence_invalid.empty()) {
            out.reason = StrategicReason::InsufficientEvidence;
            out.sufficient_evidence = false;
            out.confidence = 0.0;
            return out;
        }

        const auto record = [&](bool available, const char* name) {
            if (available) out.evidence_used.emplace_back(name);
            else out.evidence_missing.emplace_back(name);
        };
        record(c.evidence.hp, "hp");
        record(c.evidence.gold, "gold");
        record(c.evidence.level, "level");
        record(c.evidence.xp_to_next, "xp_to_next");
        record(c.evidence.streaks, "win_loss_streaks");
        record(c.evidence.relative_board_power, "relative_board_power");
        record(c.evidence.projected_next_round_income, "projected_next_round_income");
        record(c.evidence.estimated_incoming_damage, "estimated_incoming_damage");
        record(c.evidence.elimination_risk, "elimination_risk");
        record(c.evidence.progression_plan, "progression_plan");

        const bool survival_available = c.evidence.hp ||
            c.evidence.estimated_incoming_damage || c.evidence.elimination_risk;
        const bool board_available = c.evidence.relative_board_power;
        const bool economy_available = c.evidence.gold;
        const bool streak_available = c.evidence.streaks;
        const bool progression_available = c.evidence.progression_plan;
        const bool level_available = c.evidence.level && c.evidence.xp_to_next;
        const int available_groups = static_cast<int>(survival_available) +
            static_cast<int>(board_available) + static_cast<int>(economy_available) +
            static_cast<int>(streak_available) + static_cast<int>(progression_available) +
            static_cast<int>(level_available);
        const int total_groups = 6;
        if (available_groups < 2) {
            out.reason = StrategicReason::InsufficientEvidence;
            return out;
        }
        out.sufficient_evidence = true;

        const double hp_pressure = c.evidence.hp
            ? clamp01((70.0 - c.hp) / 70.0) : 0.0;
        const double incoming_pressure = c.evidence.estimated_incoming_damage
            ? clamp01(c.estimated_incoming_damage / 18.0) : 0.0;
        const double elimination_pressure = c.evidence.elimination_risk
            ? clamp01(c.elimination_risk) : 0.0;
        const double board_pressure = board_available
            ? clamp01((1.05 - c.relative_board_power) / 0.75) : 0.0;
        const double economy_pressure = economy_available
            ? clamp01(static_cast<double>(c.gold - 30) / 50.0) : 0.0;
        const double streak_strength = streak_available
            ? clamp01(static_cast<double>(std::max(c.win_streak, c.loss_streak)) / 6.0)
            : 0.0;

        double survival_sum = 0.0;
        double survival_weight = 0.0;
        if (c.evidence.hp) { survival_sum += 0.50 * hp_pressure; survival_weight += 0.50; }
        if (c.evidence.estimated_incoming_damage) {
            survival_sum += 0.25 * incoming_pressure; survival_weight += 0.25;
        }
        if (c.evidence.elimination_risk) {
            survival_sum += 0.25 * elimination_pressure; survival_weight += 0.25;
        }
        if (survival_weight > 0.0)
            out.survival_pressure = clamp01(survival_sum / survival_weight);
        if (board_available) out.board_pressure = board_pressure;
        if (economy_available) out.economy_pressure = economy_pressure;

        double scores[7] = {};
        double accumulate_sum = 0.0;
        double accumulate_weight = 0.0;
        if (survival_available) {
            accumulate_sum += 0.20 * (1.0 - out.survival_pressure);
            accumulate_weight += 0.20;
        }
        if (board_available) {
            accumulate_sum += 0.25 * (1.0 - board_pressure);
            accumulate_weight += 0.25;
        }
        if (economy_available) {
            accumulate_sum += 0.10 * (1.0 - economy_pressure);
            accumulate_weight += 0.10;
        }
        if (accumulate_weight > 0.0)
            scores[static_cast<int>(EconomicPosture::AccumulateResources)] = accumulate_sum;

        if (streak_available && c.win_streak > 0) {
            scores[static_cast<int>(EconomicPosture::PreserveWinStreak)] =
                0.35 + 0.45 * clamp01(c.win_streak / 6.0) +
                (board_available ? 0.35 * clamp01((c.relative_board_power - 0.90) / 0.60) : 0.0) +
                (survival_available ? 0.15 * (1.0 - out.survival_pressure) : 0.0) +
                0.05 * streak_strength;
        }
        if (streak_available && c.loss_streak > 0) {
            scores[static_cast<int>(EconomicPosture::PreserveLossStreak)] =
                0.20 + 0.30 * clamp01(c.loss_streak / 6.0) +
                (survival_available ? 0.25 * (1.0 - out.survival_pressure) : 0.0) -
                (board_available ? 0.20 * clamp01(c.relative_board_power) : 0.0) +
                0.05 * streak_strength;
        }

        if (level_available && economy_available) {
            const double plan_weight = progression_available
                ? (c.progression_plan == ProgressionPlan::LevelToEight ? 0.48 :
                    (c.progression_plan == ProgressionPlan::LevelToNine ? 0.56 : 0.0))
                : 0.0;
            scores[static_cast<int>(EconomicPosture::InvestExperience)] =
                plan_weight + 0.20 * clamp01((c.stage - 3.0) / 3.0) +
                0.18 * clamp01((8.0 - c.level) / 4.0) +
                0.14 * economy_pressure -
                (survival_available ? 0.28 * out.survival_pressure : 0.0);
        }

        if (c.evidence.level && economy_available) {
            const double plan_weight = progression_available &&
                c.progression_plan == ProgressionPlan::RerollForThreeStar ? 0.52 : 0.0;
            scores[static_cast<int>(EconomicPosture::RollForUpgrades)] =
                plan_weight + 0.18 * clamp01((c.gold - 20.0) / 40.0) +
                0.16 * clamp01((c.level - 4.0) / 3.0) -
                (survival_available ? 0.22 * out.survival_pressure : 0.0);
        }

        if (survival_available || board_available) {
            scores[static_cast<int>(EconomicPosture::StabilizeBoard)] =
                (survival_available ? 0.45 * out.survival_pressure : 0.0) +
                (board_available ? 0.55 * board_pressure : 0.0) +
                (economy_available && board_available
                    ? 0.25 * economy_pressure * board_pressure : 0.0) +
                (c.evidence.estimated_incoming_damage
                    ? 0.10 * clamp01(c.estimated_incoming_damage / 12.0) : 0.0);
            scores[static_cast<int>(EconomicPosture::EmergencyInvestment)] =
                (survival_available ? 0.80 * out.survival_pressure : 0.0) +
                (board_available ? 0.20 * board_pressure : 0.0) +
                (c.evidence.elimination_risk ? 0.15 * elimination_pressure : 0.0) +
                (c.evidence.hp ? 0.20 * hp_pressure : 0.0);
        }

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
        const double margin = std::max(0.0, scores[best] - std::max(0.0, second));
        const double evidence_coverage = static_cast<double>(available_groups) / total_groups;
        out.confidence = std::clamp(
            (0.50 + margin * 0.45) * evidence_coverage, 0.0, 0.90);

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
