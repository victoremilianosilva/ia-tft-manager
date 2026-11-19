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
    // Appended to preserve positional aggregate initialization.
    std::uint32_t rejected_missing_instance_identity{0};
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
            !native.alive || !context.alive || native.gold != context.gold ||
            !context.evidence.gold) {
            out.status = "invalid_or_mismatched_native_snapshot";
            return out;
        }
        if (!native.mask_generation_error.empty()) {
            out.status = "native_legality_unavailable:" + native.mask_generation_error;
            return out;
        }
        if (active && (native.composition_id != active->candidate.composition_id ||
            native.composition_version != active->version)) {
            out.status = "active_composition_identity_mismatch";
            return out;
        }
        const auto type_enabled = [&](decision::ActionType type) {
            return native.masks.type_mask[static_cast<std::size_t>(type)] == decision::MASK_ENABLED;
        };
        const auto make_id = [&](const strategy::StrategicActionCandidate& candidate) {
            return std::to_string(native.match_id) + ":" +
                std::to_string(native.player_id) + ":" +
                std::to_string(native.sequence) + ":" +
                native.composition_id + ":" + std::to_string(native.composition_version) + ":" +
                std::to_string(static_cast<int>(candidate.kind)) + ":" +
                candidate.source_unit_uuid + ":" + std::to_string(candidate.champion_id) + ":" +
                std::to_string(candidate.shop_slot) + ":" +
                std::to_string(candidate.source_slot) + ":" +
                std::to_string(candidate.target_board_slot) + ":" +
                (candidate.source_is_bench ? "bench" : "board");
        };
        const auto append = [&](strategy::StrategicActionCandidate candidate) {
            candidate.source_sequence = native.sequence;
            candidate.candidate_id = make_id(candidate);
            out.candidates.push_back(std::move(candidate));
        };
        const auto attach_marginal_interest = [&](strategy::StrategicActionCandidate& candidate) {
            if (!context.evidence.interest_if_resolved_now || candidate.gold_cost <= 0)
                return;
            const auto after_spend = std::max(0, context.gold - candidate.gold_cost);
            const auto remaining_interest = EconomyEngine{}.get_interest(after_spend);
            candidate.lost_interest_cost = std::max(0,
                context.interest_if_resolved_now - remaining_interest);
            candidate.lost_interest_evidence_available = true;
        };

        if (type_enabled(decision::ActionType::PASS)) {
            strategy::StrategicActionCandidate hold;
            hold.kind = strategy::StrategicActionKind::Hold;
            hold.evidence_reason = "explicit_neutral_baseline_no_action_value_claimed";
            hold.evidence_source = "native_pass_mask";
            hold.evidence_uncertainty = 1.0;
            append(std::move(hold));
        }

        // XP is an economy alternative even before an active composition exists.
        if (context.evidence.level && context.evidence.xp_to_next &&
            context.level < EconomyEngine::MAX_LEVEL &&
            context.xp_to_next > 0 && context.gold >= EconomyEngine::BUY_XP_COST &&
            type_enabled(decision::ActionType::BUY_XP)) {
            strategy::StrategicActionCandidate candidate;
            candidate.kind = strategy::StrategicActionKind::BuyExperience;
            candidate.gold_cost = EconomyEngine::BUY_XP_COST;
            candidate.direct_gold_cost = EconomyEngine::BUY_XP_COST;
            candidate.available = true;
            candidate.evidence_reason = "native_economy_xp_threshold_and_buy_xp_mask";
            candidate.evidence_source = "EconomyEngine+native_BUY_XP_mask";
            candidate.evidence_horizon_rounds = 1;
            candidate.evidence_uncertainty = 0.0;
            attach_marginal_interest(candidate);
            append(std::move(candidate));
        }

        // Before a composition is committed, native anchor hypotheses are the
        // only strategic target source. Permit a concrete shop BUY only when the
        // exact offer belongs to a generated anchor and the native mask allows it.
        if (!active && !context.anchor_candidates.empty() &&
            type_enabled(decision::ActionType::BUY)) {
            for (std::size_t slot = 0; slot < native.shop_champion_ids.size(); ++slot) {
                const auto id = native.shop_champion_ids[slot];
                if (id < 0 || native.masks.shop_mask[slot] != decision::MASK_ENABLED)
                    continue;
                const auto anchor = std::max_element(context.anchor_candidates.begin(),
                    context.anchor_candidates.end(), [&](const auto& left, const auto& right) {
                        const bool left_matches = left.unit.champion_id == id && left.shop_available;
                        const bool right_matches = right.unit.champion_id == id && right.shop_available;
                        if (left_matches != right_matches) return !left_matches;
                        return left.anchor_value < right.anchor_value;
                    });
                if (anchor == context.anchor_candidates.end() ||
                    anchor->unit.champion_id != id || !anchor->shop_available)
                    continue;
                const auto cost = unit_costs.find(id);
                if (cost == unit_costs.end() || cost->second < 0) {
                    ++out.rejected_missing_cost;
                    continue;
                }
                strategy::StrategicActionCandidate candidate;
                candidate.kind = strategy::StrategicActionKind::BuyUnit;
                candidate.champion_id = id;
                candidate.shop_slot = static_cast<std::int32_t>(slot);
                candidate.gold_cost = cost->second;
                candidate.direct_gold_cost = cost->second;
                candidate.expected_board_delta = std::clamp(
                    anchor->unit.board_contribution, 0.0, 1.0);
                candidate.composition_fit = std::clamp(
                    anchor->unit.composition_fit, 0.0, 1.0);
                candidate.upgrade_value = anchor->unit.copies_owned >= 2 ? 1.0 : 0.0;
                candidate.available = cost->second <= context.gold;
                candidate.opportunity_cost = strategy::action_opportunity_cost::kBuyUnit;
                candidate.evidence_reason = "native_anchor_hypothesis_and_exact_legal_shop_slot";
                candidate.evidence_source = "NativeStrategicCompositionGenerator+native_shop+native_BUY_mask";
                candidate.evidence_horizon_rounds = 1;
                candidate.evidence_uncertainty = 0.75;
                attach_marginal_interest(candidate);
                append(std::move(candidate));
            }
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
                candidate.opportunity_cost = strategy::action_opportunity_cost::kBuyUnit;
                candidate.evidence_reason = "active_target_priority_and_exact_legal_shop_slot";
                candidate.evidence_source = "native_shop+UnitPriorityPlanner+native_BUY_mask";
                candidate.evidence_horizon_rounds = 1;
                candidate.evidence_uncertainty = std::clamp(1.0 - priority->second->confidence, 0.0, 1.0);
                attach_marginal_interest(candidate);
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
                candidate.evidence_source = "UnitPriorityPlanner+native_REROLL_mask";
                candidate.evidence_horizon_rounds = 1;
                candidate.evidence_uncertainty = 1.0; // no probability model for future shop outcomes
                attach_marginal_interest(candidate);
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
                const auto& source_uuid = native.bench_unit_uuids[static_cast<std::size_t>(slot)];
                if (source_uuid.empty()) { ++out.rejected_missing_instance_identity; continue; }
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
                candidate.source_unit_uuid = source_uuid;
                candidate.direct_gold_cost = -static_cast<double>(
                    EconomyEngine::get_sell_value(cost->second, priority.highest_star));
                candidate.available = true;
                candidate.evidence_reason = "explicit_sell_candidate_unique_bench_instance";
                candidate.evidence_source = "TransitionManager+UnitPriorityPlanner+ItemEngine+native_SELL_mask";
                candidate.evidence_horizon_rounds = 0;
                candidate.evidence_uncertainty = std::clamp(1.0 - priority.confidence, 0.0, 1.0);
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
                candidate.source_unit_uuid = candidate.source_is_bench
                    ? native.bench_unit_uuids[static_cast<std::size_t>(proposal.source_slot)]
                    : native.board_unit_uuids[static_cast<std::size_t>(proposal.source_slot)];
                if (candidate.source_unit_uuid.empty()) {
                    ++out.rejected_missing_instance_identity;
                    continue;
                }
                candidate.target_board_slot = proposal.target_board_slot;
                candidate.available = true;
                candidate.evidence_reason = "role_aware_position_proposal_with_current_native_masks";
                candidate.evidence_source = "LineupPlanner+StrategicPositionPlanner+native_move_masks";
                candidate.evidence_horizon_rounds = 0;
                candidate.evidence_uncertainty = 1.0; // proposal has no calibrated confidence field
                append(std::move(candidate));
                out.positioning.push_back(std::move(proposal));
            }
        }

        out.status = out.candidates.empty() ? "no_candidates" : "candidates_generated";
        return out;
    }
};

} // namespace tft::composition_intelligence
