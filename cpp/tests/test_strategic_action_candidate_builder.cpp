#include "composition_intelligence/StrategicActionCandidateBuilder.hpp"

#include <cassert>
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
    UnitPriority frontline;
    frontline.champion_id = 20;
    frontline.intent = UnitIntent::Seek;
    frontline.priority = 80;
    frontline.board_contribution = 0.7;
    UnitPriority sale;
    sale.champion_id = 30;
    sale.intent = UnitIntent::SellCandidate;
    sale.copies_owned = 1;
    sale.highest_star = 1;
    priorities.units = {carry, frontline, sale};

    LineupPlan lineup;
    lineup.composition_id = "candidate-builder";
    lineup.composition_version = 3;
    lineup.endgame_target_ids = {10, 20};
    lineup.selected_board = {
        {10, LineupSlotKind::ActiveTarget, 90, true, true},
        {20, LineupSlotKind::ActiveTarget, 80, false, true}
    };

    StrategicSharedContext context;
    context.player_id = 0;
    context.round = 9;
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
    assert(buy->lost_interest_cost > 0.0);

    const auto xp = find(StrategicActionKind::BuyExperience);
    assert(xp != result.candidates.end() && xp->gold_cost == EconomyEngine::BUY_XP_COST);
    const auto reroll = find(StrategicActionKind::RerollShop);
    assert(reroll != result.candidates.end() && reroll->gold_cost == EconomyEngine::REROLL_COST);
    const auto sell = find(StrategicActionKind::SellUnit, 30);
    assert(sell != result.candidates.end());
    assert(sell->source_is_bench && sell->source_slot == 1);
    assert(sell->source_unit_uuid == "unit-30");
    assert(sell->direct_gold_cost == -1.0);

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

    std::unordered_set<std::string> stable_ids;
    for (const auto& candidate : result.candidates) {
        assert(!candidate.candidate_id.empty());
        assert(candidate.source_sequence == native.sequence);
        assert(stable_ids.insert(candidate.candidate_id).second);
        assert(candidate.evidence_uncertainty >= 0.0 &&
            candidate.evidence_uncertainty <= 1.0);
    }
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

int main() {
    builder_emits_snapshot_bound_physical_candidates();
    missing_cost_rejects_only_the_affected_candidate();
    xp_candidate_does_not_depend_on_an_active_composition();
    builder_refuses_stale_or_mismatched_native_snapshots();
    owned_unit_candidates_require_native_physical_identity();
    native_anchor_shop_offer_is_actionable_before_composition_lock();
    ambiguous_owned_copy_is_not_selected_by_incidental_order();
    empty_legal_action_set_is_reported_as_no_candidates();
    std::cout << "StrategicActionCandidateBuilder tests passed\\n";
}
