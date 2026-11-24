
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

struct GenericEffectDescriptor {
    const CombatEffectDefinition* effect = nullptr;
    std::string prefix;
    std::string delayed_key;
    std::string conditional_key;
    std::string periodic_key;
};

struct RuntimeUnit {
    CombatUnit unit;
    float initial_hp = 0.0f;
    // Immutable descriptors point into unit.items/unit.traits, whose effect
    // vectors remain stable for the lifetime of this combat simulation.
    std::vector<GenericEffectDescriptor> generic_effect_descriptors;
    std::vector<std::size_t> delayed_effect_indices;
    std::vector<std::size_t> conditional_effect_indices;
    std::vector<std::size_t> periodic_effect_indices;
    float damage_dealt = 0.0f;
    float damage_taken = 0.0f;
    float healing_done = 0.0f;
    float shield_hp = 0.0f;
    int attacks = 0;
    int ability_casts = 0;
    int kills = 0;
    float last_redbuff_tick = 0.0f;
    float shield_expires_at = 0.0f;
    float burn_until = 0.0f;
    float burn_next_tick = 0.0f;
    float burn_percent = 0.0f;
    int burn_source_id = -1;
    float grievous_until = 0.0f;
    float armor_shred_until = 0.0f;
    float armor_shred_percent = 0.0f;
    float mr_shred_until = 0.0f;
    float mr_shred_percent = 0.0f;
    bool resist_emblem_triggered = false;
    bool assassin_omnivamp_active = false;
    float last_status_tick = 0.0f;
    float mana_regen_per_second = 0.0f;
    float mana_gain_multiplier = 1.0f;
    float base_attack_damage = 0.0f;
    float base_attack_speed = 1.0f;
    std::unordered_map<std::string, std::vector<float>> generic_effect_stack_expiry;
    std::unordered_map<std::string, float> generic_effect_applied_amounts;
    std::unordered_map<std::string, float> generic_effect_previous_values;
    std::unordered_map<std::string, int> generic_effect_charges;
    std::unordered_set<std::string> generic_effects_applied;
    std::unordered_set<std::string> generic_effects_active;
    std::unordered_set<std::string> generic_effects_triggered;
    std::unordered_map<std::string, float> generic_effect_expiry;
    std::unordered_map<std::string, float> generic_effect_next_tick;
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

bool effect_condition_matches(
    const CombatUnit& unit, const CombatEffectDefinition& effect
);

float apply_heal(RuntimeUnit& target, float amount, float now) {
    if (target.grievous_until > now) amount *= 0.67f;
    const float actual = std::min(std::max(0.0f, amount),
        std::max(0.0f, target.unit.max_hp - target.unit.hp));
    target.unit.hp += actual;
    return actual;
}

void apply_damage_healing_effects(
    RuntimeUnit& source, std::vector<RuntimeUnit>& units, float damage, float now
) {
    if (!std::isfinite(damage) || damage <= 0.0f) return;
    const auto apply = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.trigger != "on_damage_dealt" ||
                effect.operation != "heal_damage_pct_lowest_ally" ||
                effect.target != "lowest_health_ally" ||
                !effect_condition_matches(source.unit, effect)) continue;

            std::size_t ally_index = units.size();
            float lowest_health_ratio = std::numeric_limits<float>::infinity();
            for (std::size_t i = 0; i < units.size(); ++i) {
                if (!is_alive(units[i]) ||
                    units[i].unit.team != source.unit.team) continue;
                const float ratio = units[i].unit.hp / units[i].unit.max_hp;
                if (ratio < lowest_health_ratio) {
                    lowest_health_ratio = ratio;
                    ally_index = i;
                }
            }
            if (ally_index >= units.size()) continue;
            const float healing = apply_heal(
                units[ally_index], damage * effect.value, now);
            units[ally_index].healing_done += healing;
        }
    };
    for (const auto& item : source.unit.items) apply(item.effects);
    for (const auto& trait : source.unit.traits)
        if (trait.active || trait.active_count > 0) apply(trait.effects);
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
    if (effect.condition == "trait_count_at_least") {
        if (effect.condition_trait.empty() || effect.min_trait_count <= 0) return false;
        const auto found = std::find_if(unit.traits.begin(), unit.traits.end(),
            [&](const CombatTrait& trait) {
                return trait.api_name == effect.condition_trait &&
                    (trait.active || trait.active_count > 0);
            });
        return found != unit.traits.end() && found->active_count >= effect.min_trait_count;
    }
    if (effect.condition == "role_tank") return unit.role == UnitRole::TANK;
    if (effect.condition == "role_fighter") return unit.role == UnitRole::FIGHTER;
    if (effect.condition == "role_assassin") return unit.role == UnitRole::ASSASSIN;
    if (effect.condition == "role_other")
        return unit.role != UnitRole::TANK &&
               unit.role != UnitRole::FIGHTER &&
               unit.role != UnitRole::ASSASSIN;
    if (effect.condition == "target_role_tank") return true;
    return false;
}

float apply_effect_stat(CombatUnit& unit, const CombatEffectDefinition& effect) {
    float amount = effect.value;
    if (effect.percent_of_stat) {
        if (effect.stat == "attack_damage") amount *= unit.attack_damage;
        else if (effect.stat == "attack_speed") amount *= unit.attack_speed;
        else if (effect.stat == "ability_power") amount *= unit.ability_power;
        else if (effect.stat == "max_hp") amount *= unit.max_hp;
        else if (effect.stat == "armor") amount *= unit.armor;
        else if (effect.stat == "magic_resist") amount *= unit.magic_resist;
    }
    float before = 0.0f;
    if (effect.stat == "attack_damage") {
        before = unit.attack_damage;
        unit.attack_damage += amount;
        return unit.attack_damage - before;
    }
    if (effect.stat == "critical_strike_chance") {
        before = unit.critical_strike_chance;
        unit.critical_strike_chance = std::clamp(
            unit.critical_strike_chance + amount, 0.0f, 1.0f);
        return unit.critical_strike_chance - before;
    }
    if (effect.stat == "attack_speed") {
        before = unit.attack_speed;
        unit.attack_speed += amount;
        return amount;
    }
    if (effect.stat == "ability_power") {
        unit.ability_power += amount;
        return amount;
    }
    if (effect.stat == "armor") {
        unit.armor += amount;
        return amount;
    }
    if (effect.stat == "magic_resist") {
        unit.magic_resist += amount;
        return amount;
    }
    if (effect.stat == "omnivamp") {
        before = unit.omnivamp;
        unit.omnivamp = std::clamp(unit.omnivamp + amount, 0.0f, 1.0f);
        return unit.omnivamp - before;
    }
    if (effect.stat == "damage_amplification") {
        unit.damage_amplification += amount;
        return amount;
    }
    if (effect.stat == "damage_reduction") {
        before = unit.damage_reduction;
        unit.damage_reduction = std::clamp(unit.damage_reduction + amount, 0.0f, 1.0f);
        return unit.damage_reduction - before;
    }
    if (effect.stat == "max_hp") {
        unit.max_hp += amount;
        unit.hp += amount;
        return amount;
    }
    return 0.0f;
}

template <typename Callback>
void visit_unit_effects(const CombatUnit& unit, Callback callback) {
    for (const auto& item : unit.items)
        for (const auto& effect : item.effects) callback(effect);
    for (const auto& trait : unit.traits) {
        if (trait.active || trait.active_count > 0)
            for (const auto& effect : trait.effects) callback(effect);
    }
}

void apply_start_combat_effects(RuntimeUnit& runtime) {
    visit_unit_effects(runtime.unit, [&](const CombatEffectDefinition& effect) {
        if (effect.trigger != "combat_start" ||
            !effect_condition_matches(runtime.unit, effect)) return;
        if (effect.operation == "add_stat" &&
            (effect.target.empty() || effect.target == "self")) {
            apply_effect_stat(runtime.unit, effect);
        } else if (effect.operation == "grant_shield" && effect.target == "self") {
            runtime.shield_hp += runtime.unit.max_hp * effect.value;
            runtime.shield_expires_at = std::max(
                runtime.shield_expires_at, effect.duration);
        } else if (effect.operation == "restore_mana" && effect.target == "self") {
            runtime.unit.mana = std::min(runtime.unit.max_mana,
                runtime.unit.mana + effect.value * runtime.mana_gain_multiplier);
        }
    });
}

void apply_start_combat_team_effects(std::vector<RuntimeUnit>& units) {
    struct PendingTeamEffect {
        std::size_t recipient_index;
        CombatEffectDefinition effect;
        bool attach_as_runtime_effect;
    };
    std::vector<PendingTeamEffect> pending;

    // Collect before mutating recipient trait vectors: a source can also be a
    // recipient, so applying effects while iterating those vectors would
    // invalidate iterators and could recursively re-apply an aura.
    for (const auto& source : units) {
        const auto collect = [&](const std::vector<CombatEffectDefinition>& effects) {
            for (const auto& effect : effects) {
                const bool role_condition =
                    effect.condition == "role_tank" ||
                    effect.condition == "role_fighter" ||
                    effect.condition == "role_assassin" ||
                    effect.condition == "role_other";
                // Trait/count conditions describe the aura source; role
                // conditions describe which allied recipients qualify.
                if (!role_condition && !effect_condition_matches(source.unit, effect)) continue;
                const bool team_stat = effect.trigger == "combat_start" &&
                    effect.operation == "add_stat" &&
                    (effect.target == "allies" ||
                     effect.target == "allies_same_row_within_1");
                const bool team_attack_effect = effect.target == "allies" &&
                    effect.trigger == "on_attack" &&
                    effect.operation == "bonus_damage";
                const bool team_mana_regen = effect.target == "allies" &&
                    effect.trigger == "combat_start" &&
                    effect.operation == "mana_regen";
                if (!team_stat && !team_attack_effect && !team_mana_regen) continue;

                CombatEffectDefinition source_effect = effect;
                if (source_effect.scale_by_active_trait_count) {
                    const auto trait_count = std::find_if(
                        source.unit.traits.begin(), source.unit.traits.end(),
                        [&](const CombatTrait& trait) {
                            return trait.api_name == source_effect.condition_trait &&
                                (trait.active || trait.active_count > 0);
                        });
                    if (trait_count == source.unit.traits.end() ||
                        trait_count->active_count <= 0) continue;
                    source_effect.value /= static_cast<float>(trait_count->active_count);
                }

                for (std::size_t i = 0; i < units.size(); ++i) {
                    const auto& recipient = units[i];
                    if (recipient.unit.team != source.unit.team) continue;
                    // The source already evaluates its own on_attack effect from
                    // its item/trait. Do not attach a second copy of that aura
                    // to the source itself; recipients other than the source need
                    // the runtime copy so they inherit the team bonus.
                    if (team_attack_effect &&
                        recipient.unit.id == source.unit.id) continue;
                    if (role_condition && !effect_condition_matches(recipient.unit, effect))
                        continue;
                    if (effect.target == "allies_same_row_within_1" &&
                        (recipient.unit.position.y != source.unit.position.y ||
                         std::abs(recipient.unit.position.x - source.unit.position.x) > 1))
                        continue;
                    if (team_stat) pending.push_back({i, source_effect, false});
                    else pending.push_back({i, source_effect, true});
                }
            }
        };
        for (const auto& item : source.unit.items) collect(item.effects);
        for (const auto& trait : source.unit.traits) {
            if (trait.active || trait.active_count > 0) collect(trait.effects);
        }
    }

    for (const auto& pending_effect : pending) {
        auto& recipient = units[pending_effect.recipient_index];
        if (!is_alive(recipient)) continue;
        if (pending_effect.attach_as_runtime_effect) {
            CombatEffectDefinition effect = pending_effect.effect;
            effect.target = "self";
            effect.condition.clear();
            effect.condition_trait.clear();
            CombatTrait runtime_effect;
            runtime_effect.api_name = "generic_team_aura";
            runtime_effect.name = "generic_team_aura";
            runtime_effect.active = true;
            runtime_effect.active_count = 1;
            runtime_effect.effects.push_back(std::move(effect));
            recipient.unit.traits.push_back(std::move(runtime_effect));
        } else {
            apply_effect_stat(recipient.unit, pending_effect.effect);
        }
    }
}

float effect_attack_bonus(const CombatUnit& unit, DamageType damage_type) {
    float bonus = 0.0f;
    auto accumulate = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.trigger == "on_attack" && effect.operation == "bonus_damage" &&
                effect.damage_type == damage_type &&
                effect_condition_matches(unit, effect))
                if (effect.percent_of_max_health) {
                    bonus += unit.max_hp * effect.value;
                } else if (effect.percent_of_stat) {
                    float base_stat = 0.0f;
                    if (effect.stat == "attack_damage") base_stat = unit.attack_damage;
                    else if (effect.stat == "attack_speed") base_stat = unit.attack_speed;
                    else if (effect.stat == "ability_power") base_stat = unit.ability_power;
                    else if (effect.stat == "max_hp") base_stat = unit.max_hp;
                    else if (effect.stat == "armor") base_stat = unit.armor;
                    else if (effect.stat == "magic_resist") base_stat = unit.magic_resist;
                    bonus += base_stat * effect.value;
                } else {
                    bonus += effect.value;
                }
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
                (effect.target.empty() || effect.target == "self") &&
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

float effect_mana_on_attack(const CombatUnit& unit, bool critical) {
    float amount = 0.0f;
    auto accumulate = [&](const std::vector<CombatEffectDefinition>& effects) {
        for (const auto& effect : effects) {
            if (effect.trigger != "on_attack" ||
                effect.operation != "mana_on_attack" ||
                !effect_condition_matches(unit, effect)) continue;
            amount += critical && effect.critical_value > 0.0f
                ? effect.critical_value : effect.value;
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

void prepare_generic_effect_descriptors(RuntimeUnit& runtime) {
    auto& unit = runtime.unit;
    std::size_t total = 0;
    for (const auto& item : unit.items) total += item.effects.size();
    for (const auto& trait : unit.traits)
        if (trait.active || trait.active_count > 0) total += trait.effects.size();

    runtime.generic_effect_descriptors.reserve(total);
    runtime.delayed_effect_indices.reserve(total);
    runtime.conditional_effect_indices.reserve(total);
    runtime.periodic_effect_indices.reserve(total);

    const auto append = [&](const CombatEffectDefinition& effect, std::string prefix) {
        GenericEffectDescriptor descriptor;
        descriptor.effect = &effect;
        descriptor.prefix = std::move(prefix);
        if (effect.trigger == "after_delay" && effect.operation == "add_stat") {
            descriptor.delayed_key = descriptor.prefix + "delayed:" + effect.stat + ":" +
                std::to_string(effect.delay) + ":" + std::to_string(effect.value);
        }
        if ((effect.trigger == "while_hp_below" ||
             effect.trigger == "while_hp_above") &&
            (effect.operation == "add_stat" || effect.operation == "grant_shield" ||
             effect.operation == "restore_mana" || effect.operation == "revive") &&
            effect.health_threshold > 0.0f) {
            descriptor.conditional_key = descriptor.prefix + "conditional:" +
                effect.operation + ":" + effect.trigger + ":" + effect.stat + ":" +
                std::to_string(effect.health_threshold) + ":" +
                std::to_string(effect.value) + ":" + std::to_string(effect.duration);
        }
        if (effect.trigger == "periodic" &&
            (effect.operation == "heal_max_hp_pct" ||
             effect.operation == "heal_missing_hp_pct" || effect.operation == "add_stat" ||
             effect.operation == "apply_burn" || effect.operation == "apply_wound") &&
            std::isfinite(effect.interval) && effect.interval > 0.0f) {
            descriptor.periodic_key = descriptor.prefix + "periodic:" +
                effect.operation + ":" + effect.stat + ":" + effect.condition + ":" +
                std::to_string(effect.interval) + ":" + std::to_string(effect.value) +
                ":" + std::to_string(effect.max_amount) + ":" +
                std::to_string(effect.duration) + ":" + std::to_string(effect.radius);
        }
        const std::size_t index = runtime.generic_effect_descriptors.size();
        runtime.generic_effect_descriptors.push_back(std::move(descriptor));
        const auto& stored = runtime.generic_effect_descriptors.back();
        if (!stored.delayed_key.empty()) runtime.delayed_effect_indices.push_back(index);
        if (!stored.conditional_key.empty()) runtime.conditional_effect_indices.push_back(index);
        if (!stored.periodic_key.empty()) runtime.periodic_effect_indices.push_back(index);
    };

    for (std::size_t item_index = 0; item_index < unit.items.size(); ++item_index) {
        const auto& item = unit.items[item_index];
        const std::string prefix = "item:" + item.api_name + ":" +
            std::to_string(item_index) + ":";
        for (const auto& effect : item.effects) append(effect, prefix);
    }
    for (std::size_t trait_index = 0; trait_index < unit.traits.size(); ++trait_index) {
        const auto& trait = unit.traits[trait_index];
        if (!trait.active && trait.active_count <= 0) continue;
        const std::string prefix = "trait:" + trait.api_name + ":" +
            std::to_string(trait_index) + ":";
        for (const auto& effect : trait.effects) append(effect, prefix);
    }
}

template <typename Callback>
void visit_generic_effects(RuntimeUnit& runtime, Callback callback) {
    for (const auto& descriptor : runtime.generic_effect_descriptors)
        callback(*descriptor.effect, descriptor.prefix);
}

void grant_on_kill_effect_charges(RuntimeUnit& actor) {
    visit_generic_effects(actor, [&](const CombatEffectDefinition& effect,
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
    visit_generic_effects(actor, [&](const CombatEffectDefinition& effect,
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
    for (const std::size_t index : runtime.delayed_effect_indices) {
        const auto& descriptor = runtime.generic_effect_descriptors[index];
        const auto& effect = *descriptor.effect;
        if (now < effect.delay || !effect_condition_matches(runtime.unit, effect)) continue;
        if (runtime.generic_effects_applied.insert(descriptor.delayed_key).second)
            apply_effect_stat(runtime.unit, effect);
    }
}

void apply_burn_status(RuntimeUnit& source, RuntimeUnit& target,
                        const CombatEffectDefinition& effect, float now) {
    target.burn_until = std::max(target.burn_until, now + effect.duration);
    target.burn_percent = std::max(target.burn_percent, effect.value * 100.0f);
    target.burn_source_id = source.unit.id;
    if (target.burn_next_tick < now + 1e-5f)
        target.burn_next_tick = now + 1.0f;
}

void apply_wound_status(RuntimeUnit& target,
                        const CombatEffectDefinition& effect, float now) {
    target.grievous_until = std::max(target.grievous_until, now + effect.duration);
}

void apply_shred_status(RuntimeUnit& target,
                        const CombatEffectDefinition& effect, float now) {
    if (effect.stat == "armor") {
        target.armor_shred_until = std::max(target.armor_shred_until, now + effect.duration);
        target.armor_shred_percent = std::max(target.armor_shred_percent, effect.value);
    } else if (effect.stat == "magic_resist") {
        target.mr_shred_until = std::max(target.mr_shred_until, now + effect.duration);
        target.mr_shred_percent = std::max(target.mr_shred_percent, effect.value);
    }
}

void apply_start_combat_item_effects(std::vector<RuntimeUnit>& units,
                                      float max_duration) {
    for (auto& source : units) {
        visit_unit_effects(source.unit, [&](const CombatEffectDefinition& effect) {
            if (effect.trigger != "combat_start" ||
                !effect_condition_matches(source.unit, effect)) return;
            if (effect.operation == "add_stat_per_nearby_enemy" &&
                effect.target == "self") {
                int nearby = 0;
                for (const auto& enemy : units) {
                    if (enemy.unit.team == source.unit.team || !is_alive(enemy)) continue;
                    if (distance_between(source.unit, enemy.unit) <=
                        static_cast<int>(std::ceil(effect.radius))) ++nearby;
                }
                if (nearby > 0) {
                    CombatEffectDefinition scaled = effect;
                    scaled.value *= static_cast<float>(nearby);
                    apply_effect_stat(source.unit, scaled);
                }
            } else if (effect.operation == "apply_shred" &&
                       effect.target == "enemies_within_radius") {
                CombatEffectDefinition bounded = effect;
                bounded.duration = std::min(effect.duration, max_duration);
                for (auto& enemy : units) {
                    if (enemy.unit.team == source.unit.team || !is_alive(enemy)) continue;
                    if (distance_between(source.unit, enemy.unit) >
                        static_cast<int>(std::ceil(effect.radius))) continue;
                    apply_shred_status(enemy, bounded, 0.0f);
                }
            }
        });
    }
}

void apply_periodic_effects(RuntimeUnit& runtime, float now,
                            std::vector<RuntimeUnit>& units) {
    for (const std::size_t index : runtime.periodic_effect_indices) {
        const auto& descriptor = runtime.generic_effect_descriptors[index];
        const auto& effect = *descriptor.effect;
        if (!effect_condition_matches(runtime.unit, effect)) continue;
        auto [next_tick, inserted] = runtime.generic_effect_next_tick.emplace(
            descriptor.periodic_key, effect.interval);
        (void)inserted;
        if (now + 1e-5f < next_tick->second) continue;
        const int ticks = static_cast<int>(
            std::floor((now - next_tick->second) / effect.interval)) + 1;
        if (ticks <= 0) continue;
        if (effect.operation == "heal_max_hp_pct" && effect.target == "self") {
            const float requested = runtime.unit.max_hp * effect.value *
                static_cast<float>(ticks);
            runtime.healing_done += apply_heal(runtime, requested, now);
        } else if (effect.operation == "heal_missing_hp_pct" &&
                   effect.target == "self") {
            for (int tick = 0; tick < ticks; ++tick) {
                const float missing = std::max(0.0f,
                    runtime.unit.max_hp - runtime.unit.hp);
                float requested = missing * effect.value;
                if (effect.max_amount > 0.0f)
                    requested = std::min(requested, effect.max_amount);
                runtime.healing_done += apply_heal(runtime, requested, now);
            }
        } else if (effect.operation == "add_stat" && effect.target == "self") {
            CombatEffectDefinition periodic_effect = effect;
            if (periodic_effect.scale_by_base_stat) {
                float base_stat = 0.0f;
                if (periodic_effect.stat == "attack_speed")
                    base_stat = runtime.base_attack_speed;
                if (!std::isfinite(base_stat) || base_stat <= 0.0f) continue;
                periodic_effect.value = base_stat * periodic_effect.value;
                periodic_effect.percent_of_stat = false;
                periodic_effect.scale_by_base_stat = false;
            }
            periodic_effect.value *= static_cast<float>(ticks);
            apply_effect_stat(runtime.unit, periodic_effect);
        } else if ((effect.operation == "apply_burn" ||
                    effect.operation == "apply_wound") &&
                   effect.target == "nearest_enemy_within_radius") {
            for (int tick = 0; tick < ticks; ++tick) {
                std::size_t nearest = units.size();
                int nearest_distance = std::numeric_limits<int>::max();
                for (std::size_t candidate = 0; candidate < units.size(); ++candidate) {
                    if (!is_alive(units[candidate]) ||
                        units[candidate].unit.team == runtime.unit.team) continue;
                    const int distance = distance_between(runtime.unit, units[candidate].unit);
                    if (distance > static_cast<int>(std::ceil(effect.radius))) continue;
                    if (distance < nearest_distance ||
                        (distance == nearest_distance && nearest < units.size() &&
                         units[candidate].unit.id < units[nearest].unit.id)) {
                        nearest = candidate;
                        nearest_distance = distance;
                    }
                }
                if (nearest == units.size()) continue;
                if (effect.operation == "apply_burn")
                    apply_burn_status(runtime, units[nearest], effect, now);
                else
                    apply_wound_status(units[nearest], effect, now);
            }
        }
        next_tick->second += effect.interval * static_cast<float>(ticks);
    }
}

void update_conditional_effects(RuntimeUnit& runtime, float now) {
    for (const std::size_t index : runtime.conditional_effect_indices) {
        const auto& descriptor = runtime.generic_effect_descriptors[index];
        const auto& effect = *descriptor.effect;
        if (!effect_condition_matches(runtime.unit, effect)) continue;
        const auto& key = descriptor.conditional_key;
        const float health_ratio = runtime.unit.hp / runtime.unit.max_hp;
        const bool condition_met = effect.trigger == "while_hp_above"
            ? health_ratio >= effect.health_threshold
            : health_ratio <= effect.health_threshold;
        const bool active = runtime.generic_effects_active.contains(key);
        const bool triggered = runtime.generic_effects_triggered.contains(key);
        if (condition_met && !active && !triggered) {
            if (effect.operation == "add_stat") {
                const float applied = apply_effect_stat(runtime.unit, effect);
                runtime.generic_effect_applied_amounts[key] = applied;
                runtime.generic_effects_active.insert(key);
                if (effect.duration > 0.0f)
                    runtime.generic_effect_expiry[key] = now + effect.duration;
            } else if (effect.operation == "grant_shield") {
                runtime.shield_hp += runtime.unit.max_hp * effect.value;
                runtime.shield_expires_at = std::max(
                    runtime.shield_expires_at, now + effect.duration);
                runtime.generic_effects_active.insert(key);
                runtime.generic_effect_expiry[key] = now + effect.duration;
            } else if (effect.operation == "restore_mana") {
                runtime.unit.mana = std::min(runtime.unit.max_mana,
                    runtime.unit.mana + effect.value * runtime.mana_gain_multiplier);
            } else if (effect.operation == "revive") {
                if (runtime.unit.hp <= 0.0f) {
                    runtime.unit.hp = runtime.unit.max_hp * effect.critical_value;
                    runtime.unit.alive = true;
                } else {
                    const float requested = std::max(
                        0.0f, runtime.unit.max_hp - runtime.unit.hp) * effect.value;
                    runtime.healing_done += apply_heal(runtime, requested, now);
                }
                runtime.generic_effect_previous_values[key] =
                    runtime.unit.damage_reduction;
                runtime.unit.damage_reduction = 1.0f;
                runtime.generic_effects_active.insert(key);
                runtime.generic_effect_expiry[key] = now + effect.duration;
            }
            runtime.generic_effects_triggered.insert(key);
        } else if (active) {
            const auto expiry = runtime.generic_effect_expiry.find(key);
            const bool expired = expiry != runtime.generic_effect_expiry.end() &&
                                 now >= expiry->second;
            const bool condition_ended = effect.duration <= 0.0f && !condition_met;
            if (expired || condition_ended) {
                if (effect.operation == "add_stat") {
                    const auto applied = runtime.generic_effect_applied_amounts.find(key);
                    CombatEffectDefinition inverse = effect;
                    inverse.value = applied != runtime.generic_effect_applied_amounts.end()
                        ? -applied->second : -effect.value;
                    inverse.percent_of_stat = false;
                    inverse.scale_by_base_stat = false;
                    apply_effect_stat(runtime.unit, inverse);
                    runtime.generic_effect_applied_amounts.erase(key);
                } else if (effect.operation == "revive") {
                    const auto previous = runtime.generic_effect_previous_values.find(key);
                    if (previous != runtime.generic_effect_previous_values.end()) {
                        runtime.unit.damage_reduction = previous->second;
                        runtime.generic_effect_previous_values.erase(previous);
                    }
                }
                runtime.generic_effects_active.erase(key);
                runtime.generic_effect_expiry.erase(key);
                if (condition_ended) runtime.generic_effects_triggered.erase(key);
            }
        }
    }
}

void apply_ally_shield_effects(std::vector<RuntimeUnit>& units,
                               std::size_t shielded_index) {
    if (shielded_index >= units.size()) return;
    const auto team = units[shielded_index].unit.team;
    for (auto& recipient : units) {
        if (recipient.unit.team != team || !is_alive(recipient)) continue;
        visit_generic_effects(recipient,
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

void apply_stack_stat_delta(RuntimeUnit& runtime,
                           const CombatEffectDefinition& effect,
                           float direction) {
    CombatEffectDefinition delta = effect;
    float amount = effect.value;
    if (effect.scale_by_base_stat) {
        float base = 0.0f;
        if (effect.stat == "attack_damage") base = runtime.base_attack_damage;
        else if (effect.stat == "attack_speed") base = runtime.base_attack_speed;
        if (!std::isfinite(base) || base <= 0.0f) return;
        amount *= base;
    }
    delta.value = amount * direction;
    delta.percent_of_stat = false;
    delta.scale_by_base_stat = false;
    apply_effect_stat(runtime.unit, delta);
}

void apply_stack_effects(RuntimeUnit& runtime, const std::string& trigger,
                         float now) {
    std::unordered_set<std::string> keys;
    visit_generic_effects(runtime, [&](const CombatEffectDefinition& effect,
                                       const std::string& prefix) {
        if (effect.operation == "stack_stat" && effect.trigger == trigger &&
            !effect.stack_key.empty() && effect_condition_matches(runtime.unit, effect))
            keys.insert(prefix + "stack:" + effect.stack_key);
    });

    for (const auto& key : keys) {
        int maximum = 0;
        float duration = 0.0f;
        visit_generic_effects(runtime, [&](const CombatEffectDefinition& effect,
                                           const std::string& prefix) {
            if (effect.operation == "stack_stat" &&
                prefix + "stack:" + effect.stack_key == key &&
                effect_condition_matches(runtime.unit, effect)) {
                maximum = std::max(maximum, effect.max_stacks);
                duration = std::max(duration, effect.duration);
            }
        });
        if (maximum <= 0) continue;
        int& stacks = runtime.generic_effect_charges[key];
        if (stacks >= maximum) continue;
        ++stacks;
        if (duration > 0.0f)
            runtime.generic_effect_stack_expiry[key].push_back(now + duration);

        visit_generic_effects(runtime, [&](const CombatEffectDefinition& effect,
                                           const std::string& prefix) {
            if (effect.operation == "stack_stat" &&
                prefix + "stack:" + effect.stack_key == key &&
                effect_condition_matches(runtime.unit, effect))
                apply_stack_stat_delta(runtime, effect, 1.0f);
        });

        if (stacks == maximum && runtime.generic_effects_triggered.insert(key + ":cap").second) {
            visit_generic_effects(runtime, [&](const CombatEffectDefinition& effect,
                                               const std::string& prefix) {
                if (effect.operation == "add_stat" &&
                    effect.trigger == "on_stack_cap" &&
                    prefix + "stack:" + effect.stack_key == key &&
                    effect_condition_matches(runtime.unit, effect)) {
                    CombatEffectDefinition cap_effect = effect;
                    if (cap_effect.scale_by_base_stat) {
                        float base = cap_effect.stat == "attack_damage"
                            ? runtime.base_attack_damage
                            : cap_effect.stat == "attack_speed"
                                ? runtime.base_attack_speed : 0.0f;
                        cap_effect.value *= base;
                        cap_effect.percent_of_stat = false;
                        cap_effect.scale_by_base_stat = false;
                    }
                    apply_effect_stat(runtime.unit, cap_effect);
                }
            });
        }
    }
}

void expire_generic_stacks(RuntimeUnit& runtime, float now) {
    for (auto& [key, expiries] : runtime.generic_effect_stack_expiry) {
        while (!expiries.empty() && now + 1e-5f >= expiries.front()) {
            expiries.erase(expiries.begin());
            auto count = runtime.generic_effect_charges.find(key);
            if (count != runtime.generic_effect_charges.end() && count->second > 0)
                --count->second;
            visit_generic_effects(runtime, [&](const CombatEffectDefinition& effect,
                                               const std::string& prefix) {
                if (effect.operation == "stack_stat" &&
                    prefix + effect.stack_key == key &&
                    effect_condition_matches(runtime.unit, effect))
                    apply_stack_stat_delta(runtime, effect, -1.0f);
            });
        }
    }
}

float effect_target_damage_multiplier(RuntimeUnit& source,
                                      const RuntimeUnit& target,
                                      const std::string& trigger) {
    float multiplier = 1.0f;
    visit_generic_effects(source, [&](const CombatEffectDefinition& effect,
                                      const std::string&) {
        if (effect.operation == "bonus_damage" && effect.trigger == trigger &&
            effect.condition == "target_role_tank" &&
            target.unit.role == UnitRole::TANK &&
            effect_condition_matches(source.unit, effect))
            multiplier *= 1.0f + effect.value;
    });
    return multiplier;
}

void apply_target_status_effects(RuntimeUnit& source, RuntimeUnit& target,
                                 const std::string& trigger, float now) {
    visit_generic_effects(source, [&](const CombatEffectDefinition& effect,
                                      const std::string&) {
        if (effect.trigger != trigger ||
            !effect_condition_matches(source.unit, effect)) return;
        if (effect.operation == "apply_shred" && effect.target == "target")
            apply_shred_status(target, effect, now);
        else if (effect.operation == "apply_burn" && effect.target == "target")
            apply_burn_status(source, target, effect, now);
        else if (effect.operation == "apply_wound" && effect.target == "target")
            apply_wound_status(target, effect, now);
    });
}

void apply_reflect_effects(RuntimeUnit& defender, std::vector<RuntimeUnit>& units,
                           float now, CombatResult& result,
                           const CombatConfig& config) {
    visit_generic_effects(defender, [&](const CombatEffectDefinition& effect,
                                        const std::string& prefix) {
        if (effect.trigger != "on_damage_taken" ||
            effect.operation != "reflect_damage" ||
            !effect_condition_matches(defender.unit, effect)) return;
        const std::string key = prefix + "reflect_damage";
        auto [next_proc, inserted] = defender.generic_effect_next_tick.emplace(
            key, -std::numeric_limits<float>::infinity());
        (void)inserted;
        if (now + 1e-5f < next_proc->second) return;
        next_proc->second = now + effect.interval;

        for (auto& enemy : units) {
            if (!is_alive(enemy) || enemy.unit.team == defender.unit.team ||
                distance_between(enemy.unit, defender.unit) >
                    static_cast<int>(std::ceil(effect.radius))) continue;
            float raw = effect.value;
            float damage = raw;
            if (effect.damage_type == DamageType::MAGIC)
                damage = mitigate_physical_damage(damage, enemy.unit.magic_resist);
            else if (effect.damage_type == DamageType::PHYSICAL)
                damage = mitigate_physical_damage(damage, enemy.unit.armor);
            damage *= std::clamp(1.0f - enemy.unit.damage_reduction, 0.0f, 1.0f);
            damage = std::min(damage, enemy.unit.hp + enemy.shield_hp);
            const float absorbed = std::min(enemy.shield_hp, damage);
            enemy.shield_hp -= absorbed;
            const float hp_loss = std::min(enemy.unit.hp, damage - absorbed);
            enemy.unit.hp -= hp_loss;
            enemy.damage_taken += damage;
            defender.damage_dealt += damage;
            update_conditional_effects(enemy, now);
            apply_stack_effects(enemy, "on_damage_taken", now);
            if (config.record_damage) {
                DamageEvent reflected;
                reflected.timestamp = now;
                reflected.source_unit_id = defender.unit.id;
                reflected.target_unit_id = enemy.unit.id;
                reflected.damage_type = effect.damage_type;
                reflected.raw_damage = raw;
                reflected.final_damage = damage;
                result.damage_events.push_back(reflected);
            }
            if (enemy.unit.hp <= 0.0f && enemy.unit.alive) {
                enemy.unit.hp = 0.0f;
                enemy.unit.alive = false;
                ++defender.kills;
                if (config.record_events) {
                    DeathEvent death;
                    death.timestamp = now;
                    death.unit_id = enemy.unit.id;
                    death.killer_unit_id = defender.unit.id;
                    result.death_events.push_back(death);
                    append_generic_event(result, now, "death",
                        defender.unit.id, enemy.unit.id);
                }
            }
        }
    });
}

void apply_enemy_cast_effects(RuntimeUnit& caster, std::vector<RuntimeUnit>& units,
                              float mana_cost, float now, CombatResult& result,
                              const CombatConfig& config) {
    for (auto& holder : units) {
        if (!is_alive(holder) || holder.unit.team == caster.unit.team) continue;
        visit_generic_effects(holder, [&](const CombatEffectDefinition& effect,
                                          const std::string& prefix) {
            if (effect.trigger != "on_enemy_cast" ||
                effect.operation != "damage_on_enemy_cast" ||
                !effect_condition_matches(holder.unit, effect) ||
                distance_between(holder.unit, caster.unit) >
                    static_cast<int>(std::ceil(effect.radius))) return;
            const std::string key = prefix + "enemy_cast_damage";
            auto [next_proc, inserted] = holder.generic_effect_next_tick.emplace(
                key, -std::numeric_limits<float>::infinity());
            (void)inserted;
            if (now + 1e-5f < next_proc->second) return;
            next_proc->second = now + effect.interval;
            const float raw = std::max(0.0f, mana_cost * effect.value);
            float damage = raw;
            if (effect.damage_type == DamageType::MAGIC)
                damage = mitigate_physical_damage(damage, caster.unit.magic_resist);
            else if (effect.damage_type == DamageType::PHYSICAL)
                damage = mitigate_physical_damage(damage, caster.unit.armor);
            damage *= std::clamp(1.0f - caster.unit.damage_reduction, 0.0f, 1.0f);
            damage = std::min(damage, caster.unit.hp + caster.shield_hp);
            const float absorbed = std::min(caster.shield_hp, damage);
            caster.shield_hp -= absorbed;
            const float hp_loss = std::min(caster.unit.hp, damage - absorbed);
            caster.unit.hp -= hp_loss;
            caster.damage_taken += damage;
            holder.damage_dealt += damage;
            update_conditional_effects(caster, now);
            apply_stack_effects(caster, "on_damage_taken", now);
            if (config.record_damage) {
                DamageEvent spark;
                spark.timestamp = now;
                spark.source_unit_id = holder.unit.id;
                spark.target_unit_id = caster.unit.id;
                spark.damage_type = effect.damage_type;
                spark.raw_damage = raw;
                spark.final_damage = damage;
                result.damage_events.push_back(spark);
            }
            if (caster.unit.hp <= 0.0f && caster.unit.alive) {
                caster.unit.hp = 0.0f;
                caster.unit.alive = false;
                ++holder.kills;
                if (config.record_events) {
                    DeathEvent death;
                    death.timestamp = now;
                    death.unit_id = caster.unit.id;
                    death.killer_unit_id = holder.unit.id;
                    result.death_events.push_back(death);
                    append_generic_event(result, now, "death",
                        holder.unit.id, caster.unit.id);
                }
            }
        });
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

    // The roster size is known before simulation starts. Reserve once so
    // loading teams does not repeatedly reallocate vectors or rehash ID/slot
    // sets; this changes storage only, not validation order or combat logic.
    const std::size_t expected_units =
        input.player_a.units.size() + input.player_b.units.size();
    std::unordered_set<int> ids;
    ids.reserve(expected_units);
    std::unordered_set<int> occupied_a;
    occupied_a.reserve(input.player_a.units.size());
    std::unordered_set<int> occupied_b;
    occupied_b.reserve(input.player_b.units.size());
    std::vector<RuntimeUnit> units;
    units.reserve(expected_units);

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
            loaded.base_attack_speed = loaded.unit.attack_speed;
            loaded.base_attack_damage = loaded.unit.attack_damage;
            for (const auto& item : loaded.unit.items) {
                for (const auto& effect : item.effects) {
                    if (effect.trigger == "combat_start" &&
                        effect.operation == "mana_gain_multiplier" &&
                        effect_condition_matches(loaded.unit, effect) &&
                        std::isfinite(effect.value) && effect.value > 0.0f) {
                        loaded.mana_gain_multiplier *= effect.value;
                    }
                }
            }
        }
        return true;
    };

    if (!load_team(input.player_a, UnitTeam::PLAYER_A, occupied_a) ||
        !load_team(input.player_b, UnitTeam::PLAYER_B, occupied_b)) {
        return result;
    }

    // Apply self and team-targeted start-of-combat effects only after both
    // teams are present, so ally targeting is independent of input order.
    for (auto& runtime : units) apply_start_combat_effects(runtime);
    apply_start_combat_team_effects(units);
    apply_start_combat_item_effects(units, config.max_duration);
    // Team auras are attached above; calculate generic mana regeneration only
    // after that expansion so every recipient receives the shared trait aura.
    for (auto& runtime : units)
        runtime.mana_regen_per_second += effect_mana_regeneration(runtime.unit);

    // Effects are immutable during combat. Build their ordered descriptors
    // once so event updates reuse stable IDs and only visit relevant effects.
    for (auto& runtime : units) prepare_generic_effect_descriptors(runtime);

    std::unordered_map<int, std::size_t> index_by_id;
    index_by_id.reserve(units.size());
    for (std::size_t i = 0; i < units.size(); ++i) {
        index_by_id[units[i].unit.id] = i;
        auto& runtime = units[i];
    }

    std::mt19937_64 rng(
        config.deterministic
            ? (input.seed != 0 ? input.seed : config.seed)
            : std::random_device{}()
    );
    std::uniform_real_distribution<float> roll(0.0f, 1.0f);

    // Start with enough backing storage for the initial event per unit.
    // The priority queue keeps the same comparator and push/pop order.
    std::vector<ScheduledEvent> scheduled_events;
    scheduled_events.reserve(units.size());
    std::priority_queue<
        ScheduledEvent,
        std::vector<ScheduledEvent>,
        LaterEvent
    > queue(LaterEvent{}, std::move(scheduled_events));

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
            expire_generic_stacks(runtime, now);
            apply_periodic_effects(runtime, now, units);
            apply_delayed_effects(runtime, now);
            update_conditional_effects(runtime, now);
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
            update_conditional_effects(burning, now);
            apply_stack_effects(burning, "on_damage_taken", now);
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

        // Mana regeneration and generic timed effects are driven by the
        // effect descriptors; no item identity is inspected in the event loop.
        const float elapsed = std::max(0.0f, now - actor.last_status_tick);
        if (elapsed > 0.0f) {
            actor.unit.mana = std::min(actor.unit.max_mana,
                actor.unit.mana + actor.mana_regen_per_second *
                    elapsed * actor.mana_gain_multiplier);
            actor.last_status_tick = now;
        }
        if (actor.shield_expires_at > 0.0f && now >= actor.shield_expires_at) {
            actor.shield_hp = 0.0f;
            actor.shield_expires_at = 0.0f;
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
                        raw *= effect_target_damage_multiplier(
                            actor, ability_target, "on_ability_hit");
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
                        update_conditional_effects(ability_target, now);
                        apply_stack_effects(ability_target, "on_damage_taken", now);
                        actor.damage_dealt += damage;
                        ability_event.damage += damage;
                        apply_target_status_effects(
                            actor, ability_target, "on_ability_hit", now);
                        apply_damage_healing_effects(actor, units, damage, now);
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
                apply_enemy_cast_effects(
                    actor, units, ability.mana_cost, now, result, config);
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
            raw_damage *= effect_target_damage_multiplier(
                actor, target, "on_attack");

            const float effective_armor = target.armor_shred_until > now
                ? target.unit.armor * (1.0f - target.armor_shred_percent)
                : target.unit.armor;
            float damage = mitigate_physical_damage(raw_damage, effective_armor);

            damage *= std::clamp(
                1.0f - target.unit.damage_reduction, 0.0f, 1.0f);

            damage = std::min(damage, target.unit.hp + target.shield_hp);

            const float absorbed = std::min(target.shield_hp, damage);
            target.shield_hp -= absorbed;
            const float hp_damage = std::min(target.unit.hp, damage - absorbed);
            target.unit.hp -= hp_damage;
            target.damage_taken += damage;
            update_conditional_effects(target, now);
            apply_stack_effects(target, "on_damage_taken", now);
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
                update_conditional_effects(target, now);
                apply_stack_effects(target, "on_damage_taken", now);
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

            // Item and trait mana-on-hit passives are data-driven.
            const float generic_mana_on_attack =
                effect_mana_on_attack(actor.unit, critical);
            actor.unit.mana = std::min(actor.unit.max_mana,
                actor.unit.mana + generic_mana_on_attack * actor.mana_gain_multiplier);
            apply_stack_effects(actor, "on_attack", now);
            if (critical) apply_stack_effects(actor, "on_critical_attack", now);
            apply_target_status_effects(actor, target, "on_attack", now);
            apply_damage_healing_effects(actor, units, damage, now);


            apply_reflect_effects(target, units, now, result, config);

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