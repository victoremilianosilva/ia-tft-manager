from pathlib import Path


def test_player_action_reward_path_is_independent_of_strategy_id():
    source = (Path(__file__).resolve().parents[1] / "cpp" / "src" / "lobby" / "TftEngine.cpp").read_text(encoding="utf-8")
    start_marker = "// Alinhado a RewardManager.calculate_action_reward()"
    end_marker = "// MiniTFTEnv.step() returns the action-specific reward directly."
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    reward_path = source[start:end]

    forbidden = (
        "strategy_id",
        "this->strategy",
        "strategy_action_reward(",
        "xp_strategy_reward_scale(",
        "critical_all_in_sale_penalty(",
        "phase_xp_progress_reward(",
        "surplus_xp_spending_reward(",
        "xp_progress_reward(",
        "phase_xp_opportunity_available(",
    )
    present = [token for token in forbidden if token in reward_path]
    assert not present, (
        "The runtime action reward path must use observed outcomes and state "
        f"transitions, not nominal strategy IDs; found: {present}"
    )


def test_reward_path_keeps_factual_economic_and_outcome_signals():
    source = (Path(__file__).resolve().parents[1] / "cpp" / "src" / "lobby" / "TftEngine.cpp").read_text(encoding="utf-8")
    start = source.index("// Alinhado a RewardManager.calculate_action_reward()")
    end = source.index(
        "// MiniTFTEnv.step() returns the action-specific reward directly.",
        start,
    )
    reward_path = source[start:end]

    required = (
        "reroll_quality_reward(",
        "xp_level_transition_value(",
        "sale_quality(",
        "pass_opportunity_penalty(",
        "gold_change_reward(",
        "movement_sequence_reward(",
    )
    missing = [token for token in required if token not in reward_path]
    assert not missing, (
        "Removing strategy labels must not remove independently observed "
        f"outcome/economy signals; missing: {missing}"
    )
