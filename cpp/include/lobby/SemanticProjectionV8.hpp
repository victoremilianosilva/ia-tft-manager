#pragma once

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <string_view>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <nlohmann/json.hpp>

#include "lobby/TftEngine.hpp"
#include "lobby/SemanticSha256.hpp"

namespace tft::semantic_v8 {

using json = nlohmann::json;
inline constexpr std::size_t kGlobalFeatures = 70;
inline constexpr std::size_t kEntitySlots = 42;
inline constexpr std::size_t kEntityFeatures = 45;
inline constexpr std::size_t kTraitSlots = 10;
inline constexpr std::uint32_t kTraitVocab = 65536;

struct Projection {
    std::vector<double> numeric;
    std::array<std::int64_t, kEntitySlots> champion_ids{};
    std::array<bool, kEntitySlots> occupied{};
    std::array<std::string, kEntitySlots> unit_uuids{};
    std::array<std::uint64_t, kShopSlots> shop_offer_revisions{};
    json identity;
    json item_state_identity;
    std::string item_catalog_sha256;
    std::string sha256;
};

inline std::uint32_t trait_id(std::string_view trait) {
    const auto digest = tft::semantic::sha256_hex(trait);
    return static_cast<std::uint32_t>(std::stoul(digest.substr(0, 8), nullptr, 16))
        % kTraitVocab + 1;
}

inline json strings_json(const std::vector<std::string>& values) {
    return values;
}
inline json int_json(const std::vector<std::int32_t>& values) {
    return values;
}
template <std::size_t R, std::size_t C>
inline json matrix_json(const std::array<std::array<float, C>, R>& values) {
    json result = json::array();
    for (const auto& row : values) { json converted = json::array(); for (const auto value : row) converted.push_back(static_cast<double>(value)); result.push_back(std::move(converted)); }
    return result;
}
template <typename T, std::size_t N>
inline void append(std::vector<double>& out, const std::array<T, N>& values) {
    for (const auto value : values) out.push_back(static_cast<double>(value));
}
template <std::size_t R, std::size_t C>
inline void append(std::vector<float>& out, const std::array<std::array<float, C>, R>& values) {
    for (const auto& row : values) append(out, row);
}
inline void append(std::vector<float>& out, const std::array<float, 10>& values) {
    for (const auto value : values) out.push_back(static_cast<double>(value));
}
inline double normalized_feature(double value, double denominator) {
    return std::min(value / denominator, 1.0f);
}
inline double nonnegative(std::int32_t value) {
    return static_cast<double>(std::max(value, 0));
}
inline json priority_json(const std::vector<AuditUnitStrategicPrioritySnapshot>& rows) {
    json out = json::array();
    for (const auto& row : rows) {
        out.push_back({
            {"champion_internal_id", row.champion_internal_id},
            {"priority", row.priority},
            {"intent", row.intent},
            {"relation", row.relation},
            {"confidence", row.confidence},
            {"target_star", row.target_star},
            {"sale_restricted", row.sale_restricted}
        });
    }
    return out;
}
inline json opportunity_json(const std::vector<AuditUnitOpportunityCostSnapshot>& rows) {
    json out = json::array();
    for (const auto& row : rows) {
        out.push_back({
            {"champion_internal_id", row.champion_internal_id},
            {"value", row.value},
            {"uncertainty", row.uncertainty},
            {"horizon_rounds", row.horizon_rounds},
            {"source", row.source},
            {"forgone_candidate_id", row.forgone_candidate_id},
            {"value_basis", row.value_basis}
        });
    }
    return out;
}
inline json equipped_json(const std::vector<AuditEquippedItemSnapshot>& rows) {
    json out = json::array();
    for (const auto& row : rows) {
        out.push_back({
            {"unit_uuid", row.unit_uuid},
            {"location", row.location},
            {"slot", row.slot},
            {"catalog_id", row.catalog_id}
        });
    }
    return out;
}

inline Projection project_player(
    const AuditSnapshot& snapshot,
    std::size_t lobby_index,
    std::size_t player_index,
    const std::map<std::string, std::int32_t>& catalog
) {
    if (player_index >= kPlayersPerLobby) throw std::out_of_range("semantic player index");
    const auto& state = snapshot.players[player_index];
    const auto& strategic = state.strategic_state;
    if (state.player_id < 0 || strategic.player_id != state.player_id)
        throw std::runtime_error("semantic snapshot player identity mismatch");
    if (strategic.contract_id != "tft.strategic-owner-observation" ||
        strategic.contract_version != 3 ||
        strategic.producer != "TFTEngine::get_audit_snapshot" ||
        strategic.source_namespace != "tft.engine.strategic-owners")
        throw std::runtime_error("unsupported strategic owner snapshot contract");

    Projection result;
    result.numeric.reserve(7958);
    std::unordered_set<std::int32_t> active(strategic.active_unit_ids.begin(), strategic.active_unit_ids.end());
    std::unordered_set<std::int32_t> core(strategic.active_core_unit_ids.begin(), strategic.active_core_unit_ids.end());
    std::unordered_set<std::int32_t> direction(strategic.direction_reference_unit_ids.begin(), strategic.direction_reference_unit_ids.end());
    std::unordered_set<std::int32_t> pivot(strategic.pivot_reference_unit_ids.begin(), strategic.pivot_reference_unit_ids.end());
    std::unordered_set<std::int32_t> selected(strategic.lineup_selected_unit_ids.begin(), strategic.lineup_selected_unit_ids.end());
    std::unordered_set<std::int32_t> entry(strategic.lineup_entry_unit_ids.begin(), strategic.lineup_entry_unit_ids.end());
    std::unordered_set<std::int32_t> deferred(strategic.lineup_deferred_unit_ids.begin(), strategic.lineup_deferred_unit_ids.end());
    std::unordered_set<std::int32_t> target = selected;
    target.insert(entry.begin(), entry.end());
    target.insert(deferred.begin(), deferred.end());

    std::unordered_map<std::int32_t, AuditUnitCopyProgressSnapshot> progress;
    for (const auto& row : strategic.unit_copy_progress) progress.emplace(row.champion_internal_id, row);
    std::unordered_map<std::int32_t, AuditUnitStrategicPrioritySnapshot> priorities;
    for (const auto& row : strategic.unit_priorities) priorities.emplace(row.champion_internal_id, row);
    std::unordered_map<std::int32_t, AuditUnitOpportunityCostSnapshot> opportunities;
    for (const auto& row : strategic.opportunity_costs) opportunities.emplace(row.champion_internal_id, row);

    std::size_t board_count = 0, bench_count = 0;
    for (const auto& unit : state.board) board_count += unit.occupied ? 1 : 0;
    for (const auto& unit : state.bench) bench_count += unit.occupied ? 1 : 0;
    const auto placement = state.placement.value_or(0);
    const auto level = std::max(state.level, 0);

    auto& g = result.numeric;
    g.reserve(7958);
    g.push_back(static_cast<double>(state.hp / 100.0));
    g.push_back(static_cast<float>(state.damage_taken / 100.0));
    g.push_back(state.alive ? 1.0f : 0.0f);
    g.push_back(nonnegative(state.wins) / 100.0f);
    g.push_back(nonnegative(state.losses) / 100.0f);
    g.push_back(nonnegative(state.gold) / 200.0f);
    g.push_back(nonnegative(state.level) / 10.0f);
    g.push_back(nonnegative(state.xp) / 10.0f);
    g.push_back(nonnegative(state.win_streak) / 10.0f);
    g.push_back(nonnegative(state.loss_streak) / 10.0f);
    g.push_back(nonnegative(state.gold_before_interest) / 200.0f);
    g.push_back(nonnegative(state.interest_if_resolved_now) / 5.0f);
    g.push_back(state.placement ? static_cast<float>(placement) / 8.0f : 0.0f);
    g.push_back(state.placement ? 1.0f : 0.0f);
    g.push_back(state.opponent_id ? 1.0f : 0.0f);
    g.push_back(static_cast<float>(snapshot.stage) / 7.0f);
    g.push_back(static_cast<float>(snapshot.round) / 50.0f);
    g.push_back(strategic.active_composition_valid ? 1.0f : 0.0f);
    g.push_back(strategic.direction_valid ? 1.0f : 0.0f);
    g.push_back(strategic.pivot_candidate_valid ? 1.0f : 0.0f);
    g.push_back(strategic.opportunity_cost_available ? 1.0f : 0.0f);
    g.push_back(static_cast<float>(std::min<std::size_t>(level > board_count ? level - board_count : 0, 9)) / 9.0f);
    g.push_back(static_cast<float>(9 - bench_count) / 9.0f);
    g.push_back(static_cast<float>(std::min<std::uint32_t>(state.actions_taken_this_round, 10)) / 10.0f);
    for (const auto age : state.board_move_age)
        g.push_back(static_cast<float>(std::min<std::uint32_t>(age, 10)) / 10.0f);
    g.push_back(strategic.planner_outputs_valid ? 1.0f : 0.0f);
    g.push_back(strategic.strategic_refresh_failed ? 1.0f : 0.0f);
    g.push_back(static_cast<float>(state.board_quality_score));
    g.push_back(static_cast<float>(state.board_positional_score));
    g.push_back(static_cast<float>(state.board_structural_score));
    g.push_back(static_cast<float>(state.board_exposed_carries) / 9.0f);
    g.push_back(static_cast<float>(state.board_frontline_count) / 9.0f);
    g.push_back(static_cast<float>(state.board_isolated_frontline_count) / 9.0f);
    g.push_back(static_cast<float>(state.board_important_bench_units_unplayed) / 9.0f);
    g.push_back(static_cast<float>(state.board_frontline_lane_count) / 7.0f);
    g.push_back(static_cast<float>(state.board_exposed_main_carries) / 9.0f);
    g.push_back(static_cast<float>(state.board_fragile_frontline_count) / 9.0f);
    g.push_back(static_cast<float>(state.board_missing_frontline_count) / 9.0f);
    g.push_back(static_cast<float>(state.board_missing_backline_count) / 9.0f);
    g.push_back(static_cast<float>(state.board_active_trait_count) / 28.0f);
    g.push_back(static_cast<float>(state.board_strategic_fit_score));
    g.push_back(static_cast<float>(state.board_unit_quality_score));
    g.push_back(static_cast<float>(state.board_trait_coherence_score));
    if (g.size() != kGlobalFeatures) throw std::runtime_error("semantic global v8 layout mismatch");

    auto project_group = [&](const auto& units, std::size_t offset, bool shop) {
        for (std::size_t slot = 0; slot < units.size(); ++slot) {
            const auto& unit = units[slot];
            const auto entity_index = offset + slot;
            result.occupied[entity_index] = unit.occupied;
            result.unit_uuids[entity_index] = unit.uuid;
            if (!unit.occupied) {
                g.insert(g.end(), kEntityFeatures, 0.0f);
                result.champion_ids[entity_index] = 0;
                continue;
            }
            const auto found = catalog.find(unit.champion_id);
            const bool champion_valid = found != catalog.end() &&
                unit.champion_internal_id >= 0 && found->second == unit.champion_internal_id;
            const auto native_id = champion_valid ? unit.champion_internal_id : -1;
            const auto copy = progress.find(native_id);
            const auto copies = copy == progress.end() ? 0 : copy->second.owned_copy_equivalent;
            const auto toward = copy == progress.end() ? 0 : copy->second.copies_toward_next_star;
            const auto star = std::max(unit.star, 0);
            const auto cost = std::max(unit.cost, 0);
            g.insert(g.end(), {
                1.0f, static_cast<float>(star) / 3.0f, static_cast<float>(cost) / 5.0f,
                static_cast<float>(std::min<std::size_t>(unit.item_ids.size(), 9)) / 9.0f,
                static_cast<float>(std::min<std::size_t>(unit.trait_names.size(), 10)) / 10.0f,
                champion_valid ? 1.0f : 0.0f,
                native_id >= 0 && active.contains(native_id) ? 1.0f : 0.0f,
                native_id >= 0 && core.contains(native_id) ? 1.0f : 0.0f,
                native_id >= 0 && direction.contains(native_id) ? 1.0f : 0.0f,
                native_id >= 0 && pivot.contains(native_id) ? 1.0f : 0.0f,
                static_cast<float>(std::min(copies, 9)) / 9.0f,
                static_cast<float>(toward) / 2.0f
            });
            std::array<float, 17> target_profile{};
            if (!shop) {
                if (unit.role < 0 || unit.role > 4) throw std::runtime_error("semantic target role out of range");
                const auto role = unit.role;
                const bool on_board = offset == 0;
                target_profile[0] = 1.0f;
                target_profile[1] = on_board ? 1.0f : 0.0f;
                target_profile[2] = on_board ? 0.0f : 1.0f;
                target_profile[3] = static_cast<float>(star) / 3.0f;
                target_profile[4 + role] = 1.0f;
                target_profile[9] = on_board && slot / 7 <= 1 ? 1.0f : 0.0f;
                target_profile[10] = on_board && slot / 7 >= 2 ? 1.0f : 0.0f;
                target_profile[11] = unit.attack_damage <= 0.0 ? 0.0f : normalized_feature(static_cast<float>(unit.attack_damage), 200.0f);
                target_profile[12] = unit.attack_speed <= 0.0 ? 0.0f : normalized_feature(static_cast<float>(unit.attack_speed), 2.0f);
                target_profile[13] = unit.max_health <= 0.0 ? 0.0f : normalized_feature(static_cast<float>(unit.max_health), 2000.0f);
                target_profile[14] = unit.armor <= 0.0 ? 0.0f : normalized_feature(static_cast<float>(unit.armor), 150.0f);
                target_profile[15] = unit.magic_resist <= 0.0 ? 0.0f : normalized_feature(static_cast<float>(unit.magic_resist), 150.0f);
                target_profile[16] = static_cast<float>(std::min<std::size_t>(unit.item_ids.size(), 3)) / 3.0f;
            }
            append(g, target_profile);
            if (unit.trait_names.size() > kTraitSlots) throw std::runtime_error("semantic trait slot overflow");
            for (const auto& trait : unit.trait_names)
                g.push_back(static_cast<float>(trait_id(trait)) / static_cast<float>(kTraitVocab));
            g.insert(g.end(), kTraitSlots - unit.trait_names.size(), 0.0f);
            const auto p = priorities.find(native_id);
            const auto o = opportunities.find(native_id);
            g.push_back(p == priorities.end() ? 0.0f : static_cast<float>(std::min(p->second.priority, 100)) / 100.0f);
            g.push_back(p == priorities.end() ? 0.0f : static_cast<float>(p->second.intent) / 6.0f);
            g.push_back(native_id >= 0 && selected.contains(native_id) ? 1.0f : 0.0f);
            g.push_back(native_id >= 0 && target.contains(native_id) ? 1.0f : 0.0f);
            g.push_back(o == opportunities.end() ? 0.0f : static_cast<float>(std::min(o->second.value, 100.0)) / 100.0f);
            g.push_back(o == opportunities.end() ? 0.0f : 1.0f);
            result.champion_ids[entity_index] = native_id < 0 ? 0 : static_cast<std::int64_t>(native_id) + 1;
        }
    };
    project_group(state.board, 0, false);
    project_group(state.bench, kBoardSlots, false);
    project_group(state.shop, kBoardSlots + kBenchSlots, true);
    for (std::size_t i = 0; i < kShopSlots; ++i)
        result.shop_offer_revisions[i] = state.shop_offer_revisions[i];

    append(g, state.item_component_features);
    append(g, state.item_inventory_features);
    append(g, state.item_recipe_features);
    append(g, state.item_inventory_target_fit);
    append(g, state.item_recipe_target_fit);
    g.push_back(state.pending_anvil ? 1.0f : 0.0f);
    g.push_back(state.pending_anvil && state.pending_anvil_kind == 0 ? 1.0f : 0.0f);
    g.push_back(state.pending_anvil && state.pending_anvil_kind == 1 ? 1.0f : 0.0f);
    append(g, state.pending_anvil_option_features);
    if (g.size() != 7958) throw std::runtime_error("semantic numeric v8 dimension mismatch");

    json recipe = matrix_json(state.item_recipe_features);
    json catalog_payload = {
        {"component_ids", state.item_component_catalog},
        {"recipe_features", recipe}
    };
    result.item_catalog_sha256 = tft::semantic::sha256_hex(catalog_payload.dump(-1, ' ', false));
    result.identity = {
        {"engine_instance_id", snapshot.engine_instance_id},
        {"episode_id", snapshot.episode_id},
        {"decision_sequence", snapshot.snapshot_sequence},
        {"player_decision_sequence", snapshot.player_decision_sequences[player_index]},
        {"player_id", state.player_id},
        {"round", snapshot.round},
        {"lobby_index", lobby_index}
    };
    result.item_state_identity = {
        {"item_components", state.item_components},
        {"item_inventory", state.item_inventory},
        {"equipped_items", equipped_json(state.equipped_items)},
        {"item_component_catalog", state.item_component_catalog},
        {"item_catalog_sha256", result.item_catalog_sha256},
        {"pending_anvil", state.pending_anvil},
        {"pending_anvil_sequence", state.pending_anvil_sequence},
        {"pending_anvil_kind", state.pending_anvil_kind},
        {"pending_anvil_options", state.pending_anvil_options}
    };
    json strategic_provenance = {
        {"contract_id", strategic.contract_id},
        {"contract_version", strategic.contract_version},
        {"strategic_context_sequence", strategic.strategic_context_sequence},
        {"active_composition_id", strategic.active_composition_id},
        {"active_composition_version", strategic.active_composition_version},
        {"direction_identity", strategic.direction_identity},
        {"pivot_candidate_identity", strategic.pivot_candidate_identity},
        {"pivot_target_composition_identity", strategic.pivot_target_composition_identity},
        {"pivot_source_composition_version", strategic.pivot_source_composition_version},
        {"active_composition_valid", strategic.active_composition_valid},
        {"direction_valid", strategic.direction_valid},
        {"pivot_candidate_valid", strategic.pivot_candidate_valid},
        {"opportunity_cost_available", strategic.opportunity_cost_available},
        {"planner_outputs_valid", strategic.planner_outputs_valid},
        {"planner_output_sequence", strategic.planner_output_sequence},
        {"unit_priorities", priority_json(strategic.unit_priorities)},
        {"lineup_selected_unit_ids", strategic.lineup_selected_unit_ids},
        {"lineup_entry_unit_ids", strategic.lineup_entry_unit_ids},
        {"lineup_exit_unit_ids", strategic.lineup_exit_unit_ids},
        {"lineup_deferred_unit_ids", strategic.lineup_deferred_unit_ids},
        {"opportunity_costs", opportunity_json(strategic.opportunity_costs)},
        {"strategic_refresh_failed", strategic.strategic_refresh_failed},
        {"strategic_refresh_failure_reason", strategic.strategic_refresh_failure_reason}
    };
    json hash_payload = {
        {"identity", result.identity},
        {"numeric", g},
        {"champion_ids", result.champion_ids},
        {"item_state_identity", result.item_state_identity},
        {"strategic_owner_provenance", strategic_provenance}
    };
    result.sha256 = tft::semantic::sha256_hex(hash_payload.dump(-1, ' ', false));
    return result;
}

}  // namespace tft::semantic_v8
