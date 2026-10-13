
#include <algorithm>
#include <array>
#include <cstdint>
#include <optional>
#include <stdexcept>
#include <string>
#include <vector>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "lobby/TftEngine.hpp"

namespace py = pybind11;

namespace {

using tft::PlayerActionMasks;
using tft::TFTEngine;

template <std::size_t N>
py::array_t<bool> mask_1d(
    const std::array<std::uint8_t, N>& source
) {
    py::array_t<bool> result(
        static_cast<py::ssize_t>(N)
    );

    auto out = result.mutable_unchecked<1>();

    for (std::size_t i = 0; i < N; ++i) {
        out(static_cast<py::ssize_t>(i)) =
            source[i] != 0;
    }

    return result;
}

template <std::size_t Rows, std::size_t Cols>
py::array_t<bool> mask_2d(
    const std::array<std::uint8_t, Rows * Cols>& source
) {
    py::array_t<bool> result({
        static_cast<py::ssize_t>(Rows),
        static_cast<py::ssize_t>(Cols)
    });

    auto out = result.mutable_unchecked<2>();

    for (std::size_t row = 0; row < Rows; ++row) {
        for (std::size_t col = 0; col < Cols; ++col) {
            out(
                static_cast<py::ssize_t>(row),
                static_cast<py::ssize_t>(col)
            ) = source[row * Cols + col] != 0;
        }
    }

    return result;
}

py::dict masks_to_dict(const PlayerActionMasks& masks) {
    py::dict result;

    result["type_mask"] = mask_1d(masks.type_mask);
    result["shop_mask"] = mask_1d(masks.shop_mask);
    result["bench_source_mask"] =
        mask_1d(masks.bench_source_mask);
    result["board_target_mask"] =
        mask_1d(masks.board_target_mask);
    result["board_source_mask"] =
        mask_1d(masks.board_source_mask);

    result["board_move_target_masks"] =
        mask_2d<28, 28>(
            masks.board_move_target_masks
        );

    result["bench_move_source_mask"] =
        mask_1d(masks.bench_move_source_mask);

    result["bench_to_board_target_masks"] =
        mask_2d<9, 28>(
            masks.bench_to_board_target_masks
        );

    return result;
}

py::list masks_to_list(
    const std::array<PlayerActionMasks, 8>& masks
) {
    py::list result;

    for (const auto& masks_for_player : masks) {
        result.append(masks_to_dict(masks_for_player));
    }

    return result;
}

py::array_t<float> observations_to_array(
    const std::vector<float>& values,
    std::size_t observation_dim
) {
    const std::size_t expected =
        tft::kPlayersPerLobby * observation_dim;

    if (values.size() != expected) {
        throw std::runtime_error(
            "Quantidade de observacoes inconsistente."
        );
    }

    py::array_t<float> result({
        static_cast<py::ssize_t>(tft::kPlayersPerLobby),
        static_cast<py::ssize_t>(observation_dim)
    });

    std::copy(
        values.begin(),
        values.end(),
        result.mutable_data()
    );

    return result;
}

py::dict player_info_to_dict(const tft::PlayerInfo& player) {
    py::dict result;
    result["alive"] = player.alive;
    result["eliminated"] = player.eliminated;
    result["placement"] = player.placement;
    result["health"] = player.health;
    result["gold"] = player.gold;
    result["level"] = player.level;
    return result;
}

py::list player_info_to_list(
    const std::vector<tft::PlayerInfo>& players
) {
    py::list result;

    for (const auto& player : players) {
        result.append(player_info_to_dict(player));
    }

    return result;
}

py::dict reset_to_dict(const tft::ResetResult& reset) {
    py::dict result;

    result["observations"] = observations_to_array(
        reset.observations,
        reset.observation_dim
    );

    result["action_masks"] =
        masks_to_list(reset.action_masks);

    result["episode_id"] = reset.episode_id;
    result["observation_dim"] = reset.observation_dim;

    return result;
}

py::dict step_to_dict(const tft::StepResult& step) {
    py::dict result;

    result["observations"] = observations_to_array(
        step.observations,
        step.observation_dim
    );

    py::array_t<float> rewards(8);
    py::array_t<bool> dones(8);

    auto reward_out = rewards.mutable_unchecked<1>();
    auto done_out = dones.mutable_unchecked<1>();

    for (py::ssize_t i = 0; i < 8; ++i) {
        reward_out(i) = step.rewards[
            static_cast<std::size_t>(i)
        ];

        done_out(i) = step.dones[
            static_cast<std::size_t>(i)
        ] != 0;
    }

    result["rewards"] = std::move(rewards);
    result["dones"] = std::move(dones);
    result["lobby_done"] = step.lobby_done;
    result["episode_id"] = step.episode_id;
    result["round"] = step.round;
    result["stage"] = step.stage;
    result["alive_players"] = step.alive_players;
    result["action_masks"] = masks_to_list(step.action_masks);
    result["players"] = player_info_to_list(
        std::vector<tft::PlayerInfo>(
            step.players.begin(), step.players.end()
        )
    );
    result["events"] = step.events;

    return result;
}

py::list strategies_to_list(
    const std::array<
        std::vector<tft::StrategyInfo>, 8
    >& strategies
) {
    py::list result;

    for (const auto& player_strategies : strategies) {
        py::list player_list;

        for (const auto& strategy : player_strategies) {
            py::dict item;
            item["name"] = strategy.name;
            item["score"] = strategy.score;
            item["active"] = strategy.active;
            player_list.append(item);
        }

        result.append(player_list);
    }

    return result;
}

py::list anti_loop_to_list(
    const std::array<tft::AntiLoopMetrics, 8>& metrics
) {
    py::list result;

    for (const auto& metric : metrics) {
        py::dict item;
        item["repeated_states"] = metric.repeated_states;
        item["repeated_actions"] = metric.repeated_actions;
        item["blocked_moves"] = metric.blocked_moves;
        item["prevented_loops"] = metric.prevented_loops;
        result.append(item);
    }

    return result;
}

}  // namespace

PYBIND11_MODULE(tft_engine, module) {
    module.doc() =
        "API Python do motor nativo de simulacao TFT.";

    py::class_<TFTEngine>(module, "TFTLobby")
        .def(
            py::init<std::uint64_t>(),
            py::arg("seed") = 0
        )
        .def(
            "reset",
            [](TFTEngine& self, py::object seed) {
                std::optional<std::uint64_t> parsed_seed;

                if (!seed.is_none()) {
                    parsed_seed =
                        seed.cast<std::uint64_t>();
                }

                return reset_to_dict(
                    self.reset(parsed_seed)
                );
            },
            py::arg("seed") = py::none()
        )
        .def(
            "step",
            [](TFTEngine& self,
               const std::vector<
                   std::vector<std::int32_t>
               >& raw_actions) {
                if (raw_actions.size() != 8) {
                    throw py::value_error(
                        "actions deve conter 8 jogadores."
                    );
                }

                std::array<tft::PlayerAction, 8> actions{};

                for (std::size_t player = 0; player < 8; ++player) {
                    if (raw_actions[player].size() != 6) {
                        throw py::value_error(
                            "Cada acao deve conter 6 componentes."
                        );
                    }

                    for (std::size_t component = 0;
                         component < 6;
                         ++component) {
                        actions[player].values[component] =
                            raw_actions[player][component];
                    }
                }

                return step_to_dict(self.step(actions));
            },
            py::arg("actions")
        )
        .def(
            "get_action_masks",
            [](const TFTEngine& self) {
                return masks_to_list(
                    self.get_action_masks()
                );
            }
        )
        .def(
            "get_observations",
            [](const TFTEngine& self) {
                return observations_to_array(
                    self.get_observations(),
                    self.observation_dim()
                );
            }
        )
        .def(
            "get_strategies",
            [](const TFTEngine& self) {
                return strategies_to_list(
                    self.get_strategies()
                );
            }
        )
        .def(
            "get_anti_loop_metrics",
            [](const TFTEngine& self) {
                return anti_loop_to_list(
                    self.get_anti_loop_metrics()
                );
            }
        )
        .def(
            "get_public_state",
            [](const TFTEngine& self) {
                return player_info_to_list(
                    self.get_public_state()
                );
            }
        )
        .def_property_readonly(
            "observation_dim",
            &TFTEngine::observation_dim
        )
        .def_property_readonly(
            "episode_id",
            &TFTEngine::episode_id
        )
        .def_property_readonly(
            "round",
            &TFTEngine::round
        )
        .def_property_readonly(
            "stage",
            &TFTEngine::stage
        )
        .def_property_readonly(
            "alive_players",
            &TFTEngine::alive_players
        )
        .def_property_readonly(
            "is_done",
            &TFTEngine::is_done
        )
        .def("close", &TFTEngine::close);
}
