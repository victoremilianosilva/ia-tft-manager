#pragma once
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>

namespace tft {

struct RewardManagerState {
    double previous_board_power{0.0};
    double previous_positioning_score{0.0};
    double previous_synergy_score{0.0};
    int previous_level{1};
    int previous_gold{0};
    double last_combat_reward{0.0};
    double total_reward{0.0};
    double round_reward{0.0};
};

// Behavioral port of ai/RewardManager.py. This class is deliberately
// independent from lobby reward routing: env.step() currently returns
// action reward plus lobby combat/placement rewards, not calculate_total_reward().
class RewardManager {
public:
    void reset() noexcept { state_ = RewardManagerState{}; }

    double calculate_combat_reward(bool won, double damage_dealt=0.0,
        double damage_taken=0.0, int enemy_alive=0, int own_alive=0) noexcept {
        double r = won ? 2.0 : -2.0;
        if (damage_dealt > 0) r += std::min(std::tanh(damage_dealt/10.0), 1.0);
        if (own_alive > 0) r += std::min(own_alive*0.05, 0.25);
        if (enemy_alive > 0) r -= std::min(enemy_alive*0.05, 0.25);
        if (damage_taken > 0) r -= std::min(std::tanh(damage_taken/15.0), 0.75);
        state_.last_combat_reward = r;
        return r;
    }
    double calculate_power_reward(double current) noexcept {
        const double delta=current-state_.previous_board_power;
        state_.previous_board_power=current;
        return std::abs(delta)<1e-6 ? 0.0 : std::tanh(delta/10.0);
    }
    double calculate_synergy_reward(double current) noexcept {
        const double delta=current-state_.previous_synergy_score;
        state_.previous_synergy_score=current;
        return std::tanh(delta);
    }
    double calculate_positioning_reward(double current) noexcept {
        const double delta=current-state_.previous_positioning_score;
        state_.previous_positioning_score=current;
        return std::tanh(delta)*0.5;
    }
    double calculate_level_reward(int level) noexcept {
        if (level <= state_.previous_level) return 0.0;
        const int delta=level-state_.previous_level;
        state_.previous_level=level;
        return std::min(delta*0.5,1.5);
    }
    double calculate_economy_reward(double gold, int /*level*/, double hp) const noexcept {
        double r=0.0;
        for(int threshold=10;threshold<=50;threshold+=10) if(gold>=threshold) r+=0.05;
        if(hp<=15) r-=0.15; else if(hp<=30) r-=0.05;
        return r;
    }
    double calculate_streak_reward(int win_streak,int loss_streak) const noexcept {
        double r=0;
        if(win_streak>=2) r+=std::min(win_streak*0.03,0.15);
        if(loss_streak>=2) r+=std::min(loss_streak*0.02,0.10);
        return r;
    }
    double calculate_board_reward(int occupied,int max_units) const noexcept {
        return max_units<=0 ? 0.0 : std::max(0,occupied)/static_cast<double>(max_units)*0.15;
    }
    double calculate_action_reward(const std::string& /*action_type*/,bool success,double action_value=0.0) const noexcept {
        return success ? action_value : -0.10;
    }
    double calculate_total_reward(double combat=0,double power=0,double synergy=0,
        double positioning=0,double level=0,double economy=0,double streak=0,
        double board=0,double action=0) noexcept {
        const double total=combat+power+synergy+positioning+level+economy+streak+board+action;
        state_.round_reward=std::clamp(total,-5.0,5.0);
        state_.total_reward+=state_.round_reward;
        return state_.round_reward;
    }
    RewardManagerState get_state() const noexcept { return state_; }
private:
    RewardManagerState state_{};
};

} // namespace tft
