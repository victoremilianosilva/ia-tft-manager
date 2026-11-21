#pragma once

#include "strategy/StrategicPlanning.hpp"

#include <algorithm>
#include <cstddef>
#include <cmath>
#include <cstdint>
#include <limits>
#include <string>
#include <unordered_set>
#include <vector>

namespace tft::combat_evidence {

struct CombatSnapshot {
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::int32_t opponent_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
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
            s.player_id == s.opponent_id || s.round == 0 || s.sequence == 0)
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

// A matchup can only be resolved from an actual opponent identity supplied by
// the lobby. This resolver never invents an opponent or a probability.
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
};

struct CombatCoverage {
    std::uint32_t units_seen{0};
    std::uint32_t units_supported{0};
    std::uint32_t unsupported_abilities{0};
    std::uint32_t unsupported_traits{0};
    std::uint32_t unsupported_items{0};
    std::uint32_t missing_scripts{0};
    bool all_effects_catalogued{false};
};

struct CombatCoverageResult {
    bool complete{false};
    double supported_fraction{0.0};
    std::string status{"unavailable"};
};

class CombatCoverageValidator {
public:
    CombatCoverageResult validate(const CombatCoverage& c) const {
        if (c.units_seen == 0 || c.units_supported > c.units_seen)
            return {false, 0.0, "invalid_coverage_counts"};
        const double fraction = static_cast<double>(c.units_supported) /
            static_cast<double>(c.units_seen);
        const bool complete = c.units_supported == c.units_seen &&
            c.unsupported_abilities == 0 && c.unsupported_traits == 0 &&
            c.unsupported_items == 0 && c.missing_scripts == 0 &&
            c.all_effects_catalogued;
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
};

struct DamageDistribution {
    bool calibrated{false};
    std::uint32_t sample_count{0};
    std::uint32_t minimum_sample_count{30};
    double mean{0.0};
    double p50{0.0};
    double p90{0.0};
    double uncertainty{1.0};
    std::vector<double> observed_damage_samples;
    std::string source{"unavailable_no_replay_dataset"};
};

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
        out.minimum_sample_count = minimum_samples;
        std::vector<double> values;
        std::unordered_set<std::uint64_t> seen_sequences;
        for (const auto& e : outcomes) {
            if (!e.observed || e.match_id != match_id || e.player_id != player_id ||
                e.round >= before_round || e.sequence == 0 ||
                e.sequence >= before_sequence ||
                !std::isfinite(e.incoming_damage) || e.incoming_damage < 0.0)
                continue;
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
        out.uncertainty = 1.0 / std::sqrt(static_cast<double>(values.size()));
        out.calibrated = true;
        out.source = "observed_replay_outcomes.v1";
        return out;
    }
};

struct SurvivalRiskEvidence {
    bool available{false};
    double expected_damage{0.0};
    double elimination_risk{0.0};
    std::string source{"unavailable_uncalibrated_damage"};
};

inline SurvivalRiskEvidence derive_survival_risk(
    double observed_hp, const DamageDistribution& distribution) {
    SurvivalRiskEvidence out;
    if (!std::isfinite(observed_hp) || observed_hp < 0.0 ||
        !distribution.calibrated ||
        distribution.source != "observed_replay_outcomes.v1" ||
        distribution.minimum_sample_count == 0 ||
        distribution.sample_count < distribution.minimum_sample_count ||
        distribution.observed_damage_samples.size() != distribution.sample_count ||
        !std::isfinite(distribution.mean) || distribution.mean < 0.0 ||
        !std::isfinite(distribution.p50) || !std::isfinite(distribution.p90) ||
        !std::isfinite(distribution.uncertainty) ||
        distribution.uncertainty < 0.0 || distribution.uncertainty > 1.0)
        return out;
    std::size_t lethal_outcomes = 0;
    for (const double damage : distribution.observed_damage_samples) {
        if (!std::isfinite(damage) || damage < 0.0) return out;
        if (damage >= observed_hp) ++lethal_outcomes;
    }
    out.available = true;
    out.expected_damage = distribution.mean;
    out.elimination_risk = static_cast<double>(lethal_outcomes) /
        static_cast<double>(distribution.sample_count);
    out.source = "observed_hp+calibrated_damage_distribution.v1";
    return out;
}

inline bool apply_to_economic_context(
    const SurvivalRiskEvidence& risk, strategy::StrategicSharedContext& context) {
    if (!risk.available || !std::isfinite(risk.expected_damage) ||
        !std::isfinite(risk.elimination_risk) || risk.expected_damage < 0.0 ||
        risk.elimination_risk < 0.0 || risk.elimination_risk > 1.0)
        return false;
    context.estimated_incoming_damage = risk.expected_damage;
    context.elimination_risk = risk.elimination_risk;
    context.evidence.estimated_incoming_damage = true;
    context.evidence.elimination_risk = true;
    return true;
}

} // namespace tft::combat_evidence
