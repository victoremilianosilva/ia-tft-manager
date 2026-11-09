#include "strategy/StrategicPlanner.hpp"

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
            false, 0.1, 0.1, 0.0, {"Duelist"}}
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
    assert(decision.composition_decision == CompositionDecision::Keep);
    assert(decision.target_composition_direction == "Bruiser");
    assert(std::find(decision.preserve_unit_ids.begin(),
                     decision.preserve_unit_ids.end(), 10) != decision.preserve_unit_ids.end());

    // A strong anchor cannot trigger a pivot on a single review while locked.
    context.anchor_candidates.clear();
    context.current_direction_score = 1.0;
    context.anchor_candidates.push_back(anchor(91, "Invoker", 6.0, 0.2, 2));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Keep);
    assert(commitment.consecutive_reviews == 1);
    assert(commitment.candidate_composition_direction == "Invoker");

    context.round++;
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Keep);
    assert(commitment.consecutive_reviews == 2);

    context.round++;
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Pivot);
    assert(decision.target_composition_direction == "Invoker");
    assert(decision.shadow_only);
    assert(commitment.composition_direction == "Invoker");
    assert(commitment.consecutive_reviews == 0);

    // A high-cost unit with poor fit and excessive transition cost is rejected.
    context = base_context();
    commitment = {};
    context.anchor_candidates.push_back(anchor(92, "Mage", 0.5, 10.0, 0));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Keep);

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
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Abandon);
    assert(decision.target_composition_direction == "Bruiser");

    // An empty initial direction can be initialized from a viable anchor.
    context.current_composition_direction.clear();
    context.current_direction_viable = false;
    context.anchor_candidates.push_back(anchor(94, "Warden", 3.0, 1.0, 1));
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Adapt);
    assert(decision.target_composition_direction == "Warden");

    // Invalid numeric candidates never become anchors.
    context.anchor_candidates.clear();
    auto invalid = anchor(95, "Assassin", 5.0, 0.1, 1);
    invalid.unit.item_fit = std::nan("");
    context.anchor_candidates.push_back(invalid);
    context.current_composition_direction.clear();
    decision = planner.evaluate(context, commitment);
    assert(decision.composition_decision == CompositionDecision::Keep ||
           decision.composition_decision == CompositionDecision::Adapt);
    assert(decision.anchor_champion_id == -1);

    std::cout << "strategic planner shadow tests passed\n";
    return 0;
}
