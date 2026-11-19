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
    std::uint32_t schema_version{3};
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
          {"metadata",{{"schema_version",metadata.schema_version},{"quality",context_bridge_quality_name(metadata.quality)},{"reason",metadata.reason}}},
          {"observed",{{"hp",field(hp)},{"gold",field(gold)},{"level",field(level)},{"xp",field(xp)},{"xp_to_next",field(xp_to_next)},{"win_streak",field(win_streak)},{"loss_streak",field(loss_streak)}}},
          {"derived",{{"board_power",field(board_power)},{"relative_board_power",field(relative_board_power)},{"direction_score",field(direction_score)},{"direction_viable",field(direction_viable)},{"stage",field(stage)},{"progression_plan",field(progression_plan)},{"direction",field(observed_direction)},{"focus",field(observed_focus)},{"core_traits",field(core_traits)},{"composition_locked",field(composition_locked)}}},
          {"recommended",{{"direction",field(recommended_direction)},{"composition_decision",field(composition_decision)},{"economic_posture",field(economic_posture)},{"strategic_confidence",field(strategic_confidence)},{"economic_confidence",field(economic_confidence)}}}
        };
    }
};
struct ContextBridgeInput {
    const strategy::StrategicSharedContext* strategic{nullptr};
    const strategy::StrategicPlanDecision* strategic_decision{nullptr};
    const strategy::EconomicControlDecision* economic_decision{nullptr};
    const std::optional<ActiveComposition>* active_composition{nullptr};
    std::int32_t expected_player_id{-1};
    std::uint32_t expected_round{0};
};
class StrategicContextBridge {
public:
    static StrategicContextBridgeSnapshot adapt(const ContextBridgeInput& in) {
        StrategicContextBridgeSnapshot out; auto& m=out.metadata;
        if(!in.strategic||!in.strategic_decision||!in.economic_decision){m.quality=ContextBridgeQuality::Missing;m.reason="required_strategic_or_economic_source_missing";return out;}
        const auto& c=*in.strategic;
        if(c.player_id!=in.expected_player_id){m.quality=ContextBridgeQuality::Incompatible;m.reason="player_id_mismatch";return out;}
        if(c.round!=in.expected_round){m.quality=ContextBridgeQuality::Stale;m.reason="round_mismatch";return out;}
        const bool active=in.active_composition&&in.active_composition->has_value();
        const bool has_active_composition=active;
        const auto set=[](auto& dst,auto value,ContextValueOrigin origin,const char* source,const char* reason){dst.value=std::move(value);dst.origin=origin;dst.quality=ContextBridgeQuality::Valid;dst.source=source;dst.reason=reason;};
        const auto missing=[](auto& dst,const char* source,const char* reason){dst.value.reset();dst.quality=ContextBridgeQuality::Missing;dst.source=source;dst.reason=reason;};
        const auto set_if=[&](auto& dst,bool available,auto value,ContextValueOrigin origin,const char* source,const char* reason,const char* missing_reason){
            if(available) set(dst,std::move(value),origin,source,reason);
            else missing(dst,source,missing_reason);
        };
        // Numeric defaults are not observations. Every native economic field
        // must be explicitly marked available by the producer before projection.
        set_if(out.hp,c.evidence.hp,c.hp,ContextValueOrigin::Observed,"StrategicSharedContext","live_player_state","hp_not_produced");
        set_if(out.gold,c.evidence.gold,c.gold,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state","gold_not_produced");
        set_if(out.level,c.evidence.level,c.level,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state","level_not_produced");
        set_if(out.xp,c.evidence.xp,c.xp,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state","xp_not_produced");
        set_if(out.xp_to_next,c.evidence.xp_to_next,c.xp_to_next,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state","xp_to_next_not_produced");
        set_if(out.win_streak,c.evidence.streaks,c.win_streak,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state","streak_evidence_not_produced");
        set_if(out.loss_streak,c.evidence.streaks,c.loss_streak,ContextValueOrigin::Observed,"StrategicSharedContext","live_economy_state","streak_evidence_not_produced");
        // No authoritative lock producer is wired into this bridge yet.
        missing(out.composition_locked,"unavailable","no_authoritative_lock_source");
        // Direction/focus/core traits are derived projections, not game facts.
        set_if(out.observed_direction,!c.current_composition_direction.empty(),c.current_composition_direction,ContextValueOrigin::Derived,"StrategicPlanner::StrategicCommitment","committed_current_direction","no_committed_direction");
        set_if(out.observed_focus,!c.current_composition_focus.empty(),c.current_composition_focus,ContextValueOrigin::Derived,"NativeStrategicCompositionGenerator","generated_direction_focus","no_generated_focus");
        set_if(out.core_traits,!c.current_core_traits.empty(),c.current_core_traits,ContextValueOrigin::Derived,"NativeStrategicCompositionGenerator","generated_completed_traits","no_generated_core_traits");
        set_if(out.stage,c.stage>0,c.stage,ContextValueOrigin::Derived,"StrategicSharedContext","round_stage_mapping","stage_not_produced");
        set_if(out.progression_plan,c.evidence.progression_plan,progression_name(c.progression_plan),ContextValueOrigin::Derived,"StrategicPlanner::StrategicCommitment","committed_progression_plan","progression_plan_not_inferred");
        set_if(out.board_power,c.evidence.board_power,c.board_power,ContextValueOrigin::Derived,"BoardEvaluation","board_power_estimate","board_power_not_produced");
        set_if(out.relative_board_power,c.evidence.relative_board_power,c.relative_board_power,ContextValueOrigin::Derived,"BoardEvaluation","relative_to_lobby_average","relative_board_power_not_produced");
        const bool direction_available=c.evidence.current_direction &&
            !c.current_composition_direction.empty();
        set_if(out.direction_score,direction_available,c.current_direction_score,ContextValueOrigin::Derived,"StrategicPlanner","planner_direction_score","direction_score_without_direction");
        set_if(out.direction_viable,direction_available,c.current_direction_viable,ContextValueOrigin::Derived,"StrategicPlanner","planner_viability_assessment","direction_viability_without_direction");
        set_if(out.recommended_direction,!in.strategic_decision->target_composition_direction.empty(),in.strategic_decision->target_composition_direction,ContextValueOrigin::Recommended,"StrategicPlanner","shadow_recommendation_only","no_recommended_direction");
        set_if(out.composition_decision,in.strategic_decision->composition_decision!=strategy::CompositionDecision::InsufficientEvidence,decision_name(in.strategic_decision->composition_decision),ContextValueOrigin::Recommended,"StrategicPlanner","shadow_recommendation_only","strategic_decision_insufficient_evidence");
        set_if(out.economic_posture,in.economic_decision->sufficient_evidence,posture_name(in.economic_decision->posture),ContextValueOrigin::Recommended,"EconomicController","shadow_recommendation_only","economic_decision_insufficient_evidence");
        set_if(out.strategic_confidence,in.strategic_decision->composition_decision!=strategy::CompositionDecision::InsufficientEvidence,in.strategic_decision->confidence,ContextValueOrigin::Recommended,"StrategicPlanner","uncalibrated_score_confidence","strategic_confidence_unavailable");
        set_if(out.economic_confidence,in.economic_decision->sufficient_evidence,in.economic_decision->confidence,ContextValueOrigin::Recommended,"EconomicController","uncalibrated_score_confidence","economic_confidence_unavailable");
        m.quality=has_active_composition?ContextBridgeQuality::Valid:ContextBridgeQuality::Partial;
        m.reason=has_active_composition?"validated_player_round_and_composition_identity":"player_round_valid_but_no_active_composition";
        if(!has_active_composition){out.recommended_direction.quality=ContextBridgeQuality::Partial;out.recommended_direction.reason="no_active_composition_identity";out.composition_decision.quality=ContextBridgeQuality::Partial;out.composition_decision.reason="no_active_composition_identity";}
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
