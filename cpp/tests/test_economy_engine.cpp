
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

    // 9. Valores de venda conforme custo e estrelas.
    assert(tft::EconomyEngine::get_sell_value(2, 1) == 2);
    assert(tft::EconomyEngine::get_sell_value(2, 2) == 6);
    assert(tft::EconomyEngine::get_sell_value(2, 3) == 18);

    // 10. O nível máximo impede compra e ganho de XP grátis.
    economy.level = tft::EconomyEngine::MAX_LEVEL;
    economy.xp = 0;
    engine.add_gold(economy, 100);

    assert(!engine.can_buy_xp(economy));
    assert(!engine.add_round_xp(economy));
    assert(engine.get_xp_to_next(economy) == 0);

    std::cout << "EconomyEngine: todos os testes passaram.\n";
    return 0;
}
