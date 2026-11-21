#pragma once

#include "combat/CombatEvidence.hpp"
#include "combat/CombatEngine.hpp"

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <string>
#include <unordered_set>
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
        if (input.context != CombatContext::PVP ||
            input.player_a.team != UnitTeam::PLAYER_A ||
            input.player_b.team != UnitTeam::PLAYER_B ||
            input.player_a.player_id != identity.player_id ||
            input.player_b.player_id != identity.opponent_id) {
            out.validation_reason = "combat_input_matchup_identity_mismatch";
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
                if (unit.id < 0 || unit.api_name.empty() ||
                    unit.source_unit_uuid.empty() ||
                    unit.source_unit_uuid != expected_uuids[index] ||
                    !source_uuids.insert(unit.source_unit_uuid).second ||
                    unit.source_board_position < 0 || unit.source_board_position >= 28 ||
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

    static constexpr std::uint32_t kMaximumScenarios = 32;
};

} // namespace tft::combat_evidence
