
#include "lobby/UnitInstanceFactory.hpp"

#include <array>
#include <iomanip>
#include <sstream>
#include <stdexcept>

namespace tft {

UnitInstanceFactory::UnitInstanceFactory(
    const ChampionCatalog& catalog,
    std::uint64_t seed
)
    : catalog_(catalog),
      rng_(seed) {
}

UnitInstance UnitInstanceFactory::create(
    std::int32_t champion_internal_id
) {
    const ChampionDefinition* champion =
        catalog_.find_by_id(champion_internal_id);

    if (champion == nullptr) {
        throw std::invalid_argument(
            "ID de campeao inexistente no catalogo: " +
            std::to_string(champion_internal_id)
        );
    }

    UnitInstance unit{};

    unit.champion_internal_id = champion->internal_id;
    unit.champion_id = champion->api_name;
    unit.uuid = generate_uuid();
    unit.star = 1;

    return unit;
}

std::string UnitInstanceFactory::generate_uuid() {
    // Gera 128 bits usando o gerador inicializado pelo seed.
    std::array<std::uint8_t, 16> bytes{};

    for (std::size_t i = 0; i < bytes.size(); i += 8) {
        const std::uint64_t value = rng_();

        for (std::size_t j = 0; j < 8; ++j) {
            bytes[i + j] = static_cast<std::uint8_t>(
                (value >> (j * 8)) & 0xFF
            );
        }
    }

    // Formato UUID v4: versão e variante.
    bytes[6] = static_cast<std::uint8_t>(
        (bytes[6] & 0x0F) | 0x40
    );

    bytes[8] = static_cast<std::uint8_t>(
        (bytes[8] & 0x3F) | 0x80
    );

    std::ostringstream output;
    output << std::hex << std::setfill('0');

    for (std::size_t i = 0; i < bytes.size(); ++i) {
        output << std::setw(2)
               << static_cast<unsigned int>(bytes[i]);

        if (i == 3 || i == 5 || i == 7 || i == 9) {
            output << '-';
        }
    }

    return output.str();
}

} // namespace tft
