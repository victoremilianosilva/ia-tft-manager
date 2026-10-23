
#include "lobby/TftEngine.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <map>
#include <limits>
#include <unordered_map>
#include <nlohmann/json.hpp>
#include <memory>
#include <optional>
#include <random>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#include "lobby/ChampionCatalog.hpp"
#include "lobby/UnitInstanceFactory.hpp"
#include "lobby/UnitPool.hpp"
#include "lobby/EconomyEngine.hpp"
#include "combat/CombatEngine.hpp"
#include "lobby/ShopEngine.hpp"
#include "strategy/SynergyCounter.hpp"
#include "strategy/PositioningEngine.hpp"
#include "reward/RewardModel.hpp"

#include "decision/ActionMaskEngine.hpp"
#include "decision/DecisionState.hpp"
#include "decision/AntiLoopEngine.hpp"
#include "decision/MoveValidator.hpp"
#include "decision/DecisionTypes.hpp"

#ifndef TFT_DEFAULT_CATALOG_PATH
#define TFT_DEFAULT_CATALOG_PATH "units_gerado.json"
#endif

namespace tft {

namespace {

constexpr std::uint32_t kRoundsPerStage = 7;
constexpr std::size_t kCoreObservationDim = 22;
constexpr std::size_t kBoardObservationDim = kBoardSlots * 5;
constexpr std::size_t kBenchObservationDim = kBenchSlots * 5;
constexpr std::size_t kShopObservationDim = kShopSlots * 5;
constexpr std::size_t kExtraObservationDim = 5;
constexpr std::size_t kSynergyObservationDim = 5;
constexpr std::size_t kPositioningObservationDim = 4;
constexpr std::size_t kCapacityObservationDim = 2;
// Composition-aware features: direction and core-trait flags, plus fit scores
// for each board, bench, and shop slot.
constexpr std::size_t kCompositionUnitSlots =
    kBoardSlots + kBenchSlots + kShopSlots;
// Per-slot strategic features used by the policy's shared candidate scorers.
constexpr std::size_t kCandidateFeatureDim = 8;
constexpr std::size_t kStrategicCandidateObservationDim =
    (kBenchSlots + kShopSlots) * kCandidateFeatureDim;
constexpr std::size_t kActionMemoryObservationDim = 1 + kBoardSlots;
constexpr std::uint32_t kActionMemoryHorizon = 10;

std::int32_t stage_damage(std::uint32_t stage) noexcept {
    switch (stage) {
        case 1: return 0;
        case 2: return 2;
        case 3: return 6;
        case 4: return 7;
        case 5: return 10;
        case 6: return 12;
        case 7: return 17;
        default: return 17;
    }
}

// Internal round index follows TFT's actual 1-based round sequence:
 // 1-1..1-4 are opening/PvE; each following stage has seven rounds.
std::uint32_t stage_for_round(std::uint32_t round_number) noexcept {
    if (round_number <= 4) return 1;
    return 2 + (round_number - 5) / 7;
}

bool is_pvp_round(std::uint32_t round_number) noexcept {
    if (round_number <= 4) return false;
    const auto round_in_stage = ((round_number - 5) % 7) + 1;
    return round_in_stage != 4 && round_in_stage != 7;
}

std::int32_t star_copies(std::int32_t star) noexcept {
    switch (star) {
        case 2: return 3;
        case 3: return 9;
        default: return 1;
    }
}

std::uint64_t matchup_key(std::size_t a, std::size_t b) noexcept {
    const auto low = static_cast<std::uint32_t>(std::min(a, b));
    const auto high = static_cast<std::uint32_t>(std::max(a, b));
    return (static_cast<std::uint64_t>(low) << 32U) | high;
}

// Máscaras provisórias utilizadas como fallback.
PlayerActionMasks make_default_masks() {
    PlayerActionMasks masks{};

    masks.type_mask[6] = 1;
    masks.shop_mask[0] = 1;
    masks.bench_source_mask[0] = 1;
    masks.board_target_mask[0] = 1;
    masks.board_source_mask[0] = 1;
    masks.bench_move_source_mask[0] = 1;
    masks.board_move_target_masks[0] = 1;
    masks.bench_to_board_target_masks[0] = 1;

    return masks;
}

float role_state_value(std::int32_t role) {
    switch (role) {
        case 0: return 0.2f; // tank
        case 1: return 0.4f; // carry
        case 2: return 0.6f; // support
        case 3: return 0.8f; // fighter
        case 4: return 1.0f; // assassin
        default: return 0.0f;
    }
}

float unit_strength(const ChampionDefinition& def, const UnitInstance& unit) {
    const float cost = static_cast<float>(def.cost);
    const float star = static_cast<float>(unit.star);
    return std::min(1.0f, cost / 5.0f * 0.5f + star / 3.0f * 0.5f);
}

double unit_composition_score(
    const StrategyInfo& strategy,
    const ChampionDefinition& def,
    std::int32_t star
) {
    double score = 0.0;
    if (std::find(strategy.core_unit_ids.begin(), strategy.core_unit_ids.end(),
                  def.internal_id) != strategy.core_unit_ids.end())
        score += 5.0;
    if (!strategy.composition_direction.empty() &&
        std::find(def.traits.begin(), def.traits.end(),
                  strategy.composition_direction) != def.traits.end())
        score += 3.0;
    for (const auto& trait : def.traits) {
        if (std::find(strategy.core_traits.begin(), strategy.core_traits.end(),
                      trait) != strategy.core_traits.end())
            score += 2.0;
    }
    if (star >= 2) score += 2.0;
    if (star >= 3) score += 4.0;
    // Cost is an economy attribute, not composition fit. Adding it here made
    // every positive-cost unit look strategically compatible even with no trait/core match.
    return score;
}

} // namespace

// ============================================================
// IMPLEMENTAÇÃO INTERNA
// ============================================================

struct TFTEngine::Impl {
    struct PlayerTransition {
        float action_reward{0.0f};
        bool acted{false};
        bool board_capacity_violation{false};
    };

    struct PlayerEnv {
        // Estado e serviços pertencentes exclusivamente a um jogador.
        std::unique_ptr<ShopEngine> shop;
        std::array<std::optional<UnitInstance>, kBenchSlots> bench{};
        std::array<std::optional<UnitInstance>, kBoardSlots> board{};
        // Temporal context for the feed-forward policy: actions left this round
        // and age (in actions) of the unit occupying each board slot.
        std::array<std::uint32_t, kBoardSlots> board_move_age{};
        std::uint32_t actions_taken_this_round{0};
        decision::AntiLoopEngine anti_loop;
        PlayerInfo info{};
        PlayerActionMasks action_masks{};
        std::vector<StrategyInfo> strategy;
        AntiLoopMetrics anti_loop_metrics{};
        PlayerEconomy economy{};

        double previous_board_power{0.0};
        double previous_synergy_score{0.0};
        double previous_positioning_score{0.0};
        std::int32_t previous_reward_level{1};
        double last_combat_reward{0.0};
        double round_reward_total{0.0};
        double total_reward{0.0};
        bool placement_reward_given{false};
        struct RecentPurchase {
            std::string uuid;
            std::int32_t champion_id{-1};
            std::int32_t star{1};
            std::uint64_t action_serial{0};
            int cost{0};
            bool built_pair{false};
            bool completed_upgrade{false};
            bool was_deployed{false};
            double fit_score{0.0};
            double reward{0.0};
            std::string comp_direction;
        };
        std::uint64_t action_serial{0};
        std::vector<RecentPurchase> recent_purchases;

        PlayerTransition step(
            TFTEngine::Impl& lobby,
            std::size_t player_id,
            const PlayerAction& player_action
        );
    };
    std::uint64_t seed{0};
    std::uint64_t episode_id{0};
    std::mt19937_64 matchmaking_rng{0};
    std::set<std::uint64_t> previous_matchups;

    std::uint32_t round{0};
    std::uint32_t stage{1};

    std::optional<std::int32_t> winner_id;
    std::vector<std::int32_t> ranking;

    std::unique_ptr<ChampionCatalog> catalog;
    std::unique_ptr<UnitPool> pool;
    std::unique_ptr<UnitInstanceFactory> unit_factory;

    // Uma instância C++ por jogador; o lobby coordena as oito.
    std::array<PlayerEnv, kPlayersPerLobby> player_envs{};

    // Serviços compartilhados pela lobby, não pertencem a um jogador.
    EconomyEngine economy_engine;
    CombatEngine combat_engine;
    decision::ActionMaskEngine action_mask_engine;

    std::int32_t alive_players{
        static_cast<std::int32_t>(kPlayersPerLobby)
    };

    bool done{false};
    bool closed{false};

    // No treinamento, cada jogador recebe 10 ações por rodada; PASS também conta como ação.
    // O viewer usa o temporizador de parede e não aplica este limite de ações.
    static constexpr std::uint32_t kMaxActionsPerRound = 10;
    std::array<std::uint32_t, kPlayersPerLobby> round_actions{};
    std::array<bool, kPlayersPerLobby> round_finished{};

    std::unordered_map<std::string, std::vector<int>> trait_milestones;
    // Same insertion order as UnitManager.get_all_champions() -> traits.
    std::vector<std::string> observation_trait_names;

    explicit Impl(
        std::uint64_t initial_seed,
        const std::string& catalog_path
    ) : seed(initial_seed),
        matchmaking_rng(initial_seed) {
        const std::string resolved_path =
            catalog_path.empty()
                ? TFT_DEFAULT_CATALOG_PATH
                : catalog_path;

        catalog = std::make_unique<ChampionCatalog>(
            resolved_path
        );

        for (const auto& champion : catalog->all()) {
            for (const auto& trait : champion.traits) {
                if (std::find(observation_trait_names.begin(),
                              observation_trait_names.end(), trait)
                    == observation_trait_names.end()) {
                    observation_trait_names.push_back(trait);
                }
            }
        }

        // Usa os mesmos marcos de traits.json que SynergyManager.py,
        // em vez de presumir níveis genéricos 2/4/6 para toda trait.
        const auto separator = resolved_path.find_last_of("/\\");
        const auto directory = separator == std::string::npos
            ? std::string{}
            : resolved_path.substr(0, separator + 1);
        std::ifstream traits_file(directory + "traits.json");
        if (traits_file) {
            try {
                nlohmann::json traits_json;
                traits_file >> traits_json;
                const auto& traits = traits_json.is_object() && traits_json.contains("traits")
                    ? traits_json.at("traits") : traits_json;
                if (traits.is_array()) {
                    for (const auto& trait : traits) {
                        if (!trait.is_object() || !trait.contains("name") ||
                            !trait.contains("effects") || !trait.at("effects").is_array())
                            continue;
                        std::vector<int> milestones;
                        for (const auto& effect : trait.at("effects")) {
                            if (effect.is_object() && effect.contains("minUnits") &&
                                effect.at("minUnits").is_number_integer())
                                milestones.push_back(effect.at("minUnits").get<int>());
                        }
                        std::sort(milestones.begin(), milestones.end());
                        milestones.erase(std::unique(milestones.begin(), milestones.end()),
                                          milestones.end());
                        if (!milestones.empty())
                            trait_milestones[trait.at("name").get<std::string>()] =
                                std::move(milestones);
                    }
                }
            } catch (const std::exception&) {
                trait_milestones.clear();
            }
        }

        pool = std::make_unique<UnitPool>(*catalog);

        unit_factory = std::make_unique<UnitInstanceFactory>(
            *catalog,
            seed
        );

        initialize_players();
    }

    void ensure_open() const {
        if (closed) {
            throw std::runtime_error(
                "TFTEngine ja foi fechado."
            );
        }
    }

    // ========================================================
    // ESTADO DE DECISÃO E SNAPSHOTS
    // ========================================================

    decision::PlayerState build_decision_state(
        std::size_t player_index
    ) const {
        decision::PlayerState state;

        state.player_id =
            static_cast<std::int64_t>(player_index);

        state.is_alive = player_envs[player_index].info.alive;

        const auto& economy = player_envs[player_index].economy;

        state.economy.gold = economy.gold;
        state.economy.level = economy.level;
        state.economy.max_level = EconomyEngine::MAX_LEVEL;
        state.economy.current_xp = economy.xp;
        state.economy.xp_to_next_level =
            economy_engine.get_xp_to_next(economy);
        state.economy.reroll_cost =
            EconomyEngine::REROLL_COST;
        state.economy.xp_purchase_cost =
            EconomyEngine::BUY_XP_COST;

        const auto snapshot = [this](
            const std::optional<UnitInstance>& instance
        ) -> std::optional<decision::UnitSnapshot> {
            if (!instance.has_value()) {
                return std::nullopt;
            }

            decision::UnitSnapshot unit;

            unit.identity.uuid = instance->uuid;
            unit.identity.id = instance->champion_internal_id;
            unit.identity.textual_id = instance->champion_id;

            unit.identity.star = static_cast<std::uint8_t>(
                std::clamp(instance->star, 1, 3)
            );

            const auto* definition =
                catalog->find_by_id(
                    instance->champion_internal_id
                );

            unit.cost = static_cast<std::uint8_t>(
                definition
                    ? std::clamp(definition->cost, 1, 5)
                    : 1
            );

            unit.available = true;

            return unit;
        };

        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            state.board[slot] =
                snapshot(player_envs[player_index].board[slot]);
        }

        for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
            state.bench[slot] =
                snapshot(player_envs[player_index].bench[slot]);
        }

        for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
            const auto* offer =
                player_envs[player_index].shop->get_unit(
                    static_cast<std::int32_t>(slot)
                );

            if (offer) {
                state.shop[slot] = snapshot(
                    std::optional<UnitInstance>{*offer}
                );
            }
        }

        return state;
    }

    void register_position_state(std::size_t player_index) {
        const auto state =
            build_decision_state(player_index);

        const auto signature =
            player_envs[player_index].anti_loop
                .make_board_signature(state);

        (void)player_envs[player_index].anti_loop
            .register_state(signature);
    }

    // ========================================================
    // MÁSCARAS DE AÇÃO
    // ========================================================

    void refresh_masks(std::size_t player_index) {
        const auto state =
            build_decision_state(player_index);

        const auto batch =
            action_mask_engine.generate_masks(
                state,
                player_envs[player_index].anti_loop,
                false
            );

        // Contabiliza uma vez por geração de máscara; as consultas individuais
        // do anti-loop permanecem sem efeitos colaterais.
        player_envs[player_index].anti_loop.record_mask_diagnostics(
            batch.diagnostics
        );

        auto& current = player_envs[player_index].action_masks;
        current = PlayerActionMasks{};

        current.type_mask = batch.type_mask;
        current.shop_mask = batch.shop_mask;
        current.bench_source_mask =
            batch.bench_source_mask;
        current.board_target_mask =
            batch.board_target_mask;
        current.board_source_mask =
            batch.board_source_mask;
        current.bench_move_source_mask =
            batch.bench_move_source_mask;

        for (std::size_t source = 0;
             source < kBoardSlots;
             ++source) {
            for (std::size_t target = 0;
                 target < kBoardSlots;
                 ++target) {
                current.board_move_target_masks[
                    source * kBoardSlots + target
                ] = batch.board_move_target_masks[source][target];
            }
        }

        for (std::size_t source = 0;
             source < kBenchSlots;
             ++source) {
            for (std::size_t target = 0;
                 target < kBoardSlots;
                 ++target) {
                current.bench_to_board_target_masks[
                    source * kBoardSlots + target
                ] = batch.bench_to_board_target_masks[source][target];
            }
        }
    }

    // ========================================================
    // INICIALIZAÇÃO
    // ========================================================

    void initialize_players() {
        alive_players =
            static_cast<std::int32_t>(kPlayersPerLobby);

        // RewardManager.py starts with previous_level = 1.
        // Initialize this on first construction as well as on reset.
        for (auto& player_env : player_envs) player_env.previous_reward_level = 1;
        round_actions.fill(0);
        round_finished.fill(false);
        previous_matchups.clear();
        matchmaking_rng.seed(seed + episode_id);

        // Python creates one random cost-1 starter on each player's bench
        // before rolling that player's shop. Keep the same state transition
        // and pool accounting in the native lobby.
        std::mt19937_64 starting_rng(seed + episode_id);
        for (std::size_t i = 0;
             i < kPlayersPerLobby;
             ++i) {
            PlayerInfo player{};

            player.player_id =
                static_cast<std::int32_t>(i);

            player.hp = 100.0f;

            economy_engine.reset(player_envs[i].economy);

            player.gold = player_envs[i].economy.gold;
            player.level = player_envs[i].economy.level;
            player.xp = player_envs[i].economy.xp;

            player.alive = true;
            player.eliminated = false;

            player.wins = 0;
            player.losses = 0;

            player.placement = std::nullopt;
            player.opponent_id = std::nullopt;
            player.damage_taken = 0.0f;

            player_envs[i].info = player;

            player_envs[i].bench.fill(std::nullopt);
            player_envs[i].board.fill(std::nullopt);
            player_envs[i].board_move_age.fill(kActionMemoryHorizon);
            player_envs[i].actions_taken_this_round = 0;

            // Impede que o histórico de uma partida anterior
            // interfira no novo episódio.
            // Limpa o histórico da partida, preservando as métricas acumuladas.
            player_envs[i].anti_loop.reset();

            const auto starting_champion = pool->draw_by_cost(1, starting_rng);
            if (!starting_champion.has_value()) {
                throw std::runtime_error(
                    "UnitPool sem campeao de custo 1 para a unidade inicial.");
            }
            player_envs[i].bench[0] = unit_factory->create(*starting_champion);

            player_envs[i].shop = std::make_unique<ShopEngine>(
                *pool,
                *unit_factory,
                seed + static_cast<std::uint64_t>(i)
                    + episode_id
            );

            player_envs[i].shop->roll(player.level);

            player_envs[i].action_masks = make_default_masks();

            player_envs[i].strategy.clear();
            player_envs[i].strategy.push_back(StrategyInfo{});

            player_envs[i].anti_loop_metrics = AntiLoopMetrics{};

            register_position_state(i);
            refresh_masks(i);
        }
    }

    // ========================================================
    // OBSERVAÇÕES
    // ========================================================

    std::size_t observation_dim() const noexcept {
        return kCoreObservationDim + kBoardObservationDim +
            kBenchObservationDim + kShopObservationDim +
            kExtraObservationDim + kSynergyObservationDim +
            kPositioningObservationDim + observation_trait_names.size() +
            kCapacityObservationDim +
            2 * observation_trait_names.size() + kCompositionUnitSlots +
            kActionMemoryObservationDim +
            observation_trait_names.size() + 2 +
            kStrategicCandidateObservationDim;
    }

    std::vector<float> build_observations() const {
        const auto dim = observation_dim();
        std::vector<float> observations(kPlayersPerLobby * dim, 0.0f);

        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            float* out = observations.data() + i * dim;
            const auto& player = player_envs[i].info;

            // TFTLobby.get_observations() returns an all-zero vector for
            // eliminated players. Preserve that public PPO contract exactly.
            if (!player.alive) {
                continue;
            }

            const auto& economy = player_envs[i].economy;
            const auto& strategy = player_envs[i].strategy.empty()
                ? StrategyInfo{} : player_envs[i].strategy.back();

            std::array<int, kBoardSlots> board_roles{};
            std::array<bool, kBoardSlots> board_occupied{};
            std::array<bool, kBenchSlots> bench_occupied{};
            std::vector<std::pair<std::string, int>> trait_counts;
            std::unordered_map<std::string, std::size_t> trait_count_index;
            int board_count = 0, bench_count = 0, frontline = 0, backline = 0;
            std::set<int> unique_roles;

            const auto count_traits = [&](const UnitInstance& unit) {
                const auto* def = catalog->find_by_id(unit.champion_internal_id);
                if (!def) return;
                for (const auto& trait : def->traits) {
                    auto it = trait_count_index.find(trait);
                    if (it == trait_count_index.end()) {
                        trait_count_index[trait] = trait_counts.size();
                        trait_counts.emplace_back(trait, 0);
                        it = trait_count_index.find(trait);
                    }
                    ++trait_counts[it->second].second;
                }
            };

            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                if (!player_envs[i].board[slot]) continue;
                ++board_count;
                board_occupied[slot] = true;
                const auto& unit = *player_envs[i].board[slot];
                const auto* def = catalog->find_by_id(unit.champion_internal_id);
                if (!def) continue;
                const int role = std::clamp(def->combat_profile.role, 0, 4);
                board_roles[slot] = role;
                unique_roles.insert(role);
                const int row = static_cast<int>(slot / 7);
                if (row <= 1) ++frontline;
                if (row >= 2) ++backline;
                count_traits(unit);
            }
            for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
                if (!player_envs[i].bench[slot]) continue;
                ++bench_count;
                bench_occupied[slot] = true;
                count_traits(*player_envs[i].bench[slot]);
            }

            // 1) CORE (same order/scales as MiniTFTEnv._get_state()).
            std::size_t offset = 0;
            out[offset++] = player.hp / 100.0f;
            out[offset++] = static_cast<float>(economy.gold) / 50.0f;
            out[offset++] = static_cast<float>(economy.level) / 9.0f;
            out[offset++] = static_cast<float>(economy.xp) /
                static_cast<float>(std::max(1, economy_engine.get_xp_to_next(economy)));
            out[offset++] = static_cast<float>(economy.win_streak) / 10.0f;
            out[offset++] = static_cast<float>(economy.loss_streak) / 10.0f;
            const float current_round = static_cast<float>(round + 1);
            out[offset++] = current_round / (current_round + 10.0f);
            out[offset++] = static_cast<float>(board_count) /
                static_cast<float>(std::max(1, economy.level));
            out[offset++] = static_cast<float>(bench_count) / static_cast<float>(kBenchSlots);
            out[offset++] = 1.0f; // shop vector always contains five slots in Python.
            for (int s = 0; s < 7; ++s)
                out[offset++] = strategy.strategy == s ? 1.0f : 0.0f;
            // Python's 22-wide core reserves five trailing zero features.
            offset = kCoreObservationDim;

            // 2) BOARD: occupied, cost, stars, role, strength per slot.
            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                if (!player_envs[i].board[slot]) { offset += 5; continue; }
                const auto& unit = *player_envs[i].board[slot];
                const auto* def = catalog->find_by_id(unit.champion_internal_id);
                if (!def) { offset += 5; continue; }
                out[offset++] = 1.0f;
                out[offset++] = static_cast<float>(def->cost) / 5.0f;
                out[offset++] = static_cast<float>(unit.star) / 3.0f;
                out[offset++] = role_state_value(def->combat_profile.role);
                out[offset++] = unit_strength(*def, unit);
            }

            // 3) BENCH.
            for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
                if (!player_envs[i].bench[slot]) { offset += 5; continue; }
                const auto& unit = *player_envs[i].bench[slot];
                const auto* def = catalog->find_by_id(unit.champion_internal_id);
                if (!def) { offset += 5; continue; }
                out[offset++] = 1.0f;
                out[offset++] = static_cast<float>(def->cost) / 5.0f;
                out[offset++] = static_cast<float>(unit.star) / 3.0f;
                out[offset++] = role_state_value(def->combat_profile.role);
                out[offset++] = unit_strength(*def, unit);
            }

            // 4) SHOP.
            for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
                const auto* unit = player_envs[i].shop ? player_envs[i].shop->get_unit(static_cast<std::int32_t>(slot)) : nullptr;
                if (!unit) { offset += 5; continue; }
                const auto* def = catalog->find_by_id(unit->champion_internal_id);
                if (!def) { offset += 5; continue; }
                out[offset++] = 1.0f;
                out[offset++] = static_cast<float>(def->cost) / 5.0f;
                out[offset++] = 1.0f;
                out[offset++] = role_state_value(def->combat_profile.role);
                out[offset++] = 0.0f; // Python shop strength slot is intentionally zero.
            }

            // 5) EXTRA.
            out[offset++] = static_cast<float>(board_count) / static_cast<float>(kBoardSlots);
            out[offset++] = static_cast<float>(bench_count) / static_cast<float>(kBenchSlots);
            out[offset++] = static_cast<float>(economy.gold) / 50.0f;
            out[offset++] = static_cast<float>(economy.level) / 9.0f;
            out[offset++] = player.hp / 100.0f;

            // 6) SYNERGY: first five active trait counts in insertion order.
            for (std::size_t n = 0; n < kSynergyObservationDim; ++n) {
                const float value = n < trait_counts.size()
                    ? static_cast<float>(trait_counts[n].second) / 5.0f : 0.0f;
                out[offset++] = std::min(1.0f, value);
            }

            // 7) POSITIONING: share the native implementation with the public parity API.
            std::vector<int> positioning_roles(kBoardSlots, -1);
            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                if (!player_envs[i].board[slot]) continue;
                const auto* def = catalog->find_by_id(
                    player_envs[i].board[slot]->champion_internal_id);
                if (def) positioning_roles[slot] = std::clamp(def->combat_profile.role, 0, 4);
            }
            const double positioning_score =
                PositioningEngine::evaluate_board_positioning(positioning_roles);
            out[offset++] = static_cast<float>(positioning_score);
            out[offset++] = board_count ? static_cast<float>(frontline) / board_count : 0.0f;
            out[offset++] = board_count ? static_cast<float>(backline) / board_count : 0.0f;
            out[offset++] = std::min(1.0f, static_cast<float>(unique_roles.size()) / 5.0f);

            // 8) TRAITS: fixed catalog order shared across all players.
            std::unordered_map<std::string, int> all_trait_counts;
            for (const auto& entry : trait_counts) all_trait_counts[entry.first] = entry.second;
            for (const auto& trait : observation_trait_names) {
                const auto it = all_trait_counts.find(trait);
                const float value = it == all_trait_counts.end()
                    ? 0.0f : static_cast<float>(it->second) / 5.0f;
                out[offset++] = std::min(1.0f, value);
            }

            // 9) CAPACITY.
            out[offset++] = static_cast<float>(std::max(0, economy.level - board_count)) / 9.0f;
            out[offset++] = static_cast<float>(kBenchSlots - bench_count) / 9.0f;

            // 10) COMPOSITION DIRECTION: explicit, stable one-hot over the
            // catalog trait order. This is derived from board + bench state.
            for (const auto& trait : observation_trait_names) {
                out[offset++] =
                    !strategy.composition_direction.empty() &&
                    strategy.composition_direction == trait ? 1.0f : 0.0f;
            }

            // 11) CORE TRAITS: explicit flags, aligned with the same trait order.
            for (const auto& trait : observation_trait_names) {
                out[offset++] =
                    std::find(strategy.core_traits.begin(),
                              strategy.core_traits.end(), trait) !=
                    strategy.core_traits.end() ? 1.0f : 0.0f;
            }

            // 12) COMPOSITION FIT: normalized per-unit compatibility score.
            // The score is exposed for all candidates, including shop units,
            // so PPO can compare a purchase against the current comp direction.
            const auto append_unit_fit = [&](const UnitInstance* unit) {
                if (!unit) {
                    out[offset++] = 0.0f;
                    return;
                }
                const auto* def = catalog->find_by_id(unit->champion_internal_id);
                if (!def) {
                    out[offset++] = 0.0f;
                    return;
                }
                const double score =
                    unit_composition_score(strategy, *def, unit->star);
                out[offset++] = static_cast<float>(
                    std::clamp(score / 22.5, 0.0, 1.0));
            };
            for (const auto& unit : player_envs[i].board)
                append_unit_fit(unit ? &*unit : nullptr);
            for (const auto& unit : player_envs[i].bench)
                append_unit_fit(unit ? &*unit : nullptr);
            for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
                const auto* unit = player_envs[i].shop
                    ? player_envs[i].shop->get_unit(static_cast<std::int32_t>(slot))
                    : nullptr;
                append_unit_fit(unit);
            }

            // 13) TEMPORAL ACTION MEMORY. These features are inserted before the
            // candidate tail so policy.py can continue reading candidate features
            // from the end of the observation without changing its offsets.
            out[offset++] = static_cast<float>(kActionMemoryHorizon -
                std::min(player_envs[i].actions_taken_this_round, kActionMemoryHorizon)) /
                static_cast<float>(kActionMemoryHorizon);
            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                const auto age = player_envs[i].board[slot]
                    ? std::min(player_envs[i].board_move_age[slot], kActionMemoryHorizon)
                    : kActionMemoryHorizon;
                out[offset++] = static_cast<float>(age) /
                    static_cast<float>(kActionMemoryHorizon);
            }

            // 14) COMPOSITION CONTROL FEATURES. Keep these immediately before the
            // candidate tail: policy.py extracts candidate records from the end,
            // and checkpoint migration inserts new global features at this boundary.
            // Focus weights use the stable catalog trait order shared by direction/core
            // flags and are normalized from [0, 5] to [0, 1].
            for (const auto& trait : observation_trait_names) {
                double weight = 0.0;
                for (const auto& [focus_trait, focus_weight] :
                     strategy.composition_focus_weights) {
                    if (focus_trait == trait) {
                        weight = focus_weight;
                        break;
                    }
                }
                out[offset++] = static_cast<float>(
                    std::clamp(weight / 5.0, 0.0, 1.0));
            }
            out[offset++] = strategy.composition_locked ? 1.0f : 0.0f;
            // Strategy strength is bounded to [0, 10] by its scoring formula.
            out[offset++] = static_cast<float>(
                std::clamp(strategy.composition_strength / 10.0, 0.0, 1.0));

            // 15) PER-CANDIDATE DECISION FEATURES. These are explicit slot-local
            // features so the policy can compare offers/sale candidates rather than
            // infer which global features correspond to each output index.
            const auto count_same_champion = [&](const UnitInstance& candidate) {
                int copies = 0;
                for (const auto& unit : player_envs[i].board) {
                    if (unit && unit->champion_internal_id == candidate.champion_internal_id)
                        copies += unit->star == 1 ? 1 : (unit->star == 2 ? 3 : 9);
                }
                for (const auto& unit : player_envs[i].bench) {
                    if (unit && unit->champion_internal_id == candidate.champion_internal_id)
                        copies += unit->star == 1 ? 1 : (unit->star == 2 ? 3 : 9);
                }
                return copies;
            };
            const auto append_candidate_features = [&](const UnitInstance* unit, bool sale_candidate) {
                if (!unit) {
                    for (std::size_t n = 0; n < kCandidateFeatureDim; ++n)
                        out[offset++] = 0.0f;
                    return;
                }
                const auto* def = catalog->find_by_id(unit->champion_internal_id);
                if (!def) {
                    for (std::size_t n = 0; n < kCandidateFeatureDim; ++n)
                        out[offset++] = 0.0f;
                    return;
                }
                const double fit = unit_composition_score(strategy, *def, unit->star);
                const bool core = std::find(strategy.core_unit_ids.begin(),
                    strategy.core_unit_ids.end(), def->internal_id) != strategy.core_unit_ids.end();
                const int copies = count_same_champion(*unit);
                int trait_overlap = 0;
                for (const auto& trait : def->traits) {
                    bool shared = false;
                    for (const auto& existing : player_envs[i].board) {
                        if (!existing || &*existing == unit) continue;
                        const auto* existing_def = catalog->find_by_id(existing->champion_internal_id);
                        if (existing_def && std::find(existing_def->traits.begin(),
                            existing_def->traits.end(), trait) != existing_def->traits.end()) {
                            shared = true;
                            break;
                        }
                    }
                    if (!shared) {
                        for (const auto& existing : player_envs[i].bench) {
                            if (!existing || &*existing == unit) continue;
                            const auto* existing_def = catalog->find_by_id(existing->champion_internal_id);
                            if (existing_def && std::find(existing_def->traits.begin(),
                                existing_def->traits.end(), trait) != existing_def->traits.end()) {
                                shared = true;
                                break;
                            }
                        }
                    }
                    if (shared) ++trait_overlap;
                }
                out[offset++] = static_cast<float>(std::clamp(fit / 22.5, 0.0, 1.0));
                out[offset++] = static_cast<float>(def->cost) / 5.0f;
                out[offset++] = static_cast<float>(unit->star) / 3.0f;
                out[offset++] = role_state_value(def->combat_profile.role);
                out[offset++] = core ? 1.0f : 0.0f;
                // Number of owned copies (including star-equivalent copies), normalized.
                out[offset++] = static_cast<float>(std::min(copies, 9)) / 9.0f;
                out[offset++] = static_cast<float>(std::min(trait_overlap, 5)) / 5.0f;
                if (sale_candidate) {
                    out[offset++] = static_cast<float>(
                        EconomyEngine::get_sell_value(def->cost, unit->star)) / 50.0f;
                } else {
                    out[offset++] = economy.gold >= def->cost ? 1.0f : 0.0f;
                }
            };
            for (const auto& unit : player_envs[i].bench)
                append_candidate_features(unit ? &*unit : nullptr, true);
            for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
                const auto* unit = player_envs[i].shop
                    ? player_envs[i].shop->get_unit(static_cast<std::int32_t>(slot))
                    : nullptr;
                append_candidate_features(unit, false);
            }
        }
        return observations;
    }

    // ========================================================
    // VALIDAÇÃO DE AÇÕES
    // ========================================================

    void validate_action(const PlayerAction& action) const {
        for (std::size_t i = 0;
             i < kActionComponents;
             ++i) {
            const std::int32_t value = action.values[i];

            if (value < 0 ||
                static_cast<std::size_t>(value) >=
                    kActionDims[i]) {
                throw std::invalid_argument(
                    "Componente de acao fora dos limites. "
                    "Dimensao: " + std::to_string(i) +
                    ", valor: " + std::to_string(value)
                );
            }
        }
    }

    // Preflight sem efeitos colaterais: valida a ação selecionada contra
    // o estado atual antes que qualquer jogador seja processado.
    void validate_action_against_masks(
        std::size_t player_index,
        const PlayerAction& action
    ) const {
        const auto& values = action.values;
        const auto type = static_cast<std::size_t>(values[0]);
        const auto& player_masks = player_envs[player_index].action_masks;

        // A tentativa de implantar além do nível deve ser rejeitada com
        // penalidade mesmo quando MOVE_BENCH segue habilitado por existir
        // outra substituição válida no mesmo estado.
        if (type == 3) {
            const auto state = build_decision_state(player_index);
            const auto source = static_cast<std::size_t>(values[2]);
            const auto target = static_cast<std::size_t>(values[3]);
            const auto occupied = static_cast<std::size_t>(
                std::count_if(
                    state.board.begin(),
                    state.board.end(),
                    [](const auto& unit) { return unit.has_value(); }
                )
            );
            if (
                source < state.bench.size()
                && target < state.board.size()
                && state.bench[source].has_value()
                && !state.board[target].has_value()
                && occupied >= static_cast<std::size_t>(state.economy.level)
            ) {
                return;
            }
        }

        // Se o movimento e estruturalmente valido, mas foi bloqueado
        // pelo AntiLoop, deixe-o chegar ao fluxo de execucao mesmo quando
        // nao restam movimentos validos desse tipo. A execucao registra a
        // tentativa e o motivo do bloqueio sem alterar o tabuleiro.
        // Sem este desvio, o type_mask desabilitado faz o preflight lancar
        // antes de record_execution_attempt()/record_execution_block().
        if (type == 3 || type == 4) {
            const auto state = build_decision_state(player_index);
            std::optional<std::string> block_reason;

            if (type == 3) {
                const auto source = values[2];
                const auto target = values[3];
                const auto validation =
                    decision::MoveValidator::validate_bench_to_board_move(
                        state.board,
                        state.bench,
                        source,
                        target
                    );

                if (validation.is_valid()) {
                    const auto source_index =
                        static_cast<std::size_t>(source);
                    const auto unit_identity =
                        std::optional<decision::UnitIdentity>{
                            state.bench[source_index]->identity
                        };
                    block_reason =
                        player_envs[player_index].anti_loop.get_block_reason(
                            "bench_to_board",
                            source,
                            target,
                            unit_identity
                        );
                }
            } else {
                const auto source = values[4];
                const auto target = values[5];
                const auto validation =
                    decision::MoveValidator::validate_board_move(
                        state.board,
                        source,
                        target
                    );

                if (validation.is_valid() &&
                    validation.move_type.has_value()) {
                    const auto source_index =
                        static_cast<std::size_t>(source);
                    const auto unit_identity =
                        std::optional<decision::UnitIdentity>{
                            state.board[source_index]->identity
                        };
                    const std::string move_type =
                        *validation.move_type ==
                            decision::MoveType::BOARD_SWAP
                            ? "board_swap"
                            : "board_move";
                    block_reason =
                        player_envs[player_index].anti_loop.get_block_reason(
                            move_type,
                            source,
                            target,
                            unit_identity
                        );
                }
            }

            if (block_reason.has_value()) {
                return;
            }
        }

        if (player_masks.type_mask[type] != 1) {
            throw std::invalid_argument(
                "Acao indisponivel para o estado atual do jogador "
                + std::to_string(player_index)
                + ". Tipo: " + std::to_string(type)
            );
        }

        if (type == 0) {
            const auto slot = static_cast<std::size_t>(values[1]);
            if (player_masks.shop_mask[slot] != 1) {
                throw std::invalid_argument(
                    "Compra invalida: oferta indisponivel, ouro insuficiente "
                    "ou banco cheio."
                );
            }
            return;
        }

        if (type == 5) {
            const auto slot = static_cast<std::size_t>(values[2]);
            if (player_masks.bench_source_mask[slot] != 1) {
                throw std::invalid_argument(
                    "Venda invalida: o slot selecionado do banco esta vazio."
                );
            }
            return;
        }

        // Movimentos estruturalmente válidos que o AntiLoop bloqueia
        // ainda devem chegar à engine para contabilizar a tentativa.
        if (type == 3 || type == 4) {
            const auto state = build_decision_state(player_index);
            bool valid_move = false;

            if (type == 3) {
                valid_move =
                    decision::MoveValidator::validate_bench_to_board_move(
                        state.board,
                        state.bench,
                        values[2],
                        values[3]
                    ).is_valid();
            } else {
                valid_move =
                    decision::MoveValidator::validate_board_move(
                        state.board,
                        values[4],
                        values[5]
                    ).is_valid();
            }

            if (!valid_move) {
                throw std::invalid_argument(
                    "Movimento invalido: origem vazia, destino ocupado "
                    "ou posicoes incompatíveis."
                );
            }
        }
    }

    // ========================================================
    // SINCRONIZAÇÃO DA ECONOMIA
    // ========================================================

    double board_power(std::size_t player_index) const {
        // Mesma estimativa de MiniTFTEnv._update_strategy():
        // sum(cost * star * 2.0) para as unidades no tabuleiro.
        double power = 0.0;
        for (const auto& unit : player_envs[player_index].board) {
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            power += static_cast<double>(def->cost)
                * static_cast<double>(unit->star) * 2.0;
        }
        return power;
    }

    double synergy_score(std::size_t player_index) const {
        std::vector<strategy::ChampionTraitEntry> entries;
        entries.reserve(kBoardSlots);
        for (const auto& unit : player_envs[player_index].board) {
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            entries.emplace_back(unit->champion_internal_id, def->traits);
        }
        // Keep the same unique-by-unit["id"] semantics as Python.
        const auto counts = strategy::count_unique_champion_traits(entries);
        double score = 0.0;
        for (const auto& [trait, count] : counts) {
            const auto milestones = trait_milestones.find(trait);
            if (milestones == trait_milestones.end()) continue;
            int reached = 0;
            for (const int milestone : milestones->second)
                if (count >= milestone) ++reached;
            if (reached > 0) score += static_cast<double>(reached);
            else if (std::any_of(milestones->second.begin(), milestones->second.end(),
                                 [count](int milestone) { return count == milestone - 1; }))
                score += 0.5; // progresso parcial, faltando uma unidade
        }
        return score;
    }

    double positioning_score(std::size_t player_index) const {
        const auto role_at = [&](std::size_t slot) {
            if (!player_envs[player_index].board[slot]) return UnitRole::FIGHTER;
            const auto* def = catalog->find_by_id(
                player_envs[player_index].board[slot]->champion_internal_id);
            if (!def) return UnitRole::FIGHTER;
            return static_cast<UnitRole>(std::clamp(def->combat_profile.role, 0, 4));
        };
        const auto center_score = [](int col) {
            constexpr double center = 3.0;
            return std::max(0.0, 1.0 - std::abs(col - center) / 3.0);
        };
        const auto edge_score = [](int col) {
            const int distance = std::min(col, 6 - col);
            return std::max(0.0, 1.0 - distance / 3.0);
        };
        const auto frontline_score = [](int row) { return (3.0 - row) / 3.0; };
        const auto backline_score = [](int row) { return row / 3.0; };
        const auto assassin_score = [](int row) {
            return std::max(0.0, 1.0 - std::abs(row - 1.65) / 3.0);
        };

        double score = 0.0;
        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            if (!player_envs[player_index].board[slot]) continue;
            const auto* def = catalog->find_by_id(
                player_envs[player_index].board[slot]->champion_internal_id);
            if (!def) continue;
            const int row = static_cast<int>(slot / 7);
            const int col = static_cast<int>(slot % 7);
            const auto role = role_at(slot);

            // Réplica da pontuação de evaluate_unit_placement do Python.
            if (role == UnitRole::TANK) {
                score += frontline_score(row) * 4.0 + center_score(col) * 1.5;
            } else if (role == UnitRole::FIGHTER) {
                score += frontline_score(row) * 2.5 + center_score(col);
            } else if (role == UnitRole::ASSASSIN) {
                score += assassin_score(row) * 3.0 + edge_score(col);
            } else if (role == UnitRole::SUPPORT) {
                score += backline_score(row) * 3.0 + center_score(col) * 1.5;
            } else if (role == UnitRole::CARRY) {
                score += backline_score(row) * 4.0 + center_score(col) * 2.0;
                if (col == 0 || col == 6) score -= 0.5;
            }

            int occupied_neighbors = 0;
            int tank_neighbors = 0;
            for (int dr = -1; dr <= 1; ++dr) {
                for (int dc = -1; dc <= 1; ++dc) {
                    if (dr == 0 && dc == 0) continue;
                    const int nr = row + dr, nc = col + dc;
                    if (nr < 0 || nr >= 4 || nc < 0 || nc >= 7) continue;
                    const auto neighbor = static_cast<std::size_t>(nr * 7 + nc);
                    if (!player_envs[player_index].board[neighbor]) continue;
                    ++occupied_neighbors;
                    if (role_at(neighbor) == UnitRole::TANK) ++tank_neighbors;
                }
            }
            // Réplica de evaluate_protection do Python.
            if (role == UnitRole::CARRY)
                score += occupied_neighbors * 0.8 + tank_neighbors * 1.5;
            else if (role == UnitRole::SUPPORT)
                score += occupied_neighbors * 0.6 + tank_neighbors;
            else if (role == UnitRole::TANK)
                score += occupied_neighbors * 0.2;
        }
        return score;
    }

    double combat_reward(bool won, int damage_dealt, int damage_taken,
                         int enemy_alive, int own_alive) const {
        return reward_model::combat(
            won, damage_dealt, damage_taken, enemy_alive, own_alive);
    }

    void update_strategy(std::size_t i) {
        auto& list = player_envs[i].strategy;
        StrategyInfo info = list.empty() ? StrategyInfo{} : list.back();
        const auto& player = player_envs[i].info;
        const auto& economy = player_envs[i].economy;
        const double power = board_power(i);
        double bench_strength = 0.0;
        for (const auto& unit : player_envs[i].bench) {
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (def) bench_strength += static_cast<double>(def->cost) * unit->star;
        }
        std::int32_t chosen = 0;
        float confidence = 0.50f;
        std::string reason = "Estado econômico neutro";

        // Mesma ordem de prioridade de StrategyManager.decide_strategy().
        if (player.hp <= 15.0f) {
            chosen = 4; confidence = 0.95f; reason = "HP crítico";
        } else if (player.hp <= 30.0f) {
            chosen = 1; confidence = 0.85f; reason = "HP baixo";
        } else if (economy.loss_streak >= 5) {
            chosen = 6; confidence = 0.80f; reason = "Loss streak prolongada";
        } else if (economy.win_streak >= 4 && player.hp >= 60.0f) {
            chosen = 5; confidence = 0.80f; reason = "Win streak + HP saudável";
        } else if (economy.gold >= 40 && economy.level <= 7 && player.hp >= 50.0f) {
            chosen = 0; confidence = 0.85f; reason = "Economia forte";
        } else if (economy.level >= 7 && economy.gold >= 30 && player.hp >= 50.0f) {
            chosen = 2; confidence = 0.75f; reason = "Economia suficiente para acelerar nível";
        } else if (economy.level <= 6 && economy.gold >= 30 && power >= 40.0) {
            chosen = 3; confidence = 0.70f; reason = "Board estável + economia para rolagem";
        } else if (power < 25.0) {
            chosen = 1; confidence = 0.70f; reason = "Board abaixo do esperado";
        }

        const bool changed = chosen != info.strategy;
        if (changed) {
            info.previous_strategy = info.strategy;
            info.strategy_age = 0;
            if (chosen == 1)
                info.comp_stabilize_start_round = static_cast<std::int32_t>(round + 1);
        } else {
            ++info.strategy_age;
        }
        static const std::array<const char*, 7> names{
            "ECON", "STABILIZE", "FAST8", "SLOWROLL",
            "ALL_IN", "WINSTREAK", "LOSS_STREAK"
        };
        info.strategy = chosen;
        info.strategy_name = names[static_cast<std::size_t>(chosen)];
        info.confidence = confidence;
        info.reason = reason;
        info.changed = changed;
        info.board_power = power;
        info.bench_strength = bench_strength;

        // Equivalente ao CompositionManager.update(board, bench).
        std::unordered_map<std::string, int> trait_counts;
        std::unordered_map<std::int32_t, int> copies_by_unit;
        std::unordered_map<std::int32_t, double> focus_scores;
        std::unordered_map<std::int32_t, std::string> unit_names;
        // Preserve Python dict/Counter insertion order for tie-breaking.
        std::vector<std::string> trait_order;
        std::vector<std::int32_t> unit_order;
        const auto add_owned_unit = [&](const UnitInstance& unit) {
            const auto* def = catalog->find_by_id(unit.champion_internal_id);
            if (!def) return;
            const std::int32_t id = def->internal_id;
            if (copies_by_unit.find(id) == copies_by_unit.end()) unit_order.push_back(id);
            unit_names[id] = def->api_name;
            copies_by_unit[id] += star_copies(unit.star);
            for (const auto& trait : def->traits) {
                if (trait_counts.find(trait) == trait_counts.end())
                    trait_order.push_back(trait);
                ++trait_counts[trait];
            }
        };
        for (const auto& unit : player_envs[i].board) if (unit) add_owned_unit(*unit);
        for (const auto& unit : player_envs[i].bench) if (unit) add_owned_unit(*unit);

        const auto score_owned_unit = [&](const UnitInstance& unit) {
            const auto* def = catalog->find_by_id(unit.champion_internal_id);
            if (!def) return;
            const std::int32_t id = def->internal_id;
            const double score = (unit.star - 1) * 3.0 + def->cost * 1.5
                + def->traits.size() + std::min(copies_by_unit[id], 9) * 0.5;
            focus_scores[id] = std::max(focus_scores[id], score);
        };
        for (const auto& unit : player_envs[i].board) if (unit) score_owned_unit(*unit);
        for (const auto& unit : player_envs[i].bench) if (unit) score_owned_unit(*unit);

        info.composition_focus.clear();
        info.composition_focus_id = -1;
        // Keep composition_direction persistent while composition_locked is true.
        info.core_units.clear();
        info.core_unit_ids.clear();
        info.core_traits.clear();
        info.active_traits.clear();
        info.unit_counts.clear();
        info.unit_counts_by_id.clear();

        for (const auto& trait : trait_order) {
            const auto count = trait_counts.at(trait);
            info.active_traits.emplace_back(trait, count);
        }

        // Port of Python _update_comp_direction(), _update_comp_focus(), and
        // _should_lock_comp(). Python's _get_offensive_factor() helper is not
        // part of this native engine, so champion role is used as a proxy.
        const auto offensive_factor = [](const ChampionDefinition& def) {
            switch (def.combat_profile.role) {
                case 1: // carry
                case 4: // assassin
                    return 1.20;
                case 3: // fighter
                    return 1.05;
                case 0: // tank
                case 2: // support
                    return 0.90;
                default:
                    return 1.0;
            }
        };
        const auto current_stage = stage_for_round(round + 1);
        const auto current_round = static_cast<std::int32_t>(round + 1);
        const auto count_occupied = [](const auto& slots) {
            return static_cast<std::size_t>(std::count_if(
                slots.begin(), slots.end(),
                [](const auto& unit) { return unit.has_value(); }));
        };
        const auto unit_count = count_occupied(player_envs[i].board) +
            count_occupied(player_envs[i].bench);

        std::map<std::string, double> focus;
        for (const auto& [trait, value] : info.composition_focus_weights)
            focus[trait] = value;

        std::unordered_map<std::string, int> board_trait_counts;
        for (const auto& unit : player_envs[i].board) {
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            for (const auto& trait : def->traits) ++board_trait_counts[trait];
        }
        const auto trait_level = [&](const std::string& trait, int count) {
            const auto found = trait_milestones.find(trait);
            if (found == trait_milestones.end()) return count >= 2 ? 1 : 0;
            int level = 0;
            for (const int milestone : found->second) {
                if (count >= milestone) ++level;
            }
            return level;
        };

        std::unordered_map<std::string, double> trait_score;
        const auto score_composition_unit = [&](const UnitInstance& unit) {
            const auto* def = catalog->find_by_id(unit.champion_internal_id);
            if (!def) return;
            const double base = 1.0 + def->cost * 0.15 +
                (std::clamp(unit.star, 1, 3) - 1) * 0.5;
            const double weighted = base * offensive_factor(*def);
            for (const auto& trait : def->traits) trait_score[trait] += weighted;
        };
        for (const auto& unit : player_envs[i].board) if (unit) score_composition_unit(*unit);
        for (const auto& unit : player_envs[i].bench) if (unit) score_composition_unit(*unit);

        for (const auto& [trait, count] : board_trait_counts) {
            if (trait_score.find(trait) == trait_score.end()) continue;
            const int level = trait_level(trait, count);
            if (level > 0) {
                double avg_off = 0.0;
                int matching = 0;
                const auto accumulate_offense = [&](const auto& slots) {
                    for (const auto& unit : slots) {
                        if (!unit) continue;
                        const auto* def = catalog->find_by_id(unit->champion_internal_id);
                        if (def && std::find(def->traits.begin(), def->traits.end(), trait) != def->traits.end()) {
                            avg_off += offensive_factor(*def);
                            ++matching;
                        }
                    }
                };
                accumulate_offense(player_envs[i].board);
                if (matching > 0) avg_off /= matching;
                else avg_off = 1.0;
                trait_score[trait] += (level * 2.0 + count * 0.3) * avg_off;
            }
        }
        for (const auto& [trait, count] : trait_counts) {
            if (board_trait_counts.find(trait) == board_trait_counts.end() ||
                trait_level(trait, board_trait_counts[trait]) == 0) {
                if (trait_score.find(trait) != trait_score.end())
                    trait_score[trait] += 1.0 + count * 0.2;
            }
        }
        for (auto& [trait, score] : trait_score) {
            const auto found = focus.find(trait);
            if (found != focus.end())
                score *= 1.0 + std::min(0.4, found->second * 0.08);
        }

        std::vector<std::pair<std::string, double>> sorted_traits(
            trait_score.begin(), trait_score.end());
        std::stable_sort(sorted_traits.begin(), sorted_traits.end(),
            [&](const auto& lhs, const auto& rhs) {
                if (lhs.second != rhs.second) return lhs.second > rhs.second;
                const auto left_pos = std::find(trait_order.begin(), trait_order.end(), lhs.first);
                const auto right_pos = std::find(trait_order.begin(), trait_order.end(), rhs.first);
                return left_pos < right_pos;
            });

        std::map<std::string, double> new_comp_traits;
        if (current_stage <= 2) {
            info.composition_locked = false;
            info.composition_direction.clear();
            info.composition_strength = 0.0;
        } else if (unit_count == 0) {
            info.composition_locked = false;
            info.composition_direction.clear();
            info.composition_strength = 0.0;
            focus.clear();
        } else {
            ++info.comp_direction_update_steps;
            if (info.comp_direction_update_steps >= 2) {
                info.comp_direction_update_steps = 0;
                if (!sorted_traits.empty()) {
                    const auto& top = sorted_traits.front();
                    const double second = sorted_traits.size() > 1
                        ? sorted_traits[1].second : 0.0;
                    const double gap = top.second - second;
                    const double ratio = top.second / (second + 1e-5);
                    if (!info.composition_locked && current_stage >= 3 &&
                        unit_count >= 6 && (ratio > 1.6 || gap > 2.5)) {
                        info.composition_locked = true;
                    }
                    if (info.composition_locked) {
                        int active_core = 0;
                        for (const auto& [trait, weight] : focus) {
                            const auto found = trait_score.find(trait);
                            if (found != trait_score.end() && found->second > 2.0)
                                ++active_core;
                        }
                        if (active_core == 0) info.composition_locked = false;
                    }

                    if (info.composition_locked && !focus.empty()) {
                        std::map<std::string, double> combined;
                        for (const auto& [trait, weight] : focus)
                            combined[trait] = weight * 0.6;
                        for (const auto& [trait, score] : trait_score)
                            combined[trait] += score * 0.4;
                        std::vector<std::pair<std::string, double>> ordered(
                            combined.begin(), combined.end());
                        std::stable_sort(ordered.begin(), ordered.end(),
                            [](const auto& lhs, const auto& rhs) {
                                return lhs.second > rhs.second;
                            });
                        if (!ordered.empty()) {
                            new_comp_traits[ordered[0].first] = ordered[0].second * 1.4;
                            for (std::size_t index = 1;
                                 index < std::min<std::size_t>(4, ordered.size()); ++index) {
                                if (ordered[index].second > ordered[0].second * 0.35)
                                    new_comp_traits[ordered[index].first] = ordered[index].second * 0.5;
                            }
                        }
                    } else {
                        new_comp_traits[top.first] = top.second * 1.4;
                        for (std::size_t index = 1;
                             index < std::min<std::size_t>(4, sorted_traits.size()); ++index) {
                            if (sorted_traits[index].second > top.second * 0.35)
                                new_comp_traits[sorted_traits[index].first] =
                                    sorted_traits[index].second * 0.5;
                        }
                    }
                }

                for (auto& [trait, weight] : focus) weight *= 0.95;
                for (auto it = focus.begin(); it != focus.end();) {
                    if (it->second < 0.05) it = focus.erase(it);
                    else ++it;
                }
                for (const auto& [trait, value] : new_comp_traits)
                    focus[trait] += value * 0.04;
                if (!new_comp_traits.empty()) {
                    const auto main = std::max_element(
                        new_comp_traits.begin(), new_comp_traits.end(),
                        [](const auto& lhs, const auto& rhs) { return lhs.second < rhs.second; });
                    focus[main->first] += 0.8;
                }
                if (!info.composition_direction.empty() && !new_comp_traits.empty()) {
                    const bool overlap = new_comp_traits.find(info.composition_direction) != new_comp_traits.end();
                    if (!overlap && current_stage >= 4)
                        focus[info.composition_direction] = std::max(
                            0.1, focus[info.composition_direction]) * 1.1;
                }
                for (auto& [trait, weight] : focus) weight = std::min(weight, 5.0);
                if (!new_comp_traits.empty()) {
                    const auto main = std::max_element(
                        new_comp_traits.begin(), new_comp_traits.end(),
                        [](const auto& lhs, const auto& rhs) { return lhs.second < rhs.second; });
                    info.composition_direction = main->first;
                    double total = 0.0;
                    for (const auto& [trait, value] : new_comp_traits)
                        total += std::min(value, 10.0);
                    info.composition_strength = total / new_comp_traits.size();
                } else {
                    info.composition_direction.clear();
                    info.composition_strength = 0.0;
                }
            }
        }

        // _update_comp_focus() is evaluated on every decision step, separately
        // from the direction refresh that runs every other step.
        for (auto& [trait, weight] : focus) weight *= 0.95;
        for (const auto& [trait, count] : trait_counts) {
            const auto board_count = board_trait_counts.find(trait);
            const int active_count = board_count == board_trait_counts.end()
                ? 0 : board_count->second;
            const int level = trait_level(trait, active_count);
            if (level > 0) focus[trait] += 0.25 + 0.25 * level;
            else focus[trait] += 0.10 + 0.05 * count;
        }
        if (!sorted_traits.empty()) focus[sorted_traits.front().first] += 0.8;
        if (info.composition_locked) {
            for (auto& [trait, weight] : focus) {
                const auto score = trait_score.find(trait);
                if (score != trait_score.end() && score->second > 2.0)
                    weight += 0.2;
                else
                    weight *= 0.9;
            }
        }
        if (focus.size() > 5) {
            std::vector<std::pair<std::string, double>> ordered(focus.begin(), focus.end());
            std::stable_sort(ordered.begin(), ordered.end(),
                [](const auto& lhs, const auto& rhs) { return lhs.second > rhs.second; });
            focus.clear();
            for (std::size_t index = 0; index < 5; ++index)
                focus[ordered[index].first] = ordered[index].second;
        }
        double focus_total = 0.0;
        for (const auto& [trait, weight] : focus) focus_total += std::max(0.0, weight);
        if (focus_total > 0.0) {
            for (auto& [trait, weight] : focus)
                weight = std::min(5.0, weight * 5.0 / focus_total);
        }

        // _should_lock_comp(): stage 4+ requires an active offensive synergy;
        // STABILIZE can release the lock after three rounds without a win.
        const bool stabilize_lock_suppressed =
            info.strategy == 1 && info.comp_stabilize_start_round >= 0 &&
            current_round - info.comp_stabilize_start_round >= 3 &&
            economy.win_streak == 0;
        if (!stabilize_lock_suppressed) {
            bool has_offensive_synergy = false;
            if (current_stage >= 4) {
                for (const auto& [trait, count] : board_trait_counts) {
                    if (trait_level(trait, count) < 2) continue;
                    double avg_off = 0.0;
                    int matching = 0;
                    const auto inspect = [&](const auto& slots) {
                        for (const auto& unit : slots) {
                            if (!unit) continue;
                            const auto* def = catalog->find_by_id(unit->champion_internal_id);
                            if (def && std::find(def->traits.begin(), def->traits.end(), trait) != def->traits.end()) {
                                avg_off += offensive_factor(*def);
                                ++matching;
                            }
                        }
                    };
                    inspect(player_envs[i].board);
                    inspect(player_envs[i].bench);
                    if (matching > 0 && avg_off / matching > 1.0) {
                        has_offensive_synergy = true;
                        break;
                    }
                }
            }
            if (current_stage < 4 || has_offensive_synergy) {
                double avg_board_power = 0.0;
                int alive_count = 0;
                for (std::size_t other = 0; other < kPlayersPerLobby; ++other) {
                    if (!player_envs[other].info.alive) continue;
                    avg_board_power += board_power(other);
                    ++alive_count;
                }
                if (alive_count > 0) avg_board_power /= alive_count;
                const bool board_stable = power >= avg_board_power * 0.9;
                if (economy.win_streak >= 3 ||
                    (current_stage >= 4 && board_stable) ||
                    current_stage >= 5) {
                    info.composition_locked = true;
                }
            }
        }
        info.composition_focus_weights.assign(focus.begin(), focus.end());

        for (const auto& unit_id : unit_order) {
            info.unit_counts.emplace_back(unit_names[unit_id], copies_by_unit.at(unit_id));
            info.unit_counts_by_id.emplace_back(unit_id, copies_by_unit.at(unit_id));
        }

        if (!focus_scores.empty()) {
            auto best_score = -std::numeric_limits<double>::infinity();
            for (const auto& unit_id : unit_order) {
                const auto found = focus_scores.find(unit_id);
                if (found != focus_scores.end() && found->second > best_score) {
                    best_score = found->second;
                    info.composition_focus_id = unit_id;
                    info.composition_focus = unit_names[unit_id];
                }
            }
        }

        std::vector<std::pair<std::int32_t, double>> ordered_units;
        ordered_units.reserve(focus_scores.size());
        for (const auto& unit_id : unit_order) {
            const auto found = focus_scores.find(unit_id);
            if (found != focus_scores.end()) ordered_units.emplace_back(unit_id, found->second);
        }
        std::stable_sort(ordered_units.begin(), ordered_units.end(),
            [](const auto& lhs, const auto& rhs) { return lhs.second > rhs.second; });
        for (std::size_t index = 0; index < std::min<std::size_t>(3, ordered_units.size()); ++index) {
            const auto id = ordered_units[index].first;
            info.core_unit_ids.push_back(id);
            info.core_units.push_back(unit_names[id]);
        }

        std::vector<std::pair<std::string, int>> ordered_traits;
        ordered_traits.reserve(trait_order.size());
        for (const auto& trait : trait_order)
            ordered_traits.emplace_back(trait, trait_counts.at(trait));
        std::stable_sort(ordered_traits.begin(), ordered_traits.end(),
            [](const auto& lhs, const auto& rhs) {
                return lhs.second > rhs.second;
            });
        for (const auto& [trait, count] : ordered_traits) {
            if (count >= 2 && info.core_traits.size() < 3)
                info.core_traits.push_back(trait);
        }

        // Paridade com StrategyManager.compute_strategy_confidence().
        double state_confidence = 0.5;
        if (player.hp <= 20.0f) state_confidence += 0.25;
        else if (player.hp >= 80.0f) state_confidence += 0.10;
        if (economy.gold >= 40) state_confidence += 0.15;
        else if (economy.gold < 10) state_confidence -= 0.10;
        if (power >= 70.0) state_confidence += 0.15;
        else if (power <= 20.0) state_confidence -= 0.15;
        if (economy.win_streak >= 4) state_confidence += 0.10;
        if (economy.loss_streak >= 4) state_confidence += 0.10;
        if (economy.level >= 8) state_confidence += 0.10;
        info.state_confidence = static_cast<float>(std::clamp(state_confidence, 0.0, 1.0));

        // Paridade com get_strategy_score()/choose_best_strategy().
        // O desempate mantém a primeira estratégia na ordem do enum Python.
        info.strategy_scores.clear();
        double best_score = -std::numeric_limits<double>::infinity();
        std::int32_t best_strategy = 0;
        for (std::int32_t strategy = 0; strategy < 7; ++strategy) {
            double score = 0.0;
            switch (strategy) {
                case 0: // ECON
                    score += std::min(economy.gold / 50.0, 1.0) * 5.0;
                    if (player.hp >= 60.0f) score += 2.0;
                    if (economy.loss_streak >= 3) score += 1.0;
                    break;
                case 1: // STABILIZE
                    if (player.hp < 50.0f) score += 4.0;
                    if (power < 40.0) score += 4.0;
                    if (economy.loss_streak >= 2) score += 2.0;
                    break;
                case 2: // FAST8
                    if (economy.level >= 6) score += 2.0;
                    if (economy.gold >= 30) score += 3.0;
                    if (player.hp >= 50.0f) score += 2.0;
                    break;
                case 3: // SLOWROLL
                    if (economy.level <= 6) score += 3.0;
                    if (economy.gold >= 30) score += 3.0;
                    if (power >= 30.0) score += 2.0;
                    break;
                case 4: // ALL_IN
                    if (player.hp <= 25.0f) score += 6.0;
                    if (economy.loss_streak >= 5) score += 2.0;
                    if (power < 30.0) score += 2.0;
                    break;
                case 5: // WINSTREAK
                    if (economy.win_streak >= 3) score += 5.0;
                    if (player.hp >= 60.0f) score += 2.0;
                    if (power >= 40.0) score += 2.0;
                    break;
                case 6: // LOSS_STREAK
                    if (economy.loss_streak >= 3) score += 5.0;
                    if (player.hp >= 40.0f) score += 1.0;
                    break;
            }
            info.strategy_scores.emplace_back(strategy, score);
            if (score > best_score) {
                best_score = score;
                best_strategy = strategy;
            }
        }
        info.best_scored_strategy = best_strategy;
        info.active_traits_count = static_cast<std::int32_t>(info.active_traits.size());

        if (list.empty()) list.push_back(info);
        else list.back() = info;
    }

    double state_reward(std::size_t i, double action_reward) {
        const double power = board_power(i);
        const double synergy = synergy_score(i);
        const double positioning = positioning_score(i);
        double reward = action_reward;

        reward += reward_model::power(power, player_envs[i].previous_board_power);
        player_envs[i].previous_board_power = power;

        reward += reward_model::synergy(synergy, player_envs[i].previous_synergy_score);
        player_envs[i].previous_synergy_score = synergy;

        reward += reward_model::positioning(positioning, player_envs[i].previous_positioning_score);
        player_envs[i].previous_positioning_score = positioning;

        const auto current_level = player_envs[i].economy.level;
        if (current_level > player_envs[i].previous_reward_level) {
            reward += reward_model::level(current_level, player_envs[i].previous_reward_level);
            player_envs[i].previous_reward_level = current_level;
        }

        reward += reward_model::economy(player_envs[i].economy.gold, player_envs[i].info.hp);
        reward += reward_model::streak(
            player_envs[i].economy.win_streak, player_envs[i].economy.loss_streak);

        int occupied = 0;
        for (const auto& unit : player_envs[i].board) if (unit) ++occupied;
        reward += reward_model::board(occupied, static_cast<int>(kBoardSlots));
        return reward;
    }

    void sync_player_economy(std::size_t player_index) {
        if (player_index >= kPlayersPerLobby) {
            throw std::out_of_range(
                "Indice de jogador invalido ao sincronizar economia."
            );
        }

        const auto& economy = player_envs[player_index].economy;
        auto& player = player_envs[player_index].info;

        player.gold = economy.gold;
        player.level = economy.level;
        player.xp = economy.xp;
    }

    bool all_alive_players_finished_round() const {
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (player_envs[i].info.alive && !round_finished[i]) {
                return false;
            }
        }
        return true;
    }

    void mark_round_completion(std::size_t player_index) {
        if (!player_envs[player_index].info.alive) {
            return;
        }

        ++round_actions[player_index];
        if (round_actions[player_index] >= kMaxActionsPerRound) {
            round_finished[player_index] = true;
        }
    }

    void reset_round_completion() {
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (player_envs[i].info.alive) {
                round_actions[i] = 0;
                player_envs[i].actions_taken_this_round = 0;
                round_finished[i] = false;
            } else {
                round_finished[i] = true;
            }
        }
    }

    // Converte a formação atual da lobby para a entrada da engine de combate.
    // A engine de combate permanece independente: recebe equipes e devolve o resultado.
    void append_combat_team(
        std::size_t player_index,
        UnitTeam team,
        CombatTeam& output,
        int& next_unit_id
    ) const {
        output.team = team;
        output.player_id = static_cast<std::int32_t>(player_index);
        output.player_hp = player_envs[player_index].info.hp;

        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            if (!player_envs[player_index].board[slot]) {
                continue;
            }

            const auto& instance = *player_envs[player_index].board[slot];
            const auto* definition =
                catalog->find_by_id(instance.champion_internal_id);
            if (!definition) {
                continue;
            }

            const auto& stats = definition->stats;
            const auto& profile = definition->combat_profile;

            CombatUnit unit{};
            // Same deterministic sequential IDs as TFTLobby._build_cpp_combat_input().
            unit.id = next_unit_id++;
            unit.api_name = definition->api_name;
            unit.name = definition->name;
            unit.star = std::clamp(instance.star, 1, 3);
            unit.team = team;

            const auto role_value = std::clamp(profile.role, 0, 4);
            unit.role = static_cast<UnitRole>(role_value);

            unit.position.x = static_cast<int>(slot % 7);
            unit.position.y = static_cast<int>(slot / 7);
            // Os tabuleiros ficam frente a frente durante o combate.
            if (team == UnitTeam::PLAYER_B) {
                // Python mirrors columns (x), not rows (y), for team B.
                unit.position.x = 6 - unit.position.x;
            }
            unit.source_board_position = static_cast<int>(slot);

            const double max_hp =
                profile.max_hp > 0.0 ? profile.max_hp : stats.max_hp;
            unit.max_hp = static_cast<float>(std::max(1.0, max_hp > 0.0 ? max_hp : 100.0));
            unit.hp = unit.max_hp;

            const double attack_damage =
                profile.attack_damage > 0.0
                    ? profile.attack_damage
                    : stats.attack_damage;
            // Match TFTLobby._build_cpp_combat_input() fallbacks.
            unit.attack_damage = static_cast<float>(
                std::max(1.0, attack_damage > 0.0 ? attack_damage : 30.0));

            const double attack_speed =
                profile.attack_speed > 0.0
                    ? profile.attack_speed
                    : stats.attack_speed;
            unit.attack_speed = static_cast<float>(
                std::max(0.1, attack_speed > 0.0 ? attack_speed : 1.0));

            const double attack_range =
                profile.attack_range > 0.0
                    ? profile.attack_range
                    : stats.attack_range;
            unit.attack_range = static_cast<float>(
                std::max(1.0, attack_range > 0.0 ? attack_range : 1.0));

            unit.armor = static_cast<float>(
                profile.armor > 0.0 ? profile.armor : stats.armor);
            unit.magic_resist = static_cast<float>(
                profile.magic_resist > 0.0
                    ? profile.magic_resist
                    : stats.magic_resist);

            unit.alive = true;
            unit.can_move = true;
            unit.can_attack = true;
            unit.can_cast = true;

            output.units.push_back(std::move(unit));
        }
    }

    void return_eliminated_player_units(std::size_t player_index) {
        if (player_envs[player_index].shop) player_envs[player_index].shop->return_current_shop();

        auto return_unit_copies = [this](const std::optional<UnitInstance>& unit) {
            if (!unit) return;
            for (std::int32_t copy = 0; copy < star_copies(unit->star); ++copy)
                (void)pool->give_back(unit->champion_internal_id);
        };
        for (auto& unit : player_envs[player_index].board) {
            return_unit_copies(unit);
            unit.reset();
        }
        for (auto& unit : player_envs[player_index].bench) {
            return_unit_copies(unit);
            unit.reset();
        }
        register_position_state(player_index);
    }

    void eliminate_players(std::vector<std::string>& events) {
        // Python define as colocações após todos os combates, em ordem de ID.
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            auto& player = player_envs[i].info;
            if (!player.alive || player.hp > 0.0f) continue;
            player.hp = 0.0f;
            player.alive = false;
            player.eliminated = true;
            player.placement = alive_players;
            ranking.push_back(static_cast<std::int32_t>(i));
            --alive_players;
            round_finished[i] = true;
            return_eliminated_player_units(i);
            events.emplace_back("ELIMINATED: jogador " + std::to_string(i));
        }
    }

    void finish_if_one_player_left() {
        if (alive_players > 1) return;
        done = true;
        winner_id.reset();
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (player_envs[i].info.alive) {
                winner_id = static_cast<std::int32_t>(i);
                player_envs[i].info.placement = 1;
                if (std::find(ranking.begin(), ranking.end(),
                              static_cast<std::int32_t>(i)) == ranking.end())
                    ranking.insert(ranking.begin(), static_cast<std::int32_t>(i));
                break;
            }
        }
        if (!winner_id && ranking.size() < kPlayersPerLobby) {
            for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
                if (std::find(ranking.begin(), ranking.end(),
                              static_cast<std::int32_t>(i)) == ranking.end()) {
                    player_envs[i].info.placement = static_cast<std::int32_t>(
                        kPlayersPerLobby - ranking.size());
                    ranking.push_back(static_cast<std::int32_t>(i));
                }
            }
        }

        // Public ranking is ordered best-to-worst, matching Python's
        // TFTLobby._finalize_ranking(). Eliminations are appended in the
        // order they happen (worst placement first), so insertion order is
        // not a valid final ranking once the winner is prepended.
        const auto placement_for = [this](std::int32_t player_id) {
            const auto& placement =
                player_envs[static_cast<std::size_t>(player_id)].info.placement;
            return placement.value_or(
                static_cast<std::int32_t>(kPlayersPerLobby + 1));
        };
        std::stable_sort(
            ranking.begin(),
            ranking.end(),
            [&](std::int32_t lhs, std::int32_t rhs) {
                const auto lhs_placement = placement_for(lhs);
                const auto rhs_placement = placement_for(rhs);
                if (lhs_placement != rhs_placement) {
                    return lhs_placement < rhs_placement;
                }
                return lhs < rhs;
            });
    }

    void resolve_combats(
        std::vector<std::string>& events,
        std::array<float, kPlayersPerLobby>& rewards,
        std::array<float, kPlayersPerLobby>& combat_rewards
    ) {
        std::vector<std::size_t> alive;
        alive.reserve(kPlayersPerLobby);
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            player_envs[i].info.opponent_id.reset();
            if (player_envs[i].info.alive) alive.push_back(i);
        }
        if (alive.size() < 2) {
            finish_if_one_player_left();
            return;
        }

        std::shuffle(alive.begin(), alive.end(), matchmaking_rng);
        std::vector<std::pair<std::size_t, std::size_t>> matchups;
        for (std::size_t i = 0; i + 1 < alive.size(); i += 2) {
            const auto a = alive[i];
            auto b = alive[i + 1];
            if (alive.size() > 2 && previous_matchups.contains(matchup_key(a, b))) {
                for (std::size_t j = i + 2; j < alive.size(); ++j) {
                    if (!previous_matchups.contains(matchup_key(a, alive[j]))) {
                        std::swap(alive[i + 1], alive[j]);
                        b = alive[i + 1];
                        break;
                    }
                }
            }
            matchups.emplace_back(a, b);
            player_envs[a].info.opponent_id = static_cast<std::int32_t>(b);
            player_envs[b].info.opponent_id = static_cast<std::int32_t>(a);
            previous_matchups.insert(matchup_key(a, b));
        }

        auto apply_damage = [&](std::size_t player_index, std::int32_t damage) {
            auto& player = player_envs[player_index].info;
            if (!player.alive || damage <= 0) return;
            const float applied = std::min(player.hp, static_cast<float>(damage));
            player.hp = std::max(0.0f, player.hp - applied);
            player.damage_taken += applied;
        };

        for (const auto& [a, b] : matchups) {
            if (!player_envs[a].info.alive || !player_envs[b].info.alive) continue;
            CombatInput input{};
            input.context = CombatContext::PVP;
            // Python TFTLobby sends the lobby seed unchanged for each
            // deterministic combat; unit IDs are sequential across both teams.
            input.seed = seed;
            input.config.seed = seed;
            input.config.board_rows = 4;
            input.config.board_cols = 7;
            input.config.max_duration = 30.0f;
            input.config.max_events = 100000;
            input.config.deterministic = true;
            int next_unit_id = 0;
            append_combat_team(a, UnitTeam::PLAYER_A, input.player_a, next_unit_id);
            append_combat_team(b, UnitTeam::PLAYER_B, input.player_b, next_unit_id);

            const bool empty_a = input.player_a.units.empty();
            const bool empty_b = input.player_b.units.empty();
            if (empty_a && empty_b) {
                // Igual ao Python: empate sem recompensa e sem alterar streak.
                events.emplace_back("COMBAT_DRAW_EMPTY: jogadores " +
                    std::to_string(a) + " e " + std::to_string(b));
                continue;
            }

            std::size_t winner = 0, loser = 0;
            std::int32_t winner_survivors = 0;
            std::int32_t loser_survivors = 0;
            if (empty_a || empty_b) {
                winner = empty_a ? b : a;
                loser = empty_a ? a : b;
                winner_survivors = static_cast<std::int32_t>(
                    empty_a ? input.player_b.units.size() : input.player_a.units.size());
                events.emplace_back("AUTO_WIN_EMPTY_BOARD: jogador " +
                    std::to_string(winner) + " venceu jogador " + std::to_string(loser));
            } else {
                const auto combat = combat_engine.simulate(input);
                if (!combat.success || !combat.completed)
                    throw std::runtime_error("CombatEngine falhou no confronto " +
                        std::to_string(a) + " vs " + std::to_string(b) +
                        ": " + combat.error_code + " - " + combat.error_message);
                events.emplace_back("COMBAT: jogador " + std::to_string(a) +
                    " vs " + std::to_string(b) + ", eventos=" +
                    std::to_string(combat.events_processed));
                if (combat.timeout) {
                    events.emplace_back(
                        "COMBAT_TIMEOUT: resultado parcial aceito para " +
                        std::to_string(a) + " vs " + std::to_string(b));
                }
                if (combat.winner == CombatWinner::PLAYER_A) {
                    winner = a; loser = b;
                    winner_survivors = combat.player_a_survivors;
                    loser_survivors = combat.player_b_survivors;
                } else if (combat.winner == CombatWinner::PLAYER_B) {
                    winner = b; loser = a;
                    winner_survivors = combat.player_b_survivors;
                    loser_survivors = combat.player_a_survivors;
                } else {
                    // TFTLobby.resolve_combat() não altera streak em empate:
                    // apply_combat_result() só roda quando há vencedor e perdedor.
                    sync_player_economy(a);
                    sync_player_economy(b);
                    events.emplace_back("COMBAT_DRAW: jogadores " +
                        std::to_string(a) + " e " + std::to_string(b));
                    continue;
                }
            }

            ++player_envs[winner].info.wins;
            ++player_envs[loser].info.losses;
            economy_engine.register_pvp_win(player_envs[winner].economy);
            economy_engine.register_loss(player_envs[loser].economy);
            const auto damage = stage_damage(stage) + std::max(0, winner_survivors);
            apply_damage(loser, damage);
            const double winner_reward = combat_reward(
                true, damage, 0, loser_survivors, winner_survivors);
            const double loser_reward = combat_reward(
                false, 0, damage, winner_survivors, loser_survivors);
            player_envs[winner].last_combat_reward = winner_reward;
            player_envs[loser].last_combat_reward = loser_reward;
            combat_rewards[winner] += static_cast<float>(winner_reward);
            combat_rewards[loser] += static_cast<float>(loser_reward);
            rewards[winner] += static_cast<float>(winner_reward);
            rewards[loser] += static_cast<float>(loser_reward);
            events.emplace_back("COMBAT_WIN: jogador " + std::to_string(winner) +
                ", dano=" + std::to_string(damage) +
                ", sobreviventes=" + std::to_string(winner_survivors));
            sync_player_economy(winner);
            sync_player_economy(loser);
        }

        eliminate_players(events);
        finish_if_one_player_left();
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) refresh_masks(i);
    }
};

TFTEngine::Impl::PlayerTransition TFTEngine::Impl::PlayerEnv::step(
    TFTEngine::Impl& lobby,
    std::size_t player_id,
    const PlayerAction& player_action
) {

        const auto& action = player_action.values;

        const auto type = action[0];

        const auto shop_slot = action[1];
        actions_taken_this_round = std::min<std::uint32_t>(
            kActionMemoryHorizon, actions_taken_this_round + 1);
        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            if (board[slot]) {
                board_move_age[slot] = std::min<std::uint32_t>(
                    kActionMemoryHorizon, board_move_age[slot] + 1);
            } else {
                board_move_age[slot] = kActionMemoryHorizon;
            }
        }

        auto& economy = this->economy;
        auto& shop = *this->shop;
        ++this->action_serial;
        this->recent_purchases.erase(
            std::remove_if(this->recent_purchases.begin(), this->recent_purchases.end(),
                [this](const RecentPurchase& purchase) {
                    return this->action_serial - purchase.action_serial > 4;
                }),
            this->recent_purchases.end());
        const auto old_gold = economy.gold;
        const auto old_level = economy.level;
        const auto old_xp = economy.xp;
        int old_board_count = 0, old_bench_count = 0;
        const double old_synergy_score = lobby.synergy_score(player_id);
        const double old_positioning_score = lobby.positioning_score(player_id);
        bool sold_core_unit = false;
        bool sold_unit_protects_upgrade = false;
        double sold_unit_fit_score = 0.0;
        bool buy_completes_upgrade = false;
        bool buy_builds_pair = false;
        bool bought_unit_successfully = false;
        bool bought_upgrade = false;
        bool purchase_was_recently_reversed = false;
        double reversed_purchase_prior_reward = 0.0;
        bool board_capacity_violation = false;
        bool anti_loop_blocked = false;
        std::array<std::string, kBoardSlots> old_board_layout{};
        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            if (this->board[slot]) {
                ++old_board_count;
                old_board_layout[slot] = this->board[slot]->uuid;
            }
        }
        for (const auto& unit : this->bench) if (unit) ++old_bench_count;

        // Compare a candidate against the current composition before mutating
        // the board. This makes a replacement's reward relative, not absolute.
        const StrategyInfo strategy_before = this->strategy.empty()
            ? StrategyInfo{} : this->strategy.back();
        double board_comp_score_sum = 0.0;
        int board_comp_score_count = 0;
        for (const auto& unit : this->board) {
            if (!unit) continue;
            const auto* def = lobby.catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            board_comp_score_sum += unit_composition_score(
                strategy_before, *def, unit->star);
            ++board_comp_score_count;
        }
        double candidate_comp_score = 0.0;
        double displaced_comp_score = 0.0;
        bool has_candidate_comp_score = false;
        bool has_displaced_comp_score = false;
        if (type == 0) {
            // BUY: avalia a oferta contra a direção atual da composição,
            // para que comprar qualquer unidade não tenha sempre a mesma recompensa.
            const auto* offer = shop.get_unit(shop_slot);
            if (offer) {
                const auto* def = lobby.catalog->find_by_id(
                    offer->champion_internal_id);
                if (def) {
                    candidate_comp_score = unit_composition_score(
                        strategy_before, *def, offer->star);
                    has_candidate_comp_score = true;
                    int same_star_copies = 0;
                    for (const auto& unit : this->board) {
                        if (unit && unit->champion_internal_id == offer->champion_internal_id &&
                            unit->star == offer->star) ++same_star_copies;
                    }
                    for (const auto& unit : this->bench) {
                        if (unit && unit->champion_internal_id == offer->champion_internal_id &&
                            unit->star == offer->star) ++same_star_copies;
                    }
                    buy_completes_upgrade = same_star_copies >= 2;
                    // A second matching copy is valuable future upgrade potential,
                    // but only reward it when it also fits the current comp.
                    const bool composition_fit =
                        candidate_comp_score > 0.0 ||
                        strategy_before.composition_direction.empty();
                    buy_builds_pair = same_star_copies == 1 &&
                        offer->star == 1 && composition_fit;
                }
            }
        } else if (type == 3) {
            const auto source = static_cast<std::size_t>(action[2]);
            const auto target = static_cast<std::size_t>(action[3]);
            if (source < this->bench.size() && this->bench[source]) {
                const auto* def = lobby.catalog->find_by_id(
                    this->bench[source]->champion_internal_id);
                if (def) {
                    candidate_comp_score = unit_composition_score(
                        strategy_before, *def, this->bench[source]->star);
                    has_candidate_comp_score = true;
                }
            }
            if (target < this->board.size() && this->board[target]) {
                const auto* def = lobby.catalog->find_by_id(
                    this->board[target]->champion_internal_id);
                if (def) {
                    displaced_comp_score = unit_composition_score(
                        strategy_before, *def, this->board[target]->star);
                    has_displaced_comp_score = true;
                }
            }
        }
        double composition_quality_delta = 0.0;
        if (has_candidate_comp_score) {
            if (has_displaced_comp_score) {
                composition_quality_delta =
                    candidate_comp_score - displaced_comp_score;
            } else if (board_comp_score_count > 0) {
                composition_quality_delta = candidate_comp_score -
                    board_comp_score_sum / board_comp_score_count;
            } else {
                composition_quality_delta = candidate_comp_score;
            }
        }

        if (!this->info.alive) {
            lobby.refresh_masks(player_id);
            return PlayerTransition{0.0f, false};
        }

        if (type == 0) {
            // BUY
            const auto* offer = shop.get_unit(shop_slot);

            std::size_t free_slot = kBenchSlots;

            for (std::size_t slot = 0;
                 slot < kBenchSlots;
                 ++slot) {
                if (!this->bench[slot]) {
                    free_slot = slot;
                    break;
                }
            }

            if (offer && free_slot < kBenchSlots) {
                const auto* definition =
                    lobby.catalog->find_by_id(
                        offer->champion_internal_id
                    );

                if (definition &&
                    economy.gold >= definition->cost &&
                    lobby.economy_engine.spend_gold(
                        economy,
                        definition->cost
                    )) {
                    auto purchased =
                        shop.take_unit(shop_slot);

                    if (purchased) {
                        bought_unit_successfully = true;
                        this->bench[free_slot] = std::move(*purchased);

                        // Auto-upgrade 3x1★ -> 2★ e 3x2★ -> 3★.
                        // O pool não muda: as cópias continuam pertencendo ao jogador.
                        auto& bought_unit = this->bench[free_slot];
                        while (bought_unit && bought_unit->star < 3) {
                            const auto champion_id = bought_unit->champion_internal_id;
                            const auto star = bought_unit->star;
                            std::vector<std::pair<bool, std::size_t>> matches;
                            matches.emplace_back(false, free_slot);
                            for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
                                if (slot != free_slot && this->bench[slot] &&
                                    this->bench[slot]->champion_internal_id == champion_id &&
                                    this->bench[slot]->star == star)
                                    matches.emplace_back(false, slot);
                            }
                            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                                if (this->board[slot] &&
                                    this->board[slot]->champion_internal_id == champion_id &&
                                    this->board[slot]->star == star)
                                    matches.emplace_back(true, slot);
                            }
                            if (matches.size() < 3) break;
                            bought_upgrade = true;
                            std::size_t removed = 0;
                            for (const auto& [on_board, slot] : matches) {
                                if (!on_board && slot == free_slot) continue;
                                if (on_board) this->board[slot].reset();
                                else this->bench[slot].reset();
                                if (++removed == 2) break;
                            }
                            bought_unit->star = star + 1;
                        }
                        if (bought_unit && !bought_upgrade) {
                            this->recent_purchases.push_back(RecentPurchase{
                                bought_unit->uuid,
                                bought_unit->champion_internal_id,
                                bought_unit->star,
                                this->action_serial,
                                definition->cost,
                                buy_builds_pair,
                                false,
                                false,
                                std::max(0.0, candidate_comp_score),
                                0.0,
                                strategy_before.composition_direction
                            });
                        }
                        lobby.register_position_state(player_id);
                    } else {
                        lobby.economy_engine.add_gold(
                            economy,
                            definition->cost
                        );
                    }
                }
            }
        } else if (type == 1) {
            // REROLL
            if (lobby.economy_engine.spend_gold(
                    economy,
                    EconomyEngine::REROLL_COST
                )) {
                shop.reroll(economy.level);
            }
        } else if (type == 2) {
            // BUY XP
            (void)lobby.economy_engine.buy_xp(economy);
        } else if (type == 3) {
            // MOVE_BENCH: implantação ou substituição de uma unidade.
            auto& anti_loop = this->anti_loop;
            anti_loop.record_execution_attempt();

            const auto source = action[2];
            const auto target = action[3];
            const auto state = lobby.build_decision_state(player_id);
            const auto validation =
                decision::MoveValidator::validate_bench_to_board_move(
                    state.board,
                    state.bench,
                    source,
                    target
                );

            if (validation.is_valid()) {
                const auto source_index = static_cast<std::size_t>(source);
                const auto target_index = static_cast<std::size_t>(target);

                // Uma casa vazia acrescenta uma unidade à equipe. Se o limite
                // do nível já foi atingido, rejeita a ação e aplica -0.25.
                if (
                    !state.board[target_index].has_value()
                    && old_board_count >= economy.level
                ) {
                    board_capacity_violation = true;
                } else {
                    const auto unit_identity =
                        std::optional<decision::UnitIdentity>{
                            state.bench[source_index]->identity
                        };
                    const auto displaced_unit_identity =
                        state.board[target_index].has_value()
                            ? std::optional<decision::UnitIdentity>{
                                  state.board[target_index]->identity
                              }
                            : std::nullopt;
                    const std::string move_type = "bench_to_board";
                    std::string block_reason;
                    const bool move_allowed =
                        lobby.action_mask_engine.is_bench_to_board_move_allowed(
                            state, anti_loop, source, target, &block_reason
                        );

                    if (!move_allowed) {
                        anti_loop_blocked = true;
                        (void)anti_loop.block_move(
                            move_type,
                            source,
                            target,
                            unit_identity
                        );
                        anti_loop.record_execution_block(
                            block_reason.empty() ? "cycle" : block_reason
                        );
                    } else {
                        const std::string moved_uuid = this->bench[source_index]
                            ? this->bench[source_index]->uuid : std::string{};
                        for (auto& purchase : this->recent_purchases) {
                            if (!moved_uuid.empty() && purchase.uuid == moved_uuid)
                                purchase.was_deployed = true;
                        }
                        (void)anti_loop.register_move(
                            move_type,
                            source,
                            target,
                            unit_identity,
                            displaced_unit_identity
                        );

                        if (this->board[target_index].has_value()) {
                            // Substituição: a unidade retirada volta ao slot
                            // do banco que acabou de ser liberado.
                            std::swap(
                                this->board[target_index],
                                this->bench[source_index]
                            );
                        } else {
                            this->board[target_index] =
                                std::move(this->bench[source_index]);
                            this->bench[source_index].reset();
                        }

                        anti_loop.record_successful_move(move_type);
                        board_move_age[target_index] = 0;
                        lobby.register_position_state(player_id);
                    }
                }
            }

        } else if (type == 4) {
            // MOVE_BOARD: movimento ou troca
            auto& anti_loop = this->anti_loop;

            anti_loop.record_execution_attempt();

            const auto source = action[4];
            const auto target = action[5];

            const auto state =
                lobby.build_decision_state(player_id);

            const auto validation =
                decision::MoveValidator::validate_board_move(
                    state.board,
                    source,
                    target
                );

            if (validation.is_valid() &&
                validation.move_type.has_value()) {
                const auto source_index =
                    static_cast<std::size_t>(source);

                const auto target_index =
                    static_cast<std::size_t>(target);

                const auto unit_identity =
                    std::optional<decision::UnitIdentity>{
                        state.board[source_index]->identity
                    };

                const std::string move_type =
                    *validation.move_type ==
                        decision::MoveType::BOARD_SWAP
                        ? "board_swap"
                        : "board_move";

                std::string block_reason;
                const bool move_allowed =
                    lobby.action_mask_engine.is_board_move_allowed(
                        state, anti_loop, source, target, &block_reason
                    );

                if (!move_allowed) {
                    anti_loop_blocked = true;
                    (void)anti_loop.block_move(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                    anti_loop.record_execution_block(
                        block_reason.empty() ? "cycle" : block_reason
                    );
                } else {
                    (void)anti_loop.register_move(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                    if (move_type == "board_swap") {
                        std::swap(
                            this->board[source_index],
                            this->board[target_index]
                        );
                    } else {
                        this->board[target_index] =
                            std::move(
                                this->board[source_index]
                            );

                        this->board[source_index].reset();
                    }

                    anti_loop.record_successful_move(move_type);
                    board_move_age[target_index] = 0;
                    if (move_type == "board_swap") {
                        board_move_age[source_index] = 0;
                    } else {
                        board_move_age[source_index] = kActionMemoryHorizon;
                    }

                    lobby.register_position_state(player_id);
                }
            }
        } else if (type == 5) {
            // SELL: vender unidade do banco
            const auto bench_slot =
                static_cast<std::size_t>(action[2]);

            if (bench_slot < kBenchSlots &&
                this->bench[bench_slot]) {
                const auto& unit =
                    *this->bench[bench_slot];

                const auto* definition =
                    lobby.catalog->find_by_id(
                        unit.champion_internal_id
                    );

                if (definition) {
                    const std::string sold_uuid = unit.uuid;
                    const auto recent = std::find_if(
                        this->recent_purchases.rbegin(), this->recent_purchases.rend(),
                        [&sold_uuid](const RecentPurchase& purchase) {
                            return !sold_uuid.empty() && purchase.uuid == sold_uuid;
                        });
                    if (recent != this->recent_purchases.rend()) {
                        const bool direction_changed = !this->strategy.empty() &&
                            this->strategy.back().composition_direction != recent->comp_direction;
                        if (!recent->completed_upgrade && !recent->was_deployed &&
                            recent->fit_score <= 1e-6 &&
                            old_bench_count < static_cast<int>(kBenchSlots) &&
                            !direction_changed) {
                            purchase_was_recently_reversed = true;
                            reversed_purchase_prior_reward = recent->reward;
                        }
                    }
                    if (!this->strategy.empty()) {
                        const auto& current_strategy = this->strategy.back();
                        const auto& core_unit_ids = current_strategy.core_unit_ids;
                        sold_core_unit = std::find(
                            core_unit_ids.begin(), core_unit_ids.end(),
                            unit.champion_internal_id
                        ) != core_unit_ids.end();
                        sold_unit_fit_score = std::clamp(
                            unit_composition_score(current_strategy, *definition, unit.star) / 22.5,
                            0.0, 1.0);
                    }
                    int same_star_copies = 0;
                    for (const auto& candidate : this->board) {
                        if (candidate &&
                            candidate->champion_internal_id == unit.champion_internal_id &&
                            candidate->star == unit.star) ++same_star_copies;
                    }
                    for (const auto& candidate : this->bench) {
                        if (candidate &&
                            candidate->champion_internal_id == unit.champion_internal_id &&
                            candidate->star == unit.star) ++same_star_copies;
                    }
                    // Selling one of a pair removes an immediate path toward a merge.
                    sold_unit_protects_upgrade = same_star_copies >= 2;
                    const auto sell_value =
                        EconomyEngine::get_sell_value(
                            definition->cost,
                            unit.star
                        );

                    // Só confirma a venda se a devolução ao pool
                    // for aceita.
                    bool returned_all_copies = true;
                    const auto copies = star_copies(unit.star);
                    std::int32_t returned = 0;
                    for (; returned < copies; ++returned) {
                        if (!lobby.pool->give_back(unit.champion_internal_id)) {
                            returned_all_copies = false;
                            break;
                        }
                    }
                    if (returned_all_copies) {
                        this->bench[bench_slot].reset();
                        (void)lobby.economy_engine.add_gold(economy, sell_value);
                        lobby.register_position_state(player_id);
                    } else {
                        for (std::int32_t copy = 0; copy < returned; ++copy)
                            (void)lobby.pool->take(unit.champion_internal_id);
                    }
                }
            }
        } else if (type == 6) {
            // PASS
        }

        lobby.sync_player_economy(player_id);
        int new_board_count = 0, new_bench_count = 0;
        for (const auto& unit : this->board) if (unit) ++new_board_count;
        for (const auto& unit : this->bench) if (unit) ++new_bench_count;

        // Alinhado a RewardManager.calculate_action_reward() e aos valores
        // usados em env.py para compra, reroll e XP.
        double action_reward = 0.0;
        bool success = false;
        if (type == 0) {
            // The unit may be bought successfully while immediately consuming
            // two copies in an automatic upgrade, so slot counts are not a
            // reliable signal of success. Match MiniTFTEnv._execute_buy():
            // No unconditional bonus for a normal purchase; +0.30 for a completed upgrade.
            success = bought_unit_successfully;
            action_reward = !success ? -0.10 : (bought_upgrade ? 0.30 : 0.0);
            if (success && has_candidate_comp_score) {
                // Also guide early purchases before the board has a stable comp.
                // composition_quality_delta is candidate-vs-board when a board
                // exists, or the candidate's strategic score when it is empty.
                action_reward += reward_model::purchase_quality(
                    composition_quality_delta, false);
            }
            if (success && buy_completes_upgrade) {
                action_reward += 0.12;
            } else if (success && buy_builds_pair) {
                action_reward += reward_model::purchase_pair_quality(
                    candidate_comp_score);
            }
        } else if (type == 1) {
            success = economy.gold == old_gold - EconomyEngine::REROLL_COST;
            action_reward = success ? -0.01 : -0.10;
        } else if (type == 2) {
            success = economy.gold == old_gold - EconomyEngine::BUY_XP_COST;
            action_reward = success ? 0.02 : -0.10;
            // RewardManager tracks the last rewarded level, initialized to 1,
            // not merely the level at the start of this action.
            if (success && economy.level > old_level &&
                economy.level > this->previous_reward_level) {
                action_reward += reward_model::level(
                    economy.level, this->previous_reward_level);
                this->previous_reward_level = economy.level;
            }
            (void)old_level;
            (void)old_xp;
        } else if (type == 3 || type == 4) {
            bool board_layout_changed = false;
            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                const std::string current_uuid = this->board[slot]
                    ? this->board[slot]->uuid : std::string{};
                if (current_uuid != old_board_layout[slot]) {
                    board_layout_changed = true;
                    break;
                }
            }
            // Tanto a implantação como a substituição alteram o layout.
            // Capacidade excedida é a única falha com penalidade específica.
            success = board_layout_changed;
            action_reward = board_capacity_violation
                ? -0.25
                : (anti_loop_blocked
                    ? reward_model::blocked_move()
                    : (success ? 0.0 : -0.10));

            if (success && !board_capacity_violation && !anti_loop_blocked) {
                const double positioning_delta =
                    lobby.positioning_score(player_id) - old_positioning_score;
                const double synergy_delta =
                    lobby.synergy_score(player_id) - old_synergy_score;

                // Both deployments and board-to-board moves must earn reward
                // from an actual improvement. A successful layout mutation is
                // not progress by itself: this was the source of repeated
                // Nasus/Briar shuffling (+0.02 for every board move).
                action_reward += 0.05 * std::tanh(positioning_delta);
                action_reward += 0.10 * std::tanh(synergy_delta);

                if (type == 3) {
                    action_reward += 0.10 * std::tanh(
                        composition_quality_delta / 5.0);

                    const bool composition_improved =
                        old_board_count == 0 ||
                        composition_quality_delta > 1e-6 ||
                        synergy_delta > 1e-6 ||
                        positioning_delta > 1e-6;

                    if (new_board_count > old_board_count && composition_improved) {
                        action_reward += 0.25;
                        const int board_capacity = std::min(
                            economy.level, static_cast<int>(kBoardSlots));
                        if (new_board_count == board_capacity) {
                            // Capacity bonus only applies when the deployment
                            // improves composition, synergy, or positioning.
                            action_reward += reward_model::board_capacity_completion();
                        }
                    } else if (new_board_count <= old_board_count && !composition_improved) {
                        // A replacement that neither grows the team nor improves
                        // fit/synergy/positioning must not be a free action.
                        action_reward += reward_model::movement_no_progress_penalty(
                            composition_quality_delta, synergy_delta, positioning_delta);
                    }
                } else if (
                    positioning_delta <= 1e-6 &&
                    synergy_delta <= 1e-6
                ) {
                    // Preserve the delta-based shaping above and add a baseline
                    // cost plus extra penalty proportional to actual degradation.
                    action_reward += reward_model::movement_no_progress_penalty(
                        0.0, synergy_delta, positioning_delta);
                }
            }
        } else if (type == 5) {
            success = economy.gold > old_gold;
            action_reward = success
                ? reward_model::sale_quality(
                    sold_unit_fit_score, sold_core_unit,
                    sold_unit_protects_upgrade, old_bench_count >= static_cast<int>(kBenchSlots))
                : -0.10;
            if (success && purchase_was_recently_reversed &&
                !sold_core_unit && !sold_unit_protects_upgrade &&
                old_bench_count < static_cast<int>(kBenchSlots)) {
                action_reward += reward_model::reversed_purchase_penalty();
            }
        } else {
            success = true;
        }

        // Give spending decisions immediate feedback for the opportunity cost
        // of liquid gold and the interest breakpoints. This is a potential delta,
        // not a per-step bonus, so repeatedly PASSing cannot farm reward.
        const double action_gold_reward =
            reward_model::gold_change_reward(old_gold, economy.gold);
        action_reward += action_gold_reward;

        // Persist the complete buy reward so a later proven reversal can be
        // prevented from making the aggregate purchase->sale sequence positive.
        if (type == 0 && success && !bought_upgrade) {
            for (auto it = this->recent_purchases.rbegin();
                 it != this->recent_purchases.rend(); ++it) {
                if (it->action_serial == this->action_serial) {
                    it->reward = action_reward;
                    break;
                }
            }
        }
        if (type == 5 && success && purchase_was_recently_reversed) {
            constexpr double kReversedSequenceTarget = -0.02;
            const double required_adjustment =
                kReversedSequenceTarget - reversed_purchase_prior_reward -
                action_reward - action_gold_reward;
            if (required_adjustment < 0.0)
                action_reward += required_adjustment;
        }

        // MiniTFTEnv.step() returns the action-specific reward directly.
        // RewardManager's broader state components are not called by the
        // Python environment, so applying them here would change PPO targets.
        lobby.update_strategy(player_id);
        return PlayerTransition{
            static_cast<float>(action_reward),
            true,
            board_capacity_violation
        };
}

// ============================================================
// CONSTRUTOR E DESTRUTOR
// ============================================================

TFTEngine::TFTEngine(
    std::uint64_t seed,
    std::string catalog_path
)
    : impl_(
        std::make_unique<Impl>(seed, catalog_path)
    ) {
}

TFTEngine::~TFTEngine() = default;

TFTEngine::TFTEngine(TFTEngine&&) noexcept = default;

TFTEngine& TFTEngine::operator=(TFTEngine&&) noexcept = default;

// ============================================================
// RESET
// ============================================================

ResetResult TFTEngine::reset(
    std::optional<std::uint64_t> seed
) {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    if (seed.has_value()) {
        impl_->seed = *seed;
    }

    ++impl_->episode_id;

    impl_->round = 0;
    impl_->stage = 1;
    impl_->done = false;
    impl_->winner_id = std::nullopt;
    impl_->ranking.clear();
    impl_->previous_matchups.clear();
    impl_->matchmaking_rng.seed(impl_->seed + impl_->episode_id);

    // Devolve as ofertas antes de restaurar o pool.
    for (auto& player_env : impl_->player_envs) {
        auto& shop = player_env.shop;
        if (shop) {
            shop->return_current_shop();
        }

        shop.reset();
    }

    impl_->pool->reset();

    impl_->unit_factory =
        std::make_unique<UnitInstanceFactory>(
            *impl_->catalog,
            impl_->seed
        );

    impl_->initialize_players();
    for (auto& player_env : impl_->player_envs) player_env.previous_board_power = 0.0;
    for (auto& player_env : impl_->player_envs) player_env.previous_synergy_score = 0.0;
    for (auto& player_env : impl_->player_envs) player_env.previous_positioning_score = 0.0;
    for (auto& player_env : impl_->player_envs) player_env.previous_reward_level = 1;
    for (auto& player_env : impl_->player_envs) player_env.last_combat_reward = 0.0;
    for (auto& player_env : impl_->player_envs) player_env.round_reward_total = 0.0;
    for (auto& player_env : impl_->player_envs) player_env.total_reward = 0.0;
    for (auto& player_env : impl_->player_envs) player_env.placement_reward_given = false;

    ResetResult result{};

    result.observations = impl_->build_observations();
    result.observation_dim = impl_->observation_dim();
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) result.action_masks[i] = impl_->player_envs[i].action_masks;
    result.episode_id = impl_->episode_id;

    return result;
}

// ============================================================
// STEP
// ============================================================

StepResult TFTEngine::step(
    const std::array<PlayerAction, kPlayersPerLobby>& actions,
    bool timer_enabled,
    bool timer_expired
) {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    if (impl_->done) {
        throw std::runtime_error(
            "A partida ja foi encerrada. Execute reset()."
        );
    }

    // No treinamento, um jogador só encerra suas decisões após 10 ações.
    // PASS conta como ação, mas não encerra a preparação antecipadamente.
    // No viewer, o temporizador controla a fase e o limite de ações fica desativado.
    auto effective_actions = actions;
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        if (impl_->round_finished[i]) {
            effective_actions[i].values = {6, 0, 0, 0, 0, 0};
        }
    }

    // Preflight em duas fases: valida limites e disponibilidade semântica
    // de todas as ações antes de executar a primeira. Se qualquer ação for
    // impossível, o lote falha sem alterar ouro, unidades ou posições.
    for (const auto& action : effective_actions) {
        impl_->validate_action(action);
    }
    for (std::size_t i = 0; i < actions.size(); ++i) {
        impl_->validate_action_against_masks(i, effective_actions[i]);
    }

    // ========================================================
    // AÇÕES DE LOJA, ECONOMIA E MOVIMENTAÇÃO
    // ========================================================

    std::array<float, kPlayersPerLobby> round_rewards{};
    std::array<float, kPlayersPerLobby> action_rewards{};
    std::array<float, kPlayersPerLobby> combat_rewards{};
    std::array<float, kPlayersPerLobby> placement_rewards{};
    std::array<bool, kPlayersPerLobby> capacity_violations{};
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        const auto transition = impl_->player_envs[i].step(*impl_, i, effective_actions[i]);
        if (!transition.acted) {
            continue;
        }
        action_rewards[i] = transition.action_reward;
        capacity_violations[i] = transition.board_capacity_violation;
        round_rewards[i] += transition.action_reward;
        impl_->player_envs[i].round_reward_total = round_rewards[i];
        impl_->player_envs[i].total_reward += round_rewards[i];
        impl_->sync_player_economy(i);
        impl_->refresh_masks(i);
        if (!timer_enabled) {
            impl_->mark_round_completion(i);
        }
    }

    // ========================================================
    // RESOLUÇÃO CONDICIONAL DA RODADA
    // ========================================================

    std::vector<std::string> round_events;
    bool round_resolved = false;

    // In viewer/runtime mode the wall-clock timer owns the preparation phase.
    // PASS does not resolve combat early; only the timer ends this phase.
    if (timer_enabled && timer_expired) {
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (impl_->player_envs[i].info.alive) {
                impl_->round_finished[i] = true;
            }
        }
    }

    const bool preparation_complete = timer_enabled
        ? timer_expired
        : impl_->all_alive_players_finished_round();

    if (preparation_complete) {
        round_resolved = true;

        // Primeiro resolve o PvP quando esta rodada possui combate entre
        // jogadores. PvE/carrossel não concedem bônus de vitória nem alteram
        // sequências; eles avançam a economia, mas não simulamos seus drops.
        const auto rewards_before_combat = round_rewards;
        const auto current_round_number = impl_->round + 1;
        if (is_pvp_round(current_round_number)) {
            impl_->resolve_combats(round_events, round_rewards, combat_rewards);
        } else {
            for (auto& player_env : impl_->player_envs) {
                player_env.info.opponent_id.reset();
            }
            round_events.emplace_back(
                "ROUND_NO_PVP: fase de abertura/PvE/carrossel; "
                "nenhum bônus PvP ou streak foi aplicado."
            );
        }

        // A renda/XP calculada é para a próxima preparação; o estado começa
        // em round=0 (1-1), então a próxima rodada é current_round_number + 1.
        const auto next_round_number =
            static_cast<std::int32_t>(current_round_number + 1);

        if (!impl_->done && impl_->alive_players > 1) {
            for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
                auto& player_env = impl_->player_envs[i];
                if (!player_env.info.alive || player_env.info.hp <= 0.0f) {
                    continue;
                }

                (void)impl_->economy_engine.resolve_round(
                    player_env.economy,
                    next_round_number
                );
                impl_->sync_player_economy(i);

                // A loja é renovada para o próximo turno após atualizar o nível.
                player_env.shop->roll(player_env.economy.level);
                impl_->refresh_masks(i);
            }
        }

        // TFTLobby aplica a recompensa de colocação uma única vez assim que
        // a posição do jogador é conhecida (inclusive para eliminados).
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (impl_->player_envs[i].placement_reward_given ||
                !impl_->player_envs[i].info.placement.has_value()) {
                continue;
            }
            const auto placement = *impl_->player_envs[i].info.placement;
            if (placement < 1 ||
                placement > static_cast<std::int32_t>(kPlayersPerLobby)) {
                throw std::logic_error("Colocacao invalida ao calcular recompensa terminal.");
            }
            const double placement_reward = 1.0 - 2.0 *
                (static_cast<double>(placement - 1) /
                 static_cast<double>(kPlayersPerLobby - 1));
            placement_rewards[i] = static_cast<float>(placement_reward);
            round_rewards[i] += placement_rewards[i];
            impl_->player_envs[i].placement_reward_given = true;
            round_events.emplace_back(
                "PLACEMENT_REWARD: jogador " + std::to_string(i) +
                ", colocacao=" + std::to_string(placement) +
                ", recompensa=" + std::to_string(placement_reward));
        }

        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            // Python clamps the per-player action transition inside env.step(),
            // then TFTLobby adds combat and placement rewards without clamping
            // that combined value a second time.
            impl_->player_envs[i].round_reward_total = round_rewards[i];
            impl_->player_envs[i].total_reward += round_rewards[i] - rewards_before_combat[i];
            if (impl_->player_envs[i].info.alive) {
                impl_->update_strategy(i);
            }
        }

        // O bônus de vitória já foi creditado no ouro pelo combate.
        // Limpa apenas o acumulador do relatório desta rodada.
        for (auto& player_env : impl_->player_envs) {
        auto& economy = player_env.economy;
            economy.round_win_gold = 0;
        }

        // A lobby Python só avança se ainda houver pelo menos dois
        // jogadores vivos. A partida encerrada mantém a rodada final.
        if (!impl_->done && impl_->alive_players > 1) {
            ++impl_->round;

            const std::uint32_t public_round =
                impl_->round + 1;

            impl_->stage = stage_for_round(public_round);

            // Start a fresh anti-loop local history for the new preparation,
            // while retaining only signatures from the previous four rounds.
            for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
                auto& player_env = impl_->player_envs[i];
                player_env.anti_loop.begin_round(public_round);
                if (player_env.info.alive) {
                    impl_->register_position_state(i);
                    // The old-round masks were generated before begin_round;
                    // rebuild them now so the first next-round action sees the
                    // cleared local history and the fresh visited-state window.
                    impl_->refresh_masks(i);
                }
            }
            impl_->reset_round_completion();
        }
    }

    // ========================================================
    // RESULTADO
    // ========================================================

    StepResult result{};

    result.observations = impl_->build_observations();
    result.observation_dim = impl_->observation_dim();

    result.rewards = round_rewards;
    result.action_rewards = action_rewards;
    result.combat_rewards = combat_rewards;
    result.placement_rewards = placement_rewards;
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        result.dones[i] = (!impl_->player_envs[i].info.alive || impl_->done) ? 1 : 0;
    }

    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) result.action_masks[i] = impl_->player_envs[i].action_masks;
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) result.players[i] = impl_->player_envs[i].info;

    result.lobby_done = impl_->done;
    result.episode_id = impl_->episode_id;
    result.round = impl_->round + 1;
    result.stage = impl_->stage;
    result.alive_players = impl_->alive_players;

    result.events.emplace_back(
        "Acoes de loja, economia, venda e movimentacao "
        "executadas pelo TFTEngine."
    );
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        if (capacity_violations[i]) {
            result.events.emplace_back(
                "RULE_VIOLATION: jogador " + std::to_string(i) +
                " tentou exceder a capacidade do nivel; movimento recusado."
            );
        }
    }

    if (!round_resolved) {
        result.events.emplace_back(
            "ROUND_WAITING: fase de preparacao ainda ativa; "
            "aguardando o temporizador ou PASS de todos os jogadores vivos."
        );
    } else {
        result.events.emplace_back("ROUND_RESOLVED");
    }
    result.events.insert(
        result.events.end(),
        round_events.begin(),
        round_events.end()
    );

    return result;
}

// ============================================================
// MÁSCARAS DE AÇÃO
// ============================================================

std::array<PlayerActionMasks, kPlayersPerLobby>
TFTEngine::get_action_masks() const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    std::array<PlayerActionMasks, kPlayersPerLobby> result{};
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) result[i] = impl_->player_envs[i].action_masks;
    return result;
}

AuditSnapshot TFTEngine::get_audit_snapshot() const {
    if (!impl_) {
        throw std::runtime_error("TFTEngine nao possui estado interno.");
    }
    impl_->ensure_open();

    AuditSnapshot snapshot{};
    snapshot.round = impl_->round + 1;
    snapshot.stage = impl_->stage;
    snapshot.finished = impl_->done;

    const auto describe_unit = [this](const UnitInstance* unit) {
        AuditUnitSnapshot result{};
        if (!unit) return result;
        result.occupied = true;
        result.champion_id = unit->champion_id;
        result.uuid = unit->uuid;
        result.star = unit->star;
        const auto* definition = impl_->catalog->find_by_id(
            unit->champion_internal_id
        );
        result.cost = definition ? definition->cost : 0;
        return result;
    };

    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        const auto& source = impl_->player_envs[i];
        auto& target = snapshot.players[i];
        target.player_id = static_cast<std::int32_t>(i);
        target.gold = source.economy.gold;
        target.level = source.economy.level;
        target.xp = source.economy.xp;
        target.win_streak = source.economy.win_streak;
        target.loss_streak = source.economy.loss_streak;
        target.round_gold = source.economy.round_gold;
        target.round_base_gold = source.economy.round_base_gold;
        target.round_interest = source.economy.round_interest;
        target.round_streak_gold = source.economy.round_streak_gold;
        target.round_win_gold = source.economy.last_round_win_gold;
        target.masks = source.action_masks;

        for (std::size_t slot = 0; slot < kBoardSlots; ++slot)
            target.board[slot] = describe_unit(
                source.board[slot] ? &*source.board[slot] : nullptr
            );
        for (std::size_t slot = 0; slot < kBenchSlots; ++slot)
            target.bench[slot] = describe_unit(
                source.bench[slot] ? &*source.bench[slot] : nullptr
            );
        for (std::size_t slot = 0; slot < kShopSlots; ++slot)
            target.shop[slot] = describe_unit(source.shop->get_unit(
                static_cast<std::int32_t>(slot)
            ));
    }
    return snapshot;
}

bool TFTEngine::set_unit_for_testing(
    std::int32_t player_id,
    bool on_board,
    std::int32_t slot,
    const std::string& champion_api_name,
    std::int32_t star
) {
    if (!impl_) {
        throw std::runtime_error("TFTEngine nao possui estado interno.");
    }
    impl_->ensure_open();
    if (player_id < 0 ||
        static_cast<std::size_t>(player_id) >= kPlayersPerLobby ||
        star < 1 || star > 3) {
        return false;
    }

    const auto player_index = static_cast<std::size_t>(player_id);
    const auto* definition =
        impl_->catalog->find_by_api_name(champion_api_name);
    if (!definition) return false;

    auto unit = impl_->unit_factory->create(definition->internal_id);
    unit.star = star;

    if (on_board) {
        if (slot < 0 || static_cast<std::size_t>(slot) >= kBoardSlots)
            return false;
        impl_->player_envs[player_index].board[static_cast<std::size_t>(slot)] =
            std::move(unit);
        impl_->player_envs[player_index].board_move_age[static_cast<std::size_t>(slot)] = kActionMemoryHorizon;
    } else {
        if (slot < 0 || static_cast<std::size_t>(slot) >= kBenchSlots)
            return false;
        impl_->player_envs[player_index].bench[static_cast<std::size_t>(slot)] =
            std::move(unit);
    }

    impl_->register_position_state(player_index);
    // Keep derived strategy/composition data coherent with test-only fixture
    // mutations. SELL reward reads the current core-unit set before transition.
    impl_->update_strategy(player_index);
    impl_->refresh_masks(player_index);
    return true;
}

bool TFTEngine::set_player_economy_for_testing(
    std::int32_t player_id, std::int32_t gold,
    std::int32_t level, std::int32_t xp
) {
    if (!impl_) throw std::runtime_error("TFTEngine nao possui estado interno.");
    impl_->ensure_open();
    if (player_id < 0 || static_cast<std::size_t>(player_id) >= kPlayersPerLobby ||
        gold < 0 || level < 1 || level > EconomyEngine::MAX_LEVEL || xp < 0)
        return false;
    auto& player = impl_->player_envs[static_cast<std::size_t>(player_id)];
    player.economy.gold = gold;
    player.economy.level = level;
    player.economy.xp = xp;
    impl_->refresh_masks(static_cast<std::size_t>(player_id));
    return true;
}

bool TFTEngine::set_shop_offer_for_testing(
    std::int32_t player_id, std::int32_t slot,
    const std::string& champion_api_name
) {
    if (!impl_) throw std::runtime_error("TFTEngine nao possui estado interno.");
    impl_->ensure_open();
    if (player_id < 0 || static_cast<std::size_t>(player_id) >= kPlayersPerLobby ||
        slot < 0 || static_cast<std::size_t>(slot) >= kShopSlots)
        return false;
    const auto* definition = impl_->catalog->find_by_api_name(champion_api_name);
    if (!definition) return false;
    auto& player = impl_->player_envs[static_cast<std::size_t>(player_id)];
    auto unit = impl_->unit_factory->create(definition->internal_id);
    if (!player.shop->set_offer_for_testing(slot, std::move(unit))) return false;
    impl_->refresh_masks(static_cast<std::size_t>(player_id));
    return true;
}

bool TFTEngine::set_next_shop_roll_for_testing(
    std::int32_t player_id,
    const std::vector<std::string>& champion_api_names
) {
    if (!impl_) throw std::runtime_error("TFTEngine nao possui estado interno.");
    impl_->ensure_open();
    if (player_id < 0 || static_cast<std::size_t>(player_id) >= kPlayersPerLobby ||
        champion_api_names.size() != kShopSlots)
        return false;
    std::vector<std::int32_t> ids;
    ids.reserve(kShopSlots);
    for (const auto& name : champion_api_names) {
        const auto* definition = impl_->catalog->find_by_api_name(name);
        if (!definition) return false;
        ids.push_back(definition->internal_id);
    }
    auto& player = impl_->player_envs[static_cast<std::size_t>(player_id)];
    return player.shop->set_next_roll_for_testing(ids);
}

bool TFTEngine::set_player_alive_for_testing(
    std::int32_t player_id,
    bool alive
) {
    if (!impl_) {
        throw std::runtime_error("TFTEngine nao possui estado interno.");
    }
    impl_->ensure_open();
    if (player_id < 0 ||
        static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        return false;
    }

    const auto index = static_cast<std::size_t>(player_id);
    auto& player = impl_->player_envs[index].info;
    player.alive = alive;
    player.eliminated = !alive;
    if (!alive) {
        player.hp = 0.0f;
        player.placement.reset();
        impl_->round_finished[index] = true;
    } else if (player.hp <= 0.0f) {
        player.hp = 100.0f;
    }

    impl_->alive_players = 0;
    for (const auto& env : impl_->player_envs) {
            const auto& candidate = env.info;
        if (candidate.alive) ++impl_->alive_players;
    }
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        impl_->refresh_masks(i);
    }
    return true;
}

bool TFTEngine::set_shop_locked(
    std::int32_t player_id,
    bool locked
) {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    if (player_id < 0 ||
        static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        throw std::out_of_range(
            "player_id invalido ao alterar bloqueio da loja."
        );
    }

    return impl_->player_envs[
        static_cast<std::size_t>(player_id)
    ].shop->set_locked(locked);
}

bool TFTEngine::toggle_shop_lock(
    std::int32_t player_id
) {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    if (player_id < 0 ||
        static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        throw std::out_of_range(
            "player_id invalido ao alternar bloqueio da loja."
        );
    }

    return impl_->player_envs[
        static_cast<std::size_t>(player_id)
    ].shop->toggle_lock();
}

bool TFTEngine::is_shop_locked(
    std::int32_t player_id
) const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    if (player_id < 0 ||
        static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        throw std::out_of_range(
            "player_id invalido ao consultar bloqueio da loja."
        );
    }

    return impl_->player_envs[
        static_cast<std::size_t>(player_id)
    ].shop->is_locked();
}

// ============================================================
// OBSERVAÇÕES
// ============================================================

std::vector<float> TFTEngine::get_observations() const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    return impl_->build_observations();
}

// ============================================================
// ESTRATÉGIAS
// ============================================================

std::array<std::vector<StrategyInfo>, kPlayersPerLobby>
TFTEngine::get_strategies() const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    std::array<std::vector<StrategyInfo>, kPlayersPerLobby> result{};
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) result[i] = impl_->player_envs[i].strategy;
    return result;
}

RewardState TFTEngine::get_reward_state(std::int32_t player_id) const {
    if (!impl_ || player_id < 0 ||
        player_id >= static_cast<std::int32_t>(kPlayersPerLobby)) {
        throw std::out_of_range("player_id fora do intervalo.");
    }
    impl_->ensure_open();
    const auto i = static_cast<std::size_t>(player_id);
    RewardState state{};
    state.previous_board_power = impl_->player_envs[i].previous_board_power;
    state.previous_positioning_score = impl_->player_envs[i].previous_positioning_score;
    state.previous_synergy_score = impl_->player_envs[i].previous_synergy_score;
    state.previous_level = impl_->player_envs[i].previous_reward_level;
    // RewardManager.py declares previous_gold but does not update it.
    // Keep the same observable value until the Python contract changes.
    state.previous_gold = 0;
    state.last_combat_reward = impl_->player_envs[i].last_combat_reward;
    state.round_reward = impl_->player_envs[i].round_reward_total;
    state.total_reward = impl_->player_envs[i].total_reward;
    return state;
}

// ============================================================
// MÉTRICAS ANTI-LOOP
// ============================================================

double TFTEngine::get_unit_comp_score(
    std::int32_t player_id,
    const std::string& champion_api_name,
    std::int32_t star
) const {
    if (!impl_ || player_id < 0 ||
        player_id >= static_cast<std::int32_t>(kPlayersPerLobby)) {
        throw std::out_of_range("player_id fora do intervalo.");
    }
    impl_->ensure_open();
    const auto* def = impl_->catalog->find_by_api_name(champion_api_name);
    if (!def || star < 1 || star > 3) return 0.0;
    const auto& list =
        impl_->player_envs[static_cast<std::size_t>(player_id)].strategy;
    if (list.empty()) return 0.0;
    return unit_composition_score(list.back(), *def, star);
}
bool TFTEngine::is_core_unit(std::int32_t player_id, const std::string& champion_api_name) const {
    if (!impl_ || player_id < 0 || player_id >= static_cast<std::int32_t>(kPlayersPerLobby)) return false; impl_->ensure_open(); const auto* def = impl_->catalog->find_by_api_name(champion_api_name); if (!def) return false;
    const auto& list = impl_->player_envs[static_cast<std::size_t>(player_id)].strategy; return !list.empty() && std::find(list.back().core_unit_ids.begin(), list.back().core_unit_ids.end(), def->internal_id) != list.back().core_unit_ids.end();
}
bool TFTEngine::is_core_trait(std::int32_t player_id, const std::string& trait) const {
    if (!impl_ || player_id < 0 || player_id >= static_cast<std::int32_t>(kPlayersPerLobby)) return false; impl_->ensure_open(); const auto& list = impl_->player_envs[static_cast<std::size_t>(player_id)].strategy;
    return !list.empty() && std::find(list.back().core_traits.begin(), list.back().core_traits.end(), trait) != list.back().core_traits.end();
}

std::array<AntiLoopMetrics, kPlayersPerLobby>
TFTEngine::get_anti_loop_metrics() const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    std::array<AntiLoopMetrics, kPlayersPerLobby> result{};

    for (std::size_t i = 0;
         i < kPlayersPerLobby;
         ++i) {
        const auto metrics =
            impl_->player_envs[i].anti_loop.get_metrics();

        result[i].execution_attempts =
            metrics.execution_attempts;
        result[i].execution_blocks =
            metrics.execution_blocks;
        result[i].blocked_reverse =
            metrics.blocked_reverse;
        result[i].blocked_oscillation =
            metrics.blocked_oscillation;
        result[i].blocked_explicit =
            metrics.blocked_explicit;
        result[i].blocked_bench_board_loop =
            metrics.blocked_bench_board_loop;
        result[i].blocked_cycle =
            metrics.blocked_cycle;
        result[i].board_moves_executed =
            metrics.board_moves_executed;
        result[i].bench_to_board_executed =
            metrics.bench_to_board_executed;

        result[i].mask_board_move_candidates =
            metrics.mask.board_move_candidates;
        result[i].mask_board_move_valid =
            metrics.mask.board_move_valid;
        result[i].mask_board_move_blocked_anti_loop =
            metrics.mask.board_move_blocked_anti_loop;
        result[i].mask_board_move_blocked_seen_state =
            metrics.mask.board_move_blocked_seen_state;
        result[i].mask_bench_move_candidates =
            metrics.mask.bench_move_candidates;
        result[i].mask_bench_move_valid =
            metrics.mask.bench_move_valid;
        result[i].mask_bench_move_blocked_anti_loop =
            metrics.mask.bench_move_blocked_anti_loop;
        result[i].mask_bench_move_blocked_seen_state =
            metrics.mask.bench_move_blocked_seen_state;
        result[i].mask_blocked_reverse = metrics.mask.blocked_reverse;
        result[i].mask_blocked_oscillation = metrics.mask.blocked_oscillation;
        result[i].mask_blocked_explicit = metrics.mask.blocked_explicit;
        result[i].mask_blocked_bench_board_loop =
            metrics.mask.blocked_bench_board_loop;
        result[i].mask_blocked_cycle = metrics.mask.blocked_cycle;
    }

    return result;
}

// ============================================================
// ESTADO PÚBLICO
// ============================================================

PublicState TFTEngine::get_public_state() const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    PublicState state{};

    state.stage = impl_->stage;
    state.round = impl_->round + 1;
    state.round_index = impl_->round;
    state.finished = impl_->done;
    state.winner_id = impl_->winner_id;
    state.ranking = impl_->ranking;

    state.players.reserve(kPlayersPerLobby);

    state.alive_players.reserve(
        static_cast<std::size_t>(impl_->alive_players)
    );

    for (const auto& env : impl_->player_envs) {
        const auto& player = env.info;
        state.players.push_back(player);

        if (player.alive) {
            state.alive_players.push_back(player.player_id);
        }
    }

    return state;
}

// ============================================================
// DIMENSÃO DAS OBSERVAÇÕES
// ============================================================

std::size_t TFTEngine::observation_dim() const noexcept {
    return impl_ ? impl_->observation_dim() : 0;
}

// ============================================================
// IDENTIFICADOR DO EPISÓDIO
// ============================================================

std::uint64_t TFTEngine::episode_id() const noexcept {
    return impl_ ? impl_->episode_id : 0;
}

// ============================================================
// RODADA
// ============================================================

std::uint32_t TFTEngine::round() const noexcept {
    return impl_ ? impl_->round : 0;
}

// ============================================================
// ESTÁGIO
// ============================================================

std::uint32_t TFTEngine::stage() const noexcept {
    return impl_ ? impl_->stage : 1;
}

// ============================================================
// JOGADORES VIVOS
// ============================================================

std::int32_t TFTEngine::alive_players() const noexcept {
    return impl_ ? impl_->alive_players : 0;
}

// ============================================================
// ENCERRAMENTO
// ============================================================

bool TFTEngine::is_done() const noexcept {
    return !impl_ || impl_->done || impl_->closed;
}

// ============================================================
// CONSULTAS AO POOL
// ============================================================

std::int32_t TFTEngine::pool_available(
    std::int32_t champion_internal_id
) const {
    if (!impl_ || !impl_->pool) {
        throw std::runtime_error(
            "UnitPool indisponivel."
        );
    }

    return impl_->pool->available(champion_internal_id);
}

std::int32_t TFTEngine::pool_initial_count(
    std::int32_t champion_internal_id
) const {
    if (!impl_ || !impl_->pool) {
        throw std::runtime_error(
            "UnitPool indisponivel."
        );
    }

    return impl_->pool->initial_count(champion_internal_id);
}

std::int64_t TFTEngine::pool_total_available() const {
    if (!impl_ || !impl_->pool) {
        throw std::runtime_error(
            "UnitPool indisponivel."
        );
    }

    return impl_->pool->total_available();
}

// ============================================================
// FECHAMENTO
// ============================================================

void TFTEngine::close() noexcept {
    if (!impl_) {
        return;
    }

    impl_->closed = true;
}

} // namespace tft
