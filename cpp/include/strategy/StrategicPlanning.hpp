#pragma once

// Strategic/economic planning contracts.
// This header is intentionally data-only: it must not change PPO observations,
// action masks, rewards, or the actions executed by the engine.

#include <cstdint>
#include <string>
#include <vector>

namespace tft::strategy {

enum class CompositionDecision : std::uint8_t {
    Keep = 0,
    Adapt = 1,
    Pivot = 2,
    Abandon = 3
};

enum class ProgressionPlan : std::uint8_t {
    Flexible = 0,
    StandardLeveling = 1,
    LevelToEight = 2,
    LevelToNine = 3,
    RerollForThreeStar = 4
};

enum class EconomicPosture : std::uint8_t {
    AccumulateResources = 0,
    PreserveWinStreak = 1,
    PreserveLossStreak = 2,
    InvestExperience = 3,
    RollForUpgrades = 4,
    StabilizeBoard = 5,
    EmergencyInvestment = 6
};

enum class StrategicActionKind : std::uint8_t {
    None = 0,
    BuyUnit = 1,
    BuyExperience = 2,
    RerollShop = 3,
    SellUnit = 4,
    DeployOrMove = 5,
    Hold = 6
};

enum class StrategicReason : std::uint8_t {
    None = 0,
    BoardAdvantage = 1,
    BoardDeficit = 2,
    SurvivalPressure = 3,
    ProgressionTiming = 4,
    UpgradeOpportunity = 5,
    AnchorOpportunity = 6,
    Contestation = 7,
    ItemAlignment = 8,
    TransitionCost = 9,
    EconomyConstraint = 10,
    InsufficientEvidence = 11
};

struct StrategicUnitCandidate {
    std::int32_t champion_id{-1};
    std::string champion_key;
    std::int32_t cost{0};
    std::int32_t star{1};
    std::int32_t copies_owned{0};
    bool on_board{false};
    bool on_bench{false};
    bool is_core{false};
    double board_contribution{0.0};
    double composition_fit{0.0};
    double item_fit{0.0};
};

struct StrategicAnchorCandidate {
    StrategicUnitCandidate unit;
    double anchor_value{0.0};
    double transition_cost{0.0};
    double contestation{0.0};
    std::int32_t reusable_owned_units{0};
    bool shop_available{false};
};

struct StrategicSharedContext {
    std::uint32_t schema_version{1};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint32_t stage{1};

    double hp{100.0};
    std::int32_t gold{0};
    std::int32_t level{1};
    std::int32_t xp{0};
    std::int32_t xp_to_next{0};
    std::int32_t interest_if_resolved_now{0};
    std::int32_t projected_next_round_income{0};
    std::int32_t win_streak{0};
    std::int32_t loss_streak{0};

    double board_power{0.0};
    double lobby_average_board_power{0.0};
    double relative_board_power{0.0};
    double estimated_incoming_damage{0.0};
    double elimination_risk{0.0};

    std::string current_composition_direction;
    std::string current_composition_focus;
    std::vector<std::string> current_core_traits;
    std::vector<StrategicUnitCandidate> owned_units;
    std::vector<StrategicAnchorCandidate> anchor_candidates;

    bool composition_locked{false};
    bool alive{true};
};

struct StrategicCommitment {
    ProgressionPlan progression{ProgressionPlan::Flexible};
    std::string composition_direction;
    std::vector<std::int32_t> core_unit_ids;
    std::vector<std::int32_t> flexible_unit_ids;
    std::uint32_t selected_round{0};
    std::uint32_t last_review_round{0};
    StrategicReason selection_reason{StrategicReason::None};
    StrategicReason revision_condition{StrategicReason::None};
    double confidence{0.0};
    std::uint32_t consecutive_reviews{0};
};

struct StrategicPlanDecision {
    CompositionDecision composition_decision{CompositionDecision::Keep};
    ProgressionPlan progression{ProgressionPlan::Flexible};
    EconomicPosture economic_posture{EconomicPosture::AccumulateResources};
    StrategicReason reason{StrategicReason::None};
    std::string target_composition_direction;
    std::vector<std::int32_t> preserve_unit_ids;
    std::vector<std::int32_t> replaceable_unit_ids;
    std::int32_t anchor_champion_id{-1};
    double confidence{0.0};
    double estimated_transition_cost{0.0};
    bool shadow_only{true};
};

struct ActionEvaluation {
    StrategicActionKind recommended_action{StrategicActionKind::None};
    StrategicReason reason{StrategicReason::None};
    double expected_board_delta{0.0};
    double expected_hp_preservation{0.0};
    double expected_economy_cost{0.0};
    double expected_streak_value{0.0};
    double confidence{0.0};
    bool differs_from_policy_action{false};
};

struct StrategicOutcome {
    std::uint32_t evaluated_round{0};
    double board_power_before{0.0};
    double board_power_after{0.0};
    double hp_before{0.0};
    double hp_after{0.0};
    std::int32_t gold_before{0};
    std::int32_t gold_after{0};
    std::int32_t level_before{0};
    std::int32_t level_after{0};
    std::int32_t upgrades_completed{0};
    std::int32_t streak_before{0};
    std::int32_t streak_after{0};
    bool plan_revised{false};
};

} // namespace tft::strategy
