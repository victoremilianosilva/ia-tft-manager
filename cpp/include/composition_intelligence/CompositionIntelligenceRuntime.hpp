#pragma once

#include "composition_intelligence/CompositionDiagnostics.hpp"

#include <cstdint>
#include <string>
#include <utility>
#include <vector>

namespace tft::composition_intelligence {

// State and lifecycle for one player's Shadow pipeline. One instance must be
// owned by each player; no mutable planner/recorder state is shared.
class CompositionIntelligencePlayerRuntime {
public:
    ActiveCompositionManager active;
    TransitionManager transitions;
    CompositionDiagnosticRecorder recorder;
    std::vector<nlohmann::json> snapshots;

    void begin_cycle(std::uint64_t match_id, std::int32_t player_id,
                     std::uint32_t round) {
        match_id_ = match_id;
        player_id_ = player_id;
        round_ = round;
        stage_trace_.clear();
        next_stage_sequence_ = 0;
    }

    void mark_stage(std::string name, std::string status, std::string reason = {},
                    const std::optional<ActiveComposition>& active_composition = std::nullopt) {
        nlohmann::json stage = {
            {"stage", std::move(name)},
            {"status", std::move(status)},
            {"reason", std::move(reason)},
            {"match_id", match_id_},
            {"player_id", player_id_},
            {"round", round_},
            {"stage_sequence", ++next_stage_sequence_},
            {"composition_id", active_composition
                ? active_composition->candidate.composition_id : std::string{}},
            {"composition_version", active_composition
                ? active_composition->version : std::uint64_t{0}}
        };
        stage_trace_.push_back(std::move(stage));
    }

    std::uint64_t next_player_sequence() const noexcept {
        return player_sequence_ + 1;
    }

    // Attach a deterministic execution trace and stable player/match identity.
    // Duplicate snapshots are detected after removing wall-clock/global sequence
    // fields, so repeated evaluation of unchanged state does not flood the log.
    bool append_snapshot(nlohmann::json snapshot) {
        snapshot["match_id"] = match_id_;
        snapshot["player_id"] = player_id_;
        snapshot["round"] = round_;
        snapshot["player_sequence"] = next_player_sequence();
        snapshot["runtime_execution"] = {
            {"match_id", match_id_},
            {"player_id", player_id_},
            {"round", round_},
            {"stages", stage_trace_}
        };

        auto canonical = snapshot;
        canonical.erase("sequence");
        canonical.erase("player_sequence");
        if (canonical.contains("context_bridge") &&
            canonical["context_bridge"].contains("metadata")) {
            canonical["context_bridge"]["metadata"].erase("timestamp_unix_ms");
            canonical["context_bridge"]["metadata"].erase("sequence");
        }
        const auto fingerprint = canonical.dump();
        if (fingerprint == last_snapshot_fingerprint_) return false;

        last_snapshot_fingerprint_ = fingerprint;
        ++player_sequence_;
        snapshots.push_back(std::move(snapshot));
        return true;
    }

    void reset() {
        active.reset();
        transitions = TransitionManager{};
        recorder = CompositionDiagnosticRecorder{};
        snapshots.clear();
        match_id_ = 0;
        player_id_ = -1;
        round_ = 0;
        player_sequence_ = 0;
        next_stage_sequence_ = 0;
        last_snapshot_fingerprint_.clear();
        stage_trace_.clear();
    }

private:
    std::uint64_t match_id_{0};
    std::int32_t player_id_{-1};
    std::uint32_t round_{0};
    std::uint64_t player_sequence_{0};
    std::uint64_t next_stage_sequence_{0};
    std::string last_snapshot_fingerprint_;
    std::vector<nlohmann::json> stage_trace_;
};

} // namespace tft::composition_intelligence
