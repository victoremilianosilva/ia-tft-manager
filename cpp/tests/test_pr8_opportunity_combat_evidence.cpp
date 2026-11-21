#include "strategy/OpportunityCostProducer.hpp"
#include "combat/CombatEvidence.hpp"
#include "strategy/EconomicController.hpp"

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>

using namespace tft;

int main() {
    strategy::OpportunityCostProducer producer;
    strategy::OpportunityAlternativeEvidence reroll;
    reroll.candidate_id = "reroll";
    reroll.value_basis = "shared_utility.v1";
    reroll.marginal_strategic_value = 1.2;
    reroll.upgrade_value = 0.8;
    reroll.horizon_rounds = 2;
    reroll.uncertainty = 0.4;
    reroll.available = true;
    reroll.identity_valid = true;
    // Value components are already net of these costs; they are audit metadata.
    reroll.direct_economy_cost = 2.0;
    reroll.interest_cost = 1.0;
    auto opportunity = producer.evaluate("buy-xp", {reroll}, 2, "shared_utility.v1");
    assert(opportunity.available);
    assert(std::abs(opportunity.cost - 2.0) < 1e-9);
    assert(opportunity.sacrificed_candidate_id == "reroll");
    assert(opportunity.horizon_rounds == 2);
    assert(!producer.evaluate("buy-xp", {}, 2, "shared_utility.v1").available);
    assert(!producer.evaluate("buy-xp", {reroll}, 3, "shared_utility.v1").available);
    assert(!producer.evaluate("buy-xp", {reroll}, 2, "different_utility.v1").available);
    auto high_uncertainty = reroll;
    high_uncertainty.candidate_id = "high-uncertainty";
    high_uncertainty.marginal_strategic_value = 5.0;
    high_uncertainty.upgrade_value = 0.0;
    high_uncertainty.uncertainty = 0.95;
    auto lower_uncertainty = reroll;
    lower_uncertainty.candidate_id = "lower-uncertainty";
    lower_uncertainty.marginal_strategic_value = 0.6;
    lower_uncertainty.upgrade_value = 0.0;
    lower_uncertainty.uncertainty = 0.0;
    const auto risk_adjusted = producer.evaluate(
        "buy-xp", {high_uncertainty, lower_uncertainty}, 2, "shared_utility.v1");
    assert(risk_adjusted.available);
    assert(risk_adjusted.sacrificed_candidate_id == "lower-uncertainty");
    assert(std::abs(risk_adjusted.cost - 0.6) < 1e-9);

    auto no_confidence = reroll;
    no_confidence.candidate_id = "no-confidence";
    no_confidence.uncertainty = 1.0;
    assert(!producer.evaluate("buy-xp", {no_confidence}, 2, "shared_utility.v1").available);

    reroll.identity_valid = false;
    assert(!producer.evaluate("buy-xp", {reroll}, 2, "shared_utility.v1").available);

    combat_evidence::CombatSnapshot snapshot;
    snapshot.match_id = 7; snapshot.player_id = 0; snapshot.opponent_id = 1;
    snapshot.round = 8; snapshot.sequence = 10; snapshot.engine_decision_sequence = 100;
    snapshot.player_hp = 34.5;
    snapshot.opponent_hp = 51; snapshot.player_roster_complete = true;
    snapshot.opponent_roster_complete = true;
    snapshot.player_unit_ids = {"p1", "p2"};
    snapshot.opponent_unit_ids = {"o1"};
    assert(combat_evidence::CombatSnapshotBuilder{}.validate(snapshot).valid);
    assert(!combat_evidence::CombatSnapshotBuilder{}.validate(snapshot, 11).valid);
    auto overlapping_roster = snapshot;
    overlapping_roster.opponent_unit_ids = {"p1"};
    assert(!combat_evidence::CombatSnapshotBuilder{}.validate(overlapping_roster).valid);
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
            static_cast<double>(i), true, "versioned_replay_outcome.v1",
            "replay-artifact-7", "tft-replay-dataset.v1"});
    const auto calibrator = combat_evidence::CombatPredictionCalibrator{};
    combat_evidence::CombatCalibrationCohort cohort;
    cohort.round = 50;
    cohort.horizon_rounds = 1;
    cohort.engine_version = "combat-engine-generic.v1";
    cohort.composition_signature = "composition-sha256";
    cohort.mechanics_signature = "mechanics-sha256";
    std::vector<combat_evidence::ObservedCombatOutcome> cohort_outcomes;
    for (std::uint64_t i = 0; i < 30; ++i) {
        combat_evidence::ObservedCombatOutcome sample;
        sample.match_id = 100 + i;
        sample.player_id = static_cast<std::int32_t>(i % 8);
        sample.round = 50;
        sample.sequence = 5;
        sample.incoming_damage = static_cast<double>(i + 1);
        sample.observed = true;
        sample.source = "versioned_replay_outcome.v1";
        sample.replay_artifact_id = "combat-replay-" + std::to_string(i % 3);
        sample.dataset_version = "combat-dataset.v2";
        sample.engine_version = cohort.engine_version;
        sample.composition_signature = cohort.composition_signature;
        sample.mechanics_signature = cohort.mechanics_signature;
        sample.horizon_rounds = 1;
        cohort_outcomes.push_back(sample);
    }
    auto target_match_leak = cohort_outcomes.front();
    target_match_leak.match_id = 7;
    target_match_leak.incoming_damage = 999.0;
    cohort_outcomes.push_back(target_match_leak);
    const auto cohort_distribution = calibrator.calibrate_for_cohort(
        cohort_outcomes, 7, 0, 50, 50, cohort, 30);
    assert(cohort_distribution.sample_count == 30);
    assert(cohort_distribution.source == "experimental_replay_cohort_distribution.v1");
    assert(cohort_distribution.replay_artifact_ids.size() == 3);
    assert(!cohort_distribution.calibrated);
    auto duplicate_cohort = cohort_outcomes;
    duplicate_cohort.push_back(duplicate_cohort.front());
    const auto invalid_cohort = calibrator.calibrate_for_cohort(
        duplicate_cohort, 7, 0, 50, 50, cohort, 30);
    assert(invalid_cohort.source == "invalid_duplicate_match_cohort_sample");
    auto mixed_dataset = cohort_outcomes;
    mixed_dataset[1].dataset_version = "combat-dataset.v3";
    const auto invalid_dataset = calibrator.calibrate_for_cohort(
        mixed_dataset, 7, 0, 50, 50, cohort, 30);
    assert(invalid_dataset.source == "invalid_mixed_dataset_versions");

    outcomes.push_back({7, 0, 2, 41, 999.0, true, "combat_engine_simulation",
        "synthetic-run", "tft-replay-dataset.v1"}); // simulation is not an observed replay
    outcomes.push_back({7, 0, 1, 50, 999.0, true, "versioned_replay_outcome.v1",
        "replay-artifact-7", "tft-replay-dataset.v1"}); // sequence at/after decision is stale
    auto distribution = calibrator.calibrate(outcomes, 7, 0, 50, 50, 30);
    assert(!distribution.calibrated && distribution.sample_count == 40);
    assert(distribution.source == "experimental_replay_distribution.v1");
    assert(distribution.p50 == 20.0 && distribution.p90 == 36.0);

    combat_evidence::CalibrationAcceptanceCriteria criteria;
    criteria.approved = true;
    criteria.protocol_id = "combat-calibration.v1";
    criteria.minimum_training_samples = 30;
    criteria.minimum_test_samples = 30;
    criteria.maximum_mae = 5.0;
    criteria.minimum_p90_coverage = 0.85;
    criteria.maximum_p90_coverage = 0.95;
    criteria.maximum_brier_score = 0.10;
    combat_evidence::CalibrationValidationMetrics metrics;
    metrics.report_sha256 = std::string(64, 'a');
    metrics.train_manifest_sha256 = std::string(64, 'b');
    metrics.validation_manifest_sha256 = std::string(64, 'c');
    metrics.test_manifest_sha256 = std::string(64, 'd');
    metrics.episode_splits_disjoint = true;
    metrics.test_sample_count = 40;
    metrics.mae = 1.2;
    metrics.p90_coverage = 0.90;
    metrics.brier_score = 0.05;
    assert(combat_evidence::approve_calibration(distribution, metrics, criteria));
    assert(distribution.calibrated);
    auto unapproved_distribution = calibrator.calibrate(outcomes, 7, 0, 50, 50, 30);
    assert(!combat_evidence::derive_survival_risk(34.5, unapproved_distribution).available);
    auto unapproved_criteria = criteria;
    unapproved_criteria.approved = false;
    assert(!combat_evidence::approve_calibration(
        unapproved_distribution, metrics, unapproved_criteria));
    auto overlapping_splits = metrics;
    overlapping_splits.test_manifest_sha256 = overlapping_splits.train_manifest_sha256;
    assert(!combat_evidence::approve_calibration(
        unapproved_distribution, overlapping_splits, criteria));
    auto risk = combat_evidence::derive_survival_risk(34.5, distribution);
    assert(risk.available && std::abs(risk.elimination_risk - 0.15) < 1e-9);
    const auto integer_hp_risk = combat_evidence::derive_survival_risk(34.0, distribution);
    assert(integer_hp_risk.available &&
        std::abs(integer_hp_risk.elimination_risk - 0.175) < 1e-9);
    strategy::StrategicSharedContext context;
    context.match_id = 7;
    context.player_id = 0;
    context.round = 50;
    context.sequence = 50;
    assert(combat_evidence::apply_to_economic_context(risk, context));
    assert(context.combat_calibration_protocol_id == "combat-calibration.v1");
    assert(context.combat_calibration_report_sha256 == std::string(64, 'a'));
    assert(context.combat_dataset_version == "tft-replay-dataset.v1");
    assert(context.combat_replay_artifact_ids.size() == 1);
    std::vector<combat_evidence::CombatHorizonTrajectory> trajectories;
    for (std::uint64_t i = 0; i < 40; ++i) {
        combat_evidence::CombatHorizonTrajectory trajectory;
        trajectory.scenario_id = "scenario-" + std::to_string(i);
        trajectory.match_id = 7;
        trajectory.player_id = 0;
        trajectory.scenario_weight = 1.0;
        trajectory.uncertainty = 0.10;
        trajectory.calibrated = true;
        trajectory.calibration_protocol_id = "combat-horizon.v1";
        trajectory.calibration_report_sha256 = std::string(64, 'e');
        trajectory.calibration_train_manifest_sha256 = std::string(64, 'b');
        trajectory.calibration_validation_manifest_sha256 = std::string(64, 'c');
        trajectory.calibration_test_manifest_sha256 = std::string(64, 'd');
        trajectory.episode_splits_disjoint = true;
        trajectory.calibration_mae = 1.0;
        trajectory.calibration_p90_coverage = 0.90;
        trajectory.calibration_brier_score = 0.05;
        trajectory.replay_artifact_id = "trajectory-replay-" + std::to_string(i % 4);
        trajectory.dataset_version = "combat-trajectories.v1";
        trajectory.source = "approved_replay_trajectory.v1";
        trajectory.steps.push_back({50, 50, 1, 5.0, 0.0});
        trajectory.steps.push_back({51, 51, 2, i < 20 ? 16.0 : 5.0, 0.0});
        trajectories.push_back(std::move(trajectory));
    }
    const auto multi_round_risk = combat_evidence::derive_multi_round_survival_risk(
        20.0, 7, 0, 50, 50, 2, trajectories, 30);
    assert(multi_round_risk.available);
    assert(multi_round_risk.horizon_rounds == 2);
    assert(std::abs(multi_round_risk.expected_damage - 15.5) < 1e-9);
    assert(std::abs(multi_round_risk.elimination_risk - 0.5) < 1e-9);
    assert(multi_round_risk.uncertainty > 0.0 &&
        multi_round_risk.uncertainty <= 1.0);
    auto incomplete_trajectories = trajectories;
    incomplete_trajectories.front().steps.pop_back();
    assert(!combat_evidence::derive_multi_round_survival_risk(
        20.0, 7, 0, 50, 50, 2, incomplete_trajectories, 30).available);
    auto duplicate_trajectories = trajectories;
    duplicate_trajectories.back().scenario_id =
        duplicate_trajectories.front().scenario_id;
    assert(!combat_evidence::derive_multi_round_survival_risk(
        20.0, 7, 0, 50, 50, 2, duplicate_trajectories, 30).available);
    auto invalid_weight_trajectories = trajectories;
    invalid_weight_trajectories.front().scenario_weight = 0.0;
    assert(!combat_evidence::derive_multi_round_survival_risk(
        20.0, 7, 0, 50, 50, 2, invalid_weight_trajectories, 30).available);

    strategy::StrategicSharedContext multi_context;
    multi_context.match_id = 7;
    multi_context.player_id = 0;
    multi_context.round = 50;
    multi_context.sequence = 50;
    assert(combat_evidence::apply_to_economic_context(multi_round_risk, multi_context));
    assert(multi_context.combat_evidence_horizon_rounds == 2);
    assert(multi_context.combat_calibration_protocol_id == "combat-horizon.v1");
    assert(multi_context.combat_calibration_report_sha256 == std::string(64, 'e'));
    assert(multi_context.combat_dataset_version == "combat-trajectories.v1");
    assert(multi_context.combat_replay_artifact_ids.size() == 4);
    multi_context.alive = true;
    multi_context.hp = 20.0;
    multi_context.gold = 35;
    multi_context.level = 7;
    multi_context.xp_to_next = 10;
    multi_context.win_streak = 1;
    multi_context.evidence.hp = true;
    multi_context.evidence.gold = true;
    multi_context.evidence.level = true;
    multi_context.evidence.xp_to_next = true;
    multi_context.evidence.streaks = true;
    const auto multi_economic = strategy::EconomicController{}.evaluate(multi_context);
    assert(multi_economic.evidence_invalid.empty());
    assert(multi_economic.sufficient_evidence);

    auto stale_context = context;
    stale_context.sequence = 49;
    assert(!combat_evidence::apply_to_economic_context(risk, stale_context));
    assert(context.evidence.estimated_incoming_damage);
    assert(context.evidence.elimination_risk);
    context.alive = true;
    context.hp = 34.5;
    context.gold = 35;
    context.level = 7;
    context.xp_to_next = 10;
    context.win_streak = 1;
    context.evidence.hp = true;
    context.evidence.gold = true;
    context.evidence.level = true;
    context.evidence.xp_to_next = true;
    context.evidence.streaks = true;
    const auto economic = strategy::EconomicController{}.evaluate(context);
    assert(economic.evidence_invalid.empty());
    assert(economic.sufficient_evidence);
    assert(std::find(economic.evidence_used.begin(), economic.evidence_used.end(),
        "estimated_incoming_damage") != economic.evidence_used.end());
    assert(std::find(economic.evidence_used.begin(), economic.evidence_used.end(),
        "elimination_risk") != economic.evidence_used.end());
    assert(economic.survival_pressure > 0.0);
    auto stale_combat_context = context;
    stale_combat_context.combat_evidence_sequence = 49;
    const auto stale_economic =
        strategy::EconomicController{}.evaluate(stale_combat_context);
    assert(std::find(stale_economic.evidence_invalid.begin(),
        stale_economic.evidence_invalid.end(),
        "combat_evidence_provenance_horizon_or_sequence") !=
        stale_economic.evidence_invalid.end());
    assert(!combat_evidence::derive_survival_risk(34, {}).available);
    outcomes.push_back(outcomes.front());
    const auto duplicate = calibrator.calibrate(outcomes, 7, 0, 50, 50, 30);
    assert(!duplicate.calibrated);
    assert(duplicate.source == "invalid_duplicate_outcome_sequence");
    std::cout << "PR8 opportunity and combat evidence tests passed\n";
}
