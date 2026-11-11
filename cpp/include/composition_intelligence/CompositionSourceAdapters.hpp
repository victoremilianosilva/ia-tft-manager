#pragma once
#include "composition_intelligence/ActiveCompositionManager.hpp"
#include "lobby/TftEngine.hpp"
#include <nlohmann/json.hpp>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace tft::composition_intelligence {
struct CompositionAdapterResult {
    std::vector<CompositionCandidate> candidates;
    std::vector<std::string> diagnostics;
    bool ok() const noexcept { return !candidates.empty(); }
};

namespace adapter_detail {
inline std::string set_number(const std::string& value) {
    return composition_set_number(value);
}
inline std::string champion_set(const tft::ChampionDefinition& c) {
    return composition_champion_set(c.api_name, c.character_name);
}
inline bool compatible_set(const std::string& set,const std::vector<tft::ChampionDefinition>& pool) {
    if(set.empty()) return false;
    bool has_local=false;
    for(const auto& c:pool){auto local=champion_set(c); if(local.empty())continue; has_local=true;if(local==set)return true;}
    return !has_local;
}
inline UnitRole role(const tft::ChampionDefinition& c) {
    const int r=c.combat_profile.role>=0?c.combat_profile.role:c.role;
    if(c.combat_profile.is_carry || r==1 || c.role_name=="carry" || c.combat_profile.role_name=="carry") return UnitRole::MainCarry;
    if(c.combat_profile.is_support || r==2) return UnitRole::Support;
    if(c.combat_profile.frontline || r==0 || r==3) return UnitRole::Frontline;
    return UnitRole::Flex;
}
inline std::unordered_map<std::string,const tft::ChampionDefinition*> lookup(const std::vector<tft::ChampionDefinition>& pool){
    std::unordered_map<std::string,const tft::ChampionDefinition*> m;
    for(const auto& c:pool){if(!c.api_name.empty())m[c.api_name]=&c;if(!c.character_name.empty())m[c.character_name]=&c;if(!c.name.empty())m[c.name]=&c;}
    return m;
}
inline std::int32_t main_carry(const std::vector<CompositionUnit>& units){
    const CompositionUnit* best=nullptr;
    for(const auto& u:units) if(u.role==UnitRole::MainCarry && (!best || (u.priority>0 && (best->priority==0 || u.priority<best->priority)))) best=&u;
    return best?best->champion_id:-1;
}
inline double score(const nlohmann::json& comp){
    if(!comp.contains("statistics")||!comp["statistics"].is_object())return 0.0;
    for(const char* key:{"deck","label"}) if(comp["statistics"].contains(key)&&comp["statistics"][key].is_object()){
        const auto& s=comp["statistics"][key]; double v=s.value("top4Rate",0.0);
        if(s.value("totalCount",0)>=1000&&std::isfinite(v))return std::clamp(v,0.0,1.0);
    }
    return 0.0;
}
}

class OppgCompositionAdapter {
public:
 static CompositionAdapterResult adapt(const nlohmann::json& catalog,const std::vector<tft::ChampionDefinition>& pool,double min_coverage=0.70){
    CompositionAdapterResult out;
    if(!catalog.is_object()||!catalog.contains("compositions")||!catalog["compositions"].is_array()){out.diagnostics.emplace_back("OP.GG catalog is missing a compositions array");return out;}
    if(!std::isfinite(min_coverage)||min_coverage<0.0||min_coverage>1.0){out.diagnostics.emplace_back("minimum mapping coverage must be between 0 and 1");return out;}
    const auto by_key=adapter_detail::lookup(pool); const auto patch=catalog.value("patch",std::string{});
    std::unordered_set<std::string> seen_composition_ids;
    for(const auto& comp:catalog["compositions"]){
      if(!comp.is_object()||!comp.contains("units")||!comp["units"].is_array()){out.diagnostics.emplace_back("Skipped OP.GG composition without units");continue;}
      const auto team=comp.value("team_code",std::string{}); const auto set=adapter_detail::set_number(team);
      if(!adapter_detail::compatible_set(set,pool)){out.diagnostics.emplace_back("Skipped OP.GG composition with missing/incompatible Set");continue;}
      CompositionCandidate c; c.composition_id=comp.value("id",std::string{});
      if(c.composition_id.empty())c.composition_id=comp.value("name",std::string{});
      if(c.composition_id.empty()){out.diagnostics.emplace_back("Skipped OP.GG composition without id/name");continue;}
      if(!seen_composition_ids.insert(c.composition_id).second){out.diagnostics.emplace_back("Skipped duplicate OP.GG composition id "+c.composition_id);continue;}
      c.source=CompositionSource::Oppg;c.set_id=set;c.patch=patch;c.source_score=adapter_detail::score(comp);c.source_reference=comp.value("id",std::string{});
      std::size_t source_count=0;
      for(const auto& unit:comp["units"]){
        if(!unit.is_object())continue;++source_count;
        const auto key=unit.value("key",std::string{});auto it=by_key.find(key);if(it==by_key.end())continue;
        const auto id=it->second->internal_id;
        if(id<0||std::any_of(c.units.begin(),c.units.end(),[&](const auto& u){return u.champion_id==id;}))continue;
        c.units.push_back({id,adapter_detail::role(*it->second),unit.value("is_core",false),std::max(0,unit.value("priority",0))});
      }
      const double coverage=source_count?static_cast<double>(c.units.size())/source_count:0.0;
      if(c.units.empty()||coverage<min_coverage){out.diagnostics.emplace_back("Skipped OP.GG "+c.composition_id+" due to insufficient unit mapping coverage");continue;}
      if(c.units.size()>10){out.diagnostics.emplace_back("Skipped OP.GG "+c.composition_id+" because it exceeds 10 units");continue;}
      c.main_carry_id=adapter_detail::main_carry(c.units);c.target_board_size=c.units.size();
      const auto error=ActiveCompositionManager::validate(c);
      if(!error.empty()){out.diagnostics.emplace_back("Skipped OP.GG "+c.composition_id+": "+error);continue;}
      out.candidates.push_back(std::move(c));
    }
    if(out.candidates.empty())out.diagnostics.emplace_back("OP.GG adapter produced no valid candidates");
    return out;
 }
};

class NativeCompositionAdapter {
public:
 static CompositionAdapterResult adapt(const NativeCompositionSnapshot& input,const std::vector<tft::ChampionDefinition>& pool){
    CompositionAdapterResult out;
    if(input.composition_id.empty()||input.set_id.empty()||input.units.empty()){out.diagnostics.emplace_back("Native input requires composition_id, set_id and units");return out;}
    if(!adapter_detail::compatible_set(input.set_id,pool)){out.diagnostics.emplace_back("Native composition rejected: missing or incompatible Set "+input.set_id);return out;}
    CompositionCandidate c;c.composition_id=input.composition_id;c.source=CompositionSource::Native;c.set_id=input.set_id;c.patch=input.patch;
    c.main_carry_id=input.main_carry_id;c.target_board_size=input.target_board_size?input.target_board_size:input.units.size();
    c.source_score=input.source_score;c.source_reference=input.source_reference;
    for(const auto& selected:input.units){
      auto it=std::find_if(pool.begin(),pool.end(),[&](const auto& d){return d.internal_id==selected.champion_id;});
      if(it==pool.end()){out.diagnostics.emplace_back("Native composition rejected: unknown champion id "+std::to_string(selected.champion_id));return out;}
      if(std::any_of(c.units.begin(),c.units.end(),[&](const auto& u){return u.champion_id==selected.champion_id;})){
        out.diagnostics.emplace_back("Native composition rejected: duplicate champion id "+std::to_string(selected.champion_id));return out;
      }
      const auto champion_set=adapter_detail::champion_set(*it);
      if(!champion_set.empty()&&champion_set!=input.set_id){
        out.diagnostics.emplace_back("Native composition rejected: champion "+std::to_string(selected.champion_id)+" belongs to Set "+champion_set+", not "+input.set_id);return out;
      }
      c.units.push_back({selected.champion_id,adapter_detail::role(*it),selected.core,std::max(0,selected.priority)});
    }
    if(c.main_carry_id<0)c.main_carry_id=adapter_detail::main_carry(c.units);
    const auto error=ActiveCompositionManager::validate(c);
    if(!error.empty()){out.diagnostics.emplace_back("Native composition rejected: "+error);return out;}
    out.candidates.push_back(std::move(c));return out;
 }
};
} // namespace tft::composition_intelligence
