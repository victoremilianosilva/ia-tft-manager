#pragma once

#include "composition_intelligence/StrategicActionExecutor.hpp"

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <nlohmann/json.hpp>

namespace tft::composition_intelligence {

enum class StrategicPositionRole : std::uint8_t {
    Unknown = 0, Frontline = 1, MainCarry = 2, SecondaryCarry = 3,
    Support = 4, Flex = 5
};

enum class StrategicPositionZone : std::uint8_t { Bench = 0, Board = 1 };

struct StrategicPositionUnit {
    std::int32_t champion_id{-1};
    StrategicPositionRole role{StrategicPositionRole::Unknown};
    std::int32_t priority{0};
};

struct StrategicPositionSnapshot {
    std::uint32_t schema_version{1};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    std::string composition_id;
    std::uint64_t composition_version{0};
    bool alive{false};
    std::array<std::int32_t, decision::BOARD_SIZE> board_ids{};
    std::array<std::int32_t, decision::BENCH_SIZE> bench_ids{};
    PlayerActionMasks masks{};
    std::vector<StrategicPositionUnit> composition_units;
};

struct StrategicPositionProposal {
    std::uint32_t schema_version{1};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    std::string composition_id;
    std::uint64_t composition_version{0};
    std::int32_t champion_id{-1};
    StrategicPositionRole role{StrategicPositionRole::Unknown};
    StrategicPositionZone source_zone{StrategicPositionZone::Bench};
    std::int32_t source_slot{-1};
    std::int32_t target_board_slot{-1};
    double current_position_score{0.0};
    double target_position_score{0.0};
    double improvement{0.0};
    std::string reason;
    std::string status{"no_positioning_proposal"};

    nlohmann::json to_json() const {
        return {
            {"schema_version", schema_version},
            {"identity", {{"match_id", match_id}, {"player_id", player_id},
                {"round", round}, {"sequence", sequence},
                {"composition_id", composition_id},
                {"composition_version", composition_version}}},
            {"unit", {{"champion_id", champion_id}, {"role", static_cast<int>(role)}}},
            {"source", {{"zone", source_zone == StrategicPositionZone::Bench ? "bench" : "board"},
                {"slot", source_slot}}},
            {"target", {{"zone", "board"}, {"slot", target_board_slot}}},
            {"score", {{"current", current_position_score},
                {"target", target_position_score}, {"improvement", improvement}}},
            {"reason", reason}, {"status", status}
        };
    }

    bool available() const noexcept {
        return status == "positioning_proposal_available" &&
            champion_id >= 0 && source_slot >= 0 && target_board_slot >= 0;
    }
};

// Deterministic, read-only placement proposal generator. It never mutates the
// snapshot, legality masks, engine, action queue, or game state.
class StrategicPositionPlanner {
public:
    StrategicPositionProposal plan(const StrategicPositionSnapshot& snapshot) const {
        StrategicPositionProposal out;
        out.match_id = snapshot.match_id;
        out.player_id = snapshot.player_id;
        out.round = snapshot.round;
        out.sequence = snapshot.sequence;
        out.composition_id = snapshot.composition_id;
        out.composition_version = snapshot.composition_version;

        if (snapshot.schema_version != 1 || snapshot.match_id == 0 ||
            snapshot.player_id < 0 || snapshot.sequence == 0 ||
            snapshot.composition_id.empty() || snapshot.composition_version == 0) {
            out.reason = "positioning_snapshot_identity_or_schema_invalid";
            return out;
        }
        if (!snapshot.alive) {
            out.reason = "player_not_alive";
            return out;
        }

        std::unordered_map<std::int32_t, StrategicPositionUnit> roles;
        for (const auto& unit : snapshot.composition_units) {
            if (unit.champion_id < 0 || unit.role == StrategicPositionRole::Unknown) continue;
            roles.emplace(unit.champion_id, unit);
        }
        if (roles.empty()) {
            out.reason = "no_role_evidence_for_active_composition";
            return out;
        }

        // The current native snapshot identifies champion IDs, not unique
        // instance UUIDs. Refuse duplicate copies instead of guessing a source.
        std::unordered_map<std::int32_t, std::pair<StrategicPositionZone, std::int32_t>> owned;
        std::unordered_set<std::int32_t> ambiguous;
        for (std::size_t slot = 0; slot < snapshot.board_ids.size(); ++slot) {
            const auto id = snapshot.board_ids[slot];
            if (id < 0) continue;
            if (!owned.emplace(id, std::make_pair(StrategicPositionZone::Board,
                    static_cast<std::int32_t>(slot))).second) ambiguous.insert(id);
        }
        for (std::size_t slot = 0; slot < snapshot.bench_ids.size(); ++slot) {
            const auto id = snapshot.bench_ids[slot];
            if (id < 0) continue;
            if (!owned.emplace(id, std::make_pair(StrategicPositionZone::Bench,
                    static_cast<std::int32_t>(slot))).second) ambiguous.insert(id);
        }

        bool found = false;
        double best_score = -1.0e9;
        std::int32_t best_priority = -1;
        for (const auto& [champion_id, role] : roles) {
            const auto source = owned.find(champion_id);
            if (source == owned.end() || ambiguous.count(champion_id)) continue;
            const auto zone = source->second.first;
            const auto source_slot = source->second.second;
            const auto current_score = zone == StrategicPositionZone::Board
                ? score_position(role.role, source_slot, snapshot.board_ids, champion_id)
                : 0.0;

            for (std::size_t target = 0; target < snapshot.board_ids.size(); ++target) {
                if (snapshot.board_ids[target] >= 0) continue; // no implicit swaps
                bool legal = false;
                if (zone == StrategicPositionZone::Bench) {
                    legal = snapshot.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BENCH)] == decision::MASK_ENABLED &&
                        snapshot.masks.bench_move_source_mask[static_cast<std::size_t>(source_slot)] == decision::MASK_ENABLED &&
                        snapshot.masks.bench_to_board_target_masks[
                            static_cast<std::size_t>(source_slot) * decision::BOARD_SIZE + target] == decision::MASK_ENABLED;
                } else {
                    legal = snapshot.masks.type_mask[static_cast<std::size_t>(decision::ActionType::MOVE_BOARD)] == decision::MASK_ENABLED &&
                        snapshot.masks.board_source_mask[static_cast<std::size_t>(source_slot)] == decision::MASK_ENABLED &&
                        snapshot.masks.board_move_target_masks[
                            static_cast<std::size_t>(source_slot) * decision::BOARD_SIZE + target] == decision::MASK_ENABLED;
                }
                if (!legal) continue;

                const auto target_score = score_position(role.role,
                    static_cast<std::int32_t>(target), snapshot.board_ids, champion_id);
                const auto improvement = zone == StrategicPositionZone::Board
                    ? target_score - current_score : target_score;
                if (zone == StrategicPositionZone::Board && improvement < minimum_improvement_)
                    continue;
                const auto total = target_score + (role.priority * 0.001);
                if (!found || total > best_score ||
                    (total == best_score && (source_slot < out.source_slot ||
                     (source_slot == out.source_slot && static_cast<std::int32_t>(target) < out.target_board_slot)))) {
                    found = true;
                    best_score = total;
                    best_priority = role.priority;
                    out.champion_id = champion_id;
                    out.role = role.role;
                    out.source_zone = zone;
                    out.source_slot = source_slot;
                    out.target_board_slot = static_cast<std::int32_t>(target);
                    out.current_position_score = current_score;
                    out.target_position_score = target_score;
                    out.improvement = improvement;
                    out.reason = reason_for(role.role, zone, improvement);
                    out.status = "positioning_proposal_available";
                }
            }
        }
        if (!found) {
            out.reason = "no_empty_destination_with_positive_role_fit_and_current_native_legality";
            return out;
        }
        (void)best_priority;
        return out;
    }

private:
    static constexpr double minimum_improvement_ = 1.0;

    static double score_position(StrategicPositionRole role, std::int32_t slot,
                                 const std::array<std::int32_t, decision::BOARD_SIZE>& board,
                                 std::int32_t moving_id) {
        if (slot < 0 || slot >= static_cast<std::int32_t>(decision::BOARD_SIZE)) return -1000.0;
        const auto row = slot / 7;
        const auto column = slot % 7;
        const auto centrality = 10.0 - (std::abs(column - 3) * 2.0);
        double row_score = 0.0;
        switch (role) {
            case StrategicPositionRole::Frontline:
                row_score = row == 1 ? 100.0 : row == 0 ? 70.0 : row == 2 ? 20.0 : 0.0;
                break;
            case StrategicPositionRole::MainCarry:
            case StrategicPositionRole::SecondaryCarry:
                row_score = row == 3 ? 100.0 : row == 2 ? 65.0 : row == 1 ? 15.0 : 0.0;
                break;
            case StrategicPositionRole::Support:
                row_score = row == 2 ? 85.0 : row == 3 ? 65.0 : row == 1 ? 35.0 : 10.0;
                break;
            case StrategicPositionRole::Flex:
                row_score = row == 2 ? 75.0 : row == 1 ? 65.0 : row == 3 ? 55.0 : 35.0;
                break;
            case StrategicPositionRole::Unknown:
                return -1000.0;
        }
        double protection = 0.0;
        if (role == StrategicPositionRole::MainCarry ||
            role == StrategicPositionRole::SecondaryCarry) {
            std::size_t frontline = 0;
            for (std::size_t i = 0; i < board.size(); ++i) {
                if (board[i] < 0 || board[i] == moving_id) continue;
                const auto occupied_row = static_cast<int>(i / 7);
                if (occupied_row <= 1) ++frontline;
            }
            protection = frontline > 0 ? 12.0 : -8.0;
        }
        return row_score + centrality + protection;
    }

    static std::string reason_for(StrategicPositionRole role,
                                  StrategicPositionZone zone, double improvement) {
        const std::string origin = zone == StrategicPositionZone::Bench
            ? "deploy_from_bench" : "reposition_on_board";
        const std::string role_reason = role == StrategicPositionRole::Frontline
            ? "frontline_role_fit" :
            (role == StrategicPositionRole::MainCarry || role == StrategicPositionRole::SecondaryCarry)
                ? "carry_backline_and_protection_fit" :
            role == StrategicPositionRole::Support ? "support_position_fit" : "flex_position_fit";
        return origin + ":" + role_reason + ":score_delta=" + std::to_string(improvement);
    }
};

} // namespace tft::composition_intelligence
