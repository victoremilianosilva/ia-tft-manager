#include "strategy/ActionEvaluator.hpp"

#include <cassert>
#include <cstddef>
#include <iostream>

using namespace tft::strategy;

namespace {
StrategicActionCandidate deploy_candidate(std::int32_t champion_id) {
    StrategicActionCandidate candidate;
    candidate.kind = StrategicActionKind::DeployOrMove;
    candidate.champion_id = champion_id;
    candidate.expected_board_delta = 0.50;
    candidate.available = true;
    return candidate;
}

StrategicActionCandidate buy_candidate(std::int32_t champion_id) {
    StrategicActionCandidate candidate;
    candidate.kind = StrategicActionKind::BuyUnit;
    candidate.champion_id = champion_id;
    candidate.gold_cost = 3;
    candidate.direct_gold_cost = 3.0;
    candidate.expected_board_delta = 0.50;
    candidate.available = true;
    return candidate;
}

std::size_t selected_count(const ActionEvaluation& result) {
    std::size_t count = 0;
    for (const auto& candidate : result.candidate_scores)
        if (candidate.selected) ++count;
    return count;
}

void equivalent_candidates_select_one_occurrence() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 50;
    auto first = deploy_candidate(18);
    auto duplicate = deploy_candidate(18);
    context.action_candidates = {first, duplicate};

    EconomicControlDecision posture;
    posture.posture = EconomicPosture::AccumulateResources;

    const auto result = ActionEvaluator{}.evaluate(context, posture);
    assert(result.recommended_action == StrategicActionKind::DeployOrMove);
    assert(result.recommended_champion_id == 18);
    assert(result.candidate_scores.size() == 2);
    assert(selected_count(result) == 1);
    assert(result.candidate_scores[0].selected);
    assert(!result.candidate_scores[1].selected);
}

void equivalent_shop_offers_select_one_occurrence() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 50;
    context.action_candidates = {
        buy_candidate(39),
        buy_candidate(39),
    };

    EconomicControlDecision posture;
    posture.posture = EconomicPosture::StabilizeBoard;
    const auto result = ActionEvaluator{}.evaluate(context, posture);

    assert(result.recommended_action == StrategicActionKind::BuyUnit);
    assert(result.recommended_champion_id == 39);
    assert(result.candidate_scores.size() == 2);
    assert(selected_count(result) == 1);
    assert(result.candidate_scores[0].selected);
    assert(!result.candidate_scores[1].selected);
}

void tied_candidates_select_first_occurrence_only() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 50;
    context.action_candidates = {
        deploy_candidate(18),
        deploy_candidate(19),
    };

    EconomicControlDecision posture;
    const auto result = ActionEvaluator{}.evaluate(context, posture);

    assert(result.candidate_scores.size() == 2);
    assert(selected_count(result) == 1);
    assert(result.recommended_champion_id == 18);
    assert(result.candidate_scores[0].selected);
    assert(!result.candidate_scores[1].selected);
}

void no_candidates_means_no_selected_candidate() {
    StrategicSharedContext context;
    context.alive = true;
    EconomicControlDecision posture;

    const auto result = ActionEvaluator{}.evaluate(context, posture);
    assert(result.candidate_scores.empty());
    assert(result.recommended_action == StrategicActionKind::Hold);
    assert(result.recommended_champion_id == -1);
    assert(selected_count(result) == 0);
}

void unavailable_candidates_are_not_selected() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 0;
    auto unavailable = deploy_candidate(18);
    unavailable.available = false;
    unavailable.gold_cost = 5;
    context.action_candidates.push_back(unavailable);

    EconomicControlDecision posture;
    const auto result = ActionEvaluator{}.evaluate(context, posture);

    assert(result.candidate_scores.size() == 1);
    assert(!result.candidate_scores[0].available);
    assert(selected_count(result) == 0);
    assert(result.recommended_action == StrategicActionKind::Hold);
}

void dead_player_skips_candidate_evaluation() {
    StrategicSharedContext context;
    context.alive = false;
    context.action_candidates.push_back(deploy_candidate(18));

    EconomicControlDecision posture;
    const auto result = ActionEvaluator{}.evaluate(context, posture);

    assert(result.candidate_scores.empty());
    assert(result.recommended_action == StrategicActionKind::Hold);
    assert(selected_count(result) == 0);
}
}

int main() {
    equivalent_candidates_select_one_occurrence();
    equivalent_shop_offers_select_one_occurrence();
    tied_candidates_select_first_occurrence_only();
    no_candidates_means_no_selected_candidate();
    unavailable_candidates_are_not_selected();
    dead_player_skips_candidate_evaluation();
    std::cout << "ActionEvaluator selection tests passed\n";
    return 0;
}
