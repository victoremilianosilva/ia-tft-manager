
#include "lobby/ChampionCatalog.hpp"
#include "lobby/UnitPool.hpp"

#include <cstdint>
#include <iostream>
#include <random>
#include <stdexcept>

namespace {

void require(bool condition, const char* message) {
    // Diferente de assert, esta validação também funciona em Release.
    if (!condition) {
        throw std::runtime_error(message);
    }
}

std::int32_t find_champion_id_by_cost(
    const tft::ChampionCatalog& catalog,
    std::int32_t cost
) {
    for (const auto& champion : catalog.all()) {
        if (champion.cost == cost) {
            return champion.internal_id;
        }
    }

    throw std::runtime_error("Nenhum campeão encontrado para o custo.");
}

} // namespace

int main(int argc, char** argv) {
    try {
        require(argc == 2, "Informe o caminho de units_gerado.json.");

        tft::ChampionCatalog catalog(argv[1]);
        tft::UnitPool pool(catalog);

        require(catalog.size() > 0, "Catálogo vazio.");
        require(pool.validate(), "Pool inicial inválido.");

        // 1. Verifica as quantidades iniciais por custo.
        const std::int32_t expected[] = {30, 25, 18, 10, 9};

        for (std::int32_t cost = 1; cost <= 5; ++cost) {
            const auto id = find_champion_id_by_cost(catalog, cost);
            const auto count = expected[cost - 1];

            require(
                pool.initial_count(id) == count,
                "Quantidade inicial incorreta."
            );

            require(
                pool.available(id) == count,
                "Estoque atual inicial incorreto."
            );
        }

        // 2. Retira uma cópia e confere a quantidade.
        const auto champion_id = find_champion_id_by_cost(catalog, 1);
        const auto original = pool.available(champion_id);

        require(pool.take(champion_id), "Falha ao retirar cópia.");
        require(
            pool.available(champion_id) == original - 1,
            "Estoque não foi decrementado."
        );

        // 3. Devolve a cópia.
        require(
            pool.give_back(champion_id),
            "Falha ao devolver cópia."
        );

        require(
            pool.available(champion_id) == original,
            "Estoque não foi restaurado após devolução."
        );

        // 4. Impede devolução acima do estoque inicial.
        require(
            !pool.give_back(champion_id),
            "O pool aceitou uma devolução excedente."
        );

        // 5. Esgota o estoque e tenta retirar uma cópia extra.
        const auto initial = pool.initial_count(champion_id);

        for (std::int32_t i = 0; i < initial; ++i) {
            require(pool.take(champion_id), "Falha ao esgotar o estoque.");
        }

        require(
            pool.available(champion_id) == 0,
            "Estoque deveria estar vazio."
        );

        require(
            !pool.has_available(champion_id),
            "has_available deveria retornar false."
        );

        require(
            !pool.take(champion_id),
            "O pool permitiu retirar cópia de estoque vazio."
        );

        // 6. ID inexistente não pode ser retirado nem devolvido.
        require(!pool.take(-1), "Aceitou retirada com ID inválido.");
        require(!pool.give_back(-1), "Aceitou devolução com ID inválido.");
        require(pool.available(-1) == 0, "ID inválido deveria ter estoque zero.");

        // 7. Reset restaura todas as quantidades iniciais.
        pool.reset();

        require(pool.validate(), "Pool inválido depois do reset.");

        for (const auto& champion : catalog.all()) {
            require(
                pool.available(champion.internal_id) ==
                    pool.initial_count(champion.internal_id),
                "Reset não restaurou o estoque de um campeão."
            );
        }

        // 8. O sorteio dentro do mesmo custo deve ser proporcional às
        // cópias restantes, e não uniforme entre campeões ainda disponíveis.
        std::int32_t scarce_id = -1;
        std::int32_t abundant_id = -1;
        for (const auto& champion : catalog.all()) {
            if (champion.cost != 1) continue;
            if (scarce_id < 0) scarce_id = champion.internal_id;
            else if (abundant_id < 0) abundant_id = champion.internal_id;
        }
        require(scarce_id >= 0 && abundant_id >= 0,
                "Catálogo precisa de dois campeões de custo 1 para testar pesos.");

        for (const auto& champion : catalog.all()) {
            if (champion.cost == 1 &&
                champion.internal_id != scarce_id &&
                champion.internal_id != abundant_id) {
                while (pool.take(champion.internal_id)) {}
            }
        }
        for (std::int32_t i = 0; i < pool.initial_count(scarce_id) - 1; ++i)
            require(pool.take(scarce_id), "Falha ao deixar uma cópia do campeão escasso.");
        require(pool.available(scarce_id) == 1 && pool.available(abundant_id) == 30,
                "Fixture proporcional não ficou com estoques 1:30.");

        std::mt19937_64 weighted_rng(0x5E7C18ULL);
        constexpr std::int32_t kWeightedSamples = 30000;
        std::int32_t scarce_draws = 0;
        for (std::int32_t sample = 0; sample < kWeightedSamples; ++sample) {
            const auto drawn = pool.draw_by_cost(1, weighted_rng);
            require(drawn.has_value(), "Sorteio proporcional retornou vazio.");
            if (*drawn == scarce_id) ++scarce_draws;
            require(pool.give_back(*drawn),
                    "Falha ao restaurar cópia após amostra estatística.");
        }
        // P(escasso) = 1 / (1 + 30), portanto ~968 ocorrências em 30 mil.
        // A faixa é larga o bastante para evitar flakiness e rejeita o antigo
        // algoritmo uniforme (que produziria aproximadamente 15 mil).
        require(scarce_draws >= 800 && scarce_draws <= 1150,
                "Draw_by_cost não respeitou a proporção 1:30 do estoque restante.");

        // Um campeão esgotado nunca pode ser sorteado enquanto outro do
        // mesmo custo ainda tiver cópias disponíveis.
        require(pool.take(scarce_id), "Falha ao esgotar a última cópia escassa.");
        for (std::int32_t sample = 0; sample < 100; ++sample) {
            const auto drawn = pool.draw_by_cost(1, weighted_rng);
            require(drawn && *drawn == abundant_id,
                    "Sorteio selecionou campeão sem cópias disponíveis.");
            require(pool.give_back(*drawn),
                    "Falha ao devolver cópia abundante do teste.");
        }
        pool.reset();
        require(pool.validate(), "Pool inválido após teste estatístico do sorteio.");

        std::cout << "UnitPool: OK\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "UnitPool: FALHOU: " << e.what() << '\n';
        return 1;
    }
}
