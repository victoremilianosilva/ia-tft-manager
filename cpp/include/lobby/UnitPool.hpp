
#pragma once

#include "lobby/ChampionCatalog.hpp"

#include <cstdint>
#include <string>
#include <unordered_map>

namespace tft {

class UnitPool {
public:
    explicit UnitPool(const ChampionCatalog& catalog);

    // Quantas cópias deste campeão ainda estão disponíveis?
    std::int32_t available(std::int32_t champion_internal_id) const;

    // Quantas cópias existem no estoque inicial?
    std::int32_t initial_count(std::int32_t champion_internal_id) const;

    // Tenta retirar uma cópia do estoque.
    // Retorna false se o campeão não existir ou estiver esgotado.
    bool take(std::int32_t champion_internal_id);

    // Devolve uma cópia ao estoque.
    // Retorna false se o ID for inválido ou o estoque já estiver cheio.
    bool give_back(std::int32_t champion_internal_id);

    // Restaura todos os estoques às quantidades iniciais.
    void reset();

    // Verifica se ainda existe pelo menos uma cópia disponível.
    bool has_available(std::int32_t champion_internal_id) const;

    // Soma todas as cópias atualmente disponíveis.
    std::int64_t total_available() const;

    // Verifica se todas as quantidades estão dentro dos limites.
    bool validate() const;

private:
    const ChampionCatalog& catalog_;

    // Estoque atual por ID interno do campeão.
    std::unordered_map<std::int32_t, std::int32_t> available_;

    // Quantidade original de cada campeão.
    std::unordered_map<std::int32_t, std::int32_t> initial_counts_;

    static std::int32_t copies_for_cost(std::int32_t cost);
};

} // namespace tft
