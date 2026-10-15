#pragma once

#include <algorithm>
#include <array>
#include <cctype>
#include <string>
#include <string_view>
#include <vector>

namespace tft {

enum class ProfileRole : int { TANK = 0, CARRY = 1, SUPPORT = 2, FIGHTER = 3, ASSASSIN = 4 };

struct CombatProfileInput {
    std::string ability_text;
    double attack_range = 0.0;
    double attack_speed = 0.0;
    double attack_damage = 0.0;
    double armor = 0.0;
    double magic_resist = 0.0;
    double max_hp = 0.0;
    double max_mana = 0.0;
};

struct CombatProfile {
    ProfileRole role = ProfileRole::FIGHTER;
    double attack_range = 0.0;
    double attack_speed = 0.0;
    double attack_damage = 0.0;
    double armor = 0.0;
    double magic_resist = 0.0;
    double max_hp = 0.0;
    double max_mana = 0.0;

    bool frontline() const { return role == ProfileRole::TANK || role == ProfileRole::FIGHTER; }
    bool backline() const { return role == ProfileRole::CARRY || role == ProfileRole::SUPPORT || role == ProfileRole::ASSASSIN; }
};

class CombatProfileEngine {
public:
    static constexpr std::array<std::string_view, 8> tank_keywords = {
        "shield", "armor", "defense", "defensive", "taunt", "damage reduction", "barrier", "protect"
    };
    static constexpr std::array<std::string_view, 7> carry_keywords = {
        "attack damage", "critical", "crit", "damage", "projectile", "rapid fire", "attack speed"
    };
    static constexpr std::array<std::string_view, 8> support_keywords = {
        "heal", "healing", "shield", "buff", "ally", "all allies", "mana", "restore"
    };
    static constexpr std::array<std::string_view, 6> assassin_keywords = {
        "dash", "jump", "backline", "lowest health", "furthest", "farther"
    };

    static ProfileRole infer_role(const CombatProfileInput& u) {
        std::array<double, 5> scores{};
        const std::string text = lowercase(u.ability_text);
        add_keyword_scores(scores, text, tank_keywords, 0);
        add_keyword_scores(scores, text, carry_keywords, 1);
        add_keyword_scores(scores, text, support_keywords, 2);
        add_keyword_scores(scores, text, std::array<std::string_view, 6>{
            "melee", "strike", "physical damage", "attack", "damage", "lifesteal"
        }, 3);

        if (u.max_hp >= 800) scores[0] += 2.0;
        if (u.max_hp >= 1100) scores[0] += 1.0;
        if (u.armor >= 40) scores[0] += 1.5;
        if (u.magic_resist >= 40) scores[0] += 1.0;
        if (u.attack_damage >= 70) scores[1] += 1.5;
        if (u.attack_speed >= 0.8) scores[1] += 1.0;
        if (u.attack_range > 0 && u.attack_range <= 1) {
            scores[3] += 1.0;
            if (u.armor >= 30 || u.max_hp >= 700) scores[3] += 1.0;
        }
        if (u.attack_range >= 3) {
            scores[1] += 0.5;
            scores[2] += 0.25;
        }
        if (contains_any(text, assassin_keywords)) scores[4] += 2.0;

        // Python max(dict, key=dict.get) resolves ties by enum insertion order.
        int best = 0;
        for (int i = 1; i < 5; ++i) if (scores[static_cast<std::size_t>(i)] > scores[static_cast<std::size_t>(best)]) best = i;
        return static_cast<ProfileRole>(best);
    }

    static CombatProfile build_profile(const CombatProfileInput& u) {
        return {infer_role(u), u.attack_range, u.attack_speed, u.attack_damage,
                u.armor, u.magic_resist, u.max_hp, u.max_mana};
    }

    static bool is_frontline(ProfileRole r) { return r == ProfileRole::TANK || r == ProfileRole::FIGHTER; }
    static bool is_backline(ProfileRole r) { return r == ProfileRole::CARRY || r == ProfileRole::SUPPORT || r == ProfileRole::ASSASSIN; }

private:
    static std::string lowercase(std::string s) {
        std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c) { return static_cast<char>(std::tolower(c)); });
        return s;
    }
    template <std::size_t N>
    static void add_keyword_scores(std::array<double, 5>& scores, const std::string& text,
                                   const std::array<std::string_view, N>& words, std::size_t role) {
        for (const auto word : words) if (text.find(word) != std::string::npos) scores[role] += 1.0;
    }
    template <std::size_t N>
    static bool contains_any(const std::string& text, const std::array<std::string_view, N>& words) {
        for (const auto word : words) if (text.find(word) != std::string::npos) return true;
        return false;
    }
};

} // namespace tft
