import unittest

from economy_finetuning.scenario_generator import (
    SCENARIOS, decode_observation, matching_scenarios, shaped_action_reward,
)


class ScenarioGeneratorTests(unittest.TestCase):
    def test_catalog_has_all_discussed_economic_cases(self):
        ids = {item.scenario_id for item in SCENARIOS}
        self.assertTrue({
            "s4_fast8_lvl6_gold60_hp_ok",
            "s4_fast8_lvl6_gold80",
            "s4_fast8_lvl7_gold60",
            "late_game_high_gold_underleveled",
            "critical_hp_high_gold",
            "low_hp_fast8_high_gold",
            "slowroll_gold_reserve",
            "all_in_gold_hoarding",
            "player8_all_in_gold_hoarding",
            "gold_above_50_any_strategy",
            "useful_shop_opportunity",
        }.issubset(ids))

    def test_decodes_documented_core_fields(self):
        obs = [0.75, 1.2, 6 / 9, 0, 0, 0, 0.5] + [0.0] * 3 + [0, 0, 1, 0, 0, 0, 0]
        state = decode_observation(obs)
        self.assertAlmostEqual(state["hp"], 75.0)
        self.assertAlmostEqual(state["gold"], 60.0)
        self.assertAlmostEqual(state["level"], 6.0)
        self.assertEqual(state["strategy_name"], "FAST8")

    def test_fast8_high_gold_scenario_matches(self):
        state = {"hp": 70, "gold": 65, "level": 6, "stage": 4, "round_number": 19, "strategy": 2}
        matches = {item.scenario_id for item in matching_scenarios(state)}
        self.assertIn("s4_fast8_lvl6_gold60_hp_ok", matches)

    def test_slowroll_is_not_rewarded_for_xp(self):
        state = {"hp": 80, "gold": 60, "level": 6, "stage": 4, "round_number": 19, "strategy": 3}
        reward, matches = shaped_action_reward(state, 2)
        self.assertIn("slowroll_gold_reserve", matches)
        self.assertLess(reward, 0)

    def test_player_eight_all_in_cohort_is_specific(self):
        base = {"hp": 70, "gold": 70, "level": 7, "stage": 4, "strategy": 4, "player_id": 7}
        ids = {item.scenario_id for item in matching_scenarios(base)}
        self.assertIn("player8_all_in_gold_hoarding", ids)
        base["player_id"] = 6
        ids = {item.scenario_id for item in matching_scenarios(base)}
        self.assertNotIn("player8_all_in_gold_hoarding", ids)

    def test_useful_shop_scenario_is_not_guessed_from_gold_alone(self):
        state = {"hp": 70, "gold": 80, "level": 7, "stage": 4, "strategy": 2}
        ids = {item.scenario_id for item in matching_scenarios(state)}
        self.assertNotIn("useful_shop_opportunity", ids)

    def test_native_reward_scenarios_do_not_add_synthetic_xp_bonus(self):
        state = {
            "hp": 70, "gold": 90, "level": 6, "stage": 4,
            "round_number": 19, "strategy": 2,
        }
        scenario = next(item for item in SCENARIOS if item.scenario_id == "s4_fast8_lvl6_gold60_hp_ok")
        self.assertTrue(scenario.trainable)
        self.assertEqual(scenario.reward_mode, "native")
        reward, matches = shaped_action_reward(
            state, 2, selected_scenario_id="s4_fast8_lvl6_gold60_hp_ok"
        )
        self.assertIn("s4_fast8_lvl6_gold60_hp_ok", matches)
        self.assertEqual(reward, 0.0)

    def test_slowroll_is_the_only_economic_scenario_with_xp_shaping(self):
        state = {
            "hp": 80, "gold": 60, "level": 6, "stage": 4,
            "round_number": 19, "strategy": 3,
        }
        selected, _ = shaped_action_reward(
            state, 2, selected_scenario_id="slowroll_gold_reserve"
        )
        wrong_scenario, _ = shaped_action_reward(
            state, 2, selected_scenario_id="s4_fast8_lvl6_gold60_hp_ok"
        )
        self.assertEqual(selected, -0.055)
        self.assertEqual(wrong_scenario, 0.0)

    def test_critical_hp_fast8_case_stays_monitor_only(self):
        # P4-like: low HP, high gold and level deficit. XP is not assumed to
        # be better than a useful shop purchase or emergency board stabilization.
        state = {
            "hp": 21, "gold": 125, "level": 6, "stage": 4,
            "round_number": 21, "strategy": 2,
        }
        reward, matches = shaped_action_reward(state, 2)
        self.assertIn("low_hp_fast8_high_gold", matches)
        self.assertEqual(reward, 0.0)

    def test_critical_hp_scenario_trains_only_from_native_reward(self):
        scenario = next(item for item in SCENARIOS if item.scenario_id == "critical_hp_high_gold")
        self.assertTrue(scenario.trainable)
        self.assertEqual(scenario.reward_mode, "native")
        state = {"hp": 20, "gold": 90, "level": 6, "stage": 4, "strategy": 2}
        reward, matches = shaped_action_reward(
            state, 2, selected_scenario_id="critical_hp_high_gold"
        )
        self.assertIn("critical_hp_high_gold", matches)
        self.assertEqual(reward, 0.0)
        slowroll_state = dict(state, strategy=3)
        slowroll_reward, slowroll_matches = shaped_action_reward(
            slowroll_state, 2, selected_scenario_id="critical_hp_high_gold"
        )
        self.assertIn("critical_hp_high_gold", slowroll_matches)
        self.assertEqual(slowroll_reward, 0.0)


if __name__ == "__main__":
    unittest.main()
