
#pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <memory>
#include <optional>
#include <string>
#include <utility>
#include <vector>

namespace tft {

inline constexpr std::size_t kPlayersPerLobby = 8;
inline constexpr std::size_t kBoardSlots = 28;
inline constexpr std::size_t kBenchSlots = 9;
inline constexpr std::size_t kShopSlots = 5;
inline constexpr std::size_t kActionComponents = 6;

inline constexpr std::array<std::size_t, kActionComponents>
    kActionDims{7, 5, 9, 28, 28, 28};


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
    std::array<std::uint8_t, 7> type_mask{};
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

struct ResetResult {
    // Row-major: (8, observation_dim).
    std::vector<float> observations;
    std::size_t observation_dim{0};

    std::array<PlayerActionMasks, kPlayersPerLobby>
        action_masks{};

    std::uint64_t episode_id{0};
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

struct StrategyInfo {
    // Valores compatíveis com StrategyManager.py.
    std::int32_t strategy{0};
    std::string strategy_name{"ECON"};

    std::optional<std::int32_t> previous_strategy;

    float confidence{0.0f};
    std::int32_t strategy_age{0};
    std::string reason;
    bool changed{false};
    float state_confidence{0.0f};
    std::int32_t best_scored_strategy{0};
    std::vector<std::pair<std::int32_t, double>> strategy_scores;
    double board_power{0.0};
    double bench_strength{0.0};
    std::int32_t active_traits_count{0};

    // Snapshot de CompositionManager: foco/direção e elementos core.
    std::string composition_focus;
    std::int32_t composition_focus_id{-1};
    std::string composition_direction;
    // Persistent state migrated from Python comp_direction/comp_focus logic.
    bool composition_locked{false};
    std::uint32_t comp_direction_update_steps{0};
    std::int32_t comp_stabilize_start_round{-1};
    double composition_strength{0.0};
    // Hysteresis state and auditable direction-transition diagnostics.
    std::string composition_candidate_direction;
    double composition_candidate_strength{0.0};
    std::uint32_t composition_candidate_streak{0};
    std::string previous_composition_direction;
    double previous_composition_strength{0.0};
    bool composition_direction_change_was_locked{false};
    std::int32_t composition_direction_change_round{0};
    double composition_direction_change_focus_weight{0.0};
    std::string composition_direction_change_reason{"initial"};
    std::uint64_t composition_direction_change_count{0};
    std::vector<std::pair<std::string, double>> composition_focus_weights;
    std::vector<std::string> core_units;
    std::vector<std::int32_t> core_unit_ids;
    std::vector<std::string> core_traits;
    // Explicit target lineup planned from the full champion pool. Unlike
    // core_units (owned/observed pieces), these may include units not acquired yet.
    std::vector<std::string> planned_units;
    std::vector<std::int32_t> planned_unit_ids;
    std::vector<std::string> planned_traits;
    std::int32_t planned_main_carry_id{-1};
    double planned_composition_score{0.0};
    std::vector<std::pair<std::string, std::int32_t>> active_traits;
    std::vector<std::pair<std::string, std::int32_t>> unit_counts;
    std::vector<std::pair<std::int32_t, std::int32_t>> unit_counts_by_id;
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


struct StepResult {
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

    bool lobby_done{false};
    std::uint64_t episode_id{0};
    std::uint32_t round{0};
    std::uint32_t stage{1};
    std::int32_t alive_players{8};

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


struct AuditUnitSnapshot {
    bool occupied{false};
    std::string champion_id;
    std::string uuid;
    std::int32_t star{0};
    std::int32_t cost{0};
};

struct AuditPlayerSnapshot {
    std::int32_t player_id{-1};
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
    std::int32_t round_gold{0};
    std::int32_t round_base_gold{0};
    std::int32_t round_interest{0};
    std::int32_t round_streak_gold{0};
    std::int32_t round_win_gold{0};
    std::array<AuditUnitSnapshot, kBoardSlots> board{};
    std::array<AuditUnitSnapshot, kBenchSlots> bench{};
    std::array<AuditUnitSnapshot, kShopSlots> shop{};
    PlayerActionMasks masks{};
};

struct AuditSnapshot {
    std::uint32_t round{0};
    std::uint32_t stage{1};
    bool finished{false};
    std::array<AuditPlayerSnapshot, kPlayersPerLobby> players{};
};


class TFTEngine {
public:
    explicit TFTEngine(
        std::uint64_t seed = 0,
        std::string catalog_path = {}
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

    // Hooks de fixture determinística para testes de paridade Python/C++.
    // Não alteram o pool compartilhado; usar apenas em cenários de teste.
    bool set_unit_for_testing(
        std::int32_t player_id,
        bool on_board,
        std::int32_t slot,
        const std::string& champion_api_name,
        std::int32_t star = 1
    );
    bool set_player_alive_for_testing(std::int32_t player_id, bool alive);
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

    std::vector<float> get_observations() const;

    std::array<std::vector<StrategyInfo>, kPlayersPerLobby>
    get_strategies() const;

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
