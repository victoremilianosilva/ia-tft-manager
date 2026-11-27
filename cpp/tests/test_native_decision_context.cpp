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

    tft::NativeDecisionContext context(snapshot);
    assert(context.availability() == tft::ContextAvailability::Complete);
    assert(context.player_count() == 8);
    assert(context.shared_pool().contract_version == 2);
    assert(context.player(7).player_id == 7);
    const auto provenance = context.provenance(3);
    assert(provenance.episode_id == 4);
    assert(provenance.snapshot_sequence == 9);
    assert(provenance.player_decision_sequence == 23);

    bool rejected = false;
    try { (void)context.player(8); }
    catch (const std::out_of_range&) { rejected = true; }
    assert(rejected);

    auto stale = std::make_shared<tft::AuditSnapshot>(*snapshot);
    stale->players[2].strategic_state.player_decision_sequence = 999;
    rejected = false;
    try { tft::NativeDecisionContext invalid(stale); }
    catch (const std::invalid_argument&) { rejected = true; }
    assert(rejected);

    auto incompatible = std::make_shared<tft::AuditSnapshot>(*snapshot);
    incompatible->contract_version = 7;
    rejected = false;
    try { tft::NativeDecisionContext invalid(incompatible); }
    catch (const std::invalid_argument&) { rejected = true; }
    assert(rejected);
    return 0;
}
