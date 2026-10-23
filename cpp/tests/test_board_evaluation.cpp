#include "strategy/BoardEvaluation.hpp"

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

namespace {
void require(bool condition, const std::string& message) {
    if (!condition) {
        std::cerr << "[FAIL] " << message << '\n';
        std::exit(EXIT_FAILURE);
    }
}
}

int main() {
    using tft::strategy::BoardEvaluation;
    using tft::strategy::BenchUnitProfile;
    using Roles = BoardEvaluation::Roles;
    using PE = tft::PositioningEngine;

    // Same carry: a tank in front and adjacent improves safety.
    Roles exposed(PE::size, -1);
    exposed[3 * PE::cols + 3] = PE::carry;
    Roles protected_board = exposed;
    protected_board[2 * PE::cols + 3] = PE::tank;
    const auto exposed_eval = BoardEvaluation::evaluate(exposed, {}, 0.0, {24});
    const auto protected_eval = BoardEvaluation::evaluate(protected_board, {}, 0.0, {24});
    require(protected_eval.exposed_carry_count == 0,
            "adjacent tank in front should remove generic exposed-carry signal");
    require(protected_eval.exposed_main_carry_count == 0,
            "main carry should be marked protected by an adjacent tank in front");
    require(protected_eval.total_score > exposed_eval.total_score,
            "protected main carry should score above exposed main carry");

    // Role separation: tanks prefer the front, carries prefer the back.
    Roles roles(PE::size, -1);
    roles[3 * PE::cols + 3] = PE::tank;
    roles[0 * PE::cols + 3] = PE::carry;
    Roles improved_roles(PE::size, -1);
    improved_roles[0 * PE::cols + 3] = PE::tank;
    improved_roles[3 * PE::cols + 3] = PE::carry;
    require(BoardEvaluation::evaluate(improved_roles).total_score >
            BoardEvaluation::evaluate(roles).total_score,
            "moving tank forward and carry backward should improve board quality");

    // Frontline distribution: two lanes beat a single isolated lane for a larger board.
    Roles narrow_frontline(PE::size, -1);
    narrow_frontline[0] = PE::tank;
    narrow_frontline[21] = PE::carry;
    narrow_frontline[22] = PE::support;
    Roles spread_frontline = narrow_frontline;
    spread_frontline[6] = PE::fighter;
    require(BoardEvaluation::evaluate(spread_frontline).total_score >
            BoardEvaluation::evaluate(narrow_frontline).total_score,
            "spreading frontline across lanes should improve board quality");

    // Stable context: a positioning improvement with unchanged synergy is positive.
    const auto before = BoardEvaluation::evaluate(exposed, {}, 2.0, {24});
    const auto after = BoardEvaluation::evaluate(protected_board, {}, 2.0, {24});
    require(BoardEvaluation::improvement(before, after) > 0.0,
            "protection improvement with unchanged synergy should be positive");

    // Losing important synergy must be visible in the same combined score.
    const auto synergy_before = BoardEvaluation::evaluate(exposed, {}, 4.0, {24});
    const auto synergy_after = BoardEvaluation::evaluate(protected_board, {}, 0.0, {24});
    require(BoardEvaluation::improvement(synergy_before, synergy_after) <
            BoardEvaluation::improvement(before, after),
            "synergy loss must be visible in the combined board evaluation");

    // Assassin-focused boards are not forced to have a conventional tank.
    Roles specialist(PE::size, -1);
    specialist[8] = PE::assassin;
    specialist[10] = PE::assassin;
    specialist[17] = PE::carry;
    const auto specialist_eval = BoardEvaluation::evaluate(specialist);
    require(specialist_eval.specialized_assassin_board,
            "assassin-heavy formation should be recognized as specialized");
    require(specialist_eval.structural_score > -0.45,
            "specialized formation should avoid the generic no-frontline penalty");

    // A neutral move has zero delta, so the reward path can apply no-progress cost.
    const auto same_a = BoardEvaluation::evaluate(protected_board, {}, 1.0, {24});
    const auto same_b = BoardEvaluation::evaluate(protected_board, {}, 1.0, {24});
    require(std::abs(BoardEvaluation::improvement(same_a, same_b)) < 1e-12,
            "unchanged board should have exactly zero evaluation delta");

    // Main-carry preference only applies to the designated slot.
    Roles two_carries(PE::size, -1);
    two_carries[3 * PE::cols + 1] = PE::carry;
    two_carries[3 * PE::cols + 5] = PE::carry;
    two_carries[2 * PE::cols + 1] = PE::tank;
    const auto main_left = BoardEvaluation::evaluate(two_carries, {}, 0.0, {22});
    const auto main_right = BoardEvaluation::evaluate(two_carries, {}, 0.0, {26});
    require(main_left.total_score != main_right.total_score,
            "moving main-carry designation should change which carry is protected as priority");

    // High-value bench units are only penalized when board capacity is free.
    const auto bench_signal = BoardEvaluation::evaluate(
        improved_roles, {BenchUnitProfile{PE::carry, 2}}, 0.0);
    require(bench_signal.important_bench_units_unplayed == 1,
            "high-value bench unit should be signaled when board has free capacity");
    Roles full_board(PE::size, PE::fighter);
    const auto full_eval = BoardEvaluation::evaluate(
        full_board, {BenchUnitProfile{PE::carry, 2}}, 0.0);
    require(full_eval.important_bench_units_unplayed == 0,
            "bench penalty must not apply when board is full");

    // Candidate position/swap APIs must compare whole-board deltas.
    Roles position_candidates(PE::size, -1);
    position_candidates[21] = PE::tank;
    const auto best_carry = PE::find_best_position(position_candidates, PE::carry);
    require(best_carry.first >= 0 && best_carry.second > 0.0,
            "best-position search should find a positive whole-board placement gain");

    std::cout << "[PASS] Tactical board evaluation and directional delta scenarios.\n";
    return EXIT_SUCCESS;
}
