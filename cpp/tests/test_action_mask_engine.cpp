
#include "decision/ActionMaskEngine.hpp"

#ifdef NDEBUG
#undef NDEBUG
#endif
#include <cassert>
#include <stdexcept>
#include <string>

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
    assert(masks.type_mask[ActionType::PASS] == MASK_ENABLED);

    // Nenhuma ação econômica real está disponível.
    assert(!masks.buy_available);
    assert(!masks.sell_available);
    assert(!masks.board_move_available);
    assert(!masks.bench_move_available);

    assert(masks.type_mask[ActionType::BUY] == MASK_DISABLED);
    assert(masks.type_mask[ActionType::REROLL] == MASK_DISABLED);
    assert(masks.type_mask[ActionType::BUY_XP] == MASK_DISABLED);
    assert(masks.type_mask[ActionType::MOVE_BENCH] == MASK_DISABLED);
    assert(masks.type_mask[ActionType::MOVE_BOARD] == MASK_DISABLED);
    assert(masks.type_mask[ActionType::SELL] == MASK_DISABLED);

    // Fallback técnico das cabeças categóricas.
    // O fallback não deve habilitar uma ação real.
    assert(masks.shop_mask[0] == MASK_ENABLED);
    assert(masks.bench_source_mask[0] == MASK_ENABLED);
    assert(masks.board_target_mask[0] == MASK_ENABLED);
    assert(masks.board_source_mask[0] == MASK_ENABLED);
}

void test_shop_only_allows_affordable_available_units() {
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
    assert(masks.type_mask[ActionType::BUY] == MASK_ENABLED);

    assert(masks.shop_mask[0] == MASK_ENABLED);
    assert(masks.shop_mask[1] == MASK_DISABLED);
    assert(masks.shop_mask[2] == MASK_DISABLED);
}

void test_sell_uses_real_bench_units_not_fallback() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto empty_masks = engine.generate_masks(state, anti_loop);

    assert(!empty_masks.sell_available);
    assert(empty_masks.type_mask[ActionType::SELL] == MASK_DISABLED);

    state.bench[4] = make_unit("bench-unit");

    const auto occupied_masks = engine.generate_masks(state, anti_loop);

    assert(occupied_masks.sell_available);
    assert(occupied_masks.type_mask[ActionType::SELL] == MASK_ENABLED);
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
    assert(masks.type_mask[ActionType::MOVE_BOARD] == MASK_ENABLED);

    // A origem ocupada possui destinos válidos.
    assert(masks.board_source_mask[3] == MASK_ENABLED);

    // A matriz é condicionada pela origem selecionada.
    assert(masks.board_move_target_masks[3][3] == MASK_DISABLED);
    assert(masks.board_move_target_masks[3][4] == MASK_ENABLED);

    // Uma origem vazia não deve ter movimento real.
    assert(masks.board_move_target_masks[4][3] == MASK_DISABLED);
}

void test_bench_to_board_requires_empty_target() {
    PlayerState state;
    state.economy.gold = 0;
    state.economy.level = 2;

    state.bench[2] = make_unit("bench-unit");
    state.board[10] = make_unit("board-unit");

    AntiLoopEngine anti_loop;
    ActionMaskEngine engine;

    const auto masks = engine.generate_masks(state, anti_loop);

    assert(masks.bench_move_available);
    assert(masks.type_mask[ActionType::MOVE_BENCH] == MASK_ENABLED);

    assert(masks.bench_move_source_mask[2] == MASK_ENABLED);

    // Posição vazia: movimento permitido.
    assert(masks.bench_to_board_target_masks[2][11] == MASK_ENABLED);

    // Posição ocupada: banco -> tabuleiro não pode sobrescrever unidade.
    assert(masks.bench_to_board_target_masks[2][10] == MASK_DISABLED);
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
    assert(masks.type_mask[ActionType::BUY] == MASK_DISABLED);
    assert(masks.shop_mask[0] == MASK_DISABLED);
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

    // Não permite origem vazia, origem==destino nem destino ocupado
    // para o movimento banco -> tabuleiro.
    assert(masks.board_move_target_masks[4][3] == MASK_DISABLED);
    assert(masks.board_move_target_masks[3][3] == MASK_DISABLED);
    assert(masks.bench_to_board_target_masks[2][3] == MASK_DISABLED);
    assert(masks.bench_to_board_target_masks[2][4] == MASK_ENABLED);
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
    test_shop_only_allows_affordable_available_units();
    test_sell_uses_real_bench_units_not_fallback();
    test_board_move_masks_respect_source_and_destination();
    test_bench_to_board_requires_empty_target();
    test_buy_is_disabled_when_bench_is_full();
    test_invalid_move_pairs_are_not_enabled();
    test_eliminated_player_can_only_pass();
    test_invalid_economy_is_rejected();

    return 0;
}