import unittest

from economy_finetuning.scenario_generator import (
    SCENARIOS, decode_observation, matching_scenarios,
)


class ScenarioGeneratorTests(unittest.TestCase):
    EXPECTED_CURRICULUM = (
        "critical_hp_high_gold",
        "late_game_high_gold_underleveled",
        "econ_gold_reserve",
        "econ_surplus_strong_board",
        "stabilize_weak_board",
        "fast8_strong_board",
        "all_in_emergency",
        "slowroll_winstreak",
    )

    def test_catalog_matches_the_current_focused_curriculum(self):
        ids = tuple(item.scenario_id for item in SCENARIOS)
        self.assertEqual(ids, self.EXPECTED_CURRICULUM)
        self.assertTrue(all(item.trainable for item in SCENARIOS))
        self.assertTrue(all(item.reward_mode == "native" for item in SCENARIOS))

    def test_decodes_documented_core_fields(self):
        obs = [0.75, 1.2, 6 / 9, 0, 0, 0, 0.5] + [0.0] * 3 + [0, 0, 1, 0, 0, 0, 0]
        state = decode_observation(obs)
        self.assertAlmostEqual(state["hp"], 75.0)
        self.assertAlmostEqual(state["gold"], 60.0)
        self.assertAlmostEqual(state["level"], 6.0)
        self.assertEqual(state["strategy_name"], "FAST8")

    def test_critical_hp_scenario_matches_only_its_declared_strategy_cohort(self):
        state = {
            "hp": 20, "gold": 90, "level": 6, "stage": 4,
            "round_number": 21, "strategy": 2,
        }
        ids = {item.scenario_id for item in matching_scenarios(state)}
        self.assertIn("critical_hp_high_gold", ids)

    def test_slowroll_winstreak_requires_winstreak_and_level_window(self):
        state = {
            "hp": 80, "gold": 60, "level": 6, "stage": 4,
            "round_number": 19, "strategy": 3, "win_streak": 2,
        }
        ids = {item.scenario_id for item in matching_scenarios(state)}
        self.assertIn("slowroll_winstreak", ids)
        state["win_streak"] = 1
        ids = {item.scenario_id for item in matching_scenarios(state)}
        self.assertNotIn("slowroll_winstreak", ids)

    def test_econ_gold_reserve_is_limited_to_econ_strategy_and_below_50(self):
        state = {
            "hp": 70, "gold": 40, "level": 7, "stage": 4,
            "round_number": 19, "strategy": 0,
        }
        ids = {item.scenario_id for item in matching_scenarios(state)}
        self.assertIn("econ_gold_reserve", ids)
        state["strategy"] = 2
        ids = {item.scenario_id for item in matching_scenarios(state)}
        self.assertNotIn("econ_gold_reserve", ids)


if __name__ == "__main__":
    unittest.main()
