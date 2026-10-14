
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

        require(
            engine.pool_total_available() == total_before,
            "Reset alterou a quantidade total do estoque."
        );

        for (const auto& champion : catalog.all()) {
            require(
                engine.pool_available(champion.internal_id) ==
                    engine.pool_initial_count(champion.internal_id),
                "Reset não restaurou o estoque de um campeão."
            );
        }

        // Valida renda, máscara e compra a partir da loja inicial.
        std::array<tft::PlayerAction, tft::kPlayersPerLobby> actions{};
        for (auto& action : actions) action.values = {6, 0, 0, 0, 0, 0};
        engine.step(actions); // rodada 1: sem renda
        engine.step(actions); // rodada 2: +2 de ouro
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
        require(bought.players[0].gold == 3,
                "Compra não consumiu 1 ouro antes da renda da rodada.");

        std::cout << "TFTEngine + loja/economia: OK\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "TFTEngine + UnitPool: FALHOU: "
                  << e.what() << '\n';
        return 1;
    }
}
