#include "lobby/ChampionCatalog.hpp"
#include "lobby/ShopEngine.hpp"
#include "lobby/UnitInstanceFactory.hpp"
#include "lobby/UnitPool.hpp"
#include <iostream>
#include <stdexcept>
namespace { void require(bool ok,const char* msg){if(!ok)throw std::runtime_error(msg);} }
int main(int argc,char** argv){
 try{
  require(argc==2,"Informe units_gerado.json.");
  tft::ChampionCatalog catalog(argv[1]); tft::UnitPool pool(catalog);
  tft::UnitInstanceFactory factory(catalog,1234); tft::ShopEngine shop(pool,factory,9876);
  const auto initial=pool.total_available(); shop.roll(2);
  require(pool.validate(),"Pool inválido após roll.");
  std::size_t occupied=0;
  for(const auto& offer:shop.offers()) if(offer){
   ++occupied; require(offer->is_valid(),"Oferta inválida.");
   const auto* def=catalog.find_by_id(offer->champion_internal_id);
   require(def && (def->cost==1||def->cost==2),"Custo inválido para nível 2.");
  }
  require(occupied>0 && pool.total_available()<initial,"Loja não retirou cópias do pool.");
  const auto* first=shop.get_unit(0); const auto uuid=first?first->uuid:std::string{};
  shop.set_locked(true); const auto stock=pool.total_available(); shop.roll(10);
  require(pool.total_available()==stock,"Loja bloqueada alterou estoque.");
  const auto* after=shop.get_unit(0); require((after?after->uuid:std::string{})==uuid,"Loja bloqueada mudou oferta.");
  shop.reroll(2); require(shop.is_locked(),"Reroll deve manter bloqueio.");
  require(pool.validate(),"Pool inválido após reroll.");
  std::int32_t slot=-1;
  for(std::int32_t i=0;i<static_cast<std::int32_t>(tft::kShopSlots);++i)if(shop.get_unit(i)){slot=i;break;}
  require(slot>=0,"Reroll não gerou oferta.");
  const auto id=shop.get_unit(slot)->champion_internal_id; const auto before=pool.available(id);
  require(shop.take_unit(slot).has_value(),"Compra falhou.");
  require(!shop.get_unit(slot)&&pool.available(id)==before,"Compra devolveu cópia ao pool ou não limpou slot.");
  require(!shop.take_unit(slot),"Slot permitiu compra duplicada.");
  shop.reset(); require(!shop.is_locked()&&pool.validate(),"Reset da loja inválido.");
  std::cout<<"ShopEngine: OK\n"; return 0;
 }catch(const std::exception& e){std::cerr<<"ShopEngine: FALHOU: "<<e.what()<<'\n';return 1;}
}
