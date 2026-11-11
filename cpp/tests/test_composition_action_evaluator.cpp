#include "composition_intelligence/CompositionActionEvaluator.hpp"

#include <cassert>
#include <iostream>

using namespace tft::composition_intelligence;
using namespace tft::strategy;

namespace {
ActiveComposition active() {
    CompositionCandidate c;
    c.composition_id = "comp-a"; c.set_id = "TFT18"; c.target_board_size = 2;
    c.main_carry_id = 10;
    c.units = {{10, UnitRole::MainCarry, true, 80}, {20, UnitRole::Frontline, true, 70}};
    return {c, 4};
}
UnitPrioritySnapshot priorities() {
    UnitPrioritySnapshot p; p.composition_id = "comp-a"; p.composition_version = 4;
    UnitPriority seek; seek.champion_id = 20; seek.intent = UnitIntent::Seek;
    seek.priority = 70; seek.confidence = .8;
    UnitPriority upgrade; upgrade.champion_id = 10; upgrade.intent = UnitIntent::Upgrade;
    upgrade.priority = 90; upgrade.target_star = 2; upgrade.confidence = .9;
    UnitPriority sell; sell.champion_id = 30; sell.intent = UnitIntent::SellCandidate;
    sell.priority = 5;
    p.units = {seek, upgrade, sell}; return p;
}
LineupPlan lineup() {
    LineupPlan l; l.composition_id = "comp-a"; l.composition_version = 4;
    l.endgame_target_ids = {10,20};
    l.selected_board = {{10,LineupSlotKind::ActiveTarget,90,true,true},
                        {20,LineupSlotKind::ActiveTarget,70,false,true}};
    return l;
}
StrategicActionCandidate candidate(StrategicActionKind kind, int id = -1) {
    StrategicActionCandidate c; c.kind = kind; c.champion_id = id;
    c.available = true; c.expected_board_delta = .5;
    if (kind == StrategicActionKind::BuyUnit) { c.gold_cost = 3; c.direct_gold_cost = 3; }
    return c;
}
void stale_snapshots_are_rejected() {
    auto p = priorities(); p.composition_version = 3;
    StrategicSharedContext c; c.alive = true;
    auto result = CompositionActionEvaluator{}.evaluate(active(),p,lineup(),c,{});
    assert(result.stale && result.evaluation.recommended_action == StrategicActionKind::Hold);
    assert(result.candidates.empty());
}
void buy_requires_seek_or_upgrade_and_target_membership() {
    StrategicSharedContext c; c.alive = true; c.gold = 10;
    c.action_candidates = {candidate(StrategicActionKind::BuyUnit,20),
                           candidate(StrategicActionKind::BuyUnit,30)};
    auto result = CompositionActionEvaluator{}.evaluate(active(),priorities(),lineup(),c,{});
    assert(result.candidates.size() == 2);
    assert(result.candidates[0].disposition == ActionCandidateDisposition::Accepted);
    assert(result.candidates[1].disposition == ActionCandidateDisposition::Rejected);
    assert(result.evaluation.candidate_scores.size() == 2);
    assert(!result.evaluation.candidate_scores[1].available);
}
void sell_candidate_is_not_automatic_and_restricted_sale_is_rejected() {
    auto p = priorities();
    p.units.back().sale_restricted = true;
    StrategicSharedContext c; c.alive = true; c.gold = 10;
    c.action_candidates = {candidate(StrategicActionKind::SellUnit,30)};
    auto result = CompositionActionEvaluator{}.evaluate(active(),p,lineup(),c,{});
    assert(result.candidates[0].disposition == ActionCandidateDisposition::Rejected);
    assert(!result.evaluation.candidate_scores[0].available);
}
void sell_rejects_pairs_and_existing_star_progress() {
    auto p = priorities();
    p.units.back().copies_owned = 2;
    p.units.back().highest_star = 1;
    StrategicSharedContext c; c.alive = true; c.gold = 10;
    c.action_candidates = {candidate(StrategicActionKind::SellUnit,30)};
    auto result = CompositionActionEvaluator{}.evaluate(active(),p,lineup(),c,{});
    assert(result.candidates[0].disposition == ActionCandidateDisposition::Rejected);
    assert(result.candidates[0].reason.find("pair/star") != std::string::npos);
    assert(!result.evaluation.candidate_scores[0].available);

    p.units.back().copies_owned = 1;
    p.units.back().highest_star = 2;
    result = CompositionActionEvaluator{}.evaluate(active(),p,lineup(),c,{});
    assert(result.candidates[0].disposition == ActionCandidateDisposition::Rejected);
}

void duplicate_candidates_keep_single_selection() {
    StrategicSharedContext c; c.alive = true; c.gold = 10;
    c.action_candidates = {candidate(StrategicActionKind::BuyUnit,20),
                           candidate(StrategicActionKind::BuyUnit,20)};
    auto result = CompositionActionEvaluator{}.evaluate(active(),priorities(),lineup(),c,{});
    int selected = 0;
    for (const auto& a : result.candidates) if (a.selected) ++selected;
    assert(selected == 1);
}

void validated_economy_and_item_evidence_reach_action_evaluator() {
    auto p = priorities();
    StrategicSharedContext c;
    c.alive = true;
    c.gold = 10;
    c.player_id = 0;
    c.round = 9;
    c.action_candidates = {candidate(StrategicActionKind::BuyUnit, 20),
                           candidate(StrategicActionKind::SellUnit, 30),
                           candidate(StrategicActionKind::DeployOrMove, 20)};
    PlannerEvidenceSnapshot evidence;
    evidence.match_id = 55;
    evidence.player_id = 0;
    evidence.composition_id = "comp-a";
    evidence.composition_version = 4;
    evidence.round = 9;
    const auto set_valid = [&](EvidenceSourceMetadata& m, const std::string& source) {
        m.source = source;
        m.source_version = 4;
        m.match_id = 55;
        m.player_id = 0;
        m.composition_id = "comp-a";
        m.source_round = 9;
        m.expected_round = 9;
        m.quality = EvidenceQuality::Valid;
        m.available = true;
    };
    set_valid(evidence.economy.metadata, "EconomicController");
    set_valid(evidence.board.metadata, "BoardEvaluation");
    set_valid(evidence.items.metadata, "ItemEngine");
    evidence.economy.buy_unit_opportunity_cost = 2.5;
    evidence.board.missing_frontline_count = 1;
    evidence.items.units.push_back({30, {"equipped-item"}, {}, 0.0, 0.0, true, false});
    const auto result = CompositionActionEvaluator{}.evaluate(
        active(), p, lineup(), c, {}, StrategicActionKind::None, &evidence, 55);
    assert(!result.stale);
    assert(result.economy_evidence_consumed);
    assert(result.board_evidence_validated);
    assert(result.item_evidence_consumed);
    assert(result.candidates.size() == 3);
    assert(result.candidates[1].disposition == ActionCandidateDisposition::Rejected);
    assert(result.candidates[1].reason.find("equipped-item") != std::string::npos);
    assert(result.evaluation.candidate_scores[0].opportunity_cost == 2.5);
    assert(result.evaluation.candidate_scores[2].composition_component > 0.0);
}

void hold_is_a_valid_zero_cost_baseline() {
    StrategicSharedContext c; c.alive = true; c.gold = 10;
    c.action_candidates = {candidate(StrategicActionKind::Hold)};
    auto result = CompositionActionEvaluator{}.evaluate(active(),priorities(),lineup(),c,{});
    assert(result.evaluation.recommended_action == StrategicActionKind::Hold);
    assert(result.candidates[0].disposition == ActionCandidateDisposition::Accepted);
}
}

int main() {
    stale_snapshots_are_rejected();
    buy_requires_seek_or_upgrade_and_target_membership();
    sell_candidate_is_not_automatic_and_restricted_sale_is_rejected();
    sell_rejects_pairs_and_existing_star_progress();
    duplicate_candidates_keep_single_selection();
    validated_economy_and_item_evidence_reach_action_evaluator();
    hold_is_a_valid_zero_cost_baseline();
    std::cout << "CompositionActionEvaluator tests passed\n";
}
