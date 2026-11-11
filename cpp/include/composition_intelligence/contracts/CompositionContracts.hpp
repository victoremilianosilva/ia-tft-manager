#pragma once

#include <cstddef>
#include <cctype>
#include <cstdint>
#include <string>
#include <unordered_set>
#include <vector>

namespace tft::composition_intelligence {

// Shared, dependency-free Set parsing used by source adapters and the native
// planner snapshot exporter. Keep this in contracts to avoid adapter coupling.
inline std::string composition_set_number(const std::string& value) {
    const auto marker = value.find("TFTSet");
    std::size_t begin = marker == std::string::npos ? std::string::npos : marker + 6;
    if (begin == std::string::npos && value.rfind("DA_", 0) == 0) begin = 3;
    if (begin == std::string::npos) return {};
    auto end = begin;
    while (end < value.size() && std::isdigit(static_cast<unsigned char>(value[end]))) ++end;
    return end > begin ? value.substr(begin, end - begin) : std::string{};
}

inline std::string composition_champion_set(const std::string& api_name,
                                             const std::string& character_name) {
    auto set = composition_set_number(api_name);
    return set.empty() ? composition_set_number(character_name) : set;
}

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
