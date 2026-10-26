#include "CombatEngine.hpp"

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

} // namespace

int main() {
    try {
        test_deterministic_winner_and_damage();
        test_event_limit_is_reported_as_timeout();
        test_invalid_configuration_returns_error();
        test_equipped_items_change_combat_stats();
        test_invalid_equipment_is_rejected();
        test_ability_cast_uses_mana_and_ability_power();
        test_item_mana_can_enable_an_early_cast();
    } catch (const std::exception& error) {
        std::cerr << "test_combat_engine: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
