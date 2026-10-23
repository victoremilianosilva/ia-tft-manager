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

    // 1. Same carry: adjacent tank gives a measurable protection gain.
    Roles exposed(PE::size, -1);
    exposed[3 * PE::cols + 3] = PE::carry;
    Roles protected_board = exposed;
    protected_board[2 * PE::cols + 3] = PE::tank;
    const auto exposed_eval = BoardEvaluation::evaluate(exposed);
    const auto protected_eval = BoardEvaluation::evaluate(protected_board);
    require(protected_eval.exposed_carry_count == 0,
            "adjacent tank should remove the exposed-carry signal");
    require(protected_eval.total_score > exposed_eval.total_score,
            "protected carry should score above exposed carry");

    // 2. A functional frontline improves the structure signal.
    Roles no_frontline(PE::size, -1);
    no_frontline[21] = PE::carry;
    no_frontline[22] = PE::support;
    Roles with_frontline = no_frontline;
    with_frontline[14] = PE::tank;
    require(BoardEvaluation::evaluate(with_frontline).total_score >
            BoardEvaluation::evaluate(no_frontline).total_score,
            "functional frontline should improve board quality");

    // 3. Better protection must not require removing the existing synergy score.
    const auto before = BoardEvaluation::evaluate(exposed, {}, 2.0);
    const auto after = BoardEvaluation::evaluate(protected_board, {}, 2.0);
    require(BoardEvaluation::improvement(before, after) > 0.0,
            "protection improvement with unchanged synergy should be positive");

    // 4. A position-only gain can be outweighed by loss of important synergy.
    const auto synergy_before = BoardEvaluation::evaluate(exposed, {}, 4.0);
    const auto synergy_after = BoardEvaluation::evaluate(protected_board, {}, 0.0);
    require(BoardEvaluation::improvement(synergy_before, synergy_after) <
            BoardEvaluation::improvement(before, after),
            "synergy loss must be visible in the combined board evaluation");

    // 5. Assassin-focused specialist is not forced to have a conventional tank.
    Roles specialist(PE::size, -1);
    specialist[8] = PE::assassin;
    specialist[10] = PE::assassin;
    specialist[17] = PE::carry;
    const auto specialist_eval = BoardEvaluation::evaluate(specialist);
    require(specialist_eval.specialized_assassin_board,
            "assassin-heavy formation should be recognized as specialized");
    require(specialist_eval.structural_score > -0.55,
            "specialized formation should not receive the generic no-frontline penalty");

    // 6. No meaningful layout change should yield zero delta.
    const auto same_a = BoardEvaluation::evaluate(protected_board, {}, 1.0);
    const auto same_b = BoardEvaluation::evaluate(protected_board, {}, 1.0);
    require(std::abs(BoardEvaluation::improvement(same_a, same_b)) < 1e-12,
            "unchanged board should have zero evaluation delta");

    // Important units on bench are only penalized when board capacity is free.
    const auto bench_signal = BoardEvaluation::evaluate(
        with_frontline, {BenchUnitProfile{PE::carry, 2}}, 0.0);
    require(bench_signal.important_bench_units_unplayed == 1,
            "high-value bench unit should be signaled when board has free capacity");
    Roles full_board(PE::size, PE::fighter);
    const auto full_eval = BoardEvaluation::evaluate(
        full_board, {BenchUnitProfile{PE::carry, 2}}, 0.0);
    require(full_eval.important_bench_units_unplayed == 0,
            "bench penalty must not apply when board is full");

    std::cout << "[PASS] Structural and continuous board evaluation scenarios.\n";
    return EXIT_SUCCESS;
}
