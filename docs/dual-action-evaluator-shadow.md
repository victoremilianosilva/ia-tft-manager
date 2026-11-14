# Dual Action Evaluator (Shadow)

## Contract

The current `CompositionActionEvaluator` path from #209 remains the frozen
baseline. Its implementation, candidate filtering, scoring weights, tie
breaking, and output are not modified by this issue.

`ContextualActionEvaluator` is a separate, versioned implementation
(`schema_version=1`). It consumes the same original
`StrategicSharedContext::action_candidates` collection plus the current
Unit Priority snapshot, deployable Lineup Plan, and identity-validated
Economy/Board/Item evidence. It does not call `strategy::ActionEvaluator`
or the baseline evaluator.

Both paths are passed the same context and original candidate list. The
diagnostic records each path independently and includes candidate counts,
recommendations, confidence proxies, and whether the recommendations diverged.
A divergence is diagnostic data, not an error or a target to minimize.

## Contextual scoring and eligibility

- BUY requires a current SEEK/UPGRADE unit that belongs to the active endgame target.
- DEPLOY/MOVE requires membership in the current deployable lineup.
- SELL requires explicit SELL_CANDIDATE intent and is rejected for item risk,
  transition restrictions, active target/lineup membership, or bridge units.
- REROLL requires at least one SEEK/UPGRADE target.
- BUY_XP and HOLD remain candidate types; unavailable or unaffordable candidates
  are never eligible.
- Board gaps add a bounded contextual value only when the BoardEvaluation
  evidence is valid for the exact match/player/round/composition/version.
- Economy opportunity costs are used only when the matching evidence source is
  valid. Item evidence is used only to protect equipped units from sale.

The contextual score uses its own component contract (board value, unit
priority, lineup fit, upgrade value, and economy cost). It does not reuse the
baseline's scoring function or weights. Confidence is a score-derived diagnostic,
not a calibrated probability.

## Isolation and failure behavior

- Both evaluators are read-only and Shadow-only.
- The contextual evaluator never publishes an action to the executor and never
  feeds a recommendation into PPO, training, observations, masks, legal-action
  generation, rewards, checkpoints, or game rules.
- An invalid evidence envelope for another match/player/round/composition
  makes the contextual result stale and unusable. Individual source failures
  are recorded and excluded without inventing zero-valued evidence.
- Contextual exceptions are caught locally. They cannot prevent the frozen
  baseline result from being captured in the diagnostic.
- PPO's action may remain an observational field elsewhere in the audit; it is
  not ground truth and agreement with it is not optimized.

## Diagnostic output

Each Composition Intelligence JSONL record adds
`action_evaluator_comparison` with:
- baseline implementation identifier and selected action;
- contextual schema/version, identity, evidence consumption/rejections,
  per-candidate eligibility and score decomposition;
- candidate-set parity/counts and explicit divergence flag;
- `divergence_is_diagnostic_not_error=true`, `policy_action_is_not_ground_truth=true`,
  `shadow_only=true`, and `executor_connected=false`.


## Current architecture reconciliation (2026-11-14)

The evaluator isolation described above remains normative for **recommendations
and evaluator outputs**: neither baseline nor contextual evaluator output is
fed to PPO as a label, reward target, or replacement action. The statement
about not feeding recommendations into observations must not be broadened to
mean that PPO can never receive canonical strategic context.

A future observation projection may consume approved source-owner state and
validated evidence under #286/#293, but it must not consume evaluator scores,
rankings, confidence proxies, or recommendation outcomes as supervision.
PPO action, baseline recommendation, contextual proposal, and executor
resolution remain distinct records. Divergence is diagnostic, not an error
criterion. Engine rules and masks remain final legality authority.

**Prior limitation:** the original wording grouped recommendations and all
possible strategic context under a single “not fed into observations” phrase.
**Reason for clarification:** context is useful input; evaluator outputs are
not ground truth. Conflating them would either starve PPO of approved context
or introduce imitation coupling.
**Ownership/contract:** evaluators own only their proposal/diagnostic outputs;
the versioned observation adapter is a separate read-only consumer.
**Cross-component impact:** #281/#286/#293/#294/#288 and the ownership
contract; no evaluator scoring or runtime behavior changes here.
**Validation:** documentary consistency now; executable acceptance after
Gate 8 must prove separate provenance and no evaluator-output-to-label/reward
path.
