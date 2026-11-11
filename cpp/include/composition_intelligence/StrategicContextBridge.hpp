#pragma once
#include "composition_intelligence/contracts/CompositionContracts.hpp"
#include "strategy/StrategicPlanning.hpp"
#include <cstdint>
#include <optional>
#include <string>
#include <utility>
#include <vector>
#include <nlohmann/json.hpp>

namespace tft::composition_intelligence {
enum class ContextBridgeQuality { Valid, Partial, Missing, Stale, Incompatible };
enum class ContextValueOrigin { Observed, Derived, Recommended };
inline const char* context_bridge_quality_name(ContextBridgeQuality v) noexcept {
    switch(v){case ContextBridgeQuality::Valid:return "valid";case ContextBridgeQuality::Partial:return "partial";case ContextBridgeQuality::Missing:return "missing";case ContextBridgeQuality::Stale:return "stale";case ContextBridgeQuality::Incompatible:return "incompatible";} return "missing";
}
inline const char* context_value_origin_name(ContextValueOrigin v) noexcept {
    switch(v){case ContextValueOrigin::Observed:return "observed";case ContextValueOrigin::Derived:return "derived";case ContextValueOrigin::Recommended:return "recommended";} return "observed";
}
template<class T> struct ContextBridgeValue {
    std::optional<T> value;
    ContextValueOrigin origin{ContextValueOrigin::Observed};
    ContextBridgeQuality quality{ContextBridgeQuality::Missing};
    std::string source;
    std::string reason{"not_provided"};
    bool available() const noexcept{return value.has_value();}
};
struct ContextBridgeMetadata {
    std::uint32_t schema_version{1}; std::uint64_t match_id{0};
    std::int32_t player_id{-1}; std::uint32_t round{0};
    std::uint64_t timestamp_unix_ms{0},sequence{0};
    std::string composition_id; std::uint64_t composition_version{0};
    ContextBridgeQuality quality{ContextBridgeQuality::Missing};
    std::string reason{"not_evaluated"};
};
struct StrategicContextBridgeSnapshot {
    ContextBridgeMetadata metadata;
    ContextBridgeValue<double> hp,board_power,relative_board_power,direction_score,strategic_confidence,economic_confidence;
    ContextBridgeValue<std::int32_t> gold,level,xp,xp_to_next,win_streak,loss_streak;
    ContextBridgeValue<bool> composition_locked,direction_viable;
    ContextBridgeValue<std::string> observed_direction,observed_focus,progression_plan,recommended_direction,composition_decision,economic_posture;
    ContextBridgeValue<std::vector<std::string>> core_traits;
    ContextBridgeValue<std::uint32_t> stage;
    nlohmann::json to_json() const {
        const auto field=[](const auto& v){nlohmann::json j={{"origin",context_value_origin_name(v.origin)},{"quality",context_bridge_quality_name(v.quality)},{"source",v.source},{"reason",v.reason}};j["value"]=v.value?nlohmann::json(*v.value):nlohmann::json(nullptr);return j;};
        return {
          {"metadata",{{"schema_version",metadata.schema_version},{"match_id",metadata.match_id},{"player_id",metadata.player_id},{"round",metadata.round},{"timestamp_unix_ms",metadata.timestamp_unix_ms},{"sequence",metadata.sequence},{"composition_id",metadata.composition_id},{"composition_version",metadata.composition_version},{"quality",context_bridge_quality_name(metadata.quality)},{"reason",metadata.reason}}},
          {"observed",{{"hp",field(hp)},{"gold",field(gold)},{"level",field(level)},{"xp",field(xp)},{"xp_to_next",field(xp_to_next)},{"win_streak",field(win_streak)},{"loss_streak",field(loss_streak)},{"composition_locked",field(composition_locked)},{"direction",field(observed_direction)},{"focus",field(observed_focus)},{"core_traits",field(core_traits)}}},
          {"derived",{{"board_power",field(board_power)},{"relative_board_power",field(relative_board_power)},{"direction_score",field(direction_score)},{"direction_viable",field(direction_viable)},{"stage",field(stage)},{"progression_plan",field(progression_plan)}}},
          {"recommended",{{"direction",field(recommended_direction)},{"composition_decision",field(composition_decision)},{"economic_posture",field(economic_posture)},{"strategic_confidence",field(strategic_confidence)},{"economic_confidence",field(economic_confidence)}}}
        };
    }
};
struct ContextBridgeInput {
    const strategy::StrategicSharedContext* strategic{nullptr};
    const strategy::StrategicPlanDecision* strategic_decision{nullptr};
    const strategy::EconomicControlDecision* economic_decision{nullptr};
    const std::optional<ActiveComposition>* active_composition{nullptr};
    std::uint64_t match_id{0}; std::int32_t expected_player_id{-1};
    std::uint32_t expected_round{0}; std::uint64_t timestamp_unix_ms{0},sequence{0};
};
class StrategicContextBridge {
public:
    static StrategicContextBridgeSnapshot adapt(const ContextBridgeInput& in) {
        StrategicContextBridgeSnapshot out; auto& m=out.metadata;
        m.match_id=in.match_id;m.player_id=in.expected_player_id;m.round=in.expected_round;
        m.timestamp_unix_ms=in.timestamp_unix_ms;m.sequence=in.sequence;
        if(!in.strategic||!in.strategic_decision||!in.economic_decision){m.quality=ContextBridgeQuality::Missing;m.reason="required_strategic_or_economic_source_missing";return out;}
        const auto& c=*in.strategic;
        if(c.player_id!=in.expected_player_id){m.quality=ContextBridgeQuality::Incompatible;m.reason="player_id_mismatch";return out;}
        if(c.round!=in.expected_round){m.quality=ContextBridgeQuality::Stale;m.reason="round_mismatch";return out;}
        const bool active=in.active_composition&&in.active_composition->has_value();
        if(active){const auto& a=**in.active_composition;m.composition_id=a.candidate.composition_id;m.composition_version=a.version;}
        const auto set=[](auto& dst,auto value,ContextValueOrigin origin,const char* source,const char* reason){dst.value=std::move(value);dst.origin=origin;dst.quality=ContextBridgeQuality::Valid;dst.source=source;dst.reason=reason;};
        set(out.hp,c.hp,ContextValueOrigin::Observed,"StrategicSharedContext","live_player_state");
        set(out.gold,c.gold,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state");
        set(out.level,c.level,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state");
        set(out.xp,c.xp,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state");
        set(out.xp_to_next,c.xp_to_next,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state");
        set(out.win_streak,c.win_streak,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state");
        set(out.loss_streak,c.loss_streak,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state");
        set(out.composition_locked,c.composition_locked,ContextValueOrigin::Observed,"StrategicSharedContext","live_composition_state");
        set(out.observed_direction,c.current_composition_direction,ContextValueOrigin::Observed,"StrategicSharedContext","live_composition_state");
        set(out.observed_focus,c.current_composition_focus,ContextValueOrigin::Observed,"StrategicSharedContext","live_composition_state");
        set(out.core_traits,c.current_core_traits,ContextValueOrigin::Observed,"StrategicSharedContext","live_composition_state");
        set(out.stage,c.stage,ContextValueOrigin::Derived,"StrategicSharedContext","round_stage_mapping");
        set(out.progression_plan,progression_name(c.progression_plan),ContextValueOrigin::Derived,"StrategicSharedContext","current_economic_strategy_mapping");
        set(out.board_power,c.board_power,ContextValueOrigin::Derived,"StrategicSharedContext","board_power_estimate");
        set(out.relative_board_power,c.relative_board_power,ContextValueOrigin::Derived,"StrategicSharedContext","relative_to_lobby_average");
        set(out.direction_score,c.current_direction_score,ContextValueOrigin::Derived,"StrategicSharedContext","planner_direction_score");
        set(out.direction_viable,c.current_direction_viable,ContextValueOrigin::Derived,"StrategicSharedContext","planner_viability_assessment");
        set(out.recommended_direction,in.strategic_decision->target_composition_direction,ContextValueOrigin::Recommended,"StrategicPlanner","shadow_recommendation_only");
        set(out.composition_decision,decision_name(in.strategic_decision->composition_decision),ContextValueOrigin::Recommended,"StrategicPlanner","shadow_recommendation_only");
        set(out.economic_posture,posture_name(in.economic_decision->posture),ContextValueOrigin::Recommended,"EconomicController","shadow_recommendation_only");
        set(out.strategic_confidence,in.strategic_decision->confidence,ContextValueOrigin::Recommended,"StrategicPlanner","uncalibrated_score_confidence");
        set(out.economic_confidence,in.economic_decision->confidence,ContextValueOrigin::Recommended,"EconomicController","uncalibrated_score_confidence");
        m.quality=active?ContextBridgeQuality::Valid:ContextBridgeQuality::Partial;
        m.reason=active?"validated_player_round_and_composition_identity":"player_round_valid_but_no_active_composition";
        if(!active){out.recommended_direction.quality=ContextBridgeQuality::Partial;out.recommended_direction.reason="no_active_composition_identity";out.composition_decision.quality=ContextBridgeQuality::Partial;out.composition_decision.reason="no_active_composition_identity";}
        return out;
    }
private:
    static const char* progression_name(strategy::ProgressionPlan v) noexcept {
        switch(v){case strategy::ProgressionPlan::Flexible:return "FLEXIBLE";case strategy::ProgressionPlan::StandardLeveling:return "STANDARD_LEVELING";case strategy::ProgressionPlan::LevelToEight:return "LEVEL_TO_EIGHT";case strategy::ProgressionPlan::LevelToNine:return "LEVEL_TO_NINE";case strategy::ProgressionPlan::RerollForThreeStar:return "REROLL_FOR_THREE_STAR";}return "UNKNOWN";
    }
    static const char* decision_name(strategy::CompositionDecision v) noexcept {
        switch(v){case strategy::CompositionDecision::Keep:return "KEEP";case strategy::CompositionDecision::Adapt:return "ADAPT";case strategy::CompositionDecision::Pivot:return "PIVOT";case strategy::CompositionDecision::Abandon:return "ABANDON";case strategy::CompositionDecision::InitialSelection:return "INITIAL_SELECTION";case strategy::CompositionDecision::InsufficientEvidence:return "INSUFFICIENT_EVIDENCE";}return "UNKNOWN";
    }
    static const char* posture_name(strategy::EconomicPosture v) noexcept {
        switch(v){case strategy::EconomicPosture::AccumulateResources:return "ACCUMULATE_RESOURCES";case strategy::EconomicPosture::PreserveWinStreak:return "PRESERVE_WIN_STREAK";case strategy::EconomicPosture::PreserveLossStreak:return "PRESERVE_LOSS_STREAK";case strategy::EconomicPosture::InvestExperience:return "INVEST_EXPERIENCE";case strategy::EconomicPosture::RollForUpgrades:return "ROLL_FOR_UPGRADES";case strategy::EconomicPosture::StabilizeBoard:return "STABILIZE_BOARD";case strategy::EconomicPosture::EmergencyInvestment:return "EMERGENCY_INVESTMENT";}return "UNKNOWN";
    }
};
} // namespace tft::composition_intelligence
