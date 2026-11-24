
#pragma once

#include "lobby/ChampionCatalog.hpp"

#include <cstdint>
#include <random>
#include <string>
#include <unordered_set>

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
    // UUIDs are unique within one factory lifetime (one Engine episode).
    // Cross-episode and cross-Engine scope comes from the snapshot envelope.
    std::unordered_set<std::string> issued_uuids_;

    std::string generate_uuid();
};

} // namespace tft
