#include "composition_intelligence/CompositionSourceAdapters.hpp"
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
void native_adapter_uses_neutral_snapshot(){
 NativeCompositionSnapshot input;input.composition_id="native-18";input.set_id="18";input.patch="18.1";
 input.units={{10,true,80},{11,true,100},{12,false,40}};input.target_board_size=8;input.source_score=4.25;
 auto result=NativeCompositionAdapter::adapt(input,pool());assert(result.candidates.size()==1);
 const auto& c=result.candidates.front();assert(c.source==CompositionSource::Native);assert(c.main_carry_id==11);assert(c.units.size()==3);assert(c.target_board_size==8);
}
void opgg_failure_does_not_block_native(){
 auto opgg=OppgCompositionAdapter::adapt(nlohmann::json::object(),pool());
 NativeCompositionSnapshot input;input.composition_id="native-fallback";input.set_id="18";input.units={{10,true,80},{11,true,100}};
 auto native=NativeCompositionAdapter::adapt(input,pool());assert(opgg.candidates.empty());assert(native.candidates.size()==1);
}
}
int main(){opgg_maps_to_common_contract();opgg_rejects_wrong_set_and_low_coverage();native_adapter_uses_neutral_snapshot();opgg_failure_does_not_block_native();std::cout<<"Composition source adapter tests passed\n";return 0;}
