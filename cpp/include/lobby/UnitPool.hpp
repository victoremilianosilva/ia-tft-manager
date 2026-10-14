#pragma once

#include "lobby/ChampionCatalog.hpp"

#include <cstdint>
#include <optional>
#include <random>
#include <string>
#include <unordered_map>
#include <vector>

namespace tft {

class UnitPool {
public:
    explicit UnitPool(const ChampionCatalog& catalog);

    // Quantas cópias deste campeão ainda estão disponíveis?
    std::int32_t available(std::int32_t champion_internal_id) const;

    // Quantas cópias existem no estoque inicial?
    std::int32_t initial_count(std::int32_t champion_internal_id) const;

    // Tenta retirar uma cópia específica do estoque.
    bool take(std::int32_t champion_internal_id);

    // Sorteia e retira uma cópia de um custo, considerando somente
    // campeões desse custo que ainda tenham estoque.
    // Retorna nullopt quando não há candidato disponível.
    std::optional<std::int32_t> draw(
        std::int32_t cost,
        std::mt19937_64& rng
    );

    // Devolve uma cópia ao estoque.
    bool give_back(std::int32_t champion_internal_id);

    // Restaura todos os estoques às quantidades iniciais.
    void reset();

    bool has_available(std::int32_t champion_internal_id) const;
    std::int64_t total_available() const;
    bool validate() const;

private:
    const ChampionCatalog& catalog_;
    std::unordered_map<std::int32_t, std::int32_t> available_;
    std::unordered_map<std::int32_t, std::int32_t> initial_counts_;
    std::unordered_map<std::int32_t, std::vector<std::int32_t>>
        champion_ids_by_cost_;

    static std::int32_t copies_for_cost(std::int32_t cost);
};

} // namespace tft
