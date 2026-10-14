#include "lobby/TftEngine.hpp"

#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

void require(bool condition, const std::string& message) {
    if (!condition) {
        throw std::runtime_error(message);
    }
}

struct PendingReverse {
    bool active{false};
    std::int32_t source{-1};
    std::int32_t target{-1};
};

tft::PlayerAction choose_action(
    const tft::PlayerActionMasks& masks,
    PendingReverse& pending_reverse
) {
    tft::PlayerAction action{};
    action.values = {6, 0, 0, 0, 0, 0}; // PASS seguro.

    // Tenta reverter um movimento de tabuleiro executado no passo anterior.
    // A tentativa é intencional: o AntiLoop deve bloqueá-la sem corromper estado.
    if (pending_reverse.active && masks.type_mask[4] == 1) {
        action.values = {
            4, 0, 0, 0,
            pending_reverse.target,
            pending_reverse.source
        };
        pending_reverse.active = false;
        return action;
    }
    pending_reverse.active = false;

    // Prioriza colocar unidades compradas no tabuleiro.
    if (masks.type_mask[3] == 1) {
        for (std::int32_t source = 0;
             source < static_cast<std::int32_t>(tft::kBenchSlots);
             ++source) {
            for (std::int32_t target = 0;
                 target < static_cast<std::int32_t>(tft::kBoardSlots);
                 ++target) {
                const auto index = static_cast<std::size_t>(
                    source * static_cast<std::int32_t>(tft::kBoardSlots)
                    + target
                );
                if (masks.bench_to_board_target_masks[index] == 1) {
                    action.values = {3, 0, source, target, 0, 0};
                    return action;
                }
            }
        }
    }

    // Compra uma oferta permitida pela máscara.
    if (masks.type_mask[0] == 1) {
        for (std::int32_t slot = 0;
             slot < static_cast<std::int32_t>(tft::kShopSlots);
             ++slot) {
            if (masks.shop_mask[static_cast<std::size_t>(slot)] == 1) {
                action.values = {0, slot, 0, 0, 0, 0};
                return action;
            }
        }
    }

    // Move uma unidade no tabuleiro para provocar tentativas reversas
    // controladas e exercitar a proteção anti-loop durante a simulação.
    if (masks.type_mask[4] == 1) {
        for (std::int32_t source = 0;
             source < static_cast<std::int32_t>(tft::kBoardSlots);
             ++source) {
            if (masks.board_source_mask[static_cast<std::size_t>(source)] != 1) {
                continue;
            }
            for (std::int32_t target = 0;
                 target < static_cast<std::int32_t>(tft::kBoardSlots);
                 ++target) {
                const auto index = static_cast<std::size_t>(
                    source * static_cast<std::int32_t>(tft::kBoardSlots)
                    + target
                );
                if (masks.board_move_target_masks[index] == 1) {
                    action.values = {4, 0, 0, 0, source, target};
                    pending_reverse = {true, source, target};
                    return action;
                }
            }
        }
    }

    return action;
}

} // namespace

int main(int argc, char** argv) {
    try {
        require(argc == 2, "Informe o caminho de units_gerado.json.");
        const std::string catalog_path = argv[1];

        std::uint64_t total_combat_events = 0;
        std::uint64_t total_rounds = 0;
        std::uint64_t total_blocks = 0;
        std::uint64_t total_attempts = 0;
        std::uint64_t total_wins = 0;
        std::uint64_t total_losses = 0;

        // Seeds fixas tornam falhas reproduzíveis.
        for (const std::uint64_t seed : {17ULL, 2026ULL, 99173ULL}) {
            tft::TFTEngine engine(seed, catalog_path);
            std::array<PendingReverse, tft::kPlayersPerLobby> pending{};

            for (std::uint32_t turn = 0;
                 turn < 60 && !engine.is_done();
                 ++turn) {
                const auto masks = engine.get_action_masks();
                std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};

                for (std::size_t player = 0;
                     player < tft::kPlayersPerLobby;
                     ++player) {
                    actions[player] = choose_action(masks[player], pending[player]);
                }

                const auto result = engine.step(actions);
                ++total_rounds;

                for (const auto& event : result.events) {
                    if (event.rfind("COMBAT:", 0) == 0) {
                        ++total_combat_events;
                    }
                }

                for (std::size_t player = 0;
                     player < tft::kPlayersPerLobby;
                     ++player) {
                    require(std::isfinite(result.players[player].hp),
                            "HP não finito após resolução de combate.");
                    require(result.players[player].hp >= 0.0f,
                            "HP ficou negativo após combate.");
                    require(std::isfinite(result.rewards[player]),
                            "Recompensa não finita após combate.");

                    total_wins += static_cast<std::uint64_t>(
                        result.players[player].wins);
                    total_losses += static_cast<std::uint64_t>(
                        result.players[player].losses);
                }
            }

            const auto metrics = engine.get_anti_loop_metrics();
            for (const auto& metric : metrics) {
                total_attempts += metric.execution_attempts;
                total_blocks += metric.execution_blocks;
            }
        }

        require(total_rounds >= 90,
                "A simulação terminou cedo demais para ser um soak test.");
        require(total_combat_events > 0,
                "Nenhum combate PVP foi integrado/executado durante o teste.");
        require(total_attempts > 0,
                "O teste não executou tentativas de movimentação.");
        require(total_blocks > 0,
                "O teste não observou nenhum bloqueio anti-loop.");
        require(total_wins > 0 && total_losses > 0,
                "Os resultados de combate não foram propagados para os jogadores.");

        std::cout
            << "TFT combat + anti-loop soak: OK\n"
            << "rounds=" << total_rounds
            << ", combats=" << total_combat_events
            << ", move_attempts=" << total_attempts
            << ", move_blocks=" << total_blocks
            << ", wins=" << total_wins
            << ", losses=" << total_losses << '\n';
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "TFT combat + anti-loop soak: FAILED: "
                  << error.what() << '\n';
        return 1;
    }
}
