#include "combat/CombatTraitCatalog.hpp"

#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {
void require(bool condition, const char* message) {
    if (!condition) throw std::runtime_error(message);
}
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: test_trait_combat_catalog <catalog.json>\n";
        return 2;
    }

    try {
        std::ifstream input(argv[1]);
        require(static_cast<bool>(input), "Could not open Set 18 trait combat catalog.");
        const auto catalog = tft::combat::load_trait_combat_catalog(input);
        require(catalog.set_id == "Set18", "Trait combat catalog must target Set18.");
        require(catalog.traits.size() == 36,
                "Every source Set 18 trait must be registered in the combat catalog.");

        const auto find = [&](const std::string& api_name)
            -> const tft::combat::TraitCombatDefinition& {
            const auto found = catalog.traits.find(api_name);
            require(found != catalog.traits.end(), "Expected trait is missing from catalog.");
            return found->second;
        };

        for (const auto* api_name : {
                 "DA_18_Brawler", "DA_18_Defender", "DA_18_Blossom",
                 "DA_18_Invoker", "DA_Juggernaut18"}) {
            const auto& trait = find(api_name);
            require(trait.effects_complete && !trait.tiers.empty(),
                    "A fully mapped trait must expose complete tier effects.");
            for (const auto& tier : trait.tiers)
                require(!tier.effects.empty(),
                        "Every tier of a complete combat trait must have effects.");
        }

        const auto& invoker = find("DA_18_Invoker");
        require(invoker.tiers.size() == 4 &&
                invoker.tiers.front().effects.size() == 2,
                "Invoker must expose team and self mana regeneration at each tier.");
        require(invoker.tiers.front().effects.front().operation == "mana_regen" &&
                invoker.tiers.front().effects.front().target == "allies" &&
                invoker.tiers.front().effects.front().scale_by_active_trait_count,
                "Invoker team mana regeneration must be represented as a scaled team aura.");

        for (const auto* api_name : {
                 "DA_18_Coven", "DA_18_LuxUniqueTrait",
                 "DA_DravenUniqueTrait18"}) {
            const auto& trait = find(api_name);
            require(trait.effects_complete && !trait.tiers.empty(),
                    "A non-combat trait must be explicitly complete for combat scope.");
            for (const auto& tier : trait.tiers)
                require(tier.effects.empty(),
                        "Non-combat traits must not invent combat effects.");
        }

        const auto& slayer = find("DA_18_Slayer");
        require(!slayer.effects_complete && !slayer.tiers.empty() &&
                !slayer.tiers.front().effects.empty(),
                "Partially modeled traits must remain explicitly incomplete.");

        const auto& executioner = find("DA_18_Executioner");
        require(!executioner.effects_complete && executioner.tiers.size() == 3,
                "Executioner must remain partial while its bleed effect is unsupported.");
        for (const auto& tier : executioner.tiers)
            require(tier.effects.size() == 1 &&
                    tier.effects.front().stat == "critical_strike_chance" &&
                    std::abs(tier.effects.front().value - 0.15f) < 0.0001f,
                    "Executioner critical-strike chance must be normalized at every tier.");

        const auto& spellweaver = find("DA_18_Spellweaver");
        require(!spellweaver.effects_complete && spellweaver.tiers.size() == 3,
                "Spellweaver must remain partial until AP-per-cast stacking is implemented.");
        for (const auto& tier : spellweaver.tiers)
            require(tier.effects.size() == 2 &&
                    tier.effects.front().target == "allies" &&
                    tier.effects.front().scale_by_active_trait_count,
                    "Spellweaver team AP aura and holder bonus must be normalized.");

        const auto& zyra = find("DA_18_ZyraUniqueTrait");
        require(!zyra.effects_complete && zyra.tiers.front().effects.size() == 1 &&
                zyra.tiers.front().effects.front().stat == "damage_reduction",
                "Zyra base team durability must be mapped without claiming its plant condition.");

        const auto& riftbeast = find("DA_Riftbeast18");
        require(!riftbeast.effects_complete && riftbeast.tiers.size() == 4 &&
                riftbeast.tiers[2].effects.size() == 6 &&
                riftbeast.tiers[3].effects.size() == 6,
                "Riftbeast tier-7 and tier-10 growth effects must be normalized.");
        require(std::all_of(riftbeast.tiers[2].effects.begin(),
                    riftbeast.tiers[2].effects.end(), [](const auto& effect) {
                        return effect.trigger == "combat_start" ||
                            (effect.trigger == "periodic" &&
                             std::abs(effect.interval - 5.0f) < 0.0001f);
                    }),
                "Riftbeast growth must include combat-start and five-second effects.");

        std::cout << "Loaded " << catalog.traits.size()
                  << " Set 18 traits; complete combat mappings: 5; non-combat traits: 3; partial mappings: 5.\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "Trait combat catalog validation failed: "
                  << error.what() << '\n';
        return 1;
    }
}
