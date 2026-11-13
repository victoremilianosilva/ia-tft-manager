#include "composition_intelligence/CompositionEvaluation.hpp"

#include <cassert>
#include <iostream>

using namespace tft::composition_intelligence;

namespace {
CompositionCandidate comp(std::string id, std::initializer_list<int> ids) {
    CompositionCandidate c;
    c.composition_id = std::move(id);
    c.source = CompositionSource::Native;
    c.set_id = "18";
    c.target_board_size = 8;
    int priority = 100;
    for (const auto id : ids)
        c.units.push_back({id, UnitRole::Flex, true, priority--});
    c.main_carry_id = c.units.empty() ? -1 : c.units.front().champion_id;
    return c;
}
CandidateEvidence evidence(std::string id, double board, double items = 0.7,
    double availability = 0.8, double economy = 0.8, double cost = -1.0) {
    CandidateEvidence e;
    e.composition_id = std::move(id);
    e.board_fit = board;
    e.item_fit = items;
    e.availability = availability;
    e.economy_feasibility = economy;
    e.estimated_gold_cost = cost;
    e.evidence_confidence = 0.9;
    return e;
}
CompositionEvaluationContext context(std::uint32_t round = 1) {
    CompositionEvaluationContext c;
    c.round = round;
    c.level = 8;
    c.gold = 50;
    c.match_id = 7001;
    c.player_id = 0;
    return c;
}
void selects_initial_complete_candidate() {
    ActiveCompositionManager active;
    TransitionManager transitions;
    auto c = comp("initial", {1, 2, 3});
    auto ctx = context();
    ctx.candidate_evidence = {evidence("initial", 0.8)};
    auto proposal = transitions.propose(active.current(), {c}, ctx);
    assert(proposal.decision == CompositionDecision::SelectInitial);
    assert(proposal.target.has_value());
    assert(proposal.approved);
    auto published = transitions.publish_if_approved(proposal, active);
    assert(published.status == PublishStatus::Published);
    assert(active.current()->version == 1);
}
void keeps_active_when_advantage_is_below_margin() {
    auto active = ActiveCompositionManager{};
    auto current = comp("current", {1, 2, 3});
    active.publish(current);
    auto alternative = comp("alternative", {7, 8, 9});
    auto ctx = context();
    ctx.candidate_evidence = {
        evidence("current", 0.65), evidence("alternative", 0.68)
    };
    TransitionManager transitions;
    auto proposal = transitions.propose(active.current(), {current, alternative}, ctx);
    assert(proposal.decision == CompositionDecision::Keep);
    assert(!proposal.target.has_value());
}
void pivot_requires_consecutive_rounds_and_complete_target() {
    ActiveCompositionManager active;
    auto current = comp("current", {1, 2, 3});
    active.publish(current);
    auto alternative = comp("alternative", {7, 8, 9});
    TransitionManager transitions;
    auto first = context(10);
    first.gold = 100;
    first.candidate_evidence = {
        evidence("current", 0.45), evidence("alternative", 0.95, 0.9, 0.9, 0.9, 5.0)
    };
    auto p1 = transitions.propose(active.current(), {current, alternative}, first);
    assert(p1.decision == CompositionDecision::Pivot);
    assert(p1.target && p1.target->composition_id == "alternative");
    assert(!p1.hysteresis_satisfied);
    assert(!p1.approved);

    auto second = first;
    second.round = 11;
    auto p2 = transitions.propose(active.current(), {current, alternative}, second);
    assert(p2.hysteresis_satisfied);
    assert(p2.approved);
    assert(p2.transition.shared_unit_ids.empty());
    assert(p2.transition.replaceable_unit_ids.size() == 3);
    auto published = transitions.publish_if_approved(p2, active);
    assert(published.status == PublishStatus::Published);
    assert(active.current()->candidate.composition_id == "alternative");
    assert(active.current()->version == 2);
}
void classifies_shared_bridge_replaceable_and_item_risk() {
    ActiveCompositionManager active;
    auto current = comp("current", {1, 2, 3, 6});
    active.publish(current);
    auto target = comp("target", {2, 3, 4, 5});
    auto ctx = context(3);
    ctx.gold = 100;
    ctx.owned_units = {
        {2, 1, 1, {}}, {3, 2, 2, {}}, {4, 1, 1, {}},
        {1, 1, 2, {"item-sword"}},
        {6, 1, 1, {}, 0.1, 0.1, false, true}
    };
    ctx.candidate_evidence = {
        evidence("current", 0.4), evidence("target", 0.95, 0.9, 0.9, 0.9, 3.0)
    };
    CompositionEvaluationConfig config;
    config.required_consecutive_rounds = 1;
    TransitionManager transitions(config);
    auto proposal = transitions.propose(active.current(), {current, target}, ctx);
    assert(proposal.transition.shared_unit_ids.size() == 2);
    assert(proposal.transition.bridge_unit_ids.size() == 1);
    assert(proposal.transition.replaceable_unit_ids.size() == 2);
    assert(proposal.transition.sell_candidate_unit_ids.size() == 1);
    assert(proposal.transition.sell_candidate_unit_ids.front() == 6);
    assert(proposal.transition.item_risk_unit_ids.size() == 1);
}
void transition_hysteresis_is_isolated_by_match_and_player() {
    auto current = comp("current", {1, 2, 3});
    auto alternative = comp("alternative", {7, 8, 9});
    ActiveCompositionManager active;
    active.publish(current);
    CompositionEvaluationConfig config;
    config.required_consecutive_rounds = 2;
    TransitionManager transitions(config);

    auto first = context(10);
    first.gold = 100;
    first.candidate_evidence = {
        evidence("current", 0.35), evidence("alternative", 0.95, 0.9, 0.9, 0.9, 0.0)
    };
    auto proposal = transitions.propose(active.current(), {current, alternative}, first);
    assert(proposal.evidence_streak == 1);
    assert(!proposal.approved);

    auto other_player = first;
    other_player.player_id = 1;
    other_player.round = 11;
    proposal = transitions.propose(active.current(), {current, alternative}, other_player);
    assert(proposal.evidence_streak == 1);
    assert(!proposal.approved);

    // Interleave the original player: their own prior evidence must still exist.
    auto original_player = first;
    original_player.round = 12;
    proposal = transitions.propose(active.current(), {current, alternative}, original_player);
    assert(proposal.evidence_streak == 2);
    assert(proposal.approved);

    other_player.round = 13;
    proposal = transitions.propose(active.current(), {current, alternative}, other_player);
    assert(proposal.evidence_streak == 2);
    assert(proposal.approved);

    auto other_match = other_player;
    other_match.match_id = 7002;
    other_match.round = 14;
    proposal = transitions.propose(active.current(), {current, alternative}, other_match);
    assert(proposal.evidence_streak == 1);
    assert(!proposal.approved);
}

void removed_units_need_explicit_low_value_evidence_before_sell_candidate() {
    ActiveCompositionManager active;
    auto current = comp("current", {1, 2, 3, 8});
    active.publish(current);
    auto target = comp("target", {2, 3, 4});
    auto ctx = context(4);
    ctx.gold = 100;
    ctx.owned_units = {
        {1, 1, 2, {}},
        {8, 1, 1, {"item-risk"}, 0.0, 0.0, false, true}
    };
    ctx.candidate_evidence = {
        evidence("current", 0.35), evidence("target", 0.95, 0.9, 0.9, 0.9, 0.0)
    };
    CompositionEvaluationConfig config;
    config.required_consecutive_rounds = 1;
    TransitionManager transitions(config);
    const auto proposal = transitions.propose(active.current(), {current, target}, ctx);
    assert(proposal.transition.replaceable_unit_ids.size() == 2);
    assert(proposal.transition.sell_candidate_unit_ids.empty());
    assert(proposal.transition.item_risk_unit_ids.size() == 1);
}

void rejects_stale_or_unapproved_publication() {
    ActiveCompositionManager active;
    auto current = comp("current", {1, 2, 3});
    active.publish(current);
    auto target = comp("target", {2, 3, 4});
    TransitionManager transitions;
    auto ctx = context(1);
    ctx.gold = 100;
    ctx.candidate_evidence = {
        evidence("current", 0.3), evidence("target", 0.95, 0.9, 0.9, 0.9, 0.0)
    };
    auto proposal = transitions.propose(active.current(), {current, target}, ctx);
    auto denied = transitions.publish_if_approved(proposal, active);
    assert(denied.status == PublishStatus::RejectedInvalidCandidate);

    active.publish(comp("changed", {6, 7, 8}));
    proposal.approved = true;
    auto stale = transitions.publish_if_approved(proposal, active);
    assert(stale.status == PublishStatus::RejectedInvalidCandidate);
    assert(active.current()->candidate.composition_id == "changed");
}
void rejects_cross_set_candidates_and_invalid_evidence_is_bounded() {
    auto current = comp("current", {1, 2});
    auto wrong_set = comp("wrong-set", {7, 8});
    wrong_set.set_id = "17";
    CompositionEvaluationContext ctx = context();
    ctx.candidate_evidence = {evidence("current", 0.8), evidence("wrong-set", 1.0)};
    CompositionEvaluator evaluator;
    auto proposal = evaluator.evaluate(ActiveComposition{current, 1}, {wrong_set}, ctx);
    assert(proposal.decision == CompositionDecision::Keep);
    assert(!proposal.target);
    auto invalid = evidence("current", 4.0, -3.0, 9.0, 2.0);
    ctx.candidate_evidence = {invalid};
    const auto score = evaluator.score(current, ctx);
    assert(score.board_fit == 1.0);
    assert(score.item_fit == 0.0);
    assert(score.availability == 1.0);
    assert(score.economy_feasibility == 1.0);
}
void abandons_only_when_both_sides_lack_evidence() {
    auto current = comp("current", {1, 2});
    auto alternative = comp("alternative", {3, 4});
    auto ctx = context();
    ctx.candidate_evidence = {
        evidence("current", 0.05, 0.05, 0.05, 0.05),
        evidence("alternative", 0.05, 0.05, 0.05, 0.05)
    };
    CompositionEvaluator evaluator;
    auto proposal = evaluator.evaluate(ActiveComposition{current, 4}, {current, alternative}, ctx);
    assert(proposal.decision == CompositionDecision::Abandon);
    assert(!proposal.target);
}
}

int main() {
    selects_initial_complete_candidate();
    keeps_active_when_advantage_is_below_margin();
    pivot_requires_consecutive_rounds_and_complete_target();
    classifies_shared_bridge_replaceable_and_item_risk();
    transition_hysteresis_is_isolated_by_match_and_player();
    removed_units_need_explicit_low_value_evidence_before_sell_candidate();
    rejects_stale_or_unapproved_publication();
    rejects_cross_set_candidates_and_invalid_evidence_is_bounded();
    abandons_only_when_both_sides_lack_evidence();
    std::cout << "Composition Evaluator and Transition Manager tests passed\n";
    return 0;
}
