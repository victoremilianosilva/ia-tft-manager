
#include "decision/ActionMaskEngine.hpp"

#include "decision/MoveValidator.hpp"

#include <algorithm>
#include <cstddef>
#include <stdexcept>
#include <string>

namespace tft::decision {
namespace {

constexpr const char* move_type_name(MoveType type) noexcept {
    switch (type) {
        case MoveType::BENCH_TO_BOARD:
            return "bench_to_board";
        case MoveType::BOARD_MOVE:
            return "board_move";
        case MoveType::BOARD_SWAP:
            return "board_swap";
    }

    return "";
}

std::optional<UnitIdentity> identity_of(
    const std::optional<UnitSnapshot>& unit
) {
    if (!unit.has_value() || !unit->identity.has_identity()) {
        return std::nullopt;
    }

    return unit->identity;
}

bool is_valid_mask_row(
    const std::array<MaskValue, BOARD_SIZE>& row
) noexcept {
    return std::any_of(
        row.begin(),
        row.end(),
        [](MaskValue value) {
            return value == MASK_ENABLED;
        }
    );
}

} // namespace

bool ActionMaskEngine::can_spend(
    const EconomyState& economy,
    std::int32_t amount
) noexcept {
    return amount >= 0 && economy.gold >= amount;
}

bool ActionMaskEngine::has_free_bench_slot(
    const PlayerState& state
) noexcept {
    return state.has_free_bench_slot();
}

void ActionMaskEngine::validate_state(const PlayerState& state) {
    const auto& economy = state.economy;

    if (economy.gold < 0) {
        throw std::invalid_argument(
            "ActionMaskEngine: gold nao pode ser negativo."
        );
    }

    if (
        economy.level < 1
        || economy.max_level < 1
        || economy.level > economy.max_level
    ) {
        throw std::invalid_argument(
            "ActionMaskEngine: nivel ou nivel maximo invalido."
        );
    }

    if (
        economy.current_xp < 0
        || economy.xp_to_next_level < 0
        || economy.reroll_cost < 0
        || economy.xp_purchase_cost < 0
    ) {
        throw std::invalid_argument(
            "ActionMaskEngine: estado economico inconsistente."
        );
    }

    for (const auto& unit : state.shop) {
        if (unit.has_value() &&
            (unit->cost == 0 || unit->cost > 5)) {
            throw std::invalid_argument(
                "ActionMaskEngine: custo fora do intervalo valido na loja."
            );
        }
    }
}

void ActionMaskEngine::set_fallback(ActionMaskBatch& masks) {
    // Toda cabeça categórica deve ter pelo menos uma categoria.
    // Esses valores dummy não habilitam tipos de ação.
    if (
        std::none_of(
            masks.shop_mask.begin(),
            masks.shop_mask.end(),
            [](MaskValue v) { return v == MASK_ENABLED; }
        )
    ) {
        masks.shop_mask[0] = MASK_ENABLED;
    }

    if (
        std::none_of(
            masks.bench_source_mask.begin(),
            masks.bench_source_mask.end(),
            [](MaskValue v) { return v == MASK_ENABLED; }
        )
    ) {
        masks.bench_source_mask[0] = MASK_ENABLED;
    }

    if (
        std::none_of(
            masks.board_target_mask.begin(),
            masks.board_target_mask.end(),
            [](MaskValue v) { return v == MASK_ENABLED; }
        )
    ) {
        masks.board_target_mask[0] = MASK_ENABLED;
    }

    if (
        std::none_of(
            masks.board_source_mask.begin(),
            masks.board_source_mask.end(),
            [](MaskValue v) { return v == MASK_ENABLED; }
        )
    ) {
        masks.board_source_mask[0] = MASK_ENABLED;
    }

    if (
        std::none_of(
            masks.bench_move_source_mask.begin(),
            masks.bench_move_source_mask.end(),
            [](MaskValue v) { return v == MASK_ENABLED; }
        )
    ) {
        masks.bench_move_source_mask[0] = MASK_ENABLED;
    }

    for (auto& row : masks.board_move_target_masks) {
        if (!is_valid_mask_row(row)) {
            row[0] = MASK_ENABLED;
        }
    }

    for (auto& row : masks.bench_to_board_target_masks) {
        if (!is_valid_mask_row(row)) {
            row[0] = MASK_ENABLED;
        }
    }
}

bool ActionMaskEngine::is_valid_board_move(
    const PlayerState& state,
    const AntiLoopEngine& anti_loop,
    RawIndex source,
    RawIndex target
) {
    const auto result = MoveValidator::validate_board_move(
        state.board,
        source,
        target
    );

    if (!result.is_valid() || !result.move_type.has_value()) {
        return false;
    }

    const auto source_index = to_board_index(source);
    if (!source_index.has_value()) {
        return false;
    }

    const auto target_index = to_board_index(target);
    if (!target_index.has_value()) {
        return false;
    }

    const auto move_type = *result.move_type;
    const auto unit = identity_of(state.board[*source_index]);

    if (anti_loop.should_block_move(
        move_type_name(move_type),
        source,
        target,
        unit
    )) {
        return false;
    }

    // Prevent returning to a previously visited board layout, even when
    // the individual move is not an immediate reversal (e.g. after BUY_XP
    // or across rounds). This catches multi-unit oscillations such as
    // Nasus/Briar swapping positions over 1-3, 1-4, and 2-1.
    PlayerState next_state = state;
    std::swap(
        next_state.board[*source_index],
        next_state.board[*target_index]
    );
    const auto resulting_signature =
        anti_loop.make_board_signature(next_state);

    return !anti_loop.was_state_seen(resulting_signature);
}

bool ActionMaskEngine::is_valid_bench_to_board_move(
    const PlayerState& state,
    const AntiLoopEngine& anti_loop,
    RawIndex bench_slot,
    RawIndex target
) {
    const auto result = MoveValidator::validate_bench_to_board_move(
        state.board,
        state.bench,
        bench_slot,
        target
    );

    if (!result.is_valid() || !result.move_type.has_value()) {
        return false;
    }

    const auto bench_index = to_bench_index(bench_slot);
    if (!bench_index.has_value()) {
        return false;
    }

    const auto unit = identity_of(state.bench[*bench_index]);

    return !anti_loop.should_block_move(
        move_type_name(*result.move_type),
        bench_slot,
        target,
        unit
    );
}


ActionMaskBatch ActionMaskEngine::generate_masks(
    const PlayerState& state,
    const AntiLoopEngine& anti_loop,
    bool include_board_target
) const {
    validate_state(state);

    ActionMaskBatch masks{};

    // Jogador eliminado: somente PASS é uma ação real.
    if (!state.is_alive) {
        // Match TFTLobby._dead_player_mask exactly: only the first entry
        // is a dummy fallback, including the two conditional matrices.
        masks.type_mask[static_cast<std::size_t>(ActionType::PASS)] = MASK_ENABLED;
        masks.shop_mask[0] = MASK_ENABLED;
        masks.bench_source_mask[0] = MASK_ENABLED;
        masks.board_target_mask[0] = MASK_ENABLED;
        masks.board_source_mask[0] = MASK_ENABLED;
        masks.board_move_target_masks[0][0] = MASK_ENABLED;
        masks.bench_move_source_mask[0] = MASK_ENABLED;
        masks.bench_to_board_target_masks[0][0] = MASK_ENABLED;
        return masks;
    }

    // --------------------------------------------------------
    // Loja e economia
    // --------------------------------------------------------

    const bool bench_has_space = has_free_bench_slot(state);

    for (std::size_t slot = 0; slot < SHOP_SIZE; ++slot) {
        const auto& unit = state.shop[slot];

        // Paridade com Python: a máscara considera a oferta presente,
        // espaço no banco e ouro. O flag "available" não é filtrado pela
        // implementação Python atual e não deve alterar o contrato da máscara.
        if (!bench_has_space || !unit.has_value()) {
            continue;
        }

        if (!can_spend(state.economy, unit->cost)) {
            continue;
        }

        masks.shop_mask[slot] = MASK_ENABLED;
        masks.buy_available = true;
    }

    // --------------------------------------------------------
    // Banco: seleção para venda
    // --------------------------------------------------------

    for (std::size_t slot = 0; slot < BENCH_SIZE; ++slot) {
        if (!state.bench[slot].has_value()) {
            continue;
        }

        masks.bench_source_mask[slot] = MASK_ENABLED;
        masks.sell_available = true;
    }

    // --------------------------------------------------------
    // Banco -> tabuleiro: implantação ou substituição.
    // Uma casa vazia consome espaço de equipe; uma ocupada troca a unidade
    // com o slot do banco e mantém a quantidade de unidades implantadas.
    std::size_t board_unit_count = 0;
    for (const auto& unit : state.board) {
        if (unit.has_value()) {
            ++board_unit_count;
        }
    }
    const bool has_team_capacity =
        board_unit_count < static_cast<std::size_t>(state.economy.level);

    for (std::size_t source = 0; source < BENCH_SIZE; ++source) {
        if (!state.bench[source].has_value()) {
            continue;
        }

        for (std::size_t target = 0; target < BOARD_SIZE; ++target) {
            const bool target_occupied = state.board[target].has_value();

            // O limite só bloqueia implantações em casas vazias.
            if (!target_occupied && !has_team_capacity) {
                continue;
            }

            if (!is_valid_bench_to_board_move(
                state,
                anti_loop,
                static_cast<RawIndex>(source),
                static_cast<RawIndex>(target)
            )) {
                continue;
            }

            masks.bench_to_board_target_masks[source][target] =
                MASK_ENABLED;
            masks.bench_move_source_mask[source] = MASK_ENABLED;

            if (include_board_target) {
                masks.board_target_mask[target] = MASK_ENABLED;
            }

            masks.bench_move_available = true;
        }
    }

    // Tabuleiro -> tabuleiro: origem e destino condicionados
    // --------------------------------------------------------

    for (std::size_t source = 0; source < BOARD_SIZE; ++source) {
        if (!state.board[source].has_value()) {
            continue;
        }

        for (std::size_t target = 0; target < BOARD_SIZE; ++target) {
            if (source == target) {
                continue;
            }

            if (!is_valid_board_move(
                state,
                anti_loop,
                static_cast<RawIndex>(source),
                static_cast<RawIndex>(target)
            )) {
                continue;
            }

            masks.board_move_target_masks[source][target] =
                MASK_ENABLED;

            masks.board_source_mask[source] = MASK_ENABLED;
            masks.board_move_available = true;
        }
    }

    // --------------------------------------------------------
    // União dos destinos válidos do tabuleiro
    // --------------------------------------------------------

    bool has_conditioned_target = false;

    for (std::size_t source = 0; source < BOARD_SIZE; ++source) {
        // Ignora origens sem movimento real válido.
        // Assim, os fallbacks técnicos não entram na união.
        if (masks.board_source_mask[source] != MASK_ENABLED) {
            continue;
        }

        for (std::size_t target = 0; target < BOARD_SIZE; ++target) {
            if (
                masks.board_move_target_masks[source][target]
                != MASK_ENABLED
            ) {
                continue;
            }

            masks.conditioned_board_target_mask[target] =
                MASK_ENABLED;

            has_conditioned_target = true;
        }
    }

    // Mantém uma distribuição categórica válida se não houver
    // destinos reais disponíveis.
    if (!has_conditioned_target) {
        masks.conditioned_board_target_mask[0] = MASK_ENABLED;
    }

    // --------------------------------------------------------
    // Tipo de ação: disponibilidade real, não fallback
    // --------------------------------------------------------

    if (masks.buy_available) {
        masks.type_mask[
            static_cast<std::size_t>(ActionType::BUY)
        ] = MASK_ENABLED;
    }

    if (can_spend(state.economy, state.economy.reroll_cost)) {
        masks.type_mask[
            static_cast<std::size_t>(ActionType::REROLL)
        ] = MASK_ENABLED;
    }

    if (
        state.economy.level < state.economy.max_level
        && can_spend(
            state.economy,
            state.economy.xp_purchase_cost
        )
    ) {
        masks.type_mask[
            static_cast<std::size_t>(ActionType::BUY_XP)
        ] = MASK_ENABLED;
    }

    if (masks.bench_move_available) {
        masks.type_mask[
            static_cast<std::size_t>(ActionType::MOVE_BENCH)
        ] = MASK_ENABLED;
    }

    if (masks.board_move_available) {
        masks.type_mask[
            static_cast<std::size_t>(ActionType::MOVE_BOARD)
        ] = MASK_ENABLED;
    }

    if (masks.sell_available) {
        masks.type_mask[
            static_cast<std::size_t>(ActionType::SELL)
        ] = MASK_ENABLED;
    }

    masks.type_mask[
        static_cast<std::size_t>(ActionType::PASS)
    ] = MASK_ENABLED;

    // --------------------------------------------------------
    // Fallbacks técnicos das cabeças auxiliares
    // --------------------------------------------------------

    set_fallback(masks);
    if (!bench_has_space) {
        // A full bench makes every shop choice semantically invalid. Do not
        // restore a dummy shop index that could be mistaken for a valid buy.
        masks.shop_mask.fill(MASK_DISABLED);
    }
    return masks;
}


} // namespace tft::decision