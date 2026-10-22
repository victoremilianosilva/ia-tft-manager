
#ifdef NDEBUG
#undef NDEBUG
#endif

#include "decision/ActionMaskEngine.hpp"
#include <cassert>
#include <stdexcept>
#include <string>
#include <utility>

using namespace tft::decision;

namespace {

UnitSnapshot make_unit(
    const char* uuid,
    std::uint8_t cost = 1
) {
    UnitSnapshot unit;
    unit.identity.uuid = uuid;
    unit.identity.star = 1;
    unit.cost = cost;
    unit.available = true;
    return unit;
}

void test_empty_state_keeps_pass_available() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto masks = engine.generate_masks(state, anti_loop);

    // PASS sempre deve estar disponível.
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::PASS)] == MASK_ENABLED);

    // Nenhuma ação econômica real está disponível.
    assert(!masks.buy_available);
    assert(!masks.sell_available);
    assert(!masks.board_move_available);
    assert(!masks.bench_move_available);
    // Fallbacks técnicos não contam como candidatos reais.
    assert(masks.diagnostics.board_move_candidates == 0);
    assert(masks.diagnostics.bench_move_candidates == 0);

    assert(masks.type_mask[static_cast<std::size_t>(ActionType::BUY)] == MASK_DISABLED);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::REROLL)] == MASK_DISABLED);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::BUY_XP)] == MASK_DISABLED);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::MOVE_BENCH)] == MASK_DISABLED);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::MOVE_BOARD)] == MASK_DISABLED);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::SELL)] == MASK_DISABLED);

    // Fallback técnico das cabeças categóricas.
    // O fallback não deve habilitar uma ação real.
    assert(masks.shop_mask[0] == MASK_ENABLED);
    assert(masks.bench_source_mask[0] == MASK_ENABLED);
    assert(masks.board_target_mask[0] == MASK_ENABLED);
    assert(masks.board_source_mask[0] == MASK_ENABLED);
}

void test_shop_mask_matches_python_offer_presence_semantics() {
    PlayerState state;
    state.economy.gold = 3;
    state.economy.level = 2;

    state.shop[0] = make_unit("cheap", 2);
    state.shop[1] = make_unit("expensive", 4);

    state.shop[2] = make_unit("unavailable", 1);
    state.shop[2]->available = false;

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.buy_available);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::BUY)] == MASK_ENABLED);

    assert(masks.shop_mask[0] == MASK_ENABLED);
    assert(masks.shop_mask[1] == MASK_DISABLED);
    // Python's current mask checks offer presence, affordability and bench space;
    // it does not filter the auxiliary `available` flag.
    assert(masks.shop_mask[2] == MASK_ENABLED);
}

void test_sell_uses_real_bench_units_not_fallback() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto empty_masks = engine.generate_masks(state, anti_loop);

    assert(!empty_masks.sell_available);
    assert(empty_masks.type_mask[static_cast<std::size_t>(ActionType::SELL)] == MASK_DISABLED);

    state.bench[4] = make_unit("bench-unit");

    const auto occupied_masks = engine.generate_masks(state, anti_loop);

    assert(occupied_masks.sell_available);
    assert(occupied_masks.type_mask[static_cast<std::size_t>(ActionType::SELL)] == MASK_ENABLED);
    assert(occupied_masks.bench_source_mask[4] == MASK_ENABLED);
}

void test_board_move_masks_respect_source_and_destination() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    state.board[3] = make_unit("board-unit");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.board_move_available);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::MOVE_BOARD)] == MASK_ENABLED);

    // A origem ocupada possui destinos válidos.
    assert(masks.board_source_mask[3] == MASK_ENABLED);

    // A matriz é condicionada pela origem selecionada.
    assert(masks.board_move_target_masks[3][3] == MASK_DISABLED);
    assert(masks.board_move_target_masks[3][4] == MASK_ENABLED);

    // Uma origem vazia não deve ter movimento real.
    assert(masks.board_move_target_masks[4][3] == MASK_DISABLED);
}

void test_bench_to_board_allows_replacement() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    state.bench[2] = make_unit("bench-unit");
    state.board[10] = make_unit("board-unit");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.bench_move_available);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::MOVE_BENCH)] == MASK_ENABLED);
    assert(masks.bench_move_source_mask[2] == MASK_ENABLED);

    // Uma das duas vagas de nível ainda está livre.
    assert(masks.bench_to_board_target_masks[2][11] == MASK_ENABLED);
    // Uma casa ocupada também é destino válido para substituição.
    assert(masks.bench_to_board_target_masks[2][10] == MASK_ENABLED);
}

void test_bench_to_board_masks_enforce_level_capacity_but_allow_swaps() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    state.bench[2] = make_unit("bench-unit");
    state.board[10] = make_unit("board-unit-a");
    state.board[11] = make_unit("board-unit-b");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.bench_move_available);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::MOVE_BENCH)] == MASK_ENABLED);
    assert(masks.bench_move_source_mask[2] == MASK_ENABLED);

    // A equipe já usa as duas vagas do nível: só pode substituir.
    assert(masks.bench_to_board_target_masks[2][10] == MASK_ENABLED);
    assert(masks.bench_to_board_target_masks[2][11] == MASK_ENABLED);
    assert(masks.bench_to_board_target_masks[2][12] == MASK_DISABLED);
}

void test_buy_is_disabled_when_bench_is_full() {
    PlayerState state;
    state.economy.gold = 20;
    state.economy.level = 2;
    state.shop[0] = make_unit("shop-unit", 1);

    for (std::size_t slot = 0; slot < BENCH_SIZE; ++slot) {
        state.bench[slot] = make_unit(("bench-" + std::to_string(slot)).c_str());
    }

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    assert(!masks.buy_available);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::BUY)] == MASK_DISABLED);
    assert(masks.shop_mask[0] == MASK_DISABLED);
}

void test_bench_to_board_can_replace_when_physical_grid_is_full() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;
    state.bench[0] = make_unit("bench-unit");

    for (std::size_t slot = 0; slot < BOARD_SIZE; ++slot) {
        state.board[slot] = make_unit(("board-" + std::to_string(slot)).c_str());
    }

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    // Mesmo em um estado legado inválido, substituir não amplia a equipe.
    assert(masks.bench_move_available);
    assert(masks.type_mask[static_cast<std::size_t>(ActionType::MOVE_BENCH)] == MASK_ENABLED);
    for (std::size_t target = 0; target < BOARD_SIZE; ++target) {
        assert(masks.bench_to_board_target_masks[0][target] == MASK_ENABLED);
    }
}

void test_invalid_move_pairs_are_not_enabled() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;
    state.board[3] = make_unit("board-unit");
    state.bench[2] = make_unit("bench-unit");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    // MOVE_BOARD não permite origem vazia nem origem==destino.
    // MOVE_BENCH permite uma casa ocupada como substituição.
    assert(masks.board_move_target_masks[4][3] == MASK_DISABLED);
    assert(masks.board_move_target_masks[3][3] == MASK_DISABLED);
    assert(masks.bench_to_board_target_masks[2][3] == MASK_ENABLED);
    assert(masks.bench_to_board_target_masks[2][4] == MASK_ENABLED);
}

// Regression scenario based on the Nasus/Briar oscillation observed in
// rounds 1-3, 1-4, and 2-1. Each move is legal on its own, but the last
// move would recreate the initial board layout after several unrelated moves.
void test_nasus_briar_loop_across_rounds_is_masked() {
    PlayerState state;
    state.economy.gold = 10;
    state.economy.level = 3;
    state.board[3] = make_unit("nasus");
    state.board[10] = make_unit("briar");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    auto register_current_state = [&]() {
        anti_loop.register_state(anti_loop.make_board_signature(state));
    };
    auto apply_legal_move = [&](std::size_t source, std::size_t target,
                                const char* move_type) {
        const auto masks = engine.generate_masks(state, anti_loop);
        assert(masks.board_move_target_masks[source][target] == MASK_ENABLED);

        const auto moving_unit = state.board[source]->identity;
        std::swap(state.board[source], state.board[target]);
        anti_loop.register_move(
            move_type,
            static_cast<std::int32_t>(source),
            static_cast<std::int32_t>(target),
            moving_unit
        );
        register_current_state();
    };

    // Round 1-3: initial formation and first Nasus/Briar swap.
    register_current_state();
    apply_legal_move(3, 10, "board_swap");

    // Round 1-4: reposition Nasus and Briar independently.
    apply_legal_move(10, 12, "board_move");
    apply_legal_move(3, 11, "board_move");

    // Round 2-1: Nasus returns to slot 3. Moving Briar back to slot 10
    // would recreate the already-seen 1-3 layout, without improving it.
    apply_legal_move(12, 3, "board_move");

    const auto nasus_briar_cycle = engine.generate_masks(state, anti_loop);
    assert(state.board[3].has_value());
    assert(state.board[11].has_value());
    assert(!state.board[10].has_value());

    // This is the regression assertion: the cycle-closing action must be
    // masked, even though it is not the immediate reverse of the last move.
    assert(
        nasus_briar_cycle.board_move_target_masks[11][10] == MASK_DISABLED
    );
}

void test_seen_state_from_five_rounds_ago_is_blocked_by_shared_legality() {
    PlayerState previously_seen;
    previously_seen.economy.gold = 10;
    previously_seen.economy.level = 3;
    previously_seen.board[3] = make_unit("nasus");
    previously_seen.board[10] = make_unit("briar");

    PlayerState current = previously_seen;
    current.board[3].reset();
    current.board[12] = previously_seen.board[3];

    AntiLoopEngine anti_loop;
    anti_loop.begin_round(21);
    (void)anti_loop.register_state(anti_loop.make_board_signature(previously_seen));
    anti_loop.begin_round(26);

    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(current, anti_loop);
    assert(masks.board_move_target_masks[12][3] == MASK_DISABLED);

    std::string reason;
    assert(!engine.is_board_move_allowed(current, anti_loop, 12, 3, &reason));
    assert(reason == "cycle");
    assert(engine.is_board_move_allowed(current, anti_loop, 12, 4));
}

void test_mask_diagnostics_count_real_candidates_and_seen_state_blocks() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;
    state.board[3] = make_unit("nasus");

    // O movimento 3 -> 4 recriaria uma posição já registrada.
    PlayerState previously_seen = state;
    std::swap(previously_seen.board[3], previously_seen.board[4]);

    AntiLoopEngine anti_loop;
    anti_loop.register_state(
        anti_loop.make_board_signature(previously_seen)
    );
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.diagnostics.board_move_candidates > 0);
    assert(masks.diagnostics.board_move_valid > 0);
    assert(masks.diagnostics.board_move_blocked_seen_state == 1);
    assert(masks.board_move_target_masks[3][4] == MASK_DISABLED);

    // O fallback da matriz não pode ser confundido com um movimento real.
    PlayerState empty_state;
    empty_state.economy.level = 2;
    const auto empty_masks = engine.generate_masks(empty_state, anti_loop);
    assert(!empty_masks.board_move_available);
    assert(empty_masks.diagnostics.board_move_candidates == 0);
    assert(empty_masks.diagnostics.board_move_valid == 0);
}

void test_bench_move_mask_rejects_repeated_position() {
    PlayerState state;
    state.economy.level = 3;
    state.bench[2] = make_unit("nasus");
    state.board[10] = make_unit("briar");
    PlayerState prior = state;
    std::swap(prior.board[10], prior.bench[2]);

    AntiLoopEngine anti_loop;
    (void)anti_loop.register_state(anti_loop.make_board_signature(prior));
    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.bench_to_board_target_masks[2][10] == MASK_DISABLED);
    assert(masks.diagnostics.bench_move_blocked_seen_state == 1);
    assert(masks.diagnostics.bench_move_valid > 0);
}

void test_mask_diagnostics_count_bench_replacement_loop() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 3;
    state.bench[2] = make_unit("nasus");
    state.board[10] = make_unit("briar");

    AntiLoopEngine anti_loop;
    // Briar entrou no tabuleiro e deslocou Nasus para o banco.
    anti_loop.register_move(
        "bench_to_board",
        2,
        10,
        state.board[10]->identity,
        state.bench[2]->identity
    );

    ActionMaskEngine engine;
    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.diagnostics.bench_move_candidates > 0);
    assert(masks.diagnostics.bench_move_blocked_anti_loop > 0);
    assert(
        masks.bench_to_board_target_masks[2][10] == MASK_DISABLED
    );
}

void test_eliminated_player_can_only_pass() {
    PlayerState state;
    state.is_alive = false;
    state.economy.gold = 100;
    state.economy.level = 2;

    state.shop[0] = make_unit("shop-unit", 1);
    state.bench[0] = make_unit("bench-unit");
    state.board[0] = make_unit("board-unit");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto masks = engine.generate_masks(state, anti_loop);

    for (std::size_t i = 0; i < ACTION_TYPE_COUNT; ++i) {
        const auto expected =
            i == static_cast<std::size_t>(ActionType::PASS)
                ? MASK_ENABLED
                : MASK_DISABLED;

        assert(masks.type_mask[i] == expected);
    }
}

void test_invalid_economy_is_rejected() {
    PlayerState state;
    state.economy.gold = -1;
    state.economy.level = 2;

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    bool rejected = false;

    try {
        (void)engine.generate_masks(state, anti_loop);
    } catch (const std::invalid_argument&) {
        rejected = true;
    }

    assert(rejected);
}

} // namespace

int main() {
    test_empty_state_keeps_pass_available();
    test_shop_mask_matches_python_offer_presence_semantics();
    test_sell_uses_real_bench_units_not_fallback();
    test_board_move_masks_respect_source_and_destination();
    test_bench_to_board_allows_replacement();
    test_bench_to_board_masks_enforce_level_capacity_but_allow_swaps();
    test_buy_is_disabled_when_bench_is_full();
    test_bench_to_board_can_replace_when_physical_grid_is_full();
    test_invalid_move_pairs_are_not_enabled();
    test_nasus_briar_loop_across_rounds_is_masked();
    test_seen_state_from_five_rounds_ago_is_blocked_by_shared_legality();
    test_mask_diagnostics_count_real_candidates_and_seen_state_blocks();
    test_mask_diagnostics_count_bench_replacement_loop();
    test_bench_move_mask_rejects_repeated_position();
    test_eliminated_player_can_only_pass();
    test_invalid_economy_is_rejected();

    return 0;
}