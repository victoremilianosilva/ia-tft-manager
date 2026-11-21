#include "composition_intelligence/ContextualActionEvaluator.hpp"
#include "strategy/ActionEvaluator.hpp"

#include <cassert>
#include <cmath>
#include <iostream>

using namespace tft::composition_intelligence;
using namespace tft::strategy;

namespace {
ActiveComposition active() {
    CompositionCandidate c;
    c.composition_id = "comp-a"; c.set_id = "TFT18"; c.target_board_size = 2;
    c.units = {{10, UnitRole::MainCarry, true, 80}, {20, UnitRole::Frontline, true, 70}};
    c.main_carry_id = 10;
    return {c, 4};
}
UnitPrioritySnapshot priorities() {
    UnitPrioritySnapshot p; p.composition_id = "comp-a"; p.composition_version = 4;
    UnitPriority seek; seek.champion_id = 20; seek.intent = UnitIntent::Seek;
    seek.priority = 90; seek.confidence = .8;
    UnitPriority upgrade; upgrade.champion_id = 10; upgrade.intent = UnitIntent::Upgrade;
    upgrade.priority = 80; upgrade.target_star = 2;
    UnitPriority sell; sell.champion_id = 30; sell.intent = UnitIntent::SellCandidate;
    sell.priority = 5;
    p.units = {seek, upgrade, sell}; return p;
}
LineupPlan lineup() {
    LineupPlan l; l.composition_id = "comp-a"; l.composition_version = 4;
    l.endgame_target_ids = {10,20};
    l.selected_board = {{10,LineupSlotKind::ActiveTarget,80,true,true},
                        {20,LineupSlotKind::ActiveTarget,90,false,true}};
    return l;
}
StrategicActionCandidate candidate(StrategicActionKind kind, int id = -1) {
    StrategicActionCandidate c; c.kind = kind; c.champion_id = id;
    c.candidate_id = "candidate:" + std::to_string(static_cast<int>(kind)) + ":" + std::to_string(id);
    c.source_sequence = 12;
    c.available = true; c.expected_board_delta = .8;
    if (kind == StrategicActionKind::BuyUnit) { c.gold_cost = 3; c.direct_gold_cost = 3; }
    if (kind == StrategicActionKind::RerollShop) { c.gold_cost = 2; c.direct_gold_cost = 2; }
    return c;
}
void attach_exact_marginal(StrategicActionCandidate& c, std::int32_t gold_before) {
    const auto gold_after = gold_before -
        static_cast<std::int32_t>(std::llround(c.direct_gold_cost));
    c.marginal_economy_evidence_available = true;
    c.marginal_gold_before = gold_before;
    c.marginal_gold_after = gold_after;
    c.marginal_interest_before = tft::EconomyEngine{}.get_interest(gold_before);
    c.marginal_interest_after = tft::EconomyEngine{}.get_interest(gold_after);
    c.marginal_interest_delta = c.marginal_interest_after - c.marginal_interest_before;
    c.marginal_cost_source = "native_gold+EconomyEngine::get_interest";
    c.marginal_cost_horizon_rounds = 1;
    c.marginal_cost_uncertainty = 0.0;
}
void stale_lineup_identity_is_rejected_before_scoring() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0;
    context.round = 8; context.sequence = 12; context.evidence.gold = true;
    auto stale = lineup();
    stale.match_id = 77; stale.player_id = 0; stale.round = 8;
    stale.sequence = 11;
    auto buy = candidate(StrategicActionKind::BuyUnit, 20);
    attach_exact_marginal(buy, context.gold);
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), stale, context, nullptr, 77);
    assert(result.stale);
    assert(result.stale_reason == "lineup match/player/round/sequence mismatch");
    assert(result.recommended_action == StrategicActionKind::None);
}

void no_active_composition_without_anchor_remains_stale() {
    StrategicSharedContext context;
    context.alive = true; context.player_id = 0; context.round = 8;
    const auto result = ContextualActionEvaluator{}.evaluate(
        std::nullopt, UnitPrioritySnapshot{}, LineupPlan{}, context, nullptr, 77);
    assert(result.stale);
    assert(result.stale_reason == "no active composition or native anchor hypothesis");
    assert(result.recommended_action == StrategicActionKind::None);
}

void native_anchor_purchase_is_evaluated_before_composition_lock() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    StrategicAnchorCandidate anchor;
    anchor.unit.champion_id = 20;
    anchor.unit.composition_fit = 0.9;
    anchor.unit.board_contribution = 0.8;
    anchor.shop_available = true;
    anchor.anchor_value = 4.0;
    context.anchor_candidates = {anchor};
    auto buy = candidate(StrategicActionKind::BuyUnit, 20);
    buy.shop_slot = 2;
    attach_exact_marginal(buy, context.gold);
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};

    const auto result = ContextualActionEvaluator{}.evaluate(
        std::nullopt, UnitPrioritySnapshot{}, LineupPlan{}, context, nullptr, 77);
    assert(!result.stale);
    assert(result.composition_id.empty() && result.composition_version == 0);
    assert(result.candidates.size() == 2);
    assert(result.candidates[0].eligible);
    assert(result.candidates[0].selected);
    assert(result.recommended_action == StrategicActionKind::BuyUnit);
    assert(result.rationale == "native_anchor_shop_purchase");
}

void baseline_is_unchanged_by_contextual_execution() {
    auto context = StrategicSharedContext{};
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.action_candidates = {candidate(StrategicActionKind::BuyUnit,20),
        candidate(StrategicActionKind::Hold)};
    EconomicControlDecision posture;
    const auto before = ActionEvaluator{}.evaluate(context, posture);
    const auto contextual = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    const auto after = ActionEvaluator{}.evaluate(context, posture);
    assert(contextual.candidates.size() == context.action_candidates.size());
    assert(before.recommended_action == after.recommended_action);
    assert(before.recommended_champion_id == after.recommended_champion_id);
    assert(before.confidence == after.confidence);
    assert(before.candidate_scores.size() == after.candidate_scores.size());
    for (std::size_t i=0;i<before.candidate_scores.size();++i) {
        assert(before.candidate_scores[i].total_score == after.candidate_scores[i].total_score);
        assert(before.candidate_scores[i].selected == after.candidate_scores[i].selected);
    }
}
void contextual_path_uses_priority_and_lineup_without_calling_baseline() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    context.action_candidates = {candidate(StrategicActionKind::BuyUnit,20),
        candidate(StrategicActionKind::DeployOrMove,20), candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(!result.stale);
    assert(result.candidates.size() == 3);
    assert(result.candidates[0].candidate_id == context.action_candidates[0].candidate_id);
    assert(result.recommended_action == StrategicActionKind::BuyUnit ||
        result.recommended_action == StrategicActionKind::DeployOrMove);
    int selected = 0;
    for (const auto& c : result.candidates) if (c.selected) ++selected;
    assert(selected == 1);
}
void stale_identity_disables_contextual_recommendation() {
    StrategicSharedContext context;
    context.alive = true; context.player_id = 1; context.round = 8;
    PlannerEvidenceSnapshot wrong_player;
    wrong_player.match_id = 77; wrong_player.player_id = 0;
    wrong_player.composition_id = "comp-a"; wrong_player.composition_version = 4;
    wrong_player.round = 8;
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, &wrong_player, 77);
    assert(result.stale);
    assert(result.recommended_action == StrategicActionKind::None);
    assert(result.candidates.empty());
}
void invalid_candidates_and_equipped_sales_are_rejected() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    context.action_candidates = {candidate(StrategicActionKind::BuyUnit,30),
        candidate(StrategicActionKind::SellUnit,30)};
    PlannerEvidenceSnapshot evidence;
    evidence.match_id=77; evidence.player_id=0; evidence.composition_id="comp-a";
    evidence.composition_version=4; evidence.round=8;
    auto set_valid = [&](EvidenceSourceMetadata& m, const std::string& name) {
        m.source=name; m.source_round=8; m.expected_round=8;
        m.quality=EvidenceQuality::Valid; m.available=true; m.reason="valid";
    };
    set_valid(evidence.economy.metadata,"EconomicController");
    set_valid(evidence.board.metadata,"BoardEvaluation");
    set_valid(evidence.items.metadata,"ItemEngine");
    evidence.items.units.push_back({30, {"item"}, {}, 0.0, 0.0, true, false});
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, &evidence, 77);
    assert(result.item_evidence_consumed);
    assert(!result.candidates[0].eligible);
    assert(result.candidates[1].rejection_reason == "sale_restricted_by_pair_star_item_or_transition_risk");
}
void contextual_sell_rejects_pairs_and_existing_star_progress() {
    auto p = priorities();
    p.units.back().copies_owned = 2;
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    context.action_candidates = {candidate(StrategicActionKind::SellUnit,30)};
    auto result = ContextualActionEvaluator{}.evaluate(
        active(), p, lineup(), context, nullptr, 77);
    assert(result.candidates.size() == 1);
    assert(!result.candidates[0].eligible);
    assert(result.candidates[0].rejection_reason ==
        "sale_restricted_by_pair_star_item_or_transition_risk");

    p.units.back().copies_owned = 1;
    p.units.back().highest_star = 2;
    result = ContextualActionEvaluator{}.evaluate(
        active(), p, lineup(), context, nullptr, 77);
    assert(!result.candidates[0].eligible);
}

void explicit_hold_is_selected_when_all_actions_score_below_zero() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 200; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    auto expensive_xp = candidate(StrategicActionKind::BuyExperience);
    expensive_xp.gold_cost = 100;
    expensive_xp.direct_gold_cost = 100.0;
    expensive_xp.expected_board_delta = 0.0;
    expensive_xp.marginal_economy_evidence_available = true;
    expensive_xp.marginal_gold_before = 200;
    expensive_xp.marginal_gold_after = 100;
    expensive_xp.marginal_interest_before = tft::EconomyEngine{}.get_interest(200);
    expensive_xp.marginal_interest_after = tft::EconomyEngine{}.get_interest(100);
    expensive_xp.marginal_interest_delta =
        expensive_xp.marginal_interest_after - expensive_xp.marginal_interest_before;
    expensive_xp.marginal_cost_source = "native_gold+EconomyEngine::get_interest";
    expensive_xp.marginal_cost_horizon_rounds = 1;
    expensive_xp.marginal_cost_uncertainty = 0.0;
    context.action_candidates = {expensive_xp, candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(result.recommended_action == StrategicActionKind::Hold);
    assert(result.candidates.size() == 2);
    assert(result.candidates[0].eligible);
    assert(result.candidates[0].economy_cost > 0.0);
    assert(!result.candidates[0].selected);
    assert(result.candidates[1].selected);
}

void explicit_sale_credit_is_not_discarded_as_a_positive_cost() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 0;
    context.player_id = 0;
    context.round = 8;
    context.evidence.gold = true;
    auto sale_priority = UnitPriority{};
    sale_priority.champion_id = 30;
    sale_priority.intent = UnitIntent::SellCandidate;
    sale_priority.confidence = 0.9;
    sale_priority.copies_owned = 1;
    sale_priority.highest_star = 1;
    auto p = priorities();
    p.units.push_back(sale_priority);
    auto sale = candidate(StrategicActionKind::SellUnit, 30);
    sale.gold_cost = 0;
    sale.direct_gold_cost = -3.0;
    sale.source_slot = 1;
    sale.source_is_bench = true;
    sale.marginal_economy_evidence_available = true;
    sale.marginal_gold_before = 0;
    sale.marginal_gold_after = 3;
    sale.marginal_interest_before = 0;
    sale.marginal_interest_after = 0;
    sale.marginal_interest_delta = 0;
    sale.marginal_cost_source = "native_gold+EconomyEngine::get_interest";
    sale.marginal_cost_horizon_rounds = 1;
    sale.marginal_cost_uncertainty = 0.0;
    auto hold = candidate(StrategicActionKind::Hold);
    context.action_candidates = {sale, hold};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), p, lineup(), context, nullptr, 77);
    assert(!result.stale);
    assert(result.candidates.size() == 2);
    assert(result.candidates[0].eligible);
    assert(result.candidates[0].economy_cost < 0.0);
    assert(result.recommended_action == StrategicActionKind::SellUnit);
}

void sale_credit_preserves_verified_interest_gain() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 48;
    context.player_id = 0;
    context.round = 8;
    context.evidence.gold = true;

    auto p = priorities();
    UnitPriority sell;
    sell.champion_id = 30;
    sell.intent = UnitIntent::SellCandidate;
    sell.confidence = 0.9;
    sell.copies_owned = 1;
    sell.highest_star = 1;
    p.units.push_back(sell);

    auto sale = candidate(StrategicActionKind::SellUnit, 30);
    sale.direct_gold_cost = -3.0;
    sale.source_slot = 1;
    sale.source_is_bench = true;
    attach_exact_marginal(sale, context.gold);
    context.action_candidates = {sale, candidate(StrategicActionKind::Hold)};

    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), p, lineup(), context, nullptr, 77);
    const auto& score = result.candidates.front();
    assert(score.eligible);
    assert(score.marginal_gold_delta == 3);
    assert(score.interest_delta == 1);
    assert(score.liquidity_cost < 0.0);
    const double expected_interest_cost = -0.12;
    assert(std::abs(score.economy_cost -
        (score.liquidity_cost + expected_interest_cost)) < 1e-9);
    assert(score.economy_cost < score.liquidity_cost);
    assert(result.recommended_action == StrategicActionKind::SellUnit);
}

void unproduced_opportunity_cost_is_not_consumed() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    auto without_prior = candidate(StrategicActionKind::BuyUnit, 20);
    without_prior.expected_board_delta = 0.8;
    attach_exact_marginal(without_prior, context.gold);
    auto with_unproduced_prior = without_prior;
    with_unproduced_prior.opportunity_cost = 1000.0;
    context.action_candidates = {without_prior, candidate(StrategicActionKind::Hold)};
    const auto baseline = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    context.action_candidates = {with_unproduced_prior, candidate(StrategicActionKind::Hold)};
    const auto changed = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(baseline.candidates.size() == changed.candidates.size());
    assert(baseline.candidates[0].economy_cost == changed.candidates[0].economy_cost);
    assert(baseline.candidates[0].total_score == changed.candidates[0].total_score);
    assert(changed.candidates[0].marginal_economy_evidence_available);
    assert(!changed.candidates[0].opportunity_cost_available);
    assert(changed.candidates[0].opportunity_cost_source ==
        "unavailable_no_validated_producer");
}

void validated_opportunity_cost_uses_the_same_board_value_basis() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.evidence.gold = true;
    auto buy = candidate(StrategicActionKind::BuyUnit, 20);
    buy.expected_board_delta = 0.8;
    attach_exact_marginal(buy, context.gold);
    buy.opportunity_cost = 0.4;
    buy.opportunity_cost_evidence_available = true;
    buy.opportunity_cost_source = "same_snapshot_competing_alternative.v1";
    buy.opportunity_cost_forgone_candidate_id = "competing-buy";
    buy.opportunity_cost_horizon_rounds = 1;
    buy.opportunity_cost_uncertainty = 0.2;
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    const auto& score = result.candidates.front();
    const double expected_opportunity_cost = 0.4 * 0.8 * 0.55;
    const double expected_interest_cost =
        -(static_cast<double>(score.interest_delta) * 0.12);
    assert(score.opportunity_cost_available);
    assert(score.opportunity_cost_forgone_candidate_id == "competing-buy");
    assert(std::abs(score.economy_cost -
        (score.liquidity_cost + expected_interest_cost + expected_opportunity_cost)) < 1e-9);
}

void marginal_liquidity_and_interest_are_compared_to_hold_once() {
    const auto evaluate_buy = [](std::int32_t gold) {
        StrategicSharedContext context;
        context.alive = true;
        context.gold = gold;
        context.player_id = 0;
        context.round = 8;
        context.evidence.gold = true;
        auto buy = candidate(StrategicActionKind::BuyExperience);
        buy.gold_cost = 3;
        buy.direct_gold_cost = 3.0;
        buy.expected_board_delta = 0.8;
        buy.marginal_economy_evidence_available = true;
        buy.marginal_gold_before = gold;
        buy.marginal_gold_after = gold - 3;
        buy.marginal_interest_before = tft::EconomyEngine{}.get_interest(gold);
        buy.marginal_interest_after = tft::EconomyEngine{}.get_interest(gold - 3);
        buy.marginal_interest_delta =
            buy.marginal_interest_after - buy.marginal_interest_before;
        buy.marginal_cost_source = "native_gold+EconomyEngine::get_interest";
        buy.marginal_cost_horizon_rounds = 1;
        buy.marginal_cost_uncertainty = 0.0;
        buy.evidence_source = "EconomyEngine+native_BUY_XP_mask";
        buy.evidence_horizon_rounds = 1;
        buy.evidence_uncertainty = 0.0;
        context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};
        return ContextualActionEvaluator{}.evaluate(
            active(), priorities(), lineup(), context, nullptr, 77);
    };

    const auto low_liquidity = evaluate_buy(10);
    const auto high_liquidity = evaluate_buy(50);
    const auto& low = low_liquidity.candidates.front();
    const auto& high = high_liquidity.candidates.front();
    assert(low.marginal_economy_evidence_available);
    assert(high.marginal_economy_evidence_available);
    assert(low.marginal_gold_delta == -3);
    assert(high.marginal_gold_delta == -3);
    assert(low.liquidity_cost > high.liquidity_cost);
    assert(low.economy_cost > high.economy_cost);
    assert(low.total_score < high.total_score);
    assert(low.evidence_source == "EconomyEngine+native_BUY_XP_mask");
    assert(low.evidence_horizon_rounds == 1);
    assert(low.evidence_uncertainty == 0.0);
    assert(low.marginal_cost_uncertainty == 0.0);
    // HOLD is the same-snapshot reference: it preserves gold and interest.
    assert(low_liquidity.candidates.back().kind == StrategicActionKind::Hold);
    assert(low_liquidity.candidates.back().marginal_gold_delta == 0);
    assert(low_liquidity.candidates.back().economy_cost == 0.0);
}

void economic_posture_is_explanatory_not_a_fixed_action_rule() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 20;
    context.player_id = 0;
    context.round = 8;
    context.evidence.gold = true;
    auto buy = candidate(StrategicActionKind::BuyExperience);
    buy.gold_cost = 3;
    buy.direct_gold_cost = 3.0;
    buy.expected_board_delta = 0.4;
    buy.marginal_economy_evidence_available = true;
    buy.marginal_gold_before = 20;
    buy.marginal_gold_after = 17;
    buy.marginal_interest_before = tft::EconomyEngine{}.get_interest(20);
    buy.marginal_interest_after = tft::EconomyEngine{}.get_interest(17);
    buy.marginal_interest_delta = buy.marginal_interest_after - buy.marginal_interest_before;
    buy.marginal_cost_source = "native_gold+EconomyEngine::get_interest";
    buy.marginal_cost_horizon_rounds = 1;
    buy.marginal_cost_uncertainty = 0.0;
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};

    PlannerEvidenceSnapshot evidence;
    evidence.match_id = 77;
    evidence.player_id = 0;
    evidence.composition_id = "comp-a";
    evidence.composition_version = 4;
    evidence.round = 8;
    auto& economy = evidence.economy;
    economy.metadata.source = "EconomicController";
    economy.metadata.source_round = 8;
    economy.metadata.expected_round = 8;
    economy.metadata.quality = EvidenceQuality::Valid;
    economy.metadata.available = true;
    economy.sufficient_evidence = true;
    economy.confidence = 0.73;
    economy.evidence_used = {"gold"};
    economy.evidence_missing = {"projected_next_round_income"};
    economy.survival_evidence_available = true;
    economy.survival_pressure = 0.4;
    economy.board_pressure_available = true;
    economy.board_pressure = 0.2;
    economy.economy_pressure_available = true;
    economy.economy_pressure = 0.9;
    economy.posture = EconomicPosture::AccumulateResources;
    const auto accumulate = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, &evidence, 77);

    economy.posture = EconomicPosture::EmergencyInvestment;
    economy.reason = StrategicReason::SurvivalPressure;
    const auto emergency = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, &evidence, 77);

    assert(accumulate.economic_posture_available);
    assert(emergency.economic_posture_available);
    assert(accumulate.economic_confidence_available);
    assert(accumulate.economic_confidence == 0.73);
    assert(accumulate.survival_pressure_available);
    assert(accumulate.survival_pressure == 0.4);
    assert(accumulate.board_pressure_available);
    assert(accumulate.board_pressure == 0.2);
    assert(accumulate.economy_pressure_available);
    assert(accumulate.economy_pressure == 0.9);
    assert(accumulate.economic_posture != emergency.economic_posture);
    assert(accumulate.candidates[0].total_score == emergency.candidates[0].total_score);
    assert(accumulate.recommended_action == emergency.recommended_action);
    const auto json = accumulate.to_json();
    assert(json["economic_context"]["posture_available"] == true);
    assert(json["economic_context"]["evidence_missing"][0] == "projected_next_round_income");
    assert(json["economic_context"]["projected_income_available"] == false);
    assert(json["economic_context"]["incoming_damage_available"] == false);
    assert(json["economic_context"]["elimination_risk_available"] == false);
    assert(json["economic_context"]["progression_available"] == false);
}

void spending_candidate_without_marginal_evidence_is_not_scored_as_free() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 20;
    context.player_id = 0;
    context.round = 8;
    context.evidence.gold = true;
    auto buy = candidate(StrategicActionKind::BuyUnit, 20);
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(!result.candidates[0].eligible);
    assert(result.candidates[0].rejection_reason ==
        "marginal_economy_evidence_unavailable");
    assert(!result.candidates[0].marginal_economy_evidence_available);
    assert(result.recommended_action == StrategicActionKind::Hold);
}

void missing_gold_validity_disables_marginal_cost_even_with_numeric_values() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 20;
    context.player_id = 0;
    context.round = 8;
    context.evidence.gold = false;
    auto buy = candidate(StrategicActionKind::BuyExperience);
    buy.gold_cost = 3;
    buy.direct_gold_cost = 3.0;
    buy.marginal_economy_evidence_available = true;
    buy.marginal_gold_before = 20;
    buy.marginal_gold_after = 17;
    buy.marginal_interest_before = tft::EconomyEngine{}.get_interest(20);
    buy.marginal_interest_after = tft::EconomyEngine{}.get_interest(17);
    buy.marginal_interest_delta = buy.marginal_interest_after - buy.marginal_interest_before;
    buy.marginal_cost_source = "native_gold+EconomyEngine::get_interest";
    buy.marginal_cost_horizon_rounds = 1;
    buy.marginal_cost_uncertainty = 0.0;
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(!result.candidates[0].eligible);
    assert(result.candidates[0].rejection_reason == "gold_evidence_unavailable");
    assert(!result.candidates[0].marginal_economy_evidence_available);
    assert(result.candidates[0].economy_cost == 0.0);
    assert(result.candidates[0].liquidity_cost == 0.0);
}

void validated_survival_and_streak_evidence_adjust_board_improvement_value() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 10;
    context.player_id = 0;
    context.round = 8;
    context.evidence.gold = true;
    auto buy = candidate(StrategicActionKind::BuyUnit, 20);
    buy.expected_board_delta = 0.8;
    attach_exact_marginal(buy, context.gold);
    context.action_candidates = {buy, candidate(StrategicActionKind::Hold)};

    PlannerEvidenceSnapshot evidence;
    evidence.match_id = 77;
    evidence.player_id = 0;
    evidence.composition_id = "comp-a";
    evidence.composition_version = 4;
    evidence.round = 8;
    auto& economy = evidence.economy;
    economy.metadata.source = "EconomicController";
    economy.metadata.source_round = 8;
    economy.metadata.expected_round = 8;
    economy.metadata.quality = EvidenceQuality::Valid;
    economy.metadata.available = true;
    economy.survival_evidence_available = true;
    economy.survival_pressure = 1.0;
    economy.streak_evidence_available = true;
    economy.win_streak = 6;

    const auto baseline = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, &evidence, 77);
    assert(!result.stale);
    assert(result.economy_evidence_consumed);
    assert(result.candidates.size() == 2);
    assert(baseline.candidates[0].survival_value == 0.0);
    assert(baseline.candidates[0].streak_value == 0.0);
    assert(result.candidates[0].survival_value > 0.0);
    assert(result.candidates[0].streak_value > 0.0);
    assert(result.candidates[0].total_score > baseline.candidates[0].total_score);

    // Loss streak evidence also changes the same candidate's marginal score.
    economy.win_streak = 0;
    economy.loss_streak = 6;
    const auto loss_streak_result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, &evidence, 77);
    assert(loss_streak_result.candidates[0].streak_value > 0.0);
    assert(loss_streak_result.candidates[0].total_score > baseline.candidates[0].total_score);
}

void empty_candidate_set_is_not_a_hold_recommendation() {
    StrategicSharedContext context;
    context.alive = true;
    context.player_id = 0;
    context.round = 8;
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(!result.stale);
    assert(result.candidates.empty());
    assert(result.recommended_action == StrategicActionKind::None);
    assert(result.confidence_not_probability == 0.0);
    assert(result.rationale == "no_candidates");
}

void ineligible_candidates_do_not_fall_back_to_implicit_hold() {
    StrategicSharedContext context;
    context.alive = true;
    context.gold = 10;
    context.player_id = 0;
    context.round = 8;
    auto unavailable = candidate(StrategicActionKind::BuyUnit, 20);
    unavailable.available = false;
    context.action_candidates = {unavailable};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(!result.stale);
    assert(result.candidates.size() == 1);
    assert(!result.candidates.front().eligible);
    assert(!result.candidates.front().selected);
    assert(result.recommended_action == StrategicActionKind::None);
    assert(result.confidence_not_probability == 0.0);
}

void json_is_versioned_and_shadow_only() {
    StrategicSharedContext context; context.alive=true; context.player_id=0; context.round=8;
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    const auto json = result.to_json();
    assert(json["schema_version"] == kContextualActionEvaluatorSchemaVersion);
    assert(json["shadow_only"] == true);
    assert(json["identity"]["match_id"] == 77);
}
}

int main() {
    stale_lineup_identity_is_rejected_before_scoring();
    no_active_composition_without_anchor_remains_stale();
    native_anchor_purchase_is_evaluated_before_composition_lock();
    baseline_is_unchanged_by_contextual_execution();
    contextual_path_uses_priority_and_lineup_without_calling_baseline();
    stale_identity_disables_contextual_recommendation();
    invalid_candidates_and_equipped_sales_are_rejected();
    contextual_sell_rejects_pairs_and_existing_star_progress();
    explicit_hold_is_selected_when_all_actions_score_below_zero();
    explicit_sale_credit_is_not_discarded_as_a_positive_cost();
    sale_credit_preserves_verified_interest_gain();
    unproduced_opportunity_cost_is_not_consumed();
    validated_opportunity_cost_uses_the_same_board_value_basis();
    marginal_liquidity_and_interest_are_compared_to_hold_once();
    economic_posture_is_explanatory_not_a_fixed_action_rule();
    spending_candidate_without_marginal_evidence_is_not_scored_as_free();
    missing_gold_validity_disables_marginal_cost_even_with_numeric_values();
    validated_survival_and_streak_evidence_adjust_board_improvement_value();
    empty_candidate_set_is_not_a_hold_recommendation();
    ineligible_candidates_do_not_fall_back_to_implicit_hold();
    json_is_versioned_and_shadow_only();
    std::cout << "ContextualActionEvaluator tests passed\\n";
}
