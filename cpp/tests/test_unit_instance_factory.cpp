
#include "lobby/ChampionCatalog.hpp"
#include "lobby/UnitInstanceFactory.hpp"

#include <cassert>
#include <iostream>
#include <stdexcept>

int main(int argc, char** argv) {
    assert(argc == 2);

    tft::ChampionCatalog catalog(argv[1]);
    tft::UnitInstanceFactory factory(catalog, 12345);

    assert(catalog.size() > 0);

    const auto first = factory.create(0);
    const auto second = factory.create(0);

    // As duas unidades referenciam o mesmo campeão.
    assert(first.champion_internal_id == second.champion_internal_id);
    assert(first.champion_id == second.champion_id);

    // Cada instância recebe sua própria identidade.
    assert(first.is_valid());
    assert(second.is_valid());
    assert(first.uuid != second.uuid);

    // Novas unidades começam com uma estrela.
    assert(first.star == 1);
    assert(second.star == 1);
    assert(first.has_valid_star());

    // IDs inválidos devem ser rejeitados.
    bool rejected = false;

    try {
        factory.create(-1);
    } catch (const std::invalid_argument&) {
        rejected = true;
    }

    assert(rejected);

    std::cout << "UnitInstanceFactory: OK\n";
    return 0;
}
