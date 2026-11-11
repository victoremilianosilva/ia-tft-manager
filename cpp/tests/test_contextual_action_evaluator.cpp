#include "composition_intelligence/ContextualActionEvaluator.hpp"
#include "strategy/ActionEvaluator.hpp"

#include <cassert>
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
    c.available = true; c.expected_board_delta = .8;
    if (kind == StrategicActionKind::BuyUnit) { c.gold_cost = 3; c.direct_gold_cost = 3; }
    if (kind == StrategicActionKind::RerollShop) { c.gold_cost = 2; c.direct_gold_cost = 2; }
    return c;
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
    context.action_candidates = {candidate(StrategicActionKind::BuyUnit,20),
        candidate(StrategicActionKind::DeployOrMove,20), candidate(StrategicActionKind::Hold)};
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(!result.stale);
    assert(result.candidates.size() == 3);
    assert(result.recommended_action == StrategicActionKind::BuyUnit ||
        result.recommended_action == StrategicActionKind::DeployOrMove);
    int selected = 0;
    for (const auto& c : result.candidates) if (c.selected) ++selected;
    assert(selected == 1);
}
void stale_identity_disables_contextual_recommendation() {
    StrategicSharedContext context;
    context.alive = true; context.player_id = 1; context.round = 8;
    const auto result = ContextualActionEvaluator{}.evaluate(
        active(), priorities(), lineup(), context, nullptr, 77);
    assert(result.stale);
    assert(result.recommended_action == StrategicActionKind::Hold);
    assert(result.candidates.empty());
}
void invalid_candidates_and_equipped_sales_are_rejected() {
    StrategicSharedContext context;
    context.alive = true; context.gold = 10; context.player_id = 0; context.round = 8;
    context.action_candidates = {candidate(StrategicActionKind::BuyUnit,30),
        candidate(StrategicActionKind::SellUnit,30)};
    PlannerEvidenceSnapshot evidence;
    evidence.match_id=77; evidence.player_id=0; evidence.composition_id="comp-a";
    evidence.composition_version=4; evidence.round=8;
    auto set_valid = [&](EvidenceSourceMetadata& m, const std::string& name) {
        m.source=name; m.source_version=4; m.match_id=77; m.player_id=0;
        m.composition_id="comp-a"; m.source_round=8; m.expected_round=8;
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
    assert(result.candidates[1].rejection_reason == "sale_restricted_by_item_or_transition_risk");
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
    baseline_is_unchanged_by_contextual_execution();
    contextual_path_uses_priority_and_lineup_without_calling_baseline();
    stale_identity_disables_contextual_recommendation();
    invalid_candidates_and_equipped_sales_are_rejected();
    json_is_versioned_and_shadow_only();
    std::cout << "ContextualActionEvaluator tests passed\\n";
}
