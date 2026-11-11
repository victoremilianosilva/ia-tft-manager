#include "strategy/InitialStrategicDirectionDiscovery.hpp"

#include <cassert>
#include <iostream>

using namespace tft::strategy;

static DirectionDiscoveryUnit unit(
    int id, std::vector<std::string> traits, int copies = 1,
    bool board = false, bool bench = false, bool shop = false,
    bool carry = false, bool core = false, double contribution = 0.0,
    int cost = 1) {
    DirectionDiscoveryUnit u;
    u.champion_id = id;
    u.cost = cost;
    u.copies_owned = copies;
    u.on_board = board;
    u.on_bench = bench;
    u.in_shop = shop;
    u.carry_potential = carry;
    u.core_potential = core;
    u.board_contribution = contribution;
    u.traits = std::move(traits);
    return u;
}

int main() {
    InitialStrategicDirectionDiscovery discovery;

    // Cheap early pairs are valid direction evidence; no 4/5-cost gate.
    DirectionDiscoveryInput early;
    early.round = 3;
    early.units = {
        unit(1, {"Bruiser"}, 2, false, true, false, false, true, 0.0, 1),
        unit(2, {"Bruiser"}, 1, true, false, false, false, false, 3.0, 2)
    };
    early.trait_thresholds = {{"Bruiser", 2}};
    auto result = discovery.evaluate(early);
    assert(result.status == DirectionDiscoveryStatus::HypothesesFound);
    assert(!result.hypotheses.empty());
    assert(result.hypotheses.front().anchor.direction == "Bruiser");
    assert(result.hypotheses.front().anchor.confidence > 0.0);

    // A potential carry need not already be two-star, but needs owned support.
    DirectionDiscoveryInput carry;
    carry.units = {
        unit(10, {"Invoker"}, 1, true, false, false, true, true, 2.0, 4),
        unit(11, {"Invoker"}, 1, false, true, false, false, false, 0.0, 2)
    };
    carry.trait_thresholds = {{"Invoker", 2}};
    result = discovery.evaluate(carry);
    assert(result.status == DirectionDiscoveryStatus::HypothesesFound);
    assert(result.hypotheses.front().anchor.direction == "Invoker");

    // Evidence spread across board, bench and shop can complete a trait.
    DirectionDiscoveryInput spread;
    spread.units = {
        unit(20, {"Arcanist"}, 1, true),
        unit(21, {"Arcanist"}, 1, false, true),
        unit(22, {"Arcanist"}, 0, false, false, true)
    };
    spread.trait_thresholds = {{"Arcanist", 3}};
    result = discovery.evaluate(spread);
    assert(result.status == DirectionDiscoveryStatus::HypothesesFound);
    assert(result.hypotheses.front().synergy_reachable);
    assert(result.hypotheses.front().synergy_owned_count == 2);
    assert(result.hypotheses.front().synergy_reachable_count == 3);
    assert(std::find(result.hypotheses.front().anchor.evidence.begin(),
        result.hypotheses.front().anchor.evidence.end(),
        StrategicAnchorEvidenceKind::ShopOffer) !=
        result.hypotheses.front().anchor.evidence.end());

    // One isolated unit is not enough, even if it is a 5-cost carry.
    DirectionDiscoveryInput isolated;
    isolated.units = {unit(30, {"Legend"}, 1, true, false, false, true, true, 5.0, 5)};
    result = discovery.evaluate(isolated);
    assert(result.status == DirectionDiscoveryStatus::InsufficientEvidence);
    assert(result.hypotheses.empty());

    // Empty shop / missing trait metadata does not create favorable evidence.
    DirectionDiscoveryInput no_shop;
    no_shop.units = {
        unit(40, {"Sentinel"}, 1, true),
        unit(41, {"Sentinel"}, 1, false, true)
    };
    result = discovery.evaluate(no_shop);
    assert(result.status == DirectionDiscoveryStatus::HypothesesFound);
    assert(result.hypotheses.front().shop_copies == 0);
    assert(!result.hypotheses.front().synergy_reachable ||
           result.hypotheses.front().synergy_owned_count >= 2);

    // Competing hypotheses are ranked; a small lead does not dislodge the
    // previous viable direction.
    DirectionDiscoveryInput competing;
    competing.previous_direction = "Bruiser";
    competing.maximum_hypotheses = 3;
    competing.units = {
        unit(50, {"Bruiser"}, 2, true, false, false, false, true, 2.0),
        unit(51, {"Bruiser"}, 1, false, true),
        unit(52, {"Invoker"}, 2, true, false, false, false, true, 5.0),
        unit(53, {"Invoker"}, 1, false, true)
    };
    result = discovery.evaluate(competing);
    assert(result.hypotheses.size() == 2);
    assert(result.hypotheses.front().anchor.direction == "Bruiser");

    // Cost is part of the opportunity-cost estimate, but expensive units
    // are not categorically excluded from early direction discovery.
    DirectionDiscoveryInput cost_aware;
    cost_aware.gold_available = 2;
    cost_aware.units = {
        unit(70, {"LowCost"}, 1, true, false, false, false, true, 1.0, 1),
        unit(71, {"LowCost"}, 1, false, true, false, false, false, 0.0, 1),
        unit(72, {"HighCost"}, 1, true, false, false, true, true, 1.0, 5),
        unit(73, {"HighCost"}, 1, false, true, false, false, false, 0.0, 5)
    };
    result = discovery.evaluate(cost_aware);
    assert(result.hypotheses.size() == 2);
    const auto low_cost = std::find_if(result.hypotheses.begin(),
        result.hypotheses.end(), [](const auto& h) {
            return h.anchor.direction == "LowCost";
        });
    const auto high_cost = std::find_if(result.hypotheses.begin(),
        result.hypotheses.end(), [](const auto& h) {
            return h.anchor.direction == "HighCost";
        });
    assert(low_cost != result.hypotheses.end());
    assert(high_cost != result.hypotheses.end());
    assert(low_cost->score > high_cost->score);
    assert(low_cost->score_explanation.find("cost_penalty=") != std::string::npos);

    // A defined composition suppresses free exploration entirely.
    competing.composition_defined = true;
    competing.active_composition_identity = "composition:active";
    result = discovery.evaluate(competing);
    assert(result.status == DirectionDiscoveryStatus::CompositionBound);
    assert(result.hypotheses.empty());

    // Duplicate champion rows are rejected: callers must aggregate copies.
    DirectionDiscoveryInput invalid;
    invalid.units = {unit(60, {"Duelist"}), unit(60, {"Duelist"})};
    result = discovery.evaluate(invalid);
    assert(result.status == DirectionDiscoveryStatus::InvalidInput);

    std::cout << "initial strategic direction discovery tests passed\n";
    return 0;
}
