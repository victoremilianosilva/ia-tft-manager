
#pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <memory>
#include <optional>
#include <string>
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
};

struct StrategyInfo {
    // Valores compatíveis com StrategyManager.py.
    std::int32_t strategy{0};
    std::string strategy_name{"ECON"};

    std::optional<std::int32_t> previous_strategy;

    float confidence{0.0f};
    std::int32_t strategy_age{0};
    std::string reason;
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
};


struct StepResult {
    // Row-major: (8, observation_dim).
    std::vector<float> observations;
    std::size_t observation_dim{0};

    std::array<float, kPlayersPerLobby> rewards{};
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


class TFTEngine {
public:
    explicit TFTEngine(std::uint64_t seed = 0);
    ~TFTEngine();

    TFTEngine(const TFTEngine&) = delete;
    TFTEngine& operator=(const TFTEngine&) = delete;

    TFTEngine(TFTEngine&&) noexcept;
    TFTEngine& operator=(TFTEngine&&) noexcept;

    ResetResult reset(
        std::optional<std::uint64_t> seed = std::nullopt
    );

    StepResult step(
        const std::array<PlayerAction, kPlayersPerLobby>& actions
    );

    std::array<PlayerActionMasks, kPlayersPerLobby>
    get_action_masks() const;

    std::vector<float> get_observations() const;

    std::array<std::vector<StrategyInfo>, kPlayersPerLobby>
    get_strategies() const;

    std::array<AntiLoopMetrics, kPlayersPerLobby>
    get_anti_loop_metrics() const;

    PublicState get_public_state() const;

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
