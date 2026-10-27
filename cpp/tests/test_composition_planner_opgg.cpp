#include "strategy/CompositionPlanner.hpp"

#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using tft::ChampionDefinition;
using tft::strategy::CompositionPlanner;

static ChampionDefinition make_champion(int id, const std::string& api_name,
                                        int role, std::vector<std::string> traits) {
    ChampionDefinition value;
    value.internal_id = id;
    value.api_name = api_name;
    value.character_name = api_name;
    value.name = api_name;
    value.cost = role == 1 ? 4 : 2;
    value.role = role;
    value.combat_profile.role = role;
    value.traits = std::move(traits);
    return value;
}

static std::string utc_now() {
    const auto now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
    std::tm utc{};
#if defined(_WIN32)
    gmtime_s(&utc, &now);
#else
    gmtime_r(&now, &utc);
#endif
    char buffer[32]{};
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%SZ", &utc);
    return buffer;
}

static bool configure_catalog(const std::filesystem::path& path, bool incompatible) {
    std::ofstream out(path);
    if (!out) return false;
    const std::string set_code = incompatible ? "TFTSet17" : "TFTSet18";
    out << "{\"schema_version\":1,\"source\":\"op.gg\","
        << "\"fetched_at\":\"" << utc_now() << "\",\"compositions\":[{"
        << "\"name\":\"Live item and position fixture\","
        << "\"team_code\":\"fixture" << set_code << "\","
        << "\"units\":[";
    const std::vector<std::string> names{
        "DA_18_Tank", "DA_18_Carry", "DA_18_Support",
        "DA_18_Fighter", "DA_18_Assassin"
    };
    for (std::size_t i = 0; i < names.size(); ++i) {
        if (i) out << ",";
        out << "{\"key\":\"" << names[i]
            << "\",\"is_core\":true,\"priority\":" << (i + 1)
            << ",\"traits\":[\"Invoker\"],\"items\":[\"DA_Deathblade\"],\"cell\":{\"x\":"
            << (i % 7) << ",\"y\":" << (i / 7) << "}}";
    }
    out << "],\"early_game\":{\"units\":[{\"key\":\"DA_18_Tank\"}]},"
        << "\"mid_game\":{\"units\":[{\"key\":\"DA_18_Tank\"}]},"
        << "\"statistics\":{\"deck\":{\"totalCount\":2500,\"top4Rate\":0.95},"
        << "\"label\":{\"totalCount\":0,\"top4Rate\":0.0}}}]}";
    out.close();
#if defined(_WIN32)
    return _putenv_s("TFT_OPGG_META_CATALOG", path.string().c_str()) == 0;
#else
    return setenv("TFT_OPGG_META_CATALOG", path.string().c_str(), 1) == 0;
#endif
}

int main(int argc, char** argv) {
    const bool incompatible = argc > 1 && std::string(argv[1]) == "incompatible";
    const auto path = std::filesystem::temp_directory_path() /
        (incompatible ? "tft_opgg_incompatible_fixture.json" : "tft_opgg_selection_fixture.json");
    if (!configure_catalog(path, incompatible)) {
        std::cerr << "could not configure OP.GG fixture catalog\n";
        return 2;
    }

    std::vector<ChampionDefinition> pool{
        make_champion(1, "DA_18_Tank", 0, {"Invoker", "Frontline"}),
        make_champion(2, "DA_18_Carry", 1, {"Invoker", "Carry"}),
        make_champion(3, "DA_18_Support", 2, {"Invoker", "Support"}),
        make_champion(4, "DA_18_Fighter", 3, {"Invoker", "Frontline"}),
        make_champion(5, "DA_18_Assassin", 4, {"Invoker", "Damage"})
    };
    const CompositionPlanner::TraitMilestones milestones{
        {"Invoker", {2, 4, 6}}, {"Frontline", {2, 4}}, {"Carry", {2}},
        {"Support", {2}}, {"Damage", {2}}
    };
    const CompositionPlanner::OwnedCopies owned{{1, 1}, {2, 1}, {3, 1}, {4, 1}, {5, 1}};
    const CompositionPlanner::FocusWeights focus{{"Invoker", 5.0}};
    CompositionPlanner::LiveUnitContext live;
    for (int id = 1; id <= 5; ++id) {
        live.equipped_items_by_champion[id] = {"TFT_Item_Deathblade"};
        live.board_slot_by_champion[id] = id - 1;
    }
    live.inventory_item_ids.insert("TFT_Item_Deathblade");

    const auto native_fallback = CompositionPlanner::build(
        pool, milestones, "Invoker", focus, owned, 5, 8, {}, {}, nullptr);
    const auto fallback_audit = std::find_if(
        native_fallback.acquisition_notes.begin(), native_fallback.acquisition_notes.end(),
        [](const std::string& note) { return note.find("OPGG_META_AUDIT:") == 0; });
    if (fallback_audit == native_fallback.acquisition_notes.end() ||
        fallback_audit->find("status=candidate_below_native_margin") == std::string::npos) {
        std::cerr << "meta candidate without viable item/position context should fall back: "
                  << (fallback_audit == native_fallback.acquisition_notes.end()
                      ? "no audit note" : *fallback_audit) << '\\n';
        return 6;
    }

    const auto plan = CompositionPlanner::build(
        pool, milestones, "Invoker", focus, owned, 5, 8, {}, {}, &live);
    const auto audit = std::find_if(plan.acquisition_notes.begin(), plan.acquisition_notes.end(),
        [](const std::string& note) { return note.find("OPGG_META_AUDIT:") == 0; });
    if (audit == plan.acquisition_notes.end()) {
        std::cerr << "planner did not emit OPGG_META_AUDIT\n";
        return 3;
    }
    if (incompatible) {
        if (audit->find("status=incompatible_set") == std::string::npos ||
            audit->find("status=selected") != std::string::npos) {
            std::cerr << "incompatible set must fall back to native planner: " << *audit << '\n';
            return 4;
        }
    } else if (audit->find("status=selected") == std::string::npos) {
        std::cerr << "contextual OP.GG candidate should be selected in the fixture: " << *audit << '\n';
        return 5;
    }
    std::filesystem::remove(path);
    std::cout << "OP.GG planner " << (incompatible ? "fallback" : "selection") << " test passed\n";
    return 0;
}
