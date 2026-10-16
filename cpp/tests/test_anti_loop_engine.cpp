#include "decision/AntiLoopEngine.hpp"

#include <cassert>
#include <cstdint>
#include <string>

using namespace tft::decision;

namespace {

UnitIdentity make_unit(
    const std::string& uuid,
    std::int64_t id
) {
    UnitIdentity unit;
    unit.uuid = uuid;
    unit.id = id;
    unit.star = 1;
    return unit;
}

PositionSignature make_signature(
    const UnitIdentity& unit,
    std::size_t board_position
) {
    PositionSignature signature;
    signature.board.at(board_position) = unit;
    return signature;
}

// ---------------------------------------------------------
// Reversões e movimentos repetidos
// ---------------------------------------------------------

void test_blocks_reverse_move_for_same_unit() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.register_move("board_move", 4, 12, nasus);

    assert(engine.is_reverse_move("board_move", 12, 4, nasus));
    assert(engine.should_block_move("board_move", 12, 4, nasus));
    assert(
        engine.get_block_reason("board_move", 12, 4, nasus)
        == std::optional<std::string>{"reverse"}
    );
}

void test_blocks_reverse_swap_with_different_unit_identity() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);
    const auto teemo = make_unit("teemo-1", 2);

    engine.register_move("board_swap", 3, 10, nasus);

    // Um swap reverso é identificado pelo par de posições,
    // mesmo que a outra unidade esteja agora na posição de origem.
    assert(engine.is_reverse_move("board_swap", 10, 3, teemo));
    assert(engine.should_block_move("board_swap", 10, 3, teemo));
}

void test_blocks_explicitly_repeated_move() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.block_move("board_move", 4, 12, nasus);

    assert(engine.is_move_blocked("board_move", 4, 12, nasus));
    assert(engine.should_block_move("board_move", 4, 12, nasus));
    assert(
        engine.get_block_reason("board_move", 4, 12, nasus)
        == std::optional<std::string>{"explicit"}
    );
}

// ---------------------------------------------------------
// Oscilações
// ---------------------------------------------------------

void test_detects_repeated_position_oscillation() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    // Histórico: 4 -> 12 -> 4 -> 12.
    engine.register_move("board_move", 4, 12, nasus);
    engine.register_move("board_move", 12, 4, nasus);
    engine.register_move("board_move", 4, 12, nasus);

    // A tentativa 12 -> 4 repetiria a oscilação.
    assert(engine.is_oscillating(nasus, 12, 4, "board_move"));
    assert(engine.should_block_move("board_move", 12, 4, nasus));
    assert(
        engine.get_block_reason("board_move", 12, 4, nasus)
        == std::optional<std::string>{"reverse"}
    );
}

void test_detects_bench_board_oscillation() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.register_move("MOVE_BENCH_TO_BOARD", 2, 12, nasus);
    engine.register_move("MOVE_BOARD_TO_BENCH", 12, 2, nasus);

    assert(
        engine.is_bench_board_loop(
            nasus,
            "MOVE_BENCH_TO_BOARD",
            2,
            12
        )
    );

    assert(
        engine.should_block_move(
            "MOVE_BENCH_TO_BOARD",
            2,
            12,
            nasus
        )
    );
}

// ---------------------------------------------------------
// Ciclos
// ---------------------------------------------------------

void test_allows_first_cycle_closure() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.register_move("board_move", 3, 10, nasus);
    engine.register_move("board_move", 10, 12, nasus);

    // Ainda não houve um ciclo completo no histórico.
    assert(!engine.is_cycle_move("board_move", 12, 3, nasus));
}

void test_blocks_persistent_three_position_cycle() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    // Primeira volta: 3 -> 10 -> 12 -> 3.
    engine.register_move("board_move", 3, 10, nasus);
    engine.register_move("board_move", 10, 12, nasus);
    engine.register_move("board_move", 12, 3, nasus);

    // Repetição parcial do mesmo percurso.
    engine.register_move("board_move", 3, 10, nasus);
    engine.register_move("board_move", 10, 12, nasus);

    assert(engine.is_cycle_move("board_move", 12, 3, nasus));
    assert(engine.should_block_move("board_move", 12, 3, nasus));
    assert(
        engine.get_block_reason("board_move", 12, 3, nasus)
            .has_value()
    );
}

void test_allows_move_to_new_position_after_cycle() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.register_move("board_move", 3, 10, nasus);
    engine.register_move("board_move", 10, 12, nasus);
    engine.register_move("board_move", 12, 3, nasus);
    engine.register_move("board_move", 3, 10, nasus);
    engine.register_move("board_move", 10, 12, nasus);

    // O destino 15 não fecha o ciclo anterior.
    assert(!engine.is_cycle_move("board_move", 12, 15, nasus));
}

// ---------------------------------------------------------
// Movimentos semelhantes de unidades diferentes
// ---------------------------------------------------------

void test_different_units_have_independent_move_histories() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);
    const auto teemo = make_unit("teemo-1", 2);

    engine.register_move("board_move", 4, 12, nasus);

    // Um movimento semelhante de outra unidade não é reversão
    // nem bloqueio explícito do movimento do Nasus.
    assert(!engine.is_reverse_move("board_move", 12, 4, teemo));
    assert(!engine.should_block_move("board_move", 5, 13, teemo));

    engine.register_move("board_move", 3, 10, nasus);
    engine.register_move("board_move", 10, 12, nasus);

    // O histórico de ciclo do Nasus não deve bloquear o Teemo.
    assert(!engine.is_cycle_move("board_move", 12, 3, teemo));
}

void test_same_move_by_different_unit_is_not_explicitly_blocked() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);
    const auto teemo = make_unit("teemo-1", 2);

    engine.block_move("board_move", 4, 12, nasus);

    assert(engine.is_move_blocked("board_move", 4, 12, nasus));
    assert(!engine.is_move_blocked("board_move", 4, 12, teemo));
}

// ---------------------------------------------------------
// Mudanças de estado e histórico
// ---------------------------------------------------------

void test_state_change_releases_explicit_move_block() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    const auto original_state = make_signature(nasus, 3);
    const auto changed_state = make_signature(nasus, 4);

    engine.register_state(original_state);
    engine.block_move("board_move", 4, 12, nasus);

    assert(engine.is_move_blocked("board_move", 4, 12, nasus));

    // Registrar um novo estado deve tornar inativo o bloqueio
    // vinculado à assinatura anterior.
    engine.register_state(changed_state);

    assert(!engine.is_move_blocked("board_move", 4, 12, nasus));
}

void test_move_queries_do_not_mutate_history() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.register_move("board_move", 4, 12, nasus);

    const auto before = engine.get_state();

    (void)engine.should_block_move("board_move", 12, 4, nasus);
    (void)engine.get_block_reason("board_move", 12, 4, nasus);
    (void)engine.is_cycle_move("board_move", 12, 4, nasus);

    const auto after = engine.get_state();

    assert(before.move_history_size == after.move_history_size);
    assert(before.history_size == after.history_size);
    assert(before.blocked_moves == after.blocked_moves);
}

// ---------------------------------------------------------
// Regressão: troca repetida entre duas unidades bench <-> board
// ---------------------------------------------------------

void test_blocks_bench_board_replacement_oscillation_between_units() {
    AntiLoopEngine engine;
    const auto veigar = make_unit("veigar-1", 1);
    const auto nasus = make_unit("nasus-1", 2);

    // A primeira ação coloca Veigar no board e desloca Nasus para o bench.
    engine.register_move("bench_to_board", 2, 12, veigar);

    // O mesmo slot do bench e a mesma posição do board agora trocariam
    // Nasus por Veigar novamente. É a reversão observada nos logs:
    // Veigar <-> Nasus, depois Nasus <-> Veigar.
    assert(engine.should_block_move("bench_to_board", 2, 12, nasus));

    // Mesmo que uma chamada defeituosa tenha executado a troca, a próxima
    // tentativa de alternar as mesmas duas unidades também deve ser bloqueada.
    engine.register_move("bench_to_board", 2, 12, nasus);
    assert(engine.should_block_move("bench_to_board", 2, 12, veigar));
}

void test_reset_preserves_execution_metrics_like_python() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);
    engine.record_execution_attempt();
    engine.record_execution_block("reverse");
    engine.record_successful_move("board_move");
    engine.reset();

    const auto metrics = engine.get_metrics();
    assert(metrics.execution_attempts == 1);
    assert(metrics.execution_blocks == 1);
    assert(metrics.blocked_reverse == 1);
    assert(metrics.board_moves_executed == 1);
    const auto state = engine.get_state();
    assert(state.move_history_size == 0);
    (void)nasus;
}

void test_reset_clears_move_and_state_history() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);

    engine.register_move("board_move", 4, 12, nasus);
    engine.register_state(make_signature(nasus, 3));

    engine.reset();

    const auto state = engine.get_state();

    assert(state.move_history_size == 0);
    assert(state.history_size == 0);
    assert(state.blocked_moves == 0);
    assert(!state.last_move.has_value());
}

} // namespace

int main() {
    test_blocks_reverse_move_for_same_unit();
    test_blocks_reverse_swap_with_different_unit_identity();
    test_blocks_explicitly_repeated_move();

    test_detects_repeated_position_oscillation();
    test_detects_bench_board_oscillation();
    test_blocks_bench_board_replacement_oscillation_between_units();

    test_allows_first_cycle_closure();
    test_blocks_persistent_three_position_cycle();
    test_allows_move_to_new_position_after_cycle();

    test_different_units_have_independent_move_histories();
    test_same_move_by_different_unit_is_not_explicitly_blocked();

    test_state_change_releases_explicit_move_block();
    test_move_queries_do_not_mutate_history();
    test_reset_clears_move_and_state_history();
    test_reset_preserves_execution_metrics_like_python();

    return 0;
}