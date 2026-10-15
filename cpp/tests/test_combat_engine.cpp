#include "CombatEngine.hpp"

#include <cmath>
#include <iostream>
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

} // namespace

int main() {
    try {
        test_deterministic_winner_and_damage();
        test_invalid_configuration_returns_error();
    } catch (const std::exception& error) {
        std::cerr << "test_combat_engine: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
