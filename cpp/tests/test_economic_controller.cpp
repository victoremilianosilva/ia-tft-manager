#include "strategy/EconomicController.hpp"

#include <algorithm>
#include <cassert>
#include <iostream>

using namespace tft::strategy;

namespace {
bool contains(const std::vector<std::string>& values, const std::string& value) {
    return std::find(values.begin(), values.end(), value) != values.end();
}

void empty_defaults_are_not_treated_as_observations() {
    StrategicSharedContext context;
    context.alive = true;
    const auto result = EconomicController{}.evaluate(context);
    assert(!result.sufficient_evidence);
    assert(result.reason == StrategicReason::InsufficientEvidence);
    assert(result.confidence == 0.0);
    assert(contains(result.evidence_missing, "hp"));
    assert(contains(result.evidence_missing, "gold"));
    assert(contains(result.evidence_missing, "relative_board_power"));
}

void observed_zero_and_extreme_values_remain_valid_evidence() {
    StrategicSharedContext context;
    context.alive = true;
    context.hp = 100.0;
    context.gold = 0;
    context.level = 2;
    context.xp = 0;
    context.xp_to_next = 2;
    context.win_streak = 0;
    context.loss_streak = 0;
    context.relative_board_power = 0.0;
    context.evidence.hp = true;
    context.evidence.gold = true;
    context.evidence.level = true;
    context.evidence.xp = true;
    context.evidence.xp_to_next = true;
    context.evidence.streaks = true;
    context.evidence.relative_board_power = true;

    const auto result = EconomicController{}.evaluate(context);
    assert(result.sufficient_evidence);
    assert(contains(result.evidence_used, "gold"));
    assert(contains(result.evidence_used, "win_loss_streaks"));
    assert(contains(result.evidence_used, "relative_board_power"));
    // XP, current interest and absolute board power are available elsewhere,
    // but they are not inputs to this posture score.
    assert(!contains(result.evidence_used, "xp"));
    assert(!contains(result.evidence_used, "interest_if_resolved_now"));
    assert(!contains(result.evidence_used, "board_power"));
    assert(result.economy_pressure == 0.0);
    assert(result.survival_pressure == 0.0);
    assert(result.board_pressure == 1.0);
    assert(result.confidence > 0.0);
}

void progression_opportunity_uses_observed_stage_level_and_gold_without_a_legacy_plan() {
    StrategicSharedContext context;
    context.alive = true;
    context.stage = 6;
    context.hp = 100.0;
    context.gold = 50;
    context.level = 4;
    context.xp_to_next = 4;
    context.relative_board_power = 0.6;
    context.evidence.hp = true;
    context.evidence.gold = true;
    context.evidence.level = true;
    context.evidence.xp_to_next = true;
    context.evidence.relative_board_power = true;
    // No progression-plan producer is present in this cycle.
    context.evidence.progression_plan = false;
    const auto result = EconomicController{}.evaluate(context);
    assert(result.sufficient_evidence);
    assert(contains(result.evidence_missing, "progression_plan"));
    assert(result.posture == EconomicPosture::InvestExperience);
    assert(result.reason == StrategicReason::ProgressionTiming);
}

void missing_damage_risk_income_and_progression_stay_explicitly_missing() {
    StrategicSharedContext context;
    context.alive = true;
    context.hp = 45.0;
    context.gold = 35;
    context.level = 6;
    context.xp_to_next = 4;
    context.relative_board_power = 0.8;
    context.evidence.hp = true;
    context.evidence.gold = true;
    context.evidence.level = true;
    context.evidence.xp_to_next = true;
    context.evidence.relative_board_power = true;

    const auto result = EconomicController{}.evaluate(context);
    assert(result.sufficient_evidence);
    assert(contains(result.evidence_used, "hp"));
    assert(contains(result.evidence_missing, "estimated_incoming_damage"));
    assert(contains(result.evidence_missing, "elimination_risk"));
    assert(contains(result.evidence_missing, "projected_next_round_income"));
    assert(contains(result.evidence_missing, "progression_plan"));
    // HP is the only validated survival signal; unavailable projections do not add pressure.
    assert(result.survival_pressure > 0.0);
}
}

int main() {
    empty_defaults_are_not_treated_as_observations();
    observed_zero_and_extreme_values_remain_valid_evidence();
    progression_opportunity_uses_observed_stage_level_and_gold_without_a_legacy_plan();
    missing_damage_risk_income_and_progression_stay_explicitly_missing();
    std::cout << "EconomicController tests passed\\n";
}
