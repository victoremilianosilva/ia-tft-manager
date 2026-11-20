#pragma once
#include "composition_intelligence/ActiveCompositionManager.hpp"
#include "composition_intelligence/PlannerEvidenceAdapters.hpp"
#include "composition_intelligence/UnitPriorityPlanner.hpp"
#include <algorithm>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
namespace tft::composition_intelligence {
enum class LineupSlotKind { ActiveTarget, Bridge, Temporary };
struct LineupSlot {
    std::int32_t champion_id{-1};
    LineupSlotKind kind{LineupSlotKind::ActiveTarget};
    std::int32_t priority{0};
    bool currently_on_board{false};
    bool owned{false};
};
struct LineupTargetEntry {
    std::int32_t champion_id{-1};
    std::string availability{"priority_missing"};
    std::int32_t copies_owned{0};
    std::int32_t copies_in_shop{0};
    std::int32_t affordable_shop_copies{0};
    std::int32_t pool_remaining{-1};
    bool pool_known{false};
    bool owned{false};
    bool selected{false};
    bool deferred{true};
    std::string deferred_reason;
};
struct LineupPlannerContext {
    std::uint32_t level{1};
    std::uint32_t board_capacity{0};
    std::vector<std::int32_t> current_board_ids;
    const PlannerEvidenceSnapshot* planner_evidence{nullptr};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
};
struct LineupPlannerConfig {
    bool preserve_bridge_units{true};
    bool preserve_current_board_units{true};
};
struct LineupPlan {
    std::string composition_id;
    std::uint64_t composition_version{0};
    std::uint32_t level{0};
    std::uint32_t board_capacity{0};
    std::vector<std::int32_t> endgame_target_ids;
    std::vector<LineupSlot> selected_board;
    std::vector<LineupTargetEntry> target_states;
    std::vector<std::int32_t> entries;
    std::vector<std::int32_t> exits;
    std::vector<std::int32_t> deferred_target_ids;
    std::vector<std::int32_t> bridge_ids;
    bool stale{false};
    std::string stale_reason;
    std::string status;
    bool board_evidence_available{false};
    std::int32_t observed_frontline_count{-1};
    std::int32_t observed_carry_count{-1};
    std::int32_t observed_exposed_carry_count{-1};
    std::int32_t observed_missing_frontline_count{-1};
    std::int32_t observed_missing_backline_count{-1};
    std::string board_evidence_reason{"not_provided"};
};
class LineupPlanner {
public:
    explicit LineupPlanner(LineupPlannerConfig config = {}) : config_(config) {}
    LineupPlan plan(const std::optional<ActiveComposition>& active,
                    const UnitPrioritySnapshot& priorities,
                    const LineupPlannerContext& context) const {
        LineupPlan out;
        out.level = context.level;
        out.board_capacity = context.board_capacity;
        if (!active) { out.stale = true; out.stale_reason = "no active composition"; return out; }
        out.composition_id = active->candidate.composition_id;
        out.composition_version = active->version;
        if (priorities.stale || priorities.composition_id != active->candidate.composition_id ||
            priorities.composition_version != active->version) {
            out.stale = true;
            out.stale_reason = priorities.stale ? "unit priority snapshot is stale" :
                "unit priority composition identity/version mismatch";
            return out;
        }
        if (context.planner_evidence &&
            PlannerEvidenceAdapters::snapshot_identity_matches(*context.planner_evidence,
                context.match_id, context.player_id, active->candidate.composition_id,
                active->version, context.round)) {
            const auto& board = context.planner_evidence->board;
            if (PlannerEvidenceAdapters::source_matches(board.metadata, context.round)) {
                out.board_evidence_available = true;
                out.observed_frontline_count = board.frontline_count;
                out.observed_carry_count = board.carry_count;
                out.observed_exposed_carry_count = board.exposed_carry_count;
                out.observed_missing_frontline_count = board.missing_frontline_count;
                out.observed_missing_backline_count = board.missing_backline_count;
                out.board_evidence_reason = "validated_current_round_board_snapshot";
            } else out.board_evidence_reason = board.metadata.reason;
        } else if (context.planner_evidence) {
            out.board_evidence_reason = "planner_evidence_identity_mismatch";
        }
        if (context.board_capacity == 0 || context.board_capacity > 10) {
            out.stale = true; out.stale_reason = "board_capacity must be between 1 and 10"; return out;
        }
        std::unordered_set<std::int32_t> current;
        for (auto id : context.current_board_ids) if (id >= 0) current.insert(id);
        std::unordered_map<std::int32_t, const UnitPriority*> by_id;
        for (const auto& unit : priorities.units) if (unit.champion_id >= 0) by_id[unit.champion_id] = &unit;
        auto target = active->candidate.units;
        std::stable_sort(target.begin(), target.end(), [](const auto& a, const auto& b) {
            if (a.core != b.core) return a.core > b.core;
            if (a.priority != b.priority) return a.priority > b.priority;
            return a.champion_id < b.champion_id;
        });
        std::unordered_set<std::int32_t> target_ids;
        std::vector<LineupSlot> candidates, temporary;
        for (const auto& target_unit : target) {
            out.endgame_target_ids.push_back(target_unit.champion_id);
            target_ids.insert(target_unit.champion_id);
            const auto found = by_id.find(target_unit.champion_id);
            LineupTargetEntry target_state;
            target_state.champion_id = target_unit.champion_id;
            if (found == by_id.end()) {
                target_state.deferred_reason = "unit_priority_missing";
                out.target_states.push_back(std::move(target_state));
                out.deferred_target_ids.push_back(target_unit.champion_id);
                continue;
            }
            const auto& p = *found->second;
            target_state.copies_owned = std::max(0, p.copies_owned);
            target_state.copies_in_shop = std::max(0, p.copies_in_shop);
            target_state.affordable_shop_copies = std::max(0, p.affordable_shop_copies);
            target_state.pool_known = p.pool_known;
            target_state.pool_remaining = p.pool_known ? p.pool_remaining : -1;
            target_state.owned = p.copies_owned > 0;
            if (target_state.owned) {
                target_state.availability = p.on_board ? "owned_on_board" : "owned_on_bench";
            } else if (p.copies_in_shop > 0) {
                target_state.availability = "missing_in_shop";
            } else if (p.pool_known && p.pool_remaining == 0) {
                target_state.availability = "pool_exhausted";
            } else if (p.pool_known) {
                target_state.availability = "available_in_pool";
            } else {
                target_state.availability = "pool_unknown";
            }
            out.target_states.push_back(std::move(target_state));
            if (p.copies_owned <= 0) {
                out.deferred_target_ids.push_back(target_unit.champion_id);
                continue;
            }
            const auto role_gap_priority = out.board_evidence_available &&
                ((target_unit.role == UnitRole::Frontline && out.observed_missing_frontline_count > 0) ||
                 (target_unit.role == UnitRole::MainCarry &&
                  (out.observed_missing_backline_count > 0 || out.observed_exposed_carry_count > 0))) ? 25 : 0;
            candidates.push_back({target_unit.champion_id, LineupSlotKind::ActiveTarget,
                p.priority + role_gap_priority + (target_unit.core ? 1000 : 0),
                current.count(target_unit.champion_id) != 0, true});
        }
        for (const auto& p : priorities.units) {
            if (p.champion_id < 0 || p.copies_owned <= 0 || target_ids.count(p.champion_id)) continue;
            const bool on_board = current.count(p.champion_id) != 0;
            if (p.relation == UnitStrategicRelation::Bridge && config_.preserve_bridge_units) {
                temporary.push_back({p.champion_id, LineupSlotKind::Bridge, p.priority + 500, on_board, true});
            } else if (on_board && config_.preserve_current_board_units &&
                (p.intent == UnitIntent::Keep || p.intent == UnitIntent::Hold || p.intent == UnitIntent::Upgrade)) {
                temporary.push_back({p.champion_id, LineupSlotKind::Temporary, p.priority, true, true});
            }
        }
        auto ordering = [](const auto& a, const auto& b) {
            if (a.priority != b.priority) return a.priority > b.priority;
            if (a.currently_on_board != b.currently_on_board) return a.currently_on_board > b.currently_on_board;
            return a.champion_id < b.champion_id;
        };
        std::stable_sort(candidates.begin(), candidates.end(), ordering);
        std::stable_sort(temporary.begin(), temporary.end(), ordering);
        std::unordered_set<std::int32_t> selected;
        auto append = [&](const LineupSlot& slot) {
            if (out.selected_board.size() < context.board_capacity && selected.insert(slot.champion_id).second)
                out.selected_board.push_back(slot);
        };
        for (const auto& slot : candidates) append(slot);
        for (const auto& slot : temporary) append(slot);
        for (const auto& slot : out.selected_board) {
            if (!slot.currently_on_board) out.entries.push_back(slot.champion_id);
            if (slot.kind == LineupSlotKind::Bridge) out.bridge_ids.push_back(slot.champion_id);
        }
        // A target can be owned yet still deferred when the current capacity
        // cannot fit it. Keep that distinct from a missing target or unavailable pool.
        for (auto& target_state : out.target_states) {
            target_state.selected = selected.count(target_state.champion_id) != 0;
            target_state.deferred = !target_state.selected;
            if (target_state.deferred && target_state.deferred_reason.empty()) {
                if (target_state.owned) target_state.deferred_reason = "board_capacity";
                else if (target_state.availability == "missing_in_shop")
                    target_state.deferred_reason = "target_available_in_shop";
                else if (target_state.availability == "pool_exhausted")
                    target_state.deferred_reason = "pool_exhausted";
                else if (target_state.availability == "available_in_pool")
                    target_state.deferred_reason = "target_available_in_pool";
                else if (target_state.availability == "pool_unknown")
                    target_state.deferred_reason = "pool_availability_unknown";
                else target_state.deferred_reason = "target_not_owned";
            }
        }
        for (const auto id : out.endgame_target_ids)
            if (!selected.count(id)) out.deferred_target_ids.push_back(id);
        std::sort(out.deferred_target_ids.begin(), out.deferred_target_ids.end());
        out.deferred_target_ids.erase(
            std::unique(out.deferred_target_ids.begin(), out.deferred_target_ids.end()),
            out.deferred_target_ids.end());
        for (auto id : current) if (!selected.count(id)) out.exits.push_back(id);
        std::sort(out.entries.begin(), out.entries.end());
        std::sort(out.exits.begin(), out.exits.end());
        std::sort(out.bridge_ids.begin(), out.bridge_ids.end());
        out.status = out.deferred_target_ids.empty() ? "deployable_target" : "partial_target_waiting_for_units_or_capacity";
        return out;
    }
private:
    LineupPlannerConfig config_;
};
} // namespace tft::composition_intelligence
