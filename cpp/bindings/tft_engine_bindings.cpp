
#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <limits>
#include <optional>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "lobby/TftEngine.hpp"
#include "lobby/SemanticProjectionV8.hpp"
#include "lobby/NativeDecisionContext.hpp"
#include "lobby/NativeSpatialContext.hpp"
#include "strategy/PositioningEngine.hpp"
#include "reward/RewardManager.hpp"
#include "combat/CombatProfileEngine.hpp"
#include "strategy/SynergyEngine.hpp"

namespace py = pybind11;

namespace {

using tft::PlayerActionMasks;
using tft::TFTEngine;

template <std::size_t N>
py::array_t<float> readonly_float_view(
    const std::array<float, N>& source,
    py::handle owner
) {
    py::array_t<float> view(
        {static_cast<py::ssize_t>(N)},
        {static_cast<py::ssize_t>(sizeof(float))},
        source.data(),
        owner
    );
    view.attr("setflags")(false);
    return view;
}

template <std::size_t Rows, std::size_t Cols>
py::array_t<float> readonly_float_view(
    const std::array<std::array<float, Cols>, Rows>& source,
    py::handle owner
) {
    py::array_t<float> view(
        {static_cast<py::ssize_t>(Rows), static_cast<py::ssize_t>(Cols)},
        {static_cast<py::ssize_t>(Cols * sizeof(float)),
         static_cast<py::ssize_t>(sizeof(float))},
        source.front().data(),
        owner
    );
    view.attr("setflags")(false);
    return view;
}

template <std::size_t N>
py::array_t<bool> mask_1d(
    const std::array<std::uint8_t, N>& source
) {
    py::array_t<bool> result(static_cast<py::ssize_t>(N));
    auto out = result.mutable_unchecked<1>();
    for (std::size_t i = 0; i < N; ++i) {
        out(static_cast<py::ssize_t>(i)) = source[i] != 0;
    }
    return result;
}

template <std::size_t Rows, std::size_t Cols>
py::array_t<bool> mask_2d(
    const std::array<std::uint8_t, Rows * Cols>& source
) {
    py::array_t<bool> result({
        static_cast<py::ssize_t>(Rows),
        static_cast<py::ssize_t>(Cols)
    });
    auto out = result.mutable_unchecked<2>();
    for (std::size_t row = 0; row < Rows; ++row) {
        for (std::size_t col = 0; col < Cols; ++col) {
            out(static_cast<py::ssize_t>(row), static_cast<py::ssize_t>(col)) =
                source[row * Cols + col] != 0;
        }
    }
    return result;
}

// Snapshot serialization still needs its structured per-player mask mapping.
py::dict masks_to_dict(const PlayerActionMasks& masks) {
    py::dict result;
    result["type_mask"] = mask_1d(masks.type_mask);
    result["shop_mask"] = mask_1d(masks.shop_mask);
    result["bench_source_mask"] = mask_1d(masks.bench_source_mask);
    result["board_target_mask"] = mask_1d(masks.board_target_mask);
    result["board_source_mask"] = mask_1d(masks.board_source_mask);
    result["board_move_target_masks"] = mask_2d<28, 28>(masks.board_move_target_masks);
    result["bench_move_source_mask"] = mask_1d(masks.bench_move_source_mask);
    result["bench_to_board_target_masks"] = mask_2d<9, 28>(masks.bench_to_board_target_masks);
    result["item_inventory_mask"] = mask_1d(masks.item_inventory_mask);
    result["item_component_first_mask"] = mask_1d(masks.item_component_first_mask);
    result["item_component_pair_masks"] = mask_2d<10, 10>(masks.item_component_pair_masks);
    result["item_target_mask"] = mask_1d(masks.item_target_mask);
    return result;
}

// Preserve the structured public getter used by diagnostics and legacy callers.
py::list masks_to_list(
    const std::array<PlayerActionMasks, 8>& masks
) {
    py::list result;
    for (const auto& player_masks : masks) {
        result.append(masks_to_dict(player_masks));
    }
    return result;
}

// Stable packed layout shared with CppTFTLobbyWrapper._copy_action_masks.
// The field order matches action_contract.MASK_SHAPES exactly.
constexpr std::size_t kPackedActionMaskWidth =
    9 + 5 + 9 + 28 + 28 + (28 * 28) + 9 + (9 * 28) + 9 + 10 + (10 * 10) + 37;

template <std::size_t N>
void append_packed_mask(
    bool* destination,
    std::size_t& offset,
    const std::array<std::uint8_t, N>& source
) {
    for (const auto value : source) {
        destination[offset++] = value != 0;
    }
}

py::array_t<bool> masks_to_packed_array(
    const std::array<PlayerActionMasks, 8>& masks
) {
    py::array_t<bool> result({
        static_cast<py::ssize_t>(8),
        static_cast<py::ssize_t>(kPackedActionMaskWidth)
    });
    auto* destination = result.mutable_data();

    for (std::size_t player = 0; player < masks.size(); ++player) {
        std::size_t offset = player * kPackedActionMaskWidth;
        const auto& source = masks[player];
        bool* row = destination + offset;
        offset = 0;
        append_packed_mask(row, offset, source.type_mask);
        append_packed_mask(row, offset, source.shop_mask);
        append_packed_mask(row, offset, source.bench_source_mask);
        append_packed_mask(row, offset, source.board_target_mask);
        append_packed_mask(row, offset, source.board_source_mask);
        append_packed_mask(row, offset, source.board_move_target_masks);
        append_packed_mask(row, offset, source.bench_move_source_mask);
        append_packed_mask(row, offset, source.bench_to_board_target_masks);
        append_packed_mask(row, offset, source.item_inventory_mask);
        append_packed_mask(row, offset, source.item_component_first_mask);
        append_packed_mask(row, offset, source.item_component_pair_masks);
        append_packed_mask(row, offset, source.item_target_mask);
        if (offset != kPackedActionMaskWidth) {
            throw std::runtime_error("Layout compactado de action masks inconsistente.");
        }
    }

    return result;
}

py::array_t<float> observations_to_array(
    const std::vector<float>& values,
    std::size_t observation_dim
) {
    const std::size_t expected =
        tft::kPlayersPerLobby * observation_dim;

    if (values.size() != expected) {
        throw std::runtime_error(
            "Quantidade de observacoes inconsistente."
        );
    }

    py::array_t<float> result({
        static_cast<py::ssize_t>(tft::kPlayersPerLobby),
        static_cast<py::ssize_t>(observation_dim)
    });

    std::copy(
        values.begin(),
        values.end(),
        result.mutable_data()
    );

    return result;
}


py::dict player_info_to_dict(const tft::PlayerInfo& player) {
    py::dict result;

    result["player_id"] = player.player_id;
    result["hp"] = player.hp;
    result["gold"] = player.gold;
    result["level"] = player.level;
    result["xp"] = player.xp;

    result["alive"] = player.alive;
    result["eliminated"] = player.eliminated;

    result["wins"] = player.wins;
    result["losses"] = player.losses;

    result["placement"] = player.placement.has_value()
        ? py::cast(*player.placement)
        : py::none();

    result["opponent_id"] = player.opponent_id.has_value()
        ? py::cast(*player.opponent_id)
        : py::none();

    result["damage_taken"] = player.damage_taken;
    result["board_quality_score"] = player.board_quality_score;
    result["board_positional_score"] = player.board_positional_score;
    result["board_structural_score"] = player.board_structural_score;
    result["board_quality_delta"] = player.board_quality_delta;
    result["board_exposed_carries"] = player.board_exposed_carries;
    result["board_frontline_count"] = player.board_frontline_count;
    result["board_isolated_frontline_count"] =
        player.board_isolated_frontline_count;
    result["board_important_bench_units_unplayed"] =
        player.board_important_bench_units_unplayed;

    return result;
}


template <typename Players>
py::list player_info_to_list(const Players& players) {
    py::list result;

    for (const auto& player : players) {
        result.append(player_info_to_dict(player));
    }

    return result;
}

py::dict audit_player_snapshot_to_dict(
    const tft::AuditPlayerSnapshot& player,
    bool include_masks = true,
    py::object item_view_owner = py::none()
) {
    const auto unit_to_dict = [](const tft::AuditUnitSnapshot& unit) {
        py::dict d;
        d["occupied"] = unit.occupied;
        d["champion_internal_id"] = unit.champion_internal_id;
        d["champion_id"] = unit.champion_id;
        d["uuid"] = unit.uuid;
        d["star"] = unit.star;
        d["cost"] = unit.cost;
        d["items"] = unit.item_ids;
        d["trait_names"] = unit.trait_names;
        d["role"] = unit.role;
        d["attack_damage"] = unit.attack_damage;
        d["attack_speed"] = unit.attack_speed;
        d["max_health"] = unit.max_health;
        d["armor"] = unit.armor;
        d["magic_resist"] = unit.magic_resist;
        return d;
    };
    py::dict p;
        p["player_id"] = player.player_id;
        const auto& strategic = player.strategic_state;
        py::dict strategic_state;
        strategic_state["contract_id"] = strategic.contract_id;
        strategic_state["contract_version"] = strategic.contract_version;
        strategic_state["source_namespace"] = strategic.source_namespace;
        strategic_state["producer"] = strategic.producer;
        strategic_state["episode_id"] = strategic.episode_id;
        strategic_state["player_decision_sequence"] = strategic.player_decision_sequence;
        strategic_state["strategic_context_sequence"] = strategic.strategic_context_sequence;
        strategic_state["player_id"] = strategic.player_id;
        strategic_state["round"] = strategic.round;
        strategic_state["active_composition_valid"] = strategic.active_composition_valid;
        strategic_state["active_composition_id"] = strategic.active_composition_id;
        strategic_state["active_composition_version"] = strategic.active_composition_version;
        strategic_state["active_source_sequence"] = strategic.active_source_sequence;
        strategic_state["active_unit_ids"] = strategic.active_unit_ids;
        strategic_state["active_core_unit_ids"] = strategic.active_core_unit_ids;
        strategic_state["direction_valid"] = strategic.direction_valid;
        strategic_state["direction_identity"] = strategic.direction_identity;
        strategic_state["direction_selected_round"] = strategic.direction_selected_round;
        strategic_state["direction_reference_unit_ids"] = strategic.direction_reference_unit_ids;
        strategic_state["pivot_candidate_valid"] = strategic.pivot_candidate_valid;
        strategic_state["pivot_candidate_identity"] = strategic.pivot_candidate_identity;
        strategic_state["pivot_target_composition_identity"] = strategic.pivot_target_composition_identity;
        strategic_state["pivot_source_composition_version"] = strategic.pivot_source_composition_version;
        strategic_state["pivot_reference_unit_ids"] = strategic.pivot_reference_unit_ids;
        py::list unit_copy_progress;
        for (const auto& progress : strategic.unit_copy_progress) {
            py::dict row;
            row["champion_internal_id"] = progress.champion_internal_id;
            row["owned_copy_equivalent"] = progress.owned_copy_equivalent;
            row["copies_toward_next_star"] = progress.copies_toward_next_star;
            row["highest_star"] = progress.highest_star;
            unit_copy_progress.append(std::move(row));
        }
        strategic_state["unit_copy_progress"] = std::move(unit_copy_progress);
        strategic_state["opportunity_cost_available"] = strategic.opportunity_cost_available;
        strategic_state["planner_outputs_valid"] = strategic.planner_outputs_valid;
        strategic_state["planner_output_sequence"] = strategic.planner_output_sequence;
        py::list unit_priorities;
        for (const auto& priority : strategic.unit_priorities) {
            py::dict row;
            row["champion_internal_id"] = priority.champion_internal_id;
            row["intent"] = priority.intent;
            row["relation"] = priority.relation;
            row["priority"] = priority.priority;
            row["target_star"] = priority.target_star;
            row["sale_restricted"] = priority.sale_restricted;
            row["confidence"] = priority.confidence;
            unit_priorities.append(std::move(row));
        }
        strategic_state["unit_priorities"] = std::move(unit_priorities);
        py::list opportunity_costs;
        for (const auto& opportunity : strategic.opportunity_costs) {
            py::dict row;
            row["champion_internal_id"] = opportunity.champion_internal_id;
            row["value"] = opportunity.value;
            row["uncertainty"] = opportunity.uncertainty;
            row["horizon_rounds"] = opportunity.horizon_rounds;
            row["source"] = opportunity.source;
            row["forgone_candidate_id"] = opportunity.forgone_candidate_id;
            row["value_basis"] = opportunity.value_basis;
            opportunity_costs.append(std::move(row));
        }
        strategic_state["opportunity_costs"] = std::move(opportunity_costs);
        strategic_state["lineup_selected_unit_ids"] = strategic.lineup_selected_unit_ids;
        strategic_state["lineup_entry_unit_ids"] = strategic.lineup_entry_unit_ids;
        strategic_state["lineup_exit_unit_ids"] = strategic.lineup_exit_unit_ids;
        strategic_state["lineup_deferred_unit_ids"] = strategic.lineup_deferred_unit_ids;
        strategic_state["strategic_refresh_failed"] = strategic.strategic_refresh_failed;
        strategic_state["strategic_refresh_failure_reason"] =
            strategic.strategic_refresh_failure_reason;
        p["strategic_state"] = std::move(strategic_state);
        p["hp"] = player.hp;
        p["damage_taken"] = player.damage_taken;
        p["alive"] = player.alive;
        p["wins"] = player.wins;
        p["losses"] = player.losses;
        if (player.placement.has_value()) p["placement"] = *player.placement;
        else p["placement"] = py::none();
        if (player.opponent_id.has_value()) p["opponent_id"] = *player.opponent_id;
        else p["opponent_id"] = py::none();
        p["gold"] = player.gold;
        p["level"] = player.level;
        p["xp"] = player.xp;
        p["win_streak"] = player.win_streak;
        p["loss_streak"] = player.loss_streak;
        p["gold_before_interest"] = player.gold_before_interest;
        p["interest_if_resolved_now"] = player.interest_if_resolved_now;
        p["board_power"] = player.board_power;
        p["synergy_score"] = player.synergy_score;
        p["positioning_score"] = player.positioning_score;
        p["board_quality_score"] = player.board_quality_score;
        p["board_positional_score"] = player.board_positional_score;
        p["board_structural_score"] = player.board_structural_score;
        p["board_quality_delta"] = player.board_quality_delta;
        p["board_exposed_carries"] = player.board_exposed_carries;
        p["board_frontline_count"] = player.board_frontline_count;
        p["board_isolated_frontline_count"] = player.board_isolated_frontline_count;
        p["board_important_bench_units_unplayed"] = player.board_important_bench_units_unplayed;
        p["board_frontline_lane_count"] = player.board_frontline_lane_count;
        p["board_exposed_main_carries"] = player.board_exposed_main_carries;
        p["board_fragile_frontline_count"] = player.board_fragile_frontline_count;
        p["board_missing_frontline_count"] = player.board_missing_frontline_count;
        p["board_missing_backline_count"] = player.board_missing_backline_count;
        p["board_active_trait_count"] = player.board_active_trait_count;
        p["board_strategic_fit_score"] = player.board_strategic_fit_score;
        p["board_unit_quality_score"] = player.board_unit_quality_score;
        p["board_trait_coherence_score"] = player.board_trait_coherence_score;
        p["round_gold"] = player.round_gold;
        p["round_base_gold"] = player.round_base_gold;
        p["round_interest"] = player.round_interest;
        p["round_streak_gold"] = player.round_streak_gold;
        p["round_win_gold"] = player.round_win_gold;
        py::list board, bench, shop;
        for (const auto& unit : player.board) board.append(unit_to_dict(unit));
        for (const auto& unit : player.bench) bench.append(unit_to_dict(unit));
        for (const auto& unit : player.shop) shop.append(unit_to_dict(unit));
        p["board"] = board;
        p["bench"] = bench;
        p["shop"] = shop;
        p["shop_offer_revisions"] = player.shop_offer_revisions;
        p["item_components"] = player.item_components;
        p["item_inventory"] = player.item_inventory;
        py::list component_counts, inventory_counts, equipped_items;
        for (const auto& count : player.item_component_counts) { py::dict row; row["catalog_id"] = count.catalog_id; row["count"] = count.count; component_counts.append(std::move(row)); }
        for (const auto& count : player.item_inventory_counts) { py::dict row; row["catalog_id"] = count.catalog_id; row["count"] = count.count; inventory_counts.append(std::move(row)); }
        for (const auto& equipped : player.equipped_items) { py::dict row; row["unit_uuid"] = equipped.unit_uuid; row["location"] = equipped.location; row["slot"] = equipped.slot; row["catalog_id"] = equipped.catalog_id; equipped_items.append(std::move(row)); }
        p["item_component_counts"] = std::move(component_counts);
        p["item_inventory_counts"] = std::move(inventory_counts);
        p["equipped_items"] = std::move(equipped_items);
        p["item_ownership_retired"] = player.item_ownership_retired;
        py::list retired_component_counts, retired_inventory_counts, retired_equipped_counts, retired_anvils;
        for (const auto& count : player.retired_item_component_counts) { py::dict row; row["catalog_id"] = count.catalog_id; row["count"] = count.count; retired_component_counts.append(std::move(row)); }
        for (const auto& count : player.retired_item_inventory_counts) { py::dict row; row["catalog_id"] = count.catalog_id; row["count"] = count.count; retired_inventory_counts.append(std::move(row)); }
        for (const auto& equipped : player.retired_equipped_item_counts) { py::dict row; row["unit_uuid"] = equipped.unit_uuid; row["catalog_id"] = equipped.catalog_id; row["count"] = equipped.count; retired_equipped_counts.append(std::move(row)); }
        for (const auto& anvil : player.retired_pending_anvils) { py::dict row; row["sequence"] = anvil.sequence; row["kind"] = anvil.kind; row["options"] = anvil.options; retired_anvils.append(std::move(row)); }
        p["retired_item_component_counts"] = std::move(retired_component_counts);
        p["retired_item_inventory_counts"] = std::move(retired_inventory_counts);
        p["retired_equipped_item_counts"] = std::move(retired_equipped_counts);
        p["retired_pending_anvils"] = std::move(retired_anvils);
        p["item_component_catalog"] = player.item_component_catalog;
        p["pending_anvil"] = player.pending_anvil;
        p["pending_anvil_sequence"] = player.pending_anvil_sequence;
        p["pending_anvil_kind"] = player.pending_anvil_kind;
        p["pending_anvil_options"] = player.pending_anvil_options;
        if (item_view_owner.is_none()) {
            p["item_component_features"] = player.item_component_features;
            p["item_inventory_features"] = player.item_inventory_features;
            p["item_recipe_features"] = player.item_recipe_features;
            p["item_inventory_target_fit"] = player.item_inventory_target_fit;
            p["item_recipe_target_fit"] = player.item_recipe_target_fit;
            p["pending_anvil_option_features"] = player.pending_anvil_option_features;
        } else {
            p["item_component_features"] =
                readonly_float_view(player.item_component_features, item_view_owner);
            p["item_inventory_features"] =
                readonly_float_view(player.item_inventory_features, item_view_owner);
            p["item_recipe_features"] =
                readonly_float_view(player.item_recipe_features, item_view_owner);
            p["item_inventory_target_fit"] =
                readonly_float_view(player.item_inventory_target_fit, item_view_owner);
            p["item_recipe_target_fit"] =
                readonly_float_view(player.item_recipe_target_fit, item_view_owner);
            p["pending_anvil_option_features"] =
                readonly_float_view(player.pending_anvil_option_features, item_view_owner);
        }
        p["actions_taken_this_round"] = player.actions_taken_this_round;
        p["board_move_age"] = player.board_move_age;
        p["last_item_action_kind"] = player.last_item_action_kind;
        p["last_item_id"] = player.last_item_id;
        p["last_item_first_component"] = player.last_item_first_component;
        p["last_item_second_component"] = player.last_item_second_component;
        p["last_item_target_uuid"] = player.last_item_target_uuid;
        p["last_item_target_slot"] = player.last_item_target_slot;
        p["last_item_target_on_board"] = player.last_item_target_on_board;
        p["last_item_fit"] = player.last_item_fit;
        p["last_item_immediate_strength"] = player.last_item_immediate_strength;
        p["last_item_role_alignment"] = player.last_item_role_alignment;
        p["last_item_assignment_reward"] = player.last_item_assignment_reward;
        if (include_masks) p["action_masks"] = masks_to_dict(player.masks);
        return p;

}

py::dict audit_snapshot_to_dict(
    const tft::AuditSnapshot& snapshot,
    bool include_masks = true,
    bool include_combat_events = true,
    bool include_players = true
) {
    py::dict result;
    result["contract_id"] = snapshot.contract_id;
    result["contract_version"] = snapshot.contract_version;
    result["board_geometry_id"] = snapshot.board_geometry_id;
    result["board_geometry_version"] = snapshot.board_geometry_version;
    result["board_rows"] = snapshot.board_rows;
    result["board_columns"] = snapshot.board_columns;
    result["board_position_formula"] = snapshot.board_position_formula;
    result["source_namespace"] = snapshot.source_namespace;
    result["producer"] = snapshot.producer;
    result["engine_instance_id"] = snapshot.engine_instance_id;
    result["episode_id"] = snapshot.episode_id;
    result["snapshot_sequence"] = snapshot.snapshot_sequence;
    result["player_decision_sequences"] = snapshot.player_decision_sequences;
    result["round"] = snapshot.round;
    result["stage"] = snapshot.stage;
    result["finished"] = snapshot.finished;
    result["combat_sequence"] = snapshot.combat_sequence;
    result["combat_damage_events_truncated"] = snapshot.combat_damage_events_truncated;
    result["combat_attack_events_truncated"] = snapshot.combat_attack_events_truncated;
    result["combat_death_events_truncated"] = snapshot.combat_death_events_truncated;
    if (include_combat_events) {
            py::list combat_damage_events;
        for (const auto& event : snapshot.combat_damage_events) {
            py::dict row;
            row["combat_sequence"] = event.combat_sequence;
            row["timestamp"] = event.timestamp;
            row["source_unit_id"] = event.source_unit_id;
            row["target_unit_id"] = event.target_unit_id;
            row["source_player_id"] = event.source_player_id;
            row["target_player_id"] = event.target_player_id;
            row["source_unit_uuid"] = event.source_unit_uuid;
            row["target_unit_uuid"] = event.target_unit_uuid;
            row["damage_type"] = event.damage_type;
            row["raw_damage"] = event.raw_damage;
            row["final_damage"] = event.final_damage;
            row["critical"] = event.critical;
            row["ability_damage"] = event.ability_damage;
            combat_damage_events.append(std::move(row));
    }
        result["combat_damage_events"] = std::move(combat_damage_events);
        py::list combat_attack_events;
        for (const auto& event : snapshot.combat_attack_events) {
            py::dict row;
            row["combat_sequence"] = event.combat_sequence;
            row["timestamp"] = event.timestamp;
            row["source_unit_id"] = event.source_unit_id;
            row["target_unit_id"] = event.target_unit_id;
            row["source_player_id"] = event.source_player_id;
            row["target_player_id"] = event.target_player_id;
            row["source_unit_uuid"] = event.source_unit_uuid;
            row["target_unit_uuid"] = event.target_unit_uuid;
            row["critical"] = event.critical;
            row["damage"] = event.damage;
            combat_attack_events.append(std::move(row));
    }
        result["combat_attack_events"] = std::move(combat_attack_events);
        py::list combat_death_events;
        for (const auto& event : snapshot.combat_death_events) {
            py::dict row;
            row["combat_sequence"] = event.combat_sequence;
            row["timestamp"] = event.timestamp;
            row["unit_id"] = event.unit_id;
            row["killer_unit_id"] = event.killer_unit_id;
            row["unit_player_id"] = event.unit_player_id;
            row["killer_player_id"] = event.killer_player_id;
            row["unit_uuid"] = event.unit_uuid;
            row["killer_unit_uuid"] = event.killer_unit_uuid;
            combat_death_events.append(std::move(row));
    }
        result["combat_death_events"] = std::move(combat_death_events);
    }
    py::list economy_resolution_events;
    for (const auto& event : snapshot.economy_resolution_events) {
        py::dict row;
        row["contract_id"] = event.contract_id;
        row["contract_version"] = event.contract_version;
        row["source_namespace"] = event.source_namespace;
        row["producer"] = event.producer;
        row["player_id"] = event.player_id;
        row["resolved_after_round"] = event.resolved_after_round;
        row["income_for_round"] = event.income_for_round;
        row["old_gold"] = event.old_gold;
        row["gold_before_interest"] = event.gold_before_interest;
        row["gold_before_income"] = event.gold_before_income;
        row["new_gold"] = event.new_gold;
        row["base_gold"] = event.base_gold;
        row["interest_gold"] = event.interest_gold;
        row["streak_gold"] = event.streak_gold;
        row["win_gold"] = event.win_gold;
        row["total_gold"] = event.total_gold;
        row["old_level"] = event.old_level;
        row["new_level"] = event.new_level;
        row["leveled_up"] = event.leveled_up;
        row["xp"] = event.xp;
        row["xp_to_next"] = event.xp_to_next;
        economy_resolution_events.append(std::move(row));
    }
    result["economy_resolution_events"] = std::move(economy_resolution_events);
    py::list pvp_result_credit_events;
    for (const auto& event : snapshot.pvp_result_credit_events) {
        py::dict row;
        row["combat_sequence"] = event.combat_sequence;
        row["contract_id"] = event.contract_id;
        row["contract_version"] = event.contract_version;
        row["source_namespace"] = event.source_namespace;
        row["producer"] = event.producer;
        row["winner_player_id"] = event.winner_player_id;
        row["loser_player_id"] = event.loser_player_id;
        row["gold_before_credit"] = event.gold_before_credit;
        row["gold_after_credit"] = event.gold_after_credit;
        row["credited_gold"] = event.credited_gold;
        row["win_streak_before"] = event.win_streak_before;
        row["win_streak_after"] = event.win_streak_after;
        pvp_result_credit_events.append(std::move(row));
    }
    result["pvp_result_credit_events"] = std::move(pvp_result_credit_events);
    const auto& pool = snapshot.shared_pool;
    py::dict pool_dict;
    pool_dict["contract_id"] = pool.contract_id;
    pool_dict["contract_version"] = pool.contract_version;
    pool_dict["producer"] = pool.producer;
    pool_dict["catalog_fingerprint"] = pool.catalog_fingerprint;
    pool_dict["total_available"] = pool.total_available;
    py::list pool_champions;
    for (const auto& champion : pool.champions) {
        py::dict row;
        row["champion_internal_id"] = champion.champion_internal_id;
        row["champion_id"] = champion.champion_id;
        row["cost"] = champion.cost;
        row["initial_count"] = champion.initial_count;
        row["available_count"] = champion.available_count;
        pool_champions.append(std::move(row));
    }
    pool_dict["champions"] = std::move(pool_champions);
    result["shared_pool"] = std::move(pool_dict);
    if (include_players) {
        py::list players;
        for (const auto& player : snapshot.players) {
            players.append(audit_player_snapshot_to_dict(player, include_masks));
        }
        result["players"] = std::move(players);
    }
    return result;
}


class NativeAuditSnapshotHandle {
public:
    explicit NativeAuditSnapshotHandle(
        std::shared_ptr<const tft::AuditSnapshot> snapshot
    ) : snapshot_(std::move(snapshot)) {
        if (!snapshot_) {
            throw std::invalid_argument("Native audit snapshot handle is empty.");
        }
        const auto upper = snapshot_->combat_sequence;
        const auto validate_sequence = [upper](std::uint64_t sequence) {
            if (sequence == 0 || sequence > upper) {
                throw std::runtime_error("Invalid combat event sequence in native snapshot.");
            }
        };
        for (const auto& event : snapshot_->combat_damage_events) validate_sequence(event.combat_sequence);
        for (const auto& event : snapshot_->combat_attack_events) validate_sequence(event.combat_sequence);
        for (const auto& event : snapshot_->combat_death_events) validate_sequence(event.combat_sequence);

        // One capsule pins this immutable snapshot for every player view.
        // Individual NumPy arrays retain the capsule as their base, so they
        // remain valid even after this handle is released.
        auto* pinned_owner =
            new std::shared_ptr<const tft::AuditSnapshot>(snapshot_);
        item_view_owner_ = py::capsule(pinned_owner, [](void* pointer) {
            delete static_cast<std::shared_ptr<const tft::AuditSnapshot>*>(pointer);
        });
    }

    py::object to_envelope_dict() const {
        // The training adapter consumes envelope metadata separately from
        // player records. Keep this cache independent from public to_dict().
        if (!frozen_envelope_cache_) {
            py::object mutable_envelope =
                audit_snapshot_to_dict(*snapshot_, false, false, false);
            frozen_envelope_cache_ =
                py::module_::import("immutable_snapshot")
                    .attr("freeze_snapshot")(mutable_envelope);
        }
        return frozen_envelope_cache_;
    }

    py::object to_dict() const {
        // Preserve the public complete-snapshot contract for existing callers.
        if (!frozen_snapshot_cache_) {
            py::object mutable_snapshot =
                audit_snapshot_to_dict(*snapshot_, false, false, true);
            frozen_snapshot_cache_ =
                py::module_::import("immutable_snapshot")
                    .attr("freeze_snapshot")(mutable_snapshot);
        }
        return frozen_snapshot_cache_;
    }

    py::dict player(std::size_t index) const {
        if (index >= snapshot_->players.size()) {
            throw py::index_error("native snapshot player index out of range");
        }

        // Every view shares the handle's single snapshot-pinning capsule.
        // NumPy retains its base object independently of this handle.
        return audit_player_snapshot_to_dict(
            snapshot_->players[index],
            false,
            item_view_owner_
        );
    }

    std::size_t player_count() const noexcept {
        return snapshot_->players.size();
    }

    std::shared_ptr<const tft::AuditSnapshot> shared_snapshot() const noexcept {
        return snapshot_;
    }

    py::list keys() const {
        static constexpr const char* fields[] = {
            "contract_id",
            "contract_version",
            "board_geometry_id",
            "board_geometry_version",
            "board_rows",
            "board_columns",
            "board_position_formula",
            "source_namespace",
            "producer",
            "engine_instance_id",
            "episode_id",
            "snapshot_sequence",
            "player_decision_sequences",
            "round",
            "stage",
            "finished",
            "combat_sequence",
            "combat_damage_events_truncated",
            "combat_attack_events_truncated",
            "combat_death_events_truncated",
            "economy_resolution_events",
            "pvp_result_credit_events",
            "shared_pool",
            "players",
            "combat_damage_events",
            "combat_attack_events",
            "combat_death_events"
        };
        py::list result;
        for (const auto* field : fields) result.append(field);
        return result;
    }

    py::object item(const std::string& field) const {
        if (field == "combat_damage_events" ||
            field == "combat_attack_events" ||
            field == "combat_death_events") {
            return combat_events(field);
        }
        const py::object values = to_dict();
        PyObject* value = PyDict_GetItemString(values.ptr(), field.c_str());
        if (value == nullptr) {
            throw py::key_error(field);
        }
        return py::reinterpret_borrow<py::object>(value);
    }

    py::object get(
        const std::string& field,
        py::object default_value = py::none()
    ) const {
        if (field == "combat_damage_events" ||
            field == "combat_attack_events" ||
            field == "combat_death_events") {
            return combat_events(field);
        }
        const py::object values = to_dict();
        PyObject* value = PyDict_GetItemString(values.ptr(), field.c_str());
        if (value == nullptr) return default_value;
        return py::reinterpret_borrow<py::object>(value);
    }

    py::list combat_events(const std::string& field) const {
        py::list result;
        if (field == "combat_damage_events") {
            for (const auto& event : snapshot_->combat_damage_events) {
                py::dict row;
                row["combat_sequence"] = event.combat_sequence;
                row["timestamp"] = event.timestamp;
                row["source_unit_id"] = event.source_unit_id;
                row["target_unit_id"] = event.target_unit_id;
                row["source_player_id"] = event.source_player_id;
                row["target_player_id"] = event.target_player_id;
                row["source_unit_uuid"] = event.source_unit_uuid;
                row["target_unit_uuid"] = event.target_unit_uuid;
                row["damage_type"] = event.damage_type;
                row["raw_damage"] = event.raw_damage;
                row["final_damage"] = event.final_damage;
                row["critical"] = event.critical;
                row["ability_damage"] = event.ability_damage;
                result.append(std::move(row));
            }
            return result;
        }
        if (field == "combat_attack_events") {
            for (const auto& event : snapshot_->combat_attack_events) {
                py::dict row;
                row["combat_sequence"] = event.combat_sequence;
                row["timestamp"] = event.timestamp;
                row["source_unit_id"] = event.source_unit_id;
                row["target_unit_id"] = event.target_unit_id;
                row["source_player_id"] = event.source_player_id;
                row["target_player_id"] = event.target_player_id;
                row["source_unit_uuid"] = event.source_unit_uuid;
                row["target_unit_uuid"] = event.target_unit_uuid;
                row["critical"] = event.critical;
                row["damage"] = event.damage;
                result.append(std::move(row));
            }
            return result;
        }
        if (field == "combat_death_events") {
            for (const auto& event : snapshot_->combat_death_events) {
                py::dict row;
                row["combat_sequence"] = event.combat_sequence;
                row["timestamp"] = event.timestamp;
                row["unit_id"] = event.unit_id;
                row["killer_unit_id"] = event.killer_unit_id;
                row["unit_player_id"] = event.unit_player_id;
                row["killer_player_id"] = event.killer_player_id;
                row["unit_uuid"] = event.unit_uuid;
                row["killer_unit_uuid"] = event.killer_unit_uuid;
                result.append(std::move(row));
            }
            return result;
        }
        throw py::key_error(field);
    }

public:
    const tft::AuditSnapshot& snapshot() const noexcept { return *snapshot_; }

private:
    std::shared_ptr<const tft::AuditSnapshot> snapshot_;
    py::object item_view_owner_;
    mutable py::object frozen_snapshot_cache_;
    mutable py::object frozen_envelope_cache_;
};

py::dict semantic_projection_from_snapshot_mappings(
    const py::sequence& snapshot_mappings,
    const py::dict& catalog_map,
    const std::string& contract_hash,
    py::object batch_owner = py::none()
) {
    std::map<std::string, std::int32_t> catalog;
    for (const auto& entry : catalog_map) {
        const auto name = py::cast<std::string>(entry.first);
        const auto id = py::cast<std::int32_t>(entry.second);
        catalog.emplace(name, id);
    }

    constexpr std::size_t numeric_dim = 7958;
    const auto lobby_count = static_cast<py::ssize_t>(py::len(snapshot_mappings));
    if (lobby_count <= 0) throw py::value_error("semantic projection requires at least one native snapshot");
    py::array_t<float> numeric({lobby_count, static_cast<py::ssize_t>(tft::kPlayersPerLobby),
        static_cast<py::ssize_t>(numeric_dim)});
    py::array_t<std::int64_t> champion_ids(py::array::ShapeContainer{
        lobby_count, static_cast<py::ssize_t>(tft::kPlayersPerLobby), static_cast<py::ssize_t>(42)});
    py::array_t<std::int64_t> trait_ids(py::array::ShapeContainer{
        lobby_count, static_cast<py::ssize_t>(tft::kPlayersPerLobby),
        static_cast<py::ssize_t>(42), static_cast<py::ssize_t>(10)});
    auto* numeric_data = numeric.mutable_data();
    auto* champion_data = champion_ids.mutable_data();
    auto* trait_data = trait_ids.mutable_data();
    py::list hashes;
    py::list identities;
    py::list entity_identity;
    std::string item_catalog_hash;

    for (py::ssize_t lobby_index = 0; lobby_index < lobby_count; ++lobby_index) {
        py::object snapshot_mapping =
            py::reinterpret_borrow<py::object>(snapshot_mappings[lobby_index]);
        py::object native_handle = py::getattr(snapshot_mapping, "_handle", snapshot_mapping);
        auto handle = native_handle.cast<NativeAuditSnapshotHandle>();
        const auto& snapshot = handle.snapshot();
        for (std::size_t player = 0; player < tft::kPlayersPerLobby; ++player) {
            auto projected = tft::semantic_v8::project_player(
                snapshot, static_cast<std::size_t>(lobby_index), player, catalog);
            const auto row = static_cast<std::size_t>(lobby_index) * tft::kPlayersPerLobby + player;
            std::transform(projected.numeric.begin(), projected.numeric.end(),
                numeric_data + row * numeric_dim,
                [](double value) { return static_cast<float>(value); });
            std::copy(projected.champion_ids.begin(), projected.champion_ids.end(),
                champion_data + row * 42);
            for (std::size_t slot = 0; slot < 42; ++slot) {
                std::copy(projected.trait_ids[slot].begin(), projected.trait_ids[slot].end(),
                    trait_data + row * 42 * 10 + slot * 10);
            }
            hashes.append(projected.sha256);

            py::dict identity;
            identity["engine_instance_id"] = snapshot.engine_instance_id;
            identity["episode_id"] = snapshot.episode_id;
            identity["decision_sequence"] = snapshot.snapshot_sequence;
            identity["player_decision_sequence"] = snapshot.player_decision_sequences[player];
            identity["player_id"] = snapshot.players[player].player_id;
            identity["round"] = snapshot.round;
            identity["lobby_index"] = lobby_index;
            identities.append(std::move(identity));

            py::dict physical;
            py::tuple occupied(42), unit_uuids(42), shop_revisions(5);
            for (std::size_t slot = 0; slot < 42; ++slot) {
                occupied[slot] = projected.occupied[slot];
                unit_uuids[slot] = projected.unit_uuids[slot];
            }
            for (std::size_t slot = 0; slot < 5; ++slot)
                shop_revisions[slot] = projected.shop_offer_revisions[slot];
            physical["occupied"] = std::move(occupied);
            physical["unit_uuids"] = std::move(unit_uuids);
            physical["shop_offer_revisions"] = std::move(shop_revisions);
            entity_identity.append(std::move(physical));

            if (item_catalog_hash.empty()) item_catalog_hash = projected.item_catalog_sha256;
            else if (item_catalog_hash != projected.item_catalog_sha256)
                throw std::runtime_error("native players disagree on item catalog fingerprint");
        }
    }

    numeric.attr("setflags")(false);
    champion_ids.attr("setflags")(false);
    trait_ids.attr("setflags")(false);

    // The flattened v8 carrier is the single allocation. When projection
    // originates from NativeDecisionBatch, the item views' base bundle pins
    // both that carrier and the batch owner for the entire view lifetime.
    py::object item_view_owner = numeric;
    if (!batch_owner.is_none()) {
        py::dict owner_bundle;
        owner_bundle["batch"] = std::move(batch_owner);
        owner_bundle["numeric"] = numeric;
        item_view_owner = std::move(owner_bundle);
    }
    constexpr py::ssize_t global_offset = 70;
    constexpr py::ssize_t entity_width = 42 * 45;
    constexpr py::ssize_t item_offset = global_offset + entity_width;
    const auto make_item_view = [&](py::ssize_t offset,
                                    std::vector<py::ssize_t> shape) {
        if (shape.size() < 3)
            throw std::runtime_error("semantic item view requires lobby, player and feature dimensions");
        std::vector<py::ssize_t> strides(shape.size());
        py::ssize_t stride = static_cast<py::ssize_t>(sizeof(float));
        for (std::size_t i = shape.size(); i-- > 2;) {
            strides[i] = stride;
            stride *= shape[i];
        }
        // The numeric carrier is row-major [lobby, player, 7958]. A feature
        // block is therefore a zero-copy strided view: each player row starts
        // at the next full semantic row, not immediately after the prior
        // player's slice. Claiming C-contiguity here would silently read
        // unrelated features as the next player's item block.
        strides[1] = static_cast<py::ssize_t>(numeric_dim * sizeof(float));
        strides[0] = static_cast<py::ssize_t>(tft::kPlayersPerLobby * numeric_dim * sizeof(float));
        py::array view(
            py::dtype::of<float>(), shape, strides,
            numeric_data + offset, item_view_owner
        );
        view.attr("setflags")(false);
        return view;
    };
    py::dict item_blocks;
    py::ssize_t item_cursor = item_offset;
    const auto add_item_block = [&](const char* name,
                                    std::initializer_list<py::ssize_t> tail_shape,
                                    py::ssize_t element_count) {
        std::vector<py::ssize_t> shape{
            lobby_count, static_cast<py::ssize_t>(tft::kPlayersPerLobby)
        };
        shape.insert(shape.end(), tail_shape.begin(), tail_shape.end());
        item_blocks[name] = make_item_view(item_cursor, std::move(shape));
        item_cursor += element_count;
    };
    add_item_block("components", {10}, 10);
    add_item_block("inventory", {9, 17}, 9 * 17);
    add_item_block("recipes", {100, 17}, 100 * 17);
    add_item_block("inventory_target_fit", {9, 37}, 9 * 37);
    add_item_block("recipe_target_fit", {100, 37}, 100 * 37);
    item_cursor += 3;  // anvil state is exposed separately below
    add_item_block("anvil_options", {9, 11}, 9 * 11);
    if (item_cursor != static_cast<py::ssize_t>(numeric_dim))
        throw std::runtime_error("native semantic item block offsets do not cover v8 carrier");
    item_blocks["anvil_state"] = make_item_view(
        item_offset + 10 + 9 * 17 + 100 * 17 + 9 * 37 + 100 * 37,
        {lobby_count, static_cast<py::ssize_t>(tft::kPlayersPerLobby), 3}
    );

    py::dict result;
    result["numeric"] = numeric;
    result["item_blocks"] = std::move(item_blocks);
    result["champion_ids"] = std::move(champion_ids);
    result["trait_ids"] = std::move(trait_ids);
    result["hashes"] = std::move(hashes);
    result["identities"] = std::move(identities);
    result["entity_identity"] = std::move(entity_identity);
    if (item_catalog_hash.empty()) result["item_catalog_sha256"] = py::none();
    else result["item_catalog_sha256"] = item_catalog_hash;
    result["contract_id"] = "tft.ppo.semantic-native-state.v8";
    result["contract_hash"] = contract_hash;
    return result;
}

py::dict reset_to_dict(tft::ResetResult reset, bool include_numeric_transport = true) {
    py::dict result;

    if (include_numeric_transport) {
        result["observations"] = observations_to_array(
            reset.observations,
            reset.observation_dim
        );
        result["action_masks"] = masks_to_packed_array(reset.action_masks);
    }

    result["engine_instance_id"] = reset.engine_instance_id;
    result["episode_id"] = reset.episode_id;
    result["decision_sequence"] = reset.decision_sequence;
    result["player_decision_sequences"] = reset.player_decision_sequences;
    result["native_state_snapshot"] = NativeAuditSnapshotHandle(
        std::make_shared<const tft::AuditSnapshot>(std::move(reset.native_state_snapshot))
    );
    result["observation_dim"] = reset.observation_dim;

    return result;
}

py::dict step_to_dict(tft::StepResult step, bool include_numeric_transport = true) {
    py::dict result;
    result["action_context_contract_id"] = "tft.engine.action-context";
    result["action_context_contract_version"] = 1;
    result["action_mask_contract_id"] = "tft.action-masks.packed";
    result["action_mask_contract_version"] = 1;
    result["action_mask_layout"] = "type,shop,bench_source,board_target,board_source,board_move_target,bench_move_source,bench_to_board_target,item_inventory,item_component_first,item_component_pair,item_target";

    if (include_numeric_transport) {
        result["observations"] = observations_to_array(step.observations, step.observation_dim);
        result["action_masks"] = masks_to_packed_array(step.action_masks);
        py::array_t<float> rewards(8);
        py::array_t<float> action_rewards(8);
        py::array_t<float> combat_rewards(8);
        py::array_t<float> placement_rewards(8);
        py::array_t<bool> dones(8);
        auto reward_out = rewards.mutable_unchecked<1>();
        auto action_reward_out = action_rewards.mutable_unchecked<1>();
        auto combat_reward_out = combat_rewards.mutable_unchecked<1>();
        auto placement_reward_out = placement_rewards.mutable_unchecked<1>();
        auto done_out = dones.mutable_unchecked<1>();
        for (py::ssize_t i = 0; i < 8; ++i) {
            const auto index = static_cast<std::size_t>(i);
            reward_out(i) = step.rewards[index];
            action_reward_out(i) = step.action_rewards[index];
            combat_reward_out(i) = step.combat_rewards[index];
            placement_reward_out(i) = step.placement_rewards[index];
            done_out(i) = step.dones[index] != 0;
        }
        result["rewards"] = std::move(rewards);
        result["action_rewards"] = std::move(action_rewards);
        result["combat_rewards"] = std::move(combat_rewards);
        result["placement_rewards"] = std::move(placement_rewards);
        result["dones"] = std::move(dones);
    }
    result["lobby_done"] = step.lobby_done;
    result["engine_instance_id"] = step.engine_instance_id;
    result["episode_id"] = step.episode_id;
    result["decision_sequence"] = step.decision_sequence;
    result["player_decision_sequences"] = step.player_decision_sequences;
    result["native_state_snapshot"] = NativeAuditSnapshotHandle(
        std::make_shared<const tft::AuditSnapshot>(std::move(step.native_state_snapshot))
    );
    result["round"] = step.round;
    result["stage"] = step.stage;
    result["alive_players"] = step.alive_players;
    result["players"] = player_info_to_list(step.players);
    py::list action_traces;
    for (const auto& trace : step.action_traces) {
        py::dict item;
        item["player_id"] = trace.player_id;
        item["requested_action"] = trace.requested_action;
        item["effective_action"] = trace.effective_action;
        item["handler_applied"] = trace.handler_applied;
        item["status_reason"] = trace.status_reason;
        action_traces.append(std::move(item));
    }
    result["action_traces"] = std::move(action_traces);
    py::list action_outcome_events;
    for (const auto& event : step.action_outcome_events) {
        py::dict item;
        item["contract_id"] = event.contract_id;
        item["contract_version"] = event.contract_version;
        item["event_id"] = event.event_id;
        item["engine_instance_id"] = event.engine_instance_id;
        item["episode_id"] = event.episode_id;
        item["player_id"] = event.player_id;
        item["source_player_decision_sequence"] = event.source_player_decision_sequence;
        item["outcome_player_decision_sequence"] = event.outcome_player_decision_sequence;
        item["event_sequence"] = event.event_sequence;
        item["action_type"] = event.action_type;
        item["action_family"] = event.action_family;
        item["requested_action"] = event.requested_action;
        item["normalized_action"] = event.normalized_action;
        item["effective_action"] = event.effective_action;
        item["mask_permitted"] = event.mask_permitted;
        item["preflight_accepted"] = event.preflight_accepted;
        item["handler_applied"] = event.handler_applied;
        item["decision_advanced"] = event.decision_advanced;
        item["status_reason"] = event.status_reason;
        item["status_detail"] = event.status_detail;
        item["candidate_unit_uuids"] = event.candidate_unit_uuids;
        item["affected_unit_uuids"] = event.affected_unit_uuids;
        item["catalog_champion_id"] = event.catalog_champion_id;
        item["item_action_kind"] = event.item_action_kind;
        item["item_id"] = event.item_id;
        item["first_component_id"] = event.first_component_id;
        item["second_component_id"] = event.second_component_id;
        item["gold_before"] = event.gold_before;
        item["gold_after"] = event.gold_after;
        item["gold_delta"] = event.gold_delta;
        item["xp_before"] = event.xp_before;
        item["xp_after"] = event.xp_after;
        item["level_before"] = event.level_before;
        item["level_after"] = event.level_after;
        item["action_cost"] = event.action_cost;
        item["sale_proceeds"] = event.sale_proceeds;
        item["auto_merge"] = event.auto_merge;
        action_outcome_events.append(std::move(item));
    }
    result["action_outcome_events"] = std::move(action_outcome_events);
    result["events"] = step.events;

    return result;
}


py::dict public_state_to_dict(const tft::PublicState& state) {
    py::dict result;

    result["stage"] = state.stage;
    result["round"] = state.round;
    result["round_index"] = state.round_index;
    result["finished"] = state.finished;

    result["winner_id"] = state.winner_id.has_value()
        ? py::cast(*state.winner_id)
        : py::none();

    result["ranking"] = state.ranking;

    py::list alive_players;
    for (const auto player_id : state.alive_players) {
        alive_players.append(player_id);
    }
    result["alive_players"] = std::move(alive_players);

    result["players"] = player_info_to_list(state.players);

    return result;
}


py::dict anti_loop_to_dict(
    const std::array<
        tft::AntiLoopMetrics,
        tft::kPlayersPerLobby
    >& metrics
) {
    py::dict result;

    std::uint64_t execution_attempts = 0;
    std::uint64_t execution_blocks = 0;
    std::uint64_t blocked_reverse = 0;
    std::uint64_t blocked_oscillation = 0;
    std::uint64_t blocked_explicit = 0;
    std::uint64_t blocked_bench_board_loop = 0;
    std::uint64_t blocked_cycle = 0;
    std::uint64_t board_moves_executed = 0;
    std::uint64_t bench_to_board_executed = 0;
    std::uint64_t mask_board_move_candidates = 0;
    std::uint64_t mask_board_move_valid = 0;
    std::uint64_t mask_board_move_blocked_anti_loop = 0;
    std::uint64_t mask_board_move_blocked_seen_state = 0;
    std::uint64_t mask_bench_move_candidates = 0;
    std::uint64_t mask_bench_move_valid = 0;
    std::uint64_t mask_bench_move_blocked_anti_loop = 0;
    std::uint64_t mask_bench_move_blocked_seen_state = 0;
    std::uint64_t mask_blocked_reverse = 0;
    std::uint64_t mask_blocked_oscillation = 0;
    std::uint64_t mask_blocked_explicit = 0;
    std::uint64_t mask_blocked_bench_board_loop = 0;
    std::uint64_t mask_blocked_cycle = 0;

    for (const auto& metric : metrics) {
        execution_attempts += metric.execution_attempts;
        execution_blocks += metric.execution_blocks;
        blocked_reverse += metric.blocked_reverse;
        blocked_oscillation += metric.blocked_oscillation;
        blocked_explicit += metric.blocked_explicit;
        blocked_bench_board_loop += metric.blocked_bench_board_loop;
        blocked_cycle += metric.blocked_cycle;
        board_moves_executed += metric.board_moves_executed;
        bench_to_board_executed += metric.bench_to_board_executed;
        mask_board_move_candidates += metric.mask_board_move_candidates;
        mask_board_move_valid += metric.mask_board_move_valid;
        mask_board_move_blocked_anti_loop += metric.mask_board_move_blocked_anti_loop;
        mask_board_move_blocked_seen_state += metric.mask_board_move_blocked_seen_state;
        mask_bench_move_candidates += metric.mask_bench_move_candidates;
        mask_bench_move_valid += metric.mask_bench_move_valid;
        mask_bench_move_blocked_anti_loop += metric.mask_bench_move_blocked_anti_loop;
        mask_bench_move_blocked_seen_state += metric.mask_bench_move_blocked_seen_state;
        mask_blocked_reverse += metric.mask_blocked_reverse;
        mask_blocked_oscillation += metric.mask_blocked_oscillation;
        mask_blocked_explicit += metric.mask_blocked_explicit;
        mask_blocked_bench_board_loop += metric.mask_blocked_bench_board_loop;
        mask_blocked_cycle += metric.mask_blocked_cycle;
    }

    result["execution_attempts"] = execution_attempts;
    result["execution_blocks"] = execution_blocks;
    result["blocked_reverse"] = blocked_reverse;
    result["blocked_oscillation"] = blocked_oscillation;
    result["blocked_explicit"] = blocked_explicit;
    result["blocked_bench_board_loop"] = blocked_bench_board_loop;
    result["blocked_cycle"] = blocked_cycle;
    result["board_moves_executed"] = board_moves_executed;
    result["bench_to_board_executed"] = bench_to_board_executed;
    result["mask_board_move_candidates"] = mask_board_move_candidates;
    result["mask_board_move_valid"] = mask_board_move_valid;
    result["mask_board_move_blocked_anti_loop"] = mask_board_move_blocked_anti_loop;
    result["mask_board_move_blocked_seen_state"] = mask_board_move_blocked_seen_state;
    result["mask_bench_move_candidates"] = mask_bench_move_candidates;
    result["mask_bench_move_valid"] = mask_bench_move_valid;
    result["mask_bench_move_blocked_anti_loop"] = mask_bench_move_blocked_anti_loop;
    result["mask_bench_move_blocked_seen_state"] = mask_bench_move_blocked_seen_state;
    result["mask_blocked_reverse"] = mask_blocked_reverse;
    result["mask_blocked_oscillation"] = mask_blocked_oscillation;
    result["mask_blocked_explicit"] = mask_blocked_explicit;
    result["mask_blocked_bench_board_loop"] = mask_blocked_bench_board_loop;
    result["mask_blocked_cycle"] = mask_blocked_cycle;

    return result;
}




// Versioned aggregate transport. Structured cold-path context remains pinned
// per lobby for compatibility; all fixed-shape numeric PPO carriers live in
// contiguous [lobby, player, ...] arrays owned by this batch object.
class NativeDecisionBatch : public std::enable_shared_from_this<NativeDecisionBatch> {
public:
    static constexpr std::uint32_t kContractVersion = 1;
    static constexpr std::size_t kPlayers = tft::kPlayersPerLobby;

    explicit NativeDecisionBatch(std::vector<tft::ResetResult> results)
        : kind_("reset") {
        if (results.empty()) throw std::invalid_argument("NativeDecisionBatch nao pode ser vazio.");
        initialize_layout(results.size(), results.front().observation_dim);
        for (std::size_t lobby = 0; lobby < results.size(); ++lobby) {
            auto& row = results[lobby];
            validate_observation(row.observations, row.observation_dim);
            std::copy(row.observations.begin(), row.observations.end(),
                observations_.mutable_data() + lobby * kPlayers * observation_dim_);
            copy_masks(lobby, row.action_masks);
            contexts_.push_back(reset_to_dict(std::move(row), false));
        }
        make_read_only();
    }

    explicit NativeDecisionBatch(std::vector<tft::StepResult> results)
        : kind_("step") {
        if (results.empty()) throw std::invalid_argument("NativeDecisionBatch nao pode ser vazio.");
        initialize_layout(results.size(), results.front().observation_dim);
        const auto lobby_count = static_cast<py::ssize_t>(results.size());
        rewards_ = py::array_t<float>({lobby_count, static_cast<py::ssize_t>(kPlayers)});
        action_rewards_ = py::array_t<float>({lobby_count, static_cast<py::ssize_t>(kPlayers)});
        combat_rewards_ = py::array_t<float>({lobby_count, static_cast<py::ssize_t>(kPlayers)});
        placement_rewards_ = py::array_t<float>({lobby_count, static_cast<py::ssize_t>(kPlayers)});
        dones_ = py::array_t<bool>({lobby_count, static_cast<py::ssize_t>(kPlayers)});
        lobby_done_ = py::array_t<bool>(lobby_count);

        for (std::size_t lobby = 0; lobby < results.size(); ++lobby) {
            auto& row = results[lobby];
            validate_observation(row.observations, row.observation_dim);
            std::copy(row.observations.begin(), row.observations.end(),
                observations_.mutable_data() + lobby * kPlayers * observation_dim_);
            copy_masks(lobby, row.action_masks);
            const auto offset = lobby * kPlayers;
            std::copy(row.rewards.begin(), row.rewards.end(), rewards_.mutable_data() + offset);
            std::copy(row.action_rewards.begin(), row.action_rewards.end(), action_rewards_.mutable_data() + offset);
            std::copy(row.combat_rewards.begin(), row.combat_rewards.end(), combat_rewards_.mutable_data() + offset);
            std::copy(row.placement_rewards.begin(), row.placement_rewards.end(), placement_rewards_.mutable_data() + offset);
            for (std::size_t player = 0; player < kPlayers; ++player)
                dones_.mutable_data()[offset + player] = row.dones[player] != 0;
            lobby_done_.mutable_data()[lobby] = row.lobby_done;
            contexts_.push_back(step_to_dict(std::move(row), false));
        }
        make_read_only();
    }

    std::size_t size() const noexcept { return contexts_.size(); }
    const std::string& kind() const noexcept { return kind_; }
    std::size_t observation_dim() const noexcept { return observation_dim_; }
    std::size_t mask_width() const noexcept { return mask_width_; }
    py::array observations() const { return observations_; }
    py::array action_masks() const { return action_masks_; }
    py::array rewards() const { return rewards_; }
    py::array action_rewards() const { return action_rewards_; }
    py::array combat_rewards() const { return combat_rewards_; }
    py::array placement_rewards() const { return placement_rewards_; }
    py::array dones() const { return dones_; }
    py::array lobby_done() const { return lobby_done_; }

    std::shared_ptr<tft::NativeDecisionContext> native_context(std::size_t index) const {
        if (index >= contexts_.size())
            throw py::index_error("lobby index fora do NativeDecisionBatch.");
        const auto& handle = py::cast<const NativeAuditSnapshotHandle&>(
            contexts_[index]["native_state_snapshot"]);
        return std::make_shared<tft::NativeDecisionContext>(handle.shared_snapshot());
    }

    std::shared_ptr<tft::NativeSpatialContext> native_spatial_context(
        std::size_t lobby_index, std::size_t player_index
    ) const {
        if (lobby_index >= contexts_.size())
            throw py::index_error("lobby index fora do NativeDecisionBatch.");
        const auto& handle = py::cast<const NativeAuditSnapshotHandle&>(
            contexts_[lobby_index]["native_state_snapshot"]);
        return std::make_shared<tft::NativeSpatialContext>(
            handle.shared_snapshot(), player_index);
    }

    py::dict semantic_projection(const py::dict& catalog_map, const std::string& contract_hash) {
        py::list snapshot_mappings;
        for (const auto& context : contexts_)
            snapshot_mappings.append(context["native_state_snapshot"]);
        return semantic_projection_from_snapshot_mappings(
            snapshot_mappings, catalog_map, contract_hash,
            py::cast(shared_from_this()));
    }

    py::dict lobby_result(std::size_t index) {
        if (index >= contexts_.size()) throw py::index_error("lobby index fora do NativeDecisionBatch.");
        py::dict result = contexts_[index];
        const auto owner = py::cast(shared_from_this());
        const auto obs_offset = index * kPlayers * observation_dim_;
        const auto mask_offset = index * kPlayers * mask_width_;
        auto observation_view = py::array_t<float>(
            {static_cast<py::ssize_t>(kPlayers), static_cast<py::ssize_t>(observation_dim_)},
            {static_cast<py::ssize_t>(observation_dim_ * sizeof(float)), static_cast<py::ssize_t>(sizeof(float))},
            observations_.data() + obs_offset, owner);
        auto masks_view = py::array_t<bool>(
            {static_cast<py::ssize_t>(kPlayers), static_cast<py::ssize_t>(mask_width_)},
            {static_cast<py::ssize_t>(mask_width_ * sizeof(bool)), static_cast<py::ssize_t>(sizeof(bool))},
            action_masks_.data() + mask_offset, owner);
        observation_view.attr("setflags")(false);
        masks_view.attr("setflags")(false);
        result["observations"] = std::move(observation_view);
        result["action_masks"] = std::move(masks_view);
        if (kind_ == "step") {
            const auto float_row = [&owner, index](py::array_t<float>& values) {
                return py::array_t<float>(
                    {static_cast<py::ssize_t>(kPlayers)},
                    {static_cast<py::ssize_t>(sizeof(float))},
                    values.data() + index * kPlayers, owner);
            };
            auto rewards_view = float_row(rewards_);
            auto action_rewards_view = float_row(action_rewards_);
            auto combat_rewards_view = float_row(combat_rewards_);
            auto placement_rewards_view = float_row(placement_rewards_);
            auto dones_view = py::array_t<bool>(
                {static_cast<py::ssize_t>(kPlayers)},
                {static_cast<py::ssize_t>(sizeof(bool))},
                dones_.data() + index * kPlayers, owner);
            rewards_view.attr("setflags")(false);
            action_rewards_view.attr("setflags")(false);
            combat_rewards_view.attr("setflags")(false);
            placement_rewards_view.attr("setflags")(false);
            dones_view.attr("setflags")(false);
            result["rewards"] = std::move(rewards_view);
            result["action_rewards"] = std::move(action_rewards_view);
            result["combat_rewards"] = std::move(combat_rewards_view);
            result["placement_rewards"] = std::move(placement_rewards_view);
            result["dones"] = std::move(dones_view);
        }
        py::dict action_context;
        action_context["contract_id"] = "tft.engine.action-context";
        action_context["contract_version"] = 1;
        action_context["engine_instance_id"] = result["engine_instance_id"];
        action_context["episode_id"] = result["episode_id"];
        action_context["decision_sequence"] = result["decision_sequence"];
        action_context["player_decision_sequences"] = result["player_decision_sequences"];
        action_context["action_mask_contract_id"] = "tft.action-masks.packed";
        action_context["action_mask_contract_version"] = 1;
        action_context["action_mask_layout"] = "type,shop,bench_source,board_target,board_source,board_move_target,bench_move_source,bench_to_board_target,item_inventory,item_component_first,item_component_pair,item_target";
        action_context["action_masks"] = result["action_masks"];
        action_context["native_state_snapshot"] = result["native_state_snapshot"];
        if (kind_ == "step") {
            action_context["action_traces"] = result["action_traces"];
            action_context["action_outcome_events"] = result["action_outcome_events"];
            action_context["native_decision_context"] = native_context(index);
        }
        result["action_context"] = std::move(action_context);
        return result;
    }

    py::dict action_context(std::size_t index) {
        const auto row = lobby_result(index);
        return py::cast<py::dict>(row["action_context"]);
    }

private:
    void initialize_layout(std::size_t lobby_count, std::size_t observation_dim) {
        if (observation_dim == 0) throw std::runtime_error("observation_dim invalida no NativeDecisionBatch.");
        observation_dim_ = observation_dim;
        mask_width_ = kPackedActionMaskWidth;
        const auto count = static_cast<py::ssize_t>(lobby_count);
        observations_ = py::array_t<float>({count, static_cast<py::ssize_t>(kPlayers),
            static_cast<py::ssize_t>(observation_dim_)});
        action_masks_ = py::array_t<bool>({count, static_cast<py::ssize_t>(kPlayers),
            static_cast<py::ssize_t>(mask_width_)});
    }

    void validate_observation(const std::vector<float>& values, std::size_t dimension) const {
        if (dimension != observation_dim_ || values.size() != kPlayers * observation_dim_)
            throw std::runtime_error("Dimensoes de observations divergentes no NativeDecisionBatch.");
    }

    void copy_masks(std::size_t lobby, const std::array<PlayerActionMasks, kPlayers>& masks) {
        auto* destination = action_masks_.mutable_data() + lobby * kPlayers * mask_width_;
        for (std::size_t player = 0; player < kPlayers; ++player) {
            std::size_t offset = player * mask_width_;
            const auto& source = masks[player];
            bool* row = destination + offset;
            offset = 0;
            append_packed_mask(row, offset, source.type_mask);
            append_packed_mask(row, offset, source.shop_mask);
            append_packed_mask(row, offset, source.bench_source_mask);
            append_packed_mask(row, offset, source.board_target_mask);
            append_packed_mask(row, offset, source.board_source_mask);
            append_packed_mask(row, offset, source.board_move_target_masks);
            append_packed_mask(row, offset, source.bench_move_source_mask);
            append_packed_mask(row, offset, source.bench_to_board_target_masks);
            append_packed_mask(row, offset, source.item_inventory_mask);
            append_packed_mask(row, offset, source.item_component_first_mask);
            append_packed_mask(row, offset, source.item_component_pair_masks);
            append_packed_mask(row, offset, source.item_target_mask);
            if (offset != mask_width_)
                throw std::runtime_error("Layout compactado de action masks inconsistente.");
        }
    }

    void make_read_only() {
        observations_.attr("setflags")(false);
        action_masks_.attr("setflags")(false);
        if (kind_ == "step") {
            rewards_.attr("setflags")(false);
            action_rewards_.attr("setflags")(false);
            combat_rewards_.attr("setflags")(false);
            placement_rewards_.attr("setflags")(false);
            dones_.attr("setflags")(false);
            lobby_done_.attr("setflags")(false);
        }
    }

    std::string kind_;
    std::vector<py::dict> contexts_;
    std::size_t observation_dim_{0};
    std::size_t mask_width_{0};
    py::array_t<float> observations_;
    py::array_t<bool> action_masks_;
    py::array_t<float> rewards_;
    py::array_t<float> action_rewards_;
    py::array_t<float> combat_rewards_;
    py::array_t<float> placement_rewards_;
    py::array_t<bool> dones_;
    py::array_t<bool> lobby_done_;
};

// Native sequential owner of independent complete-lobby Engines.
class NativeLobbyBatchManager {
public:
    NativeLobbyBatchManager(std::size_t lobby_count, std::uint64_t base_seed,
        const std::string& catalog_path, const std::string& item_catalog_path) {
        if (lobby_count == 0) throw std::invalid_argument("lobby_count deve ser maior que zero.");
        if (lobby_count - 1 > std::numeric_limits<std::uint64_t>::max() - base_seed)
            throw std::overflow_error("Seeds independentes excedem uint64.");
        engines_.reserve(lobby_count);
        for (std::size_t i = 0; i < lobby_count; ++i)
            engines_.push_back(std::make_unique<TFTEngine>(
                base_seed + static_cast<std::uint64_t>(i), catalog_path, item_catalog_path));
    }
    ~NativeLobbyBatchManager() { close(); }

    std::shared_ptr<NativeDecisionBatch> reset(py::object seed) {
        ensure_open();
        has_reset_ = false;
        std::optional<std::uint64_t> base_seed;
        if (!seed.is_none()) {
            if (!py::isinstance<py::int_>(seed) || PyBool_Check(seed.ptr()))
                throw py::type_error("seed deve ser um inteiro nao negativo ou None.");
            try { base_seed = seed.cast<std::uint64_t>(); }
            catch (const py::cast_error&) {
                throw py::value_error("seed deve estar entre 0 e 18446744073709551615.");
            }
            if (engines_.size() - 1 > std::numeric_limits<std::uint64_t>::max() - *base_seed)
                throw py::value_error("Offsets de seed por lobby excedem uint64.");
        }
        std::vector<tft::ResetResult> results;
        results.reserve(engines_.size());
        for (std::size_t i = 0; i < engines_.size(); ++i) {
            std::optional<std::uint64_t> lobby_seed;
            if (base_seed) lobby_seed = *base_seed + static_cast<std::uint64_t>(i);
            results.push_back(engines_[i]->reset(lobby_seed));
        }
        has_reset_ = true;
        try { return std::make_shared<NativeDecisionBatch>(std::move(results)); }
        catch (...) { has_reset_ = false; throw; }
    }

    std::shared_ptr<NativeDecisionBatch> step(const std::vector<std::vector<std::vector<std::int32_t>>>& batch_actions) {
        ensure_open();
        if (!has_reset_) throw std::runtime_error("Execute reset() antes de step().");
        if (batch_actions.size() != engines_.size())
            throw py::value_error("actions deve conter exatamente uma entrada por lobby.");
        std::vector<tft::StepResult> results;
        results.reserve(engines_.size());
        try {
            for (std::size_t lobby = 0; lobby < engines_.size(); ++lobby) {
                const auto& raw = batch_actions[lobby];
                if (raw.size() != tft::kPlayersPerLobby)
                    throw py::value_error("Cada lobby deve conter exatamente 8 jogadores.");
                std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};
                for (std::size_t player = 0; player < tft::kPlayersPerLobby; ++player) {
                    if (raw[player].size() != tft::kActionComponents)
                        throw py::value_error("Cada acao deve conter exatamente 6 componentes.");
                    for (std::size_t component = 0; component < tft::kActionComponents; ++component)
                        actions[player].values[component] = raw[player][component];
                }
                results.push_back(engines_[lobby]->step(actions));
            }
        } catch (...) {
            has_reset_ = false;
            throw;
        }
        try { return std::make_shared<NativeDecisionBatch>(std::move(results)); }
        catch (...) { has_reset_ = false; throw; }
    }

    py::dict semantic_projection_from_snapshots(
        const py::sequence& lobby_envelopes,
        const py::dict& catalog_map,
        const std::string& contract_hash
    ) const {
        py::list snapshot_mappings;
        for (py::ssize_t lobby = 0; lobby < py::len(lobby_envelopes); ++lobby) {
            py::object envelope = py::reinterpret_borrow<py::object>(lobby_envelopes[lobby]);
            if (!py::isinstance<py::dict>(envelope))
                throw py::type_error("each semantic lobby snapshot must be a mapping");
            py::dict row = py::reinterpret_borrow<py::dict>(envelope);
            if (!row.contains("native_state_snapshot"))
                throw py::value_error("lobby snapshot is missing native_state_snapshot");
            snapshot_mappings.append(row["native_state_snapshot"]);
        }
        return semantic_projection_from_snapshot_mappings(
            snapshot_mappings, catalog_map, contract_hash);
    }

    TFTEngine& engine(std::size_t index) {
        ensure_open();
        if (index >= engines_.size()) throw py::index_error("lobby index fora do intervalo.");
        return *engines_[index];
    }
    std::size_t lobby_count() const noexcept { return engines_.size(); }
    std::vector<std::string> engine_instance_ids() const {
        ensure_open();
        std::vector<std::string> ids;
        ids.reserve(engines_.size());
        for (const auto& engine : engines_) ids.push_back(engine->engine_instance_id());
        return ids;
    }
    void close() noexcept {
        if (closed_) return;
        for (auto& engine : engines_) if (engine) {
            try { engine->close(); } catch (...) {}
        }
        closed_ = true;
        has_reset_ = false;
    }
private:
    void ensure_open() const {
        if (closed_) throw std::runtime_error("LobbyBatchManager ja foi encerrado.");
    }
    std::vector<std::unique_ptr<TFTEngine>> engines_;
    bool has_reset_{false};
    bool closed_{false};
};

}  // namespace

PYBIND11_MODULE(tft_engine, module) {

    py::class_<tft::SynergyEngine>(module, "SynergyManagerNative")
        .def(py::init<tft::TraitMilestones>(), py::arg("milestones") = tft::TraitMilestones{})
        .def("set_state", &tft::SynergyEngine::set_state,
             py::arg("active_traits"), py::arg("partial_traits") = tft::TraitCounts{})
        .def("calculate_multiplier", [](const tft::SynergyEngine& self, py::object active) {
            if (active.is_none()) return self.calculate_multiplier();
            const auto parsed = active.cast<tft::TraitCounts>();
            return self.calculate_multiplier(&parsed);
        }, py::arg("active_traits") = py::none())
        .def("get_all_multipliers", [](const tft::SynergyEngine& self, py::object active) {
            if (active.is_none()) return self.get_all_multipliers();
            const auto parsed = active.cast<tft::TraitCounts>();
            return self.get_all_multipliers(&parsed);
        }, py::arg("active_traits") = py::none())
        .def("get_trait_level", &tft::SynergyEngine::get_trait_level,
             py::arg("trait_name"), py::arg("count"))
        .def("get_unit_synergy_bonus", [](const tft::SynergyEngine& self,
                                          const std::vector<std::string>& traits,
                                          py::object focus) {
            if (focus.is_none()) return self.get_unit_synergy_bonus(traits);
            const auto parsed = focus.cast<tft::TraitFocus>();
            return self.get_unit_synergy_bonus(traits, &parsed);
        }, py::arg("unit_traits"), py::arg("comp_focus") = py::none());

    py::class_<tft::RewardManager>(module, "RewardManager")
        .def(py::init<>())
        .def("reset", &tft::RewardManager::reset)
        .def("calculate_combat_reward", &tft::RewardManager::calculate_combat_reward,
             py::arg("won"), py::arg("damage_dealt")=0.0, py::arg("damage_taken")=0.0,
             py::arg("enemy_alive")=0, py::arg("own_alive")=0)
        .def("calculate_power_reward", &tft::RewardManager::calculate_power_reward)
        .def("calculate_synergy_reward", &tft::RewardManager::calculate_synergy_reward)
        .def("calculate_positioning_reward", &tft::RewardManager::calculate_positioning_reward)
        .def("calculate_level_reward", &tft::RewardManager::calculate_level_reward)
        .def("calculate_economy_reward", &tft::RewardManager::calculate_economy_reward,
             py::arg("gold"), py::arg("level"), py::arg("hp"))
        .def("calculate_streak_reward", &tft::RewardManager::calculate_streak_reward)
        .def("calculate_board_reward", &tft::RewardManager::calculate_board_reward)
        .def("calculate_action_reward", &tft::RewardManager::calculate_action_reward,
             py::arg("action_type"), py::arg("action_success"), py::arg("action_value")=0.0)
        .def("calculate_total_reward", &tft::RewardManager::calculate_total_reward,
             py::arg("combat_reward")=0.0, py::arg("power_reward")=0.0,
             py::arg("synergy_reward")=0.0, py::arg("positioning_reward")=0.0,
             py::arg("level_reward")=0.0, py::arg("economy_reward")=0.0,
             py::arg("streak_reward")=0.0, py::arg("board_reward")=0.0,
             py::arg("action_reward")=0.0)
        .def("get_state", [](const tft::RewardManager& self) {
            const auto st=self.get_state();
            py::dict d;
            d["previous_board_power"]=st.previous_board_power;
            d["previous_positioning_score"]=st.previous_positioning_score;
            d["previous_synergy_score"]=st.previous_synergy_score;
            d["previous_level"]=st.previous_level;
            d["previous_gold"]=st.previous_gold;
            d["last_combat_reward"]=st.last_combat_reward;
            d["round_reward"]=st.round_reward;
            d["total_reward"]=st.total_reward;
            return d;
        });

    module.doc() =
        "API Python do motor nativo de simulacao TFT.";

    // Contrato mínimo consumido pelo wrapper PPO:
    // reset -> step -> máscaras/diagnósticos de treino -> close.
    // Estado interno, hooks de fixture e consultas de implementação não
    // atravessam a fronteira Python/C++.
    py::class_<NativeAuditSnapshotHandle>(module, "NativeAuditSnapshotHandle")
        .def("to_dict", &NativeAuditSnapshotHandle::to_dict)
        .def("to_envelope_dict", &NativeAuditSnapshotHandle::to_envelope_dict)
        .def("player", &NativeAuditSnapshotHandle::player, py::arg("index"))
        .def("player_count", &NativeAuditSnapshotHandle::player_count)
        .def("keys", &NativeAuditSnapshotHandle::keys)
        .def("get", &NativeAuditSnapshotHandle::get,
             py::arg("field"), py::arg("default_value") = py::none())
        .def("__getitem__", &NativeAuditSnapshotHandle::item)
        .def("combat_events", &NativeAuditSnapshotHandle::combat_events, py::arg("field"));

    py::class_<TFTEngine>(module, "TFTLobby")
        .def(
            py::init<std::uint64_t, std::string, std::string>(),
            py::arg("seed") = 0,
            py::arg("catalog_path") = "",
            py::arg("item_catalog_path") = ""
        )
        .def(
            "reset",
            [](TFTEngine& self, py::object seed) {
                std::optional<std::uint64_t> parsed_seed;
                if (!seed.is_none()) {
                    if (!py::isinstance<py::int_>(seed) || PyBool_Check(seed.ptr())) {
                        throw py::type_error(
                            "seed deve ser um inteiro nao negativo ou None."
                        );
                    }
                    try {
                        parsed_seed = seed.cast<std::uint64_t>();
                    } catch (const py::cast_error&) {
                        throw py::value_error(
                            "seed deve estar entre 0 e 18446744073709551615."
                        );
                    }
                }
                return reset_to_dict(self.reset(parsed_seed));
            },
            py::arg("seed") = py::none()
        )
        .def(
            "step",
            [](TFTEngine& self,
               const std::vector<std::vector<std::int32_t>>& raw_actions,
               bool timer_enabled,
               bool timer_expired) {
                if (raw_actions.size() != tft::kPlayersPerLobby) {
                    throw py::value_error("actions deve conter 8 jogadores.");
                }

                std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};
                for (std::size_t player = 0; player < tft::kPlayersPerLobby; ++player) {
                    if (raw_actions[player].size() != tft::kActionComponents) {
                        throw py::value_error(
                            "Cada acao deve conter 6 componentes."
                        );
                    }
                    for (std::size_t component = 0;
                         component < tft::kActionComponents;
                         ++component) {
                        actions[player].values[component] =
                            raw_actions[player][component];
                    }
                }
                return step_to_dict(self.step(actions, timer_enabled, timer_expired));
            },
            py::arg("actions"),
            py::arg("timer_enabled") = false,
            py::arg("timer_expired") = false
        )
        .def(
            "validate_actions",
            [](TFTEngine& self, const std::vector<std::vector<std::int32_t>>& raw_actions) {
                if (raw_actions.size() != tft::kPlayersPerLobby)
                    throw py::value_error("actions deve conter 8 jogadores.");
                std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};
                for (std::size_t player = 0; player < tft::kPlayersPerLobby; ++player) {
                    if (raw_actions[player].size() != tft::kActionComponents)
                        throw py::value_error("Cada acao deve conter 6 componentes.");
                    for (std::size_t component = 0; component < tft::kActionComponents; ++component)
                        actions[player].values[component] = raw_actions[player][component];
                }
                const auto events = self.validate_actions(actions);
                py::list result;
                for (const auto& event : events) {
                    py::dict item;
                    item["contract_id"] = event.contract_id;
                    item["contract_version"] = event.contract_version;
                    item["event_id"] = event.event_id;
                    item["engine_instance_id"] = event.engine_instance_id;
                    item["episode_id"] = event.episode_id;
                    item["player_id"] = event.player_id;
                    item["source_player_decision_sequence"] = event.source_player_decision_sequence;
                    item["outcome_player_decision_sequence"] = event.outcome_player_decision_sequence;
                    item["event_sequence"] = event.event_sequence;
                    item["action_type"] = event.action_type;
                    item["action_family"] = event.action_family;
                    item["requested_action"] = event.requested_action;
                    item["normalized_action"] = event.normalized_action;
                    item["effective_action"] = event.effective_action;
                    item["mask_permitted"] = event.mask_permitted;
        item["preflight_accepted"] = event.preflight_accepted;
                    item["handler_applied"] = event.handler_applied;
                    item["decision_advanced"] = event.decision_advanced;
                    item["status_reason"] = event.status_reason;
        item["status_detail"] = event.status_detail;
                    result.append(std::move(item));
                }
                return result;
            },
            py::arg("actions")
        )
        .def_property_readonly(
            "engine_instance_id",
            &TFTEngine::engine_instance_id
        )
        .def(
            "adapt_opgg_compositions_json",
            &TFTEngine::adapt_opgg_compositions_json,
            py::arg("catalog_json")
        )
        .def(
            "get_champion_id_map",
            [](const TFTEngine& self) {
                py::dict result;
                for (const auto& [internal_id, api_name] : self.get_champion_api_name_map()) {
                    result[py::str(api_name)] = internal_id;
                }
                return result;
            }
        )
        .def("get_composition_diagnostics_jsonl", &TFTEngine::get_composition_diagnostics_jsonl)
        .def("set_strategic_direction_pivot_audit_path",
             &TFTEngine::set_strategic_direction_pivot_audit_path, py::arg("path"))
        .def("get_audit_snapshot", [](const TFTEngine& self) {
            return audit_snapshot_to_dict(self.get_audit_snapshot());
        })
        .def(
            "get_action_masks",
            [](const TFTEngine& self) {
                return masks_to_list(self.get_action_masks());
            }
        )
        .def(
            "get_anti_loop_metrics",
            [](const TFTEngine& self) {
                return anti_loop_to_dict(self.get_anti_loop_metrics());
            }
        )
        // Contrato público de diagnóstico e fixtures de paridade.
        // Não faz parte do caminho de execução normal do Trainer.
        .def(
            "get_public_state",
            [](const TFTEngine& self) {
                return public_state_to_dict(self.get_public_state());
            }
        )
        .def("get_unit_comp_score", &TFTEngine::get_unit_comp_score,
             py::arg("player_id"), py::arg("champion_api_name"),
             py::arg("star") = 1)
        .def("is_core_unit", &TFTEngine::is_core_unit,
             py::arg("player_id"), py::arg("champion_api_name"))
        .def("is_core_trait", &TFTEngine::is_core_trait,
             py::arg("player_id"), py::arg("trait"))
        .def("set_unit_for_testing", &TFTEngine::set_unit_for_testing,
             py::arg("player_id"), py::arg("on_board"), py::arg("slot"),
             py::arg("champion_api_name"), py::arg("star") = 1)
        .def("grant_item_component", &TFTEngine::grant_item_component,
             py::arg("player_id"), py::arg("component_id"))
        .def("grant_completed_item", &TFTEngine::grant_completed_item,
             py::arg("player_id"), py::arg("item_id"))
        .def("grant_component_anvil_for_testing", &TFTEngine::grant_component_anvil_for_testing,
             py::arg("player_id"), py::arg("options"))
        .def("add_item_component_for_testing", &TFTEngine::add_item_component_for_testing,
             py::arg("player_id"), py::arg("component_id"))
        .def("add_completed_item_for_testing", &TFTEngine::add_completed_item_for_testing,
             py::arg("player_id"), py::arg("item_id"))
        .def("set_player_alive_for_testing", &TFTEngine::set_player_alive_for_testing,
             py::arg("player_id"), py::arg("alive"))
        .def("set_player_hp_for_testing", &TFTEngine::set_player_hp_for_testing,
             py::arg("player_id"), py::arg("hp"))
        .def("set_player_economy_for_testing", &TFTEngine::set_player_economy_for_testing,
             py::arg("player_id"), py::arg("gold"), py::arg("level"), py::arg("xp"))
        .def("set_shop_offer_for_testing", &TFTEngine::set_shop_offer_for_testing,
             py::arg("player_id"), py::arg("slot"), py::arg("champion_api_name"))
        .def("set_next_shop_roll_for_testing", &TFTEngine::set_next_shop_roll_for_testing,
             py::arg("player_id"), py::arg("champion_api_names"))
        .def("pool_available", &TFTEngine::pool_available, py::arg("champion_internal_id"))
        .def("pool_initial_count", &TFTEngine::pool_initial_count, py::arg("champion_internal_id"))
        .def("pool_total_available", &TFTEngine::pool_total_available)
        .def_property_readonly("observation_dim", &TFTEngine::observation_dim)
        .def_property_readonly("episode_id", &TFTEngine::episode_id)
        .def_property_readonly("round", &TFTEngine::round)
        .def_property_readonly("stage", &TFTEngine::stage)
        .def_property_readonly("alive_players", &TFTEngine::alive_players)
        .def_property_readonly("is_done", &TFTEngine::is_done)
        .def("close", &TFTEngine::close);



    py::enum_<tft::ContextAvailability>(module, "ContextAvailability")
        .value("COMPLETE", tft::ContextAvailability::Complete)
        .value("PARTIAL", tft::ContextAvailability::Partial)
        .value("EMPTY", tft::ContextAvailability::Empty)
        .value("UNKNOWN", tft::ContextAvailability::Unknown)
        .value("MISSING", tft::ContextAvailability::Missing)
        .value("STALE", tft::ContextAvailability::Stale)
        .value("INCOMPATIBLE", tft::ContextAvailability::Incompatible)
        .value("NOT_APPLICABLE", tft::ContextAvailability::NotApplicable);

    py::class_<tft::NativeSpatialContext, std::shared_ptr<tft::NativeSpatialContext>>(
        module, "NativeSpatialContext")
        .def_property_readonly("contract_id", [](const tft::NativeSpatialContext&) {
            return tft::NativeSpatialContext::kContractId;
        })
        .def_property_readonly("contract_version", [](const tft::NativeSpatialContext&) {
            return tft::NativeSpatialContext::kContractVersion;
        })
        .def_property_readonly("geometry_id", &tft::NativeSpatialContext::geometry_id)
        .def_property_readonly("geometry_version", &tft::NativeSpatialContext::geometry_version)
        .def_property_readonly("rows", &tft::NativeSpatialContext::rows)
        .def_property_readonly("columns", &tft::NativeSpatialContext::columns)
        .def_property_readonly("availability", &tft::NativeSpatialContext::availability)
        .def_property_readonly("player_index", &tft::NativeSpatialContext::player_index)
        .def_property_readonly("engine_instance_id", &tft::NativeSpatialContext::engine_instance_id)
        .def_property_readonly("episode_id", &tft::NativeSpatialContext::episode_id)
        .def_property_readonly("snapshot_sequence", &tft::NativeSpatialContext::snapshot_sequence)
        .def_property_readonly("player_decision_sequence", &tft::NativeSpatialContext::player_decision_sequence)
        .def("row_buffer", [](std::shared_ptr<tft::NativeSpatialContext> context) {
            const auto& values = context->row_buffer();
            py::array_t<std::int32_t> result({28}, {static_cast<py::ssize_t>(sizeof(std::int32_t))},
                values.data(), py::cast(context));
            result.attr("setflags")(false); return result;
        })
        .def("column_buffer", [](std::shared_ptr<tft::NativeSpatialContext> context) {
            const auto& values = context->column_buffer();
            py::array_t<std::int32_t> result({28}, {static_cast<py::ssize_t>(sizeof(std::int32_t))},
                values.data(), py::cast(context));
            result.attr("setflags")(false); return result;
        })
        .def("occupancy_buffer", [](std::shared_ptr<tft::NativeSpatialContext> context) {
            const auto& values = context->occupancy_buffer();
            py::array_t<std::uint8_t> result({28}, {static_cast<py::ssize_t>(sizeof(std::uint8_t))},
                values.data(), py::cast(context));
            result.attr("setflags")(false); return result;
        })
        .def("catalog_id_buffer", [](std::shared_ptr<tft::NativeSpatialContext> context) {
            const auto& values = context->catalog_id_buffer();
            py::array_t<std::int32_t> result({28}, {static_cast<py::ssize_t>(sizeof(std::int32_t))},
                values.data(), py::cast(context));
            result.attr("setflags")(false); return result;
        })
        .def("role_buffer", [](std::shared_ptr<tft::NativeSpatialContext> context) {
            const auto& values = context->role_buffer();
            py::array_t<std::int32_t> result({28}, {static_cast<py::ssize_t>(sizeof(std::int32_t))},
                values.data(), py::cast(context));
            result.attr("setflags")(false); return result;
        })
        .def("stats_buffer", [](std::shared_ptr<tft::NativeSpatialContext> context) {
            const auto& values = context->stats_buffer();
            py::array_t<float> result({28, 5},
                {static_cast<py::ssize_t>(5 * sizeof(float)), static_cast<py::ssize_t>(sizeof(float))},
                values.front().data(), py::cast(context));
            result.attr("setflags")(false); return result;
        })
        .def_property_readonly("unit_uuids", [](const tft::NativeSpatialContext& context) {
            py::list result; for (const auto& value : context.uuid_buffer()) result.append(value);
            return result;
        })
        .def_property_readonly("champion_ids", [](const tft::NativeSpatialContext& context) {
            py::list result; for (const auto& value : context.champion_id_buffer()) result.append(value);
            return result;
        })
        .def_property_readonly("unit_traits", [](const tft::NativeSpatialContext& context) {
            py::list result;
            for (const auto& traits : context.trait_buffer()) result.append(py::cast(traits));
            return result;
        })
        .def_property_readonly("relations", [](const tft::NativeSpatialContext& context) {
            py::array_t<std::int32_t> result(py::array::ShapeContainer{
                static_cast<py::ssize_t>(context.relations().size()), static_cast<py::ssize_t>(3)});
            auto out = result.mutable_unchecked<2>();
            for (std::size_t i = 0; i < context.relations().size(); ++i) {
                const auto& relation = context.relations()[i];
                out(static_cast<py::ssize_t>(i), 0) = relation.source_slot;
                out(static_cast<py::ssize_t>(i), 1) = relation.target_slot;
                out(static_cast<py::ssize_t>(i), 2) = static_cast<std::int32_t>(relation.kind);
            }
            result.attr("setflags")(false); return result;
        })
        .def_property_readonly("board_metrics", [](const tft::NativeSpatialContext& context) {
            const auto& p = context.metrics(); py::dict result;
            result["quality"] = p.board_quality_score;
            result["positional"] = p.board_positional_score;
            result["structural"] = p.board_structural_score;
            result["quality_delta"] = p.board_quality_delta;
            result["exposed_carries"] = p.board_exposed_carries;
            result["frontline_count"] = p.board_frontline_count;
            result["isolated_frontline_count"] = p.board_isolated_frontline_count;
            result["frontline_lane_count"] = p.board_frontline_lane_count;
            result["exposed_main_carries"] = p.board_exposed_main_carries;
            result["fragile_frontline_count"] = p.board_fragile_frontline_count;
            result["missing_frontline_count"] = p.board_missing_frontline_count;
            result["missing_backline_count"] = p.board_missing_backline_count;
            return result;
        });

    py::class_<tft::NativeDecisionContext, std::shared_ptr<tft::NativeDecisionContext>>(
        module, "NativeDecisionContext")
        .def_property_readonly("availability", [](const tft::NativeDecisionContext& context) {
            return context.availability();
        })
        .def_property_readonly("engine_instance_id", [](const tft::NativeDecisionContext& context) {
            return context.snapshot().engine_instance_id;
        })
        .def_property_readonly("episode_id", [](const tft::NativeDecisionContext& context) {
            return context.snapshot().episode_id;
        })
        .def_property_readonly("snapshot_sequence", [](const tft::NativeDecisionContext& context) {
            return context.snapshot().snapshot_sequence;
        })
        .def_property_readonly("round", [](const tft::NativeDecisionContext& context) {
            return context.snapshot().round;
        })
        .def_property_readonly("shared_pool", [](const tft::NativeDecisionContext& context) {
            const auto& pool = context.shared_pool();
            py::dict result;
            result["contract_id"] = pool.contract_id;
            result["contract_version"] = pool.contract_version;
            result["producer"] = pool.producer;
            result["catalog_fingerprint"] = pool.catalog_fingerprint;
            result["total_available"] = pool.total_available;
            py::list champions;
            for (const auto& champion : pool.champions) {
                py::dict row;
                row["champion_internal_id"] = champion.champion_internal_id;
                row["champion_id"] = champion.champion_id;
                row["cost"] = champion.cost;
                row["initial_count"] = champion.initial_count;
                row["available_count"] = champion.available_count;
                champions.append(std::move(row));
            }
            result["champions"] = std::move(champions);
            return result;
        })
        .def("player", [](std::shared_ptr<tft::NativeDecisionContext> context, std::size_t index) {
            const auto owner = py::cast(context);
            return audit_player_snapshot_to_dict(context->player(index), false, owner);
        }, py::arg("index"))
        .def("provenance", [](const tft::NativeDecisionContext& context, std::size_t index) {
            const auto source = context.provenance(index);
            py::dict result;
            result["producer"] = source.producer;
            result["source_namespace"] = source.source_namespace;
            result["contract_version"] = source.contract_version;
            result["episode_id"] = source.episode_id;
            result["snapshot_sequence"] = source.snapshot_sequence;
            result["player_decision_sequence"] = source.player_decision_sequence;
            return result;
        }, py::arg("player_index"))
        .def_property_readonly("player_count", &tft::NativeDecisionContext::player_count)
        .def("player_sequence_availability", &tft::NativeDecisionContext::player_sequence_availability)
        .def("strategic_availability", &tft::NativeDecisionContext::strategic_availability)
        .def("item_inventory_availability", &tft::NativeDecisionContext::item_inventory_availability)
        .def("pending_anvil_availability", &tft::NativeDecisionContext::pending_anvil_availability)
        .def("trait_counts", [](const tft::NativeDecisionContext& context, std::size_t player_index) {
            py::list result;
            for (const auto& trait : context.trait_counts(player_index)) {
                py::dict row;
                row["trait_id"] = trait.trait_id;
                row["board_count"] = trait.board_count;
                row["bench_count"] = trait.bench_count;
                row["board_bench_count"] = trait.board_bench_count;
                row["item_granted_availability"] = trait.item_granted_availability;
                result.append(std::move(row));
            }
            return result;
        }, py::arg("player_index"));

    py::class_<NativeDecisionBatch, std::shared_ptr<NativeDecisionBatch>>(module, "NativeDecisionBatch")
        .def_property_readonly("contract_id", [](const NativeDecisionBatch&) { return "tft.native-decision-batch"; })
        .def_property_readonly("contract_version", [](const NativeDecisionBatch&) { return NativeDecisionBatch::kContractVersion; })
        .def_property_readonly("kind", &NativeDecisionBatch::kind)
        .def_property_readonly("lobby_count", &NativeDecisionBatch::size)
        .def_property_readonly("players_per_lobby", [](const NativeDecisionBatch&) { return NativeDecisionBatch::kPlayers; })
        .def_property_readonly("observation_dim", &NativeDecisionBatch::observation_dim)
        .def_property_readonly("action_mask_width", &NativeDecisionBatch::mask_width)
        .def_property_readonly("action_context_contract_id", [](const NativeDecisionBatch&) { return "tft.engine.action-context"; })
        .def_property_readonly("action_context_contract_version", [](const NativeDecisionBatch&) { return 1; })
        .def_property_readonly("action_mask_contract_id", [](const NativeDecisionBatch&) { return "tft.action-masks.packed"; })
        .def_property_readonly("action_mask_contract_version", [](const NativeDecisionBatch&) { return 1; })
        .def_property_readonly("action_mask_layout", [](const NativeDecisionBatch&) { return "type,shop,bench_source,board_target,board_source,board_move_target,bench_move_source,bench_to_board_target,item_inventory,item_component_first,item_component_pair,item_target"; })
        .def_property_readonly("observations", &NativeDecisionBatch::observations)
        .def_property_readonly("action_masks", &NativeDecisionBatch::action_masks)
        .def_property_readonly("rewards", &NativeDecisionBatch::rewards)
        .def_property_readonly("action_rewards", &NativeDecisionBatch::action_rewards)
        .def_property_readonly("combat_rewards", &NativeDecisionBatch::combat_rewards)
        .def_property_readonly("placement_rewards", &NativeDecisionBatch::placement_rewards)
        .def_property_readonly("dones", &NativeDecisionBatch::dones)
        .def_property_readonly("lobby_done", &NativeDecisionBatch::lobby_done)
        .def("lobby_result", &NativeDecisionBatch::lobby_result, py::arg("index"))
        .def("action_context", &NativeDecisionBatch::action_context, py::arg("lobby_index"))
        .def("semantic_projection", &NativeDecisionBatch::semantic_projection, py::arg("catalog_map"), py::arg("contract_hash"))
        .def("native_context", &NativeDecisionBatch::native_context, py::arg("lobby_index"))
        .def("native_spatial_context", &NativeDecisionBatch::native_spatial_context,
             py::arg("lobby_index"), py::arg("player_index"))
        .def("__len__", &NativeDecisionBatch::size)
        .def("__getitem__", &NativeDecisionBatch::lobby_result);

    py::class_<NativeLobbyBatchManager>(module, "LobbyBatchManager")
        .def(py::init<std::size_t, std::uint64_t, const std::string&, const std::string&>(),
            py::arg("lobby_count"), py::arg("base_seed") = 0,
            py::arg("catalog_path") = "", py::arg("item_catalog_path") = "")
        .def("reset", &NativeLobbyBatchManager::reset, py::arg("seed") = py::none())
        .def("engine", &NativeLobbyBatchManager::engine, py::arg("index"), py::return_value_policy::reference_internal)
        .def("step", &NativeLobbyBatchManager::step, py::arg("actions"))
        .def("semantic_projection_from_snapshots", &NativeLobbyBatchManager::semantic_projection_from_snapshots,
            py::arg("lobby_snapshots"), py::arg("catalog_map"), py::arg("contract_hash"))
        .def_property_readonly("lobby_count", &NativeLobbyBatchManager::lobby_count)
        .def_property_readonly("engine_instance_ids", &NativeLobbyBatchManager::engine_instance_ids)
        .def("close", &NativeLobbyBatchManager::close);


    // CombatProfileManager.py parity API. This is deliberately stateless:
    // Python's mutable profile cache remains a Python lifecycle detail.
    module.def("combat_profile_get_profile", [](py::dict unit) {
        auto numeric = [&unit](const char* key, double fallback = 0.0) {
            if (!unit.contains(key) || unit[key].is_none()) return fallback;
            try { return py::cast<double>(unit[key]); } catch (...) { return fallback; }
        };
        auto text_value = [](py::handle value) -> std::string {
            if (py::isinstance<py::str>(value)) return py::cast<std::string>(value);
            return {};
        };
        std::string ability_text;
        if (unit.contains("ability")) {
            py::handle ability = unit["ability"];
            if (py::isinstance<py::str>(ability)) ability_text = text_value(ability);
            else if (py::isinstance<py::dict>(ability)) {
                py::dict d = py::reinterpret_borrow<py::dict>(ability);
                for (const char* key : {"description", "desc", "name", "effect"}) {
                    if (d.contains(key) && py::isinstance<py::str>(d[key])) {
                        ability_text = text_value(d[key]); break;
                    }
                }
            }
        }
        if (ability_text.empty()) {
            for (const char* key : {"ability_description", "ability_desc", "description"}) {
                if (unit.contains(key) && py::isinstance<py::str>(unit[key])) {
                    ability_text = text_value(unit[key]); break;
                }
            }
        }
        const double hp = numeric("max_hp", numeric("hp", 0.0));
        const double ad = numeric("attack_damage", numeric("ad", 0.0));
        const double mr = numeric("magic_resist", numeric("mr", 0.0));
        tft::CombatProfileInput input{ability_text, numeric("attack_range"), numeric("attack_speed"),
            ad, numeric("armor"), mr, hp, numeric("max_mana")};
        const auto p = tft::CombatProfileEngine::build_profile(input);
        const int role = static_cast<int>(p.role);
        py::dict out;
        out["role"] = role;
        out["role_name"] = std::array<const char*,5>{"tank","carry","support","fighter","assassin"}[role];
        out["frontline"] = p.frontline();
        out["backline"] = p.backline();
        out["is_tank"] = role == 0;
        out["is_carry"] = role == 1;
        out["is_support"] = role == 2;
        out["is_fighter"] = role == 3;
        out["is_assassin"] = role == 4;
        out["attack_range"] = p.attack_range;
        out["attack_speed"] = p.attack_speed;
        out["attack_damage"] = p.attack_damage;
        out["armor"] = p.armor;
        out["magic_resist"] = p.magic_resist;
        out["max_hp"] = p.max_hp;
        out["max_mana"] = p.max_mana;
        return out;
    });
    module.def("combat_profile_get_role", [](py::object unit) {
        if (unit.is_none()) return 3;
        py::dict d = py::cast<py::dict>(unit);
        auto p = py::cast<py::dict>(py::module_::import("tft_engine").attr("combat_profile_get_profile")(d));
        return py::cast<int>(p["role"]);
    });
    module.def("combat_profile_is_frontline", [](py::object unit) {
        if (unit.is_none()) return true;
        const int role = py::cast<int>(py::module_::import("tft_engine").attr("combat_profile_get_role")(unit));
        return tft::CombatProfileEngine::is_frontline(static_cast<tft::ProfileRole>(role));
    });
    module.def("combat_profile_is_backline", [](py::object unit) {
        if (unit.is_none()) return false;
        const int role = py::cast<int>(py::module_::import("tft_engine").attr("combat_profile_get_role")(unit));
        return tft::CombatProfileEngine::is_backline(static_cast<tft::ProfileRole>(role));
    });
    module.def("combat_profile_build_combat_input", [](py::dict unit) {
        auto numeric = [&unit](const char* key, double fallback = 0.0) {
            if (!unit.contains(key) || unit[key].is_none()) return fallback;
            try { return py::cast<double>(unit[key]); } catch (...) { return fallback; }
        };
        auto identifier = [&unit]() -> py::object {
            for (const char* key : {"id", "champion_id", "apiName", "characterName"})
                if (unit.contains(key) && !unit[key].is_none()) return py::reinterpret_borrow<py::object>(unit[key]);
            return py::none();
        };
        py::dict profile = py::cast<py::dict>(
            py::module_::import("tft_engine").attr("combat_profile_get_profile")(unit));
        py::dict out;
        out["id"] = identifier();
        int star = 1;
        try { if (unit.contains("star")) star = py::cast<int>(unit["star"]); } catch (...) {}
        out["star"] = star;
        out["hp"] = numeric("hp", py::cast<double>(profile["max_hp"]));
        out["max_hp"] = profile["max_hp"];
        out["mana"] = numeric("mana");
        out["max_mana"] = profile["max_mana"];
        out["attack_damage"] = profile["attack_damage"];
        out["attack_speed"] = profile["attack_speed"];
        out["armor"] = profile["armor"];
        out["magic_resist"] = profile["magic_resist"];
        out["attack_range"] = profile["attack_range"];
        out["role"] = profile["role"];
        return out;
    });

    // PositioningManager.py parity API. Boards are vectors of role IDs:
    // -1 = empty; 0 tank, 1 carry, 2 support, 3 fighter, 4 assassin.
    module.def("positioning_is_valid_position", &tft::PositioningEngine::is_valid_position);
    module.def("positioning_position_to_row_col", [](int p) { auto v=tft::PositioningEngine::position_to_row_col(p); return py::make_tuple(v.first,v.second); });
    module.def("positioning_row_col_to_position", &tft::PositioningEngine::row_col_to_position);
    module.def("positioning_get_neighbors", &tft::PositioningEngine::get_neighbors, py::arg("position"), py::arg("include_diagonal")=true);
    module.def("positioning_evaluate_unit_placement", &tft::PositioningEngine::evaluate_unit_placement, py::arg("board"), py::arg("position"), py::arg("candidate_role")=-2);
    module.def("positioning_evaluate_protection", &tft::PositioningEngine::evaluate_protection);
    module.def("positioning_evaluate_board_positioning", &tft::PositioningEngine::evaluate_board_positioning);
    module.def("positioning_find_best_position", [](const std::vector<int>& board,int role,const std::vector<int>& candidates) { auto v=tft::PositioningEngine::find_best_position(board,role,candidates); return py::make_tuple(v.first,v.second); }, py::arg("board"),py::arg("role"),py::arg("candidate_positions")=std::vector<int>{});
    module.def("positioning_find_best_swap", [](const std::vector<int>& board,int source,const std::vector<int>& candidates) { auto v=tft::PositioningEngine::find_best_swap(board,source,candidates); return py::make_tuple(v.first,v.second); }, py::arg("board"),py::arg("source_position"),py::arg("candidate_positions")=std::vector<int>{});
    module.def("positioning_is_board_stable", &tft::PositioningEngine::is_board_stable, py::arg("board"),py::arg("tolerance")=0.01);
    module.def("positioning_get_normalized_score", &tft::PositioningEngine::get_normalized_positioning_score);
}
