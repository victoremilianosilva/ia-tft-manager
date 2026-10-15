#pragma once

#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

namespace tft {

using TraitCounts = std::map<std::string, int>;
using TraitMilestones = std::map<std::string, std::vector<int>>;
using TraitFocus = std::map<std::string, double>;

struct SynergyState {
    TraitCounts active_traits;
    TraitCounts partial_traits;
};

class SynergyEngine {
public:
    explicit SynergyEngine(TraitMilestones milestones = {}) : milestones_(std::move(milestones)) {
        for (auto& [name, values] : milestones_) {
            (void)name;
            std::sort(values.begin(), values.end());
        }
    }

    const TraitMilestones& milestones() const { return milestones_; }
    const SynergyState& state() const { return state_; }

    void set_state(TraitCounts active, TraitCounts partial = {}) {
        state_.active_traits = std::move(active);
        state_.partial_traits = std::move(partial);
    }

    double calculate_multiplier(const TraitCounts* active_traits = nullptr) const {
        const auto& source = active_traits ? *active_traits : state_.active_traits;
        double total = 1.0;
        for (const auto& [name, count] : source) {
            const auto it = milestones_.find(name);
            if (it == milestones_.end()) continue;
            const int reached = trait_level(name, count);
            if (reached > 0) total += std::pow(static_cast<double>(reached), 1.8) * 0.20;
        }
        return total;
    }

    std::map<std::string, double> get_all_multipliers(const TraitCounts* active_traits = nullptr) const {
        const auto& source = active_traits ? *active_traits : state_.active_traits;
        std::map<std::string, double> result;
        for (const auto& [name, thresholds] : milestones_) {
            const auto it = source.find(name);
            const int count = it == source.end() ? 0 : it->second;
            const int reached = static_cast<int>(std::count_if(
                thresholds.begin(), thresholds.end(), [count](int m) { return count >= m; }));
            result[name] = reached > 0 ? 1.0 + std::pow(static_cast<double>(reached), 1.8) * 0.20 : 1.0;
        }
        return result;
    }

    int get_trait_level(const std::string& name, int count) const {
        return trait_level(name, count);
    }

    double get_unit_synergy_bonus(const std::vector<std::string>& unit_traits,
                                  const TraitFocus* comp_focus = nullptr) const {
        double bonus = 0.0;
        for (const auto& trait : unit_traits) {
            const auto active_it = state_.active_traits.find(trait);
            const int count = active_it == state_.active_traits.end() ? 0 : active_it->second;
            const int level = trait_level(trait, count);
            double trait_bonus = 0.0;
            if (level > 0) {
                trait_bonus = 1.0 + (level * 0.9);
                trait_bonus += count * 0.15;
            } else if (state_.partial_traits.find(trait) != state_.partial_traits.end()) {
                trait_bonus = 0.6 + (state_.partial_traits.at(trait) * 0.2);
            } else {
                trait_bonus = -0.25;
            }
            if (comp_focus && !comp_focus->empty()) {
                const auto focus_it = comp_focus->find(trait);
                const double strength = focus_it == comp_focus->end() ? 0.0 : focus_it->second;
                if (strength > 0.0) trait_bonus *= (1.0 + std::min(0.5, strength * 0.08));
                else trait_bonus *= 0.85;
            }
            bonus += trait_bonus;
        }
        return bonus;
    }

private:
    int trait_level(const std::string& name, int count) const {
        const auto it = milestones_.find(name);
        if (it == milestones_.end()) return 0;
        return static_cast<int>(std::count_if(
            it->second.begin(), it->second.end(), [count](int m) { return count >= m; }));
    }

    TraitMilestones milestones_;
    SynergyState state_;
};

} // namespace tft
