#pragma once

// Versioned, player-scoped context for the new strategic planner.
// This contract intentionally has no dependency on StrategyInfo,
// CompositionDirectionPolicy, or CompositionPlanner.

#include "strategy/StrategicPlanning.hpp"

#include <cstdint>
#include <string>
#include <utility>
#include <vector>

namespace tft::strategy {

enum class StrategicEvidenceQuality : std::uint8_t {
    Complete = 0,
    Partial = 1,
    Missing = 2,
    Stale = 3,
    Incompatible = 4
};

struct StrategicEvidenceProvenance {
    std::string field;
    std::string source;
    std::string reason;
};

struct StrategicEvidenceContext {
    static constexpr std::uint32_t kSchemaVersion = 2;

    std::uint32_t schema_version{kSchemaVersion};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    StrategicEvidenceQuality quality{StrategicEvidenceQuality::Missing};
    std::string quality_reason{"not_built"};
    std::vector<StrategicEvidenceProvenance> provenance;

    // Observed facts and new-architecture inferences are kept distinct.
    std::vector<StrategicUnitCandidate> observed_units;
    std::string proposed_or_confirmed_direction;
    std::vector<std::string> derived_focus_traits;
    std::vector<std::int32_t> derived_core_unit_ids;
    std::string direction_identity;
    std::string direction_source{"none"};

    // This projection is consumed by StrategicPlanner. Its strategic fields
    // are populated exclusively by this builder from new evidence above.
    StrategicSharedContext planner_context;

    bool valid_for(std::uint64_t expected_match_id,
                   std::int32_t expected_player_id,
                   std::uint32_t expected_round) const noexcept {
        return schema_version == kSchemaVersion &&
            quality != StrategicEvidenceQuality::Stale &&
            quality != StrategicEvidenceQuality::Incompatible &&
            match_id == expected_match_id &&
            player_id == expected_player_id &&
            round == expected_round &&
            planner_context.player_id == expected_player_id &&
            planner_context.round == expected_round;
    }
};

struct StrategicEvidenceContextInput {
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
    std::uint64_t sequence{0};
    StrategicSharedContext observed_context;
    std::string direction;
    std::string direction_identity;
    std::string direction_source{"native_strategic_commitment"};
    std::vector<std::string> focus_traits;
    std::vector<std::int32_t> core_unit_ids;
    std::vector<StrategicEvidenceProvenance> provenance;
};

class StrategicEvidenceContextBuilder {
public:
    StrategicEvidenceContext build(StrategicEvidenceContextInput input) const {
        StrategicEvidenceContext out;
        out.match_id = input.match_id;
        out.player_id = input.player_id;
        out.round = input.round;
        out.sequence = input.sequence;
        out.provenance = std::move(input.provenance);
        out.proposed_or_confirmed_direction = std::move(input.direction);
        out.direction_identity = std::move(input.direction_identity);
        out.direction_source = std::move(input.direction_source);
        out.derived_focus_traits = std::move(input.focus_traits);
        out.derived_core_unit_ids = std::move(input.core_unit_ids);

        if (input.player_id < 0 || input.sequence == 0 ||
            input.observed_context.player_id != input.player_id ||
            input.observed_context.round != input.round) {
            out.quality = StrategicEvidenceQuality::Incompatible;
            out.quality_reason = "player_round_or_sequence_metadata_invalid";
            return out;
        }

        out.planner_context = std::move(input.observed_context);
        out.planner_context.schema_version = StrategicEvidenceContext::kSchemaVersion;
        out.planner_context.current_composition_direction =
            out.proposed_or_confirmed_direction;
        out.planner_context.current_composition_focus =
            out.derived_focus_traits.empty() ? std::string{} :
                out.derived_focus_traits.front();
        out.planner_context.current_core_traits = out.derived_focus_traits;
        out.planner_context.composition_locked = false;
        out.observed_units = out.planner_context.owned_units;

        if (out.proposed_or_confirmed_direction.empty()) {
            out.planner_context.current_direction_score = 0.0;
            out.planner_context.current_direction_viable = false;
            out.quality = out.observed_units.empty()
                ? StrategicEvidenceQuality::Missing
                : StrategicEvidenceQuality::Partial;
            out.quality_reason = out.observed_units.empty()
                ? "no_observed_units_or_direction_evidence"
                : "observed_units_available_direction_not_established";
        } else {
            out.quality = StrategicEvidenceQuality::Complete;
            out.quality_reason = "new_evidence_context_built";
            out.provenance.push_back({
                "direction", out.direction_source,
                "derived_from_new_architecture_evidence"
            });
        }
        return out;
    }
};

} // namespace tft::strategy
