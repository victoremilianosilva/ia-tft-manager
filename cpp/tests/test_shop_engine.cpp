#include "lobby/ChampionCatalog.hpp"
#include "lobby/ShopEngine.hpp"
#include "lobby/UnitInstanceFactory.hpp"
#include "lobby/UnitPool.hpp"
#include <iostream>
#include <cmath>
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
  std::array<std::string, tft::kShopSlots> locked_uuids{};
  for(std::size_t i=0;i<tft::kShopSlots;++i){
   const auto* offer=shop.get_unit(static_cast<std::int32_t>(i));
   locked_uuids[i]=offer?offer->uuid:std::string{};
  }
  shop.set_locked(true); const auto stock=pool.total_available(); shop.roll(10);
  require(pool.total_available()==stock,"Loja bloqueada alterou estoque.");
  for(std::size_t i=0;i<tft::kShopSlots;++i){
   const auto* offer=shop.get_unit(static_cast<std::int32_t>(i));
   require((offer?offer->uuid:std::string{})==locked_uuids[i],
           "Loja bloqueada mudou uma das ofertas.");
  }
  // As probabilidades por nível devem espelhar GameConfig.SHOP_ODDS.
  const std::array<std::array<double, 5>, 10> expected_odds{{
   {{1.00,0.00,0.00,0.00,0.00}}, {{1.00,0.00,0.00,0.00,0.00}},
   {{0.75,0.25,0.00,0.00,0.00}}, {{0.55,0.30,0.15,0.00,0.00}},
   {{0.45,0.33,0.20,0.02,0.00}}, {{0.30,0.40,0.25,0.05,0.00}},
   {{0.19,0.30,0.40,0.10,0.01}}, {{0.15,0.20,0.32,0.30,0.03}},
   {{0.10,0.17,0.25,0.33,0.15}}, {{0.05,0.10,0.20,0.40,0.25}}
  }};
  require(tft::ShopEngine::odds_by_level() == expected_odds,
          "Odds da loja divergem da tabela Set 18.");
  for (std::size_t level = 0; level < expected_odds.size(); ++level) {
   double total_probability = 0.0;
   for (const auto probability : expected_odds[level]) {
    require(probability >= 0.0 && probability <= 1.0,
            "Probabilidade de custo fora do intervalo [0,1].");
    total_probability += probability;
   }
   require(std::abs(total_probability - 1.0) < 1e-9,
           "As probabilidades por nível não somam 100%.");
  }
  require(expected_odds[6] == std::array<double, 5>{{0.19,0.30,0.40,0.10,0.01}},
          "Nível 7 deve usar 19/30/40/10/1 no Set 18.");
  require(expected_odds[9] == std::array<double, 5>{{0.05,0.10,0.20,0.40,0.25}},
          "Nível 10 deve manter 5/10/20/40/25 no Set 18.");
  for (int level=1; level<=10; ++level) {
   shop.reroll(level);
   require(pool.validate(),"Pool inválido após reroll por nível.");
   for (const auto& offer: shop.offers()) if (offer) {
    const auto* def=catalog.find_by_id(offer->champion_internal_id);
    require(def!=nullptr,"Oferta referencia campeão ausente.");
    const auto cost_index=static_cast<std::size_t>(def->cost-1);
    require(cost_index<5 && expected_odds[static_cast<std::size_t>(level-1)][cost_index]>0.0,
            "Loja gerou custo com probabilidade zero para o nível.");
   }
  }

  // Verifica também a distribuição efetivamente usada pelo roll_cost,
  // e não apenas os valores estáticos da tabela.
  constexpr std::int32_t kLevelSevenRolls = 3000;
  std::array<std::int32_t, 5> observed_costs{};
  for (std::int32_t roll = 0; roll < kLevelSevenRolls; ++roll) {
   shop.reroll(7);
   for (const auto& offer : shop.offers()) {
    require(offer.has_value(), "Roll de nível 7 deixou slot vazio com pool disponível.");
    const auto* def = catalog.find_by_id(offer->champion_internal_id);
    require(def && def->cost >= 1 && def->cost <= 5,
            "Roll de nível 7 gerou campeão com custo inválido.");
    ++observed_costs[static_cast<std::size_t>(def->cost - 1)];
   }
  }
  const auto total_slots = static_cast<double>(kLevelSevenRolls * tft::kShopSlots);
  for (std::size_t cost = 0; cost < 5; ++cost) {
   const auto expected_count = total_slots * expected_odds[6][cost];
   const auto tolerance = total_slots * 0.035; // margem estatística de 3,5 p.p.
   require(std::abs(static_cast<double>(observed_costs[cost]) - expected_count) <= tolerance,
           "Frequência observada de custo divergiu das odds do nível 7.");
  }

  // O reroll manual força a renovação, mas não altera o estado do lock.
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
