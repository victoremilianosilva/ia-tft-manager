
#include "lobby/TftEngine.hpp"
#include "lobby/ChampionCatalog.hpp"

#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

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
        const auto initial_observations = engine.get_observations();
        require(engine.observation_dim() > 248,
                "Observacao PPO deve incluir o vetor de traits do catalogo.");
        require(initial_observations.size() ==
                    tft::kPlayersPerLobby * engine.observation_dim(),
                "Tamanho do lote de observacoes nao corresponde a dimensao declarada.");

        // Composition must be part of the actual PPO observation, not only
        // diagnostic metadata. Verify its fixed layout and live values.
        std::vector<std::string> trait_order;
        for (const auto& champion : catalog.all()) {
            for (const auto& trait : champion.traits) {
                if (std::find(trait_order.begin(), trait_order.end(), trait) ==
                    trait_order.end()) {
                    trait_order.push_back(trait);
                }
            }
        }
        const std::size_t legacy_observation_dim = 248 + trait_order.size();
        const std::size_t expected_observation_dim =
            legacy_observation_dim + 2 * trait_order.size() +
            tft::kBoardSlots + tft::kBenchSlots + tft::kShopSlots +
            1 + tft::kBoardSlots + trait_order.size() + 2 +
            8 * (tft::kBenchSlots + tft::kShopSlots);
        require(engine.observation_dim() == expected_observation_dim,
                "Dimensao PPO nao inclui os novos recursos de composicao.");

        const auto comp_champion = std::find_if(
            catalog.all().begin(), catalog.all().end(),
            [](const auto& champion) { return !champion.traits.empty(); });
        require(comp_champion != catalog.all().end(),
                "Catalogo nao possui campeao com traits para testar composicao.");
        require(engine.set_unit_for_testing(
                    0, true, 0, comp_champion->api_name, 1),
                "Nao foi possivel configurar unidade de teste para composicao.");

        const auto strategy_after_fixture = engine.get_strategies()[0].back();
        const auto composition_observations = engine.get_observations();
        const auto* player_observation = composition_observations.data();
        const std::size_t direction_offset = legacy_observation_dim;
        const std::size_t core_traits_offset =
            direction_offset + trait_order.size();
        const std::size_t unit_fit_offset =
            core_traits_offset + trait_order.size();
        require(player_observation[unit_fit_offset] > 0.0f,
                "Score de compatibilidade da unidade nao chegou a observacao PPO.");
        const std::size_t candidate_features_offset =
            expected_observation_dim - 8 * (tft::kBenchSlots + tft::kShopSlots);
        const std::size_t focus_weights_offset =
            candidate_features_offset - trait_order.size() - 2;
        const std::size_t locked_offset = focus_weights_offset + trait_order.size();
        const std::size_t strength_offset = locked_offset + 1;
        for (std::size_t trait_index = 0;
             trait_index < trait_order.size(); ++trait_index) {
            double expected_weight = 0.0;
            for (const auto& [trait, weight] :
                 strategy_after_fixture.composition_focus_weights) {
                if (trait == trait_order[trait_index]) {
                    expected_weight = weight;
                    break;
                }
            }
            const float expected_normalized_weight = static_cast<float>(
                std::clamp(expected_weight / 10.0, 0.0, 1.0));
            require(std::abs(player_observation[focus_weights_offset + trait_index] -
                             expected_normalized_weight) < 1e-5f,
                    "Focus weights nao estao alinhados com a ordem fixa de traits.");
            require(player_observation[focus_weights_offset + trait_index] >= 0.0f &&
                    player_observation[focus_weights_offset + trait_index] <= 1.0f,
                    "Focus weight normalizado fora de [0, 1].");
        }
        require(player_observation[locked_offset] ==
                    (strategy_after_fixture.composition_locked ? 1.0f : 0.0f),
                "Estado composition_locked diverge do snapshot estrategico.");
        require(std::abs(player_observation[strength_offset] -
                         static_cast<float>(std::clamp(
                             strategy_after_fixture.composition_strength / 10.0, 0.0, 1.0))) < 1e-5f,
                "composition_strength nao esta normalizado/alinhado.");
        require(candidate_features_offset + 8 * (tft::kBenchSlots + tft::kShopSlots) ==
                    expected_observation_dim,
                "Features de candidatos deixaram de ocupar a cauda da observacao.");
        require(player_observation[candidate_features_offset] > 0.0f,
                "Features estrategicas da primeira unidade do banco ausentes.");
        const std::size_t shop_candidate_offset =
            candidate_features_offset + 8 * tft::kBenchSlots;
        require(player_observation[shop_candidate_offset] > 0.0f,
                "Features estrategicas da primeira oferta da loja ausentes.");
        if (!strategy_after_fixture.composition_direction.empty()) {
            const auto direction_it = std::find(
                trait_order.begin(), trait_order.end(),
                strategy_after_fixture.composition_direction);
            require(direction_it != trait_order.end(),
                    "Direcao da composicao nao existe na ordem fixa de traits.");
            const auto direction_index = static_cast<std::size_t>(
                std::distance(trait_order.begin(), direction_it));
            require(player_observation[direction_offset + direction_index] == 1.0f,
                    "Direcao da composicao nao foi codificada na observacao PPO.");
        }
        for (std::size_t trait_index = 0;
             trait_index < trait_order.size(); ++trait_index) {
            const bool expected_core_trait = std::find(
                strategy_after_fixture.core_traits.begin(),
                strategy_after_fixture.core_traits.end(),
                trait_order[trait_index]) !=
                strategy_after_fixture.core_traits.end();
            require(player_observation[core_traits_offset + trait_index] ==
                        (expected_core_trait ? 1.0f : 0.0f),
                    "Core traits divergem entre StrategyInfo e observacao PPO.");
        }

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
        invalid_actions[0].values = {5, 0, 8, 0, 0, 0}; // Slot vazio; slot 0 contém a unidade inicial.

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
        // O treinamento só resolve a preparação depois de 10 ações de cada
        // jogador; PASS conta como ação, mas não encerra a rodada sozinho.
        for (int action = 0; action < 20; ++action) {
            (void)engine.step(actions);
        } // duas rodadas completas de 10 ações

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
        actions[0].values = {5, 0, 8, 0, 0, 0}; // Slot vazio; slot 0 contém a unidade inicial.
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
        require(std::abs(bought.rewards[0] - bought.action_rewards[0]) < 1e-6f,
                "Compra sem combate deve retornar apenas a recompensa da acao.");
        require(bought.action_rewards[0] > -0.25f && bought.action_rewards[0] < 0.50f,
                "Recompensa de compra com shaping economico deve permanecer limitada.");

        // CompositionManager/StrategyManager devem refletir as unidades
        // compradas no snapshot público, sem depender de combate.
        const auto strategy_snapshot = engine.get_strategies()[0];
        require(!strategy_snapshot.empty(),
                "StrategyManager não publicou estado para o jogador.");
        require(!strategy_snapshot.back().composition_focus.empty(),
                "CompositionManager não identificou unidade foco.");
        require(!strategy_snapshot.back().unit_counts.empty(),
                "CompositionManager não contabilizou cópias do jogador.");
        require(strategy_snapshot.back().strategy >= 0 &&
                    strategy_snapshot.back().strategy <= 6,
                "StrategyManager publicou estratégia fora do enum válido.");

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
            "a renda da rodada ainda não deve ser aplicada antes da décima ação."
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

        // Mesmo quando todos enviam PASS, o treinamento aguarda 10 ações.
        const auto round_before_pass = engine.round();
        actions[0].values = {6, 0, 0, 0, 0, 0};
        const auto after_pass = engine.step(actions);
        require(
            engine.round() == round_before_pass,
            "PASS encerrou a rodada antes de completar 10 ações."
        );
        bool resolved_too_early = false;
        for (const auto& event : after_pass.events) {
            if (event == "ROUND_RESOLVED") {
                resolved_too_early = true;
                break;
            }
        }
        require(!resolved_too_early,
                "A engine resolveu a rodada antes da décima ação.");

        // A agenda oficial tem abertura/PvE até 1-4; o primeiro PvP ocorre em 2-1.
        // Como só o jogador 0 possui unidade no tabuleiro, a primeira rodada PvP
        // deve conceder a ele uma vitória automática contra uma equipe vazia.
        auto combat_round = after_pass;
        for (int wait = 0;
             wait < 80 && combat_round.players[0].wins == 0;
             ++wait) {
            for (auto& action : actions) {
                action.values = {6, 0, 0, 0, 0, 0};
            }
            combat_round = engine.step(actions);
        }
        require(
            combat_round.players[0].wins >= 1,
            "Equipe com unidades não recebeu vitória automática na primeira rodada PvP."
        );
        require(
            combat_round.players[0].opponent_id.has_value(),
            "Matchmaking não registrou o oponente do jogador 0."
        );
        const auto opponent_id = static_cast<std::size_t>(
            *combat_round.players[0].opponent_id
        );
        require(opponent_id < tft::kPlayersPerLobby && opponent_id != 0,
                "Matchmaking atribuiu um oponente inválido.");
        require(
            combat_round.players[opponent_id].losses >= 1,
            "A derrota automática não foi registrada no oponente."
        );
        require(
            combat_round.players[opponent_id].damage_taken >= 1.0f,
            "Dano ao jogador não incluiu os sobreviventes da vitória automática."
        );
        bool saw_auto_win = false;
        for (const auto& event : combat_round.events) {
            if (event.find("AUTO_WIN_EMPTY_BOARD") != std::string::npos) {
                saw_auto_win = true;
                break;
            }
        }
        require(saw_auto_win,
                "Faltou evento de diagnóstico para vitória automática.");

        // A partir daqui, as ações econômicas são testadas na preparação posterior
        // ao primeiro PvP, já com sua renda e bônus de vitória aplicados.
        const auto round_before_economic_actions = engine.round();

        // Validação integrada de REROLL: custo 2, nova oferta e rodada
        // continua aberta até todos os jogadores completarem 10 ações.
        const auto gold_before_reroll = engine.get_public_state().players[0].gold;
        require(gold_before_reroll >= 2,
                "Pré-condição econômica inesperada para testar reroll.");
        const auto masks_before_reroll = engine.get_action_masks();
        require(masks_before_reroll[0].type_mask[1] == 1,
                "REROLL deveria estar habilitado com ouro suficiente.");
        actions[0].values = {1, 0, 0, 0, 0, 0};
        const auto rerolled = engine.step(actions);
        require(rerolled.players[0].gold == gold_before_reroll - 2,
                "REROLL não descontou exatamente 2 de ouro.");
        require(engine.round() == round_before_economic_actions,
                "REROLL encerrou a rodada sem PASS.");
        actions[0].values = {6, 0, 0, 0, 0, 0};
        auto next_round = engine.step(actions);
        for (int action = 2; action < 10; ++action) {
            next_round = engine.step(actions);
        }
        require(engine.round() == round_before_economic_actions + 1,
                "A rodada não avançou após 10 ações por jogador.");

        // Com renda da rodada e bônus de vitória, deve haver ouro suficiente
        // para comprar XP. O nível/XP são verificados no estado público.
        const auto gold_before_xp = next_round.players[0].gold;
        require(gold_before_xp >= 4,
                "Pré-condição econômica inesperada para testar compra de XP.");
        const auto masks_before_xp = engine.get_action_masks();
        require(masks_before_xp[0].type_mask[2] == 1,
                "BUY_XP deveria estar habilitado com ouro suficiente.");
        const auto level_before_xp = next_round.players[0].level;
        const auto xp_before_xp = next_round.players[0].xp;
        actions[0].values = {2, 0, 0, 0, 0, 0};
        const auto bought_xp = engine.step(actions);
        require(bought_xp.players[0].gold == gold_before_xp - 4,
                "BUY_XP não descontou exatamente 4 de ouro.");
        require(level_before_xp == 4 && xp_before_xp == 4,
                "Progressão de XP passivo divergiu antes da compra de XP.");
        require(bought_xp.players[0].level == 4 && bought_xp.players[0].xp == 8,
                "BUY_XP deveria adicionar exatamente 4 XP sem subir de nível neste estado.");
        require(engine.round() == round_before_economic_actions + 1,
                "BUY_XP encerrou a rodada sem PASS.");

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

        // Regression: a dominant trait with six owned units should lock in
        // stage 3, and the direction must survive a small off-comp addition.
        tft::TFTEngine comp_engine(56789, json_path);
        std::map<std::string, std::vector<std::string>> champions_by_trait;
        for (const auto& champion : catalog.all()) {
            for (const auto& trait : champion.traits)
                champions_by_trait[trait].push_back(champion.api_name);
        }
        auto dominant = std::find_if(
            champions_by_trait.begin(), champions_by_trait.end(),
            [](const auto& entry) { return entry.second.size() >= 6; });
        require(dominant != champions_by_trait.end(),
                "Catalogo nao possui trait com seis campeoes para testar comp lock.");
        for (std::size_t slot = 0; slot < 6; ++slot) {
            require(comp_engine.set_unit_for_testing(
                        0, false, static_cast<std::int32_t>(slot),
                        dominant->second[slot], 1),
                    "Nao foi possivel montar fixture de seis unidades para comp lock.");
        }
        std::array<tft::PlayerAction, tft::kPlayersPerLobby> pass_actions{};
        for (auto& action : pass_actions) action.values = {6, 0, 0, 0, 0, 0};
        for (int completed_rounds = 0;
             completed_rounds < 14 && comp_engine.stage() < 3;
             ++completed_rounds) {
            for (int action = 0; action < 10; ++action)
                (void)comp_engine.step(pass_actions);
        }
        require(comp_engine.stage() >= 3,
                "Fixture nao alcancou stage 3 para validar o comp lock.");
        // Stage is advanced after combat resolution; let the strategy update
        // run twice in the newly opened stage-3 preparation phase.
        (void)comp_engine.step(pass_actions);
        (void)comp_engine.step(pass_actions);
        auto comp_state = comp_engine.get_strategies()[0].back();
        require(comp_state.composition_locked,
                "Composicao dominante com seis unidades nao ativou o lock no stage 3.");
        require(!comp_state.composition_direction.empty(),
                "Lock ativo nao preservou uma direcao de composicao.");
        const auto locked_direction = comp_state.composition_direction;
        const auto off_comp = std::find_if(
            catalog.all().begin(), catalog.all().end(),
            [&](const auto& champion) {
                return std::find(champion.traits.begin(), champion.traits.end(),
                                 locked_direction) == champion.traits.end();
            });
        if (off_comp != catalog.all().end()) {
            require(comp_engine.set_unit_for_testing(
                        0, false, 6, off_comp->api_name, 1),
                    "Nao foi possivel adicionar unidade fora da composicao.");
            (void)comp_engine.set_unit_for_testing(
                0, false, 7, off_comp->api_name, 1);
            comp_state = comp_engine.get_strategies()[0].back();
            require(comp_state.composition_locked,
                    "Lock foi perdido apos adicionar uma unidade fora da composicao.");
            require(comp_state.composition_direction == locked_direction,
                    "Direcao mudou imediatamente apesar do lock ativo.");
        }

        // End-to-end regressions for the Viewer buy/sell loop. The same low-fit
        // sequence is replayed with Teemo, Caitlyn, Ezreal and Twisted Fate.
        // Sell the newly bought UUID specifically so a pre-existing copy cannot
        // accidentally make the test pass without exercising RecentPurchase.
        for (const std::string target_name :
             {"Teemo", "Caitlyn", "Ezreal", "Twisted Fate"}) {
            tft::TFTEngine reversal_engine(24680, json_path);
            const auto target = std::find_if(
                catalog.all().begin(), catalog.all().end(),
                [&](const auto& champion) {
                    return champion.api_name.find(target_name) != std::string::npos ||
                        champion.name.find(target_name) != std::string::npos ||
                        champion.character_name.find(target_name) != std::string::npos;
                });
            require(target != catalog.all().end(),
                    ("Catalogo precisa conter " + target_name +
                     " para reproduzir o ciclo do Viewer.").c_str());

            const auto starter = std::find_if(
                catalog.all().begin(), catalog.all().end(),
                [&](const auto& champion) {
                    return champion.internal_id != target->internal_id;
                });
            require(starter != catalog.all().end(),
                    "Catalogo nao possui unidade alternativa para fixture.");
            require(reversal_engine.set_unit_for_testing(0, false, 0, starter->api_name, 1),
                    "Nao foi possivel isolar a unidade inicial da compra de teste.");
            require(reversal_engine.set_player_economy_for_testing(0, 10, 2, 0),
                    "Nao foi possivel configurar ouro para o teste de compra/venda.");
            require(reversal_engine.set_shop_offer_for_testing(0, 0, target->api_name),
                    ("Nao foi possivel colocar " + target_name + " na loja de teste.").c_str());

            const auto before_buy = reversal_engine.get_audit_snapshot();
            std::array<tft::PlayerAction, tft::kPlayersPerLobby> reversal_actions{};
            for (auto& action : reversal_actions)
                action.values = {6, 0, 0, 0, 0, 0};
            reversal_actions[0].values = {0, 0, 0, 0, 0, 0};
            const auto buy_result = reversal_engine.step(reversal_actions);
            const float buy_reward = buy_result.action_rewards[0];

            const auto after_buy = reversal_engine.get_audit_snapshot();
            std::int32_t purchased_slot = -1;
            for (std::size_t slot = 0; slot < after_buy.players[0].bench.size(); ++slot) {
                const auto& unit = after_buy.players[0].bench[slot];
                const bool existed_before = std::any_of(
                    before_buy.players[0].bench.begin(),
                    before_buy.players[0].bench.end(),
                    [&](const auto& old_unit) {
                        return old_unit.occupied && old_unit.uuid == unit.uuid;
                    });
                if (unit.occupied && unit.champion_id == target->api_name && !existed_before) {
                    purchased_slot = static_cast<std::int32_t>(slot);
                    break;
                }
            }
            require(purchased_slot >= 0,
                    ("Compra de " + target_name + " nao deixou a nova copia no banco.").c_str());
            reversal_actions[0].values = {5, 0, purchased_slot, 0, 0, 0};
            const auto sell_result = reversal_engine.step(reversal_actions);
            const float sell_reward = sell_result.action_rewards[0];
            require(sell_reward < 0.0f,
                    ("Venda imediata de " + target_name +
                     " recebeu recompensa nao negativa; RecentPurchase foi ignorado.").c_str());
            require(buy_reward + sell_reward <= -0.05f,
                    ("Compra/venda imediata de " + target_name +
                     " nao manteve a sequencia suficientemente negativa.").c_str());
        }

        std::cout << "TFTEngine + loja/economia/ActionMask/AntiLoop/CompLock: OK\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "TFTEngine + UnitPool: FALHOU: "
                  << e.what() << '\n';
        return 1;
    }
}
