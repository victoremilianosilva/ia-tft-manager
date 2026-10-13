
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "decision/AntiLoopEngine.hpp"
#include "decision/DecisionEngine.hpp"
#include "decision/ActionMaskEngine.hpp"

namespace py = pybind11;

using namespace tft::decision;

PYBIND11_MODULE(decision_engine, module) {
    module.doc() = "TFT Decision Engine and AntiLoop Engine";

    // =========================================================
    // Identidade e estado das unidades
    // =========================================================

    py::class_<UnitIdentity>(module, "UnitIdentity")
        .def(py::init<>())
        .def_readwrite("uuid", &UnitIdentity::uuid)
        .def_readwrite("id", &UnitIdentity::id)
        .def_readwrite("star", &UnitIdentity::star)
        .def("has_identity", &UnitIdentity::has_identity);

    py::class_<UnitSnapshot>(module, "UnitSnapshot")
        .def(py::init<>())
        .def_readwrite("identity", &UnitSnapshot::identity)
        .def_readwrite("cost", &UnitSnapshot::cost)
        .def_readwrite("available", &UnitSnapshot::available);

    py::class_<EconomyState>(module, "EconomyState")
        .def(py::init<>())
        .def_readwrite("gold", &EconomyState::gold)
        .def_readwrite("level", &EconomyState::level)
        .def_readwrite("current_xp", &EconomyState::current_xp)
        .def_readwrite("max_level", &EconomyState::max_level)
        .def_readwrite(
            "xp_to_next_level",
            &EconomyState::xp_to_next_level
        )
        .def_readwrite("reroll_cost", &EconomyState::reroll_cost)
        .def_readwrite(
            "xp_purchase_cost",
            &EconomyState::xp_purchase_cost
        );

    py::class_<PlayerState>(module, "PlayerState")
        .def(py::init<>())
        .def_readwrite("player_id", &PlayerState::player_id)
        .def_readwrite("is_alive", &PlayerState::is_alive)
        .def_readwrite("economy", &PlayerState::economy)
        .def_readwrite("board", &PlayerState::board)
        .def_readwrite("bench", &PlayerState::bench)
        .def_readwrite("shop", &PlayerState::shop)
        .def(
            "has_free_board_slot",
            &PlayerState::has_free_board_slot
        )
        .def(
            "has_free_bench_slot",
            &PlayerState::has_free_bench_slot
        );

    // =========================================================
    // Tipos usados no histórico
    // =========================================================

    py::class_<PositionSignature>(module, "PositionSignature")
        .def(py::init<>())
        .def_readwrite("board", &PositionSignature::board)
        .def_readwrite("bench", &PositionSignature::bench);

    py::class_<MoveRecord>(module, "MoveRecord")
        .def(py::init<>())
        .def_readwrite("move_type", &MoveRecord::move_type)
        .def_readwrite("source", &MoveRecord::source)
        .def_readwrite("target", &MoveRecord::target)
        .def_readwrite("unit", &MoveRecord::unit);

    py::class_<MoveKey>(module, "MoveKey")
        .def(py::init<>())
        .def_readwrite("move_type", &MoveKey::move_type)
        .def_readwrite("source", &MoveKey::source)
        .def_readwrite("target", &MoveKey::target)
        .def_readwrite(
            "unit_identity",
            &MoveKey::unit_identity
        );

    py::class_<AntiLoopConfig>(module, "AntiLoopConfig")
        .def(py::init<>())
        .def_readwrite(
            "history_size",
            &AntiLoopConfig::history_size
        )
        .def_readwrite(
            "blocked_move_size",
            &AntiLoopConfig::blocked_move_size
        )
        .def_readwrite(
            "loop_threshold",
            &AntiLoopConfig::loop_threshold
        );

    py::class_<StateRegistrationResult>(
        module,
        "StateRegistrationResult"
    )
        .def_readonly(
            "signature",
            &StateRegistrationResult::signature
        )
        .def_readonly(
            "repeated",
            &StateRegistrationResult::repeated
        )
        .def_readonly(
            "visits",
            &StateRegistrationResult::visits
        );

    py::class_<AntiLoopStateSummary>(
        module,
        "AntiLoopStateSummary"
    )
        .def_readonly(
            "history_size",
            &AntiLoopStateSummary::history_size
        )
        .def_readonly(
            "move_history_size",
            &AntiLoopStateSummary::move_history_size
        )
        .def_readonly(
            "blocked_moves",
            &AntiLoopStateSummary::blocked_moves
        )
        .def_readonly(
            "known_states",
            &AntiLoopStateSummary::known_states
        )
        .def_readonly(
            "last_move",
            &AntiLoopStateSummary::last_move
        );

    py::class_<ExecutionMetrics>(module, "ExecutionMetrics")
        .def_readonly(
            "execution_attempts",
            &ExecutionMetrics::execution_attempts
        )
        .def_readonly(
            "execution_blocks",
            &ExecutionMetrics::execution_blocks
        )
        .def_readonly(
            "blocked_reverse",
            &ExecutionMetrics::blocked_reverse
        )
        .def_readonly(
            "blocked_oscillation",
            &ExecutionMetrics::blocked_oscillation
        )
        .def_readonly(
            "blocked_explicit",
            &ExecutionMetrics::blocked_explicit
        )
        .def_readonly(
            "blocked_bench_board_loop",
            &ExecutionMetrics::blocked_bench_board_loop
        )
        .def_readonly(
            "blocked_cycle",
            &ExecutionMetrics::blocked_cycle
        )
        .def_readonly(
            "board_moves_executed",
            &ExecutionMetrics::board_moves_executed
        )
        .def_readonly(
            "bench_to_board_executed",
            &ExecutionMetrics::bench_to_board_executed
        );

    // =========================================================
    // AntiLoopEngine
    // =========================================================

    py::class_<AntiLoopEngine>(module, "AntiLoopEngine")
        .def(
            py::init<AntiLoopConfig>(),
            py::arg("config") = AntiLoopConfig{}
        )
        .def("reset", &AntiLoopEngine::reset)

        .def(
            "make_move_key",
            &AntiLoopEngine::make_move_key,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "make_board_signature",
            &AntiLoopEngine::make_board_signature,
            py::arg("state")
        )

        .def(
            "register_state",
            &AntiLoopEngine::register_state,
            py::arg("signature")
        )
        .def(
            "register_move",
            &AntiLoopEngine::register_move,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "block_move",
            &AntiLoopEngine::block_move,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )

        .def(
            "is_move_blocked",
            &AntiLoopEngine::is_move_blocked,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "is_reverse_move",
            &AntiLoopEngine::is_reverse_move,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "is_oscillating",
            &AntiLoopEngine::is_oscillating,
            py::arg("unit"),
            py::arg("source"),
            py::arg("target"),
            py::arg("move_type") = std::nullopt
        )
        .def(
            "is_bench_board_loop",
            &AntiLoopEngine::is_bench_board_loop,
            py::arg("unit"),
            py::arg("move_type") = std::nullopt,
            py::arg("source") = std::nullopt,
            py::arg("target") = std::nullopt
        )
        .def(
            "is_cycle_move",
            &AntiLoopEngine::is_cycle_move,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "get_block_reason",
            &AntiLoopEngine::get_block_reason,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "should_block_move",
            &AntiLoopEngine::should_block_move,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )
        .def(
            "evaluate_move_risk",
            &AntiLoopEngine::evaluate_move_risk,
            py::arg("move_type"),
            py::arg("source"),
            py::arg("target"),
            py::arg("unit") = std::nullopt
        )

        .def(
            "was_state_seen",
            &AntiLoopEngine::was_state_seen,
            py::arg("signature")
        )
        .def(
            "get_state_visits",
            &AntiLoopEngine::get_state_visits,
            py::arg("signature")
        )
        .def("get_state", &AntiLoopEngine::get_state)
        .def("get_metrics", &AntiLoopEngine::get_metrics)
        .def("clear_old_blocks", &AntiLoopEngine::clear_old_blocks)

        .def(
            "record_execution_attempt",
            &AntiLoopEngine::record_execution_attempt
        )
        .def(
            "record_execution_block",
            &AntiLoopEngine::record_execution_block,
            py::arg("reason")
        )
        .def(
            "record_successful_move",
            &AntiLoopEngine::record_successful_move,
            py::arg("move_type")
        );

    // =========================================================
    // DecisionEngine existente
    // =========================================================

    py::class_<DecisionEngine>(module, "DecisionEngine")
        .def(py::init<>())
        .def("version", &DecisionEngine::version);

    
py::class_<ActionMaskBatch>(module, "ActionMaskBatch")
    .def_readonly("type_mask", &ActionMaskBatch::type_mask)
    .def_readonly("shop_mask", &ActionMaskBatch::shop_mask)
    .def_readonly(
        "bench_source_mask",
        &ActionMaskBatch::bench_source_mask
    )
    .def_readonly(
        "board_target_mask",
        &ActionMaskBatch::board_target_mask
    )
    .def_readonly(
        "board_source_mask",
        &ActionMaskBatch::board_source_mask
    )
    .def_readonly(
        "board_move_target_masks",
        &ActionMaskBatch::board_move_target_masks
    )
    .def_readonly(
        "bench_move_source_mask",
        &ActionMaskBatch::bench_move_source_mask
    )
    .def_readonly(
        "bench_to_board_target_masks",
        &ActionMaskBatch::bench_to_board_target_masks
    )
    .def_readonly("buy_available", &ActionMaskBatch::buy_available)
    .def_readonly("sell_available", &ActionMaskBatch::sell_available)
    .def_readonly(
        "board_move_available",
        &ActionMaskBatch::board_move_available
    )
    .def_readonly(
        "bench_move_available",
        &ActionMaskBatch::bench_move_available
    );

py::class_<ActionMaskEngine>(module, "ActionMaskEngine")
    .def(py::init<>())
    .def(
        "generate_masks",
        &ActionMaskEngine::generate_masks,
        py::arg("state"),
        py::arg("anti_loop"),
        py::arg("include_board_target") = true
    );
}