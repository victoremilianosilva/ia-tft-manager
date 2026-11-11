#pragma once

#include <cstddef>
#include <cstdint>
#include <string>
#include <unordered_set>
#include <vector>

namespace tft::composition_intelligence {

enum class CompositionSource {
    Oppg,
    Native
};

enum class UnitRole {
    MainCarry,
    SecondaryCarry,
    Frontline,
    Support,
    Flex
};

struct CompositionUnit {
    std::int32_t champion_id{-1};
    UnitRole role{UnitRole::Flex};
    bool core{false};
    int priority{0};

    bool operator==(const CompositionUnit&) const = default;
};

struct NativeUnitSelection {
    std::int32_t champion_id{-1};
    bool core{false};
    int priority{0};
};

struct NativeCompositionSnapshot {
    std::string composition_id;
    std::string set_id;
    std::string patch;
    std::vector<NativeUnitSelection> units;
    std::int32_t main_carry_id{-1};
    std::size_t target_board_size{0};
    double source_score{0.0};
    std::string source_reference{"native-generator"};
};

struct CompositionCandidate {
    std::string composition_id;
    CompositionSource source{CompositionSource::Native};
    std::string set_id;
    std::string patch;
    std::vector<CompositionUnit> units;
    std::int32_t main_carry_id{-1};
    std::size_t target_board_size{0};
    double source_score{0.0};
    std::string source_reference;
};

struct ActiveComposition {
    CompositionCandidate candidate;
    std::uint64_t version{0};
};

enum class CompositionTransitionReason {
    InitialSelection,
    SourceReplacement,
    StrategicPivot,
    Refinement
};

struct CompositionTransition {
    std::uint64_t previous_version{0};
    std::uint64_t new_version{0};
    std::string previous_composition_id;
    std::string new_composition_id;
    CompositionTransitionReason reason{CompositionTransitionReason::InitialSelection};
    std::vector<std::int32_t> shared_unit_ids;
    std::vector<std::int32_t> added_unit_ids;
    std::vector<std::int32_t> removed_unit_ids;
};

enum class PublishStatus {
    Published,
    Unchanged,
    RejectedInvalidCandidate
};

struct PublishResult {
    PublishStatus status{PublishStatus::RejectedInvalidCandidate};
    std::string validation_error;
    ActiveComposition active;
    bool has_transition{false};
    CompositionTransition transition;
};

} // namespace tft::composition_intelligence
