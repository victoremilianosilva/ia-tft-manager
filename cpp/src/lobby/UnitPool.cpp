
#include "lobby/UnitPool.hpp"

#include <stdexcept>

namespace tft {

UnitPool::UnitPool(const ChampionCatalog& catalog)
    : catalog_(catalog) {

    // Inicializa o estoque de cada campeão do catálogo.
    for (const auto& champion : catalog_.all()) {
        const auto id = champion.internal_id;
        const auto count = copies_for_cost(champion.cost);

        // IDs duplicados indicam um problema no catálogo.
        if (!initial_counts_.emplace(id, count).second) {
            throw std::runtime_error(
                "ID interno duplicado ao inicializar UnitPool."
            );
        }

        available_.emplace(id, count);
    }

    if (!validate()) {
        throw std::runtime_error(
            "UnitPool foi inicializado com estoque inválido."
        );
    }
}

std::int32_t UnitPool::copies_for_cost(std::int32_t cost) {
    // Mantém as quantidades usadas pela implementação Python.
    switch (cost) {
        case 1: return 30;
        case 2: return 25;
        case 3: return 18;
        case 4: return 10;
        case 5: return 9;
        default:
            throw std::invalid_argument(
                "Custo inválido ao inicializar UnitPool."
            );
    }
}

std::int32_t UnitPool::available(
    std::int32_t champion_internal_id
) const {
    const auto it = available_.find(champion_internal_id);

    if (it == available_.end()) {
        return 0;
    }

    return it->second;
}

std::int32_t UnitPool::initial_count(
    std::int32_t champion_internal_id
) const {
    const auto it = initial_counts_.find(champion_internal_id);

    if (it == initial_counts_.end()) {
        return 0;
    }

    return it->second;
}

bool UnitPool::take(std::int32_t champion_internal_id) {
    auto it = available_.find(champion_internal_id);

    // Campeão inexistente ou estoque esgotado.
    if (it == available_.end() || it->second <= 0) {
        return false;
    }

    --it->second;
    return true;
}

bool UnitPool::give_back(std::int32_t champion_internal_id) {
    auto it = available_.find(champion_internal_id);
    const auto initial_it = initial_counts_.find(champion_internal_id);

    // O ID precisa existir nos dois mapas.
    if (it == available_.end() ||
        initial_it == initial_counts_.end()) {
        return false;
    }

    // Evita devolver mais cópias do que o estoque original.
    if (it->second >= initial_it->second) {
        return false;
    }

    ++it->second;
    return true;
}

void UnitPool::reset() {
    // Reconstrói o estoque atual usando as quantidades originais.
    available_ = initial_counts_;
}

bool UnitPool::has_available(
    std::int32_t champion_internal_id
) const {
    return available(champion_internal_id) > 0;
}

std::int64_t UnitPool::total_available() const {
    std::int64_t total = 0;

    for (const auto& [id, count] : available_) {
        (void)id;
        total += count;
    }

    return total;
}

bool UnitPool::validate() const {
    // Os mapas devem representar exatamente os mesmos campeões.
    if (available_.size() != initial_counts_.size()) {
        return false;
    }

    for (const auto& [id, initial] : initial_counts_) {
        const auto current_it = available_.find(id);

        if (current_it == available_.end()) {
            return false;
        }

        const auto current = current_it->second;

        // O estoque nunca pode ser negativo nem superar o inicial.
        if (initial < 0 || current < 0 || current > initial) {
            return false;
        }
    }

    return true;
}

} // namespace tft
