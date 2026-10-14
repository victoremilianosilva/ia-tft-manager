
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

        require(catalog.size() > 0, "Catálogo vazio.");

        for (const auto& champion : catalog.all()) {
            require(
                engine.pool_initial_count(champion.internal_id) > 0,
                "Campeão sem estoque inicial."
            );

            require(
                engine.pool_available(champion.internal_id) ==
                    engine.pool_initial_count(champion.internal_id),
                "Estoque inicial incorreto no motor."
            );
        }

        const auto total_before = engine.pool_total_available();

        // Reset da partida não pode duplicar nem perder cópias.
        engine.reset(12345);

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

        std::cout << "TFTEngine + UnitPool: OK\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "TFTEngine + UnitPool: FALHOU: "
                  << e.what() << '\n';
        return 1;
    }
}
