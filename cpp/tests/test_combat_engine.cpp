#include "CombatEngine.hpp"
#include "items/ItemEngine.hpp"
#include "items/CombatItemAdapter.hpp"

#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <stdexcept>

namespace {
void require(bool condition, const char* message) {
    if (!condition) throw std::runtime_error(message);
}

tft::CombatInput make_input() {
    tft::CombatInput input;
    input.context = tft::CombatContext::PVP;
    input.seed = 123;
    input.config.seed = 123;
    input.config.deterministic = true;
    input.config.board_rows = 4;
    input.config.board_cols = 7;
    input.config.max_duration = 30.0f;
    input.config.max_events = 100000;

    input.player_a.team = tft::UnitTeam::PLAYER_A;
    input.player_a.player_id = 0;
    input.player_a.player_hp = 100.0f;

    input.player_b.team = tft::UnitTeam::PLAYER_B;
    input.player_b.player_id = 1;
    input.player_b.player_hp = 100.0f;

    tft::CombatUnit carry;
    carry.id = 0;
    carry.api_name = "test_carry";
    carry.name = "Test Carry";
    carry.team = tft::UnitTeam::PLAYER_A;
    carry.role = tft::UnitRole::CARRY;
    carry.position = {3, 1};
    carry.hp = carry.max_hp = 100.0f;
    carry.attack_damage = 1000.0f;
    carry.attack_speed = 10.0f;
    carry.attack_range = 7.0f;
    carry.alive = true;

    tft::CombatUnit dummy;
    dummy.id = 1;
    dummy.api_name = "test_dummy";
    dummy.name = "Test Dummy";
    dummy.team = tft::UnitTeam::PLAYER_B;
    dummy.role = tft::UnitRole::TANK;
    dummy.position = {3, 2};
    dummy.hp = dummy.max_hp = 100.0f;
    dummy.attack_damage = 1.0f;
    dummy.attack_speed = 0.1f;
    dummy.attack_range = 1.0f;
    dummy.alive = true;

    input.player_a.units.push_back(carry);
    input.player_b.units.push_back(dummy);
    return input;
}

void test_deterministic_winner_and_damage() {
    tft::CombatEngine engine;
    const auto input = make_input();
    const auto first = engine.simulate(input);
    const auto second = engine.simulate(input);

    require(first.success, "Valid combat should succeed.");
    require(first.completed, "Valid combat should complete.");
    require(!first.timeout, "Normal combat should not time out.");
    require(first.winner == tft::CombatWinner::PLAYER_A,
            "High-damage carry should defeat the dummy.");
    require(first.player_a_survivors == 1,
            "Winning team should have one survivor.");
    require(first.player_b_survivors == 0,
            "Losing team should have no survivors.");
    require(first.units.size() == 2, "Result should include both unit results.");
    require(first.winner == second.winner,
            "Deterministic replay changed the winner.");
    require(first.player_a_survivors == second.player_a_survivors &&
            first.player_b_survivors == second.player_b_survivors,
            "Deterministic replay changed survivor counts.");
}

void test_trait_team_effect_scaling_applies_once() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.05f;

    auto make_brawler_trait = [] {
        tft::CombatTrait trait;
        trait.api_name = "DA_18_Brawler";
        trait.name = "Brawler";
        trait.active = true;
        trait.active_count = 2;

        tft::CombatEffectDefinition team_health;
        team_health.trigger = "combat_start";
        team_health.operation = "add_stat";
        team_health.stat = "max_hp";
        team_health.target = "allies";
        team_health.value = 120.0f;
        team_health.condition = "trait_count_at_least";
        team_health.condition_trait = "DA_18_Brawler";
        team_health.min_trait_count = 2;
        team_health.scale_by_active_trait_count = true;

        tft::CombatEffectDefinition brawler_health;
        brawler_health.trigger = "combat_start";
        brawler_health.operation = "add_stat";
        brawler_health.stat = "max_hp";
        brawler_health.target = "self";
        brawler_health.value = 0.25f;
        brawler_health.percent_of_stat = true;
        brawler_health.condition = "trait_count_at_least";
        brawler_health.condition_trait = "DA_18_Brawler";
        brawler_health.min_trait_count = 2;

        trait.effects = {team_health, brawler_health};
        trait.effects_complete = true;
        return trait;
    };

    auto& first = input.player_a.units.front();
    first.can_attack = false;
    first.can_move = false;
    first.can_cast = false;
    first.hp = first.max_hp = 100.0f;
    first.traits.push_back(make_brawler_trait());

    auto second = first;
    second.id = 2;
    second.api_name = "second_brawler";
    second.name = "Second Brawler";
    second.position = {2, 1};
    input.player_a.units.push_back(second);

    tft::CombatUnit ally;
    ally.id = 3;
    ally.api_name = "non_brawler_ally";
    ally.name = "Non-Brawler Ally";
    ally.team = tft::UnitTeam::PLAYER_A;
    ally.role = tft::UnitRole::SUPPORT;
    ally.position = {4, 1};
    ally.hp = ally.max_hp = 100.0f;
    ally.attack_damage = 1.0f;
    ally.attack_speed = 1.0f;
    ally.can_attack = false;
    ally.can_move = false;
    ally.can_cast = false;
    input.player_a.units.push_back(ally);

    auto& enemy = input.player_b.units.front();
    enemy.can_attack = false;
    enemy.can_move = false;
    enemy.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Trait effect combat should succeed.");
    const auto final_hp = [&](int unit_id) {
        const auto found = std::find_if(result.units.begin(), result.units.end(),
            [&](const auto& unit) { return unit.unit_id == unit_id; });
        require(found != result.units.end(), "Trait effect result unit is missing.");
        return found->final_hp;
    };
    require(std::abs(final_hp(0) - 245.0f) < 0.01f,
            "Each Brawler should receive the team health aura once plus its trait bonus.");
    require(std::abs(final_hp(2) - 245.0f) < 0.01f,
            "The second Brawler should receive the same tier effects.");
    require(std::abs(final_hp(3) - 220.0f) < 0.01f,
            "Non-Brawler allies should receive the team health aura exactly once.");
}

void test_generic_percent_max_health_item_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.05f;
    auto& holder = input.player_a.units.front();
    holder.hp = holder.max_hp = 100.0f;
    holder.can_attack = false;
    holder.can_move = false;
    holder.can_cast = false;

    tft::CombatItem item;
    item.api_name = "catalog_generic_health_item";
    item.name = "Generic Health Item";
    item.effects_complete = true;
    tft::CombatEffectDefinition effect;
    effect.trigger = "combat_start";
    effect.operation = "add_stat";
    effect.stat = "max_hp";
    effect.target = "self";
    effect.value = 0.18f;
    effect.percent_of_stat = true;
    item.effects.push_back(effect);
    holder.items.push_back(item);

    auto& enemy = input.player_b.units.front();
    enemy.can_attack = false;
    enemy.can_move = false;
    enemy.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Generic max-health item effect combat should succeed.");
    const auto found = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.unit_id == 0; });
    require(found != result.units.end(), "Generic max-health result unit is missing.");
    require(std::abs(found->final_hp - 118.0f) < 0.01f,
            "Generic percent max-health effect must be applied exactly once.");
}

void test_generic_damage_amplification_item_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.2f;
    input.config.record_damage = true;

    auto& holder = input.player_a.units.front();
    holder.attack_damage = 10.0f;
    holder.attack_speed = 1.0f;
    holder.attack_range = 7.0f;
    holder.can_move = false;
    holder.can_cast = false;

    tft::CombatItem item;
    item.api_name = "catalog_generic_damage_item";
    item.name = "Generic Damage Item";
    item.effects_complete = true;
    tft::CombatEffectDefinition effect;
    effect.trigger = "combat_start";
    effect.operation = "add_stat";
    effect.stat = "damage_amplification";
    effect.target = "self";
    effect.value = 0.15f;
    item.effects.push_back(effect);
    holder.items.push_back(item);

    auto& target = input.player_b.units.front();
    target.hp = target.max_hp = 1000.0f;
    target.armor = 0.0f;
    target.can_attack = false;
    target.can_move = false;
    target.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Generic damage amplification combat should succeed.");
    require(!result.damage_events.empty(),
            "Generic damage amplification should reach the basic attack resolver.");
    require(std::abs(result.damage_events.front().raw_damage - 11.5f) < 0.01f,
            "Generic damage amplification should increase raw attack damage by 15 percent.");
}

void test_generic_while_hp_above_effect_reverses_at_threshold() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 3.1f;
    input.config.record_damage = true;

    auto& attacker = input.player_a.units.front();
    attacker.attack_damage = 300.0f;
    attacker.attack_speed = 1.0f;
    attacker.attack_range = 7.0f;
    attacker.can_move = false;
    attacker.can_cast = false;

    auto& holder = input.player_b.units.front();
    holder.hp = holder.max_hp = 1200.0f;
    holder.armor = 0.0f;
    holder.can_attack = false;
    holder.can_move = false;
    holder.can_cast = false;

    tft::CombatItem item;
    item.api_name = "catalog_generic_conditional_durability";
    item.name = "Generic Conditional Durability";
    item.effects_complete = false;

    tft::CombatEffectDefinition base;
    base.trigger = "combat_start";
    base.operation = "add_stat";
    base.stat = "damage_reduction";
    base.target = "self";
    base.value = 0.05f;

    tft::CombatEffectDefinition empowered;
    empowered.trigger = "while_hp_above";
    empowered.operation = "add_stat";
    empowered.stat = "damage_reduction";
    empowered.target = "self";
    empowered.value = 0.15f;
    empowered.health_threshold = 0.5f;
    item.effects = {base, empowered};
    holder.items.push_back(item);

    const auto result = engine.simulate(input);
    require(result.success, "Conditional generic item effect combat should succeed.");
    require(result.damage_events.size() >= 4,
            "Expected four attacks to cross the conditional health threshold.");
    require(std::abs(result.damage_events[0].final_damage - 240.0f) < 0.01f &&
            std::abs(result.damage_events[1].final_damage - 240.0f) < 0.01f &&
            std::abs(result.damage_events[2].final_damage - 240.0f) < 0.01f,
            "The empowered damage reduction should apply while HP remains above 50 percent.");
    require(std::abs(result.damage_events[3].final_damage - 285.0f) < 0.01f,
            "The conditional bonus should be removed after HP falls below 50 percent.");
}

void test_generic_role_condition_item_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.2f;
    input.config.record_damage = true;

    auto& holder = input.player_a.units.front();
    holder.role = tft::UnitRole::CARRY;
    holder.attack_damage = 100.0f;
    holder.attack_speed = 1.0f;
    holder.attack_range = 7.0f;
    holder.can_move = false;
    holder.can_cast = false;

    tft::CombatItem item;
    item.api_name = "catalog_generic_role_item";
    item.name = "Generic Role Item";
    tft::CombatEffectDefinition effect;
    effect.trigger = "combat_start";
    effect.operation = "add_stat";
    effect.stat = "attack_damage";
    effect.target = "self";
    effect.value = 0.10f;
    effect.percent_of_stat = true;
    effect.condition = "role_other";
    item.effects.push_back(effect);
    holder.items.push_back(item);

    auto& target = input.player_b.units.front();
    target.hp = target.max_hp = 1000.0f;
    target.armor = 0.0f;
    target.can_attack = false;
    target.can_move = false;
    target.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success && !result.damage_events.empty(),
            "Role-conditioned generic item effect should reach combat.");
    require(std::abs(result.damage_events.front().raw_damage - 110.0f) < 0.01f,
            "Generic role_other effect should apply to carry units.");
}

void test_generic_mana_gain_multiplier_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 2.1f;

    auto& holder = input.player_a.units.front();
    holder.hp = holder.max_hp = 1000.0f;
    holder.mana = 77.0f;
    holder.max_mana = 105.0f;
    holder.attack_damage = 1.0f;
    holder.attack_speed = 1.0f;
    holder.attack_range = 7.0f;
    holder.can_attack = true;
    holder.can_move = false;
    holder.can_cast = true;
    holder.ability.mana_cost = 105.0f;
    holder.ability.has_damage = true;
    holder.ability.base_damage = 1.0f;

    tft::CombatItem item;
    item.api_name = "catalog_generic_mana_multiplier";
    item.name = "Generic Mana Multiplier";

    tft::CombatEffectDefinition regen;
    regen.trigger = "combat_start";
    regen.operation = "mana_regen";
    regen.value = 3.0f;

    tft::CombatEffectDefinition multiplier;
    multiplier.trigger = "combat_start";
    multiplier.operation = "mana_gain_multiplier";
    multiplier.target = "self";
    multiplier.value = 1.15f;
    item.effects = {regen, multiplier};
    holder.items.push_back(item);

    auto& target = input.player_b.units.front();
    target.hp = target.max_hp = 1000.0f;
    target.can_attack = false;
    target.can_move = false;
    target.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Generic mana multiplier combat should succeed.");
    const auto found = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.unit_id == 0; });
    require(found != result.units.end(), "Mana multiplier result unit is missing.");
    require(found->ability_casts > 0,
            "Generic mana gain multiplier should allow the unit to reach its cast threshold.");
}

void test_trait_team_mana_regeneration_is_applied_once() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 1.1f;

    auto make_invoker = [](tft::CombatUnit unit) {
        tft::CombatTrait trait;
        trait.api_name = "DA_18_Invoker";
        trait.name = "Invoker";
        trait.active = true;
        trait.active_count = 2;

        tft::CombatEffectDefinition team_regen;
        team_regen.trigger = "combat_start";
        team_regen.operation = "mana_regen";
        team_regen.target = "allies";
        team_regen.value = 1.0f;
        team_regen.condition = "trait_count_at_least";
        team_regen.condition_trait = "DA_18_Invoker";
        team_regen.min_trait_count = 2;
        team_regen.scale_by_active_trait_count = true;

        tft::CombatEffectDefinition invoker_bonus;
        invoker_bonus.trigger = "combat_start";
        invoker_bonus.operation = "mana_regen";
        invoker_bonus.target = "self";
        invoker_bonus.value = 3.0f;
        invoker_bonus.condition = "trait_count_at_least";
        invoker_bonus.condition_trait = "DA_18_Invoker";
        invoker_bonus.min_trait_count = 2;

        trait.effects = {team_regen, invoker_bonus};
        unit.traits.push_back(trait);
        return unit;
    };

    auto& first = input.player_a.units.front();
    first = make_invoker(first);
    first.mana = 86.0f;
    first.max_mana = 100.0f;
    first.attack_damage = 1.0f;
    first.attack_speed = 1.0f;
    first.attack_range = 7.0f;
    first.can_attack = true;
    first.can_move = false;
    first.can_cast = true;
    first.ability.mana_cost = 100.0f;
    first.ability.has_damage = true;
    first.ability.base_damage = 1.0f;
    first.ability.target_type = tft::AbilityTargetType::ENEMY;

    auto second = first;
    second.id = 2;
    second.api_name = "second_invoker";
    second.name = "Second Invoker";
    second.position = {2, 1};
    input.player_a.units.push_back(second);

    tft::CombatUnit ally;
    ally.id = 3;
    ally.api_name = "non_invoker_ally";
    ally.name = "Non-Invoker Ally";
    ally.team = tft::UnitTeam::PLAYER_A;
    ally.role = tft::UnitRole::SUPPORT;
    ally.position = {4, 1};
    ally.hp = ally.max_hp = 1000.0f;
    ally.mana = 86.0f;
    ally.max_mana = 100.0f;
    ally.attack_damage = 1.0f;
    ally.attack_speed = 1.0f;
    ally.attack_range = 7.0f;
    ally.can_attack = true;
    ally.can_move = false;
    ally.can_cast = true;
    ally.ability.mana_cost = 100.0f;
    ally.ability.has_damage = true;
    ally.ability.base_damage = 1.0f;
    ally.ability.target_type = tft::AbilityTargetType::ENEMY;
    input.player_a.units.push_back(ally);

    auto& enemy = input.player_b.units.front();
    enemy.hp = enemy.max_hp = 10000.0f;
    enemy.can_attack = false;
    enemy.can_move = false;
    enemy.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Invoker team mana regeneration combat should succeed.");
    const auto casts = [&](int unit_id) {
        const auto found = std::find_if(result.units.begin(), result.units.end(),
            [&](const auto& unit) { return unit.unit_id == unit_id; });
        require(found != result.units.end(), "Invoker result unit is missing.");
        return found->ability_casts;
    };
    require(casts(0) > 0 && casts(2) > 0,
            "Invoker holders should receive team and self mana regeneration.");
    require(casts(3) == 0,
            "Non-Invoker allies should receive the team aura once, not the Invoker bonus.");
}

void test_riftbeast_periodic_stat_growth_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 5.1f;
    input.config.record_damage = true;

    auto& attacker = input.player_a.units.front();
    attacker.attack_damage = 100.0f;
    attacker.attack_speed = 1.0f;
    attacker.attack_range = 7.0f;
    attacker.can_attack = true;
    attacker.can_move = false;
    attacker.can_cast = false;

    tft::CombatTrait riftbeast;
    riftbeast.api_name = "DA_Riftbeast18";
    riftbeast.active = true;
    riftbeast.active_count = 7;

    tft::CombatEffectDefinition combat_start;
    combat_start.trigger = "combat_start";
    combat_start.operation = "add_stat";
    combat_start.stat = "attack_damage";
    combat_start.target = "self";
    combat_start.value = 0.06f;
    combat_start.percent_of_stat = true;
    combat_start.condition = "trait_count_at_least";
    combat_start.condition_trait = riftbeast.api_name;
    combat_start.min_trait_count = 7;

    tft::CombatEffectDefinition periodic = combat_start;
    periodic.trigger = "periodic";
    periodic.interval = 5.0f;
    riftbeast.effects = {combat_start, periodic};
    attacker.traits.push_back(riftbeast);

    auto& target = input.player_b.units.front();
    target.hp = target.max_hp = 10000.0f;
    target.armor = 0.0f;
    target.can_attack = false;
    target.can_move = false;
    target.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success && result.damage_events.size() >= 6,
            "Riftbeast periodic growth combat should complete with attack samples.");
    require(std::abs(result.damage_events.front().raw_damage - 106.0f) < 0.01f,
            "Riftbeast combat-start growth should apply before the first attack.");
    const auto fifth_second_hit = std::find_if(result.damage_events.begin(),
        result.damage_events.end(), [](const auto& event) {
            return std::abs(event.timestamp - 5.0f) < 0.01f;
        });
    require(fifth_second_hit != result.damage_events.end() &&
            std::abs(fifth_second_hit->raw_damage - 112.36f) < 0.02f,
            "Riftbeast periodic growth should apply again after five seconds.");
}

void test_generic_trait_critical_chance_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.1f;
    input.config.record_damage = true;

    auto& attacker = input.player_a.units.front();
    attacker.attack_damage = 10.0f;
    attacker.attack_speed = 1.0f;
    attacker.attack_range = 7.0f;
    attacker.critical_strike_chance = 0.85f;
    attacker.critical_strike_damage = 2.0f;
    attacker.can_attack = true;
    attacker.can_move = false;
    attacker.can_cast = false;

    tft::CombatTrait executioner;
    executioner.api_name = "DA_18_Executioner";
    executioner.active = true;
    executioner.active_count = 2;
    tft::CombatEffectDefinition crit_chance;
    crit_chance.trigger = "combat_start";
    crit_chance.operation = "add_stat";
    crit_chance.stat = "critical_strike_chance";
    crit_chance.target = "self";
    crit_chance.value = 0.15f;
    crit_chance.condition = "trait_count_at_least";
    crit_chance.condition_trait = executioner.api_name;
    crit_chance.min_trait_count = 2;
    executioner.effects.push_back(crit_chance);
    attacker.traits.push_back(executioner);

    auto& target = input.player_b.units.front();
    target.hp = target.max_hp = 1000.0f;
    target.armor = 0.0f;
    target.can_attack = false;
    target.can_move = false;
    target.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success && !result.damage_events.empty(),
            "Generic trait critical-chance effect should reach the attack resolver.");
    require(std::abs(result.damage_events.front().raw_damage - 20.0f) < 0.01f,
            "Trait critical chance should be applied before the first attack roll.");
}

void test_generic_mana_on_attack_item_effects() {
    const auto casts_with_effect = [](float base_mana, float critical_mana,
                                      float crit_chance) {
        tft::CombatEngine engine;
        auto input = make_input();
        input.config.max_duration = 1.1f;

        auto& attacker = input.player_a.units.front();
        attacker.mana = 86.0f;
        attacker.max_mana = 100.0f;
        attacker.attack_damage = 1.0f;
        attacker.attack_speed = 1.0f;
        attacker.attack_range = 7.0f;
        attacker.critical_strike_chance = crit_chance;
        attacker.critical_strike_damage = 1.0f;
        attacker.can_attack = true;
        attacker.can_move = false;
        attacker.can_cast = true;
        attacker.ability.mana_cost = 100.0f;
        attacker.ability.has_damage = true;
        attacker.ability.base_damage = 1.0f;
        attacker.ability.target_type = tft::AbilityTargetType::ENEMY;

        tft::CombatItem item;
        item.api_name = "generic_mana_on_attack_test";
        tft::CombatEffectDefinition effect;
        effect.trigger = "on_attack";
        effect.operation = "mana_on_attack";
        effect.value = base_mana;
        effect.critical_value = critical_mana;
        item.effects.push_back(effect);
        attacker.items.push_back(item);

        auto& target = input.player_b.units.front();
        target.hp = target.max_hp = 10000.0f;
        target.can_attack = false;
        target.can_move = false;
        target.can_cast = false;

        const auto result = engine.simulate(input);
        require(result.success, "Generic mana-on-attack combat should succeed.");
        const auto found = std::find_if(result.units.begin(), result.units.end(),
            [](const auto& unit) { return unit.unit_id == 0; });
        require(found != result.units.end(), "Mana-on-attack result unit is missing.");
        return found->ability_casts;
    };

    require(casts_with_effect(2.0f, 4.0f, 1.0f) > 0,
            "Critical Leviathan-style hit should use the critical mana value.");
    require(casts_with_effect(2.0f, 4.0f, 0.0f) == 0,
            "Non-critical Leviathan-style hit should use only the base mana value.");
    require(casts_with_effect(5.0f, 0.0f, 0.0f) > 0,
            "Shojin-style mana-on-attack should be applied generically.");
}

void test_generic_periodic_heal_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 2.1f;

    auto& holder = input.player_a.units.front();
    holder.hp = 500.0f;
    holder.max_hp = 1000.0f;
    holder.can_attack = false;
    holder.can_move = false;
    holder.can_cast = false;

    tft::CombatItem item;
    item.api_name = "catalog_generic_periodic_heal";
    item.name = "Generic Periodic Heal";
    tft::CombatEffectDefinition heal;
    heal.trigger = "periodic";
    heal.operation = "heal_max_hp_pct";
    heal.target = "self";
    heal.value = 0.025f;
    heal.interval = 2.0f;
    item.effects.push_back(heal);
    holder.items.push_back(item);

    auto& attacker = input.player_b.units.front();
    attacker.attack_damage = 1.0f;
    attacker.attack_speed = 1.0f;
    attacker.attack_range = 7.0f;
    attacker.can_attack = true;
    attacker.can_move = false;
    attacker.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Generic periodic heal combat should succeed.");
    const auto found = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.unit_id == 0; });
    require(found != result.units.end(), "Periodic heal result unit is missing.");
    require(found->healing_done >= 24.9f,
            "Generic periodic heal should restore 2.5 percent max HP every two seconds.");
}

void test_generic_periodic_missing_health_heal_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 2.1f;

    auto& holder = input.player_a.units.front();
    holder.hp = 500.0f;
    holder.max_hp = 1000.0f;
    holder.can_attack = false;
    holder.can_move = false;
    holder.can_cast = false;

    tft::CombatItem redemption;
    redemption.api_name = "generic_missing_health_heal";
    tft::CombatEffectDefinition heal;
    heal.trigger = "periodic";
    heal.operation = "heal_missing_hp_pct";
    heal.target = "self";
    heal.value = 0.02f;
    heal.interval = 1.0f;
    heal.max_amount = 250.0f;
    redemption.effects.push_back(heal);
    holder.items.push_back(redemption);

    auto& attacker = input.player_b.units.front();
    attacker.attack_damage = 1.0f;
    attacker.attack_speed = 1.0f;
    attacker.attack_range = 7.0f;
    attacker.can_attack = true;
    attacker.can_move = false;
    attacker.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success, "Generic missing-health periodic heal combat should succeed.");
    const auto found = std::find_if(result.units.begin(), result.units.end(),
        [](const auto& unit) { return unit.unit_id == 0; });
    require(found != result.units.end(), "Missing-health heal result unit is missing.");
    require(std::abs(found->healing_done - 19.8f) < 0.2f,
            "Missing-health healing should recalculate the missing-health amount per tick.");
}

void test_generic_periodic_stat_effect() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 2.1f;
    input.config.record_damage = true;

    auto& attacker = input.player_a.units.front();
    attacker.attack_damage = 100.0f;
    attacker.attack_speed = 1.0f;
    attacker.attack_range = 7.0f;
    attacker.can_move = false;
    attacker.can_cast = false;

    tft::CombatItem item;
    item.api_name = "catalog_generic_periodic_stat";
    item.name = "Generic Periodic Stat";
    tft::CombatEffectDefinition effect;
    effect.trigger = "periodic";
    effect.operation = "add_stat";
    effect.stat = "attack_damage";
    effect.target = "self";
    effect.value = 0.10f;
    effect.percent_of_stat = true;
    effect.interval = 1.0f;
    item.effects.push_back(effect);
    attacker.items.push_back(item);

    auto& target = input.player_b.units.front();
    target.hp = target.max_hp = 10000.0f;
    target.armor = 0.0f;
    target.can_attack = false;
    target.can_move = false;
    target.can_cast = false;

    const auto result = engine.simulate(input);
    require(result.success && result.damage_events.size() >= 3,
            "Generic periodic stat effect should produce three attack samples.");
    require(std::abs(result.damage_events[0].raw_damage - 100.0f) < 0.01f &&
            std::abs(result.damage_events[1].raw_damage - 110.0f) < 0.01f &&
            std::abs(result.damage_events[2].raw_damage - 121.0f) < 0.01f,
            "Periodic percentage stat effect should apply and compound once per interval.");
}

void test_defender_team_aura_and_tier_bonus_apply_once() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.05f;
    input.config.record_damage = true;

    auto make_defender_trait = [] {
        tft::CombatTrait trait;
        trait.api_name = "DA_18_Defender";
        trait.name = "Defender";
        trait.active = true;
        trait.active_count = 2;
        trait.effects_complete = true;

        const auto make_effect = [](const char* stat, const char* target,
                                    float value, bool team_aura) {
            tft::CombatEffectDefinition effect;
            effect.trigger = "combat_start";
            effect.operation = "add_stat";
            effect.stat = stat;
            effect.target = target;
            effect.value = value;
            effect.condition = "trait_count_at_least";
            effect.condition_trait = "DA_18_Defender";
            effect.min_trait_count = 2;
            effect.scale_by_active_trait_count = team_aura;
            return effect;
        };
        trait.effects = {
            make_effect("armor", "allies", 12.0f, true),
            make_effect("magic_resist", "allies", 12.0f, true),
            make_effect("armor", "self", 13.0f, false),
            make_effect("magic_resist", "self", 13.0f, false)
        };
        return trait;
    };

    auto& first_defender = input.player_a.units.front();
    first_defender.position = {0, 0};
    first_defender.role = tft::UnitRole::TANK;
    first_defender.hp = first_defender.max_hp = 1000.0f;
    first_defender.can_attack = false;
    first_defender.can_move = false;
    first_defender.can_cast = false;
    first_defender.traits.push_back(make_defender_trait());

    auto second_defender = first_defender;
    second_defender.id = 2;
    second_defender.api_name = "second_defender";
    second_defender.position = {0, 2};
    input.player_a.units.push_back(second_defender);

    auto non_defender = input.player_a.units.front();
    non_defender.id = 4;
    non_defender.api_name = "non_defender_ally";
    non_defender.role = tft::UnitRole::CARRY;
    non_defender.position = {4, 1};
    non_defender.traits.clear();
    input.player_a.units.push_back(non_defender);

    auto& first_attacker = input.player_b.units.front();
    first_attacker.position = {5, 1};
    first_attacker.attack_damage = 100.0f;
    first_attacker.attack_speed = 1.0f;
    first_attacker.attack_range = 7.0f;
    first_attacker.can_attack = true;
    first_attacker.can_move = false;
    first_attacker.can_cast = false;

    auto second_attacker = first_attacker;
    second_attacker.id = 3;
    second_attacker.api_name = "second_attacker";
    second_attacker.position = {1, 0};
    input.player_b.units.push_back(second_attacker);

    const auto result = engine.simulate(input);
    require(result.success && result.damage_events.size() >= 2,
            "Defender team aura combat should resolve both attacks.");

    const auto damage_to = [&](int target_id) {
        const auto found = std::find_if(result.damage_events.begin(),
            result.damage_events.end(), [&](const auto& event) {
                return event.target_unit_id == target_id;
            });
        require(found != result.damage_events.end(), "Expected Defender test target was not attacked.");
        return found->final_damage;
    };
    require(std::abs(damage_to(4) - (100.0f * 100.0f / 112.0f)) < 0.05f,
            "Non-Defender allies should receive the shared 12 armor aura exactly once.");
    require(std::abs(damage_to(0) - 80.0f) < 0.05f,
            "Defenders should receive their tier bonus in addition to the shared aura.");
}

void test_event_limit_is_reported_as_timeout() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_events = 1;
    input.player_a.units[0].hp = input.player_a.units[0].max_hp = 1000.0f;
    input.player_a.units[0].attack_damage = 1.0f;
    input.player_a.units[0].attack_speed = 0.1f;
    input.player_b.units[0].hp = input.player_b.units[0].max_hp = 1000.0f;
    input.player_b.units[0].attack_damage = 1.0f;
    input.player_b.units[0].attack_speed = 0.1f;

    const auto result = engine.simulate(input);
    require(result.success, "Event-limit result should be a valid simulation result.");
    require(result.completed, "Engine currently returns a completed partial result on event timeout.");
    require(result.timeout, "Reaching max_events with pending events must report timeout.");
}

void test_invalid_configuration_returns_error() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.0f;
    const auto result = engine.simulate(input);

    require(!result.success, "Invalid configuration must fail.");
    require(!result.completed, "Invalid configuration cannot complete.");
    require(result.error_code == "INVALID_MAX_DURATION",
            "Invalid configuration should return the specific error code.");
}

void test_equipped_items_change_combat_stats() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.1f;
    input.config.record_damage = true;
    input.player_a.units[0].attack_damage = 10.0f;
    input.player_a.units[0].attack_speed = 1.0f;
    input.player_a.units[0].max_hp = input.player_a.units[0].hp = 100.0f;
    input.player_b.units[0].attack_damage = 0.1f;
    input.player_b.units[0].attack_speed = 0.1f;
    input.player_b.units[0].max_hp = input.player_b.units[0].hp = 1000.0f;

    const auto baseline = engine.simulate(input);
    require(baseline.success && !baseline.damage_events.empty(),
            "Baseline combat should record basic attacks.");
    const float baseline_damage = baseline.damage_events.front().raw_damage;

    input.player_a.units[0].hp = 50.0f;
    tft::CombatItem item;
    item.id = 101;
    item.api_name = "test_item";
    item.name = "Test Item";
    item.attack_damage = 15.0f;
    item.health = 25.0f;
    item.omnivamp = 0.5f;
    input.player_a.units[0].items.push_back(item);

    const auto equipped = engine.simulate(input);
    require(equipped.success && !equipped.damage_events.empty(),
            "Combat with a valid item should succeed.");
    require(std::abs(equipped.damage_events.front().raw_damage -
                     (baseline_damage + 15.0f)) < 0.001f,
            "Item attack damage must affect the actual attack calculation.");
    require(std::abs(equipped.units.front().initial_hp - 75.0f) < 0.001f,
            "Item health must increase current HP by its bonus without healing missing health.");
    require(equipped.units.front().final_hp > equipped.units.front().initial_hp,
            "Omnivamp must heal the attacker after dealing damage.");
}

void test_invalid_equipment_is_rejected() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.player_a.units[0].items.resize(4);
    const auto too_many = engine.simulate(input);
    require(!too_many.success && too_many.error_code == "INVALID_ITEM_ATTRIBUTES",
            "More than three equipped items must be rejected.");

    input = make_input();
    tft::CombatItem invalid;
    invalid.api_name = "invalid_item";
    invalid.attack_damage = std::numeric_limits<float>::quiet_NaN();
    input.player_a.units[0].items.push_back(invalid);
    const auto non_finite = engine.simulate(input);
    require(!non_finite.success &&
            non_finite.error_code == "INVALID_ITEM_ATTRIBUTES",
            "Non-finite item stats must be rejected.");
}

void test_ability_cast_uses_mana_and_ability_power() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.1f;
    input.config.record_abilities = true;
    input.config.record_damage = true;

    auto& caster = input.player_a.units[0];
    caster.attack_damage = 1.0f;
    caster.attack_speed = 1.0f;
    caster.ability_power = 50.0f;
    caster.mana = 100.0f;
    caster.max_mana = 100.0f;
    caster.ability.api_name = "test_spell";
    caster.ability.mana_cost = 100.0f;
    caster.ability.target_type = tft::AbilityTargetType::ENEMY;
    caster.ability.damage_type = tft::DamageType::MAGIC;
    caster.ability.base_damage = 10.0f;
    caster.ability.ability_power_ratio = 2.0f;
    caster.ability.has_damage = true;

    auto& target = input.player_b.units[0];
    target.hp = target.max_hp = 1000.0f;
    target.magic_resist = 0.0f;
    target.attack_damage = 0.1f;

    const auto result = engine.simulate(input);
    require(result.success, "Ability combat should succeed.");
    require(result.ability_events.size() == 1,
            "A caster with enough mana should cast its ability.");
    require(result.ability_events.front().ability_id == "test_spell",
            "Ability event should identify the cast ability.");
    require(result.ability_events.front().damage >= 109.9f,
            "Ability damage should include base damage and AP scaling.");
    bool saw_ability_damage = false;
    for (const auto& event : result.damage_events)
        if (event.ability_damage) saw_ability_damage = true;
    require(saw_ability_damage,
            "Ability damage should be distinguished in combat damage events.");

    input.player_a.units[0].mana = 0.0f;
    const auto no_mana = engine.simulate(input);
    require(no_mana.success && no_mana.ability_events.empty(),
            "A unit below ability mana cost must not cast.");
}

void test_item_mana_can_enable_an_early_cast() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.1f;
    input.config.record_abilities = true;
    input.player_a.units[0].attack_damage = 1.0f;
    input.player_a.units[0].mana = 0.0f;
    input.player_a.units[0].max_mana = 100.0f;
    input.player_a.units[0].ability.api_name = "mana_test";
    input.player_a.units[0].ability.mana_cost = 50.0f;
    input.player_a.units[0].ability.base_damage = 1.0f;
    input.player_a.units[0].ability.has_damage = true;
    input.player_a.units[0].ability.target_type = tft::AbilityTargetType::ENEMY;
    input.player_a.units[0].items.push_back(tft::CombatItem{
        .id = 202, .api_name = "test_mana_item", .name = "Mana Start",
        .mana = 50.0f
    });
    input.player_b.units[0].hp = input.player_b.units[0].max_hp = 1000.0f;
    input.player_b.units[0].attack_damage = 0.1f;

    const auto result = engine.simulate(input);
    require(result.success && result.ability_events.size() == 1,
            "Item-provided starting mana should enable a cast at combat start.");
}

void test_unique_item_effects_and_combinations() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 3.0f;
    input.config.record_damage = true;
    input.player_a.units[0].attack_damage = 10.0f;
    input.player_a.units[0].attack_speed = 1.0f;
    input.player_a.units[0].max_hp = input.player_a.units[0].hp = 500.0f;
    input.player_a.units[0].mana = 0.0f;
    input.player_a.units[0].max_mana = 100.0f;
    input.player_b.units[0].attack_damage = 0.1f;
    input.player_b.units[0].attack_speed = 0.1f;
    input.player_b.units[0].max_hp = input.player_b.units[0].hp = 2000.0f;

    // Guinsoo deve aumentar a velocidade ao longo do tempo; Shojin aumenta
    // a mana gerada por ataques. Os dois efeitos devem coexistir.
    tft::CombatItem guinsoo;
    guinsoo.api_name = "TFT_Item_GuinsoosRageblade";
    guinsoo.attack_speed = 0.1f;
    tft::CombatItem shojin;
    shojin.api_name = "TFT_Item_SpearOfShojin";
    input.player_a.units[0].items = {guinsoo, shojin};
    const auto combined = engine.simulate(input);
    require(combined.success, "Combined unique item effects should simulate.");
    require(combined.units.front().attacks >= 3,
            "Combined attack-speed and mana items should allow repeated attacks.");
    require(combined.units.front().damage_dealt > 30.0f,
            "Combined item effects should change actual combat damage.");

    // Bramble must deal extra damage back to an attacker, changing its HP.
    auto bramble_input = make_input();
    bramble_input.config.max_duration = 0.1f;
    bramble_input.config.record_damage = true;
    bramble_input.player_a.units[0].attack_damage = 1.0f;
    bramble_input.player_a.units[0].max_hp = bramble_input.player_a.units[0].hp = 500.0f;
    bramble_input.player_b.units[0].attack_damage = 10.0f;
    bramble_input.player_b.units[0].max_hp = bramble_input.player_b.units[0].hp = 500.0f;
    tft::CombatItem bramble;
    bramble.api_name = "TFT_Item_BrambleVest";
    bramble_input.player_b.units[0].items.push_back(bramble);
    const auto reflected = engine.simulate(bramble_input);
    require(reflected.success, "Bramble combat should simulate.");
    bool saw_reflect = false;
    for (const auto& event : reflected.damage_events) {
        if (event.source_unit_id == bramble_input.player_b.units[0].id &&
            event.target_unit_id == bramble_input.player_a.units[0].id &&
            event.damage_type == tft::DamageType::MAGIC &&
            std::abs(event.raw_damage - 100.0f) < 0.001f) saw_reflect = true;
    }
    require(saw_reflect, "Bramble should record its reflected magic damage.");
    require(reflected.units.front().final_hp < reflected.units.front().initial_hp,
            "Bramble reflection should reduce the attacker's final HP.");

    // Sterak's shield should absorb a later hit after the health threshold.
    auto sterak_input = make_input();
    sterak_input.config.max_duration = 2.0f;
    sterak_input.player_a.units[0].attack_damage = 0.1f;
    sterak_input.player_a.units[0].attack_speed = 0.1f;
    sterak_input.player_a.units[0].max_hp = sterak_input.player_a.units[0].hp = 100.0f;
    sterak_input.player_b.units[0].attack_damage = 30.0f;
    sterak_input.player_b.units[0].attack_speed = 1.0f;
    sterak_input.player_b.units[0].max_hp = sterak_input.player_b.units[0].hp = 1000.0f;
    const auto no_sterak = engine.simulate(sterak_input);
    tft::CombatItem sterak;
    sterak.api_name = "TFT_Item_SteraksGage";
    sterak_input.player_a.units[0].items.push_back(sterak);
    const auto shielded = engine.simulate(sterak_input);
    require(shielded.success && no_sterak.success, "Sterak comparison combats should simulate.");
    require(shielded.units.front().final_hp > no_sterak.units.front().final_hp,
            "Sterak's threshold shield should preserve more HP than the no-item baseline.");
}

void test_shojin_changes_cast_timing_and_dragons_claw_heals() {
    tft::CombatEngine engine;
    auto mana_input = make_input();
    mana_input.config.max_duration = 1.1f;
    mana_input.player_a.units[0].attack_damage = 1.0f;
    mana_input.player_a.units[0].attack_speed = 1.0f;
    mana_input.player_a.units[0].mana = 0.0f;
    mana_input.player_a.units[0].max_mana = 100.0f;
    mana_input.player_a.units[0].ability.api_name = "shojin_timing_test";
    mana_input.player_a.units[0].ability.mana_cost = 15.0f;
    mana_input.player_a.units[0].ability.base_damage = 1.0f;
    mana_input.player_a.units[0].ability.has_damage = true;
    mana_input.player_a.units[0].ability.target_type = tft::AbilityTargetType::ENEMY;
    mana_input.player_b.units[0].max_hp = mana_input.player_b.units[0].hp = 1000.0f;
    mana_input.player_b.units[0].attack_damage = 0.1f;

    const auto no_shojin = engine.simulate(mana_input);
    tft::CombatItem shojin;
    shojin.api_name = "TFT_Item_SpearOfShojin";
    tft::CombatEffectDefinition shojin_mana;
    shojin_mana.trigger = "on_attack";
    shojin_mana.operation = "mana_on_attack";
    shojin_mana.value = 5.0f;
    shojin.effects.push_back(shojin_mana);
    mana_input.player_a.units[0].items.push_back(shojin);
    const auto with_shojin = engine.simulate(mana_input);
    require(no_shojin.success && with_shojin.success, "Shojin comparison should simulate.");
    require(no_shojin.units.front().ability_casts == 0 &&
            with_shojin.units.front().ability_casts == 1,
            "Shojin's bonus mana on attack should enable an earlier ability cast.");

    auto healing_input = make_input();
    healing_input.config.max_duration = 4.1f;
    healing_input.player_a.units[0].attack_damage = 1.0f;
    healing_input.player_a.units[0].attack_speed = 0.5f;
    healing_input.player_a.units[0].max_hp = 500.0f;
    healing_input.player_a.units[0].hp = 350.0f;
    healing_input.player_b.units[0].attack_damage = 0.1f;
    healing_input.player_b.units[0].attack_speed = 0.1f;
    healing_input.player_b.units[0].max_hp = healing_input.player_b.units[0].hp = 1000.0f;

    const auto no_claw = engine.simulate(healing_input);
    tft::CombatItem claw;
    claw.api_name = "TFT_Item_DragonsClaw";
    // Direct CombatEngine tests must provide the normalized catalog contract;
    // the simulator no longer infers item mechanics from API-name branches.
    tft::CombatEffectDefinition claw_health;
    claw_health.trigger = "combat_start";
    claw_health.operation = "add_stat";
    claw_health.stat = "max_hp";
    claw_health.target = "self";
    claw_health.value = 0.06f;
    claw_health.percent_of_stat = true;
    tft::CombatEffectDefinition claw_heal;
    claw_heal.trigger = "periodic";
    claw_heal.operation = "heal_max_hp_pct";
    claw_heal.target = "self";
    claw_heal.value = 0.025f;
    claw_heal.interval = 2.0f;
    claw.effects = {claw_health, claw_heal};
    healing_input.player_a.units[0].items.push_back(claw);
    const auto with_claw = engine.simulate(healing_input);
    require(no_claw.success && with_claw.success, "Dragon's Claw comparison should simulate.");
    require(with_claw.units.front().healing_done > no_claw.units.front().healing_done,
            "Dragon's Claw should periodically heal and record healing in the combat result.");
}

void test_titans_resolve_and_seeded_item_impact() {
    tft::CombatEngine engine;
    auto base = make_input();
    base.config.max_duration = 4.1f;
    base.config.record_damage = true;
    base.player_a.units[0].attack_damage = 10.0f;
    base.player_a.units[0].attack_speed = 1.0f;
    base.player_b.units[0].attack_damage = 0.1f;
    base.player_b.units[0].attack_speed = 0.1f;
    base.player_b.units[0].max_hp = base.player_b.units[0].hp = 5000.0f;

    const auto no_titans = engine.simulate(base);
    tft::CombatItem titans;
    titans.api_name = "TFT_Item_TitansResolve";
    auto with_titans_input = base;
    with_titans_input.player_a.units[0].items.push_back(titans);
    const auto with_titans = engine.simulate(with_titans_input);
    require(no_titans.success && with_titans.success, "Titan's Resolve comparison should simulate.");
    require(with_titans.units.front().damage_dealt > no_titans.units.front().damage_dealt,
            "Titan's Resolve stacks should increase actual damage dealt.");

    // Repeated deterministic battles check that a combined offensive build
    // changes combat output consistently rather than only changing metadata.
    for (std::uint64_t seed = 20261020; seed < 20261028; ++seed) {
        auto baseline = base;
        baseline.seed = seed;
        auto equipped = base;
        equipped.seed = seed;
        equipped.player_a.units[0].items.push_back(titans);
        tft::CombatItem guinsoo;
        guinsoo.api_name = "TFT_Item_GuinsoosRageblade";
        equipped.player_a.units[0].items.push_back(guinsoo);
        const auto before = engine.simulate(baseline);
        const auto after = engine.simulate(equipped);
        require(before.success && after.success,
                "Seeded item outcome comparison must complete successfully.");
        require(after.units.front().damage_dealt > before.units.front().damage_dealt,
                "Combined unique items should improve actual damage across deterministic seeds.");
    }
}

void test_set17_burn_and_shred_change_combat_damage() {
    tft::CombatEngine engine;
    auto base = make_input();
    base.config.max_duration = 3.1f;
    base.player_a.units[0].attack_damage = 10.0f;
    base.player_a.units[0].attack_speed = 1.0f;
    base.player_b.units[0].attack_damage = 0.1f;
    base.player_b.units[0].attack_speed = 0.1f;
    base.player_b.units[0].armor = 100.0f;
    base.player_b.units[0].max_hp = base.player_b.units[0].hp = 5000.0f;

    const auto baseline = engine.simulate(base);
    auto burned_input = base;
    tft::CombatItem morello;
    morello.api_name = "TFT_Item_Morellonomicon";
    burned_input.player_a.units[0].items.push_back(morello);
    const auto burned = engine.simulate(burned_input);
    require(baseline.success && burned.success, "Burn comparison battles should complete.");
    require(burned.units.front().damage_dealt > baseline.units.front().damage_dealt,
            "Morellonomicon burn should increase actual damage dealt over time.");

    auto shredded_input = base;
    tft::CombatItem whisper;
    whisper.api_name = "TFT_Item_LastWhisper";
    shredded_input.player_a.units[0].items.push_back(whisper);
    const auto shredded = engine.simulate(shredded_input);
    require(shredded.success, "Armor shred battle should complete.");
    require(shredded.units.front().damage_dealt > baseline.units.front().damage_dealt,
            "Last Whisper should increase subsequent damage through armor shred.");
}

void test_set17_healing_and_defensive_items_change_survival() {
    tft::CombatEngine engine;
    auto base = make_input();
    base.config.max_duration = 3.1f;
    base.player_a.units[0].attack_damage = 0.1f;
    base.player_a.units[0].attack_speed = 0.1f;
    base.player_a.units[0].max_hp = base.player_a.units[0].hp = 100.0f;
    base.player_b.units[0].attack_damage = 30.0f;
    base.player_b.units[0].attack_speed = 1.0f;
    base.player_b.units[0].max_hp = base.player_b.units[0].hp = 1000.0f;

    const auto baseline = engine.simulate(base);
    auto protected_input = base;
    tft::CombatItem bloodthirster;
    bloodthirster.api_name = "TFT_Item_Bloodthirster";
    protected_input.player_a.units[0].items.push_back(bloodthirster);
    const auto protected_result = engine.simulate(protected_input);
    require(baseline.success && protected_result.success,
            "Defensive item comparison battles should complete.");
    require(protected_result.units.front().final_hp > baseline.units.front().final_hp,
            "Bloodthirster shield should improve survival after its health threshold.");

    auto healing_input = make_input();
    healing_input.config.max_duration = 2.1f;
    healing_input.player_a.units[0].attack_damage = 20.0f;
    healing_input.player_a.units[0].attack_speed = 1.0f;
    healing_input.player_b.units[0].attack_damage = 0.1f;
    healing_input.player_b.units[0].attack_speed = 0.1f;
    healing_input.player_b.units[0].max_hp = healing_input.player_b.units[0].hp = 1000.0f;
    tft::CombatUnit ally;
    ally.id = 2;
    ally.api_name = "test_ally";
    ally.name = "Test Ally";
    ally.team = tft::UnitTeam::PLAYER_A;
    ally.role = tft::UnitRole::SUPPORT;
    ally.position = {4, 1};
    ally.hp = 40.0f;
    ally.max_hp = 100.0f;
    ally.attack_damage = 0.1f;
    ally.attack_speed = 0.1f;
    ally.alive = true;
    healing_input.player_a.units.push_back(ally);
    tft::CombatItem gunblade;
    gunblade.api_name = "TFT_Item_HextechGunblade";
    tft::CombatEffectDefinition ally_healing;
    ally_healing.trigger = "on_damage_dealt";
    ally_healing.operation = "heal_damage_pct_lowest_ally";
    ally_healing.target = "lowest_health_ally";
    ally_healing.value = 0.20f;
    gunblade.effects.push_back(ally_healing);
    healing_input.player_a.units[0].items.push_back(gunblade);
    const auto healed = engine.simulate(healing_input);
    require(healed.success, "Gunblade ally-healing battle should complete.");
    bool ally_healed = false;
    for (const auto& unit : healed.units)
        if (unit.unit_id == 2 && unit.healing_done > 0.0f) ally_healed = true;
    require(ally_healed, "Hextech Gunblade should heal the lowest-health ally from damage dealt.");
}

void test_set17_ionic_spark_and_emblem_passives() {
    tft::CombatEngine engine;
    auto spark_input = make_input();
    spark_input.config.max_duration = 0.1f;
    spark_input.config.record_damage = true;
    spark_input.player_a.units[0].can_attack = false;
    spark_input.player_a.units[0].can_cast = false;
    spark_input.player_a.units[0].max_hp = spark_input.player_a.units[0].hp = 1000.0f;
    spark_input.player_b.units[0].can_attack = false;
    spark_input.player_b.units[0].attack_damage = 0.1f;
    spark_input.player_b.units[0].mana = 100.0f;
    spark_input.player_b.units[0].max_mana = 100.0f;
    spark_input.player_b.units[0].ability.api_name = "ionic_trigger_test";
    spark_input.player_b.units[0].ability.mana_cost = 100.0f;
    spark_input.player_b.units[0].ability.base_damage = 1.0f;
    spark_input.player_b.units[0].ability.has_damage = true;
    spark_input.player_b.units[0].ability.target_type = tft::AbilityTargetType::ENEMY;
    tft::CombatItem ionic;
    ionic.api_name = "TFT_Item_IonicSpark";
    spark_input.player_a.units[0].items.push_back(ionic);
    const auto spark = engine.simulate(spark_input);
    require(spark.success, "Ionic Spark trigger battle should complete.");
    bool saw_spark = false;
    for (const auto& event : spark.damage_events)
        if (event.source_unit_id == spark_input.player_a.units[0].id &&
            event.target_unit_id == spark_input.player_b.units[0].id &&
            std::abs(event.raw_damage - 150.0f) < 0.001f) saw_spark = true;
    require(saw_spark, "Ionic Spark should damage a nearby enemy when it casts.");

    auto tank_input = make_input();
    tank_input.config.max_duration = 0.1f;
    tank_input.config.record_damage = true;
    tank_input.player_a.units[0].attack_damage = 10.0f;
    tank_input.player_a.units[0].max_hp = tank_input.player_a.units[0].hp = 1000.0f;
    tank_input.player_b.units[0].max_hp = tank_input.player_b.units[0].hp = 2000.0f;
    tank_input.player_b.units[0].magic_resist = 0.0f;
    tank_input.player_b.units[0].attack_damage = 0.1f;
    tft::CombatItem fighter_emblem;
    fighter_emblem.api_name = "an_item_name_not_known_to_the_engine";
    fighter_emblem.grants_trait = "TFT17_HPTank";
    tft::CombatEffectDefinition brawler_damage;
    brawler_damage.trigger = "on_attack";
    brawler_damage.operation = "bonus_damage";
    brawler_damage.damage_type = tft::DamageType::MAGIC;
    brawler_damage.value = 0.03f;
    brawler_damage.percent_of_max_health = true;
    fighter_emblem.effects.push_back(brawler_damage);
    tank_input.player_a.units[0].items.push_back(fighter_emblem);
    const auto emblem = engine.simulate(tank_input);
    require(emblem.success, "Fighter emblem combat should complete.");
    bool saw_magic_bonus = false;
    for (const auto& event : emblem.damage_events)
        if (event.source_unit_id == tank_input.player_a.units[0].id &&
            event.target_unit_id == tank_input.player_b.units[0].id &&
            event.damage_type == tft::DamageType::MAGIC &&
            std::abs(event.raw_damage - 30.0f) < 0.001f) saw_magic_bonus = true;
    require(saw_magic_bonus, "Fighter emblem should add magic damage based on max health.");
}

void test_data_driven_trait_emblem_effects() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 0.5f;
    input.config.record_damage = true;
    input.player_a.units[0].hp = input.player_a.units[0].max_hp = 1000.0f;
    input.player_a.units[0].attack_damage = 10.0f;
    input.player_a.units[0].attack_speed = 10.0f;
    input.player_b.units[0].hp = input.player_b.units[0].max_hp = 5000.0f;
    input.player_b.units[0].armor = 0.0f;
    input.player_b.units[0].attack_damage = 0.1f;

    tft::CombatItem emblem;
    emblem.api_name = "an_item_name_not_known_to_the_engine";
    emblem.grants_trait = "TFT17_TestTrait";
    emblem.granted_trait_active_count = 1;

    tft::CombatEffectDefinition start_bonus;
    start_bonus.trigger = "combat_start";
    start_bonus.operation = "add_stat";
    start_bonus.stat = "attack_damage";
    start_bonus.value = 5.0f;
    emblem.effects.push_back(start_bonus);

    tft::CombatEffectDefinition trait_attack_bonus;
    trait_attack_bonus.trigger = "on_attack";
    trait_attack_bonus.operation = "bonus_damage";
    trait_attack_bonus.damage_type = tft::DamageType::PHYSICAL;
    trait_attack_bonus.value = 0.01f;
    trait_attack_bonus.percent_of_max_health = true;
    trait_attack_bonus.condition = "has_trait";
    trait_attack_bonus.condition_trait = "TFT17_TestTrait";
    emblem.effects.push_back(trait_attack_bonus);
    input.player_a.units[0].items.push_back(emblem);

    const auto result = engine.simulate(input);
    require(result.success, "Data-driven trait emblem combat should complete.");
    bool saw_data_driven_damage = false;
    for (const auto& event : result.damage_events) {
        if (event.source_unit_id == input.player_a.units[0].id &&
            event.target_unit_id == input.player_b.units[0].id &&
            std::abs(event.raw_damage - 25.0f) < 0.001f) {
            saw_data_driven_damage = true;
            break;
        }
    }
    require(saw_data_driven_damage,
        "Trait grant and item effects should work without an item API-name branch.");

    auto aura_input = make_input();
    aura_input.config.max_duration = 0.1f;
    aura_input.config.record_damage = true;
    aura_input.player_a.units[0].role = tft::UnitRole::FIGHTER;
    aura_input.player_a.units[0].position.x = 1;
    aura_input.player_a.units[0].attack_damage = 0.1f;
    aura_input.player_a.units[0].attack_speed = 0.1f;
    aura_input.player_a.units[0].hp = aura_input.player_a.units[0].max_hp = 1000.0f;
    auto tank_ally = aura_input.player_a.units[0];
    tank_ally.id = 77;
    tank_ally.role = tft::UnitRole::TANK;
    tank_ally.position.x = 0;
    tank_ally.armor = 0.0f;
    tank_ally.items.clear();
    aura_input.player_a.units.push_back(tank_ally);
    aura_input.player_b.units[0].position.x = 0;
    aura_input.player_b.units[0].attack_damage = 100.0f;
    aura_input.player_b.units[0].attack_speed = 10.0f;
    aura_input.player_b.units[0].hp = aura_input.player_b.units[0].max_hp = 1000.0f;

    tft::CombatItem role_aura;
    role_aura.api_name = "unknown_voyager_emblem";
    role_aura.grants_trait = "TFT17_FlexTrait";
    tft::CombatEffectDefinition tank_resists;
    tank_resists.trigger = "combat_start";
    tank_resists.operation = "add_stat";
    tank_resists.stat = "armor";
    tank_resists.target = "allies_same_row_within_1";
    tank_resists.condition = "role_tank";
    tank_resists.value = 10.0f;
    role_aura.effects.push_back(tank_resists);
    aura_input.player_a.units[0].items.push_back(role_aura);

    const auto aura_result = engine.simulate(aura_input);
    require(aura_result.success, "Data-driven team aura combat should complete.");
    bool saw_armor_mitigated_hit = false;
    for (const auto& event : aura_result.damage_events) {
        if (event.source_unit_id == aura_input.player_b.units[0].id &&
            event.target_unit_id == tank_ally.id &&
            std::abs(event.final_damage - (100.0f * 100.0f / 110.0f)) < 0.05f) {
            saw_armor_mitigated_hit = true;
            break;
        }
    }
    require(saw_armor_mitigated_hit,
        "Generic role-conditioned aura should apply to same-row allies at combat start.");

    // N.O.V.A.'s capstone is data-driven: the team effect only activates when
    // the source unit sees the required team trait count, and its true-damage
    // bonus is inherited by allies rather than staying on the emblem carrier.
    auto capstone_input = make_input();
    capstone_input.config.max_duration = 0.5f;
    capstone_input.config.record_damage = true;
    auto& capstone_source = capstone_input.player_a.units[0];
    capstone_source.attack_damage = 10.0f;
    capstone_source.attack_speed = 10.0f;
    capstone_source.hp = capstone_source.max_hp = 1000.0f;
    tft::CombatTrait nova_trait;
    nova_trait.api_name = "TFT17_DRX";
    nova_trait.active = true;
    nova_trait.active_count = 5;
    capstone_source.traits.push_back(nova_trait);
    capstone_source.items.clear();
    tft::CombatItem nova_emblem;
    nova_emblem.api_name = "unrecognized_nova_emblem";
    nova_emblem.grants_trait = "TFT17_DRX";
    // Exercise the actual emblem grant path for the capstone threshold too.
    nova_emblem.granted_trait_active_count = 5;
    tft::CombatEffectDefinition nova_capstone;
    nova_capstone.trigger = "on_attack";
    nova_capstone.operation = "bonus_damage";
    nova_capstone.target = "allies";
    nova_capstone.condition = "trait_count_at_least";
    nova_capstone.condition_trait = "TFT17_DRX";
    nova_capstone.min_trait_count = 5;
    nova_capstone.damage_type = tft::DamageType::TRUE_DAMAGE;
    nova_capstone.value = 0.10f;
    nova_capstone.percent_of_stat = true;
    nova_capstone.stat = "attack_damage";
    nova_emblem.effects.push_back(nova_capstone);
    capstone_source.items.push_back(nova_emblem);
    capstone_input.player_b.units[0].attack_damage = 0.1f;
    capstone_input.player_b.units[0].attack_speed = 10.0f;
    capstone_input.player_b.units[0].hp = capstone_input.player_b.units[0].max_hp = 5000.0f;

    const auto capstone_result = engine.simulate(capstone_input);
    require(capstone_result.success, "Trait-count-gated capstone combat should complete.");
    bool saw_capstone_true_damage = false;
    for (const auto& event : capstone_result.damage_events) {
        if (event.source_unit_id == capstone_source.id &&
            event.damage_type == tft::DamageType::TRUE_DAMAGE &&
            std::abs(event.raw_damage - 1.0f) < 0.001f) {
            saw_capstone_true_damage = true;
            break;
        }
    }
    require(saw_capstone_true_damage,
        "A trait-count-gated team aura should grant the generic true-damage effect.");
}

void test_component_to_craft_to_equipment_to_combat_cycle() {
    tft::CombatEngine combat;
    auto baseline_input = make_input();
    baseline_input.config.max_duration = 0.1f;
    baseline_input.config.record_damage = true;
    baseline_input.player_a.units[0].attack_damage = 10.0f;
    baseline_input.player_a.units[0].attack_speed = 1.0f;
    baseline_input.player_b.units[0].attack_damage = 0.1f;
    baseline_input.player_b.units[0].attack_speed = 0.1f;
    baseline_input.player_b.units[0].armor = 0.0f;
    baseline_input.player_b.units[0].hp = baseline_input.player_b.units[0].max_hp = 5000.0f;

    const auto baseline = combat.simulate(baseline_input);
    require(baseline.success && !baseline.damage_events.empty(),
            "Baseline for the item lifecycle integration test must run.");

    tft::items::ItemDefinition definition;
    definition.id = "cycle_blade";
    definition.name = "Cycle Blade";
    definition.recipe_components = {"component_sword", "component_bow"};
    definition.attack_damage = 15.0;
    tft::CombatEffectDefinition passive;
    passive.trigger = "combat_start";
    passive.operation = "add_stat";
    passive.stat = "attack_damage";
    passive.target = "self";
    passive.value = 0.20f;
    passive.percent_of_stat = true;
    definition.combat_effects.push_back(passive);

    tft::items::ItemEngine item_engine(
        {definition}, {"component_sword", "component_bow"});
    require(item_engine.add_component("component_sword") &&
            item_engine.add_component("component_bow"),
            "Acquired components must enter the item inventory.");
    const auto crafted = item_engine.craft("component_sword", "component_bow");
    require(crafted && *crafted == "cycle_blade",
            "The component recipe must produce the expected finished item.");

    tft::items::UnitProfile target{
        "cycle-carry-uuid", 1, 1, false, true,
        10.0, 1.0, 0.0, 100.0, 0.0, 0.0, 1.0
    };
    tft::items::ItemActionCommand equip;
    equip.operation = tft::items::ItemOperation::EQUIP_FROM_INVENTORY;
    equip.item_id = *crafted;
    equip.target_unit_uuid = target.uuid;
    const auto equipped = item_engine.apply_action(equip, {target});
    require(equipped.success && item_engine.inventory().empty() &&
            item_engine.equipped(target.uuid).size() == 1,
            "The crafted item must move from inventory to the selected unit UUID.");

    const auto* equipped_definition = item_engine.find(item_engine.equipped(target.uuid).front());
    require(equipped_definition != nullptr,
            "Equipped item ID must resolve to its catalog definition.");
    auto combat_input = baseline_input;
    combat_input.player_a.units[0].items.push_back(
        tft::items::to_combat_item(*equipped_definition));
    const auto with_item = combat.simulate(combat_input);
    require(with_item.success && !with_item.damage_events.empty(),
            "The equipped catalog item must reach the combat simulator.");
    require(with_item.damage_events.front().raw_damage >
                baseline.damage_events.front().raw_damage,
            "Numeric stats and the generic passive must change actual combat damage.");
}

void test_generic_source_ad_effect_changes_combat() {
    tft::CombatEngine engine;
    auto baseline_input = make_input();
    baseline_input.config.max_duration = 0.5f;
    baseline_input.config.record_damage = true;
    baseline_input.player_a.units[0].attack_damage = 10.0f;
    baseline_input.player_a.units[0].attack_speed = 10.0f;
    baseline_input.player_b.units[0].armor = 0.0f;
    baseline_input.player_b.units[0].max_hp = baseline_input.player_b.units[0].hp = 5000.0f;

    const auto baseline = engine.simulate(baseline_input);
    auto item_input = baseline_input;
    tft::CombatItem item;
    item.api_name = "TFT_Item_GenericSourceAD";
    tft::CombatEffectDefinition source_ad;
    source_ad.trigger = "combat_start";
    source_ad.operation = "add_stat";
    source_ad.stat = "attack_damage";
    source_ad.target = "self";
    source_ad.value = 0.55f;
    source_ad.percent_of_stat = true;
    item.effects.push_back(source_ad);
    item_input.player_a.units[0].items.push_back(item);

    const auto with_item = engine.simulate(item_input);
    require(baseline.success && with_item.success,
            "Generic source-derived AD effect should simulate.");
    require(with_item.units.front().damage_dealt > baseline.units.front().damage_dealt,
            "Normalized percentage AD effect must change actual combat damage.");
}


void test_movement_distance_handles_board_edges_and_preserves_input() {
    tft::CombatEngine engine;
    auto input = make_input();
    input.config.max_duration = 2.0f;
    input.config.record_positions = true;

    auto& mover = input.player_a.units.front();
    mover.position = {0, 1};
    mover.attack_range = 1.0f;
    mover.can_attack = false;
    mover.can_cast = false;
    mover.can_move = true;

    auto& target = input.player_b.units.front();
    target.position = {3, 1};
    target.can_attack = false;
    target.can_cast = false;
    target.can_move = false;

    const auto original_mover = mover;
    const auto original_target = target;
    const auto result = engine.simulate(input);

    require(result.success && result.completed,
            "Movement edge fixture must complete.");
    require(result.position_events.size() >= 2,
            "Mover should advance along the only improving in-bounds route.");

    int expected_x = 0;
    for (const auto& event : result.position_events) {
        require(event.unit_id == mover.id,
                "Only the configured mover should produce position events.");
        require(event.to_x >= 0 && event.to_x < input.config.board_cols &&
                event.to_y >= 0 && event.to_y < input.config.board_rows,
                "Movement must never select a position outside the board.");
        require(std::abs(event.to_x - event.from_x) +
                std::abs(event.to_y - event.from_y) == 1,
                "Movement must remain orthogonal by exactly one cell.");
        require(event.from_y == 1 && event.to_y == 1 &&
                event.from_x == expected_x &&
                event.to_x == expected_x + 1,
                "Edge movement must follow the deterministic in-bounds route.");
        expected_x = event.to_x;
    }
    require(expected_x == 2,
            "Mover should stop within attack range before the occupied target cell.");

    require(mover.position.x == original_mover.position.x &&
            mover.position.y == original_mover.position.y &&
            mover.hp == original_mover.hp &&
            mover.items.size() == original_mover.items.size() &&
            mover.traits.size() == original_mover.traits.size(),
            "Simulation must not mutate the caller's mover input.");
    require(target.position.x == original_target.position.x &&
            target.position.y == original_target.position.y &&
            target.hp == original_target.hp,
            "Simulation must not mutate the caller's target input.");
}

void test_detailed_events_are_optional_without_changing_combat_outcome() {
    tft::CombatEngine engine;
    auto detailed_input = make_input();
    detailed_input.config.max_duration = 2.0f;
    detailed_input.config.deterministic = true;
    detailed_input.config.seed = 987654;
    detailed_input.config.record_damage = true;
    detailed_input.config.record_events = true;

    const auto detailed = engine.simulate(detailed_input);
    require(detailed.success && detailed.completed,
            "Detailed combat fixture must complete.");

    auto training_input = detailed_input;
    training_input.config.record_damage = false;
    training_input.config.record_events = false;
    const auto training = engine.simulate(training_input);
    require(training.success && training.completed,
            "Training combat fixture must complete.");

    require(training.winner == detailed.winner &&
            training.duration == detailed.duration &&
            training.player_a_survivors == detailed.player_a_survivors &&
            training.player_b_survivors == detailed.player_b_survivors &&
            training.player_a_damage == detailed.player_a_damage &&
            training.player_b_damage == detailed.player_b_damage &&
            training.units.size() == detailed.units.size(),
            "Disabling detailed events must preserve the combat outcome.");

    for (std::size_t i = 0; i < detailed.units.size(); ++i) {
        const auto& expected = detailed.units[i];
        const auto& actual = training.units[i];
        require(actual.unit_id == expected.unit_id &&
                actual.team == expected.team &&
                actual.survived == expected.survived &&
                actual.initial_hp == expected.initial_hp &&
                actual.final_hp == expected.final_hp &&
                actual.damage_dealt == expected.damage_dealt &&
                actual.damage_taken == expected.damage_taken &&
                actual.healing_done == expected.healing_done &&
                actual.kills == expected.kills &&
                actual.attacks == expected.attacks &&
                actual.ability_casts == expected.ability_casts,
                "Disabling detailed events must preserve per-unit aggregate evidence.");
    }

    require(training.damage_events.empty() && training.attack_events.empty() &&
            training.death_events.empty() && training.events.empty(),
            "Training mode must not retain detailed event collections.");
    require(!detailed.damage_events.empty() || !detailed.attack_events.empty() ||
            !detailed.death_events.empty() || !detailed.events.empty(),
            "Audit mode must continue to expose detailed event collections.");
}

} // namespace

int main() {
    try {
        test_deterministic_winner_and_damage();
        test_defender_team_aura_and_tier_bonus_apply_once();
        test_generic_periodic_stat_effect();
        test_generic_periodic_heal_effect();
        test_generic_periodic_missing_health_heal_effect();
        test_generic_mana_gain_multiplier_effect();
        test_riftbeast_periodic_stat_growth_effect();
        test_generic_trait_critical_chance_effect();
        test_generic_mana_on_attack_item_effects();
        test_trait_team_mana_regeneration_is_applied_once();
        test_generic_role_condition_item_effect();
        test_generic_while_hp_above_effect_reverses_at_threshold();
        test_generic_damage_amplification_item_effect();
        test_generic_percent_max_health_item_effect();
        test_trait_team_effect_scaling_applies_once();
        test_event_limit_is_reported_as_timeout();
        test_invalid_configuration_returns_error();
        test_equipped_items_change_combat_stats();
        test_invalid_equipment_is_rejected();
        test_ability_cast_uses_mana_and_ability_power();
        test_item_mana_can_enable_an_early_cast();
        test_unique_item_effects_and_combinations();
        test_shojin_changes_cast_timing_and_dragons_claw_heals();
        test_titans_resolve_and_seeded_item_impact();
        test_set17_burn_and_shred_change_combat_damage();
        test_set17_healing_and_defensive_items_change_survival();
        test_set17_ionic_spark_and_emblem_passives();
        test_data_driven_trait_emblem_effects();
        test_component_to_craft_to_equipment_to_combat_cycle();
        test_generic_source_ad_effect_changes_combat();
        test_movement_distance_handles_board_edges_and_preserves_input();
        test_detailed_events_are_optional_without_changing_combat_outcome();
    } catch (const std::exception& error) {
        std::cerr << "test_combat_engine: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
