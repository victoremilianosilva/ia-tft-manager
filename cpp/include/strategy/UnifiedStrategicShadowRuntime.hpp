#pragma once

#include "strategy/StrategicDirectionPivotAuditRecorder.hpp"

namespace tft::strategy {

// Session-scoped entry point for callers that own the unified shadow planner.
// The recorder observes the returned value only; recording failure never
// changes the strategic result or propagates to the game/runtime caller.
class UnifiedStrategicShadowRuntime {
public:
    explicit UnifiedStrategicShadowRuntime(std::filesystem::path audit_path,
                                            PivotConfirmationPolicy policy = {})
        : machine_(policy), recorder_(std::move(audit_path)) {}

    StrategicCycleResult refresh(const StrategicCycleAuditContext& context,
                                 const StrategicCycleInput& input) noexcept {
        StrategicCycleResult result;
        try {
            result = machine_.refresh(input);
        } catch (...) {
            // The strategic shadow cycle is isolated from the caller as well.
            result.phase = StrategicCyclePhase::NoEvidence;
            result.diagnostics.transition_reason = "shadow_cycle_exception_contained";
            result.shadow_only = true;
            return result;
        }
        (void)recorder_.append(context, input, result);
        return result;
    }

    void reset_machine() noexcept {
        machine_ = UnifiedStrategicStateMachine{};
    }

    void reset_session() noexcept {
        recorder_.reset_session();
        reset_machine();
    }

    const UnifiedStrategicStateMachine& machine() const noexcept { return machine_; }

private:
    UnifiedStrategicStateMachine machine_;
    StrategicDirectionPivotAuditRecorder recorder_;
};

} // namespace tft::strategy
