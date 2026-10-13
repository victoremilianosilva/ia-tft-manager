
#pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <memory>
#include <optional>
#include <vector>

namespace tft {

inline constexpr std::size_t kPlayersPerLobby = 8;
inline constexpr std::size_t kBoardSlots = 28;
inline constexpr std::size_t kBenchSlots = 9;
inline constexpr std::size_t kShopSlots = 5;
inline constexpr std::size_t kActionComponents = 6;

inline constexpr std::array<std::size_t, 6> kActionDims{
    7, 5, 9, 28, 28, 28
};

struct PlayerAction {
    // type, shop_slot, bench_slot,
    // board_target, board_source, board_move_target
    std::array<std::int32_t, 6> values{6, 0, 0, 0, 0, 0};
};

struct PlayerActionMasks {
    std::array<std::uint8_t, 7> type_mask{};
    std::array<std::uint8_t, 5> shop_mask{};
    std::array<std::uint8_t, 9> bench_source_mask{};
    std::array<std::uint8_t, 28> board_target_mask{};
    std::array<std::uint8_t, 28> board_source_mask{};

    // [origem, destino]
    std::array<std::uint8_t, 28 * 28>
        board_move_target_masks{};

    std::array<std::uint8_t, 9> bench_move_source_mask{};

    // [origem no banco, destino no tabuleiro]
    std::array<std::uint8_t, 9 * 28>
        bench_to_board_target_masks{};
};

struct ResetResult {
    // Shape: (8, observation_dim)
    std::vector<float> observations;
    std::size_t observation_dim{0};

    std::array<PlayerActionMasks, 8> action_masks{};
    std::uint64_t episode_id{0};
};

struct StepResult {
    // Shape: (8, observation_dim)
    std::vector<float> observations;
    std::size_t observation_dim{0};

    std::array<float, 8> rewards{};
    std::array<std::uint8_t, 8> dones{};
    std::array<PlayerActionMasks, 8> action_masks{};

    bool lobby_done{false};
    std::uint32_t round{0};
    std::int32_t alive_players{8};
};

class TFTEngine {
public:
    explicit TFTEngine(std::uint64_t seed = 0);
    ~TFTEngine();

    TFTEngine(const TFTEngine&) = delete;
    TFTEngine& operator=(const TFTEngine&) = delete;

    TFTLobbyEngine(TFTEngine&&) noexcept;
    TFTEngine& operator=(TFTEngine&&) noexcept;

    ResetResult reset(
        std::optional<std::uint64_t> seed = std::nullopt
    );

    StepResult step(
        const std::array<PlayerAction, 8>& actions
    );

    std::array<PlayerActionMasks, 8>
    get_action_masks() const;

    std::size_t observation_dim() const noexcept;
    std::uint64_t episode_id() const noexcept;
    std::uint32_t round() const noexcept;
    bool is_done() const noexcept;

    void close() noexcept;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace tft
