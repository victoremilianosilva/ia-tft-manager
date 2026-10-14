#include "lobby/ShopEngine.hpp"
#include <algorithm>
#include <stdexcept>
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
    return_current_shop();
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
        if (!pool_.give_back(offer->champion_internal_id)
            throw std::logic_error("Falha ao devolver oferta: estoque inconsistente.");
        offer.reset();
    }
}
void ShopEngine::reset() { return_current_shop(); locked_ = false; }
} // namespace tft
