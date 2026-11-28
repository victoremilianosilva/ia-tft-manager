#include <cassert>
#include <memory>
#include "lobby/NativeSpatialContext.hpp"
int main(){
 auto s=std::make_shared<tft::AuditSnapshot>(); auto& p=s->players[0];
 auto& a=p.board[1];a.occupied=true;a.uuid="tank-a";a.champion_internal_id=10;a.role=0;a.attack_damage=40;a.trait_names={"Frontline","Trait_A"};
 auto& b=p.board[8];b.occupied=true;b.uuid="carry-b";b.champion_internal_id=11;b.role=1;
 auto& c=p.board[9];c.occupied=true;c.uuid="carry-c";c.champion_internal_id=11;c.role=1;
 tft::NativeSpatialContext x(s,0);assert(x.availability()==tft::ContextAvailability::Complete);
 assert(x.row_buffer()[1]==0&&x.column_buffer()[1]==1);assert(x.uuid_buffer()[8]!=x.uuid_buffer()[9]);
 assert(x.stats_buffer()[1][0]==40.0f);assert(x.trait_buffer()[1].size()==2);assert(x.player_decision_sequence()==s->player_decision_sequences[0]);bool n=false,f=false;
 for(const auto&r:x.relations()){if(r.source_slot==1&&r.target_slot==8&&r.kind==tft::SpatialRelationKind::RectangularNeighbor)n=true;
 if(r.source_slot==1&&r.target_slot==8&&r.kind==tft::SpatialRelationKind::FrontlineSupportsBackline)f=true;}
 assert(n&&f);auto bad=std::make_shared<tft::AuditSnapshot>(*s);bad->board_geometry_id="hex";
 tft::NativeSpatialContext y(bad,0);assert(y.availability()==tft::ContextAvailability::Incompatible&&y.relations().empty());
}