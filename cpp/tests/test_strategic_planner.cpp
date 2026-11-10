#include "strategy/StrategicPlanner.hpp"
#include "strategy/EconomicController.hpp"
#include "strategy/ActionEvaluator.hpp"

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>

using namespace tft::strategy;

namespace {
StrategicSharedContext base_context() {
    StrategicSharedContext c;
    c.round = 20;
    c.hp = 65.0;
    c.gold = 45;
    c.level = 7;
    c.current_composition_direction = "Bruiser";
    c.current_direction_viable = true;
    c.current_direction_score = 5.0;
    c.composition_locked = true;
    c.owned_units = {
        StrategicUnitCandidate{10, "HighCostCarry", 4, 2, 3, true, false,
            true, 1.0, 0.8, 0.9, {"Bruiser", "Invoker"}},
        StrategicUnitCandidate{11, "FlexibleTank", 3, 2, 3, true, false,
            false, 0.8, 0.6, 0.1, {"Warden"}},
        StrategicUnitCandidate{12, "LowValueUnit", 1, 1, 1, false, true,
            false, 0.1, 0.1, 0.0, {"Duelist"}},
        StrategicUnitCandidate{13, "WeakOldCore", 1, 1, 1, true, false,
            true, 0.1, 0.0, 0.0, {"Bruiser"}}
    };
    return c;
}
StrategicAnchorCandidate anchor(
    std::int32_t id, const std::string& direction, double value,
    double transition, std::int32_t reusable, bool shop = true) {
    StrategicAnchorCandidate a;
    a.unit.champion_id = id;
    a.unit.champion_key = "Anchor";
    a.unit.cost = 5;
    a.unit.star = 1;
    a.unit.board_contribution = 0.4;
    a.unit.composition_fit = 0.9;
    a.unit.item_fit = 0.8;
    a.target_composition_direction = direction;
    a.anchor_value = value;
    a.transition_cost = transition;
    a.reusable_owned_units = reusable;
    a.shop_available = shop;
    return a;
}
}

int main() {
    StrategicPlanner planner;
    auto context = base_context();
    StrategicCommitment commitment;

    // Existing pieces are preserved; a poor pivot candidate is ignored.
    context.anchor_candidates.push_back(anchor(90, "Invoker", 1.0, 4.0, 0));
    auto decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::InsufficientEvidence);
    assert(!decision.candidate_diagnostics.empty());
    assert(!decision.candidate_diagnostics.front().accepted);
    assert(decision.target_composition_direction == "Bruiser");
    assert(decision.decision_path_reason == "all_anchor_candidates_rejected");
    assert(decision.anchor_confidence == 0.0);
    assert(decision.current_direction_confidence > 0.0);
    assert(std::find(decision.preserve_unit_ids.begin(),
                     decision.preserve_unit_ids.end(), 10) != decision.preserve_unit_ids.end());

    // An alternative with less than the minimum ADAPT advantage is explicitly
    // classified, with current and anchor confidence kept separate.
    context.anchor_candidates.clear();
    context.current_direction_score = 5.0;
    context.anchor_candidates.push_back(anchor(88, "Invoker", 3.9, 0.2, 2));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::InsufficientEvidence);
    assert(decision.decision_path_reason == "alternative_below_minimum_adapt_advantage");
    assert(decision.alternative_advantage < decision.minimum_adapt_advantage);
    assert(decision.required_pivot_advantage == 1.0);
    assert(decision.anchor_confidence > 0.0);
    assert(decision.current_direction_confidence > 0.0);
    assert(decision.anchor_confidence != decision.current_direction_confidence);

    // A candidate direction can be refined without pivoting away from the
    // current composition.
    context.anchor_candidates.clear();
    context.anchor_candidates.push_back(anchor(89, "Bruiser", 4.0, 0.2, 2));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Keep);
    assert(decision.target_composition_direction == "Bruiser");

    // A candidate above the ADAPT floor but below the absolute/relative
    // pivot threshold must report the exact limiting threshold.
    context = base_context();
    commitment = {};
    context.anchor_candidates.push_back(anchor(87, "Invoker", 4.3, 0.2, 2));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Adapt);
    assert(decision.alternative_advantage >= decision.minimum_adapt_advantage);
    assert(decision.alternative_advantage < decision.required_pivot_advantage);
    assert(decision.decision_path_reason == "alternative_below_required_advantage");

    // A strong anchor cannot trigger a pivot on a single review while locked.
    context.anchor_candidates.clear();
    context.current_direction_score = 1.0;
    context.anchor_candidates.push_back(anchor(91, "Invoker", 6.0, 0.2, 2));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Adapt);
    assert(decision.decision_path_reason == "alternative_waiting_for_persistence");
    assert(commitment.consecutive_reviews == 1);
    assert(commitment.candidate_composition_direction == "Invoker");

    // Repeated actions in the same round do not count as independent evidence.
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Adapt);
    assert(commitment.consecutive_reviews == 1);

    context.round++;
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Adapt);
    assert(commitment.consecutive_reviews == 2);

    context.round++;
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Pivot);
    assert(decision.target_composition_direction == "Invoker");
    assert(std::find(decision.replaceable_unit_ids.begin(),
                     decision.replaceable_unit_ids.end(), 13) !=
           decision.replaceable_unit_ids.end());
    assert(decision.shadow_only);
    assert(commitment.composition_direction == "Bruiser");
    assert(commitment.consecutive_reviews == 3);
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Pivot);
    assert(decision.target_composition_direction == "Invoker");
    assert(commitment.composition_direction == "Bruiser");

    // A high-cost unit with poor fit and excessive transition cost is rejected.
    context = base_context();
    commitment = {};
    context.anchor_candidates.push_back(anchor(92, "Mage", 0.5, 10.0, 0));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::InsufficientEvidence);

    // If the old direction is no longer viable, a supported alternative can
    // be selected immediately; it does not wait for the locked-plan timer.
    context.current_direction_viable = false;
    context.anchor_candidates.clear();
    context.anchor_candidates.push_back(anchor(93, "Ranger", 4.0, 0.5, 1));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Pivot);
    assert(decision.target_composition_direction == "Ranger");

    // If the current direction is unviable and no alternative exists, abandon
    // the old direction without inventing a replacement.
    context.anchor_candidates.clear();
    context.candidate_generation.no_candidate_reason = "no_high_cost_anchor_units_seen";
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Abandon);
    assert(decision.decision_path_reason == "current_direction_unviable_without_alternative");
    assert(decision.target_composition_direction.empty());

    // An empty initial direction can be initialized from a viable anchor.
    context.current_composition_direction.clear();
    context.current_direction_viable = false;
    context.anchor_candidates.push_back(anchor(94, "Warden", 3.0, 1.0, 1));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::InitialSelection);
    assert(decision.target_composition_direction == "Warden");

    // Invalid numeric candidates never become anchors.
    context.anchor_candidates.clear();
    auto invalid = anchor(95, "Assassin", 5.0, 0.1, 1);
    invalid.unit.item_fit = std::nan("");
    context.anchor_candidates.push_back(invalid);
    context.current_composition_direction.clear();
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::InsufficientEvidence);
    assert(decision.anchor_champion_id == -1);

    // Economic posture is contextual: a strong win streak can outweigh
    // passive accumulation, while survival pressure can justify investment.
    EconomicController economic_controller;
    StrategicSharedContext economy_context;
    economy_context.alive = true;
    economy_context.hp = 90.0;
    economy_context.gold = 40;
    economy_context.level = 7;
    economy_context.stage = 4;
    economy_context.relative_board_power = 1.20;
    economy_context.win_streak = 5;
    auto posture = economic_controller.evaluate(economy_context);
    assert(posture.posture == EconomicPosture::PreserveWinStreak);
    assert(posture.shadow_only);
    assert(posture.confidence >= 0.50);

    economy_context.hp = 20.0;
    economy_context.relative_board_power = 0.65;
    economy_context.win_streak = 0;
    posture = economic_controller.evaluate(economy_context);
    assert(posture.posture == EconomicPosture::EmergencyInvestment);
    assert(posture.survival_pressure > 0.0);
    assert(posture.board_pressure > 0.0);

    StrategicSharedContext progression_context;
    progression_context.hp = 90.0;
    progression_context.gold = 50;
    progression_context.level = 6;
    progression_context.stage = 4;
    progression_context.relative_board_power = 1.0;
    progression_context.progression_plan = ProgressionPlan::LevelToEight;
    const auto xp_posture = economic_controller.evaluate(progression_context);
    assert(xp_posture.posture == EconomicPosture::InvestExperience);
    progression_context.progression_plan = ProgressionPlan::RerollForThreeStar;
    const auto roll_posture = economic_controller.evaluate(progression_context);
    assert(roll_posture.posture == EconomicPosture::RollForUpgrades);

    // A surplus player with a materially weak board should consider
    // converting resources into strength instead of accumulating indefinitely.
    StrategicSharedContext surplus_context;
    surplus_context.hp = 82.0;
    surplus_context.gold = 80;
    surplus_context.level = 6;
    surplus_context.stage = 4;
    surplus_context.relative_board_power = 0.70;
    const auto surplus_posture = economic_controller.evaluate(surplus_context);
    assert(surplus_posture.posture == EconomicPosture::StabilizeBoard);

    // Marginal action evaluation compares candidates against expected benefit
    // and opportunity cost; it does not mutate the context.
    ActionEvaluator action_evaluator;
    economy_context.hp = 48.0;
    economy_context.gold = 35;
    economy_context.relative_board_power = 0.75;
    economy_context.action_candidates.clear();
    StrategicActionCandidate hold;
    hold.kind = StrategicActionKind::Hold;
    economy_context.action_candidates.push_back(hold);
    StrategicActionCandidate purchase;
    purchase.kind = StrategicActionKind::BuyUnit;
    purchase.champion_id = 123;
    purchase.gold_cost = 3;
    purchase.expected_economy_cost = 3.0;
    purchase.expected_board_delta = 0.62;
    purchase.composition_fit = 0.80;
    purchase.upgrade_value = 0.50;
    economy_context.action_candidates.push_back(purchase);
    posture = economic_controller.evaluate(economy_context);
    const auto action = action_evaluator.evaluate(economy_context, posture);
    assert(action.recommended_action == StrategicActionKind::BuyUnit);
    assert(action.expected_economy_cost == 3.0);
    assert(action.expected_board_delta == 0.62);
    assert(action.confidence >= 0.50);
    assert(economy_context.action_candidates.size() == 2);
    assert(!action.candidate_scores.empty());

    // Reroll's search opportunity cost is intentionally higher than buying XP.
    StrategicActionCandidate xp_candidate;
    xp_candidate.kind = StrategicActionKind::BuyExperience;
    xp_candidate.gold_cost = 4;
    xp_candidate.direct_gold_cost = 4.0;
    xp_candidate.opportunity_cost = 0.25;
    StrategicActionCandidate reroll_candidate;
    reroll_candidate.kind = StrategicActionKind::RerollShop;
    reroll_candidate.gold_cost = 2;
    reroll_candidate.direct_gold_cost = 2.0;
    reroll_candidate.opportunity_cost = 2.50;
    reroll_candidate.opportunity_cost =
        action_opportunity_cost::kRerollWithUpgradeTarget;
    xp_candidate.opportunity_cost = action_opportunity_cost::kBuyExperience;
    assert(reroll_candidate.opportunity_cost > xp_candidate.opportunity_cost);
    // Even if XP crosses one extra interest threshold, reroll remains the
    // more expensive opportunity once its search premium is included.
    reroll_candidate.lost_interest_cost = 0.0;
    xp_candidate.lost_interest_cost = 1.0;
    assert(reroll_candidate.direct_gold_cost + reroll_candidate.lost_interest_cost +
               reroll_candidate.opportunity_cost >
           xp_candidate.direct_gold_cost + xp_candidate.lost_interest_cost +
               xp_candidate.opportunity_cost);

    economy_context.action_candidates.clear();
    const auto no_candidate = action_evaluator.evaluate(economy_context, posture);
    assert(no_candidate.recommended_action == StrategicActionKind::Hold);
    assert(no_candidate.confidence == 0.0);
    assert(no_candidate.candidate_scores.empty());

    // With a strong win streak, a marginal low-value purchase should not
    // beat holding resources merely because spending is possible.
    StrategicSharedContext streak_context;
    streak_context.hp = 90.0;
    streak_context.gold = 45;
    streak_context.relative_board_power = 1.15;
    streak_context.win_streak = 5;
    StrategicActionCandidate streak_hold;
    streak_hold.kind = StrategicActionKind::Hold;
    streak_context.action_candidates.push_back(streak_hold);
    StrategicActionCandidate weak_purchase;
    weak_purchase.kind = StrategicActionKind::BuyUnit;
    weak_purchase.gold_cost = 3;
    weak_purchase.expected_economy_cost = 3.0;
    weak_purchase.expected_board_delta = 0.10;
    weak_purchase.composition_fit = 0.10;
    streak_context.action_candidates.push_back(weak_purchase);
    const auto streak_posture = economic_controller.evaluate(streak_context);
    const auto streak_action = action_evaluator.evaluate(
        streak_context, streak_posture);
    assert(streak_posture.posture == EconomicPosture::PreserveWinStreak);
    assert(streak_action.recommended_action == StrategicActionKind::Hold);
    assert(std::any_of(streak_action.candidate_scores.begin(),
                       streak_action.candidate_scores.end(),
                       [](const ActionCandidateScore& score) {
                           return score.kind == StrategicActionKind::Hold &&
                                  score.selected;
                       }));

    std::cout << "strategic planner shadow tests passed\n";
    return 0;
}
