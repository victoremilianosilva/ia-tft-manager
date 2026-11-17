#pragma once

#include <algorithm>
#include <cmath>
#include <limits>
#include <utility>
#include <vector>

namespace tft {
class PositioningEngine {
public:
    static constexpr int rows = 4, cols = 7, size = 28;
    static constexpr int tank = 0, carry = 1, support = 2, fighter = 3, assassin = 4;

    static bool is_valid_position(int p) noexcept { return p >= 0 && p < size; }

    static std::pair<int, int> position_to_row_col(int p) noexcept {
        return is_valid_position(p) ? std::pair<int, int>{p / cols, p % cols}
                                    : std::pair<int, int>{-1, -1};
    }

    static int row_col_to_position(int r, int c) noexcept {
        return r >= 0 && r < rows && c >= 0 && c < cols ? r * cols + c : -1;
    }

    static std::vector<int> get_neighbors(int p, bool diagonal = true) {
        std::vector<int> out;
        const auto [r, c] = position_to_row_col(p);
        if (r < 0) return out;
        constexpr int dirs8[8][2] = {
            {-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1}
        };
        constexpr int dirs4[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        if (diagonal) {
            for (const auto& d : dirs8) {
                const int n = row_col_to_position(r + d[0], c + d[1]);
                if (n >= 0) out.push_back(n);
            }
        } else {
            for (const auto& d : dirs4) {
                const int n = row_col_to_position(r + d[0], c + d[1]);
                if (n >= 0) out.push_back(n);
            }
        }
        return out;
    }

    // Role-based preference only. Protection and formation structure are
    // evaluated by BoardEvaluation, so the same tactical signal is not counted
    // twice with incompatible scales.
    static double evaluate_unit_placement(const std::vector<int>& board, int p,
                                         int candidate = -2) {
        if (!is_valid_position(p)) return -999.0;
        int role = candidate == -2 ? role_at(board, p) : candidate;
        if (role < 0) return 0.0;
        if (role > assassin) role = fighter;
        const auto [r, c] = position_to_row_col(p);
        const double front = (3.0 - r) / 3.0;
        const double back = r / 3.0;
        const double center = std::max(0.0, 1.0 - std::abs(c - 3.0) / 3.0);
        const double edge = (c == 0 || c == cols - 1) ? 1.0 : 0.0;

        switch (role) {
            case tank:     return front * 4.0 + center * 1.0;
            case fighter:  return front * 2.5 + center * 0.75;
            case assassin: return (1.0 - std::min(1.0, std::abs(r - 1.5) / 2.0)) * 2.0 + edge * 0.75;
            case support:  return back * 2.5 + center * 1.0;
            case carry:    return back * 3.5 + center * 1.5 + edge * 0.15;
            default:       return 0.0;
        }
    }

    // Legacy helper retained for callers/tests; BoardEvaluation owns the
    // authoritative tactical protection penalties and bonuses.
    static double evaluate_protection(const std::vector<int>& board, int p) {
        const int role = role_at(board, p);
        if (role < 0) return 0.0;
        int occupied = 0, tanks_in_front = 0;
        const auto [r, c] = position_to_row_col(p);
        (void)c;
        for (const int n : get_neighbors(p, true)) {
            const int nr = role_at(board, n);
            if (nr < 0) continue;
            ++occupied;
            const auto [neighbor_row, neighbor_col] = position_to_row_col(n);
            (void)neighbor_col;
            if (nr == tank && neighbor_row < r) ++tanks_in_front;
        }
        if (role == carry) return std::min(1.0, occupied * 0.15 + tanks_in_front * 0.5);
        if (role == support) return std::min(0.6, occupied * 0.12 + tanks_in_front * 0.2);
        if (role == tank) return occupied * 0.1;
        return 0.0;
    }

    static double evaluate_board_positioning(const std::vector<int>& board) {
        double score = 0.0;
        const int limit = std::min(static_cast<int>(board.size()), size);
        for (int p = 0; p < limit; ++p)
            if (role_at(board, p) >= 0) score += evaluate_unit_placement(board, p);
        return score;
    }

    static std::pair<int, double> find_best_position(
        const std::vector<int>& board, int role,
        const std::vector<int>& candidates = {}) {
        std::vector<int> slots = candidates;
        if (slots.empty())
            for (int p = 0; p < size; ++p)
                if (role_at(board, p) < 0) slots.push_back(p);

        int best = -1;
        double best_delta = 0.0;
        const double before = evaluate_board_positioning(board);
        for (const int p : slots) {
            if (!is_valid_position(p) || role_at(board, p) >= 0) continue;
            auto simulated = normalized(board);
            simulated[p] = norm_role(role);
            const double delta = evaluate_board_positioning(simulated) - before;
            if (delta > best_delta) { best = p; best_delta = delta; }
        }
        return {best, best_delta};
    }

    static std::pair<int, double> find_best_swap(
        const std::vector<int>& board, int source,
        const std::vector<int>& candidates = {}) {
        if (!is_valid_position(source) || role_at(board, source) < 0)
            return {-1, -std::numeric_limits<double>::infinity()};
        std::vector<int> slots = candidates;
        if (slots.empty())
            for (int p = 0; p < std::min(static_cast<int>(board.size()), size); ++p)
                if (p != source) slots.push_back(p);

        int best = -1;
        double best_delta = 0.0;
        const double before = evaluate_board_positioning(board);
        for (const int target : slots) {
            if (!is_valid_position(target) || target == source) continue;
            auto simulated = normalized(board);
            std::swap(simulated[source], simulated[target]);
            const double delta = evaluate_board_positioning(simulated) - before;
            if (delta > best_delta) { best = target; best_delta = delta; }
        }
        return {best, best_delta};
    }

    static bool is_board_stable(const std::vector<int>& board, double tolerance = 0.01) {
        for (int p = 0; p < std::min(static_cast<int>(board.size()), size); ++p) {
            if (role_at(board, p) < 0) continue;
            const auto [target, delta] = find_best_swap(board, p);
            if (target >= 0 && delta > tolerance) return false;
        }
        return true;
    }

    static double get_normalized_positioning_score(const std::vector<int>& board) {
        int count = 0;
        for (int p = 0; p < std::min(static_cast<int>(board.size()), size); ++p)
            if (role_at(board, p) >= 0) ++count;
        if (count == 0) return 0.0;
        // The strongest role-placement preference is about 6 points/unit.
        // Keep this in a stable, interpretable 0..1 range across board sizes.
        return std::clamp(evaluate_board_positioning(board) /
                          (static_cast<double>(count) * 6.0), 0.0, 1.0);
    }

private:
    static int norm_role(int role) { return role >= 0 && role <= assassin ? role : fighter; }
    static int role_at(const std::vector<int>& board, int p) {
        if (!is_valid_position(p) || static_cast<std::size_t>(p) >= board.size() || board[p] < 0)
            return -1;
        return norm_role(board[p]);
    }
    static std::vector<int> normalized(const std::vector<int>& board) {
        std::vector<int> out(size, -1);
        std::copy_n(board.begin(), std::min(board.size(), out.size()), out.begin());
        return out;
    }
};
} // namespace tft
