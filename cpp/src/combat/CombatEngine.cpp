
#include "CombatEngine.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <limits>
#include <queue>
#include <random>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace tft {
namespace {

struct RuntimeUnit {
    CombatUnit unit;
    float initial_hp = 0.0f;
    float damage_dealt = 0.0f;
    float damage_taken = 0.0f;
    float healing_done = 0.0f;
    float shield_hp = 0.0f;
    int attacks = 0;
    int ability_casts = 0;
    int kills = 0;
};

struct ScheduledEvent {
    float time;
    std::uint64_t order;
    std::size_t unit_index;
};

struct LaterEvent {
    bool operator()(const ScheduledEvent& a,
                    const ScheduledEvent& b) const {
        if (a.time != b.time) return a.time > b.time;
        return a.order > b.order;
    }
};

void set_error(CombatResult& result,
               const std::string& code,
               const std::string& message) {
    result.success = false;
    result.completed = false;
    result.error_code = code;
    result.error_message = message;
}

int distance_between(const CombatUnit& a, const CombatUnit& b) {
    return std::abs(a.position.x - b.position.x)
         + std::abs(a.position.y - b.position.y);
}

bool is_alive(const RuntimeUnit& unit) {
    return unit.unit.alive && unit.unit.hp > 0.0f;
}

int count_alive(const std::vector<RuntimeUnit>& units,
                UnitTeam team) {
    int count = 0;
    for (const auto& u : units) {
        if (u.unit.team == team && is_alive(u)) ++count;
    }
    return count;
}

float total_remaining_hp(const std::vector<RuntimeUnit>& units,
                         UnitTeam team) {
    float total = 0.0f;
    for (const auto& u : units) {
        if (u.unit.team == team && is_alive(u)) {
            total += u.unit.hp;
        }
    }
    return total;
}

float mitigate_physical_damage(float damage, float armor) {
    // Fórmula compatível com armadura positiva e negativa.
    float multiplier;
    if (armor >= 0.0f) {
        multiplier = 100.0f / (100.0f + armor);
    } else {
        multiplier = 2.0f - (100.0f / (100.0f - armor));
    }
    return std::max(0.0f, damage * multiplier);
}

bool apply_item_stats(CombatUnit& unit, std::string& error) {
    if (unit.items.size() > 3) {
        error = "Uma unidade nao pode carregar mais de tres itens.";
        return false;
    }

    for (const auto& item : unit.items) {
        const float values[] = {
            item.attack_damage, item.ability_power, item.attack_speed,
            item.critical_strike_chance, item.critical_strike_damage,
            item.health, item.armor, item.magic_resist, item.mana,
            item.omnivamp, item.damage_amplification, item.damage_reduction
        };
        for (const float value : values) {
            if (!std::isfinite(value) || value < 0.0f) {
                error = "Item possui atributo nao finito ou negativo.";
                return false;
            }
        }

        // CombatItem values are additive bonuses. Percentages are represented
        // as fractions (e.g. 0.15 = +15% attack speed / damage amplification).
        unit.attack_damage += item.attack_damage;
        unit.ability_power += item.ability_power;
        unit.attack_speed += item.attack_speed;
        unit.critical_strike_chance += item.critical_strike_chance;
        unit.critical_strike_damage += item.critical_strike_damage;
        unit.max_hp += item.health;
        unit.hp += item.health;
        unit.armor += item.armor;
        unit.magic_resist += item.magic_resist;
        unit.mana += item.mana;
        unit.omnivamp += item.omnivamp;
        unit.damage_amplification += item.damage_amplification;
        unit.damage_reduction += item.damage_reduction;
    }

    if (!std::isfinite(unit.max_hp) || !std::isfinite(unit.hp) ||
        !std::isfinite(unit.attack_damage) || !std::isfinite(unit.attack_speed) ||
        !std::isfinite(unit.ability_power) || !std::isfinite(unit.mana) ||
        !std::isfinite(unit.critical_strike_chance) ||
        !std::isfinite(unit.critical_strike_damage) ||
        !std::isfinite(unit.armor) || !std::isfinite(unit.magic_resist) ||
        !std::isfinite(unit.omnivamp) ||
        !std::isfinite(unit.damage_amplification) ||
        !std::isfinite(unit.damage_reduction)) {
        error = "A soma dos atributos de itens excede os limites numericos.";
        return false;
    }
    unit.critical_strike_chance =
        std::clamp(unit.critical_strike_chance, 0.0f, 1.0f);
    unit.damage_reduction = std::clamp(unit.damage_reduction, 0.0f, 1.0f);
    unit.omnivamp = std::clamp(unit.omnivamp, 0.0f, 1.0f);
    return true;
}

void append_generic_event(CombatResult& result,
                          float time,
                          const std::string& type,
                          int source,
                          int target,
                          float value = 0.0f) {
    if (!result.events.empty() || true) {
        // A configuração controla o registro detalhado.
        // O chamador só invoca esta função quando record_events está ativo.
        CombatEvent event;
        event.timestamp = time;
        event.type = type;
        event.source_unit_id = source;
        event.target_unit_id = target;
        event.value = value;
        result.events.push_back(event);
    }
}

} // namespace

CombatResult CombatEngine::simulate(const CombatInput& input) const {
    CombatResult result;
    result.context = input.context;
    result.success = true;
    result.completed = false;
    result.winner = CombatWinner::DRAW;

    const auto& config = input.config;

    if (config.board_rows <= 0 || config.board_cols <= 0) {
        set_error(result, "INVALID_BOARD_SIZE",
                  "As dimensoes do tabuleiro devem ser positivas.");
        return result;
    }

    if (!std::isfinite(config.max_duration) ||
        config.max_duration <= 0.0f) {
        set_error(result, "INVALID_MAX_DURATION",
                  "max_duration deve ser finito e positivo.");
        return result;
    }

    if (config.max_events == 0) {
        set_error(result, "INVALID_MAX_EVENTS",
                  "max_events deve ser maior que zero.");
        return result;
    }

    std::unordered_set<int> ids;
    std::unordered_set<int> occupied_a;
    std::unordered_set<int> occupied_b;
    std::vector<RuntimeUnit> units;

    auto load_team = [&](const CombatTeam& team,
                         UnitTeam expected,
                         std::unordered_set<int>& occupied) -> bool {
        if (team.team != expected || team.units.empty()) {
            set_error(result, "INVALID_TEAM",
                      "Equipe vazia ou identificacao incorreta.");
            return false;
        }

        if (!std::isfinite(team.player_hp) || team.player_hp <= 0.0f) {
            set_error(result, "INVALID_PLAYER_HP",
                      "A vida do jogador deve ser positiva.");
            return false;
        }

        for (const auto& unit : team.units) {
            if (unit.id < 0 || !ids.insert(unit.id).second) {
                set_error(result, "INVALID_UNIT_ID",
                          "IDs devem ser unicos e nao negativos.");
                return false;
            }

            if (unit.team != expected || !unit.alive ||
                unit.star < 1 || unit.star > 3) {
                set_error(result, "INVALID_UNIT",
                          "Equipe, estado ou estrelas da unidade invalidos.");
                return false;
            }

            if (unit.position.x < 0 ||
                unit.position.x >= config.board_cols ||
                unit.position.y < 0 ||
                unit.position.y >= config.board_rows) {
                set_error(result, "INVALID_POSITION",
                          "Unidade fora dos limites do tabuleiro.");
                return false;
            }

            const int key =
                unit.position.y * config.board_cols + unit.position.x;

            if (!occupied.insert(key).second) {
                set_error(result, "DUPLICATE_POSITION",
                          "Duas unidades aliadas ocupam a mesma posicao.");
                return false;
            }

            if (!std::isfinite(unit.hp) ||
                !std::isfinite(unit.max_hp) || unit.max_hp <= 0.0f ||
                unit.hp <= 0.0f || unit.hp > unit.max_hp ||
                !std::isfinite(unit.attack_speed) || unit.attack_speed <= 0.0f ||
                !std::isfinite(unit.attack_damage) || unit.attack_damage < 0.0f ||
                !std::isfinite(unit.attack_range) || unit.attack_range < 0.0f ||
                !std::isfinite(unit.mana) || unit.mana < 0.0f ||
                !std::isfinite(unit.max_mana) || unit.max_mana <= 0.0f ||
                !std::isfinite(unit.ability_power) || unit.ability_power < 0.0f ||
                !std::isfinite(unit.magic_resist) ||
                !std::isfinite(unit.armor) ||
                !std::isfinite(unit.critical_strike_chance) ||
                !std::isfinite(unit.critical_strike_damage) ||
                !std::isfinite(unit.ability.mana_cost) || unit.ability.mana_cost < 0.0f ||
                !std::isfinite(unit.ability.base_damage) || unit.ability.base_damage < 0.0f ||
                !std::isfinite(unit.ability.base_healing) || unit.ability.base_healing < 0.0f ||
                !std::isfinite(unit.ability.shield_amount) || unit.ability.shield_amount < 0.0f ||
                !std::isfinite(unit.ability.ability_power_ratio) || unit.ability.ability_power_ratio < 0.0f ||
                !std::isfinite(unit.ability.attack_damage_ratio) || unit.ability.attack_damage_ratio < 0.0f ||
                !std::isfinite(unit.ability.area_radius) || unit.ability.area_radius < 0.0f) {
                set_error(result, "INVALID_UNIT_ATTRIBUTES",
                          "Atributos numericos invalidos.");
                return false;
            }

            CombatUnit effective_unit = unit;
            std::string item_error;
            if (!apply_item_stats(effective_unit, item_error)) {
                set_error(result, "INVALID_ITEM_ATTRIBUTES", item_error);
                return false;
            }

            if (!std::isfinite(effective_unit.hp) ||
                !std::isfinite(effective_unit.max_hp) ||
                effective_unit.max_hp <= 0.0f ||
                effective_unit.hp <= 0.0f ||
                effective_unit.hp > effective_unit.max_hp ||
                !std::isfinite(effective_unit.attack_speed) ||
                effective_unit.attack_speed <= 0.0f ||
                !std::isfinite(effective_unit.attack_damage) ||
                effective_unit.attack_damage < 0.0f ||
                !std::isfinite(effective_unit.attack_range) ||
                effective_unit.attack_range < 0.0f ||
                !std::isfinite(effective_unit.armor) ||
                !std::isfinite(effective_unit.critical_strike_chance) ||
                !std::isfinite(effective_unit.critical_strike_damage)) {
                set_error(result, "INVALID_UNIT_ATTRIBUTES",
                          "Atributos numericos invalidos.");
                return false;
            }

            units.push_back(RuntimeUnit{effective_unit, effective_unit.hp});
        }
        return true;
    };

    if (!load_team(input.player_a, UnitTeam::PLAYER_A, occupied_a) ||
        !load_team(input.player_b, UnitTeam::PLAYER_B, occupied_b)) {
        return result;
    }

    std::unordered_map<int, std::size_t> index_by_id;
    for (std::size_t i = 0; i < units.size(); ++i) {
        index_by_id[units[i].unit.id] = i;
    }

    std::mt19937_64 rng(
        config.deterministic
            ? (input.seed != 0 ? input.seed : config.seed)
            : std::random_device{}()
    );
    std::uniform_real_distribution<float> roll(0.0f, 1.0f);

    std::priority_queue<
        ScheduledEvent,
        std::vector<ScheduledEvent>,
        LaterEvent
    > queue;

    std::uint64_t sequence = 0;
    auto schedule = [&](std::size_t index, float time) {
        queue.push(ScheduledEvent{time, sequence++, index});
    };

    for (std::size_t i = 0; i < units.size(); ++i) {
        schedule(i, 0.0f);
    }

    float now = 0.0f;

    while (!queue.empty() &&
           result.events_processed < config.max_events) {
        const auto event = queue.top();
        queue.pop();

        if (event.time > config.max_duration) {
            result.timeout = true;
            now = config.max_duration;
            break;
        }

        now = event.time;
        ++result.events_processed;

        auto& actor = units[event.unit_index];
        if (!is_alive(actor) || (!actor.unit.can_attack && !actor.unit.can_cast)) {
            continue;
        }

        // Escolhe o inimigo vivo mais próximo; desempate por ID.
        std::size_t target_index = units.size();
        int best_distance = 1'000'000;

        for (std::size_t i = 0; i < units.size(); ++i) {
            const auto& candidate = units[i];

            if (!is_alive(candidate) ||
                candidate.unit.team == actor.unit.team) {
                continue;
            }

            const int d = distance_between(actor.unit, candidate.unit);
            if (d < best_distance ||
                (d == best_distance &&
                 target_index < units.size() &&
                 candidate.unit.id < units[target_index].unit.id)) {
                best_distance = d;
                target_index = i;
            }
        }

        if (target_index == units.size()) {
            break;
        }

        auto& target = units[target_index];

        // Generic ability resolution uses the ability data supplied by the
        // adapter. It is deliberately data-driven; champion-specific scripts
        // and unmodeled buff/debuff semantics remain outside this resolver.
        const auto& ability = actor.unit.ability;
        const bool ability_has_effect = ability.has_damage || ability.has_healing ||
            ability.has_shield;
        if (actor.unit.can_cast && ability_has_effect &&
            std::isfinite(ability.mana_cost) && ability.mana_cost > 0.0f &&
            actor.unit.mana >= ability.mana_cost) {
            std::vector<std::size_t> ability_targets;
            auto add_target = [&](std::size_t i) {
                if (i < units.size() && is_alive(units[i]) &&
                    std::find(ability_targets.begin(), ability_targets.end(), i) ==
                        ability_targets.end()) {
                    ability_targets.push_back(i);
                }
            };
            auto lowest_hp_ally = [&]() -> std::size_t {
                std::size_t best = units.size();
                float ratio = std::numeric_limits<float>::infinity();
                for (std::size_t i = 0; i < units.size(); ++i) {
                    if (!is_alive(units[i]) || units[i].unit.team != actor.unit.team) continue;
                    const float candidate = units[i].unit.hp / units[i].unit.max_hp;
                    if (candidate < ratio || (candidate == ratio &&
                        (best == units.size() || units[i].unit.id < units[best].unit.id))) {
                        best = i;
                        ratio = candidate;
                    }
                }
                return best;
            };
            switch (ability.target_type) {
            case AbilityTargetType::SELF:
                add_target(event.unit_index);
                break;
            case AbilityTargetType::ALLY: {
                const auto ally = lowest_hp_ally();
                add_target(ally);
                break;
            }
            case AbilityTargetType::ALL_ALLIES:
                for (std::size_t i = 0; i < units.size(); ++i)
                    if (units[i].unit.team == actor.unit.team) add_target(i);
                break;
            case AbilityTargetType::ALL_ENEMIES:
                for (std::size_t i = 0; i < units.size(); ++i)
                    if (units[i].unit.team != actor.unit.team) add_target(i);
                break;
            case AbilityTargetType::RANDOM_ENEMY: {
                std::vector<std::size_t> enemies;
                for (std::size_t i = 0; i < units.size(); ++i)
                    if (is_alive(units[i]) && units[i].unit.team != actor.unit.team)
                        enemies.push_back(i);
                if (!enemies.empty()) {
                    std::uniform_int_distribution<std::size_t> pick(0, enemies.size() - 1);
                    add_target(enemies[pick(rng)]);
                }
                break;
            }
            case AbilityTargetType::LOWEST_HP_ENEMY:
            case AbilityTargetType::HIGHEST_HP_ENEMY: {
                std::size_t best = units.size();
                for (std::size_t i = 0; i < units.size(); ++i) {
                    if (!is_alive(units[i]) || units[i].unit.team == actor.unit.team) continue;
                    if (best == units.size() ||
                        (ability.target_type == AbilityTargetType::LOWEST_HP_ENEMY &&
                         units[i].unit.hp < units[best].unit.hp) ||
                        (ability.target_type == AbilityTargetType::HIGHEST_HP_ENEMY &&
                         units[i].unit.hp > units[best].unit.hp) ||
                        (units[i].unit.hp == units[best].unit.hp &&
                         units[i].unit.id < units[best].unit.id)) best = i;
                }
                add_target(best);
                break;
            }
            case AbilityTargetType::AREA:
                for (std::size_t i = 0; i < units.size(); ++i) {
                    if (!is_alive(units[i]) || units[i].unit.team == actor.unit.team) continue;
                    if (distance_between(units[i].unit, target.unit) <=
                        static_cast<int>(std::max(0.0f, std::ceil(ability.area_radius))))
                        add_target(i);
                }
                if (ability_targets.empty()) add_target(target_index);
                break;
            case AbilityTargetType::ENEMY:
            default:
                add_target(target_index);
                break;
            }

            if (!ability_targets.empty()) {
                actor.unit.mana = std::max(0.0f, actor.unit.mana - ability.mana_cost);
                ++actor.ability_casts;
                AbilityEvent ability_event;
                ability_event.timestamp = now;
                ability_event.source_unit_id = actor.unit.id;
                ability_event.ability_id = ability.api_name;
                for (const auto target_id : ability_targets) {
                    auto& ability_target = units[target_id];
                    ability_event.target_unit_ids.push_back(ability_target.unit.id);

                    if (ability.has_damage) {
                        float raw = std::max(0.0f, ability.base_damage) +
                            std::max(0.0f, ability.ability_power_ratio) *
                                actor.unit.ability_power +
                            std::max(0.0f, ability.attack_damage_ratio) *
                                actor.unit.attack_damage;
                        raw *= std::max(0.0f, 1.0f + actor.unit.damage_amplification);
                        float damage = raw;
                        if (ability.damage_type == DamageType::PHYSICAL)
                            damage = mitigate_physical_damage(damage, ability_target.unit.armor);
                        else if (ability.damage_type == DamageType::MAGIC)
                            damage = mitigate_physical_damage(damage, ability_target.unit.magic_resist);
                        damage *= std::clamp(1.0f - ability_target.unit.damage_reduction, 0.0f, 1.0f);
                        damage = std::min(damage, ability_target.unit.hp + ability_target.shield_hp);
                        const float absorbed = std::min(ability_target.shield_hp, damage);
                        ability_target.shield_hp -= absorbed;
                        const float hp_damage = std::min(ability_target.unit.hp, damage - absorbed);
                        ability_target.unit.hp -= hp_damage;
                        ability_target.damage_taken += damage;
                        actor.damage_dealt += damage;
                        ability_event.damage += damage;
                        if (actor.unit.omnivamp > 0.0f && damage > 0.0f)
                            actor.unit.hp = std::min(actor.unit.max_hp,
                                actor.unit.hp + damage * actor.unit.omnivamp);

                        if (config.record_damage) {
                            DamageEvent de;
                            de.timestamp = now;
                            de.source_unit_id = actor.unit.id;
                            de.target_unit_id = ability_target.unit.id;
                            de.damage_type = ability.damage_type;
                            de.raw_damage = raw;
                            de.final_damage = damage;
                            de.ability_damage = true;
                            result.damage_events.push_back(de);
                        }
                    }

                    if (ability.has_healing) {
                        const float healing = std::max(0.0f, ability.base_healing) +
                            std::max(0.0f, ability.ability_power_ratio) *
                                actor.unit.ability_power;
                        const float actual = std::min(healing,
                            ability_target.unit.max_hp - ability_target.unit.hp);
                        ability_target.unit.hp += actual;
                        actor.healing_done += actual;
                        ability_event.healing += actual;
                    }
                    if (ability.has_shield) {
                        const float shield = std::max(0.0f, ability.shield_amount) +
                            std::max(0.0f, ability.ability_power_ratio) *
                                actor.unit.ability_power;
                        ability_target.shield_hp += shield;
                        ability_event.shield += shield;
                    }

                    if (ability_target.unit.hp <= 0.0f && ability_target.unit.alive) {
                        ability_target.unit.hp = 0.0f;
                        ability_target.unit.alive = false;
                        ++actor.kills;
                        if (config.record_events) {
                            DeathEvent death;
                            death.timestamp = now;
                            death.unit_id = ability_target.unit.id;
                            death.killer_unit_id = actor.unit.id;
                            result.death_events.push_back(death);
                            append_generic_event(result, now, "death",
                                actor.unit.id, ability_target.unit.id);
                        }
                    }
                }
                if (config.record_abilities) result.ability_events.push_back(ability_event);
                if (config.record_events)
                    append_generic_event(result, now, "ability",
                        actor.unit.id, ability_targets.front(), ability_event.damage);
                schedule(event.unit_index, now + std::max(0.05f, 1.0f / actor.unit.attack_speed));
                if (count_alive(units, UnitTeam::PLAYER_A) == 0 ||
                    count_alive(units, UnitTeam::PLAYER_B) == 0) break;
                continue;
            }
        }

        if (actor.unit.can_attack &&
            static_cast<float>(best_distance) <= actor.unit.attack_range) {
            // Ataque básico.
            float raw_damage = actor.unit.attack_damage;
            const bool critical =
                roll(rng) < std::clamp(
                    actor.unit.critical_strike_chance, 0.0f, 1.0f);

            if (critical) {
                raw_damage *= std::max(
                    1.0f, actor.unit.critical_strike_damage);
            }

            raw_damage *= std::max(
                0.0f, 1.0f + actor.unit.damage_amplification);

            float damage = mitigate_physical_damage(
                raw_damage, target.unit.armor);

            damage *= std::clamp(
                1.0f - target.unit.damage_reduction, 0.0f, 1.0f);

            damage = std::min(damage, target.unit.hp);

            const float absorbed = std::min(target.shield_hp, damage);
            target.shield_hp -= absorbed;
            const float hp_damage = std::min(target.unit.hp, damage - absorbed);
            target.unit.hp -= hp_damage;
            target.damage_taken += damage;
            actor.damage_dealt += damage;
            if (actor.unit.omnivamp > 0.0f && damage > 0.0f) {
                actor.unit.hp = std::min(
                    actor.unit.max_hp,
                    actor.unit.hp + damage * actor.unit.omnivamp);
            }
            ++actor.attacks;
            actor.unit.mana = std::min(actor.unit.max_mana, actor.unit.mana + 10.0f);

            if (config.record_damage) {
                DamageEvent de;
                de.timestamp = now;
                de.source_unit_id = actor.unit.id;
                de.target_unit_id = target.unit.id;
                de.damage_type = DamageType::PHYSICAL;
                de.raw_damage = raw_damage;
                de.final_damage = damage;
                de.critical = critical;
                result.damage_events.push_back(de);
            }

            if (config.record_events) {
                AttackEvent ae;
                ae.timestamp = now;
                ae.source_unit_id = actor.unit.id;
                ae.target_unit_id = target.unit.id;
                ae.critical = critical;
                ae.damage = damage;
                result.attack_events.push_back(ae);
                append_generic_event(
                    result, now, "attack", actor.unit.id,
                    target.unit.id, damage);
            }

            if (target.unit.hp <= 0.0f && target.unit.alive) {
                target.unit.hp = 0.0f;
                target.unit.alive = false;
                ++actor.kills;

                if (config.record_events) {
                    DeathEvent de;
                    de.timestamp = now;
                    de.unit_id = target.unit.id;
                    de.killer_unit_id = actor.unit.id;
                    result.death_events.push_back(de);
                    append_generic_event(
                        result, now, "death", actor.unit.id,
                        target.unit.id);
                }
            }

            const float cooldown =
                std::max(0.05f, 1.0f / actor.unit.attack_speed);
            schedule(event.unit_index, now + cooldown);
        } else if (actor.unit.can_move) {
            // Movimento ortogonal: escolhe a casa livre que reduz
            // a distância ao alvo. A ordem fixa garante desempate estável.
            const int dx[] = {0, -1, 1, 0};
            const int dy[] = {-1, 0, 0, 1};

            int best_x = actor.unit.position.x;
            int best_y = actor.unit.position.y;
            int next_distance = best_distance;

            for (int step = 0; step < 4; ++step) {
                const int x = actor.unit.position.x + dx[step];
                const int y = actor.unit.position.y + dy[step];

                if (x < 0 || x >= config.board_cols ||
                    y < 0 || y >= config.board_rows) {
                    continue;
                }

                bool blocked = false;
                for (const auto& other : units) {
                    if (&other == &actor || !is_alive(other)) continue;
                    if (other.unit.position.x == x &&
                        other.unit.position.y == y) {
                        blocked = true;
                        break;
                    }
                }
                if (blocked) continue;

                CombatUnit probe = actor.unit;
                probe.position.x = x;
                probe.position.y = y;
                const int d = distance_between(probe, target.unit);

                if (d < next_distance) {
                    next_distance = d;
                    best_x = x;
                    best_y = y;
                }
            }

            if (best_x != actor.unit.position.x ||
                best_y != actor.unit.position.y) {
                const int from_x = actor.unit.position.x;
                const int from_y = actor.unit.position.y;

                actor.unit.position.x = best_x;
                actor.unit.position.y = best_y;

                if (config.record_positions) {
                    PositionEvent pe;
                    pe.timestamp = now;
                    pe.unit_id = actor.unit.id;
                    pe.from_x = from_x;
                    pe.from_y = from_y;
                    pe.to_x = best_x;
                    pe.to_y = best_y;
                    result.position_events.push_back(pe);
                }

                if (config.record_events) {
                    append_generic_event(
                        result, now, "move", actor.unit.id, -1);
                }
            }

            schedule(event.unit_index, now + 0.25f);
        }

        if (count_alive(units, UnitTeam::PLAYER_A) == 0 ||
            count_alive(units, UnitTeam::PLAYER_B) == 0) {
            break;
        }
    }

    if (!queue.empty() &&
        result.events_processed >= config.max_events) {
        result.timeout = true;
        now = std::min(now, config.max_duration);
    }

    result.duration = std::min(now, config.max_duration);
    result.completed = true;
    result.success = true;

    result.player_a_survivors =
        count_alive(units, UnitTeam::PLAYER_A);
    result.player_b_survivors =
        count_alive(units, UnitTeam::PLAYER_B);

    result.player_a_deaths =
        static_cast<int>(input.player_a.units.size())
        - result.player_a_survivors;
    result.player_b_deaths =
        static_cast<int>(input.player_b.units.size())
        - result.player_b_survivors;

    for (const auto& u : units) {
        if (u.unit.team == UnitTeam::PLAYER_A) {
            result.player_a_damage_dealt += u.damage_dealt;
        } else {
            result.player_b_damage_dealt += u.damage_dealt;
        }

        CombatUnitResult ur;
        ur.unit_id = u.unit.id;
        ur.team = u.unit.team;
        ur.survived = is_alive(u);
        ur.initial_hp = u.initial_hp;
        ur.final_hp = u.unit.hp;
        ur.damage_dealt = u.damage_dealt;
        ur.damage_taken = u.damage_taken;
        ur.kills = u.kills;
        ur.attacks = u.attacks;
        ur.ability_casts = u.ability_casts;
        ur.healing_done = u.healing_done;
        ur.final_x = u.unit.position.x;
        ur.final_y = u.unit.position.y;
        result.units.push_back(ur);
    }

    const int alive_a = result.player_a_survivors;
    const int alive_b = result.player_b_survivors;

    if (alive_a == 0 && alive_b > 0) {
        result.winner = CombatWinner::PLAYER_B;
    } else if (alive_b == 0 && alive_a > 0) {
        result.winner = CombatWinner::PLAYER_A;
    } else {
        const float hp_a = total_remaining_hp(units, UnitTeam::PLAYER_A);
        const float hp_b = total_remaining_hp(units, UnitTeam::PLAYER_B);

        if (alive_a > alive_b) {
            result.winner = CombatWinner::PLAYER_A;
        } else if (alive_b > alive_a) {
            result.winner = CombatWinner::PLAYER_B;
        } else if (hp_a > hp_b) {
            result.winner = CombatWinner::PLAYER_A;
        } else if (hp_b > hp_a) {
            result.winner = CombatWinner::PLAYER_B;
        } else {
            result.winner = CombatWinner::DRAW;
        }
    }

    return result;
}

} // namespace tft