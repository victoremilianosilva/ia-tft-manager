#pragma once

#include "lobby/TftEngine.hpp"

#include <cstddef>
#include <cstdint>
#include <memory>
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
            snapshot_->engine_instance_id.empty()) {
            return ContextAvailability::Incompatible;
        }
        return ContextAvailability::Complete;
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
            if (snapshot_->player_decision_sequences[i] == 0) {
                throw std::invalid_argument("Native decision context player sequence is missing");
            }
            const auto& strategic = state.strategic_state;
            if (strategic.player_id != state.player_id ||
                strategic.episode_id != snapshot_->episode_id ||
                strategic.player_decision_sequence != snapshot_->player_decision_sequences[i] ||
                strategic.round != snapshot_->round) {
                throw std::invalid_argument("Native strategic context is not correlated to decision snapshot");
            }
        }
    }

    std::shared_ptr<const AuditSnapshot> snapshot_;
};

} // namespace tft
