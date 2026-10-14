
#include "lobby/EconomyEngine.hpp"

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

    // 7. Vitória PvP dá +1 ouro e aumenta a streak.
    engine.register_pvp_win(economy);
    assert(economy.gold == 3);
    assert(economy.round_win_gold == 1);
    assert(economy.win_streak == 1);

    // 8. Valores de venda conforme custo e estrelas.
    assert(tft::EconomyEngine::get_sell_value(2, 1) == 2);
    assert(tft::EconomyEngine::get_sell_value(2, 2) == 6);
    assert(tft::EconomyEngine::get_sell_value(2, 3) == 18);

    // 9. O nível máximo impede compra e ganho de XP grátis.
    economy.level = tft::EconomyEngine::MAX_LEVEL;
    economy.xp = 0;
    engine.add_gold(economy, 100);

    assert(!engine.can_buy_xp(economy));
    assert(!engine.add_round_xp(economy));
    assert(engine.get_xp_to_next(economy) == 0);

    std::cout << "EconomyEngine: todos os testes passaram.\n";
    return 0;
}
