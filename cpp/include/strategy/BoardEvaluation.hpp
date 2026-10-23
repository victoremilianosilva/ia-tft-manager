#pragma once

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <vector>

#include "strategy/PositioningEngine.hpp"

namespace tft::strategy {

struct BenchUnitProfile {
    int role{-1};
    int star{1};
};

struct BoardEvaluationResult {
    double positional_score{0.0};
    double structural_score{0.0};
    double synergy_score{0.0};
    double total_score{0.0};
    int unit_count{0};
    int frontline_count{0};
    int carry_count{0};
    int exposed_carry_count{0};
    int fragile_frontline_count{0};
    int isolated_frontline_count{0};
    int important_bench_units_unplayed{0};
    bool specialized_assassin_board{false};
};

class BoardEvaluation {
public:
    using Roles = std::vector<int>;
    static constexpr double kSynergyWeight = 0.20;

    // Roles use PositioningEngine's stable role ids: tank=0, carry=1,
    // support=2, fighter=3, assassin=4. Empty slots are -1.
    // This is a soft evaluator: no single formation is mandatory, and an
    // assassin-heavy board reduces the generic frontline expectation.
    static BoardEvaluationResult evaluate(
        const Roles& board,
        const std::vector<BenchUnitProfile>& bench = {},
        double active_synergy_score = 0.0
    ) {
        BoardEvaluationResult result{};
        const int slots = std::min(static_cast<int>(board.size()),
                                   PositioningEngine::size);
        Roles normalized(PositioningEngine::size, -1);
        for (int p = 0; p < slots; ++p) {
            const int role = board[static_cast<std::size_t>(p)];
            if (role >= PositioningEngine::tank &&
                role <= PositioningEngine::assassin) {
                normalized[static_cast<std::size_t>(p)] = role;
                ++result.unit_count;
                if (role == PositioningEngine::tank ||
                    role == PositioningEngine::fighter) ++result.frontline_count;
                if (role == PositioningEngine::carry) ++result.carry_count;
            }
        }
        if (result.unit_count == 0) return result;

        int assassins = 0;
        for (int role : normalized)
            if (role == PositioningEngine::assassin) ++assassins;
        result.specialized_assassin_board =
            assassins >= 2 && assassins * 2 >= result.unit_count;

        result.positional_score =
            PositioningEngine::get_normalized_positioning_score(normalized);

        double penalty = 0.0;
        // Lack of conventional frontline is a signal, not a hard prohibition.
        // Assassin-focused boards can intentionally trade frontline for access.
        if (result.frontline_count == 0) {
            penalty += result.specialized_assassin_board ? 0.10 : 0.55;
        } else if (result.frontline_count == 1 && result.unit_count >= 4) {
            penalty += 0.12;
        }

        for (int p = 0; p < PositioningEngine::size; ++p) {
            const int role = normalized[static_cast<std::size_t>(p)];
            if (role < 0) continue;
            const int row = p / PositioningEngine::cols;
            int occupied_neighbors = 0;
            int tank_neighbors = 0;
            for (const int neighbor : PositioningEngine::get_neighbors(p, true)) {
                const int neighbor_role = normalized[static_cast<std::size_t>(neighbor)];
                if (neighbor_role < 0) continue;
                ++occupied_neighbors;
                if (neighbor_role == PositioningEngine::tank) ++tank_neighbors;
            }

            if (role == PositioningEngine::carry) {
                const double protection = std::min(
                    1.0, occupied_neighbors * 0.20 + tank_neighbors * 0.35);
                if (protection < 0.35) {
                    ++result.exposed_carry_count;
                    penalty += 0.30 * (0.35 - protection) / 0.35;
                }
                if (row == 0) {
                    // Only penalize fragile carries at the front; the scale is
                    // reduced for a specialist board rather than forbidding it.
                    penalty += result.specialized_assassin_board ? 0.04 : 0.18;
                    ++result.fragile_frontline_count;
                }
            } else if (role == PositioningEngine::support && row == 0) {
                penalty += 0.12;
                ++result.fragile_frontline_count;
            }

            if ((role == PositioningEngine::tank || role == PositioningEngine::fighter) &&
                row == 0 && occupied_neighbors == 0) {
                ++result.isolated_frontline_count;
                penalty += role == PositioningEngine::tank ? 0.14 : 0.10;
            }
        }

        // Reward deploying useful bench units only when a slot is actually free.
        // A role is "important" here only if it is a 2+ star unit or fills a
        // missing tank/carry role; this avoids requiring every bench unit on board.
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

        result.structural_score = -penalty;
        result.synergy_score = std::max(0.0, active_synergy_score);
        // Normalize the synergy contribution so it is a modest context signal,
        // not a replacement for the separate synergy reward or combat results.
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
