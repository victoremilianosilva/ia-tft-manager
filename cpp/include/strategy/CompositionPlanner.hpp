#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <limits>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include "lobby/TftEngine.hpp"
#include "lobby/ShopEngine.hpp"

namespace tft::strategy {

// A flexible target lineup derived from the current direction and the full
// champion pool. The direction is an anchor, not a requirement that every slot
// belong to the same trait.
struct CompositionPlan {
    std::vector<std::int32_t> unit_ids;
    std::vector<std::string> unit_names;
    std::vector<std::string> core_traits;
    std::int32_t main_carry_id{-1};
    double score{0.0};
    std::vector<std::string> acquisition_notes;
};

class CompositionPlanner {
public:
    // Levels 1-8 share a stable eight-unit target. At levels 9/10 the planner
    // expands to the actual level and is recomputed from the latest game state.
    static std::size_t target_slots_for_level(int level) noexcept {
        return level <= 8 ? 8U
            : static_cast<std::size_t>(std::clamp(level, 9, 10));
    }

    using TraitMilestones = std::unordered_map<std::string, std::vector<int>>;
    using OwnedCopies = std::unordered_map<std::int32_t, int>;
    using FocusWeights = std::vector<std::pair<std::string, double>>;
    using AvailableCopies = std::unordered_map<std::int32_t, int>;

    static CompositionPlan build(
        const std::vector<ChampionDefinition>& pool,
        const TraitMilestones& milestones,
        const std::string& direction,
        const FocusWeights& focus_weights,
        const OwnedCopies& owned_copies,
        std::size_t requested_slots,
        int current_level = 1,
        const AvailableCopies& available_copies = {}) {
        CompositionPlan plan;
        if (pool.empty() || requested_slots == 0) return plan;

        const std::size_t slots = std::min<std::size_t>(requested_slots, 10);
        const int safe_level = std::clamp(current_level, 1, 10);
        const auto& shop_odds = tft::ShopEngine::odds_by_level();
        std::array<double, 5> available_by_cost{};
        for (const auto& champion : pool) {
            const auto found = available_copies.find(champion.internal_id);
            if (found != available_copies.end() && champion.cost >= 1 && champion.cost <= 5)
                available_by_cost[static_cast<std::size_t>(champion.cost - 1)] += std::max(0, found->second);
        }
        const auto acquisition = [&](const ChampionDefinition& champion) {
            const auto owned = owned_copies.find(champion.internal_id);
            if (owned != owned_copies.end() && owned->second > 0)
                return std::pair<double, double>{1.0, 0.0};
            if (available_copies.empty() || champion.cost < 1 || champion.cost > 5)
                return std::pair<double, double>{1.0, 0.0};
            const auto available = available_copies.find(champion.internal_id);
            const double copies = available == available_copies.end() ? 0.0 : static_cast<double>(std::max(0, available->second));
            const double tier_total = available_by_cost[static_cast<std::size_t>(champion.cost - 1)];
            const double tier_odds = shop_odds[static_cast<std::size_t>(safe_level - 1)][static_cast<std::size_t>(champion.cost - 1)];
            if (copies <= 0.0 || tier_total <= 0.0 || tier_odds <= 0.0)
                return std::pair<double, double>{0.0, 4.5};
            const double per_slot = tier_odds * copies / tier_total;
            const double per_shop = 1.0 - std::pow(1.0 - std::clamp(per_slot, 0.0, 1.0), 5.0);
            const double penalty = 3.5 * (1.0 - std::clamp(per_shop / 0.20, 0.0, 1.0));
            return std::pair<double, double>{per_shop, penalty};
        };
        std::unordered_map<std::string, double> focus;
        for (const auto& [trait, weight] : focus_weights)
            if (!trait.empty() && std::isfinite(weight))
                focus[trait] = std::max(0.0, weight);

        std::unordered_set<std::string> anchor_traits;
        if (!direction.empty()) anchor_traits.insert(direction);
        // Champions that carry the current direction reveal compatible
        // bridge traits. This allows, for example, a carry with a secondary
        // trait to connect a defensive frontline direction to damage.
        for (const auto& champion : pool) {
            if (std::find(champion.traits.begin(), champion.traits.end(), direction)
                == champion.traits.end()) continue;
            for (const auto& trait : champion.traits)
                if (trait != direction) anchor_traits.insert(trait);
        }

        const auto role_of = [](const ChampionDefinition& champion) {
            return champion.combat_profile.role >= 0
                ? champion.combat_profile.role : champion.role;
        };
        const auto has_trait = [](const ChampionDefinition& champion,
                                  const std::string& trait) {
            return !trait.empty() &&
                std::find(champion.traits.begin(), champion.traits.end(), trait)
                    != champion.traits.end();
        };
        const auto count_role = [&](int role) {
            return static_cast<int>(std::count_if(
                plan.unit_ids.begin(), plan.unit_ids.end(),
                [&](std::int32_t id) {
                    const auto it = std::find_if(pool.begin(), pool.end(),
                        [id](const ChampionDefinition& champion) {
                            return champion.internal_id == id;
                        });
                    return it != pool.end() && role_of(*it) == role;
                }));
        };

        // Select a carry first. It may be outside the anchor trait if it shares
        // a bridge trait with a champion in that direction or with current focus.
        const ChampionDefinition* selected_carry = nullptr;
        double best_carry_score = -std::numeric_limits<double>::infinity();
        for (const auto& champion : pool) {
            if (role_of(champion) != 1) continue;
            if (acquisition(champion).first <= 0.0) continue;
            double score = 2.5 + champion.cost * 0.10;
            if (has_trait(champion, direction)) score += 2.2;
            for (const auto& trait : champion.traits) {
                const auto focus_it = focus.find(trait);
                if (focus_it != focus.end()) score += std::min(1.5, focus_it->second * 0.20);
                if (anchor_traits.count(trait) != 0) score += 0.8;
            }
            const auto owned = owned_copies.find(champion.internal_id);
            if (owned != owned_copies.end()) score += std::min(2.0, owned->second * 0.35);
            const auto [shop_probability, acquisition_penalty] = acquisition(champion);
            (void)shop_probability;
            score -= acquisition_penalty * 1.35;
            if (score > best_carry_score) {
                best_carry_score = score;
                selected_carry = &champion;
            }
        }
        if (selected_carry) {
            plan.unit_ids.push_back(selected_carry->internal_id);
            plan.unit_names.push_back(selected_carry->api_name.empty()
                ? selected_carry->name : selected_carry->api_name);
            plan.main_carry_id = selected_carry->internal_id;
            plan.score += best_carry_score;
        }

        std::unordered_map<std::string, int> selected_trait_counts;
        const auto add_champion_traits = [&](const ChampionDefinition& champion) {
            for (const auto& trait : champion.traits) ++selected_trait_counts[trait];
        };
        if (selected_carry) add_champion_traits(*selected_carry);

        while (plan.unit_ids.size() < slots) {
            const ChampionDefinition* best = nullptr;
            double best_score = -std::numeric_limits<double>::infinity();
            for (const auto& champion : pool) {
                if (std::find(plan.unit_ids.begin(), plan.unit_ids.end(),
                              champion.internal_id) != plan.unit_ids.end()) continue;
                if (acquisition(champion).first <= 0.0) continue;
                const int role = role_of(champion);
                double score = 0.0;

                // Prefer completing useful trait breakpoints, but do not force
                // every slot into the primary trait.
                for (const auto& trait : champion.traits) {
                    const int before = selected_trait_counts[trait];
                    const auto milestone_it = milestones.find(trait);
                    if (milestone_it != milestones.end()) {
                        for (const int milestone : milestone_it->second) {
                            if (milestone > before && milestone <= before + 1) {
                                score += 1.0 + (trait == direction ? 1.1 : 0.0);
                                break;
                            }
                        }
                    } else if (before == 1) {
                        score += trait == direction ? 1.4 : 0.35;
                    }
                    if (trait == direction) score += 1.0;
                    const auto focus_it = focus.find(trait);
                    if (focus_it != focus.end())
                        score += std::min(1.2, focus_it->second * 0.16);
                    if (anchor_traits.count(trait) != 0 && trait != direction)
                        score += 0.45;
                    if (before > 0) score += std::min(0.45, before * 0.12);
                }

                if (role == 1 && count_role(1) == 0) score += 2.8;
                if ((role == 0 || role == 3) && count_role(0) + count_role(3) == 0)
                    score += 2.0;
                else if ((role == 0 || role == 3) &&
                         count_role(0) + count_role(3) == 1)
                    score += 0.9;
                if (role == 2) score += 0.25; // support has flexible utility
                score += std::min(1.8, owned_copies.count(champion.internal_id)
                    ? owned_copies.at(champion.internal_id) * 0.35 : 0.0);
                score -= champion.cost * 0.12; // avoid an all-expensive theoretical board
                const auto [shop_probability, acquisition_penalty] = acquisition(champion);
                (void)shop_probability;
                score -= acquisition_penalty;
                if (score > best_score) {
                    best_score = score;
                    best = &champion;
                }
            }
            if (!best) break;
            plan.unit_ids.push_back(best->internal_id);
            plan.unit_names.push_back(best->api_name.empty() ? best->name : best->api_name);
            plan.score += best_score;
            add_champion_traits(*best);
        }

        // Keep a compact strategic summary: primary direction first, then the
        // strongest additional traits actually represented by the planned lineup.
        if (!direction.empty() && selected_trait_counts.count(direction) != 0)
            plan.core_traits.push_back(direction);
        std::vector<std::pair<std::string, int>> traits(
            selected_trait_counts.begin(), selected_trait_counts.end());
        std::stable_sort(traits.begin(), traits.end(),
            [&](const auto& lhs, const auto& rhs) {
                if (lhs.second != rhs.second) return lhs.second > rhs.second;
                return focus[lhs.first] > focus[rhs.first];
            });
        for (const auto& [trait, count] : traits) {
            if (trait == direction || count < 2) continue;
            if (plan.core_traits.size() >= 3) break;
            plan.core_traits.push_back(trait);
        }
        if (!available_copies.empty()) {
            for (const auto id : plan.unit_ids) {
                const auto champion_it = std::find_if(pool.begin(), pool.end(),
                    [id](const ChampionDefinition& item) { return item.internal_id == id; });
                if (champion_it == pool.end()) continue;
                const auto owned = owned_copies.find(id);
                if (owned != owned_copies.end() && owned->second > 0) continue;
                const auto [per_shop, penalty] = acquisition(*champion_it);
                const int percent = static_cast<int>(std::round(per_shop * 100.0));
                std::string note = champion_it->api_name.empty() ? champion_it->name : champion_it->api_name;
                note += " (cost=" + std::to_string(champion_it->cost) + ", chance_any_shop~" + std::to_string(percent) + "%";
                if (per_shop <= 0.0) note += ", unavailable";
                else if (penalty >= 2.0) note += ", hard_to_find";
                else if (penalty >= 0.8) note += ", low_odds";
                else note += ", viable";
                note += ")";
                plan.acquisition_notes.push_back(std::move(note));
            }

            // Explain why a missing, low-probability carry was not chosen.
            // Limit this to three candidates so logs remain useful rather than noisy.
            std::size_t rejected_carries = 0;
            for (const auto& champion : pool) {
                if (rejected_carries >= 3) break;
                if (role_of(champion) != 1 ||
                    std::find(plan.unit_ids.begin(), plan.unit_ids.end(), champion.internal_id) != plan.unit_ids.end())
                    continue;
                const auto owned = owned_copies.find(champion.internal_id);
                if (owned != owned_copies.end() && owned->second > 0) continue;
                const auto [per_shop, penalty] = acquisition(champion);
                if (penalty < 1.5) continue;
                const int percent = static_cast<int>(std::round(per_shop * 100.0));
                std::string note = "NOT_SELECTED_CARRY: ";
                note += champion.api_name.empty() ? champion.name : champion.api_name;
                note += " (cost=" + std::to_string(champion.cost) +
                    ", chance_any_shop~" + std::to_string(percent) +
                    "%, hard_to_find; alternative carry preferred)";
                plan.acquisition_notes.push_back(std::move(note));
                ++rejected_carries;
            }
        }
        return plan;
    }
};

}  // namespace tft::strategy
