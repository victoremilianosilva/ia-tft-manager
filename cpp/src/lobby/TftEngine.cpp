
#include "lobby/TftEngine.hpp"

#include <algorithm>
#include <stdexcept>
#include <utility>

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
PlayerActionMasks make_default_masks() {
    PlayerActionMasks masks{};

    masks.type_mask[6] = 1;

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

    Impl() {
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
            player.gold = 0;
            player.level = 1;
            player.xp = 0;

            player.alive = true;
            player.eliminated = false;

            player.wins = 0;
            player.losses = 0;

            player.placement = std::nullopt;
            player.opponent_id = std::nullopt;

            player.damage_taken = 0.0f;

            players[i] = player;
            masks[i] = make_default_masks();

            strategies[i].clear();
            strategies[i].push_back(StrategyInfo{});

            anti_loop_metrics[i] = AntiLoopMetrics{};
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
                round,
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
};

// ============================================================
// 🏗️ CONSTRUTOR E DESTRUTOR
// ============================================================

TFTEngine::TFTEngine(std::uint64_t seed)
    : impl_(std::make_unique<Impl>()) {
    impl_->seed = seed;
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
    // 2. Avançar o estado provisório
    // --------------------------------------------------------
    //
    // Este é apenas um avanço de contrato.
    // Nenhuma ação de jogo é executada nesta etapa.
    // --------------------------------------------------------

    ++impl_->round;

    impl_->stage =
        ((impl_->round - 1) / kRoundsPerStage) + 1;

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
    result.round = impl_->round;
    result.stage = impl_->stage;
    result.alive_players = impl_->alive_players;

    result.events.emplace_back(
        "Etapa 1: step executado em modo esqueleto; "
        "as acoes ainda nao alteram o jogo."
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

    // As métricas ficam zeradas até a integração com
    // o motor real de decisão e movimentação.
    return impl_->anti_loop_metrics;
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
