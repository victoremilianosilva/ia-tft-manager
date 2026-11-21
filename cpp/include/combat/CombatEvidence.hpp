#pragma once

#include "strategy/StrategicPlanning.hpp"
#include "combat/CombatInput.hpp"

#include <algorithm>
#include <cstddef>
#include <cmath>
#include <cstdint>
#include <limits>
#include <string>
#include <unordered_set>
#include <vector>

namespace tft::combat_evidence {

struct DamageDistribution;
struct CalibrationValidationMetrics;
struct CalibrationAcceptanceCriteria;
struct SurvivalRiskEvidence;
struct CombatHorizonTrajectory;

class CalibrationApprovalToken {
public:
    bool valid() const noexcept { return valid_; }

private:
    bool valid_{false};
    std::uint64_t match_id_{0};
    std::int32_t player_id_{-1};
    std::uint32_t round_{0};
    std::uint64_t sequence_{0};
    std::uint32_t horizon_rounds_{0};
    double expected_damage_{0.0};
    double elimination_risk_{0.0};
    double uncertainty_{1.0};
    std::string source_;
    std::string protocol_id_;
    std::string report_sha256_;
    std::string dataset_version_;
    std::vector<std::string> replay_artifact_ids_;

    friend bool approve_calibration(
        DamageDistribution&, const CalibrationValidationMetrics&,
        const CalibrationAcceptanceCriteria&);
    friend SurvivalRiskEvidence derive_survival_risk(
        double, const DamageDistribution&);
    friend SurvivalRiskEvidence derive_multi_round_survival_risk(
        double, std::uint64_t, std::int32_t, std::uint32_t, std::uint64_t,
        std::uint32_t, const std::vector<CombatHorizonTrajectory>&, std::uint32_t);
    friend bool apply_to_economic_context(
        const SurvivalRiskEvidence&, strategy::StrategicSharedContext&);
};

struct CombatSnapshot {
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::int32_t opponent_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0}; // per-player strategic-context sequence
    std::uint64_t engine_decision_sequence{0};
    double player_hp{-1.0};
    double opponent_hp{-1.0};
    std::vector<std::string> player_unit_ids;
    std::vector<std::string> opponent_unit_ids;
    bool player_roster_complete{false};
    bool opponent_roster_complete{false};
};

struct CombatSnapshotValidation {
    bool valid{false};
    std::string reason{"missing_identity"};
};

class CombatSnapshotBuilder {
public:
    CombatSnapshotValidation validate(const CombatSnapshot& s, std::uint64_t expected_sequence = 0) const {
        if (s.match_id == 0 || s.player_id < 0 || s.opponent_id < 0 ||
            s.player_id == s.opponent_id || s.round == 0 || s.sequence == 0 ||
            s.engine_decision_sequence == 0)
            return {false, "invalid_or_missing_identity"};
        if (expected_sequence != 0 && s.sequence != expected_sequence)
            return {false, "stale_snapshot_sequence"};
        if (!std::isfinite(s.player_hp) || !std::isfinite(s.opponent_hp) ||
            s.player_hp < 0.0 || s.opponent_hp < 0.0)
            return {false, "hp_unavailable"};
        if (!s.player_roster_complete || !s.opponent_roster_complete ||
            s.player_unit_ids.empty() || s.opponent_unit_ids.empty())
            return {false, "roster_incomplete"};
        const auto unique_nonempty = [](const std::vector<std::string>& ids) {
            for (std::size_t i = 0; i < ids.size(); ++i) {
                if (ids[i].empty()) return false;
                if (std::find(ids.begin(), ids.begin() + static_cast<std::ptrdiff_t>(i), ids[i]) !=
                    ids.begin() + static_cast<std::ptrdiff_t>(i)) return false;
            }
            return true;
        };
        if (!unique_nonempty(s.player_unit_ids) || !unique_nonempty(s.opponent_unit_ids))
            return {false, "unit_identity_missing_or_duplicate"};
        for (const auto& player_unit_id : s.player_unit_ids) {
            if (std::find(s.opponent_unit_ids.begin(), s.opponent_unit_ids.end(),
                          player_unit_id) != s.opponent_unit_ids.end())
                return {false, "unit_identity_shared_between_opponents"};
        }
        return {true, "valid"};
    }
};

struct MatchupCandidateProbability {
    std::int32_t opponent_id{-1};
    double probability{0.0};
};

struct MatchupCandidateSet {
    bool available{false};
    std::vector<MatchupCandidateProbability> candidates;
    double total_probability{0.0};
    std::string reason{"matchup_candidates_unavailable"};
};

// A matchup can only be resolved from an actual opponent identity supplied by
// the lobby, or from a complete externally supplied probability distribution.
class MatchupResolver {
public:
    bool resolve(const CombatSnapshot& snapshot, std::int32_t actual_opponent_id,
                 std::int32_t& resolved_opponent_id) const {
        if (snapshot.match_id == 0 || snapshot.player_id < 0 ||
            snapshot.opponent_id < 0 || actual_opponent_id < 0 ||
            snapshot.player_id == snapshot.opponent_id ||
            snapshot.opponent_id != actual_opponent_id) return false;
        resolved_opponent_id = actual_opponent_id;
        return true;
    }

    MatchupCandidateSet resolve_candidates(
        std::int32_t player_id,
        const std::vector<MatchupCandidateProbability>& candidates) const {
        MatchupCandidateSet out;
        if (player_id < 0 || candidates.empty()) return out;
        std::unordered_set<std::int32_t> opponent_ids;
        double total = 0.0;
        for (const auto& candidate : candidates) {
            if (candidate.opponent_id < 0 || candidate.opponent_id == player_id ||
                !opponent_ids.insert(candidate.opponent_id).second ||
                !std::isfinite(candidate.probability) ||
                candidate.probability <= 0.0 || candidate.probability > 1.0) {
                out.reason = "invalid_or_duplicate_matchup_candidate";
                return out;
            }
            total += candidate.probability;
        }
        if (!std::isfinite(total) || std::abs(total - 1.0) > 1e-6) {
            out.reason = "matchup_probabilities_do_not_sum_to_one";
            return out;
        }
        out.available = true;
        out.candidates = candidates;
        out.total_probability = total;
        out.reason = "explicit_matchup_probability_distribution";
        return out;
    }
};

struct CombatCoverage {
    std::uint32_t units_seen{0};
    std::uint32_t units_supported{0};
    std::uint32_t unsupported_abilities{0};
    std::uint32_t unsupported_traits{0};
    std::uint32_t unsupported_items{0};
    std::uint32_t missing_scripts{0};
    bool all_effects_catalogued{false};
    std::uint32_t unsupported_effects{0};
    std::uint32_t missing_ability_metadata{0};
    std::uint32_t missing_item_effect_metadata{0};
    std::uint32_t missing_trait_effect_metadata{0};
    std::uint32_t abilities_seen{0}, abilities_supported{0};
    std::uint32_t items_seen{0}, items_supported{0};
    std::uint32_t traits_seen{0}, traits_supported{0};
    std::uint32_t effects_seen{0}, effects_supported{0};
};

struct CombatCoverageResult {
    bool complete{false};
    double supported_fraction{0.0};
    std::string status{"unavailable"};
};

class CombatCoverageValidator {
public:
    // Inspect the exact CombatInput consumed by CombatEngine. Unknown or
    // absent mechanics metadata is unsupported, never silently assumed safe.
    CombatCoverage inspect(const CombatInput& input) const {
        CombatCoverage coverage;
        const auto supported_effect = [](const CombatEffectDefinition& effect) {
            const bool trigger_supported =
                effect.trigger.empty() || effect.trigger == "combat_start" ||
                effect.trigger == "on_attack" || effect.trigger == "on_kill" ||
                effect.trigger == "after_delay" || effect.trigger == "while_hp_below" ||
                effect.trigger == "on_ally_shield";
            const bool operation_supported =
                effect.operation == "add_stat" || effect.operation == "bonus_damage" ||
                effect.operation == "heal_max_hp_pct" ||
                effect.operation == "grant_charges" || effect.operation == "mana_regen";
            const bool target_supported =
                effect.target.empty() || effect.target == "self" ||
                effect.target == "allies" ||
                effect.target == "allies_same_row_within_1";
            const bool condition_supported =
                effect.condition.empty() || effect.condition == "has_trait" ||
                effect.condition == "trait_count_at_least" ||
                effect.condition == "role_tank" || effect.condition == "role_fighter" ||
                effect.condition == "role_assassin" || effect.condition == "role_other";
            const bool stat_supported =
                effect.operation != "add_stat" ||
                effect.stat == "attack_damage" || effect.stat == "attack_speed" ||
                effect.stat == "ability_power" || effect.stat == "armor" ||
                effect.stat == "magic_resist" || effect.stat == "omnivamp" ||
                effect.stat == "damage_amplification" ||
                effect.stat == "damage_reduction" || effect.stat == "max_hp";
            return trigger_supported && operation_supported && target_supported &&
                condition_supported && stat_supported &&
                std::isfinite(effect.value) && std::isfinite(effect.duration) &&
                std::isfinite(effect.interval) && std::isfinite(effect.delay) &&
                std::isfinite(effect.health_threshold);
        };
        const auto inspect_effects = [&](const std::vector<CombatEffectDefinition>& effects) {
            for (const auto& effect : effects) {
                ++coverage.effects_seen;
                if (supported_effect(effect)) ++coverage.effects_supported;
                else ++coverage.unsupported_effects;
            }
        };
        const auto inspect_team = [&](const CombatTeam& team) {
            for (const auto& unit : team.units) {
                ++coverage.units_seen;
                bool unit_supported = !unit.api_name.empty();
                ++coverage.abilities_seen;
                bool ability_supported = !unit.ability.api_name.empty() &&
                    unit.ability.metadata_complete;
                if (!ability_supported) {
                    ++coverage.missing_scripts;
                    ++coverage.missing_ability_metadata;
                    unit_supported = false;
                }
                if (unit.ability.has_buff || unit.ability.has_debuff ||
                    unit.ability.has_area_effect) {
                    ++coverage.unsupported_abilities;
                    ability_supported = false;
                    unit_supported = false;
                }
                if (ability_supported) ++coverage.abilities_supported;
                for (const auto& item : unit.items) {
                    ++coverage.items_seen;
                    if (!item.effects_complete) {
                        ++coverage.missing_item_effect_metadata;
                        ++coverage.unsupported_items;
                        unit_supported = false;
                    } else {
                        const auto before = coverage.unsupported_effects;
                        inspect_effects(item.effects);
                        if (coverage.unsupported_effects != before) {
                            ++coverage.unsupported_items;
                            unit_supported = false;
                        } else {
                            ++coverage.items_supported;
                        }
                    }
                }
                for (const auto& trait : unit.traits) {
                    if (!(trait.active || trait.active_count > 0)) continue;
                    ++coverage.traits_seen;
                    if (!trait.effects_complete) {
                        ++coverage.missing_trait_effect_metadata;
                        ++coverage.unsupported_traits;
                        unit_supported = false;
                    } else {
                        const auto before = coverage.unsupported_effects;
                        inspect_effects(trait.effects);
                        if (coverage.unsupported_effects != before) {
                            ++coverage.unsupported_traits;
                            unit_supported = false;
                        } else {
                            ++coverage.traits_supported;
                        }
                    }
                }
                if (unit_supported) ++coverage.units_supported;
            }
        };
        inspect_team(input.player_a);
        inspect_team(input.player_b);
        coverage.all_effects_catalogued =
            coverage.abilities_supported == coverage.abilities_seen &&
            coverage.items_supported == coverage.items_seen &&
            coverage.traits_supported == coverage.traits_seen &&
            coverage.effects_supported == coverage.effects_seen &&
            coverage.unsupported_effects == 0 && coverage.missing_scripts == 0 &&
            coverage.unsupported_abilities == 0 && coverage.unsupported_items == 0 &&
            coverage.unsupported_traits == 0;
        return coverage;
    }

    CombatCoverageResult validate(const CombatCoverage& c) const {
        if (c.units_seen == 0 || c.units_supported > c.units_seen ||
            c.abilities_supported > c.abilities_seen ||
            c.items_supported > c.items_seen || c.traits_supported > c.traits_seen ||
            c.effects_supported > c.effects_seen ||
            c.abilities_seen != c.units_seen)
            return {false, 0.0, "invalid_coverage_counts"};
        const double fraction = static_cast<double>(c.units_supported) /
            static_cast<double>(c.units_seen);
        const bool complete = c.units_supported == c.units_seen &&
            c.unsupported_abilities == 0 && c.unsupported_traits == 0 &&
            c.unsupported_items == 0 && c.missing_scripts == 0 &&
            c.unsupported_effects == 0 && c.missing_ability_metadata == 0 &&
            c.missing_item_effect_metadata == 0 &&
            c.missing_trait_effect_metadata == 0 &&
            c.abilities_supported == c.abilities_seen &&
            c.items_supported == c.items_seen &&
            c.traits_supported == c.traits_seen &&
            c.effects_supported == c.effects_seen && c.all_effects_catalogued;
        return {complete, fraction, complete ? "complete" : "partial_unsupported_mechanics"};
    }
};

struct ObservedCombatOutcome {
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    double incoming_damage{0.0};
    bool observed{false};
    std::string source{"unknown"};
    std::string replay_artifact_id;
    std::string dataset_version;
    std::string engine_version;
    std::string composition_signature;
    std::string mechanics_signature;
    std::uint32_t horizon_rounds{1};
};

struct CombatCalibrationCohort {
    std::uint32_t round{0};
    std::uint32_t horizon_rounds{1};
    std::string engine_version;
    std::string composition_signature;
    std::string mechanics_signature;
};

struct DamageDistribution {
    bool calibrated{false};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t before_round{0};
    std::uint64_t before_sequence{0};
    std::uint32_t sample_count{0};
    std::uint32_t minimum_sample_count{30};
    double mean{0.0};
    double p50{0.0};
    double p90{0.0};
    double uncertainty{1.0};
    std::vector<double> observed_damage_samples;
    std::string replay_artifact_id;
    std::vector<std::string> replay_artifact_ids;
    std::string dataset_version;
    std::string engine_version;
    std::string composition_signature;
    std::string mechanics_signature;
    std::uint32_t horizon_rounds{1};
    std::string calibration_protocol_id;
    std::string calibration_report_sha256;
    std::string calibration_train_manifest_sha256;
    std::string calibration_validation_manifest_sha256;
    std::string calibration_test_manifest_sha256;
    double calibration_mae{0.0};
    double calibration_p90_coverage{0.0};
    double calibration_brier_score{0.0};
    std::string source{"unavailable_no_replay_dataset"};
    CalibrationApprovalToken approval;
};

// Empirical calibration is promoted only by an explicit evaluation report.
// Sample count alone is never evidence that a predictor is calibrated.
struct CalibrationAcceptanceCriteria {
    bool approved{false};
    std::string protocol_id;
    std::uint32_t minimum_training_samples{0};
    std::uint32_t minimum_validation_samples{0};
    std::uint32_t minimum_test_samples{0};
    double maximum_mae{0.0};
    double minimum_p90_coverage{0.0};
    double maximum_p90_coverage{1.0};
    double maximum_brier_score{1.0};
};

struct CalibrationValidationMetrics {
    std::string report_sha256;
    std::string train_manifest_sha256;
    std::string validation_manifest_sha256;
    std::string test_manifest_sha256;
    bool episode_splits_disjoint{false};
    std::uint32_t validation_sample_count{0};
    std::uint32_t test_sample_count{0};
    double mae{0.0};
    double p90_coverage{0.0};
    double brier_score{0.0};
};

inline bool is_sha256(const std::string& value) {
    return value.size() == 64 &&
        std::all_of(value.begin(), value.end(), [](unsigned char c) {
            return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f');
        });
}

inline bool approve_calibration(
    DamageDistribution& distribution,
    const CalibrationValidationMetrics& metrics,
    const CalibrationAcceptanceCriteria& criteria) {
    const bool valid_criteria = criteria.approved && !criteria.protocol_id.empty() &&
        criteria.minimum_training_samples > 0 &&
        criteria.minimum_validation_samples > 0 &&
        criteria.minimum_test_samples > 0 &&
        std::isfinite(criteria.maximum_mae) && criteria.maximum_mae >= 0.0 &&
        std::isfinite(criteria.minimum_p90_coverage) &&
        std::isfinite(criteria.maximum_p90_coverage) &&
        criteria.minimum_p90_coverage >= 0.0 &&
        criteria.maximum_p90_coverage <= 1.0 &&
        criteria.minimum_p90_coverage <= criteria.maximum_p90_coverage &&
        std::isfinite(criteria.maximum_brier_score) &&
        criteria.maximum_brier_score >= 0.0 && criteria.maximum_brier_score <= 1.0;
    const bool valid_metrics = is_sha256(metrics.report_sha256) &&
        is_sha256(metrics.train_manifest_sha256) &&
        is_sha256(metrics.validation_manifest_sha256) &&
        is_sha256(metrics.test_manifest_sha256) &&
        metrics.train_manifest_sha256 != metrics.validation_manifest_sha256 &&
        metrics.train_manifest_sha256 != metrics.test_manifest_sha256 &&
        metrics.validation_manifest_sha256 != metrics.test_manifest_sha256 &&
        metrics.episode_splits_disjoint &&
        metrics.validation_sample_count >= criteria.minimum_validation_samples &&
        metrics.test_sample_count >= criteria.minimum_test_samples &&
        std::isfinite(metrics.mae) && metrics.mae >= 0.0 &&
        std::isfinite(metrics.p90_coverage) &&
        metrics.p90_coverage >= 0.0 && metrics.p90_coverage <= 1.0 &&
        std::isfinite(metrics.brier_score) &&
        metrics.brier_score >= 0.0 && metrics.brier_score <= 1.0;
    if (!valid_criteria || !valid_metrics || distribution.calibrated ||
        distribution.sample_count < criteria.minimum_training_samples ||
        distribution.replay_artifact_ids.empty() ||
        std::any_of(distribution.replay_artifact_ids.begin(),
            distribution.replay_artifact_ids.end(),
            [](const std::string& artifact) { return artifact.empty(); }) ||
        distribution.dataset_version.empty() || distribution.engine_version.empty() ||
        distribution.composition_signature.empty() ||
        distribution.mechanics_signature.empty() || distribution.horizon_rounds != 1 ||
        distribution.source != "experimental_replay_cohort_distribution.v1" ||
        metrics.mae > criteria.maximum_mae ||
        metrics.p90_coverage < criteria.minimum_p90_coverage ||
        metrics.p90_coverage > criteria.maximum_p90_coverage ||
        metrics.brier_score > criteria.maximum_brier_score)
        return false;

    distribution.calibrated = true;
    distribution.calibration_protocol_id = criteria.protocol_id;
    distribution.calibration_report_sha256 = metrics.report_sha256;
    distribution.calibration_train_manifest_sha256 = metrics.train_manifest_sha256;
    distribution.calibration_validation_manifest_sha256 = metrics.validation_manifest_sha256;
    distribution.calibration_test_manifest_sha256 = metrics.test_manifest_sha256;
    distribution.calibration_mae = metrics.mae;
    distribution.calibration_p90_coverage = metrics.p90_coverage;
    distribution.calibration_brier_score = metrics.brier_score;
    distribution.source = "approved_replay_calibration.v1";
    distribution.approval.valid_ = true;
    distribution.approval.match_id_ = distribution.match_id;
    distribution.approval.player_id_ = distribution.player_id;
    distribution.approval.round_ = distribution.before_round;
    distribution.approval.sequence_ = distribution.before_sequence;
    distribution.approval.horizon_rounds_ = distribution.horizon_rounds;
    distribution.approval.expected_damage_ = distribution.mean;
    distribution.approval.uncertainty_ = distribution.uncertainty;
    distribution.approval.source_ = distribution.source;
    distribution.approval.protocol_id_ = distribution.calibration_protocol_id;
    distribution.approval.report_sha256_ = distribution.calibration_report_sha256;
    distribution.approval.dataset_version_ = distribution.dataset_version;
    distribution.approval.replay_artifact_ids_ = distribution.replay_artifact_ids;
    return true;
}

// Calibration is empirical only: synthetic simulations and uncalibrated
// CombatEngine output cannot be passed off as observed opponent damage.
class CombatPredictionCalibrator {
public:
    DamageDistribution calibrate(
        const std::vector<ObservedCombatOutcome>& outcomes,
        std::uint64_t match_id, std::int32_t player_id,
        std::uint32_t before_round, std::uint64_t before_sequence,
        std::uint32_t minimum_samples = 30) const {
        DamageDistribution out;
        out.match_id = match_id;
        out.player_id = player_id;
        out.before_round = before_round;
        out.before_sequence = before_sequence;
        out.minimum_sample_count = minimum_samples;
        if (match_id == 0 || player_id < 0 || before_round == 0 ||
            before_sequence == 0 || minimum_samples == 0) {
            out.source = "invalid_calibration_identity_or_window";
            return out;
        }
        std::vector<double> values;
        std::unordered_set<std::uint64_t> seen_sequences;
        std::unordered_set<std::string> replay_artifact_ids;
        std::string dataset_version;
        for (const auto& e : outcomes) {
            if (!e.observed || e.source != "versioned_replay_outcome.v1" ||
                e.replay_artifact_id.empty() || e.dataset_version.empty() ||
                e.match_id != match_id || e.player_id != player_id ||
                e.round >= before_round || e.sequence == 0 ||
                e.sequence >= before_sequence ||
                !std::isfinite(e.incoming_damage) || e.incoming_damage < 0.0)
                continue;
            if (dataset_version.empty()) dataset_version = e.dataset_version;
            else if (dataset_version != e.dataset_version) {
                out.source = "invalid_mixed_dataset_versions";
                return out;
            }
            replay_artifact_ids.insert(e.replay_artifact_id);
            if (!seen_sequences.insert(e.sequence).second) {
                out.source = "invalid_duplicate_outcome_sequence";
                return out;
            }
            values.push_back(e.incoming_damage);
        }
        out.sample_count = static_cast<std::uint32_t>(values.size());
        if (minimum_samples == 0 || values.size() < minimum_samples) return out;
        std::sort(values.begin(), values.end());
        const auto quantile = [&](double q) {
            const auto index = static_cast<std::size_t>(
                std::ceil(q * static_cast<double>(values.size())) - 1.0);
            return values[std::min(index, values.size() - 1)];
        };
        double sum = 0.0;
        for (double v : values) sum += v;
        out.mean = sum / static_cast<double>(values.size());
        out.p50 = quantile(0.50);
        out.p90 = quantile(0.90);
        out.observed_damage_samples = values;
        out.replay_artifact_ids.assign(replay_artifact_ids.begin(), replay_artifact_ids.end());
        std::sort(out.replay_artifact_ids.begin(), out.replay_artifact_ids.end());
        if (out.replay_artifact_ids.size() == 1)
            out.replay_artifact_id = out.replay_artifact_ids.front();
        out.dataset_version = dataset_version;
        out.uncertainty = 1.0 / std::sqrt(static_cast<double>(values.size()));
        out.calibrated = false;
        out.source = "experimental_same_match_diagnostic_distribution.v1";
        return out;
    }

    // Cohort calibration generalizes across independent matches while keeping
    // engine, composition/mechanics signature, round and horizon identical.
    // The target match is excluded to prevent same-match outcome leakage.
    DamageDistribution calibrate_for_cohort(
        const std::vector<ObservedCombatOutcome>& outcomes,
        std::uint64_t target_match_id,
        std::int32_t target_player_id,
        std::uint32_t before_round,
        std::uint64_t before_sequence,
        const CombatCalibrationCohort& cohort,
        std::uint32_t minimum_samples = 30) const {
        DamageDistribution out;
        out.match_id = target_match_id;
        out.player_id = target_player_id;
        out.before_round = before_round;
        out.before_sequence = before_sequence;
        out.minimum_sample_count = minimum_samples;
        out.engine_version = cohort.engine_version;
        out.composition_signature = cohort.composition_signature;
        out.mechanics_signature = cohort.mechanics_signature;
        out.horizon_rounds = cohort.horizon_rounds;
        if (target_match_id == 0 || target_player_id < 0 || before_round == 0 ||
            before_sequence == 0 || minimum_samples == 0 || cohort.round != before_round ||
            cohort.horizon_rounds != 1 || cohort.engine_version.empty() ||
            cohort.composition_signature.empty() || cohort.mechanics_signature.empty()) {
            out.source = "invalid_calibration_cohort_identity";
            return out;
        }

        std::vector<double> values;
        std::unordered_set<std::uint64_t> seen_matches;
        std::unordered_set<std::string> seen_samples;
        std::unordered_set<std::string> artifact_ids;
        std::string dataset_version;
        for (const auto& outcome : outcomes) {
            if (!outcome.observed || outcome.source != "versioned_replay_outcome.v1" ||
                outcome.match_id == 0 || outcome.match_id == target_match_id ||
                outcome.player_id < 0 || outcome.round != cohort.round ||
                outcome.sequence == 0 || outcome.horizon_rounds != cohort.horizon_rounds ||
                outcome.engine_version != cohort.engine_version ||
                outcome.composition_signature != cohort.composition_signature ||
                outcome.mechanics_signature != cohort.mechanics_signature ||
                outcome.replay_artifact_id.empty() || outcome.dataset_version.empty() ||
                !std::isfinite(outcome.incoming_damage) || outcome.incoming_damage < 0.0)
                continue;
            if (dataset_version.empty()) dataset_version = outcome.dataset_version;
            else if (dataset_version != outcome.dataset_version) {
                out.source = "invalid_mixed_dataset_versions";
                return out;
            }
            const auto sample_key = std::to_string(outcome.match_id) + ":" +
                std::to_string(outcome.sequence);
            if (!seen_samples.insert(sample_key).second ||
                !seen_matches.insert(outcome.match_id).second) {
                out.source = "invalid_duplicate_match_cohort_sample";
                return out;
            }
            artifact_ids.insert(outcome.replay_artifact_id);
            values.push_back(outcome.incoming_damage);
        }
        out.sample_count = static_cast<std::uint32_t>(values.size());
        if (values.size() < minimum_samples) {
            out.source = "insufficient_independent_match_cohort_samples";
            return out;
        }
        std::sort(values.begin(), values.end());
        const auto quantile = [&](double q) {
            const auto index = static_cast<std::size_t>(
                std::ceil(q * static_cast<double>(values.size())) - 1.0);
            return values[std::min(index, values.size() - 1)];
        };
        double sum = 0.0;
        for (const double value : values) sum += value;
        out.mean = sum / static_cast<double>(values.size());
        out.p50 = quantile(0.50);
        out.p90 = quantile(0.90);
        out.observed_damage_samples = std::move(values);
        out.replay_artifact_ids.assign(artifact_ids.begin(), artifact_ids.end());
        std::sort(out.replay_artifact_ids.begin(), out.replay_artifact_ids.end());
        if (out.replay_artifact_ids.size() == 1)
            out.replay_artifact_id = out.replay_artifact_ids.front();
        out.dataset_version = dataset_version;
        out.uncertainty = 1.0 / std::sqrt(static_cast<double>(out.sample_count));
        out.calibrated = false;
        out.source = "experimental_replay_cohort_distribution.v1";
        return out;
    }
};

struct SurvivalRiskEvidence {
    bool available{false};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    double expected_damage{0.0};
    double elimination_risk{0.0};
    std::uint32_t horizon_rounds{1};
    double uncertainty{1.0};
    std::string calibration_protocol_id;
    std::string calibration_report_sha256;
    std::string dataset_version;
    std::vector<std::string> replay_artifact_ids;
    CalibrationApprovalToken approval;
    std::string source{"unavailable_uncalibrated_damage"};
};

inline SurvivalRiskEvidence derive_survival_risk(
    double observed_hp, const DamageDistribution& distribution) {
    SurvivalRiskEvidence out;
    if (!std::isfinite(observed_hp) || observed_hp < 0.0 ||
        !distribution.calibrated ||
        distribution.source != "approved_replay_calibration.v1" ||
        (distribution.replay_artifact_id.empty() &&
            distribution.replay_artifact_ids.empty()) ||
        distribution.dataset_version.empty() || distribution.engine_version.empty() ||
        distribution.composition_signature.empty() ||
        distribution.mechanics_signature.empty() || distribution.horizon_rounds != 1 ||
        distribution.replay_artifact_ids.empty() ||
        !distribution.approval.valid_ ||
        distribution.approval.match_id_ != distribution.match_id ||
        distribution.approval.player_id_ != distribution.player_id ||
        distribution.approval.round_ != distribution.before_round ||
        distribution.approval.sequence_ != distribution.before_sequence ||
        distribution.approval.horizon_rounds_ != distribution.horizon_rounds ||
        distribution.approval.expected_damage_ != distribution.mean ||
        distribution.approval.source_ != "approved_replay_calibration.v1" ||
        distribution.approval.protocol_id_ != distribution.calibration_protocol_id ||
        distribution.approval.report_sha256_ != distribution.calibration_report_sha256 ||
        distribution.approval.dataset_version_ != distribution.dataset_version ||
        distribution.approval.replay_artifact_ids_ != distribution.replay_artifact_ids ||
        distribution.minimum_sample_count == 0 ||
        distribution.sample_count < distribution.minimum_sample_count ||
        distribution.observed_damage_samples.size() != distribution.sample_count ||
        distribution.calibration_protocol_id.empty() ||
        !is_sha256(distribution.calibration_report_sha256) ||
        !is_sha256(distribution.calibration_train_manifest_sha256) ||
        !is_sha256(distribution.calibration_validation_manifest_sha256) ||
        !is_sha256(distribution.calibration_test_manifest_sha256) ||
        distribution.calibration_train_manifest_sha256 ==
            distribution.calibration_validation_manifest_sha256 ||
        distribution.calibration_train_manifest_sha256 ==
            distribution.calibration_test_manifest_sha256 ||
        distribution.calibration_validation_manifest_sha256 ==
            distribution.calibration_test_manifest_sha256 ||
        !std::isfinite(distribution.calibration_mae) ||
        distribution.calibration_mae < 0.0 ||
        !std::isfinite(distribution.calibration_p90_coverage) ||
        distribution.calibration_p90_coverage < 0.0 ||
        distribution.calibration_p90_coverage > 1.0 ||
        !std::isfinite(distribution.calibration_brier_score) ||
        distribution.calibration_brier_score < 0.0 ||
        distribution.calibration_brier_score > 1.0 ||
        !std::isfinite(distribution.mean) || distribution.mean < 0.0 ||
        !std::isfinite(distribution.p50) || distribution.p50 < 0.0 ||
        !std::isfinite(distribution.p90) || distribution.p90 < distribution.p50 ||
        !std::isfinite(distribution.uncertainty) ||
        distribution.uncertainty < 0.0 || distribution.uncertainty > 1.0)
        return out;
    std::size_t lethal_outcomes = 0;
    for (const double damage : distribution.observed_damage_samples) {
        if (!std::isfinite(damage) || damage < 0.0) return out;
        if (damage >= observed_hp) ++lethal_outcomes;
    }
    out.available = true;
    out.match_id = distribution.match_id;
    out.player_id = distribution.player_id;
    out.round = distribution.before_round;
    out.sequence = distribution.before_sequence;
    out.expected_damage = distribution.mean;
    out.elimination_risk = static_cast<double>(lethal_outcomes) /
        static_cast<double>(distribution.sample_count);
    out.horizon_rounds = 1;
    out.uncertainty = distribution.uncertainty;
    out.calibration_protocol_id = distribution.calibration_protocol_id;
    out.calibration_report_sha256 = distribution.calibration_report_sha256;
    out.dataset_version = distribution.dataset_version;
    out.replay_artifact_ids = distribution.replay_artifact_ids;
    if (out.replay_artifact_ids.empty() && !distribution.replay_artifact_id.empty())
        out.replay_artifact_ids.push_back(distribution.replay_artifact_id);
    out.source = "observed_hp+approved_replay_calibration.v1";
    out.approval.valid_ = true;
    out.approval.match_id_ = out.match_id;
    out.approval.player_id_ = out.player_id;
    out.approval.round_ = out.round;
    out.approval.sequence_ = out.sequence;
    out.approval.horizon_rounds_ = out.horizon_rounds;
    out.approval.expected_damage_ = out.expected_damage;
    out.approval.elimination_risk_ = out.elimination_risk;
    out.approval.uncertainty_ = out.uncertainty;
    out.approval.source_ = out.source;
    out.approval.protocol_id_ = out.calibration_protocol_id;
    out.approval.report_sha256_ = out.calibration_report_sha256;
    out.approval.dataset_version_ = out.dataset_version;
    out.approval.replay_artifact_ids_ = out.replay_artifact_ids;
    return out;
}

struct CombatHorizonStep {
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    std::int32_t opponent_id{-1};
    double incoming_damage{0.0};
    double non_combat_hp_delta{0.0};
};

struct CombatHorizonTrajectory {
    std::string scenario_id;
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    double scenario_weight{0.0};
    double uncertainty{1.0};
    bool calibrated{false};
    std::string calibration_protocol_id;
    std::string calibration_report_sha256;
    std::string calibration_train_manifest_sha256;
    std::string calibration_validation_manifest_sha256;
    std::string calibration_test_manifest_sha256;
    bool episode_splits_disjoint{false};
    double calibration_mae{0.0};
    double calibration_p90_coverage{0.0};
    double calibration_brier_score{1.0};
    std::string replay_artifact_id;
    std::string dataset_version;
    std::string source{"unavailable"};
    std::vector<CombatHorizonStep> steps;
};

// Multi-round survival is computed over complete, weighted trajectories.
// Marginal per-round means are never multiplied or treated as independent.
inline SurvivalRiskEvidence derive_multi_round_survival_risk(
    double observed_hp,
    std::uint64_t match_id,
    std::int32_t player_id,
    std::uint32_t first_round,
    std::uint64_t first_sequence,
    std::uint32_t horizon_rounds,
    const std::vector<CombatHorizonTrajectory>& trajectories,
    std::uint32_t minimum_scenarios = 30) {
    SurvivalRiskEvidence out;
    if (!std::isfinite(observed_hp) || observed_hp < 0.0 || match_id == 0 ||
        player_id < 0 || first_round == 0 || first_sequence == 0 ||
        horizon_rounds < 2 || horizon_rounds > 10 ||
        minimum_scenarios == 0 || trajectories.size() < minimum_scenarios)
        return out;

    std::unordered_set<std::string> scenario_ids;
    std::unordered_set<std::string> artifact_ids;
    std::string dataset_version;
    std::string calibration_protocol_id;
    std::string calibration_report_sha256;
    std::string calibration_train_manifest_sha256;
    std::string calibration_validation_manifest_sha256;
    std::string calibration_test_manifest_sha256;
    bool episode_splits_disjoint = true;
    double calibration_mae = 0.0;
    double calibration_p90_coverage = 0.0;
    double calibration_brier_score = 0.0;
    std::vector<std::uint64_t> expected_sequences;
    double total_weight = 0.0;
    double weighted_damage = 0.0;
    double weighted_elimination = 0.0;
    double weighted_uncertainty = 0.0;

    for (const auto& trajectory : trajectories) {
        if (!trajectory.calibrated ||
            trajectory.source != "approved_replay_trajectory.v1" ||
            trajectory.match_id != match_id || trajectory.player_id != player_id ||
            trajectory.scenario_id.empty() || trajectory.replay_artifact_id.empty() ||
            trajectory.dataset_version.empty() || trajectory.calibration_protocol_id.empty() ||
            !is_sha256(trajectory.calibration_report_sha256) ||
            !is_sha256(trajectory.calibration_train_manifest_sha256) ||
            !is_sha256(trajectory.calibration_validation_manifest_sha256) ||
            !is_sha256(trajectory.calibration_test_manifest_sha256) ||
            trajectory.calibration_train_manifest_sha256 ==
                trajectory.calibration_validation_manifest_sha256 ||
            trajectory.calibration_train_manifest_sha256 ==
                trajectory.calibration_test_manifest_sha256 ||
            trajectory.calibration_validation_manifest_sha256 ==
                trajectory.calibration_test_manifest_sha256 ||
            !trajectory.episode_splits_disjoint ||
            !std::isfinite(trajectory.calibration_mae) ||
            trajectory.calibration_mae < 0.0 ||
            !std::isfinite(trajectory.calibration_p90_coverage) ||
            trajectory.calibration_p90_coverage < 0.0 ||
            trajectory.calibration_p90_coverage > 1.0 ||
            !std::isfinite(trajectory.calibration_brier_score) ||
            trajectory.calibration_brier_score < 0.0 ||
            trajectory.calibration_brier_score > 1.0 ||
            trajectory.steps.size() != horizon_rounds ||
            !std::isfinite(trajectory.scenario_weight) ||
            trajectory.scenario_weight <= 0.0 ||
            !std::isfinite(trajectory.uncertainty) ||
            trajectory.uncertainty < 0.0 || trajectory.uncertainty > 1.0)
            return out;
        if (!scenario_ids.insert(trajectory.scenario_id).second) return out;
        if (dataset_version.empty()) {
            dataset_version = trajectory.dataset_version;
            calibration_protocol_id = trajectory.calibration_protocol_id;
            calibration_report_sha256 = trajectory.calibration_report_sha256;
            calibration_train_manifest_sha256 = trajectory.calibration_train_manifest_sha256;
            calibration_validation_manifest_sha256 = trajectory.calibration_validation_manifest_sha256;
            calibration_test_manifest_sha256 = trajectory.calibration_test_manifest_sha256;
            calibration_mae = trajectory.calibration_mae;
            calibration_p90_coverage = trajectory.calibration_p90_coverage;
            calibration_brier_score = trajectory.calibration_brier_score;
        } else if (dataset_version != trajectory.dataset_version ||
                   calibration_protocol_id != trajectory.calibration_protocol_id ||
                   calibration_report_sha256 != trajectory.calibration_report_sha256 ||
                   calibration_train_manifest_sha256 != trajectory.calibration_train_manifest_sha256 ||
                   calibration_validation_manifest_sha256 != trajectory.calibration_validation_manifest_sha256 ||
                   calibration_test_manifest_sha256 != trajectory.calibration_test_manifest_sha256 ||
                   calibration_mae != trajectory.calibration_mae ||
                   calibration_p90_coverage != trajectory.calibration_p90_coverage ||
                   calibration_brier_score != trajectory.calibration_brier_score ||
                   episode_splits_disjoint != trajectory.episode_splits_disjoint) {
            return out;
        }

        double hp = observed_hp;
        double cumulative_damage = 0.0;
        bool eliminated = false;
        std::uint64_t previous_sequence = 0;
        for (std::uint32_t step_index = 0; step_index < horizon_rounds; ++step_index) {
            const auto& step = trajectory.steps[step_index];
            if (step.round != first_round + step_index || step.opponent_id < 0 ||
                step.sequence == 0 || !std::isfinite(step.incoming_damage) ||
                step.incoming_damage < 0.0 ||
                !std::isfinite(step.non_combat_hp_delta) ||
                (step_index == 0 && step.sequence != first_sequence) ||
                (step_index > 0 && step.sequence <= previous_sequence))
                return out;
            if (expected_sequences.size() <= step_index)
                expected_sequences.push_back(step.sequence);
            else if (expected_sequences[step_index] != step.sequence)
                return out;
            previous_sequence = step.sequence;
            cumulative_damage += step.incoming_damage;
            hp += step.non_combat_hp_delta - step.incoming_damage;
            if (hp <= 0.0) {
                eliminated = true;
                break;
            }
        }
        total_weight += trajectory.scenario_weight;
        weighted_damage += trajectory.scenario_weight * cumulative_damage;
        weighted_elimination += trajectory.scenario_weight * (eliminated ? 1.0 : 0.0);
        weighted_uncertainty += trajectory.scenario_weight * trajectory.uncertainty;
        artifact_ids.insert(trajectory.replay_artifact_id);
    }
    if (!std::isfinite(total_weight) || std::abs(total_weight - 1.0) > 1e-6 ||
        artifact_ids.empty() || calibration_protocol_id.empty() ||
        !is_sha256(calibration_report_sha256) || dataset_version.empty()) return out;

    out.available = true;
    out.match_id = match_id;
    out.player_id = player_id;
    out.round = first_round;
    out.sequence = first_sequence;
    out.horizon_rounds = horizon_rounds;
    out.expected_damage = weighted_damage / total_weight;
    out.elimination_risk = weighted_elimination / total_weight;
    out.uncertainty = std::clamp(
        weighted_uncertainty / total_weight +
            1.0 / std::sqrt(static_cast<double>(trajectories.size())),
        0.0, 1.0);
    out.calibration_protocol_id = calibration_protocol_id;
    out.calibration_report_sha256 = calibration_report_sha256;
    out.dataset_version = dataset_version;
    out.replay_artifact_ids.assign(artifact_ids.begin(), artifact_ids.end());
    std::sort(out.replay_artifact_ids.begin(), out.replay_artifact_ids.end());
    out.source = "observed_hp+approved_replay_trajectory.v1";
    return out;
}

inline bool apply_to_economic_context(
    const SurvivalRiskEvidence& risk, strategy::StrategicSharedContext& context) {
    const bool approved_source =
        risk.source == "observed_hp+approved_replay_calibration.v1" ||
        risk.source == "observed_hp+approved_replay_trajectory.v1";
    if (!risk.available || risk.match_id == 0 || risk.player_id < 0 ||
        risk.round == 0 || risk.sequence == 0 || risk.horizon_rounds == 0 ||
        risk.horizon_rounds > 10 || !approved_source ||
        risk.calibration_protocol_id.empty() ||
        !is_sha256(risk.calibration_report_sha256) ||
        risk.dataset_version.empty() || risk.replay_artifact_ids.empty() ||
        !std::isfinite(risk.uncertainty) || risk.uncertainty < 0.0 ||
        risk.uncertainty > 1.0 ||
        context.match_id != risk.match_id ||
        context.player_id != risk.player_id || context.round != risk.round ||
        context.sequence != risk.sequence ||
        !std::isfinite(risk.expected_damage) ||
        !std::isfinite(risk.elimination_risk) || risk.expected_damage < 0.0 ||
        risk.elimination_risk < 0.0 || risk.elimination_risk > 1.0)
        return false;
    context.estimated_incoming_damage = risk.expected_damage;
    context.elimination_risk = risk.elimination_risk;
    context.incoming_damage_source = risk.source;
    context.elimination_risk_source = risk.source;
    context.combat_evidence_horizon_rounds = risk.horizon_rounds;
    context.combat_evidence_sequence = risk.sequence;
    context.combat_evidence_uncertainty = risk.uncertainty;
    context.combat_calibration_protocol_id = risk.calibration_protocol_id;
    context.combat_calibration_report_sha256 = risk.calibration_report_sha256;
    context.combat_dataset_version = risk.dataset_version;
    context.combat_replay_artifact_ids = risk.replay_artifact_ids;
    context.evidence.estimated_incoming_damage = true;
    context.evidence.elimination_risk = true;
    return true;
}

} // namespace tft::combat_evidence
