#include "lobby/ShopEngine.hpp"
#include <algorithm>
#include <map>
#include <stdexcept>
#include <utility>
#include "lobby/ChampionCatalog.hpp"
namespace tft {
ShopEngine::ShopEngine(UnitPool& pool, UnitInstanceFactory& factory, std::uint64_t seed)
    : pool_(pool), factory_(factory), rng_(seed) {}
const std::array<std::array<double, 5>, 10>& ShopEngine::odds_by_level() {
    static const std::array<std::array<double, 5>, 10> odds{{
        {{1.00,0.00,0.00,0.00,0.00}}, {{1.00,0.00,0.00,0.00,0.00}},
        {{0.75,0.25,0.00,0.00,0.00}}, {{0.55,0.30,0.15,0.00,0.00}},
        {{0.45,0.33,0.20,0.02,0.00}}, {{0.30,0.40,0.25,0.05,0.00}},
        {{0.16,0.30,0.43,0.10,0.01}}, {{0.15,0.20,0.32,0.30,0.03}},
        {{0.10,0.17,0.25,0.33,0.15}}, {{0.05,0.10,0.20,0.40,0.25}}
    }};
    return odds;
}
std::int32_t ShopEngine::roll_cost(std::int32_t level) {
    const auto safe_level = std::clamp(level, 1, 10);
    const auto& weights = odds_by_level()[static_cast<std::size_t>(safe_level - 1)];
    std::discrete_distribution<std::int32_t> dist(weights.begin(), weights.end());
    return dist(rng_) + 1;
}
std::optional<UnitInstance> ShopEngine::draw(std::int32_t cost) {
    const auto id = pool_.draw_by_cost(cost, rng_);
    if (!id) return std::nullopt;
    try { return factory_.create(*id); }
    catch (...) { pool_.give_back(*id); throw; }
}
void ShopEngine::roll(std::int32_t level, bool force) {
    if (locked_ && !force) return;
    if (next_roll_for_testing_ && next_roll_for_testing_->size() != kShopSlots)
        throw std::invalid_argument("Fixture de reroll deve conter exatamente cinco campeoes.");

    const auto previous_offers = offers_;
    return_current_shop();

    if (next_roll_for_testing_) {
        const auto ids = *next_roll_for_testing_;
        std::map<std::int32_t, std::int32_t> required;
        for (const auto id : ids) ++required[id];
        for (const auto& [id, count] : required) {
            if (pool_.available(id) < count) {
                for (const auto& offer : previous_offers) {
                    if (offer && !pool_.take(offer->champion_internal_id))
                        throw std::logic_error("Falha ao restaurar loja apos fixture invalida.");
                }
                offers_ = previous_offers;
                throw std::invalid_argument("Fixture de reroll excede o estoque disponivel.");
            }
        }

        std::vector<std::int32_t> taken;
        try {
            for (std::size_t slot = 0; slot < kShopSlots; ++slot) {
                if (!pool_.take(ids[slot]))
                    throw std::invalid_argument("Campeao indisponivel na fixture de reroll.");
                taken.push_back(ids[slot]);
                offers_[slot] = factory_.create(ids[slot]);
            }
        } catch (...) {
            for (const auto id : taken) (void)pool_.give_back(id);
            offers_ = {};
            for (const auto& offer : previous_offers) {
                if (offer && !pool_.take(offer->champion_internal_id))
                    throw std::logic_error("Falha ao restaurar loja apos erro na fixture.");
            }
            offers_ = previous_offers;
            throw;
        }
        next_roll_for_testing_.reset();
        return;
    }

    for (auto& offer : offers_) offer = draw(roll_cost(level));
}
void ShopEngine::reroll(std::int32_t level) { roll(level, true); }
bool ShopEngine::set_locked(bool locked) noexcept {
    const bool changed = locked_ != locked; locked_ = locked; return changed;
}
bool ShopEngine::toggle_lock() noexcept { locked_ = !locked_; return locked_; }
bool ShopEngine::is_locked() const noexcept { return locked_; }
const std::array<std::optional<UnitInstance>, kShopSlots>& ShopEngine::offers() const noexcept { return offers_; }
const UnitInstance* ShopEngine::get_unit(std::int32_t slot) const noexcept {
    if (slot < 0 || static_cast<std::size_t>(slot) >= offers_.size()) return nullptr;
    const auto& offer = offers_[static_cast<std::size_t>(slot)];
    return offer ? &*offer : nullptr;
}
std::optional<UnitInstance> ShopEngine::take_unit(std::int32_t slot) noexcept {
    if (slot < 0 || static_cast<std::size_t>(slot) >= offers_.size()) return std::nullopt;
    auto& offer = offers_[static_cast<std::size_t>(slot)];
    if (!offer) return std::nullopt;
    auto result = std::move(offer); offer.reset(); return result;
}
void ShopEngine::return_current_shop() {
    for (auto& offer : offers_) {
        if (!offer) continue;
        if (!pool_.give_back(offer->champion_internal_id))
            throw std::logic_error("Falha ao devolver oferta: estoque inconsistente.");
        offer.reset();
    }
}
bool ShopEngine::set_offer_for_testing(std::int32_t slot, UnitInstance unit) {
    if (slot < 0 || static_cast<std::size_t>(slot) >= kShopSlots ||
        unit.champion_internal_id < 0)
        return false;
    const auto index = static_cast<std::size_t>(slot);
    if (offers_[index] &&
        offers_[index]->champion_internal_id == unit.champion_internal_id)
        return true;
    if (!pool_.take(unit.champion_internal_id)) return false;
    if (offers_[index] && !pool_.give_back(offers_[index]->champion_internal_id)) {
        (void)pool_.give_back(unit.champion_internal_id);
        return false;
    }
    offers_[index] = std::move(unit);
    return true;
}

bool ShopEngine::set_next_roll_for_testing(
    const std::vector<std::int32_t>& champion_internal_ids
) {
    if (champion_internal_ids.size() != kShopSlots) return false;
    if (std::any_of(champion_internal_ids.begin(), champion_internal_ids.end(),
                    [](std::int32_t id) { return id < 0; }))
        return false;
    next_roll_for_testing_ = champion_internal_ids;
    return true;
}

void ShopEngine::reset() {
    return_current_shop();
    locked_ = false;
    next_roll_for_testing_.reset();
}
} // namespace tft
