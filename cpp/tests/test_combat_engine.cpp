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
        test_unique_item_effects_and_combinations();
        test_shojin_changes_cast_timing_and_dragons_claw_heals();
        test_titans_resolve_and_seeded_item_impact();
        test_set17_burn_and_shred_change_combat_damage();
        test_set17_healing_and_defensive_items_change_survival();
        test_set17_ionic_spark_and_emblem_passives();
        test_data_driven_trait_emblem_effects();
        test_generic_source_ad_effect_changes_combat();
    } catch (const std::exception& error) {
        std::cerr << "test_combat_engine: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
