#pragma once
#include <algorithm>
#include <cmath>
#include <limits>
#include <utility>
#include <vector>
namespace tft {
class PositioningEngine {
public:
 static constexpr int rows=4, cols=7, size=28, tank=0, carry=1, support=2, fighter=3, assassin=4;
 static bool is_valid_position(int p) noexcept { return p>=0&&p<size; }
 static std::pair<int,int> position_to_row_col(int p) noexcept { return is_valid_position(p)?std::pair<int,int>{p/cols,p%cols}:std::pair<int,int>{-1,-1}; }
 static int row_col_to_position(int r,int c) noexcept { return r>=0&&r<rows&&c>=0&&c<cols?r*cols+c:-1; }
 static std::vector<int> get_neighbors(int p,bool diagonal=true) {
  std::vector<int> out; auto [r,c]=position_to_row_col(p); if(r<0)return out;
  const int dirs8[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
  const int dirs4[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
  if(diagonal){for(auto& d:dirs8){int n=row_col_to_position(r+d[0],c+d[1]);if(n>=0)out.push_back(n);}}
  else {for(auto& d:dirs4){int n=row_col_to_position(r+d[0],c+d[1]);if(n>=0)out.push_back(n);}}
  return out;
 }
 static double evaluate_unit_placement(const std::vector<int>& b,int p,int candidate=-2) {
  if(!is_valid_position(p))return -999.0; int role=candidate==-2?role_at(b,p):candidate; if(role<0)return 0.0; if(role>assassin)role=fighter;
  auto [r,c]=position_to_row_col(p); double f=(3-r)/3.0, back=r/3.0, center=std::max(0.0,1.0-std::abs(c-3.0)/3.0), edge=std::max(0.0,1.0-std::min(c,6-c)/3.0);
  if(role==tank)return f*4.0+center*1.5;
  if(role==fighter)return f*2.5+center;
  if(role==assassin)return std::max(0.0,1.0-std::abs(r-1.65)/3.0)*3.0+edge;
  if(role==support)return back*3.0+center*1.5;
  return back*4.0+center*2.0+((c==0||c==6)?-0.5:0.0);
 }
 static double evaluate_protection(const std::vector<int>& b,int p) {
  int role=role_at(b,p);if(role<0)return 0.0;int occupied=0,tanks=0;
  for(int n:get_neighbors(p,true)){int nr=role_at(b,n);if(nr<0)continue;++occupied;if(nr==tank)++tanks;}
  if(role==carry)return occupied*0.8+tanks*1.5;
  if(role==support)return occupied*0.6+tanks;
  if(role==tank)return occupied*0.2;
  return 0.0;
 }
 static double evaluate_board_positioning(const std::vector<int>& b) {
  double score=0;for(int p=0;p<std::min((int)b.size(),size);++p)if(role_at(b,p)>=0)score+=evaluate_unit_placement(b,p)+evaluate_protection(b,p);return score;
 }
 static std::pair<int,double> find_best_position(const std::vector<int>& b,int role,const std::vector<int>& candidates={}) {
  std::vector<int> c=candidates;if(c.empty())for(int p=0;p<size;++p)if(role_at(b,p)<0)c.push_back(p);
  int best=-1;double best_score=-std::numeric_limits<double>::infinity();
  for(int p:c){if(!is_valid_position(p)||role_at(b,p)>=0)continue;auto sim=normalized(b);sim[p]=norm_role(role);double score=evaluate_unit_placement(sim,p)+evaluate_protection(sim,p);if(score>best_score){best=p;best_score=score;}}
  return {best,best_score};
 }
 static std::pair<int,double> find_best_swap(const std::vector<int>& b,int source,const std::vector<int>& candidates={}) {
  if(!is_valid_position(source)||role_at(b,source)<0)return {-1,-std::numeric_limits<double>::infinity()};
  std::vector<int> c=candidates;if(c.empty())for(int p=0;p<std::min((int)b.size(),size);++p)if(p!=source)c.push_back(p);
  int role=role_at(b,source),best=-1;double current=evaluate_unit_placement(b,source),delta_best=0;
  for(int target:c){if(!is_valid_position(target)||target==source)continue;auto sim=normalized(b);std::swap(sim[source],sim[target]);double score=evaluate_unit_placement(sim,target,role)+evaluate_protection(sim,target);double delta=score-current;if(delta>delta_best){delta_best=delta;best=target;}}
  return {best,delta_best};
 }
 static bool is_board_stable(const std::vector<int>& b,double tolerance=0.01) {
  for(int p=0;p<std::min((int)b.size(),size);++p)if(role_at(b,p)>=0){auto [target,delta]=find_best_swap(b,p);if(target>=0&&delta>tolerance)return false;}return true;
 }
 static double get_normalized_positioning_score(const std::vector<int>& b) {
  int count=0;for(int p=0;p<std::min((int)b.size(),size);++p)if(role_at(b,p)>=0)++count;if(!count)return 0;
  return std::clamp(evaluate_board_positioning(b)/(count*10.0),-1.0,1.0);
 }
private:
 static int norm_role(int r){return r>=0&&r<=assassin?r:fighter;}
 static int role_at(const std::vector<int>& b,int p){if(!is_valid_position(p)||(size_t)p>=b.size()||b[p]<0)return -1;return norm_role(b[p]);}
 static std::vector<int> normalized(const std::vector<int>& b){std::vector<int> out(size,-1);std::copy_n(b.begin(),std::min(b.size(),out.size()),out.begin());return out;}
};
}
