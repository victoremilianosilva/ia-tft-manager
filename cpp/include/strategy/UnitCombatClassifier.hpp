#pragma once
#include <algorithm>
#include <cctype>
#include <initializer_list>
#include <string>
#include <string_view>
namespace tft::strategy {
enum class UnitArchetype { TANK, FRONTLINE_FIGHTER, PHYSICAL_CARRY, MAGIC_CARRY, SUPPORT, FLEXIBLE };
struct UnitCombatSignals {
 int base_role{3}; double attack_range{1.0}, max_health{0.0}, armor{0.0}, magic_resist{0.0};
 double attack_damage{0.0}, attack_speed{0.0}, ability_power{0.0};
 double item_health{0.0}, item_armor{0.0}, item_magic_resist{0.0};
 double item_attack_damage{0.0}, item_attack_speed{0.0}, item_ability_power{0.0}, item_crit{0.0};
 bool planned_main_carry{false}; std::string ability_text;
};
struct UnitCombatClassification {
 UnitArchetype archetype{UnitArchetype::FLEXIBLE}; int positioning_role{3};
 bool physical_damage_profile{false}, magical_damage_profile{false}; double confidence{0.0};
};
class UnitCombatClassifier {
public:
 static UnitCombatClassification classify(const UnitCombatSignals& s) {
  const std::string text=lower(s.ability_text); const double range=std::max(0.0,s.attack_range);
  const double hp=s.max_health+s.item_health, armor=s.armor+s.item_armor, mr=s.magic_resist+s.item_magic_resist;
  const double ad=s.attack_damage+s.item_attack_damage, as=s.attack_speed+s.item_attack_speed, ap=s.ability_power+s.item_ability_power;
  const bool support=contains(text,{"heal allies","heals allies","healing allies","shield allies","buff allies","all allies","restore health to allies","grant mana to allies","grant mana","cura aliados","cura os aliados","escudo aliados","escudo aos aliados","concede escudo aos aliados","restaura vida dos aliados","concede mana aos aliados"});
  const bool tank=(hp>=850.0&&(armor>=40.0||mr>=40.0))||(armor>=55.0&&mr>=55.0)||(s.base_role==0&&hp>=650.0);
  if(support||(s.base_role==2&&text.empty())) return {UnitArchetype::SUPPORT,2,false,false,support?0.90:0.72};
  if(s.base_role==0||tank) return {UnitArchetype::TANK,0,false,false,tank?0.90:0.72};
  if(s.base_role==4) return {UnitArchetype::FLEXIBLE,4,false,false,0.65};
  const bool phys_text=contains(text,{"physical damage","dano físico","dano fisico","scalead","attack damage","dano de ataque"});
  const bool magic_text=contains(text,{"magic damage","dano mágico","dano magico","scaleap","ability power","poder de habilidade"});
  const double physical=(phys_text?2.0:0.0)+std::min(2.0,ad/50.0)+std::min(1.5,as*1.2)+std::min(1.0,s.item_crit*2.0);
  const double magical=(magic_text?2.0:0.0)+std::min(2.5,ap/40.0);
  if(range>=3.0&&(s.planned_main_carry||physical>=1.5||magical>=1.5)) {
   if(magical>physical+0.25) return {UnitArchetype::MAGIC_CARRY,1,false,true,std::min(0.98,0.62+(magical-physical)*0.08)};
   if(physical>magical+0.25) return {UnitArchetype::PHYSICAL_CARRY,1,true,false,std::min(0.98,0.62+(physical-magical)*0.08)};
  }
  if(range>0.0&&range<=1.0&&(physical>=1.0||s.base_role==3||s.base_role==1))
   return {UnitArchetype::FRONTLINE_FIGHTER,3,phys_text,magic_text,std::min(0.95,0.65+physical*0.06)};
  if(range>=2.0&&range<3.0) return {UnitArchetype::FLEXIBLE,3,physical>magical,magical>physical,0.55};
  if(range>=3.0) return {UnitArchetype::FLEXIBLE,1,physical>magical,magical>physical,0.52};
  return {UnitArchetype::FLEXIBLE,s.base_role==1?1:3,physical>magical,magical>physical,0.45};
 }
private:
 static std::string lower(std::string v){std::transform(v.begin(),v.end(),v.begin(),[](unsigned char c){return static_cast<char>(std::tolower(c));});return v;}
 static bool contains(const std::string& t,std::initializer_list<std::string_view> terms){for(auto term:terms)if(t.find(term)!=std::string::npos)return true;return false;}
};
} // namespace tft::strategy
