#include "combat/CombatProjectionEngine.hpp"

#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>

using namespace tft;
using namespace tft::combat_evidence;

namespace {
CombatUnit make_unit(int id, UnitTeam team, int x, int source_slot) {
    CombatUnit unit;
    unit.id = id;
    unit.source_unit_uuid = team == UnitTeam::PLAYER_A
        ? "player-unit-uuid" : "opponent-unit-uuid";
    unit.api_name = "TFT_TestUnit";
    unit.name = "Test Unit";
    unit.team = team;
    unit.position = {x, 1};
    unit.source_board_position = source_slot;
    unit.hp = 100.0f;
    unit.max_hp = 100.0f;
    unit.attack_damage = 30.0f;
    unit.attack_speed = 1.0f;
    unit.attack_range = 1.0f;
    unit.ability.api_name = "generic_basic_attack_only";
    unit.ability.metadata_complete = true;
    auto& provenance = unit.provenance;
    provenance.identity = "observed:test_fixture";
    provenance.star = "observed:test_fixture";
    provenance.position = "observed:test_fixture";
    provenance.hp = "derived:test_fixture";
    provenance.max_hp = "catalog:test_fixture";
    provenance.attack_damage = "catalog:test_fixture";
    provenance.attack_speed = "catalog:test_fixture";
    provenance.attack_range = "catalog:test_fixture";
    provenance.armor = "catalog:test_fixture";
    provenance.magic_resist = "catalog:test_fixture";
    provenance.mana = "observed:test_fixture";
    provenance.max_mana = "catalog:test_fixture";
    provenance.ability_power = "catalog:test_fixture";
    provenance.critical_strike_chance = "catalog:test_fixture";
    provenance.critical_strike_damage = "catalog:test_fixture";
    provenance.damage_amplification = "catalog:test_fixture";
    provenance.damage_reduction = "catalog:test_fixture";
    provenance.omnivamp = "catalog:test_fixture";
    provenance.role = "catalog:test_fixture";
    provenance.ability = "catalog:test_fixture_complete";
    provenance.items = "observed:test_fixture";
    provenance.traits = "derived:test_fixture";
    return unit;
}

CombatInput make_input() {
    CombatInput input;
    input.context = CombatContext::PVP;
    input.seed = 7;
    input.config.seed = 7;
    input.config.max_duration = 30.0f;
    input.config.deterministic = true;
    input.player_a.team = UnitTeam::PLAYER_A;
    input.player_a.player_id = 0;
    input.player_a.player_hp = 40.0f;
    input.player_a.units.push_back(make_unit(0, UnitTeam::PLAYER_A, 0, 0));
    input.player_b.team = UnitTeam::PLAYER_B;
    input.player_b.player_id = 1;
    input.player_b.player_hp = 70.0f;
    input.player_b.units.push_back(make_unit(1, UnitTeam::PLAYER_B, 6, 0));
    return input;
}

CombatSnapshot make_identity() {
    CombatSnapshot identity;
    identity.match_id = 17;
    identity.player_id = 0;
    identity.opponent_id = 1;
    identity.round = 12;
    identity.sequence = 31;
    identity.engine_decision_sequence = 88;
    identity.player_hp = 40.0;
    identity.opponent_hp = 70.0;
    identity.player_unit_ids = {"player-unit-uuid"};
    identity.opponent_unit_ids = {"opponent-unit-uuid"};
    identity.player_roster_complete = true;
    identity.opponent_roster_complete = true;
    return identity;
}
}

int main() {
    const auto input = make_input();
    const auto identity = make_identity();
    const auto builder = CombatProjectionSnapshotBuilder{};
    auto snapshot = builder.build(identity, input, 31);
    assert(snapshot.valid);
    assert(snapshot.validation_reason == "valid");

    const auto coverage = CombatCoverageValidator{}.validate(snapshot.coverage);
    assert(coverage.complete);
    assert(coverage.status == "complete");
    assert(snapshot.coverage.abilities_seen == 2);
    assert(snapshot.coverage.abilities_supported == 2);
    assert(snapshot.coverage.items_seen == 0);
    assert(snapshot.coverage.traits_seen == 0);

    auto supported_effect_input = input;
    CombatItem supported_item;
    supported_item.api_name = "TFT_TestItem";
    supported_item.effects_complete = true;
    CombatEffectDefinition supported_effect;
    supported_effect.trigger = "combat_start";
    supported_effect.operation = "add_stat";
    supported_effect.stat = "attack_damage";
    supported_effect.target = "self";
    supported_effect.value = 10.0f;
    supported_item.effects.push_back(supported_effect);
    supported_effect_input.player_a.units.front().items.push_back(supported_item);
    const auto supported_effect_snapshot =
        builder.build(identity, supported_effect_input, 31);
    const auto supported_effect_coverage =
        CombatCoverageValidator{}.validate(supported_effect_snapshot.coverage);
    assert(supported_effect_snapshot.valid && supported_effect_coverage.complete);
    assert(supported_effect_snapshot.coverage.effects_seen == 1);
    assert(supported_effect_snapshot.coverage.effects_supported == 1);

    auto fallback_stat_input = input;
    fallback_stat_input.player_a.units.front().provenance.attack_damage =
        "engine_fallback";
    const auto fallback_stat_snapshot =
        builder.build(identity, fallback_stat_input, 31);
    assert(!CombatCoverageValidator{}.validate(fallback_stat_snapshot.coverage).complete);
    assert(fallback_stat_snapshot.coverage.missing_unit_provenance == 1);

    auto unsupported_effect_input = supported_effect_input;
    unsupported_effect_input.player_a.units.front().items.front().effects.front().trigger.clear();
    const auto unsupported_effect_snapshot =
        builder.build(identity, unsupported_effect_input, 31);
    const auto unsupported_effect_coverage =
        CombatCoverageValidator{}.validate(unsupported_effect_snapshot.coverage);
    assert(unsupported_effect_snapshot.valid && !unsupported_effect_coverage.complete);
    assert(unsupported_effect_snapshot.coverage.unsupported_effects == 1);
    assert(unsupported_effect_snapshot.coverage.unsupported_items == 1);

    auto orphaned_charge_consumer_input = supported_effect_input;
    CombatEffectDefinition orphaned_heal;
    orphaned_heal.trigger = "on_attack";
    orphaned_heal.operation = "heal_max_hp_pct";
    orphaned_heal.target = "self";
    orphaned_heal.stack_key = "attack-heal";
    orphaned_heal.value = 0.10f;
    orphaned_charge_consumer_input.player_a.units.front().items.front()
        .effects.push_back(orphaned_heal);
    const auto orphaned_charge_consumer_snapshot =
        builder.build(identity, orphaned_charge_consumer_input, 31);
    assert(!CombatCoverageValidator{}.validate(
        orphaned_charge_consumer_snapshot.coverage).complete);
    assert(orphaned_charge_consumer_snapshot.coverage.unsupported_effects == 1);

    auto valid_charge_pair_input = supported_effect_input;
    CombatEffectDefinition charge_source;
    charge_source.trigger = "on_kill";
    charge_source.operation = "grant_charges";
    charge_source.stack_key = "attack-heal";
    charge_source.value = 1.0f;
    charge_source.max_stacks = 1;
    CombatEffectDefinition charge_consumer = orphaned_heal;
    valid_charge_pair_input.player_a.units.front().items.front().effects.push_back(
        charge_source);
    valid_charge_pair_input.player_a.units.front().items.front().effects.push_back(
        charge_consumer);
    const auto valid_charge_pair_snapshot =
        builder.build(identity, valid_charge_pair_input, 31);
    assert(CombatCoverageValidator{}.validate(valid_charge_pair_snapshot.coverage).complete);
    assert(valid_charge_pair_snapshot.coverage.effects_seen == 3);
    assert(valid_charge_pair_snapshot.coverage.effects_supported == 3);

    auto unimplemented_trigger_input = supported_effect_input;
    unimplemented_trigger_input.player_a.units.front().items.front().effects.front().trigger =
        "on_ally_shield";
    const auto unimplemented_trigger_snapshot =
        builder.build(identity, unimplemented_trigger_input, 31);
    assert(!CombatCoverageValidator{}.validate(
        unimplemented_trigger_snapshot.coverage).complete);
    assert(unimplemented_trigger_snapshot.coverage.unsupported_effects == 1);

    const auto projection = CombatProjectionEngine{}.project(snapshot, 6, 4, 100);
    assert(projection.simulation_completed);
    assert(!projection.decision_eligible);
    assert(projection.status == "experimental_uncalibrated");
    assert(projection.reason == "awaiting_replay_calibration");
    assert(projection.scenarios_requested == 4);
    assert(projection.scenarios_completed == 4);
    assert(projection.incoming_damage_samples.size() == 4);
    assert(std::isfinite(projection.expected_incoming_damage));
    assert(std::isfinite(projection.p50_incoming_damage));
    assert(std::isfinite(projection.p90_incoming_damage));
    for (const auto damage : projection.incoming_damage_samples)
        assert(damage >= 6.0);
    assert(projection.elimination_probability_available);
    assert(projection.observed_player_hp == identity.player_hp);
    assert(projection.experimental_elimination_probability >= 0.0 &&
        projection.experimental_elimination_probability <= 1.0);

    CombatCalibrationCohort evaluation_cohort;
    evaluation_cohort.round = identity.round;
    evaluation_cohort.horizon_rounds = 1;
    evaluation_cohort.engine_version = projection.simulator_version;
    evaluation_cohort.composition_signature = "fixture-composition";
    evaluation_cohort.mechanics_signature = "fixture-mechanics";
    std::vector<CalibrationPredictionEvaluationSample> evaluation_samples;
    const auto append_evaluation_split = [&](CalibrationDatasetSplit split,
                                             std::uint64_t first_match,
                                             std::uint32_t count) {
        for (std::uint32_t index = 0; index < count; ++index) {
            CalibrationPredictionEvaluationSample sample;
            sample.match_id = first_match + index;
            sample.player_id = projection.player_id;
            sample.opponent_id = projection.opponent_id;
            sample.round = identity.round;
            sample.sequence = identity.sequence;
            sample.engine_decision_sequence = projection.engine_decision_sequence;
            sample.horizon_rounds = 1;
            sample.projection_simulation_completed = projection.simulation_completed;
            sample.projection_coverage_complete =
                CombatCoverageValidator{}.validate(projection.coverage).complete;
            sample.projection_decision_eligible = projection.decision_eligible;
            sample.predicted_player_hp = projection.observed_player_hp;
            sample.predicted_expected_damage = projection.expected_incoming_damage;
            sample.predicted_p90_damage = std::max(5.0, projection.p90_incoming_damage);
            sample.predicted_elimination_probability =
                projection.experimental_elimination_probability;
            sample.observed_hp_before = identity.player_hp;
            sample.observed_hp_after = identity.player_hp - 5.0;
            sample.observed_damage = 5.0;
            sample.split = split;
            sample.replay_artifact_id = "fixture-replay-" + std::to_string(sample.match_id);
            sample.dataset_version = "fixture-evaluation-dataset.v1";
            sample.engine_version = evaluation_cohort.engine_version;
            sample.composition_signature = evaluation_cohort.composition_signature;
            sample.mechanics_signature = evaluation_cohort.mechanics_signature;
            evaluation_samples.push_back(std::move(sample));
        }
    };
    append_evaluation_split(CalibrationDatasetSplit::TRAIN, 1000, 5);
    append_evaluation_split(CalibrationDatasetSplit::VALIDATION, 2000, 3);
    append_evaluation_split(CalibrationDatasetSplit::TEST, 3000, 5);
    CalibrationEvaluationManifest evaluation_manifest;
    evaluation_manifest.report_sha256 = std::string(64, 'a');
    evaluation_manifest.train_manifest_sha256 = std::string(64, 'b');
    evaluation_manifest.validation_manifest_sha256 = std::string(64, 'c');
    evaluation_manifest.test_manifest_sha256 = std::string(64, 'd');
    const auto evaluation = evaluate_calibration_predictions(
        evaluation_samples, evaluation_cohort, evaluation_manifest);
    assert(evaluation.valid);
    assert(evaluation.metrics.episode_splits_disjoint);
    assert(evaluation.metrics.training_sample_count == 5);
    assert(evaluation.metrics.validation_sample_count == 3);
    assert(evaluation.metrics.test_sample_count == 5);
    assert(std::abs(evaluation.metrics.mae -
        std::abs(projection.expected_incoming_damage - 5.0)) <= 1e-9);
    assert(evaluation.metrics.p90_coverage == 1.0);

    auto incomplete_projection_samples = evaluation_samples;
    incomplete_projection_samples.front().projection_coverage_complete = false;
    const auto incomplete_projection_evaluation = evaluate_calibration_predictions(
        incomplete_projection_samples, evaluation_cohort, evaluation_manifest);
    assert(!incomplete_projection_evaluation.valid);
    assert(incomplete_projection_evaluation.reason ==
        "invalid_paired_prediction_outcome_sample");

    DamageDistribution evaluated_distribution;
    evaluated_distribution.match_id = identity.match_id;
    evaluated_distribution.player_id = identity.player_id;
    evaluated_distribution.before_round = identity.round;
    evaluated_distribution.before_sequence = identity.sequence;
    evaluated_distribution.sample_count = 5;
    evaluated_distribution.minimum_sample_count = 5;
    evaluated_distribution.mean = 5.0;
    evaluated_distribution.p50 = 5.0;
    evaluated_distribution.p90 = 5.0;
    evaluated_distribution.uncertainty = 1.0 / std::sqrt(5.0);
    evaluated_distribution.observed_damage_samples = {5.0, 5.0, 5.0, 5.0, 5.0};
    evaluated_distribution.dataset_version = "fixture-evaluation-dataset.v1";
    evaluated_distribution.engine_version = evaluation_cohort.engine_version;
    evaluated_distribution.composition_signature = evaluation_cohort.composition_signature;
    evaluated_distribution.mechanics_signature = evaluation_cohort.mechanics_signature;
    evaluated_distribution.horizon_rounds = 1;
    evaluated_distribution.source = "experimental_replay_cohort_distribution.v1";
    for (std::uint64_t match = 1000; match < 1005; ++match)
        evaluated_distribution.replay_artifact_ids.push_back(
            "fixture-replay-" + std::to_string(match));
    CalibrationAcceptanceCriteria evaluation_criteria;
    evaluation_criteria.approved = true;
    evaluation_criteria.protocol_id = "fixture-evaluation-protocol.v1";
    evaluation_criteria.minimum_training_samples = 5;
    evaluation_criteria.minimum_validation_samples = 3;
    evaluation_criteria.minimum_test_samples = 5;
    evaluation_criteria.maximum_mae = 100.0;
    evaluation_criteria.minimum_p90_coverage = 0.0;
    evaluation_criteria.maximum_p90_coverage = 1.0;
    evaluation_criteria.maximum_brier_score = 1.0;
    assert(approve_calibration(
        evaluated_distribution, evaluation.metrics, evaluation_criteria));
    const auto evaluated_risk = derive_survival_risk(
        identity.player_hp, evaluated_distribution);
    assert(evaluated_risk.available);

    auto overlapping_split_samples = evaluation_samples;
    auto overlap = overlapping_split_samples.front();
    overlap.sequence += 1;
    overlap.split = CalibrationDatasetSplit::VALIDATION;
    overlapping_split_samples.push_back(overlap);
    const auto overlapping_evaluation = evaluate_calibration_predictions(
        overlapping_split_samples, evaluation_cohort, evaluation_manifest);
    assert(!overlapping_evaluation.valid);
    assert(overlapping_evaluation.reason == "evaluation_splits_empty_or_episode_overlap");

    auto mismatched_hp_samples = evaluation_samples;
    mismatched_hp_samples.front().observed_hp_before -= 1.0;
    const auto mismatched_hp_evaluation = evaluate_calibration_predictions(
        mismatched_hp_samples, evaluation_cohort, evaluation_manifest);
    assert(!mismatched_hp_evaluation.valid);
    assert(mismatched_hp_evaluation.reason ==
        "invalid_paired_prediction_outcome_sample");

    auto missing_ability = input;
    missing_ability.player_a.units.front().ability.api_name.clear();
    missing_ability.player_a.units.front().ability.metadata_complete = false;
    auto incomplete_snapshot = builder.build(identity, missing_ability, 31);
    assert(incomplete_snapshot.valid);
    assert(!CombatCoverageValidator{}.validate(incomplete_snapshot.coverage).complete);
    const auto partial_projection =
        CombatProjectionEngine{}.project(incomplete_snapshot, 6, 2, 200);
    assert(partial_projection.simulation_completed);
    assert(!partial_projection.decision_eligible);
    assert(partial_projection.status == "partial_unsupported_mechanics");

    auto missing_trait_metadata = input;
    CombatTrait active_trait;
    active_trait.api_name = "TFT_TestTrait";
    active_trait.active = true;
    active_trait.active_count = 2;
    missing_trait_metadata.player_a.units.front().traits.push_back(active_trait);
    const auto trait_snapshot = builder.build(identity, missing_trait_metadata, 31);
    assert(!CombatCoverageValidator{}.validate(trait_snapshot.coverage).complete);
    assert(trait_snapshot.coverage.missing_trait_effect_metadata == 1);
    assert(trait_snapshot.coverage.traits_seen == 1);
    assert(trait_snapshot.coverage.traits_supported == 0);

    auto stale = identity;
    stale.sequence = 30;
    assert(!builder.build(stale, input, 31).valid);

    auto wrong_hp = input;
    wrong_hp.player_a.player_hp += 1.0f;
    const auto wrong_hp_snapshot = builder.build(identity, wrong_hp, 31);
    assert(!wrong_hp_snapshot.valid);
    assert(wrong_hp_snapshot.validation_reason ==
        "combat_input_matchup_or_hp_identity_mismatch");

    auto invalid_stat = input;
    invalid_stat.player_a.units.front().attack_damage =
        std::numeric_limits<float>::quiet_NaN();
    const auto invalid_stat_snapshot = builder.build(identity, invalid_stat, 31);
    assert(!invalid_stat_snapshot.valid);
    assert(invalid_stat_snapshot.validation_reason ==
        "combat_input_unit_identity_position_or_stat_invalid");

    auto invalid_config = input;
    invalid_config.config.seed += 1;
    const auto invalid_config_snapshot = builder.build(identity, invalid_config, 31);
    assert(!invalid_config_snapshot.valid);
    assert(invalid_config_snapshot.validation_reason ==
        "combat_input_simulator_configuration_invalid");

    auto wrong_matchup = input;
    wrong_matchup.player_b.player_id = 2;
    assert(!builder.build(identity, wrong_matchup, 31).valid);
    auto wrong_unit_uuid = input;
    wrong_unit_uuid.player_b.units.front().source_unit_uuid = "wrong-unit-uuid";
    assert(!builder.build(identity, wrong_unit_uuid, 31).valid);

    assert(!CombatProjectionEngine{}.project(snapshot, 6, 0, 300).simulation_completed);
    assert(!CombatProjectionEngine{}.project(snapshot, 6, 33, 300).simulation_completed);

    auto second_opponent_input = input;
    second_opponent_input.player_b.player_id = 2;
    second_opponent_input.player_b.player_hp = 60.0f;
    second_opponent_input.player_b.units.front().source_unit_uuid = "opponent-two-unit-uuid";
    auto second_opponent_identity = identity;
    second_opponent_identity.opponent_id = 2;
    second_opponent_identity.opponent_hp = 60.0;
    second_opponent_identity.opponent_unit_ids = {"opponent-two-unit-uuid"};
    const auto second_opponent_snapshot =
        builder.build(second_opponent_identity, second_opponent_input, 31);
    assert(second_opponent_snapshot.valid);
    const std::vector<CombatMatchupProjectionCandidate> matchup_candidates{
        {0.75, snapshot}, {0.25, second_opponent_snapshot}};
    const auto matchup_projection =
        CombatProjectionEngine{}.project_matchups(matchup_candidates, 6, 2, 500);
    assert(matchup_projection.simulation_completed);
    assert(!matchup_projection.decision_eligible);
    assert(matchup_projection.opponent_id == -1);
    assert(matchup_projection.weighted_scenarios.size() == 4);
    double probability_sum = 0.0;
    double weighted_damage = 0.0;
    bool saw_first_opponent = false;
    bool saw_second_opponent = false;
    for (const auto& scenario : matchup_projection.weighted_scenarios) {
        probability_sum += scenario.probability;
        weighted_damage += scenario.probability * scenario.incoming_damage;
        saw_first_opponent = saw_first_opponent || scenario.opponent_id == 1;
        saw_second_opponent = saw_second_opponent || scenario.opponent_id == 2;
    }
    assert(std::abs(probability_sum - 1.0) < 1e-9);
    assert(std::abs(weighted_damage - matchup_projection.expected_incoming_damage) < 1e-9);
    assert(saw_first_opponent && saw_second_opponent);
    assert(matchup_projection.status == "experimental_uncalibrated");
    auto invalid_matchup_candidates = matchup_candidates;
    invalid_matchup_candidates[0].probability = 0.50;
    invalid_matchup_candidates[1].probability = 0.25;
    const auto invalid_matchup_projection =
        CombatProjectionEngine{}.project_matchups(invalid_matchup_candidates, 6, 2, 600);
    assert(!invalid_matchup_projection.simulation_completed);
    assert(invalid_matchup_projection.reason ==
        "matchup_probabilities_do_not_sum_to_one");

    std::cout << "combat prediction pipeline tests passed\n";
}
