#pragma once

#include "composition_intelligence/StrategicPositionPlanner.hpp"
#include "lobby/EconomyEngine.hpp"

#include <algorithm>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace tft::composition_intelligence {

struct StrategicActionCandidateBuildResult {
    std::vector<strategy::StrategicActionCandidate> candidates;
    std::vector<StrategicPositionProposal> positioning;
    std::uint32_t rejected_missing_cost{0};
    std::uint32_t rejected_ambiguous_instance{0};
    std::string status{"not_evaluated"};
};

// Produces only snapshot-bound, read-only alternatives. Native masks remain the
// authority for legality; this builder never executes or mutates game state.
class StrategicActionCandidateBuilder {
public:
    StrategicActionCandidateBuildResult build(
        const strategy::StrategicSharedContext& context,
        const std::optional<ActiveComposition>& active,
        const UnitPrioritySnapshot& priorities,
        const LineupPlan& lineup,
        StrategicActionNativeSnapshot& native,
        const std::unordered_map<std::int32_t, std::int32_t>& unit_costs) const {
        StrategicActionCandidateBuildResult out;
        if (native.match_id == 0 || native.player_id != context.player_id ||
            native.round != context.round || native.sequence == 0 ||
            !native.alive || !context.alive || native.gold != context.gold) {
            out.status = "invalid_or_mismatched_native_snapshot";
            return out;
        }
        const auto type_enabled = [&](decision::ActionType type) {
            return native.masks.type_mask[static_cast<std::size_t>(type)] == decision::MASK_ENABLED;
        };
        const auto make_id = [&](strategy::StrategicActionKind kind, std::int32_t champion,
                                 std::int32_t slot) {
            return std::to_string(native.match_id) + ":" +
                std::to_string(native.player_id) + ":" +
                std::to_string(native.sequence) + ":" +
                std::to_string(static_cast<int>(kind)) + ":" +
                std::to_string(champion) + ":" + std::to_string(slot);
        };
        const auto append = [&](strategy::StrategicActionCandidate candidate) {
            candidate.source_sequence = native.sequence;
            candidate.candidate_id = make_id(candidate.kind, candidate.champion_id,
                candidate.kind == strategy::StrategicActionKind::BuyUnit
                    ? candidate.shop_slot : candidate.source_slot);
            out.candidates.push_back(std::move(candidate));
        };

        if (type_enabled(decision::ActionType::PASS)) {
            strategy::StrategicActionCandidate hold;
            hold.kind = strategy::StrategicActionKind::Hold;
            hold.evidence_reason = "explicit_neutral_baseline_no_action_value_claimed";
            append(std::move(hold));
        }

        if (active && !priorities.stale && !lineup.stale &&
            priorities.composition_id == active->candidate.composition_id &&
            priorities.composition_version == active->version &&
            lineup.composition_id == active->candidate.composition_id &&
            lineup.composition_version == active->version) {
            std::unordered_set<std::int32_t> target_ids(
                lineup.endgame_target_ids.begin(), lineup.endgame_target_ids.end());
            std::unordered_map<std::int32_t, const UnitPriority*> by_id;
            for (const auto& unit : priorities.units)
                if (unit.champion_id >= 0) by_id[unit.champion_id] = &unit;

            for (std::size_t slot = 0; slot < native.shop_champion_ids.size(); ++slot) {
                const auto id = native.shop_champion_ids[slot];
                if (id < 0 || native.masks.shop_mask[slot] != decision::MASK_ENABLED ||
                    !target_ids.count(id)) continue;
                const auto priority = by_id.find(id);
                if (priority == by_id.end() ||
                    (priority->second->intent != UnitIntent::Seek &&
                     priority->second->intent != UnitIntent::Upgrade)) continue;
                const auto cost = unit_costs.find(id);
                if (cost == unit_costs.end() || cost->second < 0) {
                    ++out.rejected_missing_cost;
                    continue;
                }
                strategy::StrategicActionCandidate candidate;
                candidate.kind = strategy::StrategicActionKind::BuyUnit;
                candidate.champion_id = id;
                candidate.gold_cost = cost->second;
                candidate.direct_gold_cost = cost->second;
                candidate.expected_board_delta = priority->second->board_contribution;
                candidate.composition_fit = 1.0;
                candidate.upgrade_value = priority->second->target_star > 0 ? 1.0 : 0.0;
                candidate.shop_slot = static_cast<std::int32_t>(slot);
                candidate.available = cost->second <= context.gold;
                candidate.evidence_reason = "active_target_priority_and_exact_legal_shop_slot";
                append(std::move(candidate));
            }

            if (context.level < EconomyEngine::MAX_LEVEL &&
                context.xp_to_next > 0 && context.gold >= EconomyEngine::BUY_XP_COST &&
                type_enabled(decision::ActionType::BUY_XP)) {
                strategy::StrategicActionCandidate candidate;
                candidate.kind = strategy::StrategicActionKind::BuyExperience;
                candidate.gold_cost = EconomyEngine::BUY_XP_COST;
                candidate.direct_gold_cost = EconomyEngine::BUY_XP_COST;
                candidate.available = true;
                candidate.evidence_reason = "native_economy_xp_threshold_and_buy_xp_mask";
                append(std::move(candidate));
            }
            const bool has_upgrade_target = std::any_of(priorities.units.begin(),
                priorities.units.end(), [](const auto& unit) {
                    return unit.intent == UnitIntent::Seek || unit.intent == UnitIntent::Upgrade;
                });
            if (has_upgrade_target && context.gold >= EconomyEngine::REROLL_COST &&
                type_enabled(decision::ActionType::REROLL)) {
                strategy::StrategicActionCandidate candidate;
                candidate.kind = strategy::StrategicActionKind::RerollShop;
                candidate.gold_cost = EconomyEngine::REROLL_COST;
                candidate.direct_gold_cost = EconomyEngine::REROLL_COST;
                candidate.opportunity_cost = strategy::action_opportunity_cost::kRerollWithUpgradeTarget;
                candidate.available = true;
                candidate.evidence_reason = "upgrade_target_exists_and_native_reroll_mask";
                append(std::move(candidate));
            }

            // Sell only a uniquely identified bench instance explicitly marked
            // SellCandidate by UnitPriorityPlanner; never choose by incidental order.
            for (const auto& priority : priorities.units) {
                if (priority.intent != UnitIntent::SellCandidate ||
                    priority.sale_restricted || priority.copies_owned >= 2 ||
                    priority.highest_star > 1 || priority.target_star > 0 ||
                    target_ids.count(priority.champion_id)) continue;
                std::int32_t slot = -1;
                for (std::size_t i = 0; i < native.bench_champion_ids.size(); ++i) {
                    if (native.bench_champion_ids[i] != priority.champion_id) continue;
                    if (slot >= 0) { slot = -2; break; }
                    slot = static_cast<std::int32_t>(i);
                }
                if (slot == -2) { ++out.rejected_ambiguous_instance; continue; }
                if (slot < 0 || native.masks.bench_source_mask[static_cast<std::size_t>(slot)] != decision::MASK_ENABLED ||
                    !type_enabled(decision::ActionType::SELL)) continue;
                const auto cost = unit_costs.find(priority.champion_id);
                if (cost == unit_costs.end() || cost->second < 0) {
                    ++out.rejected_missing_cost;
                    continue;
                }
                strategy::StrategicActionCandidate candidate;
                candidate.kind = strategy::StrategicActionKind::SellUnit;
                candidate.champion_id = priority.champion_id;
                candidate.source_slot = slot;
                candidate.source_is_bench = true;
                candidate.direct_gold_cost = -static_cast<double>(
                    EconomyEngine::get_sell_value(cost->second, priority.highest_star));
                candidate.available = true;
                candidate.evidence_reason = "explicit_sell_candidate_unique_bench_instance";
                append(std::move(candidate));
            }

            // Generate concrete, legal destinations for each owned lineup member.
            for (const auto& slot : lineup.selected_board) {
                if (slot.champion_id < 0) continue;
                const auto unit = std::find_if(active->candidate.units.begin(),
                    active->candidate.units.end(), [&](const auto& item) {
                        return item.champion_id == slot.champion_id;
                    });
                if (unit == active->candidate.units.end()) continue;
                StrategicPositionSnapshot snapshot;
                snapshot.match_id = native.match_id;
                snapshot.player_id = native.player_id;
                snapshot.round = native.round;
                snapshot.sequence = native.sequence;
                snapshot.composition_id = native.composition_id;
                snapshot.composition_version = native.composition_version;
                snapshot.alive = native.alive;
                snapshot.requested_champion_id = slot.champion_id;
                snapshot.board_ids = native.board_champion_ids;
                snapshot.bench_ids = native.bench_champion_ids;
                snapshot.masks = native.masks;
                StrategicPositionRole role = StrategicPositionRole::Flex;
                switch (unit->role) {
                    case UnitRole::MainCarry: role = StrategicPositionRole::MainCarry; break;
                    case UnitRole::SecondaryCarry: role = StrategicPositionRole::SecondaryCarry; break;
                    case UnitRole::Frontline: role = StrategicPositionRole::Frontline; break;
                    case UnitRole::Support: role = StrategicPositionRole::Support; break;
                    case UnitRole::Flex: role = StrategicPositionRole::Flex; break;
                }
                snapshot.composition_units.push_back({unit->champion_id, role, unit->priority});
                auto proposal = StrategicPositionPlanner{}.plan(snapshot);
                if (!proposal.available()) continue;
                native.requested_move_targets.push_back({
                    proposal.champion_id, proposal.target_board_slot});
                strategy::StrategicActionCandidate candidate;
                candidate.kind = strategy::StrategicActionKind::DeployOrMove;
                candidate.champion_id = proposal.champion_id;
                candidate.expected_board_delta = std::max(0.0, proposal.improvement) / 100.0;
                candidate.composition_fit = 1.0;
                candidate.source_slot = proposal.source_slot;
                candidate.source_is_bench = proposal.source_zone == StrategicPositionZone::Bench;
                candidate.target_board_slot = proposal.target_board_slot;
                candidate.available = true;
                candidate.evidence_reason = "role_aware_position_proposal_with_current_native_masks";
                append(std::move(candidate));
                out.positioning.push_back(std::move(proposal));
            }
        }

        out.status = out.candidates.empty() ? "no_candidates" : "candidates_generated";
        return out;
    }
};

} // namespace tft::composition_intelligence
