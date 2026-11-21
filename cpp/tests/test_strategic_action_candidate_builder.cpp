#include "composition_intelligence/StrategicActionCandidateBuilder.hpp"
#include "composition_intelligence/ContextualActionEvaluator.hpp"
#include "composition_intelligence/StrategicActionExecutor.hpp"

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <unordered_set>

using namespace tft;
using namespace tft::composition_intelligence;
using namespace tft::strategy;

namespace {
void enables(PlayerActionMasks& masks, decision::ActionType type) {
    masks.type_mask[static_cast<std::size_t>(type)] = decision::MASK_ENABLED;
}

void builder_emits_snapshot_bound_physical_candidates() {
    CompositionCandidate composition;
    composition.composition_id = "candidate-builder";
    composition.set_id = "TFT18";
    composition.target_board_size = 2;
    composition.units = {
        {10, tft::composition_intelligence::UnitRole::MainCarry, true, 80},
        {20, tft::composition_intelligence::UnitRole::Frontline, true, 70}
    };
    const std::optional<ActiveComposition> active = ActiveComposition{composition, 3};

    UnitPrioritySnapshot priorities;
    priorities.composition_id = "candidate-builder";
    priorities.composition_version = 3;
    UnitPriority carry;
    carry.champion_id = 10;
    carry.intent = UnitIntent::Upgrade;
    carry.target_star = 2;
    carry.priority = 90;
    carry.board_contribution = 0.8;
    carry.confidence = 0.8;
    UnitPriority frontline;
    frontline.champion_id = 20;
    frontline.intent = UnitIntent::Seek;
    frontline.priority = 80;
    frontline.board_contribution = 0.7;
    frontline.confidence = 0.8;
    UnitPriority sale;
    sale.champion_id = 30;
    sale.intent = UnitIntent::SellCandidate;
    sale.copies_owned = 1;
    sale.highest_star = 1;
    sale.priority = 40;
    sale.confidence = 0.8;
    sale.board_contribution = 0.3;
    priorities.units = {carry, frontline, sale};

    LineupPlan lineup;
    lineup.composition_id = "candidate-builder";
    lineup.composition_version = 3;
    lineup.match_id = 77; lineup.player_id = 0; lineup.round = 9; lineup.sequence = 42;
    lineup.endgame_target_ids = {10, 20};
    lineup.selected_board = {
        {10, LineupSlotKind::ActiveTarget, 90, true, true},
        {20, LineupSlotKind::ActiveTarget, 80, false, true}
    };

    StrategicSharedContext context;
    context.match_id = 77;
    context.player_id = 0;
    context.round = 9;
    context.sequence = 42;
    context.alive = true;
    context.gold = 20;
    context.level = 5;
    context.xp_to_next = 4;
    context.evidence.gold = true;
    context.evidence.interest_if_resolved_now = true;
    context.interest_if_resolved_now = EconomyEngine{}.get_interest(context.gold);
    context.evidence.level = true;
    context.evidence.xp_to_next = true;

    StrategicActionNativeSnapshot native;
    native.match_id = 77;
    native.player_id = 0;
    native.round = 9;
    native.sequence = 42;
    native.composition_id = "candidate-builder";
    native.composition_version = 3;
    native.gold = 20;
    native.alive = true;
    native.shop_champion_ids[0] = 10;
    native.shop_champion_ids[1] = 20;
    native.bench_champion_ids[0] = 20;
    native.bench_champion_ids[1] = 30;
    native.bench_unit_uuids[0] = "unit-20";
    native.bench_unit_uuids[1] = "unit-30";
    enables(native.masks, decision::ActionType::PASS);
    enables(native.masks, decision::ActionType::BUY);
    enables(native.masks, decision::ActionType::BUY_XP);
    enables(native.masks, decision::ActionType::REROLL);
    enables(native.masks, decision::ActionType::SELL);
    enables(native.masks, decision::ActionType::MOVE_BENCH);
    native.masks.shop_mask[0] = decision::MASK_ENABLED;
    native.masks.shop_mask[1] = decision::MASK_ENABLED;
    native.masks.bench_source_mask[1] = decision::MASK_ENABLED;
    native.masks.bench_move_source_mask[0] = decision::MASK_ENABLED;
    native.masks.bench_to_board_target_masks[0] = decision::MASK_ENABLED;

    const std::unordered_map<std::int32_t, std::int32_t> costs{
        {10, 3}, {20, 2}, {30, 1}
    };
    const auto result = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, lineup, native, costs);
    assert(result.status == "candidates_generated");
    assert(result.candidates.size() >= 6);

    const auto find = [&](StrategicActionKind kind, std::int32_t id = -1) {
        return std::find_if(result.candidates.begin(), result.candidates.end(),
            [&](const auto& candidate) {
                return candidate.kind == kind && candidate.champion_id == id;
            });
    };
    const auto buy = find(StrategicActionKind::BuyUnit, 10);
    assert(buy != result.candidates.end());
    assert(buy->shop_slot == 0 && buy->source_sequence == 42);
    assert(!buy->candidate_id.empty());
    assert(buy->evidence_source.find("native_shop") != std::string::npos);
    assert(buy->evidence_horizon_rounds == 1);
    assert(buy->lost_interest_evidence_available);
    assert(buy->lost_interest_cost == 1.0);
    assert(buy->marginal_economy_evidence_available);
    assert(buy->marginal_gold_before == 20 && buy->marginal_gold_after == 17);
    assert(buy->marginal_interest_before == 2 && buy->marginal_interest_after == 1);
    assert(buy->marginal_interest_delta == -1);
    assert(buy->marginal_cost_horizon_rounds == 1);
    assert(buy->marginal_cost_uncertainty == 0.0);
    assert(buy->marginal_cost_source == "native_gold+EconomyEngine::get_interest");
    const auto competing_buy = find(StrategicActionKind::BuyUnit, 20);
    assert(competing_buy != result.candidates.end());
    assert(!buy->opportunity_cost_evidence_available);
    assert(!competing_buy->opportunity_cost_evidence_available);

    const auto xp = find(StrategicActionKind::BuyExperience);
    assert(xp != result.candidates.end() && xp->gold_cost == EconomyEngine::BUY_XP_COST);
    const auto reroll = find(StrategicActionKind::RerollShop);
    assert(reroll != result.candidates.end() && reroll->gold_cost == EconomyEngine::REROLL_COST);
    const auto sell = find(StrategicActionKind::SellUnit, 30);
    assert(sell != result.candidates.end());
    assert(sell->source_is_bench && sell->source_slot == 1);
    assert(sell->source_unit_uuid == "unit-30");
    assert(sell->direct_gold_cost == -1.0);
    assert(sell->marginal_economy_evidence_available);
    assert(sell->marginal_gold_before == 20 && sell->marginal_gold_after == 21);

    const auto deploy = find(StrategicActionKind::DeployOrMove, 20);
    assert(deploy != result.candidates.end());
    assert(deploy->source_is_bench && deploy->source_slot == 0);
    assert(deploy->source_unit_uuid == "unit-20");
    assert(deploy->target_board_slot >= 0);
    assert(deploy->candidate_id.find(std::to_string(deploy->target_board_slot)) != std::string::npos);
    assert(deploy->candidate_id.find("candidate-builder") != std::string::npos);
    assert(deploy->candidate_id.find("unit-20") != std::string::npos);
    assert(deploy->evidence_source.find("StrategicPositionPlanner") != std::string::npos);
    assert(!native.requested_move_targets.empty());

    const auto hold = find(StrategicActionKind::Hold);
    assert(hold != result.candidates.end());
    assert(hold->evidence_reason.find("neutral_baseline") != std::string::npos);
    assert(hold->marginal_economy_evidence_available);
    assert(hold->marginal_gold_before == hold->marginal_gold_after);
    assert(hold->marginal_interest_delta == 0);

    // The evaluator compares the net candidate scores across action families,
    // after each alternative's own economy/liquidity costs have been applied.
    auto opportunity_context = context;
    const auto sale_candidate = find(StrategicActionKind::SellUnit, 30);
    assert(sale_candidate != result.candidates.end());
    opportunity_context.action_candidates = {
        *buy, *competing_buy, *deploy, *sale_candidate, *hold};
    const auto opportunity_evaluation = ContextualActionEvaluator{}.evaluate(
        active, priorities, lineup, opportunity_context, nullptr, native.match_id);
    assert(!opportunity_evaluation.stale);
    const auto buy_score = std::find_if(
        opportunity_evaluation.candidates.begin(), opportunity_evaluation.candidates.end(),
        [&](const auto& score) { return score.candidate_id == buy->candidate_id; });
    assert(buy_score != opportunity_evaluation.candidates.end());
    assert(buy_score->opportunity_cost_available);
    assert(buy_score->opportunity_cost > 0.0);
    assert(buy_score->opportunity_cost_source == "same_snapshot_competing_alternative.v1");
    assert(buy_score->opportunity_cost_value_basis == "contextual_action_score.v1");
    assert(buy_score->opportunity_cost_forgone_candidate_id != buy->candidate_id);
    assert(buy_score->opportunity_cost_forgone_candidate_id == competing_buy->candidate_id ||
        buy_score->opportunity_cost_forgone_candidate_id == deploy->candidate_id ||
        buy_score->opportunity_cost_forgone_candidate_id == sale_candidate->candidate_id);
    const auto sale_score = std::find_if(
        opportunity_evaluation.candidates.begin(), opportunity_evaluation.candidates.end(),
        [&](const auto& score) { return score.candidate_id == sale_candidate->candidate_id; });
    assert(sale_score != opportunity_evaluation.candidates.end());
    assert(sale_score->unit_priority_value < 0.0);

    struct BaselineAlternativeScore {
        double net_score{0.0};
        double uncertainty{1.0};
        bool eligible{false};
    };
    const auto net_score_against_hold = [&](const StrategicActionCandidate& alternative) {
        auto baseline_context = context;
        baseline_context.action_candidates = {alternative, *hold};
        const auto baseline = ContextualActionEvaluator{}.evaluate(
            active, priorities, lineup, baseline_context, nullptr, native.match_id);
        const auto baseline_score = std::find_if(
            baseline.candidates.begin(), baseline.candidates.end(),
            [&](const auto& score) { return score.candidate_id == alternative.candidate_id; });
        assert(baseline_score != baseline.candidates.end());
        return BaselineAlternativeScore{
            baseline_score->total_score, baseline_score->evidence_uncertainty,
            baseline_score->eligible};
    };
    double best_risk_adjusted_value = 0.0;
    double expected_forgone_net_score = 0.0;
    std::string expected_forgone_candidate_id;
    for (const auto& alternative : {
        *competing_buy, *deploy, *sale_candidate
    }) {
        const auto baseline = net_score_against_hold(alternative);
        if (!baseline.eligible || baseline.net_score <= 0.0 ||
            !std::isfinite(baseline.uncertainty) ||
            baseline.uncertainty < 0.0 || baseline.uncertainty >= 1.0)
            continue;
        const double risk_adjusted =
            baseline.net_score * (1.0 - baseline.uncertainty);
        if (risk_adjusted <= best_risk_adjusted_value) continue;
        best_risk_adjusted_value = risk_adjusted;
        expected_forgone_net_score = baseline.net_score;
        expected_forgone_candidate_id = alternative.candidate_id;
    }
    assert(best_risk_adjusted_value > 0.0);
    assert(std::abs(buy_score->opportunity_cost - expected_forgone_net_score) < 1e-9);
    assert(buy_score->opportunity_cost_forgone_candidate_id ==
        expected_forgone_candidate_id);

    auto baseline_buy_context = context;
    baseline_buy_context.action_candidates = {*buy, *hold};
    const auto baseline_buy = ContextualActionEvaluator{}.evaluate(
        active, priorities, lineup, baseline_buy_context, nullptr, native.match_id);
    const auto baseline_buy_score = std::find_if(
        baseline_buy.candidates.begin(), baseline_buy.candidates.end(),
        [&](const auto& score) { return score.candidate_id == buy->candidate_id; });
    assert(baseline_buy_score != baseline_buy.candidates.end());
    const double effective_opportunity_cost =
        buy_score->opportunity_cost * (1.0 - buy_score->opportunity_cost_uncertainty);
    assert(std::abs(buy_score->economy_cost -
        (baseline_buy_score->economy_cost + effective_opportunity_cost)) < 1e-9);

    // Prove the complete native chain using the exact lineup and physical unit.
    auto integrated_context = context;
    integrated_context.sequence = native.sequence;
    integrated_context.action_candidates = {*deploy, *hold};
    const auto contextual = ContextualActionEvaluator{}.evaluate(
        active, priorities, lineup, integrated_context, nullptr, native.match_id);
    assert(!contextual.stale);
    assert(contextual.recommended_action == StrategicActionKind::DeployOrMove);
    StrategicActionResolutionRequest request;
    request.recommendation_id = "lineup-position-executor-integration";
    request.expected_snapshot_sequence = native.sequence;
    request.recommendation = &contextual;
    request.source_context = &integrated_context;
    request.current_state = &native;
    const auto resolution = StrategicActionExecutor{}.resolve(request);
    assert(resolution.accepted);
    assert(resolution.recommended_kind == StrategicActionKind::DeployOrMove);
    assert(resolution.recommended_champion_id == 20);
    assert(resolution.native_action.values[0] ==
        static_cast<std::int32_t>(decision::ActionType::MOVE_BENCH));
    assert(resolution.native_action.values[2] == deploy->source_slot);
    assert(resolution.native_action.values[3] == deploy->target_board_slot);

    std::unordered_set<std::string> stable_ids;
    for (const auto& candidate : result.candidates) {
        assert(!candidate.candidate_id.empty());
        assert(candidate.source_sequence == native.sequence);
        assert(stable_ids.insert(candidate.candidate_id).second);
        assert(candidate.evidence_uncertainty >= 0.0 &&
            candidate.evidence_uncertainty <= 1.0);
    }

    auto protected_lineup = lineup;
    protected_lineup.selected_board.push_back(
        {30, LineupSlotKind::Bridge, 50, false, true});
    auto protected_native = native;
    const auto protected_result = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, protected_lineup, protected_native, costs);
    const auto protected_sale = std::find_if(
        protected_result.candidates.begin(), protected_result.candidates.end(),
        [](const auto& candidate) {
            return candidate.kind == StrategicActionKind::SellUnit &&
                candidate.champion_id == 30;
        });
    assert(protected_sale == protected_result.candidates.end());

    auto stale_lineup = lineup;
    stale_lineup.sequence = native.sequence - 1;
    auto stale_native = native;
    const auto rejected = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, stale_lineup, stale_native, costs);
    assert(rejected.candidates.empty());
    assert(rejected.status == "lineup_identity_or_sequence_mismatch");
}

void missing_cost_rejects_only_the_affected_candidate() {
    CompositionCandidate composition;
    composition.composition_id = "partial-candidate-set";
    composition.set_id = "TFT18";
    composition.target_board_size = 1;
    composition.units = {{10, tft::composition_intelligence::UnitRole::MainCarry, true, 80}};
    composition.main_carry_id = 10;
    const std::optional<ActiveComposition> active = ActiveComposition{composition, 2};

    UnitPriority priority;
    priority.champion_id = 10;
    priority.intent = UnitIntent::Seek;
    UnitPrioritySnapshot priorities;
    priorities.composition_id = composition.composition_id;
    priorities.composition_version = 2;
    priorities.units = {priority};
    LineupPlan lineup;
    lineup.composition_id = composition.composition_id;
    lineup.composition_version = 2;
    lineup.match_id = 88; lineup.player_id = 0; lineup.round = 10; lineup.sequence = 7;
    lineup.endgame_target_ids = {10};

    StrategicSharedContext context;
    context.player_id = 0;
    context.round = 10;
    context.gold = 10;
    context.alive = true;
    context.evidence.gold = true;
    StrategicActionNativeSnapshot native;
    native.match_id = 88;
    native.player_id = 0;
    native.round = 10;
    native.sequence = 7;
    native.composition_id = composition.composition_id;
    native.composition_version = 2;
    native.gold = 10;
    native.alive = true;
    native.shop_champion_ids[0] = 10;
    enables(native.masks, decision::ActionType::PASS);
    enables(native.masks, decision::ActionType::BUY);
    native.masks.shop_mask[0] = decision::MASK_ENABLED;

    const auto result = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, lineup, native, {});
    assert(result.status == "candidates_generated");
    assert(result.rejected_missing_cost == 1);
    assert(result.candidates.size() == 1);
    assert(result.candidates.front().kind == StrategicActionKind::Hold);
}

void xp_candidate_does_not_depend_on_an_active_composition() {
    StrategicSharedContext context;
    context.player_id = 0;
    context.round = 3;
    context.alive = true;
    context.gold = 8;
    context.level = 4;
    context.xp_to_next = 4;
    context.evidence.gold = true;
    context.evidence.level = true;
    context.evidence.xp_to_next = true;

    StrategicActionNativeSnapshot native;
    native.match_id = 9;
    native.player_id = 0;
    native.round = 3;
    native.sequence = 2;
    native.gold = 8;
    native.alive = true;
    enables(native.masks, decision::ActionType::BUY_XP);

    const auto result = StrategicActionCandidateBuilder{}.build(
        context, std::nullopt, {}, {}, native, {});
    assert(result.status == "candidates_generated");
    assert(result.candidates.size() == 1);
    assert(result.candidates.front().kind == StrategicActionKind::BuyExperience);
    assert(result.candidates.front().gold_cost == EconomyEngine::BUY_XP_COST);
}

void xp_level_up_values_only_a_verified_selected_bench_unit() {
    CompositionCandidate composition;
    composition.composition_id = "xp-progression";
    composition.set_id = "TFT18";
    composition.target_board_size = 2;
    composition.units = {
        {10, tft::composition_intelligence::UnitRole::MainCarry, true, 80},
        {20, tft::composition_intelligence::UnitRole::Frontline, true, 70}
    };
    const std::optional<ActiveComposition> active = ActiveComposition{composition, 2};

    UnitPriority bench_priority;
    bench_priority.champion_id = 20;
    bench_priority.intent = UnitIntent::Seek;
    bench_priority.priority = 80;
    bench_priority.board_contribution = 0.7;
    bench_priority.confidence = 0.8;
    UnitPrioritySnapshot priorities;
    priorities.composition_id = composition.composition_id;
    priorities.composition_version = 2;
    UnitPriority carry_priority;
    carry_priority.champion_id = 10;
    carry_priority.intent = UnitIntent::Upgrade;
    carry_priority.priority = 90;
    carry_priority.copies_owned = 1;
    carry_priority.highest_star = 1;
    carry_priority.target_star = 2;
    carry_priority.board_contribution = 0.8;
    carry_priority.confidence = 0.9;
    priorities.units = {bench_priority, carry_priority};

    LineupPlan lineup;
    lineup.composition_id = composition.composition_id;
    lineup.composition_version = 2;
    lineup.match_id = 77; lineup.player_id = 0; lineup.round = 9; lineup.sequence = 42;
    lineup.endgame_target_ids = {10, 20};
    lineup.selected_board = {
        {10, LineupSlotKind::ActiveTarget, 90, true, true},
        {20, LineupSlotKind::ActiveTarget, 80, false, true}
    };

    StrategicSharedContext context;
    context.match_id = 77; context.player_id = 0; context.round = 9;
    context.sequence = 42; context.alive = true; context.gold = 20;
    context.level = 1; context.xp_to_next = EconomyEngine::XP_PER_BUY;
    context.evidence.gold = true; context.evidence.level = true;
    context.evidence.xp_to_next = true;
    StrategicUnitCandidate owned_bench_unit;
    owned_bench_unit.champion_id = 20;
    owned_bench_unit.on_bench = true;
    owned_bench_unit.board_contribution = 0.7;
    owned_bench_unit.composition_fit = 0.8;
    context.owned_units = {owned_bench_unit};

    StrategicActionNativeSnapshot native;
    native.match_id = 77; native.player_id = 0; native.round = 9;
    native.sequence = 42; native.composition_id = composition.composition_id;
    native.composition_version = 2; native.gold = 20; native.alive = true;
    native.board_champion_ids[0] = 10;
    native.board_unit_uuids[0] = "unit-10";
    native.bench_champion_ids[0] = 20;
    native.bench_unit_uuids[0] = "unit-20";
    native.shop_champion_ids[0] = 10;
    native.unit_costs[10] = 3;
    native.masks.shop_mask[0] = MASK_ENABLED;
    enables(native.masks, decision::ActionType::PASS);
    enables(native.masks, decision::ActionType::BUY);
    enables(native.masks, decision::ActionType::BUY_XP);

    const auto result = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, lineup, native, {});
    const auto xp = std::find_if(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) {
            return candidate.kind == StrategicActionKind::BuyExperience;
        });
    assert(xp != result.candidates.end());
    assert(std::abs(xp->expected_board_delta - 0.7) < 1e-9);
    assert(xp->evidence_source.find("UnitPriorityPlanner") != std::string::npos);
    assert(xp->evidence_horizon_rounds == 1);
    assert(std::abs(xp->evidence_uncertainty - 0.2) < 1e-9);

    const auto hold = std::find_if(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) { return candidate.kind == StrategicActionKind::Hold; });
    assert(hold != result.candidates.end());
    context.action_candidates = {*xp, *hold};
    const auto evaluation = ContextualActionEvaluator{}.evaluate(
        active, priorities, lineup, context, nullptr, native.match_id);
    assert(!evaluation.stale);
    assert(evaluation.recommended_action == StrategicActionKind::BuyExperience);
    const auto xp_score = std::find_if(evaluation.candidates.begin(), evaluation.candidates.end(),
        [&](const auto& score) { return score.candidate_id == xp->candidate_id; });
    assert(xp_score != evaluation.candidates.end());
    assert(xp_score->board_value > 0.0);
    assert(xp_score->total_score > 0.0);

    const auto buy_candidate = std::find_if(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) {
            return candidate.kind == StrategicActionKind::BuyUnit &&
                candidate.champion_id == 10;
        });
    assert(buy_candidate != result.candidates.end());
    context.action_candidates = {*xp, *buy_candidate, *hold};
    const auto cross_action = ContextualActionEvaluator{}.evaluate(
        active, priorities, lineup, context, nullptr, native.match_id);
    assert(cross_action.recommended_action == StrategicActionKind::BuyUnit);
    const auto progression_score = std::find_if(
        cross_action.candidates.begin(), cross_action.candidates.end(),
        [&](const auto& score) { return score.candidate_id == xp->candidate_id; });
    assert(progression_score != cross_action.candidates.end());
    assert(progression_score->opportunity_cost_available);
    assert(progression_score->opportunity_cost_value_basis == "contextual_action_score.v1");
    assert(progression_score->opportunity_cost_forgone_candidate_id ==
        buy_candidate->candidate_id);
}

void native_anchor_shop_offer_is_actionable_before_composition_lock() {
    StrategicSharedContext context;
    context.player_id = 0; context.round = 4; context.gold = 8;
    context.alive = true; context.evidence.gold = true;
    StrategicAnchorCandidate anchor;
    anchor.unit.champion_id = 44;
    anchor.unit.board_contribution = 0.65;
    anchor.unit.composition_fit = 0.9;
    anchor.unit.copies_owned = 2;
    anchor.target_composition_direction = "Invoker";
    anchor.anchor_value = 4.2;
    anchor.shop_available = true;
    anchor.candidate_unit_ids = {44, 45, 46};
    context.anchor_candidates = {anchor};

    StrategicActionNativeSnapshot native;
    native.match_id = 77; native.player_id = 0; native.round = 4;
    native.sequence = 11; native.gold = 8; native.alive = true;
    native.shop_champion_ids[2] = 44;
    enables(native.masks, decision::ActionType::BUY);
    native.masks.shop_mask[2] = decision::MASK_ENABLED;

    const auto result = StrategicActionCandidateBuilder{}.build(
        context, std::nullopt, {}, {}, native, {{44, 3}});
    const auto buy = std::find_if(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) {
            return candidate.kind == StrategicActionKind::BuyUnit && candidate.champion_id == 44;
        });
    assert(buy != result.candidates.end());
    assert(buy->shop_slot == 2 && buy->source_sequence == 11);
    assert(buy->evidence_source.find("NativeStrategicCompositionGenerator") != std::string::npos);
    assert(buy->composition_fit == 0.9 && buy->upgrade_value == 1.0);
}

void owned_unit_candidates_require_native_physical_identity() {
    CompositionCandidate composition;
    composition.composition_id = "uuid-required";
    composition.set_id = "TFT18";
    composition.target_board_size = 1;
    composition.units = {{10, tft::composition_intelligence::UnitRole::MainCarry, true, 80}};
    const std::optional<ActiveComposition> active = ActiveComposition{composition, 1};
    UnitPriority sell;
    sell.champion_id = 30; sell.intent = UnitIntent::SellCandidate;
    sell.copies_owned = 1; sell.highest_star = 1;
    UnitPrioritySnapshot priorities;
    priorities.composition_id = composition.composition_id;
    priorities.composition_version = 1;
    priorities.units = {sell};
    LineupPlan lineup;
    lineup.composition_id = composition.composition_id;
    lineup.composition_version = 1;
    lineup.match_id = 7; lineup.player_id = 0; lineup.round = 2; lineup.sequence = 9;
    StrategicSharedContext context;
    context.player_id = 0; context.round = 2; context.gold = 5;
    context.alive = true; context.evidence.gold = true;
    StrategicActionNativeSnapshot native;
    native.match_id = 7; native.player_id = 0; native.round = 2;
    native.sequence = 9; native.composition_id = composition.composition_id;
    native.composition_version = 1; native.gold = 5; native.alive = true;
    native.bench_champion_ids[0] = 30;
    enables(native.masks, decision::ActionType::SELL);
    native.masks.bench_source_mask[0] = decision::MASK_ENABLED;
    const auto result = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, lineup, native, {{30, 1}});
    assert(result.rejected_missing_instance_identity == 1);
    assert(std::none_of(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) { return candidate.kind == StrategicActionKind::SellUnit; }));
}

void ambiguous_owned_copy_is_not_selected_by_incidental_order() {
    CompositionCandidate composition;
    composition.composition_id = "ambiguous-copy"; composition.set_id = "TFT18";
    composition.target_board_size = 1;
    composition.units = {{10, tft::composition_intelligence::UnitRole::MainCarry, true, 80}};
    const std::optional<ActiveComposition> active = ActiveComposition{composition, 1};
    UnitPriority sell;
    sell.champion_id = 30; sell.intent = UnitIntent::SellCandidate;
    sell.copies_owned = 1; sell.highest_star = 1;
    UnitPrioritySnapshot priorities;
    priorities.composition_id = composition.composition_id;
    priorities.composition_version = 1; priorities.units = {sell};
    LineupPlan lineup;
    lineup.composition_id = composition.composition_id;
    lineup.composition_version = 1;
    lineup.match_id = 7; lineup.player_id = 0; lineup.round = 2; lineup.sequence = 9;
    StrategicSharedContext context;
    context.player_id = 0; context.round = 2; context.gold = 5;
    context.alive = true; context.evidence.gold = true;
    StrategicActionNativeSnapshot native;
    native.match_id = 7; native.player_id = 0; native.round = 2;
    native.sequence = 9; native.composition_id = composition.composition_id;
    native.composition_version = 1; native.gold = 5; native.alive = true;
    native.bench_champion_ids[0] = 30; native.bench_champion_ids[1] = 30;
    native.bench_unit_uuids[0] = "copy-a"; native.bench_unit_uuids[1] = "copy-b";
    enables(native.masks, decision::ActionType::SELL);
    native.masks.bench_source_mask[0] = decision::MASK_ENABLED;
    native.masks.bench_source_mask[1] = decision::MASK_ENABLED;
    const auto result = StrategicActionCandidateBuilder{}.build(
        context, active, priorities, lineup, native, {{30, 1}});
    assert(result.rejected_ambiguous_instance == 1);
    assert(std::none_of(result.candidates.begin(), result.candidates.end(),
        [](const auto& candidate) { return candidate.kind == StrategicActionKind::SellUnit; }));
}

void empty_legal_action_set_is_reported_as_no_candidates() {
    StrategicSharedContext context;
    context.player_id = 0; context.round = 2; context.gold = 5;
    context.alive = true; context.evidence.gold = true;
    StrategicActionNativeSnapshot native;
    native.match_id = 7; native.player_id = 0; native.round = 2;
    native.sequence = 9; native.gold = 5; native.alive = true;
    const auto result = StrategicActionCandidateBuilder{}.build(
        context, std::nullopt, {}, {}, native, {});
    assert(result.candidates.empty());
    assert(result.status == "no_candidates");
}

void builder_refuses_stale_or_mismatched_native_snapshots() {
    StrategicSharedContext context;
    context.player_id = 1;
    context.round = 2;
    context.alive = true;
    context.gold = 10;
    StrategicActionNativeSnapshot native;
    native.match_id = 4;
    native.player_id = 0;
    native.round = 2;
    native.sequence = 5;
    native.gold = 10;
    native.alive = true;
    const auto result = StrategicActionCandidateBuilder{}.build(
        context, std::nullopt, {}, {}, native, {});
    assert(result.candidates.empty());
    assert(result.status == "invalid_or_mismatched_native_snapshot");
}
}

void interest_breakpoints_are_compared_to_the_same_hold_snapshot() {
    const auto evaluate = [](std::int32_t gold) {
        StrategicSharedContext context;
        context.player_id = 0; context.round = 5; context.gold = gold;
        context.level = 4; context.xp_to_next = 4; context.alive = true;
        context.evidence.gold = true; context.evidence.level = true;
        context.evidence.xp_to_next = true;
        StrategicActionNativeSnapshot native;
        native.match_id = 19; native.player_id = 0; native.round = 5;
        native.sequence = 3; native.gold = gold; native.alive = true;
        enables(native.masks, decision::ActionType::PASS);
        enables(native.masks, decision::ActionType::BUY_XP);
        return StrategicActionCandidateBuilder{}.build(
            context, std::nullopt, {}, {}, native, {});
    };
    for (const auto gold : {9, 10, 11}) {
        const auto result = evaluate(gold);
        const auto xp = std::find_if(result.candidates.begin(), result.candidates.end(),
            [](const auto& value) { return value.kind == StrategicActionKind::BuyExperience; });
        assert(xp != result.candidates.end());
        assert(xp->marginal_economy_evidence_available);
        const auto expected_before = EconomyEngine{}.get_interest(gold);
        const auto expected_after = EconomyEngine{}.get_interest(gold - EconomyEngine::BUY_XP_COST);
        assert(xp->marginal_interest_before == expected_before);
        assert(xp->marginal_interest_after == expected_after);
        assert(xp->lost_interest_cost == std::max(0, expected_before - expected_after));
    }
}

int main() {
    builder_emits_snapshot_bound_physical_candidates();
    interest_breakpoints_are_compared_to_the_same_hold_snapshot();
    missing_cost_rejects_only_the_affected_candidate();
    xp_candidate_does_not_depend_on_an_active_composition();
    xp_level_up_values_only_a_verified_selected_bench_unit();
    builder_refuses_stale_or_mismatched_native_snapshots();
    owned_unit_candidates_require_native_physical_identity();
    native_anchor_shop_offer_is_actionable_before_composition_lock();
    ambiguous_owned_copy_is_not_selected_by_incidental_order();
    empty_legal_action_set_is_reported_as_no_candidates();
    std::cout << "StrategicActionCandidateBuilder tests passed\\n";
}
