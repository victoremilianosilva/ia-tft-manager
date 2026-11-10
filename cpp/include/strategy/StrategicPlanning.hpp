#pragma once

// Data-only contracts for the strategic/economic planner architecture.
// This header must not change PPO observations, masks, rewards, or execution.

#include <cstdint>
#include <string>
#include <vector>

namespace tft::strategy {

enum class CompositionDecision : std::uint8_t {
    Keep = 0, Adapt = 1, Pivot = 2, Abandon = 3,
    InitialSelection = 4, InsufficientEvidence = 5
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
    None = 0, BuyUnit = 1, BuyExperience = 2, RerollShop = 3,
    SellUnit = 4, DeployOrMove = 5, Hold = 6
};

enum class StrategicReason : std::uint8_t {
    None = 0, BoardAdvantage = 1, BoardDeficit = 2,
    SurvivalPressure = 3, ProgressionTiming = 4,
    UpgradeOpportunity = 5, AnchorOpportunity = 6,
    Contestation = 7, ItemAlignment = 8, TransitionCost = 9,
    EconomyConstraint = 10, InsufficientEvidence = 11
};

// Explicit heuristic opportunity premiums. Reroll is intentionally more
// expensive than XP because it consumes a shop search without guaranteeing
// a unit or advancing level progression.
namespace action_opportunity_cost {
inline constexpr double kBuyExperience = 0.25;
inline constexpr double kRerollWithUpgradeTarget = 3.50;
inline constexpr double kRerollWithoutUpgradeTarget = 4.00;
inline constexpr double kBuyUnit = 0.35;
} // namespace action_opportunity_cost

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
    std::vector<std::string> traits;
};

struct StrategicAnchorCandidate {
    StrategicUnitCandidate unit;
    std::string target_composition_direction;
    double anchor_value{0.0};
    double transition_cost{0.0};
    double contestation{0.0};
    std::int32_t reusable_owned_units{0};
    bool shop_available{false};
};

struct StrategicActionCandidate {
    StrategicActionKind kind{StrategicActionKind::None};
    std::int32_t champion_id{-1};
    std::int32_t gold_cost{0};
    double direct_gold_cost{0.0};
    double lost_interest_cost{0.0};
    double opportunity_cost{0.0};
    double expected_economy_cost{0.0};
    double expected_board_delta{0.0};
    double composition_fit{0.0};
    double upgrade_value{0.0};
    bool available{true};
};

struct ActionCandidateScore {
    StrategicActionKind kind{StrategicActionKind::None};
    std::int32_t champion_id{-1};
    double direct_gold_cost{0.0};
    double lost_interest_cost{0.0};
    double opportunity_cost{0.0};
    double board_component{0.0};
    double survival_component{0.0};
    double streak_component{0.0};
    double composition_component{0.0};
    double upgrade_component{0.0};
    double posture_component{0.0};
    double direct_cost_component{0.0};
    double lost_interest_component{0.0};
    double opportunity_cost_component{0.0};
    double total_score{0.0};
    bool available{true};
    bool selected{false};
};

struct StrategicCandidateGenerationDiagnostics {
    std::uint32_t anchors_considered{0};
    std::uint32_t rejected_cost_below_four{0};
    std::uint32_t rejected_empty_trait{0};
    std::uint32_t rejected_duplicate_direction{0};
    std::uint32_t rejected_direction_limit{0};
    std::uint32_t rejected_empty_plan{0};
    std::uint32_t rejected_anchor_not_in_plan{0};
    std::uint32_t candidates_generated{0};
    std::string no_candidate_reason{"not_evaluated"};
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
    ProgressionPlan progression_plan{ProgressionPlan::Flexible};
    std::int32_t interest_if_resolved_now{0};
    std::int32_t projected_next_round_income{0};
    std::int32_t win_streak{0};
    std::int32_t loss_streak{0};
    double board_power{0.0};
    double lobby_average_board_power{0.0};
    double relative_board_power{0.0};
    double estimated_incoming_damage{0.0};
    double elimination_risk{0.0};
    double current_direction_score{0.0};
    bool current_direction_viable{true};
    std::string current_composition_direction;
    std::string current_composition_focus;
    std::vector<std::string> current_core_traits;
    std::vector<StrategicUnitCandidate> owned_units;
    std::vector<StrategicAnchorCandidate> anchor_candidates;\n    StrategicCandidateGenerationDiagnostics candidate_generation;
    bool composition_locked{false};
    bool alive{true};
    // Candidate actions are diagnostic estimates assembled from native state.
    std::vector<StrategicActionCandidate> action_candidates;
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
    std::string candidate_composition_direction;
    std::int32_t candidate_anchor_id{-1};
    double candidate_score{0.0};
};

struct StrategicCandidateDiagnostic {
    std::int32_t champion_id{-1};
    std::string target_composition_direction;
    double score{0.0};
    bool accepted{false};
    std::string evaluation_reason;
};

struct StrategicPlanDecision {
    CompositionDecision composition_decision{CompositionDecision::InsufficientEvidence};
    ProgressionPlan progression{ProgressionPlan::Flexible};
    EconomicPosture economic_posture{EconomicPosture::AccumulateResources};
    StrategicReason reason{StrategicReason::None};
    std::string target_composition_direction;
    std::vector<std::int32_t> preserve_unit_ids;
    std::vector<std::int32_t> replaceable_unit_ids;
    std::int32_t anchor_champion_id{-1};
    double confidence{0.0};
    double estimated_transition_cost{0.0};
    std::vector<StrategicCandidateDiagnostic> candidate_diagnostics;
    bool shadow_only{true};
};

struct EconomicControlDecision {
    EconomicPosture posture{EconomicPosture::AccumulateResources};
    StrategicReason reason{StrategicReason::InsufficientEvidence};
    double confidence{0.0};
    double survival_pressure{0.0};
    double board_pressure{0.0};
    double economy_pressure{0.0};
    bool shadow_only{true};
};

struct ActionEvaluation {
    StrategicActionKind recommended_action{StrategicActionKind::None};
    std::int32_t recommended_champion_id{-1};
    StrategicReason reason{StrategicReason::None};
    double expected_board_delta{0.0};
    double expected_hp_preservation{0.0};
    double expected_economy_cost{0.0};
    double expected_direct_gold_cost{0.0};
    double expected_lost_interest_cost{0.0};
    double expected_opportunity_cost{0.0};
    double expected_streak_value{0.0};
    double confidence{0.0};
    std::vector<ActionCandidateScore> candidate_scores;
    bool differs_from_policy_action{false};
    bool shadow_only{true};
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
