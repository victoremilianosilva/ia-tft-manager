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
    // Avoid generic combat words ("damage", "attack", "shield") dominating
    // role inference: many fighter/carry abilities mention damage, and support
    // abilities may shield allies without making the champion a tank.
    static constexpr std::array<std::string_view, 6> tank_keywords = {
        "taunt", "damage reduction", "increased armor", "bonus armor", "fortify", "unbreakable"
    };
    static constexpr std::array<std::string_view, 7> carry_keywords = {
        "attack damage", "critical", "crit", "projectile", "rapid fire", "attack speed"
    };
    static constexpr std::array<std::string_view, 7> support_keywords = {
        "heal", "healing", "shield allies", "buff allies", "all allies", "restore health", "grant mana"
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
        add_keyword_scores(scores, text, std::array<std::string_view, 4>{
            "melee", "strike", "lifesteal", "physical attack"
        }, 3);

        // Tankiness is a combination of durability stats, not HP alone.
        // HP/armor are common on bruisers, so require multiple defensive signals.
        const int defensive_signals =
            (u.max_hp >= 850 ? 1 : 0) +
            (u.armor >= 45 ? 1 : 0) +
            (u.magic_resist >= 45 ? 1 : 0);
        if (u.max_hp >= 850) scores[0] += 0.75;
        if (defensive_signals >= 2) scores[0] += 1.75;
        if (u.max_hp >= 1150 && defensive_signals >= 2) scores[0] += 0.75;
        if (u.armor >= 55 && u.magic_resist >= 55) scores[0] += 0.75;

        if (u.attack_damage >= 70) scores[1] += 1.75;
        if (u.attack_speed >= 0.8) scores[1] += 1.25;
        if (u.attack_range >= 3) scores[1] += 0.75;
        if (u.attack_range > 0 && u.attack_range <= 1) {
            scores[3] += 1.25;
            if (u.attack_damage >= 55 || u.attack_speed >= 0.75) scores[3] += 0.75;
            if (u.armor >= 30 || u.max_hp >= 700) scores[3] += 0.5;
        }
        if (u.attack_range >= 3) scores[2] += 0.15;
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
