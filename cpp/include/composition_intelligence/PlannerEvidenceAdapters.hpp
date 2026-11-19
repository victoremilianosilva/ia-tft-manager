#pragma once
#include "items/ItemEngine.hpp"
#include "strategy/BoardEvaluation.hpp"
#include "strategy/EconomicController.hpp"
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>
#include <utility>
#include <vector>
namespace tft::composition_intelligence {
enum class EvidenceQuality { Missing, Stale, Valid, Partial, Invalid };
struct EvidenceSourceMetadata {
 std::string source;
 std::uint32_t source_round{0}; std::uint32_t expected_round{0}; EvidenceQuality quality{EvidenceQuality::Missing};
 std::string reason{"not_provided"}; bool available{false};
};
struct EconomicPlannerEvidence {
 EvidenceSourceMetadata metadata; std::int32_t gold{0},level{0},xp{0},xp_to_next{0};
 std::int32_t interest_if_resolved_now{0},projected_next_round_income{0},win_streak{0},loss_streak{0};
 strategy::EconomicPosture posture{strategy::EconomicPosture::AccumulateResources};
 strategy::StrategicReason reason{strategy::StrategicReason::InsufficientEvidence};
 double survival_pressure{0},board_pressure{0},economy_pressure{0},confidence{0};
 double buy_experience_opportunity_cost{0},reroll_with_target_opportunity_cost{0};
 double reroll_without_target_opportunity_cost{0},buy_unit_opportunity_cost{0};
 // Appended to preserve existing aggregate initialization contracts.
 bool sufficient_evidence{false};
 std::vector<std::string> evidence_used,evidence_missing;
 bool survival_evidence_available{false};
 bool streak_evidence_available{false};
 // Per-field availability: a valid source envelope does not make every field present.
 bool gold_available{false},level_available{false},xp_available{false},xp_to_next_available{false};
 bool interest_available{false},projected_income_available{false};
 bool win_streak_available{false},loss_streak_available{false};
 bool board_pressure_available{false},economy_pressure_available{false};
};
struct BoardPlannerEvidence {
 EvidenceSourceMetadata metadata;
 double positional_score{0},structural_score{0},synergy_score{0},total_score{0};
 double strategic_fit_score{0},unit_quality_score{0},trait_coherence_score{0};
 std::int32_t unit_count{0},frontline_count{0},carry_count{0},exposed_carry_count{0};
 std::int32_t missing_frontline_count{0},missing_backline_count{0};
};
struct ItemUnitBinding {
 std::int32_t champion_id{-1};
 items::UnitProfile profile;
 std::string role_source{"derived:UnitCombatClassifier"};
 std::string composition_source{"unavailable_without_active_composition"};
 std::string composition_id;
 std::uint64_t composition_version{0};
};
struct ItemUnitPlannerEvidence {
 std::int32_t champion_id{-1}; std::vector<std::string> equipped_item_ids;
 std::string best_inventory_item_id; double equipped_fit{0},best_inventory_fit{0};
 bool has_equipped_items{false},has_inventory_candidate{false};
 // Observed profile facts and composition-derived preferences remain distinct.
 std::string role_source{"unknown"};
 std::string composition_source{"unavailable"};
 std::string composition_id;
 std::uint64_t composition_version{0};
 double composition_fit{0.0};
 std::vector<std::string> preferred_traits;
};
struct ItemPlannerEvidence {
 EvidenceSourceMetadata metadata; std::size_t inventory_count{0},component_count{0};
 std::vector<ItemUnitPlannerEvidence> units;
};
struct PlannerEvidenceSnapshot {
 std::uint32_t schema_version{3}; std::uint64_t match_id{0}; std::int32_t player_id{-1};
 std::string composition_id; std::uint64_t composition_version{0}; std::uint32_t round{0};
 EconomicPlannerEvidence economy; BoardPlannerEvidence board; ItemPlannerEvidence items;
};
class PlannerEvidenceAdapters {
public:
 static EconomicPlannerEvidence economic(const strategy::StrategicSharedContext& c,
  const strategy::EconomicControlDecision& d,std::uint32_t expected_round,
  std::int32_t expected_player_id) {
  EconomicPlannerEvidence o;
  o.metadata=make_metadata("EconomicController",c.round,expected_round,c.alive&&d.shadow_only);
  if(c.player_id!=expected_player_id){o.metadata.available=false;o.metadata.quality=EvidenceQuality::Invalid;o.metadata.reason="player_id_mismatch";return o;}
  if(!std::isfinite(d.survival_pressure)||!std::isfinite(d.board_pressure)||!std::isfinite(d.economy_pressure)||!std::isfinite(d.confidence)){o.metadata.available=false;o.metadata.quality=EvidenceQuality::Invalid;o.metadata.reason="non_finite_economic_metric";return o;}
  if(!o.metadata.available)return o;
  o.gold=c.gold;o.level=c.level;o.xp=c.xp;o.xp_to_next=c.xp_to_next;
  o.interest_if_resolved_now=c.interest_if_resolved_now;o.projected_next_round_income=c.projected_next_round_income;
  o.win_streak=c.win_streak;o.loss_streak=c.loss_streak;o.posture=d.posture;o.reason=d.reason;
  o.gold_available=c.evidence.gold;o.level_available=c.evidence.level;
  o.xp_available=c.evidence.xp;o.xp_to_next_available=c.evidence.xp_to_next;
  o.interest_available=c.evidence.interest_if_resolved_now;
  o.projected_income_available=c.evidence.projected_next_round_income;
  o.win_streak_available=c.evidence.streaks;o.loss_streak_available=c.evidence.streaks;
  o.sufficient_evidence=d.sufficient_evidence;
  o.evidence_used=d.evidence_used;o.evidence_missing=d.evidence_missing;
  o.survival_evidence_available=c.evidence.hp ||
   c.evidence.estimated_incoming_damage || c.evidence.elimination_risk;
  o.streak_evidence_available=c.evidence.streaks;
  o.board_pressure_available=c.evidence.relative_board_power;
  o.economy_pressure_available=c.evidence.gold;
  o.survival_pressure=unit(d.survival_pressure);o.board_pressure=unit(d.board_pressure);
  o.economy_pressure=unit(d.economy_pressure);o.confidence=unit(d.confidence);
  o.buy_experience_opportunity_cost=strategy::action_opportunity_cost::kBuyExperience;
  o.reroll_with_target_opportunity_cost=strategy::action_opportunity_cost::kRerollWithUpgradeTarget;
  o.reroll_without_target_opportunity_cost=strategy::action_opportunity_cost::kRerollWithoutUpgradeTarget;
  o.buy_unit_opportunity_cost=strategy::action_opportunity_cost::kBuyUnit;return o;
 }
 static BoardPlannerEvidence board(const strategy::BoardEvaluationResult& r,
  std::uint32_t source_round,std::uint32_t expected_round) {
  BoardPlannerEvidence o;o.metadata=make_metadata("BoardEvaluation",source_round,expected_round,r.unit_count>0);
  if(!o.metadata.available)return o;
  if(!std::isfinite(r.positional_score)||!std::isfinite(r.structural_score)||!std::isfinite(r.synergy_score)||!std::isfinite(r.total_score)||!std::isfinite(r.strategic_fit_score)||!std::isfinite(r.unit_quality_score)||!std::isfinite(r.trait_coherence_score)){o.metadata.available=false;o.metadata.quality=EvidenceQuality::Invalid;o.metadata.reason="non_finite_board_metric";return o;}
  o.positional_score=unit(r.positional_score);o.structural_score=unit(r.structural_score);
  o.synergy_score=unit(r.synergy_score);o.total_score=unit(r.total_score);
  o.strategic_fit_score=signed_unit(r.strategic_fit_score);o.unit_quality_score=unit(r.unit_quality_score);
  o.trait_coherence_score=unit(r.trait_coherence_score);o.unit_count=r.unit_count;
  o.frontline_count=r.frontline_count;o.carry_count=r.carry_count;
  o.exposed_carry_count=r.exposed_carry_count;o.missing_frontline_count=r.missing_frontline_count;
  o.missing_backline_count=r.missing_backline_count;return o;
 }
 static ItemPlannerEvidence item(const items::ItemEngine& engine,const items::ItemPlayerState& state,
  const std::vector<ItemUnitBinding>& bindings,
  std::uint32_t source_round,std::uint32_t expected_round) {
  ItemPlannerEvidence o;o.metadata=make_metadata("ItemEngine",source_round,expected_round,true);
  if(!o.metadata.available)return o;
  o.inventory_count=state.inventory.size();o.component_count=state.components.size();
  for(const auto& b:bindings) {
   if(b.champion_id<0||b.profile.uuid.empty())continue;
   ItemUnitPlannerEvidence u;u.champion_id=b.champion_id;
   u.role_source=b.role_source;u.composition_source=b.composition_source;
   u.composition_id=b.composition_id;u.composition_version=b.composition_version;
   u.composition_fit=unit(b.profile.composition_fit);
   u.preferred_traits=b.profile.preferred_traits;
   const auto eq=state.equipped_by_unit_uuid.find(b.profile.uuid);
   if(eq!=state.equipped_by_unit_uuid.end()) {
    u.equipped_item_ids=eq->second;u.has_equipped_items=!eq->second.empty();
    double sum=0;std::size_t count=0;
    for(const auto& id:eq->second){double fit=engine.item_fit(id,b.profile);
     if(fit>=0&&std::isfinite(fit)){sum+=fit;++count;}}
    u.equipped_fit=count?unit(sum/static_cast<double>(count)):0;
   }
   for(const auto& id:state.inventory){double fit=engine.item_fit(id,b.profile);
    if(fit>=0&&std::isfinite(fit)&&(!u.has_inventory_candidate||fit>u.best_inventory_fit)){
     u.has_inventory_candidate=true;u.best_inventory_fit=unit(fit);u.best_inventory_item_id=id;}}
   o.units.push_back(std::move(u));
  }
  if(bindings.empty()){o.metadata.quality=EvidenceQuality::Partial;o.metadata.reason="inventory_available_but_no_unit_bindings";}
  return o;
 }
 static bool snapshot_identity_matches(const PlannerEvidenceSnapshot& snapshot,
  std::uint64_t match_id,std::int32_t player_id,const std::string& composition_id,
  std::uint64_t composition_version,std::uint32_t round) {
  return snapshot.match_id==match_id&&snapshot.player_id==player_id&&
   snapshot.composition_id==composition_id&&snapshot.composition_version==composition_version&&
   snapshot.round==round;
 }
 static bool source_matches(const EvidenceSourceMetadata& m,std::uint32_t round) {
  return m.available&&m.source_round==round&&m.expected_round==round&&
   m.quality==EvidenceQuality::Valid;
 }
private:
 static EvidenceSourceMetadata make_metadata(std::string source,
  std::uint32_t source_round,std::uint32_t expected_round,bool available) {
  EvidenceSourceMetadata o;o.source=std::move(source);
  o.source_round=source_round;o.expected_round=expected_round;o.available=available;
  if(!o.available){o.quality=EvidenceQuality::Missing;o.reason="source_unavailable";}
  else if(source_round!=expected_round){o.available=false;o.quality=EvidenceQuality::Stale;o.reason="round_mismatch";}
  else{o.quality=EvidenceQuality::Valid;o.reason="validated_read_only_snapshot";}return o;
 }
 static double unit(double v){return std::isfinite(v)?std::clamp(v,0.0,1.0):0.0;}
 static double signed_unit(double v){return std::isfinite(v)?std::clamp(v,-1.0,1.0):0.0;}
};
} // namespace tft::composition_intelligence
