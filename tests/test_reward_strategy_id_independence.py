from pathlib import Path


def _reward_path():
    source = (
        Path(__file__).resolve().parents[1]
        / "cpp"
        / "src"
        / "lobby"
        / "TftEngine.cpp"
    ).read_text(encoding="utf-8")
    start = source.index("// Reward Contract v1 deliberately")
    end = source.index(
        "// MiniTFTEnv.step() returns the action-specific reward directly.",
        start,
    )
    return source, source[start:end]


def test_action_reward_does_not_consume_legacy_or_shadow_scores():
    _, reward_path = _reward_path()
    forbidden = (
        "StrategyInfo",
        "this->strategy",
        "strategy_id",
        "unit_composition_score",
        "composition_quality_delta",
        "reroll_quality_reward(",
        "sale_quality(",
        "pass_opportunity_penalty(",
        "gold_change_reward(",
        "movement_sequence_reward(",
        "item_assignment_reward",
        "core_displacement_penalty(",
        "xp_level_transition_value(",
        "spending_timing_reward(",
    )
    present = [token for token in forbidden if token in reward_path]
    assert not present, (
        "PPO action rewards must not use legacy composition, Shadow scores, "
        f"or uncalibrated heuristic shaping; found: {present}"
    )


def test_action_reward_is_neutral_but_execution_success_is_still_traced():
    _, reward_path = _reward_path()
    assert "double action_reward = 0.0;" in reward_path
    assert "success = bought_unit_successfully;" in reward_path
    assert "success = economy.gold == old_gold - EconomyEngine::REROLL_COST;" in reward_path
    assert "success = economy.gold == old_gold - EconomyEngine::BUY_XP_COST;" in reward_path
    assert "success = board_layout_changed && !board_capacity_violation" in reward_path
    assert "success = economy.gold > old_gold;" in reward_path


def test_native_combat_and_one_time_terminal_placement_rewards_remain():
    source, _ = _reward_path()
    assert "reward_model::combat(" in source
    assert "placement_reward_given" in source
    assert "const double placement_reward = 1.0 - 2.0 *" in source
