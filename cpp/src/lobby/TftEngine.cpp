
#include "lobby/TftEngine.hpp"

#include <algorithm>
#include <stdexcept>
#include <utility>

#include "lobby/ChampionCatalog.hpp"
#include "lobby/UnitInstanceFactory.hpp"
#include "lobby/UnitPool.hpp"
#include "lobby/EconomyEngine.hpp"
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

// ============================================================
// ⚙️ Configuração provisória da Etapa 1
// ============================================================

// Observação provisória com 8 atributos por jogador:
// [hp, gold, level, xp, alive, wins, losses, round].
//
// IMPORTANTE:
// Este vetor existe para validar o contrato do binding.
// Ainda não representa o vetor de observações definitivo do PPO.
constexpr std::size_t kObservationDim = 8;

// Configuração provisória do estágio.
constexpr std::uint32_t kRoundsPerStage = 7;

// Cria máscaras seguras para o esqueleto.
// Somente a ação neutra (type = 6) fica habilitada.

 // Cria máscaras provisórias seguras para o contrato da Etapa 1.
// Não representa as ações reais do jogo.
// Índice 0 funciona como opção dummy para as dimensões
// que não são utilizadas pela ação neutra PASS (índice 6).
PlayerActionMasks make_default_masks() {
    PlayerActionMasks masks{};

    // Tipo de ação: PASS.
    masks.type_mask[6] = 1;

    // Slots dummy válidos para as demais dimensões.
    masks.shop_mask[0] = 1;
    masks.bench_source_mask[0] = 1;
    masks.board_target_mask[0] = 1;
    masks.board_source_mask[0] = 1;
    masks.bench_move_source_mask[0] = 1;

    // Destino dummy para movimentação no tabuleiro.
    // Layout row-major: [origem, destino].
    masks.board_move_target_masks[0] = 1;

    // Destino dummy para movimentação do banco ao tabuleiro.
    // Layout row-major: [origem do banco, destino no tabuleiro].
    masks.bench_to_board_target_masks[0] = 1;

    return masks;
}


// Converte o estado de um jogador em uma observação provisória.
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
// 🧠 IMPLEMENTAÇÃO INTERNA
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
    std::array<std::unique_ptr<ShopEngine>, kPlayersPerLobby> shops{};
    std::array<std::array<std::optional<UnitInstance>, kBenchSlots>, kPlayersPerLobby> benches{};
    std::array<std::array<std::optional<UnitInstance>, kBoardSlots>, kPlayersPerLobby> boards{};

    // Um histórico AntiLoop isolado por jogador evita interferência entre rivais.
    std::array<decision::AntiLoopEngine, kPlayersPerLobby> anti_loop_engines{};
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

    // ============================================================
    // 💰 ESTADO ECONÔMICO
    // ============================================================

    // Motor sem estado próprio: as operações recebem o jogador
    // econômico que devem consultar ou modificar.
    EconomyEngine economy_engine;

    // Um estado econômico independente por jogador.
    std::array<PlayerEconomy, kPlayersPerLobby> economies{};

   explicit Impl(
        std::uint64_t initial_seed,
        const std::string& catalog_path
    ) : seed(initial_seed) {
        const std::string resolved_path =
            catalog_path.empty()
                ? TFT_DEFAULT_CATALOG_PATH
                : catalog_path;

        // Um catálogo por partida.
        catalog = std::make_unique<ChampionCatalog>(
            resolved_path
        );

        // Um pool por partida, compartilhado pelos oito jogadores.
        pool = std::make_unique<UnitPool>(*catalog);

        // A fábrica usa o catálogo da mesma partida.
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

    void initialize_players() {
        alive_players =
            static_cast<std::int32_t>(kPlayersPerLobby);

        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            PlayerInfo player{};

            player.player_id = static_cast<std::int32_t>(i);
            player.hp = 100.0f;

            // Inicializa a economia conforme GameConfig.py.
            economy_engine.reset(economies[i]);

            // Mantém PlayerInfo sincronizado desde o primeiro frame.
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
            anti_loop_engines[i] = decision::AntiLoopEngine{};
            shops[i] = std::make_unique<ShopEngine>(
                *pool, *unit_factory, seed + static_cast<std::uint64_t>(i) + episode_id
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

    decision::PlayerState build_decision_state(std::size_t player_index) const {
        decision::PlayerState state;
        state.player_id = static_cast<std::int64_t>(player_index);
        state.is_alive = players[player_index].alive;

        const auto& economy = economies[player_index];
        state.economy.gold = economy.gold;
        state.economy.level = economy.level;
        state.economy.max_level = EconomyEngine::MAX_LEVEL;
        state.economy.current_xp = economy.xp;
        state.economy.xp_to_next_level = economy_engine.get_xp_to_next(economy);
        state.economy.reroll_cost = EconomyEngine::REROLL_COST;
        state.economy.xp_purchase_cost = EconomyEngine::BUY_XP_COST;

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
                catalog->find_by_id(instance->champion_internal_id);
            unit.cost = static_cast<std::uint8_t>(
                definition ? std::clamp(definition->cost, 1, 5) : 1
            );
            unit.available = true;
            return unit;
        };

        for (std::size_t slot = 0; slot < kBoardSlots; ++slot) {
            state.board[slot] = snapshot(boards[player_index][slot]);
        }
        for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
            state.bench[slot] = snapshot(benches[player_index][slot]);
        }
        for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
            const auto* offer = shops[player_index]->get_unit(
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
        const auto state = build_decision_state(player_index);
        const auto signature =
            anti_loop_engines[player_index].make_board_signature(state);
        (void)anti_loop_engines[player_index].register_state(signature);
    }

    void refresh_masks(std::size_t player_index) {
        const auto state = build_decision_state(player_index);
        const auto batch = action_mask_engine.generate_masks(
            state,
            anti_loop_engines[player_index]
        );

        auto& current = masks[player_index];
        current = PlayerActionMasks{};
        current.type_mask = batch.type_mask;
        current.shop_mask = batch.shop_mask;
        current.bench_source_mask = batch.bench_source_mask;
        current.board_target_mask = batch.board_target_mask;
        current.board_source_mask = batch.board_source_mask;
        current.bench_move_source_mask = batch.bench_move_source_mask;

        for (std::size_t source = 0; source < kBoardSlots; ++source) {
            for (std::size_t target = 0; target < kBoardSlots; ++target) {
                current.board_move_target_masks[
                    source * kBoardSlots + target
                ] = batch.board_move_target_masks[source][target];
            }
        }

        for (std::size_t source = 0; source < kBenchSlots; ++source) {
            for (std::size_t target = 0; target < kBoardSlots; ++target) {
                current.bench_to_board_target_masks[
                    source * kBoardSlots + target
                ] = batch.bench_to_board_target_masks[source][target];
            }
        }
    }

    std::vector<float> build_observations() const {
        std::vector<float> observations(
            kPlayersPerLobby * kObservationDim,
            0.0f
        );

        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            write_observation(
                players[i],
                round + 1,
                observations.data() + i * kObservationDim
            );
        }

        return observations;
    }

    void validate_action(const PlayerAction& action) const {
        for (std::size_t i = 0; i < kActionComponents; ++i) {
            const std::int32_t value = action.values[i];

            if (value < 0 ||
                static_cast<std::size_t>(value) >= kActionDims[i]) {
                throw std::invalid_argument(
                    "Componente de acao fora dos limites. "
                    "Dimensao: " + std::to_string(i) +
                    ", valor: " + std::to_string(value)
                );
            }
        }
    }

    // ============================================================
    // 🔄 SINCRONIZAÇÃO DA ECONOMIA
    // ============================================================

    // PlayerInfo continua sendo a representação pública usada
    // pelas observações e pelos bindings Python.
    //
    // PlayerEconomy é a fonte interna para ouro, nível e XP.
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
};

// ============================================================
// 🏗️ CONSTRUTOR E DESTRUTOR
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
// 🔄 RESET
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
    // Devolve ofertas antes de restaurar o pool.
    for (auto& shop : impl_->shops) {
        if (shop) shop->return_current_shop();
        shop.reset();
    }
    impl_->pool->reset();

    // Reinicia a sequência de geração de UUIDs para a seed atual.
    impl_->unit_factory = std::make_unique<UnitInstanceFactory>(
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
// ▶️ STEP
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

    // --------------------------------------------------------
    // 1. Validar as ações recebidas
    // --------------------------------------------------------

    for (const auto& action : actions) {
        impl_->validate_action(action);
    }

    // --------------------------------------------------------
    // 2. Executar ações de loja e economia
    // --------------------------------------------------------
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        const auto& action = actions[i].values;
        const auto type = action[0];
        const auto shop_slot = action[1];
        auto& economy = impl_->economies[i];
        auto& shop = *impl_->shops[i];
        if (!impl_->players[i].alive) { impl_->refresh_masks(i); continue; }

        if (type == 0) { // BUY
            const auto* offer = shop.get_unit(shop_slot);
            std::size_t free_slot = kBenchSlots;
            for (std::size_t slot = 0; slot < kBenchSlots; ++slot) {
                if (!impl_->benches[i][slot]) { free_slot = slot; break; }
            }

            if (offer && free_slot < kBenchSlots) {
                const auto* definition =
                    impl_->catalog->find_by_id(offer->champion_internal_id);
                if (definition && economy.gold >= definition->cost
                    && impl_->economy_engine.spend_gold(economy, definition->cost)) {
                    auto purchased = shop.take_unit(shop_slot);
                    if (purchased) {
                        impl_->benches[i][free_slot] = std::move(*purchased);
                        impl_->register_position_state(i);
                    } else {
                        impl_->economy_engine.add_gold(economy, definition->cost);
                    }
                }
            }
        } else if (type == 1) { // REROLL
            if (impl_->economy_engine.spend_gold(economy, EconomyEngine::REROLL_COST)) {
                shop.reroll(economy.level);
            }
        } else if (type == 2) { // BUY XP
            (void)impl_->economy_engine.buy_xp(economy);
        } else if (type == 3) { // MOVE_BENCH: banco -> tabuleiro
            auto& anti_loop = impl_->anti_loop_engines[i];
            anti_loop.record_execution_attempt();

            const auto source = action[2];
            const auto target = action[3];
            const auto state = impl_->build_decision_state(i);
            const auto validation = decision::MoveValidator::validate_bench_to_board_move(
                state.board, state.bench, source, target
            );

            if (validation.is_valid()) {
                const auto source_index = static_cast<std::size_t>(source);
                const auto target_index = static_cast<std::size_t>(target);
                const auto unit_identity =
                    std::optional<decision::UnitIdentity>{
                        state.bench[source_index]->identity
                    };
                const std::string move_type = "bench_to_board";
                const auto reason = anti_loop.get_block_reason(
                    move_type, source, target, unit_identity
                );

                if (reason.has_value()) {
                    (void)anti_loop.block_move(move_type, source, target, unit_identity);
                    anti_loop.record_execution_block(*reason);
                } else {
                    (void)anti_loop.register_move(move_type, source, target, unit_identity);
                    impl_->boards[i][target_index] =
                        std::move(impl_->benches[i][source_index]);
                    impl_->benches[i][source_index].reset();
                    anti_loop.record_successful_move(move_type);
                    impl_->register_position_state(i);
                }
            }
        } else if (type == 4) { // MOVE_BOARD: movimento ou troca
            auto& anti_loop = impl_->anti_loop_engines[i];
            anti_loop.record_execution_attempt();

            const auto source = action[4];
            const auto target = action[5];
            const auto state = impl_->build_decision_state(i);
            const auto validation = decision::MoveValidator::validate_board_move(
                state.board, source, target
            );

            if (validation.is_valid() && validation.move_type.has_value()) {
                const auto source_index = static_cast<std::size_t>(source);
                const auto target_index = static_cast<std::size_t>(target);
                const auto unit_identity =
                    std::optional<decision::UnitIdentity>{
                        state.board[source_index]->identity
                    };
                const std::string move_type =
                    *validation.move_type == decision::MoveType::BOARD_SWAP
                        ? "board_swap"
                        : "board_move";
                const auto reason = anti_loop.get_block_reason(
                    move_type, source, target, unit_identity
                );

                if (reason.has_value()) {
                    (void)anti_loop.block_move(move_type, source, target, unit_identity);
                    anti_loop.record_execution_block(*reason);
                } else {
                    (void)anti_loop.register_move(move_type, source, target, unit_identity);
                    if (move_type == "board_swap") {
                        std::swap(
                            impl_->boards[i][source_index],
                            impl_->boards[i][target_index]
                        );
                    } else {
                        impl_->boards[i][target_index] =
                            std::move(impl_->boards[i][source_index]);
                        impl_->boards[i][source_index].reset();
                    }
                    anti_loop.record_successful_move(move_type);
                    impl_->register_position_state(i);
                }
            }
        } else if (type == 5) { // SELL: vende uma unidade do banco
            const auto bench_slot = static_cast<std::size_t>(action[2]);
            if (impl_->benches[i][bench_slot].has_value()) {
                const auto& unit = *impl_->benches[i][bench_slot];
                const auto* definition =
                    impl_->catalog->find_by_id(unit.champion_internal_id);

                if (definition) {
                    const auto sell_value = EconomyEngine::get_sell_value(
                        definition->cost, unit.star
                    );

                    // Só altera o estado se a cópia puder ser devolvida ao pool.
                    if (impl_->pool->give_back(unit.champion_internal_id)) {
                        impl_->benches[i][bench_slot].reset();
                        (void)impl_->economy_engine.add_gold(economy, sell_value);
                        impl_->register_position_state(i);
                    }
                }
            }
        } else if (type == 6) {
            // PASS: nenhuma alteração.
        }

        impl_->sync_player_economy(i);
        impl_->refresh_masks(i);
    }

    // Renda e XP passivo da rodada.
    const auto resolving_round = static_cast<std::int32_t>(impl_->round + 1);
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        if (impl_->players[i].alive) {
            (void)impl_->economy_engine.resolve_round(impl_->economies[i], resolving_round);
            impl_->sync_player_economy(i);
            impl_->refresh_masks(i);
        }
    }

    // O contador interno representa as rodadas já avançadas.
    ++impl_->round;

    // A rodada pública seguinte é impl_->round + 1.
    // O estágio deve corresponder a essa rodada pública.
    const std::uint32_t public_round = impl_->round + 1;

    impl_->stage =
        ((public_round - 1) / kRoundsPerStage) + 1;

    // --------------------------------------------------------
    // 3. Montar o resultado
    // --------------------------------------------------------

    StepResult result{};

    result.observations = impl_->build_observations();
    result.observation_dim = kObservationDim;

    result.rewards.fill(0.0f);
    result.dones.fill(0);

    result.action_masks = impl_->masks;
    result.players = impl_->players;

    result.lobby_done = impl_->done;
    result.episode_id = impl_->episode_id;
    // Mantém StepResult alinhado com get_public_state().
    result.round = impl_->round + 1;
    result.stage = impl_->stage;
    result.alive_players = impl_->alive_players;

    result.events.emplace_back(
        "Ações de loja, economia, venda e movimentação executadas pelo TFTEngine."
    );

    return result;
}

// ============================================================
// 🎭 MÁSCARAS DE AÇÃO
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
        throw std::runtime_error("TFTEngine nao possui estado interno.");
    }
    impl_->ensure_open();
    if (player_id < 0 || static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        throw std::out_of_range("player_id invalido ao alterar bloqueio da loja.");
    }
    return impl_->shops[static_cast<std::size_t>(player_id)]->set_locked(locked);
}

bool TFTEngine::toggle_shop_lock(std::int32_t player_id) {
    if (!impl_) {
        throw std::runtime_error("TFTEngine nao possui estado interno.");
    }
    impl_->ensure_open();
    if (player_id < 0 || static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        throw std::out_of_range("player_id invalido ao alternar bloqueio da loja.");
    }
    return impl_->shops[static_cast<std::size_t>(player_id)]->toggle_lock();
}

bool TFTEngine::is_shop_locked(std::int32_t player_id) const {
    if (!impl_) {
        throw std::runtime_error("TFTEngine nao possui estado interno.");
    }
    impl_->ensure_open();
    if (player_id < 0 || static_cast<std::size_t>(player_id) >= kPlayersPerLobby) {
        throw std::out_of_range("player_id invalido ao consultar bloqueio da loja.");
    }
    return impl_->shops[static_cast<std::size_t>(player_id)]->is_locked();
}

// ============================================================
// 👁️ OBSERVAÇÕES
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
// 🧠 ESTRATÉGIAS
// ============================================================

std::array<std::vector<StrategyInfo>, kPlayersPerLobby>
TFTEngine::get_strategies() const {
    if (!impl_) {
        throw std::runtime_error(
            "TFTEngine nao possui estado interno."
        );
    }

    impl_->ensure_open();

    // Uma estratégia atual por jogador.
    // O binding transforma isso em uma lista Python plana.
    return impl_->strategies;
}

// ============================================================
// 🔁 MÉTRICAS ANTI-LOOP
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
    for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
        const auto metrics = impl_->anti_loop_engines[i].get_metrics();
        result[i].execution_attempts = metrics.execution_attempts;
        result[i].execution_blocks = metrics.execution_blocks;
        result[i].blocked_reverse = metrics.blocked_reverse;
        result[i].blocked_oscillation = metrics.blocked_oscillation;
        result[i].blocked_explicit = metrics.blocked_explicit;
        result[i].blocked_bench_board_loop = metrics.blocked_bench_board_loop;
        result[i].blocked_cycle = metrics.blocked_cycle;
        result[i].board_moves_executed = metrics.board_moves_executed;
        result[i].bench_to_board_executed = metrics.bench_to_board_executed;
    }
    return result;
}

// ============================================================
// 🌐 ESTADO PÚBLICO DOS JOGADORES
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

    // O contrato Python começa com round=1 e round_index=0.
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
// 📏 DIMENSÃO DAS OBSERVAÇÕES
// ============================================================

std::size_t TFTEngine::observation_dim() const noexcept {
    return kObservationDim;
}

// ============================================================
// 🆔 IDENTIFICADOR DO EPISÓDIO
// ============================================================

std::uint64_t TFTEngine::episode_id() const noexcept {
    return impl_ ? impl_->episode_id : 0;
}

// ============================================================
// 🔢 RODADA
// ============================================================

std::uint32_t TFTEngine::round() const noexcept {
    return impl_ ? impl_->round : 0;
}

// ============================================================
// 🎚️ ESTÁGIO
// ============================================================

std::uint32_t TFTEngine::stage() const noexcept {
    return impl_ ? impl_->stage : 1;
}

// ============================================================
// 👥 JOGADORES VIVOS
// ============================================================

std::int32_t TFTEngine::alive_players() const noexcept {
    return impl_ ? impl_->alive_players : 0;
}

// ============================================================
// 🏁 ESTADO DE ENCERRAMENTO
// ============================================================

bool TFTEngine::is_done() const noexcept {
    return !impl_ || impl_->done || impl_->closed;
}

std::int32_t TFTEngine::pool_available(
    std::int32_t champion_internal_id
) const {
    if (!impl_ || !impl_->pool) {
        throw std::runtime_error("UnitPool indisponivel.");
    }

    return impl_->pool->available(champion_internal_id);
}

std::int32_t TFTEngine::pool_initial_count(
    std::int32_t champion_internal_id
) const {
    if (!impl_ || !impl_->pool) {
        throw std::runtime_error("UnitPool indisponivel.");
    }

    return impl_->pool->initial_count(champion_internal_id);
}

std::int64_t TFTEngine::pool_total_available() const {
    if (!impl_ || !impl_->pool) {
        throw std::runtime_error("UnitPool indisponivel.");
    }

    return impl_->pool->total_available();
}

// ============================================================
// 🧹 FECHAMENTO
// ============================================================

void TFTEngine::close() noexcept {
    if (!impl_) {
        return;
    }

    impl_->closed = true;
}

} // namespace tft
