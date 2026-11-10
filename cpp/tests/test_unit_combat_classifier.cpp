#include "strategy/UnitCombatClassifier.hpp"
#include <cstdlib>
#include <iostream>
static void req(bool x,const char* m){if(!x){std::cerr<<"[FAIL] "<<m<<'\n';std::exit(EXIT_FAILURE);}}
int main(){using namespace tft::strategy; UnitCombatSignals s;
s.base_role=3;s.attack_range=1;s.max_health=900;s.armor=55;s.magic_resist=55;req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::TANK,"durability identifies tank");
s={};s.base_role=3;s.attack_range=1;s.attack_damage=70;s.attack_speed=.9;s.ability_text="Dano Físico";req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::FRONTLINE_FIGHTER,"melee damage dealer is frontline fighter");
s={};s.base_role=3;s.attack_range=4;s.attack_damage=75;s.attack_speed=.9;s.ability_text="Dano Físico";req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::PHYSICAL_CARRY,"ranged AD is physical carry");
s={};s.base_role=3;s.attack_range=4;s.item_ability_power=80;s.ability_text="Dano Mágico baseado em Poder de Habilidade";req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::MAGIC_CARRY,"ranged AP is magic carry");
s={};s.base_role=3;s.attack_range=4;s.ability_text="Concede escudo aos aliados";req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::SUPPORT,"ally protection identifies support");
s={};s.base_role=3;s.attack_range=2;req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::FLEXIBLE,"range two remains flexible");
s={};s.base_role=2;s.attack_range=1;s.attack_damage=70;s.ability_text="Cura a si mesmo e causa dano físico";req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::FRONTLINE_FIGHTER,"self-healing melee damage dealer must not become support");
s={};s.base_role=3;s.attack_range=4;s.item_attack_damage=80;req(UnitCombatClassifier::classify(s).archetype==UnitArchetype::PHYSICAL_CARRY,"items influence effective damage profile");
s={};s.base_role=3;s.attack_range=4;s.planned_main_carry=true;req(UnitCombatClassifier::classify(s).positioning_role==1,"planned main carry nudges ambiguous ranged unit");
std::cout<<"[PASS] Unit classification by range, role, items and composition.\n";}
