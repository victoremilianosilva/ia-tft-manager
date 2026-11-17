
#pragma once

#include "lobby/ChampionCatalog.hpp"

#include <cstdint>
#include <random>

namespace tft {

// 🏭 Cria instâncias individuais a partir do catálogo.
// Não modifica o catálogo nem controla o estoque.
class UnitInstanceFactory {
public:
    explicit UnitInstanceFactory(
        const ChampionCatalog& catalog,
        std::uint64_t seed = 0
    );

    UnitInstance create(
        std::int32_t champion_internal_id
    );

private:
    const ChampionCatalog& catalog_;
    std::mt19937_64 rng_;

    std::string generate_uuid();
};

} // namespace tft
