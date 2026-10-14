
#pragma once

#include "lobby/TftEngine.hpp"

#include <string>
#include <unordered_map>
#include <vector>

namespace tft {

// 📚 Catálogo imutável durante a partida.
// Não armazena estrelas, UUIDs ou cópias compradas.
class ChampionCatalog {
public:
    // Carrega e valida o JSON.
    explicit ChampionCatalog(const std::string& json_path);

    const std::vector<ChampionDefinition>& all() const noexcept;

    const ChampionDefinition* find_by_id(
        std::int32_t internal_id
    ) const noexcept;

    const ChampionDefinition* find_by_api_name(
        const std::string& api_name
    ) const noexcept;

    std::size_t size() const noexcept;

private:
    std::vector<ChampionDefinition> champions_;
    std::unordered_map<std::string, std::size_t> api_name_index_;

    void load(const std::string& json_path);
    void validate() const;
};

} // namespace tft
