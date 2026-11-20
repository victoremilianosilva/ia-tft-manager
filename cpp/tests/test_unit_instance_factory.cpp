
#include "lobby/ChampionCatalog.hpp"
#include "lobby/UnitInstanceFactory.hpp"

#include <cassert>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <unordered_set>

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

    // Value copies/moves preserve physical identity; they do not mint a new unit.
    const auto copied = first;
    assert(copied.uuid == first.uuid);
    auto moved = std::move(copied);
    assert(moved.uuid == first.uuid);

    // A same-seed factory reproduces its local UUID stream. Cross-episode joins
    // must therefore include the Engine-episode scope, not the raw UUID alone.
    tft::UnitInstanceFactory replay_factory(catalog, 12345);
    assert(replay_factory.create(0).uuid == first.uuid);

    // UUID issuance remains unique for the full lifetime of this episode factory.
    std::unordered_set<std::string> issued{first.uuid, second.uuid};
    for (int i = 0; i < 128; ++i) {
        const auto unit = factory.create(0);
        assert(!unit.uuid.empty());
        assert(issued.insert(unit.uuid).second);
    }

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
