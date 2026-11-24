#include "lobby/TftEngine.hpp"

#include <nlohmann/json.hpp>

#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
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

    // Se uma bigorna estiver aberta, resolver a escolha primeiro. O head 7
    // também serve para equipar itens, mas com alvo sentinela 0 e opção válida
    // a engine interpreta a ação como escolha da bigorna pendente.
    if (masks.type_mask[7] == 1 &&
        masks.item_inventory_mask[0] == 1 &&
        masks.item_target_mask[0] == 1) {
        action.values = {7, 0, 0, 0, 0, 0};
        pending_reverse.active = false;
        return action;
    }

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

    return action;
}

} // namespace

int main(int argc, char** argv) {
    try {
#if defined(_WIN32)
        if (_putenv_s("TFT_COMBAT_REPLAY_MODE", "audit") != 0) {
            throw std::runtime_error("Não foi possível habilitar o modo audit de replay.");
        }
#else
        if (setenv("TFT_COMBAT_REPLAY_MODE", "audit", 1) != 0) {
            throw std::runtime_error("Não foi possível habilitar o modo audit de replay.");
        }
#endif
        require(argc == 2, "Informe o caminho de units_gerado.json.");
        const std::string catalog_path = argv[1];

        std::uint64_t total_combat_events = 0;
        std::uint64_t total_simulation_artifacts = 0;
        std::uint64_t total_linked_simulation_outcomes = 0;
        std::uint64_t total_rounds = 0;
        std::uint64_t total_blocks = 0;
        std::uint64_t total_attempts = 0;
        std::uint64_t total_wins = 0;
        std::uint64_t total_losses = 0;

        // Seeds fixas tornam falhas reproduzíveis.
        for (const std::uint64_t seed : {17ULL, 2026ULL, 99173ULL}) {
            tft::TFTEngine engine(seed, catalog_path);
            std::array<PendingReverse, tft::kPlayersPerLobby> pending{};
            std::array<std::int32_t, tft::kPlayersPerLobby> previous_wins{};
            std::array<std::int32_t, tft::kPlayersPerLobby> previous_losses{};

            for (std::uint32_t turn = 0;
                 turn < 240 && !engine.is_done();
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
                    } else if (event.rfind("COMBAT_SIMULATION_REPLAY_V1:", 0) == 0) {
                        const auto artifact = nlohmann::json::parse(
                            event.substr(std::string("COMBAT_SIMULATION_REPLAY_V1:").size()));
                        require(artifact.value("schema_version", 0) == 1,
                                "Simulation replay artifact schema version is missing.");
                        require(artifact.value("authoritative_game_replay", true) == false,
                                "Native simulation trace was mislabeled as an authoritative replay.");
                        require(artifact.value("calibration_eligible", true) == false,
                                "Native simulation trace became calibration eligible.");
                        require(artifact.contains("player_a_units") &&
                                artifact.contains("player_b_units") &&
                                artifact.contains("result"),
                                "Simulation replay artifact is missing input/result data.");
                        ++total_simulation_artifacts;
                    } else if (event.rfind("COMBAT_OUTCOME_V1:", 0) == 0) {
                        const auto outcome = nlohmann::json::parse(
                            event.substr(std::string("COMBAT_OUTCOME_V1:").size()));
                        require(outcome.value("calibration_eligible", true) == false,
                                "Combat outcome became calibration eligible without an authoritative replay.");
                        require(outcome.value("authoritative_game_replay", true) == false &&
                                outcome.value("observation_scope", "") == "native_lobby_simulation",
                                "Native outcome was mislabeled as an authoritative game replay.");
                        require(outcome["replay_artifact_id"].is_null() &&
                                outcome["dataset_version"].is_null(),
                                "Native simulation artifact leaked into authoritative replay fields.");
                        if (outcome.contains("simulation_artifact_id") &&
                            outcome["simulation_artifact_id"].is_string()) {
                            require(outcome.value("simulation_dataset_version", "").size() > 0,
                                    "Linked simulation artifact has no dataset schema version.");
                            ++total_linked_simulation_outcomes;
                        }
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

                    require(result.players[player].wins >= previous_wins[player],
                            "Contador de vitórias regrediu durante a partida.");
                    require(result.players[player].losses >= previous_losses[player],
                            "Contador de derrotas regrediu durante a partida.");
                    total_wins += static_cast<std::uint64_t>(
                        result.players[player].wins - previous_wins[player]);
                    total_losses += static_cast<std::uint64_t>(
                        result.players[player].losses - previous_losses[player]);
                    previous_wins[player] = result.players[player].wins;
                    previous_losses[player] = result.players[player].losses;
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
        require(total_simulation_artifacts > 0,
                "Nenhum artefato de replay do simulador nativo foi emitido.");
        require(total_linked_simulation_outcomes > 0,
                "Nenhum resultado de combate foi ligado ao artefato do simulador.");
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
