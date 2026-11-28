#pragma once
#include "lobby/NativeDecisionContext.hpp"
#include <array>
#include <cstdint>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>
namespace tft {
enum class SpatialRelationKind : std::uint8_t { RectangularNeighbor = 1, FrontlineSupportsBackline = 2 };
struct NativeSpatialRelation { std::uint8_t source_slot{0}, target_slot{0}; SpatialRelationKind kind{SpatialRelationKind::RectangularNeighbor}; };
class NativeSpatialContext final {
public:
 explicit NativeSpatialContext(std::shared_ptr<const AuditSnapshot> snapshot, std::size_t player_index)
  : snapshot_(std::move(snapshot)), player_index_(player_index) {
  if (!snapshot_) throw std::invalid_argument("NativeSpatialContext requires an owned snapshot");
  if (player_index_ >= kPlayersPerLobby) throw std::out_of_range("spatial player index out of range");
  build();
 }
 static constexpr const char* kContractId="tft.native-spatial-context";
 static constexpr std::uint32_t kContractVersion=1;
 static constexpr const char* kGeometryId="tft.board-grid.rectangular-4x7";
 const std::string& geometry_id() const noexcept{return geometry_id_;}
 std::uint32_t geometry_version() const noexcept{return geometry_version_;}
 std::uint32_t rows() const noexcept{return rows_;}
 std::uint32_t columns() const noexcept{return columns_;}
 ContextAvailability availability() const noexcept{return availability_;}
 std::size_t player_index() const noexcept{return player_index_;}
 const std::string& engine_instance_id() const noexcept{return snapshot_->engine_instance_id;}
 std::uint64_t episode_id() const noexcept{return snapshot_->episode_id;}
 std::uint64_t snapshot_sequence() const noexcept{return snapshot_->snapshot_sequence;}
 std::uint64_t player_decision_sequence() const noexcept{return snapshot_->player_decision_sequences[player_index_];}
 const std::array<std::int32_t,kBoardSlots>& row_buffer() const noexcept{return rows_buffer_;}
 const std::array<std::int32_t,kBoardSlots>& column_buffer() const noexcept{return columns_buffer_;}
 const std::array<std::uint8_t,kBoardSlots>& occupancy_buffer() const noexcept{return occupancy_buffer_;}
 const std::array<std::int32_t,kBoardSlots>& catalog_id_buffer() const noexcept{return catalog_id_buffer_;}
 const std::array<std::int32_t,kBoardSlots>& role_buffer() const noexcept{return role_buffer_;}
 const std::array<std::array<float,5>,kBoardSlots>& stats_buffer() const noexcept{return stats_buffer_;}
 const std::array<std::string,kBoardSlots>& uuid_buffer() const noexcept{return uuid_buffer_;}
 const std::array<std::string,kBoardSlots>& champion_id_buffer() const noexcept{return champion_id_buffer_;}
 const std::array<std::vector<std::string>,kBoardSlots>& trait_buffer() const noexcept{return trait_buffer_;}
 const std::vector<NativeSpatialRelation>& relations() const noexcept{return relations_;}
 const AuditPlayerSnapshot& metrics() const noexcept{return snapshot_->players[player_index_];}
private:
 static bool frontline(std::int32_t r) noexcept{return r==0||r==3;}
 static bool backline(std::int32_t r) noexcept{return r==1||r==2;}
 void build(){
  geometry_id_=snapshot_->board_geometry_id; geometry_version_=snapshot_->board_geometry_version;
  rows_=snapshot_->board_rows; columns_=snapshot_->board_columns;
  if(geometry_id_!=kGeometryId||geometry_version_!=1||rows_!=4||columns_!=7){availability_=ContextAvailability::Incompatible;return;}
  const auto& p=snapshot_->players[player_index_];
  for(std::size_t s=0;s<kBoardSlots;++s){
   const auto& u=p.board[s]; rows_buffer_[s]=static_cast<std::int32_t>(s/columns_);
   columns_buffer_[s]=static_cast<std::int32_t>(s%columns_); occupancy_buffer_[s]=u.occupied?1:0;
   catalog_id_buffer_[s]=u.champion_internal_id; role_buffer_[s]=u.occupied?u.role:-1;
   uuid_buffer_[s]=u.uuid; champion_id_buffer_[s]=u.champion_id; trait_buffer_[s]=u.trait_names;
   stats_buffer_[s]={static_cast<float>(u.attack_damage),static_cast<float>(u.attack_speed),
    static_cast<float>(u.max_health),static_cast<float>(u.armor),static_cast<float>(u.magic_resist)};
  }
  // Same bounded rectangular 8-neighbor relation used by BoardEvaluation; not TFT hex adjacency/facing.
  constexpr int dirs[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
  for(std::size_t a=0;a<kBoardSlots;++a){
   if(!occupancy_buffer_[a]||uuid_buffer_[a].empty())continue;
   for(const auto& d:dirs){
    int r=rows_buffer_[a]+d[0],c=columns_buffer_[a]+d[1]; if(r<0||r>=4||c<0||c>=7)continue;
    auto b=static_cast<std::size_t>(r*7+c);
    if(b<=a||!occupancy_buffer_[b]||uuid_buffer_[b].empty())continue;
    relations_.push_back({static_cast<std::uint8_t>(a),static_cast<std::uint8_t>(b),SpatialRelationKind::RectangularNeighbor});
    if(frontline(role_buffer_[a])&&backline(role_buffer_[b])&&rows_buffer_[a]<rows_buffer_[b])
     relations_.push_back({static_cast<std::uint8_t>(a),static_cast<std::uint8_t>(b),SpatialRelationKind::FrontlineSupportsBackline});
    else if(frontline(role_buffer_[b])&&backline(role_buffer_[a])&&rows_buffer_[b]<rows_buffer_[a])
     relations_.push_back({static_cast<std::uint8_t>(b),static_cast<std::uint8_t>(a),SpatialRelationKind::FrontlineSupportsBackline});
   }
  }
  availability_=ContextAvailability::Complete;
 }
 std::shared_ptr<const AuditSnapshot> snapshot_; std::size_t player_index_{0};
 std::string geometry_id_; std::uint32_t geometry_version_{0},rows_{0},columns_{0};
 ContextAvailability availability_{ContextAvailability::Unknown};
 std::array<std::int32_t,kBoardSlots> rows_buffer_{};
 std::array<std::int32_t,kBoardSlots> columns_buffer_{},catalog_id_buffer_{},role_buffer_{};
 std::array<std::uint8_t,kBoardSlots> occupancy_buffer_{};
 std::array<std::array<float,5>,kBoardSlots> stats_buffer_{};
 std::array<std::string,kBoardSlots> uuid_buffer_{},champion_id_buffer_{};
 std::array<std::vector<std::string>,kBoardSlots> trait_buffer_{};
 std::vector<NativeSpatialRelation> relations_;
};
}