#include "composition_intelligence/CompositionSourceAdapters.hpp"
#include "strategy/CompositionPlanner.hpp"
#include <cassert>
#include <iostream>
using namespace tft;
using namespace tft::composition_intelligence;
namespace {
ChampionDefinition make(int id,const std::string& key,int role,bool carry=false,bool frontline=false,bool support=false){
 ChampionDefinition c;c.internal_id=id;c.api_name=key;c.character_name=key;c.name=key;c.role=role;c.combat_profile.role=role;
 c.combat_profile.is_carry=carry;c.combat_profile.frontline=frontline;c.combat_profile.is_support=support;return c;
}
std::vector<ChampionDefinition> pool(){return {make(10,"DA_18_Tank",0,false,true),make(11,"DA_18_Carry",1,true),make(12,"DA_18_Support",2,false,false,true),make(13,"DA_18_Flex",4)};}
void opgg_maps_to_common_contract(){
 auto catalog=nlohmann::json{{"patch","18.1"},{"compositions",nlohmann::json::array({
  {{"id","opgg-1"},{"team_code","abcTFTSet18"},{"units",nlohmann::json::array({
   {{"key","DA_18_Tank"},{"is_core",true},{"priority",2}},
   {{"key","DA_18_Carry"},{"is_core",true},{"priority",1}},
   {{"key","DA_18_Support"},{"is_core",false},{"priority",0}}})},
   {"statistics",{{"deck",{{"totalCount",2000},{"top4Rate",0.72}}}}}}
 })}};
 auto result=OppgCompositionAdapter::adapt(catalog,pool());assert(result.candidates.size()==1);
 const auto& c=result.candidates.front();assert(c.source==CompositionSource::Oppg);assert(c.set_id=="18");assert(c.patch=="18.1");
 assert(c.main_carry_id==11);assert(c.target_board_size==3);assert(c.units.size()==3);assert(c.source_score>0.71&&c.source_score<0.73);
}
void opgg_rejects_wrong_set_and_low_coverage(){
 auto wrong=nlohmann::json{{"compositions",nlohmann::json::array({{{"id","wrong"},{"team_code","TFTSet17"},{"units",nlohmann::json::array({{{"key","DA_18_Carry"}}})}}})}};
 assert(OppgCompositionAdapter::adapt(wrong,pool()).candidates.empty());
 auto partial=nlohmann::json{{"compositions",nlohmann::json::array({{{"id","partial"},{"team_code","TFTSet18"},{"units",nlohmann::json::array({
  {{"key","DA_18_Carry"}},{{"key","missing-a"}},{{"key","missing-b"}},{{"key","missing-c"}}})}}})}};
 assert(OppgCompositionAdapter::adapt(partial,pool()).candidates.empty());
}
void opgg_rejects_duplicate_composition_ids(){
 auto first=nlohmann::json{
  {"id","duplicate-id"},{"team_code","abcTFTSet18"},
  {"units",nlohmann::json::array({{{"key","DA_18_Carry"}}})}
 };
 auto catalog=nlohmann::json{{"patch","18.1"},
  {"compositions",nlohmann::json::array({first,first})}};
 const auto result=OppgCompositionAdapter::adapt(catalog,pool(),0.5);
 assert(result.candidates.size()==1);
 assert(std::any_of(result.diagnostics.begin(),result.diagnostics.end(),
  [](const std::string& value){return value.find("duplicate OP.GG composition id")!=std::string::npos;}));
}
void native_adapter_uses_neutral_snapshot(){
 NativeCompositionSnapshot input;input.composition_id="native-18";input.set_id="18";input.patch="18.1";
 input.units={{10,true,80},{11,true,100},{12,false,40}};input.target_board_size=8;input.source_score=4.25;
 auto result=NativeCompositionAdapter::adapt(input,pool());assert(result.candidates.size()==1);
 const auto& c=result.candidates.front();assert(c.source==CompositionSource::Native);assert(c.main_carry_id==11);assert(c.units.size()==3);assert(c.target_board_size==8);
}
void native_adapter_rejects_unknown_or_wrong_set_units(){
 NativeCompositionSnapshot unknown;unknown.composition_id="native-unknown";unknown.set_id="18";unknown.units={{10,true,80},{999,true,100}};
 auto unknown_result=NativeCompositionAdapter::adapt(unknown,pool());assert(unknown_result.candidates.empty());
 NativeCompositionSnapshot wrong_set;wrong_set.composition_id="native-wrong-set";wrong_set.set_id="17";wrong_set.units={{10,true,80},{11,true,100}};
 auto set_result=NativeCompositionAdapter::adapt(wrong_set,pool());assert(set_result.candidates.empty());
}
void opgg_failure_does_not_block_native(){
 auto opgg=OppgCompositionAdapter::adapt(nlohmann::json::object(),pool());
 NativeCompositionSnapshot input;input.composition_id="native-fallback";input.set_id="18";input.units={{10,true,80},{11,true,100}};
 auto native=NativeCompositionAdapter::adapt(input,pool());assert(opgg.candidates.empty());assert(native.candidates.size()==1);
}

void native_planner_exports_pre_opgg_candidate(){
 auto champions=pool();
 champions[0].traits={"Shepherd","Guardian"};
 champions[1].traits={"Shepherd","Invoker"};
 champions[2].traits={"Guardian","Invoker"};
 champions[3].traits={"Invoker"};
 for(auto& champion:champions) champion.cost=2;
 strategy::CompositionPlanner::TraitMilestones milestones{
  {"Shepherd",{2}},{"Guardian",{2}},{"Invoker",{2}}
 };
 strategy::CompositionPlanner::OwnedCopies owned;
 strategy::CompositionPlanner::AvailableCopies available;
 for(const auto& champion:champions) available[champion.internal_id]=10;
 const auto plan=strategy::CompositionPlanner::build(
  champions,milestones,"Shepherd",{},owned,4,5,available,{},nullptr,-1,true);
 assert(!plan.native_snapshot.composition_id.empty());
 assert(plan.native_snapshot.set_id=="18");
 assert(plan.native_snapshot.source_reference=="composition-planner/native-before-opgg");
 assert(!plan.native_snapshot.units.empty());
 assert(plan.native_candidates.size()==1);
 assert(plan.native_candidates.front().source==CompositionSource::Native);
 assert(plan.native_candidates.front().composition_id==plan.native_snapshot.composition_id);
}
}
int main(){opgg_maps_to_common_contract();opgg_rejects_wrong_set_and_low_coverage();opgg_rejects_duplicate_composition_ids();native_adapter_uses_neutral_snapshot();native_adapter_rejects_unknown_or_wrong_set_units();opgg_failure_does_not_block_native();native_planner_exports_pre_opgg_candidate();std::cout<<"Composition source adapter tests passed\n";return 0;}
