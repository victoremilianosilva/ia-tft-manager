
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
    int titans_stacks = 0;
    float last_guinsoo_tick = 0.0f;
    float last_dragons_claw_tick = 0.0f;
    float last_redemption_tick = 0.0f;
    float last_archangel_tick = 0.0f;
    float last_quicksilver_tick = 0.0f;
    float last_redbuff_tick = 0.0f;
    float last_bramble_proc = -1000.0f;
    float last_ionic_proc = -1000.0f;
    float shield_expires_at = 0.0f;
    float crown_shield_expires_at = 0.0f;
    float burn_until = 0.0f;
    float burn_next_tick = 0.0f;
    float burn_percent = 0.0f;
    int burn_source_id = -1;
    float grievous_until = 0.0f;
    float armor_shred_until = 0.0f;
    float armor_shred_percent = 0.0f;
    float mr_shred_until = 0.0f;
    float mr_shred_percent = 0.0f;
    int runaan_stacks = 0;
    int power_gauntlet_stacks = 0;
    int challenger_attacks_remaining = 0;
    bool resist_emblem_triggered = false;
    bool assassin_omnivamp_active = false;
    bool bloodthirster_triggered = false;
    bool sterak_triggered = false;
    bool frozen_heart_triggered = false;
    bool guardian_angel_triggered = false;
    bool crown_shield_triggered = false;
    bool night_harvester_bonus_active = false;
    bool hand_of_justice_ad_ap_active = false;
    float hand_of_justice_ad_bonus = 0.0f;
    float hand_of_justice_ap_bonus = 15.0f;
    float guardian_angel_until = 0.0f;
    float guardian_previous_damage_reduction = 0.0f;
    float last_status_tick = 0.0f;
    float mana_regen_per_second = 0.0f;
    float mana_gain_multiplier = 1.0f;
    float base_attack_speed = 1.0f;
    float titans_base_ad = 0.0f;
    float runaans_base_ad = 0.0f;
    std::vector<float> power_gauntlet_stack_times;
    std::unordered_map<std::string, int> generic_effect_charges;
    std::unordered_set<std::string> generic_effects_applied;
    std::unordered_set<std::string> generic_effects_active;
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

bool has_item(const CombatUnit& unit, const char* api_name) {
    return std::any_of(unit.items.begin(), unit.items.end(),
        [&](const CombatItem& item) { return item.api_name == api_name; });
}

void add_titans_stack(RuntimeUnit& unit) {
    if (unit.titans_stacks >= 25) return;
    ++unit.titans_stacks;
    unit.unit.attack_damage += unit.titans_base_ad * 0.02f;
    unit.unit.ability_power += 2.0f;
    if (unit.titans_stacks == 25)
        unit.unit.damage_amplification += 0.10f;
}

float apply_heal(RuntimeUnit& target, float amount, float now) {
    if (target.grievous_until > now) amount *= 0.67f;
    const float actual = std::min(std::max(0.0f, amount),
        std::max(0.0f, target.unit.max_hp - target.unit.hp));
    target.unit.hp += actual;
    return actual;
}

void trigger_defensive_items(RuntimeUnit& unit, float now) {
    if (has_item(unit.unit, "TFT_Item_Bloodthirster") &&
        !unit.bloodthirster_triggered && unit.unit.hp <= unit.unit.max_hp * 0.40f) {
        unit.shield_hp += unit.unit.max_hp * 0.25f;
        unit.shield_expires_at = std::max(unit.shield_expires_at, now + 5.0f);
        unit.bloodthirster_triggered = true;
    }
    if (has_item(unit.unit, "TFT_Item_SteraksGage") &&
        !unit.sterak_triggered && unit.unit.hp <= unit.unit.max_hp * 0.60f) {
        unit.shield_hp += unit.unit.max_hp * 0.40f;
        unit.shield_expires_at = std::max(unit.shield_expires_at, now + 4.0f);
        unit.sterak_triggered = true;
    }
    if (has_item(unit.unit, "TFT_Item_FrozenHeart") &&
        !unit.frozen_heart_triggered && unit.unit.hp <= unit.unit.max_hp * 0.40f) {
        unit.unit.mana = std::min(unit.unit.max_mana, unit.unit.mana + 15.0f);
        unit.shield_hp += unit.unit.max_hp * 0.20f;
        unit.shield_expires_at = std::max(unit.shield_expires_at, now + 60.0f);
        unit.frozen_heart_triggered = true;
    }
    if (has_item(unit.unit, "TFT_Item_GuardianAngel") &&
        !unit.guardian_angel_triggered && unit.unit.hp <= unit.unit.max_hp * 0.60f) {
        unit.guardian_angel_triggered = true;
        unit.guardian_previous_damage_reduction = unit.unit.damage_reduction;
        unit.unit.damage_reduction = 1.0f;
        unit.guardian_angel_until = now + 1.0f;
        const float heal = apply_heal(unit,
            std::max(0.0f, (unit.unit.max_hp - unit.unit.hp) * 0.20f), now);
        if (unit.unit.hp <= 0.0f) unit.unit.hp = unit.unit.max_hp * 0.20f;
        unit.unit.alive = true;
        unit.healing_done += heal;
    }
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

    const float base_attack_damage = unit.attack_damage;
    const float base_max_hp = unit.max_hp;
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

        // Percentuais que o normalizador do catálogo preserva em source_effects,
        // mas que não aparecem como atributo aditivo no campo stats.
        if (item.api_name == "TFT_Item_Deathblade")
            unit.attack_damage += base_attack_damage * 0.55f;
        else if (item.api_name == "TFT_Item_Bloodthirster")
            unit.attack_damage += base_attack_damage * 0.15f;
        else if (item.api_name == "TFT_Item_BlueBuff")
            unit.attack_damage += base_attack_damage * 0.15f;
        else if (item.api_name == "TFT_Item_LastWhisper")
            unit.attack_damage += base_attack_damage * 0.15f;
        else if (item.api_name == "TFT_Item_RunaansHurricane")
            unit.attack_damage += base_attack_damage * 0.10f;
        else if (item.api_name == "TFT_Item_SteraksGage")
            unit.attack_damage += base_attack_damage * 0.45f;
        else if (item.api_name == "TFT_Item_MadredsBloodrazor")
            unit.attack_damage += base_attack_damage * 0.15f;
        else if (item.api_name == "TFT_Item_InfinityEdge")
            unit.attack_damage += base_attack_damage * 0.35f;
        else if (item.api_name == "TFT_Item_WarmogsArmor")
            unit.max_hp += base_max_hp * 0.18f, unit.hp += base_max_hp * 0.18f;
        else if (item.api_name == "TFT_Item_DragonsClaw")
            unit.max_hp += base_max_hp * 0.06f, unit.hp += base_max_hp * 0.06f;
        else if (item.api_name == "TFT_Item_BrambleVest")
            unit.max_hp += base_max_hp * 0.06f, unit.hp += base_max_hp * 0.06f;
        else if (item.api_name == "TFT_Item_RedBuff")
            unit.max_hp += base_max_hp * 0.08f, unit.hp += base_max_hp * 0.08f;
        else if (item.api_name == "TFT_Item_UnstableConcoction") {
            unit.attack_damage += base_attack_damage * 0.15f;
            unit.ability_power += 15.0f;
            unit.omnivamp = std::min(1.0f, unit.omnivamp + 0.12f);
        }
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

bool has_trait(const CombatUnit& unit, const std::string& trait_name) {
    return std::any_of(unit.traits.begin(), unit.traits.end(),
        [&](const CombatTrait& trait) {
            return trait.api_name == trait_name && (trait.active || trait.active_count > 0);
        });
}

bool effect_condition_matches(const CombatUnit& unit,
                              const CombatEffectDefinition& effect) {
    if (effect.condition.empty()) return true;
    if (effect.condition == "has_trait")
        return has_trait(unit, effect.condition_trait);
    if (effect.condition == "role_tank") return unit.role == UnitRole::TANK;
    if (effect.condition == "role_fighter") return unit.role == UnitRole::FIGHTER;
    if (effect.condition == "role_assassin") return unit.role == UnitRole::ASSASSIN;
    if (effect.condition == "role_other")
        return unit.role != UnitRole::TANK &&
               unit.role != UnitRole::FIGHTER &&
               unit.role != UnitRole::ASSASSIN;
    return false;
}

void apply_effect_stat(CombatUnit& unit, const CombatEffectDefinition& effect) {
    float amount = effect.value;
    if (effect.percent_of_stat) {
        if (effect.stat == "attack_damage") amount *= unit.attack_damage;
        else if (effect.stat == "attack_speed") amount *= unit.attack_speed;
        else if (effect.stat == "ability_power") amount *= unit.ability_power;
        else if (effect.stat == "max_hp") amount *= unit.max_hp;
        else if (effect.stat == "armor") amount *= unit.armor;
        else if (effect.stat == "magic_resist") amount *= unit.magic_resist;
    }
    if (effect.stat == "attack_damage") unit.attack_damage += amount;
    else if (effect.stat == "attack_speed") unit.attack_speed += amount;
    else if (effect.stat == "ability_power") unit.ability_power += amount;
    else if (effect.stat == "armor") unit.armor += amount;
    else if (effect.stat == "magic_resist") unit.magic_resist += amount;
    else if (effect.stat == "omnivamp")
        unit.omnivamp = std::clamp(unit.omnivamp + amount, 0.0f, 1.0f);
    else if (effect.stat == "damage_amplification")
        unit.damage_amplification += amount;
    else if (effect.stat == "damage_reduction")
        unit.damage_reduction = std::clamp(unit.damage_reduction + amount, 0.0f, 1.0f);
    else if (effect.stat == "max_hp") {
        unit.max_hp += amount;
        unit.hp += amount;
    }
}

void apply_start_combat_effects(CombatUnit& unit) {
    auto apply = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.trigger == "combat_start" && effect.operation == "add_stat" &&
                effect_condition_matches(unit, effect))
                apply_effect_stat(unit, effect);
        }
    };
    for (const auto& item : unit.items) apply(item.effects);
    for (const auto& trait : unit.traits) {
        if (trait.active || trait.active_count > 0) apply(trait.effects);
    }
}

float effect_attack_bonus(const CombatUnit& unit, DamageType damage_type) {
    float bonus = 0.0f;
    auto accumulate = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.trigger == "on_attack" && effect.operation == "bonus_damage" &&
                effect.damage_type == damage_type &&
                effect_condition_matches(unit, effect))
                bonus += effect.percent_of_max_health
                    ? unit.max_hp * effect.value : effect.value;
        }
    };
    for (const auto& item : unit.items) accumulate(item.effects);
    for (const auto& trait : unit.traits) {
        if (trait.active || trait.active_count > 0) accumulate(trait.effects);
    }
    return bonus;
}

float effect_mana_regeneration(const CombatUnit& unit) {
    float amount = 0.0f;
    auto accumulate = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.operation == "mana_regen" &&
                (effect.trigger.empty() || effect.trigger == "combat_start") &&
                effect_condition_matches(unit, effect))
                amount += effect.value;
        }
    };
    for (const auto& item : unit.items) accumulate(item.effects);
    for (const auto& trait : unit.traits) {
        if (trait.active || trait.active_count > 0) accumulate(trait.effects);
    }
    return amount;
}

template <typename Callback>
void visit_generic_effects(CombatUnit& unit, Callback callback) {
    for (std::size_t item_index = 0; item_index < unit.items.size(); ++item_index) {
        const auto& item = unit.items[item_index];
        for (std::size_t effect_index = 0; effect_index < item.effects.size(); ++effect_index) {
            callback(item.effects[effect_index],
                "item:" + item.api_name + ":" + std::to_string(item_index) + ":");
        }
    }
    for (std::size_t trait_index = 0; trait_index < unit.traits.size(); ++trait_index) {
        auto& trait = unit.traits[trait_index];
        if (!trait.active && trait.active_count <= 0) continue;
        for (std::size_t effect_index = 0; effect_index < trait.effects.size(); ++effect_index) {
            callback(trait.effects[effect_index],
                "trait:" + trait.api_name + ":" + std::to_string(trait_index) + ":");
        }
    }
}

void grant_on_kill_effect_charges(RuntimeUnit& actor) {
    visit_generic_effects(actor.unit, [&](const CombatEffectDefinition& effect,
                                         const std::string& prefix) {
        if (effect.trigger != "on_kill" || effect.operation != "grant_charges" ||
            effect.stack_key.empty() || !effect_condition_matches(actor.unit, effect)) return;
        const int amount = effect.max_stacks > 0
            ? std::min(effect.max_stacks, static_cast<int>(effect.value))
            : static_cast<int>(effect.value);
        if (amount > 0) actor.generic_effect_charges[prefix + effect.stack_key] = amount;
    });
}

float apply_charged_attack_healing(RuntimeUnit& actor, float now) {
    float total = 0.0f;
    visit_generic_effects(actor.unit, [&](const CombatEffectDefinition& effect,
                                         const std::string& prefix) {
        if (effect.trigger != "on_attack" || effect.operation != "heal_max_hp_pct" ||
            effect.stack_key.empty() || !effect_condition_matches(actor.unit, effect)) return;
        auto it = actor.generic_effect_charges.find(prefix + effect.stack_key);
        if (it == actor.generic_effect_charges.end() || it->second <= 0) return;
        total += actor.unit.max_hp * effect.value;
        --it->second;
    });
    return total > 0.0f ? apply_heal(actor, total, now) : 0.0f;
}

void apply_delayed_effects(RuntimeUnit& runtime, float now) {
    visit_generic_effects(runtime.unit, [&](const CombatEffectDefinition& effect,
                                           const std::string& prefix) {
        if (effect.trigger != "after_delay" || effect.operation != "add_stat" ||
            now < effect.delay || !effect_condition_matches(runtime.unit, effect)) return;
        const std::string key = prefix + "delayed:" + effect.stat + ":" +
            std::to_string(effect.delay) + ":" + std::to_string(effect.value);
        if (runtime.generic_effects_applied.insert(key).second)
            apply_effect_stat(runtime.unit, effect);
    });
}

void update_conditional_effects(RuntimeUnit& runtime) {
    visit_generic_effects(runtime.unit, [&](const CombatEffectDefinition& effect,
                                           const std::string& prefix) {
        if (effect.trigger != "while_hp_below" || effect.operation != "add_stat" ||
            effect.health_threshold <= 0.0f ||
            !effect_condition_matches(runtime.unit, effect)) return;
        const std::string key = prefix + "conditional:" + effect.stat + ":" +
            std::to_string(effect.health_threshold) + ":" + std::to_string(effect.value);
        const bool should_be_active = runtime.unit.hp / runtime.unit.max_hp <= effect.health_threshold;
        const bool is_active = runtime.generic_effects_active.contains(key);
        if (should_be_active && !is_active) {
            apply_effect_stat(runtime.unit, effect);
            runtime.generic_effects_active.insert(key);
        } else if (!should_be_active && is_active) {
            CombatEffectDefinition inverse = effect;
            inverse.value = -inverse.value;
            apply_effect_stat(runtime.unit, inverse);
            runtime.generic_effects_active.erase(key);
        }
    });
}

void apply_ally_shield_effects(std::vector<RuntimeUnit>& units,
                               std::size_t shielded_index) {
    if (shielded_index >= units.size()) return;
    const auto team = units[shielded_index].unit.team;
    for (auto& recipient : units) {
        if (recipient.unit.team != team || !is_alive(recipient)) continue;
        visit_generic_effects(recipient.unit,
            [&](const CombatEffectDefinition& effect, const std::string&) {
                if (effect.trigger == "on_ally_shield" &&
                    effect.operation == "add_stat" &&
                    effect_condition_matches(recipient.unit, effect))
                    apply_effect_stat(recipient.unit, effect);
            });
    }
}

float effect_kill_healing(const CombatUnit& unit) {
    float healing = 0.0f;
    auto accumulate = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.trigger == "on_kill" && effect.operation == "heal_max_hp_pct" &&
                effect_condition_matches(unit, effect))
                healing += unit.max_hp * effect.value;
        }
    };
    for (const auto& item : unit.items) accumulate(item.effects);
    for (const auto& trait : unit.traits) {
        if (trait.active || trait.active_count > 0) accumulate(trait.effects);
    }
    return healing;
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
            // Emblems declare granted traits in catalog data, not in item-name switches.
            for (const auto& item : effective_unit.items) {
                if (item.grants_trait.empty()) continue;
                auto it = std::find_if(effective_unit.traits.begin(),
                    effective_unit.traits.end(), [&](const CombatTrait& trait) {
                        return trait.api_name == item.grants_trait;
                    });
                if (it == effective_unit.traits.end()) {
                    CombatTrait granted;
                    granted.api_name = item.grants_trait;
                    granted.name = item.grants_trait;
                    granted.active_count = item.granted_trait_active_count;
                    granted.active = true;
                    effective_unit.traits.push_back(granted);
                } else {
                    it->active_count = std::max(it->active_count,
                        item.granted_trait_active_count);
                    it->active = true;
                }
            }
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
            auto& loaded = units.back();
            apply_start_combat_effects(loaded.unit);
            loaded.base_attack_speed = loaded.unit.attack_speed;
            loaded.titans_base_ad = loaded.unit.attack_damage;
            loaded.runaans_base_ad = loaded.unit.attack_damage;
            if (has_item(loaded.unit, "TFT_Item_AdaptiveHelm"))
                loaded.mana_gain_multiplier = 1.15f;
            for (const auto& item : loaded.unit.items) {
                if (item.api_name == "TFT_Item_AdaptiveHelm") loaded.mana_regen_per_second += 3.0f;
                else if (item.api_name == "TFT_Item_ArchangelsStaff" ||
                         item.api_name == "TFT_Item_HextechGunblade" ||
                         item.api_name == "TFT_Item_Morellonomicon" ||
                         item.api_name == "TFT_Item_SpearOfShojin" ||
                         item.api_name == "TFT_Item_StatikkShiv") loaded.mana_regen_per_second += 1.0f;
                else if (item.api_name == "TFT_Item_BlueBuff") loaded.mana_regen_per_second += 5.0f;
                else if (item.api_name == "TFT_Item_Redemption") loaded.mana_regen_per_second += 2.0f;

            }
            loaded.mana_regen_per_second += effect_mana_regeneration(loaded.unit);
            if (has_item(loaded.unit, "TFT_Item_UnstableConcoction")) {
                loaded.hand_of_justice_ad_bonus =
                    loaded.unit.attack_damage * (0.15f / 1.15f);
                loaded.hand_of_justice_ad_ap_active =
                    loaded.unit.hp / loaded.unit.max_hp > 0.50f;
                if (loaded.hand_of_justice_ad_ap_active) {
                    loaded.unit.attack_damage += loaded.hand_of_justice_ad_bonus;
                    loaded.unit.ability_power += loaded.hand_of_justice_ap_bonus;
                } else {
                    loaded.unit.omnivamp = std::min(1.0f, loaded.unit.omnivamp + 0.12f);
                }
            }
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
        auto& runtime = units[i];
        // Efeitos de início de combate: escudo e mana inicial.
        if (has_item(runtime.unit, "TFT_Item_Crownguard")) {
            runtime.shield_hp += runtime.unit.max_hp * 0.25f;
            runtime.crown_shield_triggered = true;
            runtime.crown_shield_expires_at = 8.0f;
            runtime.shield_expires_at = 8.0f;
        }
        if (has_item(runtime.unit, "TFT_Item_FrozenHeart"))
            runtime.unit.mana = std::min(runtime.unit.max_mana,
                runtime.unit.mana + 20.0f * runtime.mana_gain_multiplier);
        if (has_item(runtime.unit, "TFT_Item_AdaptiveHelm")) {

            if (runtime.unit.role == UnitRole::TANK ||
                runtime.unit.role == UnitRole::FIGHTER) {
                runtime.unit.armor += 30.0f;
                runtime.unit.magic_resist += 30.0f;
            } else {
                runtime.unit.attack_damage *= 1.10f;
                runtime.unit.ability_power *= 1.10f;
            }
        }
        if (has_item(runtime.unit, "TFT_Item_BlueBuff")) {
            runtime.unit.attack_damage *= 1.10f;
            runtime.unit.ability_power *= 1.10f;
        }
        if (has_item(runtime.unit, "TFT_Item_Deathblade"))
            runtime.unit.damage_amplification += 0.10f;
        if (has_item(runtime.unit, "TFT_Item_RabadonsDeathcap"))
            runtime.unit.damage_amplification += 0.15f;
        if (has_item(runtime.unit, "TFT_Item_NightHarvester")) {
            runtime.unit.damage_reduction += 0.05f;
            if (runtime.unit.hp / runtime.unit.max_hp > 0.50f)
                runtime.unit.damage_reduction += 0.15f;
            runtime.night_harvester_bonus_active =
                runtime.unit.hp / runtime.unit.max_hp > 0.50f;
        }
        if (has_item(runtime.unit, "TFT17_Item_FlexTraitEmblemItem")) {
            for (auto& ally : units) {
                if (ally.unit.team != runtime.unit.team ||
                    std::abs(ally.unit.position.y - runtime.unit.position.y) != 0 ||
                    std::abs(ally.unit.position.x - runtime.unit.position.x) > 1) continue;
                if (ally.unit.role == UnitRole::TANK) {
                    ally.unit.armor += 10.0f;
                    ally.unit.magic_resist += 10.0f;
                } else if (ally.unit.role == UnitRole::FIGHTER ||
                           ally.unit.role == UnitRole::ASSASSIN) {
                    ally.unit.omnivamp = std::min(1.0f, ally.unit.omnivamp + 0.10f);
                } else {
                    ally.unit.attack_speed += 0.10f;
                }
            }
        }
        if (has_item(runtime.unit, "TFT_Item_IonicSpark")) {
            for (auto& enemy : units) {
                if (enemy.unit.team != runtime.unit.team && is_alive(enemy) &&
                    distance_between(runtime.unit, enemy.unit) <= 2) {
                    enemy.mr_shred_until = config.max_duration;
                    enemy.mr_shred_percent = 0.30f;
                }
            }
        }
        if (has_item(runtime.unit, "TFT_Item_GargoyleStoneplate")) {
            int nearby_enemies = 0;
            for (const auto& enemy : units) {
                if (enemy.unit.team != runtime.unit.team &&
                    is_alive(enemy) && distance_between(runtime.unit, enemy.unit) <= 2)
                    ++nearby_enemies;
            }
            runtime.unit.armor += 10.0f * nearby_enemies;
            runtime.unit.magic_resist += 10.0f * nearby_enemies;
        }
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
        for (auto& runtime : units) {
            apply_delayed_effects(runtime, now);
            update_conditional_effects(runtime);
        }

        // Processa queimadura uma vez por segundo, independentemente da ordem
        // de ações da unidade que aplicou o efeito.
        for (auto& burning : units) {
            if (!is_alive(burning) || burning.burn_until <= now ||
                burning.burn_next_tick > now) continue;
            const float raw_burn = burning.unit.max_hp * burning.burn_percent / 100.0f;
            const float hp_loss = std::min(burning.unit.hp, raw_burn);
            burning.unit.hp -= hp_loss;
            burning.damage_taken += hp_loss;
            if (burning.burn_source_id >= 0) {
                const auto source_it = index_by_id.find(burning.burn_source_id);
                if (source_it != index_by_id.end())
                    units[source_it->second].damage_dealt += hp_loss;
            }
            if (config.record_damage) {
                DamageEvent burn_event;
                burn_event.timestamp = now;
                burn_event.source_unit_id = burning.burn_source_id;
                burn_event.target_unit_id = burning.unit.id;
                burn_event.damage_type = DamageType::TRUE_DAMAGE;
                burn_event.raw_damage = raw_burn;
                burn_event.final_damage = hp_loss;
                result.damage_events.push_back(burn_event);
            }
            burning.burn_next_tick += 1.0f;
            if (burning.unit.hp <= 0.0f && burning.unit.alive) {
                burning.unit.hp = 0.0f;
                burning.unit.alive = false;
                if (burning.burn_source_id >= 0) {
                    const auto source_it = index_by_id.find(burning.burn_source_id);
                    if (source_it != index_by_id.end()) ++units[source_it->second].kills;
                }
                if (config.record_events) {
                    DeathEvent death;
                    death.timestamp = now;
                    death.unit_id = burning.unit.id;
                    death.killer_unit_id = burning.burn_source_id;
                    result.death_events.push_back(death);
                }
            }
        }

        auto& actor = units[event.unit_index];
        if (!is_alive(actor) || (!actor.unit.can_attack && !actor.unit.can_cast)) {
            continue;
        }

        // Passivas temporizadas e gatilhos defensivos dos itens do Set 17.
        const float elapsed = std::max(0.0f, now - actor.last_status_tick);
        if (elapsed > 0.0f) {
            actor.unit.mana = std::min(actor.unit.max_mana,
                actor.unit.mana + actor.mana_regen_per_second *
                    elapsed * actor.mana_gain_multiplier);
            if (has_item(actor.unit, "TFT_Item_ArchangelsStaff") &&
                now - actor.last_archangel_tick >= 5.0f) {
                const int ticks = static_cast<int>((now - actor.last_archangel_tick) / 5.0f);
                actor.unit.ability_power += actor.unit.ability_power * 0.20f * ticks;
                actor.last_archangel_tick += 5.0f * ticks;
            }
            if (has_item(actor.unit, "TFT_Item_Quicksilver") &&
                now - actor.last_quicksilver_tick >= 1.0f) {
                const int ticks = static_cast<int>(now - actor.last_quicksilver_tick);
                actor.unit.attack_speed += 0.03f * ticks;
                actor.last_quicksilver_tick += static_cast<float>(ticks);
            }
            if (has_item(actor.unit, "TFT_Item_Redemption") &&
                now - actor.last_redemption_tick >= 1.0f) {
                const int ticks = static_cast<int>(now - actor.last_redemption_tick);
                const float missing = actor.unit.max_hp - actor.unit.hp;
                const float heal = apply_heal(actor,
                    std::min(missing * 0.02f * ticks, 250.0f * ticks), now);
                actor.healing_done += heal;
                actor.last_redemption_tick += static_cast<float>(ticks);
            }
            if (has_item(actor.unit, "TFT_Item_DragonsClaw") &&
                now - actor.last_dragons_claw_tick >= 2.0f) {
                const int ticks = static_cast<int>((now - actor.last_dragons_claw_tick) / 2.0f);
                const float heal = apply_heal(actor,
                    actor.unit.max_hp * 0.025f * ticks, now);
                actor.healing_done += heal;
                actor.last_dragons_claw_tick += 2.0f * ticks;
            }
            if (actor.crown_shield_triggered && actor.crown_shield_expires_at > 0.0f &&
                now >= actor.crown_shield_expires_at) {
                actor.unit.ability_power += 25.0f;
                actor.crown_shield_expires_at = 0.0f;
            }
            actor.last_status_tick = now;
        }
        if (has_item(actor.unit, "TFT_Item_PowerGauntlet")) {
            while (!actor.power_gauntlet_stack_times.empty() &&
                   now - actor.power_gauntlet_stack_times.front() >= 5.0f) {
                actor.power_gauntlet_stack_times.erase(
                    actor.power_gauntlet_stack_times.begin());
                actor.unit.damage_amplification = std::max(
                    0.0f, actor.unit.damage_amplification - 0.05f);
            }
            actor.power_gauntlet_stacks =
                static_cast<int>(actor.power_gauntlet_stack_times.size());
        }
        trigger_defensive_items(actor, now);
        if (actor.shield_expires_at > 0.0f && now >= actor.shield_expires_at) {
            actor.shield_hp = 0.0f;
            actor.shield_expires_at = 0.0f;
        }
        if (actor.guardian_angel_until > 0.0f && now >= actor.guardian_angel_until) {
            actor.unit.damage_reduction = actor.guardian_previous_damage_reduction;
            actor.guardian_angel_until = 0.0f;
        }


        // Guinsoo's and item cooldown clocks use elapsed combat time.
        for (const auto& item : actor.unit.items) {
            if (item.api_name == "TFT_Item_GuinsoosRageblade") {
                const int ticks = static_cast<int>(std::floor(now)) -
                                  static_cast<int>(std::floor(actor.last_guinsoo_tick));
                if (ticks > 0) {
                    actor.unit.attack_speed += actor.base_attack_speed * 0.07f * static_cast<float>(ticks);
                    actor.last_guinsoo_tick = now;
                }
            }
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
                        if (ability.damage_type == DamageType::PHYSICAL) {
                            const float armor = ability_target.armor_shred_until > now
                                ? ability_target.unit.armor * (1.0f - ability_target.armor_shred_percent)
                                : ability_target.unit.armor;
                            damage = mitigate_physical_damage(damage, armor);
                        } else if (ability.damage_type == DamageType::MAGIC) {
                            const float mr = ability_target.mr_shred_until > now
                                ? ability_target.unit.magic_resist * (1.0f - ability_target.mr_shred_percent)
                                : ability_target.unit.magic_resist;
                            damage = mitigate_physical_damage(damage, mr);
                        }
                        damage *= std::clamp(1.0f - ability_target.unit.damage_reduction, 0.0f, 1.0f);
                        damage = std::min(damage, ability_target.unit.hp + ability_target.shield_hp);
                        const float absorbed = std::min(ability_target.shield_hp, damage);
                        ability_target.shield_hp -= absorbed;
                        const float hp_damage = std::min(ability_target.unit.hp, damage - absorbed);
                        ability_target.unit.hp -= hp_damage;
                        ability_target.damage_taken += damage;
                        if (has_item(ability_target.unit, "TFT_Item_TitansResolve"))
                            add_titans_stack(ability_target);
                        trigger_defensive_items(ability_target, now);
                        actor.damage_dealt += damage;
                        ability_event.damage += damage;
                        if (has_item(actor.unit, "TFT_Item_MadredsBloodrazor") &&
                            ability_target.unit.role == UnitRole::TANK) {
                            const float bonus = damage * 0.15f;
                            const float extra_hp = std::min(ability_target.unit.hp, bonus);
                            ability_target.unit.hp -= extra_hp;
                            ability_target.damage_taken += extra_hp;
                            actor.damage_dealt += extra_hp;
                            ability_event.damage += extra_hp;
                        }
                        if (has_item(actor.unit, "TFT_Item_LastWhisper")) {
                            ability_target.armor_shred_until = now + 3.0f;
                            ability_target.armor_shred_percent = 0.30f;
                        }
                        if (has_item(actor.unit, "TFT_Item_StatikkShiv")) {
                            ability_target.mr_shred_until = now + 5.0f;
                            ability_target.mr_shred_percent = 0.30f;
                        }
                        if (has_item(actor.unit, "TFT_Item_Morellonomicon") ||
                            has_item(actor.unit, "TFT_Item_RedBuff") ||
                            has_item(actor.unit, "TFT_Item_RapidFireCannon")) {
                            ability_target.burn_until = std::max(ability_target.burn_until,
                                now + (has_item(actor.unit, "TFT_Item_Morellonomicon") ? 10.0f : 5.0f));
                            ability_target.burn_percent = std::max(ability_target.burn_percent, 1.0f);
                            ability_target.burn_source_id = actor.unit.id;
                            if (ability_target.burn_next_tick < now)
                                ability_target.burn_next_tick = now + 1.0f;
                            ability_target.grievous_until = std::max(ability_target.grievous_until,
                                now + (has_item(actor.unit, "TFT_Item_Morellonomicon") ? 10.0f : 5.0f));
                        }
                        if (has_item(actor.unit, "TFT_Item_HextechGunblade")) {
                            std::size_t ally = units.size();
                            float lowest = std::numeric_limits<float>::infinity();
                            for (std::size_t i = 0; i < units.size(); ++i) {
                                if (!is_alive(units[i]) || units[i].unit.team != actor.unit.team) continue;
                                const float ratio = units[i].unit.hp / units[i].unit.max_hp;
                                if (ratio < lowest) { lowest = ratio; ally = i; }
                            }
                            if (ally < units.size()) {
                                const float heal = apply_heal(units[ally], damage * 0.20f, now);
                                units[ally].healing_done += heal;
                            }
                        }
                        if (actor.unit.omnivamp > 0.0f && damage > 0.0f) {
                            const float heal = apply_heal(actor,
                                damage * actor.unit.omnivamp, now);
                            actor.healing_done += heal;
                        }

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
                        const float actual = apply_heal(ability_target, healing, now);
                        actor.healing_done += actual;
                        ability_event.healing += actual;
                    }
                    if (ability.has_shield) {
                        const float shield = std::max(0.0f, ability.shield_amount) +
                            std::max(0.0f, ability.ability_power_ratio) *
                                actor.unit.ability_power;
                        ability_target.shield_hp += shield;
                        ability_event.shield += shield;
                        for (auto& ally : units) {
                            if (ally.unit.team == actor.unit.team &&
                                has_item(ally.unit, "TFT17_Item_ShieldTankEmblemItem"))
                                ally.unit.ability_power += 2.0f;
                        }
                    }

                    if (ability_target.unit.hp <= 0.0f && ability_target.unit.alive) {
                        ability_target.unit.hp = 0.0f;
                        ability_target.unit.alive = false;
                        ++actor.kills;
                        grant_on_kill_effect_charges(actor);
                        const float generic_kill_heal = effect_kill_healing(actor.unit);
                        if (generic_kill_heal > 0.0f) {
                            const float actual_heal = apply_heal(actor, generic_kill_heal, now);
                            actor.healing_done += actual_heal;
                        }
                        if (has_item(actor.unit, "TFT17_Item_ASTraitEmblemItem"))
                            actor.challenger_attacks_remaining = 3;
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
                // Centelha Iônica pune conjurações inimigas próximas, com recarga.
                for (auto& holder : units) {
                    if (!is_alive(holder) || holder.unit.team == actor.unit.team ||
                        !has_item(holder.unit, "TFT_Item_IonicSpark") ||
                        now - holder.last_ionic_proc < 2.0f ||
                        distance_between(holder.unit, actor.unit) > 2) continue;
                    holder.last_ionic_proc = now;
                    const float raw = ability.mana_cost * 1.50f;
                    const float mitigated = mitigate_physical_damage(raw, actor.unit.magic_resist);
                    const float final_damage = mitigated *
                        std::clamp(1.0f - actor.unit.damage_reduction, 0.0f, 1.0f);
                    const float absorbed = std::min(actor.shield_hp, final_damage);
                    actor.shield_hp -= absorbed;
                    const float hp_loss = std::min(actor.unit.hp, final_damage - absorbed);
                    actor.unit.hp -= hp_loss;
                    actor.damage_taken += final_damage;
                    holder.damage_dealt += final_damage;
                    if (config.record_damage) {
                        DamageEvent spark;
                        spark.timestamp = now;
                        spark.source_unit_id = holder.unit.id;
                        spark.target_unit_id = actor.unit.id;
                        spark.damage_type = DamageType::MAGIC;
                        spark.raw_damage = raw;
                        spark.final_damage = final_damage;
                        result.damage_events.push_back(spark);
                    }
                    if (actor.unit.hp <= 0.0f) {
                        trigger_defensive_items(actor, now);
                        if (actor.unit.hp <= 0.0f) {
                            actor.unit.alive = false;
                            if (config.record_events) {
                                DeathEvent death;
                                death.timestamp = now;
                                death.unit_id = actor.unit.id;
                                death.killer_unit_id = holder.unit.id;
                                result.death_events.push_back(death);
                            }
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
            raw_damage += effect_attack_bonus(actor.unit, DamageType::PHYSICAL);

            raw_damage *= std::max(
                0.0f, 1.0f + actor.unit.damage_amplification);
            if (has_item(actor.unit, "TFT_Item_MadredsBloodrazor") &&
                target.unit.role == UnitRole::TANK)
                raw_damage *= 1.15f;

            const float effective_armor = target.armor_shred_until > now
                ? target.unit.armor * (1.0f - target.armor_shred_percent)
                : target.unit.armor;
            float damage = mitigate_physical_damage(raw_damage, effective_armor);

            damage *= std::clamp(
                1.0f - target.unit.damage_reduction, 0.0f, 1.0f);
            if (has_item(target.unit, "TFT_Item_BrambleVest"))
                damage *= 0.95f;

            damage = std::min(damage, target.unit.hp + target.shield_hp);

            const float absorbed = std::min(target.shield_hp, damage);
            target.shield_hp -= absorbed;
            const float hp_damage = std::min(target.unit.hp, damage - absorbed);
            target.unit.hp -= hp_damage;
            target.damage_taken += damage;
            if (has_item(target.unit, "TFT_Item_TitansResolve"))
                add_titans_stack(target);
            trigger_defensive_items(target, now);
            actor.damage_dealt += damage;
            if (actor.unit.omnivamp > 0.0f && damage > 0.0f) {
                const float heal = apply_heal(actor,
                    damage * actor.unit.omnivamp, now);
                actor.healing_done += heal;
            }
            ++actor.attacks;
            const float generic_charged_heal = apply_charged_attack_healing(actor, now);
            actor.healing_done += generic_charged_heal;
            if (actor.challenger_attacks_remaining > 0) {
                const float heal = apply_heal(actor,
                    actor.unit.max_hp * 0.05f, now);
                actor.healing_done += heal;
                --actor.challenger_attacks_remaining;
            }
            // Generic data-driven bonus damage supports physical, magic and true damage.
            for (const DamageType bonus_type : {DamageType::MAGIC, DamageType::TRUE_DAMAGE}) {
                const float raw_bonus = effect_attack_bonus(actor.unit, bonus_type);
                if (raw_bonus <= 0.0f) continue;
                const float mitigated = bonus_type == DamageType::MAGIC
                    ? mitigate_physical_damage(raw_bonus, target.unit.magic_resist)
                    : raw_bonus;
                const float bonus = std::min(mitigated, target.unit.hp + target.shield_hp);
                const float absorbed_bonus = std::min(target.shield_hp, bonus);
                target.shield_hp -= absorbed_bonus;
                const float hp_bonus = std::min(target.unit.hp, bonus - absorbed_bonus);
                target.unit.hp -= hp_bonus;
                target.damage_taken += bonus;
                trigger_defensive_items(target, now);
                actor.damage_dealt += bonus;
                if (config.record_damage) {
                    DamageEvent bonus_event;
                    bonus_event.timestamp = now;
                    bonus_event.source_unit_id = actor.unit.id;
                    bonus_event.target_unit_id = target.unit.id;
                    bonus_event.damage_type = bonus_type;
                    bonus_event.raw_damage = raw_bonus;
                    bonus_event.final_damage = bonus;
                    result.damage_events.push_back(bonus_event);
                }
            }
            actor.unit.mana = std::min(actor.unit.max_mana,
                actor.unit.mana + 10.0f * actor.mana_gain_multiplier);

            // Shojin e Leviathan: mana adicional por ataque acertado.
            for (const auto& item : actor.unit.items) {
                if (item.api_name == "TFT_Item_SpearOfShojin")
                    actor.unit.mana = std::min(actor.unit.max_mana,
                        actor.unit.mana + 5.0f * actor.mana_gain_multiplier);
                else if (item.api_name == "TFT_Item_Leviathan") {
                    const float mana_on_hit = critical ? 4.0f : 2.0f;
                    actor.unit.mana = std::min(actor.unit.max_mana,
                        actor.unit.mana + mana_on_hit * actor.mana_gain_multiplier);
                }
                else if (item.api_name == "TFT_Item_TitansResolve")
                    add_titans_stack(actor);
                else if (item.api_name == "TFT_Item_RunaansHurricane") {
                    if (actor.runaan_stacks < 15) {
                        ++actor.runaan_stacks;
                        actor.unit.attack_damage += actor.runaans_base_ad * 0.035f;
                        if (actor.runaan_stacks == 15)
                            actor.unit.attack_speed += actor.base_attack_speed * 0.15f;
                    }
                }
                else if (item.api_name == "TFT_Item_PowerGauntlet" && critical) {
                    if (actor.power_gauntlet_stacks < 4) {
                        actor.power_gauntlet_stack_times.push_back(now);
                        ++actor.power_gauntlet_stacks;
                        actor.unit.damage_amplification += 0.05f;
                    }
                }
            }

            // Efeitos aplicados ao alvo por ataques: fatiamento, queimadura e ferimentos.
            if (has_item(actor.unit, "TFT_Item_LastWhisper")) {
                target.armor_shred_until = now + 3.0f;
                target.armor_shred_percent = 0.30f;
            }
            if (has_item(actor.unit, "TFT_Item_StatikkShiv")) {
                target.mr_shred_until = now + 5.0f;
                target.mr_shred_percent = 0.30f;
            }
            if (has_item(actor.unit, "TFT_Item_Morellonomicon") ||
                has_item(actor.unit, "TFT_Item_RedBuff") ||
                has_item(actor.unit, "TFT_Item_RapidFireCannon")) {
                target.burn_until = std::max(target.burn_until, now +
                    (has_item(actor.unit, "TFT_Item_Morellonomicon") ? 10.0f : 5.0f));
                target.burn_percent = std::max(target.burn_percent, 1.0f);
                target.burn_source_id = actor.unit.id;
                if (target.burn_next_tick < now) target.burn_next_tick = now + 1.0f;
                target.grievous_until = std::max(target.grievous_until,
                    now + (has_item(actor.unit, "TFT_Item_Morellonomicon") ? 10.0f : 5.0f));
            }
            if (has_item(actor.unit, "TFT_Item_HextechGunblade") && damage > 0.0f) {
                std::size_t ally = units.size();
                float lowest = std::numeric_limits<float>::infinity();
                for (std::size_t i = 0; i < units.size(); ++i) {
                    if (!is_alive(units[i]) || units[i].unit.team != actor.unit.team) continue;
                    const float ratio = units[i].unit.hp / units[i].unit.max_hp;
                    if (ratio < lowest) { lowest = ratio; ally = i; }
                }
                if (ally < units.size()) {
                    const float heal = apply_heal(units[ally], damage * 0.20f, now);
                    units[ally].healing_done += heal;
                }
            }

            // Colete Espinhoso: dano mágico em área com recarga de 2 segundos.
            for (const auto& item : target.unit.items) {
                if (item.api_name == "TFT_Item_BrambleVest" &&
                    now - target.last_bramble_proc >= 2.0f) {
                    target.last_bramble_proc = now;
                    for (auto& enemy : units) {
                        if (!is_alive(enemy) || enemy.unit.team == target.unit.team ||
                            distance_between(enemy.unit, target.unit) > 2) continue;
                        const float reflected = mitigate_physical_damage(100.0f,
                            enemy.unit.magic_resist);
                        const float absorbed_reflect = std::min(enemy.shield_hp, reflected);
                        enemy.shield_hp -= absorbed_reflect;
                        const float hp_loss = std::min(enemy.unit.hp, reflected - absorbed_reflect);
                        enemy.unit.hp -= hp_loss;
                        enemy.damage_taken += reflected;
                        target.damage_dealt += reflected;
                        if (config.record_damage) {
                            DamageEvent reflected_event;
                            reflected_event.timestamp = now;
                            reflected_event.source_unit_id = target.unit.id;
                            reflected_event.target_unit_id = enemy.unit.id;
                            reflected_event.damage_type = DamageType::MAGIC;
                            reflected_event.raw_damage = 100.0f;
                            reflected_event.final_damage = reflected;
                            reflected_event.ability_damage = false;
                            result.damage_events.push_back(reflected_event);
                        }
                        if (enemy.unit.hp <= 0.0f && enemy.unit.alive) {
                            enemy.unit.hp = 0.0f;
                            enemy.unit.alive = false;
                            ++target.kills;
                            if (config.record_events) {
                                DeathEvent death;
                                death.timestamp = now;
                                death.unit_id = enemy.unit.id;
                                death.killer_unit_id = target.unit.id;
                                result.death_events.push_back(death);
                            }
                        }
                    }
                    break;
                }
            }

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
                grant_on_kill_effect_charges(actor);
                const float generic_kill_heal = effect_kill_healing(actor.unit);
                if (generic_kill_heal > 0.0f) {
                    const float actual_heal = apply_heal(actor, generic_kill_heal, now);
                    actor.healing_done += actual_heal;
                }
                if (has_item(actor.unit, "TFT17_Item_ASTraitEmblemItem"))
                    actor.challenger_attacks_remaining = 3;

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