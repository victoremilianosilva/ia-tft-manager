#include "strategy/BoardEvaluation.hpp"

#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

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

    // Repeated reads of an unchanged snapshot reuse the exact evaluation.
    // A changed signature forces the evaluator to run again and replace the score.
    tft::strategy::BoardEvaluationCache evaluation_cache;
    std::uint32_t evaluations = 0;
    const auto evaluate_snapshot = [&](std::uint64_t signature, double score) {
        if (!evaluation_cache.matches(signature)) {
            tft::strategy::BoardEvaluationResult result{};
            result.total_score = score;
            ++evaluations;
            evaluation_cache.store(signature, result);
        }
        return evaluation_cache.value().total_score;
    };
    require(evaluate_snapshot(1001U, 1.25) == 1.25,
            "first board snapshot should be evaluated and cached");
    require(evaluate_snapshot(1001U, 9.99) == 1.25 && evaluations == 1,
            "unchanged board snapshot must reuse the cached score");
    require(evaluate_snapshot(1002U, 2.75) == 2.75 && evaluations == 2,
            "changed board snapshot must recompute and return the updated score");
    evaluation_cache.invalidate();
    require(!evaluation_cache.matches(1002U),
            "explicit cache invalidation must force recomputation");

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

    // A fighter is a weaker protector than a tank, but should still count as
    // frontline when it stands directly in front of the carry.
    Roles fighter_protection(PE::size, -1);
    fighter_protection[2 * PE::cols + 3] = PE::fighter;
    fighter_protection[3 * PE::cols + 3] = PE::carry;
    const auto fighter_protected_eval =
        BoardEvaluation::evaluate(fighter_protection, {}, 0.0, {24});
    require(fighter_protected_eval.exposed_carry_count == 0,
            "frontline fighter directly in front should protect a carry");
    require(fighter_protected_eval.exposed_main_carry_count == 0,
            "main carry should accept a fighter as partial frontline protection");

    // Frontline distribution: two lanes beat a single isolated lane for a larger board.
    Roles narrow_frontline(PE::size, -1);
    narrow_frontline[3] = PE::tank;       // row 0, column 3
    narrow_frontline[10] = PE::fighter;   // row 1, same column
    narrow_frontline[24] = PE::carry;
    narrow_frontline[25] = PE::support;
    Roles spread_frontline(PE::size, -1);
    spread_frontline[0] = PE::tank;       // row 0, column 0
    spread_frontline[8] = PE::fighter;    // row 1, column 1; still adjacent to tank
    spread_frontline[24] = PE::carry;
    spread_frontline[25] = PE::support;
    const auto narrow_eval = BoardEvaluation::evaluate(narrow_frontline);
    const auto spread_eval = BoardEvaluation::evaluate(spread_frontline);
    require(spread_eval.frontline_lane_count > narrow_eval.frontline_lane_count,
            "frontline spread must count distinct columns, not just units");
    require(spread_eval.total_score > narrow_eval.total_score,
            "spreading a frontline across lanes should improve board quality");

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

    // Strategic coherence: a six-unit board needs both frontline and
    // damage/backline coverage; a pile of carries is not a complete lineup.
    Roles coherent_roles(PE::size, -1);
    coherent_roles[0] = PE::tank;
    coherent_roles[1] = PE::fighter;
    coherent_roles[7] = PE::carry;
    coherent_roles[8] = PE::support;
    coherent_roles[14] = PE::carry;
    coherent_roles[15] = PE::fighter;
    Roles carry_only_roles(PE::size, -1);
    carry_only_roles[0] = PE::carry;
    carry_only_roles[1] = PE::carry;
    carry_only_roles[7] = PE::carry;
    carry_only_roles[8] = PE::carry;
    carry_only_roles[14] = PE::assassin;
    carry_only_roles[15] = PE::assassin;
    std::vector<tft::strategy::BoardUnitProfile> coherent_profiles(PE::size);
    const auto set_profile = [&](int slot, int id, int role, int cost,
                                 std::vector<std::string> traits) {
        coherent_profiles[static_cast<std::size_t>(slot)] =
            tft::strategy::BoardUnitProfile{id, role, 1, cost, std::move(traits)};
    };
    set_profile(0, 100, PE::tank, 3, {"Aegis"});
    set_profile(1, 101, PE::fighter, 2, {"Invoker"});
    set_profile(7, 102, PE::carry, 4, {"Invoker"});
    set_profile(8, 103, PE::support, 3, {"Aegis"});
    set_profile(14, 104, PE::carry, 2, {"Dynamo"});
    set_profile(15, 105, PE::fighter, 2, {"Dynamo"});
    tft::strategy::StrategicBoardContext strategic_context;
    strategic_context.level = 8;
    strategic_context.direction = "Invoker";
    strategic_context.planned_unit_ids = {101, 102, 103};
    strategic_context.core_unit_ids = {102};
    strategic_context.planned_traits = {"Invoker", "Aegis"};
    strategic_context.trait_milestones = {
        {"Invoker", {2, 4}}, {"Aegis", {2, 4}}, {"Dynamo", {2, 4}}
    };
    const auto coherent_eval = BoardEvaluation::evaluate(
        coherent_roles, {}, 0.0, {}, coherent_profiles, strategic_context);
    const auto carry_only_eval = BoardEvaluation::evaluate(
        carry_only_roles, {}, 0.0, {}, coherent_profiles, strategic_context);
    require(carry_only_eval.missing_frontline_count > 0,
            "role coverage must identify a board with no frontline");
    require(coherent_eval.total_score > carry_only_eval.total_score,
            "balanced frontline/backline coverage should beat an incomplete carry-heavy board");

    // Composition-aligned units improve strategic fit without making
    // off-direction bridge units invalid.
    auto neutral_context = strategic_context;
    neutral_context.direction.clear();
    neutral_context.core_unit_ids.clear();
    neutral_context.planned_unit_ids.clear();
    neutral_context.core_traits.clear();
    neutral_context.planned_traits.clear();
    const auto neutral_eval = BoardEvaluation::evaluate(
        coherent_roles, {}, 0.0, {}, coherent_profiles, neutral_context);
    require(coherent_eval.strategic_fit_score > neutral_eval.strategic_fit_score,
            "planned/core units should improve strategic fit");
    require(coherent_eval.active_trait_count >= 2,
            "active trait milestones should be counted from unique champion traits");

    // Early boards remain flexible; the same role gap matters more once
    // the lineup is mature and its strategic direction should be established.
    auto early_context = strategic_context;
    early_context.level = 2;
    auto mature_context = strategic_context;
    mature_context.level = 8;
    const auto early_eval = BoardEvaluation::evaluate(
        carry_only_roles, {}, 0.0, {}, coherent_profiles, early_context);
    const auto mature_eval = BoardEvaluation::evaluate(
        carry_only_roles, {}, 0.0, {}, coherent_profiles, mature_context);
    require(mature_eval.structural_score < early_eval.structural_score,
            "structural role gaps should matter more as the composition matures");

    // Star/cost quality is bounded and should not overwhelm structural fit.
    auto upgraded_profiles = coherent_profiles;
    upgraded_profiles[7].star = 2;
    const auto upgraded_eval = BoardEvaluation::evaluate(
        coherent_roles, {}, 0.0, {}, upgraded_profiles, strategic_context);
    require(upgraded_eval.unit_quality_score > coherent_eval.unit_quality_score,
            "upgraded deployed units should improve the bounded quality component");

    std::cout << "[PASS] Tactical board evaluation and directional delta scenarios.\n";
    return EXIT_SUCCESS;
}
