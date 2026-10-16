
#include "lobby/EconomyEngine.hpp"

// Keep assertions active even when CMake builds the tests with Release/NDEBUG.
#ifdef NDEBUG
#undef NDEBUG
#endif
#include <cassert>
#include <iostream>
#include <algorithm>
#include <cstdlib>

int main() {
    tft::EconomyEngine engine;
    tft::PlayerEconomy economy;

    // 1. Reset e valores iniciais equivalentes ao Python.
    engine.reset(economy);
    assert(economy.gold == 0);
    assert(economy.level == 2);
    assert(economy.xp == 0);

    // 2. Não permite gastar saldo insuficiente nem valor negativo.
    assert(!engine.spend_gold(economy, 1));
    assert(!engine.spend_gold(economy, -1));
    assert(economy.gold == 0);

    // 3. Compra de XP: 4 gold por 4 XP.
    engine.add_gold(economy, 4);
    const auto xp_result = engine.buy_xp(economy);

    assert(xp_result.success);
    assert(xp_result.xp_gained == 4);
    assert(xp_result.old_level == 2);
    assert(xp_result.new_level == 3);
    assert(economy.gold == 0);
    assert(economy.xp == 2); // 4 XP - 2 necessários para nível 3.

    // 4. Juros: calculados por dezenas, com teto de 5.
    assert(engine.get_interest(0) == 0);
    assert(engine.get_interest(9) == 0);
    assert(engine.get_interest(10) == 1);
    assert(engine.get_interest(19) == 1);
    assert(engine.get_interest(20) == 2);
    assert(engine.get_interest(49) == 4);
    assert(engine.get_interest(50) == 5);
    assert(engine.get_interest(100) == 5);

    // 5. Bônus de streak.
    engine.reset(economy);
    engine.register_win(economy);
    assert(engine.get_streak(economy) == 1);
    assert(engine.get_streak_gold(economy) == 0);

    engine.register_win(economy);
    assert(engine.get_streak(economy) == 2);
    assert(engine.get_streak_gold(economy) == 1);

    engine.register_loss(economy);
    assert(engine.get_streak(economy) == -1);
    assert(economy.win_streak == 0);

    // 6. Renda por rodada e XP grátis.
    engine.reset(economy);
    auto round1 = engine.resolve_round(economy, 1);
    assert(round1.base_gold == 0);
    assert(economy.level == 3);
    assert(economy.xp == 0);

    auto round2 = engine.resolve_round(economy, 2);
    assert(round2.base_gold == 2);
    assert(round2.new_gold == 2);
    assert(economy.level == 3);
    assert(economy.xp == 2);

    // 7. Renda da rodada usa o saldo anterior à renda para calcular juros.
    engine.reset(economy);
    economy.gold = 19;
    economy.win_streak = 2;
    const auto income_round = engine.resolve_round(economy, 3);
    assert(income_round.old_gold == 19);
    assert(income_round.base_gold == 2);
    assert(income_round.interest_gold == 1);
    assert(income_round.streak_gold == 1);
    assert(income_round.new_gold == 23);
    assert(income_round.total_gold == 4);
    assert(economy.round_gold == 4);
    assert(economy.round_interest == 1);
    assert(economy.round_base_gold == 2);
    assert(economy.round_streak_gold == 1);

    // 8. Vitória PvP credita +1 imediatamente e registra o bônus
    // para o relatório da próxima resolução, sem duplicar o crédito.
    engine.reset(economy);
    economy.gold = 2;
    engine.register_pvp_win(economy);
    assert(economy.gold == 3);
    assert(economy.round_win_gold == 1);
    assert(economy.win_streak == 1);

    const auto win_round = engine.resolve_round(economy, 3);
    assert(win_round.win_gold == 1);
    assert(win_round.base_gold == 2);
    assert(win_round.interest_gold == 0);
    assert(win_round.streak_gold == 0);
    assert(win_round.new_gold == 5);
    assert(win_round.total_gold == 3); // Renda base + bônus de vitória já creditado.
    assert(economy.round_win_gold == 0); // Não pode ser contabilizado duas vezes.

    // 9. Valores de venda: unidades de 1 custo são exceção;
    // unidades aprimoradas de custo >= 2 perdem 1 ouro na combinação.
    assert(tft::EconomyEngine::get_sell_value(1, 1) == 1);
    assert(tft::EconomyEngine::get_sell_value(1, 2) == 3);
    assert(tft::EconomyEngine::get_sell_value(1, 3) == 9);
    assert(tft::EconomyEngine::get_sell_value(2, 1) == 2);
    assert(tft::EconomyEngine::get_sell_value(2, 2) == 5);
    assert(tft::EconomyEngine::get_sell_value(2, 3) == 17);
    assert(tft::EconomyEngine::get_sell_value(4, 2) == 11);
    assert(tft::EconomyEngine::get_sell_value(4, 3) == 35);
    assert(tft::EconomyEngine::get_sell_value(5, 2) == 14);
    assert(tft::EconomyEngine::get_sell_value(5, 3) == 44);

    // 10. O nível máximo impede compra e ganho de XP grátis.
    economy.level = tft::EconomyEngine::MAX_LEVEL;
    economy.xp = 0;
    engine.add_gold(economy, 100);

    assert(!engine.can_buy_xp(economy));
    assert(!engine.add_round_xp(economy));
    assert(engine.get_xp_to_next(economy) == 0);

    // 11. Equivalência de streak nos limites configurados pelo Python.
    engine.reset(economy);
    for (int streak = 0; streak <= 7; ++streak) {
        economy.win_streak = streak;
        economy.loss_streak = 0;
        const int expected = streak < 2 ? 0 : streak <= 4 ? 1 : streak == 5 ? 2 : 3;
        assert(engine.get_streak_gold(economy) == expected);
        economy.win_streak = 0;
        economy.loss_streak = streak;
        assert(engine.get_streak_gold(economy) == expected);
    }

    // 12. Progressão de XP por compra e limite máximo de nível.
    engine.reset(economy);
    economy.gold = 40;
    economy.level = 3;
    economy.xp = 0;
    auto xp_purchase = engine.buy_xp(economy);
    assert(xp_purchase.success && economy.gold == 36 && economy.xp == 4);
    xp_purchase = engine.buy_xp(economy);
    assert(xp_purchase.success && economy.gold == 32 && economy.level == 4);
    assert(economy.xp == 2); // 8 XP menos os 6 necessários para subir.
    economy.level = tft::EconomyEngine::MAX_LEVEL;
    economy.xp = 0;
    const auto gold_at_max_level = economy.gold;
    xp_purchase = engine.buy_xp(economy);
    assert(!xp_purchase.success);
    assert(economy.gold == gold_at_max_level && economy.xp == 0);

    // 13. Renda base por rodada deve corresponder à configuração Python.
    engine.reset(economy);
    const int expected_income[] = {0, 2, 2, 3, 4, 5, 5};
    for (int round = 1; round <= 7; ++round) {
        const auto income = engine.resolve_round(economy, round);
        assert(income.base_gold == expected_income[round - 1]);
        assert(income.passive_gold == expected_income[round - 1]);
    }

    // 14. Juros são calculados antes de renda/streak e limitados a 5.
    engine.reset(economy);
    economy.gold = 50;
    economy.loss_streak = 6;
    const auto max_interest_round = engine.resolve_round(economy, 6);
    assert(max_interest_round.interest_gold == 5);
    assert(max_interest_round.streak_gold == 3);
    assert(max_interest_round.base_gold == 5);
    assert(max_interest_round.new_gold == 63);

    std::cout << "EconomyEngine: todos os testes passaram.\n";
    return 0;
}
