#pragma once

#include "composition_intelligence/CompositionEvaluation.hpp"
#include "composition_intelligence/PlannerEvidenceAdapters.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <optional>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace tft::composition_intelligence {

enum class UnitIntent { Keep, Seek, Upgrade, Replace, Hold, SellCandidate };
enum class UnitPriorityTier { Carry, TraitCompletion, Core, Composition, Bridge, TemporarySupport, OutsideTarget };
enum class UnitStrategicRelation { ActiveCore, ActiveFlex, SharedCore, SharedFlex, Bridge, OutsideTarget, MissingTarget };
enum class UnitReasonCode {
    RequiredByActiveComposition, CorePriority, BoardContribution, SynergyContribution,
    UpgradeProgress, TargetUnitMissing, BridgeDuringTransition, EquippedItemRisk,
    NotInActiveTarget, InsufficientEvidence, InvestmentIsNotStrategicValue,
    CompositionSnapshotStale, NoActiveComposition, TraitCompletionPriority,
    TemporarySupportJustification
};

struct UnitPriorityReason {
    UnitReasonCode code{UnitReasonCode::InsufficientEvidence};
    std::string message;
};

struct UnitPriorityEvidence {
    std::int32_t champion_id{-1};
    double board_contribution{0.5}; // normalized [0,1], supplied by caller
    double synergy_contribution{0.5}; // normalized [0,1], supplied by caller
    double confidence{0.5}; // evidence confidence, not a calibrated probability
    std::int32_t copies_toward_next_star{0};
    std::int32_t copies_in_shop{0};
    bool trait_completion{false};
};

struct UnitPriorityOwnedUnit {
    std::int32_t champion_id{-1};
    std::int32_t copies{0};
    std::int32_t highest_star{1};
    bool on_board{false};
    std::vector<std::string> equipped_item_ids;
};

struct UnitPriorityTemporarySupport {
    std::int32_t champion_id{-1};
    std::string reason;
    double confidence{0.0};
};

struct UnitPriorityContext {
    std::string composition_id;
    std::uint64_t composition_version{0};
    std::optional<CompositionTransitionPlan> transition;
    std::vector<UnitPriorityOwnedUnit> owned_units; // board + bench, aggregated per champion
    std::vector<UnitPriorityEvidence> evidence;
    std::vector<UnitPriorityTemporarySupport> temporary_support;
    const PlannerEvidenceSnapshot* planner_evidence{nullptr};
    std::uint64_t match_id{0};
    std::int32_t player_id{-1};
    std::uint32_t round{0};
};

struct UnitPriorityConfig {
    double minimum_evidence_confidence{0.25};
    double keep_contribution_threshold{0.35};
    double upgrade_contribution_threshold{0.25};
    std::int32_t copies_to_next_star_threshold{2};
};

struct UnitPriority {
    std::int32_t champion_id{-1};
    UnitIntent intent{UnitIntent::Hold};
    UnitPriorityTier tier{UnitPriorityTier::OutsideTarget};
    UnitStrategicRelation relation{UnitStrategicRelation::OutsideTarget};
    std::int32_t copies_owned{0};
    std::int32_t highest_star{1};
    std::int32_t target_star{0}; // 0 means no upgrade target
    bool on_board{false};
    bool sale_restricted{false};
    std::int32_t priority{0}; // larger means more strategically urgent
    double confidence{0.0}; // explicitly not a probability
    double board_contribution{0.0};
    double synergy_contribution{0.0};
    std::vector<UnitPriorityReason> reasons;
};

struct UnitPrioritySnapshot {
    std::string composition_id;
    std::uint64_t composition_version{0};
    std::vector<UnitPriority> units; // owned units plus missing target units
    bool stale{false};
    std::string stale_reason;
    std::vector<std::string> evidence_consumed;
    std::vector<std::string> evidence_rejected;
};

class UnitPriorityPlanner {
public:
    explicit UnitPriorityPlanner(UnitPriorityConfig config = {}) : config_(config) {}

    UnitPrioritySnapshot resolve(
        const std::optional<ActiveComposition>& active,
        const UnitPriorityContext& context) const {
        UnitPrioritySnapshot out;
        if (!active) {
            out.stale = true;
            out.stale_reason = "no active composition";
            return out;
        }
        out.composition_id = active->candidate.composition_id;
        out.composition_version = active->version;
        if (context.composition_id != active->candidate.composition_id ||
            context.composition_version != active->version) {
            out.stale = true;
            out.stale_reason = "context composition identity/version does not match active composition";
            return out;
        }

        const PlannerEvidenceSnapshot* accepted_evidence = nullptr;
        bool board_evidence_valid = false;
        if (context.planner_evidence) {
            const auto& snapshot = *context.planner_evidence;
            if (PlannerEvidenceAdapters::snapshot_identity_matches(snapshot, context.match_id,
                    context.player_id, active->candidate.composition_id, active->version, context.round)) {
                accepted_evidence = &snapshot;
                if (PlannerEvidenceAdapters::source_matches(snapshot.board.metadata, context.match_id,
                        context.player_id, active->candidate.composition_id, active->version, context.round)) {
                    board_evidence_valid = true;
                    out.evidence_consumed.push_back("BoardEvaluation:role_gap_priority_context");
                }
                else out.evidence_rejected.push_back("BoardEvaluation:" + snapshot.board.metadata.reason);
                if (PlannerEvidenceAdapters::source_matches(snapshot.items.metadata, context.match_id,
                        context.player_id, active->candidate.composition_id, active->version, context.round))
                    out.evidence_consumed.push_back("ItemEngine:equipped_item_risk");
                else out.evidence_rejected.push_back("ItemEngine:" + snapshot.items.metadata.reason);
            } else out.evidence_rejected.push_back("PlannerEvidenceSnapshot:identity_mismatch");
        }
        std::unordered_map<std::int32_t, const UnitPriorityOwnedUnit*> owned;
        for (const auto& unit : context.owned_units) {
            if (unit.champion_id < 0 || unit.copies <= 0) continue;
            owned[unit.champion_id] = &unit;
        }
        std::unordered_map<std::int32_t, const UnitPriorityEvidence*> evidence;
        for (const auto& item : context.evidence)
            if (item.champion_id >= 0) evidence[item.champion_id] = &item;

        std::unordered_set<std::int32_t> emitted;
        for (const auto& target : active->candidate.units) {
            const auto found = owned.find(target.champion_id);
            if (found == owned.end()) {
                const auto* ev = find_evidence(evidence, target.champion_id);
                auto item = missing_target(target);
                item.tier = priority_tier(target, ev);
                item.priority = tier_base(item.tier) + std::clamp(target.priority, 0, 49);
                if (ev && ev->copies_in_shop > 0) {
                    item.priority += std::min(15, ev->copies_in_shop * 5);
                    item.reasons.push_back({UnitReasonCode::UpgradeProgress,
                        "Oferta na loja contribui para o progresso de evolução desta unidade da composição.");
                }
                if (ev && ev->trait_completion)
                    item.reasons.push_back({UnitReasonCode::TraitCompletionPriority,
                        "Unidade necessária para completar ou ativar trait relevante da composição.");
                item.confidence = 0.35;
                if (board_evidence_valid) {
                    const auto& board = accepted_evidence->board;
                    if (target.role == UnitRole::Frontline && board.missing_frontline_count > 0)
                        item.priority += 15;
                    if (target.role == UnitRole::MainCarry &&
                        (board.missing_backline_count > 0 || board.exposed_carry_count > 0))
                        item.priority += 15;
                }
                item.reasons.push_back({UnitReasonCode::TargetUnitMissing,
                    target.core ? "Core da composição ativa ainda não possuído; procurar a unidade."
                                : "Slot da composição ativa ainda não possuído; procurar quando viável."});
                out.units.push_back(std::move(item));
                emitted.insert(target.champion_id);
                continue;
            }
            const auto* ev = find_evidence(evidence, target.champion_id);
            auto owned_with_items = *found->second;
            if (accepted_evidence && PlannerEvidenceAdapters::source_matches(
                    accepted_evidence->items.metadata, context.match_id, context.player_id,
                    active->candidate.composition_id, active->version, context.round)) {
                const auto item_unit = std::find_if(accepted_evidence->items.units.begin(),
                    accepted_evidence->items.units.end(), [&](const auto& item) {
                        return item.champion_id == target.champion_id;
                    });
                if (item_unit != accepted_evidence->items.units.end())
                    owned_with_items.equipped_item_ids = item_unit->equipped_item_ids;
            }
            auto resolved = resolve_owned(target, owned_with_items, ev, context);
            if (board_evidence_valid) {
                const auto& board = accepted_evidence->board;
                if (target.role == UnitRole::Frontline && board.missing_frontline_count > 0)
                    resolved.priority += 15;
                if (target.role == UnitRole::MainCarry &&
                    (board.missing_backline_count > 0 || board.exposed_carry_count > 0))
                    resolved.priority += 15;
            }
            out.units.push_back(std::move(resolved));
            emitted.insert(target.champion_id);
        }

        for (const auto& owned_pair : owned) {
            if (emitted.count(owned_pair.first)) continue;
            const auto* ev = find_evidence(evidence, owned_pair.first);
            auto owned_with_items = *owned_pair.second;
            if (accepted_evidence && PlannerEvidenceAdapters::source_matches(accepted_evidence->items.metadata, context.match_id, context.player_id, active->candidate.composition_id, active->version, context.round)) {
                const auto item_unit = std::find_if(accepted_evidence->items.units.begin(), accepted_evidence->items.units.end(), [&](const auto& item) { return item.champion_id == owned_pair.first; });
                if (item_unit != accepted_evidence->items.units.end()) owned_with_items.equipped_item_ids = item_unit->equipped_item_ids;
            }
            out.units.push_back(resolve_outside_target(owned_pair.first, owned_with_items, ev, context));
        }
        std::sort(out.units.begin(), out.units.end(), [](const auto& a, const auto& b) {
            if (a.priority != b.priority) return a.priority > b.priority;
            return a.champion_id < b.champion_id;
        });
        return out;
    }

private:
    static std::int32_t tier_base(UnitPriorityTier tier) {
        switch (tier) {
            case UnitPriorityTier::Carry: return 500;
            case UnitPriorityTier::TraitCompletion: return 400;
            case UnitPriorityTier::Core: return 300;
            case UnitPriorityTier::Composition: return 200;
            case UnitPriorityTier::Bridge: return 150;
            case UnitPriorityTier::TemporarySupport: return 100;
            case UnitPriorityTier::OutsideTarget: return 0;
        }
        return 0;
    }
    static UnitPriorityTier priority_tier(const CompositionUnit& target,
                                          const UnitPriorityEvidence* ev) {
        if (target.role == UnitRole::MainCarry || target.role == UnitRole::SecondaryCarry)
            return UnitPriorityTier::Carry;
        if (ev && ev->trait_completion) return UnitPriorityTier::TraitCompletion;
        if (target.core) return UnitPriorityTier::Core;
        return UnitPriorityTier::Composition;
    }
    static const UnitPriorityTemporarySupport* find_temporary_support(
        const UnitPriorityContext& context, std::int32_t id) {
        const auto it = std::find_if(context.temporary_support.begin(), context.temporary_support.end(),
            [&](const auto& item) { return item.champion_id == id && !item.reason.empty() &&
                std::isfinite(item.confidence) && item.confidence >= 0.25; });
        return it == context.temporary_support.end() ? nullptr : &*it;
    }
    static double clamp01(double v) {
        return std::isfinite(v) ? std::clamp(v, 0.0, 1.0) : 0.0;
    }
    static const UnitPriorityEvidence* find_evidence(
        const std::unordered_map<std::int32_t, const UnitPriorityEvidence*>& map,
        std::int32_t id) {
        const auto it = map.find(id);
        return it == map.end() ? nullptr : it->second;
    }
    static bool contains(const std::vector<std::int32_t>& ids, std::int32_t id) {
        return std::find(ids.begin(), ids.end(), id) != ids.end();
    }
    static UnitStrategicRelation relation(
        const CompositionUnit& unit, const UnitPriorityContext& context) {
        const bool shared = context.transition &&
            contains(context.transition->shared_unit_ids, unit.champion_id);
        if (shared)
            return unit.core ? UnitStrategicRelation::SharedCore : UnitStrategicRelation::SharedFlex;
        return unit.core ? UnitStrategicRelation::ActiveCore : UnitStrategicRelation::ActiveFlex;
    }
    static UnitPriority missing_target(const CompositionUnit& target) {
        UnitPriority out;
        out.champion_id = target.champion_id;
        out.intent = UnitIntent::Seek;
        out.relation = UnitStrategicRelation::MissingTarget;
        out.priority = target.priority;
        out.reasons.push_back({UnitReasonCode::TargetUnitMissing, "Unidade prevista na composição, mas ainda não possuída."});
        return out;
    }
    UnitPriority resolve_owned(
        const CompositionUnit& target, const UnitPriorityOwnedUnit& owned,
        const UnitPriorityEvidence* ev, const UnitPriorityContext& context) const {
        UnitPriority out;
        out.champion_id = target.champion_id;
        out.tier = priority_tier(target, ev);
        out.relation = relation(target, context);
        out.copies_owned = owned.copies;
        out.highest_star = std::clamp(owned.highest_star, 1, 3);
        out.on_board = owned.on_board;
        out.board_contribution = ev ? clamp01(ev->board_contribution) : 0.5;
        out.synergy_contribution = ev ? clamp01(ev->synergy_contribution) : 0.5;
        out.confidence = ev ? clamp01(ev->confidence) : 0.25;
        out.priority = tier_base(out.tier) + std::clamp(target.priority, 0, 49);
        out.reasons.push_back({UnitReasonCode::RequiredByActiveComposition,
            target.core ? "Unidade core da composição ativa." : "Unidade prevista na composição ativa."});
        if (target.core)
            out.reasons.push_back({UnitReasonCode::CorePriority, "A composição marca esta unidade como core."});
        if (ev && out.board_contribution >= config_.keep_contribution_threshold)
            out.reasons.push_back({UnitReasonCode::BoardContribution, "Contribuição observada no board acima do limite configurado."});
        if (ev && out.synergy_contribution >= config_.keep_contribution_threshold)
            out.reasons.push_back({UnitReasonCode::SynergyContribution, "Contribuição observada para sinergias acima do limite configurado."});

        const auto copies_to_upgrade = ev
            ? std::max(0, ev->copies_toward_next_star) + std::max(0, ev->copies_in_shop)
            : 0;
        if (ev && ev->trait_completion)
            out.reasons.push_back({UnitReasonCode::TraitCompletionPriority,
                "Unidade completa ou ativa trait relevante da composição; prioridade acima das demais peças flexíveis."});
        if (out.confidence < config_.minimum_evidence_confidence && !target.core &&
            target.role != UnitRole::MainCarry && target.role != UnitRole::SecondaryCarry &&
            !(ev && ev->trait_completion)) {
            out.intent = UnitIntent::Hold;
            out.priority = std::max(0, target.priority);
            out.reasons.push_back({UnitReasonCode::InsufficientEvidence, "Evidência insuficiente para promover upgrade ou substituição; manter em observação."});
        } else if (out.highest_star < 3 &&
                   copies_to_upgrade >= std::max(1, config_.copies_to_next_star_threshold) &&
                   (out.board_contribution >= config_.upgrade_contribution_threshold || target.core ||
                    target.role == UnitRole::MainCarry || target.role == UnitRole::SecondaryCarry ||
                    (ev && ev->trait_completion))) {
            out.intent = UnitIntent::Upgrade;
            out.target_star = out.highest_star < 2 ? 2 : out.highest_star + 1;
            out.priority += 20;
            out.reasons.push_back({UnitReasonCode::UpgradeProgress, "Há cópias em progresso para o próximo nível de estrelas e contribuição suficiente."});
        } else {
            out.intent = UnitIntent::Keep;
            out.reasons.push_back({UnitReasonCode::InvestmentIsNotStrategicValue,
                "A posse/investimento foi registrado, mas a decisão KEEP decorre do papel na composição ativa, não do custo passado."});
        }
        if (!owned.equipped_item_ids.empty()) {
            out.sale_restricted = true;
            out.reasons.push_back({UnitReasonCode::EquippedItemRisk, "Unidade possui itens equipados; qualquer substituição/venda exige avaliação explícita do risco dos itens."});
        }
        (void)context;
        return out;
    }

    UnitPriority resolve_outside_target(
        std::int32_t id, const UnitPriorityOwnedUnit& owned,
        const UnitPriorityEvidence* ev, const UnitPriorityContext& context) const {
        UnitPriority out;
        out.champion_id = id;
        out.copies_owned = owned.copies;
        out.highest_star = std::clamp(owned.highest_star, 1, 3);
        out.on_board = owned.on_board;
        out.board_contribution = ev ? clamp01(ev->board_contribution) : 0.0;
        out.synergy_contribution = ev ? clamp01(ev->synergy_contribution) : 0.0;
        out.confidence = ev ? clamp01(ev->confidence) : 0.2;
        out.priority = 0;
        const auto* transition = context.transition ? &*context.transition : nullptr;
        out.tier = UnitPriorityTier::OutsideTarget;
        if (transition && contains(transition->bridge_unit_ids, id)) {
            out.tier = UnitPriorityTier::Bridge;
            out.intent = UnitIntent::Hold;
            out.relation = UnitStrategicRelation::Bridge;
            out.priority = tier_base(out.tier);
            out.reasons.push_back({UnitReasonCode::BridgeDuringTransition, "Unidade fora do alvo final, mas identificada como ponte na transição ativa."});
        } else if (const auto* temporary = find_temporary_support(context, id)) {
            out.intent = UnitIntent::Hold;
            out.relation = UnitStrategicRelation::OutsideTarget;
            out.tier = UnitPriorityTier::TemporarySupport;
            out.priority = tier_base(out.tier);
            out.confidence = clamp01(temporary->confidence);
            out.reasons.push_back({UnitReasonCode::TemporarySupportJustification,
                "Retenção temporária explicitamente justificada: " + temporary->reason});
        } else if (ev && out.confidence >= config_.minimum_evidence_confidence &&
                   out.board_contribution >= config_.keep_contribution_threshold) {
            out.intent = UnitIntent::Hold;
            out.relation = UnitStrategicRelation::OutsideTarget;
            out.priority = 20;
            out.reasons.push_back({UnitReasonCode::BoardContribution, "Contribuição atual no board justifica retenção temporária apesar de não pertencer ao alvo."});
        } else if (!owned.equipped_item_ids.empty() ||
                   (transition && contains(transition->item_risk_unit_ids, id))) {
            out.intent = UnitIntent::Hold;
            out.relation = UnitStrategicRelation::OutsideTarget;
            out.sale_restricted = true;
            out.priority = 10;
            out.reasons.push_back({UnitReasonCode::EquippedItemRisk, "Risco de itens impede recomendar venda sem avaliação adicional."});
        } else if (owned.copies >= 2 || out.highest_star > 1) {
            out.intent = UnitIntent::Hold;
            out.relation = UnitStrategicRelation::OutsideTarget;
            out.sale_restricted = true;
            out.priority = 15;
            out.reasons.push_back({UnitReasonCode::UpgradeProgress,
                "Unidade possui par ou nível de estrelas concluído; preservar até avaliar explicitamente o custo de quebrar esse progresso."});
        } else if (transition && contains(transition->sell_candidate_unit_ids, id)) {
            if (!ev || out.confidence < config_.minimum_evidence_confidence) {
                out.intent = UnitIntent::Hold;
                out.relation = UnitStrategicRelation::OutsideTarget;
                out.priority = 10;
                out.reasons.push_back({UnitReasonCode::InsufficientEvidence,
                    "Evidência insuficiente para confirmar que a unidade fora do alvo é dispensável; não recomendar venda."});
            } else {
                out.intent = UnitIntent::SellCandidate;
                out.relation = UnitStrategicRelation::OutsideTarget;
                out.priority = 5;
                out.reasons.push_back({UnitReasonCode::NotInActiveTarget, "Transição classificou a unidade como candidata à venda; nenhuma ação é executada."});
            }
        } else {
            out.intent = UnitIntent::Replace;
            out.relation = UnitStrategicRelation::OutsideTarget;
            out.priority = 0;
            out.reasons.push_back({UnitReasonCode::NotInActiveTarget, "Unidade não pertence à composição ativa e não foi identificada como bridge."});
        }
        if (owned.copies > 0)
            out.reasons.push_back({UnitReasonCode::InvestmentIsNotStrategicValue, "Cópias e investimento passado não são, isoladamente, motivo para KEEP."});
        return out;
    }

    UnitPriorityConfig config_;
};

} // namespace tft::composition_intelligence
