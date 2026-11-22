#pragma once

#include "combat/CombatEvidence.hpp"
#include "combat/CombatEngine.hpp"

#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <limits>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

namespace tft::combat_evidence {

struct CombatProjectionSnapshot {
    CombatSnapshot identity;
    CombatInput input;
    CombatCoverage coverage;
    bool valid{false};
    std::string validation_reason{"not_built"};
};

class CombatProjectionSnapshotBuilder {
public:
    CombatProjectionSnapshot build(
        const CombatSnapshot& identity,
        const CombatInput& input,
        std::uint64_t expected_strategic_sequence = 0) const {
        CombatProjectionSnapshot out;
        out.identity = identity;
        out.input = input;
        const auto identity_validation =
            CombatSnapshotBuilder{}.validate(identity, expected_strategic_sequence);
        if (!identity_validation.valid) {
            out.validation_reason = identity_validation.reason;
            return out;
        }
        const auto hp_matches = [](double input_hp, double snapshot_hp) {
            return std::isfinite(input_hp) && input_hp >= 0.0 &&
                std::abs(input_hp - snapshot_hp) <= 1e-6;
        };
        if (input.context != CombatContext::PVP ||
            input.player_a.team != UnitTeam::PLAYER_A ||
            input.player_b.team != UnitTeam::PLAYER_B ||
            input.player_a.player_id != identity.player_id ||
            input.player_b.player_id != identity.opponent_id ||
            !hp_matches(input.player_a.player_hp, identity.player_hp) ||
            !hp_matches(input.player_b.player_hp, identity.opponent_hp)) {
            out.validation_reason = "combat_input_matchup_or_hp_identity_mismatch";
            return out;
        }
        if (input.seed != input.config.seed || !input.config.deterministic ||
            input.config.board_rows <= 0 || input.config.board_cols <= 0 ||
            input.config.board_rows * input.config.board_cols != 28 ||
            !std::isfinite(input.config.max_duration) ||
            input.config.max_duration <= 0.0f || input.config.max_events == 0) {
            out.validation_reason = "combat_input_simulator_configuration_invalid";
            return out;
        }
        if (input.player_a.units.size() != identity.player_unit_ids.size() ||
            input.player_b.units.size() != identity.opponent_unit_ids.size()) {
            out.validation_reason = "combat_input_roster_size_mismatch";
            return out;
        }
        const auto valid_team = [](
            const CombatTeam& team, const std::vector<std::string>& expected_uuids) {
            if (team.units.size() != expected_uuids.size()) return false;
            std::unordered_set<int> unit_ids;
            std::unordered_set<int> board_positions;
            std::unordered_set<std::string> source_uuids;
            for (std::size_t index = 0; index < team.units.size(); ++index) {
                const auto& unit = team.units[index];
                const std::array<float, 15> numeric_stats{
                    unit.hp, unit.max_hp, unit.mana, unit.max_mana,
                    unit.attack_damage, unit.ability_power, unit.attack_speed,
                    unit.attack_range, unit.critical_strike_chance,
                    unit.critical_strike_damage, unit.armor, unit.magic_resist,
                    unit.damage_amplification, unit.damage_reduction, unit.omnivamp
                };
                const bool finite_stats = std::all_of(
                    numeric_stats.begin(), numeric_stats.end(),
                    [](float value) { return std::isfinite(value); });
                if (unit.id < 0 || unit.api_name.empty() ||
                    unit.source_unit_uuid.empty() ||
                    unit.source_unit_uuid != expected_uuids[index] ||
                    !source_uuids.insert(unit.source_unit_uuid).second ||
                    unit.source_board_position < 0 || unit.source_board_position >= 28 ||
                    unit.position.x < 0 || unit.position.x >= 7 ||
                    unit.position.y < 0 || unit.position.y >= 4 ||
                    unit.star < 1 || unit.star > 3 ||
                    !finite_stats || unit.hp < 0.0f || unit.max_hp <= 0.0f ||
                    unit.hp > unit.max_hp + 1e-4f || unit.mana < 0.0f ||
                    unit.max_mana < 0.0f || unit.attack_damage < 0.0f ||
                    unit.attack_speed <= 0.0f || unit.attack_range <= 0.0f ||
                    unit.damage_reduction < 0.0f || unit.damage_reduction > 1.0f ||
                    unit.omnivamp < 0.0f || unit.omnivamp > 1.0f ||
                    !unit_ids.insert(unit.id).second ||
                    !board_positions.insert(unit.source_board_position).second)
                    return false;
            }
            return true;
        };
        if (!valid_team(input.player_a, identity.player_unit_ids) ||
            !valid_team(input.player_b, identity.opponent_unit_ids)) {
            out.validation_reason = "combat_input_unit_identity_or_board_position_invalid";
            return out;
        }
        std::unordered_set<int> all_unit_ids;
        for (const auto& unit : input.player_a.units) all_unit_ids.insert(unit.id);
        for (const auto& unit : input.player_b.units) {
            if (!all_unit_ids.insert(unit.id).second) {
                out.validation_reason = "combat_input_unit_id_shared_between_teams";
                return out;
            }
        }
        out.coverage = CombatCoverageValidator{}.inspect(input);
        out.valid = true;
        out.validation_reason = "valid";
        return out;
    }
};

struct WeightedCombatScenario {
    std::int32_t opponent_id{-1};
    std::uint32_t scenario_index{0};
    double incoming_damage{0.0};
    double probability{0.0};
};

struct CombatMatchupProjectionCandidate {
    double probability{0.0};
    CombatProjectionSnapshot snapshot;
};

struct CombatProjectionResult {
    bool simulation_completed{false};
    bool decision_eligible{false}; // always false until replay calibration approves it
    std::string status{"unavailable"};
    std::string reason{"not_projected"};
    std::string simulator_version{"combat-engine-generic.v1"};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::int32_t opponent_id{-1};
    std::uint32_t round{0};
    std::uint64_t strategic_sequence{0};
    std::uint64_t engine_decision_sequence{0};
    std::uint32_t horizon_rounds{1};
    std::uint32_t scenarios_requested{0};
    std::uint32_t scenarios_completed{0};
    double expected_incoming_damage{0.0};
    double p50_incoming_damage{0.0};
    double p90_incoming_damage{0.0};
    double uncertainty{1.0};
    CombatCoverage coverage;
    std::vector<double> incoming_damage_samples;
    std::vector<WeightedCombatScenario> weighted_scenarios;
};

class CombatProjectionEngine {
public:
    CombatProjectionResult project(
        const CombatProjectionSnapshot& snapshot,
        std::int32_t authoritative_round_damage,
        std::uint32_t scenario_count = 1,
        std::uint64_t first_seed = 1) const {
        CombatProjectionResult out;
        out.match_id = snapshot.identity.match_id;
        out.player_id = snapshot.identity.player_id;
        out.opponent_id = snapshot.identity.opponent_id;
        out.round = snapshot.identity.round;
        out.strategic_sequence = snapshot.identity.sequence;
        out.engine_decision_sequence = snapshot.identity.engine_decision_sequence;
        out.coverage = snapshot.coverage;
        out.scenarios_requested = scenario_count;
        if (!snapshot.valid) {
            out.reason = snapshot.validation_reason;
            return out;
        }
        if (authoritative_round_damage < 0 || scenario_count == 0 ||
            scenario_count > kMaximumScenarios || first_seed == 0) {
            out.reason = "invalid_projection_horizon_scenario_or_damage_input";
            return out;
        }

        CombatEngine engine;
        std::vector<double> damage_samples;
        damage_samples.reserve(scenario_count);
        for (std::uint32_t scenario = 0; scenario < scenario_count; ++scenario) {
            CombatInput scenario_input = snapshot.input;
            const std::uint64_t seed = first_seed + scenario;
            if (seed < first_seed) {
                out.reason = "scenario_seed_overflow";
                return out;
            }
            scenario_input.seed = seed;
            scenario_input.config.seed = seed;
            scenario_input.config.deterministic = true;
            const auto result = engine.simulate(scenario_input);
            if (!result.success || !result.completed || result.timeout) {
                out.reason = "combat_engine_scenario_incomplete";
                out.scenarios_completed = static_cast<std::uint32_t>(damage_samples.size());
                return out;
            }
            // TFT player damage is round base damage plus surviving enemy units.
            // Player A is the projection subject; Player B is the actual opponent.
            damage_samples.push_back(static_cast<double>(authoritative_round_damage) +
                static_cast<double>(std::max(0, result.player_b_survivors)));
        }

        std::sort(damage_samples.begin(), damage_samples.end());
        const auto quantile = [&](double q) {
            const auto index = static_cast<std::size_t>(
                std::ceil(q * static_cast<double>(damage_samples.size())) - 1.0);
            return damage_samples[std::min(index, damage_samples.size() - 1)];
        };
        double sum = 0.0;
        for (const double value : damage_samples) sum += value;
        out.expected_incoming_damage = sum / static_cast<double>(damage_samples.size());
        out.p50_incoming_damage = quantile(0.50);
        out.p90_incoming_damage = quantile(0.90);
        out.uncertainty = 1.0 / std::sqrt(static_cast<double>(damage_samples.size()));
        out.incoming_damage_samples = std::move(damage_samples);
        out.scenarios_completed = scenario_count;
        out.simulation_completed = true;
        out.decision_eligible = false;
        const auto coverage = CombatCoverageValidator{}.validate(snapshot.coverage);
        out.status = coverage.complete ? "experimental_uncalibrated" :
            "partial_unsupported_mechanics";
        out.reason = coverage.complete ? "awaiting_replay_calibration" :
            "material_mechanics_not_fully_supported";
        return out;
    }

    CombatProjectionResult project_matchups(
        const std::vector<CombatMatchupProjectionCandidate>& candidates,
        std::int32_t authoritative_round_damage,
        std::uint32_t scenarios_per_matchup = 4,
        std::uint64_t first_seed = 1) const {
        CombatProjectionResult out;
        if (candidates.empty() || candidates.size() > 7 || scenarios_per_matchup == 0 ||
            scenarios_per_matchup > kMaximumScenarios || first_seed == 0 ||
            authoritative_round_damage < 0) {
            out.reason = "matchup_candidates_or_projection_parameters_unavailable";
            return out;
        }

        std::vector<MatchupCandidateProbability> probabilities;
        probabilities.reserve(candidates.size());
        const auto& first = candidates.front().snapshot.identity;
        for (const auto& candidate : candidates) {
            probabilities.push_back({
                candidate.snapshot.identity.opponent_id, candidate.probability});
            const auto& identity = candidate.snapshot.identity;
            if (!candidate.snapshot.valid || identity.match_id != first.match_id ||
                identity.player_id != first.player_id || identity.round != first.round ||
                identity.sequence != first.sequence ||
                identity.engine_decision_sequence != first.engine_decision_sequence ||
                identity.player_hp != first.player_hp ||
                identity.player_unit_ids != first.player_unit_ids) {
                out.reason = "candidate_snapshot_identity_or_player_board_mismatch";
                return out;
            }
        }
        const auto matchup_set =
            MatchupResolver{}.resolve_candidates(first.player_id, probabilities);
        if (!matchup_set.available) {
            out.reason = matchup_set.reason;
            return out;
        }

        out.match_id = first.match_id;
        out.player_id = first.player_id;
        out.opponent_id = -1;
        out.round = first.round;
        out.strategic_sequence = first.sequence;
        out.engine_decision_sequence = first.engine_decision_sequence;
        out.horizon_rounds = 1;
        out.scenarios_requested = static_cast<std::uint32_t>(
            candidates.size() * scenarios_per_matchup);
        double expected_damage = 0.0;
        double simulation_uncertainty = 0.0;
        double matchup_entropy = 0.0;
        bool all_candidate_coverage_complete = true;
        std::vector<WeightedCombatScenario> scenarios;
        scenarios.reserve(out.scenarios_requested);

        for (std::size_t candidate_index = 0;
             candidate_index < candidates.size(); ++candidate_index) {
            const auto seed_offset = static_cast<std::uint64_t>(
                candidate_index * scenarios_per_matchup);
            if (first_seed > std::numeric_limits<std::uint64_t>::max() - seed_offset) {
                out.reason = "scenario_seed_overflow";
                return out;
            }
            const auto& candidate = candidates[candidate_index];
            auto candidate_result = project(
                candidate.snapshot, authoritative_round_damage,
                scenarios_per_matchup, first_seed + seed_offset);
            if (!candidate_result.simulation_completed) {
                out.reason = candidate_result.reason;
                return out;
            }
            const auto& coverage = candidate_result.coverage;
            all_candidate_coverage_complete = all_candidate_coverage_complete &&
                CombatCoverageValidator{}.validate(coverage).complete;
            out.coverage.units_seen += coverage.units_seen;
            out.coverage.units_supported += coverage.units_supported;
            out.coverage.unsupported_abilities += coverage.unsupported_abilities;
            out.coverage.unsupported_traits += coverage.unsupported_traits;
            out.coverage.unsupported_items += coverage.unsupported_items;
            out.coverage.missing_scripts += coverage.missing_scripts;
            out.coverage.unsupported_effects += coverage.unsupported_effects;
            out.coverage.missing_ability_metadata += coverage.missing_ability_metadata;
            out.coverage.missing_item_effect_metadata += coverage.missing_item_effect_metadata;
            out.coverage.missing_trait_effect_metadata += coverage.missing_trait_effect_metadata;
            out.coverage.abilities_seen += coverage.abilities_seen;
            out.coverage.abilities_supported += coverage.abilities_supported;
            out.coverage.items_seen += coverage.items_seen;
            out.coverage.items_supported += coverage.items_supported;
            out.coverage.traits_seen += coverage.traits_seen;
            out.coverage.traits_supported += coverage.traits_supported;
            out.coverage.effects_seen += coverage.effects_seen;
            out.coverage.effects_supported += coverage.effects_supported;
            simulation_uncertainty += candidate.probability * candidate_result.uncertainty;
            for (std::size_t scenario_index = 0;
                 scenario_index < candidate_result.incoming_damage_samples.size();
                 ++scenario_index) {
                const double probability = candidate.probability /
                    static_cast<double>(scenarios_per_matchup);
                const double damage =
                    candidate_result.incoming_damage_samples[scenario_index];
                scenarios.push_back({
                    candidate.snapshot.identity.opponent_id,
                    static_cast<std::uint32_t>(scenario_index),
                    damage, probability});
                expected_damage += probability * damage;
            }
            out.scenarios_completed += candidate_result.scenarios_completed;
        }
        if (candidates.size() > 1) {
            for (const auto& candidate : candidates)
                matchup_entropy -= candidate.probability *
                    std::log(candidate.probability);
            matchup_entropy /= std::log(static_cast<double>(candidates.size()));
        }
        std::sort(scenarios.begin(), scenarios.end(),
            [](const auto& lhs, const auto& rhs) {
                return lhs.incoming_damage < rhs.incoming_damage;
            });
        const auto weighted_quantile = [&](double q) {
            double cumulative = 0.0;
            for (const auto& scenario : scenarios) {
                cumulative += scenario.probability;
                if (cumulative + 1e-12 >= q) return scenario.incoming_damage;
            }
            return scenarios.back().incoming_damage;
        };
        out.expected_incoming_damage = expected_damage;
        out.p50_incoming_damage = weighted_quantile(0.50);
        out.p90_incoming_damage = weighted_quantile(0.90);
        out.uncertainty = std::clamp(
            simulation_uncertainty + matchup_entropy, 0.0, 1.0);
        out.incoming_damage_samples.reserve(scenarios.size());
        for (const auto& scenario : scenarios)
            out.incoming_damage_samples.push_back(scenario.incoming_damage);
        out.weighted_scenarios = std::move(scenarios);
        out.coverage.all_effects_catalogued = all_candidate_coverage_complete;
        const auto coverage = CombatCoverageValidator{}.validate(out.coverage);
        out.simulation_completed = true;
        out.decision_eligible = false;
        out.status = coverage.complete ? "experimental_uncalibrated" :
            "partial_unsupported_mechanics";
        out.reason = coverage.complete ? "awaiting_replay_calibration" :
            "material_mechanics_not_fully_supported";
        return out;
    }

    static constexpr std::uint32_t kMaximumScenarios = 32;
};

} // namespace tft::combat_evidence
