
#pragma once

#include "combat/CombatInput.hpp"
#include "items/ItemActionContract.hpp"

#include <array>
#include <cstddef>
#include <cstdint>
#include <memory>
#include <optional>
#include <string>
#include <utility>
#include <vector>

namespace tft::combat_evidence {
struct SurvivalRiskEvidence;
}

namespace tft {

inline constexpr std::size_t kPlayersPerLobby = 8;
inline constexpr std::size_t kBoardSlots = 28;
inline constexpr std::size_t kBenchSlots = 9;
inline constexpr std::size_t kShopSlots = 5;
inline constexpr std::size_t kActionComponents = 6;

inline constexpr std::array<std::size_t, kActionComponents>
    kActionDims{9, 5, 9, 28, 28, 28};


 // ============================================================
 // 🧩 CATÁLOGO ESTÁTICO DE CAMPEÕES
 // ============================================================

// Atributos-base normalizados pelo UnitManager.py.
struct ChampionStats {
    double max_hp{0.0};
    double attack_damage{0.0};
    double attack_speed{0.0};
    double armor{0.0};
    double magic_resist{0.0};
    double attack_range{0.0};
};

// Perfil de combate já calculado pelo gerador Python.
struct ChampionCombatProfile {
    std::int32_t role{3};
    std::string role_name{"fighter"};

    bool frontline{false};
    bool backline{false};

    bool is_tank{false};
    bool is_carry{false};
    bool is_support{false};
    bool is_fighter{false};
    bool is_assassin{false};

    double attack_range{0.0};
    double attack_speed{0.0};
    double attack_damage{0.0};
    double armor{0.0};
    double magic_resist{0.0};
    double max_hp{0.0};
    double max_mana{0.0};
};

// Variável da habilidade, preservando os valores por nível.
struct ChampionAbilityVariable {
    std::string name;
    std::vector<double> values;
};

// Dados estáticos da habilidade.
struct ChampionAbility {
    std::string name;
    std::string description;
    std::string icon;
    std::vector<ChampionAbilityVariable> variables;
};

// Registro estático de um campeão do units_gerado.json.
//
// internal_id:
//   Índice interno usado pelo UnitManager Python.
//
// api_name / character_name:
//   Identificadores originais do catálogo.
//
// Esta estrutura NÃO representa uma cópia comprada por jogador.
struct ChampionDefinition {
    std::int32_t internal_id{-1};

    std::string api_name;
    std::string character_name;
    std::string name;

    std::int32_t cost{1};
    std::int32_t role{3};
    std::string role_name{"fighter"};

    std::vector<std::string> traits;

    ChampionStats stats;
    ChampionCombatProfile combat_profile;
    ChampionAbility ability;

    std::string icon;
    std::string square_icon;
    std::string tile_icon;
};


 // ============================================================
// 🧍 INSTÂNCIA INDIVIDUAL DE UMA UNIDADE
// ============================================================
//
// ChampionDefinition = dados estáticos do campeão.
// UnitInstance      = identidade e estado de uma cópia.
//
// Exemplo:
//   ChampionDefinition: Teemo, custo 2, atributos-base.
//   UnitInstance A: Teemo, UUID A, 1 estrela.
//   UnitInstance B: Teemo, UUID B, 2 estrelas.
//
// As duas instâncias apontam para o mesmo campeão do catálogo,
// mas podem ter estados diferentes.

struct UnitInstance {
    // 🆔 Referência ao catálogo estático.
    // Corresponde ao ID interno usado pelo UnitManager.py.
    std::int32_t champion_internal_id{-1};

    // Identificador original do campeão, normalmente apiName.
    std::string champion_id;

    // Identidade única desta cópia.
    // A geração efetiva do UUID será implementada posteriormente.
    std::string uuid;

    // ⭐ Estado mutável da unidade.
    std::int32_t star{1};

    // Equipment follows the individual copy, not the champion definition.
    std::vector<CombatItem> items;

    // Retorna se a instância possui uma referência válida.
    bool is_valid() const noexcept {
        return champion_internal_id >= 0 && !uuid.empty();
    }

    // Verifica se a quantidade de estrelas está dentro do
    // intervalo atualmente suportado pelo jogo.
    bool has_valid_star() const noexcept {
        return star >= 1 && star <= 3;
    }
};


// Ordem da policy atual.
// type, shop_slot, bench_slot, board_target,
// board_source, board_move_target.
struct PlayerAction {
    std::array<std::int32_t, kActionComponents> values{
        6, 0, 0, 0, 0, 0
    };
};

// Todas as máscaras são armazenadas como uint8_t:
// 0 = inválido, 1 = válido.
struct PlayerActionMasks {
    std::array<std::uint8_t, 9> type_mask{};
    std::array<std::uint8_t, 5> shop_mask{};
    std::array<std::uint8_t, 9> bench_source_mask{};
    std::array<std::uint8_t, 28> board_target_mask{};
    std::array<std::uint8_t, 28> board_source_mask{};

    // Row-major: [board_source, board_target].
    std::array<std::uint8_t, 28 * 28>
        board_move_target_masks{};

    std::array<std::uint8_t, 9> bench_move_source_mask{};

    // Row-major: [bench_source, board_target].
    std::array<std::uint8_t, 9 * 28>
        bench_to_board_target_masks{};

    // Item-action masks are conditional on action type and remain separate
    // from shop/movement masks even though the legacy action vector is six-wide.
    std::array<std::uint8_t, 9> item_inventory_mask{};
    std::array<std::uint8_t, 10> item_component_first_mask{};
    std::array<std::uint8_t, 10 * 10> item_component_pair_masks{};
    std::array<std::uint8_t, 37> item_target_mask{};
};

struct RewardState {
    double previous_board_power{0.0};
    double previous_positioning_score{0.0};
    double previous_synergy_score{0.0};
    std::int32_t previous_level{1};
    std::int32_t previous_gold{0};
    double last_combat_reward{0.0};
    double round_reward{0.0};
    double total_reward{0.0};
};

struct AuditUnitSnapshot {
    bool occupied{false};
    std::int32_t champion_internal_id{-1};
    std::string champion_id;
    std::string uuid;
    std::int32_t star{0};
    std::int32_t cost{0};
    std::vector<std::string> item_ids;
    // Exact static catalog membership from ChampionDefinition::traits.
    // This excludes item-granted traits and active trait counts.
    std::vector<std::string> trait_names;
    // Native target profile consumed by item-target action heads.
    std::int32_t role{3};
    double attack_damage{0.0};
    double attack_speed{0.0};
    double max_health{0.0};
    double armor{0.0};
    double magic_resist{0.0};
};

struct AuditItemCount { std::string catalog_id; std::uint32_t count{0}; };
struct AuditEquippedItemSnapshot { std::string unit_uuid; std::string location; std::int32_t slot{-1}; std::string catalog_id; };
struct AuditRetiredEquippedItemCount { std::string unit_uuid; std::string catalog_id; std::uint32_t count{0}; };
struct AuditRetiredAnvilSnapshot { std::uint64_t sequence{0}; std::int32_t kind{-1}; std::vector<std::string> options; };
// Combat rows inherit round/decision identity; each retains its own combat_sequence.
struct AuditCombatDamageEvent {
    std::uint64_t combat_sequence{0};
    float timestamp{0.0f};
    std::int32_t source_unit_id{-1};
    std::int32_t target_unit_id{-1};
    std::int32_t source_player_id{-1};
    std::int32_t target_player_id{-1};
    std::string source_unit_uuid;
    std::string target_unit_uuid;
    std::uint8_t damage_type{0};
    float raw_damage{0.0f};
    float final_damage{0.0f};
    bool critical{false};
    bool ability_damage{false};
};
struct AuditCombatAttackEvent {
    std::uint64_t combat_sequence{0};
    float timestamp{0.0f};
    std::int32_t source_unit_id{-1};
    std::int32_t target_unit_id{-1};
    std::int32_t source_player_id{-1};
    std::int32_t target_player_id{-1};
    std::string source_unit_uuid;
    std::string target_unit_uuid;
    bool critical{false};
    float damage{0.0f};
};
struct AuditCombatDeathEvent {
    std::uint64_t combat_sequence{0};
    float timestamp{0.0f};
    std::int32_t unit_id{-1};
    std::int32_t killer_unit_id{-1};
    std::int32_t unit_player_id{-1};
    std::int32_t killer_player_id{-1};
    std::string unit_uuid;
    std::string killer_unit_uuid;
};
struct AuditEconomyResolutionEvent {
    std::string contract_id{"tft.economy-resolution-event"};
    std::uint32_t contract_version{2};
    std::string source_namespace{"tft.economy-engine.resolve-round"};
    std::string producer{"EconomyEngine::resolve_round"};
    // Engine/episode/snapshot/player sequence are inherited from AuditSnapshot.
    std::int32_t player_id{-1};
    // The completed preparation round and the next round receiving this income.
    std::uint32_t resolved_after_round{0};
    std::int32_t income_for_round{0};
    std::int32_t old_gold{0};
    std::int32_t gold_before_interest{0};
    std::int32_t gold_before_income{0};
    std::int32_t new_gold{0};
    std::int32_t base_gold{0};
    std::int32_t interest_gold{0};
    std::int32_t streak_gold{0};
    std::int32_t win_gold{0};
    std::int32_t total_gold{0};
    std::int32_t old_level{0};
    std::int32_t new_level{0};
    bool leveled_up{false};
    std::int32_t xp{0};
    std::int32_t xp_to_next{0};
};

struct AuditPvpResultCreditEvent {
    std::string contract_id{"tft.pvp-result-credit-event"};
    std::uint32_t contract_version{2};
    std::string source_namespace{"tft.economy-engine.register-pvp-win"};
    std::string producer{"EconomyEngine::register_pvp_win"};
    // Identity and round are inherited; combat_sequence identifies this specific matchup.
    std::uint64_t combat_sequence{0};
    std::int32_t winner_player_id{-1};
    std::int32_t loser_player_id{-1};
    std::int32_t gold_before_credit{0};
    std::int32_t gold_after_credit{0};
    std::int32_t credited_gold{0};
    std::int32_t win_streak_before{0};
    std::int32_t win_streak_after{0};
};

struct AuditUnitCopyProgressSnapshot {
    std::int32_t champion_internal_id{-1};
    std::int32_t owned_copy_equivalent{0};
    std::int32_t copies_toward_next_star{0};
    std::int32_t highest_star{0};
};

struct AuditUnitStrategicPrioritySnapshot {
    std::int32_t champion_internal_id{-1};
    std::int32_t intent{0};
    std::int32_t relation{0};
    std::int32_t priority{0};
    std::int32_t target_star{0};
    bool sale_restricted{false};
    double confidence{0.0};
    std::int32_t tier{6};
    std::int32_t copies_owned{0};
    std::int32_t highest_star{1};
    bool on_board{false};
    double board_contribution{0.0};
    double synergy_contribution{0.0};
    std::array<std::int32_t, 4> copies_by_star{};
    std::int32_t copies_in_shop{0};
    std::int32_t affordable_shop_copies{0};
    std::int32_t copies_toward_next_star{0};
    std::int32_t copies_needed_for_next_star{0};
    std::int32_t pool_remaining{-1};
    bool pool_known{false};
    bool target_unit{false};
    bool has_pair{false};
    std::int32_t copies_needed_for_pair{0};
};

struct AuditUnitOpportunityCostSnapshot {
    std::int32_t champion_internal_id{-1};
    double value{0.0};
    double uncertainty{1.0};
    std::uint32_t horizon_rounds{0};
    std::string source;
    std::string forgone_candidate_id;
    std::string value_basis;
};

struct AuditStrategicOwnerSnapshot {
    std::string contract_id{"tft.strategic-owner-observation"};
    std::uint32_t contract_version{4};
    std::string source_namespace{"tft.engine.strategic-owners"};
    std::string producer{"TFTEngine::get_audit_snapshot"};
    std::uint64_t episode_id{0};
    std::uint64_t player_decision_sequence{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    bool active_composition_valid{false};
    std::string active_composition_id;
    std::uint64_t active_composition_version{0};
    std::uint64_t active_source_sequence{0};
    std::vector<std::int32_t> active_unit_ids;
    std::vector<std::int32_t> active_core_unit_ids;
    bool direction_valid{false};
    std::string direction_identity;
    std::string direction_value;
    bool direction_composition_bound{false};
    std::string direction_composition_identity;
    std::uint64_t direction_composition_version{0};
    double direction_confidence{0.0};
    std::string direction_reason;
    std::int32_t direction_lifecycle{0};
    std::vector<std::int32_t> direction_evidence;
    std::string direction_value_for_diagnostics;
    std::uint32_t direction_selected_round{0};
    std::vector<std::int32_t> direction_reference_unit_ids;
    bool pivot_candidate_valid{false};
    std::string pivot_candidate_identity;
    std::string pivot_target_composition_identity;
    std::string pivot_target_direction;
    std::string pivot_source_direction_identity;
    double pivot_confidence{0.0};
    std::string pivot_reason;
    std::int32_t pivot_lifecycle{0};
    std::vector<std::int32_t> pivot_evidence;
    // Internal diagnostic for native pivot proposal production; not serialized.
    std::string pivot_generation_diagnostic_for_diagnostics;
    std::uint64_t pivot_source_composition_version{0};
    std::vector<std::int32_t> pivot_reference_unit_ids;
    // Values are produced by strategy::UnitCopyProgress from this snapshot's
    // physical board/bench copies; the Python projection must not recalculate.
    std::vector<AuditUnitCopyProgressSnapshot> unit_copy_progress;
    // False means unavailable, never a measured zero.
    bool opportunity_cost_available{false};
    // Sequence consumed by strategic evidence/candidate/action owners; a distinct scope.
    // Appended to preserve existing aggregate initialization.
    std::uint64_t strategic_context_sequence{0};
    // Same-cycle native planner outputs projected as PPO context, never as forced actions.
    bool planner_outputs_valid{false};
    std::uint64_t planner_output_sequence{0};
    std::vector<AuditUnitStrategicPrioritySnapshot> unit_priorities;
    std::vector<AuditUnitOpportunityCostSnapshot> opportunity_costs;
    std::vector<std::int32_t> lineup_selected_unit_ids;
    std::vector<std::int32_t> lineup_entry_unit_ids;
    std::vector<std::int32_t> lineup_exit_unit_ids;
    std::vector<std::int32_t> lineup_deferred_unit_ids;
    std::vector<std::int32_t> lineup_bridge_unit_ids;
    std::vector<std::int32_t> lineup_endgame_target_unit_ids;
    bool strategic_refresh_failed{false};
    std::string strategic_refresh_failure_reason;
};

struct AuditBoardRelationSnapshot {
    std::int32_t slot{-1};
    std::int32_t row{-1};
    std::int32_t column{-1};
    std::int32_t role{-1};
    std::string unit_uuid;
    // Stable board-slot references; no duplicate UnitInstance or champion maps.
    std::vector<std::int32_t> adjacent_slots;
    std::vector<std::int32_t> frontline_slots_in_front;
    std::uint32_t adjacent_occupied_count{0};
    std::uint32_t tanks_in_front{0};
    std::uint32_t fighters_in_front{0};
};

struct AuditPlayerSnapshot {
    std::int32_t player_id{-1};
    AuditStrategicOwnerSnapshot strategic_state{};
    // Player survival and standing facts, correlated by the enclosing snapshot identity.
    double hp{100.0};
    double damage_taken{0.0};
    bool alive{true};
    std::int32_t wins{0};
    std::int32_t losses{0};
    std::optional<std::int32_t> placement;
    std::optional<std::int32_t> opponent_id;
    std::int32_t gold{0};
    std::int32_t level{0};
    std::int32_t xp{0};
    std::int32_t win_streak{0};
    std::int32_t loss_streak{0};
    std::int32_t gold_before_interest{0};
    std::int32_t interest_if_resolved_now{0};
    double board_power{0.0};
    double synergy_score{0.0};
    double positioning_score{0.0};
    // Keep native board-evaluation diagnostics in the audit snapshot; the
    // Viewer cannot reconstruct structural quality from board power alone.
    double board_quality_score{0.0};
    double board_positional_score{0.0};
    double board_structural_score{0.0};
    double board_quality_delta{0.0};
    std::int32_t board_exposed_carries{0};
    std::int32_t board_frontline_count{0};
    std::int32_t board_isolated_frontline_count{0};
    std::int32_t board_important_bench_units_unplayed{0};
    std::int32_t board_frontline_lane_count{0};
    std::int32_t board_exposed_main_carries{0};
    std::int32_t board_fragile_frontline_count{0};
    std::int32_t board_missing_frontline_count{0};
    std::int32_t board_missing_backline_count{0};
    std::int32_t board_active_trait_count{0};
    double board_strategic_fit_score{0.0};
    double board_unit_quality_score{0.0};
    double board_trait_coherence_score{0.0};
    std::int32_t round_gold{0};
    std::int32_t round_base_gold{0};
    std::int32_t round_interest{0};
    std::int32_t round_streak_gold{0};
    std::int32_t round_win_gold{0};
    // Read-only relation facts over the exact board geometry and occupied slots.
    std::string positioning_contract_id{"tft.board-position-relations"};
    std::uint32_t positioning_contract_version{1};
    std::string positioning_producer{"TFTEngine::get_audit_snapshot"};
    std::vector<AuditBoardRelationSnapshot> board_relations;
    std::array<AuditUnitSnapshot, kBoardSlots> board{};
    std::array<AuditUnitSnapshot, kBenchSlots> bench{};
    std::array<AuditUnitSnapshot, kShopSlots> shop{};
    std::array<std::uint64_t, kShopSlots> shop_offer_revisions{};
    // Item state is part of the audit snapshot so the viewer can distinguish
    // loose components, completed items in the bag, and unit equipment.
    std::vector<std::string> item_components;
    std::vector<std::string> item_inventory;
    std::vector<AuditItemCount> item_component_counts;
    std::vector<AuditItemCount> item_inventory_counts;
    std::vector<AuditEquippedItemSnapshot> equipped_items;
    bool item_ownership_retired{false};
    std::vector<AuditItemCount> retired_item_component_counts;
    std::vector<AuditItemCount> retired_item_inventory_counts;
    std::vector<AuditRetiredEquippedItemCount> retired_equipped_item_counts;
    std::vector<AuditRetiredAnvilSnapshot> retired_pending_anvils;
    std::vector<std::string> item_component_catalog;
    bool pending_anvil{false};
    std::uint64_t pending_anvil_sequence{0};
    std::int32_t pending_anvil_kind{-1};
    std::vector<std::string> pending_anvil_options;
    // Structured native item observations. These are populated from the same
    // ItemEngine/catalog/profile producers as the legacy observation writer.
    std::array<float, 10> item_component_features{};
    std::array<std::array<float, 17>, 9> item_inventory_features{};
    std::array<std::array<float, 17>, 100> item_recipe_features{};
    std::array<std::array<float, 37>, 9> item_inventory_target_fit{};
    std::array<std::array<float, 37>, 100> item_recipe_target_fit{};
    std::array<std::array<float, 11>, 9> pending_anvil_option_features{};
    // Native temporal facts used by the PPO semantic global encoder.
    std::uint32_t actions_taken_this_round{0};
    std::array<std::uint32_t, kBoardSlots> board_move_age{};
    // Last item decision is carried by the post-action snapshot for exact
    // Viewer attribution (normal equip/craft versus forced anvil selection).
    std::string last_item_action_kind;
    std::string last_item_id;
    std::string last_item_first_component;
    std::string last_item_second_component;
    std::string last_item_target_uuid;
    std::int32_t last_item_target_slot{-1};
    bool last_item_target_on_board{false};
    double last_item_fit{0.0};
    double last_item_immediate_strength{0.0};
    double last_item_role_alignment{0.0};
    double last_item_assignment_reward{0.0};
    PlayerActionMasks masks{};
};

struct AuditPoolChampionCount {
    std::int32_t champion_internal_id{-1};
    std::string champion_id;
    std::int32_t cost{0};
    std::int32_t initial_count{0};
    std::int32_t available_count{0};
};
struct AuditSharedPoolSnapshot {
    std::string contract_id{"tft.shared-champion-pool-snapshot"};
    std::uint32_t contract_version{2};
    std::string producer{"UnitPool::available"};
    // Correlation identity and source namespace are inherited from AuditSnapshot.
    std::int64_t total_available{0};
    std::vector<AuditPoolChampionCount> champions;
};
struct AuditSnapshot {
    AuditSharedPoolSnapshot shared_pool;
    std::string contract_id{"tft.native-state-snapshot"};
    std::uint32_t contract_version{6};
    // Current native board-slot geometry: rectangular 4x7, not canonical hex.
    std::string board_geometry_id{"tft.board-grid.rectangular-4x7"};
    std::uint32_t board_geometry_version{1};
    std::uint32_t board_rows{4};
    std::uint32_t board_columns{7};
    std::string board_position_formula{"row=slot/7;column=slot%7"};
    std::string source_namespace{"tft.engine.observation-snapshot"};
    std::string producer{"TFTEngine::get_audit_snapshot"};
    std::string engine_instance_id;
    std::uint64_t episode_id{0};
    std::uint64_t snapshot_sequence{0};
    std::array<std::uint64_t, kPlayersPerLobby> player_decision_sequences{};
    std::uint32_t round{0};
    std::uint32_t stage{1};
    bool finished{false};
    std::uint64_t combat_sequence{0};
    bool combat_damage_events_truncated{false};
    std::vector<AuditCombatDamageEvent> combat_damage_events;
    bool combat_attack_events_truncated{false};
    std::vector<AuditCombatAttackEvent> combat_attack_events;
    bool combat_death_events_truncated{false};
    std::vector<AuditCombatDeathEvent> combat_death_events;
    std::vector<AuditEconomyResolutionEvent> economy_resolution_events;
    std::vector<AuditPvpResultCreditEvent> pvp_result_credit_events;
    std::array<AuditPlayerSnapshot, kPlayersPerLobby> players{};
};


struct ResetResult {
    std::string engine_instance_id;
    // Row-major: (8, observation_dim).
    std::vector<float> observations;
    std::size_t observation_dim{0};

    std::array<PlayerActionMasks, kPlayersPerLobby>
        action_masks{};

    std::uint64_t episode_id{0};
    // Monotonic per Engine instance; identifies the exact published observation/mask snapshot.
    std::uint64_t decision_sequence{0};
    // Per-player decision-snapshot sequence; advances with every published row.
    std::array<std::uint64_t, kPlayersPerLobby> player_decision_sequences{};
    // Structured native facts captured atomically with observations and masks.
    AuditSnapshot native_state_snapshot{};
};


struct PlayerInfo {
    std::int32_t player_id{-1};

    float hp{100.0f};
    std::int32_t gold{0};
    std::int32_t level{1};
    std::int32_t xp{0};

    bool alive{true};
    bool eliminated{false};

    std::int32_t wins{0};
    std::int32_t losses{0};

    std::optional<std::int32_t> placement;
    std::optional<std::int32_t> opponent_id;

    float damage_taken{0.0f};

    // Per-action board quality diagnostics; exposed for Viewer/audit correlation
    // with combat outcomes rather than treating heuristics as ground truth.
    double board_quality_score{0.0};
    double board_positional_score{0.0};
    double board_structural_score{0.0};
    double board_quality_delta{0.0};
    std::int32_t board_exposed_carries{0};
    std::int32_t board_frontline_count{0};
    std::int32_t board_isolated_frontline_count{0};
    std::int32_t board_important_bench_units_unplayed{0};
};

struct AntiLoopMetrics {
    // Nomes alinhados ao AntiLoopManager.execution_metrics.
    std::uint64_t execution_attempts{0};
    std::uint64_t execution_blocks{0};

    std::uint64_t blocked_reverse{0};
    std::uint64_t blocked_oscillation{0};
    std::uint64_t blocked_explicit{0};
    std::uint64_t blocked_bench_board_loop{0};
    std::uint64_t blocked_cycle{0};

    std::uint64_t board_moves_executed{0};
    std::uint64_t bench_to_board_executed{0};

    // Contadores cumulativos da geração de máscaras, separados da execução.
    std::uint64_t mask_board_move_candidates{0};
    std::uint64_t mask_board_move_valid{0};
    std::uint64_t mask_board_move_blocked_anti_loop{0};
    std::uint64_t mask_board_move_blocked_seen_state{0};
    std::uint64_t mask_bench_move_candidates{0};
    std::uint64_t mask_bench_move_valid{0};
    std::uint64_t mask_bench_move_blocked_anti_loop{0};
    std::uint64_t mask_bench_move_blocked_seen_state{0};
    std::uint64_t mask_blocked_reverse{0};
    std::uint64_t mask_blocked_oscillation{0};
    std::uint64_t mask_blocked_explicit{0};
    std::uint64_t mask_blocked_bench_board_loop{0};
    std::uint64_t mask_blocked_cycle{0};
};


struct ActionExecutionTrace {
    std::string contract_id{"tft.action-execution-event"};
    std::uint32_t contract_version{1};
    std::string source_namespace{"tft.engine.action-execution"};
    std::string producer{"TFTEngine::step"};
    // Explicit owner of this trace; array position alone is not identity.
    std::int32_t player_id{-1};
    std::array<std::int32_t, kActionComponents> requested_action{};
    std::array<std::int32_t, kActionComponents> effective_action{};
    // True only when the native action handler reports successful application.
    bool handler_applied{false};
    // Stable machine-readable reason; never inferred from reward values.
    std::string status_reason;
    // Causal identity inherited from the source and outcome decision snapshots.
    std::uint64_t source_snapshot_sequence{0};
    std::uint64_t outcome_snapshot_sequence{0};
    std::uint64_t source_player_decision_sequence{0};
    std::uint64_t outcome_player_decision_sequence{0};
    std::uint32_t source_round{0};
    std::uint32_t outcome_round{0};
    std::uint32_t source_stage{0};
    std::uint32_t outcome_stage{0};
};

struct StepResult {
    std::string engine_instance_id;
    // Row-major: (8, observation_dim).
    std::vector<float> observations;
    std::size_t observation_dim{0};

    std::array<float, kPlayersPerLobby> rewards{};
    // Componentes expostos separadamente para auditoria de paridade.
    std::array<float, kPlayersPerLobby> action_rewards{};
    std::array<float, kPlayersPerLobby> combat_rewards{};
    std::array<float, kPlayersPerLobby> placement_rewards{};
    std::array<std::uint8_t, kPlayersPerLobby> dones{};

    std::array<PlayerActionMasks, kPlayersPerLobby>
        action_masks{};

    std::array<PlayerInfo, kPlayersPerLobby> players{};
    // Per-player trace linking caller input to Engine-normalized and applied action.
    std::array<ActionExecutionTrace, kPlayersPerLobby> action_traces{};

    bool lobby_done{false};
    std::uint64_t episode_id{0};
    // Monotonic per Engine instance; identifies the exact published observation/mask snapshot.
    std::uint64_t decision_sequence{0};
    // Per-player decision-snapshot sequence; advances with every published row.
    std::array<std::uint64_t, kPlayersPerLobby> player_decision_sequences{};
    std::uint32_t round{0};
    std::uint32_t stage{1};
    std::int32_t alive_players{8};
    // Structured native facts captured atomically with observations and masks.
    AuditSnapshot native_state_snapshot{};

    // Diagnósticos adicionais sem acoplar o PPO às engines.
    std::vector<std::string> events;
};

struct PublicState {
    std::uint32_t stage{1};
    std::uint32_t round{1};
    std::uint32_t round_index{0};

    bool finished{false};
    std::optional<std::int32_t> winner_id;

    std::vector<std::int32_t> ranking;
    std::vector<std::int32_t> alive_players;
    std::vector<PlayerInfo> players;
};




class TFTEngine {
public:
    explicit TFTEngine(
        std::uint64_t seed = 0,
        std::string catalog_path = {},
        std::string item_catalog_path = {}
    );

    ~TFTEngine();

    TFTEngine(const TFTEngine&) = delete;
    TFTEngine& operator=(const TFTEngine&) = delete;

    TFTEngine(TFTEngine&&) noexcept;
    TFTEngine& operator=(TFTEngine&&) noexcept;

    ResetResult reset(
        std::optional<std::uint64_t> seed = std::nullopt
    );

    // timer_enabled=true: a lobby step cannot resolve preparation until
    // timer_expired=true. When expired, all living players are forced to PASS.
    // Defaults preserve turn-based PPO/training behavior.
    StepResult step(
        const std::array<PlayerAction, kPlayersPerLobby>& actions,
        bool timer_enabled = false,
        bool timer_expired = false
    );

    std::array<PlayerActionMasks, kPlayersPerLobby>
    get_action_masks() const;
    AuditSnapshot get_audit_snapshot() const;

    // Read-only identity map from the exact catalog loaded by this engine.
    // Keys are units_gerado.json apiName values; values are native internal IDs.
    std::vector<std::pair<std::int32_t, std::string>>
    get_champion_api_name_map() const;

    // Adapt OP.GG compositions against this engine's loaded native catalog.
    // Input/output are JSON strings to keep catalog types out of the public API.
    std::string adapt_opgg_compositions_json(const std::string& catalog_json) const;
    std::vector<std::string> get_composition_diagnostics_jsonl() const;

    // Configures the optional session sidecar for unified strategic Shadow events.
    void set_strategic_direction_pivot_audit_path(const std::string& path);

    // Injects one approved, identity-bound combat risk for the next Shadow
    // decision snapshot. Experimental projections are rejected by the contract.
    // This never changes PPO observations, rewards, masks or action execution.
    bool publish_combat_prediction_evidence(
        const combat_evidence::SurvivalRiskEvidence& evidence
    );

    // Hooks de fixture determinística para testes de paridade Python/C++.
    // Não alteram o pool compartilhado; usar apenas em cenários de teste.
    bool set_unit_for_testing(
        std::int32_t player_id,
        bool on_board,
        std::int32_t slot,
        const std::string& champion_api_name,
        std::int32_t star = 1
    );
    // Deterministic fixture hook for combat/equipment regression tests only.
    bool set_unit_items_for_testing(
        std::int32_t player_id,
        bool on_board,
        std::int32_t slot,
        const std::vector<CombatItem>& items
    );
    // Returns the same combat-team conversion used by normal match resolution.
    // Test hook verifies that lobby equipment reaches CombatEngine unchanged.
    CombatTeam get_combat_team_for_testing(
        std::int32_t player_id, UnitTeam team = UnitTeam::PLAYER_A
    ) const;
    // Event hooks for the authoritative loot/armory source; these are not policy actions.
    bool grant_item_component(std::int32_t player_id, const std::string& component_id);
    bool grant_completed_item(std::int32_t player_id, const std::string& item_id);
    bool add_item_component_for_testing(
        std::int32_t player_id, const std::string& component_id
    );
    bool add_completed_item_for_testing(
        std::int32_t player_id, const std::string& item_id
    );
    bool set_player_alive_for_testing(std::int32_t player_id, bool alive);
    bool set_player_hp_for_testing(std::int32_t player_id, float hp);
    bool set_player_economy_for_testing(
        std::int32_t player_id, std::int32_t gold,
        std::int32_t level, std::int32_t xp
    );
    bool set_shop_offer_for_testing(
        std::int32_t player_id, std::int32_t slot,
        const std::string& champion_api_name
    );
    bool set_next_shop_roll_for_testing(
        std::int32_t player_id,
        const std::vector<std::string>& champion_api_names
    );

    // Controla o bloqueio da loja sem alterar as dimensões da policy PPO.
    bool set_shop_locked(std::int32_t player_id, bool locked);
    bool toggle_shop_lock(std::int32_t player_id);
    bool is_shop_locked(std::int32_t player_id) const;

    // Neutral [players, 1] transport only. Decision features are read from
    // the identity-bound native semantic snapshot, never positional offsets.
    std::vector<float> get_observations() const;

    RewardState get_reward_state(std::int32_t player_id) const;
    double get_unit_comp_score(std::int32_t player_id, const std::string& champion_api_name, std::int32_t star = 1) const;
    bool is_core_unit(std::int32_t player_id, const std::string& champion_api_name) const;
    bool is_core_trait(std::int32_t player_id, const std::string& trait) const;

    std::array<AntiLoopMetrics, kPlayersPerLobby>
    get_anti_loop_metrics() const;

    PublicState get_public_state() const;

    // Consultas do estoque global de campeões.
    std::int32_t pool_available(
        std::int32_t champion_internal_id
    ) const;

    std::int32_t pool_initial_count(
        std::int32_t champion_internal_id
    ) const;

    std::int64_t pool_total_available() const;

    std::size_t observation_dim() const noexcept;
    std::string engine_instance_id() const;
    std::uint64_t episode_id() const noexcept;
    std::uint32_t round() const noexcept;
    std::uint32_t stage() const noexcept;
    std::int32_t alive_players() const noexcept;
    bool is_done() const noexcept;

    void close() noexcept;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace tft
