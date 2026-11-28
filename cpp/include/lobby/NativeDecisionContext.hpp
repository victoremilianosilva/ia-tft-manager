#pragma once

#include "lobby/TftEngine.hpp"

#include <cstddef>
#include <cstdint>
#include <memory>
#include <map>
#include <unordered_set>
#include <stdexcept>
#include <string>

namespace tft {

// Explicit availability prevents a default numeric value from being confused
// with an observed zero. This status is metadata, never a policy feature.
enum class ContextAvailability : std::uint8_t {
    Complete,
    Partial,
    Empty,
    Unknown,
    Missing,
    Stale,
    Incompatible,
    NotApplicable
};

struct NativeTraitCount {
    std::string trait_id;
    std::uint32_t board_count{0};
    std::uint32_t bench_count{0};
    std::uint32_t board_bench_count{0};
    // AuditUnitSnapshot::trait_names is static catalog membership. The current
    // Engine does not publish item-granted trait ownership as a separate fact.
    ContextAvailability item_granted_availability{ContextAvailability::Unknown};
};

struct ContextProvenance {
    std::string producer;
    std::string source_namespace;
    std::uint32_t contract_version{0};
    std::uint64_t episode_id{0};
    std::uint64_t snapshot_sequence{0};
    std::uint64_t player_decision_sequence{0};
};

// Immutable, owner-backed view over the exact AuditSnapshot captured with the
// observation/mask decision. It deliberately references the snapshot rather
// than copying lobby/player/item structures into a second schema.
class NativeDecisionContext final {
public:
    explicit NativeDecisionContext(
        std::shared_ptr<const AuditSnapshot> snapshot
    ) : snapshot_(std::move(snapshot)) {
        if (!snapshot_) {
            throw std::invalid_argument("NativeDecisionContext requires an owned snapshot");
        }
        validate_identity();
    }

    const AuditSnapshot& snapshot() const noexcept { return *snapshot_; }
    const AuditSharedPoolSnapshot& shared_pool() const noexcept {
        return snapshot_->shared_pool;
    }
    const AuditPlayerSnapshot& player(std::size_t index) const {
        if (index >= kPlayersPerLobby) {
            throw std::out_of_range("NativeDecisionContext player index out of range");
        }
        return snapshot_->players[index];
    }
    std::size_t player_count() const noexcept { return kPlayersPerLobby; }

    ContextProvenance provenance(std::size_t player_index) const {
        const auto& state = player(player_index);
        return ContextProvenance{
            snapshot_->producer,
            snapshot_->source_namespace,
            snapshot_->contract_version,
            snapshot_->episode_id,
            snapshot_->snapshot_sequence,
            snapshot_->player_decision_sequences[player_index]
        };
    }

    ContextAvailability availability() const noexcept {
        if (snapshot_->contract_id != "tft.native-state-snapshot" ||
            snapshot_->contract_version != 6 ||
            snapshot_->engine_instance_id.empty() ||
            snapshot_->shared_pool.contract_id != "tft.shared-champion-pool-snapshot" ||
            snapshot_->shared_pool.contract_version != 2 ||
            snapshot_->shared_pool.catalog_fingerprint.size() != 64) {
            return ContextAvailability::Incompatible;
        }
        return ContextAvailability::Complete;
    }

    ContextAvailability player_sequence_availability(std::size_t player_index) const {
        (void)player(player_index);
        return snapshot_->player_decision_sequences[player_index] == 0
            ? ContextAvailability::Missing
            : ContextAvailability::Complete;
    }

    ContextAvailability strategic_availability(std::size_t player_index) const {
        const auto& state = player(player_index);
        const auto& strategic = state.strategic_state;
        if (strategic.player_id != state.player_id ||
            strategic.episode_id != snapshot_->episode_id ||
            strategic.player_decision_sequence != snapshot_->player_decision_sequences[player_index] ||
            strategic.round != snapshot_->round) {
            return ContextAvailability::Stale;
        }
        return strategic.planner_outputs_valid
            ? ContextAvailability::Complete
            : ContextAvailability::Unknown;
    }

    ContextAvailability item_inventory_availability(std::size_t player_index) const {
        const auto& state = player(player_index);
        if (state.item_ownership_retired) {
            return ContextAvailability::Incompatible;
        }
        if (state.item_component_catalog.empty()) {
            return ContextAvailability::Unknown;
        }
        if (state.item_components.empty() && state.item_inventory.empty() &&
            state.equipped_items.empty()) {
            return ContextAvailability::Empty;
        }
        return ContextAvailability::Complete;
    }

    ContextAvailability pending_anvil_availability(std::size_t player_index) const {
        const auto& state = player(player_index);
        if (!state.pending_anvil) {
            return state.pending_anvil_sequence == 0 &&
                state.pending_anvil_options.empty()
                ? ContextAvailability::NotApplicable
                : ContextAvailability::Incompatible;
        }
        if (state.pending_anvil_sequence == 0 || state.pending_anvil_options.empty()) {
            return ContextAvailability::Partial;
        }
        return ContextAvailability::Complete;
    }

    std::vector<NativeTraitCount> trait_counts(std::size_t player_index) const {
        const auto& state = player(player_index);
        struct Counts { std::uint32_t board{0}; std::uint32_t bench{0}; };
        std::map<std::string, Counts> counts;
        const auto accumulate = [&counts](
            const auto& slots, bool on_board
        ) {
            for (const auto& unit : slots) {
                if (!unit.occupied) continue;
                std::unordered_set<std::string> unique_traits;
                for (const auto& trait : unit.trait_names) {
                    if (trait.empty() || !unique_traits.insert(trait).second) continue;
                    auto& value = counts[trait];
                    if (on_board) ++value.board;
                    else ++value.bench;
                }
            }
        };
        accumulate(state.board, true);
        accumulate(state.bench, false);
        std::vector<NativeTraitCount> result;
        result.reserve(counts.size());
        for (const auto& [trait, value] : counts) {
            result.push_back(NativeTraitCount{
                trait, value.board, value.bench, value.board + value.bench,
                ContextAvailability::Unknown
            });
        }
        return result;
    }

private:
    void validate_identity() const {
        if (snapshot_->contract_id != "tft.native-state-snapshot" ||
            snapshot_->contract_version != 6) {
            throw std::invalid_argument("Unsupported native decision context contract");
        }
        if (snapshot_->engine_instance_id.empty() || snapshot_->snapshot_sequence == 0) {
            throw std::invalid_argument("Native decision context identity is incomplete");
        }
        if (snapshot_->shared_pool.contract_id != "tft.shared-champion-pool-snapshot" ||
            snapshot_->shared_pool.contract_version != 2) {
            throw std::invalid_argument("Native shared pool snapshot contract mismatch");
        }
        for (std::size_t i = 0; i < kPlayersPerLobby; ++i) {
            const auto& state = snapshot_->players[i];
            if (state.player_id != static_cast<std::int32_t>(i)) {
                throw std::invalid_argument("Native decision context player ordering mismatch");
            }
            // Player sequence and strategic-owner correlation are surfaced as
            // field availability below; do not erase a stale/missing record by
            // failing the whole immutable lobby context.
        }
    }

    std::shared_ptr<const AuditSnapshot> snapshot_;
};

} // namespace tft
