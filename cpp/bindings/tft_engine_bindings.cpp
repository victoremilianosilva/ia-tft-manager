
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
#include "strategy/PositioningEngine.hpp"
#include "reward/RewardManager.hpp"
#include "combat/CombatProfileEngine.hpp"
#include "strategy/SynergyEngine.hpp"

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

    result["player_id"] = player.player_id;
    result["hp"] = player.hp;
    result["gold"] = player.gold;
    result["level"] = player.level;
    result["xp"] = player.xp;

    result["alive"] = player.alive;
    result["eliminated"] = player.eliminated;

    result["wins"] = player.wins;
    result["losses"] = player.losses;

    result["placement"] = player.placement.has_value()
        ? py::cast(*player.placement)
        : py::none();

    result["opponent_id"] = player.opponent_id.has_value()
        ? py::cast(*player.opponent_id)
        : py::none();

    result["damage_taken"] = player.damage_taken;

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
    py::array_t<float> action_rewards(8);
    py::array_t<float> combat_rewards(8);
    py::array_t<float> placement_rewards(8);
    py::array_t<bool> dones(8);

    auto reward_out = rewards.mutable_unchecked<1>();
    auto action_reward_out = action_rewards.mutable_unchecked<1>();
    auto combat_reward_out = combat_rewards.mutable_unchecked<1>();
    auto placement_reward_out = placement_rewards.mutable_unchecked<1>();
    auto done_out = dones.mutable_unchecked<1>();

    for (py::ssize_t i = 0; i < 8; ++i) {
        const auto index = static_cast<std::size_t>(i);
        reward_out(i) = step.rewards[index];
        action_reward_out(i) = step.action_rewards[index];
        combat_reward_out(i) = step.combat_rewards[index];
        placement_reward_out(i) = step.placement_rewards[index];
        done_out(i) = step.dones[index] != 0;
    }

    result["rewards"] = std::move(rewards);
    result["action_rewards"] = std::move(action_rewards);
    result["combat_rewards"] = std::move(combat_rewards);
    result["placement_rewards"] = std::move(placement_rewards);
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
        std::vector<tft::StrategyInfo>,
        tft::kPlayersPerLobby
    >& strategies
) {
    py::list result;

    // Uma estratégia atual por jogador.
    for (const auto& player_strategies : strategies) {
        py::dict item;

        if (player_strategies.empty()) {
            item["strategy"] = 0;
            item["strategy_name"] = "ECON";
            item["previous_strategy"] = py::none();
            item["confidence"] = 0.0f;
            item["strategy_age"] = 0;
            item["reason"] = "";
            item["changed"] = false;
            item["state_confidence"] = 0.0f;
            item["best_scored_strategy"] = 0;
            item["strategy_scores"] = py::dict();
            item["board_power"] = 0.0;
            item["bench_strength"] = 0.0;
            item["active_traits_count"] = 0;
            item["composition_focus"] = "";
            item["composition_focus_id"] = -1;
            item["composition_direction"] = "";
            item["core_units"] = py::list();
            item["core_unit_ids"] = py::list();
            item["core_traits"] = py::list();
            item["active_traits"] = py::dict();
            item["unit_counts"] = py::dict();
            item["unit_counts_by_id"] = py::dict();
        } else {
            const auto& strategy = player_strategies.back();

            item["strategy"] = strategy.strategy;
            item["strategy_name"] = strategy.strategy_name;

            item["previous_strategy"] =
                strategy.previous_strategy.has_value()
                    ? py::cast(*strategy.previous_strategy)
                    : py::none();

            item["confidence"] = strategy.confidence;
            item["strategy_age"] = strategy.strategy_age;
            item["reason"] = strategy.reason;
            item["changed"] = strategy.changed;
            item["state_confidence"] = strategy.state_confidence;
            item["best_scored_strategy"] = strategy.best_scored_strategy;
            py::dict strategy_scores;
            for (const auto& [strategy_id, score] : strategy.strategy_scores)
                strategy_scores[py::int_(strategy_id)] = score;
            item["strategy_scores"] = std::move(strategy_scores);
            item["board_power"] = strategy.board_power;
            item["bench_strength"] = strategy.bench_strength;
            item["active_traits_count"] = strategy.active_traits_count;
            item["composition_focus"] = strategy.composition_focus;
            item["composition_focus_id"] = strategy.composition_focus_id;
            item["composition_direction"] = strategy.composition_direction;
            item["core_units"] = strategy.core_units;
            item["core_unit_ids"] = strategy.core_unit_ids;
            item["core_traits"] = strategy.core_traits;
            py::dict active_traits;
            for (const auto& [trait, count] : strategy.active_traits)
                active_traits[py::str(trait)] = count;
            item["active_traits"] = std::move(active_traits);
            py::dict unit_counts;
            for (const auto& [unit_id, count] : strategy.unit_counts)
                unit_counts[py::str(unit_id)] = count;
            item["unit_counts"] = std::move(unit_counts);
            py::dict unit_counts_by_id;
            for (const auto& [unit_id, count] : strategy.unit_counts_by_id) unit_counts_by_id[py::int_(unit_id)] = count;
            item["unit_counts_by_id"] = std::move(unit_counts_by_id);
        }

        result.append(std::move(item));
    }

    return result;
}


py::dict public_state_to_dict(const tft::PublicState& state) {
    py::dict result;

    result["stage"] = state.stage;
    result["round"] = state.round;
    result["round_index"] = state.round_index;
    result["finished"] = state.finished;

    result["winner_id"] = state.winner_id.has_value()
        ? py::cast(*state.winner_id)
        : py::none();

    result["ranking"] = state.ranking;

    py::list alive_players;
    for (const auto player_id : state.alive_players) {
        alive_players.append(player_id);
    }
    result["alive_players"] = std::move(alive_players);

    result["players"] = player_info_to_list(state.players);

    return result;
}


py::dict anti_loop_to_dict(
    const std::array<
        tft::AntiLoopMetrics,
        tft::kPlayersPerLobby
    >& metrics
) {
    py::dict result;

    std::uint64_t execution_attempts = 0;
    std::uint64_t execution_blocks = 0;
    std::uint64_t blocked_reverse = 0;
    std::uint64_t blocked_oscillation = 0;
    std::uint64_t blocked_explicit = 0;
    std::uint64_t blocked_bench_board_loop = 0;
    std::uint64_t blocked_cycle = 0;
    std::uint64_t board_moves_executed = 0;
    std::uint64_t bench_to_board_executed = 0;
    std::uint64_t mask_board_move_candidates = 0;
    std::uint64_t mask_board_move_valid = 0;
    std::uint64_t mask_board_move_blocked_anti_loop = 0;
    std::uint64_t mask_board_move_blocked_seen_state = 0;
    std::uint64_t mask_bench_move_candidates = 0;
    std::uint64_t mask_bench_move_valid = 0;
    std::uint64_t mask_bench_move_blocked_anti_loop = 0;
    std::uint64_t mask_blocked_reverse = 0;
    std::uint64_t mask_blocked_oscillation = 0;
    std::uint64_t mask_blocked_explicit = 0;
    std::uint64_t mask_blocked_bench_board_loop = 0;
    std::uint64_t mask_blocked_cycle = 0;

    for (const auto& metric : metrics) {
        execution_attempts += metric.execution_attempts;
        execution_blocks += metric.execution_blocks;
        blocked_reverse += metric.blocked_reverse;
        blocked_oscillation += metric.blocked_oscillation;
        blocked_explicit += metric.blocked_explicit;
        blocked_bench_board_loop += metric.blocked_bench_board_loop;
        blocked_cycle += metric.blocked_cycle;
        board_moves_executed += metric.board_moves_executed;
        bench_to_board_executed += metric.bench_to_board_executed;
        mask_board_move_candidates += metric.mask_board_move_candidates;
        mask_board_move_valid += metric.mask_board_move_valid;
        mask_board_move_blocked_anti_loop += metric.mask_board_move_blocked_anti_loop;
        mask_board_move_blocked_seen_state += metric.mask_board_move_blocked_seen_state;
        mask_bench_move_candidates += metric.mask_bench_move_candidates;
        mask_bench_move_valid += metric.mask_bench_move_valid;
        mask_bench_move_blocked_anti_loop += metric.mask_bench_move_blocked_anti_loop;
        mask_blocked_reverse += metric.mask_blocked_reverse;
        mask_blocked_oscillation += metric.mask_blocked_oscillation;
        mask_blocked_explicit += metric.mask_blocked_explicit;
        mask_blocked_bench_board_loop += metric.mask_blocked_bench_board_loop;
        mask_blocked_cycle += metric.mask_blocked_cycle;
    }

    result["execution_attempts"] = execution_attempts;
    result["execution_blocks"] = execution_blocks;
    result["blocked_reverse"] = blocked_reverse;
    result["blocked_oscillation"] = blocked_oscillation;
    result["blocked_explicit"] = blocked_explicit;
    result["blocked_bench_board_loop"] = blocked_bench_board_loop;
    result["blocked_cycle"] = blocked_cycle;
    result["board_moves_executed"] = board_moves_executed;
    result["bench_to_board_executed"] = bench_to_board_executed;
    result["mask_board_move_candidates"] = mask_board_move_candidates;
    result["mask_board_move_valid"] = mask_board_move_valid;
    result["mask_board_move_blocked_anti_loop"] = mask_board_move_blocked_anti_loop;
    result["mask_board_move_blocked_seen_state"] = mask_board_move_blocked_seen_state;
    result["mask_bench_move_candidates"] = mask_bench_move_candidates;
    result["mask_bench_move_valid"] = mask_bench_move_valid;
    result["mask_bench_move_blocked_anti_loop"] = mask_bench_move_blocked_anti_loop;
    result["mask_blocked_reverse"] = mask_blocked_reverse;
    result["mask_blocked_oscillation"] = mask_blocked_oscillation;
    result["mask_blocked_explicit"] = mask_blocked_explicit;
    result["mask_blocked_bench_board_loop"] = mask_blocked_bench_board_loop;
    result["mask_blocked_cycle"] = mask_blocked_cycle;

    return result;
}


}  // namespace

PYBIND11_MODULE(tft_engine, module) {

    py::class_<tft::SynergyEngine>(module, "SynergyManagerNative")
        .def(py::init<tft::TraitMilestones>(), py::arg("milestones") = tft::TraitMilestones{})
        .def("set_state", &tft::SynergyEngine::set_state,
             py::arg("active_traits"), py::arg("partial_traits") = tft::TraitCounts{})
        .def("calculate_multiplier", [](const tft::SynergyEngine& self, py::object active) {
            if (active.is_none()) return self.calculate_multiplier();
            const auto parsed = active.cast<tft::TraitCounts>();
            return self.calculate_multiplier(&parsed);
        }, py::arg("active_traits") = py::none())
        .def("get_all_multipliers", [](const tft::SynergyEngine& self, py::object active) {
            if (active.is_none()) return self.get_all_multipliers();
            const auto parsed = active.cast<tft::TraitCounts>();
            return self.get_all_multipliers(&parsed);
        }, py::arg("active_traits") = py::none())
        .def("get_trait_level", &tft::SynergyEngine::get_trait_level,
             py::arg("trait_name"), py::arg("count"))
        .def("get_unit_synergy_bonus", [](const tft::SynergyEngine& self,
                                          const std::vector<std::string>& traits,
                                          py::object focus) {
            if (focus.is_none()) return self.get_unit_synergy_bonus(traits);
            const auto parsed = focus.cast<tft::TraitFocus>();
            return self.get_unit_synergy_bonus(traits, &parsed);
        }, py::arg("unit_traits"), py::arg("comp_focus") = py::none());

    py::class_<tft::RewardManager>(module, "RewardManager")
        .def(py::init<>())
        .def("reset", &tft::RewardManager::reset)
        .def("calculate_combat_reward", &tft::RewardManager::calculate_combat_reward,
             py::arg("won"), py::arg("damage_dealt")=0.0, py::arg("damage_taken")=0.0,
             py::arg("enemy_alive")=0, py::arg("own_alive")=0)
        .def("calculate_power_reward", &tft::RewardManager::calculate_power_reward)
        .def("calculate_synergy_reward", &tft::RewardManager::calculate_synergy_reward)
        .def("calculate_positioning_reward", &tft::RewardManager::calculate_positioning_reward)
        .def("calculate_level_reward", &tft::RewardManager::calculate_level_reward)
        .def("calculate_economy_reward", &tft::RewardManager::calculate_economy_reward,
             py::arg("gold"), py::arg("level"), py::arg("hp"))
        .def("calculate_streak_reward", &tft::RewardManager::calculate_streak_reward)
        .def("calculate_board_reward", &tft::RewardManager::calculate_board_reward)
        .def("calculate_action_reward", &tft::RewardManager::calculate_action_reward,
             py::arg("action_type"), py::arg("action_success"), py::arg("action_value")=0.0)
        .def("calculate_total_reward", &tft::RewardManager::calculate_total_reward,
             py::arg("combat_reward")=0.0, py::arg("power_reward")=0.0,
             py::arg("synergy_reward")=0.0, py::arg("positioning_reward")=0.0,
             py::arg("level_reward")=0.0, py::arg("economy_reward")=0.0,
             py::arg("streak_reward")=0.0, py::arg("board_reward")=0.0,
             py::arg("action_reward")=0.0)
        .def("get_state", [](const tft::RewardManager& self) {
            const auto st=self.get_state();
            py::dict d;
            d["previous_board_power"]=st.previous_board_power;
            d["previous_positioning_score"]=st.previous_positioning_score;
            d["previous_synergy_score"]=st.previous_synergy_score;
            d["previous_level"]=st.previous_level;
            d["previous_gold"]=st.previous_gold;
            d["last_combat_reward"]=st.last_combat_reward;
            d["round_reward"]=st.round_reward;
            d["total_reward"]=st.total_reward;
            return d;
        });

    module.doc() =
        "API Python do motor nativo de simulacao TFT.";

    // Contrato mínimo consumido pelo wrapper PPO:
    // reset -> step -> máscaras/diagnósticos de treino -> close.
    // Estado interno, hooks de fixture e consultas de implementação não
    // atravessam a fronteira Python/C++.
    py::class_<TFTEngine>(module, "TFTLobby")
        .def(
            py::init<std::uint64_t, std::string>(),
            py::arg("seed") = 0,
            py::arg("catalog_path") = ""
        )
        .def(
            "reset",
            [](TFTEngine& self, py::object seed) {
                std::optional<std::uint64_t> parsed_seed;
                if (!seed.is_none()) {
                    if (!py::isinstance<py::int_>(seed) || PyBool_Check(seed.ptr())) {
                        throw py::type_error(
                            "seed deve ser um inteiro nao negativo ou None."
                        );
                    }
                    try {
                        parsed_seed = seed.cast<std::uint64_t>();
                    } catch (const py::cast_error&) {
                        throw py::value_error(
                            "seed deve estar entre 0 e 18446744073709551615."
                        );
                    }
                }
                return reset_to_dict(self.reset(parsed_seed));
            },
            py::arg("seed") = py::none()
        )
        .def(
            "step",
            [](TFTEngine& self,
               const std::vector<std::vector<std::int32_t>>& raw_actions,
               bool timer_enabled,
               bool timer_expired) {
                if (raw_actions.size() != tft::kPlayersPerLobby) {
                    throw py::value_error("actions deve conter 8 jogadores.");
                }

                std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};
                for (std::size_t player = 0; player < tft::kPlayersPerLobby; ++player) {
                    if (raw_actions[player].size() != tft::kActionComponents) {
                        throw py::value_error(
                            "Cada acao deve conter 6 componentes."
                        );
                    }
                    for (std::size_t component = 0;
                         component < tft::kActionComponents;
                         ++component) {
                        actions[player].values[component] =
                            raw_actions[player][component];
                    }
                }
                return step_to_dict(self.step(actions, timer_enabled, timer_expired));
            },
            py::arg("actions"),
            py::arg("timer_enabled") = false,
            py::arg("timer_expired") = false
        )
        .def(
            "get_audit_snapshot",
            [](const TFTEngine& self) {
                const auto snapshot = self.get_audit_snapshot();
                py::dict result;
                result["round"] = snapshot.round;
                result["stage"] = snapshot.stage;
                result["finished"] = snapshot.finished;
                py::list players;
                const auto unit_to_dict = [](const tft::AuditUnitSnapshot& unit) {
                    py::dict d;
                    d["occupied"] = unit.occupied;
                    d["champion_id"] = unit.champion_id;
                    d["uuid"] = unit.uuid;
                    d["star"] = unit.star;
                    d["cost"] = unit.cost;
                    return d;
                };
                for (const auto& player : snapshot.players) {
                    py::dict p;
                    p["player_id"] = player.player_id;
                    p["gold"] = player.gold;
                    p["level"] = player.level;
                    p["xp"] = player.xp;
                    p["win_streak"] = player.win_streak;
                    p["loss_streak"] = player.loss_streak;
                    py::list board, bench, shop;
                    for (const auto& unit : player.board) board.append(unit_to_dict(unit));
                    for (const auto& unit : player.bench) bench.append(unit_to_dict(unit));
                    for (const auto& unit : player.shop) shop.append(unit_to_dict(unit));
                    p["board"] = board;
                    p["bench"] = bench;
                    p["shop"] = shop;
                    p["action_masks"] = masks_to_dict(player.masks);
                    players.append(p);
                }
                result["players"] = players;
                return result;
            }
        )
        .def(
            "get_action_masks",
            [](const TFTEngine& self) {
                return masks_to_list(self.get_action_masks());
            }
        )
        .def(
            "get_strategies",
            [](const TFTEngine& self) {
                return strategies_to_list(self.get_strategies());
            }
        )
        .def(
            "get_anti_loop_metrics",
            [](const TFTEngine& self) {
                return anti_loop_to_dict(self.get_anti_loop_metrics());
            }
        )
        // Contrato público de diagnóstico e fixtures de paridade.
        // Não faz parte do caminho de execução normal do Trainer.
        .def(
            "get_public_state",
            [](const TFTEngine& self) {
                return public_state_to_dict(self.get_public_state());
            }
        )
        .def("get_unit_comp_score", &TFTEngine::get_unit_comp_score,
             py::arg("player_id"), py::arg("champion_api_name"),
             py::arg("star") = 1)
        .def("is_core_unit", &TFTEngine::is_core_unit,
             py::arg("player_id"), py::arg("champion_api_name"))
        .def("is_core_trait", &TFTEngine::is_core_trait,
             py::arg("player_id"), py::arg("trait"))
        .def("set_unit_for_testing", &TFTEngine::set_unit_for_testing,
             py::arg("player_id"), py::arg("on_board"), py::arg("slot"),
             py::arg("champion_api_name"), py::arg("star") = 1)
        .def("set_player_alive_for_testing", &TFTEngine::set_player_alive_for_testing,
             py::arg("player_id"), py::arg("alive"))
        .def("set_player_economy_for_testing", &TFTEngine::set_player_economy_for_testing,
             py::arg("player_id"), py::arg("gold"), py::arg("level"), py::arg("xp"))
        .def("set_shop_offer_for_testing", &TFTEngine::set_shop_offer_for_testing,
             py::arg("player_id"), py::arg("slot"), py::arg("champion_api_name"))
        .def("set_next_shop_roll_for_testing", &TFTEngine::set_next_shop_roll_for_testing,
             py::arg("player_id"), py::arg("champion_api_names"))
        .def("pool_available", &TFTEngine::pool_available, py::arg("champion_internal_id"))
        .def("pool_initial_count", &TFTEngine::pool_initial_count, py::arg("champion_internal_id"))
        .def("pool_total_available", &TFTEngine::pool_total_available)
        .def_property_readonly("observation_dim", &TFTEngine::observation_dim)
        .def_property_readonly("episode_id", &TFTEngine::episode_id)
        .def_property_readonly("round", &TFTEngine::round)
        .def_property_readonly("stage", &TFTEngine::stage)
        .def_property_readonly("alive_players", &TFTEngine::alive_players)
        .def_property_readonly("is_done", &TFTEngine::is_done)
        .def("close", &TFTEngine::close);


    // CombatProfileManager.py parity API. This is deliberately stateless:
    // Python's mutable profile cache remains a Python lifecycle detail.
    module.def("combat_profile_get_profile", [](py::dict unit) {
        auto numeric = [&unit](const char* key, double fallback = 0.0) {
            if (!unit.contains(key) || unit[key].is_none()) return fallback;
            try { return py::cast<double>(unit[key]); } catch (...) { return fallback; }
        };
        auto text_value = [](py::handle value) -> std::string {
            if (py::isinstance<py::str>(value)) return py::cast<std::string>(value);
            return {};
        };
        std::string ability_text;
        if (unit.contains("ability")) {
            py::handle ability = unit["ability"];
            if (py::isinstance<py::str>(ability)) ability_text = text_value(ability);
            else if (py::isinstance<py::dict>(ability)) {
                py::dict d = py::reinterpret_borrow<py::dict>(ability);
                for (const char* key : {"description", "desc", "name", "effect"}) {
                    if (d.contains(key) && py::isinstance<py::str>(d[key])) {
                        ability_text = text_value(d[key]); break;
                    }
                }
            }
        }
        if (ability_text.empty()) {
            for (const char* key : {"ability_description", "ability_desc", "description"}) {
                if (unit.contains(key) && py::isinstance<py::str>(unit[key])) {
                    ability_text = text_value(unit[key]); break;
                }
            }
        }
        const double hp = numeric("max_hp", numeric("hp", 0.0));
        const double ad = numeric("attack_damage", numeric("ad", 0.0));
        const double mr = numeric("magic_resist", numeric("mr", 0.0));
        tft::CombatProfileInput input{ability_text, numeric("attack_range"), numeric("attack_speed"),
            ad, numeric("armor"), mr, hp, numeric("max_mana")};
        const auto p = tft::CombatProfileEngine::build_profile(input);
        const int role = static_cast<int>(p.role);
        py::dict out;
        out["role"] = role;
        out["role_name"] = std::array<const char*,5>{"tank","carry","support","fighter","assassin"}[role];
        out["frontline"] = p.frontline();
        out["backline"] = p.backline();
        out["is_tank"] = role == 0;
        out["is_carry"] = role == 1;
        out["is_support"] = role == 2;
        out["is_fighter"] = role == 3;
        out["is_assassin"] = role == 4;
        out["attack_range"] = p.attack_range;
        out["attack_speed"] = p.attack_speed;
        out["attack_damage"] = p.attack_damage;
        out["armor"] = p.armor;
        out["magic_resist"] = p.magic_resist;
        out["max_hp"] = p.max_hp;
        out["max_mana"] = p.max_mana;
        return out;
    });
    module.def("combat_profile_get_role", [](py::object unit) {
        if (unit.is_none()) return 3;
        py::dict d = py::cast<py::dict>(unit);
        auto p = py::cast<py::dict>(py::module_::import("tft_engine").attr("combat_profile_get_profile")(d));
        return py::cast<int>(p["role"]);
    });
    module.def("combat_profile_is_frontline", [](py::object unit) {
        if (unit.is_none()) return true;
        const int role = py::cast<int>(py::module_::import("tft_engine").attr("combat_profile_get_role")(unit));
        return tft::CombatProfileEngine::is_frontline(static_cast<tft::ProfileRole>(role));
    });
    module.def("combat_profile_is_backline", [](py::object unit) {
        if (unit.is_none()) return false;
        const int role = py::cast<int>(py::module_::import("tft_engine").attr("combat_profile_get_role")(unit));
        return tft::CombatProfileEngine::is_backline(static_cast<tft::ProfileRole>(role));
    });
    module.def("combat_profile_build_combat_input", [](py::dict unit) {
        auto numeric = [&unit](const char* key, double fallback = 0.0) {
            if (!unit.contains(key) || unit[key].is_none()) return fallback;
            try { return py::cast<double>(unit[key]); } catch (...) { return fallback; }
        };
        auto identifier = [&unit]() -> py::object {
            for (const char* key : {"id", "champion_id", "apiName", "characterName"})
                if (unit.contains(key) && !unit[key].is_none()) return py::reinterpret_borrow<py::object>(unit[key]);
            return py::none();
        };
        py::dict profile = py::cast<py::dict>(
            py::module_::import("tft_engine").attr("combat_profile_get_profile")(unit));
        py::dict out;
        out["id"] = identifier();
        int star = 1;
        try { if (unit.contains("star")) star = py::cast<int>(unit["star"]); } catch (...) {}
        out["star"] = star;
        out["hp"] = numeric("hp", py::cast<double>(profile["max_hp"]));
        out["max_hp"] = profile["max_hp"];
        out["mana"] = numeric("mana");
        out["max_mana"] = profile["max_mana"];
        out["attack_damage"] = profile["attack_damage"];
        out["attack_speed"] = profile["attack_speed"];
        out["armor"] = profile["armor"];
        out["magic_resist"] = profile["magic_resist"];
        out["attack_range"] = profile["attack_range"];
        out["role"] = profile["role"];
        return out;
    });

    // PositioningManager.py parity API. Boards are vectors of role IDs:
    // -1 = empty; 0 tank, 1 carry, 2 support, 3 fighter, 4 assassin.
    module.def("positioning_is_valid_position", &tft::PositioningEngine::is_valid_position);
    module.def("positioning_position_to_row_col", [](int p) { auto v=tft::PositioningEngine::position_to_row_col(p); return py::make_tuple(v.first,v.second); });
    module.def("positioning_row_col_to_position", &tft::PositioningEngine::row_col_to_position);
    module.def("positioning_get_neighbors", &tft::PositioningEngine::get_neighbors, py::arg("position"), py::arg("include_diagonal")=true);
    module.def("positioning_evaluate_unit_placement", &tft::PositioningEngine::evaluate_unit_placement, py::arg("board"), py::arg("position"), py::arg("candidate_role")=-2);
    module.def("positioning_evaluate_protection", &tft::PositioningEngine::evaluate_protection);
    module.def("positioning_evaluate_board_positioning", &tft::PositioningEngine::evaluate_board_positioning);
    module.def("positioning_find_best_position", [](const std::vector<int>& board,int role,const std::vector<int>& candidates) { auto v=tft::PositioningEngine::find_best_position(board,role,candidates); return py::make_tuple(v.first,v.second); }, py::arg("board"),py::arg("role"),py::arg("candidate_positions")=std::vector<int>{});
    module.def("positioning_find_best_swap", [](const std::vector<int>& board,int source,const std::vector<int>& candidates) { auto v=tft::PositioningEngine::find_best_swap(board,source,candidates); return py::make_tuple(v.first,v.second); }, py::arg("board"),py::arg("source_position"),py::arg("candidate_positions")=std::vector<int>{});
    module.def("positioning_is_board_stable", &tft::PositioningEngine::is_board_stable, py::arg("board"),py::arg("tolerance")=0.01);
    module.def("positioning_get_normalized_score", &tft::PositioningEngine::get_normalized_positioning_score);
}
