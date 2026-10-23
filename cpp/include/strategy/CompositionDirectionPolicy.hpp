#pragma once

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>

namespace tft::strategy {

// Hysteresis policy for composition direction changes. The policy is deliberately
// independent from trait scoring so it can be tested deterministically.
struct CompositionDirectionConfig {
    double min_relative_advantage{0.20};
    double min_absolute_advantage{0.75};
    std::uint32_t consecutive_updates{3};
};

struct CompositionDirectionState {
    std::string direction;
    double strength{0.0};
    bool locked{false};
    std::string candidate_direction;
    double candidate_strength{0.0};
    std::uint32_t candidate_streak{0};
    std::string previous_direction;
    std::string change_reason{"initial"};
    std::uint64_t change_count{0};
};

struct CompositionDirectionInput {
    std::string candidate_direction;
    double candidate_strength{0.0};
    bool current_direction_viable{true};
    bool emergency{false};
};

struct CompositionDirectionResult {
    bool changed{false};
    bool unlocked{false};
    std::string reason;
};

class CompositionDirectionPolicy {
public:
    explicit CompositionDirectionPolicy(CompositionDirectionConfig config = {})
        : config_(config) {
        config_.min_relative_advantage =
            std::max(0.0, config_.min_relative_advantage);
        config_.min_absolute_advantage =
            std::max(0.0, config_.min_absolute_advantage);
        config_.consecutive_updates =
            std::max<std::uint32_t>(1, config_.consecutive_updates);
    }

    CompositionDirectionResult update(
        CompositionDirectionState& state,
        const CompositionDirectionInput& input) const {
        CompositionDirectionResult result;
        const bool has_candidate = !input.candidate_direction.empty() &&
            std::isfinite(input.candidate_strength) && input.candidate_strength > 0.0;

        // Never erase an established direction because a single update had no
        // usable trait scores. An empty direction can still be initialized later.
        if (!has_candidate) {
            state.candidate_direction.clear();
            state.candidate_strength = 0.0;
            state.candidate_streak = 0;
            if (!state.locked && state.direction.empty()) {
                state.strength = 0.0;
            }
            result.reason = state.locked ? "candidate_missing_keep_locked_direction"
                                         : "candidate_missing";
            return result;
        }

        if (state.direction.empty()) {
            apply(state, input.candidate_direction, input.candidate_strength,
                  "initial_direction");
            result.changed = true;
            result.reason = state.change_reason;
            return result;
        }

        if (input.candidate_direction == state.direction) {
            state.strength = input.candidate_strength;
            state.candidate_direction.clear();
            state.candidate_strength = 0.0;
            state.candidate_streak = 0;
            state.change_reason = "direction_maintained";
            result.reason = state.change_reason;
            return result;
        }

        if (!state.locked) {
            apply(state, input.candidate_direction, input.candidate_strength,
                  "unlocked_candidate");
            result.changed = true;
            result.reason = state.change_reason;
            return result;
        }

        if (!input.current_direction_viable || input.emergency) {
            state.locked = false;
            result.unlocked = true;
            apply(state, input.candidate_direction, input.candidate_strength,
                  input.emergency ? "emergency_transition"
                                  : "current_direction_unviable");
            result.changed = true;
            result.reason = state.change_reason;
            return result;
        }

        const double absolute_advantage =
            input.candidate_strength - state.strength;
        const double relative_advantage =
            absolute_advantage / std::max(std::abs(state.strength), 1e-6);
        const bool sufficiently_better =
            absolute_advantage >= config_.min_absolute_advantage &&
            relative_advantage >= config_.min_relative_advantage;

        if (!sufficiently_better) {
            state.candidate_direction.clear();
            state.candidate_strength = 0.0;
            state.candidate_streak = 0;
            state.change_reason = "locked_candidate_not_significantly_better";
            result.reason = state.change_reason;
            return result;
        }

        if (state.candidate_direction == input.candidate_direction) {
            ++state.candidate_streak;
        } else {
            state.candidate_direction = input.candidate_direction;
            state.candidate_strength = input.candidate_strength;
            state.candidate_streak = 1;
        }
        state.candidate_strength = input.candidate_strength;
        state.change_reason = "locked_candidate_pending";
        if (state.candidate_streak < config_.consecutive_updates) {
            result.reason = state.change_reason;
            return result;
        }

        state.locked = false;
        result.unlocked = true;
        apply(state, input.candidate_direction, input.candidate_strength,
              "persistent_superior_candidate");
        result.changed = true;
        result.reason = state.change_reason;
        return result;
    }

private:
    CompositionDirectionConfig config_;

    static void apply(CompositionDirectionState& state,
                      const std::string& direction,
                      double strength,
                      const char* reason) {
        state.previous_direction = state.direction;
        state.direction = direction;
        state.strength = strength;
        state.candidate_direction.clear();
        state.candidate_strength = 0.0;
        state.candidate_streak = 0;
        state.change_reason = reason;
        ++state.change_count;
    }
};

}  // namespace tft::strategy
