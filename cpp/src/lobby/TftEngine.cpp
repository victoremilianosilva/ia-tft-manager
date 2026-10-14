
#include "lobby/TftEngine.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <map>
#include <unordered_map>
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

constexpr std::size_t kObservationDim = 8;
constexpr std::uint32_t kRoundsPerStage = 7;

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

void write_observation(
    const PlayerInfo& player,
    std::uint32_t round,
    float* output
) {
    output[0] = player.hp;
    output[1] = static_cast<float>(player.gold);
    output[2] = static_cast<float>(player.level);
    output[3] = static_cast<float>(player.xp);
    output[4] = player.alive ? 1.0f : 0.0f;
    output[5] = static_cast<float>(player.wins);
    output[6] = static_cast<float>(player.losses);
    output[7] = static_cast<float>(round);
}

} // namespace

// ============================================================
// IMPLEMENTAÇÃO INTERNA
// ============================================================

struct TFTEngine::Impl {
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

    std::array<
        std::unique_ptr<ShopEngine>,
        kPlayersPerLobby
    > shops{};

    std::array<
        std::array<std::optional<UnitInstance>, kBenchSlots>,
        kPlayersPerLobby
    > benches{};

    std::array<
        std::array<std::optional<UnitInstance>, kBoardSlots>,
        kPlayersPerLobby
    > boards{};

    // Um histórico anti-loop independente para cada jogador.
    std::array<
        decision::AntiLoopEngine,
        kPlayersPerLobby
    > anti_loop_engines{};

    decision::ActionMaskEngine action_mask_engine;

    std::int32_t alive_players{
        static_cast<std::int32_t>(kPlayersPerLobby)
    };

    bool done{false};
    bool closed{false};

    // O PASS encerra a fase de preparação daquele jogador.
    // A rodada só é resolvida quando todos os jogadores vivos terminaram,
    // ou quando atingem o limite de ações da rodada (igual à lobby Python).
    static constexpr std::uint32_t kMaxActionsPerRound = 20;
    std::array<std::uint32_t, kPlayersPerLobby> round_actions{};
    std::array<bool, kPlayersPerLobby> round_finished{};

    std::array<PlayerInfo, kPlayersPerLobby> players{};
    std::array<PlayerActionMasks, kPlayersPerLobby> masks{};

    std::array<std::vector<StrategyInfo>, kPlayersPerLobby>
        strategies{};

    std::array<AntiLoopMetrics, kPlayersPerLobby>
        anti_loop_metrics{};

    // Economia independente por jogador.
    EconomyEngine economy_engine;
    CombatEngine combat_engine;
    std::array<PlayerEconomy, kPlayersPerLobby> economies{};

    // Estado incremental do RewardManager Python.
    std::array<double, kPlayersPerLobby> previous_board_power{};
    std::array<double, kPlayersPerLobby> previous_synergy_score{};
    std::array<double, kPlayersPerLobby> previous_positioning_score{};
    std::array<std::int32_t, kPlayersPerLobby> previous_reward_level{};
    std::array<double, kPlayersPerLobby> last_combat_reward{};
    std::array<double, kPlayersPerLobby> round_reward_total{};
    std::array<double, kPlayersPerLobby> total_reward{};

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

        state.is_alive = players[player_index].alive;

        const auto& economy = economies[player_index];

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
                snapshot(boards[player_index][slot]);
        }

        for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
            state.bench[slot] =
                snapshot(benches[player_index][slot]);
        }

        for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
            const auto* offer =
                shops[player_index]->get_unit(
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
            anti_loop_engines[player_index]
                .make_board_signature(state);

        (void)anti_loop_engines[player_index]
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
                anti_loop_engines[player_index]
            );

        auto& current = masks[player_index];
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
        round_actions.fill(0);
        round_finished.fill(false);
        previous_matchups.clear();
        matchmaking_rng.seed(seed + episode_id);

        for (std::size_t i = 0;
             i < kPlayersPerLobby;
             ++i) {
            PlayerInfo player{};

            player.player_id =
                static_cast<std::int32_t>(i);

            player.hp = 100.0f;

            economy_engine.reset(economies[i]);

            player.gold = economies[i].gold;
            player.level = economies[i].level;
            player.xp = economies[i].xp;

            player.alive = true;
            player.eliminated = false;

            player.wins = 0;
            player.losses = 0;

            player.placement = std::nullopt;
            player.opponent_id = std::nullopt;
            player.damage_taken = 0.0f;

            players[i] = player;

            benches[i].fill(std::nullopt);
            boards[i].fill(std::nullopt);

            // Impede que o histórico de uma partida anterior
            // interfira no novo episódio.
            // Limpa o histórico da partida, preservando as métricas acumuladas.
            anti_loop_engines[i].reset();

            shops[i] = std::make_unique<ShopEngine>(
                *pool,
                *unit_factory,
                seed + static_cast<std::uint64_t>(i)
                    + episode_id
            );

            shops[i]->roll(player.level);

            masks[i] = make_default_masks();

            strategies[i].clear();
            strategies[i].push_back(StrategyInfo{});

            anti_loop_metrics[i] = AntiLoopMetrics{};

            register_position_state(i);
            refresh_masks(i);
        }
    }

    // ========================================================
    // OBSERVAÇÕES
    // ========================================================

    std::vector<float> build_observations() const {
        std::vector<float> observations(
            kPlayersPerLobby * kObservationDim,
            0.0f
        );

        for (std::size_t i = 0;
             i < kPlayersPerLobby;
             ++i) {
            write_observation(
                players[i],
                round + 1,
                observations.data() + i * kObservationDim
            );
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
        const auto& player_masks = masks[player_index];

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
        double power = 0.0;
        for (const auto& unit : boards[player_index]) {
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            const auto& s = def->stats;
            const double raw = std::max(0.0, s.max_hp) * 0.02
                + std::max(0.0, s.attack_damage) * 0.20
                + std::max(0.0, s.attack_speed) * 2.0
                + std::max(0.0, s.armor) * 0.05
                + std::max(0.0, s.magic_resist) * 0.05
                + std::max(0.0, s.attack_range);
            power += raw * static_cast<double>(std::max(1, unit->star));
        }
        return power;
    }

    double synergy_score(std::size_t player_index) const {
        std::unordered_map<std::string, int> counts;
        for (const auto& unit : boards[player_index]) {
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            for (const auto& trait : def->traits) ++counts[trait];
        }
        double score = 0.0;
        for (const auto& [trait, count] : counts) {
            (void)trait;
            if (count >= 2) score += 1.0;
            if (count >= 4) score += 1.0;
            if (count >= 6) score += 1.0;
        }
        return score;
    }

    double positioning_score(std::size_t player_index) const {
        double score = 0.0;
        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            const auto& unit = boards[player_index][slot];
            if (!unit) continue;
            const auto* def = catalog->find_by_id(unit->champion_internal_id);
            if (!def) continue;
            const auto row = static_cast<int>(slot / 7);
            const auto& profile = def->combat_profile;
            const bool frontline = profile.frontline || profile.is_tank || profile.is_fighter;
            const bool backline = profile.backline || profile.is_carry || profile.is_support;
            // Tabuleiro 4x7: linhas 0-1 são frontline; 2-3 backline.
            if (frontline) score += row <= 1 ? 1.0 : -0.5;
            else if (backline) score += row >= 2 ? 1.0 : -0.5;
            if (profile.is_assassin && row <= 1) score -= 0.25;
        }
        return score;
    }

    double combat_reward(bool won, int damage_dealt, int damage_taken,
                         int enemy_alive, int own_alive) const {
        double reward = won ? 2.0 : -2.0;
        if (damage_dealt > 0)
            reward += std::min(std::tanh(static_cast<double>(damage_dealt) / 10.0), 1.0);
        if (own_alive > 0)
            reward += std::min(static_cast<double>(own_alive) * 0.05, 0.25);
        if (enemy_alive > 0)
            reward -= std::min(static_cast<double>(enemy_alive) * 0.05, 0.25);
        if (damage_taken > 0)
            reward -= std::min(std::tanh(static_cast<double>(damage_taken) / 15.0), 0.75);
        return reward;
    }

    void update_strategy(std::size_t i) {
        auto& list = strategies[i];
        StrategyInfo info = list.empty() ? StrategyInfo{} : list.back();
        const auto& player = players[i];
        const auto& economy = economies[i];
        const double power = board_power(i);
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

        if (chosen != info.strategy) {
            info.previous_strategy = info.strategy;
            info.strategy_age = 0;
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
        if (list.empty()) list.push_back(info);
        else list.back() = info;
    }

    double state_reward(std::size_t i, double action_reward) {
        const double power = board_power(i);
        const double synergy = synergy_score(i);
        const double positioning = positioning_score(i);
        double reward = action_reward;

        const double power_delta = power - previous_board_power[i];
        previous_board_power[i] = power;
        if (std::abs(power_delta) >= 1e-6) reward += std::tanh(power_delta / 10.0);

        const double synergy_delta = synergy - previous_synergy_score[i];
        previous_synergy_score[i] = synergy;
        reward += std::tanh(synergy_delta);

        const double position_delta = positioning - previous_positioning_score[i];
        previous_positioning_score[i] = positioning;
        reward += std::tanh(position_delta) * 0.5;

        const auto level = economies[i].level;
        if (level > previous_reward_level[i]) {
            reward += std::min((level - previous_reward_level[i]) * 0.5, 1.5);
        }
        previous_reward_level[i] = level;

        const auto gold = economies[i].gold;
        for (int threshold = 10; threshold <= 50; threshold += 10)
            if (gold >= threshold) reward += 0.05;
        if (players[i].hp <= 15.0f) reward -= 0.15;
        else if (players[i].hp <= 30.0f) reward -= 0.05;

        if (economies[i].win_streak >= 2)
            reward += std::min(economies[i].win_streak * 0.03, 0.15);
        if (economies[i].loss_streak >= 2)
            reward += std::min(economies[i].loss_streak * 0.02, 0.10);

        int occupied = 0;
        for (const auto& unit : boards[i]) if (unit) ++occupied;
        reward += static_cast<double>(occupied) / static_cast<double>(kBoardSlots) * 0.15;
        return reward;
    }

    void sync_player_economy(std::size_t player_index) {
        if (player_index >= kPlayersPerLobby) {
            throw std::out_of_range(
                "Indice de jogador invalido ao sincronizar economia."
            );
        }

        const auto& economy = economies[player_index];
        auto& player = players[player_index];

        player.gold = economy.gold;
        player.level = economy.level;
        player.xp = economy.xp;
    }

    bool all_alive_players_finished_round() const {
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (players[i].alive && !round_finished[i]) {
                return false;
            }
        }
        return true;
    }

    void mark_round_completion(std::size_t player_index, std::int32_t action_type) {
        if (!players[player_index].alive) {
            return;
        }

        ++round_actions[player_index];
        if (action_type == 6 ||
            round_actions[player_index] >= kMaxActionsPerRound) {
            round_finished[player_index] = true;
        }
    }

    void reset_round_completion() {
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (players[i].alive) {
                round_actions[i] = 0;
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
        CombatTeam& output
    ) const {
        output.team = team;
        output.player_id = static_cast<std::int32_t>(player_index);
        output.player_hp = players[player_index].hp;

        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            if (!boards[player_index][slot]) {
                continue;
            }

            const auto& instance = *boards[player_index][slot];
            const auto* definition =
                catalog->find_by_id(instance.champion_internal_id);
            if (!definition) {
                continue;
            }

            const auto& stats = definition->stats;
            const auto& profile = definition->combat_profile;

            CombatUnit unit{};
            unit.id = static_cast<int>(player_index * 100 + slot);
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
                unit.position.y = 3 - unit.position.y;
            }
            unit.source_board_position = static_cast<int>(slot);

            const double max_hp =
                profile.max_hp > 0.0 ? profile.max_hp : stats.max_hp;
            unit.max_hp = static_cast<float>(max_hp > 0.0 ? max_hp : 100.0);
            unit.hp = unit.max_hp;

            const double attack_damage =
                profile.attack_damage > 0.0
                    ? profile.attack_damage
                    : stats.attack_damage;
            unit.attack_damage = static_cast<float>(
                std::max(0.0, attack_damage));

            const double attack_speed =
                profile.attack_speed > 0.0
                    ? profile.attack_speed
                    : stats.attack_speed;
            unit.attack_speed = static_cast<float>(
                attack_speed > 0.0 ? attack_speed : 1.0);

            const double attack_range =
                profile.attack_range > 0.0
                    ? profile.attack_range
                    : stats.attack_range;
            unit.attack_range = static_cast<float>(
                attack_range > 0.0 ? attack_range : 1.0);

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
        if (shops[player_index]) shops[player_index]->return_current_shop();

        auto return_unit_copies = [this](const std::optional<UnitInstance>& unit) {
            if (!unit) return;
            for (std::int32_t copy = 0; copy < star_copies(unit->star); ++copy)
                (void)pool->give_back(unit->champion_internal_id);
        };
        for (auto& unit : boards[player_index]) {
            return_unit_copies(unit);
            unit.reset();
        }
        for (auto& unit : benches[player_index]) {
            return_unit_copies(unit);
            unit.reset();
        }
        register_position_state(player_index);
    }

    void eliminate_players(std::vector<std::string>& events) {
        // Python define as colocações após todos os combates, em ordem de ID.
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            auto& player = players[i];
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
            if (players[i].alive) {
                winner_id = static_cast<std::int32_t>(i);
                players[i].placement = 1;
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
                    players[i].placement = static_cast<std::int32_t>(
                        kPlayersPerLobby - ranking.size());
                    ranking.push_back(static_cast<std::int32_t>(i));
                }
            }
        }
    }

    void resolve_combats(
        std::vector<std::string>& events,
        std::array<float, kPlayersPerLobby>& rewards
    ) {
        std::vector<std::size_t> alive;
        alive.reserve(kPlayersPerLobby);
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            players[i].opponent_id.reset();
            if (players[i].alive) alive.push_back(i);
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
            players[a].opponent_id = static_cast<std::int32_t>(b);
            players[b].opponent_id = static_cast<std::int32_t>(a);
            previous_matchups.insert(matchup_key(a, b));
        }

        auto apply_damage = [&](std::size_t player_index, std::int32_t damage) {
            auto& player = players[player_index];
            if (!player.alive || damage <= 0) return;
            const float applied = std::min(player.hp, static_cast<float>(damage));
            player.hp = std::max(0.0f, player.hp - applied);
            player.damage_taken += applied;
        };

        for (const auto& [a, b] : matchups) {
            if (!players[a].alive || !players[b].alive) continue;
            CombatInput input{};
            input.context = CombatContext::PVP;
            input.seed = seed + static_cast<std::uint64_t>(round + 1) * 1000003ULL
                + static_cast<std::uint64_t>(a) * 101ULL
                + static_cast<std::uint64_t>(b) * 1009ULL;
            input.config.seed = input.seed;
            input.config.deterministic = true;
            append_combat_team(a, UnitTeam::PLAYER_A, input.player_a);
            append_combat_team(b, UnitTeam::PLAYER_B, input.player_b);

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

            ++players[winner].wins;
            ++players[loser].losses;
            economy_engine.register_pvp_win(economies[winner]);
            economy_engine.register_loss(economies[loser]);
            const auto damage = stage_damage(stage) + std::max(0, winner_survivors);
            apply_damage(loser, damage);
            const double winner_reward = combat_reward(
                true, damage, 0, loser_survivors, winner_survivors);
            const double loser_reward = combat_reward(
                false, 0, damage, winner_survivors, loser_survivors);
            last_combat_reward[winner] = winner_reward;
            last_combat_reward[loser] = loser_reward;
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
    for (auto& shop : impl_->shops) {
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
    impl_->previous_board_power.fill(0.0);
    impl_->previous_synergy_score.fill(0.0);
    impl_->previous_positioning_score.fill(0.0);
    impl_->previous_reward_level.fill(1);
    impl_->last_combat_reward.fill(0.0);
    impl_->round_reward_total.fill(0.0);
    impl_->total_reward.fill(0.0);

    ResetResult result{};

    result.observations = impl_->build_observations();
    result.observation_dim = kObservationDim;
    result.action_masks = impl_->masks;
    result.episode_id = impl_->episode_id;

    return result;
}

// ============================================================
// STEP
// ============================================================

StepResult TFTEngine::step(
    const std::array<PlayerAction, kPlayersPerLobby>& actions
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

    // Preflight em duas fases: valida limites e disponibilidade semântica
    // de todas as ações antes de executar a primeira. Se qualquer ação for
    // impossível, o lote falha sem alterar ouro, unidades ou posições.
    for (const auto& action : actions) {
        impl_->validate_action(action);
    }
    for (std::size_t i = 0; i < actions.size(); ++i) {
        impl_->validate_action_against_masks(i, actions[i]);
    }

    // ========================================================
    // AÇÕES DE LOJA, ECONOMIA E MOVIMENTAÇÃO
    // ========================================================

    std::array<float, kPlayersPerLobby> round_rewards{};
    std::array<double, kPlayersPerLobby> action_reward_values{};
    for (std::size_t i = 0;
         i < kPlayersPerLobby;
         ++i) {
        const auto& action = actions[i].values;

        const auto type = action[0];

        const auto shop_slot = action[1];

        auto& economy = impl_->economies[i];
        auto& shop = *impl_->shops[i];
        const auto old_gold = economy.gold;
        const auto old_level = economy.level;
        const auto old_xp = economy.xp;
        int old_board_count = 0, old_bench_count = 0;
        for (const auto& unit : impl_->boards[i]) if (unit) ++old_board_count;
        for (const auto& unit : impl_->benches[i]) if (unit) ++old_bench_count;

        if (!impl_->players[i].alive) {
            impl_->refresh_masks(i);
            continue;
        }

        if (type == 0) {
            // BUY
            const auto* offer = shop.get_unit(shop_slot);

            std::size_t free_slot = kBenchSlots;

            for (std::size_t slot = 0;
                 slot < kBenchSlots;
                 ++slot) {
                if (!impl_->benches[i][slot]) {
                    free_slot = slot;
                    break;
                }
            }

            if (offer && free_slot < kBenchSlots) {
                const auto* definition =
                    impl_->catalog->find_by_id(
                        offer->champion_internal_id
                    );

                if (definition &&
                    economy.gold >= definition->cost &&
                    impl_->economy_engine.spend_gold(
                        economy,
                        definition->cost
                    )) {
                    auto purchased =
                        shop.take_unit(shop_slot);

                    if (purchased) {
                        impl_->benches[i][free_slot] = std::move(*purchased);

                        // Auto-upgrade 3x1★ -> 2★ e 3x2★ -> 3★.
                        // O pool não muda: as cópias continuam pertencendo ao jogador.
                        auto& bought_unit = impl_->benches[i][free_slot];
                        while (bought_unit && bought_unit->star < 3) {
                            const auto champion_id = bought_unit->champion_internal_id;
                            const auto star = bought_unit->star;
                            std::vector<std::pair<bool, std::size_t>> matches;
                            matches.emplace_back(false, free_slot);
                            for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
                                if (slot != free_slot && impl_->benches[i][slot] &&
                                    impl_->benches[i][slot]->champion_internal_id == champion_id &&
                                    impl_->benches[i][slot]->star == star)
                                    matches.emplace_back(false, slot);
                            }
                            for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
                                if (impl_->boards[i][slot] &&
                                    impl_->boards[i][slot]->champion_internal_id == champion_id &&
                                    impl_->boards[i][slot]->star == star)
                                    matches.emplace_back(true, slot);
                            }
                            if (matches.size() < 3) break;
                            std::size_t removed = 0;
                            for (const auto& [on_board, slot] : matches) {
                                if (!on_board && slot == free_slot) continue;
                                if (on_board) impl_->boards[i][slot].reset();
                                else impl_->benches[i][slot].reset();
                                if (++removed == 2) break;
                            }
                            bought_unit->star = star + 1;
                        }
                        impl_->register_position_state(i);
                    } else {
                        impl_->economy_engine.add_gold(
                            economy,
                            definition->cost
                        );
                    }
                }
            }
        } else if (type == 1) {
            // REROLL
            if (impl_->economy_engine.spend_gold(
                    economy,
                    EconomyEngine::REROLL_COST
                )) {
                shop.reroll(economy.level);
            }
        } else if (type == 2) {
            // BUY XP
            (void)impl_->economy_engine.buy_xp(economy);
        } else if (type == 3) {
            // MOVE_BENCH: banco -> tabuleiro
            auto& anti_loop = impl_->anti_loop_engines[i];

            anti_loop.record_execution_attempt();

            const auto source = action[2];
            const auto target = action[3];

            const auto state =
                impl_->build_decision_state(i);

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

                const auto target_index =
                    static_cast<std::size_t>(target);

                const auto unit_identity =
                    std::optional<decision::UnitIdentity>{
                        state.bench[source_index]->identity
                    };

                const std::string move_type =
                    "bench_to_board";

                const auto reason =
                    anti_loop.get_block_reason(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                if (reason.has_value()) {
                    (void)anti_loop.block_move(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                    anti_loop.record_execution_block(*reason);
                } else {
                    (void)anti_loop.register_move(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                    impl_->boards[i][target_index] =
                        std::move(
                            impl_->benches[i][source_index]
                        );

                    impl_->benches[i][source_index].reset();

                    anti_loop.record_successful_move(move_type);

                    impl_->register_position_state(i);
                }
            }
        } else if (type == 4) {
            // MOVE_BOARD: movimento ou troca
            auto& anti_loop = impl_->anti_loop_engines[i];

            anti_loop.record_execution_attempt();

            const auto source = action[4];
            const auto target = action[5];

            const auto state =
                impl_->build_decision_state(i);

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

                const auto reason =
                    anti_loop.get_block_reason(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                if (reason.has_value()) {
                    (void)anti_loop.block_move(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                    anti_loop.record_execution_block(*reason);
                } else {
                    (void)anti_loop.register_move(
                        move_type,
                        source,
                        target,
                        unit_identity
                    );

                    if (move_type == "board_swap") {
                        std::swap(
                            impl_->boards[i][source_index],
                            impl_->boards[i][target_index]
                        );
                    } else {
                        impl_->boards[i][target_index] =
                            std::move(
                                impl_->boards[i][source_index]
                            );

                        impl_->boards[i][source_index].reset();
                    }

                    anti_loop.record_successful_move(move_type);

                    impl_->register_position_state(i);
                }
            }
        } else if (type == 5) {
            // SELL: vender unidade do banco
            const auto bench_slot =
                static_cast<std::size_t>(action[2]);

            if (bench_slot < kBenchSlots &&
                impl_->benches[i][bench_slot]) {
                const auto& unit =
                    *impl_->benches[i][bench_slot];

                const auto* definition =
                    impl_->catalog->find_by_id(
                        unit.champion_internal_id
                    );

                if (definition) {
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
                        if (!impl_->pool->give_back(unit.champion_internal_id)) {
                            returned_all_copies = false;
                            break;
                        }
                    }
                    if (returned_all_copies) {
                        impl_->benches[i][bench_slot].reset();
                        (void)impl_->economy_engine.add_gold(economy, sell_value);
                        impl_->register_position_state(i);
                    } else {
                        for (std::int32_t copy = 0; copy < returned; ++copy)
                            (void)impl_->pool->take(unit.champion_internal_id);
                    }
                }
            }
        } else if (type == 6) {
            // PASS
        }

        impl_->sync_player_economy(i);
        int new_board_count = 0, new_bench_count = 0;
        for (const auto& unit : impl_->boards[i]) if (unit) ++new_board_count;
        for (const auto& unit : impl_->benches[i]) if (unit) ++new_bench_count;

        // Alinhado a RewardManager.calculate_action_reward() e aos valores
        // usados em env.py para compra, reroll e XP.
        double action_reward = 0.0;
        bool success = false;
        if (type == 0) {
            success = new_bench_count > old_bench_count || new_board_count > old_board_count ||
                      (old_bench_count == new_bench_count && old_board_count == new_board_count &&
                       economy.gold < old_gold);
            action_reward = success ? 0.05 : -0.10;
            if (success && (new_board_count < old_board_count || new_bench_count < old_bench_count))
                action_reward = 0.30; // compra que conclui upgrade automático
        } else if (type == 1) {
            success = economy.gold == old_gold - EconomyEngine::REROLL_COST;
            action_reward = success ? -0.01 : -0.10;
        } else if (type == 2) {
            success = economy.gold == old_gold - EconomyEngine::BUY_XP_COST;
            action_reward = success ? 0.02 : -0.10;
            if (success && economy.level > old_level)
                action_reward += std::min((economy.level - old_level) * 0.5, 1.5);
            (void)old_xp;
        } else if (type == 3 || type == 4) {
            success = new_board_count != old_board_count ||
                (type == 4 && new_board_count == old_board_count);
            action_reward = success ? 0.0 : -0.10;
            if (type == 3 && success)
                action_reward += impl_->positioning_score(i) * 0.05;
        } else if (type == 5) {
            success = economy.gold > old_gold;
            action_reward = success ? 0.0 : -0.10;
        } else {
            success = true;
        }

        action_reward_values[i] = action_reward;
        round_rewards[i] += static_cast<float>(
            std::clamp(impl_->state_reward(i, action_reward), -5.0, 5.0));
        impl_->round_reward_total[i] = round_rewards[i];
        impl_->total_reward[i] += round_rewards[i];
        impl_->update_strategy(i);

        impl_->sync_player_economy(i);
        impl_->refresh_masks(i);
        impl_->mark_round_completion(i, type);
    }

    // ========================================================
    // RESOLUÇÃO CONDICIONAL DA RODADA
    // ========================================================

    std::vector<std::string> round_events;
    bool round_resolved = false;

    if (impl_->all_alive_players_finished_round()) {
        round_resolved = true;

        // A ordem acompanha TFTLobby._resolve_round(): primeiro a renda/XP
        // da rodada e a preparação das lojas; depois os confrontos PVP.
        const auto resolving_round =
            static_cast<std::int32_t>(impl_->round + 1);

        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (!impl_->players[i].alive) {
                continue;
            }

            (void)impl_->economy_engine.resolve_round(
                impl_->economies[i],
                resolving_round
            );
            impl_->sync_player_economy(i);

            // A loja da próxima rodada só é preparada quando a rodada
            // realmente fecha, nunca em cada ação individual.
            impl_->shops[i]->roll(impl_->economies[i].level);
            impl_->refresh_masks(i);
        }

        impl_->resolve_combats(round_events, round_rewards);
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (!impl_->players[i].alive) continue;
            round_rewards[i] += static_cast<float>(
                std::clamp(impl_->state_reward(i, 0.0), -5.0, 5.0));
            impl_->round_reward_total[i] = round_rewards[i];
            impl_->total_reward[i] += round_rewards[i];
            impl_->update_strategy(i);
        }

        // O bônus de vitória já foi creditado no ouro pelo combate.
        // Limpa apenas o acumulador do relatório desta rodada.
        for (auto& economy : impl_->economies) {
            economy.round_win_gold = 0;
        }

        // A lobby Python só avança se ainda houver pelo menos dois
        // jogadores vivos. A partida encerrada mantém a rodada final.
        if (!impl_->done && impl_->alive_players > 1) {
            ++impl_->round;

            const std::uint32_t public_round =
                impl_->round + 1;

            impl_->stage =
                ((public_round - 1) / kRoundsPerStage) + 1;

            impl_->reset_round_completion();
        }
    }

    // ========================================================
    // RESULTADO
    // ========================================================

    StepResult result{};

    result.observations = impl_->build_observations();
    result.observation_dim = kObservationDim;

    result.rewards = round_rewards;
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        result.dones[i] = (!impl_->players[i].alive || impl_->done) ? 1 : 0;
    }

    result.action_masks = impl_->masks;
    result.players = impl_->players;

    result.lobby_done = impl_->done;
    result.episode_id = impl_->episode_id;
    result.round = impl_->round + 1;
    result.stage = impl_->stage;
    result.alive_players = impl_->alive_players;

    result.events.emplace_back(
        "Acoes de loja, economia, venda e movimentacao "
        "executadas pelo TFTEngine."
    );
    if (!round_resolved) {
        result.events.emplace_back(
            "ROUND_WAITING: aguardando PASS ou limite de acoes "
            "de todos os jogadores vivos."
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

    return impl_->masks;
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

    return impl_->shops[
        static_cast<std::size_t>(player_id)
    ]->set_locked(locked);
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

    return impl_->shops[
        static_cast<std::size_t>(player_id)
    ]->toggle_lock();
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

    return impl_->shops[
        static_cast<std::size_t>(player_id)
    ]->is_locked();
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

    return impl_->strategies;
}

// ============================================================
// MÉTRICAS ANTI-LOOP
// ============================================================

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
            impl_->anti_loop_engines[i].get_metrics();

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

    for (const auto& player : impl_->players) {
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
    return kObservationDim;
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
