#include "composition_intelligence/StrategicActionCandidateBuilder.hpp"

#include <cassert>
#include <iostream>

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
        {10, UnitRole::MainCarry, true, 80},
        {20, UnitRole::Frontline, true, 70}
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

    const auto xp = find(StrategicActionKind::BuyExperience);
    assert(xp != result.candidates.end() && xp->gold_cost == EconomyEngine::BUY_XP_COST);
    const auto reroll = find(StrategicActionKind::RerollShop);
    assert(reroll != result.candidates.end() && reroll->gold_cost == EconomyEngine::REROLL_COST);
    const auto sell = find(StrategicActionKind::SellUnit, 30);
    assert(sell != result.candidates.end());
    assert(sell->source_is_bench && sell->source_slot == 1);
    assert(sell->direct_gold_cost == -1.0);

    const auto deploy = find(StrategicActionKind::DeployOrMove, 20);
    assert(deploy != result.candidates.end());
    assert(deploy->source_is_bench && deploy->source_slot == 0);
    assert(deploy->target_board_slot >= 0);
    assert(!native.requested_move_targets.empty());

    const auto hold = find(StrategicActionKind::Hold);
    assert(hold != result.candidates.end());
    assert(hold->evidence_reason.find("neutral_baseline") != std::string::npos);
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
    builder_refuses_stale_or_mismatched_native_snapshots();
    std::cout << "StrategicActionCandidateBuilder tests passed\\n";
}
