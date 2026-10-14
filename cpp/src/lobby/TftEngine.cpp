
#include "lobby/TftEngine.hpp"

#include <algorithm>
#include <cstdint>
#include <memory>
#include <optional>
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

    explicit Impl(
        std::uint64_t initial_seed,
        const std::string& catalog_path
    ) : seed(initial_seed) {
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

    void resolve_combats(
        std::vector<std::string>& events,
        std::array<float, kPlayersPerLobby>& rewards
    ) {
        std::vector<std::size_t> alive;
        alive.reserve(kPlayersPerLobby);
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            if (players[i].alive) {
                alive.push_back(i);
            }
        }

        if (alive.size() < 2) {
            if (alive.size() == 1) {
                done = true;
                winner_id = static_cast<std::int32_t>(alive.front());
                players[alive.front()].placement = 1;
                if (ranking.empty() ||
                    ranking.front() != static_cast<std::int32_t>(alive.front())) {
                    ranking.insert(
                        ranking.begin(),
                        static_cast<std::int32_t>(alive.front()));
                }
            }
            return;
        }

        // Rotação determinística para evitar que os mesmos jogadores se
        // enfrentem em todas as rodadas.
        const auto offset = static_cast<std::ptrdiff_t>(
            round % alive.size());
        std::rotate(alive.begin(), alive.begin() + offset, alive.end());

        auto apply_damage = [&](std::size_t player_index, int damage) {
            auto& player = players[player_index];
            if (!player.alive || damage <= 0) {
                return;
            }

            const float applied = std::min(
                player.hp, static_cast<float>(damage));
            player.hp = std::max(0.0f, player.hp - applied);
            player.damage_taken += applied;

            if (player.hp <= 0.0f) {
                player.alive = false;
                player.eliminated = true;
                player.placement = alive_players;
                ranking.push_back(static_cast<std::int32_t>(player_index));
                --alive_players;
                events.emplace_back(
                    "ELIMINATED: jogador " +
                    std::to_string(player_index));
            }
        };

        for (std::size_t pair = 0; pair + 1 < alive.size(); pair += 2) {
            const auto a = alive[pair];
            const auto b = alive[pair + 1];
            if (!players[a].alive || !players[b].alive) {
                continue;
            }

            CombatInput input{};
            input.context = CombatContext::PVP;
            input.seed = seed
                + static_cast<std::uint64_t>(round + 1) * 1000003ULL
                + static_cast<std::uint64_t>(a) * 101ULL
                + static_cast<std::uint64_t>(b) * 1009ULL;
            input.config.seed = input.seed;
            input.config.deterministic = true;

            append_combat_team(a, UnitTeam::PLAYER_A, input.player_a);
            append_combat_team(b, UnitTeam::PLAYER_B, input.player_b);

            // Jogadores sem unidades no tabuleiro ainda estão montando a
            // composição; não devem perder vida por um combate inexistente.
            if (input.player_a.units.empty() || input.player_b.units.empty()) {
                events.emplace_back(
                    "COMBAT_SKIPPED: jogador " + std::to_string(a) +
                    " vs " + std::to_string(b) +
                    " (um dos tabuleiros está vazio).");
                continue;
            }

            const auto combat = combat_engine.simulate(input);
            if (!combat.success || !combat.completed) {
                throw std::runtime_error(
                    "CombatEngine falhou no confronto " +
                    std::to_string(a) + " vs " + std::to_string(b) +
                    ": " + combat.error_code + " - " +
                    combat.error_message);
            }

            events.emplace_back(
                "COMBAT: jogador " + std::to_string(a) +
                " vs " + std::to_string(b) +
                ", eventos=" + std::to_string(combat.events_processed));

            if (combat.winner == CombatWinner::PLAYER_A) {
                ++players[a].wins;
                ++players[b].losses;
                economy_engine.register_pvp_win(economies[a]);
                economy_engine.register_loss(economies[b]);
                rewards[a] += 1.0f;
                rewards[b] -= 1.0f;
                apply_damage(b, std::max(1, combat.player_a_survivors));
                events.emplace_back(
                    "COMBAT_WIN: jogador " + std::to_string(a));
            } else if (combat.winner == CombatWinner::PLAYER_B) {
                ++players[b].wins;
                ++players[a].losses;
                economy_engine.register_pvp_win(economies[b]);
                economy_engine.register_loss(economies[a]);
                rewards[b] += 1.0f;
                rewards[a] -= 1.0f;
                apply_damage(a, std::max(1, combat.player_b_survivors));
                events.emplace_back(
                    "COMBAT_WIN: jogador " + std::to_string(b));
            } else {
                economy_engine.reset_streak(economies[a]);
                economy_engine.reset_streak(economies[b]);
                events.emplace_back(
                    "COMBAT_DRAW: jogadores " + std::to_string(a) +
                    " e " + std::to_string(b));
            }

            sync_player_economy(a);
            sync_player_economy(b);
        }

        if (alive_players <= 1) {
            done = true;
            for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
                if (players[i].alive) {
                    winner_id = static_cast<std::int32_t>(i);
                    players[i].placement = 1;
                    ranking.insert(ranking.begin(),
                                   static_cast<std::int32_t>(i));
                    break;
                }
            }
        }

        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            refresh_masks(i);
        }
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

    for (std::size_t i = 0;
         i < kPlayersPerLobby;
         ++i) {
        const auto& action = actions[i].values;

        const auto type = action[0];

        const auto shop_slot = action[1];

        auto& economy = impl_->economies[i];
        auto& shop = *impl_->shops[i];

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
                        impl_->benches[i][free_slot] =
                            std::move(*purchased);

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
                    if (impl_->pool->give_back(
                            unit.champion_internal_id
                        )) {
                        impl_->benches[i][bench_slot].reset();

                        (void)impl_->economy_engine.add_gold(
                            economy,
                            sell_value
                        );

                        impl_->register_position_state(i);
                    }
                }
            }
        } else if (type == 6) {
            // PASS
        }

        impl_->sync_player_economy(i);
        impl_->refresh_masks(i);
    }

    // ========================================================
    // RENDA E XP PASSIVO DA RODADA
    // ========================================================

    const auto resolving_round =
        static_cast<std::int32_t>(impl_->round + 1);

    for (std::size_t i = 0;
         i < kPlayersPerLobby;
         ++i) {
        if (impl_->players[i].alive) {
            (void)impl_->economy_engine.resolve_round(
                impl_->economies[i],
                resolving_round
            );

            impl_->sync_player_economy(i);

            // Prepara a loja da próxima rodada. ShopEngine respeita o
            // bloqueio: ofertas permanecem iguais quando a loja está locked.
            impl_->shops[i]->roll(impl_->economies[i].level);

            impl_->refresh_masks(i);
        }
    }

    ++impl_->round;

    const std::uint32_t public_round =
        impl_->round + 1;

    impl_->stage =
        ((public_round - 1) / kRoundsPerStage) + 1;

    // ========================================================
    // RESULTADO
    // ========================================================

    StepResult result{};

    result.observations = impl_->build_observations();
    result.observation_dim = kObservationDim;

    result.rewards.fill(0.0f);
    result.dones.fill(0);

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
