
#include <algorithm>
#include <cstdint>
#include <optional>
#include <vector>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "lobby/TFTEngine.hpp"

namespace py = pybind11;
using tft::PlayerActionMasks;
using tft::TFTLobbyEngine;

namespace {

template <std::size_t N>
py::array_t<bool> mask_1d(
    const std::array<std::uint8_t, N>& source
) {
    py::array_t<bool> result(N);
    auto output = result.mutable_unchecked<1>();

    for (py::ssize_t i = 0; i < static_cast<py::ssize_t>(N); ++i) {
        output(i) = source[static_cast<std::size_t>(i)] != 0;
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

    auto output = result.mutable_unchecked<2>();

    for (py::ssize_t row = 0; row < Rows; ++row) {
        for (py::ssize_t col = 0; col < Cols; ++col) {
            output(row, col) =
                source[static_cast<std::size_t>(row * Cols + col)] != 0;
        }
    }

    return result;
}

py::dict masks_to_dict(const PlayerActionMasks& masks) {
    py::dict result;

    result["type_mask"] = mask_1d(masks.type_mask);
    result["shop_mask"] = mask_1d(masks.shop_mask);
    result["bench_source_mask"] = mask_1d(masks.bench_source_mask);
    result["board_target_mask"] = mask_1d(masks.board_target_mask);
    result["board_source_mask"] = mask_1d(masks.board_source_mask);

    result["board_move_target_masks"] =
        mask_2d<28, 28>(masks.board_move_target_masks);

    result["bench_move_source_mask"] =
        mask_1d(masks.bench_move_source_mask);

    result["bench_to_board_target_masks"] =
        mask_2d<9, 28>(masks.bench_to_board_target_masks);

    return result;
}

py::list masks_to_list(
    const std::array<PlayerActionMasks, 8>& masks
) {
    py::list result;

    for (const auto& mask : masks) {
        result.append(masks_to_dict(mask));
    }

    return result;
}

py::array_t<float> observations_to_array(
    const std::vector<float>& values,
    std::size_t observation_dim
) {
    if (values.size() != 8 * observation_dim) {
        throw std::runtime_error(
            "Dimensao das observacoes inconsistente."
        );
    }

    py::array_t<float> result({
        static_cast<py::ssize_t>(8),
        static_cast<py::ssize_t>(observation_dim)
    });

    std::copy(
        values.begin(),
        values.end(),
        result.mutable_data()
    );

    return result;
}

py::dict reset_to_dict(const tft::ResetResult& reset) {
    py::dict result;

    result["observations"] =
        observations_to_array(
            reset.observations,
            reset.observation_dim
        );

    result["action_masks"] = masks_to_list(reset.action_masks);
    result["episode_id"] = reset.episode_id;
    result["observation_dim"] = reset.observation_dim;

    return result;
}

py::dict step_to_dict(const tft::StepResult& step) {
    py::dict result;

    result["observations"] =
        observations_to_array(
            step.observations,
            step.observation_dim
        );

    py::array_t<float> rewards(8);
    py::array_t<bool> dones(8);

    auto reward_output = rewards.mutable_unchecked<1>();
    auto done_output = dones.mutable_unchecked<1>();

    for (py::ssize_t i = 0; i < 8; ++i) {
        reward_output(i) = step.rewards[i];
        done_output(i) = step.dones[i] != 0;
    }

    py::dict info;
    info["round"] = step.round;
    info["alive_players"] = step.alive_players;

    result["rewards"] = std::move(rewards);
    result["dones"] = std::move(dones);
    result["lobby_done"] = step.lobby_done;
    result["action_masks"] = masks_to_list(step.action_masks);
    result["info"] = std::move(info);

    return result;
}

}  // namespace

PYBIND11_MODULE(tft_engine, module) {
    module.doc() = "Motor C++ nativo da lobby TFT";

    py::class_<TFTLobbyEngine>(module, "TFTLobby")
        .def(
            py::init<std::uint64_t>(),
            py::arg("seed") = 0
        )
        .def(
            "reset",
            [](TFTLobbyEngine& self, py::object seed) {
                std::optional<std::uint64_t> parsed_seed;

                if (!seed.is_none()) {
                    parsed_seed = seed.cast<std::uint64_t>();
                }

                return reset_to_dict(self.reset(parsed_seed));
            },
            py::arg("seed") = py::none()
        )
        .def(
            "step",
            [](TFTLobbyEngine& self,
               const std::vector<std::vector<std::int32_t>>& raw) {
                if (raw.size() != 8) {
                    throw py::value_error(
                        "actions precisa conter 8 jogadores."
                    );
                }

                std::array<tft::PlayerAction, 8> actions{};

                for (std::size_t player = 0; player < 8; ++player) {
                    if (raw[player].size() != 6) {
                        throw py::value_error(
                            "Cada acao precisa conter 6 componentes."
                        );
                    }

                    for (std::size_t component = 0; component < 6; ++component) {
                        actions[player].values[component] =
                            raw[player][component];
                    }
                }

                return step_to_dict(self.step(actions));
            },
            py::arg("actions")
        )
        .def(
            "get_action_masks",
            [](const TFTLobbyEngine& self) {
                return masks_to_list(self.get_action_masks());
            }
        )
        .def_property_readonly(
            "observation_dim",
            &TFTLobbyEngine::observation_dim
        )
        .def_property_readonly(
            "episode_id",
            &TFTLobbyEngine::episode_id
        )
        .def_property_readonly(
            "round",
            &TFTLobbyEngine::round
        )
        .def_property_readonly(
            "is_done",
            &TFTLobbyEngine::is_done
        )
        .def("close", &TFTLobbyEngine::close);
}
