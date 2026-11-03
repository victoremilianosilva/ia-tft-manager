#pragma once

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>

#include "strategy/PositioningEngine.hpp"

namespace tft::strategy {

struct BenchUnitProfile {
    int role{-1};
    int star{1};
};

struct BoardUnitProfile {
    int champion_id{-1};
    int role{-1};
    int star{1};
    int cost{1};
    std::vector<std::string> traits;
};

struct StrategicBoardContext {
    int level{1};
    std::string direction;
    std::vector<std::pair<std::string, double>> focus_weights;
    std::vector<std::int32_t> core_unit_ids;
    std::vector<std::int32_t> planned_unit_ids;
    std::vector<std::string> core_traits;
    std::vector<std::string> planned_traits;
    std::unordered_map<std::string, std::vector<int>> trait_milestones;
};

struct BoardEvaluationResult {
    double positional_score{0.0};
    double structural_score{0.0};
    double synergy_score{0.0};
    double total_score{0.0};
    int unit_count{0};
    int frontline_count{0};
    int frontline_lane_count{0};
    int carry_count{0};
    int exposed_carry_count{0};
    int main_carry_count{0};
    int exposed_main_carry_count{0};
    int fragile_frontline_count{0};
    int isolated_frontline_count{0};
    int important_bench_units_unplayed{0};
    bool specialized_assassin_board{false};
    double strategic_fit_score{0.0};
    double unit_quality_score{0.0};
    double trait_coherence_score{0.0};
    int active_trait_count{0};
    int missing_frontline_count{0};
    int missing_backline_count{0};
};

class BoardEvaluation {
public:
    using Roles = std::vector<int>;
    static constexpr double kSynergyWeight = 0.20;

    // main_carry_positions are row-major board slots identified by the
    // composition strategy. If empty, all carries still receive generic safety
    // evaluation; no specific unit is arbitrarily assumed to be the carry.
    static BoardEvaluationResult evaluate(
        const Roles& board,
        const std::vector<BenchUnitProfile>& bench = {},
        double active_synergy_score = 0.0,
        const std::vector<int>& main_carry_positions = {},
        const std::vector<BoardUnitProfile>& unit_profiles = {},
        const StrategicBoardContext& context = {}) {
        BoardEvaluationResult result{};
        const int slots = std::min(static_cast<int>(board.size()), PositioningEngine::size);
        Roles normalized(PositioningEngine::size, -1);
        std::vector<bool> main_carry(PositioningEngine::size, false);
        std::vector<bool> frontline_columns(PositioningEngine::cols, false);
        for (const int p : main_carry_positions)
            if (PositioningEngine::is_valid_position(p))
                main_carry[static_cast<std::size_t>(p)] = true;

        for (int p = 0; p < slots; ++p) {
            const int role = board[static_cast<std::size_t>(p)];
            if (role < PositioningEngine::tank || role > PositioningEngine::assassin) continue;
            normalized[static_cast<std::size_t>(p)] = role;
            ++result.unit_count;
            if (role == PositioningEngine::tank || role == PositioningEngine::fighter) {
                ++result.frontline_count;
                const int row = p / PositioningEngine::cols;
                const int col = p % PositioningEngine::cols;
                if (row <= 1) frontline_columns[static_cast<std::size_t>(col)] = true;
            }
            if (role == PositioningEngine::carry) ++result.carry_count;
        }
        for (const bool occupied_lane : frontline_columns)
            if (occupied_lane) ++result.frontline_lane_count;
        if (result.unit_count == 0) return result;

        int assassins = 0;
        for (int role : normalized)
            if (role == PositioningEngine::assassin) ++assassins;
        result.specialized_assassin_board =
            assassins >= 2 && assassins * 2 >= result.unit_count;

        result.positional_score =
            PositioningEngine::get_normalized_positioning_score(normalized);

        double penalty = 0.0;
        double bonus = 0.0;
        if (result.frontline_count == 0) {
            penalty += result.specialized_assassin_board ? 0.10 : 0.45;
        } else if (result.frontline_count == 1 && result.unit_count >= 4) {
            penalty += 0.10;
        }
        if (result.frontline_count > 0 && result.frontline_lane_count == 0) {
            penalty += 0.25;
        } else if (result.frontline_lane_count == 1 && result.unit_count >= 4) {
            penalty += 0.08;
        } else if (result.frontline_lane_count >= 2) {
            // A spread frontline can absorb pressure better than a single stack.
            bonus += 0.04;
        }

        for (int p = 0; p < PositioningEngine::size; ++p) {
            const int role = normalized[static_cast<std::size_t>(p)];
            if (role < 0) continue;
            const int row = p / PositioningEngine::cols;
            int occupied_neighbors = 0;
            int tank_neighbors = 0;
            int tanks_in_front = 0;
            int fighter_neighbors = 0;
            int fighters_in_front = 0;
            for (const int neighbor : PositioningEngine::get_neighbors(p, true)) {
                const int neighbor_role = normalized[static_cast<std::size_t>(neighbor)];
                if (neighbor_role < 0) continue;
                ++occupied_neighbors;
                const int neighbor_row = neighbor / PositioningEngine::cols;
                if (neighbor_role == PositioningEngine::tank) {
                    ++tank_neighbors;
                    if (neighbor_row < row) ++tanks_in_front;
                } else if (neighbor_role == PositioningEngine::fighter) {
                    ++fighter_neighbors;
                    if (neighbor_row < row) ++fighters_in_front;
                }
            }

            if (role == PositioningEngine::carry) {
                // Fighters are legitimate frontline bodies, but provide less
                // protection than tanks. Counting only tanks left carries marked
                // exposed even when a fighter was directly in front of them.
                const double protection = std::min(
                    1.0, occupied_neighbors * 0.03 + tank_neighbors * 0.25 +
                        tanks_in_front * 0.25 + fighter_neighbors * 0.16 +
                        fighters_in_front * 0.16);
                if (protection < 0.35) {
                    ++result.exposed_carry_count;
                    penalty += 0.18 * (0.35 - protection) / 0.35;
                }
                if (row == 0) {
                    penalty += result.specialized_assassin_board ? 0.04 : 0.16;
                    ++result.fragile_frontline_count;
                }
                if (main_carry[static_cast<std::size_t>(p)]) {
                    ++result.main_carry_count;
                    if (row <= 1) penalty += 0.18;
                    else bonus += 0.04;
                    if (protection >= 0.35 &&
                        (tanks_in_front > 0 || fighters_in_front > 0)) {
                        bonus += tanks_in_front > 0 ? 0.16 : 0.08;
                    } else {
                        ++result.exposed_main_carry_count;
                        penalty += 0.22;
                    }
                }
            } else if (role == PositioningEngine::support && row == 0) {
                penalty += 0.10;
                ++result.fragile_frontline_count;
            }

            if ((role == PositioningEngine::tank || role == PositioningEngine::fighter) &&
                row == 0 && occupied_neighbors == 0) {
                ++result.isolated_frontline_count;
                penalty += role == PositioningEngine::tank ? 0.12 : 0.08;
            }
        }

        // Reward deploying useful bench units only when a slot is actually free.
        const int free_slots = PositioningEngine::size - result.unit_count;
        if (free_slots > 0) {
            bool board_has_tank = false, board_has_carry = false;
            for (int role : normalized) {
                board_has_tank |= role == PositioningEngine::tank;
                board_has_carry |= role == PositioningEngine::carry;
            }
            for (const auto& unit : bench) {
                if (unit.role < PositioningEngine::tank ||
                    unit.role > PositioningEngine::assassin) continue;
                const bool fills_gap =
                    (unit.role == PositioningEngine::tank && !board_has_tank) ||
                    (unit.role == PositioningEngine::carry && !board_has_carry);
                if (unit.star >= 2 || fills_gap) {
                    ++result.important_bench_units_unplayed;
                    penalty += 0.06;
                    if (result.important_bench_units_unplayed >= free_slots) break;
                }
            }
        }

        // Bounded lineup-level evaluation: role coverage, unit investment,
        // trait milestones and fit with the active composition.
        int carries = 0, backliners = 0, supports = 0, tanks = 0, fighters = 0;
        std::unordered_set<int> seen_champions;
        std::unordered_map<std::string, int> trait_counts;
        std::unordered_map<std::string, double> focus;
        for (const auto& [trait, weight] : context.focus_weights)
            if (!trait.empty() && std::isfinite(weight)) focus[trait] = std::max(0.0, weight);
        const double maturity = std::clamp((std::clamp(context.level, 1, 10) - 2.0) / 6.0, 0.0, 1.0);
        for (std::size_t slot = 0; slot < unit_profiles.size() &&
             slot < static_cast<std::size_t>(slots); ++slot) {
            const auto& unit = unit_profiles[slot];
            if (unit.champion_id < 0 || normalized[slot] < 0) continue;
            const int role = normalized[slot];
            carries += role == PositioningEngine::carry;
            supports += role == PositioningEngine::support;
            tanks += role == PositioningEngine::tank;
            fighters += role == PositioningEngine::fighter;
            backliners += role == PositioningEngine::carry ||
                role == PositioningEngine::support || role == PositioningEngine::assassin;
            if (!seen_champions.insert(unit.champion_id).second) continue;
            for (const auto& trait : unit.traits) if (!trait.empty()) ++trait_counts[trait];
            result.unit_quality_score +=
                (std::clamp(unit.star, 1, 3) - 1) * 0.16 +
                std::clamp(unit.cost, 1, 5) * 0.035;
            const bool core = std::find(context.core_unit_ids.begin(),
                context.core_unit_ids.end(), unit.champion_id) != context.core_unit_ids.end();
            const bool planned = std::find(context.planned_unit_ids.begin(),
                context.planned_unit_ids.end(), unit.champion_id) != context.planned_unit_ids.end();
            if (core) result.strategic_fit_score += 0.22;
            else if (planned) result.strategic_fit_score += 0.14;
            else if (!context.direction.empty()) result.strategic_fit_score -= 0.025;
        }
        const int frontline = tanks + fighters;
        const int expected_frontline = result.specialized_assassin_board ? 0 : (result.unit_count >= 6 ? 2 : 1);
        if (frontline < expected_frontline) {
            result.missing_frontline_count = expected_frontline - frontline;
            penalty += maturity * 0.12 * result.missing_frontline_count;
        }
        if (result.unit_count >= 4 && backliners == 0) {
            result.missing_backline_count = 1;
            penalty += maturity * 0.10;
        }
        if (result.unit_count >= 5 && carries == 0) penalty += maturity * 0.10;
        if (result.unit_count >= 6 && carries > 2)
            penalty += maturity * 0.035 * (carries - 2);
        if (supports > 0 && frontline == 0 && !result.specialized_assassin_board)
            penalty += maturity * 0.04;

        for (const auto& [trait, count] : trait_counts) {
            const auto found = context.trait_milestones.find(trait);
            if (found == context.trait_milestones.end() || found->second.empty()) continue;
            int reached = 0, next = 0;
            for (const int milestone : found->second) {
                if (milestone > 0 && count >= milestone) ++reached;
                else if (milestone > count && (next == 0 || milestone < next)) next = milestone;
            }
            if (reached > 0) ++result.active_trait_count;
            const double progress = next > 0
                ? std::clamp(static_cast<double>(count) / next, 0.0, 1.0) : 1.0;
            const bool aligned = trait == context.direction ||
                std::find(context.core_traits.begin(), context.core_traits.end(), trait) != context.core_traits.end() ||
                std::find(context.planned_traits.begin(), context.planned_traits.end(), trait) != context.planned_traits.end() ||
                focus.count(trait) != 0;
            result.trait_coherence_score +=
                (reached > 0 ? 0.035 : 0.012 * progress) * (aligned ? 1.35 : 1.0);
        }
        result.trait_coherence_score = std::min(0.16, result.trait_coherence_score);
        result.strategic_fit_score = std::clamp(result.strategic_fit_score, -0.20, 0.45);
        result.unit_quality_score = std::min(0.28, result.unit_quality_score * 0.18);
        bonus += result.trait_coherence_score + result.unit_quality_score +
            result.strategic_fit_score * (0.35 + 0.65 * maturity);

        result.structural_score = bonus - penalty;
        result.synergy_score = std::max(0.0, active_synergy_score);
        result.total_score = result.positional_score + result.structural_score +
            kSynergyWeight * std::tanh(result.synergy_score);
        return result;
    }

    static double improvement(const BoardEvaluationResult& before,
                              const BoardEvaluationResult& after) noexcept {
        return after.total_score - before.total_score;
    }
};

} // namespace tft::strategy
