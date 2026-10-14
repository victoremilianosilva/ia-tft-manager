
#include "lobby/ChampionCatalog.hpp"

#include <nlohmann/json.hpp>

#include <cmath>
#include <fstream>
#include <stdexcept>
#include <unordered_set>
#include <utility>

namespace tft {
namespace {

using Json = nlohmann::json;

std::string get_string(
    const Json& obj,
    const char* key,
    const std::string& fallback = ""
) {
    if (!obj.is_object() || !obj.contains(key) ||
        !obj[key].is_string()) {
        return fallback;
    }

    return obj[key].get<std::string>();
}

double get_number(
    const Json& obj,
    const char* key,
    double fallback = 0.0
) {
    if (!obj.is_object() || !obj.contains(key) ||
        !obj[key].is_number()) {
        return fallback;
    }

    const double value = obj[key].get<double>();

    if (!std::isfinite(value)) {
        throw std::runtime_error(
            std::string("Valor numerico invalido: ") + key
        );
    }

    return value;
}

bool get_bool(
    const Json& obj,
    const char* key,
    bool fallback = false
) {
    if (!obj.is_object() || !obj.contains(key) ||
        !obj[key].is_boolean()) {
        return fallback;
    }

    return obj[key].get<bool>();
}

std::vector<std::string> get_strings(
    const Json& obj,
    const char* key
) {
    std::vector<std::string> result;

    if (!obj.is_object() || !obj.contains(key)) {
        return result;
    }

    if (!obj[key].is_array()) {
        throw std::runtime_error(
            std::string("Campo deve ser uma lista: ") + key
        );
    }

    for (const auto& value : obj[key]) {
        if (!value.is_string()) {
            throw std::runtime_error(
                std::string("Elemento invalido em: ") + key
            );
        }

        result.push_back(value.get<std::string>());
    }

    return result;
}

ChampionStats parse_stats(const Json& json) {
    ChampionStats stats{};

    stats.max_hp = get_number(json, "max_hp");
    stats.attack_damage = get_number(json, "attack_damage");
    stats.attack_speed = get_number(json, "attack_speed");
    stats.armor = get_number(json, "armor");
    stats.magic_resist = get_number(json, "magic_resist");
    stats.attack_range = get_number(json, "attack_range");

    return stats;
}

ChampionCombatProfile parse_combat_profile(
    const Json& json
) {
    ChampionCombatProfile profile{};

    profile.role = static_cast<std::int32_t>(
        get_number(json, "role", 3)
    );

    profile.role_name = get_string(
        json, "role_name", "fighter"
    );

    profile.frontline = get_bool(json, "frontline");
    profile.backline = get_bool(json, "backline");

    profile.is_tank = get_bool(json, "is_tank");
    profile.is_carry = get_bool(json, "is_carry");
    profile.is_support = get_bool(json, "is_support");
    profile.is_fighter = get_bool(json, "is_fighter");
    profile.is_assassin = get_bool(json, "is_assassin");

    profile.attack_range = get_number(json, "attack_range");
    profile.attack_speed = get_number(json, "attack_speed");
    profile.attack_damage = get_number(json, "attack_damage");
    profile.armor = get_number(json, "armor");
    profile.magic_resist = get_number(json, "magic_resist");
    profile.max_hp = get_number(json, "max_hp");
    profile.max_mana = get_number(json, "max_mana");

    return profile;
}

ChampionAbility parse_ability(const Json& json) {
    ChampionAbility ability{};

    if (!json.is_object()) {
        return ability;
    }

    ability.name = get_string(json, "name");
    ability.description = get_string(json, "desc");
    ability.icon = get_string(json, "icon");

    if (!json.contains("variables")) {
        return ability;
    }

    if (!json["variables"].is_array()) {
        throw std::runtime_error(
            "ability.variables deve ser uma lista."
        );
    }

    for (const auto& variable_json : json["variables"]) {
        if (!variable_json.is_object()) {
            throw std::runtime_error(
                "Variavel de habilidade invalida."
            );
        }

        ChampionAbilityVariable variable;
        variable.name = get_string(variable_json, "name");

        if (variable.name.empty()) {
            throw std::runtime_error(
                "Variavel de habilidade sem nome."
            );
        }

        
        if (variable_json.contains("value")) {
            const auto& values = variable_json["value"];

            // Alguns campeões possuem value=null no JSON.
            // Nesse caso, a variável existe, mas não possui valores
            // numéricos para armazenar.
            if (values.is_null()) {
                // Mantém a variável e seu nome, com values vazio.
            } else {
                if (!values.is_array()) {
                    throw std::runtime_error(
                        "ability.variables[].value deve ser uma lista "
                        "ou null."
                    );
                }

                for (const auto& value : values) {
                    if (!value.is_number()) {
                        throw std::runtime_error(
                            "Valor nao numerico em habilidade."
                        );
                    }

                    const double number = value.get<double>();

                    if (!std::isfinite(number)) {
                        throw std::runtime_error(
                            "Valor nao finito em habilidade."
                        );
                    }

                    variable.values.push_back(number);
                }
            }
        }

        ability.variables.push_back(std::move(variable));
    }

    return ability;
}

ChampionDefinition parse_champion(
    const Json& json,
    std::size_t index
) {
    if (!json.is_object()) {
        throw std::runtime_error(
            "Cada campeao precisa ser um objeto JSON."
        );
    }

    ChampionDefinition champion{};

    champion.internal_id = static_cast<std::int32_t>(index);

    champion.api_name = get_string(json, "apiName");
    champion.character_name = get_string(json, "characterName");
    champion.name = get_string(json, "name");

    champion.cost = static_cast<std::int32_t>(
        get_number(json, "cost", 1)
    );

    champion.role = static_cast<std::int32_t>(
        get_number(json, "role", 3)
    );

    champion.role_name = get_string(
        json, "role_name", "fighter"
    );

    champion.traits = get_strings(json, "traits");

    if (json.contains("stats")) {
        champion.stats = parse_stats(json["stats"]);
    }

    if (json.contains("combat_profile")) {
        champion.combat_profile =
            parse_combat_profile(json["combat_profile"]);
    }

    if (json.contains("ability")) {
        champion.ability = parse_ability(json["ability"]);
    }

    champion.icon = get_string(json, "icon");
    champion.square_icon = get_string(json, "squareIcon");
    champion.tile_icon = get_string(json, "tileIcon");

    return champion;
}

} // namespace

ChampionCatalog::ChampionCatalog(
    const std::string& json_path
) {
    load(json_path);
    validate();
}

void ChampionCatalog::load(const std::string& json_path) {
    std::ifstream file(json_path);

    if (!file.is_open()) {
        throw std::runtime_error(
            "Nao foi possivel abrir o catalogo: " + json_path
        );
    }

    Json root;

    try {
        file >> root;
    } catch (const Json::exception& error) {
        throw std::runtime_error(
            "JSON de campeoes invalido: " +
            std::string(error.what())
        );
    }

    if (!root.is_array()) {
        throw std::runtime_error(
            "O catalogo deve ser uma lista JSON."
        );
    }

    champions_.clear();
    api_name_index_.clear();

    champions_.reserve(root.size());

    for (std::size_t i = 0; i < root.size(); ++i) {
        auto champion = parse_champion(root[i], i);

        const auto [it, inserted] =
            api_name_index_.emplace(
                champion.api_name, champions_.size()
            );

        if (!inserted) {
            throw std::runtime_error(
                "apiName duplicado: " + champion.api_name
            );
        }

        champions_.push_back(std::move(champion));
    }
}

void ChampionCatalog::validate() const {
    if (champions_.empty()) {
        throw std::runtime_error(
            "O catalogo nao possui campeoes."
        );
    }

    for (const auto& champion : champions_) {
        if (champion.api_name.empty()) {
            throw std::runtime_error(
                "Campeao sem apiName."
            );
        }

        if (champion.name.empty()) {
            throw std::runtime_error(
                "Campeao sem nome: " + champion.api_name
            );
        }

        if (champion.cost < 1 || champion.cost > 5) {
            throw std::runtime_error(
                "Custo fora do intervalo esperado para " +
                champion.api_name
            );
        }

        const auto& s = champion.stats;

        if (s.max_hp < 0.0 ||
            s.attack_damage < 0.0 ||
            s.attack_speed < 0.0 ||
            s.armor < 0.0 ||
            s.magic_resist < 0.0 ||
            s.attack_range < 0.0) {
            throw std::runtime_error(
                "Atributo negativo para " + champion.api_name
            );
        }
    }
}

const std::vector<ChampionDefinition>&
ChampionCatalog::all() const noexcept {
    return champions_;
}

const ChampionDefinition*
ChampionCatalog::find_by_id(
    std::int32_t internal_id
) const noexcept {
    if (internal_id < 0 ||
        static_cast<std::size_t>(internal_id) >= champions_.size()) {
        return nullptr;
    }

    return &champions_[static_cast<std::size_t>(internal_id)];
}

const ChampionDefinition*
ChampionCatalog::find_by_api_name(
    const std::string& api_name
) const noexcept {
    const auto it = api_name_index_.find(api_name);

    if (it == api_name_index_.end()) {
        return nullptr;
    }

    return &champions_[it->second];
}

std::size_t ChampionCatalog::size() const noexcept {
    return champions_.size();
}

} // namespace tft
