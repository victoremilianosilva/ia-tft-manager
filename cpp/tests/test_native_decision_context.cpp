#include <cassert>
#include <memory>
#include <stdexcept>

#include "lobby/NativeDecisionContext.hpp"

int main() {
    auto snapshot = std::make_shared<tft::AuditSnapshot>();
    snapshot->engine_instance_id = "engine:586";
    snapshot->episode_id = 4;
    snapshot->snapshot_sequence = 9;
    snapshot->round = 12;
    snapshot->shared_pool.contract_id = "tft.shared-champion-pool-snapshot";
    snapshot->shared_pool.contract_version = 2;
    snapshot->shared_pool.catalog_fingerprint = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    snapshot->shared_pool.champions.push_back({7, "TFT_Test", 2, 25, 11});
    snapshot->shared_pool.total_available = 11;
    for (std::size_t i = 0; i < tft::kPlayersPerLobby; ++i) {
        snapshot->player_decision_sequences[i] = 20 + i;
        auto& player = snapshot->players[i];
        player.player_id = static_cast<std::int32_t>(i);
        auto& strategic = player.strategic_state;
        strategic.player_id = player.player_id;
        strategic.episode_id = snapshot->episode_id;
        strategic.player_decision_sequence = snapshot->player_decision_sequences[i];
        strategic.round = snapshot->round;
    }
    snapshot->players[0].board[0].occupied = true;
    snapshot->players[0].board[0].trait_names = {"Trait_A", "Trait_A", "Trait_B"};
    snapshot->players[0].board[0].uuid = "physical-board-copy";
    snapshot->players[0].gold = 37;
    snapshot->players[0].level = 6;
    snapshot->players[0].xp = 8;
    snapshot->players[0].shop_offer_revisions[0] = 19;
    snapshot->players[0].item_inventory = {"TFT_Item_Test"};
    snapshot->players[0].item_component_catalog = {"component:test"};
    snapshot->players[0].equipped_items.push_back({"physical-board-copy", "board", 0, "TFT_Item_Test"});
    snapshot->players[0].bench[0].occupied = true;
    snapshot->players[0].bench[0].trait_names = {"Trait_A", "Trait_C"};

    tft::NativeDecisionContext context(snapshot);
    assert(context.availability() == tft::ContextAvailability::Complete);
    assert(context.player_count() == 8);
    assert(context.shared_pool().contract_version == 2);
    assert(context.shared_pool().catalog_fingerprint == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
    assert(context.shared_pool().total_available == 11);
    assert(context.shared_pool().champions.front().available_count == 11);
    assert(context.player(7).player_id == 7);
    assert(context.player(0).gold == 37 && context.player(0).level == 6);
    assert(context.player(0).board[0].uuid == "physical-board-copy");
    assert(context.player(0).shop_offer_revisions[0] == 19);
    assert(context.player(0).item_inventory.front() == "TFT_Item_Test");
    assert(context.player(0).equipped_items.front().unit_uuid == "physical-board-copy");
    assert(context.strategic_availability(0) == tft::ContextAvailability::Unknown);
    assert(context.item_inventory_availability(0) == tft::ContextAvailability::Complete);
    assert(context.item_inventory_availability(1) == tft::ContextAvailability::Unknown);
    assert(context.pending_anvil_availability(0) == tft::ContextAvailability::NotApplicable);
    const auto traits = context.trait_counts(0);
    assert(traits.size() == 3);
    assert(traits[0].trait_id == "Trait_A");
    assert(traits[0].board_count == 1 && traits[0].bench_count == 1);
    assert(traits[0].board_bench_count == 2);
    assert(traits[0].item_granted_availability == tft::ContextAvailability::Unknown);
    const auto provenance = context.provenance(3);
    assert(provenance.episode_id == 4);
    assert(provenance.snapshot_sequence == 9);
    assert(provenance.player_decision_sequence == 23);

    bool rejected = false;
    try { (void)context.player(8); }
    catch (const std::out_of_range&) { rejected = true; }
    assert(rejected);
    rejected = false;
    try { (void)context.player_sequence_availability(8); }
    catch (const std::out_of_range&) { rejected = true; }
    assert(rejected);

    auto stale = std::make_shared<tft::AuditSnapshot>(*snapshot);
    stale->players[2].strategic_state.player_decision_sequence = 999;
    tft::NativeDecisionContext stale_context(stale);
    assert(stale_context.strategic_availability(2) == tft::ContextAvailability::Stale);

    auto missing_sequence = std::make_shared<tft::AuditSnapshot>(*snapshot);
    missing_sequence->player_decision_sequences[4] = 0;
    tft::NativeDecisionContext missing_context(missing_sequence);
    assert(missing_context.player_sequence_availability(4) == tft::ContextAvailability::Missing);
    assert(missing_context.strategic_availability(4) == tft::ContextAvailability::Stale);

    auto empty_inventory = std::make_shared<tft::AuditSnapshot>(*snapshot);
    empty_inventory->players[0].item_component_catalog = {"component:test"};
    tft::NativeDecisionContext empty_context(empty_inventory);
    assert(empty_context.item_inventory_availability(0) == tft::ContextAvailability::Empty);

    auto retired_inventory = std::make_shared<tft::AuditSnapshot>(*snapshot);
    retired_inventory->players[0].item_ownership_retired = true;
    tft::NativeDecisionContext retired_context(retired_inventory);
    assert(retired_context.item_inventory_availability(0) == tft::ContextAvailability::Incompatible);

    auto no_catalog = std::make_shared<tft::AuditSnapshot>(*snapshot);
    no_catalog->shared_pool.catalog_fingerprint.clear();
    tft::NativeDecisionContext no_catalog_context(no_catalog);
    assert(no_catalog_context.availability() == tft::ContextAvailability::Incompatible);

    auto partial_anvil = std::make_shared<tft::AuditSnapshot>(*snapshot);
    partial_anvil->players[0].pending_anvil = true;
    partial_anvil->players[0].pending_anvil_sequence = 4;
    tft::NativeDecisionContext partial_context(partial_anvil);
    assert(partial_context.pending_anvil_availability(0) == tft::ContextAvailability::Partial);

    auto incompatible = std::make_shared<tft::AuditSnapshot>(*snapshot);
    incompatible->contract_version = 7;
    rejected = false;
    try { tft::NativeDecisionContext invalid(incompatible); }
    catch (const std::invalid_argument&) { rejected = true; }
    assert(rejected);
    return 0;
}
