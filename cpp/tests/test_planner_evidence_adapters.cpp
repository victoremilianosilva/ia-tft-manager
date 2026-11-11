#include "composition_intelligence/PlannerEvidenceAdapters.hpp"
#include <cassert>
#include <cmath>
#include <iostream>
using namespace tft::composition_intelligence;
void economy_test(){
 tft::strategy::StrategicSharedContext c;c.round=12;c.gold=38;c.level=7;c.xp=4;c.xp_to_next=8;
 c.interest_if_resolved_now=3;c.projected_next_round_income=8;c.win_streak=2;c.alive=true;
 tft::strategy::EconomicControlDecision d;d.shadow_only=true;d.posture=tft::strategy::EconomicPosture::InvestExperience;
 d.reason=tft::strategy::StrategicReason::ProgressionTiming;d.survival_pressure=.2;d.board_pressure=.4;
 d.economy_pressure=.7;d.confidence=.8;
 auto e=PlannerEvidenceAdapters::economic(c,d,4,12);
 assert(e.metadata.available&&e.metadata.quality==EvidenceQuality::Valid&&e.gold==38&&e.xp_to_next==8);
 assert(e.posture==tft::strategy::EconomicPosture::InvestExperience);
 assert(e.buy_experience_opportunity_cost==tft::strategy::action_opportunity_cost::kBuyExperience);
 auto stale=PlannerEvidenceAdapters::economic(c,d,4,13);
 assert(!stale.metadata.available&&stale.metadata.quality==EvidenceQuality::Stale);
 d.shadow_only=false;assert(!PlannerEvidenceAdapters::economic(c,d,4,12).metadata.available);
}
void board_test(){
 tft::strategy::BoardEvaluationResult r;r.unit_count=6;r.frontline_count=2;r.carry_count=2;
 r.positional_score=.8;r.structural_score=.7;r.synergy_score=.6;r.total_score=.72;
 r.strategic_fit_score=.4;r.exposed_carry_count=1;
 auto e=PlannerEvidenceAdapters::board(r,3,12,12);
 assert(e.metadata.available&&e.frontline_count==2&&e.exposed_carry_count==1);
 assert(std::abs(e.total_score-.72)<1e-9);
 r.unit_count=0;auto missing=PlannerEvidenceAdapters::board(r,3,12,12);
 assert(!missing.metadata.available&&missing.metadata.quality==EvidenceQuality::Missing);
}
void item_test(){
 tft::items::ItemDefinition sword;sword.id="test_sword";sword.name="Test Sword";
 sword.attack_damage=20;sword.carry_weight=1.0;sword.unit_equipable=true;
 tft::items::ItemEngine engine({sword},{"bf"});tft::items::ItemPlayerState state;
 state.inventory={"test_sword"};state.equipped_by_unit_uuid["unit-1"]={"test_sword"};
 tft::items::UnitProfile profile;profile.uuid="unit-1";profile.role=1;profile.backline=true;profile.attack_damage=100;
 auto e=PlannerEvidenceAdapters::item(engine,state,{{42,profile}},5,12,12);
 assert(e.metadata.available&&e.units.size()==1&&e.units[0].has_equipped_items&&e.units[0].has_inventory_candidate);
 assert(e.units[0].best_inventory_item_id=="test_sword"&&e.inventory_count==1&&state.inventory.size()==1);
 auto stale=PlannerEvidenceAdapters::item(engine,state,{{42,profile}},5,11,12);
 assert(!stale.metadata.available&&stale.metadata.quality==EvidenceQuality::Stale);
}
void combine_test(){
 auto s=PlannerEvidenceAdapters::combine("comp-X",9,15,{},{},{});
 assert(s.composition_id=="comp-X"&&s.composition_version==9&&s.round==15);
}

void identity_and_source_freshness_are_enforced() {
 PlannerEvidenceSnapshot snapshot;
 snapshot.match_id=77;snapshot.player_id=2;snapshot.composition_id="comp-A";
 snapshot.composition_version=5;snapshot.round=16;
 const auto set_valid=[&](EvidenceSourceMetadata& m,const std::string& source) {
  m.source=source;m.source_version=5;m.match_id=77;m.player_id=2;
  m.composition_id="comp-A";m.source_round=16;m.expected_round=16;
  m.quality=EvidenceQuality::Valid;m.available=true;
 };
 set_valid(snapshot.economy.metadata,"EconomicController");
 set_valid(snapshot.board.metadata,"BoardEvaluation");
 set_valid(snapshot.items.metadata,"ItemEngine");
 assert(PlannerEvidenceAdapters::snapshot_identity_matches(snapshot,77,2,"comp-A",5,16));
 assert(PlannerEvidenceAdapters::source_matches(snapshot.economy.metadata,77,2,"comp-A",5,16));
 assert(!PlannerEvidenceAdapters::snapshot_identity_matches(snapshot,77,1,"comp-A",5,16));
 assert(!PlannerEvidenceAdapters::snapshot_identity_matches(snapshot,77,2,"comp-A",6,16));
 assert(!PlannerEvidenceAdapters::source_matches(snapshot.board.metadata,77,2,"comp-A",5,17));
 snapshot.items.metadata.quality=EvidenceQuality::Partial;
 assert(!PlannerEvidenceAdapters::source_matches(snapshot.items.metadata,77,2,"comp-A",5,16));
}

int main(){economy_test();board_test();item_test();combine_test();identity_and_source_freshness_are_enforced();std::cout<<"Planner evidence adapter tests passed\n";}
