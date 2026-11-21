#include "strategy/OpportunityCostProducer.hpp"
#include "combat/CombatEvidence.hpp"

#include <cassert>
#include <cmath>
#include <iostream>

using namespace tft;

int main() {
    strategy::OpportunityCostProducer producer;
    strategy::OpportunityAlternativeEvidence reroll;
    reroll.candidate_id = "reroll";
    reroll.marginal_strategic_value = 1.2;
    reroll.upgrade_value = 0.8;
    reroll.horizon_rounds = 2;
    reroll.uncertainty = 0.4;
    reroll.available = true;
    reroll.identity_valid = true;
    reroll.direct_economy_cost = 2.0;
    reroll.interest_cost = 1.0;
    auto opportunity = producer.evaluate("buy-xp", {reroll});
    assert(opportunity.available);
    assert(std::abs(opportunity.cost - 2.0) < 1e-9);
    assert(opportunity.sacrificed_candidate_id == "reroll");
    assert(opportunity.horizon_rounds == 2);
    assert(!producer.evaluate("buy-xp", {}).available);
    reroll.identity_valid = false;
    assert(!producer.evaluate("buy-xp", {reroll}).available);

    combat_evidence::CombatSnapshot snapshot;
    snapshot.match_id = 7; snapshot.player_id = 0; snapshot.opponent_id = 1;
    snapshot.round = 8; snapshot.sequence = 10; snapshot.player_hp = 34;
    snapshot.opponent_hp = 51; snapshot.player_roster_complete = true;
    snapshot.opponent_roster_complete = true;
    snapshot.player_unit_ids = {"p1", "p2"};
    snapshot.opponent_unit_ids = {"o1"};
    assert(combat_evidence::CombatSnapshotBuilder{}.validate(snapshot).valid);
    assert(!combat_evidence::CombatSnapshotBuilder{}.validate(snapshot, 11).valid);
    std::int32_t opponent = -1;
    assert(combat_evidence::MatchupResolver{}.resolve(snapshot, 1, opponent));
    assert(opponent == 1);
    assert(!combat_evidence::MatchupResolver{}.resolve(snapshot, 2, opponent));

    combat_evidence::CombatCoverage partial;
    partial.units_seen = 2; partial.units_supported = 1;
    partial.unsupported_abilities = 1;
    assert(!combat_evidence::CombatCoverageValidator{}.validate(partial).complete);

    std::vector<combat_evidence::ObservedCombatOutcome> outcomes;
    for (std::uint64_t i = 1; i <= 40; ++i)
        outcomes.push_back({7, 0, static_cast<std::uint32_t>(i), i,
            static_cast<double>(i), true});
    const auto calibrator = combat_evidence::CombatPredictionCalibrator{};
    auto distribution = calibrator.calibrate(outcomes, 7, 0, 50, 30);
    assert(distribution.calibrated && distribution.sample_count == 40);
    assert(distribution.p50 == 20.0 && distribution.p90 == 36.0);
    auto risk = combat_evidence::derive_survival_risk(34, distribution);
    assert(risk.available && std::abs(risk.elimination_risk - 0.175) < 1e-9);
    strategy::StrategicSharedContext context;
    assert(combat_evidence::apply_to_economic_context(risk, context));
    assert(context.evidence.estimated_incoming_damage);
    assert(context.evidence.elimination_risk);
    assert(!combat_evidence::derive_survival_risk(34, {}).available);
    outcomes.push_back(outcomes.front());
    const auto duplicate = calibrator.calibrate(outcomes, 7, 0, 50, 30);
    assert(!duplicate.calibrated);
    assert(duplicate.source == "invalid_duplicate_outcome_sequence");
    std::cout << "PR8 opportunity and combat evidence tests passed\n";
}
