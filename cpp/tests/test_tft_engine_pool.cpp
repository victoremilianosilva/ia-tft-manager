
#include "lobby/TftEngine.hpp"
#include "lobby/ChampionCatalog.hpp"

#include <iostream>
#include <stdexcept>
#include <string>

void require(bool condition, const char* message) {
    if (!condition) {
        throw std::runtime_error(message);
    }
}

int main(int argc, char** argv) {
    try {
        require(argc == 2, "Informe o caminho do JSON.");

        const std::string json_path = argv[1];

        tft::ChampionCatalog catalog(json_path);
        tft::TFTEngine engine(12345, json_path);

        const auto initial_state = engine.get_public_state();

        require(
            initial_state.players.size() == tft::kPlayersPerLobby,
            "Quantidade inicial de jogadores incorreta."
        );

        for (const auto& player : initial_state.players) {
            require(player.gold == 0, "Ouro inicial deveria ser zero.");
            require(player.level == 2, "Nivel inicial deveria ser 2.");
            require(player.xp == 0, "XP inicial deveria ser zero.");
        }

        require(catalog.size() > 0, "Catálogo vazio.");

        for (const auto& champion : catalog.all()) {
            require(
                engine.pool_initial_count(champion.internal_id) > 0,
                "Campeão sem estoque inicial."
            );

            require(
                engine.pool_available(champion.internal_id) <=
                    engine.pool_initial_count(champion.internal_id),
                "Estoque ultrapassou a quantidade inicial."
            );
        }

        const auto total_with_initial_shops = engine.pool_total_available();

        // O reset devolve as ofertas antigas e gera lojas novas sem
        // duplicar nem perder cópias do pool compartilhado.
        engine.reset(12345);
        const auto total_after_reset = engine.pool_total_available();
        require(total_after_reset == total_with_initial_shops,
                "Reset mudou o estoque líquido das lojas iniciais.");

        const auto reset_state = engine.get_public_state();

        require(
            reset_state.players.size() == tft::kPlayersPerLobby,
            "Quantidade de jogadores incorreta apos reset."
        );

        for (const auto& player : reset_state.players) {
            require(player.gold == 0, "Reset nao restaurou o ouro.");
            require(player.level == 2, "Reset nao restaurou o nivel.");
            require(player.xp == 0, "Reset nao restaurou o XP.");
        }

        // As ofertas iniciais permanecem retiradas do pool após reset.
        // O total líquido já foi comparado acima e cada estoque deve
        // continuar dentro dos limites definidos para o campeão.
        require(engine.pool_total_available() <= total_with_initial_shops,
                "Pool aumentou inesperadamente após reset.");
        for (const auto& champion : catalog.all()) {
            require(
                engine.pool_available(champion.internal_id) <=
                    engine.pool_initial_count(champion.internal_id),
                "Reset ultrapassou o estoque inicial de um campeão."
            );
        }

        // Ações semanticamente inválidas devem falhar antes de qualquer
        // mutação do lote (inclusive renda/avanço de rodada).
        const auto round_before_invalid = engine.round();
        const auto pool_before_invalid = engine.pool_total_available();
        const auto gold_before_invalid =
            engine.get_public_state().players[0].gold;

        std::array<tft::PlayerAction, tft::kPlayersPerLobby> invalid_actions{};
        for (auto& action : invalid_actions) {
            action.values = {6, 0, 0, 0, 0, 0};
        }
        invalid_actions[0].values = {5, 0, 0, 0, 0, 0}; // Banco vazio.

        bool invalid_sell_rejected = false;
        try {
            (void)engine.step(invalid_actions);
        } catch (const std::invalid_argument&) {
            invalid_sell_rejected = true;
        }
        require(invalid_sell_rejected,
                "Venda de slot vazio deveria ser rejeitada.");
        require(engine.round() == round_before_invalid,
                "Ação inválida avançou a rodada.");
        require(engine.pool_total_available() == pool_before_invalid,
                "Ação inválida alterou o estoque.");
        require(engine.get_public_state().players[0].gold == gold_before_invalid,
                "Ação inválida alterou o ouro.");

        invalid_actions[0].values = {0, 0, 0, 0, 0, 0}; // Sem ouro.
        bool invalid_buy_rejected = false;
        try {
            (void)engine.step(invalid_actions);
        } catch (const std::invalid_argument&) {
            invalid_buy_rejected = true;
        }
        require(invalid_buy_rejected,
                "Compra sem ouro deveria ser rejeitada.");
        require(engine.round() == round_before_invalid,
                "Compra inválida avançou a rodada.");
        require(engine.pool_total_available() == pool_before_invalid,
                "Compra inválida alterou o estoque.");
        require(engine.get_public_state().players[0].gold == gold_before_invalid,
                "Compra inválida alterou o ouro.");

        // Valida renda, máscara e compra a partir da loja inicial.
        std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};
        for (auto& action : actions) action.values = {6, 0, 0, 0, 0, 0};
        engine.step(actions); // rodada 1: sem renda
        engine.step(actions); // rodada 2: +2 de ouro

        // Uma ação inválida do jogador 0 não pode permitir que uma compra
        // válida do jogador 1 seja executada parcialmente no mesmo lote.
        const auto state_before_atomic_batch = engine.get_public_state();
        const auto pool_before_atomic_batch = engine.pool_total_available();
        const auto masks_before_atomic_batch = engine.get_action_masks();
        std::int32_t player1_buy_slot = -1;
        for (std::int32_t slot = 0;
             slot < static_cast<std::int32_t>(tft::kShopSlots);
             ++slot) {
            if (masks_before_atomic_batch[1].shop_mask[
                    static_cast<std::size_t>(slot)] == 1) {
                player1_buy_slot = slot;
                break;
            }
        }
        require(player1_buy_slot >= 0,
                "Jogador 1 deveria ter uma compra válida para testar atomicidade.");

        for (auto& action : actions) {
            action.values = {6, 0, 0, 0, 0, 0};
        }
        actions[0].values = {5, 0, 0, 0, 0, 0}; // Venda inválida.
        actions[1].values = {0, player1_buy_slot, 0, 0, 0, 0}; // Compra válida.

        bool mixed_batch_rejected = false;
        try {
            (void)engine.step(actions);
        } catch (const std::invalid_argument&) {
            mixed_batch_rejected = true;
        }
        require(mixed_batch_rejected,
                "Lote com uma ação inválida deveria ser rejeitado.");
        const auto state_after_atomic_batch = engine.get_public_state();
        require(engine.round() == 2,
                "Lote inválido avançou a rodada.");
        require(engine.pool_total_available() == pool_before_atomic_batch,
                "Compra de outro jogador foi executada apesar do lote inválido.");
        require(state_after_atomic_batch.players[1].gold ==
                    state_before_atomic_batch.players[1].gold,
                "Lote inválido alterou o ouro de outro jogador.");

        for (auto& action : actions) {
            action.values = {6, 0, 0, 0, 0, 0};
        }
        const auto masks = engine.get_action_masks();
        require(masks[0].type_mask[0] == 1,
                "BUY deveria estar habilitado com ouro e espaço no banco.");
        std::int32_t buy_slot = -1;
        for (std::int32_t slot = 0; slot < static_cast<std::int32_t>(tft::kShopSlots); ++slot) {
            if (masks[0].shop_mask[static_cast<std::size_t>(slot)] == 1) {
                buy_slot = slot; break;
            }
        }
        require(buy_slot >= 0, "Nenhum slot de compra válido foi mascarado.");
        actions[0].values = {0, buy_slot, 0, 0, 0, 0};
        const auto bought = engine.step(actions);
        require(bought.players[0].gold >= 0,
                "Compra deixou ouro negativo.");

        // Mesmo com MOVE_BENCH habilitado por existir uma unidade no banco,
        // uma origem vazia deve rejeitar o lote sem efeitos colaterais.
        const auto round_before_invalid_move = engine.round();
        const auto gold_before_invalid_move =
            engine.get_public_state().players[0].gold;
        const auto pool_before_invalid_move = engine.pool_total_available();
        const auto metrics_before_invalid_move =
            engine.get_anti_loop_metrics()[0];

        actions[0].values = {3, 0, 8, 27, 0, 0}; // Slot 8 vazio.
        bool invalid_move_rejected = false;
        try {
            (void)engine.step(actions);
        } catch (const std::invalid_argument&) {
            invalid_move_rejected = true;
        }
        require(invalid_move_rejected,
                "Movimento a partir de slot vazio deveria ser rejeitado.");
        require(engine.round() == round_before_invalid_move,
                "Movimento inválido avançou a rodada.");
        require(engine.get_public_state().players[0].gold ==
                    gold_before_invalid_move,
                "Movimento inválido alterou o ouro.");
        require(engine.pool_total_available() == pool_before_invalid_move,
                "Movimento inválido alterou o estoque.");
        require(engine.get_anti_loop_metrics()[0].execution_attempts ==
                    metrics_before_invalid_move.execution_attempts,
                "Movimento inválido alterou as métricas anti-loop.");

        actions[0].values = {6, 0, 0, 0, 0, 0};

        require(engine.set_shop_locked(0, true),
                "A loja deveria passar de desbloqueada para bloqueada.");
        require(engine.is_shop_locked(0), "A loja não ficou bloqueada.");
        require(!engine.toggle_shop_lock(0), "Toggle deveria desbloquear a loja.");
        require(!engine.is_shop_locked(0), "A loja deveria estar desbloqueada.");

        const auto pool_before_sale = engine.pool_total_available();
        actions[0].values = {5, 0, 0, 0, 0, 0};
        const auto sold = engine.step(actions);
        require(engine.pool_total_available() == pool_before_sale + 1,
                "Venda não devolveu exatamente uma cópia ao pool.");
        const auto sale_gold_delta =
            sold.players[0].gold - bought.players[0].gold;
        require(
            sale_gold_delta == 1 || sale_gold_delta == 2,
            "Venda deveria creditar somente o valor do campeão; "
            "a renda da rodada ainda não deve ser aplicada antes do PASS."
        );
        require(
            engine.round() == 2,
            "A rodada avançou antes de o jogador 0 terminar a preparação."
        );

        const auto buy_masks = engine.get_action_masks();
        std::int32_t second_buy_slot = -1;
        for (std::int32_t slot = 0; slot < static_cast<std::int32_t>(tft::kShopSlots); ++slot) {
            if (buy_masks[0].shop_mask[static_cast<std::size_t>(slot)] == 1) {
                second_buy_slot = slot;
                break;
            }
        }
        require(second_buy_slot >= 0, "Nenhuma oferta válida para segunda compra.");
        actions[0].values = {0, second_buy_slot, 0, 0, 0, 0};
        (void)engine.step(actions);

        const auto bench_masks = engine.get_action_masks();
        require(bench_masks[0].type_mask[3] == 1,
                "MOVE_BENCH deveria estar habilitado para unidade no banco.");
        std::int32_t bench_slot = -1;
        std::int32_t board_target = -1;
        for (std::int32_t source = 0; source < static_cast<std::int32_t>(tft::kBenchSlots); ++source) {
            for (std::int32_t target = 0; target < static_cast<std::int32_t>(tft::kBoardSlots); ++target) {
                const auto index = static_cast<std::size_t>(
                    source * static_cast<std::int32_t>(tft::kBoardSlots) + target
                );
                if (bench_masks[0].bench_to_board_target_masks[index] == 1) {
                    bench_slot = source;
                    board_target = target;
                    break;
                }
            }
            if (bench_slot >= 0) break;
        }
        require(bench_slot >= 0 && board_target >= 0,
                "ActionMaskEngine não encontrou movimento banco-tabuleiro.");
        actions[0].values = {3, 0, bench_slot, board_target, 0, 0};
        (void)engine.step(actions);

        auto metrics = engine.get_anti_loop_metrics();
        require(metrics[0].execution_attempts == 1,
                "Tentativa de movimento não foi contabilizada.");
        require(metrics[0].bench_to_board_executed == 1,
                "Movimento banco-tabuleiro não foi contabilizado.");

        const auto board_masks = engine.get_action_masks();
        require(board_masks[0].type_mask[4] == 1,
                "MOVE_BOARD deveria estar habilitado após colocar unidade no tabuleiro.");
        std::int32_t board_source = -1;
        std::int32_t next_target = -1;
        for (std::int32_t source = 0; source < static_cast<std::int32_t>(tft::kBoardSlots); ++source) {
            if (board_masks[0].board_source_mask[static_cast<std::size_t>(source)] != 1) continue;
            for (std::int32_t target = 0; target < static_cast<std::int32_t>(tft::kBoardSlots); ++target) {
                const auto index = static_cast<std::size_t>(
                    source * static_cast<std::int32_t>(tft::kBoardSlots) + target
                );
                if (board_masks[0].board_move_target_masks[index] == 1) {
                    board_source = source;
                    next_target = target;
                    break;
                }
            }
            if (board_source >= 0) break;
        }
        require(board_source >= 0 && next_target >= 0,
                "ActionMaskEngine não encontrou movimento de tabuleiro válido.");
        actions[0].values = {4, 0, 0, 0, board_source, next_target};
        (void)engine.step(actions);

        metrics = engine.get_anti_loop_metrics();
        require(metrics[0].execution_attempts == 2,
                "Métrica de tentativas não acompanhou movimento no tabuleiro.");
        require(metrics[0].board_moves_executed == 1,
                "Movimento no tabuleiro não foi contabilizado.");

        actions[0].values = {4, 0, 0, 0, next_target, board_source};
        (void)engine.step(actions);
        metrics = engine.get_anti_loop_metrics();
        require(metrics[0].execution_attempts == 3,
                "Tentativa de movimento reverso não foi contabilizada.");
        require(metrics[0].execution_blocks == 1 && metrics[0].blocked_reverse == 1,
                "AntiLoop não bloqueou/contabilizou o movimento reverso.");

        // A rodada permanece aberta durante ações de preparação. Um PASS
        // do jogador 0 fecha a rodada porque os demais já enviaram PASS.
        const auto round_before_pass = engine.round();
        actions[0].values = {6, 0, 0, 0, 0, 0};
        const auto closed_round = engine.step(actions);
        require(
            engine.round() == round_before_pass + 1,
            "PASS do último jogador não resolveu/avançou a rodada."
        );
        bool saw_round_resolved = false;
        for (const auto& event : closed_round.events) {
            if (event == "ROUND_RESOLVED") {
                saw_round_resolved = true;
                break;
            }
        }
        require(saw_round_resolved,
                "O resultado não informou que a rodada foi resolvida.");

        // Reset de episódio limpa os históricos de movimentos, mas mantém
        // as métricas acumuladas para diagnóstico entre episódios.
        const auto metrics_before_reset = engine.get_anti_loop_metrics();
        engine.reset(12345);
        const auto metrics_after_reset = engine.get_anti_loop_metrics();
        require(
            metrics_after_reset[0].execution_attempts ==
                metrics_before_reset[0].execution_attempts,
            "Reset apagou as métricas acumuladas do AntiLoop."
        );
        require(
            metrics_after_reset[0].execution_blocks ==
                metrics_before_reset[0].execution_blocks,
            "Reset apagou os bloqueios acumulados do AntiLoop."
        );

        std::cout << "TFTEngine + loja/economia/ActionMask/AntiLoop: OK\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "TFTEngine + UnitPool: FALHOU: "
                  << e.what() << '\n';
        return 1;
    }
}
