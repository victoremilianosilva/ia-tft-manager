#ifdef NDEBUG
#undef NDEBUG
#endif

#include "decision/AntiLoopEngine.hpp"

#include <cassert>
#include <cstdint>
#include <string>
#include <stdexcept>

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

    const auto lissandra = make_unit("lissandra-1", 2);
    // The executor records a replacement as bench_to_board and stores the
    // displaced unit, rather than emitting a separate board_to_bench action.
    engine.register_move("MOVE_BENCH_TO_BOARD", 2, 12, lissandra, nasus);

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

void test_blocks_candidate_closing_loop_after_unit_revisits_position() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-cycle", 1);
    const auto teemo = make_unit("teemo-interleaved", 2);

    // Nasus revisits slot 3 (0 -> 3 -> 5 -> 3). Teemo's moves are
    // interleaved and must not reset Nasus's trajectory.
    engine.register_move("board_move", 0, 3, nasus);
    engine.register_move("board_move", 1, 4, teemo);
    engine.register_move("board_move", 3, 5, nasus);
    engine.register_move("board_move", 4, 6, teemo);
    engine.register_move("board_move", 5, 3, nasus);
    engine.register_move("board_move", 6, 7, teemo);

    // Returning Nasus from 3 to 0 would repeat the path after the prior
    // revisit; the first, not-yet-repeated cycle closure remains allowed.
    assert(engine.is_cycle_move("board_move", 3, 0, nasus));
    assert(engine.should_block_move("board_move", 3, 0, nasus));
    assert(!engine.is_cycle_move("board_move", 3, 0, teemo));
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
    const auto lissandra = make_unit("lissandra-1", 1);
    const auto nasus = make_unit("nasus-1", 2);

    constexpr std::int32_t bench_slot = 2;
    constexpr std::int32_t board_position = 12;
    const std::string move_type = "bench_to_board";

    // Reproduz deterministicamente o padrão do log:
    // Lissandra <-> Nasus -> Nasus <-> Lissandra -> ...
    // A primeira troca é legítima; a segunda inverteria imediatamente
    // o par de unidades nos mesmos slots e precisa ser bloqueada.
    const UnitIdentity* sequence[] = {
        &lissandra, &nasus, &lissandra, &nasus, &lissandra
    };

    bool loop_was_blocked = false;

    for (std::size_t i = 0; i < (sizeof(sequence) / sizeof(sequence[0])); ++i) {
        const auto& unit = *sequence[i];
        const bool blocked = engine.should_block_move(
            move_type, bench_slot, board_position, unit
        );

        if (i == 0) {
            // Não bloquear a primeira ação legítima.
            if (blocked) {
                throw std::runtime_error(
                    "AntiLoop blocked the first legitimate bench-to-board move"
                );
            }
            // Lissandra entra no board e desloca Nasus para o bench.
            engine.register_move(
                move_type, bench_slot, board_position, unit, nasus
            );
            continue;
        }

        // A partir da segunda ação, permitir a troca inicia a oscilação.
        // A asserção falha imediatamente se o AntiLoop deixar o loop passar.
        if (!blocked) {
            throw std::runtime_error(
                "AntiLoop allowed a bench/board replacement oscillation"
            );
        }
        loop_was_blocked = true;
        if (blocked) {
            break;
        }

        engine.register_move(move_type, bench_slot, board_position, unit);
    }

    // O teste só é bem-sucedido se a sequência for interrompida pelo bloqueio.
    if (!loop_was_blocked) {
        throw std::runtime_error(
            "AntiLoop did not block the reproducible bench/board oscillation"
        );
    }
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

void test_mask_diagnostics_accumulate_and_survive_reset() {
    AntiLoopEngine engine;
    MaskDiagnostics diagnostics;
    diagnostics.board_move_candidates = 12;
    diagnostics.board_move_valid = 8;
    diagnostics.board_move_blocked_anti_loop = 2;
    diagnostics.board_move_blocked_seen_state = 2;
    diagnostics.bench_move_candidates = 5;
    diagnostics.bench_move_valid = 4;
    diagnostics.bench_move_blocked_anti_loop = 1;
    diagnostics.blocked_cycle = 2;

    engine.record_mask_diagnostics(diagnostics);
    engine.reset();

    const auto metrics = engine.get_metrics();
    assert(metrics.mask.board_move_candidates == 12);
    assert(metrics.mask.board_move_valid == 8);
    assert(metrics.mask.board_move_blocked_anti_loop == 2);
    assert(metrics.mask.board_move_blocked_seen_state == 2);
    assert(metrics.mask.bench_move_candidates == 5);
    assert(metrics.mask.bench_move_valid == 4);
    assert(metrics.mask.bench_move_blocked_anti_loop == 1);
    assert(metrics.mask.blocked_cycle == 2);
}

void test_incremental_signature_hash_matches_full_recomputation() {
    const auto nasus = make_unit("nasus-1", 1);
    PositionSignature signature = make_signature(nasus, 3);
    const auto original_hash = PositionSignatureHash{}(signature);

    signature.swap_board_slots(3, 4);
    PositionSignature expected_board;
    expected_board.board[4] = nasus;
    const auto moved_hash = PositionSignatureHash{}(signature);
    const auto expected_hash = PositionSignatureHash{}(expected_board);
    assert(moved_hash == expected_hash);
    assert(moved_hash != original_hash);

    signature.bench[2] = make_unit("briar-1", 2);
    signature.hash_cached = false;
    const auto before_swap = PositionSignatureHash{}(signature);
    signature.swap_board_bench(4, 2);
    PositionSignature expected_replacement;
    expected_replacement.board[4] = make_unit("briar-1", 2);
    expected_replacement.bench[2] = nasus;
    const auto replacement_hash = PositionSignatureHash{}(signature);
    const auto expected_replacement_hash = PositionSignatureHash{}(expected_replacement);
    assert(replacement_hash == expected_replacement_hash);
    assert(replacement_hash != before_swap);
}

void test_round_window_expires_old_states_and_clears_local_history() {
    AntiLoopEngine engine;
    const auto nasus = make_unit("nasus-1", 1);
    const auto signature = make_signature(nasus, 3);
    engine.register_move("board_move", 3, 4, nasus);
    engine.block_move("board_move", 4, 12, nasus);
    engine.register_state(signature);

    engine.begin_round(2);
    assert(engine.get_state().move_history_size == 0);
    assert(engine.get_state().blocked_moves == 0);
    assert(!engine.get_state().last_move.has_value());
    assert(engine.was_state_seen(signature));

    // Keep exact layouts long enough to catch the observed round 21 -> 26 loop.
    engine.begin_round(9);
    assert(engine.was_state_seen(signature));
    engine.begin_round(10);
    assert(!engine.was_state_seen(signature));
    assert(engine.get_state_visits(signature) == 0);
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
    test_incremental_signature_hash_matches_full_recomputation();
    test_round_window_expires_old_states_and_clears_local_history();
    test_reset_clears_move_and_state_history();
    test_reset_preserves_execution_metrics_like_python();
    test_mask_diagnostics_accumulate_and_survive_reset();

    return 0;
}